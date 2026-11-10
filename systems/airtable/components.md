# Airtable components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.airtable.com's public marketing pages on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Nothing was signed into, submitted, bought or sent; no consent dialog was answered and no form was submitted.

The public surface is the **www.airtable.com marketing site**: white surfaces, #181d26 ink text in Haas, a --color-primitive-* ramp system plus --color-surface/text/border-* semantics and a per-section --theme_* set all declared on :root. Most pages typeset in Haas/ATSeasonSans; /pricing runs Inter Display and /marketplace GT Eesti Display. The site is light-only - prefers-color-scheme changes nothing (`themeChecks` in raw/css-vars.json). Third-party UI (the Qualified 'Riley' chat widget and Google One Tap) is swept out of every shot.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (79 components, 168 states). The page layouts are described in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/18 500, #000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (168 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` . Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). There is no dark pass - the site ships one theme.

| Surface | URL | Screenshots |
|---|---|---|
| www.airtable.com home. Hero, feature carousel, coloured path tiles, resource cards; also the nav drawer and the promo bar closed. | `https://www.airtable.com/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [nav-dropdown](screenshots/home-light-nav-dropdown.png), [promo-closed](screenshots/home-light-promo-closed.png) |
| www.airtable.com/platform. 'The Airtable Platform' hero, building cards, customer-stories carousel. | `https://www.airtable.com/platform` | [default](screenshots/platform-light-default.png), [full](screenshots/platform-light-full.png) |
| www.airtable.com/platform/ai. The AI page: 'Airtable Agents', card grids, FAQ. | `https://www.airtable.com/platform/ai` | [default](screenshots/platform-ai-light-default.png), [full](screenshots/platform-ai-light-full.png) |
| www.airtable.com/solutions. The solutions index. | `https://www.airtable.com/solutions` | [default](screenshots/solutions-light-default.png), [full](screenshots/solutions-light-full.png) |
| www.airtable.com/solutions/enterprise. The enterprise page. | `https://www.airtable.com/solutions/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| www.airtable.com/pricing. Plan columns, comparison grid, FAQ. | `https://www.airtable.com/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| www.airtable.com/contact-sales. The sales form, never submitted. | `https://www.airtable.com/contact-sales` | [default](screenshots/contact-sales-light-default.png), [full](screenshots/contact-sales-light-full.png) |
| www.airtable.com/customer-stories. The stories index. | `https://www.airtable.com/customer-stories` | [default](screenshots/customer-stories-light-default.png), [full](screenshots/customer-stories-light-full.png) |
| www.airtable.com/templates. Filter rail + template gallery. | `https://www.airtable.com/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| www.airtable.com/marketplace. Category tiles + extension rows. | `https://www.airtable.com/marketplace` | [default](screenshots/marketplace-light-default.png), [full](screenshots/marketplace-light-full.png) |
| www.airtable.com/whatsnew. 'Where Airtable is headed.' + the embedded release gallery. | `https://www.airtable.com/whatsnew` | [default](screenshots/whatsnew-light-default.png), [full](screenshots/whatsnew-light-full.png) |
| www.airtable.com/about. The about page. | `https://www.airtable.com/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| www.airtable.com home at 390: menu button, hero, the side sheet open. | `https://www.airtable.com/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [nav-open](screenshots/mobile-home-light-nav-open.png) |
| www.airtable.com/pricing at 390. | `https://www.airtable.com/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| www.airtable.com/platform at 390. | `https://www.airtable.com/platform` | [default](screenshots/mobile-platform-light-default.png), [full](screenshots/mobile-platform-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Nav drawer | www.airtable.com | the Platform trigger was clicked once; a local disclosure, closed with Escape | [home-light-nav-dropdown](screenshots/home-light-nav-dropdown.png), [nav-dropdown](#nav-drawer) |
| Promo dismissal | www.airtable.com | the promo bar's close button hid it; a local toggle | [home-light-promo-closed](screenshots/home-light-promo-closed.png), [promo-close](#promo-close-button) |
| Country dropdown | www.airtable.com/contact-sales | the 'Country' combobox was clicked open; nothing chosen | [select-field-open](#select-field-open) |
| FAQ accordions | www.airtable.com/platform/ai, /pricing | one question each was expanded; a local disclosure | [faq-item-open](#faq-item-open), [pricing-faq-item-open](#pricing-faq-item-open) |
| Mobile nav sheet | www.airtable.com at 390 | the 'Open side menu' button opened the drawer | [mobile-home-light-nav-open](screenshots/mobile-home-light-nav-open.png), [m-nav-sheet](#mobile-nav-sheet) |

## Checklist coverage

The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. 11 of 19 are captured; the rest do not exist on the public marketing surface.

| Component | Entries | States captured |
|---|---|---|
| Button | [Hero primary CTA](#hero-primary-cta), [Hero secondary CTA](#hero-secondary-cta), [Sign up button](#sign-up-button), [Book Demo button](#book-demo-button), [Platform CTA](#platform-cta), [Plan CTA](#plan-cta), [Submit button](#submit-button) | default, hover, focus-visible, pressed |
| Icon button | [Promo close button](#promo-close-button), [Carousel control](#carousel-control), [Stories previous button](#stories-previous-button), [Stories next button](#stories-next-button), [Stories pause button](#stories-pause-button), [Nav menu button (mobile)](#nav-menu-button-mobile) | default, hover, focus-visible, pressed |
| Link | [Nav link](#nav-link), [Footer link](#footer-link), [Promo link](#promo-link), [Log in link](#log-in-link), [Drawer link](#drawer-link) | default, hover, focus-visible, pressed |
| Text field | [Text field](#text-field), [Text field box](#text-field-box), [Email field](#email-field), [Phone field](#phone-field), [Marketplace search field](#marketplace-search-field) | default, focused, filled |
| Text area | [Text area](#text-area) | default, focused |
| Select | [Select field](#select-field), [Select field, open](#select-field-open), [Country selector](#country-selector), [What's new filter](#whats-new-filter) | default, hover, focus-visible |
| Checkbox | not captured: the sales form has none; the templates filter rail is a plain link list | - |
| Radio | not captured: none on the public surface | - |
| Switch | not captured: none measured; no public toggle was found | - |
| Tabs | [Feature tab](#feature-tab), [Feature tab, selected](#feature-tab-selected) | default, hover, focus-visible, pressed |
| Menu | [Nav drawer](#nav-drawer), [Drawer link](#drawer-link), [Mobile nav sheet](#mobile-nav-sheet), [Nav dropdown trigger](#nav-dropdown-trigger) | default, hover, focus-visible, pressed |
| Tooltip | not captured: none appeared on hover or focus | - |
| Dialog | not captured: no dialog on the public pages; the nav drawer is the closest disclosure | - |
| Toast | not captured: no toast appeared after any action the capture took signed out | - |
| Card | [Feature card](#feature-card), [Coloured tile card](#coloured-tile-card), [Platform feature card](#platform-feature-card), [Platform AI card](#platform-ai-card), [Resource card](#resource-card), [Marketplace category card](#marketplace-category-card), [Template card](#template-card), [What's new card](#whats-new-card), [Story row](#story-row), [About page card](#about-page-card), [Solutions card](#solutions-card), [Enterprise card](#enterprise-card), [Plan card](#plan-card) | default, hover |
| List row | [Comparison row](#comparison-row), [Filter section](#filter-section), [Filter section, open](#filter-section-open), [FAQ item](#faq-item), [Pricing FAQ item](#pricing-faq-item) | default, hover, focus-visible |
| Table | [Plan comparison table](#plan-comparison-table), [Comparison row](#comparison-row) | default |
| Avatar | not captured: no avatars on the public surface | - |
| Badge | not captured: the whatsnew release cards carry plan chips inside the embed, not a standalone badge | - |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 24 components were given a real keyboard focus. 21 show a change: `promo-close` (1px auto #333840, offset 0px), `nav-trigger` (2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 0px), `nav-link` (2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 2px), `nav-demo` (2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 2px), `nav-signup` (2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 2px), `nav-login` (2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 2px), `hero-cta-primary` (ring shadow rgba(153, 160, 174, 0.16) 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px), `hero-cta-secondary` (ring shadow rgba(153, 160, 174, 0.16) 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px), `platform-cta` (2px solid #161616, offset 2px), `feature-tab` (2px solid #161616, offset -2px), `stories-prev` (2px solid #ffffff `primitive-neutrals-white`, offset 2px), `stories-next` (2px solid #ffffff `primitive-neutrals-white`, offset 2px), `stories-pause` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px), `platform-ai-cta` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px), `plan-cta` (1px auto #005fcc, offset 1px), `country-selector` (1px auto #005fcc, offset 0px), `filter-section` (1px auto #005fcc, offset 0px), `market-cta` (2px solid #166ee1, offset 2px), `carousel-control` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px), `submit-button` (ring shadow rgba(153, 160, 174, 0.16) 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px), `whatsnew-filter` (2px solid #166ee1, offset 0px). The other 3 draw nothing new - buttons and nav controls take a 2px rgba(4,14,32,.69) ring offset 2-4px and fields a 1px #005fcc outline: `promo-link`, `footer-link`, `plan-see-more`.

**Pressed.** Pressed was forced with DevTools, so it is the :active styles only: the dark ink CTAs darken to rgba(7,12,20,.82) and the outline buttons fill rgba(15,48,106,.05). The submit button and every sign-in/demo link were never pressed for real.

**Motion.** Transitions measured on the components, by duration; the site's declared curves are the --motion-* set (core.motion in tokens.json): standard/decelerate/accelerate at 150-600ms.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.085s | `ease-in` | all | market-card |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | background-color, border-color, box-shadow, color | carousel-control, platform-ai-cta, stories-pause, template-card |
| 0.15s | `ease` | background-color, border-color, color | platform-card, platform-cta, stories-next, stories-prev |
| 0.15s | `ease-in` | all, transform | m-nav-bar, nav-bar, nav-demo, nav-dropdown-link, nav-link, nav-login, nav-trigger, promo-link and more |
| 0.2s | `linear` | all | hero-cta-primary, hero-cta-secondary, nav-signup, submit-button |
| 0.25s | `ease` | all | field-label |
| 0.25s | `ease-in` | all | hero-title, m-hero-title, solutions-card-title, story-card-title |

**Layout.** Read on each page ([raw/layout.json](raw/layout.json)).

| Page | Frame | Content column | Grids | Fixed |
|---|---|---|---|---|
| home | - | max-width 1536px | 8 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky) |
| platform | - | max-width 1344px | 5 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky) |
| platform-ai | - | max-width 1344px | 7 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky), Home (sticky) |
| solutions | - | max-width 1536px | 8 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky) |
| enterprise | - | max-width 1344px | 6 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky) |
| pricing | - | full width | 4 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky), Bring your Airtable data into Claude. (sticky) |
| contact-sales | - | max-width 1536px | 8 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky), Contact our sales team (sticky) |
| customer-stories | - | max-width 1536px | 8 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky) |
| templates | - | full width | 8 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky), Search templates (sticky) |
| marketplace | - | full width | 4 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky), Bring your Airtable data into Claude. (sticky) |
| whatsnew | - | max-width 350px | 5 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky) |
| about | - | max-width 1344px | 6 grids (2 col gap 0px; 2 col gap 32px) | Bring your Airtable data into Claude. (sticky) |
| mobile-home | - | max-width 1536px | 8 grids (2 col gap 0px; 2 col gap normal) | Bring your Airtable data into Claude. (sticky), Platform (fixed) |

**Card shapes.** Default-state values; the entries hold the states. The signature cards are the 32px-radius coloured tiles (#c7e5f2 blue, #fcab79 orange) and the 16px white index cards on #e0e2e6 borders; release cards run 6px, marketplace tiles 12px.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature card](#feature-card) | 1312 x 371.14 | 1px solid #e0e2e6 | 16px | #f8fafc | none | 0 |
| [Coloured tile card](#coloured-tile-card) | 437.34 x 427 | - | 32px | #c7e5f2 | none | 24px 0px 0px 0px |
| [Platform feature card](#platform-feature-card) | 670 x 540.97 | - | - | #ffffff `primitive-neutrals-white` | none | 0 |
| [Solutions card](#solutions-card) | 437.33 x 207.59 | 1px solid #e0e2e6 | 16px | #ffffff `primitive-neutrals-white` | none | 24px |
| [Marketplace category card](#marketplace-category-card) | 373.33 x 279.98 | - | 12px | - | transparent 0px 0px 0px 5px | 0px 0px 279.984px 0px |
| [What's new card](#whats-new-card) | 387 x 565 | - | 6px | #ffffff `primitive-neutrals-white` | rgba(0, 0, 0, 0.24) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 2px 0px, rgba(0, 0, 0, 0.08) 0px 2px 4px 0px | 0 |
| [Plan card](#plan-card) | 296.5 x 454.5 | R: 1px solid #0d52ac; B: 1px solid #0d52ac; L: 1px solid #0d52ac | 0px 0px 12px 12px | rgba(240, 246, 255, 0.5) | none | 0px 24px 16px 24px |
| [Nav drawer](#nav-drawer) | 710.59 x 900 | - | 50% | #ffffff `primitive-neutrals-white` | none | 121.297px 0px 0px 0px |

## Components

### Shell and navigation

The chrome shared by every marketing page: a 121px top bar - a promo strip above the wordmark + section drawers (Platform / Solutions / Resources), Book Demo, a dark Sign up pill and Log in - plus the link-columns footer. Platform and Solutions open a 710px nav drawer; on a phone the bar collapses to a menu button and a side sheet.

#### Promo bar
The dismissible strip above the nav ("Bring your Airtable data into Claude. Try it now"). Read as `promo-bar` on the www.airtable.com/platform page.

**Values (default).** size 1440 x 42.5; background #f0f6ff; text ATSeasonSans 14/17.5 400, #333840; icon 18 x 12, #254fad.

![Promo bar default](components/crops/promo-bar-default.png)

#### Promo link
The "Try it now" link in the promo bar. Measured and focused, never followed. Read as `promo-link` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 82.28 x 18.19; radius 10px; background transparent; outline 2px solid transparent, offset 4px; text ATSeasonSans 14/18.2 650, #254fad; transition all 0.15s ease-in; icon 18 x 12, #254fad |
| hover | opacity 0.75 |
| focus-visible | outline 2px solid #254fad, offset 4px; opacity 0.75 |
| pressed | opacity 0.75 |

Child layers that carry the look: a 82.3x18.2 radius 10px.

![Promo link default](components/crops/promo-link-default.png) ![Promo link hover](components/crops/promo-link-hover.png) ![Promo link focus-visible](components/crops/promo-link-focus-visible.png) ![Promo link pressed](components/crops/promo-link-pressed.png)

#### Promo close button
The × that dismisses the promo bar; a local dismissal, measured and focused, never pressed. Read as `promo-close` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 12 x 12; background transparent; text ATSeasonSans 14/17.5 400, #333840; icon 12 x 12, #333840 |
| focus-visible | outline 1px auto #333840, offset 0px |

![Promo close button default](components/crops/promo-close-default.png) ![Promo close button hover](components/crops/promo-close-hover.png) ![Promo close button focus-visible](components/crops/promo-close-focus-visible.png)

#### Top navigation bar
The header on every marketing page: the Airtable wordmark, Platform/Solutions/Resources triggers, Enterprise, Pricing, What's new, and Book Demo / Sign up for free / Log in. Read as `nav-bar` on the www.airtable.com/platform page.

**Values (default).** size 1440 x 121.3; background transparent; text ATSeasonSans 14/17.5 400, #333840; transition all 0.15s ease-in; icon 18 x 12, #254fad.

Child layers that carry the look: nav 1440x121.3 background #ffffff `primitive-neutrals-white` shadow rgba(15, 48, 106, 0.05) 0px 0px 20px 0px; div 1440x42.5 background #f0f6ff; a 82.3x18.2 radius 10px.

![Top navigation bar default](components/crops/nav-bar-default.png)

#### Nav dropdown trigger
A section trigger in the header (Platform); opens the section drawer on click. Measured, never followed. Read as `nav-trigger` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 77.97 x 20.8; background transparent; text ATSeasonSans 16/20.8 650, #181d26 `primitive-neutrals-black`; transition all 0.15s ease-in; icon 12 x 12, #181d26 `primitive-neutrals-black` |
| hover | text ATSeasonSans 16/20.8 650, #254fad; icon 12 x 12, #254fad |
| focus-visible | outline 2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 0px; text ATSeasonSans 16/20.8 650, #254fad; icon 12 x 12, #254fad |
| pressed | text ATSeasonSans 16/20.8 650, #254fad; icon 12 x 12, #254fad |

![Nav dropdown trigger default](components/crops/nav-trigger-default.png) ![Nav dropdown trigger hover](components/crops/nav-trigger-hover.png) ![Nav dropdown trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav dropdown trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
A direct link in the header (Enterprise, Pricing, What's new). Measured, never followed. Read as `nav-link` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 50.25 x 20.8; background transparent; text ATSeasonSans 16/20.8 650, #181d26 `primitive-neutrals-black`; transition all 0.15s ease-in |
| hover | text ATSeasonSans 16/20.8 650, #254fad |
| focus-visible | outline 2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 2px; text ATSeasonSans 16/20.8 650, #254fad |
| pressed | text ATSeasonSans 16/20.8 650, #254fad |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Book Demo button
The outline "Book Demo" button in the header. Measured and focused, never followed (it leaves for the demo form). Read as `nav-demo` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 134.64 x 54.8; padding 16px 24px; border 1px solid #181d26 `primitive-neutrals-black`; radius 12px; background transparent; text ATSeasonSans 16/20.8 650, #181d26 `primitive-neutrals-black`; transition all 0.15s ease-in |
| hover | border 1px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`; text ATSeasonSans 16/20.8 650, rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5` |
| focus-visible | background rgba(249, 252, 255, 0.97); shadow rgba(153, 160, 174, 0.16) 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px; outline 2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 2px |
| pressed | background rgba(15, 48, 106, 0.05); text ATSeasonSans 16/20.8 650, rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5` |

![Book Demo button default](components/crops/nav-demo-default.png) ![Book Demo button hover](components/crops/nav-demo-hover.png) ![Book Demo button focus-visible](components/crops/nav-demo-focus-visible.png) ![Book Demo button pressed](components/crops/nav-demo-pressed.png)

#### Sign up button
The dark "Sign up for free" pill in the header. Measured and focused, never followed. Read as `nav-signup` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160.06 x 54.8; padding 16px 24px; border 1px solid #181d26 `primitive-neutrals-black`; radius 12px; background #181d26 `primitive-neutrals-black`; text ATSeasonSans 16/20.8 650, #ffffff `primitive-neutrals-white`; transition all 0.2s linear |
| hover | border 1px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`; background rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5` |
| focus-visible | shadow rgba(153, 160, 174, 0.16) 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px; outline 2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 2px |
| pressed | border 1px solid rgba(7, 12, 20, 0.82) `primitive-opacity-darken-6`; background rgba(7, 12, 20, 0.82) `primitive-opacity-darken-6` |

![Sign up button default](components/crops/nav-signup-default.png) ![Sign up button hover](components/crops/nav-signup-hover.png) ![Sign up button focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign up button pressed](components/crops/nav-signup-pressed.png)

#### Log in link
The "Log in" text link in the header. Measured and focused, never followed. Read as `nav-login` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 42.69 x 20.8; background transparent; text ATSeasonSans 16/20.8 650, #181d26 `primitive-neutrals-black`; transition all 0.15s ease-in |
| hover | text ATSeasonSans 16/20.8 650, #254fad |
| focus-visible | outline 2px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`, offset 2px; text ATSeasonSans 16/20.8 650, #254fad |
| pressed | text ATSeasonSans 16/20.8 650, #254fad |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Nav drawer
The full-height drawer the Platform trigger opens (product areas and a promo card). Shown click-open; a local disclosure. Read as `nav-dropdown` on the www.airtable.com/platform page.

**Values (default).** size 710.59 x 900; padding 121.297px 0px 0px 0px; background #ffffff `primitive-neutrals-white`; text ATSeasonSans 14/18.9 650, rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`.

![Nav drawer default](components/crops/nav-dropdown-default.png)

#### Footer
The site footer: link columns (Platform, Solutions, Resources, Learn, Company), social icons, legal row. Read as `footer` on the www.airtable.com/platform page.

**Values (default).** size 1248 x 307.19; background transparent; text ATSeasonSans 16/21.6 650, #333333.

Child layers that carry the look: a 112.6x25.6 border 2px solid transparent; a 72.5x25.6 border 2px solid transparent; a 126x25.6 border 2px solid transparent.

![Footer default](components/crops/footer-default.png)

#### Footer link
A link in the footer columns. Measured, never followed. Read as `footer-link` on the www.airtable.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 211.2 x 30; background transparent; text Haas 16/21.6 400, #333840 |

Child layers that carry the look: a 38.4x25.6 border 2px solid transparent.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Drawer link
An item in the open nav drawer (Airtable Platform). Read as `nav-dropdown-link` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 710.59 x 74.8; padding 12px 48px; background transparent; text ATSeasonSans 20/26 650, #181d26 `primitive-neutrals-black`; transition all 0.15s ease-in |
| hover | background rgba(15, 48, 106, 0.05) |

![Drawer link default](components/crops/nav-dropdown-link-default.png) ![Drawer link hover](components/crops/nav-dropdown-link-hover.png)

### Home

www.airtable.com's home: the 'Your team's apps. Fast.' hero with dark ink CTAs, the feature carousel (tabs, pause, prev/next arrows on a dark band), the coloured 32px-radius path tiles, and the resource cards.

#### Hero title
The home h1 ("All your teams, all their workflows — connected in one workspace"). Read as `hero-title` on the www.airtable.com home page.

**Values (default).** size 906.67 x 96; background transparent; text Haas 40/48 400, #333840; transition all 0.25s ease-in.

![Hero title default](components/crops/hero-title-default.png)

#### Hero primary CTA
The dark "Get started for free" pill under the hero title. Read as `hero-cta-primary` on the www.airtable.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200.59 x 55.59; padding 16px 24px; border 1px solid #181d26 `primitive-neutrals-black`; radius 12px; background #181d26 `primitive-neutrals-black`; shadow rgba(0, 0, 0, 0.32) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 2px 0px, rgba(45, 127, 249, 0.28) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 0px 0px 0.5px inset; text Haas 16/21.6 500, #ffffff `primitive-neutrals-white`; transition all 0.2s linear |
| hover | border 1px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`; background rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`; shadow none |
| focus-visible | shadow rgba(153, 160, 174, 0.16) 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px |
| pressed | border 1px solid rgba(7, 12, 20, 0.82) `primitive-opacity-darken-6`; background rgba(7, 12, 20, 0.82) `primitive-opacity-darken-6`; shadow none |

![Hero primary CTA default](components/crops/hero-cta-primary-default.png) ![Hero primary CTA hover](components/crops/hero-cta-primary-hover.png) ![Hero primary CTA focus-visible](components/crops/hero-cta-primary-focus-visible.png) ![Hero primary CTA pressed](components/crops/hero-cta-primary-pressed.png)

#### Hero secondary CTA
The outline "Book demo" pill beside the primary CTA. Read as `hero-cta-secondary` on the www.airtable.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138.33 x 55.59; padding 16px 24px; border 1px solid #181d26 `primitive-neutrals-black`; radius 12px; background transparent; shadow rgba(0, 0, 0, 0.32) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 2px 0px, rgba(0, 0, 0, 0.08) 0px 1px 3px 0px, rgba(1, 20, 53, 0.12) 0px 0px 0px 1px inset; text Haas 16/21.6 500, #181d26 `primitive-neutrals-black`; transition all 0.2s linear |
| hover | border 1px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`; shadow none; text Haas 16/21.6 500, rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5` |
| focus-visible | background rgba(249, 252, 255, 0.97); shadow rgba(153, 160, 174, 0.16) 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px |
| pressed | background rgba(15, 48, 106, 0.05); shadow none; text Haas 16/21.6 500, rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5` |

![Hero secondary CTA default](components/crops/hero-cta-secondary-default.png) ![Hero secondary CTA hover](components/crops/hero-cta-secondary-hover.png) ![Hero secondary CTA focus-visible](components/crops/hero-cta-secondary-focus-visible.png) ![Hero secondary CTA pressed](components/crops/hero-cta-secondary-pressed.png)

#### Feature card
The large red "Sophisticated workflows" feature card. Read as `feature-card` on the www.airtable.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1312 x 371.14; background transparent; text Haas 18/21.6 500, #181d26 `primitive-neutrals-black` |

Child layers that carry the look: div 405.3x371.1 background #f8fafc border 1px solid #e0e2e6 radius 16px; div 405.3x371.1 background #f8fafc border 1px solid #e0e2e6 radius 16px; div 405.3x371.1 background #f8fafc border 1px solid #e0e2e6 radius 16px.

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

#### AI feature card
The light-blue "Say hello to Omni" card. Read as `ai-card` on the www.airtable.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 683.3 x 107; background transparent; text Haas 24/39 400, #181d26 `primitive-neutrals-black` |

![AI feature card default](components/crops/ai-card-default.png) ![AI feature card hover](components/crops/ai-card-hover.png)

#### Coloured tile card
A coloured tile in the "path to 10x" grid (orange, blue, green surfaces). Read as `tile-card` on the www.airtable.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 437.34 x 427; padding 24px 0px 0px 0px; radius 32px; background #c7e5f2; text Haas 32/40 500, #0a2e0e |

![Coloured tile card default](components/crops/tile-card-default.png) ![Coloured tile card hover](components/crops/tile-card-hover.png)

#### About page title
The h1 on /about. Read as `about-title` on the www.airtable.com/about page.

**Values (default).** size 741.97 x 55.19; background transparent; text ATSeasonSans 48/55.2 500, #181d26 `primitive-neutrals-black`.

![About page title default](components/crops/about-title-default.png)

#### About page card
A card on the about page (values, offices, news). Read as `about-card` on the www.airtable.com/about page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1342 x 116.19; border T: 1px solid #e0dcdb `primitive-warm-gray-300`; background transparent; text ATSeasonSans 18/24.3 600, #181d26 `primitive-neutrals-black` |

![About page card default](components/crops/about-card-default.png) ![About page card hover](components/crops/about-card-hover.png)

#### Resource card
A card in the "Resources to inspire" row (Builders & Breakthroughs). Read as `resource-card` on the www.airtable.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 906.66 x 427; padding 24px 0px 0px 0px; radius 32px; background #fcab79; text Haas 32/40 500, #aa2d00 |

![Resource card default](components/crops/resource-card-default.png) ![Resource card hover](components/crops/resource-card-hover.png)

#### Carousel control
A round control of the home feature carousel (the pause or next button). Read as `carousel-control` on the www.airtable.com home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid transparent; radius 9999px; background #181d26 `primitive-neutrals-black`; text Haas 20/0 400, #ffffff `primitive-neutrals-white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ffffff `primitive-neutrals-white` |
| hover | background rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5` |
| focus-visible | shadow #0768f8 0px 0px 0px 2px |
| pressed | background rgba(2, 13, 32, 0.43) |

![Carousel control default](components/crops/carousel-control-default.png) ![Carousel control hover](components/crops/carousel-control-hover.png) ![Carousel control focus-visible](components/crops/carousel-control-focus-visible.png) ![Carousel control pressed](components/crops/carousel-control-pressed.png)

### Cards and indexes

The index pages: /templates (search + filter rail + card gallery), /marketplace (coloured category tiles + extension rows), /whatsnew (an embedded Airtable gallery - the release cards and 'Available on' filters live inside airtable.com/embed), /customer-stories, /solutions, /about.

#### Customer stories title
Read as `story-card-title` on the www.airtable.com/customer-stories page.

**Values (default).** size 766.38 x 40; background transparent; text Haas 32/40 400, #41454d; transition all 0.25s ease-in.

![Customer stories title default](components/crops/story-card-title-default.png)

#### Story row
Story row: a linked customer story row on the index. Read as `story-card` on the www.airtable.com/customer-stories page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 876 x 492.75; background transparent; text Haas 14/18.9 500, rgba(255, 255, 255, 0.8); transition transform 0.15s ease-in; icon 20 x 20, rgba(255, 255, 255, 0.8) |
| hover | size 902.28 x 507.53; transform scale(1.03); icon 20.6 x 20.6, rgba(255, 255, 255, 0.8) |

Child layers that carry the look: div 876x492.8 background #ffffff `primitive-neutrals-white` radius 20px; div 876x492.8 background #000000 radius 20px; div 0x0 background rgba(24, 29, 38, 0.8).

![Story row default](components/crops/story-card-default.png) ![Story row hover](components/crops/story-card-hover.png)

#### Templates title
The "Templates" h1. Read as `templates-title` on the www.airtable.com/templates page.

**Values (default).** size 1120 x 80; background transparent; text Haas Groot Disp 64/80 700, #101828.

![Templates title default](components/crops/templates-title-default.png)

#### Template search field
The "Search templates" field in the filter rail. Focused, nothing typed. Read as `templates-search` on the www.airtable.com/templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 36; padding 6px 12px 6px 32px; radius 3.35544e+07px; background transparent; shadow rgba(0, 0, 0, 0.13) 0px 0px 0px 1px, rgba(0, 0, 0, 0.13) 0px 1px 2px 0px; text Haas Groot Disp 18/24 400, #333333; placeholder rgba(51, 51, 51, 0.5) |
| focused | shadow rgba(0, 0, 0, 0.25) 0px 0px 0px 2px, rgba(0, 0, 0, 0.13) 0px 1px 2px 0px |

![Template search field default](components/crops/templates-search-default.png) ![Template search field focused](components/crops/templates-search-focused.png)

#### Filter section
A collapsible filter group in the templates rail (By Use Case / By Industry / By Feature). Read as `filter-section` on the www.airtable.com/templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 224 x 27.23; background transparent; text Haas Groot Disp 14.8/19.24 700, #9ca3af; icon 14 x 14, #9ca3af |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Filter section default](components/crops/filter-section-default.png) ![Filter section hover](components/crops/filter-section-hover.png) ![Filter section focus-visible](components/crops/filter-section-focus-visible.png)

#### Filter section, open
The filter group clicked open; a local expand. Read as `filter-section-open` on the www.airtable.com/templates page.

**Values (default).** size 224 x 286.92; background transparent; text Haas Groot Disp 14.8/19.24 700, #9ca3af; icon 14 x 14, #9ca3af.

![Filter section, open default](components/crops/filter-section-open-default.png)

#### Marketplace title
The "Marketplace" h1. Read as `marketplace-title` on the www.airtable.com/marketplace page.

**Values (default).** size 622.59 x 35; background transparent; text GT Eesti Display 28/35 500, #1d1f25.

![Marketplace title default](components/crops/marketplace-title-default.png)

#### Marketplace search field
The "Find an extension" field. Focused, nothing typed. Read as `marketplace-search` on the www.airtable.com/marketplace page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 280 x 24; padding 1px 2px 1px 12px; background transparent; text GT Eesti Display 19.2/normal 400, #1d1f25; placeholder #757575 |

![Marketplace search field default](components/crops/marketplace-search-default.png) ![Marketplace search field focused](components/crops/marketplace-search-focused.png)

#### Marketplace category card
A category card on the marketplace ("For marketing teams", "Page designer", "Scripting"). Read as `market-card` on the www.airtable.com/marketplace page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 373.33 x 279.98; padding 0px 0px 279.984px 0px; radius 12px; background transparent; image url(…); text -apple-system 12.8/16 400, #1d1f25; transition all 0.085s ease-in |
| hover | shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 5px |

![Marketplace category card default](components/crops/market-card-default.png) ![Marketplace category card hover](components/crops/market-card-hover.png)

#### Marketplace CTA
A "View all …" button in the marketplace. Measured and focused, never followed. Read as `market-cta` on the www.airtable.com/marketplace page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 108.23 x 32; padding 1px 12px; radius 6px; background #ffffff `primitive-neutrals-white`; shadow rgba(0, 0, 0, 0.32) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 2px 0px, rgba(0, 0, 0, 0.08) 0px 1px 3px 0px; text GT Eesti Display 13/22 400, #166ee1 |
| hover | shadow rgba(0, 0, 0, 0.32) 0px 0px 1px 0px, rgba(0, 0, 0, 0.11) 0px 0px 3px 0px, rgba(0, 0, 0, 0.12) 0px 1px 4px 0px |
| focus-visible | outline 2px solid #166ee1, offset 2px |
| pressed | shadow rgba(0, 0, 0, 0.32) 0px 0px 1px 0px, rgba(0, 0, 0, 0.11) 0px 0px 3px 0px, rgba(0, 0, 0, 0.12) 0px 1px 4px 0px |

![Marketplace CTA default](components/crops/market-cta-default.png) ![Marketplace CTA hover](components/crops/market-cta-hover.png) ![Marketplace CTA focus-visible](components/crops/market-cta-focus-visible.png) ![Marketplace CTA pressed](components/crops/market-cta-pressed.png)

#### Template card
A template tile in the gallery (the "Project Management" use-case tiles and the featured cards below). Read as `template-card` on the www.airtable.com/templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 215; radius 32px; background transparent; image linear-gradient(to right bottom, #faf5ff, #ede9fe); shadow rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px; text Haas Groot Disp 20/27.5 600, #101828; transition box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | shadow rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.1) 0px 2px 4px -2px |

![Template card default](components/crops/template-card-default.png) ![Template card hover](components/crops/template-card-hover.png)

#### What's new title
The "Where Airtable is headed." heading. Read as `whatsnew-title` on the www.airtable.com/whatsnew page.

**Values (default).** size 459.33 x 94.16; background transparent; text Haas 44/47.08 550, #161616.

![What's new title default](components/crops/whatsnew-title-default.png)

#### What's new card
A release card in the embedded roadmap gallery (plan chips and a release-month chip), inside airtable.com/embed/appL2oaKxSWg9qz8y. Read as `whatsnew-item` on the www.airtable.com/whatsnew page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 387 x 565; radius 6px; background #ffffff `primitive-neutrals-white`; shadow rgba(0, 0, 0, 0.24) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 2px 0px, rgba(0, 0, 0, 0.08) 0px 2px 4px 0px; text Inter Display 17/25.5 675, #1d1f25 |
| hover | shadow rgba(0, 0, 0, 0.24) 0px 0px 1px 0px, rgba(0, 0, 0, 0.16) 0px 0px 2px 0px, rgba(0, 0, 0, 0.06) 0px 3px 4px 0px, rgba(0, 0, 0, 0.06) 0px 6px 8px 0px, rgba(0, 0, 0, 0.08) 0px 12px 16px 0px, rgba(0, 0, 0, 0.06) 0px 18px 32px 0px |

![What's new card default](components/crops/whatsnew-item-default.png) ![What's new card hover](components/crops/whatsnew-item-hover.png)

#### What's new filter
An "Available on" / "Release month" filter dropdown in the embedded release gallery. Measured and focused, never opened. Read as `whatsnew-filter` on the www.airtable.com/whatsnew page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112.22 x 28; padding 0px 0px 0px 8px; radius 6px; background #ffffff `primitive-neutrals-white`; shadow rgba(0, 0, 0, 0.32) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 2px 0px, rgba(0, 0, 0, 0.08) 0px 1px 3px 0px; text -apple-system 13/22 400, #1d1f25; icon 16 x 16, #1d1f25 |
| hover | shadow rgba(0, 0, 0, 0.32) 0px 0px 1px 0px, rgba(0, 0, 0, 0.11) 0px 0px 3px 0px, rgba(0, 0, 0, 0.12) 0px 1px 4px 0px |
| focus-visible | outline 2px solid #166ee1, offset 0px |

![What's new filter default](components/crops/whatsnew-filter-default.png) ![What's new filter hover](components/crops/whatsnew-filter-hover.png) ![What's new filter focus-visible](components/crops/whatsnew-filter-focus-visible.png)

### Platform pages

/platform and /platform/ai: the ATSeasonSans display titles, the 'Ways to start building' linked cards, the customer-stories carousel on the dark band (pause + prev/next arrows), and the FAQ accordion.

#### Platform page title
The h1 on https://www.airtable.com/platform. Read as `platform-title` on the www.airtable.com/platform page.

**Values (default).** size 1184 x 174.22; background transparent; text ATSeasonSans 79.2/87.12 550, #161616.

![Platform page title default](components/crops/platform-title-default.png)

#### Platform CTA
A primary button on the platform page. Measured and focused, never followed. Read as `platform-cta` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 131.8 x 47.59; padding 12px 24px; border 1px solid #161616; radius 4px; background #ffffff `primitive-neutrals-white`; text ATSeasonSans 16/21.6 650, #161616; transition background-color 0.15s ease, color 0.15s ease, border-color 0.15s ease |
| hover | background #f5f5f5 |
| focus-visible | background #f5f5f5; outline 2px solid #161616, offset 2px |
| pressed | background #f5f5f5 |

![Platform CTA default](components/crops/platform-cta-default.png) ![Platform CTA hover](components/crops/platform-cta-hover.png) ![Platform CTA focus-visible](components/crops/platform-cta-focus-visible.png) ![Platform CTA pressed](components/crops/platform-cta-pressed.png)

#### Platform feature card
A linked card on /platform (a "Ways to start building with agents" tile). Read as `platform-card` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 670 x 540.97; background #ffffff `primitive-neutrals-white`; text ATSeasonSans 24/31.2 550, #161616; transition background-color 0.15s ease; icon 16 x 16, #161616 |
| hover | background #f8f6f6 `primitive-warm-gray-100` |

![Platform feature card default](components/crops/platform-card-default.png) ![Platform feature card hover](components/crops/platform-card-hover.png)

#### Feature tab list
The vertical tab strip ("Data that fits your business": Shared data, Durable workflows, Open surfaces, Governance). Read as `feature-tablist` on the www.airtable.com/platform page.

**Values (default).** size 425 x 700; background #ffffff `primitive-neutrals-white`; text ATSeasonSans 16/21.6 650, #181d26 `primitive-neutrals-black`.

![Feature tab list default](components/crops/feature-tablist-default.png)

#### Feature tab
One segment of the feature tab strip. Read as `feature-tab` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 425 x 80.19; padding 24px 40px; border B: 1px solid #181d26 `primitive-neutrals-black`; background #ffffff `primitive-neutrals-white`; text ATSeasonSans 24/31.2 550, #181d26 `primitive-neutrals-black` |
| focus-visible | outline 2px solid #161616, offset -2px |

![Feature tab default](components/crops/feature-tab-default.png) ![Feature tab hover](components/crops/feature-tab-hover.png) ![Feature tab focus-visible](components/crops/feature-tab-focus-visible.png) ![Feature tab pressed](components/crops/feature-tab-pressed.png)

#### Feature tab, selected
The selected segment of the tab strip. Read as `feature-tab-active` on the www.airtable.com/platform page.

**Values (default).** size 425 x 80.19; padding 24px 40px; border B: 1px solid #181d26 `primitive-neutrals-black`; background #ffffff `primitive-neutrals-white`; text ATSeasonSans 24/31.2 550, #181d26 `primitive-neutrals-black`.

![Feature tab, selected default](components/crops/feature-tab-active-default.png)

#### Stories previous button
The previous-arrow of the customer-stories carousel, shown after the carousel leaves its first slide. Read as `stories-prev` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid rgba(255, 255, 255, 0.23); radius 50%; background transparent; text Haas 20/30 400, #ffffff `primitive-neutrals-white`; transition background-color 0.15s ease, border-color 0.15s ease; icon 16 x 16, #ffffff `primitive-neutrals-white` |
| hover | border 1px solid rgba(255, 255, 255, 0.5); background rgba(255, 255, 255, 0.08) |
| focus-visible | border 1px solid rgba(255, 255, 255, 0.5); background rgba(255, 255, 255, 0.08); outline 2px solid #ffffff `primitive-neutrals-white`, offset 2px |
| pressed | border 1px solid rgba(255, 255, 255, 0.5); background rgba(255, 255, 255, 0.08) |

![Stories previous button default](components/crops/stories-prev-default.png) ![Stories previous button hover](components/crops/stories-prev-hover.png) ![Stories previous button focus-visible](components/crops/stories-prev-focus-visible.png) ![Stories previous button pressed](components/crops/stories-prev-pressed.png)

#### Stories next button
The next-arrow of the customer-stories carousel. Read as `stories-next` on the www.airtable.com/platform page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid rgba(255, 255, 255, 0.23); radius 50%; background transparent; text Haas 20/30 400, #ffffff `primitive-neutrals-white`; transition background-color 0.15s ease, border-color 0.15s ease; icon 16 x 16, #ffffff `primitive-neutrals-white` |
| hover | border 1px solid rgba(255, 255, 255, 0.5); background rgba(255, 255, 255, 0.08) |
| focus-visible | border 1px solid rgba(255, 255, 255, 0.5); background rgba(255, 255, 255, 0.08); outline 2px solid #ffffff `primitive-neutrals-white`, offset 2px |
| pressed | border 1px solid rgba(255, 255, 255, 0.5); background rgba(255, 255, 255, 0.08) |

![Stories next button default](components/crops/stories-next-default.png) ![Stories next button hover](components/crops/stories-next-hover.png) ![Stories next button focus-visible](components/crops/stories-next-focus-visible.png) ![Stories next button pressed](components/crops/stories-next-pressed.png)

#### Stories pause button
The pause-autoplay button of the customer-stories carousel; measured and focused, never pressed. Read as `stories-pause` on the www.airtable.com/platform/ai page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; border 1px solid transparent; radius 9999px; background #181d26 `primitive-neutrals-black`; text Haas 20/0 400, #ffffff `primitive-neutrals-white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ffffff `primitive-neutrals-white` |
| hover | background rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5` |
| focus-visible | shadow #0768f8 0px 0px 0px 2px |

![Stories pause button default](components/crops/stories-pause-default.png) ![Stories pause button hover](components/crops/stories-pause-hover.png) ![Stories pause button focus-visible](components/crops/stories-pause-focus-visible.png)

#### Platform page title
The h1 on https://www.airtable.com/platform/ai. Read as `platform-ai-title` on the www.airtable.com/platform/ai page.

**Values (default).** size 884 x 110.38; background transparent; text ATSeasonSans 48/55.2 500, #181d26 `primitive-neutrals-black`.

![Platform page title default](components/crops/platform-ai-title-default.png)

#### Platform CTA
A primary button on the platform page. Measured and focused, never followed. Read as `platform-ai-cta` on the www.airtable.com/platform/ai page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 131.42 x 47.59; padding 12px 24px; border 1px solid #181d26 `primitive-neutrals-black`; radius 4px; background transparent; text ATSeasonSans 16/21.6 600, #181d26 `primitive-neutrals-black`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(242, 244, 247, 0.92) |
| focus-visible | background rgba(242, 244, 247, 0.92); shadow #0768f8 0px 0px 0px 2px |
| pressed | background rgba(242, 244, 247, 0.92) |

![Platform CTA default](components/crops/platform-ai-cta-default.png) ![Platform CTA hover](components/crops/platform-ai-cta-hover.png) ![Platform CTA focus-visible](components/crops/platform-ai-cta-focus-visible.png) ![Platform CTA pressed](components/crops/platform-ai-cta-pressed.png)

#### Solutions page title
Read as `solutions-card-title` on the www.airtable.com/solutions page.

**Values (default).** size 620.73 x 48; background transparent; text Haas 40/48 400, #333840; transition all 0.25s ease-in.

![Solutions page title default](components/crops/solutions-card-title-default.png)

#### Solutions card
Solutions card: a team tile in the solutions grid (Marketing teams, Product teams, ...). Read as `solutions-card` on the www.airtable.com/solutions page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 437.33 x 207.59; padding 24px; border 1px solid #e0e2e6; radius 16px; background #ffffff `primitive-neutrals-white`; text Haas 16/21.6 500, #181d26 `primitive-neutrals-black`; icon 16 x 12, #0768f8 `primitive-ui-link-2` |

![Solutions card default](components/crops/solutions-card-default.png) ![Solutions card hover](components/crops/solutions-card-hover.png)

#### Enterprise page title
Read as `enterprise-card-title` on the www.airtable.com/solutions/enterprise page.

**Values (default).** size 1184 x 174.22; background transparent; text ATSeasonSans 79.2/87.12 550, #161616.

![Enterprise page title default](components/crops/enterprise-card-title-default.png)

#### Enterprise card
Enterprise card: a linked capability card on the enterprise page. Read as `enterprise-card` on the www.airtable.com/solutions/enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 335.5 x 351; border T: 1px solid #e0dcdb `primitive-warm-gray-300`; B: 1px solid #e0dcdb `primitive-warm-gray-300`; background transparent; text ATSeasonSans 24/31.2 550, #181d26 `primitive-neutrals-black`; icon 16 x 16, #161616 |

![Enterprise card default](components/crops/enterprise-card-default.png) ![Enterprise card hover](components/crops/enterprise-card-hover.png)

#### FAQ item
An accordion question in the "You have questions? We have answers." section. Read as `faq-item` on the www.airtable.com/platform/ai page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 814 x 32; background transparent; text ATSeasonSans 16/21.6 600, #181d26 `primitive-neutrals-black`; icon 32 x 32, #9297a0 `primitive-gray-brand` |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item hover](components/crops/faq-item-hover.png)

#### FAQ item, open
The same accordion item clicked open; a local expand. Read as `faq-item-open` on the www.airtable.com/platform/ai page.

**Values (default).** size 814 x 110.78; padding 0px 0px 24px 0px; border B: 1px solid #e0dcdb `primitive-warm-gray-300`; background transparent; text ATSeasonSans 16/21.6 600, #181d26 `primitive-neutrals-black`; icon 32 x 32, #9297a0 `primitive-gray-brand`.

Child layers that carry the look: div 814x110.8 border 1px solid #e0dcdb `primitive-warm-gray-300`.

![FAQ item, open default](components/crops/faq-item-open-default.png)

#### Platform AI card
A card of the "Add AI to your workflows" grid on /platform/ai ("Generate high-impact campaign concepts"). Read as `platform-ai-card` on the www.airtable.com/platform/ai page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 447.33 x 224.97; border R: 1px solid #e0dcdb `primitive-warm-gray-300`; background #f8f6f6 `primitive-warm-gray-100`; text ATSeasonSans 18/24.3 600, #181d26 `primitive-neutrals-black` |

![Platform AI card default](components/crops/platform-ai-card-default.png) ![Platform AI card hover](components/crops/platform-ai-card-hover.png)

### Pricing

www.airtable.com/pricing (in Inter Display, not Haas): the Free/Team/Business/Enterprise Scale plan columns with 2px-bordered CTAs, and the 'Compare our plans' div grid of hover-container feature rows.

#### Pricing title
The "A plan for every organization's needs" h1. Read as `pricing-title` on the www.airtable.com/pricing page.

**Values (default).** size 1250 x 55.98; background transparent; text Inter Display 44.8/56 475, #1d1f25.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan CTA
A button inside a plan card ("Contact Sales" pill). Measured and focused, never followed. Read as `plan-cta` on the www.airtable.com/pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 246.5 x 56; padding 16px; border 2px solid #1d1f25; radius 9999px; background #ffffff `primitive-neutrals-white`; text Inter Display 16/20 575, #1d1f25 |
| hover | background #f2f4f8 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #f2f4f8 |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### See more link
The "See more" / "See all features and compare plans" expander. Measured, never followed. Read as `plan-see-more` on the www.airtable.com/pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 211.19 x 25.59; background transparent; text Haas 16/21.6 500, #1d1f25 |

Child layers that carry the look: a 75.5x25.6 border 2px solid transparent.

![See more link default](components/crops/plan-see-more-default.png) ![See more link hover](components/crops/plan-see-more-hover.png) ![See more link focus-visible](components/crops/plan-see-more-focus-visible.png) ![See more link pressed](components/crops/plan-see-more-pressed.png)

#### Pricing FAQ item
An accordion question in the pricing FAQ ("How does Airtable's pricing work?"). Read as `pricing-faq-item` on the www.airtable.com/pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 768 x 25.5; background transparent; text Inter Display 17/25.5 575, #1d1f25; icon 16 x 16, #1d1f25 |

![Pricing FAQ item default](components/crops/pricing-faq-item-default.png) ![Pricing FAQ item hover](components/crops/pricing-faq-item-hover.png)

#### Pricing FAQ item, open
The same accordion item clicked open; a local expand. Read as `pricing-faq-item-open` on the www.airtable.com/pricing page.

**Values (default).** size 768 x 206.73; padding 0px 0px 2.24px 0px; border B: 3px solid rgba(0, 0, 0, 0.1); background transparent; text Inter Display 17/25.5 575, #1d1f25; icon 16 x 16, #1d1f25.

Child layers that carry the look: div 768x206.7 border 3px solid rgba(0, 0, 0, 0.1).

![Pricing FAQ item, open default](components/crops/pricing-faq-item-open-default.png)

#### Plan card
A plan column on the pricing grid (Free, Team $20, Business $45, Enterprise Scale). Read as `plan-card` on the www.airtable.com/pricing page.

**Values (default).** size 296.5 x 454.5; padding 0px 24px 16px 24px; border R: 1px solid #0d52ac; B: 1px solid #0d52ac; L: 1px solid #0d52ac; radius 0px 0px 12px 12px; background rgba(240, 246, 255, 0.5); text Inter Display 16/20 475, #1d1f25; icon 20 x 20, #1d1f25.

![Plan card default](components/crops/plan-card-default.png)

#### Plan comparison table
The "Compare our plans" feature table: a div grid of plan columns against feature rows with checks (measured whole; no <table> element). Read as `compare-table` on the www.airtable.com/pricing page.

**Values (default).** size 1250 x 5329; background transparent; text Inter Display 32/40 475, #1d1f25; icon 24 x 24, #1d1f25.

Child layers that carry the look: div 1250x161 background #ffffff `primitive-neutrals-white`; a 163x56 background #ffffff `primitive-neutrals-white` border 2px solid #1d1f25 radius 9999px; a 163x52 background #166ee1 radius 9999px.

![Plan comparison table default](components/crops/compare-table-default.png)

#### Comparison row
A feature row in the comparison table (a hover-container flex row). Read as `compare-table-row` on the www.airtable.com/pricing page.

**Values (default).** size 1266 x 36; background transparent; text Inter Display 16/20 400, #1d1f25.

Child layers that carry the look: a 41.2x22 border 2px dotted #dddddd.

![Comparison row default](components/crops/compare-table-row-default.png)

### Contact sales form

www.airtable.com/contact-sales: the 430px-wide sales form - text fields, a phone field, a text area, the custom 'Country' combobox and the dark Submit. Measured at rest, focused and filled; never submitted.

#### Contact page title
The "Get in touch with us!" heading over the form. Read as `contact-title` on the www.airtable.com/contact-sales page.

**Values (default).** size 785.33 x 60; background transparent; text Haas 48/60 600, #333333.

![Contact page title default](components/crops/contact-title-default.png)

#### Contact form
The Marketo contact-sales form (a hidden mkto <form> with a visible React fields grid): First/Last name, Work Email, Phone with a country selector, Company Name, Job Title, Country, a message area and Submit. Photographed and focused, never submitted. Read as `contact-form` on the www.airtable.com/contact-sales page.

**Values (default).** size 430.66 x 619.23; background transparent; text Haas 12/18 500, #c2214c; icon 20 x 20, #cccccc.

Child layers that carry the look: div 211.3x56 background #ffffff `primitive-neutrals-white` border 1px solid rgba(0, 14, 38, 0.23) radius 8px; div 211.3x56 background #ffffff `primitive-neutrals-white` border 1px solid rgba(0, 14, 38, 0.23) radius 8px; div 430.7x53.6 background #ffffff `primitive-neutrals-white` border 1px solid rgba(0, 14, 38, 0.23) radius 8px.

![Contact form default](components/crops/contact-form-default.png)

#### Field label
A floating label inside a field of the form ("* First Name"). Read as `field-label` on the www.airtable.com/contact-sales page.

**Values (default).** size 70.33 x 18; background transparent; text Haas 12/18 500, #c2214c; transition all 0.25s ease.

![Field label default](components/crops/field-label-default.png)

#### Text field
A text input in the form (First name). Focused and filled with sample text that was deleted; nothing was sent. Read as `text-field` on the www.airtable.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 185.33 x 21.59; background transparent; text Haas 16/21.6 400, #181d26 `primitive-neutrals-black`; placeholder #181d26 `primitive-neutrals-black` |
| focused, filled | shadow #ffffff 0px 0px 0px 1000px inset |

![Text field default](components/crops/text-field-default.png) ![Text field focused](components/crops/text-field-focused.png) ![Text field filled](components/crops/text-field-filled.png)

#### Text field box
The same field measured at rest (default only). Read as `text-field-box` on the www.airtable.com/contact-sales page.

**Values (default).** size 185.33 x 21.59; background transparent; text Haas 16/21.6 400, #181d26 `primitive-neutrals-black`; placeholder #181d26 `primitive-neutrals-black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Phone field
The phone input beside the country selector. Read as `phone-field` on the www.airtable.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 375.91 x 18.89; padding 0px 0px 0px 8px; radius 0px 4px 4px 0px; background #ffffff `primitive-neutrals-white`; text Haas 14/18.9 400, #222222; placeholder #222222 |
| focused | shadow #ffffff 0px 0px 0px 1000px inset |

![Phone field default](components/crops/phone-field-default.png) ![Phone field focused](components/crops/phone-field-focused.png)

#### Country selector
The phone country combobox button. Measured and focused, never opened (a choice posts a value). Read as `country-selector` on the www.airtable.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 29.75 x 12; radius 4px 0px 0px 4px; background #ffffff `primitive-neutrals-white`; text Haas 20/30 400, #333333 |
| hover | background transparent |
| focus-visible | background transparent; outline 1px auto #005fcc, offset 0px |

![Country selector default](components/crops/country-selector-default.png) ![Country selector hover](components/crops/country-selector-hover.png) ![Country selector focus-visible](components/crops/country-selector-focus-visible.png)

#### Email field
The work-email input. Read as `email-field` on the www.airtable.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 404.66 x 21.59; background transparent; text Haas 16/21.6 400, #181d26 `primitive-neutrals-black`; placeholder #181d26 `primitive-neutrals-black` |
| focused | shadow #ffffff 0px 0px 0px 1000px inset |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png)

#### Text area
The "How can we help?" message textarea. Read as `text-area` on the www.airtable.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 398.66 x 48; background transparent; text Haas 16/24 400, #333840; placeholder #333840 |

![Text area default](components/crops/text-area-default.png) ![Text area focused](components/crops/text-area-focused.png)

#### Select field
The "Country" dropdown in the form (a custom combobox, not a native select). Measured at rest; never submitted. Read as `select-field` on the www.airtable.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 430.66 x 56.59; background transparent; text Haas 20/30 400, #c2214c; icon 20 x 20, #cccccc |

Child layers that carry the look: div 430.7x56.6 border 1px solid rgba(0, 14, 38, 0.23) radius 8px.

![Select field default](components/crops/select-field-default.png) ![Select field hover](components/crops/select-field-hover.png)

#### Select field, open
The Country dropdown clicked open; a local disclosure, nothing chosen. Read as `select-field-open` on the www.airtable.com/contact-sales page.

**Values (default).** size 430.66 x 300; radius 4px; background #ffffff `primitive-neutrals-white`; shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 4px 11px 0px; text Haas 16/24 400, #333333.

![Select field, open default](components/crops/select-field-open-default.png)

#### Submit button
The dark "Submit" of the sales form. Measured and focused, never pressed. Read as `submit-button` on the www.airtable.com/contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 430.66 x 55.59; padding 16px 24px; border 1px solid #181d26 `primitive-neutrals-black`; radius 12px; background #181d26 `primitive-neutrals-black`; shadow rgba(0, 0, 0, 0.32) 0px 0px 1px 0px, rgba(0, 0, 0, 0.08) 0px 0px 2px 0px, rgba(45, 127, 249, 0.28) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 0px 0px 0.5px inset; text Haas 16/21.6 500, #ffffff `primitive-neutrals-white`; transition all 0.2s linear |
| hover | border 1px solid rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`; background rgba(4, 14, 32, 0.69) `primitive-opacity-darken-5`; shadow none |
| focus-visible | shadow rgba(153, 160, 174, 0.16) 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px |

![Submit button default](components/crops/submit-button-default.png) ![Submit button hover](components/crops/submit-button-hover.png) ![Submit button focus-visible](components/crops/submit-button-focus-visible.png)

### Mobile (390 wide)

www.airtable.com at 390: the collapsed nav bar, the menu button and the side sheet it opens.

#### Top navigation bar (mobile)
The header at 390: wordmark and menu button. Read as `m-nav-bar` on the www.airtable.com home page at 390 wide.

**Values (default).** size 390 x 143.69; background transparent; text Haas 14/17.5 400, #333840; transition all 0.15s ease-in; icon 18 x 12, #254fad.

Child layers that carry the look: nav 390x143.7 background #ffffff `primitive-neutrals-white` shadow rgba(15, 48, 106, 0.05) 0px 0px 20px 0px; div 390x67.7 background #f0f6ff; a 88.3x18.2 radius 10px.

![Top navigation bar (mobile) default](components/crops/m-nav-bar-default.png)

#### Nav menu button (mobile)
The "Open side menu" button in the mobile header. Opened for the screenshot; nothing is followed. Read as `m-nav-menu-btn` on the www.airtable.com home page at 390 wide.

**Values (default).** size 32 x 32; radius 6px; background transparent; text Haas 20/25 400, #181d26 `primitive-neutrals-black`.

Child layers that carry the look: span 24x2 background #181d26 `primitive-neutrals-black` radius 6px; span 24x2 background #181d26 `primitive-neutrals-black` radius 6px.

![Nav menu button (mobile) default](components/crops/m-nav-menu-btn-default.png)

#### Mobile nav sheet
The side drawer the "Open side menu" button opens at 390. Read as `m-nav-sheet` on the www.airtable.com at 390 page at 390 wide.

Not on the page when it was captured.

#### Hero title (mobile)
The h1 at 390. Read as `m-hero-title` on the www.airtable.com home page at 390 wide.

**Values (default).** size 342 x 120; background transparent; text Haas 32/40 400, #333840; transition all 0.25s ease-in.

![Hero title (mobile) default](components/crops/m-hero-title-default.png)

## Gaps

### Pages

- **The products.** app.airtable.com is the signed-in product: nothing behind Sign up, Log in or Book Demo was captured - the workspace, base editor, interfaces, automations and billing are all missing. The kit never signs in, registers, or books a demo.
- **Checkout and account.** The plan CTAs and the contact-sales form lead to flows that were never submitted; no purchase was made and no field was filled with real contact details.
- **Page-depth pages.** The index pages were captured; individual templates, marketplace extensions and customer stories were not opened.
- **Embedded content.** whatsnew's release gallery is Airtable's own published interface served in an iframe (airtable.com/embed/appL2oaKxSWg9qz8y); cards and filters were measured inside it.
- **Third-party widgets.** The Qualified 'Riley' chat launcher and Google One Tap are swept out of every capture; they are not Airtable design system components.
- **Consent.** The 'Privacy choices' footer control opens consent settings; it was never opened because answering it is a submission.

### Themes

The site ships one theme: no dark values are declared and nothing changed under prefers-color-scheme (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file has no `dark` set - that is a documented gap, not an omission.

### Fonts

- **Haas** (Neue Haas Grotesk) is the body face and **Haas Groot Disp** the display face on most pages; **ATSeasonSans** carries the nav and platform-page headlines; **Inter Display** typesets /pricing and **GT Eesti Display** /marketplace. All are commercial faces served from Airtable's hosts (see fontFaces in [raw/css-vars.json](raw/css-vars.json)) - not redistributable; the style guide stands in with system faces.

### Screenshots

- People, logos and product imagery are Airtable's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Page prose was not transcribed into the package; the components around it were measured.
- No personal data was captured: the pages were read signed out, and no form was filled with real contact details.

