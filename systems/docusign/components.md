# Docusign components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from docusign.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. docusign.com signed out is three surfaces: the Next.js + Emotion marketing site in DS Indigo, the signature generator (the only declaring surface, on its ecru ground), and the /en-SG/ ecom pricing storefront plus the account.docusign.com sign-in card (Tailwind + Emotion, the DXP layer). Nothing was signed into, purchased or submitted; the login and trial forms were never sent; a signature name was typed only to render the local preview.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (73 components, 209 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (206 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light` (the marketing .dark islands appear inside light shots). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| eSignature | `/products/electronic-signature` | [default](screenshots/esignature-light-default.png), [faq](screenshots/esignature-light-faq.png), [full](screenshots/esignature-light-full.png), [modal](screenshots/esignature-light-modal.png) |
| Free trial | `/free-trial` | [default](screenshots/trial-light-default.png), [full](screenshots/trial-light-full.png) |
| Signature generator | `/signature-generator` | [default](screenshots/signgen-light-default.png), [full](screenshots/signgen-light-full.png), [type](screenshots/signgen-light-type.png) |
| Customer stories | `/customer-stories` | [default](screenshots/stories-light-default.png), [full](screenshots/stories-light-full.png) |
| Company | `/company` | [default](screenshots/company-light-default.png), [full](screenshots/company-light-full.png) |
| Pricing storefront | `ecom /en-SG/plans-and-pricing/esignature` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png), [monthly](screenshots/pricing-light-monthly.png) |
| Log in | `account.docusign.com (via /login)` | [default](screenshots/login-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Signature generator, phone | `/signature-generator` | [default](screenshots/mobile-signgen-light-default.png), [full](screenshots/mobile-signgen-light-full.png) |
| Pricing storefront, phone | `ecom /en-SG/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Products mega-menu | every marketing page | the Products trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| Customer-story video dialog | eSignature page | the Expand-video button's own click; closed with Escape | [esignature-light-modal](screenshots/esignature-light-modal.png), [video-dialog](#video-dialog) |
| FAQ accordion | eSignature page | a row's own toggle | [esignature-light-faq](screenshots/esignature-light-faq.png), [faq-open](#faq-row-open) |
| Signature Type mode | signature generator | the Type tab's own click; a sample name was typed, nothing sent | [signgen-light-type](screenshots/signgen-light-type.png), [sg-field](#name-field) |
| Billing toggle | pricing storefront | the Monthly half's own click re-priced the cards | [pricing-light-monthly](screenshots/pricing-light-monthly.png), [ec-billing-monthly](#monthly-toggle) |
| Mobile menu | home, phone width | the hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| OneTrust consent, Sierra chat, Guideflow player | every page | hidden, never answered (no consent control was ever clicked) | hidden before every shot and reading |
| Signed-in product | apps.docusign.com workspace | the agreement workspace lives behind account.docusign.com/oauth | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 40 components were given a real keyboard focus. 35 draw an outline ring: `logo` (2px solid #4c00ff `color.cobalt`, offset 2px), `nav-trigger` (2px solid #4c00ff `color.cobalt`, offset 2px), `nav-link` (2px solid #4c00ff `color.cobalt`, offset 2px), `nav-contact` (2px solid #4c00ff `color.cobalt`, offset 2px), `nav-buy` (2px solid #4c00ff `color.cobalt`, offset 2px), `nav-cta` (2px solid #4c00ff `color.cobalt`, offset 2px), `nav-search` (2px solid #cbc2ff `color.mist`, offset 2px), `login-link` (2px solid #cbc2ff `color.mist`, offset 2px), `menu-link` (2px solid #4c00ff `color.cobalt`, offset 2px), `hero-cta` (2px solid #ffffff `color.white`, offset 2px), `hero-link` (2px solid #4c00ff `color.cobalt`, offset 2px), `hero-checkbox` (on a child: 1px auto rgb(0, 95, 204) offset 2px), `hero-country` (on a child: 1px auto rgb(0, 95, 204) offset 0px), `blog-card` (2px solid #4c00ff `color.cobalt`, offset 2px), `e-cta` (2px solid #4c00ff `color.cobalt`, offset 2px), `video-expand` (2px solid #4c00ff `color.cobalt`, offset 2px), `faq-button` (2px solid #4c00ff `color.cobalt`, offset 0px), `trial-checkbox` (on a child: 1px auto rgb(0, 95, 204) offset 2px), `trial-cta` (2px solid #4c00ff `color.cobalt`, offset 2px), `help-button` (2px solid #4c00ff `color.cobalt`, offset 2px), `sg-tab-draw` (1px auto #005fcc `color.focus-auto`, offset 0px), `sg-tab-type` (1px auto #005fcc `color.focus-auto`, offset 0px), `sg-font` (1px auto #005fcc `color.focus-auto`, offset 0px), `filter-button` (2px solid #4c00ff `color.cobalt`, offset 2px), `story-card` (2px solid #4c00ff `color.cobalt`, offset 2px), `ec-billing-annual` (1px auto #005fcc `color.focus-auto`, offset 0px), `ec-billing-monthly` (1px auto #005fcc `color.focus-auto`, offset 0px), `feature-row` (1px auto #005fcc `color.focus-auto`, offset 0px), `auth-next` (2px solid #130032 `color.inkwell`, offset 2px), `auth-lang` (2px solid #130032 `color.inkwell`, offset 2px), `auth-signup` (2px solid #130032 `color.inkwell`, offset 2px), `footer-link` (2px solid #4c00ff `color.cobalt`, offset 2px), `m-menu-button` (1px auto #005fcc `color.focus-auto`, offset 0px), `m-nav-item` (2px solid #4c00ff `color.cobalt`, offset 2px), `m-cta` (2px solid #4c00ff `color.cobalt`, offset 2px). 4 draw a focus ring as a shadow instead: `sg-color`, `buy-now`, `contact-sales`, `see-all`. 1 change only their border: `locale-button`. Focus could not be captured on 3 more (keyboard focus never landed on them, so their readings are left out): `assistant`, `sg-clear`, `sg-download`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.33, 0, 0.67, 1)` | background-color, border-color, box-shadow, color | auth-lang, auth-next, auth-signup, e-cta, help-button, hero-cta, m-cta, m-nav-item and more |
| 0.1s | `ease` | all | assistant |
| 0.15s | `cubic-bezier(0.4, 0, 1, 1)` | backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, stroke, transform | buy-now, contact-sales, see-all |
| 0.15s | `ease` | transform | sg-color |
| 0.15s | `ease-in-out` | color | blog-card, footer-link, menu-link |
| 0.2s | `ease` | all, box-shadow | sg-clear, sg-color, sg-field, sg-font, sg-tab-draw, sg-tab-type |
| 0.2s | `ease-in-out` | border-color | hero-field, trial-field |
| 0.3s | `ease` | all | sg-download |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Trial form band](#trial-form-band) | 1408 x 303 | - | - | transparent | none | 0px 0px 24px 0px |
| [Plan card](#plan-card) | 301 x 922.2 | 1px solid rgba(19, 0, 50, 0.5) `color.ink-50` | 16px | #ffffff `color.white` | none | 0 |
| [Login card](#login-card) | 556 x 439.59 | 1px solid rgba(25, 24, 35, 0.15) `color.hairline-auth` | 4px | #ffffff `color.white` | none | 64px 0px |
| [Story card](#story-card) | 328 x 445.75 | - | 4px | transparent | none | 0 |
| [Video dialog](#video-dialog) | 1440 x 900 | - | - | rgba(19, 0, 50, 0.898) `color.scrim` | none | 0 |
| [Nav dropdown](#nav-dropdown) | 1360 x 379 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The marketing chrome: the 30px deep-violet utility strip, the 69px white header with the Products/Solutions/Resources mega-menu triggers, uppercase text actions and the cobalt Try-for-free pill.

#### Utility bar
The top strip over the main nav: the announcement link, sales phone, Search, Support, Access Documents and Log In. Read as `utilitynav` on the home page.

**Values (default).** size 1440 x 30; background transparent; text DSIndigo 12/18 500, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white`; layers div.css-1qdnkw1.e1p96sfz1 1440.0x30.0 rgb(38, 6, 93); a::before.css-8vbptu.e1tasy2f0 23.5pxx14px rgb(203, 194, 255) T:1px solid rgb(203, 194, 255) 4px; div::after.css-g4mfjf.e1tasy2f1 0pxx1px rgb(255, 255, 255); div::after.css-g4mfjf.e1tasy2f1 0pxx1px rgb(255, 255, 255); div::after.css-g4mfjf.e1tasy2f1 0pxx1px rgb(255, 255, 255); div::after.css-g4mfjf.e1tasy2f1 0pxx1px rgb(255, 255, 255).

Child layers that carry the look: div 1440x30 background #26065d `color.deep-violet`; a::before 23.5pxx14px background #cbc2ff `color.mist` border 1px solid #cbc2ff `color.mist` radius 4px; div::after 0pxx1px background #ffffff `color.white`.

![Utility bar default](components/crops/utilitynav-default.png)

#### Header
The primary nav inside the sticky chrome: wordmark, the Products/Solutions/Resources dropdown triggers, Enterprise and Plans & Pricing links, and the Contact-sales/Buy-now/Try-for-free actions. Read as `header` on the home page.

**Values (default).** size 1440 x 69; background #ffffff `color.white`; text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`.

![Header default](components/crops/header-default.png)

#### Logo
The Docusign wordmark anchor (aria-label "Docusign"). Read as `logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 132 x 26.55; radius 4px; background transparent; text DSIndigo 16/24 500, #0000ee; layers div::after.css-1ra4uzk.e1tasy2f1 0pxx1px rgb(76, 0, 255) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers a.css-dmyhku.e1tasy2f0 132.0x26.5 2px solid rgb(76, 0, 255) offset 2px 4px; div::after.css-1ra4uzk.e1tasy2f1 0pxx1px rgb(76, 0, 255) |
| pressed | text DSIndigo 16/24 500, #ff0000; layers div::after.css-1ra4uzk.e1tasy2f1 0pxx1px rgb(19, 0, 50) |

Child layers that carry the look: div::after 0pxx1px background #4c00ff `color.cobalt`.

![Logo default](components/crops/logo-default.png) ![Logo hover](components/crops/logo-hover.png) ![Logo focus-visible](components/crops/logo-focus-visible.png) ![Logo pressed](components/crops/logo-pressed.png)

#### Nav trigger
The Products button that opens the full-width mega-menu; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 75.73 x 69; padding 24px 0px; radius 4px; background transparent; text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; icon 16 x 16, rgba(19, 0, 50, 0.75) `color.ink-75`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | layers ::after rgb(76, 0, 255) 0px none 1; button::after.css-qscr5r 75.7344pxx2px rgb(76, 0, 255) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers ::after rgb(76, 0, 255) 0px none 1; button.css-qscr5r 75.7x69.0 2px solid rgb(76, 0, 255) offset 2px 4px; button::after.css-qscr5r 75.7344pxx2px rgb(76, 0, 255) |
| pressed | layers ::after rgb(76, 0, 255) 0px none 1; button::after.css-qscr5r 75.7344pxx2px rgb(76, 0, 255) |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The plain Plans-&-Pricing header link. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 95.61 x 69; padding 24px 0px; radius 4px; background transparent; text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; layers ::after rgba(0, 0, 0, 0) 0px none 1; div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75) |
| hover | layers ::after rgb(76, 0, 255) 0px none 1; a::after.css-17gi7l6.e1tasy2f0 95.6094pxx2px rgb(76, 0, 255); div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers ::after rgb(76, 0, 255) 0px none 1; a.css-17gi7l6.e1tasy2f0 95.6x69.0 2px solid rgb(76, 0, 255) offset 2px 4px; a::after.css-17gi7l6.e1tasy2f0 95.6094pxx2px rgb(76, 0, 255); div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75) |
| pressed | layers ::after rgb(76, 0, 255) 0px none 1; a::after.css-17gi7l6.e1tasy2f0 95.6094pxx2px rgb(76, 0, 255); div::after.css-1eg020q.e1tasy2f1 0pxx1px rgb(19, 0, 50) |

Child layers that carry the look: div::after 0pxx1px background rgba(19, 0, 50, 0.75) `color.ink-75`.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Contact-sales link
The uppercase Contact-sales text action; measured never followed. Read as `nav-contact` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 145.83 x 45; padding 12px 16px; radius 8px; background transparent; text DSIndigo 14/21 600, #4c00ff `color.cobalt`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1); layers a.css-5lds31.evij40y0 145.8x45.0 rgba(0, 0, 0, 0) 0px 0px 0px 1px inset 8px |
| hover | shadow rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset; layers a.css-5lds31.evij40y0 145.8x45.0 rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset 8px |
| focus-visible | shadow rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset; outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers a.css-5lds31.evij40y0 145.8x45.0 rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset 2px solid rgb(76, 0, 255) offset 2px 8px |
| pressed | shadow rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset; layers a.css-5lds31.evij40y0 145.8x45.0 rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset 8px |

![Contact-sales link default](components/crops/nav-contact-default.png) ![Contact-sales link hover](components/crops/nav-contact-hover.png) ![Contact-sales link focus-visible](components/crops/nav-contact-focus-visible.png) ![Contact-sales link pressed](components/crops/nav-contact-pressed.png)

#### Buy-now link
The uppercase Buy-now text action; measured never followed. Read as `nav-buy` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.14 x 45; padding 12px 16px; radius 8px; background transparent; text DSIndigo 14/21 600, #4c00ff `color.cobalt`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1); layers a.css-5lds31.evij40y0 97.1x45.0 rgba(0, 0, 0, 0) 0px 0px 0px 1px inset 8px |
| hover | shadow rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset; layers a.css-5lds31.evij40y0 97.1x45.0 rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset 8px |
| focus-visible | shadow rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset; outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers a.css-5lds31.evij40y0 97.1x45.0 rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset 2px solid rgb(76, 0, 255) offset 2px 8px |
| pressed | shadow rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset; layers a.css-5lds31.evij40y0 97.1x45.0 rgba(19, 0, 50, 0.15) 0px 0px 0px 1px inset 8px |

![Buy-now link default](components/crops/nav-buy-default.png) ![Buy-now link hover](components/crops/nav-buy-hover.png) ![Buy-now link focus-visible](components/crops/nav-buy-focus-visible.png) ![Buy-now link pressed](components/crops/nav-buy-pressed.png)

#### Try-for-free CTA
The filled purple Try-for-free pill; measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128.09 x 45; padding 12px 16px; radius 8px; background #4c00ff `color.cobalt`; text DSIndigo 14/21 600, #ffffff `color.white`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1) |
| hover | background #4000cc `color.cobalt-hover` |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px |
| pressed | background #4000cc `color.cobalt-hover` |

![Try-for-free CTA default](components/crops/nav-cta-default.png) ![Try-for-free CTA hover](components/crops/nav-cta-hover.png) ![Try-for-free CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Try-for-free CTA pressed](components/crops/nav-cta-pressed.png)

#### Search button
The Search button in the utility bar. Read as `nav-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 39.33 x 18; radius 4px; background transparent; text DSIndigo 12/18 500, #ffffff `color.white` |
| hover | text DSIndigo 12/18 500, #cbc2ff `color.mist` |
| focus-visible | outline 2px solid #cbc2ff `color.mist`, offset 2px; text DSIndigo 12/18 500, #cbc2ff `color.mist`; layers button.css-1jjw43b 39.3x18.0 2px solid rgb(203, 194, 255) offset 2px 4px |
| pressed | text DSIndigo 12/18 500, #cbc2ff `color.mist` |

![Search button default](components/crops/nav-search-default.png) ![Search button hover](components/crops/nav-search-hover.png) ![Search button focus-visible](components/crops/nav-search-focus-visible.png) ![Search button pressed](components/crops/nav-search-pressed.png)

#### Log-in link
The utility-bar Log In link; measured never followed. Read as `login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 33.83 x 18; radius 4px; background transparent; text DSIndigo 12/18 500, #ffffff `color.white`; layers div::after.css-g4mfjf.e1tasy2f1 0pxx1px rgb(255, 255, 255) |
| hover | text DSIndigo 12/18 500, #cbc2ff `color.mist` |
| focus-visible | outline 2px solid #cbc2ff `color.mist`, offset 2px; text DSIndigo 12/18 500, #cbc2ff `color.mist`; layers a.css-121l1fb.e1tasy2f0 33.8x18.0 2px solid rgb(203, 194, 255) offset 2px 4px; div::after.css-g4mfjf.e1tasy2f1 0pxx1px rgb(255, 255, 255) |
| pressed | text DSIndigo 12/18 500, #cbc2ff `color.mist`; layers div::after.css-g4mfjf.e1tasy2f1 0pxx1px rgba(255, 255, 255, 0.8) |

Child layers that carry the look: div::after 0pxx1px background #ffffff `color.white`.

![Log-in link default](components/crops/login-link-default.png) ![Log-in link hover](components/crops/login-link-hover.png) ![Log-in link focus-visible](components/crops/login-link-focus-visible.png) ![Log-in link pressed](components/crops/login-link-pressed.png)

#### Nav dropdown
The Products mega-menu panel, opened by its own trigger (a full-width white sheet). Read as `nav-dropdown` on the home page.

**Values (default).** size 1360 x 379; background transparent; text DSIndigo 18/27 500, #130032 `color.inkwell`; icon 16 x 16, #4c00ff `color.cobalt`; layers span.css-11bm945 885.3x40.0 B:1px solid rgb(203, 194, 255); div::after.css-aknfkn.e1tasy2f1 0pxx1px rgb(19, 0, 50); div::after.css-aknfkn.e1tasy2f1 0pxx1px rgb(19, 0, 50); div::after.css-aknfkn.e1tasy2f1 0pxx1px rgb(19, 0, 50); div::after.css-aknfkn.e1tasy2f1 0pxx1px rgb(19, 0, 50); div::after.css-aknfkn.e1tasy2f1 0pxx1px rgb(19, 0, 50).

Child layers that carry the look: span 885.3x40 border 1px solid #cbc2ff `color.mist`; div::after 0pxx1px background #130032 `color.inkwell`; div::after 0pxx1px background #130032 `color.inkwell`.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A product link inside the opened mega-menu (bold label over a grey description). Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 410.67 x 47; radius 4px; background transparent; text DSIndigo 16/24 500, #130032 `color.inkwell`; transition color 0.15s ease-in-out; layers div::after.css-aknfkn.e1tasy2f1 0pxx1px rgb(19, 0, 50) |
| hover | text DSIndigo 16/24 500, #4c00ff `color.cobalt`; layers div::after.css-aknfkn.e1tasy2f1 100%x1px rgb(19, 0, 50) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; text DSIndigo 16/24 500, #4c00ff `color.cobalt`; layers a.css-1itjty0.e1tasy2f0 410.7x47.0 2px solid rgb(76, 0, 255) offset 2px 4px; div::after.css-aknfkn.e1tasy2f1 0pxx1px rgb(19, 0, 50) |
| pressed | text DSIndigo 16/24 500, #4c00ff `color.cobalt`; layers div::after.css-aknfkn.e1tasy2f1 100%x1px rgb(19, 0, 50) |

Child layers that carry the look: div::after 0pxx1px background #130032 `color.inkwell`.

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home hero

The deep-violet home hero: the 80px weight-300 headline, the email-capture field and the inkwell Get-Started button.

#### Hero section
The painted #26065d deep-purple hero band. Read as `hero-section` on the home page.

**Values (default).** size 1440 x 570.39; padding 96px 80px 80px 80px; background transparent; image radial-gradient(100% 100% at 50% 0%, #4c00ff `color.cobalt` 0%, #26065d `color.deep-violet` 100%); text DSIndigo 80/86.4 300, #ffffff `color.white`; icon 14.4 x 14.4, #ffffff `color.white`.

![Hero section default](components/crops/hero-section-default.png)

#### Hero headline
The 80px DSIndigo-300 white headline on the purple band. Read as `hero-title` on the home page.

**Values (default).** size 990.56 x 86.39; background transparent; text DSIndigo 80/86.4 300, #ffffff `color.white`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the hero headline. Read as `hero-lede` on the home page.

**Values (default).** size 412.02 x 27; background transparent; text DSIndigo 18/27 400, #ffffff `color.white`.

![Hero copy default](components/crops/hero-lede-default.png)

#### Hero CTA
The filled Get-Started pill in the hero; measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 119.47 x 61; padding 12px 16px; radius 0px 8px 8px 0px; background #130032 `color.inkwell`; text DSIndigo 16/24 500, #ffffff `color.white`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1) |
| focus-visible | outline 2px solid #ffffff `color.white`, offset 2px |
| pressed | background #4e4067 `color.inkwell-hover` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero link
The Explore-Docusign-IAM arrow link under the hero CTA; measured never followed. Read as `hero-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 171.95 x 24; radius 4px; background transparent; text DSIndigo 16/24 500, #4c00ff `color.cobalt`; icon 16 x 16, #4c00ff `color.cobalt`; layers span::after.css-n219vx.e201y4g1 0pxx1px rgb(76, 0, 255) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers a.css-1bhha0e.e201y4g0 172.0x24.0 2px solid rgb(76, 0, 255) offset 2px 4px; span::after.css-n219vx.e201y4g1 0pxx1px rgb(76, 0, 255) |
| pressed | text DSIndigo 16/24 500, #130032 `color.inkwell`; icon 16 x 16, #130032 `color.inkwell`; layers span::after.css-n219vx.e201y4g1 0pxx1px rgb(19, 0, 50) |

Child layers that carry the look: span::after 0pxx1px background #4c00ff `color.cobalt`.

![Hero link default](components/crops/hero-link-default.png) ![Hero link hover](components/crops/hero-link-hover.png) ![Hero link focus-visible](components/crops/hero-link-focus-visible.png) ![Hero link pressed](components/crops/hero-link-pressed.png)

#### Hero email field
The hero work-email input on the purple band; sample text was typed and deleted, nothing sent. Read as `hero-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 472.53 x 61; padding 24px 16px 8px 16px; border 1px solid rgba(19, 0, 50, 0.15) `color.ink-15`; radius 8px 0px 0px 8px; background #ffffff `color.white`; text DSIndigo 18/27 400, #130032 `color.inkwell`; transition border-color 0.2s ease-in-out; placeholder #130032 `color.inkwell` |
| focused, filled | border 1px solid #4c00ff `color.cobalt`; shadow #4c00ff 0px 0px 0px 1px inset |

![Hero email field default](components/crops/hero-field-default.png) ![Hero email field focused](components/crops/hero-field-focused.png) ![Hero email field filled](components/crops/hero-field-filled.png)

#### Hero consent checkbox
The painted square of the marketing-opt-in checkbox on the purple band (the real input is a 1x1 inside it); measured, never toggled on this surface. Read as `hero-checkbox` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 592 x 37; background transparent; text DSIndigo 12/18 400, #ffffff `color.white`; layers span.styledCheckbox.css-ci2u9i 20.0x20.0 T:2px solid rgba(255, 255, 255, 0.35) / R:2px solid rgba(255, 255, 255, 0.35) / B:2px solid rgba(255, 255, 255, 0.35) / L:2px solid rgba(255, 255, 255, 0.35) 2px |
| hover | layers span.styledCheckbox.css-ci2u9i 20.0x20.0 T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 2px; span::before.styledCheckbox.css-ci2u9i 32pxx32px rgba(19, 0, 50, 0.15) 4px |
| focus-visible | layers input.css-5w2lwp 1.0x1.0 1px auto rgb(0, 95, 204) offset 2px; span.styledCheckbox.css-ci2u9i 20.0x20.0 T:2px solid rgba(255, 255, 255, 0.35) / R:2px solid rgba(255, 255, 255, 0.35) / B:2px solid rgba(255, 255, 255, 0.35) / L:2px solid rgba(255, 255, 255, 0.35) 2px solid rgb(203, 194, 255) offset 4px 2px |
| pressed | layers span.styledCheckbox.css-ci2u9i 20.0x20.0 T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255) 2px; span::before.styledCheckbox.css-ci2u9i 32pxx32px rgba(19, 0, 50, 0.15) 4px |

Child layers that carry the look: span 20x20 border 2px solid rgba(255, 255, 255, 0.35) radius 2px.

![Hero consent checkbox default](components/crops/hero-checkbox-default.png) ![Hero consent checkbox hover](components/crops/hero-checkbox-hover.png) ![Hero consent checkbox focus-visible](components/crops/hero-checkbox-focus-visible.png) ![Hero consent checkbox pressed](components/crops/hero-checkbox-pressed.png)

#### Country picker
The Country/region labelled control under the hero form (a native select at opacity 0 inside its painted label; reads Singapore on this vantage); measured, never opened. Read as `hero-country` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 189.5 x 21; padding 0px 3.2px; background transparent; text DSIndigo 14/21 400, #ffffff `color.white`; icon 14.4 x 14.4, #ffffff `color.white`; layers select.fs-mask.css-p8qupu 189.5x22.0 rgb(255, 255, 255) T:1px solid rgb(118, 118, 118) / R:1px solid rgb(118, 118, 118) / B:1px solid rgb(118, 118, 118) / L:1px solid rgb(118, 118, 118) |
| focus-visible | radius 4px; shadow #cbc2ff 0px 0px 0px 2px; layers label.elk0b8n0.css-iao6pr 189.5x21.0 rgb(203, 194, 255) 0px 0px 0px 2px 4px; select.fs-mask.css-p8qupu 189.5x22.0 rgb(255, 255, 255) T:1px solid rgb(118, 118, 118) / R:1px solid rgb(118, 118, 118) / B:1px solid rgb(118, 118, 118) / L:1px solid rgb(118, 118, 118) 1px auto rgb(0, 95, 204) offset 0px |

Child layers that carry the look: select 189.5x22 background #ffffff `color.white` border 1px solid #767676.

![Country picker default](components/crops/hero-country-default.png) ![Country picker hover](components/crops/hero-country-hover.png) ![Country picker focus-visible](components/crops/hero-country-focus-visible.png) ![Country picker pressed](components/crops/hero-country-pressed.png)

### Home

Sections of the home page: the 58px section headings, the card links and the floating Docusign Assistant launcher.

#### Section heading
A marketing section h2 (DSIndigo). Read as `h2-section` on the home page.

**Values (default).** size 1080 x 62.63; background transparent; image linear-gradient(97.84deg, #4c00ff `color.cobalt` -38.62%, #ff5252 `color.poppy` 141.03%); text DSIndigo 58/62.64 300, #130032 `color.inkwell`.

![Section heading default](components/crops/h2-section-default.png)

#### Card link
A marketing card link (blog-teaser or resource card); measured never followed. Read as `blog-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 184 x 24; radius 4px; background transparent; text DSIndigo 14/21 500, #130032 `color.inkwell`; transition color 0.15s ease-in-out; layers div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75) |
| hover | text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; layers div::after.css-1eg020q.e1tasy2f1 100%x1px rgba(19, 0, 50, 0.75) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; layers a.css-1po7wbl.e1tasy2f0 184.0x24.0 2px solid rgb(76, 0, 255) offset 2px 4px; div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75) |
| pressed | text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; layers div::after.css-1eg020q.e1tasy2f1 100%x1px rgb(19, 0, 50) |

Child layers that carry the look: div::after 0pxx1px background rgba(19, 0, 50, 0.75) `color.ink-75`.

![Card link default](components/crops/blog-card-default.png) ![Card link hover](components/crops/blog-card-hover.png) ![Card link focus-visible](components/crops/blog-card-focus-visible.png) ![Card link pressed](components/crops/blog-card-pressed.png)

#### Assistant launcher
The floating Docusign-Assistant chat pill; measured, never opened. Read as `assistant` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 227.59 x 54; padding 16px 24px; border 1px solid #4014ea `color.assistant`; radius 9999px; background #4014ea `color.assistant`; shadow rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px; text -apple-system 16/normal 700, #ffffff `color.white`; transition all 0.1s ease; icon 20 x 20, #ffffff `color.white` |
| hover | background #ffffff `color.white`; text -apple-system 16/normal 700, #4014ea `color.assistant`; icon 20 x 20, #4014ea `color.assistant` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Assistant launcher default](components/crops/assistant-default.png) ![Assistant launcher hover](components/crops/assistant-hover.png)

### eSignature page

The /products/electronic-signature page: its 48px display heading, the customer-story video dialog and the FAQ accordion.

#### eSignature title
The product page display heading. Read as `e-title` on the eSignature page.

**Values (default).** size 948 x 103.66; background transparent; text DSIndigo 48/51.84 300, #130032 `color.inkwell`.

![eSignature title default](components/crops/e-title-default.png)

#### eSignature CTA
A plan/trial call to action; measured never followed. Read as `e-cta` on the eSignature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128.09 x 45; padding 12px 16px; radius 8px; background #4c00ff `color.cobalt`; text DSIndigo 14/21 600, #ffffff `color.white`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1) |
| hover | background #4000cc `color.cobalt-hover` |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px |
| pressed | background #4000cc `color.cobalt-hover` |

![eSignature CTA default](components/crops/e-cta-default.png) ![eSignature CTA hover](components/crops/e-cta-hover.png) ![eSignature CTA focus-visible](components/crops/e-cta-focus-visible.png) ![eSignature CTA pressed](components/crops/e-cta-pressed.png)

#### Video expand button
An expand-video icon button on a customer-story tile; one was pressed to open the dialog below. Read as `video-expand` on the eSignature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 816 x 459; background transparent; text DSIndigo 13.33/normal 400, #000000 `color.black`; icon 24 x 24, #ffffff `color.white`; layers span.css-1p8odxa.e1nf4qrp1 40.0x40.0 rgba(19, 0, 50, 0.25) 100% |
| hover | layers span.css-1p8odxa.e1nf4qrp1 40.0x40.0 rgb(76, 0, 255) 100% |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers button.css-8mph9b.e1nf4qrp0 816.0x459.0 2px solid rgb(76, 0, 255) offset 2px; span.css-1p8odxa.e1nf4qrp1 40.0x40.0 rgb(76, 0, 255) 100% |
| pressed | layers span.css-1p8odxa.e1nf4qrp1 40.0x40.0 rgb(76, 0, 255) 100% |

Child layers that carry the look: span 40x40 background rgba(19, 0, 50, 0.25) radius 100%.

![Video expand button default](components/crops/video-expand-default.png) ![Video expand button hover](components/crops/video-expand-hover.png) ![Video expand button focus-visible](components/crops/video-expand-focus-visible.png) ![Video expand button pressed](components/crops/video-expand-pressed.png)

#### Video dialog
The modal a video Expand button opens (scrim + framed player); opened and closed with the product's own controls. Read as `video-dialog` on the eSignature page.

**Values (default).** size 1440 x 900; background rgba(19, 0, 50, 0.898) `color.scrim`; text DSIndigo 16/normal 400, #130032 `color.inkwell`; opacity 0.9.

![Video dialog default](components/crops/video-dialog-default.png)

#### FAQ row
A collapsed FAQ accordion row in the page footer; toggled open once for the panel below. Read as `faq-button` on the eSignature page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1280 x 93.75; padding 32px 0px; background transparent; text DSIndigo 24/29.76 500, #130032 `color.inkwell`; icon 16 x 16, #130032 `color.inkwell` |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 0px; layers button.css-1yg0mla.e1mn5vlf1 1280.0x93.8 2px solid rgb(76, 0, 255) offset 0px |

![FAQ row default](components/crops/faq-button-default.png) ![FAQ row hover](components/crops/faq-button-hover.png) ![FAQ row focus-visible](components/crops/faq-button-focus-visible.png) ![FAQ row pressed](components/crops/faq-button-pressed.png)

#### FAQ row, open
The same accordion row after its own toggle (aria-expanded). Read as `faq-open` on the eSignature page.

**Values (default).** size 1280 x 93.75; padding 32px 0px; background transparent; text DSIndigo 24/29.76 500, #130032 `color.inkwell`; icon 16 x 16, #130032 `color.inkwell`.

![FAQ row, open default](components/crops/faq-open-default.png)

#### FAQ panel
The answer text revealed under an open FAQ row. Read as `faq-panel` on the eSignature page.

**Values (default).** size 1280 x 165.75; background transparent; text DSIndigo 24/29.76 500, #130032 `color.inkwell`; icon 16 x 16, #130032 `color.inkwell`.

![FAQ panel default](components/crops/faq-panel-default.png)

### Free trial

The /free-trial form band: floating-label fields, the consent checkbox and the cobalt Get-Started submit — measured, never submitted.

#### Trial form band
The painted free-trial form band; never submitted. Read as `trial-card` on the free trial page.

**Values (default).** size 1408 x 303; padding 0px 0px 24px 0px; background transparent; text DSIndigo 40/48 400, #130032 `color.inkwell`; layers input.fs-mask.css-1czprqx 488.0x61.0 rgb(255, 255, 255) T:1px solid rgba(19, 0, 50, 0.15) / R:1px solid rgba(19, 0, 50, 0.15) / B:1px solid rgba(19, 0, 50, 0.15) / L:1px solid rgba(19, 0, 50, 0.15) 8px; span.styledCheckbox.css-lnan8r 20.0x20.0 T:2px solid rgba(19, 0, 50, 0.15) / R:2px solid rgba(19, 0, 50, 0.15) / B:2px solid rgba(19, 0, 50, 0.15) / L:2px solid rgba(19, 0, 50, 0.15) 2px.

Child layers that carry the look: input 488x61 background #ffffff `color.white` border 1px solid rgba(19, 0, 50, 0.15) `color.ink-15` radius 8px; span 20x20 border 2px solid rgba(19, 0, 50, 0.15) `color.ink-15` radius 2px.

![Trial form band default](components/crops/trial-card-default.png)

#### Work-email field
The work-email input; sample text was typed and deleted, nothing sent. Read as `trial-field` on the free trial page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 488 x 61; padding 24px 16px 8px 16px; border 1px solid rgba(19, 0, 50, 0.15) `color.ink-15`; radius 8px; background #ffffff `color.white`; text DSIndigo 18/27 400, #130032 `color.inkwell`; transition border-color 0.2s ease-in-out; placeholder #130032 `color.inkwell` |
| focused, filled | border 1px solid #4c00ff `color.cobalt`; shadow #4c00ff 0px 0px 0px 1px inset |

![Work-email field default](components/crops/trial-field-default.png) ![Work-email field focused](components/crops/trial-field-focused.png) ![Work-email field filled](components/crops/trial-field-filled.png)

#### Consent checkbox
The painted square of the opt-in marketing checkbox (the real input is a 1x1 inside it); measured, never toggled. Read as `trial-checkbox` on the free trial page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 805.5 x 24; background transparent; text DSIndigo 12/18 400, #130032 `color.inkwell`; layers span.styledCheckbox.css-lnan8r 20.0x20.0 T:2px solid rgba(19, 0, 50, 0.15) / R:2px solid rgba(19, 0, 50, 0.15) / B:2px solid rgba(19, 0, 50, 0.15) / L:2px solid rgba(19, 0, 50, 0.15) 2px |
| hover | layers span.styledCheckbox.css-lnan8r 20.0x20.0 T:2px solid rgb(19, 0, 50) / R:2px solid rgb(19, 0, 50) / B:2px solid rgb(19, 0, 50) / L:2px solid rgb(19, 0, 50) 2px; span::before.styledCheckbox.css-lnan8r 32pxx32px rgba(19, 0, 50, 0.15) 4px |
| focus-visible | layers input.css-xrchdt 1.0x1.0 1px auto rgb(0, 95, 204) offset 2px; span.styledCheckbox.css-lnan8r 20.0x20.0 T:2px solid rgba(19, 0, 50, 0.15) / R:2px solid rgba(19, 0, 50, 0.15) / B:2px solid rgba(19, 0, 50, 0.15) / L:2px solid rgba(19, 0, 50, 0.15) 2px solid rgb(76, 0, 255) offset 4px 2px |
| pressed | layers span.styledCheckbox.css-lnan8r 20.0x20.0 T:2px solid rgb(19, 0, 50) / R:2px solid rgb(19, 0, 50) / B:2px solid rgb(19, 0, 50) / L:2px solid rgb(19, 0, 50) 2px; span::before.styledCheckbox.css-lnan8r 32pxx32px rgba(19, 0, 50, 0.15) 4px |

Child layers that carry the look: span 20x20 border 2px solid rgba(19, 0, 50, 0.15) `color.ink-15` radius 2px.

![Consent checkbox default](components/crops/trial-checkbox-default.png) ![Consent checkbox hover](components/crops/trial-checkbox-hover.png) ![Consent checkbox focus-visible](components/crops/trial-checkbox-focus-visible.png) ![Consent checkbox pressed](components/crops/trial-checkbox-pressed.png)

#### Trial submit
The Get-Started submit button; measured, never pressed (a press submits the form). Read as `trial-cta` on the free trial page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 488 x 40; padding 4px 12px; radius 4px; background #4c00ff `color.cobalt`; text DSIndigo 16/24 500, #ffffff `color.white`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1) |
| hover | background #4000cc `color.cobalt-hover` |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px |
| pressed | background #4000cc `color.cobalt-hover` |

![Trial submit default](components/crops/trial-cta-default.png) ![Trial submit hover](components/crops/trial-cta-hover.png) ![Trial submit focus-visible](components/crops/trial-cta-focus-visible.png) ![Trial submit pressed](components/crops/trial-cta-pressed.png)

#### Help button
The floating Help launcher; measured, never opened. Read as `help-button` on the free trial page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.61 x 40; padding 12px 16px; radius 8px; background #ffffff `color.white`; text DSIndigo 16/24 500, #130032 `color.inkwell`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1); icon 16 x 16, #130032 `color.inkwell` |
| hover | background #f8f3f0 `color.ecru` |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px |
| pressed | background #f8f3f0 `color.ecru` |

![Help button default](components/crops/help-button-default.png) ![Help button hover](components/crops/help-button-hover.png) ![Help button focus-visible](components/crops/help-button-focus-visible.png) ![Help button pressed](components/crops/help-button-pressed.png)

### Signature generator

The /signature-generator app on its ecru ground: Draw/Type tabs, the signature canvas, colour swatches, script-face picker and mist Download buttons — the only surface that declares a token layer.

#### Generator title
The signature-generator display heading. Read as `sg-title` on the signature generator page.

**Values (default).** size 864 x 155.5; background transparent; text DS Indigo 72/77.76 300, #130032 `color.inkwell`.

![Generator title default](components/crops/sg-title-default.png)

#### Draw tab
The Draw half of the Draw/Type mode toggle. Read as `sg-tab-draw` on the signature generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 122.72 x 45; padding 12px 32px; border 1px solid #cbc2ff `color.mist`; radius 6px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.04) 0px 1px 3px 0px; text DS Indigo 14/normal 500, #4c00ff `color.cobalt`; transition all 0.2s ease; icon 16 x 16, #4c00ff `color.cobalt` |
| focus-visible | outline 1px auto #005fcc `color.focus-auto`, offset 0px |

![Draw tab default](components/crops/sg-tab-draw-default.png) ![Draw tab hover](components/crops/sg-tab-draw-hover.png) ![Draw tab focus-visible](components/crops/sg-tab-draw-focus-visible.png) ![Draw tab pressed](components/crops/sg-tab-draw-pressed.png)

#### Type tab
The Type half of the mode toggle; its own click revealed the name field below. Read as `sg-tab-type` on the signature generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 119.48 x 45; padding 12px 32px; border 1px solid transparent; radius 6px; background transparent; text DS Indigo 14/normal 500, #130032 `color.inkwell`; transition all 0.2s ease; icon 16 x 16, #130032 `color.inkwell` |
| hover | text DS Indigo 14/normal 500, #4c00ff `color.cobalt`; icon 16 x 16, #4c00ff `color.cobalt` |
| focus-visible | outline 1px auto #005fcc `color.focus-auto`, offset 0px |
| pressed | text DS Indigo 14/normal 500, #4c00ff `color.cobalt`; icon 16 x 16, #4c00ff `color.cobalt` |

![Type tab default](components/crops/sg-tab-type-default.png) ![Type tab hover](components/crops/sg-tab-type-hover.png) ![Type tab focus-visible](components/crops/sg-tab-type-focus-visible.png) ![Type tab pressed](components/crops/sg-tab-type-pressed.png)

#### Signature canvas
The signature preview surface in Draw mode. Read as `sg-canvas` on the signature generator page.

**Values (default).** size 888 x 260; background transparent; text DSIndigo 16/normal 400, #130032 `color.inkwell`.

![Signature canvas default](components/crops/sg-canvas-default.png)

#### Colour swatch
A signature colour swatch button (Cobalt), read at rest, hovered, focused and pressed; never selected here. Read as `sg-color` on the signature generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 1px 6px; radius 50%; background #4c00ff `color.cobalt`; text DSIndigo 13.33/normal 400, #000000 `color.black`; transition transform 0.15s ease, box-shadow 0.2s ease |
| hover | size 35.2 x 35.2; transform scale(1.1) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px |
| pressed | size 30.4 x 30.4; transform scale(0.95) |

![Colour swatch default](components/crops/sg-color-default.png) ![Colour swatch hover](components/crops/sg-color-hover.png) ![Colour swatch focus-visible](components/crops/sg-color-focus-visible.png) ![Colour swatch pressed](components/crops/sg-color-pressed.png)

#### Clear button
The Clear action on the draw canvas. Read as `sg-clear` on the signature generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83.48 x 35; padding 8px 12px; radius 8px; background transparent; text DS Indigo 14/normal 500, rgba(38, 6, 93, 0.3) `color.violet-30`; transition all 0.2s ease; icon 18 x 18, rgba(38, 6, 93, 0.3) `color.violet-30` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Clear button default](components/crops/sg-clear-default.png) ![Clear button hover](components/crops/sg-clear-hover.png) ![Clear button pressed](components/crops/sg-clear-pressed.png)

#### Download button
The Download-as-PNG action; measured, never pressed (a press downloads a file). Read as `sg-download` on the signature generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 438 x 48; padding 0px 24px; radius 8px; background #cbc2ff `color.mist`; text DS Indigo 16/normal 500, rgba(38, 6, 93, 0.5) `color.violet-50`; transition all 0.3s ease; icon 18 x 18, rgba(38, 6, 93, 0.5) `color.violet-50` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Download button default](components/crops/sg-download-default.png) ![Download button hover](components/crops/sg-download-hover.png) ![Download button pressed](components/crops/sg-download-pressed.png)

#### Name field
The "Your name" input in Type mode; a sample name (Alex Sample) was typed to render the script previews, nothing sent. Read as `sg-field` on the signature generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 888 x 52; padding 0px 16px; border 1px solid #cbc2ff `color.mist`; radius 8px; background #ffffff `color.white`; text DS Indigo 16/normal 400, #130032 `color.inkwell`; transition all 0.2s ease; placeholder rgba(38, 6, 93, 0.4) |
| focused | border 1px solid #4c00ff `color.cobalt`; shadow rgba(76, 0, 255, 0.1) 0px 0px 0px 3px |

![Name field default](components/crops/sg-field-default.png) ![Name field focused](components/crops/sg-field-focused.png)

#### Script-face option
A signature script-face picker option (The Curator et al.); toggled, which re-renders the preview. Read as `sg-font` on the signature generator page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 438 x 85; padding 14px 16px 16px 16px; border 1px solid #4c00ff `color.cobalt`; radius 8px; background #ffffff `color.white`; text DS Indigo 11/normal 400, rgba(38, 6, 93, 0.5) `color.violet-50`; transition all 0.2s ease; icon 12 x 12, #ffffff `color.white` |
| focus-visible | outline 1px auto #005fcc `color.focus-auto`, offset 0px |

![Script-face option default](components/crops/sg-font-default.png) ![Script-face option hover](components/crops/sg-font-hover.png) ![Script-face option focus-visible](components/crops/sg-font-focus-visible.png) ![Script-face option pressed](components/crops/sg-font-pressed.png)

### Customer stories

The /customer-stories index: filter dropdowns, story cards and logo tiles.

#### Stories title
The customer-stories page heading. Read as `st-title` on the customer stories page.

**Values (default).** size 123.89 x 56; padding 16px 0px; background transparent; text DSIndigo 16/24 500, #130032 `color.inkwell`; layers span::after.css-oa7nr3.e1kahpgs1 0%x1px rgb(76, 0, 255).

Child layers that carry the look: span::after 0%x1px background #4c00ff `color.cobalt`.

![Stories title default](components/crops/st-title-default.png)

#### Filter dropdown
A stories filter dropdown trigger (Products used/Industry/Department); measured, never opened. Read as `filter-button` on the customer stories page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.02 x 53; padding 16px 0px; radius 4px; background transparent; text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; icon 16 x 16, rgba(19, 0, 50, 0.75) `color.ink-75`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | layers ::after rgb(76, 0, 255) 0px none 1; button::after.css-1lg64h2.e1fdzuzw15 97.0156pxx2px rgb(76, 0, 255) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers ::after rgb(76, 0, 255) 0px none 1; button.css-1lg64h2.e1fdzuzw15 97.0x53.0 2px solid rgb(76, 0, 255) offset 2px 4px; button::after.css-1lg64h2.e1fdzuzw15 97.0156pxx2px rgb(76, 0, 255) |
| pressed | layers ::after rgb(76, 0, 255) 0px none 1; button::after.css-1lg64h2.e1fdzuzw15 97.0156pxx2px rgb(76, 0, 255) |

![Filter dropdown default](components/crops/filter-button-default.png) ![Filter dropdown hover](components/crops/filter-button-hover.png) ![Filter dropdown focus-visible](components/crops/filter-button-focus-visible.png) ![Filter dropdown pressed](components/crops/filter-button-pressed.png)

#### Story card
A customer-story card link; measured never followed. Read as `story-card` on the customer stories page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 328 x 445.75; radius 4px; background transparent; text DSIndigo 24/29.76 500, #130032 `color.inkwell`; layers div.css-7m64jd 328.0x164.0 rgb(248, 243, 240) 16px; h2.css-uuneru.e1et20720 286.1x152.0; p.css-10gbszt.e11vtv6p0 311.6x59.0 T:1px solid rgba(19, 0, 50, 0.15) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers a.e1c0i0370.css-1cvxahv 328.0x445.8 2px solid rgb(76, 0, 255) offset 2px 4px; div.css-7m64jd 328.0x164.0 rgb(248, 243, 240) 16px; h2.css-uuneru.e1et20720 286.1x152.0; p.css-10gbszt.e11vtv6p0 311.6x59.0 T:1px solid rgba(19, 0, 50, 0.15) |

Child layers that carry the look: div 328x164 background #f8f3f0 `color.ecru` radius 16px; h2 286.1x152 image linear-gradient(transparent calc(100% - 1px), #130032 `color.inkwell` 1px); p 311.6x59 border 1px solid rgba(19, 0, 50, 0.15) `color.ink-15`.

![Story card default](components/crops/story-card-default.png) ![Story card hover](components/crops/story-card-hover.png) ![Story card focus-visible](components/crops/story-card-focus-visible.png) ![Story card pressed](components/crops/story-card-pressed.png)

#### Story logo
A customer logo tile on the stories page. Read as `story-logo` on the customer stories page.

**Values (default).** size 328 x 328; radius 16px; background #f8f3f0 `color.ecru`; text DSIndigo 16/normal 400, #ffffff `color.white`.

![Story logo default](components/crops/story-logo-default.png)

### Pricing storefront (ecom)

The ecom plans page (served /en-SG/ on this vantage): the billing toggle, 16px-radius plan cards, cobalt Buy-now and inkwell Contact-sales actions.

#### Storefront header
The ecom storefront chrome (its own header, Log In). Read as `ec-header` on the pricing storefront page.

**Values (default).** size 1440 x 69; padding 0px 80px; background transparent; text DS Indigo 16/24 400, rgba(19, 0, 50, 0.9) `color.ink-90`; layers a.css-1azp2gh 128.0x34.0 2px solid rgba(0, 0, 0, 0) offset 2px 2px; button.css-144qxs6 77.0x40.0 T:1px solid rgba(19, 0, 50, 0.5) / R:1px solid rgba(19, 0, 50, 0.5) / B:1px solid rgba(19, 0, 50, 0.5) / L:1px solid rgba(19, 0, 50, 0.5) 4px.

Child layers that carry the look: a 128x34 radius 2px; button 77x40 border 1px solid rgba(19, 0, 50, 0.5) `color.ink-50` radius 4px.

![Storefront header default](components/crops/ec-header-default.png)

#### Pricing title
The storefront page heading. Read as `ec-title` on the pricing storefront page.

**Values (default).** size 762.98 x 149.13; padding 80px 0px 0px 0px; background transparent; text DS Indigo 64/69.12 300, rgba(19, 0, 50, 0.9) `color.ink-90`.

![Pricing title default](components/crops/ec-title-default.png)

#### Annual toggle
The Annual half of the billing-period toggle. Read as `ec-billing-annual` on the pricing storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81 x 28; padding 2px 12px; radius 4px; background rgba(19, 0, 50, 0.05) `color.ink-05`; text DS Indigo 16/24 500, rgba(19, 0, 50, 0.9) `color.ink-90` |
| focus-visible | outline 1px auto #005fcc `color.focus-auto`, offset 0px |

![Annual toggle default](components/crops/ec-billing-annual-default.png) ![Annual toggle hover](components/crops/ec-billing-annual-hover.png) ![Annual toggle focus-visible](components/crops/ec-billing-annual-focus-visible.png) ![Annual toggle pressed](components/crops/ec-billing-annual-pressed.png)

#### Monthly toggle
The Monthly half of the billing toggle, read unselected; the monthly screenshot comes from the screenshot pass. Read as `ec-billing-monthly` on the pricing storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81 x 28; padding 2px 12px; radius 4px; background transparent; text DS Indigo 16/24 500, rgba(19, 0, 50, 0.7) `color.ink-70` |
| focus-visible | outline 1px auto #005fcc `color.focus-auto`, offset 0px; layers button.css-18x2esv 81.0x28.0 1px auto rgb(0, 95, 204) offset 0px 4px |

![Monthly toggle default](components/crops/ec-billing-monthly-default.png) ![Monthly toggle hover](components/crops/ec-billing-monthly-hover.png) ![Monthly toggle focus-visible](components/crops/ec-billing-monthly-focus-visible.png) ![Monthly toggle pressed](components/crops/ec-billing-monthly-pressed.png)

#### Plan name
A plan card's name. Read as `plan-name` on the pricing storefront page.

**Values (default).** size 251 x 37.2; background transparent; text DS Indigo 30/37.2 400, #130032 `color.inkwell`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
A plan card's price figure (SGD on the /en-SG/ route). Read as `plan-price` on the pricing storefront page.

**Values (default).** size 194.88 x 72; padding 16px 0px; background transparent; text DS Indigo 20/28 400, #130032 `color.inkwell`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan card
A pricing plan card (the painted section ancestor of a Buy-now action). Read as `plan-card` on the pricing storefront page.

**Values (default).** size 301 x 922.2; border 1px solid rgba(19, 0, 50, 0.5) `color.ink-50`; radius 16px; background #ffffff `color.white`; text DS Indigo 30/37.2 400, #130032 `color.inkwell`.

![Plan card default](components/crops/plan-card-default.png)

#### Buy-now CTA
A plan's Buy-Now action; measured never followed. Read as `buy-now` on the pricing storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 251 x 56; padding 8px 16px; radius 8px; background #4c00ff `color.cobalt`; text DS Indigo 16/24 500, #ffffff `color.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 1, 1), border-color 0.15s cubic-bezier(0.4, 0, 1, 1), color 0.15s cubic-bezier(0.4, 0, 1, 1), fill 0.15s cubic-bezier(0.4, 0, 1, 1), stroke 0.15s cubic-bezier(0.4, 0, 1, 1), opacity 0.15s cubic-bezier(0.4, 0, 1, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 1, 1), transform 0.15s cubic-bezier(0.4, 0, 1, 1), filter 0.15s cubic-bezier(0.4, 0, 1, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 1, 1) |
| hover | background #4000cc `color.cobalt-hover` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |
| pressed | background #330099 `color.cobalt-pressed` |

![Buy-now CTA default](components/crops/buy-now-default.png) ![Buy-now CTA hover](components/crops/buy-now-hover.png) ![Buy-now CTA focus-visible](components/crops/buy-now-focus-visible.png) ![Buy-now CTA pressed](components/crops/buy-now-pressed.png)

#### Contact-sales CTA
The enterprise plan's Contact-Sales action; measured never followed. Read as `contact-sales` on the pricing storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 249 x 56; padding 8px 16px; border 1px solid #130032 `color.inkwell`; radius 8px; background #130032 `color.inkwell`; text DS Indigo 16/16 500, #ffffff `color.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 1, 1), border-color 0.15s cubic-bezier(0.4, 0, 1, 1), color 0.15s cubic-bezier(0.4, 0, 1, 1), fill 0.15s cubic-bezier(0.4, 0, 1, 1), stroke 0.15s cubic-bezier(0.4, 0, 1, 1), opacity 0.15s cubic-bezier(0.4, 0, 1, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 1, 1), transform 0.15s cubic-bezier(0.4, 0, 1, 1), filter 0.15s cubic-bezier(0.4, 0, 1, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 1, 1) |
| hover | border 1px solid rgba(19, 0, 50, 0.9) `color.ink-90`; background rgba(19, 0, 50, 0.9) `color.ink-90` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |
| pressed | border 1px solid rgba(19, 0, 50, 0.75) `color.ink-75`; background rgba(19, 0, 50, 0.75) `color.ink-75`; text DS Indigo 16/16 500, rgba(255, 255, 255, 0.8) |

![Contact-sales CTA default](components/crops/contact-sales-default.png) ![Contact-sales CTA hover](components/crops/contact-sales-hover.png) ![Contact-sales CTA focus-visible](components/crops/contact-sales-focus-visible.png) ![Contact-sales CTA pressed](components/crops/contact-sales-pressed.png)

#### Feature row
An expandable feature row on a plan card, read at rest, hovered, focused and pressed; never expanded here. Read as `feature-row` on the pricing storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 176.3 x 20; background transparent; text DS Indigo 14/20 400, #130032 `color.inkwell` |
| focus-visible | outline 1px auto #005fcc `color.focus-auto`, offset 0px; layers button.css-1wo266l 176.3x20.0 1px auto rgb(0, 95, 204) offset 0px |

![Feature row default](components/crops/feature-row-default.png) ![Feature row hover](components/crops/feature-row-hover.png) ![Feature row focus-visible](components/crops/feature-row-focus-visible.png) ![Feature row pressed](components/crops/feature-row-pressed.png)

#### See-all-features
The See-All-Features expander; measured, never expanded. Read as `see-all` on the pricing storefront page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 251 x 51.77; padding 12px 16px; border 1px solid #4c00ff `color.cobalt`; radius 8px; background transparent; text DS Indigo 16/24 400, #4c00ff `color.cobalt`; transition background-color 0.15s cubic-bezier(0.4, 0, 1, 1), border-color 0.15s cubic-bezier(0.4, 0, 1, 1), color 0.15s cubic-bezier(0.4, 0, 1, 1), fill 0.15s cubic-bezier(0.4, 0, 1, 1), stroke 0.15s cubic-bezier(0.4, 0, 1, 1), opacity 0.15s cubic-bezier(0.4, 0, 1, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 1, 1), transform 0.15s cubic-bezier(0.4, 0, 1, 1), filter 0.15s cubic-bezier(0.4, 0, 1, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 1, 1) |
| hover | border 1px solid #ede5ff `color.mist-soft`; background #ede5ff `color.mist-soft` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px; outline 2px solid transparent, offset 2px |
| pressed | border 1px solid #ede5ff `color.mist-soft`; background #ede5ff `color.mist-soft`; text DS Indigo 16/24 400, #130032 `color.inkwell` |

![See-all-features default](components/crops/see-all-default.png) ![See-all-features hover](components/crops/see-all-hover.png) ![See-all-features focus-visible](components/crops/see-all-focus-visible.png) ![See-all-features pressed](components/crops/see-all-pressed.png)

### Log in

The public sign-in card on account.docusign.com (the OAuth surface apps.docusign.com/send lands on): measured, never filled past the sample text or submitted.

#### Login card
The centred OAuth login card on account.docusign.com; never filled or submitted. Read as `auth-card` on the log in page.

**Values (default).** size 556 x 439.59; padding 64px 0px; border 1px solid rgba(25, 24, 35, 0.15) `color.hairline-auth`; radius 4px; background #ffffff `color.white`; text DS Indigo 24/30 400, rgba(19, 0, 50, 0.9) `color.ink-90`.

![Login card default](components/crops/auth-card-default.png)

#### Email field
The Enter-email input; sample text was typed and deleted, nothing sent. Read as `auth-field` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 424 x 38; padding 8px 16px; background transparent; text DS Indigo 16/24 400, rgba(19, 0, 50, 0.9) `color.ink-90`; placeholder rgba(19, 0, 50, 0.7) `color.ink-70` |
| filled | placeholder rgba(19, 0, 50, 0.9) `color.ink-90` |

![Email field default](components/crops/auth-field-default.png) ![Email field focused](components/crops/auth-field-focused.png) ![Email field filled](components/crops/auth-field-filled.png)

#### Next button
The Next submit; measured, never pressed (a press continues sign-in). Read as `auth-next` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 426 x 40; padding 4px 12px; border 1px solid transparent; radius 4px; background #260559 `color.auth-deep`; text DS Indigo 16/24 500, #ffffff `color.white`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1) |
| hover | background #2b047f `color.auth-deep-hover` |
| focus-visible | outline 2px solid #130032 `color.inkwell`, offset 2px |
| pressed | background #37039e `color.auth-deep-pressed` |

![Next button default](components/crops/auth-next-default.png) ![Next button hover](components/crops/auth-next-hover.png) ![Next button focus-visible](components/crops/auth-next-focus-visible.png) ![Next button pressed](components/crops/auth-next-pressed.png)

#### Language picker
The English-(US) language menu trigger; measured, never opened. Read as `auth-lang` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.64 x 20; padding 0px 0px 0px 6px; border 1px solid transparent; radius 4px; background rgba(19, 0, 50, 0.05) `color.ink-05`; text DS Indigo 10/12 500, rgba(19, 0, 50, 0.9) `color.ink-90`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1); icon 20 x 20, rgba(19, 0, 50, 0.9) `color.ink-90` |
| hover | background rgba(19, 0, 50, 0.1) `color.ink-10` |
| focus-visible | outline 2px solid #130032 `color.inkwell`, offset 2px |
| pressed | background rgba(19, 0, 50, 0.15) `color.ink-15` |

![Language picker default](components/crops/auth-lang-default.png) ![Language picker hover](components/crops/auth-lang-hover.png) ![Language picker focus-visible](components/crops/auth-lang-focus-visible.png) ![Language picker pressed](components/crops/auth-lang-pressed.png)

#### Signup link
The Sign-Up-for-Free link under the card; measured never followed. Read as `auth-signup` on the log in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 426 x 40; padding 4px 12px; border 1px solid transparent; radius 4px; background rgba(19, 0, 50, 0.05) `color.ink-05`; text DS Indigo 16/24 500, rgba(19, 0, 50, 0.9) `color.ink-90`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1) |
| hover | background rgba(19, 0, 50, 0.1) `color.ink-10` |
| focus-visible | outline 2px solid #130032 `color.inkwell`, offset 2px |
| pressed | background rgba(19, 0, 50, 0.15) `color.ink-15` |

![Signup link default](components/crops/auth-signup-default.png) ![Signup link hover](components/crops/auth-signup-hover.png) ![Signup link focus-visible](components/crops/auth-signup-focus-visible.png) ![Signup link pressed](components/crops/auth-signup-pressed.png)

### Footer

The marketing footer: link columns, the locale selector and legal.

#### Footer
The marketing footer: link columns, locale selector, legal and social. Read as `footer` on the home page.

**Values (default).** size 1440 x 974; background transparent; text DSIndigo 12/18 600, #130032 `color.inkwell`; icon 16 x 16, rgba(19, 0, 50, 0.75) `color.ink-75`; layers section.css-29n46u.e1p96sfz1 1440.0x746.0 rgb(248, 243, 240); div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75); div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75); div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75); div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75); div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75).

Child layers that carry the look: section 1440x746 background #f8f3f0 `color.ecru`; div::after 0pxx1px background rgba(19, 0, 50, 0.75) `color.ink-75`; div::after 0pxx1px background rgba(19, 0, 50, 0.75) `color.ink-75`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 184 x 44; radius 4px; background transparent; text DSIndigo 14/21 500, #130032 `color.inkwell`; transition color 0.15s ease-in-out; layers div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75) |
| hover | text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; layers div::after.css-1eg020q.e1tasy2f1 100%x1px rgba(19, 0, 50, 0.75) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; layers a.css-1po7wbl.e1tasy2f0 184.0x44.0 2px solid rgb(76, 0, 255) offset 2px 4px; div::after.css-1eg020q.e1tasy2f1 0pxx1px rgba(19, 0, 50, 0.75) |
| pressed | text DSIndigo 14/21 500, rgba(19, 0, 50, 0.75) `color.ink-75`; layers div::after.css-1eg020q.e1tasy2f1 100%x1px rgb(19, 0, 50) |

Child layers that carry the look: div::after 0pxx1px background rgba(19, 0, 50, 0.75) `color.ink-75`.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Locale button
The United-States locale menu trigger; measured, never opened. Read as `locale-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 200 x 40; padding 8px 48px 8px 16px; border 1px solid rgba(19, 0, 50, 0.15) `color.ink-15`; radius 2px; background transparent; text DSIndigo 16/24 400, #130032 `color.inkwell` |
| hover, focus-visible, pressed | border 1px solid #4c00ff `color.cobalt` |

![Locale button default](components/crops/locale-button-default.png) ![Locale button hover](components/crops/locale-button-hover.png) ![Locale button focus-visible](components/crops/locale-button-focus-visible.png) ![Locale button pressed](components/crops/locale-button-pressed.png)

### Mobile (390 wide)

The marketing surface at phone width: the 77px header, the hamburger menu and the stacked hero.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 77; background #ffffff `color.white`; text DSIndigo 14/21 600, #ffffff `color.white`; icon 24 x 24, #130032 `color.inkwell`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header hamburger toggle. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 30; background transparent; text DSIndigo 16/normal 400, #130032 `color.inkwell`; icon 24 x 24, #130032 `color.inkwell` |
| focus-visible | outline 1px auto #005fcc `color.focus-auto`, offset 0px; layers button.css-kkuep2 24.0x30.0 1px auto rgb(0, 95, 204) offset 0px |

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The header menu opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 77; background #ffffff `color.white`; text DSIndigo 18/normal 500, rgba(19, 0, 50, 0.75) `color.ink-75`; icon 24 x 24, #4c00ff `color.cobalt`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened header menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.36 x 73; padding 24px 0px; radius 4px; background transparent; text DSIndigo 18/normal 500, rgba(19, 0, 50, 0.75) `color.ink-75`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1); icon 16 x 16, rgba(19, 0, 50, 0.75) `color.ink-75`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | layers ::after rgb(76, 0, 255) 0px none 1; button::after.css-15xalk.e1yg1y6k0 91.3594pxx2px rgb(76, 0, 255) |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px; layers ::after rgb(76, 0, 255) 0px none 1; button.css-15xalk.e1yg1y6k0 91.4x73.0 2px solid rgb(76, 0, 255) offset 2px 4px; button::after.css-15xalk.e1yg1y6k0 91.3594pxx2px rgb(76, 0, 255) |
| pressed | layers ::after rgb(76, 0, 255) 0px none 1; button::after.css-15xalk.e1yg1y6k0 91.3594pxx2px rgb(76, 0, 255) |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 342 x 187.88; background transparent; text DSIndigo 58/62.64 300, #ffffff `color.white`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile CTA
The hero call to action at phone width. Read as `m-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 358 x 56; padding 16px 24px; radius 8px; background #4c00ff `color.cobalt`; text DSIndigo 16/24 500, #ffffff `color.white`; transition background-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), border-color 0.1s cubic-bezier(0.33, 0, 0.67, 1), box-shadow 0.1s cubic-bezier(0.33, 0, 0.67, 1), color 0.1s cubic-bezier(0.33, 0, 0.67, 1) |
| hover | background #4000cc `color.cobalt-hover` |
| focus-visible | outline 2px solid #4c00ff `color.cobalt`, offset 2px |
| pressed | background #4000cc `color.cobalt-hover` |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Docusign wordmark, the 7_Docusign icon-font glyphs, product illustrations and customer logos) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Docusign's product — the send/sign envelope flow, templates, CLM, IAM workspaces, billing and admin — lives behind account.docusign.com on apps.docusign.com and was never reached. /login was captured as the public OAuth card on account.docusign.com and never filled past sample text or submitted; the Access-Documents link reaches a public validation flow that was never used.

### Pages

- **The workspace.** Every post-login surface (envelopes, templates, agreement actions, workflows, settings, billing, admin) needs an account and was never reached.
- **Checkout and purchase.** Every Buy-now, Try-for-free, Contact-sales and Get-Started control was measured, never followed past its public landing — no plan was ever purchased and no trial started.
- **The trial and hero forms.** The work-email fields were measured with sample text typed and deleted; the forms were never submitted, so the onboarding steps behind them are uncaptured.
- **The country/localised surfaces.** The marketing site serves many locales; only the en-US surface was captured, and the storefront geo-redirected to /en-SG/ on this vantage, so prices and copy are as served for Singapore.
- **Signature downloads.** The generator's Download buttons were measured, never pressed — no PNG/JPEG was exported, so the rendered signature asset itself is uncaptured.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover), so any script-side mousedown behaviour is missing. `assistant` pressed failed to a stale node — recorded as a failed state, not a measured absence.
- **Disabled, error and loading states** were not seen on the public surface.
- **The mega-menu's other panels** (Solutions, Resources) were not opened; only the Products panel was measured.
- **Search** overlay in the utility bar was never opened; the locale menu in the footer was measured closed.

### Themes

Every captured surface paints light. The deep-violet hero/footer bands and the inkwell dark buttons are painted sections, not a theme; no dark surface exists on the public site, and no dark set is emitted.

### Fonts

- **DSIndigo** (marketing, weights 300-600) and **'DS Indigo'** (generator, storefront and account stacks) are the served faces from DocuSign's CDN; the **7_Docusign / 2_Docusign** icon fonts and **Noto Sans Mono** are also declared, and the generator serves six signature script faces (STFelicetteScript, TDNStockinette, TDNRhubarbTart, STAmpersandist, STConstant-UltraItalic, STNebulith-Display). The style guide falls back to system sans.

### Screenshots

- Product illustrations, photography, the Docusign wordmark and customer logos in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, customer stories and blog content are the product's content; only frames and components were measured.
