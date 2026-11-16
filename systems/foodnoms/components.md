# Foodnoms components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from foodnoms.com on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844, the Dark group at 1440 x 900 under emulated prefers-color-scheme: dark — the site's own media rule, the theme a dark-system visitor sees), with computed styles read from the running page. There is no web sign-in anywhere: the product is an iOS/macOS app sold through the App Store, so every Download / Get-the-App / press-kit link was measured, never followed; the help search was opened and typed into then cleared, and the newsletter field was typed into then cleared — nothing was ever submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (94 components, 164 states). The layout patterns are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (158 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`: every captured surface paints light, and the routes listed under Dark also painted the site's authored dark theme under emulated prefers-color-scheme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). /terms is ~18k px tall, captured as two stitched tiles.

| Surface | URL | Light | Dark |
|---|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png) |
| Pricing (Foodnoms+) | `/plus` | [default](screenshots/plus-light-default.png), [full](screenshots/plus-light-full.png) | [default](screenshots/plus-dark-default.png), [full](screenshots/plus-dark-full.png) |
| Help center | `/help` | [accordion-open](screenshots/help-light-accordion-open.png), [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png), [search](screenshots/help-light-search.png) | [accordion-open](screenshots/help-dark-accordion-open.png), [default](screenshots/help-dark-default.png), [full](screenshots/help-dark-full.png), [search](screenshots/help-dark-search.png) |
| News | `/news` | [default](screenshots/news-light-default.png), [full](screenshots/news-light-full.png) | [default](screenshots/news-dark-default.png), [full](screenshots/news-dark-full.png) |
| Press hub | `/press` | [default](screenshots/press-light-default.png), [full](screenshots/press-light-full.png) | - |
| Family plan | `/family-plan` | [default](screenshots/family-plan-light-default.png), [full](screenshots/family-plan-light-full.png) | - |
| vs MyFitnessPal | `/vs/myfitnesspal` | [default](screenshots/vs-mfp-light-default.png), [full](screenshots/vs-mfp-light-full.png) | [default](screenshots/vs-mfp-dark-default.png), [full](screenshots/vs-mfp-dark-full.png) |
| Help article | `/help/barcode-scanning` | [default](screenshots/help-article-light-default.png), [full](screenshots/help-article-light-full.png) | [default](screenshots/help-article-dark-default.png), [full](screenshots/help-article-dark-full.png) |
| News article | `/news/foodnoms-2` | [default](screenshots/news-article-light-default.png), [full](screenshots/news-article-light-full.png) | - |
| Terms | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) | - |
| Privacy | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) | - |
| Open-in-app interstitial | `/open/settings/sign-up` | [default](screenshots/open-signup-light-default.png) | - |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) | - |
| Pricing, phone | `/plus` | [default](screenshots/mobile-plus-light-default.png), [full](screenshots/mobile-plus-light-full.png) | - |
| Help center, phone | `/help` | [default](screenshots/mobile-help-light-default.png), [full](screenshots/mobile-help-light-full.png) | - |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Framer search modal | /help | the "Search" trigger — a local UI toggle; text was typed and deleted, never submitted | [help-light-search](screenshots/help-light-search.png), [help-search-modal](#search-modal), [help-search-input](#search-field) |
| Help accordion | /help | the "About Foodnoms" section's own header (Closed -> Open) — a local UI toggle | [help-light-accordion-open](screenshots/help-light-accordion-open.png), [help-accordion-open](#accordion-section-open) |
| Mobile nav overlay | home, phone width | the "Open navigation menu" button — a local UI toggle; its label flips to Close | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-hamburger](#mobile-hamburger) |
| Newsletter form | /news | the email field was focused and typed into then deleted; the submit was hovered and focused, never pressed | [nl-email](#newsletter-email-field), [nl-submit](#newsletter-submit) |
| App Store links | every page | Download / Get the App / Try Foodnoms links and the press-kit zips were measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 22 components were given a real keyboard focus. 21 draw an outline ring: `nav-link` (1px auto #101010, offset 1px), `nav-cta` (1px auto #101010, offset 1px), `hero-icon-btn` (1px auto #101010, offset 1px), `cta-secondary` (1px auto #101010, offset 1px), `footer-link` (1px auto #101010, offset 1px), `plus-cta` (1px auto #101010, offset 1px), `plus-cta-secondary` (1px auto #101010, offset 1px), `help-search` (1px auto #101010, offset 0px), `help-accordion-header` (1px auto #101010, offset 0px), `help-accordion-link` (1px auto #101010, offset 1px), `help-contact-cta` (1px auto #101010, offset 1px), `news-card` (1px auto #101010, offset 1px), `press-asset` (1px auto #101010, offset 1px), `press-contact-cta` (1px auto #101010, offset 1px), `ha-back` (1px auto #101010, offset 1px), `ha-link` (1px auto #101010, offset 1px), `os-primary` (1px auto #101010, offset 1px), `m-hamburger` (1px auto #e59700, offset 0px), `m-hero-cta` (1px auto #e59700, offset 1px), `m-footer-link` (1px auto #e59700, offset 1px), `na-inline-link` (1px auto #101010, offset 1px). The other 1 show no measured change: `nl-submit`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.4s | `cubic-bezier(0.44, 0, 0.56, 1)` | color | d-footer-link, d-nav-link, footer-link, ha-link, help-accordion-link, m-footer-link, na-inline-link, nav-link |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 590 x 400 | - | 18.8px | #f2f2f2 `color.palette.neutral-50` | none | 40px 40px 0px 40px |
| [Value card](#value-card) | 300 x 181.58 | - | - | transparent | none | 0 |
| [Review card](#review-card) | 279 x 260 | - | - | transparent | none | 0 |
| [Article card](#article-card) | 442.66 x 396.52 | - | - | transparent | none | 0 |
| [Comparison table](#comparison-table) | 1000 x 1388.45 | - | - | transparent | none | 0 |
| [FAQ block](#faq-block) | 800 x 726.3 | - | - | transparent | none | 0 |
| [Mobile feature card](#mobile-feature-card) | 358 x 542.81 | - | 18.8px | #f2f2f2 `color.palette.neutral-50` | none | 40px 40px 0px 40px |

## Components

### App shell and navigation

The marketing header: app-icon + Foodnoms wordmark, News / Foodnoms+ / Help links and the orange "Get the App" App-Store pill.

#### Marketing header row
The top bar: app icon + Foodnoms name, News/Foodnoms+/Help links and the "Get the App" primary pill. Read as `nav-bar` on the home page.

**Values (default).** size 1200 x 40; background transparent; text Aquawax Pro Bold 24/24 700, #ff5406 `color.palette.misc-59`; layers a.framer-5UbMV.framer-OHnkM 145.0x40.0 color(display-p3 0.972549 0.384 0.18) 20px.

Child layers that carry the look: a 145x40 background #ff5406 `color.palette.misc-59` radius 20px.

![Marketing header row default](components/crops/nav-bar-default.png)

#### Logo
The Foodnoms app-icon + wordmark in the header; links home. Read as `nav-logo` on the home page.

**Values (default).** size 166 x 36; background transparent; text Aquawax Pro Bold 24/24 700, #ff5406 `color.palette.misc-59`.

![Logo default](components/crops/nav-logo-default.png)

#### Nav link
A header link (News / Foodnoms+ / Help); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 38 x 18; background transparent; text Aquawax Pro Medium 15/15 500, #666666 `color.palette.neutral-600`; transition color 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| hover | text Aquawax Pro Medium 15/15 500, #ff9c7b `color.palette.accent-200` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-text.framer-styles-preset-277bjg 38.0x18.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Aquawax Pro Medium 15/15 500, #ff9c7b `color.palette.accent-200` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Get-the-App pill
The orange "Get the App ↗" primary pill in the header; an App-Store link, measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 145 x 40; padding 12px 18px; radius 20px; background #ff5406 `color.palette.misc-59`; text Aquawax Pro DemiBold 16/16 600, #ffffff `color.palette.neutral-0` |
| hover | background #ff9c7b `color.palette.accent-200` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Get-the-App pill default](components/crops/nav-cta-default.png) ![Get-the-App pill hover](components/crops/nav-cta-hover.png) ![Get-the-App pill focus-visible](components/crops/nav-cta-focus-visible.png) ![Get-the-App pill pressed](components/crops/nav-cta-pressed.png)

### Home

The home page: the rotating-benefit hero ticker, the goal-pill marquee, the "As Featured By" press strip, feature cards, the values trio (Privacy First / Your Data, Your Control / No Ads, Ever), the review marquee and the closing CTA.

#### Hero headline ticker
The rotating benefit headline ("Track Nutrition", "Lose Weight", "Eat Healthy", …). The semantic h1 is visually hidden; this Title container is the painted display text. Read as `hero-ticker` on the home page.

**Values (default).** size 411 x 133.59; background transparent; text Aquawax Pro Bold 56/61.6 700, #ff5406 `color.palette.misc-59`; layers button 0.0x0.0 rgba(0, 0, 0, 0.2) 40px; button 0.0x0.0 rgba(0, 0, 0, 0.2) 40px.

Child layers that carry the look: button 0x0 background rgba(0, 0, 0, 0.2) radius 40px; button 0x0 background rgba(0, 0, 0, 0.2) radius 40px.

![Hero headline ticker default](components/crops/hero-ticker-default.png)

#### Hero lede
"A simple, clear nutrition tracker for building healthier habits." — the intro paragraph under the ticker. Read as `hero-lede` on the home page.

**Values (default).** size 800 x 28.8; background transparent; text Aquawax Pro Medium 18/28.8 500, #666666 `color.palette.neutral-600`.

![Hero lede default](components/crops/hero-lede-default.png)

#### Hero icon button
The circular icon button beside the hero headline (a Framer "Button" component with an inline svg). Read as `hero-icon-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 120 x 40; background transparent; text sans-serif 12/normal 400, #0000ee |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-hseoqs.framer-lux5qc 120.0x40.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text sans-serif 12/normal 400, #ff0000 |

![Hero icon button default](components/crops/hero-icon-btn-default.png) ![Hero icon button hover](components/crops/hero-icon-btn-hover.png) ![Hero icon button focus-visible](components/crops/hero-icon-btn-focus-visible.png) ![Hero icon button pressed](components/crops/hero-icon-btn-pressed.png)

#### Goal pill
A nutrition-goal chip in the benefits marquee (Weight, Healthy, Sugars, Water, Sodium, Muscle, Alcohol, Caffeine). Read as `goal-pill` on the home page.

**Values (default).** size 411 x 72; background transparent; text sans-serif 12/normal 400, #000000 `color.palette.neutral-1000`; opacity 0.6.

![Goal pill default](components/crops/goal-pill-default.png)

#### As-Featured-By label
The "As Featured By" caption over the press-logo strip. Read as `featured-title` on the home page.

**Values (default).** size 600 x 30.8; background transparent; text Aquawax Pro Bold 22/30.8 700, #0d0d0d `color.palette.neutral-950`.

![As-Featured-By label default](components/crops/featured-title-default.png)

#### Press logo
One outlet logo in the "As Featured By" strip (MacStories, iMore, 9to5Mac, PopSugar, Good Housekeeping, Prevention). Read as `featured-logo` on the home page.

**Values (default).** size 128 x 32; background transparent; text sans-serif 12/normal 400, #000000 `color.palette.neutral-1000`.

![Press logo default](components/crops/featured-logo-default.png)

#### Feature card
A feature section card ("Effortlessly Scan Food"): h3 title, paragraph and a product screenshot. Read as `feature-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 590 x 400; padding 40px 40px 0px 40px; radius 18.8px; background #f2f2f2 `color.palette.neutral-50`; text Aquawax Pro Bold 28/33.6 700, #0099f9 `color.palette.blue` |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

#### Feature heading
The h3 inside a feature card ("Effortlessly Scan Food"). Read as `feature-title` on the home page.

**Values (default).** size 239 x 67.19; background transparent; text Aquawax Pro Bold 28/33.6 700, #0099f9 `color.palette.blue`.

![Feature heading default](components/crops/feature-title-default.png)

#### Value card
A values card ("Privacy First", "Your Data, Your Control", "No Ads, Ever"): glyph, h4 title and paragraph. Read as `value-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 300 x 181.58; background transparent; text Aquawax Pro Bold 22/30.8 700, #0d0d0d `color.palette.neutral-950`; layers div.framer-WLnLp.framer-i4k58q 40.0x40.0 color(display-p3 0.486275 0.631373 0.760784) |

Child layers that carry the look: div 40x40 background #72a2c5 `color.palette.steel`.

![Value card default](components/crops/value-card-default.png) ![Value card hover](components/crops/value-card-hover.png)

#### Value glyph
The svg glyph on a values card. Read as `value-icon` on the home page.

**Values (default).** size 40 x 40; background #72a2c5 `color.palette.steel`; text sans-serif 12/normal 400, #000000 `color.palette.neutral-1000`.

![Value glyph default](components/crops/value-icon-default.png)

#### Reviews heading
"Trusted By Thousands of Users" — the reviews section h2. Read as `reviews-h2` on the home page.

**Values (default).** size 600 x 43.2; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![Reviews heading default](components/crops/reviews-h2-default.png)

#### Review card
An App-Store review card in the scrolling marquee (quote, handle, star row). Read as `review-card` on the home page.

**Values (default).** size 279 x 260; background transparent; text Aquawax Pro Bold 18/25.2 700, #0d0d0d `color.palette.neutral-950`; transform translate(10166px, 0px); layers div.framer-1075njn 279.0x260.0 color(display-p3 0.94902 0.94902 0.94902) 18.8px; div.framer-P8O4K.framer-hqvmb2 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1kv394 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1uk5w5j 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-194z1ba 18.0x18.0 color(display-p.

Child layers that carry the look: div 279x260 background #f2f2f2 `color.palette.neutral-50` radius 18.8px; div 18x18 background #ff5406 `color.palette.misc-59`; div 18x18 background #ff5406 `color.palette.misc-59`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Star rating
The five-star row on a review card. Read as `review-stars` on the home page.

**Values (default).** size 138 x 18; background transparent; text sans-serif 12/normal 400, #000000 `color.palette.neutral-1000`; layers div.framer-P8O4K.framer-hqvmb2 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1kv394 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1uk5w5j 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-194z1ba 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1yg8gv0 18.0x18.0 color(di.

Child layers that carry the look: div 18x18 background #ff5406 `color.palette.misc-59`; div 18x18 background #ff5406 `color.palette.misc-59`; div 18x18 background #ff5406 `color.palette.misc-59`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### CTA heading
"Start Tracking Macros for Free" — the closing call-to-action block. Read as `cta-h2` on the home page.

**Values (default).** size 600 x 43.2; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![CTA heading default](components/crops/cta-h2-default.png)

#### Secondary CTA
The "Download the App ↗" secondary pill inside the closing CTA; an App-Store link, measured never followed. Read as `cta-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 196 x 40; padding 12px 18px; radius 20px; background #f2f2f2 `color.palette.neutral-50`; text Aquawax Pro DemiBold 16/16 600, #ff5406 `color.palette.misc-59` |
| hover | background #e6e6e6 `color.palette.neutral-100` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Secondary CTA default](components/crops/cta-secondary-default.png) ![Secondary CTA hover](components/crops/cta-secondary-hover.png) ![Secondary CTA focus-visible](components/crops/cta-secondary-focus-visible.png) ![Secondary CTA pressed](components/crops/cta-secondary-pressed.png)

### Pricing (Foodnoms+)

The /plus surface: headline, the "Find pricing info for your region in the app" tag, the two download CTAs and the Free vs Foodnoms+ comparison table (a Framer Row/Header/Paragraph/Divider/Symbol component, not a <table>).

#### Pricing headline
"Level Up Your Nutrition Tracking" — the Foodnoms+ page headline. Read as `plus-h1` on the Foodnoms+ page.

**Values (default).** size 600 x 123.19; background transparent; text Aquawax Pro Bold 56/61.6 700, #0d0d0d `color.palette.neutral-950`.

![Pricing headline default](components/crops/plus-h1-default.png)

#### Tag chip
The "Find pricing info for your region in the app." note chip under the headline. Read as `plus-tag` on the Foodnoms+ page.

**Values (default).** size 310 x 21; background transparent; text Aquawax Pro Medium 15/21 500, #ffffff `color.palette.neutral-0`.

![Tag chip default](components/crops/plus-tag-default.png)

#### Try-for-free CTA
The "Try Foodnoms for Free ↗" primary pill; an App-Store link, measured never followed. Read as `plus-cta` on the Foodnoms+ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 224 x 40; padding 12px 18px; radius 20px; background #ff5406 `color.palette.misc-59`; text Aquawax Pro DemiBold 16/16 600, #ffffff `color.palette.neutral-0` |
| hover | background #ff9c7b `color.palette.accent-200` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Try-for-free CTA default](components/crops/plus-cta-default.png) ![Try-for-free CTA hover](components/crops/plus-cta-hover.png) ![Try-for-free CTA focus-visible](components/crops/plus-cta-focus-visible.png) ![Try-for-free CTA pressed](components/crops/plus-cta-pressed.png)

#### Secondary download pill
The "Download the App ↗" secondary pill on /plus; measured never followed. Read as `plus-cta-secondary` on the Foodnoms+ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 196 x 40; padding 12px 18px; radius 20px; background #f2f2f2 `color.palette.neutral-50`; text Aquawax Pro DemiBold 16/16 600, #ff5406 `color.palette.misc-59` |
| hover | background #e6e6e6 `color.palette.neutral-100` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Secondary download pill default](components/crops/plus-cta-secondary-default.png) ![Secondary download pill hover](components/crops/plus-cta-secondary-hover.png) ![Secondary download pill focus-visible](components/crops/plus-cta-secondary-focus-visible.png) ![Secondary download pill pressed](components/crops/plus-cta-secondary-pressed.png)

#### Comparison table
The Free vs Foodnoms+ feature-comparison table — a Framer component of Row/Header/Title/Paragraph/Divider/Symbol cells, not a <table> element. Read as `pricing-table` on the Foodnoms+ page.

**Values (default).** size 1000 x 1388.45; background transparent; text Aquawax Pro Bold 17/23.8 700, #0d0d0d `color.palette.neutral-950`; layers div.framer-g3o7pp 1000.0x1.0 color(display-p3 0.901961 0.901961 0.901961); div.framer-1ujdjyv 1000.0x1.0 color(display-p3 0.901961 0.901961 0.901961); div.framer-3cz472 1000.0x1.0 color(display-p3 0.901961 0.901961 0.901961); div.framer-10hz6qp 1000.0x1.0 color(display-p3 0.901961 0.901961 0.901961); div.framer-Mn18G.framer-1whp2gz 16.0x16.0 color(display-p3 0.972549 0.384314 0.180392); div.framer.

Child layers that carry the look: div 1000x1 background #e6e6e6 `color.palette.neutral-100`; div 1000x1 background #e6e6e6 `color.palette.neutral-100`; div 1000x1 background #e6e6e6 `color.palette.neutral-100`.

![Comparison table default](components/crops/pricing-table-default.png)

#### Table header cell
A column header cell in the comparison table ("Features" / "Free" / "Foodnoms+"). Read as `pricing-head` on the Foodnoms+ page.

**Values (default).** size 500 x 23.8; background transparent; text Aquawax Pro Bold 17/23.8 700, #0d0d0d `color.palette.neutral-950`.

![Table header cell default](components/crops/pricing-head-default.png)

#### Table row
A feature row ("Nutrient Tracking") with its Free and Foodnoms+ cells. Read as `pricing-row` on the Foodnoms+ page.

**Values (default).** size 1000 x 25.59; radius 12px; background transparent; text Aquawax Pro Medium 16/25.6 500, #333333 `color.palette.neutral-800`.

![Table row default](components/crops/pricing-row-default.png)

#### Table cell text
A feature cell value ("Calories & Macros" under Free). Read as `pricing-cell` on the Foodnoms+ page.

**Values (default).** size 218 x 25.59; background transparent; text Aquawax Pro Medium 16/25.6 500, #666666 `color.palette.neutral-600`.

![Table cell text default](components/crops/pricing-cell-default.png)

#### Table check glyph
The check-mark svg used for included features in the comparison table. Read as `pricing-check` on the Foodnoms+ page.

**Values (default).** size 16 x 16; background #ff5406 `color.palette.misc-59`; text sans-serif 12/normal 400, #000000 `color.palette.neutral-1000`.

![Table check glyph default](components/crops/pricing-check-default.png)

#### Table divider
The hairline divider between comparison rows. Read as `pricing-divider` on the Foodnoms+ page.

**Values (default).** size 1000 x 1; background #e6e6e6 `color.palette.neutral-100`; text sans-serif 12/normal 400, #000000 `color.palette.neutral-1000`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Help center

The /help landing: the Search trigger that opens Framer's search modal, the topic accordions (Closed -> Open via the section header, a local UI toggle) and the Contact Us block.

#### Help headline
"Help Center". Read as `help-h1` on the help center page.

**Values (default).** size 600 x 48.41; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![Help headline default](components/crops/help-h1-default.png)

#### Search trigger
The "Search" control on the help landing — a Framer component that opens the search modal when clicked (a local UI toggle). Read as `help-search` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 113 x 40; padding 12px 18px 12px 16px; radius 20px; background #ff5406 `color.palette.misc-59`; text Aquawax Pro DemiBold 16/16 600, #ffffff `color.palette.neutral-0`; icon 32 x 32, rgba(255, 255, 255, 0) |
| hover | background #ff9c7b `color.palette.accent-200` |
| focus-visible | outline 1px auto #101010, offset 0px |

![Search trigger default](components/crops/help-search-default.png) ![Search trigger hover](components/crops/help-search-hover.png) ![Search trigger focus-visible](components/crops/help-search-focus-visible.png) ![Search trigger pressed](components/crops/help-search-pressed.png)

#### Search modal
The Framer search overlay opened by the Search trigger. Read as `help-search-modal` on the help center page.

**Values (default).** size 1440 x 900; background transparent; text sans-serif 12/normal 400, #000000 `color.palette.neutral-1000`; icon 17.84 x 17.84, #ff5406 `color.palette.misc-59`; layers div 1440.0x900.0 rgba(46, 46, 46, 0.6); div 594.7x56.5 color(display-p3 1 1 1) rgba(46, 46, 46, 0.26) 0px 0px 20px 0px 26px.

Child layers that carry the look: div 1440x900 background rgba(46, 46, 46, 0.6); div 594.7x56.5 background #ffffff `color.palette.neutral-0` radius 26px shadow rgba(46, 46, 46, 0.26) 0px 0px 20px 0px.

![Search modal default](components/crops/help-search-modal-default.png)

#### Search field
The real input inside the Framer search modal; focused and typed into then cleared — never submitted. Read as `help-search-input` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 530 x 34; background transparent; text Aquawax Pro Medium 17/34 500, #2f2f2f `color.palette.ink`; placeholder rgba(47, 47, 47, 0.64) `color.palette.ink-64` `color.palette.ink-64` |
| filled | size 500 x 34 |

![Search field default](components/crops/help-search-input-default.png) ![Search field focused](components/crops/help-search-input-focused.png) ![Search field filled](components/crops/help-search-input-filled.png)

#### Accordion section (closed)
A collapsed topic group ("About Foodnoms"): header row with title and rotating + chevron; the question links sit inside. Read as `help-accordion` on the help center page.

**Values (default).** size 800 x 25.2; background transparent; text Aquawax Pro Bold 18/25.2 700, #0d0d0d `color.palette.neutral-950`; icon 22.63 x 22.63, #000000 `color.palette.neutral-1000`.

![Accordion section (closed) default](components/crops/help-accordion-default.png)

#### Accordion section (open)
The same topic group expanded — measured after clicking its own Header (a local UI toggle; Closed -> Open). Read as `help-accordion-open` on the help center page.

**Values (default).** size 800 x 112.39; background transparent; text Aquawax Pro Bold 18/25.2 700, #0d0d0d `color.palette.neutral-950`; icon 16 x 16, #000000 `color.palette.neutral-1000`.

![Accordion section (open) default](components/crops/help-accordion-open-default.png)

#### Accordion header
The clickable header row of a topic group (tabindex=0, data-highlight): title + chevron. Read as `help-accordion-header` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 800 x 25.2; background transparent; text Aquawax Pro Bold 18/25.2 700, #0d0d0d `color.palette.neutral-950`; icon 16 x 16, #000000 `color.palette.neutral-1000` |
| focus-visible | outline 1px auto #101010, offset 0px; layers div.framer-3e3bb0 800.0x25.2 1px auto rgb(16, 16, 16) offset 0px |

![Accordion header default](components/crops/help-accordion-header-default.png) ![Accordion header hover](components/crops/help-accordion-header-hover.png) ![Accordion header focus-visible](components/crops/help-accordion-header-focus-visible.png)

#### Accordion question link
A question link inside an open accordion ("What is Foodnoms?"); measured, never followed. Read as `help-accordion-link` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 149 x 18; background transparent; text Aquawax Pro Medium 16/25.6 500, #ff5406 `color.palette.misc-59`; transition color 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-text.framer-styles-preset-ksvyhk 149.0x18.0 1px auto rgb(16, 16, 16) offset 1px |

![Accordion question link default](components/crops/help-accordion-link-default.png) ![Accordion question link hover](components/crops/help-accordion-link-hover.png) ![Accordion question link focus-visible](components/crops/help-accordion-link-focus-visible.png) ![Accordion question link pressed](components/crops/help-accordion-link-pressed.png)

#### Contact block
The "Contact Us" block under the accordion sections. Read as `help-contact` on the help center page.

**Values (default).** size 1200 x 146; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`; layers a.framer-5UbMV.framer-OHnkM 116.0x40.0 color(display-p3 0.972549 0.384 0.18) 20px.

Child layers that carry the look: a 116x40 background #ff5406 `color.palette.misc-59` radius 20px.

![Contact block default](components/crops/help-contact-default.png)

#### Contact CTA
The mailto CTA in the Contact block (support@foodnoms.com, a published contact address); measured, never activated. Read as `help-contact-cta` on the help center page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 116 x 40; padding 12px 18px; radius 20px; background #ff5406 `color.palette.misc-59`; text Aquawax Pro DemiBold 16/16 600, #ffffff `color.palette.neutral-0` |
| hover | background #ff9c7b `color.palette.accent-200` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Contact CTA default](components/crops/help-contact-cta-default.png) ![Contact CTA hover](components/crops/help-contact-cta-hover.png) ![Contact CTA focus-visible](components/crops/help-contact-cta-focus-visible.png) ![Contact CTA pressed](components/crops/help-contact-cta-pressed.png)

### News

The /news index: article cards and the "Become a Foodnoms Insider" newsletter block, whose email field was focused and typed into then cleared, never submitted.

#### News headline
"News & Updates". Read as `news-h1` on the news page.

**Values (default).** size 600 x 48.41; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![News headline default](components/crops/news-h1-default.png)

#### Article card
A news article card (CMS image, title, date) linking to a /news/* article; measured, never followed. Read as `news-card` on the news page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 442.66 x 396.52; background transparent; text Aquawax Pro Bold 18/25.2 700, #333333 `color.palette.neutral-800` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-EwUIO.framer-hjQD7 442.7x396.5 1px auto rgb(16, 16, 16) offset 1px |

![Article card default](components/crops/news-card-default.png) ![Article card hover](components/crops/news-card-hover.png) ![Article card focus-visible](components/crops/news-card-focus-visible.png) ![Article card pressed](components/crops/news-card-pressed.png)

#### Card date
The publish-date label on a news card. Read as `news-date` on the news page.

**Values (default).** size 398.39 x 21; background transparent; text Aquawax Pro Medium 15/21 500, #666666 `color.palette.neutral-600`.

![Card date default](components/crops/news-date-default.png)

#### Newsletter heading
"Become a Foodnoms Insider" — the newsletter block heading. Read as `nl-h2` on the news page.

**Values (default).** size 600 x 43.2; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![Newsletter heading default](components/crops/nl-h2-default.png)

#### Newsletter email field
The pill-shaped email field in the newsletter block; focused and typed into then cleared — never submitted. Read as `nl-email` on the news page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 294 x 42; padding 12px 18px; radius 40px; background #f2f2f2 `color.palette.neutral-50`; shadow #ff784b 0px 0px 0px 0px inset, #e6e6e6 0px 0px 0px 1px inset; text Aquawax Pro Medium 16/16 500, #333333 `color.palette.neutral-800`; placeholder #cccccc `color.palette.neutral-200` |
| focused, filled | shadow #ff784b 0px 0px 0px 2px inset, #e6e6e6 0px 0px 0px 1px inset |

![Newsletter email field default](components/crops/nl-email-default.png) ![Newsletter email field focused](components/crops/nl-email-focused.png) ![Newsletter email field filled](components/crops/nl-email-filled.png)

#### Newsletter submit
The subscribe submit control; hovered and focused only — never pressed (it posts the form). Read as `nl-submit` on the news page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 96 x 42; padding 12px 18px; radius 40px; background #ff5406 `color.palette.misc-59`; text Aquawax Pro DemiBold 16/16 600, #ffffff `color.palette.neutral-0`; placeholder #ffffff `color.palette.neutral-0` |

![Newsletter submit default](components/crops/nl-submit-default.png) ![Newsletter submit hover](components/crops/nl-submit-hover.png) ![Newsletter submit focus-visible](components/crops/nl-submit-focus-visible.png)

### Press

The /press hub: the app-details block, the press-kit asset links (measured, never downloaded) and the press-contact mailto pill.

#### Press headline
"Press Hub". Read as `press-h1` on the press hub page.

**Values (default).** size 600 x 48.41; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![Press headline default](components/crops/press-h1-default.png)

#### Section tag
A tag label on the press page sections. Read as `press-tag` on the press hub page.

**Values (default).** size 600 x 25.2; background transparent; text Aquawax Pro Bold 18/25.2 700, #0d0d0d `color.palette.neutral-950`.

![Section tag default](components/crops/press-tag-default.png)

#### App details block
The "App Details" fact block on the press hub. Read as `press-details` on the press hub page.

**Values (default).** size 800 x 212.8; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![App details block default](components/crops/press-details-default.png)

#### Asset download link
The "Download Screenshots" asset link (a framerusercontent .zip); measured, never downloaded. Read as `press-asset` on the press hub page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 241 x 40; padding 12px 18px; radius 50px; background #f2f2f2 `color.palette.neutral-50`; text Aquawax Pro DemiBold 16/16 600, #ff5406 `color.palette.misc-59` |
| hover | background #e6e6e6 `color.palette.neutral-100` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Asset download link default](components/crops/press-asset-default.png) ![Asset download link hover](components/crops/press-asset-hover.png) ![Asset download link focus-visible](components/crops/press-asset-focus-visible.png) ![Asset download link pressed](components/crops/press-asset-pressed.png)

#### Press contact CTA
The "Email Ryan />" secondary pill (a published press-contact mailto); measured, never activated. Read as `press-contact-cta` on the press hub page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 137 x 40; padding 12px 18px; radius 20px; background #f2f2f2 `color.palette.neutral-50`; text Aquawax Pro DemiBold 16/16 600, #ff5406 `color.palette.misc-59` |
| hover | background #e6e6e6 `color.palette.neutral-100` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Press contact CTA default](components/crops/press-contact-cta-default.png) ![Press contact CTA hover](components/crops/press-contact-cta-hover.png) ![Press contact CTA focus-visible](components/crops/press-contact-cta-focus-visible.png) ![Press contact CTA pressed](components/crops/press-contact-cta-pressed.png)

### Article pages

The long-form surfaces: /family-plan, /vs/myfitnesspal, a help article and a news article — headline, tag/date, prose and a static FAQ block.

#### Article headline
"A calorie tracker with a family plan" — the /family-plan article headline. Read as `fp-h1` on the family plan page.

**Values (default).** size 800 x 48.41; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![Article headline default](components/crops/fp-h1-default.png)

#### Intro paragraph
The article intro block under the headline. Read as `fp-intro` on the family plan page.

**Values (default).** size 800 x 167.97; background transparent; text Aquawax Pro Medium 16/25.6 500, #333333 `color.palette.neutral-800`.

![Intro paragraph default](components/crops/fp-intro-default.png)

#### FAQ block
The "Frequently asked questions" block — static question + Answer rows, not an accordion. Read as `fp-faq` on the family plan page.

**Values (default).** size 800 x 726.3; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![FAQ block default](components/crops/fp-faq-default.png)

#### FAQ answer
An answer paragraph inside the FAQ block. Read as `fp-faq-answer` on the family plan page.

**Values (default).** size 800 x 51.19; background transparent; text Aquawax Pro Medium 16/25.6 500, #333333 `color.palette.neutral-800`.

![FAQ answer default](components/crops/fp-faq-answer-default.png)

#### Comparison headline
The /vs/myfitnesspal article headline. Read as `vs-h1` on the vs MyFitnessPal page.

**Values (default).** size 800 x 145.22; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![Comparison headline default](components/crops/vs-h1-default.png)

#### Article body
A body paragraph in the comparison article. Read as `vs-body` on the vs MyFitnessPal page.

**Values (default).** size 800 x 102.38; background transparent; text Aquawax Pro Medium 16/25.6 500, #333333 `color.palette.neutral-800`.

![Article body default](components/crops/vs-body-default.png)

#### Comparison table
The "Quick Comparison" feature table inside the article body. Read as `vs-table` on the vs MyFitnessPal page.

**Values (default).** size 800 x 811.28; background transparent; text Aquawax Pro Medium 16/25.6 500, #333333 `color.palette.neutral-800`; layers th.framer-text 172.2x51.6 color(display-p3 0.94902 0.94902 0.94902) B:2px solid; th.framer-text 328.0x51.6 color(display-p3 0.94902 0.94902 0.94902) B:2px solid; th.framer-text 299.8x51.6 color(display-p3 0.94902 0.94902 0.94902) B:2px solid; td.framer-text 172.2x50.6 B:1px solid; td.framer-text 328.0x50.6 B:1px solid; td.framer-text 299.8x50.6 B:1px solid.

Child layers that carry the look: th 172.2x51.6 background #f2f2f2 `color.palette.neutral-50` border 2px solid; th 328x51.6 background #f2f2f2 `color.palette.neutral-50` border 2px solid; th 299.8x51.6 background #f2f2f2 `color.palette.neutral-50` border 2px solid.

![Comparison table default](components/crops/vs-table-default.png)

#### FAQ heading
The "Frequently Asked Questions" h2 in the article. Read as `vs-faq-h2` on the vs MyFitnessPal page.

**Values (default).** size 800 x 43.2; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![FAQ heading default](components/crops/vs-faq-h2-default.png)

#### Back link
The "← Back" pill at the top of a help article (links to /help); measured, never followed. Read as `ha-back` on the help article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 95 x 40; padding 12px 18px; radius 20px; background #f2f2f2 `color.palette.neutral-50`; text Aquawax Pro DemiBold 16/16 600, #ff5406 `color.palette.misc-59` |
| hover | background #e6e6e6 `color.palette.neutral-100` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Back link default](components/crops/ha-back-default.png) ![Back link hover](components/crops/ha-back-hover.png) ![Back link focus-visible](components/crops/ha-back-focus-visible.png) ![Back link pressed](components/crops/ha-back-pressed.png)

#### Article tag
The category tag chip on a help article. Read as `ha-tag` on the help article page.

**Values (default).** size 400 x 23.8; background transparent; text Aquawax Pro Bold 17/23.8 700, #666666 `color.palette.neutral-600`.

![Article tag default](components/crops/ha-tag-default.png)

#### Article headline
"How do I scan barcodes?" — a help article title. Read as `ha-h1` on the help article page.

**Values (default).** size 800 x 48.41; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![Article headline default](components/crops/ha-h1-default.png)

#### Article body
A body paragraph inside the help article. Read as `ha-body` on the help article page.

**Values (default).** size 780 x 25.59; background transparent; text Aquawax Pro Medium 16/25.6 500, #333333 `color.palette.neutral-800`.

![Article body default](components/crops/ha-body-default.png)

#### Article section heading
A section heading inside the article ("Scanning a Barcode"). Read as `ha-h2` on the help article page.

**Values (default).** size 800 x 43.2; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![Article section heading default](components/crops/ha-h2-default.png)

#### Inline link
A link inside a help article's prose (the /help/mcp article; the barcode article has none); measured, never followed. Read as `ha-link` on the help-mcp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 184 x 18; background transparent; text Aquawax Pro Medium 16/25.6 500, #ff5406 `color.palette.misc-59`; transition color 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-text.framer-styles-preset-ksvyhk 184.0x18.0 1px auto rgb(16, 16, 16) offset 1px |

![Inline link default](components/crops/ha-link-default.png) ![Inline link hover](components/crops/ha-link-hover.png) ![Inline link focus-visible](components/crops/ha-link-focus-visible.png) ![Inline link pressed](components/crops/ha-link-pressed.png)

#### Article date
The publish-date label above the article title. Read as `na-date` on the news article page.

**Values (default).** size 400 x 23.8; background transparent; text Aquawax Pro Bold 17/23.8 700, #666666 `color.palette.neutral-600`.

![Article date default](components/crops/na-date-default.png)

#### Article headline
"FoodNoms 2: Feature Overview" — a news article title. Read as `na-h1` on the news article page.

**Values (default).** size 800 x 48.41; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![Article headline default](components/crops/na-h1-default.png)

#### Table of contents label
The "Table of Contents" heading beside the anchor list. Read as `na-toc` on the news article page.

**Values (default).** size 800 x 43.2; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![Table of contents label default](components/crops/na-toc-default.png)

#### Article section heading
A section heading inside the news article. Read as `na-h2` on the news article page.

**Values (default).** size 800 x 43.2; background transparent; text Aquawax Pro Bold 36/43.2 700, #0d0d0d `color.palette.neutral-950`.

![Article section heading default](components/crops/na-h2-default.png)

#### Article body
A body paragraph in the news article. Read as `na-body` on the news article page.

**Values (default).** size 800 x 51.19; background transparent; text Aquawax Pro Medium 16/25.6 500, #333333 `color.palette.neutral-800`.

![Article body default](components/crops/na-body-default.png)

#### Inline link
An inline link inside the article prose ("HidrateSpark"); measured, never followed. Read as `na-inline-link` on the news article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 102 x 18; background transparent; text Aquawax Pro Medium 16/25.6 500, #ff5406 `color.palette.misc-59`; transition color 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-text.framer-styles-preset-ksvyhk 102.0x18.0 1px auto rgb(16, 16, 16) offset 1px |

![Inline link default](components/crops/na-inline-link-default.png) ![Inline link hover](components/crops/na-inline-link-hover.png) ![Inline link focus-visible](components/crops/na-inline-link-focus-visible.png) ![Inline link pressed](components/crops/na-inline-link-pressed.png)

### Legal

The /terms page: one tall Legal Item body under the h1 (/privacy is the same shape).

#### Terms headline
"Terms of Use". Read as `terms-h1` on the terms page.

**Values (default).** size 600 x 48.41; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![Terms headline default](components/crops/terms-h1-default.png)

#### Legal section heading
A numbered section heading inside the legal body ("1. Agreement to these Terms" style; the single Legal Item component holds the whole document). Read as `terms-item` on the terms page.

**Values (default).** size 800 x 33.59; background transparent; text Aquawax Pro Bold 28/33.6 700, #0d0d0d `color.palette.neutral-950`.

![Legal section heading default](components/crops/terms-item-default.png)

### Open-in-app interstitial

The /open/settings/sign-up page: the "Open in Foodnoms" interstitial an app deep link lands on in a browser.

#### Interstitial headline
"Open in Foodnoms" — the deep-link interstitial shown when an app link is opened on the web. Read as `os-h1` on the open-in-app interstitial page.

**Values (default).** size 600 x 48.41; background transparent; text Aquawax Pro Bold 44/48.4 700, #0d0d0d `color.palette.neutral-950`.

![Interstitial headline default](components/crops/os-h1-default.png)

#### Interstitial action
The "Open in Foodnoms" pill on the interstitial — the page's own action (a deep link back into the app); measured, never followed. Read as `os-primary` on the open-in-app interstitial page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 181 x 40; padding 12px 18px; radius 20px; background #f2f2f2 `color.palette.neutral-50`; text Aquawax Pro DemiBold 16/16 600, #ff5406 `color.palette.misc-59` |
| hover | background #e6e6e6 `color.palette.neutral-100` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Interstitial action default](components/crops/os-primary-default.png) ![Interstitial action hover](components/crops/os-primary-hover.png) ![Interstitial action focus-visible](components/crops/os-primary-focus-visible.png) ![Interstitial action pressed](components/crops/os-primary-pressed.png)

### Dark theme (emulated prefers-color-scheme)

The same home components under the site's own (prefers-color-scheme: dark) media rule, painted in a dark-scheme browser context — the theme a dark-system visitor sees, not a reconstruction.

#### Page canvas (dark)
The top-level frame under the dark media rule. Read as `d-body` on the home, dark page.

**Values (default).** size 1440 x 4462.67; background transparent; text Aquawax Pro Bold 24/24 700, #ff5406 `color.palette.misc-59`; layers div.framer-HghBH.framer-pfRB1 1440.0x4462.7 color(display-p3 0 0 0); a.framer-5UbMV.framer-OHnkM 145.0x40.0 color(display-p3 0.972549 0.384 0.18) 20px; div.framer-yY4Sd.framer-wYouK 0.0x0.0 color(display-p3 0 0 0); button 0.0x0.0 rgba(0, 0, 0, 0.2) 40px; button 0.0x0.0 rgba(0, 0, 0, 0.2) 40px; div.framer-15q1eiy 590.0x400.0 color(display-p3 0.101 0.101 0.101) 18.8px.

Child layers that carry the look: div 1440x4462.7 background #000000 `color.palette.neutral-1000`; a 145x40 background #ff5406 `color.palette.misc-59` radius 20px; div 0x0 background #000000 `color.palette.neutral-1000`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Get-the-App pill (dark)
The header primary pill under the dark media rule. Read as `d-nav-cta` on the home, dark page.

**Values (default).** size 145 x 40; padding 12px 18px; radius 20px; background #ff5406 `color.palette.misc-59`; text Aquawax Pro DemiBold 16/16 600, #ffffff `color.palette.neutral-0`.

![Get-the-App pill (dark) default](components/crops/d-nav-cta-default.png)

#### Nav link (dark)
A header link under the dark media rule. Read as `d-nav-link` on the home, dark page.

**Values (default).** size 38 x 18; background transparent; text Aquawax Pro Medium 15/15 500, #999999 `color.palette.neutral-400`; transition color 0.4s cubic-bezier(0.44, 0, 0.56, 1).

![Nav link (dark) default](components/crops/d-nav-link-default.png)

#### Hero lede (dark)
The hero paragraph under the dark media rule. Read as `d-hero-lede` on the home, dark page.

**Values (default).** size 800 x 28.8; background transparent; text Aquawax Pro Medium 18/28.8 500, #999999 `color.palette.neutral-400`.

![Hero lede (dark) default](components/crops/d-hero-lede-default.png)

#### Feature card (dark)
A feature card under the dark media rule. Read as `d-feature-card` on the home, dark page.

**Values (default).** size 590 x 400; padding 40px 40px 0px 40px; radius 18.8px; background #1a1a1a `color.palette.misc-11`; text Aquawax Pro Bold 28/33.6 700, #0099f9 `color.palette.blue`.

![Feature card (dark) default](components/crops/d-feature-card-default.png)

#### Value card (dark)
A values card under the dark media rule. Read as `d-value-card` on the home, dark page.

**Values (default).** size 300 x 181.58; background transparent; text Aquawax Pro Bold 22/30.8 700, #f2f2f2 `color.palette.neutral-50`; layers div.framer-WLnLp.framer-i4k58q 40.0x40.0 color(display-p3 0.486275 0.631373 0.760784).

Child layers that carry the look: div 40x40 background #72a2c5 `color.palette.steel`.

![Value card (dark) default](components/crops/d-value-card-default.png)

#### Review card (dark)
A review card under the dark media rule. Read as `d-review-card` on the home, dark page.

**Values (default).** size 279 x 260; background transparent; text Aquawax Pro Bold 18/25.2 700, #f2f2f2 `color.palette.neutral-50`; transform translate(10166px, 0px); layers div.framer-1075njn 279.0x260.0 color(display-p3 0.101 0.101 0.101) 18.8px; div.framer-P8O4K.framer-hqvmb2 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1kv394 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1uk5w5j 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-194z1ba 18.0x18.0 color(display-p3 0.97.

Child layers that carry the look: div 279x260 background #1a1a1a `color.palette.misc-11` radius 18.8px; div 18x18 background #ff5406 `color.palette.misc-59`; div 18x18 background #ff5406 `color.palette.misc-59`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Footer (dark)
The footer under the dark media rule. Read as `d-footer` on the home, dark page.

**Values (default).** size 1376 x 288.8; background transparent; text Aquawax Pro Bold 17/23.8 700, #ffffff `color.palette.neutral-0`; layers div.framer-13gyf4z 1376.0x243.8 color(display-p3 0.972549 0.384314 0.180392) 18.8px; div.framer-cVfOO.framer-pqxif3 126.0x74.1 color(display-p3 1 1 1); div.framer-1g93id6 96.0x1.0 rgb(187, 221, 255).

Child layers that carry the look: div 1376x243.8 background #ff5406 `color.palette.misc-59` radius 18.8px; div 126x74.1 background #ffffff `color.palette.neutral-0`; div 96x1 background #bbddff.

![Footer (dark) default](components/crops/d-footer-default.png)

#### Footer link (dark)
A footer link under the dark media rule. Read as `d-footer-link` on the home, dark page.

**Values (default).** size 87 x 18; background transparent; text Aquawax Pro Medium 15/15 500, #ffffff `color.palette.neutral-0`; transition color 0.4s cubic-bezier(0.44, 0, 0.56, 1).

![Footer link (dark) default](components/crops/d-footer-link-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the top bar with hamburger (its overlay is evidenced by the mobile-home-light-drawer screenshot), the hero and cards at mobile metrics.

#### Mobile top bar
The phone top bar: app icon, Foodnoms name and the hamburger. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 358 x 40; background transparent; text Aquawax Pro Bold 24/24 700, #ff5406 `color.palette.misc-59`; icon 24 x 24, #000000 `color.palette.neutral-1000`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile hamburger
The "Open navigation menu" button that opens the phone nav overlay (its aria-label flips to "Close navigation menu" once open, so the opened overlay is evidenced by the mobile-home-light-drawer screenshot and the m-drawer-link reading taken inside it). Read as `m-hamburger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40 x 40; background transparent; text sans-serif 12/normal 400, #000000 `color.palette.neutral-1000`; icon 24 x 24, #000000 `color.palette.neutral-1000` |
| focus-visible | outline 1px auto #e59700, offset 0px; layers button.framer-x03zsu 40.0x40.0 1px auto rgb(229, 151, 0) offset 0px |

![Mobile hamburger default](components/crops/m-hamburger-default.png) ![Mobile hamburger hover](components/crops/m-hamburger-hover.png) ![Mobile hamburger focus-visible](components/crops/m-hamburger-focus-visible.png) ![Mobile hamburger pressed](components/crops/m-hamburger-pressed.png)

#### Mobile hero ticker
The rotating headline at 390 wide. Read as `m-hero-ticker` on the home page at 390 wide.

**Values (default).** size 266 x 85.59; background transparent; text Aquawax Pro Bold 36/39.6 700, #ff5406 `color.palette.misc-59`; layers button 0.0x0.0 rgba(0, 0, 0, 0.2) 40px; button 0.0x0.0 rgba(0, 0, 0, 0.2) 40px.

Child layers that carry the look: button 0x0 background rgba(0, 0, 0, 0.2) radius 40px; button 0x0 background rgba(0, 0, 0, 0.2) radius 40px.

![Mobile hero ticker default](components/crops/m-hero-ticker-default.png)

#### Mobile hero CTA
The primary App-Store pill on the phone layout; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 145 x 40; padding 12px 18px; radius 20px; background #ff5406 `color.palette.misc-59`; text Aquawax Pro DemiBold 16/16 600, #ffffff `color.palette.neutral-0` |
| hover | background #ff9c7b `color.palette.accent-200` |
| focus-visible | outline 1px auto #e59700, offset 1px |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

#### Mobile feature card
A feature card at 390 wide. Read as `m-feature-card` on the home page at 390 wide.

**Values (default).** size 358 x 542.81; padding 40px 40px 0px 40px; radius 18.8px; background #f2f2f2 `color.palette.neutral-50`; text Aquawax Pro Bold 22/26.4 700, #0099f9 `color.palette.blue`.

![Mobile feature card default](components/crops/m-feature-card-default.png)

#### Mobile review card
A review card at 390 wide. Read as `m-review-card` on the home page at 390 wide.

**Values (default).** size 279 x 260; background transparent; text Aquawax Pro Bold 16/22.4 700, #0d0d0d `color.palette.neutral-950`; transform translate(10166px, 0px); layers div.framer-1075njn 279.0x260.0 color(display-p3 0.94902 0.94902 0.94902) 18.8px; div.framer-P8O4K.framer-hqvmb2 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1kv394 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-1uk5w5j 18.0x18.0 color(display-p3 0.972549 0.384314 0.180392); div.framer-P8O4K.framer-194z1ba 18.0x18.0 color(display-p.

Child layers that carry the look: div 279x260 background #f2f2f2 `color.palette.neutral-50` radius 18.8px; div 18x18 background #ff5406 `color.palette.misc-59`; div 18x18 background #ff5406 `color.palette.misc-59`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile footer link
A footer link at 390 wide; measured, never followed. Read as `m-footer-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87 x 18; background transparent; text Aquawax Pro Medium 15/15 500, #ffffff `color.palette.neutral-0`; transition color 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| hover | text Aquawax Pro Medium 15/15 500, #ff9c7b `color.palette.accent-200` |
| focus-visible | outline 1px auto #e59700, offset 1px; layers a.framer-text.framer-styles-preset-277bjg 87.0x18.0 1px auto rgb(229, 151, 0) offset 1px |
| pressed | text Aquawax Pro Medium 15/15 500, #ff9c7b `color.palette.accent-200` |

![Mobile footer link default](components/crops/m-footer-link-default.png) ![Mobile footer link hover](components/crops/m-footer-link-hover.png) ![Mobile footer link focus-visible](components/crops/m-footer-link-focus-visible.png) ![Mobile footer link pressed](components/crops/m-footer-link-pressed.png)

### Footer

The site footer: Explore / Comparisons / Company / Social link columns, the mailto link and the legal row.

#### Footer
The site footer: logo, Explore / Comparisons / Company / Social link columns and the legal row. Read as `footer` on the home page.

**Values (default).** size 1376 x 288.8; background transparent; text Aquawax Pro Bold 17/23.8 700, #ffffff `color.palette.neutral-0`; layers div.framer-13gyf4z 1376.0x243.8 color(display-p3 0.972549 0.384314 0.180392) 18.8px; div.framer-cVfOO.framer-pqxif3 126.0x74.1 color(display-p3 1 1 1); div.framer-1g93id6 96.0x1.0 rgb(187, 221, 255).

Child layers that carry the look: div 1376x243.8 background #ff5406 `color.palette.misc-59` radius 18.8px; div 126x74.1 background #ffffff `color.palette.neutral-0`; div 96x1 background #bbddff.

![Footer default](components/crops/footer-default.png)

#### Footer column label
A link-column heading in the footer ("Explore"). Read as `footer-col` on the home page.

**Values (default).** size 61 x 23.8; background transparent; text Aquawax Pro Bold 17/23.8 700, #ffffff `color.palette.neutral-0`.

![Footer column label default](components/crops/footer-col-default.png)

#### Footer link
A footer link ("Download ↗" under Explore); measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87 x 18; background transparent; text Aquawax Pro Medium 15/15 500, #ffffff `color.palette.neutral-0`; transition color 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| hover | text Aquawax Pro Medium 15/15 500, #ff9c7b `color.palette.accent-200` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.framer-text.framer-styles-preset-277bjg 87.0x18.0 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text Aquawax Pro Medium 15/15 500, #ff9c7b `color.palette.accent-200` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Copyright line
The "(C) 2026. Algebraic Labs, LLC." line beside the Terms/Privacy links. Read as `footer-legal` on the home page.

**Values (default).** size 199 x 15; background transparent; text Aquawax Pro Medium 15/15 500, #333333 `color.palette.neutral-800`.

![Copyright line default](components/crops/footer-legal-default.png)

## Icons

13 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv): the gradient wordmark, the search magnifiers, the close/X glyphs, and the mask-painted glyphs — Framer draws most icons as a div with a `-webkit-mask-image` data-URI SVG whose `background-color` supplies the tint (recorded in the tint column): the shield/cloud/eye-off value glyphs, the pricing checks and crosses, the goal-pill star, the question, megaphone and newspaper glyphs. The press outlets' logos in the "As Featured By" strip, the App Store badge and the Foodnoms app icon are brand artwork and were left out. The SVGs are the product's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [wordmark](icons/wordmark.svg) | 120x33 | 0 0 144 40 | inline | home | Label |
| [shield-check](icons/shield-check.svg) | 40x40 | 0 0 40 40 | mask data-URI | home | Symbol |
| [cloud](icons/cloud.svg) | 40x40 | 0 0 40 40 | mask data-URI | home | Symbol |
| [eye-off](icons/eye-off.svg) | 40x40 | 0 0 40 40 | mask data-URI | home | Symbol |
| [star](icons/star.svg) | 18x18, 17x18 | 0 0 40 40 | mask data-URI | home | Symbol |
| [check-circle](icons/check-circle.svg) | 16x16 | 0 0 40 40 | mask data-URI | plus | Symbol |
| [xmark-circle](icons/xmark-circle.svg) | 16x16 | 0 0 40 40 | mask data-URI | plus | Symbol |
| [search](icons/search.svg) | 32x32 | 0 0 256 256 | inline | help | Variant 1 |
| [xmark](icons/xmark.svg) | 22x22, 20x20 | 0 0 40 40 | inline | help, mobile-home | Symbol; Close navigation menu |
| [question](icons/question.svg) | 40x40 | 0 0 40 40 | mask data-URI | help | Symbol |
| [search-small](icons/search-small.svg) | 16x16 | 0 0 40 40 | mask data-URI | help | Symbol |
| [megaphone](icons/megaphone.svg) | 40x40 | 0 0 40 40 | mask data-URI | news | Symbol |
| [newspaper](icons/newspaper.svg) | 40x40 | 0 0 40 40 | mask data-URI | press | Symbol |

## Gaps

### The product itself

Foodnoms is an iOS/macOS app sold through the App Store — there is no web app and no web sign-in. Everything the product does inside the app (food logging, AI scanning, widgets, the community database editor, subscription purchase) lives behind the App Store download, which was never installed or opened. /download is a JS redirect to apps.apple.com and was never followed; the /open/settings/* pages are static deep-link interstitials, measured at rest only.

### Pages

- **Pricing amounts.** /plus says "Find pricing info for your region in the app" — no prices are rendered publicly, so none are evidence here.
- **Further routes.** The sitemap lists dozens more help, news, press and comparison articles of the same templates; one representative of each was captured.
- **The help search results.** The modal was opened and typed into, but result rows were never clicked.
- **app./community./web. subdomains** did not answer; api.foodnoms.com 404s.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing. Several anchors' own `color` stays the browser default (rgb(0,0,238)) while the painted text inside carries the real colour — each entry's text row shows the painted value.
- **Disabled, error and loading states** were not seen on the public surface.
- **The mobile drawer** could not be re-measured as a component (the toggle's aria-label flips once open and its links share text with the footer); it is evidenced by the mobile-home-light-drawer screenshot.

### Themes

The site repaints a real dark theme under `(prefers-color-scheme: dark)` — 39 `--token-*` names redeclare (the neutral ramp inverts; the accent ramp re-points; the accent pills stay orange). It is captured under an emulated dark scheme, the same code path a dark-system visitor takes. There is no user-facing theme toggle on the site; the theme follows the OS.

### Fonts

- **Aquawax Pro** (Bold/DemiBold/Medium/Heavy) is a proprietary uploaded font, loaded from Framer's CDN; the style guide falls back to a rounded system sans. **Fragment Mono** is declared in @font-face but no measured surface paints it. Font files are never committed.

### Screenshots

- Product screenshots, the app icon, press-kit logos, review text and outlet marks in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article prose, review quotes, the press-kit zips' contents and the app-store copy are the product's content; only frames and components were measured.
