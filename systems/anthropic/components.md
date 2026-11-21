# Anthropic components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.anthropic.com, claude.com and docs.claude.com on 2026-11-09, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Nothing was signed into, submitted, bought or sent; no consent dialog was answered and no form was submitted.

The public surface is three hosts sharing one type system: **www.anthropic.com** (the marketing site: ivory #faf9f5 ground, ink #141413, anthropicSerif headlines, pill nav chrome, a --color-* palette on :root), **claude.com** (the product pages: the same build plus a `--theme-*` semantic set and fluid clamp() type), and **docs.claude.com** (the Claude Platform docs: the cds-* Tailwind system on a cooler gray ramp, anthropicSans/anthropicMono, a #184f95 accent). Only the docs ship a dark theme.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (67 components, 123 states). The page layouts are described in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/18 500, #000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (122 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (the docs dark pass is `{page}-dark-{state}.png`). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| www.anthropic.com home. Serif hero, feature card, news cards; header menus open on click. | `https://www.anthropic.com/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [research menu](screenshots/home-light-nav-research.png) |
| www.anthropic.com/news. The announcements index. | `https://www.anthropic.com/news` | [default](screenshots/news-light-default.png), [full](screenshots/news-light-full.png) |
| www.anthropic.com/research. The research index on dark media. | `https://www.anthropic.com/research` | [default](screenshots/research-light-default.png), [full](screenshots/research-light-full.png) |
| www.anthropic.com/engineering. The engineering index. | `https://www.anthropic.com/engineering` | [default](screenshots/engineering-light-default.png), [full](screenshots/engineering-light-full.png) |
| www.anthropic.com/policy. Policy index. | `https://www.anthropic.com/policy` | [default](screenshots/policy-light-default.png), [full](screenshots/policy-light-full.png) |
| www.anthropic.com/company. About page. | `https://www.anthropic.com/company` | [default](screenshots/company-light-default.png), [full](screenshots/company-light-full.png) |
| www.anthropic.com/careers. Careers page. Explore open roles was not followed. | `https://www.anthropic.com/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| www.anthropic.com/search. Empty search. Nothing typed. | `https://www.anthropic.com/search` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| www.anthropic.com/claude/opus. Model page. Try Claude and Get API access were not followed. | `https://www.anthropic.com/claude/opus` | [default](screenshots/model-light-default.png), [full](screenshots/model-light-full.png) |
| www.anthropic.com/legal. Legal center. | `https://www.anthropic.com/legal` | [default](screenshots/legal-light-default.png), [full](screenshots/legal-light-full.png) |
| www.anthropic.com/constitution. Constitution. | `https://www.anthropic.com/constitution` | [default](screenshots/constitution-light-default.png), [full](screenshots/constitution-light-full.png) |
| www.anthropic.com home at 390: menu button, hero, the ink nav sheet. | `https://www.anthropic.com/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| www.anthropic.com/news at 390. | `https://www.anthropic.com/news` | [default](screenshots/mobile-news-light-default.png), [full](screenshots/mobile-news-light-full.png) |
| www.anthropic.com/research at 390. | `https://www.anthropic.com/research` | [default](screenshots/mobile-research-light-default.png), [full](screenshots/mobile-research-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Header menus | the marketing nav, on click | Research, Policy, Commitments, Company, and Try Claude were opened and closed. Try Claude's links were not followed. | [home-light-nav-research](screenshots/home-light-nav-research.png), [home-light-nav-try](screenshots/home-light-nav-try.png) |
| Phone menu | Open menu at 390 | the dialog was opened. Contact Sales, Download app, and Try Claude links were not followed. | [mobile-home-light-nav-open](screenshots/mobile-home-light-nav-open.png) |
| Mobile nav sheet | www.anthropic.com at 390 | the menu button opened the full-screen ink sheet | [m-nav-sheet](#mobile-nav-sheet) |

## Checklist coverage

The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. 14 of 19 are captured; the rest do not exist on the public marketing surface.

| Component | Entries | States captured |
|---|---|---|
| Button | [Hero CTA](#hero-cta), [Nav CTA button](#nav-cta-button), [Product CTA](#product-cta), [Platform CTA](#platform-cta), [Plan CTA](#plan-cta), [Submit button](#submit-button), [Copy page button](#copy-page-button) | default, hover, focus-visible, pressed |
| Icon button | [Nav search button](#nav-search-button), [Nav menu button (mobile)](#nav-menu-button-mobile), [Search field](#search-field) | default, hover, focus-visible, pressed |
| Link | [Footer link](#footer-link), [News card title link](#news-card-title-link), [Research entry title link](#research-entry-title-link), [Engineering entry title link](#engineering-entry-title-link), [Docs nav link](#docs-nav-link) | default, hover, focus-visible, pressed |
| Text field | [Text field](#text-field), [Text field box](#text-field-box), [Search input](#search-input) | default, focused, filled |
| Text area | [Text area](#text-area) | default, focused |
| Select | [Select field](#select-field) | default |
| Checkbox | not captured: no public form has one; --theme-checkbox-* tokens exist on claude.com | - |
| Radio | [Radio input](#radio-input), [Topic radio row](#topic-radio-row) | default, hover |
| Switch | [Batch toggle](#batch-toggle) | default, hover, focus-visible, pressed |
| Tabs | [Plan tab](#plan-tab), [Plan tab, switched](#plan-tab-switched), [Docs top tab](#docs-top-tab) | default, hover, focus-visible, pressed |
| Menu | [Nav dropdown](#nav-dropdown), [Mobile nav sheet](#mobile-nav-sheet) | default |
| Tooltip | not captured: none appeared on hover or focus | - |
| Dialog | [Search dialog](#search-dialog) | default |
| Toast | not captured: no toast appeared after any action the capture took signed out | - |
| Card | [Feature card](#feature-card), [News card](#news-card), [Research entry](#research-entry), [Engineering entry](#engineering-entry), [Product card](#product-card), [Plan card](#plan-card) | default, hover |
| List row | [FAQ item](#faq-item), [News card](#news-card) | default, hover |
| Table | not captured: pricing lays plans out as cards, not a table | - |
| Avatar | not captured: no avatars on the public surface | - |
| Badge | [HTTP method badge](#http-method-badge) | default |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 13 components were given a real keyboard focus. 11 show a change: `nav-search` (2px solid #154c92 `brand.periwinkle-interactive`, offset 4px), `nav-cta` (2px solid #154c92 `brand.periwinkle-interactive`, offset 4px), `hero-cta` (2px solid #154c92 `brand.periwinkle-interactive`, offset 4px), `product-cta` (2px solid #c46849, offset 4px), `plan-tab` (2px solid #c46849, offset 2px), `plan-cta` (2px solid #c46849, offset 4px), `docs-nav-link` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px), `batch-toggle` (2px solid #c46849, offset 2px), `docs-search-field` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px), `nav-pill` (2px solid #154c92 `brand.periwinkle-interactive`, offset 4px), `nav-trigger` (2px solid #c46849, offset 2px). The other 2 draw nothing new - the marketing pills draw a deliberate 2px #154c92 periwinkle ring offset 4px, the product pages a 2px #c46849 clay-dark ring offset 2-4px, the docs outline in #2a78d6, and text links take the browser's ring: `footer-link`, `submit-button`. Focus could not be captured on 2 more (keyboard focus never landed on them, so their readings are left out): `api-cta`, `docs-tab`.

**Pressed.** Pressed was forced with DevTools, so it is the :active styles only: the nav pills swap to their #e8e6dc pressed fill under :active, while the ink CTAs and docs controls keep their resting paint. The submit button and every sign-in link were never pressed for real.

**Motion.** Transitions measured on the components, by duration. The everyday hover rides 0.2s ease-out on colour and fill; the pills press in 0.15s; menus and overlays take 0.25-0.5s on the site's quart/expo curves.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.06s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | docs-copy-page, docs-lang, docs-search-field |
| 0.1s | `ease-in-out` | color | plan-cta, plan-tab, plan-tab-active, product-cta |
| 0.12s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | scale | docs-search-dialog |
| 0.15s | `ease` | opacity | m-nav-sheet |
| 0.15s | `ease-in-out` | background-color, border-color, box-shadow, color | nav-cta |
| 0.2s | `ease` | background-color, border-color, box-shadow | topic-radio |
| 0.2s | `ease-in-out` | background-color, border-color, box-shadow, color | hero-cta, m-nav-menu-btn, nav-pill, nav-search, plan-cta, plan-tab, plan-tab-active, product-cta |
| 0.3s | `ease` | background-color, border-color, box-shadow, color, transform | engineering-card-title, hero-title, m-hero-title, m-nav-bar, select-field, text-area, text-field, text-field-box |
| 0.4s | `cubic-bezier(0.35, 1.5, 0.6, 1)` | background-color, border-color | batch-toggle |
| 0.5s | `cubic-bezier(0.19, 1, 0.22, 1)` | color | nav-trigger |
| 0.75s | `cubic-bezier(0.25, 1, 0.5, 1)` | opacity, transform | api-title, contact-title |

**Layout.** Read on each page ([raw/layout.json](raw/layout.json)).

| Page | Frame | Content column | Grids | Fixed |
|---|---|---|---|---|
| home | - | max-width 604.976px | 5 grids (3 col gap 16px; 15 col gap 16px) | News (sticky) |
| news | - | max-width 1920px | 8 grids (3 col gap 16px; 12 col gap 16px) | News (sticky) |
| research | - | max-width 655.39px | 8 grids (3 col gap 16px; 12 col gap 16px) | News (sticky), News (sticky) |
| engineering | - | max-width 1920px | 6 grids (3 col gap 16px; 12 col gap 16px) | News (sticky) |
| product | - | max-width 704px | 5 grids (3 col gap 32px; 3 col gap 2.22222%) | div.transition-overlay (fixed), Latest news (fixed), Product (fixed) |
| platform-api | - | max-width 1440px | 8 grids (12 col gap 32px; 4 col gap 32px) | div.transition-overlay (fixed), Product (fixed) |
| pricing | - | max-width 1440px | 7 grids (4 col gap 24px; 3 col gap 24px) | div.transition-overlay (fixed), Product (fixed) |
| contact-sales | - | max-width 1440px | 5 grids (12 col gap 32px; 2 col gap 32px) | div.transition-overlay (fixed), Product (fixed) |
| docs-home | - | max-width 1152px | 8 grids (2 col gap 28px; 3 col gap 12px) | canvas.pointer-events-none (fixed), Claude Platform Docs (fixed), Ask Docs (fixed) |
| docs-start | - | max-width 1536px | 2 grids (2 col gap 16px; 4 col gap 32px) | canvas.pointer-events-none (fixed), Claude Platform Docs (fixed),  (fixed) |
| docs-api | - | max-width 1536px | 1 grids (4 col gap 32px) | canvas.pointer-events-none (fixed), Claude Platform Docs (fixed),  (fixed) |
| mobile-home | - | max-width 579.829px | 3 grids (2 col gap 16px; 10 col gap 16px) | Try Claude (sticky), div (fixed), Menu (fixed) |

**Card shapes.** Default-state values; the entries hold the states. The signature card is the 24px-radius white plan card on ivory; media cards run 19px on gray-150 and the docs dialog is a 12px white panel with an ink ring.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 1440 x 810 | - | - | #f5f4ed `gray.100` | none | 224px 0px |
| [News card](#news-card) | 632 x 104.17 | - | - | transparent | none | 0 |
| [Product card](#product-card) | 480 x 270 | 1px solid #e8e6dc `gray.200` | 19px | #f0eee6 `gray.150` | none | 0 |
| [Plan card](#plan-card) | 420 x 375.2 | 1px solid #f0eee6 `gray.150` | 24px | #ffffff `gray.000` | none | 40px 32px 48px 32px |
| [Search dialog](#search-dialog) | 672 x 500 | - | 12px | #ffffff `gray.000` | rgba(11, 11, 11, 0.1) 0px 0px 0px 0px inset, rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(11, 11, 11, 0.08) 0px 4px 8px 0px, rgba(11, 11, 11, 0.08) 0px 12px 28px -2px | 0 |
| [Mobile nav sheet](#mobile-nav-sheet) | 390 x 844 | - | - | #141413 `gray.950` | none | 0 |

## Components

### Shell and navigation

The chrome shared by the marketing and product pages: an 84px bar of ivory pills (a wordmark, section links, a Search pill and the Try Claude CTA) over the ivory ground, and the ink footer whose prompt bar takes a clay Send. On a phone the pills collapse to a menu button and a full-screen ink sheet.

#### Top navigation bar
The fixed header on every marketing and product page: the Anthropic wordmark, section triggers, Search and the Try Claude pill. Read as `nav-bar` on the claude.com/product/overview page.

**Values (default).** size 593.09 x 88; padding 24px 0px; background transparent; text anthropicSans 15/24 400, #30302e `gray.750`; icon 16 x 16, #5e5d59 `gray.600`.

Child layers that carry the look: div 200x453 background #ffffff `gray.000` radius 12px shadow rgba(0, 0, 0, 0.1) 0px 4px 16px 0px; div 0x368 background #e8e6dc `gray.200`; div 0x368 background #e8e6dc `gray.200`.

![Top navigation bar default](components/crops/nav-bar-default.png)

#### Nav search button
The square search icon button in the header. Read as `nav-search` on the www.anthropic.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; padding 8px; border 1px solid #e8e6dc `gray.200`; radius 8px; background #f5f4ed `gray.100`; text anthropicSans 13/20.02 400, #3d3d3a `gray.700`; transition border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, background-color 0.2s ease-in-out, color 0.2s ease-in-out; icon 20 x 20, #3d3d3a `gray.700` |
| hover | background #e8e6dc `gray.200`; shadow #e8e6dc 0px 0px 0px 1px; text anthropicSans 13/20.02 400, #141413 `gray.950`; icon 20 x 20, #141413 `gray.950` |
| focus-visible | outline 2px solid #154c92 `brand.periwinkle-interactive`, offset 4px; text anthropicSans 13/20.02 400, #141413 `gray.950`; icon 20 x 20, #141413 `gray.950` |
| pressed | background #e8e6dc `gray.200`; shadow #e8e6dc 0px 0px 0px 1px; text anthropicSans 13/20.02 400, #141413 `gray.950`; icon 20 x 20, #141413 `gray.950` |

![Nav search button default](components/crops/nav-search-default.png) ![Nav search button hover](components/crops/nav-search-hover.png) ![Nav search button focus-visible](components/crops/nav-search-focus-visible.png) ![Nav search button pressed](components/crops/nav-search-pressed.png)

#### Nav CTA button
The header's primary action pill ("Try Claude" on the marketing site, "Explore here" on claude.com). Measured and focused, never followed. Read as `nav-cta` on the www.anthropic.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 116.73 x 28; padding 8px 12px 8px 16px; border 1px solid #e8e6dc `gray.200`; radius 999999px; background #f5f4ed `gray.100`; text anthropicSans 13/20.02 400, #3d3d3a `gray.700`; transition border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, background-color 0.15s ease-in-out, color 0.15s ease-in-out; icon 16 x 16, #3d3d3a `gray.700` |
| hover | border 1px solid #141413 `gray.950`; background #141413 `gray.950`; shadow #141413 0px 0px 0px 1px; text anthropicSans 13/20.02 400, #faf9f5 `gray.050`; icon 16 x 16, #faf9f5 `gray.050` |
| focus-visible | outline 2px solid #154c92 `brand.periwinkle-interactive`, offset 4px; text anthropicSans 13/20.02 400, #141413 `gray.950`; icon 16 x 16, #141413 `gray.950` |
| pressed | background #e8e6dc `gray.200`; shadow #e8e6dc 0px 0px 0px 1px; text anthropicSans 13/20.02 400, #141413 `gray.950`; icon 16 x 16, #141413 `gray.950` |

![Nav CTA button default](components/crops/nav-cta-default.png) ![Nav CTA button hover](components/crops/nav-cta-hover.png) ![Nav CTA button focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA button pressed](components/crops/nav-cta-pressed.png)

#### Footer
The site footer: link columns, the wordmark, legal row with Privacy choices. Read as `footer` on the claude.com/product/overview page.

**Values (default).** size 1440 x 1226.78; padding 95.9999px 0px; border T: 1px solid #30302e `gray.750`; background #141413 `gray.950`; text anthropicSans 11/16.5 400, #87867f `gray.500`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A link in the footer columns. Privacy choices opens a settings dialog and is never pressed. Read as `footer-link` on the claude.com/product/overview page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 189.34 x 27.19; background transparent; text anthropicSans 12/19.2 400, #faf9f5 `gray.050` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Nav pill link
A section pill in the header (News, Research, Policy, Commitments, Company). Measured, never followed. Read as `nav-pill` on the www.anthropic.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69.2 x 28; padding 8px 16px; border 1px solid #e8e6dc `gray.200`; radius 999999px; background #f5f4ed `gray.100`; text anthropicSans 13/20.02 400, #3d3d3a `gray.700`; transition border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, background-color 0.2s ease-in-out, color 0.2s ease-in-out |
| hover | background #e8e6dc `gray.200`; shadow #e8e6dc 0px 0px 0px 1px; text anthropicSans 13/20.02 400, #141413 `gray.950` |
| focus-visible | outline 2px solid #154c92 `brand.periwinkle-interactive`, offset 4px; text anthropicSans 13/20.02 400, #141413 `gray.950` |
| pressed | background #e8e6dc `gray.200`; shadow #e8e6dc 0px 0px 0px 1px; text anthropicSans 13/20.02 400, #141413 `gray.950` |

![Nav pill link default](components/crops/nav-pill-default.png) ![Nav pill link hover](components/crops/nav-pill-hover.png) ![Nav pill link focus-visible](components/crops/nav-pill-focus-visible.png) ![Nav pill link pressed](components/crops/nav-pill-pressed.png)

#### Nav dropdown trigger
A section trigger in the header; opens the section dropdown on hover. Measured, never followed. Read as `nav-trigger` on the claude.com/product/overview page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96.67 x 40; padding 8px 8px 8px 12px; background transparent; text anthropicSans 15/24 400, #30302e `gray.750`; transition color 0.5s cubic-bezier(0.19, 1, 0.22, 1); icon 16 x 16, #5e5d59 `gray.600` |
| hover | text anthropicSans 15/24 400, #141413 `gray.950`; icon 16.68 x 16.68, #141413 `gray.950` |
| focus-visible | outline 2px solid #c46849, offset 2px; icon 16.37 x 16.37, #5e5d59 `gray.600` |
| pressed | text anthropicSans 15/24 400, #141413 `gray.950`; icon 16 x 16, #141413 `gray.950` |

![Nav dropdown trigger default](components/crops/nav-trigger-default.png) ![Nav dropdown trigger hover](components/crops/nav-trigger-hover.png) ![Nav dropdown trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav dropdown
The dropdown under a header section (Product: Claude, Claude Code, Claude in Chrome, …). Shown in its hover-open state. Read as `nav-dropdown` on the claude.com/product/overview page.

Not on the page when it was captured.

### Home

www.anthropic.com's home: the serif hero ('AI research and products that put safety at the frontier.') with an ink CTA, the big #f5f4ed feature card, and the news card list.

#### Hero title
The home h1, a large serif display line ("AI research and products that put safety at the frontier."). Read as `hero-title` on the www.anthropic.com home page.

**Values (default).** size 1280 x 152.95; background transparent; text anthropicSans 40.78/50.98 600, #141413 `gray.950`; transition color 0.3s ease.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
The primary pill under the hero title. Read as `hero-cta` on the www.anthropic.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138.94 x 36; padding 12px 24px; border 1px solid #141413 `gray.950`; radius 10px; background #141413 `gray.950`; text anthropicSans 16.68/25.53 400, #faf9f5 `gray.050`; transition border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, background-color 0.2s ease-in-out, color 0.2s ease-in-out |
| hover | shadow #141413 0px 0px 0px 1px |
| focus-visible | outline 2px solid #154c92 `brand.periwinkle-interactive`, offset 4px |
| pressed | shadow #141413 0px 0px 0px 1px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

### Cards and indexes

The card grids on the index pages: news and engineering cards on ivory, and the research cards that sit on ink-tinted media.

#### News page title
Read as `news-card-title` on the www.anthropic.com/news page.

**Values (default).** size 1 x 1; background transparent; text anthropicSans 16.68/25.53 400, #141413 `gray.950`.

![News page title default](components/crops/news-card-title-default.png)

#### News card
News card: a linked post card in the news index. Read as `news-card` on the www.anthropic.com/news page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 632 x 104.17; background transparent; text anthropicSans 32.54/37.10 700, #141413 `gray.950` |
| hover | text anthropicSans 32.54/37.10 700, #87867f `gray.500` |

![News card default](components/crops/news-card-default.png) ![News card hover](components/crops/news-card-hover.png)

#### Research page title
Read as `research-card-title` on the www.anthropic.com/research page.

**Values (default).** size 1280 x 94.88; background transparent; text anthropicSans 42.35/47.43 600, #141413 `gray.950`.

![Research page title default](components/crops/research-card-title-default.png)

#### Engineering page title
Read as `engineering-card-title` on the www.anthropic.com/engineering page.

**Values (default).** size 1280 x 203.94; background transparent; text anthropicSans 40.78/50.98 600, #141413 `gray.950`; transition color 0.3s ease.

Child layers that carry the look: span 40.8x40.8 background #141413 `gray.950` radius 7.74902px; span 27.3x27.3 background #141413 `gray.950`.

![Engineering page title default](components/crops/engineering-card-title-default.png)

#### Engineering entry
Engineering entry: a linked post in the engineering index. Read as `engineering-card` on the www.anthropic.com/engineering page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 848 x 477; background transparent; text anthropicSans 16.68/25.53 400, #141413 `gray.950` |

![Engineering entry default](components/crops/engineering-card-default.png) ![Engineering entry hover](components/crops/engineering-card-hover.png)

#### Feature card
A large card or slide on the home page (the report/announcement feature). Read as `feature-card` on the www.anthropic.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1440 x 810; padding 224px 0px; background #f5f4ed `gray.100`; text anthropicSans 51.90/56.05 600, #141413 `gray.950`; icon 20 x 20, #3d3d3a `gray.700` |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

#### News card title link
The caption/title link of an index entry. Read as `news-card-link` on the www.anthropic.com/news page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 26.72; background transparent; text anthropicSans 21.37/26.71 700, #141413 `gray.950` |
| hover | text anthropicSans 21.37/26.71 700, #87867f `gray.500` |

![News card title link default](components/crops/news-card-link-default.png) ![News card title link hover](components/crops/news-card-link-hover.png)

#### Research entry
Research entry: a linked paper/post in the research index. Read as `research-card` on the www.anthropic.com/research page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 928 x 522; background transparent; text anthropicSans 16.68/25.53 400, #faf9f5 `gray.050` |

![Research entry default](components/crops/research-card-default.png) ![Research entry hover](components/crops/research-card-hover.png)

#### Research entry title link
The caption/title link of an index entry. Read as `research-card-link` on the www.anthropic.com/research page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 53.44; background transparent; text anthropicSans 21.37/26.71 700, #faf9f5 `gray.050` |
| hover | text anthropicSans 21.37/26.71 700, #5e5d59 `gray.600` |

![Research entry title link default](components/crops/research-card-link-default.png) ![Research entry title link hover](components/crops/research-card-link-hover.png)

#### Engineering entry title link
The caption/title link of an index entry. Read as `engineering-card-link` on the www.anthropic.com/engineering page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 308 x 53.44; background transparent; text anthropicSans 21.37/26.71 700, #141413 `gray.950` |
| hover | text anthropicSans 21.37/26.71 700, #87867f `gray.500` |

![Engineering entry title link default](components/crops/engineering-card-link-default.png) ![Engineering entry title link hover](components/crops/engineering-card-link-hover.png)

### Product pages

claude.com/product/overview and /platform/api: serif display titles, ink CTAs and the muted media cards (radius 19, gray-150).

#### Product page title
The product page h1 (the Claude product overview). Read as `product-title` on the claude.com/product/overview page.

**Values (default).** size 606.48 x 79.19; background transparent; text anthropicSerif 72/79.2 500, #141413 `gray.950`.

![Product page title default](components/crops/product-title-default.png)

#### Product CTA
A primary button on the product page. Read as `product-cta` on the claude.com/product/overview page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 100.25 x 36; padding 8px 12px; radius 8px; background #141413 `gray.950`; shadow #141413 0px 0px 0px 0px; text anthropicSans 15/15 500, #faf9f5 `gray.050`; transition color 0.1s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| hover | shadow #141413 0px 0px 0px 2px |
| focus-visible | outline 2px solid #c46849, offset 4px |
| pressed | shadow #141413 0px 0px 0px 2px |

![Product CTA default](components/crops/product-cta-default.png) ![Product CTA hover](components/crops/product-cta-hover.png) ![Product CTA focus-visible](components/crops/product-cta-focus-visible.png) ![Product CTA pressed](components/crops/product-cta-pressed.png)

#### Product card
A card on the product overview page. Read as `product-card` on the claude.com/product/overview page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 480 x 270; border 1px solid #e8e6dc `gray.200`; radius 19px; background #f0eee6 `gray.150`; text anthropicSans 20/32 400, #141413 `gray.950`; icon 32 x 32, #faf9f5 `gray.050` |
| hover | icon 33.92 x 33.92, #faf9f5 `gray.050` |

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png)

#### Platform page title
The Claude Platform/API page headline. Read as `api-title` on the claude.com/platform/api page.

**Values (default).** size 752 x 116.47; background transparent; text anthropicSerif 64/70.4 500, #141413 `gray.950`; transition opacity 0.75s cubic-bezier(0.25, 1, 0.5, 1), transform 0.75s cubic-bezier(0.25, 1, 0.5, 1).

![Platform page title default](components/crops/api-title-default.png)

#### Platform CTA
A primary button or link on the platform page. Read as `api-cta` on the claude.com/platform/api page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 238.03 x 20; background transparent; text anthropicSans 12/19.2 400, #5e5d59 `gray.600`; icon 20 x 20, #5e5d59 `gray.600` |

![Platform CTA default](components/crops/api-cta-default.png) ![Platform CTA hover](components/crops/api-cta-hover.png) ![Platform CTA pressed](components/crops/api-cta-pressed.png)

### Pricing

claude.com/pricing: the serif title, the segmented plan tabs (gray-150 track, white selected), white plan cards at radius 24, the batch-processing switch and the FAQ list.

#### Pricing title
The "Pricing" h1 on claude.com/pricing. Read as `pricing-title` on the claude.com/pricing page.

**Values (default).** size 1246.05 x 49.28; background transparent; text anthropicSerif 64/70.4 500, #141413 `gray.950`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan type tabs
The Individual / Developer / Team plan tabs. Read as `plan-tabs` on the claude.com/pricing page.

**Values (default).** size 1312 x 48; background transparent; text anthropicSans 12/19.2 400, #141413 `gray.950`.

Child layers that carry the look: div 375.7x48 background #f0eee6 `gray.150` radius 16px; button 88x40 background #ffffff `gray.000` radius 12px; button 0x0 background #ffffff `gray.000` border 1px solid #f0eee6 `gray.150` radius 12px.

![Plan type tabs default](components/crops/plan-tabs-default.png)

#### Plan tab
One segment of the plan-type tabs. Read as `plan-tab` on the claude.com/pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.33 x 40; padding 8px 16px; radius 12px; background transparent; text anthropicSans 12/19.2 400, #5e5d59 `gray.600`; transition background-color 0.2s ease-in-out, color 0.1s ease-in-out |
| hover | background #faf9f5 `gray.050`; text anthropicSans 12/19.2 400, #141413 `gray.950` |
| focus-visible | outline 2px solid #c46849, offset 2px |
| pressed | background #faf9f5 `gray.050`; text anthropicSans 12/19.2 400, #141413 `gray.950` |

![Plan tab default](components/crops/plan-tab-default.png) ![Plan tab hover](components/crops/plan-tab-hover.png) ![Plan tab focus-visible](components/crops/plan-tab-focus-visible.png) ![Plan tab pressed](components/crops/plan-tab-pressed.png)

#### Plan tab, switched
The same tab strip after a local click: the API segment is the active one, and the API usage table replaces the plan cards. Read as `plan-tab-active` on the claude.com/pricing page.

**Values (default).** size 51.81 x 40; padding 8px 16px; radius 12px; background #ffffff `gray.000`; text anthropicSans 12/19.2 400, #141413 `gray.950`; transition background-color 0.2s ease-in-out, color 0.1s ease-in-out.

![Plan tab, switched default](components/crops/plan-tab-active-default.png)

#### Plan card
A plan card on the pricing grid. Read as `plan-card` on the claude.com/pricing page.

**Values (default).** size 420 x 375.2; padding 40px 32px 48px 32px; border 1px solid #f0eee6 `gray.150`; radius 24px; background #ffffff `gray.000`; text anthropicSerif 32/35.2 500, #141413 `gray.950`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
A button inside a plan card ("Try Claude", "Contact sales"). Measured and focused, never followed. Read as `plan-cta` on the claude.com/pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 108.25 x 36; padding 8px 16px; radius 8px; background #141413 `gray.950`; shadow #141413 0px 0px 0px 0px; text anthropicSans 15/15 500, #faf9f5 `gray.050`; transition color 0.1s ease-in-out, background-color 0.2s ease-in-out, border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out |
| hover | shadow #141413 0px 0px 0px 2px |
| focus-visible | outline 2px solid #c46849, offset 4px |
| pressed | shadow #141413 0px 0px 0px 2px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### FAQ item
An accordion question in the pricing FAQ. Read as `faq-item` on the claude.com/pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 640 x 88; padding 32px 0px; background transparent; text anthropicSerif 19/22.8 500, #141413 `gray.950` |

Child layers that carry the look: span 14x1 background #5e5d59 `gray.600`; span 1x14 background #5e5d59 `gray.600`.

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item hover](components/crops/faq-item-hover.png)

#### Batch processing banner
The "Save 50% with batch processing" toggle banner on the API pricing tab. Read as `batch-banner` on the claude.com/pricing page.

**Values (default).** size 200.8 x 34; background transparent; text anthropicSans 15/24 400, #3d3d3a `gray.700`.

Child layers that carry the look: span 56x34 background #dedcd1 `gray.250` border 1px solid #c2c0b6 `gray.350` radius 30px; span::after 23pxx23px background #ffffff `gray.000` border 1px solid #9c9a92 `gray.450` radius 50% shadow rgba(0, 0, 0, 0.05) 0px 4px 24px 0px.

![Batch processing banner default](components/crops/batch-banner-default.png)

#### Batch toggle
The switch that shows batch-processing prices; a local toggle. Read as `batch-toggle` on the claude.com/pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 56 x 34; padding 4px; border 1px solid #c2c0b6 `gray.350`; radius 30px; background #dedcd1 `gray.250`; text anthropicSans 15/22.5 400, #141413 `gray.950`; transition background-color 0.4s cubic-bezier(0.35, 1.5, 0.6, 1), border-color 0.4s cubic-bezier(0.35, 1.5, 0.6, 1) |
| focus-visible | outline 2px solid #c46849, offset 2px |

![Batch toggle default](components/crops/batch-toggle-default.png) ![Batch toggle hover](components/crops/batch-toggle-hover.png) ![Batch toggle focus-visible](components/crops/batch-toggle-focus-visible.png) ![Batch toggle pressed](components/crops/batch-toggle-pressed.png)

### Contact sales form

claude.com/contact-sales: the 755px sales form - text fields, a text area, a select and a radio row measured in default, focused and filled states. Nothing was submitted.

#### Contact page title
The heading over the contact-sales form. Read as `contact-title` on the claude.com/contact-sales page.

**Values (default).** size 448.03 x 79.19; background transparent; text anthropicSerif 72/79.2 500, #141413 `gray.950`; transition opacity 0.75s cubic-bezier(0.25, 1, 0.5, 1), transform 0.75s cubic-bezier(0.25, 1, 0.5, 1).

![Contact page title default](components/crops/contact-title-default.png)

#### Contact form
The HubSpot contact-sales form: a "What can we help you with?" radio topic group first, then dependent fields. Photographed and focused, never submitted. Read as `contact-form` on the claude.com/contact-sales page.

**Values (default).** size 755.38 x 303.48; background transparent; text anthropicSans 15/19.5 500, #141413 `gray.950`.

Child layers that carry the look: div::after 16pxx16px background #5e5d59 `gray.600`; input 20x20 background #faf9f5 `gray.050` border 1px solid #5e5d59 `gray.600` radius 9999px shadow rgba(0, 0, 0, 0.02) 0px 0px 0px 1px inset; input::after 8pxx8px background #faf9f5 `gray.050` radius 9999px.

![Contact form default](components/crops/contact-form-default.png)

#### Text field
A text input in the form. Focused and filled with sample text that was deleted; nothing was sent. Read as `text-field` on the claude.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 755.38 x 56; padding 16px 24px; border 1px solid #e8e6dc `gray.200`; radius 16px; background #faf9f5 `gray.050`; text anthropicSans 15/18 400, #141413 `gray.950`; transition border-color 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease; placeholder #5e5d59 `gray.600` |
| focused, filled | border 1px solid #5e5d59 `gray.600` |

![Text field default](components/crops/text-field-default.png) ![Text field focused](components/crops/text-field-focused.png) ![Text field filled](components/crops/text-field-filled.png)

#### Text field box
The same field measured at rest (default only). Read as `text-field-box` on the claude.com/contact-sales page.

**Values (default).** size 755.38 x 56; padding 16px 24px; border 1px solid #e8e6dc `gray.200`; radius 16px; background #faf9f5 `gray.050`; text anthropicSans 15/18 400, #141413 `gray.950`; transition border-color 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease; placeholder #5e5d59 `gray.600`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Text area
The message textarea. Read as `text-area` on the claude.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 755.38 x 120; padding 16px 24px; border 1px solid #e8e6dc `gray.200`; radius 16px; background #faf9f5 `gray.050`; text anthropicSans 15/18 400, #141413 `gray.950`; transition border-color 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease; placeholder #5e5d59 `gray.600` |
| focused | border 1px solid #5e5d59 `gray.600` |

![Text area default](components/crops/text-area-default.png) ![Text area focused](components/crops/text-area-focused.png)

#### Select field
A select/combobox in the form. Read as `select-field` on the claude.com/contact-sales page.

**Values (default).** size 755.38 x 56; padding 16px 24px; border 1px solid #e8e6dc `gray.200`; radius 16px; background #faf9f5 `gray.050`; text anthropicSans 15/18 400, #141413 `gray.950`; transition border-color 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease.

![Select field default](components/crops/select-field-default.png)

#### Submit button
The form submit. Measured and focused, never pressed. Read as `submit-button` on the claude.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 755.38 x 44; background transparent; text anthropicSans 15/19.5 500, #141413 `gray.950` |

Child layers that carry the look: input 20x20 background #141413 `gray.950` border 1px solid #141413 `gray.950` radius 9999px shadow rgba(0, 0, 0, 0.02) 0px 0px 0px 1px inset; input::after 8pxx8px background #faf9f5 `gray.050` radius 9999px.

![Submit button default](components/crops/submit-button-default.png) ![Submit button hover](components/crops/submit-button-hover.png) ![Submit button focus-visible](components/crops/submit-button-focus-visible.png)

#### Topic radio row
A radio row in the "What can we help you with?" topic group. Read as `topic-radio-row` on the claude.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 755.38 x 44; background transparent; text anthropicSans 15/19.5 500, #141413 `gray.950` |

Child layers that carry the look: input 20x20 background #faf9f5 `gray.050` border 1px solid #5e5d59 `gray.600` radius 9999px shadow rgba(0, 0, 0, 0.02) 0px 0px 0px 1px inset; input::after 8pxx8px background #faf9f5 `gray.050` radius 9999px.

![Topic radio row default](components/crops/topic-radio-row-default.png) ![Topic radio row hover](components/crops/topic-radio-row-hover.png)

#### Radio input
The radio input inside a topic row. Read as `topic-radio` on the claude.com/contact-sales page.

**Values (default).** size 20 x 20; border 1px solid #5e5d59 `gray.600`; radius 9999px; background #faf9f5 `gray.050`; shadow rgba(0, 0, 0, 0.02) 0px 0px 0px 1px inset; text anthropicSans 15/17.25 400, #000000 `gray.1000`; transition border-color 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease; placeholder #000000 `gray.1000`.

![Radio input default](components/crops/topic-radio-default.png)

#### Field label
A label over a field in the form. Read as `field-label` on the claude.com/contact-sales page.

**Values (default).** size 73.3 x 19; background transparent; text anthropicSans 15/19.5 500, #141413 `gray.950`.

![Field label default](components/crops/field-label-default.png)

### Docs (platform.claude.com)

docs.claude.com: a cooler cds-* system - the 56px topbar, 264px sidebar with an ink-tint active pill, serif titles, 13/19 anthropicMono code, and the #184f95 method badge.

#### Docs top bar
The 56px docs header: product tabs, search, language, Console, Log in. Read as `docs-topbar` on the docs.claude.com API reference page.

**Values (default).** size 1440 x 56; padding 0px 16px; border B: 1px solid rgba(11, 11, 11, 0.1); background #fcfcfb `docs.gray-10`; text anthropicSerif 20/20 500, #0b0b0b `docs.gray-900`; icon 20 x 20, #0b0b0b `docs.gray-900`.

![Docs top bar default](components/crops/docs-topbar-default.png)

#### Docs top tab
A product tab in the docs header. Read as `docs-tab` on the docs.claude.com API reference page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 66.47 x 32; background transparent; text anthropicSans 14/20 400, #898781 `docs.gray-400` |

![Docs top tab default](components/crops/docs-tab-default.png) ![Docs top tab hover](components/crops/docs-tab-hover.png) ![Docs top tab pressed](components/crops/docs-tab-pressed.png)

#### Language picker
The "English" locale picker in the docs header. Read as `docs-lang` on the docs.claude.com API reference page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 89.33 x 32; padding 0px 12px; radius 8px; background transparent; text anthropicSans 14/20 400, #0b0b0b `docs.gray-900`; transition box-shadow 0.06s cubic-bezier(0.4, 0, 0.2, 1) |

![Language picker default](components/crops/docs-lang-default.png) ![Language picker hover](components/crops/docs-lang-hover.png)

#### Docs home title
The docs home h1 ("Start building with Claude"). Read as `docs-hero-title` on the docs.claude.com home page.

**Values (default).** size 317.48 x 114.38; background transparent; text anthropicSerif 52/57.2 300, #0b0b0b `docs.gray-900`.

![Docs home title default](components/crops/docs-hero-title-default.png)

#### Docs sidebar
The left docs navigation: section groups and page links. Read as `docs-sidebar` on the docs.claude.com API reference page.

**Values (default).** size 264 x 844; border R: 1px solid rgba(11, 11, 11, 0.1); background transparent; text Anthropicons-Variable 16/16 533.25, #898781 `docs.gray-400`.

Child layers that carry the look: aside 264x844 border 1px solid rgba(11, 11, 11, 0.1); button 239x32 background rgba(255, 255, 255, 0.5) radius 8px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(11, 11, 11, 0.1) 0px 0px 0px 1px inset; kbd 18x18 border 1px solid rgba(109, 107, 103, 0.18) radius 4px.

![Docs sidebar default](components/crops/docs-sidebar-default.png)

#### Docs nav link
A link in the docs sidebar. Read as `docs-nav-link` on the docs.claude.com API reference page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 247 x 32; radius 8px; background transparent; text anthropicSans 14/20 500, #0b0b0b `docs.gray-900` |
| focus-visible | shadow #fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px |

![Docs nav link default](components/crops/docs-nav-link-default.png) ![Docs nav link hover](components/crops/docs-nav-link-hover.png) ![Docs nav link focus-visible](components/crops/docs-nav-link-focus-visible.png) ![Docs nav link pressed](components/crops/docs-nav-link-pressed.png)

#### Docs nav link, current
The current page in the docs sidebar. Read as `docs-nav-active` on the docs.claude.com get-started page.

**Values (default).** size 91.09 x 32; padding 0px 12px; radius 3.35544e+07px; background rgba(11, 11, 11, 0.1); text anthropicSans 14/20 400, #0b0b0b `docs.gray-900`.

![Docs nav link, current default](components/crops/docs-nav-active-default.png)

#### Docs page title
The h1 at the top of a docs page. Read as `docs-start-title` on the docs.claude.com get-started page.

**Values (default).** size 295.2 x 32.81; background transparent; text anthropicSerif 26.25/32.81 520, #0b0b0b `docs.gray-900`.

![Docs page title default](components/crops/docs-start-title-default.png)

#### Docs body text
A paragraph of docs body copy. Read as `docs-start-body` on the docs.claude.com get-started page.

**Values (default).** size 832 x 25.31; background transparent; text anthropicSans 16.87/25.31 400, #52514e `docs.gray-600`.

![Docs body text default](components/crops/docs-start-body-default.png)

#### Docs code block
A fenced code block in the docs. Read as `docs-start-code-block` on the docs.claude.com get-started page.

**Values (default).** size 754 x 57; background transparent; text anthropicMono 13/19 400, #953800.

![Docs code block default](components/crops/docs-start-code-block-default.png)

#### Docs inline code
Inline `code` in the docs body. Read as `docs-start-inline-code` on the docs.claude.com get-started page.

**Values (default).** size 770 x 16; background transparent; text anthropicMono 13/19 400, #953800.

![Docs inline code default](components/crops/docs-start-inline-code-default.png)

#### Copy page button
The "Copy page" utility button above the docs body. Read as `docs-copy-page` on the docs.claude.com get-started page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 111.86 x 28; padding 0px 10px; radius 7px 0px 0px 7px; background transparent; text Anthropicons-Variable 20/20 433.25, #0b0b0b `docs.gray-900`; transition box-shadow 0.06s cubic-bezier(0.4, 0, 0.2, 1) |

Child layers that carry the look: span 111.9x28 background rgba(255, 255, 255, 0.1) radius 7px 0px 0px 7px.

![Copy page button default](components/crops/docs-copy-page-default.png) ![Copy page button hover](components/crops/docs-copy-page-hover.png)

#### Docs page title
The h1 at the top of a docs page. Read as `docs-api-title` on the docs.claude.com API reference page.

**Values (default).** size 130.3 x 35; background transparent; text anthropicSerif 28/35 520, #0b0b0b `docs.gray-900`.

![Docs page title default](components/crops/docs-api-title-default.png)

#### Docs body text
A paragraph of docs body copy. Read as `docs-api-body` on the docs.claude.com API reference page.

**Values (default).** size 720 x 42; background transparent; text anthropicSans 14/21 400, #52514e `docs.gray-600`.

![Docs body text default](components/crops/docs-api-body-default.png)

#### Docs inline code
Inline `code` in the docs body. Read as `docs-api-inline-code` on the docs.claude.com API reference page.

Not on the page when it was captured.

#### HTTP method badge
The method badge on an endpoint (POST, GET). Read as `docs-method-badge` on the docs.claude.com API reference page.

**Values (default).** size 31.38 x 15.59; padding 0px 0px 0.6px 0px; background transparent; text anthropicSans 12/15 500, #184f95 `brand.periwinkle-deep`.

![HTTP method badge default](components/crops/docs-method-badge-default.png)

#### Search field
The "Search ⌘K" field in the docs chrome (288x32, bg-fill-field). Opens the search dialog. Read as `docs-search-field` on the docs.claude.com API reference page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 239 x 32; padding 0px 5px 0px 8px; radius 8px; background rgba(255, 255, 255, 0.5); shadow rgba(11, 11, 11, 0.1) 0px 0px 0px 1px inset; text Anthropicons-Variable 16/16 533.25, #898781 `docs.gray-400`; transition color 0.06s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.06s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.06s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.06s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.06s cubic-bezier(0.4, 0, 0.2, 1), fill 0.06s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.06s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.06s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.06s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.06s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.06s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.06s cubic-bezier(0.4, 0, 0.2, 1), transform 0.06s cubic-bezier(0.4, 0, 0.2, 1), translate 0.06s cubic-bezier(0.4, 0, 0.2, 1), scale 0.06s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.06s cubic-bezier(0.4, 0, 0.2, 1), filter 0.06s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.06s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.06s cubic-bezier(0.4, 0, 0.2, 1), display 0.06s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.06s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.06s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.06s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | shadow rgba(11, 11, 11, 0.2) 0px 0px 0px 1px inset |
| focus-visible | shadow #fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px |

![Search field default](components/crops/docs-search-field-default.png) ![Search field hover](components/crops/docs-search-field-hover.png) ![Search field focus-visible](components/crops/docs-search-field-focus-visible.png)

### Overlays

The overlays a fresh profile meets: the nav dropdown (opened by a real hover) and the docs search dialog (opened from its field, measured open, nothing typed).

#### Search dialog
The docs search dialog opened from the header field. Nothing was typed. Read as `docs-search-dialog` on the docs.claude.com home page.

**Values (default).** size 672 x 500; radius 12px; background #ffffff `gray.000`; shadow rgba(11, 11, 11, 0.1) 0px 0px 0px 0px inset, rgba(11, 11, 11, 0.1) 0px 0px 0px 1px, rgba(11, 11, 11, 0.08) 0px 4px 8px 0px, rgba(11, 11, 11, 0.08) 0px 12px 28px -2px; text Anthropicons-Variable 16/16 533.25, #898781 `docs.gray-400`; transition scale 0.12s cubic-bezier(0.165, 0.84, 0.44, 1).

![Search dialog default](components/crops/docs-search-dialog-default.png)

#### Search input
The field inside the search dialog. Read as `docs-search-input` on the docs.claude.com home page.

**Values (default).** size 564 x 56; padding 16px 0px; background transparent; text anthropicSans 16/24 400, #0b0b0b `docs.gray-900`; placeholder #898781 `docs.gray-400`.

![Search input default](components/crops/docs-search-input-default.png)

### Mobile (390 wide)

The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the nav collapses to a menu button and a full-screen ink sheet.

#### Top navigation bar (mobile)
The header at 390: wordmark and menu button. Read as `m-nav-bar` on the www.anthropic.com home page at 390 wide.

**Values (default).** size 390 x 84; background #faf9f5 `gray.050`; text anthropicSans 13/20.02 400, #3d3d3a `gray.700`; transition transform 0.3s ease.

![Top navigation bar (mobile) default](components/crops/m-nav-bar-default.png)

#### Nav menu button (mobile)
The menu button in the mobile header. Opened for the screenshot; nothing is followed. Read as `m-nav-menu-btn` on the www.anthropic.com home page at 390 wide.

**Values (default).** size 28 x 28; padding 8px; border 1px solid #e8e6dc `gray.200`; radius 8px; background #f5f4ed `gray.100`; text anthropicSans 13/20.02 400, #3d3d3a `gray.700`; transition border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out, background-color 0.2s ease-in-out, color 0.2s ease-in-out; icon 20 x 20, #3d3d3a `gray.700`.

![Nav menu button (mobile) default](components/crops/m-nav-menu-btn-default.png)

#### Mobile nav sheet
The open navigation sheet at 390. Read as `m-nav-sheet` on the www.anthropic.com home page at 390 wide.

**Values (default).** size 390 x 844; background #141413 `gray.950`; text anthropicSans 30/38 600, #faf9f5 `gray.050`; transition opacity 0.15s ease; icon 35 x 24, #faf9f5 `gray.050`.

![Mobile nav sheet default](components/crops/m-nav-sheet-default.png)

#### Hero title (mobile)
The h1 at 390. Read as `m-hero-title` on the www.anthropic.com home page at 390 wide.

**Values (default).** size 326 x 260; background transparent; text anthropicSans 25/32.5 600, #141413 `gray.950`; transition color 0.3s ease.

![Hero title (mobile) default](components/crops/m-hero-title-default.png)

## Gaps

### Pages

- **The products.** claude.ai and console.anthropic.com are the signed-in surfaces: nothing behind Try Claude, Log in or Console was captured, and the chat UI, API keys, billing and Workbench are all missing. The kit never signs in or registers.
- **Checkout and account.** The plan CTAs and the contact-sales form lead to flows that were never submitted; no purchase was made and no field was filled for real.
- **Article-depth pages.** The index pages were captured; news posts, research papers and engineering entries were not opened.
- **Privacy choices dialog.** The footer's 'Privacy choices' opens a consent settings dialog; it was never opened because answering it is a submission.

### Themes

Only the docs ship a dark theme: `data-mode="system"` on html flips it under prefers-color-scheme: dark (captured as docs-home-dark / docs-api-dark). The marketing and product pages declare no dark values and did not change under prefers-color-scheme (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)), so the token file's `dark` set is the docs' theme only.

### Fonts

- **anthropicSans** is the UI face everywhere (also as anthropicSansDisplay and anthropicSansRomanFallback). **anthropicSerif** carries display headlines and the docs' titles; **anthropicMono** is 13/19 code on the docs. All are variable 300-800 faces served from Anthropic's hosts (see fontFaces in [raw/css-vars.json](raw/css-vars.json)).
- **Anthropicons-Variable** is the docs' icon font; its measured fractional weights tune the glyphs. All are commercial faces, not redistributable; Lato, Newsreader and IBM Plex Mono stand in inside the style guide.

### Screenshots

- People, paper and product imagery are Anthropic's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The docs' prose was not transcribed into the package; the components around it were measured.
- No personal data was captured: the pages were read signed out, and no form was filled with real contact details.

