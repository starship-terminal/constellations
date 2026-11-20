# Clipchamp components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from clipchamp.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid for or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (45 components, 88 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `segoeVariableFont 16/24 500, #6453e4`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (87 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png`; every public route paints the same light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages (1x on desktop, 2x on mobile); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/en/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Pricing | `/en/pricing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Features | `/en/features/` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Products | `/en/products/` | [default](screenshots/products-light-default.png), [full](screenshots/products-light-full.png) |
| For work | `/en/clipchamp-for-work/` | [default](screenshots/forwork-light-default.png), [full](screenshots/forwork-light-full.png) |
| For education | `/en/clipchamp-for-education/` | [default](screenshots/education-light-default.png), [full](screenshots/education-light-full.png) |
| Video templates | `/en/video-templates/` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Company | `/en/company/` | [default](screenshots/company-light-default.png), [full](screenshots/company-light-full.png) |
| Blog | `/en/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| What's new | `/en/whats-new/` | [default](screenshots/whatsnew-light-default.png), [full](screenshots/whatsnew-light-full.png) |
| Stock | `/en/stock/` | [default](screenshots/stock-light-default.png), [full](screenshots/stock-light-full.png) |
| Screen recorder | `/en/screen-recorder/` | [default](screenshots/recorder-light-default.png), [full](screenshots/recorder-light-full.png) |
| Sign-in (boundary) | `app.clipchamp.com/login` | [default](screenshots/signin-light-default.png) |
| Home, phone | `/en/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu-open](screenshots/mobile-home-light-menu-open.png) |
| Pricing, phone | `/en/pricing/` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Features, phone | `/en/features/` | [default](screenshots/mobile-features-light-default.png), [full](screenshots/mobile-features-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu, open | bar, phone | the hamburger's own press | [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png), [m-menu-open](#mobile-menu-open) |
| Nav dropdown, open | nav bar, desktop | the Features trigger's own hover (href="#", held open) | [nav-submenu](#nav-submenu), [nav-submenu-link](#nav-submenu-link) |
| FAQ item, open | pricing page | the details summary's own toggle | [faq-item](#faq-item) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus. 14 show a visible focus state: `nav-item` (1px auto #101010, offset 1px), `nav-signin` (2px solid #000000, offset 2px), `nav-cta` (2px solid #000000, offset 2px), `hero-cta` (2px solid #ffffff, offset 2px), `cta-secondary` (2px solid #000000, offset 2px), `cta-white` (2px solid #ffffff, offset 2px), `feature-card` (1px auto rgb(16, 16, 16) offset 1px on a (child layer)), `inline-link` (1px auto #101010, offset 1px), `signin-button` (visible change in boxShadow/borderTopColor), `footer-link` (1px auto #101010, offset 1px), `footer-social` (2px solid #6453e4 `color.purple.80`, offset 2px), `m-menu-link` (5px auto #e59700, offset 2px), `feature-link` (1px auto #101010, offset 1px), `pricing-cta` (2px solid #ffffff, offset 2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the purple controls hold their #4d43de hover step and 1.05 scale through press — hover and pressed are the same painted step on this surface. Nothing a real press would submit or navigate was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | background, color | feature-cell, feature-tooltip, nav-item |
| 0.1s | `ease-in-out` | all | signin-button |
| 0.2s | `ease` | all, box-shadow, color, font-variation-settings, transform | cta-secondary, cta-white, feature-card, footer-lang, footer-link, hero-cta, m-menu-button, nav-cta and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Feature link card](#feature-link-card) | 402.61 x 221.38 | - | 12px | #ffffff | rgba(28, 28, 40, 0.1) 0px 4px 8px 0px, rgba(28, 28, 40, 0.1) 0px 0px 2px 0px | 16px |

## Components

### Shell and navigation

The sticky top nav on the light ground: wordmark, the four dropdown menus, the outline Sign-in button and the purple Try-for-free CTA.

#### Nav bar
The sticky 1440 top nav (position:sticky): logo, four dropdown menus, Sign-in and Try-for-free actions. Read as `header` on the home page.

**Values (default).** size 1440 x 62; background #ffffff; text segoeVariableFont 18/20 400, #545472.

![Nav bar default](components/crops/header-default.png)

#### Logo
The Clipchamp wordmark anchor (purple mark + logotype; the mark paints #5a4cdb). Read as `logo` on the home page.

**Values (default).** size 146.81 x 32; background transparent; text segoeVariableFont 16/20 400, #6453e4 `color.purple.80`.

![Logo default](components/crops/logo-default.png)

#### Nav menu trigger
The "Features" dropdown trigger — an anchor with role=button/aria-haspopup that opens its submenu locally, never navigates. Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 108 x 44; padding 12px; background transparent; text segoeVariableFont 18/20 400, #545472; transition color 0.1s ease; icon 16 x 16, rgba(28, 28, 28, 0.5) |
| hover | text segoeVariableFont 18/20 400, #6453e4 `color.purple.80`; icon 16 x 16, #6453e4 `color.purple.80` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a: size 108.0x44.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text segoeVariableFont 18/20 400, #6453e4 `color.purple.80`; icon 16 x 16, #6453e4 `color.purple.80` |

![Nav menu trigger default](components/crops/nav-item-default.png) ![Nav menu trigger hover](components/crops/nav-item-hover.png) ![Nav menu trigger focus-visible](components/crops/nav-item-focus-visible.png) ![Nav menu trigger pressed](components/crops/nav-item-pressed.png)

#### Nav submenu
The Features dropdown panel, held open by hovering its trigger (DesktopNavSubMenuContainer). Read as `nav-submenu` on the home page.

**Values (default).** size 248 x 810; padding 8px 24px; background transparent; text segoeVariableFont 18/18 400, #313242 `color.grey.20`; transform translate(0px, 810px).

![Nav submenu default](components/crops/nav-submenu-default.png)

#### Submenu link
A link inside the open Features submenu. Read as `nav-submenu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 232 x 38; padding 10px 16px; radius 12px; background transparent; text segoeVariableFont 18/18 400, #313242 `color.grey.20`; transition all 0.2s ease |
| hover | background #6453e4 `color.purple.80`; text segoeVariableFont 18/18 400, #ffffff; child paint a: size 232.0x38.0; background #6453e4 `color.purple.80`; radius 12px |

![Submenu link default](components/crops/nav-submenu-link-default.png) ![Submenu link hover](components/crops/nav-submenu-link-hover.png)

#### Sign-in button
The outline "Sign in" button (AccentOutlineButton) linking to app.clipchamp.com/login; measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 111 x 42; padding 8px 30px; border 1px solid #433ac7 `color.purple.60`; radius 10px; background transparent; text segoeVariableFont 16/24 500, #433ac7 `color.purple.60`; transition all 0.2s ease |
| hover | size 116.55 x 44.1; border 1px solid #6453e4 `color.purple.80`; text segoeVariableFont 16/24 500, #6453e4 `color.purple.80`; transform scale(1.05); child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: size 116.6x44.1; border 1px solid #6453e4 `color.purple.80` |
| focus-visible | border 1px solid #000000; outline 2px solid #000000, offset 2px; text segoeVariableFont 16/24 500, #000000; child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: border 1px solid #000000; outline 2px solid rgb(0, 0, 0) offset 2px |
| pressed | size 116.55 x 44.1; border 1px solid #6453e4 `color.purple.80`; text segoeVariableFont 16/24 500, #6453e4 `color.purple.80`; transform scale(1.05); child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: size 116.6x44.1; border 1px solid #6453e4 `color.purple.80` |

![Sign-in button default](components/crops/nav-signin-default.png) ![Sign-in button hover](components/crops/nav-signin-hover.png) ![Sign-in button focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in button pressed](components/crops/nav-signin-pressed.png)

#### Nav CTA
The "Try for free" button (GradientButton class; paints solid #6453e4 over a 1px same-colour border) linking to app.clipchamp.com/signup; measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 139 x 42; padding 8px 30px; border 1px solid #6453e4 `color.purple.80`; radius 10px; background #6453e4 `color.purple.80`; text segoeVariableFont 16/24 500, #ffffff; transition all 0.2s ease |
| hover | size 145.95 x 44.1; border 1px solid #4d43de `color.purple.70`; background #4d43de `color.purple.70`; transform scale(1.05); child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: size 145.9x44.1; background #4d43de `color.purple.70`; border 1px solid #4d43de `color.purple.70` |
| focus-visible | border 1px solid #000000; outline 2px solid #000000, offset 2px; child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: border 1px solid #000000; outline 2px solid rgb(0, 0, 0) offset 2px |
| pressed | size 145.95 x 44.1; border 1px solid #4d43de `color.purple.70`; background #4d43de `color.purple.70`; transform scale(1.05); child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: size 145.9x44.1; background #4d43de `color.purple.70`; border 1px solid #4d43de `color.purple.70` |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

### Home

The hero (Online video editor), the solid-purple Create-a-video CTA, the feature link cards, content blocks, the dark band and the testimonial/rating rows.

#### Hero title
"Online video editor" — the hero display headline. Read as `hero-title` on the home page.

**Values (default).** size 359 x 48; background transparent; text segoeVariableFont 40/48 700, #ffffff.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subtitle
The hero subline under the headline. Read as `hero-subtitle` on the home page.

**Values (default).** size 480 x 60; background transparent; text segoeVariableFont 20/30 700, rgba(255, 255, 255, 0.867).

![Hero subtitle default](components/crops/hero-subtitle-default.png)

#### Hero CTA
The "Create a video" WhiteButton under the hero copy — a light pill on the purple hero band; links to signup, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 163 x 42; padding 8px 30px; border 1px solid #ffffff; radius 10px; background #ffffff; shadow rgba(28, 28, 40, 0.204) 0px 16px 24px -8px; text segoeVariableFont 16/24 500, #6e006c `color.pink.50`; transition all 0.2s ease |
| hover | size 171.15 x 44.1; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px; text segoeVariableFont 16/24 500, #b50ac1 `color.pink.80`; transform scale(1.05); child paint a.DL38bq_Accent1Palette._8v3Nwa_DefaultButton: size 171.2x44.1; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px |
| focus-visible | border 1px solid #000000; shadow none; outline 2px solid #ffffff, offset 2px; text segoeVariableFont 16/24 500, #b50ac1 `color.pink.80`; child paint a.DL38bq_Accent1Palette._8v3Nwa_DefaultButton: border 1px solid #000000; outline 2px solid rgb(255, 255, 255) offset 2px |
| pressed | size 171.15 x 44.1; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px; text segoeVariableFont 16/24 500, #b50ac1 `color.pink.80`; transform scale(1.05); child paint a.DL38bq_Accent1Palette._8v3Nwa_DefaultButton: size 171.2x44.1; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Section CTA
A mid-page GradientButton inside a ButtonContainer — the section-level signup CTA, the same solid-purple style as the nav CTA in content context. Read as `cta-secondary` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208 x 42; padding 8px 30px; border 1px solid #6453e4 `color.purple.80`; radius 10px; background #6453e4 `color.purple.80`; text segoeVariableFont 16/24 500, #ffffff; transition all 0.2s ease |
| hover | size 218.4 x 44.1; border 1px solid #4d43de `color.purple.70`; background #4d43de `color.purple.70`; transform scale(1.05); child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: size 218.4x44.1; background #4d43de `color.purple.70`; border 1px solid #4d43de `color.purple.70` |
| focus-visible | border 1px solid #000000; outline 2px solid #000000, offset 2px; child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: border 1px solid #000000; outline 2px solid rgb(0, 0, 0) offset 2px |
| pressed | size 218.4 x 44.1; border 1px solid #4d43de `color.purple.70`; background #4d43de `color.purple.70`; transform scale(1.05); child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: size 218.4x44.1; background #4d43de `color.purple.70`; border 1px solid #4d43de `color.purple.70` |

![Section CTA default](components/crops/cta-secondary-default.png) ![Section CTA hover](components/crops/cta-secondary-hover.png) ![Section CTA focus-visible](components/crops/cta-secondary-focus-visible.png) ![Section CTA pressed](components/crops/cta-secondary-pressed.png)

#### White CTA on dark band
The "Create a video" WhiteButton in the dark AlignedContentWrapper promo block — the light-on-dark signup style (the hero's WhiteButton is hero-cta). Read as `cta-white` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 163 x 42; padding 8px 30px; border 1px solid #ffffff; radius 10px; background #ffffff; shadow rgba(28, 28, 40, 0.204) 0px 16px 24px -8px; text segoeVariableFont 16/24 500, #433ac7 `color.purple.60`; transition all 0.2s ease |
| hover | size 171.15 x 44.1; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px; text segoeVariableFont 16/24 500, #6453e4 `color.purple.80`; transform scale(1.05); child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: size 171.2x44.1; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px |
| focus-visible | border 1px solid #000000; shadow none; outline 2px solid #ffffff, offset 2px; text segoeVariableFont 16/24 500, #6453e4 `color.purple.80`; child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: border 1px solid #000000; outline 2px solid rgb(255, 255, 255) offset 2px |
| pressed | size 171.15 x 44.1; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px; text segoeVariableFont 16/24 500, #6453e4 `color.purple.80`; transform scale(1.05); child paint a.DL38bq_BrandPalette._8v3Nwa_DefaultButton: size 171.2x44.1; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px |

![White CTA on dark band default](components/crops/cta-white-default.png) ![White CTA on dark band hover](components/crops/cta-white-hover.png) ![White CTA on dark band focus-visible](components/crops/cta-white-focus-visible.png) ![White CTA on dark band pressed](components/crops/cta-white-pressed.png)

#### Feature link card
A feature link card (LinkCardStyle): a GradientButton-labelled card into a feature page, never followed. Read as `feature-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 402.61 x 221.38; padding 16px; radius 12px; background #ffffff; shadow rgba(28, 28, 40, 0.1) 0px 4px 8px 0px, rgba(28, 28, 40, 0.1) 0px 0px 2px 0px; text segoeVariableFont 18/21.6 500, #313242 `color.grey.20`; transition all 0.2s ease; icon 16 x 16, #433ac7 `color.purple.60` |
| hover | size 414.69 x 228.02; shadow rgba(28, 28, 40, 0.25) 0px 8px 16px 0px, rgba(28, 28, 40, 0.2) 0px 0px 2px 0px; text segoeVariableFont 18/21.6 500, #6453e4 `color.purple.80`; transform scale(1.03); icon 16.48 x 16.48, #433ac7 `color.purple.60`; child paint div.PG5dYG_LinkCardStyle: size 414.7x228.0; shadow rgba(28, 28, 40, 0.25) 0px 8px 16px 0px, rgba(28, 28, 40, 0.2) 0px 0px 2px 0px |
| focus-visible | child paint a: size 124.0x21.6; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | size 414.69 x 228.02; shadow rgba(28, 28, 40, 0.25) 0px 8px 16px 0px, rgba(28, 28, 40, 0.2) 0px 0px 2px 0px; text segoeVariableFont 18/21.6 500, #6453e4 `color.purple.80`; transform scale(1.03); icon 16.48 x 16.48, #433ac7 `color.purple.60`; child paint div.PG5dYG_LinkCardStyle: size 414.7x228.0; shadow rgba(28, 28, 40, 0.25) 0px 8px 16px 0px, rgba(28, 28, 40, 0.2) 0px 0px 2px 0px |

![Feature link card default](components/crops/feature-card-default.png) ![Feature link card hover](components/crops/feature-card-hover.png) ![Feature link card focus-visible](components/crops/feature-card-focus-visible.png) ![Feature link card pressed](components/crops/feature-card-pressed.png)

#### Content block
A content slice (ContentBlock) — copy column beside media. Read as `content-block` on the home page.

**Values (default).** size 508 x 120; background transparent; text segoeVariableFont 20/30 400, #313242 `color.grey.20`.

![Content block default](components/crops/content-block-default.png)

#### Dark band heading
A heading's `_DarkBackground` text variant inside a dark band, read instead of the band: the element paints transparent, so the band's fill is only the pixel sample `core.sampled.surfaceDark` (README, What is not here). Read as `content-block-dark` on the home page.

**Values (default).** size 640 x 79.19; background transparent; text segoeVariableFont 36/39.6 700, #ffffff.

![Dark band heading default](components/crops/content-block-dark-default.png)

#### Testimonial
A customer quote block (QuoteWrapper) with the author line. Read as `quote` on the home page.

**Values (default).** size 1280 x 178; background transparent; text segoeVariableFont 17.6/17.6 500, #4a4a56.

Child layers that carry the look: div 616x112 background #eaeafa radius 2px 16px 16px; div 616x112 background #eaeafa radius 2px 16px 16px.

![Testimonial default](components/crops/quote-default.png)

#### Rating badge
The store-rating badge row (RatingContainer: stars + score). Read as `rating` on the home page.

**Values (default).** size 352 x 91.19; padding 16px; border 1px solid #e4e4eb; radius 16px; background #ffffff; text segoeVariableFont 14.4/20 500, #64647c `color.grey.40`; transition box-shadow 0.2s ease, transform 0.2s ease.

![Rating badge default](components/crops/rating-default.png)

#### Section title
The first section heading under the hero. Read as `section-title` on the home page.

**Values (default).** size 508 x 79.19; background transparent; text segoeVariableFont 36/39.6 700, #313242 `color.grey.20`.

![Section title default](components/crops/section-title-default.png)

#### Page ground
The body element's painted fill — the page ground. Read as `page-ground` on the home page.

**Values (default).** size 1440 x 5716.92; background #ffffff; text segoeVariableFont 18/20 400, #545472.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The pricing route: the Free/Premium comparison table, plan header cells, feature rows and the FAQ accordion.

#### Pricing title
The pricing page headline over the plan comparison table. Read as `pricing-title` on the pricing page.

**Values (default).** size 608 x 48; background transparent; text segoeVariableFont 40/48 700, #ffffff.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan table
The Free/Premium comparison table (TableWrapper): header plan cells + feature rows. Read as `plan-table` on the pricing page.

**Values (default).** size 1280 x 625; background transparent; text segoeVariableFont 16/20 500, #232330; icon 18 x 18, #64647c `color.grey.40`.

Child layers that carry the look: table 1280x625 border 1px solid #eaeafa shadow rgba(60, 60, 72, 0.1) 0px 4px 24px 0px; th 672.2x48 background #eaeafa; th 311.4x48 background #eaeafa.

![Plan table default](components/crops/plan-table-default.png)

#### Plan header icon
The 52 x 24 icon (`_HeadIcon`) inside a plan header cell, read instead of the cell with the plan name and price (README, What is not here); the header row's fill is in the plan table's child layers. Read as `plan-head` on the pricing page.

**Values (default).** size 52 x 24; padding 0px 20px 0px 8px; background transparent; text segoeVariableFont 16/20 500, #232330.

![Plan header icon default](components/crops/plan-head-default.png)

#### Feature row head
A feature name cell down the left of the comparison table (RowHeadCell). Read as `feature-row-head` on the pricing page.

**Values (default).** size 672.23 x 48; padding 8px 12px; border 1px solid #eaeafa; background transparent; wrapper table.YLPCUG_Table: shadow rgba(60, 60, 72, 0.1) 0px 4px 24px 0px; text segoeVariableFont 16/20 500, #232330.

![Feature row head default](components/crops/feature-row-head-default.png)

#### Feature cell
A plan value cell in the table (Cell/CellStyle): check, value or dash. Read as `feature-cell` on the pricing page.

**Values (default).** size 311.41 x 48; padding 8px 12px; border 1px solid #f2f2f8; background transparent; wrapper table.YLPCUG_Table: shadow rgba(60, 60, 72, 0.1) 0px 4px 24px 0px; text segoeVariableFont 16/20 400, #64647c `color.grey.40`; transition background 0.1s ease.

![Feature cell default](components/crops/feature-cell-default.png)

#### Tooltip cell
A plan value cell (`_CellTooltip`) read with its tooltip closed: the Fluent tooltip node inside it measured 0 x 0, so this capture has no open tooltip (README, What is not here). Read as `feature-tooltip` on the pricing page.

**Values (default).** size 311.41 x 48; padding 8px 12px; border 1px solid #f2f2f8; background transparent; wrapper table.YLPCUG_Table: shadow rgba(60, 60, 72, 0.1) 0px 4px 24px 0px; text segoeVariableFont 16/20 500, #64647c `color.grey.40`; transition background 0.1s ease; icon 18 x 18, #64647c `color.grey.40`.

![Tooltip cell default](components/crops/feature-tooltip-default.png)

#### FAQ item
A pricing FAQ accordion item (details/ItemHeaderContainer); opened with its own summary toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 696 x 56; background transparent; text segoeVariableFont 20/24 400, #5d6276 `color.collapsible.header`; icon 24 x 24, #6453e4 `color.purple.80` |
| opened | size 696 x 208; text segoeVariableFont 20/24 400, #6453e4 `color.purple.80` |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item opened](components/crops/faq-item-opened.png)

#### Inline link
An inline entry link in the page copy (InlineEntryLink). Read as `inline-link` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 207 x 30; background transparent; text segoeVariableFont 20/30 400, #4d43de `color.purple.70` |
| hover | text segoeVariableFont 20/30 400, #433ac7 `color.purple.60` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.hQWgwW_InlineEntryLink: size 207.0x30.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text segoeVariableFont 20/30 400, #433ac7 `color.purple.60` |

![Inline link default](components/crops/inline-link-default.png) ![Inline link hover](components/crops/inline-link-hover.png) ![Inline link focus-visible](components/crops/inline-link-focus-visible.png) ![Inline link pressed](components/crops/inline-link-pressed.png)

#### Pricing dark hero
The dark hero band over the plan table (DarkHeroTitle + WhiteButton). Read as `pricing-hero` on the pricing page.

**Values (default).** size 640 x 352; padding 0px 32px 0px 0px; background transparent; text segoeVariableFont 40/48 700, #ffffff.

Child layers that carry the look: a 211x40 background #ffffff radius 10px shadow rgba(28, 28, 40, 0.204) 0px 16px 24px -8px.

![Pricing dark hero default](components/crops/pricing-hero-default.png)

#### Pricing hero CTA
The "Create videos for free" WhiteButton in the dark pricing hero; links to signup, never followed. Read as `pricing-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 211 x 40; padding 8px 30px; radius 10px; background #ffffff; shadow rgba(28, 28, 40, 0.204) 0px 16px 24px -8px; text segoeVariableFont 16/24 500, #232330; transition all 0.2s ease |
| focus-visible | shadow none; outline 2px solid #ffffff, offset 2px; child paint a.brand._8v3Nwa_DefaultButton: outline 2px solid rgb(255, 255, 255) offset 2px |
| pressed | size 221.55 x 42; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px; transform scale(1.05); child paint a.brand._8v3Nwa_DefaultButton: size 221.5x42.0; shadow rgba(28, 28, 40, 0.4) 0px 16px 24px -8px |

![Pricing hero CTA default](components/crops/pricing-cta-default.png) ![Pricing hero CTA hover](components/crops/pricing-cta-hover.png) ![Pricing hero CTA focus-visible](components/crops/pricing-cta-focus-visible.png) ![Pricing hero CTA pressed](components/crops/pricing-cta-pressed.png)

### Features

The features index: its headline and the feature entry cards.

#### Features title
The features index headline. Read as `features-title` on the features page.

**Values (default).** size 608 x 48; background transparent; text segoeVariableFont 40/48 700, #ffffff.

![Features title default](components/crops/features-title-default.png)

#### Feature section
An aligned content block on the features index: title, body list of entry links, side media (AlignedContentContainer). Read as `feature-section` on the features page.

**Values (default).** size 1200 x 539.06; background transparent; text segoeVariableFont 36/39.6 700, #313242 `color.grey.20`.

![Feature section default](components/crops/feature-section-default.png)

#### Feature entry link
An inline feature link inside a content list (InlineEntryLink); measured never followed. Read as `feature-link` on the features page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 139 x 30; background transparent; text segoeVariableFont 20/30 400, #4d43de `color.purple.70` |
| hover | text segoeVariableFont 20/30 400, #433ac7 `color.purple.60` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a.hQWgwW_InlineEntryLink: size 139.0x30.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text segoeVariableFont 20/30 400, #433ac7 `color.purple.60` |

![Feature entry link default](components/crops/feature-link-default.png) ![Feature entry link hover](components/crops/feature-link-hover.png) ![Feature entry link focus-visible](components/crops/feature-link-focus-visible.png) ![Feature entry link pressed](components/crops/feature-link-pressed.png)

#### Feature section heading
A feature section title inside an aligned content block (ContentTitle/StyledHeading with anchor). Read as `feature-heading` on the features page.

**Values (default).** size 508 x 79.19; background transparent; text segoeVariableFont 36/39.6 700, #313242 `color.grey.20`.

![Feature section heading default](components/crops/feature-heading-default.png)

### App sign-in (boundary)

app.clipchamp.com's public login surface — measured at rest; nothing was typed, signed into or submitted.

#### Sign-in card
The app.clipchamp.com login surface: the sign-in card the SPA paints. Measured at rest, never submitted. Read as `signin-card` on the sign-in page.

**Values (default).** size 792 x 900; background #ffffff; text Segoe UI 32/38.4 600, #232330; icon 24 x 24, #232330.

![Sign-in card default](components/crops/signin-card-default.png)

#### Account field
The account/email field on the sign-in card; focused locally, never submitted. Read as `signin-field` on the sign-in page.

Not on the page when it was captured.

#### Continue button
A sign-in/continue control on the card; measured never pressed. Read as `signin-button` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 648 x 60; padding 16px; border 2px solid #dfdfe8; radius 4px; background rgba(19, 19, 27, 0.05); text Segoe UI 18/20 600, #232330; transition all 0.1s ease-in-out; icon 24 x 24, #232330 |
| hover | border 2px solid #d0d0dd; background rgba(19, 19, 27, 0.1); child paint button.fui-Button.r1f29ykk: background rgba(19, 19, 27, 0.1); border 2px solid #d0d0dd |
| focus-visible | size 648 x 58; border 1px solid #000000; shadow #000000 0px 0px 0px 1px inset; outline 2px solid transparent, offset 0px; child paint button.fui-Button.r1f29ykk: size 648.0x58.0; border 1px solid #000000; shadow rgb(0, 0, 0) 0px 0px 0px 1px inset; outline 2px solid rgba(0, 0, 0, 0) offset 0px |
| pressed | border 2px solid transparent; background rgba(19, 19, 27, 0.2); child paint button.fui-Button.r1f29ykk: background rgba(19, 19, 27, 0.2); border 2px solid transparent |

![Continue button default](components/crops/signin-button-default.png) ![Continue button hover](components/crops/signin-button-hover.png) ![Continue button focus-visible](components/crops/signin-button-focus-visible.png) ![Continue button pressed](components/crops/signin-button-pressed.png)

### Footer

The footer band, its link columns, language selector and social icons.

#### Footer
The footer band: link columns, language selector, social icons and the legal subfooter. Read as `footer` on the home page.

**Values (default).** size 1440 x 1062.41; background transparent; text segoeVariableFont 14/22.4 700, #2e248f.

![Footer default](components/crops/footer-default.png)

#### Footer link
A link in a footer link column. The footer renders duplicate tabindex="-1" clones for the collapsed/mobile variant; only tabindex=0 copies are measured. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 21; background transparent; text segoeVariableFont 16/32 400, #313242 `color.grey.20`; transition font-variation-settings 0.2s ease, color 0.2s ease |
| hover | text segoeVariableFont 16/32 400, #6453e4 `color.purple.80` |
| focus-visible | outline 1px auto #101010, offset 1px; child paint a: size 120.0x21.0; outline 1px auto rgb(16, 16, 16) offset 1px |
| pressed | text segoeVariableFont 16/32 400, #6453e4 `color.purple.80` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A footer social icon link. Read as `footer-social` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 24 x 21; radius 4px; background transparent; text segoeVariableFont 16/20 400, #313242 `color.grey.20`; icon 24 x 24, #313242 `color.grey.20` |
| hover | icon 26.4 x 26.4, #ff0000 |
| focus-visible | outline 2px solid #6453e4 `color.purple.80`, offset 2px; child paint a: size 24.0x21.0; radius 4px; outline 2px solid rgb(100, 83, 228) offset 2px |

![Social link default](components/crops/footer-social-default.png) ![Social link hover](components/crops/footer-social-hover.png) ![Social link focus-visible](components/crops/footer-social-focus-visible.png) ![Social link pressed](components/crops/footer-social-pressed.png)

#### Language selector
The footer language selector (LanguageSelectorWrapper). Read as `footer-lang` on the home page.

**Values (default).** size 240 x 42; background transparent; text segoeVariableFont 16/normal 400, #2e248f; transition color 0.2s ease, transform 0.2s ease; icon 20 x 20, #2e248f.

Child layers that carry the look: select 240x42 background #ffffff border 1px solid #2e248f radius 10px.

![Language selector default](components/crops/footer-lang-default.png)

### Mobile (390 wide)

The same surface at phone width: the collapsed bar and the side-bar drawer.

#### Mobile bar
The 390 mobile nav bar: logo + menu toggle. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 72; background #ffffff; shadow rgba(28, 28, 40, 0.15) 0px 0px 16px 4px, rgba(28, 28, 40, 0.15) 0px 0px 2px 0px; text segoeVariableFont 16/24 500, rgba(28, 28, 28, 0.7).

![Mobile bar default](components/crops/m-header-default.png)

#### Menu button
The hamburger (side-bar-nav-button); its own press opens the drawer. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 60 x 60; padding 1px 6px; background transparent; wrapper header.Wg1Dzq_Header.sticky: shadow rgba(28, 28, 40, 0.15) 0px 0px 16px 4px, rgba(28, 28, 40, 0.15) 0px 0px 2px 0px; text segoeVariableFont 13.33/60 400, #313242 `color.grey.20`; transition box-shadow 0.2s ease; icon 32 x 32, #313242 `color.grey.20`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The side-bar drawer after the hamburger press. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; background transparent; wrapper header.Wg1Dzq_Header.sticky: shadow rgba(28, 28, 40, 0.15) 0px 0px 16px 4px, rgba(28, 28, 40, 0.15) 0px 0px 2px 0px; text segoeVariableFont 16/24 500, rgba(28, 28, 28, 0.7); icon 32 x 32, #313242 `color.grey.20`.

Child layers that carry the look: div 390x844 background rgba(33, 30, 79, 0.9); div 390x844 background #ffffff; a 310x42 border 1px solid #433ac7 `color.purple.60` radius 10px.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Menu link
A link row inside the open drawer. Read as `m-menu-link` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 50 x 48; padding 12px 0px; background transparent; text segoeVariableFont 16/24 500, rgba(28, 28, 28, 0.7) |
| focus-visible | outline 5px auto #e59700, offset 2px; child paint a: size 50.0x48.0; outline 5px auto rgb(229, 151, 0) offset 2px |

![Menu link default](components/crops/m-menu-link-default.png) ![Menu link hover](components/crops/m-menu-link-hover.png) ![Menu link focus-visible](components/crops/m-menu-link-focus-visible.png) ![Menu link pressed](components/crops/m-menu-link-pressed.png)

#### Mobile headline
The hero headline at 390. Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 251 x 35; background transparent; text segoeVariableFont 28/35 700, #ffffff.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Clipchamp's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **The product itself.** Clipchamp's video editor — projects, the timeline, exports and settings — lives behind app.clipchamp.com sign-in; the public login surface was measured but never submitted, and the paid upgrade checkout was never entered.
- **The editor itself is a different stack.** The marketing site is a React/Fluent-UI build; the in-app editor UI is not reachable signed out and is not claimed here.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One theme: the whole public surface paints light. Dark bands exist inside the theme (ContentBlockDark sections), but no second theme is offered.

### Fonts

- **The UI fonts** are webfonts the site declares (Segoe UI and friends via the Fluent-style `--font-*` variables; `fonts` in [raw/css-vars.json](raw/css-vars.json) holds the @font-face records); the font files themselves are not committed.
- Illustrations, video posters, badge artwork and the wordmark in the screenshots are Clipchamp's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The illustrations, video posters and the wordmark are Clipchamp's content; only the frames and components were measured.
