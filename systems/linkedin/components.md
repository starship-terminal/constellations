# LinkedIn components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from linkedin.com on 2026-11-18, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or purchased. Sign in, Join now, Apply, Follow and Message were measured, never followed. Consent overlays were hidden, never clicked.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (32 components, 80 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (80 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at CSS scale (one CSS pixel per image pixel — mobile fulls are 390 wide); mobile viewport shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Guest home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Jobs search | `/jobs/search/` | [default](screenshots/jobs-light-default.png), [full](screenshots/jobs-light-full.png) |
| Company | `/company/linkedin` | [default](screenshots/company-light-default.png), [full](screenshots/company-light-full.png) |
| Public profile | `/in/reidhoffman` | [default](screenshots/profile-light-default.png), [full](screenshots/profile-light-full.png) |
| User Agreement | `/legal/user-agreement` | [default](screenshots/legal-light-default.png), [full](screenshots/legal-light-full.png) |
| Sign-in wall | `/login` | [default](screenshots/signin-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Jobs, phone | `/jobs/search/` | [default](screenshots/mobile-jobs-light-default.png), [full](screenshots/mobile-jobs-light-full.png) |
| Company, phone | `/company/linkedin` | [default](screenshots/mobile-company-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Date posted filter | jobs search | the chip was opened as a local dropdown, then Escape | no screenshot; [opened crop](components/crops/filter-chip-opened.png) |
| Consent overlay | every page | hidden when present, never clicked | boundary; see Gaps |
| Sign in / Join now / Apply / Follow / Message | nav, jobs, company, profile | measured, never followed or submitted | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 16 components were given a real keyboard focus. 16 draw an outline ring: `nav-link` (1px auto #005fcc, offset 1px), `nav-signin` (1px auto #005fcc, offset 1px), `nav-join` (1px auto #005fcc, offset 1px), `hero-email` (1px auto #005fcc, offset 1px), `topic-chip` (1px auto #005fcc, offset 1px), `job-chip` (1px auto #005fcc, offset 1px), `footer-link` (1px auto #005fcc, offset 1px), `filter-chip` (1px auto #005fcc, offset 0px), `job-row` (on a child: 1px auto rgb(0, 95, 204) offset 4px), `apply-cta` (1px auto #005fcc, offset 0px), `company-follow` (1px auto #005fcc, offset 1px), `company-jobs` (1px auto #005fcc, offset 1px), `profile-join` (1px auto #005fcc, offset 1px), `profile-message` (1px auto #005fcc, offset 0px), `legal-link` (1px auto #005fcc, offset 1px), `signin-submit` (1px auto #005fcc, offset 0px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.084s | `ease` | border-color, box-shadow | signin-email |
| 0.336s | `cubic-bezier(0.34, 0, 0.21, 1)` | opacity | avatar |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|

## Components

### Shell and navigation

The guest header shared by the public pages: wordmark, Top Content, People, Learning, Jobs, Games, a Sign in outline pill and a Join now filled pill, plus the legal footer.

#### Guest nav
The guest header: logo, Top Content, People, Learning, Jobs, Games, Sign in, Join now. Read as `header-nav` on the home page.

**Values (default).** size 1128 x 80; padding 12px 0px 16px 0px; background transparent; text -apple-system 12/15 400, rgba(0, 0, 0, 0.6) `light.color.text-secondary`; layers ul::after.top-nav-menu.flex 1pxx37px rgba(0, 0, 0, 0.3); a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 rgb(10, 102, 194) 0px 0px 0px 1px 24px; a.nav__button-tertiary.btn-primary 115.2x48.0 rgb(10, 102, 194) rgba(0, 0, 0, 0) 0px 0px 0px 1px 24px; ancestors div.sticky.top-0 bg #ffffff `light.color.text-on-brand`.

Child layers that carry the look: ul::after 1pxx37px background rgba(0, 0, 0, 0.3); a 99.2x48 radius 24px shadow #0a66c2 `light.color.brand` 0px 0px 0px 1px; a 115.2x48 background #0a66c2 `light.color.brand` radius 24px shadow transparent 0px 0px 0px 1px.

![Guest nav default](components/crops/header-nav-default.png)

#### Logo
The LinkedIn wordmark in the guest nav. Measured, never followed. Read as `nav-logo` on the home page.

**Values (default).** size 102 x 52; background transparent; text -apple-system 16/24 600, #0a66c2 `light.color.brand`.

![Logo default](components/crops/nav-logo-default.png)

#### Nav link
"Jobs" in the guest nav. A destination link, measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64 x 52; background transparent; text -apple-system 12/15 400, rgba(0, 0, 0, 0.6) `light.color.text-secondary`; icon 20 x 18, rgba(0, 0, 0, 0.6) `light.color.text-secondary` |
| hover | text -apple-system 12/15 400, rgba(0, 0, 0, 0.9) `light.color.text`; icon 20 x 18, rgba(0, 0, 0, 0.9) `light.color.text` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text -apple-system 12/15 400, #0a66c2 `light.color.brand`; icon 20 x 18, #0a66c2 `light.color.brand`; layers a.top-nav-link.flex 64.0x52.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text -apple-system 12/15 400, rgba(0, 0, 0, 0.9) `light.color.text`; icon 20 x 18, rgba(0, 0, 0, 0.9) `light.color.text` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign in
"Sign in" secondary-emphasis pill. A sign-in destination, measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 99.17 x 48; padding 12px 24px; radius 24px; background transparent; shadow #0a66c2 0px 0px 0px 1px; text -apple-system 16/24 600, #0a66c2 `light.color.brand`; layers a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 rgb(10, 102, 194) 0px 0px 0px 1px 24px |
| hover | background rgba(112, 181, 249, 0.1) `light.color.button-secondary-emphasis-hover`; text -apple-system 16/24 600, #004182 `light.color.brand-hover`; layers none |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 rgb(10, 102, 194) 0px 0px 0px 1px 1px auto rgb(0, 95, 204) offset 1px 24px |
| pressed | background rgba(112, 181, 249, 0.2); shadow #004182 0px 0px 0px 1px; text -apple-system 16/24 600, #004182 `light.color.brand-hover`; layers none |

![Sign in default](components/crops/nav-signin-default.png) ![Sign in hover](components/crops/nav-signin-hover.png) ![Sign in focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in pressed](components/crops/nav-signin-pressed.png)

#### Join now
"Join now" primary pill. A sign-in destination, measured, never followed. Read as `nav-join` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 115.23 x 48; padding 12px 24px; radius 24px; background #0a66c2 `light.color.brand`; text -apple-system 16/24 600, #ffffff `light.color.text-on-brand` |
| hover | background #004182 `light.color.brand-hover` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #004182 `light.color.brand-hover`; text -apple-system 16/24 600, rgba(255, 255, 255, 0.6) |

![Join now default](components/crops/nav-join-default.png) ![Join now hover](components/crops/nav-join-hover.png) ![Join now focus-visible](components/crops/nav-join-focus-visible.png) ![Join now pressed](components/crops/nav-join-pressed.png)

#### Footer
The guest footer: legal links and the LinkedIn Corporation line. Read as `footer` on the home page.

**Values (default).** size 1440 x 50; background transparent; text -apple-system 12/18 400, #666666; icon 56 x 14, #000000; layers ul.collapsible-dropdown__list.hidden 0.0x0.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.3) 0px 4px 12px 0px 8px; button.font-sans.text-xs 0.0x0.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0); button.font-sans.text-xs 0.0x0.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid r.

Child layers that carry the look: ul 0x0 background #ffffff `light.color.text-on-brand` radius 8px shadow rgba(0, 0, 0, 0.3) 0px 4px 12px 0px; button 0x0 border 1px solid transparent; button 0x0 border 1px solid transparent.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer legal link. Measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 35.66 x 18; background transparent; text -apple-system 12/18 600, #666666 |
| hover | text -apple-system 12/18 600, #004182 `light.color.brand-hover` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text -apple-system 12/18 600, #0a66c2 `light.color.brand`; layers a.li-footer__item-link.flex 35.7x18.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text -apple-system 12/18 600, #004182 `light.color.brand-hover` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

### Guest home

The signed-out home: a 48px heading, Continue with Google, Sign in with email, topic chips and job-category chips.

#### Hero heading
"Welcome to your professional community" at text-display-lg (48px). Read as `hero-h1` on the home page.

**Values (default).** size 572.39 x 120; background transparent; text -apple-system 48/60 400, rgba(0, 0, 0, 0.9) `light.color.text`.

![Hero heading default](components/crops/hero-h1-default.png)

#### Sign in with email
"Sign in with email" outline pill under the hero. A sign-in destination, measured, never followed. Read as `hero-email` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 40; padding 8px 24px; radius 24px; background transparent; shadow rgba(0, 0, 0, 0.75) 0px 0px 0px 1px; text -apple-system 16/24 600, rgba(0, 0, 0, 0.75) `light.color.input-border`; layers a.sign-in-form__sign-in-cta.my-2 400.0x40.0 rgba(0, 0, 0, 0.75) 0px 0px 0px 1px 24px |
| hover | background rgba(0, 0, 0, 0.04); text -apple-system 16/24 600, rgba(0, 0, 0, 0.9) `light.color.text`; layers none |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.sign-in-form__sign-in-cta.my-2 400.0x40.0 rgba(0, 0, 0, 0.75) 0px 0px 0px 1px 1px auto rgb(0, 95, 204) offset 1px 24px |
| pressed | background rgba(0, 0, 0, 0.08) `light.color.border-faint`; shadow rgba(0, 0, 0, 0.9) 0px 0px 0px 1px; text -apple-system 16/24 600, rgba(0, 0, 0, 0.9) `light.color.text`; layers none |

![Sign in with email default](components/crops/hero-email-default.png) ![Sign in with email hover](components/crops/hero-email-hover.png) ![Sign in with email focus-visible](components/crops/hero-email-focus-visible.png) ![Sign in with email pressed](components/crops/hero-email-pressed.png)

#### Topic chip
A topic pill ("Career") in Explore top LinkedIn content. Measured, never followed. Read as `topic-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 99.14 x 48; padding 12px 24px; radius 24px; background transparent; shadow rgba(0, 0, 0, 0.75) 0px 0px 0px 1px; text -apple-system 16/24 600, rgba(0, 0, 0, 0.75) `light.color.input-border`; layers a.btn-md.babybear:btn-sm 99.1x48.0 rgba(0, 0, 0, 0.75) 0px 0px 0px 1px 24px |
| hover | background rgba(0, 0, 0, 0.04); text -apple-system 16/24 600, rgba(0, 0, 0, 0.9) `light.color.text`; layers none |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.btn-md.babybear:btn-sm 99.1x48.0 rgba(0, 0, 0, 0.75) 0px 0px 0px 1px 1px auto rgb(0, 95, 204) offset 1px 24px |
| pressed | background rgba(0, 0, 0, 0.08) `light.color.border-faint`; shadow rgba(0, 0, 0, 0.9) 0px 0px 0px 1px; text -apple-system 16/24 600, rgba(0, 0, 0, 0.9) `light.color.text`; layers none |

![Topic chip default](components/crops/topic-chip-default.png) ![Topic chip hover](components/crops/topic-chip-hover.png) ![Topic chip focus-visible](components/crops/topic-chip-focus-visible.png) ![Topic chip pressed](components/crops/topic-chip-pressed.png)

#### Job category chip
A suggested job-search chip. Measured, never followed. Read as `job-chip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138.41 x 48; padding 12px 24px; radius 24px; background transparent; shadow rgba(0, 0, 0, 0.75) 0px 0px 0px 1px; text -apple-system 16/24 600, rgba(0, 0, 0, 0.75) `light.color.input-border`; layers a.btn-md.babybear:btn-sm 138.4x48.0 rgba(0, 0, 0, 0.75) 0px 0px 0px 1px 24px |
| hover | background rgba(0, 0, 0, 0.04); text -apple-system 16/24 600, rgba(0, 0, 0, 0.9) `light.color.text`; layers none |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.btn-md.babybear:btn-sm 138.4x48.0 rgba(0, 0, 0, 0.75) 0px 0px 0px 1px 1px auto rgb(0, 95, 204) offset 1px 24px |

![Job category chip default](components/crops/job-chip-default.png) ![Job category chip hover](components/crops/job-chip-hover.png) ![Job category chip focus-visible](components/crops/job-chip-focus-visible.png)

#### Section heading
"Explore top LinkedIn content", the first section heading on the guest home. Read as `section-heading` on the home page.

**Values (default).** size 429 x 40; background transparent; text -apple-system 32/40 400, rgba(0, 0, 0, 0.9) `light.color.text`.

![Section heading default](components/crops/section-heading-default.png)

### Jobs search

The public jobs search: keyword field, filter chips, job cards and an Apply control that was measured and never followed.

#### Results heading
The jobs-search results heading, as the page painted it for this capture IP. Read as `jobs-h1` on the jobs page.

**Values (default).** size 472 x 24; background transparent; text -apple-system 16/24 400, rgba(0, 0, 0, 0.6) `light.color.text-secondary`.

![Results heading default](components/crops/jobs-h1-default.png)

#### Filter chip
"Date posted" filter chip. Opened as a local dropdown, never submitted. Read as `filter-chip` on the jobs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140.02 x 32; padding 3.5px 16px; border 1px solid rgba(0, 0, 0, 0.3); radius 16px; background transparent; text -apple-system 14/normal 600, rgba(0, 0, 0, 0.75) `light.color.input-border`; icon 24 x 24, rgba(0, 0, 0, 0.75) `light.color.input-border` |
| hover | border 1px solid rgba(0, 0, 0, 0.45); background rgba(0, 0, 0, 0.04); text -apple-system 14/normal 600, rgba(0, 0, 0, 0.9) `light.color.text`; icon 24 x 24, rgba(0, 0, 0, 0.9) `light.color.text` |
| focus-visible | padding 4px 16px; outline 1px auto #005fcc, offset 0px |
| pressed | border 1px solid rgba(0, 0, 0, 0.45); background rgba(0, 0, 0, 0.08) `light.color.border-faint`; text -apple-system 14/normal 600, rgba(0, 0, 0, 0.9) `light.color.text`; icon 24 x 24, rgba(0, 0, 0, 0.9) `light.color.text` |
| opened | border 1px solid rgba(0, 0, 0, 0.45); background rgba(0, 0, 0, 0.04); text -apple-system 14/normal 600, rgba(0, 0, 0, 0.9) `light.color.text`; icon 24 x 24, rgba(0, 0, 0, 0.9) `light.color.text` |

![Filter chip default](components/crops/filter-chip-default.png) ![Filter chip hover](components/crops/filter-chip-hover.png) ![Filter chip focus-visible](components/crops/filter-chip-focus-visible.png) ![Filter chip pressed](components/crops/filter-chip-pressed.png) ![Filter chip opened](components/crops/filter-chip-opened.png)

#### Job card
A job result card on the public search. Measured, never followed. Apply was not clicked. Read as `job-row` on the jobs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 504 x 132.98; background transparent; text -apple-system 18/23.99 600, rgba(0, 0, 0, 0.9) `light.color.text`; layers div.base-card.relative 504.0x133.0 rgb(230, 247, 255) B:1px solid rgb(230, 233, 236); img.artdeco-entity-image.artdeco-entity-image--square-4 56.0x56.0 T:4px solid rgba(0, 0, 0, 0) / R:4px solid rgba(0, 0, 0, 0) / B:4px solid rgba(0, 0, 0, 0) / L:4px solid rgba(0, 0, 0, 0) 6px |
| focus-visible | layers div.base-card.relative 504.0x133.0 rgb(230, 247, 255) B:1px solid rgb(230, 233, 236); a.base-card__full-link.absolute 504.0x132.0 1px auto rgb(0, 95, 204) offset 4px; img.artdeco-entity-image.artdeco-entity-image--square-4 56.0x56.0 T:4px solid rgba(0, 0, 0, 0) / R:4px solid rgba(0, 0, 0, 0) / B:4px solid rgba(0, 0, 0, 0) / L:4px solid rgba(0, 0, 0, 0) 6px |

Child layers that carry the look: div 504x133 background #e6f7ff border 1px solid #e6e9ec; img 56x56 border 4px solid transparent radius 6px.

![Job card default](components/crops/job-row-default.png) ![Job card hover](components/crops/job-row-hover.png) ![Job card focus-visible](components/crops/job-row-focus-visible.png)

#### Apply
"Apply" on the job detail pane. A sign-in destination, measured, never followed. Read as `apply-cta` on the jobs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.86 x 48; padding 12px 24px; border 1px solid transparent; radius 24px; background #0a66c2 `light.color.brand`; text -apple-system 16/normal 600, #ffffff `light.color.text-on-brand`; icon 16 x 16, #ffffff `light.color.text-on-brand` |
| hover | background #004182 `light.color.brand-hover` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #004182 `light.color.brand-hover`; text -apple-system 16/normal 600, rgba(255, 255, 255, 0.6); icon 16 x 16, rgba(255, 255, 255, 0.6) |

![Apply default](components/crops/apply-cta-default.png) ![Apply hover](components/crops/apply-cta-hover.png) ![Apply focus-visible](components/crops/apply-cta-focus-visible.png) ![Apply pressed](components/crops/apply-cta-pressed.png)

### Company page

The public LinkedIn company page: name, Follow, See jobs and the About tab.

#### Company name
The public company page title. Read as `company-h1` on the company page.

**Values (default).** size 422 x 36; background transparent; text -apple-system 24/36 600, rgba(0, 0, 0, 0.9) `light.color.text`.

![Company name default](components/crops/company-h1-default.png)

#### Follow
"Follow" on the company top card. A sign-in destination, measured, never followed. Read as `company-follow` on the company page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96.88 x 48; padding 12px 24px; radius 24px; background transparent; shadow rgba(0, 0, 0, 0.75) 0px 0px 0px 1px; text -apple-system 16/24 600, rgba(0, 0, 0, 0.75) `light.color.input-border`; layers a.top-card-layout__cta.mt-2 96.9x48.0 rgba(0, 0, 0, 0.75) 0px 0px 0px 1px 24px |
| hover | background rgba(0, 0, 0, 0.04); text -apple-system 16/24 600, rgba(0, 0, 0, 0.9) `light.color.text`; layers none |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.top-card-layout__cta.mt-2 96.9x48.0 rgba(0, 0, 0, 0.75) 0px 0px 0px 1px 1px auto rgb(0, 95, 204) offset 1px 24px |
| pressed | background rgba(0, 0, 0, 0.08) `light.color.border-faint`; shadow rgba(0, 0, 0, 0.9) 0px 0px 0px 1px; text -apple-system 16/24 600, rgba(0, 0, 0, 0.9) `light.color.text`; layers none |

![Follow default](components/crops/company-follow-default.png) ![Follow hover](components/crops/company-follow-hover.png) ![Follow focus-visible](components/crops/company-follow-focus-visible.png) ![Follow pressed](components/crops/company-follow-pressed.png)

#### See jobs
"See jobs" primary pill. Measured, never followed. Read as `company-jobs` on the company page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112.45 x 48; padding 12px 24px; radius 24px; background #0a66c2 `light.color.brand`; text -apple-system 16/24 600, #ffffff `light.color.text-on-brand` |
| hover | background #004182 `light.color.brand-hover` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #004182 `light.color.brand-hover`; text -apple-system 16/24 600, rgba(255, 255, 255, 0.6) |

![See jobs default](components/crops/company-jobs-default.png) ![See jobs hover](components/crops/company-jobs-hover.png) ![See jobs focus-visible](components/crops/company-jobs-focus-visible.png) ![See jobs pressed](components/crops/company-jobs-pressed.png)

### Public profile

A published profile that loads signed out. Message and Join to view profile are sign-in destinations.

#### Profile name
The public profile name. A published profile, captured signed out. Read as `profile-h1` on the profile page.

**Values (default).** size 149.16 x 36; background transparent; text -apple-system 24/36 600, rgba(0, 0, 0, 0.9) `light.color.text`.

![Profile name default](components/crops/profile-h1-default.png)

#### Headline
The public profile headline under the name. Read as `profile-headline` on the profile page.

**Values (default).** size 422 x 72; background transparent; text -apple-system 16/24 400, rgba(0, 0, 0, 0.9) `light.color.text`.

![Headline default](components/crops/profile-headline-default.png)

#### Join to view profile
"Join to view profile". A sign-in destination, measured, never followed. Read as `profile-join` on the profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 190.61 x 48; padding 12px 24px; radius 24px; background #0a66c2 `light.color.brand`; text -apple-system 16/24 600, #ffffff `light.color.text-on-brand` |
| hover | background #004182 `light.color.brand-hover` |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background #004182 `light.color.brand-hover`; text -apple-system 16/24 600, rgba(255, 255, 255, 0.6) |

![Join to view profile default](components/crops/profile-join-default.png) ![Join to view profile hover](components/crops/profile-join-hover.png) ![Join to view profile focus-visible](components/crops/profile-join-focus-visible.png) ![Join to view profile pressed](components/crops/profile-join-pressed.png)

#### Message
"Message". A sign-in destination into messaging, measured, never followed. Read as `profile-message` on the profile page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 145.88 x 48; padding 12px 24px; border 1px solid transparent; radius 24px; background transparent; shadow #0a66c2 0px 0px 0px 1px; text -apple-system 16/normal 600, #0a66c2 `light.color.brand`; icon 16 x 16, #0a66c2 `light.color.brand` |
| hover | background rgba(112, 181, 249, 0.1) `light.color.button-secondary-emphasis-hover`; text -apple-system 16/normal 600, #004182 `light.color.brand-hover`; icon 16 x 16, #004182 `light.color.brand-hover` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background rgba(112, 181, 249, 0.2); shadow #004182 0px 0px 0px 1px; text -apple-system 16/normal 600, #004182 `light.color.brand-hover`; icon 16 x 16, #004182 `light.color.brand-hover` |

![Message default](components/crops/profile-message-default.png) ![Message hover](components/crops/profile-message-hover.png) ![Message focus-visible](components/crops/profile-message-focus-visible.png) ![Message pressed](components/crops/profile-message-pressed.png)

#### Avatar
The public profile photo as the page paints it. Read as `avatar` on the profile page.

**Values (default).** size 128 x 128; border 4px solid #ffffff `light.color.text-on-brand`; radius 50%; background transparent; shadow rgba(0, 0, 0, 0.3) 0px 4px 12px 0px; text -apple-system 13.33/normal 400, #000000; transition opacity 0.336s cubic-bezier(0.34, 0, 0.21, 1).

![Avatar default](components/crops/avatar-default.png)

### Legal

The public User Agreement.

#### Legal heading
The User Agreement banner heading (t-64). Read as `legal-h1` on the legal page.

**Values (default).** size 648 x 72; background transparent; text -apple-system 64/72 400, rgba(0, 0, 0, 0.9) `light.color.text`.

![Legal heading default](components/crops/legal-h1-default.png)

#### Legal nav link
A legal-section link. Measured, never followed. Read as `legal-link` on the legal page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102.88 x 24; background transparent; text -apple-system 16/24 500, rgba(0, 0, 0, 0.6) `light.color.text-secondary` |
| hover | text -apple-system 16/24 500, #000000; ancestors li bg transparent |
| focus-visible | outline 1px auto #005fcc, offset 1px; text -apple-system 16/24 500, #0a66c2 `light.color.brand`; layers a.t-sans.t-black--light 102.9x24.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text -apple-system 16/24 500, #000000 |

![Legal nav link default](components/crops/legal-link-default.png) ![Legal nav link hover](components/crops/legal-link-hover.png) ![Legal nav link focus-visible](components/crops/legal-link-focus-visible.png) ![Legal nav link pressed](components/crops/legal-link-pressed.png)

### Sign-in wall

The /login page at rest. Nothing was typed or submitted.

#### Sign-in heading
The sign-in wall heading, captured at rest. Nothing was typed or submitted. Read as `signin-heading` on the signin page.

**Values (default).** size 400 x 33.75; background transparent; text system-ui 30/33.75 600, rgba(0, 0, 0, 0.9) `light.color.text`.

![Sign-in heading default](components/crops/signin-heading-default.png)

#### Email field
The sign-in email field at rest and focused. No text was typed. The form was not submitted. Read as `signin-email` on the signin page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 48; padding 1px 12px; border 1px solid rgba(0, 0, 0, 0.75) `light.color.input-border`; radius 4px; background rgba(255, 255, 255, 0); text system-ui 16/20 400, rgba(0, 0, 0, 0.9) `light.color.text`; transition box-shadow 0.084s ease, border-color 0.084s ease; placeholder rgba(0, 0, 0, 0.9) `light.color.text` |
| focused | border 1px solid rgba(0, 0, 0, 0.9) `light.color.text`; shadow rgba(0, 0, 0, 0.9) 0px 0px 0px 1px inset; outline 3px auto #005fcc, offset -1px |

![Email field default](components/crops/signin-email-default.png) ![Email field focused](components/crops/signin-email-focused.png)

#### Sign in submit
The sign-in submit control. Hover and focus only. It was not pressed, so no sign-in was attempted. Read as `signin-submit` on the signin page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 48; background transparent; text system-ui 16/20 600, #ffffff `light.color.text-on-brand`; layers span.aaalzr.aaalyb 400.0x48.0 rgb(10, 102, 194) 24px |
| hover | layers span.aaalzr.aaalyb 400.0x48.0 rgb(0, 65, 130) 24px |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.aaalxl.aaalxk 400.0x48.0 1px auto rgb(0, 95, 204) offset 0px; span.aaalzr.aaalyb 400.0x48.0 rgb(10, 102, 194) 24px |

Child layers that carry the look: span 400x48 background #0a66c2 `light.color.brand` radius 24px.

![Sign in submit default](components/crops/signin-submit-default.png) ![Sign in submit hover](components/crops/signin-submit-hover.png) ![Sign in submit focus-visible](components/crops/signin-submit-focus-visible.png)

### Mobile (390 wide)

The guest home at 390px: the wrapped nav, Join now, and the heading.

#### Mobile nav
The guest nav at 390px. Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 76; padding 12px 16px; background transparent; text -apple-system 16/24 600, #0a66c2 `light.color.brand`; icon 26 x 26, #0a66c2 `light.color.brand`; layers a.nav__button-secondary.btn-secondary-emphasis 99.2x48.0 rgb(10, 102, 194) 0px 0px 0px 1px 24px; a.nav__button-tertiary.btn-primary 115.2x48.0 rgb(10, 102, 194) rgba(0, 0, 0, 0) 0px 0px 0px 1px 24px; ancestors div.sticky.top-0 bg #ffffff `light.color.text-on-brand`.

Child layers that carry the look: a 99.2x48 radius 24px shadow #0a66c2 `light.color.brand` 0px 0px 0px 1px; a 115.2x48 background #0a66c2 `light.color.brand` radius 24px shadow transparent 0px 0px 0px 1px.

![Mobile nav default](components/crops/m-nav-default.png)

#### Mobile Join now
The Join now pill at 390px. A sign-in destination, measured, never followed. Read as `m-join` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 83.83 x 48; background transparent; text system-ui 14/17.5 600, #0a66c2 `light.color.brand`; layers span.aaalzr.aaalyb 83.8x32.0 rgba(255, 255, 255, 0) rgb(10, 102, 194) 0px 0px 0px 1px inset 24px |

Child layers that carry the look: span 83.8x32 background rgba(255, 255, 255, 0) radius 24px shadow #0a66c2 `light.color.brand` 0px 0px 0px 1px inset.

![Mobile Join now default](components/crops/m-join-default.png) ![Mobile Join now pressed](components/crops/m-join-pressed.png)

#### Mobile hero heading
The guest-home heading at 390px. Read as `m-h1` on the home page at 390 wide.

**Values (default).** size 358 x 67.5; background transparent; text system-ui 30/33.75 400, rgba(0, 0, 0, 0.9) `light.color.text`.

![Mobile hero heading default](components/crops/m-h1-default.png)

## Icons

No standalone SVG icon set was lifted on this pass. The wordmark, nav glyphs and job-card marks are visible in the crops and screenshots. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Members and external destinations

The feed, messaging, and job apply sit behind sign-in. This package covers the public signed-out surfaces only. Sign in, Join now, Apply, Follow and Message were measured as destinations, never followed and never submitted.

### Pages

- **Sign-in wall.** /login was captured at rest. The form was not submitted.
- **about.linkedin.com, business.linkedin.com and news.linkedin.com** returned 403 to this headless client. They are not in the package.
- **People directory.** /pub/dir/+/+ redirected to an auth wall (HTTP 999). Not captured.
- **Premium.** /premium redirected to the sign-in wall. Not followed.
- **Job listings are geo-served.** The search was for designer jobs in the United States; the cards shown are whatever that query returned on this date.

### States

- **Pressed** was forced with DevTools on controls, so a state a script adds on mousedown is missing. No sign-in, apply or follow control was clicked.
- **The jobs keyword field** was focused and filled with sample text, then cleared. Enter was never pressed, so the search was not submitted.
- **Easy Apply, messaging, the feed and onboarding** sit behind sign-in and were not captured.

### Themes

One painted theme: a white page, a #f3f2f0 canvas, rgba(0,0,0,0.9) text and #0a66c2 brand pills. tokens.json emits light only. No guest dark theme was observed.

### Fonts

- The guest sheet names a system-ui stack (`-apple-system`, `system-ui`, `Segoe UI`, `Roboto`). Font files are not shipped in this package.

### Screenshots

- The public profile of Reid Hoffman is published content, captured signed out. Job cards are whatever the public search returned on the capture date.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Job descriptions, company copy and profile text are the product's published content; only frames and components were measured.
