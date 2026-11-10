# apollographql components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from apollographql.com on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was bought, downloaded, signed into, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (55 components, 143 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Aeonik 60/63 400, #ffffff`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (143 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`: the marketing pages paint dark (`home`, `graphos`, `agent-services`, `pricing`, `customers`, `why-apollo`), the blog and contact-sales intro paint light, and the Studio auth pages are `login`/`signup` light. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x). The app host studio.apollographql.com rendered its login and signup pages, which were captured at rest and never submitted, so every authenticated surface is a recorded boundary, not captured.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Eyebrow strip, space-dark hero, conic-ring CTA, alternating dark/light sections; consent banner, open Products menu and full page. | `/` | [cookie-banner](screenshots/home-dark-cookie-banner.png), [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [nav-products-open](screenshots/home-dark-nav-products-open.png) |
| Graphos. The platform product page, dark bands alternating with white; full page. | `/graphos` | [default](screenshots/graphos-dark-default.png), [full](screenshots/graphos-dark-full.png) |
| Graphos Agent Services. The product page, dark bands alternating with white; full page. | `/graphos-agent-services` | [default](screenshots/agent-services-dark-default.png), [full](screenshots/agent-services-dark-full.png) |
| Pricing. Tier/billing segments, plan cards, stats and FAQ cards, promo banner; billing-toggle state and full page. | `/pricing` | [billing-toggle](screenshots/pricing-dark-billing-toggle.png), [default](screenshots/pricing-dark-default.png), [full](screenshots/pricing-dark-full.png) |
| Customers. Title, orange CTA pair, stats band, story cards; full page. | `/customers` | [default](screenshots/customers-dark-default.png), [full](screenshots/customers-dark-full.png) |
| Blog. "What's new" index on the light surface, satellite and regolith cards; full page. | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Why Apollo. The positioning page, alternating dark/light bands; full page. | `/why-apollo` | [default](screenshots/why-apollo-dark-default.png), [full](screenshots/why-apollo-dark-full.png) |
| Contact sales. Light intro, the navy HubSpot form band; form-fields state and full page. | `/contact-sales` | [default](screenshots/contact-sales-light-default.png), [form-fields](screenshots/contact-sales-light-form-fields.png), [full](screenshots/contact-sales-light-full.png) |
| Studio login. The app's sign-in page, captured at rest — never submitted. | `studio.apollographql.com/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Studio signup. The app's sign-up page, captured at rest — never submitted. | `studio.apollographql.com/signup` | [default](screenshots/signup-light-default.png), [full](screenshots/signup-light-full.png) |
| Home at 390: burger, 36px hero, full-width CTAs; consent banner and full page. | `/` | [cookie-banner](screenshots/mobile-home-dark-cookie-banner.png), [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png) |
| Pricing at 390; full page. | `/pricing` | [default](screenshots/mobile-pricing-dark-default.png), [full](screenshots/mobile-pricing-dark-full.png) |
| Contact sales at 390; full page. | `/contact-sales` | [default](screenshots/mobile-contact-sales-light-default.png), [full](screenshots/mobile-contact-sales-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | home | the OneTrust card allowed to mount and captured; hidden by CSS afterwards — never answered | [home-dark-cookie-banner](screenshots/home-dark-cookie-banner.png), [cookie-card](#cookie-consent-card) |
| Products menu | home nav | the Products disclosure pressed (a local menu open, no navigation) | [home-dark-nav-products-open](screenshots/home-dark-nav-products-open.png), [nav-menu](#products-menu) |
| Billing toggle | pricing | the Monthly/Yearly segment pressed (client-side state, nothing sent) | [pricing-dark-billing-toggle](screenshots/pricing-dark-billing-toggle.png) |
| Contact form fields | contact-sales | fields clicked into and typed in, then cleared; the form was never submitted | [contact-sales-light-form-fields](screenshots/contact-sales-light-form-fields.png), [field](#text-field) |
| Studio auth pages | studio.apollographql.com | login/signup loaded signed out and captured at rest | [login-light-default](screenshots/login-light-default.png), [signup-light-default](screenshots/signup-light-default.png) — never submitted |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 27 components were given a real keyboard focus. 23 draw a ring: `logo` (2px solid #ff7b3c `focus-orange`, offset 2px), `nav-trigger` (2px solid #ff7b3c `focus-orange`, offset 2px), `nav-cta` (2px solid #ff7b3c `focus-orange`, offset 2px), `nav-search` (1px solid #f8f8f8 `offwhite`, offset 8px), `cta-primary` (2px solid #2fd1e0 `focus-cyan`, offset 4px), `cta-secondary` (2px solid #2fd1e0 `focus-cyan`, offset 4px), `pause-motion` (2px solid #e75e15 `brand-accent`, offset 2px), `text-link` (2px solid #e75e15 `brand-accent`, offset 4px), `link-pill` (2px solid #e75e15 `brand-accent`, offset 4px), `video-card` (2px solid #e75e15 `brand-accent`, offset -4px), `copy-row` (2px solid #666666 `content-muted`, offset 4px), `carousel-arrow` (2px solid #e75e15 `brand-accent`, offset 2px), `footer-link` (1px auto #99c8ff `focus-blue`, offset 1px), `social-link` (1px auto #99c8ff `focus-blue`, offset 1px), `tier-segment` (5px auto #99c8ff `focus-blue`, offset 0px), `billing-segment` (5px auto #99c8ff `focus-blue`, offset 0px), `volume-pill-on` (2px solid #f8f8f8 `offwhite`, offset 2px), `volume-pill` (2px solid #f8f8f8 `offwhite`, offset 2px), `plan-cta` (2px solid #ff7b3c `focus-orange`, offset 2px), `cta-orange` (2px solid #e75e15 `brand-accent`, offset 8px), `cta-orange-outline` (2px solid #e75e15 `brand-accent`, offset 8px), `pagination` (5px auto #99c8ff `focus-blue`, offset 0px), `submit` (2px solid #e75e15 `brand-accent`, offset 8px). The other 4 draw none, so a keyboard user sees no change: `faq-item`, `story-card`, `article-card`, `article-card-regolith`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). The filled orange pills darken to #d84f08 — the same colour the hover draws — and the ghost pills pick up the translucent hover fill; see the per-component state rows.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.12s | `ease` | background-color, border-color | cookie-accept |
| 0.15s | `cubic-bezier(0.17, 0.17, 0, 1)` | transform | social-link |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | cta-orange, cta-orange-outline, cta-primary, cta-secondary, link-pill, m-burger, m-cta-primary, m-cta-secondary and more |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | height | nav-menu |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | billing-segment, tier-segment, volume-pill, volume-pill-on |
| 0.2s | `ease` | background-color | submit |
| 0.3s | `cubic-bezier(0.06, 0.47, 0.1, 1)` | background-color, opacity | article-card-regolith, pagination, pagination-on |
| 0.3s | `cubic-bezier(0.17, 0.17, 0, 1)` | background-color, border-color, color, rotate, scale, transform, translate | m-nav-bar, nav-bar, nav-search, social-link |
| 0.3s | `cubic-bezier(0.23, 0.4, 0.53, 0.88)` | border-color | field, field-filled, select, textarea |
| 0.5s | `cubic-bezier(0.06, 0.47, 0.1, 1)` | transform | article-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Nav bar](#nav-bar) | 1440 x 65 | 1px solid #e75e15 `brand-accent` | 999px | #e75e15 `brand-accent` | none | 0 |
| [Cookie consent card](#cookie-consent-card) | 760 x 188.56 | 1px solid #e3e7ea | 16px | #ffffff `white` | rgba(21, 37, 45, 0.14) 0px 12px 32px 0px, rgba(21, 37, 45, 0.06) 0px 2px 6px 0px | 20px 20px 18px 20px |
| [Stats band card](#stats-band-card) | 1344 x 669.5 | - | 32px | #15252d `nebula` | none | 94px 80px |
| [FAQ card](#faq-card) | 1344 x 612.5 | - | 32px | #e3e3e3 `faq-gray` | none | 72px |
| [Promo banner](#promo-banner) | 1344 x 264.53 | - | 32px | #15252d `nebula` | none | 40px |
| [Stats band](#stats-band) | 1344 x 332 | - | 32px | #15252d `nebula` | none | 0 |
| [Story card](#story-card) | 432 x 584.5 | - | 32px | #f8f8f8 `offwhite` | none | 0 |
| [Article card (satellite)](#article-card-satellite) | 444 x 298.81 | - | 32px | #cfd7d6 `satellite-dark` | none | 0 |
| [Article card (regolith)](#article-card-regolith) | 672 x 209.39 | - | 32px | #ffffff `white` | none | 0 |
| [Video card](#video-card) | 520 x 292.5 | - | 24px | #15252d `nebula` | none | 0 |
| [Footer](#footer) | 1440 x 627.47 | 1px solid transparent | 999px | #e75e15 `brand-accent` | none | 0 |

## Components

### Shell and navigation

The chrome on the public pages: the Summit eyebrow strip, the sticky transparent nav over the dark hero (Apollo wordmark left, Products/Solutions/Resources/Company disclosures centre, search icon and the Start-for-free orange pill right), the Products dropdown menu, the footer band, and the OneTrust consent card (captured, never answered).

#### Cookie consent card
The OneTrust bottom-left card (white, 16px radius, double shadow): copy, Accept All / Decline Non-Necessary / Manage Preferences buttons. Read as `cookie-card` on the home page.

**Values (default).** size 760 x 188.56; padding 20px 20px 18px 20px; border 1px solid #e3e7ea; radius 16px; background #ffffff `white`; shadow rgba(21, 37, 45, 0.14) 0px 12px 32px 0px, rgba(21, 37, 45, 0.06) 0px 2px 6px 0px; text __interFont_b14d2f 13/20.15 400, #3d4a52.

![Cookie consent card default](components/crops/cookie-card-default.png)

#### Cookie Accept button
The dark pill inside the OneTrust card. Measured, never clicked. Read as `cookie-accept` on the home page.

**Values (default).** size 222.22 x 32; padding 0px 12px; border 1px solid #15252d `nebula`; radius 999px; background #15252d `nebula`; text __interFont_b14d2f 12.5/12.5 600, #ffffff `white`; transition background-color 0.12s ease, border-color 0.12s ease.

![Cookie Accept button default](components/crops/cookie-accept-default.png)

#### Summit eyebrow
The "Apollo Summit 2026 keynote available / Watch keynote" strip above the nav, with its own close. Read as `eyebrow` on the home page.

**Values (default).** size 1440 x 55; padding 10px 48px; background #1a1a1a `eyebrow`; text Aeonik 18/18 700, #ffffff `white`; icon 10 x 12, #000000.

![Summit eyebrow default](components/crops/eyebrow-default.png)

#### Nav bar
The sticky transparent header over the dark hero: logo, Products/Solutions/Resources/Company disclosures, Pricing and Contact us links, search, Start for free pill. Read as `nav-bar` on the home page.

**Values (default).** size 1440 x 65; background transparent; text __interFont_b14d2f 15/22.5 500, oklab(0.999994 0.0000455678 0.0000200868 / 0.72); transition transform 0.3s cubic-bezier(0.17, 0.17, 0, 1), translate 0.3s cubic-bezier(0.17, 0.17, 0, 1), scale 0.3s cubic-bezier(0.17, 0.17, 0, 1), rotate 0.3s cubic-bezier(0.17, 0.17, 0, 1); icon 62.33 x 22, #15252d `nebula`.

Child layers that carry the look: div 1440x65 background #02060a `lightfall` border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.08); span 1x24 background oklab(0.999994 0.0000455678 0.0000200868 / 0.12); a 110.5x40 border 1px solid #f06d2b `cta-glow-orange` radius 999px.

![Nav bar default](components/crops/nav-bar-default.png)

#### Logo
The Apollo wordmark, top-left of the nav. Read as `logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 62.33 x 32; padding 5px 0px; radius 8px; background transparent; text __interFont_b14d2f 16/24 400, #15252d `nebula`; icon 62.33 x 22, #15252d `nebula` |
| focus-visible | outline 2px solid #ff7b3c `focus-orange`, offset 2px |

![Logo default](components/crops/logo-default.png) ![Logo hover](components/crops/logo-hover.png) ![Logo focus-visible](components/crops/logo-focus-visible.png) ![Logo pressed](components/crops/logo-pressed.png)

#### Nav disclosure
A nav menu trigger (Products / Solutions / Resources / Company): 38px, 8px radius, Inter 15px 500 at 72% white. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 104.77 x 38; padding 0px 13px; radius 8px; background transparent; text __interFont_b14d2f 15/22.5 500, oklab(0.999994 0.0000455678 0.0000200868 / 0.72); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 11 x 11, oklab(0.999994 0.0000455678 0.0000200868 / 0.72) |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.15); text __interFont_b14d2f 15/22.5 500, #ffffff `white`; icon 11 x 11, #ffffff `white` |
| focus-visible | outline 2px solid #ff7b3c `focus-orange`, offset 2px |
| pressed | background oklab(0.999994 0.0000455678 0.0000200868 / 0.1); text __interFont_b14d2f 15/22.5 500, #ffffff `white`; icon 11 x 11, #ffffff `white` |

![Nav disclosure default](components/crops/nav-trigger-default.png) ![Nav disclosure hover](components/crops/nav-trigger-hover.png) ![Nav disclosure focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav disclosure pressed](components/crops/nav-trigger-pressed.png)

#### Products menu
The Products dropdown panel: product rows with one-line descriptions, plus the two promo links at the foot. Read as `nav-menu` on the home page.

**Values (open).** size 1440 x 463; background transparent; text __interFont_b14d2f 16/24 700, #15252d `nebula`; transition height 0.2s cubic-bezier(0, 0, 0.2, 1); transform translate(0px, -6.47463px); opacity 0.0750526; icon 44 x 44, #15252d `nebula`.

Child layers that carry the look: div 1312x463 background #ffffff `white` border 1px solid #efefef `satellite` radius 16px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(9, 27, 35, 0.42) 0px 28px 64px -20px, rgba(9, 27, 35, 0.08) 0px 6px 16px 0px; a 447x96 image linear-gradient(to right in oklab, #fff1e9 0px, #f3f6f8 100%) border 1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) radius 12px; a 447x96 image linear-gradient(to right in oklab, #fff1e9 0px, #f3f6f8 100%) border 1px solid oklab(0.794287 0.0879803 0.0925078 / 0.3) radius 12px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Menu item
A product row inside the Products dropdown. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| open (same: hover) | size 149.44 x 48; radius 999px; background transparent; text __aeonikFont_a2019c 16/24 500, #c74100 `horizon-dark`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

Child layers that carry the look: span 149.4x29 border 1px solid #c74100 `horizon-dark`.

![Menu item open](components/crops/nav-menu-item-open.png) ![Menu item hover](components/crops/nav-menu-item-hover.png)

#### Start for free button
The pill at the right of the nav; links to studio.apollographql.com/signup. Hovered and focused only. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 123.42 x 40; padding 0px 18px; border 1px solid #e75e15 `brand-accent`; radius 999px; background #e75e15 `brand-accent`; text __interFont_b14d2f 14/21 500, #ffffff `white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #d84f08 `brand-hover`; background #d84f08 `brand-hover` |
| focus-visible | outline 2px solid #ff7b3c `focus-orange`, offset 2px |
| pressed | border 1px solid #d84f08 `brand-hover`; background #d84f08 `brand-hover` |

![Start for free button default](components/crops/nav-cta-default.png) ![Start for free button hover](components/crops/nav-cta-hover.png) ![Start for free button focus-visible](components/crops/nav-cta-focus-visible.png) ![Start for free button pressed](components/crops/nav-cta-pressed.png)

#### Search button
The Algolia detached search icon in the nav. Read as `nav-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 20 x 20; radius 3px; background transparent; text __interFont_b14d2f 16/16 400, #15252d `nebula`; transition background-color 0.3s cubic-bezier(0.17, 0.17, 0, 1), border-color 0.3s cubic-bezier(0.17, 0.17, 0, 1); icon 20 x 24, #f8f8f8 `offwhite` |
| hover | icon 20 x 24, #f6f6f6 |
| focus-visible | outline 1px solid #f8f8f8 `offwhite`, offset 8px |
| pressed | icon 20 x 24, #f6f6f6 |

![Search button default](components/crops/nav-search-default.png) ![Search button hover](components/crops/nav-search-hover.png) ![Search button focus-visible](components/crops/nav-search-focus-visible.png) ![Search button pressed](components/crops/nav-search-pressed.png)

### Home

The landing page: the 60px Aeonik hero over the near-black space field, the conic-ring primary CTA and outline secondary, the pause-motion and carousel chips, the alternating dark/light sections and the video card.

#### Hero title
"Give AI access to the systems that run your business" — Aeonik 60px white over the dark animated hero. Read as `hero-title` on the home page.

**Values (default).** size 832 x 126; background transparent; text __aeonikFont_a2019c 60/63 400, #ffffff `white`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subhead
The 20px Aeonik lede under the hero title. Read as `hero-sub` on the home page.

**Values (default).** size 864 x 65; background transparent; text __aeonikFont_a2019c 20/32.5 500, #d1d1d1 `border`.

![Hero subhead default](components/crops/hero-sub-default.png)

#### Primary CTA
The white 999px pill "Talk to Apollo" (60px tall, Aeonik 18px 500) with a soft warm shadow. Read as `cta-primary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 210.47 x 60; padding 16px 48px; border 2px solid transparent; radius 999px; background transparent; image linear-gradient(#02060a `lightfall`, #02060a `lightfall`), conic-gradient(from 411.894deg, #4ca6b5 `teal`, #f06d2b `cta-glow-orange`, #4ca6b5 `teal`); shadow oklab(0.676327 -0.0761709 -0.0438468 / 0.25) 2.3064px -1.6936px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) -2.3064px 1.6936px 16px 0px; text __aeonikFont_a2019c 18/24 500, #ffffff `white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | image linear-gradient(#15252d `nebula`, #15252d `nebula`), conic-gradient(from 568.884deg, #7cc3ce, #ff7b3c `focus-orange`, #7cc3ce); shadow oklab(0.77422 -0.0641362 -0.0343847 / 0.25) -1.28373px 2.71627px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) 1.28373px -2.71627px 16px 0px |
| focus-visible | image linear-gradient(#02060a `lightfall`, #02060a `lightfall`), conic-gradient(from 319.884deg, #4ca6b5 `teal`, #f06d2b `cta-glow-orange`, #4ca6b5 `teal`); shadow oklab(0.676327 -0.0761709 -0.0438468 / 0.25) -1.78293px -2.21707px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) 1.78293px 2.21707px 16px 0px; outline 2px solid #2fd1e0 `focus-cyan`, offset 4px |
| pressed | image linear-gradient(#15252d `nebula`, #15252d `nebula`), conic-gradient(from 454.878deg, #7cc3ce, #ff7b3c `focus-orange`, #7cc3ce); shadow oklab(0.77422 -0.0641362 -0.0343847 / 0.25) 3.7832px 0.2168px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) -3.7832px -0.2168px 16px 0px |

![Primary CTA default](components/crops/cta-primary-default.png) ![Primary CTA hover](components/crops/cta-primary-hover.png) ![Primary CTA focus-visible](components/crops/cta-primary-focus-visible.png) ![Primary CTA pressed](components/crops/cta-primary-pressed.png)

#### Secondary CTA
The 1px white/35 outline pill beside the primary. Read as `cta-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 238.02 x 60; padding 16px 48px; border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35); radius 999px; background transparent; text __aeonikFont_a2019c 18/24 500, #ffffff `white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #ffffff `white`; background oklab(0.999994 0.0000455678 0.0000200868 / 0.1) |
| focus-visible | outline 2px solid #2fd1e0 `focus-cyan`, offset 4px |
| pressed | border 1px solid #ffffff `white`; background oklab(0.999994 0.0000455678 0.0000200868 / 0.1) |

![Secondary CTA default](components/crops/cta-secondary-default.png) ![Secondary CTA hover](components/crops/cta-secondary-hover.png) ![Secondary CTA focus-visible](components/crops/cta-secondary-focus-visible.png) ![Secondary CTA pressed](components/crops/cta-secondary-pressed.png)

#### Pause motion button
The ghost chip bottom-right of the hero (80% black fill, 1px white/20 border, 4px radius). Read as `pause-motion` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.91 x 34; padding 8px 12px; border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2); radius 4px; background oklab(0.117506 -0.00815131 -0.0132371 / 0.8); text __aeonikFont_a2019c 12/16 400, oklab(0.999994 0.0000455677 0.0000200868 / 0.7); icon 12 x 12, oklab(0.999994 0.0000455677 0.0000200868 / 0.7) |
| hover | text __aeonikFont_a2019c 12/16 400, #ffffff `white`; icon 12 x 12, #ffffff `white` |
| focus-visible | outline 2px solid #e75e15 `brand-accent`, offset 2px |
| pressed | text __aeonikFont_a2019c 12/16 400, #ffffff `white`; icon 12 x 12, #ffffff `white` |

![Pause motion button default](components/crops/pause-motion-default.png) ![Pause motion button hover](components/crops/pause-motion-hover.png) ![Pause motion button focus-visible](components/crops/pause-motion-focus-visible.png) ![Pause motion button pressed](components/crops/pause-motion-pressed.png)

#### Text link
The solar-orange inline link (Aeonik 18px 700) inside body copy. Read as `text-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 298.59 x 33; background transparent; text __aeonikFont_a2019c 18/28 700, #c74100 `horizon-dark`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #c74100 `horizon-dark` |
| hover | text __aeonikFont_a2019c 18/28 700, #e75e15 `brand-accent`; icon 16 x 16, #e75e15 `brand-accent` |
| focus-visible | outline 2px solid #e75e15 `brand-accent`, offset 4px |
| pressed | text __aeonikFont_a2019c 18/28 700, #e75e15 `brand-accent`; icon 16 x 16, #e75e15 `brand-accent` |

Child layers that carry the look: span 298.6x33 border 1px solid #c74100 `horizon-dark`.

![Text link default](components/crops/text-link-default.png) ![Text link hover](components/crops/text-link-hover.png) ![Text link focus-visible](components/crops/text-link-focus-visible.png) ![Text link pressed](components/crops/text-link-pressed.png)

#### Arrow link pill
An orange "Explore … →" pill link between sections (Aeonik 16px 500). Read as `link-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 149.44 x 48; radius 999px; background transparent; text __aeonikFont_a2019c 16/24 500, #c74100 `horizon-dark`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid #e75e15 `brand-accent`, offset 4px |

Child layers that carry the look: span 149.4x29 border 1px solid #c74100 `horizon-dark`.

![Arrow link pill default](components/crops/link-pill-default.png) ![Arrow link pill hover](components/crops/link-pill-hover.png) ![Arrow link pill focus-visible](components/crops/link-pill-focus-visible.png) ![Arrow link pill pressed](components/crops/link-pill-pressed.png)

#### Section title (light)
An Aeonik 42px heading on a light content section — the site alternates dark hero / light content bands. Read as `section-title-light` on the home page.

**Values (default).** size 1296 x 52.5; background transparent; text __aeonikFont_a2019c 42/52.5 400, #000000.

![Section title (light) default](components/crops/section-title-light-default.png)

#### Video card
The 520x293 "PLAY VIDEO" card, 24px radius on eclipse. Read as `video-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 520 x 292.5; radius 24px; background #15252d `nebula`; text __aeonikFont_a2019c 14/14 700, #15252d `nebula`; icon 20 x 20, #15252d `nebula` |
| hover | text __aeonikFont_a2019c 14/14 700, #f8f8f8 `offwhite`; icon 20 x 20, #f8f8f8 `offwhite` |
| focus-visible | outline 2px solid #e75e15 `brand-accent`, offset -4px; text __aeonikFont_a2019c 14/14 700, #f8f8f8 `offwhite`; icon 20 x 20, #f8f8f8 `offwhite` |
| pressed | text __aeonikFont_a2019c 14/14 700, #f8f8f8 `offwhite`; icon 19 x 19, #f8f8f8 `offwhite` |

![Video card default](components/crops/video-card-default.png) ![Video card hover](components/crops/video-card-hover.png) ![Video card focus-visible](components/crops/video-card-focus-visible.png) ![Video card pressed](components/crops/video-card-pressed.png)

#### Copy control row
One of the three 416x84 copy rows in the architecture animation panel. Read as `copy-row` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 416 x 84; background transparent; text __aeonikFont_a2019c 16/24 400, #000000 |
| focus-visible | outline 2px solid #666666 `content-muted`, offset 4px |

![Copy control row default](components/crops/copy-row-default.png) ![Copy control row hover](components/crops/copy-row-hover.png) ![Copy control row focus-visible](components/crops/copy-row-focus-visible.png) ![Copy control row pressed](components/crops/copy-row-pressed.png)

#### Carousel arrow
A 42x42 white 16px-radius arrow button on the logo/customer carousel. Read as `carousel-arrow` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.91 x 34; padding 8px 12px; border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.2); radius 4px; background oklab(0.117506 -0.00815131 -0.0132371 / 0.8); text __aeonikFont_a2019c 12/16 400, oklab(0.999994 0.0000455677 0.0000200868 / 0.7); icon 12 x 12, oklab(0.999994 0.0000455677 0.0000200868 / 0.7) |
| hover | text __aeonikFont_a2019c 12/16 400, #ffffff `white`; icon 12 x 12, #ffffff `white` |
| focus-visible | outline 2px solid #e75e15 `brand-accent`, offset 2px |
| pressed | text __aeonikFont_a2019c 12/16 400, #ffffff `white`; icon 12 x 12, #ffffff `white` |

![Carousel arrow default](components/crops/carousel-arrow-default.png) ![Carousel arrow hover](components/crops/carousel-arrow-hover.png) ![Carousel arrow focus-visible](components/crops/carousel-arrow-focus-visible.png) ![Carousel arrow pressed](components/crops/carousel-arrow-pressed.png)

#### Footer
The footer band: tagline, five link columns, small orange Start for free pill, social icons. Read as `footer` on the home page.

**Values (default).** size 1440 x 627.47; background transparent; text __interFont_b14d2f 16/24 900, #f8f8f8 `offwhite`; icon 85 x 30, #f8f8f8 `offwhite`.

Child layers that carry the look: div 1344x367.5 border 1px solid #f6f6f6; a 107.2x34 background #e75e15 `brand-accent` border 1px solid transparent radius 999px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A 14px Inter footer column link at 97% white. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 85 x 30; background transparent; text __interFont_b14d2f 16/24 400, #f8f8f8 `offwhite`; icon 85 x 30, #f8f8f8 `offwhite` |
| focus-visible | outline 1px auto #99c8ff `focus-blue`, offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon
A 28x28 social icon in the footer row. Read as `social-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 28 x 28; background transparent; text __interFont_b14d2f 16/24 400, #f8f8f8 `offwhite`; transition color 0.3s cubic-bezier(0.17, 0.17, 0, 1), transform 0.15s cubic-bezier(0.17, 0.17, 0, 1); icon 28 x 32, #f8f8f8 `offwhite` |
| focus-visible | outline 1px auto #99c8ff `focus-blue`, offset 1px |

![Social icon default](components/crops/social-link-default.png) ![Social icon hover](components/crops/social-link-hover.png) ![Social icon focus-visible](components/crops/social-link-focus-visible.png) ![Social icon pressed](components/crops/social-link-pressed.png)

### Pricing

The pricing page: the plan-tier and Monthly/Yearly segment pills, the request-volume pills (the held one paints #fc5200), the per-plan orange CTAs, the eclipse stats card, the grey FAQ card and the connectors promo banner.

#### Pricing title
"Pricing that makes sense at any scale…" — Inter 50px 500 on the dark page. Read as `pricing-title` on the pricing page.

**Values (default).** size 880 x 276.78; background transparent; text __interFont_b14d2f 50/55 500, #f8f8f8 `offwhite`; icon 25 x 25, #f8f8f8 `offwhite`.

Child layers that carry the look: a 146.8x49 background #e75e15 `brand-accent` border 1px solid transparent radius 999px; a 190.5x49 border 1px solid #e75e15 `brand-accent` radius 999px.

![Pricing title default](components/crops/pricing-title-default.png)

#### Tier segment
A plan-tier filter pill (Developer / …), 43px tall, 20px radius, 1px white border. Read as `tier-segment` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 125.55 x 43; padding 10px 16px; border 1px solid #f8f8f8 `offwhite`; radius 20px; background transparent; text __interFont_b14d2f 14/21 400, #f8f8f8 `offwhite`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text __interFont_b14d2f 14/21 400, #ffffff `white` |
| focus-visible | outline 5px auto #99c8ff `focus-blue`, offset 0px |
| pressed | text __interFont_b14d2f 14/21 400, #ffffff `white` |

![Tier segment default](components/crops/tier-segment-default.png) ![Tier segment hover](components/crops/tier-segment-hover.png) ![Tier segment focus-visible](components/crops/tier-segment-focus-visible.png) ![Tier segment pressed](components/crops/tier-segment-pressed.png)

#### Billing segment
The Monthly/Yearly billing pill beside the tier pills. Read as `billing-segment` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111.5 x 43; padding 10px 16px; border 1px solid #f8f8f8 `offwhite`; radius 20px; background transparent; text __interFont_b14d2f 14/21 400, #f8f8f8 `offwhite`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text __interFont_b14d2f 14/21 400, #ffffff `white` |
| focus-visible | outline 5px auto #99c8ff `focus-blue`, offset 0px |
| pressed | text __interFont_b14d2f 14/21 400, #ffffff `white` |

![Billing segment default](components/crops/billing-segment-default.png) ![Billing segment hover](components/crops/billing-segment-hover.png) ![Billing segment focus-visible](components/crops/billing-segment-focus-visible.png) ![Billing segment pressed](components/crops/billing-segment-pressed.png)

#### Volume pill (selected)
The held request-volume pill: #fc5200 solar fill, eclipse text, 8px radius. Read as `volume-pill-on` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 39.97 x 39; padding 8px 10px; border 1px solid #fc5200 `brand`; radius 8px; background #fc5200 `brand`; text __interFont_b14d2f 14/21 400, #15252d `nebula`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid #f8f8f8 `offwhite`, offset 2px |

![Volume pill (selected) default](components/crops/volume-pill-on-default.png) ![Volume pill (selected) hover](components/crops/volume-pill-on-hover.png) ![Volume pill (selected) focus-visible](components/crops/volume-pill-on-focus-visible.png) ![Volume pill (selected) pressed](components/crops/volume-pill-on-pressed.png)

#### Volume pill
An unheld volume pill: transparent, 1px border, 8px radius. Read as `volume-pill` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48.8 x 39; padding 8px 10px; border 1px solid #f8f8f8 `offwhite`; radius 8px; background transparent; text __interFont_b14d2f 14/21 400, #f8f8f8 `offwhite`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid #f8f8f8 `offwhite`, offset 2px |

![Volume pill default](components/crops/volume-pill-default.png) ![Volume pill hover](components/crops/volume-pill-hover.png) ![Volume pill focus-visible](components/crops/volume-pill-focus-visible.png) ![Volume pill pressed](components/crops/volume-pill-pressed.png)

#### Plan CTA
The orange "Start for free" pill on pricing (49px, Inter 16px 500). Links to Studio signup; hovered and focused only. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 123.42 x 40; padding 0px 18px; border 1px solid #e75e15 `brand-accent`; radius 999px; background #e75e15 `brand-accent`; text __interFont_b14d2f 14/21 500, #ffffff `white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #d84f08 `brand-hover`; background #d84f08 `brand-hover` |
| focus-visible | outline 2px solid #ff7b3c `focus-orange`, offset 2px |
| pressed | border 1px solid #d84f08 `brand-hover`; background #d84f08 `brand-hover` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Stats band card
The 1344x670 eclipse card ("Trusted by digital leaders"), 32px radius. Read as `stats-card` on the pricing page.

**Values (default).** size 1344 x 669.5; padding 94px 80px; radius 32px; background #15252d `nebula`; text __interFont_b14d2f 38/47.5 700, #f8f8f8 `offwhite`.

![Stats band card default](components/crops/stats-card-default.png)

#### FAQ card
The light regolith-grey FAQ card (#e3e3e3), 32px radius. Read as `faq-card` on the pricing page.

**Values (default).** size 1344 x 612.5; padding 72px; radius 32px; background #e3e3e3 `faq-gray`; text __interFont_b14d2f 38/47.5 700, #15252d `nebula`; icon 48 x 48, #15252d `nebula`.

![FAQ card default](components/crops/faq-card-default.png)

#### FAQ item
A question row inside the FAQ card. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 1200 x 48; background transparent; text __interFont_b14d2f 24/31.2 400, #15252d `nebula`; icon 48 x 48, #15252d `nebula` |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item hover](components/crops/faq-item-hover.png) ![FAQ item focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ item pressed](components/crops/faq-item-pressed.png)

#### Promo banner
The "Amazing together" connectors promo card: eclipse fill, 32px radius. Read as `promo-banner` on the pricing page.

**Values (default).** size 1344 x 264.53; padding 40px; radius 32px; background #15252d `nebula`; text __interFont_b14d2f 38/47.5 700, #f8f8f8 `offwhite`.

![Promo banner default](components/crops/promo-banner-default.png)

### Customers

The customers page: the 50px title, the filled and outline orange CTA pair, the stats band and the white customer-story cards.

#### Customers title
"API Orchestration Success Stories" — Inter 50px 500. Read as `customers-title` on the customers page.

**Values (default).** size 392.14 x 110; background transparent; text __interFont_b14d2f 50/55 500, #f8f8f8 `offwhite`.

![Customers title default](components/crops/customers-title-default.png)

#### Orange CTA
The solar-orange pill "Talk to an expert" (49px, Inter 16px 500, eclipse text on orange). Read as `cta-orange` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 175.83 x 49.03; padding 16px 24px; border 1px solid transparent; radius 999px; background #e75e15 `brand-accent`; text __interFont_b14d2f 16/15.04 500, #15252d `nebula`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.649255 0.136349 0.125914 / 0.9) |
| focus-visible | outline 2px solid #e75e15 `brand-accent`, offset 8px |
| pressed | background oklab(0.649255 0.136349 0.125914 / 0.9) |

![Orange CTA default](components/crops/cta-orange-default.png) ![Orange CTA hover](components/crops/cta-orange-hover.png) ![Orange CTA focus-visible](components/crops/cta-orange-focus-visible.png) ![Orange CTA pressed](components/crops/cta-orange-pressed.png)

#### Orange outline CTA
The 1px orange-outline pill beside the filled one. Read as `cta-orange-outline` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 176.89 x 49.03; padding 16px 24px; border 1px solid #e75e15 `brand-accent`; radius 999px; background transparent; text __interFont_b14d2f 16/15.04 500, #ffffff `white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.649255 0.136349 0.125914 / 0.1) |
| focus-visible | outline 2px solid #e75e15 `brand-accent`, offset 8px |
| pressed | background oklab(0.649255 0.136349 0.125914 / 0.1) |

![Orange outline CTA default](components/crops/cta-orange-outline-default.png) ![Orange outline CTA hover](components/crops/cta-orange-outline-hover.png) ![Orange outline CTA focus-visible](components/crops/cta-orange-outline-focus-visible.png) ![Orange outline CTA pressed](components/crops/cta-orange-outline-pressed.png)

#### Stats band
The eclipse stats card ("0M monthly downloads / 0% of the Fortune 100…"), 32px radius. Read as `stats-band` on the customers page.

**Values (default).** size 1344 x 332; radius 32px; background #15252d `nebula`; text __firaCodeFont_e66e50 72/72 700, #f8f8f8 `offwhite`.

![Stats band default](components/crops/stats-band-default.png)

#### Story card
A customer-story card (432x585): white 32px-radius card with cover image, company name, title and author. Read as `story-card` on the customers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 432 x 584.5; background transparent; text __interFont_b14d2f 30/37.5 700, #15252d `nebula` |

Child layers that carry the look: div 432x584.5 background #f8f8f8 `offwhite` radius 32px; div 432x283.5 background #efefef `satellite` radius 32px.

![Story card default](components/crops/story-card-default.png) ![Story card hover](components/crops/story-card-hover.png) ![Story card focus-visible](components/crops/story-card-focus-visible.png) ![Story card pressed](components/crops/story-card-pressed.png)

### Blog

The blog index: "What's new" in Aeonik 60px on the light page, the satellite-grey featured cards, the white regolith archive cards and the numbered pagination.

#### Blog title
"What's new" — Aeonik 60px on the light page. Read as `blog-title` on the blog page.

**Values (default).** size 1368 x 67.19; background transparent; text __aeonikFont_68f9fd 60/67.2 400, #15252d `nebula`.

![Blog title default](components/crops/blog-title-default.png)

#### Article card (satellite)
A featured article card on the satellite grey (#cfd7d6), 32px radius: date, title, author. Read as `article-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 444 x 298.81; radius 32px; background #cfd7d6 `satellite-dark`; text __Inter_8b46f2 16/22.4 400, #15252d `nebula`; transition transform 0.5s cubic-bezier(0.06, 0.47, 0.1, 1) |
| hover | transform translate(0px, -2.98119px) |
| pressed | transform translate(0px, -2.95858px) |

![Article card (satellite) default](components/crops/article-card-default.png) ![Article card (satellite) hover](components/crops/article-card-hover.png) ![Article card (satellite) focus-visible](components/crops/article-card-focus-visible.png) ![Article card (satellite) pressed](components/crops/article-card-pressed.png)

#### Article card (regolith)
A past-posts card on white regolith, 32px radius. Read as `article-card-regolith` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 672 x 209.39; radius 32px; background #ffffff `white`; text __Inter_8b46f2 16/22.4 400, #15252d `nebula`; transition background-color 0.3s cubic-bezier(0.06, 0.47, 0.1, 1) |

![Article card (regolith) default](components/crops/article-card-regolith-default.png) ![Article card (regolith) hover](components/crops/article-card-regolith-hover.png) ![Article card (regolith) focus-visible](components/crops/article-card-regolith-focus-visible.png) ![Article card (regolith) pressed](components/crops/article-card-regolith-pressed.png)

#### Pagination button
A numbered page button in the archive pagination. Read as `pagination` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 23 x 24.47; background transparent; text __Inter_8b46f2 18/24.48 400, #15252d `nebula`; transition opacity 0.3s cubic-bezier(0.06, 0.47, 0.1, 1); opacity 0.3 |
| focus-visible | outline 5px auto #99c8ff `focus-blue`, offset 0px |

![Pagination button default](components/crops/pagination-default.png) ![Pagination button hover](components/crops/pagination-hover.png) ![Pagination button focus-visible](components/crops/pagination-focus-visible.png) ![Pagination button pressed](components/crops/pagination-pressed.png)

#### Pagination (active)
The held page number in the pagination. Read as `pagination-on` on the blog page.

**Values (default).** size 23 x 24.47; background transparent; text __Inter_8b46f2 18/24.48 400, #15252d `nebula`; transition opacity 0.3s cubic-bezier(0.06, 0.47, 0.1, 1).

![Pagination (active) default](components/crops/pagination-on-default.png)

### Contact sales

The contact-sales page: the light intro, then the HubSpot form on an eclipse-navy band — 54px fields with 16px radius and offwhite borders that turn #fc5200 on focus, and the orange pill submit (never pressed through).

#### Contact title
"Contact us" — Inter 50px 500, eclipse on the light page. Read as `contact-title` on the contact-sales page.

**Values (default).** size 498 x 55; background transparent; text __interFont_b14d2f 50/55 500, #15252d `nebula`.

![Contact title default](components/crops/contact-title-default.png)

#### Text field
A HubSpot text input: 54px, 16px radius, eclipse fill, 1px white border, Inter 18px. Clicked into once; nothing typed or sent. Read as `field` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 574.03 x 54; padding 0px 24px; border 1px solid #f8f8f8 `offwhite`; radius 16px; background #15252d `nebula`; text __interFont_b14d2f 18/25.2 400, #f8f8f8 `offwhite`; transition border-color 0.3s cubic-bezier(0.23, 0.4, 0.53, 0.88); placeholder rgba(255, 234, 219, 0.5) |
| focused | border 1px solid #fc5200 `brand` |

![Text field default](components/crops/field-default.png) ![Text field focused](components/crops/field-focused.png)

#### Text field (filled)
The same field with text typed, then deleted before close; the form was never submitted. Read as `field-filled` on the contact-sales page.

**Values (filled).** size 574.03 x 54; padding 0px 24px; border 1px solid #fc5200 `brand`; radius 16px; background #15252d `nebula`; text __interFont_b14d2f 18/25.2 400, #f8f8f8 `offwhite`; transition border-color 0.3s cubic-bezier(0.23, 0.4, 0.53, 0.88); placeholder rgba(255, 234, 219, 0.5).

![Text field (filled) filled](components/crops/field-filled-filled.png)

#### Select
A country/topic select: same 54x16 field shell, placeholder state. Read as `select` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 574.03 x 54; padding 0px 24px; border 1px solid #f8f8f8 `offwhite`; radius 16px; background #15252d `nebula`; image an image (data URI); text __interFont_b14d2f 18/25.2 400, #f8f8f8 `offwhite`; transition border-color 0.3s cubic-bezier(0.23, 0.4, 0.53, 0.88) |
| focused | border 1px solid #fc5200 `brand` |

![Select default](components/crops/select-default.png) ![Select focused](components/crops/select-focused.png)

#### Textarea
The 120px message textarea, same field shell. Read as `textarea` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 574.03 x 120; padding 0px 24px; border 1px solid #f8f8f8 `offwhite`; radius 16px; background #15252d `nebula`; text __interFont_b14d2f 18/25.2 400, #f8f8f8 `offwhite`; transition border-color 0.3s cubic-bezier(0.23, 0.4, 0.53, 0.88); placeholder rgba(255, 234, 219, 0.5) |
| focused | border 1px solid #fc5200 `brand` |

![Textarea default](components/crops/textarea-default.png) ![Textarea focused](components/crops/textarea-focused.png)

#### Submit button
The orange pill submit (50px, radius 9999, Inter 16px 500). Measured and hovered only — never clicked. Read as `submit` on the contact-sales page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 103.25 x 50; padding 16px 24px; border 1px solid transparent; radius 9999px; background #e75e15 `brand-accent`; text __interFont_b14d2f 16/16 500, #ffffff `white`; transition background-color 0.2s ease; placeholder #ffffff `white` |
| hover | opacity 0.9 |
| focus-visible | border 1px solid #fc5200 `brand`; outline 2px solid #e75e15 `brand-accent`, offset 8px |
| pressed | opacity 0.9 |

![Submit button default](components/crops/submit-default.png) ![Submit button hover](components/crops/submit-hover.png) ![Submit button focus-visible](components/crops/submit-focus-visible.png) ![Submit button pressed](components/crops/submit-pressed.png)

### Mobile (390 wide)

The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the burger menu, the 36px hero and the full-width CTAs.

#### Mobile nav bar
The mobile header: logo left, hamburger right. Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 390 x 65; background transparent; text __interFont_b14d2f 16/24 400, #15252d `nebula`; transition transform 0.3s cubic-bezier(0.17, 0.17, 0, 1), translate 0.3s cubic-bezier(0.17, 0.17, 0, 1), scale 0.3s cubic-bezier(0.17, 0.17, 0, 1), rotate 0.3s cubic-bezier(0.17, 0.17, 0, 1); icon 62.33 x 22, #15252d `nebula`.

Child layers that carry the look: div 390x65 background #02060a `lightfall` border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.08); span 0x0 background oklab(0.999994 0.0000455678 0.0000200868 / 0.12); a 0x0 border 1px solid #f06d2b `cta-glow-orange` radius 999px.

![Mobile nav bar default](components/crops/m-nav-bar-default.png)

#### Hamburger
The mobile menu button. Not opened — the menu overlays the measured content. Read as `m-burger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 40 x 40; radius 8px; background transparent; text __interFont_b14d2f 16/24 400, oklab(0.999994 0.0000455678 0.0000200868 / 0.82); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, oklab(0.999994 0.0000455678 0.0000200868 / 0.82) |

![Hamburger default](components/crops/m-burger-default.png) ![Hamburger pressed](components/crops/m-burger-pressed.png)

#### Mobile hero title
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 342 x 113.39; background transparent; text __aeonikFont_a2019c 36/37.8 400, #ffffff `white`.

![Mobile hero title default](components/crops/m-hero-title-default.png)

#### Mobile primary CTA
The white pill, full width on phone. Read as `m-cta-primary` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 342 x 60; padding 16px 48px; border 2px solid transparent; radius 999px; background transparent; image linear-gradient(#02060a `lightfall`, #02060a `lightfall`), conic-gradient(from 458.976deg, #4ca6b5 `teal`, #f06d2b `cta-glow-orange`, #4ca6b5 `teal`); shadow oklab(0.676327 -0.0761709 -0.0438468 / 0.25) 3.60106px 0.398941px 16px 0px, oklab(0.684338 0.128575 0.123564 / 0.25) -3.60106px -0.398941px 16px 0px; text __aeonikFont_a2019c 18/24 500, #ffffff `white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| pressed | image linear-gradient(#15252d `nebula`, #15252d `nebula`), conic-gradient(from 513.972deg, #7cc3ce, #ff7b3c `focus-orange`, #7cc3ce); shadow oklab(0.77422 -0.0641362 -0.0343847 / 0.25) 1.15679px 2.84321px 16px 0px, oklab(0.727177 0.128214 0.123105 / 0.25) -1.15679px -2.84321px 16px 0px |

![Mobile primary CTA default](components/crops/m-cta-primary-default.png) ![Mobile primary CTA pressed](components/crops/m-cta-primary-pressed.png)

#### Mobile secondary CTA
The outline pill under it. Read as `m-cta-secondary` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 342 x 60; padding 16px 48px; border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.35); radius 999px; background transparent; text __aeonikFont_a2019c 18/24 500, #ffffff `white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Mobile secondary CTA default](components/crops/m-cta-secondary-default.png) ![Mobile secondary CTA pressed](components/crops/m-cta-secondary-pressed.png)

## Icons

36 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. The SVGs are Apollo GraphQL's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [go-to-homepage](icons/go-to-homepage.svg) | 62x22 | 0 0 85 30 | fill | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Go to homepage |
| [icon-15d486fd](icons/icon-15d486fd.svg) | 20x20 20x24 | 0 0 24 24 | fill | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact |  |
| [apollo-graphql-on-github](icons/apollo-graphql-on-github.svg) | 28x28 28x32 | 0 0 32 32 | fill | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Apollo GraphQL on GitHub |
| [your-privacy-choices](icons/your-privacy-choices.svg) | 30x14 | 0 0 30 14 | fill | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Your Privacy Choices |
| [products](icons/products.svg) | 11x11 | 0 0 24 24 | stroke | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Products / Solutions / Resources |
| [sociallink](icons/sociallink-6727abcc.svg) | 28x28 28x32 | 0 0 32 32 | fill | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Apollo GraphQL on YouTube |
| [sociallink](icons/sociallink-6c9b8fd8.svg) | 28x28 28x32 | 0 0 24 24 | fill | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Apollo GraphQL on LinkedIn |
| [sociallink](icons/sociallink-78c1197f.svg) | 28x28 28x32 | 0 0 33 33 | fill | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Apollo GraphQL on Twitter |
| [apollo-graphos](icons/apollo-graphos.svg) | 16x16 | 0 0 24 24 | stroke | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Apollo GraphOS / GraphOS Agent Services / GraphOS Studio |
| [apollo-router-core](icons/apollo-router-core.svg) | 14x14 |  | stroke | home; graphos; agent-services; pricing; customers; blog; why-apollo; contact | Apollo Router Core / Docs / Community |
| [dismiss-banner](icons/dismiss-banner.svg) | 20x20 | 0 0 47 48 | stroke | home; graphos; agent-services; pricing; customers; why-apollo; contact | Dismiss banner |
| [watch-keynote](icons/watch-keynote.svg) | 10x12 | 0 0 10 12 | fill | home; graphos; agent-services; pricing; customers; why-apollo; contact | Watch keynote |
| [icon-0249fed4](icons/icon-0249fed4.svg) | 20x20 | 0 0 16 16 | stroke | home | Play video: Intuit: See GraphOS in actio |
| [pause-hero-animation](icons/pause-hero-animation.svg) | 12x12 | 0 0 16 16 | stroke | home | Pause hero animation |
| [previous-testimonial](icons/previous-testimonial.svg) | 20x20 | 0 0 16 16 | stroke | home | Previous testimonial |
| [icon-3f70aa80](icons/icon-3f70aa80.svg) | 25x25 26x26 32x32 40x40 | 0 0 32 32 | stroke | pricing; why-apollo; contact | Only pay for the API volume and features / Volume discounts  |
| [icon-a4931061](icons/icon-a4931061.svg) | 16x16 20x20 | 0 0 16 16 | stroke | home | Read more about domain models / Next testimonial / Apollo Gr |
| [icon-5c18a5ce](icons/icon-5c18a5ce.svg) | 12x12 24x24 25x25 | 0 0 16 16 | stroke | graphos; pricing | Asynchronously execute requests across a / Minimize latency  |
| [icon-8081ab1a](icons/icon-8081ab1a.svg) | 24x24 | 0 0 24 24 | stroke | graphos; agent-services | EXPLORE MORE Explore Apollo GraphOS docu / CUSTOMER STORY Ho |
| [trusted-api-access](icons/trusted-api-access.svg) | 24x24 32x32 | 0 0 16 16 | stroke | graphos; agent-services | Trusted API access |
| [accordionarrow](icons/accordionarrow.svg) | 30x30 48x48 | 0 0 112 112 | stroke | pricing; why-apollo | How do you measure the number of request / How does the prom |
| [icon-04791097](icons/icon-04791097.svg) | 12x12 | 0 0 12 12 | stroke | home | Get Started (opens in a new tab) Start b |
| [one-access-layer](icons/one-access-layer.svg) | 24x24 | 0 0 16 16 | stroke | graphos | One access layer |
| [icon-24661aa5](icons/icon-24661aa5.svg) | 15x15 | 0 0 16 16 | stroke | pricing | Schema Proposals - Collaboration and app / Single sign-on (S |
| [icon-3cb239c8](icons/icon-3cb239c8.svg) | 32x32 | 0 0 24 24 | stroke | agent-services |  |
| [play-video](icons/play-video.svg) | 16x16 | 0 0 32 32 | stroke | why-apollo | Play video |
| [icon](icons/icon.svg) | 16x16 28x28 | 0 0 32 32 | fill | blog | Subscribe to the RSS feed / RSS feed |
| [icon-5eec27c2](icons/icon-5eec27c2.svg) | 24x24 | 0 0 16 16 | stroke | graphos | Ship new capabilities, faster |
| [icon-6d7d0d48](icons/icon-6d7d0d48.svg) | 24x24 |  | fill | agent-services |  |
| [icon-73de2292](icons/icon-73de2292.svg) | 24x24 |  | stroke | agent-services |  |
| [link](icons/link.svg) | 24x24 | 0 0 24 24 | stroke | why-apollo | Artificial intelligence Modern AI applic / Mergers & acquisi |
| [icon-9f1202a3](icons/icon-9f1202a3.svg) | 44x44 | 0 0 61 61 | fill | home | Apollo GraphOS Platform API Orchestratio / GraphOS Agent Ser |
| [arrowbtn](icons/arrowbtn.svg) | 30x30 | 0 0 25 25 | stroke | blog |  |
| [icon-b97dd98f](icons/icon-b97dd98f.svg) | 24x24 | 0 0 16 16 | stroke | agent-services | What are GraphOS Agent Services? / Do I need an existing gra |
| [icon-d5160243](icons/icon-d5160243.svg) | 32x32 | 0 0 24 24 | stroke | agent-services |  |
| [type-field-or-tag](icons/type-field-or-tag.svg) | 16x16 32x32 | 0 0 16 16 | stroke | agent-services | Type, field, or tag |

## Gaps

### Pages

- **Apollo Studio and everything behind sign-in.** The product itself lives on studio.apollographql.com (the nav's Start-for-free and every plan CTA point there). Its /login and /signup pages rendered signed out and were captured at rest ([login-light-default](screenshots/login-light-default.png), [signup-light-default](screenshots/signup-light-default.png)), but nothing was typed and no button that posts was pressed: Studio's console, onboarding and every authenticated surface are a recorded boundary, not captured.
- **Anything that sends.** No form was submitted, nothing bought, nothing signed into, and the OneTrust consent card was never answered; the contact form's fields were clicked into and typed in, then cleared before close.
- **The nav search.** The Algolia search button was measured at rest; its detached overlay was not opened (it mounts a modal over measured content).
- **The mobile menu.** The 390-wide burger was measured; the drawer it opens was not captured.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so a state a script adds on mousedown (if any) is missing.
- **The billing toggle** was pressed once for the alternate billing state (client-side, nothing posted) and left as found.
- **The FAQ accordion** was measured closed; its rows were not opened, so the open answer state is not in this package.
- **Carousels and video.** The logo/customer carousel and the PLAY VIDEO card were measured at rest; slides were not advanced and no video was played.

### Themes

The site paints two surfaces across its pages — dark navy/near-black sections (home, graphos, agent-services, most of pricing/customers/why-apollo, the contact form band) and light sections (blog, the contact-sales intro, the FAQ card) — and the stylesheet carries a `[data-theme="dark"]` block that re-binds the semantic `--color-*` names for dark sections. Both are in tokens.json as the `light` and `dark` sets.

### Fonts

- **Aeonik** (display, 400/500) and **Aeonik Air** are Apollo's proprietary faces, self-hosted through next/font as `__aeonikFont_*` (`fonts` in [raw/css-vars.json](raw/css-vars.json)); **Inter** (UI, 400–700) and **Fira Code** (code) ship the same way. The style guide renders them with the system fallback stack.

### Screenshots

- Screens and product imagery are apollographql.com's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- No personal data was captured: every page was read signed out with an empty session, the only presses were the Products disclosure and the billing segment (both client-side), and the text typed into the contact form (`name@example.com`, a placeholder literal) was deleted before close.
