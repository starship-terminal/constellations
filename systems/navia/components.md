# Navia components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.thenavia.com on 2026-11-21, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was sent, submitted or signed into. The measurement file records its own read date as 2026-11-21.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (29 components, 66 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (61 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [cookie-preferences](screenshots/home-light-cookie-preferences.png), [cookies](screenshots/home-light-cookies.png), [default](screenshots/home-light-default.png), [feature](screenshots/home-light-feature.png), [full](screenshots/home-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog post | `/blog/how-do-i-know-if-my-marketing-is-working` | [default](screenshots/post-light-default.png), [full](screenshots/post-light-full.png) |
| Contact | `/contact-us` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png), [select-focused](screenshots/contact-light-select-focused.png) |
| Privacy | `/privacy-policy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Terms | `/terms-and-conditions` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Do not sell | `/do-not-sell-or-share-my-personal-information` | [default](screenshots/do-not-sell-light-default.png), [full](screenshots/do-not-sell-light-full.png) |
| App wall | `https://app.thenavia.com/` | [default](screenshots/app-wall-light-default.png) |
| Home, phone | `/` | [cookies](screenshots/mobile-home-light-cookies.png), [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Blog, phone | `/blog` | [default](screenshots/mobile-blog-light-default.png), [full](screenshots/mobile-blog-light-full.png) |
| Post, phone | `/blog/how-do-i-know-if-my-marketing-is-working` | [default](screenshots/mobile-post-light-default.png) |
| Contact, phone | `/contact-us` | [default](screenshots/mobile-contact-light-default.png), [full](screenshots/mobile-contact-light-full.png) |
| Privacy, phone | `/privacy-policy` | [default](screenshots/mobile-privacy-light-default.png) |
| App wall, phone | `https://app.thenavia.com/` | [default](screenshots/mobile-app-wall-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie banner | every marketing page | first paint, before Reject All | [home-light-cookies](screenshots/home-light-cookies.png) |
| Cookie preferences | home | Customise on the cookie banner | [home-light-cookie-preferences](screenshots/home-light-cookie-preferences.png) |
| Feature item selected | home | click a feature row; selection stays on the page | [home-light-feature](screenshots/home-light-feature.png) |
| Topic select focused | contact | focus the select; no option chosen | [contact-light-select-focused](screenshots/contact-light-select-focused.png) |
| Mobile menu, open | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 11 components were given a real keyboard focus (a further 1 could not be driven: `submit`). 11 show a visible focus state: `nav-link` (1px auto #005fcc, offset 1px), `hero-cta` (1px auto #005fcc, offset 1px), `hero-secondary` (1px auto #005fcc, offset 1px), `feature-item` (2px solid #36312a `color.scheme.1..text`, offset 6px), `plan-cta` (1px auto #005fcc, offset 1px), `article-card` (1px auto #005fcc, offset 1px), `pager-next` (2px solid #36312a `color.scheme.1..text`, offset 3px), `text-field` (visible change in borderTopColor/backgroundColor), `select` (visible change in borderTopColor/backgroundColor), `footer-link` (1px auto #005fcc, offset 1px), `m-menu-button` (1px solid #4d65ff, offset 1.90625px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): links and buttons fade or lift as measured. Nothing that would submit or navigate was pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | background-color, border-color, color, padding | email-field, select, submit, text-area, text-field |
| 0.3s | `cubic-bezier(0.625, 0.05, 0, 1)` | background-color, border-color, color | pager-next |
| 0.5s | `cubic-bezier(0.625, 0.05, 0, 1)` | transform | header, m-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Header](#header) | 1440 x 72 | 1px solid rgba(255, 255, 255, 0.2) | 8px | rgba(255, 255, 255, 0.15) | none | 0px 72px |
| [Hero title](#hero-title) | 800 x 184.78 | - | - | transparent | none | 0 |
| [Plan card](#plan-card) | 410.66 x 797.59 | - | 64px | #f88450 | none | 40px 32px 32px 32px |
| [Article card](#article-card) | 944 x 720 | - | 80px | #ffffff `base.color.neutral..white` | none | 32px |
| [Text field](#text-field) | 292 x 44 | 1px solid #36312a `color.scheme.1..text` | 4px | #faf4e6 `color.scheme.1..background` | none | 8px 12px |
| [Submit](#submit) | 101.69 x 48 | - | 64px | #f88450 | none | 12px 24px |
| [Footer](#footer) | 1296 x 900 | - | 64px | #e8ff39 `color.scheme.1..accent` | none | 240px 0px 32px 0px |

## Components

### Shell and navigation

The cream header: wordmark, Platform, Pricing, Resources, and the chartreuse Get started pill.

#### Header
The top nav: wordmark, Platform, Pricing, Resources, Get started. Read as `header` on the home page.

**Values (default).** size 1440 x 72; padding 0px 72px; background transparent; text Publicsans Variablefont Wght 16/16 400, #ffffff `base.color.neutral..white`; transition transform 0.5s cubic-bezier(0.625, 0.05, 0, 1).

Child layers that carry the look: nav 324.6x58 background rgba(255, 255, 255, 0.15) border 1px solid rgba(255, 255, 255, 0.2) radius 8px; div 0x0 background #e8ff39 `color.scheme.1..accent` radius 64px; div 0x0 background #ffffff `base.color.neutral..white`.

![Header default](components/crops/header-default.png)

#### Logo
The wordmark. Measured, never followed. Read as `logo` on the home page.

**Values (default).** size 270.84 x 36; background transparent; text Publicsans Variablefont Wght 16/24 400, #36312a `color.scheme.1..text`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A nav item. Measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 64.42 x 48; background transparent; text Publicsans Variablefont Wght 16/16 400, #ffffff `base.color.neutral..white` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav Get started
The nav action. It opens the app sign-in wall. Measured, never followed. Read as `nav-cta` on the home page.

Not on the page when it was captured.

### Home

The landing: Lora hero, feature list, plan cards.

#### Hero title
Read as `hero-title` on the home page.

**Values (default).** size 800 x 184.78; background transparent; text Lora Variablefont Wght 56/61.6 400, #ffffff `base.color.neutral..white`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero CTA
Primary action. Opens the app wall. Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 241.09 x 48; background transparent; text Publicsans Variablefont Wght 16/24 500, #36312a `color.scheme.1..text` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

Child layers that carry the look: div 193.1x48 background #e8ff39 `color.scheme.1..accent` radius 64px; div 231.7x57.6 background #ffffff `base.color.neutral..white`; div 48x48 background #e8ff39 `color.scheme.1..accent` radius 100%.

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Book a demo
Secondary action. Opens an external calendar. Measured, never followed. Read as `hero-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 144.22 x 48; background transparent; text Publicsans Variablefont Wght 16/24 500, #36312a `color.scheme.1..text` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

Child layers that carry the look: div 144.2x48 background #ffffff `base.color.neutral..white` radius 64px; div 173.1x57.6 background #e8ff39 `color.scheme.1..accent`; div 0x0 background #ffffff `base.color.neutral..white` radius 100%.

![Book a demo default](components/crops/hero-secondary-default.png) ![Book a demo hover](components/crops/hero-secondary-hover.png) ![Book a demo focus-visible](components/crops/hero-secondary-focus-visible.png) ![Book a demo pressed](components/crops/hero-secondary-pressed.png)

#### Feature item
One of four in-page feature selectors. Read as `feature-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 531.2 x 107.88; background transparent; text Lora Variablefont Wght 22.4/26.88 400, #36312a `color.scheme.1..text` |
| focus-visible | outline 2px solid #36312a `color.scheme.1..text`, offset 6px |

Child layers that carry the look: div 531.2x1 background #cdc7b8 `color.scheme.1..border`.

![Feature item default](components/crops/feature-item-default.png) ![Feature item hover](components/crops/feature-item-hover.png) ![Feature item focus-visible](components/crops/feature-item-focus-visible.png) ![Feature item pressed](components/crops/feature-item-pressed.png)

#### Feature item, selected
A feature item after its own toggle. The selection moves locally. Read as `feature-item-selected` on the home page.

**Values (selected).** size 531.2 x 75.25; padding 14px 0px 0px 0px; background transparent; text Lora Variablefont Wght 22.4/26.88 400, #36312a `color.scheme.1..text`; opacity 0.698.

Child layers that carry the look: div 531.2x1 background #cdc7b8 `color.scheme.1..border`.

![Feature item, selected selected](components/crops/feature-item-selected-selected.png)

#### Section heading
Read as `section-title` on the home page.

**Values (default).** size 624 x 172.78; background transparent; text Lora Variablefont Wght 48/57.6 400, #36312a `color.scheme.1..text`.

![Section heading default](components/crops/section-title-default.png)

#### Plan card
A pricing plan. The Sign up link is not followed. Read as `plan-card` on the home page.

**Values (default).** size 410.66 x 797.59; padding 40px 32px 32px 32px; border 1px solid #cdc7b8 `color.scheme.1..border`; radius 8px; background transparent; text Notemakersmark 40/40 400, #f88450; icon 12.8 x 16, #f88450.

![Plan card default](components/crops/plan-card-default.png)

#### Plan Sign up
A plan action. Opens the app wall. Measured, never followed. Read as `plan-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 344.66 x 48; background transparent; text Publicsans Variablefont Wght 16/24 500, #36312a `color.scheme.1..text` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

Child layers that carry the look: div 241.3x48 background #f88450 radius 64px; div 289.5x57.6 background #ffffff `base.color.neutral..white`; div 48x48 background #f88450 radius 100%.

![Plan Sign up default](components/crops/plan-cta-default.png) ![Plan Sign up hover](components/crops/plan-cta-hover.png) ![Plan Sign up focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan Sign up pressed](components/crops/plan-cta-pressed.png)

#### Testimonial
Read as `testimonial` on the home page.

**Values (default).** size 400 x 348.41; radius 4px; background transparent; text Publicsans Variablefont Wght 16/24 400, #36312a `color.scheme.1..text`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Blog

The resources index and its pager.

#### Blog title
Read as `blog-title` on the blog page.

**Values (default).** size 880 x 192; background transparent; text Lora Variablefont Wght 80/96 400, #36312a `color.scheme.1..text`.

![Blog title default](components/crops/blog-title-default.png)

#### Article card
A blog index card. Measured, never followed. Read as `article-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 944 x 720; padding 32px; background transparent; text Publicsans Variablefont Wght 16/24 400, #36312a `color.scheme.1..text` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

Child layers that carry the look: div 99x40 background #ffffff `base.color.neutral..white` radius 80px; div 137.7x48 background #e8ff39 `color.scheme.1..accent` radius 64px; div 165.2x57.6 background #ffffff `base.color.neutral..white`.

![Article card default](components/crops/article-card-default.png) ![Article card hover](components/crops/article-card-hover.png) ![Article card focus-visible](components/crops/article-card-focus-visible.png) ![Article card pressed](components/crops/article-card-pressed.png)

#### Blog Next
The index pager. Measured, never followed in this pass. Read as `pager-next` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 109.36 x 48; padding 12px 24px; border 1px solid #f88450; radius 64px; background #f88450; text Publicsans Variablefont Wght 16/16 400, #36312a `color.scheme.1..text`; transition background-color 0.3s cubic-bezier(0.625, 0.05, 0, 1), color 0.3s cubic-bezier(0.625, 0.05, 0, 1), border-color 0.3s cubic-bezier(0.625, 0.05, 0, 1); icon 12 x 12, #36312a `color.scheme.1..text` |
| hover | border 1px solid #36312a `color.scheme.1..text`; background #36312a `color.scheme.1..text`; text Publicsans Variablefont Wght 16/16 400, #ffffff `base.color.neutral..white`; icon 12 x 12, #ffffff `base.color.neutral..white` |
| focus-visible | outline 2px solid #36312a `color.scheme.1..text`, offset 3px |
| pressed | border 1px solid #36312a `color.scheme.1..text`; background #36312a `color.scheme.1..text`; text Publicsans Variablefont Wght 16/16 400, #ffffff `base.color.neutral..white`; icon 12 x 12, #ffffff `base.color.neutral..white` |

![Blog Next default](components/crops/pager-next-default.png) ![Blog Next hover](components/crops/pager-next-hover.png) ![Blog Next focus-visible](components/crops/pager-next-focus-visible.png) ![Blog Next pressed](components/crops/pager-next-pressed.png)

### Contact

The public contact form. Fields were focused. Nothing was typed or submitted.

#### Contact title
Read as `contact-title` on the contact page.

**Values (default).** size 480 x 76.8; background transparent; text Lora Variablefont Wght 64/76.8 400, #36312a `color.scheme.1..text`.

![Contact title default](components/crops/contact-title-default.png)

#### Text field
A contact field. Focused only. Nothing typed or sent. Read as `text-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 292 x 44; padding 8px 12px; border 1px solid #36312a `color.scheme.1..text`; radius 4px; background #faf4e6 `color.scheme.1..background`; text Publicsans Variablefont Wght 16/25.6 400, #36312a `color.scheme.1..text`; transition background-color 0.2s ease, padding 0.2s ease, border-color 0.2s ease; placeholder rgba(0, 0, 0, 0.6) |
| hover | border 1px solid #f88450 |
| focus-visible, focused | padding 8px 12px 8px 16px; border 1px solid #ffffff `base.color.neutral..white`; background #ffffff `base.color.neutral..white` |

![Text field default](components/crops/text-field-default.png) ![Text field hover](components/crops/text-field-hover.png) ![Text field focus-visible](components/crops/text-field-focus-visible.png) ![Text field focused](components/crops/text-field-focused.png)

#### Email field
Focused only. Nothing typed or sent. Read as `email-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 292 x 44; padding 8px 12px; border 1px solid #36312a `color.scheme.1..text`; radius 4px; background #faf4e6 `color.scheme.1..background`; text Publicsans Variablefont Wght 16/25.6 400, #36312a `color.scheme.1..text`; transition background-color 0.2s ease, padding 0.2s ease, border-color 0.2s ease; placeholder rgba(0, 0, 0, 0.6) |
| focused | padding 8px 12px 8px 16px; border 1px solid #ffffff `base.color.neutral..white`; background #ffffff `base.color.neutral..white` |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png)

#### Message field
Focused only. Nothing typed or sent. Read as `text-area` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 608 x 180; padding 12px; border 1px solid #36312a `color.scheme.1..text`; radius 4px; background #faf4e6 `color.scheme.1..background`; text Publicsans Variablefont Wght 16/25.6 400, #36312a `color.scheme.1..text`; transition background-color 0.2s ease, padding 0.2s ease, border-color 0.2s ease; placeholder rgba(0, 0, 0, 0.6) |
| focused | padding 12px 12px 12px 16px; border 1px solid #ffffff `base.color.neutral..white`; background #ffffff `base.color.neutral..white` |

![Message field default](components/crops/text-area-default.png) ![Message field focused](components/crops/text-area-focused.png)

#### Topic select
Focused only. No option chosen and nothing sent. Read as `select` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 608 x 44; padding 8px 12px; border 1px solid #36312a `color.scheme.1..text`; radius 4px; background #faf4e6 `color.scheme.1..background`; image url(…); text Publicsans Variablefont Wght 16/25.6 400, #36312a `color.scheme.1..text`; transition background-color 0.2s ease, padding 0.2s ease, border-color 0.2s ease |
| hover | border 1px solid #f88450 |
| focus-visible, focused | padding 8px 12px 8px 16px; border 1px solid #ffffff `base.color.neutral..white`; background #ffffff `base.color.neutral..white` |

![Topic select default](components/crops/select-default.png) ![Topic select hover](components/crops/select-hover.png) ![Topic select focus-visible](components/crops/select-focus-visible.png) ![Topic select focused](components/crops/select-focused.png)

#### Submit
The contact submit. Measured, never pressed. Read as `submit` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 101.69 x 48; padding 12px 24px; radius 64px; background #f88450; text Publicsans Variablefont Wght 16/24 400, #36312a `color.scheme.1..text`; transition background-color 0.2s ease, color 0.2s ease; placeholder #36312a `color.scheme.1..text` |
| hover | background #36312a `color.scheme.1..text`; text Publicsans Variablefont Wght 16/24 400, #ffffff `base.color.neutral..white`; placeholder #ffffff `base.color.neutral..white` |

![Submit default](components/crops/submit-default.png) ![Submit hover](components/crops/submit-hover.png) ![Submit focus-visible](components/crops/submit-focus-visible.png)

### Legal

The privacy-policy title.

#### Legal title
Read as `legal-title` on the privacy policy page.

**Values (default).** size 640 x 76.8; background transparent; text Lora Variablefont Wght 64/76.8 400, #36312a `color.scheme.1..text`.

![Legal title default](components/crops/legal-title-default.png)

### Footer

Footer links on the home page.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1296 x 900; padding 240px 0px 32px 0px; background transparent; text Lora Variablefont Wght 48/57.6 400, #ffffff `base.color.neutral..white`.

Child layers that carry the look: div 193.1x48 background #e8ff39 `color.scheme.1..accent` radius 64px; div 231.7x57.6 background #ffffff `base.color.neutral..white`; div 48x48 background #e8ff39 `color.scheme.1..accent` radius 100%.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 241.09 x 48; background transparent; text Publicsans Variablefont Wght 16/24 500, #36312a `color.scheme.1..text` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

Child layers that carry the look: div 193.1x48 background #e8ff39 `color.scheme.1..accent` radius 64px; div 231.7x57.6 background #ffffff `base.color.neutral..white`; div 48x48 background #e8ff39 `color.scheme.1..accent` radius 100%.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Mobile (390 wide)

The same home surface at 390 wide, with the menu open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 61.02; padding 0px 19.5px; background transparent; text Publicsans Variablefont Wght 15.25/22.88 400, #36312a `color.scheme.1..text`; transition transform 0.5s cubic-bezier(0.625, 0.05, 0, 1); icon 118.22 x 34.31, #36312a `color.scheme.1..text`.

Child layers that carry the look: nav 0x0 background #36312a `color.scheme.1..text`; div 0x0 background #e8ff39 `color.scheme.1..accent` radius 61.0209px; div 0x0 background #ffffff `base.color.neutral..white`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 40.38 x 48; background transparent; text Publicsans Variablefont Wght 24/36 400, #36312a `color.scheme.1..text` |
| focus-visible | outline 1px solid #4d65ff, offset 1.90625px |

Child layers that carry the look: div 24x2 background #ffffff `base.color.neutral..white`; div 24x2 background #ffffff `base.color.neutral..white`; div 24x2 background #ffffff `base.color.neutral..white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile menu, open
The bar after its own toggle. The crop is the opened nav panel. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 40.38 x 48; background transparent; text Publicsans Variablefont Wght 24/36 400, #ffffff `base.color.neutral..white`.

Child layers that carry the look: div 18.4x18.4 background #ffffff `base.color.neutral..white`; div 24x2 background #ffffff `base.color.neutral..white`; div 18.4x18.4 background #ffffff `base.color.neutral..white`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
Read inside the open menu. Measured, never followed. Read as `m-nav-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 336.63 x 76.27; background transparent; text Lora Variablefont Wght 30.51/30.51 400, #ffffff `base.color.neutral..white` |

![Mobile nav link default](components/crops/m-nav-link-default.png) ![Mobile nav link hover](components/crops/m-nav-link-hover.png)

## Icons

No standalone SVG icon set was lifted. The wordmark, hamburger bars, and social glyphs stay in the crops and screenshots. They are Navia's artwork.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Anything that sends, submits or signs in.** No form was submitted and no account was created. Contact fields were focused only. The app wall at app.thenavia.com was recorded and not passed. accounts.thenavia.com/sign-in stopped at a Cloudflare check.

### States

- **Pressed** was forced with DevTools on controls that expose it. Submit has no pressed state in the measurement file.
- **Disabled, error, loading, and success** were not shown. The contact form and the newsletter popup were not submitted, so validation states are Not captured.
- **Designed focus ring.** Measured focus-visible states did not paint a site-authored outline. Recorded as Not captured, not as a sampled blue ring.

### Themes

The site paints one light theme on every captured route: no dark class or attribute is bound, so the dark set is not emitted. The Relume/Webflow palette is recorded in [raw/css-vars.json](raw/css-vars.json).

### Fonts

- **Headings** compute `Lora Variablefont Wght`. **UI and fields** compute `Publicsans Variablefont Wght`. **Notemakersmark** is declared on :root and was not computed on a captured control.
- The style guide renders with Georgia and system-ui fallbacks. The variable font files are not bundled.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- Blog index pages 3 and 4 were mapped and not screenshotted. Phone captures omit terms and do-not-sell. The hamburger crop was empty after quantize because the icon is three 24 by 2 bars on a transparent button; the open menu screenshot shows it.

### Content left out

- Photography, the wordmark, and article copy belong to Navia. The published contact mailbox was hidden before the contact screenshots were taken and is not written in this package.
