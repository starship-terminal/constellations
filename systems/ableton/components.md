# Ableton components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.ableton.com on 2026-11-08, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, downloaded, sent or submitted, and the cookie consent was never answered (it was hidden for the clean captures, which is not a consent).

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (78 components, 164 states). The page layouts at four widths are in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `futura-pt 20/30 700, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (164 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (Ableton has one theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 390 wide.

| Surface | URL | Screenshots |
|---|---|---|
| Home. Hero teaser, the photo-cell grid, striped promo card, blog teasers, footer. The cookie banner and the opened More menu captured as separate states. | `/en/` | [cookie-banner](screenshots/home-light-cookie-banner.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [more-menu](screenshots/home-light-more-menu.png) |
| Live. The 21k px product page: display titles, Try/Buy buttons, video and audio controls, feature collapses, dark photo bands. | `/en/live/` | [default](screenshots/live-light-default.png), [full](screenshots/live-light-full.png) |
| Push. Product hero and feature sections. | `/en/push/` | [default](screenshots/push-light-default.png), [full](screenshots/push-light-full.png) |
| Move. Product hero and feature sections. | `/en/move/` | [default](screenshots/move-light-default.png), [full](screenshots/move-light-full.png) |
| Note. Product hero and feature sections. | `/en/note/` | [default](screenshots/note-light-default.png), [full](screenshots/note-light-full.png) |
| Link. Product page and the Link-enabled-products CTA. | `/en/link/` | [default](screenshots/link-light-default.png), [full](screenshots/link-light-full.png) |
| Trial. Edition cards and Download buttons. | `/en/trial/` | [default](screenshots/trial-light-default.png), [full](screenshots/trial-light-full.png) |
| Shop index. Product cards with prices and add-to-cart. | `/en/shop/` | [default](screenshots/shop-light-default.png), [full](screenshots/shop-light-full.png) |
| Packs catalogue. The 40k px grid of pack cards. | `/en/packs/` | [default](screenshots/packs-light-default.png), [full](screenshots/packs-light-full.png) |
| Blog index. Post rows with salmon category badges. | `/en/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| About. The company page. | `/en/about/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Help. Support sections and links. | `/en/help/` | [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png) |
| Jobs. Openings list. | `/en/jobs/` | [default](screenshots/jobs-light-default.png), [full](screenshots/jobs-light-full.png) |
| Log in / register. Both forms at rest; nothing submitted. | `/en/login/` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Home at 390: collapsed nav, hero teaser, the cell grid single-column. | `/en/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Live at 390. | `/en/live/` | [default](screenshots/mobile-live-light-default.png), [full](screenshots/mobile-live-light-full.png) |
| Shop at 390. | `/en/shop/` | [default](screenshots/mobile-shop-light-default.png), [full](screenshots/mobile-shop-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent card | every page, on load | at rest; hidden by CSS for every clean capture, never accepted or closed | [home-light-cookie-banner](screenshots/home-light-cookie-banner.png), [cookie-bar](#cookie-bar) |
| Nav "More" panel, open | home | the More button pressed (opens the disclosure) | [home-light-more-menu](screenshots/home-light-more-menu.png), [nav-more-panel](#nav-more-panel) |
| Feature collapse, open | Live | the collapse row's own toggle pressed (a local UI disclosure) | [collapse-toggle-open](#collapse-toggle-open) |
| Video / audio players | Live | measured at rest; Play was never pressed (media streams and modals stay uncaptured) | [btn-video](#btn-video), [btn-audio](#btn-audio) |
| Form focus | footer newsletter, login and register | tabbed or clicked into; sample text typed and deleted on the field-measurement pass, nothing sent | [newsletter-field](#newsletter-field), [login-field](#login-field), [register-field](#register-field) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 24 components were given a real keyboard focus. 20 draw a ring: `nav-logo` (1px auto #005fcc `focus-blue`, offset 1px), `nav-link` (1px auto #005fcc `focus-blue`, offset 1px), `nav-more` (1px auto #005fcc `focus-blue`, offset 0px), `nav-trial-cta` (1px auto #005fcc `focus-blue`, offset 1px), `nav-login` (1px auto #005fcc `focus-blue`, offset 1px), `panel-cat-link` (1px auto #005fcc `focus-blue`, offset 1px), `footer-link` (1px auto #005fcc `focus-blue`, offset 1px), `footer-social` (1px auto #005fcc `focus-blue`, offset 1px), `newsletter-submit` (1px auto #005fcc `focus-blue`, offset 0px), `cookie-close` (1px auto #005fcc `focus-blue`, offset 0px), `cookie-more-info` (1px auto #005fcc `focus-blue`, offset 1px), `btn-try` (2px solid #ff764d `focus-orange`, offset 2px), `btn-buy` (2px solid #0000ff `blue`, offset 2px), `anchor-link` (2px solid #0000ff `blue`, offset 2px), `push-cta` (2px solid #ff764d `focus-orange`, offset 2px), `move-cta` (2px solid #ff764d `focus-orange`, offset 2px), `note-cta` (2px solid #ff764d `focus-orange`, offset 2px), `link-cta` (1px auto #005fcc `focus-blue`, offset 1px), `pack-download` (1px auto #005fcc `focus-blue`, offset 1px), `login-submit` (1px auto #005fcc `focus-blue`, offset 0px). The other 4 draw none, so a keyboard user sees no change: `hero-cta`, `cookie-accept`, `trial-download`, `add-to-cart`. Ableton uses two rings: the browser's `auto 1px #005fcc` on text links, and a deliberate `solid 2px #ff764d` orange on the boxed buttons.

**Pressed.** Forced `:active` changed almost nothing measurable on Ableton: the deep-blue Buy button darkens to `#042b9f` (its hover colour) and everything else reads the same as default. The site's controls do not shrink or recolour under the finger; hover on most `abl-button`s is likewise a no-op, with the boxed Try button instead swapping its text from blue to black.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease` | bottom | scroll-down |
| 0.3s | `ease-in-out` | background-color, border-color, bottom, box-shadow, color, height, left, max-height, max-width, opacity, padding-bottom, padding-left, padding-right, padding-top, right, text-decoration, top, transform, width | anchor-link, btn-audio, btn-buy, btn-try, btn-video, collapse-toggle, collapse-toggle-open, move-cta and more |
| 0.35s | `ease` | color | m-menu-trigger |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 0, 1440 wide | content x 160, 1600 wide | content x 0, 1024 wide | content x 0, 390 wide |
| live | content x 0, 1440 wide | content x 160, 1600 wide | content x 0, 1024 wide | content x 0, 390 wide |
| packs | content x 0, 1440 wide | content x 160, 1600 wide | content x 0, 1024 wide | content x 0, 390 wide |
| shop | content x 0, 1440 wide | content x 160, 1600 wide | content x 0, 1024 wide | content x 0, 390 wide |
| trial | content x 0, 1440 wide; grid 120 120 120 120 120 120 120 120 120 120 120 120 gap normal | content x 0, 1920 wide; grid 133.3 133.3 133.3 133.3 133.3 133.3 133.3 133.3 133.3 133.3 133.3 133.3 gap normal | content x 0, 1024 wide; grid 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 85.3 gap normal | content x 0, 390 wide; grid 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 32.5 gap normal |
| blog | content x 0, 1440 wide; grid 360 360.0 360 gap 60px | content x 0, 1920 wide; grid 400 400.0 400 gap 66.6667px | content x 0, 1024 wide; grid 256 256.0 256 gap 42.6667px | content x 0, 390 wide |
| about | content x 0, 1440 wide | content x 160, 1600 wide | content x 0, 1024 wide | content x 0, 390 wide |
| login | content x 0, 1440 wide | content x 160, 1600 wide | content x 0, 1024 wide | content x 0, 390 wide |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Promo card](#promo-card) | 479.98 x 319.98 | 1px solid #000000 `black` | - | - | none | 0 |
| [Blog teaser card](#blog-teaser-card) | 360 x 303.05 | - | - | #eeeeee `field-gray` | none | 0 |
| [Product teaser card](#product-teaser-card) | 720 x 720 | - | - | #ffc3a5 | none | 120px |
| [Pack card](#pack-card) | 1440 x 348 | - | - | #000000 `black` | none | 90px 120px |
| [Trial edition panel](#trial-edition-panel) | 720 x 654.97 | - | - | #fbffa7 | none | 120px 0px |
| [Discover-more collapse](#discover-more-collapse) | 1210 x 72 | 2px solid #0000ff `blue` | - | #ffffff `white` | none | 16px |
| [Cookie consent card](#cookie-consent-card) | 453.33 x 414.91 | - | - | #000000 `black` | none | 20px |
| [Newsletter email field](#newsletter-email-field) | 360 x 42 | - | - | #eeeeee `field-gray` | none | 8px 15px |
| [Username field](#username-field) | 380 x 46 | - | - | #eeeeee `field-gray` | none | 8px 15px |
| [Country select](#country-select) | 380 x 44 | - | - | #eeeeee `field-gray` | none | 7px 50px 7px 15px |

## Components

### Shell and navigation

The shell every marketing page shares: a 69px top bar with the grid-mark logo, the product links (Live / Push / Move / Note / Link / Shop / Packs / Help), a "More" disclosure, "Try Live 12 for free" in signature blue and "Log in or register"; and the fat white footer with heading columns, the newsletter form, locale picker and social buttons. Everything is square: no rounded corners anywhere.

#### Top navigation bar
The white top bar: the Ableton logo (the grid mark), product links (Live / Push / Move / Note / Link / Shop / Packs / Help), the "More" disclosure, "Try Live 12 for free" in blue and "Log in or register". Read as `nav-bar` on the home page.

**Values (default).** size 1440 x 69; padding 20px 0px 0px 0px; background transparent; text futura-pt 20/30 700, #000000 `black`; icon 60 x 28, #000000 `black`.

Child layers that carry the look: button::after 0pxx0px border 5px solid #000000 `black`; span::before 12pxx2px background #000000 `black`; span::before 12pxx2px background #000000 `black`.

![Top navigation bar default](components/crops/nav-bar-default.png)

#### Logo
The Ableton grid-mark wordmark linking home. Read as `nav-logo` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 60 x 28; background transparent; text futura-pt 16/24 400, #000000 `black`; icon 60 x 28, #000000 `black` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Logo default](components/crops/nav-logo-default.png) ![Logo hover](components/crops/nav-logo-hover.png) ![Logo focus-visible](components/crops/nav-logo-focus-visible.png) ![Logo pressed](components/crops/nav-logo-pressed.png)

#### Nav link
A product link in the top bar. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 30.69 x 26; background transparent; text futura-pt 20/30 700, #000000 `black` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### More button
The "More +" disclosure button opening the extended menu. Read as `nav-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 63.31 x 26; background transparent; text futura-pt 20/normal 700, #000000 `black` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 0px |

Child layers that carry the look: span::before 12pxx2px background #000000 `black`; span::before 12pxx2px background #000000 `black`; span::after 2pxx12px background #000000 `black`.

![More button default](components/crops/nav-more-default.png) ![More button hover](components/crops/nav-more-hover.png) ![More button focus-visible](components/crops/nav-more-focus-visible.png) ![More button pressed](components/crops/nav-more-pressed.png)

#### More menu panel
The expanded "More" menu: "More on Ableton.com" link row plus "More from Ableton" cards (Ableton Learn, Learning Synths, Making Music). Read as `nav-more-panel` on the home page.

**Values (open).** size 1440 x 380.27; padding 27px 40px 55px 40px; background transparent; text futura-pt 30/42 700, #000000 `black`.

![More menu panel open](components/crops/nav-more-panel-open.png)

#### More menu link
A link inside the expanded More menu. Read as `nav-more-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| open (same: hover) | size 35.77 x 26; background transparent; text futura-pt 20/30 400, #000000 `black` |

![More menu link open](components/crops/nav-more-link-open.png) ![More menu link hover](components/crops/nav-more-link-hover.png)

#### Trial CTA link
The blue "Try Live 12 for free" link at the right end of the top bar; links to /en/trial/. Hovered and focused only. Read as `nav-trial-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 147.95 x 26; background transparent; text futura-pt 20/30 700, #0000ff `blue` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Trial CTA link default](components/crops/nav-trial-cta-default.png) ![Trial CTA link hover](components/crops/nav-trial-cta-hover.png) ![Trial CTA link focus-visible](components/crops/nav-trial-cta-focus-visible.png) ![Trial CTA link pressed](components/crops/nav-trial-cta-pressed.png)

#### Log in link
"Log in or register" in the top bar; links to /en/login/. Hovered and focused only. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 106.78 x 21; background transparent; text futura-pt 16/24 700, #000000 `black` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Footer
The page footer: link columns, the newsletter form, social buttons, the language and location selectors and the legal row. Read as `footer` on the home page.

**Values (default).** size 1440 x 783.97; background #ffffff `white`; text futura-pt 20/30 700, #000000 `black`; icon 32 x 32, #000000 `black`.

![Footer default](components/crops/footer-default.png)

#### Footer column heading
Read as `footer-heading` on the home page.

**Values (default).** size 480 x 30; background transparent; text futura-pt 20/30 700, #000000 `black`.

![Footer column heading default](components/crops/footer-heading-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 218.55 x 26; background transparent; text futura-pt 20/30 400, #000000 `black` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

Child layers that carry the look: a::after 6pxx6px border 1px solid #000000 `black`.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon link
One of the social-icon links (Facebook, X, YouTube, Instagram, TikTok, Discord). Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44 x 44; background transparent; text futura-pt 0/0 700, #000000 `black`; icon 32 x 32, #000000 `black` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Social icon link default](components/crops/footer-social-default.png) ![Social icon link hover](components/crops/footer-social-hover.png) ![Social icon link focus-visible](components/crops/footer-social-focus-visible.png) ![Social icon link pressed](components/crops/footer-social-pressed.png)

#### Newsletter email field
The email field of the footer newsletter form; clicked into, nothing typed or sent. Read as `newsletter-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 42; padding 8px 15px; background #eeeeee `field-gray`; text futura-pt 20/normal 400, #000000 `black`; placeholder #666666 |
| focused | outline 1px auto #005fcc `focus-blue`, offset 0px |

![Newsletter email field default](components/crops/newsletter-field-default.png) ![Newsletter email field focused](components/crops/newsletter-field-focused.png)

#### Newsletter sign-up button
The "Sign up" button of the footer newsletter form. Measured, never pressed. Read as `newsletter-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 120 x 42; padding 7px 30px; background #0000ff `blue`; text futura-pt 20/normal 700, #ffffff `white`; placeholder #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 0px |

![Newsletter sign-up button default](components/crops/newsletter-submit-default.png) ![Newsletter sign-up button hover](components/crops/newsletter-submit-hover.png) ![Newsletter sign-up button focus-visible](components/crops/newsletter-submit-focus-visible.png)

#### Language selector
The footer language <select>. Read as `footer-locale` on the home page.

**Values (default).** size 116.5 x 30; background transparent; text futura-pt 14/21 400, #000000 `black`.

Child layers that carry the look: div::after 30pxx30px image url(data:…); select 116.5x30 background #eeeeee `field-gray`.

![Language selector default](components/crops/footer-locale-default.png)

### Home

The home page is a grid of full-bleed photo/video teaser cells (one cell per product or story) under a hero, plus a striped promo card and a blog-teaser panel. Text sits on the photography in white, always Futura PT bold.

#### Hero teaser
The lead tile of the home grid: a photo/video cell with a large white headline and a "See what's new" link. Read as `hero-teaser` on the home page.

**Values (default).** size 839.98 x 559.98; padding 0px 0px 559.984px 0px; background transparent; text futura-pt 60/66 700, #ffffff `white`.

Child layers that carry the look: span::after 7.1875pxx7.1875px border 2px solid #ffffff `white`.

![Hero teaser default](components/crops/hero-teaser-default.png)

#### Hero headline
The white display headline over the hero media. Read as `hero-title` on the home page.

**Values (default).** size 719.98 x 198; background transparent; text futura-pt 60/66 700, #ffffff `white`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero link
"See what's new" — the arrow link under the hero headline. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 719.98 x 36; background transparent; text futura-pt 24/36 700, #ffffff `white` |

Child layers that carry the look: span::after 7.1875pxx7.1875px border 2px solid #ffffff `white`.

![Hero link default](components/crops/hero-cta-default.png) ![Hero link hover](components/crops/hero-cta-hover.png) ![Hero link focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero link pressed](components/crops/hero-cta-pressed.png)

#### Grid cell
One tile of the loose homepage grid: the layout mixes image cells and text-on-white cells. Read as `home-cell` on the home page.

**Values (default).** size 839.98 x 559.98; background transparent; text futura-pt 60/66 700, #ffffff `white`.

Child layers that carry the look: span::after 7.1875pxx7.1875px border 2px solid #ffffff `white`.

![Grid cell default](components/crops/home-cell-default.png)

#### Promo card
A text-on-tint promo cell in the grid (the rent-to-own card on lime stripes). Read as `home-promo-card` on the home page.

**Values (default).** size 479.98 x 319.98; background transparent; text futura-pt 30/42 700, #000000 `black`.

Child layers that carry the look: span::after 6pxx6px border 1px solid #000000 `black`.

![Promo card default](components/crops/home-promo-card-default.png)

#### Scroll-down button
The blue chevron button pinned under the first screen; an in-page anchor, measured at rest. Read as `scroll-down` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 60 x 60; background #0000ff `blue`; text futura-pt 16/24 400, #000000 `black`; transition bottom 0.15s ease |

![Scroll-down button default](components/crops/scroll-down-default.png) ![Scroll-down button hover](components/crops/scroll-down-hover.png)

#### Section headline
A section headline over a blog-teaser row ("From the blog" and friends). Read as `panel-title` on the home page.

**Values (default).** size 1200.03 x 48; background transparent; text futura-pt 40/48 700, #000000 `black`.

![Section headline default](components/crops/panel-title-default.png)

#### Blog teaser card
An article teaser in the home/blog rows: media cell, category tag and headline. Read as `blog-teaser` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 360 x 303.05; background transparent; text futura-pt 14/21 700, #000000 `black` |

Child layers that carry the look: div 360x202.5 background #eeeeee `field-gray`; a 87x24.9 background #ff8389 `salmon`.

![Blog teaser card default](components/crops/blog-teaser-default.png) ![Blog teaser card hover](components/crops/blog-teaser-hover.png)

#### Blog teaser headline
Read as `blog-teaser-title` on the home page.

**Values (default).** size 360 x 60; background transparent; text futura-pt 20/30 700, #000000 `black`.

![Blog teaser headline default](components/crops/blog-teaser-title-default.png)

#### Blog teaser category
Read as `blog-teaser-tag` on the home page.

**Values (default).** size 87.03 x 24.91; padding 1.96px 11.9px; background #ff8389 `salmon`; text futura-pt 14/21 700, #000000 `black`.

![Blog teaser category default](components/crops/blog-teaser-tag-default.png)

#### Category link
A blog category filter link under a teasers panel. Read as `panel-cat-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 141.39 x 36; background transparent; text futura-pt 24/36 700, #0000ff `blue` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

Child layers that carry the look: a::after 7.1875pxx7.1875px border 2px solid #0000ff `blue`.

![Category link default](components/crops/panel-cat-link-default.png) ![Category link hover](components/crops/panel-cat-link-hover.png) ![Category link focus-visible](components/crops/panel-cat-link-focus-visible.png) ![Category link pressed](components/crops/panel-cat-link-pressed.png)

### Consent overlay

Ableton's cookie consent (`#biscuits-overlay`): a black card pinned to the bottom of every page, with Accept in signature blue, and Close / More info as 2px-outline buttons. It was captured as found; Accept was never clicked (the capture hides the overlay by CSS for the clean shots, which is a hide, not a consent).

#### Cookie consent card
The black consent card fixed at the bottom left: "Clicking Accept means you consent…" copy with Accept (blue), Close and More info buttons. Re-shown for the measurement, never answered. Read as `cookie-bar` on the home page.

**Values (open).** size 453.33 x 414.91; padding 20px; background #000000 `black`; text futura-pt 16/24 400, #ffffff `white`.

![Cookie consent card open](components/crops/cookie-bar-open.png)

#### Accept button
The blue "Accept" button of the consent card. Measured in every state — never pressed (it would post consent). Read as `cookie-accept` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 413.33 x 47; padding 6.5px 30px; border 2px solid transparent; background #0000ff `blue`; text futura-pt 20/30 700, #ffffff `white` |
| focus-visible | border 2px solid #000000 `black` |

![Accept button default](components/crops/cookie-accept-default.png) ![Accept button hover](components/crops/cookie-accept-hover.png) ![Accept button focus-visible](components/crops/cookie-accept-focus-visible.png) ![Accept button pressed](components/crops/cookie-accept-pressed.png)

#### Close button
The outline "Close" button, which denies consent. Measured, never pressed. Read as `cookie-close` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 201.66 x 47; padding 6.5px 30px; border 2px solid #ffffff `white`; background transparent; text futura-pt 20/30 700, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 0px |

![Close button default](components/crops/cookie-close-default.png) ![Close button hover](components/crops/cookie-close-hover.png) ![Close button focus-visible](components/crops/cookie-close-focus-visible.png) ![Close button pressed](components/crops/cookie-close-pressed.png)

#### More info link
"More info" — the outline link to /en/cookie-settings/. Hovered and focused only. Read as `cookie-more-info` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 201.67 x 47; padding 6.5px 30px; border 2px solid #ffffff `white`; background transparent; text futura-pt 20/30 700, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![More info link default](components/crops/cookie-more-info-default.png) ![More info link hover](components/crops/cookie-more-info-hover.png) ![More info link focus-visible](components/crops/cookie-more-info-focus-visible.png) ![More info link pressed](components/crops/cookie-more-info-pressed.png)

### Live page

The Live product page: the biggest marketing surface (21k px tall at 1440), all dark photo bands and white type. Its own button set: Try (boxed outline), Buy (boxed deep-blue fill), Watch-video and Play-audio buttons, deep-blue anchor links, and the feature-collapse rows that open with a 2px blue border.

#### Page title
"Find … in Ableton Live" — the product page title in the largest abl-type step. Read as `live-title` on the Live page.

**Values (default).** size 115.2 x 77; background transparent; text Futura PT 60/78 700, #ffffff `white`.

![Page title default](components/crops/live-title-default.png)

#### Section title
A big section heading ("Play freely with ideas"). Read as `live-section-title` on the Live page.

**Values (default).** size 396.31 x 155; background transparent; text Futura PT 60/78 700, #ffffff `white`.

![Section title default](components/crops/live-section-title-default.png)

#### Try-for-free button
The boxed "Try Live 12 for free" button on the product page; links to /en/trial/. Hovered and focused only. Read as `btn-try` on the Live page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 185.95 x 50; padding 10px 0px 10px 38px; background transparent; text Futura PT 20/30 700, #0000ff `blue`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out |
| hover | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; text Futura PT 20/30 700, #000000 `black` |
| focus-visible | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; outline 2px solid #ff764d `focus-orange`, offset 2px; text Futura PT 20/30 700, #000000 `black` |
| pressed | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; text Futura PT 20/30 700, #000000 `black` |

![Try-for-free button default](components/crops/btn-try-default.png) ![Try-for-free button hover](components/crops/btn-try-hover.png) ![Try-for-free button focus-visible](components/crops/btn-try-focus-visible.png) ![Try-for-free button pressed](components/crops/btn-try-pressed.png)

#### Buy now button
The boxed "Buy now" button; links to the shop. Hovered and focused only. Read as `btn-buy` on the Live page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 130.33 x 48; padding 8px 30px; border 1px solid #0032e6 `blue-deep`; background #0032e6 `blue-deep`; text Futura PT 20/30 700, #ffffff `white`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out |
| hover | border 1px solid #042b9f `blue-hover`; shadow rgba(4, 43, 159, 0) 0px 0px 0px 0px |
| focus-visible | border 1px solid #042b9f `blue-hover`; shadow rgba(4, 43, 159, 0) 0px 0px 0px 0px; outline 2px solid #0000ff `blue`, offset 2px |
| pressed | border 1px solid #042b9f `blue-hover`; shadow rgba(4, 43, 159, 0) 0px 0px 0px 0px |

![Buy now button default](components/crops/btn-buy-default.png) ![Buy now button hover](components/crops/btn-buy-hover.png) ![Buy now button focus-visible](components/crops/btn-buy-focus-visible.png) ![Buy now button pressed](components/crops/btn-buy-pressed.png)

#### Video play button
The "Play: VIDEO" overlay button on a demo clip. Hovered only — pressing plays the video. Read as `btn-video` on the Live page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 60 x 60; background rgba(0, 0, 0, 0.5); text Futura PT 20/28 400, #ffffff `white`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out; icon 60 x 60, #ffffff `white` |

![Video play button default](components/crops/btn-video-default.png) ![Video play button hover](components/crops/btn-video-hover.png)

#### Audio play button
A "Play: <sound>" button on an audio example. Hovered only — pressing plays audio. Read as `btn-audio` on the Live page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32.84; background #0000ff `blue`; text Futura PT 20/28 400, #ffffff `white`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out; icon 32 x 32, #ffffff `white` |

![Audio play button default](components/crops/btn-audio-default.png) ![Audio play button hover](components/crops/btn-audio-hover.png)

#### Anchor link
An in-page anchor link in the feature navigation row. Read as `anchor-link` on the Live page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 151.42 x 34; padding 5px 0px 2px 0px; background transparent; text Futura PT 18/27 700, #0032e6 `blue-deep`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out, transform 0.3s ease-in-out |
| hover | text Futura PT 18/27 700, #0000ff `blue` |
| focus-visible | outline 2px solid #0000ff `blue`, offset 2px |
| pressed | text Futura PT 18/27 700, #0000ff `blue` |

![Anchor link default](components/crops/anchor-link-default.png) ![Anchor link hover](components/crops/anchor-link-hover.png) ![Anchor link focus-visible](components/crops/anchor-link-focus-visible.png) ![Anchor link pressed](components/crops/anchor-link-pressed.png)

#### Discover-more collapse
A "Discover more … sounds" collapsed-content toggle. Read as `collapse-toggle` on the Live page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1210 x 72; padding 16px; border 2px solid #0000ff `blue`; background #ffffff `white`; text Futura PT 24/36 700, #0000ff `blue`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out, transform 0.3s ease-in-out; icon 20 x 20, #0000ff `blue` |

![Discover-more collapse default](components/crops/collapse-toggle-default.png) ![Discover-more collapse hover](components/crops/collapse-toggle-hover.png)

#### Discover-more collapse (open)
The same toggle after being pressed once; client-side expand, nothing sent. Read as `collapse-toggle-open` on the Live page.

**Values (open).** size 1210 x 72; padding 16px; border 2px solid #0000ff `blue`; background #ffffff `white`; text Futura PT 24/36 700, #0000ff `blue`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out, transform 0.3s ease-in-out; icon 20 x 20, #0000ff `blue`.

![Discover-more collapse (open) open](components/crops/collapse-toggle-open-open.png)

### Content pages

The rest of the product and editorial pages share the home's vocabulary: 60px display titles, text on photography, a signature-blue or boxed CTA. Push, Move, Note and Link are product pages; about/help/jobs are the editorial trio.

#### Push page title
Read as `push-title` on the Push page.

**Values (default).** size 156.67 x 78; background transparent; text Futura PT 60/78 700, #ffffff `white`.

![Push page title default](components/crops/push-title-default.png)

#### push primary CTA
Read as `push-cta` on the Push page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 185.95 x 50; padding 10px 0px 10px 38px; background transparent; text Futura PT 20/30 700, #0000ff `blue`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out |
| hover | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; text Futura PT 20/30 700, #000000 `black` |
| focus-visible | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; outline 2px solid #ff764d `focus-orange`, offset 2px; text Futura PT 20/30 700, #000000 `black` |
| pressed | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; text Futura PT 20/30 700, #000000 `black` |

![push primary CTA default](components/crops/push-cta-default.png) ![push primary CTA hover](components/crops/push-cta-hover.png) ![push primary CTA focus-visible](components/crops/push-cta-focus-visible.png) ![push primary CTA pressed](components/crops/push-cta-pressed.png)

#### Move page title
Read as `move-title` on the Move page.

**Values (default).** size 1200 x 175.03; padding 20px 0px 0px 0px; background transparent; text Futura PT 60/78 700, #ffffff `white`.

![Move page title default](components/crops/move-title-default.png)

#### move primary CTA
Read as `move-cta` on the Move page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 185.95 x 50; padding 10px 0px 10px 38px; background transparent; text Futura PT 20/30 700, #0000ff `blue`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out |
| hover | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; text Futura PT 20/30 700, #000000 `black` |
| focus-visible | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; outline 2px solid #ff764d `focus-orange`, offset 2px; text Futura PT 20/30 700, #000000 `black` |
| pressed | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; text Futura PT 20/30 700, #000000 `black` |

![move primary CTA default](components/crops/move-cta-default.png) ![move primary CTA hover](components/crops/move-cta-hover.png) ![move primary CTA focus-visible](components/crops/move-cta-focus-visible.png) ![move primary CTA pressed](components/crops/move-cta-pressed.png)

#### Note page title
Read as `note-title` on the Note page.

**Values (default).** size 1207 x 144; background transparent; text Futura PT 120/144 700, #d6ff00.

![Note page title default](components/crops/note-title-default.png)

#### note primary CTA
Read as `note-cta` on the Note page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 185.95 x 50; padding 10px 0px 10px 38px; background transparent; text Futura PT 20/30 700, #0000ff `blue`; transition opacity 0.3s ease-in-out, color 0.3s ease-in-out, background-color 0.3s ease-in-out, text-decoration 0.3s ease-in-out, top 0.3s ease-in-out, right 0.3s ease-in-out, bottom 0.3s ease-in-out, left 0.3s ease-in-out, width 0.3s ease-in-out, max-width 0.3s ease-in-out, height 0.3s ease-in-out, max-height 0.3s ease-in-out, padding-top 0.3s ease-in-out, padding-right 0.3s ease-in-out, padding-bottom 0.3s ease-in-out, padding-left 0.3s ease-in-out, box-shadow 0.3s ease-in-out, border-color 0.3s ease-in-out |
| hover | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; text Futura PT 20/30 700, #000000 `black` |
| focus-visible | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; outline 2px solid #ff764d `focus-orange`, offset 2px; text Futura PT 20/30 700, #000000 `black` |
| pressed | shadow rgba(255, 255, 255, 0) 0px 0px 0px 0px; text Futura PT 20/30 700, #000000 `black` |

![note primary CTA default](components/crops/note-cta-default.png) ![note primary CTA hover](components/crops/note-cta-hover.png) ![note primary CTA focus-visible](components/crops/note-cta-focus-visible.png) ![note primary CTA pressed](components/crops/note-cta-pressed.png)

#### Link page title
Read as `link-title` on the Link page.

**Values (default).** size 1200 x 220; background transparent; text futura-pt 110/110 700, #ffffff `white`.

![Link page title default](components/crops/link-title-default.png)

#### link primary CTA
The page's main call-to-action (a boxed button, or an arrow link on Link). Read as `link-cta` on the Link page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 410.13 x 31; background transparent; text futura-pt 24/36 700, #0000ff `blue` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

Child layers that carry the look: a::after 7.1875pxx7.1875px border 2px solid #0000ff `blue`.

![link primary CTA default](components/crops/link-cta-default.png) ![link primary CTA hover](components/crops/link-cta-hover.png) ![link primary CTA focus-visible](components/crops/link-cta-focus-visible.png) ![link primary CTA pressed](components/crops/link-cta-pressed.png)

#### About title
Read as `about-title` on the about page.

**Values (default).** size 666.69 x 84; background transparent; text Futura PT 30/42 700, #000000 `black`.

![About title default](components/crops/about-title-default.png)

#### about body text
Read as `about-body` on the about page.

**Values (default).** size 377.64 x 156; padding 0px 0px 12px 0px; background transparent; text Futura PT 120/144 700, #ffffff `white`.

![about body text default](components/crops/about-body-default.png)

#### Help title
Read as `help-title` on the help page.

**Values (default).** size 1200 x 144; background transparent; text Futura PT 120/144 700, #000000 `black`.

![Help title default](components/crops/help-title-default.png)

#### help body text
Read as `help-body` on the help page.

**Values (default).** size 317.78 x 56; background transparent; text Futura PT 20/28 400, #000000 `black`.

![help body text default](components/crops/help-body-default.png)

#### Jobs title
Read as `jobs-title` on the jobs page.

**Values (default).** size 1200.03 x 799.73; background transparent; text futura-pt 110/110 700, #00ffff.

![Jobs title default](components/crops/jobs-title-default.png)

#### jobs body text
Read as `jobs-body` on the jobs page.

**Values (default).** size 720 x 180; background transparent; text futura-pt 20/30 400, #000000 `black`.

![jobs body text default](components/crops/jobs-body-default.png)

### Trial page

The trial landing: a title, the edition cards and the signature-blue Download buttons. Nothing was ever downloaded.

#### Trial page title
"Start your free trial of Ableton Live" in the heading_l style. Read as `trial-title` on the trial page.

**Values (default).** size 720 x 216; background transparent; text futura-pt 90/108 700, #000000 `black`.

![Trial page title default](components/crops/trial-title-default.png)

#### Download button
A "Download" button for a trial edition. Measured, never pressed — the download would start. Read as `trial-download` on the trial page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 147.14 x 47; padding 6.5px 30px; border 2px solid transparent; background #0000ff `blue`; text futura-pt 20/30 700, #ffffff `white` |
| focus-visible | border 2px solid #000000 `black` |

![Download button default](components/crops/trial-download-default.png) ![Download button hover](components/crops/trial-download-hover.png) ![Download button focus-visible](components/crops/trial-download-focus-visible.png) ![Download button pressed](components/crops/trial-download-pressed.png)

#### Trial edition panel
A panel choosing between the Live editions for the trial. Read as `trial-edition-card` on the trial page.

**Values (default).** size 720 x 654.97; padding 120px 0px; background transparent; text futura-pt 90/108 700, #000000 `black`.

Child layers that carry the look: div 0x0 background #fbffa7; button 0x0 border 2px solid transparent; button::after 6pxx6px border 1px solid #0000ff `blue`.

![Trial edition panel default](components/crops/trial-edition-card-default.png)

### Shop

The shop index: product cards with a photo, a name, a price and an add-to-cart control. Nothing was added or bought.

#### Shop page title
Read as `shop-title` on the shop page.

**Values (default).** size 360 x 66; background transparent; text futura-pt 60/66 700, #000000 `black`.

![Shop page title default](components/crops/shop-title-default.png)

#### Product teaser card
A product tile in the shop grid (Live editions, Push, merchandise). Read as `product-card` on the shop page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 720 x 720; padding 120px; background #ffc3a5; text futura-pt 60/66 700, #000000 `black` |

![Product teaser card default](components/crops/product-card-default.png) ![Product teaser card hover](components/crops/product-card-hover.png)

#### Price
A product price in the shop. Read as `product-price` on the shop page.

**Values (default).** size 72.27 x 30; background transparent; text futura-pt 20/30 700, #ffffff `white`.

![Price default](components/crops/product-price-default.png)

#### Add-to-cart button
The buy control on a shop tile. Measured, never pressed — pressing carts a product. Read as `add-to-cart` on the shop page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 360 x 44; background transparent; text futura-pt 16/24 400, #ffffff `white` |

Child layers that carry the look: input 128.3x44 background #0000ff `blue`.

![Add-to-cart button default](components/crops/add-to-cart-default.png) ![Add-to-cart button hover](components/crops/add-to-cart-hover.png) ![Add-to-cart button focus-visible](components/crops/add-to-cart-focus-visible.png) ![Add-to-cart button pressed](components/crops/add-to-cart-pressed.png)

### Packs

The Packs catalogue: a 40k px grid of pack cards (artwork, name, genre tags) with signature-blue download/buy controls. Nothing was bought or downloaded.

#### Packs page title
Read as `packs-title` on the Packs page.

**Values (default).** size 1200.03 x 66; background transparent; text futura-pt 60/66 700, #00ffaf.

![Packs page title default](components/crops/packs-title-default.png)

#### Pack card
A Pack tile in the catalogue grid. Read as `pack-card` on the Packs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1440 x 348; padding 90px 120px; background #000000 `black`; text futura-pt 60/66 700, #00ffaf |

![Pack card default](components/crops/pack-card-default.png) ![Pack card hover](components/crops/pack-card-hover.png)

#### Pack download button
A "Download" button on a Pack row; links to /en/login/ (the download needs an account). Measured, never followed. Read as `pack-download` on the Packs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 143.14 x 44; padding 7px 30px; background #0000ff `blue`; text futura-pt 20/30 700, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 1px |

![Pack download button default](components/crops/pack-download-default.png) ![Pack download button hover](components/crops/pack-download-hover.png) ![Pack download button focus-visible](components/crops/pack-download-focus-visible.png) ![Pack download button pressed](components/crops/pack-download-pressed.png)

### Blog

The blog index: a title, then rows of posts each carrying a salmon category badge.

#### Blog page title
Read as `blog-title` on the blog page.

**Values (default).** size 1200.03 x 78; background transparent; text futura-pt 60/78 700, #000000 `black`.

![Blog page title default](components/crops/blog-title-default.png)

#### Article teaser
An article row in the blog index. Read as `blog-row` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 360 x 521.5; background transparent; text futura-pt 14/21 700, #000000 `black` |

Child layers that carry the look: abl-click-remote 360x202.5 background #bfbfbf; a 87.3x25 background #ff8389 `salmon`; li::before 2.8pxx2.8px background #000000 `black`.

![Article teaser default](components/crops/blog-row-default.png) ![Article teaser hover](components/crops/blog-row-hover.png)

#### Entry category badge
The coloured category badge on a blog index row (Artists / Downloads / Tutorials). Read as `blog-category-badge` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 87.25 x 25; padding 2px 12px; background #ff8389 `salmon`; text futura-pt 14/21 700, #000000 `black` |

![Entry category badge default](components/crops/blog-category-badge-default.png) ![Entry category badge hover](components/crops/blog-category-badge-hover.png)

### Log in / register (resting only)

The account page's two forms side by side: Log in (email + password + submit) and Register (email + country select + terms checkbox + submit). Captured at rest and focused only: no credentials were ever typed and neither form was submitted.

#### Log in title
Read as `login-title` on the log in / register page.

**Values (default).** size 540 x 66; background transparent; text futura-pt 60/66 700, #000000 `black`.

![Log in title default](components/crops/login-title-default.png)

#### Log in form
The Log in card: username and password fields plus the submit. Measured at rest — nothing typed, nothing submitted. Read as `login-form` on the log in / register page.

**Values (default).** size 540 x 246.38; background transparent; text futura-pt 14/21 700, #000000 `black`.

Child layers that carry the look: input 380x46 background #eeeeee `field-gray`; input 380x46 background #eeeeee `field-gray`; input 107.9x44 background #0000ff `blue`.

![Log in form default](components/crops/login-form-default.png)

#### Username field
The username text field. Clicked into for the focus style; nothing typed. Read as `login-field` on the log in / register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 46; padding 8px 15px; background #eeeeee `field-gray`; text futura-pt 20/30 400, #000000 `black`; placeholder #000000 `black` |
| focused | outline 1px auto #005fcc `focus-blue`, offset 0px |

![Username field default](components/crops/login-field-default.png) ![Username field focused](components/crops/login-field-focused.png)

#### Log in button
The form's submit. Measured in every state — never pressed. Read as `login-submit` on the log in / register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 107.89 x 44; padding 7px 30px; background #0000ff `blue`; text futura-pt 20/30 700, #ffffff `white`; placeholder #ffffff `white` |
| focus-visible | outline 1px auto #005fcc `focus-blue`, offset 0px |

![Log in button default](components/crops/login-submit-default.png) ![Log in button hover](components/crops/login-submit-hover.png) ![Log in button focus-visible](components/crops/login-submit-focus-visible.png) ![Log in button pressed](components/crops/login-submit-pressed.png)

#### Register form
The Register card beside Log in: email, password, names, country select and a newsletter checkbox. Measured at rest. Read as `register-form` on the log in / register page.

**Values (default).** size 540 x 768.95; background transparent; text futura-pt 14/21 700, #000000 `black`.

Child layers that carry the look: input 380x46 background #eeeeee `field-gray`; ul 0x0 background #ffc2ca; ul::after autoxauto border 8px solid transparent.

![Register form default](components/crops/register-form-default.png)

#### Register email field
The email field of the register form. Clicked into only. Read as `register-field` on the log in / register page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 46; padding 8px 15px; background #eeeeee `field-gray`; text futura-pt 20/30 400, #000000 `black`; placeholder #000000 `black` |
| focused | outline 1px auto #005fcc `focus-blue`, offset 0px |

![Register email field default](components/crops/register-field-default.png) ![Register email field focused](components/crops/register-field-focused.png)

#### Country select
Read as `register-select` on the log in / register page.

**Values (default).** size 380 x 44; padding 7px 50px 7px 15px; background #eeeeee `field-gray`; text futura-pt 20/30 400, #000000 `black`.

![Country select default](components/crops/register-select-default.png)

#### Newsletter checkbox
Read as `register-checkbox` on the log in / register page.

**Values (default).** size 13 x 13; background transparent; text futura-pt 20/normal 400, #000000 `black`; placeholder #000000 `black`.

![Newsletter checkbox default](components/crops/register-checkbox-default.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844: the collapsed top bar with its hamburger trigger, the hero title at 20px, the trial CTA.

#### Mobile top bar
The mobile header: logo left, menu trigger right. Read as `m-nav-bar` on the home page at 390 wide.

**Values (default).** size 390 x 69; padding 20px 0px 0px 0px; background transparent; text futura-pt 20/30 700, #000000 `black`; icon 60 x 28, #000000 `black`.

Child layers that carry the look: button::after 0pxx0px border 5px solid #000000 `black`; div 390x1004 background #0000ff `blue`; span::before 12pxx2px background #ffffff `white`.

![Mobile top bar default](components/crops/m-nav-bar-default.png)

#### Mobile menu trigger
The mobile menu button. Measured, not opened. Read as `m-menu-trigger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 64.06 x 30; background transparent; text futura-pt 20/30 700, #000000 `black`; transition color 0.35s ease |

Child layers that carry the look: button::after 0pxx0px border 5px solid #000000 `black`.

![Mobile menu trigger default](components/crops/m-menu-trigger-default.png) ![Mobile menu trigger pressed](components/crops/m-menu-trigger-pressed.png)

#### Mobile hero headline
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 325.03 x 60; background transparent; text futura-pt 20/30 700, #ffffff `white`.

![Mobile hero headline default](components/crops/m-hero-title-default.png)

#### Mobile trial CTA
Read as `m-trial-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 147.95 x 26; background transparent; text futura-pt 20/30 700, #ffffff `white` |

![Mobile trial CTA default](components/crops/m-trial-cta-default.png) ![Mobile trial CTA pressed](components/crops/m-trial-cta-pressed.png)

## Icons

11 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Photography and product artwork were left out; these are the interface icons (the grid-mark logo, the social buttons, the video/audio play badges, a disclosure chevron). The SVGs are Ableton's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [ableton](icons/ableton.svg) | 60x30 | 0 0 45 21 | fill | en/live/; en/help/ | Ableton |
| [discover-more-roar-sounds](icons/discover-more-roar-sounds.svg) | 20x20 | 0 0 20 20 | stroke | en/live/ | Discover more Roar sounds |
| [go-to-discord](icons/go-to-discord.svg) | 32x32 | 0 0 48 48 | fill | en/; en/blog/; en/packs/; en/login/ | Go to Discord |
| [go-to-facebook](icons/go-to-facebook.svg) | 32x32 | 0 0 48 48 | fill | en/; en/blog/; en/packs/; en/login/ | Go to Facebook |
| [go-to-homepage](icons/go-to-homepage.svg) | 60x28 | 0 0 45 21 | fill | en/; en/blog/; en/packs/; en/login/ | Go to homepage |
| [go-to-instagram](icons/go-to-instagram.svg) | 32x32 | 0 0 48 48 | fill | en/; en/blog/; en/packs/; en/login/ | Go to Instagram |
| [go-to-tiktok](icons/go-to-tiktok.svg) | 32x32 | 0 0 48 48 | fill | en/; en/blog/; en/packs/; en/login/ | Go to TikTok |
| [go-to-twitter](icons/go-to-twitter.svg) | 32x32 | 0 0 48 48 | fill | en/; en/blog/; en/packs/; en/login/ | Go to Twitter |
| [go-to-youtube](icons/go-to-youtube.svg) | 32x32 | 0 0 48 48 | fill | en/; en/blog/; en/packs/; en/login/ | Go to Youtube |
| [play-bassline](icons/play-bassline.svg) | 32x32 | 0 0 32 32 | fill | en/live/ | Play : Bassline |
| [play-video](icons/play-video.svg) | 60x60 | 0 0 60 60 | fill | en/live/ | Play: VIDEO |

## Gaps

### Pages

- **Everything behind the account.** The login and register forms were measured at rest and focus only: no credentials were entered and nothing was submitted, so the signed-in account area (licenses, downloads, order history, settings, the forum, the ableton.com user section) is completely uncaptured.
- **The checkout.** Add-to-cart was never pressed and no purchase flow was started, so the cart, checkout and payment steps are missing.
- **Downloads.** The trial Download and the Packs' download/buy controls were measured but never pressed; no file was fetched.
- **Learning microsites.** `learn.ableton.com`, `learningsynths.ableton.com` and `makingmusic.ableton.com` are separate Ableton properties with their own front ends; they were linked but not captured.
- **A few public sections were skipped for scope:** the Classroom, Colleges & Universities, Certified Training and Ausbildung pages were probed and are plain content pages in the same shell; they add no new components.

### States

- **Pressed** was forced with DevTools (`:active`), so a state a script adds on mousedown is missing if one exists.
- **The consent states.** Accept / Close / More-info were measured but never clicked: the post-consent UI (whatever the site does once you answer) is uncaptured.
- **Video and audio.** The Live page's play buttons open a YouTube modal or start an audio player; neither was started, so the players are measured at rest only.
- **The mobile menu overlay** was probed through `m-menu-trigger` but its opened full-screen menu was not captured as a screenshot state.
- **Disabled states** were not seen on any public control.

### Themes

Ableton shows one light theme. Its stylesheets declare no CSS custom properties at all (`raw/css-vars.json` resolves zero rules; the only unreadable sheets were the two cross-origin Adobe Typekit kit sheets), no `prefers-color-scheme` variant and no theme attribute, so the token file ships a single `light` set and every colour is a measured literal rather than a variable alias.

### Fonts

- **Futura PT** is served from Adobe Typekit (`use.typekit.net`), whose sheets are cross-origin to CSSOM reads; the family name and weights are measured on the rendered elements instead, and the style guide falls back to a system sans for display.

### Screenshots

- Photography, product artwork and video frames are Ableton's content and appear only inside screenshots and crops. Hero cells carry video, so two captures of the same page can differ in the frame shown.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article body text, product copy and form option lists were not transcribed; only the frames around them were measured.
- No personal data was captured: every page was read signed out, and the only forms touched were fields measured and left empty.
