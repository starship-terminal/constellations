# Hitchd components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from www.hitchd.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the mobile entries at 390 x 844), with computed styles read from the running page. Nothing was signed into, paid, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (20 components, 42 states). The page layouts are described in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter Variable 16/24 400, #111212`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (14 files, named `{component}-{state}.png`). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (Hitchd has one theme — no dark variant or theme switch exists anywhere on the surveyed pages). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x, stitched from tiles when a page is taller than one GPU texture; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. The closure announcement strip, the hairline-serif hero ("Tie the knot, without tangles."), marketing sections, footer. Full page captured. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Log in. The auth card at rest: email field, password field, disabled Continue, forgot-password and sign-up links. | `/login` | [default](screenshots/login-light-default.png) |
| Sign up. The same auth shell at rest; nothing typed or submitted. | `/signup` | [default](screenshots/signup-light-default.png) |
| Forgot password. The reset form at rest. | `/forgot-password` | [default](screenshots/forgot-password-light-default.png) |
| Blog index. Article rows; the page is ~50,000px tall, so only the viewport is captured — see Gaps. | `/blog` | [default](screenshots/blog-light-default.png) |
| Blog post. A full article ("What is a honeymoon registry?"). | `/blog/what-is-a-honeymoon-registry` | [default](screenshots/post-light-default.png), [full](screenshots/post-light-full.png) |
| Terms of service. Prose page. | `/terms` | [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| Privacy policy. Prose page. | `/privacy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Destination landing (/trips/australia). | `/trips/australia` | [default](screenshots/trips-light-default.png), [full](screenshots/trips-light-full.png) |
| Guide page ("Add Hitchd to a Knot wedding website"). | `/guides/add-hitchd-to-knot-wedding-webiste` | [default](screenshots/guide-light-default.png), [full](screenshots/guide-light-full.png) |
| The public demo registry (/zoeandnoah): hero with the couple's names, Sort by filter, gift grid, footer; the filter's opened and filtered states and a gift modal. | `/zoeandnoah` | [default](screenshots/registry-light-default.png), [filter-still-needed](screenshots/registry-light-filter-still-needed.png), [full](screenshots/registry-light-full.png), [gift-modal](screenshots/registry-light-gift-modal.png), [sort-open](screenshots/registry-light-sort-open.png) |
| A not-yet-live registry (/avaandbenjamin) — its public countdown page. | `/avaandbenjamin` | [default](screenshots/coming-soon-light-default.png) |
| Home at 390: announcement strip, hero, full page. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Log in at 390. | `/login` | [default](screenshots/mobile-login-light-default.png) |
| Blog index at 390. | `/blog` | [default](screenshots/mobile-blog-light-default.png) |
| Blog post at 390. | `/blog/what-is-a-honeymoon-registry` | [default](screenshots/mobile-post-light-default.png), [full](screenshots/mobile-post-light-full.png) |
| Demo registry at 390. | `/zoeandnoah` | [default](screenshots/mobile-registry-light-default.png), [full](screenshots/mobile-registry-light-full.png) |
| Countdown registry at 390. | `/avaandbenjamin` | [default](screenshots/mobile-coming-soon-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Sort by filter, opened | demo registry | the filter select's own click | [registry-light-sort-open](screenshots/registry-light-sort-open.png), [sort-filter](#sort-filter) |
| Filtered list ("Still needed") | demo registry | an option chosen in the filter select; the list re-filters, nothing is submitted | [registry-light-filter-still-needed](screenshots/registry-light-filter-still-needed.png) |
| Gift modal | demo registry | a gift card's own tap navigates to /<registry>/<gift-slug> and the app draws the modal; read at rest, Give never pressed | [registry-light-gift-modal](screenshots/registry-light-gift-modal.png), [gift-modal](#gift-modal) |
| Mobile menu | demo registry at 390 | the .mobile-menu drawer exists on the page (with registry-owner links) but no guest-facing control opens it — it stays hidden, so it was measured at rest rather than captured open | [mobile-menu](#mobile-menu) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus and pressed.** Components were read at rest — Hitchd's auth forms were never focused (that would mean typing toward a sign-in), so focus-ring and pressed evidence is a documented gap rather than a measurement.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease-in` | all | mobile-menu |
| 0.15s | `ease-in-out` | all | auth-button, auth-field, auth-link, gift-modal |

**Layout.** Read on each page at each width ([raw/layout.json](raw/layout.json)): the page's full height, its widest Foundation `.row` content band, and the fixed/sticky layers it carries.

| Page | 1440 x 900 | 390 x 844 |
|---|---|---|
| home | page 900px tall, widest band 1440px, 0 fixed/sticky | page 844px tall, widest band 390px, 0 fixed/sticky |
| login | page 900px tall, no band found, 2 fixed/sticky | page 893px tall, no band found, 2 fixed/sticky |
| signup | page 900px tall, widest band 1440px, 2 fixed/sticky | page 844px tall, widest band 390px, 2 fixed/sticky |
| forgot-password | page 900px tall, no band found, 2 fixed/sticky | page 844px tall, no band found, 2 fixed/sticky |
| blog | page 46060px tall, widest band 1280px, 0 fixed/sticky | page 127663px tall, widest band 390px, 0 fixed/sticky |
| post | page 8827px tall, widest band 1280px, 1 fixed/sticky | page 16310px tall, widest band 390px, 1 fixed/sticky |
| terms | page 16589px tall, widest band 1392px, 0 fixed/sticky | page 27434px tall, widest band 366px, 0 fixed/sticky |
| privacy | page 6757px tall, widest band 1392px, 0 fixed/sticky | page 11425px tall, widest band 366px, 0 fixed/sticky |
| trips | page 6538px tall, widest band 1440px, 0 fixed/sticky | page 10903px tall, widest band 342px, 0 fixed/sticky |
| guide | page 8049px tall, widest band 1280px, 1 fixed/sticky | page 8547px tall, widest band 390px, 2 fixed/sticky |
| registry | page 7690px tall, widest band 1440px, 3 fixed/sticky | page 15050px tall, widest band 390px, 5 fixed/sticky |

**Card shapes.** Default-state values for each component's own container part; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Gift card](#gift-card) | 1416 x 472 | - | - | transparent | none | 0 |
| [Gift card (mobile)](#gift-card-mobile) | 370 x 294.5 | - | - | transparent | none | 0 |
| [Blog index card](#blog-index-card) | 386.66 x 600 | - | - | transparent | none | 0 |
| [Auth form card](#auth-form-card) | 450 x 437 | - | - | transparent | none | 0 |
| [Gift modal](#gift-modal) | 1440 x 779.77 | - | - | #ffffff `heroInk` | none | 0 |

## Components

### Chrome

The page furniture: the marketing header over the home hero, the full-width closure announcement strip, the footer, and the registry's own top bar with its #hashtag link and Try It Free call to action.

#### Marketing nav
the home header bar and its logo + Log In link. Read as `marketing-nav` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| header | size 1440 x 96; padding 24px 56px; background transparent; text Inter Variable 16/24 400, #ffffff `heroInk` |
| logo | size 74 x 27.02; padding none; text Inter Variable 16/24 400, #2c2e2f |
| loginLink | size 70 x 48; padding 12px 0px 12px 24px |

![Marketing nav header](components/crops/nav.png)

#### Closure announcement banner
the full-width "Hitchd is closing on 31 December 2026" strip above the header. Read as `announcement-banner` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| banner | size 1440 x 98; padding 20px 24px; background #f6f3ef `cream`; text Inter Variable 20/30 500, #111212 `ink` |
| text | size 705 x 58; padding none; background transparent |

![Closure announcement banner banner](components/crops/announcement.png)

#### Footer
the marketing footer and its links (the closure home has no footer; read on the destination page) Read as `marketing-footer` on the https://www.hitchd.com/trips/australia page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| footer | size 1440 x 370; padding 64px 24px 40px 24px; background #ffffff `heroInk`; text Inter Variable 15/26 600, #000000 |
| link | size 0 x 0; padding none; background transparent; text Inter Variable 17/22 400, #111212 `ink` |

![Footer footer](components/crops/footer.png)

#### Registry nav
the registry top bar, #hashtag link and Try It Free CTA. Read as `registry-nav` on the demo registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| bar | size 1440 x 80; background rgba(255, 255, 255, 0.92); shadow rgba(0, 0, 0, 0.08) 0px -1px 0px 0px; text Inter Variable 17/80 500, #111212 `ink` |
| cta | size 117 x 40; padding 0px 20px; radius 100px; background #111212 `ink`; shadow none; text Inter Variable 16/40 500, #ffffff `heroInk` |
| hashtag | size 137 x 28.39; border B: 2px solid transparent; background transparent; shadow none; text Inter Variable 22/26.4 500, #ffffff `heroInk` |

![Registry nav bar](components/crops/registry-nav.png)

### Type

Hitchd's voice is a hairline serif for marketing display (DDNR, weight 100) over Inter Variable for everything else; the registry couples' names set in the app's own display face (`classic` on the demo). Each surface sets its own scale — the registry's hero runs to 96px.

#### Hero heading
the home hero — "Tie the knot, without tangles." set in DDNR. Read as `hero` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| h1 | size 576 x 184.78; background transparent; text DDNR 88/92.4 100, #ffffff `heroInk` |
| lead | size 576 x 114.17; padding 26px 0px 0px 0px; text Inter Variable 21/29.4 400, #ffffff `heroInk` |

![Hero heading h1](components/crops/hero.png)

#### Marketing H2
a section heading on the marketing surface (the closure home carries no h2, so this was read on the destination page) Read as `marketing-h2` on the https://www.hitchd.com/trips/australia page.

**Values (h2).** size 672 x 120; background transparent; text Inter Variable 56/60 600, #000000.

![Marketing H2 h2](components/crops/h2.png)

#### Article type
the blog post H1, body copy and inline link. Read as `article-type` on the blog post page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| h1 | size 680 x 168; padding 48px 0px 0px 24px; background transparent; text Inter Variable 56/60.00 700, #111212 `ink` |
| body | size 1208 x 54; padding none; text Inter Variable 19/27.00 400, #111212 `ink` |
| link | size 45 x 17; padding none; text Inter Variable 14/17.99 500, #6e6e73 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Legal prose
a terms page heading and paragraph. Read as `prose-h2` on the terms page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| h2 | size 118 x 36; background transparent; text Inter Variable 32/36 600, #000000 |
| body | size 700 x 24; text Inter Variable 16/24 400, #333333 |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Registry hero
the demo registry heading and couple names. Read as `registry-hero` on the demo registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| heading | size 1392 x 192; background transparent; text classic 96/96 400, #ffffff `heroInk` |
| names | size 685 x 173.95; text Inter Variable 22/26.4 400, #ffffff `heroInk` |

![Registry hero heading](components/crops/registry-hero.png)

### Cards

The gift tiles of the registry grid, a blog index row, and the auth form's container.

#### Blog index card
a post row on /blog. Read as `blog-card` on the blog index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| card | size 386.66 x 600; background transparent; text Inter Variable 15/20 400, #737373 |
| title | size 328.66 x 96; text Inter Variable 26/32 600, #2c2e2f |

Child layers that carry the look: div 386.7x299 background #ffffff `heroInk`; span 3x3 background #737373 radius 50%; a::after 102pxx1px background #000000.

![Blog index card card](components/crops/blog-card.png)

#### Gift card
a gift tile in the registry list. Read as `gift-card` on the demo registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| card | size 1416 x 472; background transparent; text Inter Variable 12/24 500, #ffffff `heroInk` |
| title | size 616 x 40; padding 0px 16px 0px 0px; text Inter Variable 36/40 600, #111212 `ink` |
| info | size 708 x 472; padding 0px 12px 0px 80px; text Inter Variable 36/40 600, #111212 `ink` |

Child layers that carry the look: div 708x472 radius 20px shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 1px inset; div 123x28 image linear-gradient(#080c0c 0%, #0c1212 100%) border 1px solid #080c0c radius 50px shadow rgba(0, 0, 0, 0.1) 0px 1px 2px 0px; div 75x34 background #ffffff `heroInk` radius 50px shadow rgba(17, 18, 18, 0.12) 0px 0px 0px 1px.

![Gift card card](components/crops/gift-card.png)

#### Gift card (mobile)
a gift tile at 390 x 844. Read as `mobile-gift-card` on the demo registry page.

**Values (card).** size 370 x 294.5; background transparent; text Inter Variable 12/24 500, #ffffff `heroInk`.

Child layers that carry the look: div 342x256.5 radius 16px shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 1px inset; div 123x28 image linear-gradient(#080c0c 0%, #0c1212 100%) border 1px solid #080c0c radius 50px shadow rgba(0, 0, 0, 0.1) 0px 1px 2px 0px.

![Gift card (mobile) card](components/crops/mobile-gift-card.png)

### Forms

The couple app's auth surfaces — /login, /signup and /forgot-password — read at rest. Nothing was focused, typed or submitted.

#### Auth form card
the /login form container and heading, at rest. Read as `auth-layout` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| h1 | size 450 x 32; background transparent; text Inter Variable 28/32 600, #111212 `ink` |
| card | size 450 x 437; text Inter Variable 16/20 600, #111212 `ink` |
| page | size 1440 x 900; background #ffffff `heroInk` |

![Auth form card h1](components/crops/auth-card.png)

#### Auth text field
the email input and its label, at rest. Read as `auth-field` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| input | size 450 x 48; padding 0px 16px; border 1px solid #d2d2d7 `fieldLine`; radius 8px; background transparent; text Inter Variable 17/24 400, #111212 `ink`; transition all 0.15s ease-in-out; placeholder #111212 `ink` |
| label | size 40 x 20; padding none; border none; radius none; text Inter Variable 16/20 600, #111212 `ink`; transition none; placeholder none |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Auth submit button
the Continue button in its disabled-at-rest state. Read as `auth-button` on the login page.

**Values (button).** size 450 x 48; radius 50px; background #cdcfd0 `disabled`; text Inter Variable 16/48 500, #ffffff `heroInk`; transition all 0.15s ease-in-out.

![Auth submit button button](components/crops/auth-button.png)

#### Auth links
the forgot-password link and helper copy. Read as `auth-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| link | size 125 x 21; border B: 1px solid rgba(0, 0, 0, 0.12); background transparent; text Inter Variable 14/20 500, #111212 `ink`; transition all 0.15s ease-in-out |
| muted | size 450 x 21; border none; text Inter Variable 14/20 400, #575a5d `muted`; transition none |

Child layers that carry the look: a 125x21 border 1px solid rgba(0, 0, 0, 0.12).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Controls

The registry's Sort by filter select and the phone's .mobile-menu drawer — present on the demo registry but never opened for a guest.

#### Sort filter
the "Sort by" select in the registry header. Read as `sort-filter` on the demo registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| control | size 158 x 48; background transparent; text Inter Variable 13/20 500, #96999c |
| select | size 111 x 24; padding 0px 24px 0px 0px; image url(…); text Inter Variable 15/17.25 500, #393c3c |

Child layers that carry the look: option 0x0 shadow #111212 `ink` 0px 0px 0px 1.5px inset.

![Sort filter control](components/crops/sort-filter.png)

#### Mobile menu
the registry .mobile-menu drawer at 390px — it exists (with owner links) but no guest-facing control opens it, so it was measured hidden at rest. Read as `mobile-menu` on the demo registry page.

**Values (menu).** size 390 x 844; padding 12px 24px 24px 24px; background #ffffff `heroInk`; text Inter Variable 16/normal 400, #545759; transition all 0.15s ease-in; opacity 0; icon 24 x 24, #111212 `ink`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Dialogs

The gift modal: a gift card's own tap navigates to /<registry>/<gift-slug> and the guest app draws the modal over the list. Read at rest; the Give/contribute flow was never entered.

#### Gift modal
a gift card's modal, opened by its own tap and read at rest; the Give flow is never entered. Read as `gift-modal` on the demo registry page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| modal | size 1440 x 779.77; background #ffffff `heroInk`; text Inter Variable 36/40.5 600, #111212 `ink`; icon 32 x 32, #ffffff `heroInk` |
| title | size 453.33 x 40.5; background transparent; icon none |
| give | size 453.33 x 50; background transparent; text Inter Variable 17/50 500, #ffffff `heroInk`; icon none |
| giveWrap | size 453.33 x 50; radius 100px; background #c5c8ca; text Inter Variable 17/50 500, #ffffff `heroInk`; transition all 0.15s ease-in-out; icon none |

![Gift modal modal](components/crops/gift-modal.png)

### Boundaries

Routes that a signed-out guest cannot reach: the registry's internal pages each bounce back to /.

#### Registry internal routes
contributions / payment-methods / ask / quick-thanks each bounce the signed-out guest back to /. Read as `internal-route-bounces` on the demo registry page.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

## Icons

3 distinct inline SVGs were lifted from the pages into [icons/](icons), and 58 linked SVG references were indexed, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Hitchd's icons carry no name in the DOM, so glyphs are filed by geometry hash under `unnamed/`; the wordmark itself is a linked SVG (`/marketing/images/hitchd-home-brand-logo.svg`), recorded in the index but not vendored. The SVGs are Hitchd's property, kept for reference only.

| Icon | Rendered size | Seen on | Context |
|---|---|---|---|
| [unnamed/8e722494a2.svg](icons/unnamed/8e722494a2.svg) | 64 x 28 | registry |  |
| [unnamed/c7f6d7b5f4.svg](icons/unnamed/c7f6d7b5f4.svg) | 32 x 32 | gift-modal |  |
| [unnamed/ebf7009e68.svg](icons/unnamed/ebf7009e68.svg) | 22 x 23 | gift-modal |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-home-brand-logo.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-honeymoon-registry-logo-dark.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-mobile-menu-button-black.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-honeymoon-registry-logo-light.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/icon-fb.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/icon-insta.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/icon-pinterest.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/icon-mail.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-honeymoon-registry-logo-dark.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/mobile-menu-black-edge.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-mobile-menu-close.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-honeymoon-registry-logo-dark.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/mobile-menu-black-edge.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-honeymoon-registry-logo-light.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-footer-brand-logo.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/www-social-insta.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/www-social-fb.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/www-social-pinterest.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/footer-external-arrow.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-honeymoon-registry-logo-light.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/link-block.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-features-company-logos-small.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-honeymoon-registry-logo-dark.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-honeymoon-registry-logo-dark.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/mobile-menu-black-edge.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-mobile-menu-close.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/hitchd-logo-light.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/hitchd-dark-round.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/small-x-destroy.svg | — |  |
| linked svg — https://www.hitchd.com/marketing/images/tp-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/edit-palette.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/hitchd-gift-logo.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/signup-fb-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/edit-palette.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/hitchd-gift-logo.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/edit-palette.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/hitchd-gift-logo.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/reg-gift-purchased-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/hitchdcom-logo-full.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/authed-fb-logo.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/authed-insta-logo.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/authed-pinterest-logo.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/authed-fb-contact-dark.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/mob-menu-close.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-home-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-website-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-registry-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-guests-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-account-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/hitchd-logo-light.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/hitchd-gift-logo.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/img-close-icon-back-new.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/mob-menu-close.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-home-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-website-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-registry-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-guests-icon.svg | — |  |
| linked svg — https://www.hitchd.com/assets/public/images/nav-account-icon.svg | — |  |

## Gaps

### Pages

- **Signed-in pages.** Nothing behind sign-in was captured: the couple dashboard, the registry editor, guest lists, contribution management, payout/payment settings and account settings. The kit never signs in.
- **Anything that pays or submits.** No contribution or gift purchase was started: the gift modal's Give button and everything behind it (amounts, card details, checkout) is unmeasured by policy. No auth form was typed into or submitted, no password-reset or sign-up sent.
- **Registry internal routes.** `/zoeandnoah/contributions`, `/payment-methods`, `/ask` and `/quick-thanks` each bounce the signed-out guest back to `/` (measured in `internal-route-bounces`); those views belong to the couple's live registry, not the demo.
- **Redirected marketing routes.** `/how-it-works`, `/about`, `/pricing`, `/press-kit`, `/zola-alternative`, `/honeyfund-alternative`, `/travelersjoy-alternative`, `/referrals` and `/honeymoon-registry` all redirect to `/` — Hitchd announced it is closing on 31 December 2026 and is not accepting new customers, so those pages no longer exist to capture.
- **Blog index, full page.** `/blog` is ~50,000px of article rows; the tiled full-page screenshot exceeded the capture timeout and was abandoned. The viewport shot stands; the truncation is the documented boundary, not a missing capture.

### States

- **Focus, hover and pressed** were not forced on the auth controls (focusing a field is the first step of signing in) and are a documented gap; the registry's filter and modal states that a guest can reach at rest are captured.
- **The gift modal's later steps** (amount entry, payment method, confirmation) were never entered.
- **The registry's signed-in owner view** and the couple-facing menu items (Log out, Quick Thanks) are not guest surfaces.

### Themes

Hitchd shows one light theme. No stylesheet, page or app surveyed declares a dark variant, no page sets a theme attribute, and no theme switch exists on the marketing pages, the auth app or the registry app. The token file therefore ships a single light set and no dark evidence exists to label.

### Fonts

- **DDNR** (the display serif) and **Inter Variable** are the marketing stack's self-hosted woff2 faces, declared in `/marketing/css/styles.min.css`; the style guide links to them rather than vendoring them.
- The registry app loads its own display faces so each couple can theme their registry — the demo registry's heading is set in **classic**, one of ~20 registry font names (@font-face families named classic, clean, dramatic, editorial, elegant, romantic…) in the guest app's styles, alongside Google-served faces (EB Garamond, Roboto Flex, Noto Sans Display…).
- The auth app and registry app otherwise set the same **Inter Variable** body stack as marketing.

### Screenshots

- Gift photography and registry images are Hitchd's or the couples' content and appear only inside screenshots and crops; remote asset URLs (the registry's CDN image URLs) were never written to a committed file — `url(…)` appears in their place in the raw readings.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The public demo registry shows real gift data for a sample couple; only the interface was measured, not the catalogue's full contents.
- No personal data was captured beyond the public names and registry content the demo itself publishes.
