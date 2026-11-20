# Fresha components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fresha.com's signed-out surfaces on 2026-11-16, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, booked, bought, sent or submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (79 components, 183 states).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Roobert 16/16 400, #262627`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (180 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`; the partner sign-in also has `partner-signin-dark-default.png` (the one painted dark state). Desktop shots are 1440 x 900; `-full` shots are whole pages; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). Each PNG has a `.capture.json` sidecar with the real viewport, DPR and document size.

| Surface | URL | Screenshots |
|---|---|---|
| Consumer home. The 72px header, the display hero with the search row, recommended-venue cards, then marketing sections and the footer. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [search-focus](screenshots/home-light-search-focus.png) |
| The user-flow chooser: customer or business, with the back button and the language button. | `/user-flow` | [default](screenshots/user-flow-light-default.png) |
| The consumer sign-in: the email field (shown filled, then cleared), Continue, the SSO row, passkey and cross-links. | `/auth` | [default](screenshots/auth-light-default.png), [filled](screenshots/auth-light-filled.png) |
| The partners.fresha.com professional sign-in, in light and in the dark theme it paints under prefers-color-scheme: dark. | `/users/sign-in on partners.fresha.com` | [default](screenshots/partner-signin-light-default.png), [dark](screenshots/partner-signin-dark-default.png) |
| A venue profile: gallery, title, tabs, services with Book buttons, reviews, hours and the Book now bar. | `/a/ha-lu-hair-design-singapore-11-mohamed-sultan-road-f7vhwpo1` | [default](screenshots/venue-light-default.png), [full](screenshots/venue-light-full.png), [services](screenshots/venue-light-services.png) |
| The booking wizard at the service-selection boundary: a service ticked (ticked), then unticked; never continued. | `/a/…/booking` | [default](screenshots/booking-light-default.png), [ticked](screenshots/booking-light-ticked.png) |
| Pricing: the plan cards, feature list and the FAQ (one disclosure opened). | `/pricing` | [default](screenshots/pricing-light-default.png), [faq-open](screenshots/pricing-light-faq-open.png), [full](screenshots/pricing-light-full.png) |
| For business: nav, display hero, business-type grid and stats; the Business types flyout open. | `/for-business` | [default](screenshots/for-business-light-default.png), [flyout](screenshots/for-business-light-flyout.png), [full](screenshots/for-business-light-full.png) |
| Legacy LP category page: hero, city chips, global venue rows. | `/lp/en/bt/hair-salons` | [default](screenshots/lp-category-light-default.png), [full](screenshots/lp-category-light-full.png) |
| Legacy LP browse: category chip rail, venue cards, map button, pagination. | `/lp/en/bt/hair-salons/in/singapore` | [default](screenshots/lp-browse-light-default.png), [full](screenshots/lp-browse-light-full.png) |
| Help centre: the search pill and the topic/article lists. | `/help-center` | [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png) |
| Careers. | `/careers` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| The blog index. | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Download the app. | `/download-app` | [default](screenshots/download-app-light-default.png), [full](screenshots/download-app-light-full.png) |
| The cookies policy page. | `/cookies` | [default](screenshots/cookies-light-default.png) |
| Consumer home at 390: the compact header and hero. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| The consumer sign-in at 390. | `/auth` | [default](screenshots/mobile-auth-light-default.png) |
| LP browse at 390. | `/lp/en/bt/hair-salons/in/singapore` | [default](screenshots/mobile-lp-browse-light-default.png), [full](screenshots/mobile-lp-browse-light-full.png) |
| The venue page at 390. | `/a/…` | [default](screenshots/mobile-venue-light-default.png), [full](screenshots/mobile-venue-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Menu drawer | consumer home | the header's Menu button; dismissed after capture | [home-light-menu](screenshots/home-light-menu.png), [menu-drawer](#menu-drawer) |
| Search suggestions | consumer home | focus in the What are you looking for? field; nothing searched | [home-light-search-focus](screenshots/home-light-search-focus.png), [search-suggestions](#search-suggestions) |
| Business types flyout | /for-business | the nav's Business types button; dismissed with Escape | [for-business-light-flyout](screenshots/for-business-light-flyout.png), [nav-flyout](#nav-flyout) |
| FAQ open | /pricing | one FAQ disclosure's own button | [pricing-light-faq-open](screenshots/pricing-light-faq-open.png), [faq-item](#faq-item) |
| Service ticked | booking wizard | a service row's own Add checkbox, then unticked; Continue never pressed | [booking-light-ticked](screenshots/booking-light-ticked.png), [booking-cart](#cart-summary) |
| Email filled | consumer and partner sign-in | typed into the field, then cleared before capture continued; nothing submitted | [auth-light-filled](screenshots/auth-light-filled.png), [auth-email-field](#email-field) |
| Dark theme | partner sign-in | data-theme="auto" honours prefers-color-scheme: dark; captured under an emulated dark preference | [partner-signin-dark-default](screenshots/partner-signin-dark-default.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 25 components were given a real keyboard focus. 20 draw a visible ring.
- ::before shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px (opacity 0 to 1): `shell-login-link`, `shell-business-link`, `shell-menu-button`, `shell-getapp-button`, `search-button`, `carousel-button`, `back-button`, `auth-back`, `auth-continue`, `sso-button`, `book-now`, `gallery-button`, `service-book-button`.
- ::before shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px (opacity 0 to 1): `language-button`, `m-menu-button`.
- ::before shadow #ffffff 0px 0px 0px 2px, radius 999px (opacity 0 to 1): `partner-continue`, `partner-sso`.
- ::before shadow #ffffff 0px 0px 0px 2px inset; border 2px solid #0d0d0d `colors.background.primary`, radius 8px (opacity 0 to 1): `venue-tab`.
- outline 1px auto #101010, offset 0px: `info-icon`.
- outline 2px solid #0d0d0d `colors.background.primary`, offset 2px: `lp-map-button`.
The rest draw none — most declare only a 2px transparent outline that stays invisible: `booking-add-button`, `plan-cta`, `nav-flyout-button`, `b2b-cta`, `watch-button`.
Focus could not be captured on 2: keyboard focus never reached them (or they took focus without matching :focus-visible), so their focus look is unknown, not absent: `chooser-card`, `booking-continue`.

**Pressed.** Measured by forcing :active through DevTools. Fresha's solid buttons (the auth/partner Continue, the B2B CTAs, the map button) shrink slightly on press (the B2B CTA goes from 180x48 to about 173x46); the text buttons barely change.

**Motion.** Transitions measured on the components, by duration. The motion probe read every moving element on eight public pages both ways ([raw/motion.json](raw/motion.json)): prefers-reduced-motion only partially honoured — the consumer home, venue and LP pages reduce some motion; the pricing, for-business, help, auth and partner pages leave every transition running.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.85, 0, 0.15, 1)` | opacity | carousel-button |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | faq-item |
| 0.2s | `cubic-bezier(0, 0.55, 0.45, 1)` | background-color, border-color, color, fill, stroke, text-decoration-color, transform | b2b-cta, nav-flyout-button, plan-cta, watch-button |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | all | article-link, topic-card |
| 0.2s | `cubic-bezier(0.85, 0, 0.15, 1)` | block-size, max-inline-size | auth-back, auth-continue, back-button, book-now, booking-continue, gallery-button, m-header, partner-continue and more |
| 0.25s | `cubic-bezier(0.42, 0, 0.58, 1)` | border-color | lp-category-chip |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, box-shadow | b2b-header, business-type-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Venue card](#venue-card) | 322 x 284.66 | - | - | transparent | none | 0 |
| [Browse venue card](#browse-venue-card) | 381.33 x 543.5 | - | - | transparent | none | 0 |
| [Mobile venue card](#mobile-venue-card) | 236 x 227.33 | - | - | transparent | none | 0 |
| [Plan card](#plan-card) | 277 x 368.5 | - | - | transparent | none | 0 |
| [Business-type card](#business-type-card) | 378.66 x 378.67 | - | 18px | transparent | none | 0 |
| [Customer/professional card](#customerprofessional-card) | 368 x 42 | - | - | transparent | none | 0 |
| [Review card](#review-card) | 418 x 170 | - | - | transparent | none | 0 |
| [Help topic card](#help-topic-card) | 362.66 x 210 | 1px solid #e5e5e5 `colors.background.neutral` | 8px | #ffffff `colors.background.base` | none | 32px |
| [Article link](#article-link) | 362.67 x 234 | 1px solid #e5e5e5 `colors.background.neutral` | 8px | #ffffff `colors.background.base` | none | 32px |
| [Cart summary](#cart-summary) | 444 x 756 | - | - | transparent | none | 0px 32px |
| [Search suggestions](#search-suggestions) | 536 x 2049 | - | - | transparent | none | 0 |
| [Nav flyout](#nav-flyout) | 588 x 391 | - | 16px | #f5f5f5 `colors.app.dark.foreground.neutral` | none | 0 |
| [Menu drawer](#menu-drawer) | 198 x 177 | - | - | transparent | none | 0 |
| [Opening times](#opening-times) | 418 x 250 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The consumer marketplace shell every www.fresha.com page shares: a 72px header with the Fresha wordmark, Log in, For business, a menu button and the Get the app pill, and the footer. The menu opens a drawer (its own entry, below).

#### Top bar
The consumer app bar: logo left, Log in / For businesses / Menu / Get the app right, over the hero. Read as `shell-header` on the consumer home page.

**Values (default).** size 1440 x 72; padding 12px 32px; background transparent; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; icon 74.97 x 22, #0d0d0d `colors.background.primary`.

Child layers that carry the look: a::before 74.9688pxx48px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; a::before 86.4062pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 86.4x48 background rgba(19, 19, 19, 0) `colors.background.transparent` border 1px rgba(255, 255, 255, 0) `colors.background.onLoud` radius 999px.

![Top bar default](components/crops/shell-header-default.png)

#### Log in link
Header link to the /user-flow chooser. Measured, never followed. Read as `shell-login-link` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 86.41 x 48; radius 999px; background transparent; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 86.40pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: a::before 86.4062pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 86.4x48 background rgba(19, 19, 19, 0) `colors.background.transparent` border 1px rgba(255, 255, 255, 0) `colors.background.onLoud` radius 999px.

![Log in link default](components/crops/shell-login-link-default.png) ![Log in link hover](components/crops/shell-login-link-hover.png) ![Log in link focus-visible](components/crops/shell-login-link-focus-visible.png) ![Log in link pressed](components/crops/shell-login-link-pressed.png)

#### For businesses link
Header link to the B2B marketing app. Measured, never followed. Read as `shell-business-link` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 153.61 x 48; radius 999px; background transparent; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 153.60pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: a::before 153.609pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 153.6x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![For businesses link default](components/crops/shell-business-link-default.png) ![For businesses link hover](components/crops/shell-business-link-hover.png) ![For businesses link focus-visible](components/crops/shell-business-link-focus-visible.png) ![For businesses link pressed](components/crops/shell-business-link-pressed.png)

#### Menu button
Header button that opens the consumer drawer (aria-haspopup). Read as `shell-menu-button` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 109.61 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1); icon 24 x 24, #0d0d0d `colors.background.primary` |
| focus-visible | pseudo ::before 109.60pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |
| pressed | icon 23.04 x 23.04, #0d0d0d `colors.background.primary` |

Child layers that carry the look: button 109.6x48 radius 999px; button::before 109.609pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 109.6x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Menu button default](components/crops/shell-menu-button-default.png) ![Menu button hover](components/crops/shell-menu-button-hover.png) ![Menu button focus-visible](components/crops/shell-menu-button-focus-visible.png) ![Menu button pressed](components/crops/shell-menu-button-pressed.png)

#### Get the app button
Header button. Opens the app-download dialog on click — captured open where the dialog mounts. Read as `shell-getapp-button` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 160.91 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1); icon 24 x 24, #0d0d0d `colors.background.primary` |
| focus-visible | pseudo ::before 160.90pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |
| pressed | icon 23.04 x 23.04, #0d0d0d `colors.background.primary` |

Child layers that carry the look: button 160.9x48 radius 999px; button::before 160.906pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 160.9x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Get the app button default](components/crops/shell-getapp-button-default.png) ![Get the app button hover](components/crops/shell-getapp-button-hover.png) ![Get the app button focus-visible](components/crops/shell-getapp-button-focus-visible.png) ![Get the app button pressed](components/crops/shell-getapp-button-pressed.png)

#### Footer
The site footer: link columns, app badges, region and legal links. Read as `footer` on the consumer home page.

**Values (default).** size 1440 x 310; background #f2f2f2 `colors.background.baseActive`; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; icon 74.97 x 22, #0d0d0d `colors.background.primary`.

![Footer default](components/crops/footer-default.png)

### Dialogs, menus and overlays

The local overlays the shell can open without submitting anything: the home page's menu drawer and its items, the search suggestion popover under the hero field, and the for-business mega-menu flyout. Each was opened, measured or photographed, then dismissed.

#### Menu drawer
The consumer menu popover opened by the Menu button: "Log in or sign up", "Download the app", "Help and support", "English (US)", "For businesses". Opened by its own button, closed after measuring. Read as `menu-drawer` on the consumer home page.

**Values (default).** size 198 x 177; background transparent; text Roobert 14/20 500, #6950f3 `colors.background.accent`; icon 20 x 20, #0d0d0d `colors.background.primary`.

Child layers that carry the look: li 222x40 background rgba(19, 19, 19, 0) `colors.background.transparent` radius 8px; li::before 222pxx40px radius 8px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; a 222x40.

![Menu drawer default](components/crops/menu-drawer-default.png)

#### Menu drawer item
A row in the menu popover. Measured, never followed. Read as `menu-item` on the consumer home page.

**Values (default).** size 198 x 20; background transparent; text Roobert 14/20 500, #6950f3 `colors.background.accent`.

![Menu drawer item default](components/crops/menu-item-default.png)

#### Search suggestions
The dropdown the treatment field opens on focus: suggestion rows for services and venues. Opened by focusing the field; Escape closes it; nothing is chosen. Read as `search-suggestions` on the consumer home page.

**Values (default).** size 536 x 2049; background transparent; text Roobert 14/20 500, #ffffff `colors.background.base`; icon 20 x 20, #6950f3 `colors.background.accent`.

Child layers that carry the look: div 600x81 background #ffffff `colors.background.base`; div 536x37 background #ffffff `colors.background.base`; div 64x36 image linear-gradient(to left, transparent, #ffffff `colors.background.base`).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Nav flyout
The mega-menu under "Business types": a column of vertical links (Salon, Barber, Nails, Spa & sauna, Medspa, Massage …). Opened by its own button. Read as `nav-flyout` on the for-business page.

**Values (default).** size 588 x 391; radius 16px; background #f5f5f5 `colors.app.dark.foreground.neutral`; text Roobert 28/36 600, #141414 `colors.app.background.primary`; icon 37.48 x 11, #141414 `colors.app.background.primary`.

![Nav flyout default](components/crops/nav-flyout-default.png)

#### Tooltip
The tooltip an info icon opens on hover: dark fill, small body copy. Opened by hovering its trigger, dismissed by moving off. Read as `tooltip` on the pricing page.

**Values (default).** size 260 x 48; padding 8px; radius 8px; background #141414 `colors.app.background.primary`; shadow rgba(0, 0, 0, 0.05) 0px 1px 2px 0px; text Roobert 12/16 400, #ffffff `colors.background.base`.

![Tooltip default](components/crops/tooltip-default.png)

### Consumer home

The marketplace landing page: a large display hero and the card carousels that follow it (recommended venues, categories, app promo).

#### Hero title
"Book local selfcare services" — the Roobert display size over the home hero. Read as `home-hero-title` on the consumer home page.

**Values (default).** size 960 x 68; background transparent; text Roobert 64/68 700, #0d0d0d `colors.background.primary`.

![Hero title default](components/crops/home-hero-title-default.png)

#### Carousel arrow
The circular Prev/Next buttons on the recommended carousel. Read as `carousel-button` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 48 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/18.4 400, #0d0d0d `colors.background.primary`; transition opacity 0.1s cubic-bezier(0.85, 0, 0.15, 1); transform translate(0px, -24px) |
| pressed | opacity 0 |
| focus-visible | pseudo ::before 48pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: button 48x48 radius 999px; button::before 48pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 48x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Carousel arrow default](components/crops/carousel-button-default.png) ![Carousel arrow pressed](components/crops/carousel-button-pressed.png) ![Carousel arrow hover](components/crops/carousel-button-hover.png) ![Carousel arrow focus-visible](components/crops/carousel-button-focus-visible.png)

### Search

The hero search row on the consumer home: a What are you looking for? treatment field, a Current location field, an Any time control and the round search button. The fields were focused only; nothing was searched.

#### Treatment field
The "All treatments" combobox of the hero search bar. Focused opens a suggestion list; nothing is submitted. Read as `search-treatment-field` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 274.53 x 22; padding 1px 2px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 14/20 500, #000000 `colors.app.black`; placeholder #0d0d0d `colors.background.primary` |

Child layers that carry the look: input 274.5x22.

![Treatment field default](components/crops/search-treatment-field-default.png) ![Treatment field focused](components/crops/search-treatment-field-focused.png)

#### Location field
The "Current location" input of the hero search bar. Focused only — no query is sent. Read as `search-location-field` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 274.53 x 22; padding 1px 2px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 14/20 500, #000000 `colors.app.black`; placeholder #0d0d0d `colors.background.primary` |

Child layers that carry the look: input 274.5x22.

![Location field default](components/crops/search-location-field-default.png) ![Location field focused](components/crops/search-location-field-focused.png)

#### When control
The "Any time" control of the hero search bar: opens the date/time popover. Focused state only in the field view; the open popover is measured where it mounts. Read as `search-when-control` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 274.53 x 22; padding 1px 2px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 14/20 500, #000000 `colors.app.black`; placeholder #0d0d0d `colors.background.primary` |

Child layers that carry the look: input 274.5x22.

![When control default](components/crops/search-when-control-default.png) ![When control focused](components/crops/search-when-control-focused.png)

#### Search button
The hero search submit. Measured, never pressed — a press runs a search query. Read as `search-button` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 94.41 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/22 600, #ffffff `colors.background.base`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 94.40pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: button 94.4x48 radius 999px; button::before 94.4062pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 94.4x48 background #0d0d0d `colors.background.primary` border 1px #0d0d0d `colors.background.primary` radius 999px.

![Search button default](components/crops/search-button-default.png) ![Search button hover](components/crops/search-button-hover.png) ![Search button focus-visible](components/crops/search-button-focus-visible.png) ![Search button pressed](components/crops/search-button-pressed.png)

### Cards

The marketplace venue card (photo, name, rating, area, category) and the business-type tile on /for-business.

#### Venue card
A recommended-venue card in the home carousel: photo, name, rating badge and score, address line and a tag ("Best in Class", "Featured"). The whole card is one link; measured, never followed. Read as `venue-card` on the consumer home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 322 x 284.66; background transparent; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; icon 14 x 14, #ffc00a `colors.background.warning` |

Child layers that carry the look: a::before 322pxx284.656px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; button 32x32 background rgba(19, 19, 19, 0.33) `colors.background.shade600` radius 999px; button::before 32pxx32px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px.

![Venue card default](components/crops/venue-card-default.png) ![Venue card hover](components/crops/venue-card-hover.png)

#### Rating badge
The score chip on a venue card ("4.9" with a star): badge fill plus the count beside it. The screen-reader "4.9 rating" copy is excluded. Read as `rating-badge` on the consumer home page.

**Values (default).** size 18.7 x 16; background transparent; text Roobert 13/16 600, #0d0d0d `colors.background.primary`.

![Rating badge default](components/crops/rating-badge-default.png)

#### Business-type card
A vertical-market card ("More info on …"): name plus icon. A link; measured, never followed. Read as `business-type-card` on the for-business page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 378.66 x 378.67; radius 18px; background transparent; text Roobert 28/36 700, #ffffff `colors.background.base`; transition box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #141414 `colors.app.background.primary` |
| hover | shadow rgba(13, 22, 25, 0.06) 0px 4px 8px 0px, rgba(13, 22, 25, 0.06) 0px 12px 20px 0px |

Child layers that carry the look: div 378.7x378.7 image linear-gradient(0deg, #000000 `colors.app.black` -5%, transparent 20%) radius 18px; button 42x42 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Business-type card default](components/crops/business-type-card-default.png) ![Business-type card hover](components/crops/business-type-card-hover.png)

### Sign-in shell

The /user-flow chooser (a back button, the customer-or-business card and a language button), the /auth consumer sign-in (email field, Continue, Google/Facebook/Apple SSO buttons, a passkey button, cross-links) and the partners.fresha.com professional sign-in (email, Continue, an SSO row and a decoy password field). Nothing was submitted; the email fields were typed into and cleared.

#### Back button
The round "Go back" control every auth-shell page carries. Read as `back-button` on the user-flow shell page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/18.4 400, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 48pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: button 48x48 radius 999px; button::before 48pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 48x48 background rgba(19, 19, 19, 0) `colors.background.transparent` border 1px rgba(255, 255, 255, 0) `colors.background.onLoud` radius 999px.

![Back button default](components/crops/back-button-default.png) ![Back button hover](components/crops/back-button-hover.png) ![Back button focus-visible](components/crops/back-button-focus-visible.png) ![Back button pressed](components/crops/back-button-pressed.png)

#### Customer/professional card
One of the two chooser cards on /user-flow ("Fresha for customers", "Fresha for professionals"): title, description and chevron. A link to the auth shell; measured, never followed. Read as `chooser-card` on the user-flow shell page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 368 x 42; background transparent; text Roobert 16/22 500, #0d0d0d `colors.background.primary` |

![Customer/professional card default](components/crops/chooser-card-default.png) ![Customer/professional card hover](components/crops/chooser-card-hover.png)

#### Language button
The "English (US)" locale picker on the chooser. Measured; not opened (opening it may navigate). Read as `language-button` on the user-flow shell page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.81 x 36; padding 8px 0px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 14/20 500, #6950f3 `colors.background.accent`; icon 20 x 20, #6950f3 `colors.background.accent` |
| hover | text Roobert 14/20 500, #5c4ace `colors.background.accentHover`; icon 20 x 20, #5c4ace `colors.background.accentHover` |
| focus-visible | pseudo ::before 97.81pxx36px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, opacity 1 |
| pressed | text Roobert 14/20 500, #403591 `colors.background.accentActive`; icon 20 x 20, #403591 `colors.background.accentActive` |

Child layers that carry the look: button 97.8x36; button::before 97.8125pxx36px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px.

![Language button default](components/crops/language-button-default.png) ![Language button hover](components/crops/language-button-hover.png) ![Language button focus-visible](components/crops/language-button-focus-visible.png) ![Language button pressed](components/crops/language-button-pressed.png)

#### Auth back button
Read as `auth-back` on the consumer sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/18.4 400, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 48pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: button 48x48 radius 999px; button::before 48pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 48x48 background rgba(19, 19, 19, 0) `colors.background.transparent` border 1px rgba(255, 255, 255, 0) `colors.background.onLoud` radius 999px.

![Auth back button default](components/crops/auth-back-default.png) ![Auth back button hover](components/crops/auth-back-hover.png) ![Auth back button focus-visible](components/crops/auth-back-focus-visible.png) ![Auth back button pressed](components/crops/auth-back-pressed.png)

#### Continue button
The email submit — a press requests a verification code, so it is only measured. Read as `auth-continue` on the consumer sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 448 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/22 600, #ffffff `colors.background.base`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 448pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: button 448x48 radius 999px; button::before 448pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 448x48 background #0d0d0d `colors.background.primary` border 1px #0d0d0d `colors.background.primary` radius 999px.

![Continue button default](components/crops/auth-continue-default.png) ![Continue button hover](components/crops/auth-continue-hover.png) ![Continue button focus-visible](components/crops/auth-continue-focus-visible.png) ![Continue button pressed](components/crops/auth-continue-pressed.png)

#### SSO button
"Continue with Google" (the Apple and passkey rows share the style): a full-width outlined button with the provider mark. Never pressed — a press starts an OAuth flow. Read as `sso-button` on the consumer sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 448 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 448pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: button 448x48 radius 999px; button::before 448pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 448x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![SSO button default](components/crops/sso-button-default.png) ![SSO button hover](components/crops/sso-button-hover.png) ![SSO button focus-visible](components/crops/sso-button-focus-visible.png) ![SSO button pressed](components/crops/sso-button-pressed.png)

#### Passkey button
Read as `passkey-button` on the consumer sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 448 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1); icon 24 x 24, #0d0d0d `colors.background.primary` |

Child layers that carry the look: button 448x48 radius 999px; button::before 448pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 448x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Passkey button default](components/crops/passkey-button-default.png) ![Passkey button hover](components/crops/passkey-button-hover.png)

#### Cross-over link
"Have a business account? Go to Fresha for professionals" — the link out to the partner sign-in. Measured, never followed. Read as `auth-cross-link` on the consumer sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 198.02 x 16; radius 4px; background transparent; text Roobert 14/20 500, #6950f3 `colors.background.accent` |
| hover | text Roobert 14/20 500, #5c4ace `colors.background.accentHover` |

Child layers that carry the look: a::before 19816pxx16px radius 4px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px.

![Cross-over link default](components/crops/auth-cross-link-default.png) ![Cross-over link hover](components/crops/auth-cross-link-hover.png)

#### Partner continue button
The professional sign-in submit. Measured, never pressed. Read as `partner-continue` on the partner sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 396 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 17/24 600, #ffffff `colors.background.base`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 396pxx48px: shadow #ffffff 0px 0px 0px 2px, radius 999px, opacity 1 |

Child layers that carry the look: button 396x48 radius 999px; div 396x48 background #0d0d0d `colors.background.primary` border 1px #0d0d0d `colors.background.primary` radius 999px.

![Partner continue button default](components/crops/partner-continue-default.png) ![Partner continue button hover](components/crops/partner-continue-hover.png) ![Partner continue button focus-visible](components/crops/partner-continue-focus-visible.png) ![Partner continue button pressed](components/crops/partner-continue-pressed.png)

#### Partner SSO button
Read as `partner-sso` on the partner sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 396 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 17/24 600, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 396pxx48px: shadow #ffffff 0px 0px 0px 2px, radius 999px, opacity 1 |

Child layers that carry the look: button 396x48 radius 999px; div 396x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Partner SSO button default](components/crops/partner-sso-default.png) ![Partner SSO button hover](components/crops/partner-sso-hover.png) ![Partner SSO button focus-visible](components/crops/partner-sso-focus-visible.png) ![Partner SSO button pressed](components/crops/partner-sso-pressed.png)

#### Partner cross link
The link sending customers back to the consumer sign-in. Measured, never followed. Read as `partner-cross-link` on the partner sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 184.41 x 18; radius 4px; background transparent; text Roobert 15/20 500, #6950f3 `colors.background.accent` |
| hover | text Roobert 15/20 500, #5c4ace `colors.background.accentHover` |

![Partner cross link default](components/crops/partner-cross-link-default.png) ![Partner cross link hover](components/crops/partner-cross-link-hover.png)

### Form controls

The sign-in email fields and the partner form's decoy password input (the LP browse page carries no sort select — `lp-sort-select` is recorded as missing).

#### Email field
The auth shell's single text input: "We'll send you a verification code". Typed into then cleared; Continue is never pressed — no code is ever requested. Read as `auth-email-field` on the consumer sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 374 x 46; padding 16px; radius 12px; background rgba(19, 19, 19, 0) `colors.background.transparent`; outline 2px solid transparent, offset 2px; text Roobert 16/22 400, #0d0d0d `colors.background.primary`; placeholder #0d0d0d `colors.background.primary` |

![Email field default](components/crops/auth-email-field-default.png) ![Email field focused](components/crops/auth-email-field-focused.png) ![Email field filled](components/crops/auth-email-field-filled.png)

#### Partner email field
The professional sign-in's email input. Typed into then cleared; nothing is submitted. Read as `partner-email-field` on the partner sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 394 x 46; padding 16px; radius 12px; background rgba(19, 19, 19, 0) `colors.background.transparent`; outline 2px solid transparent, offset 2px; text Roobert 15/20 400, #0d0d0d `colors.background.primary`; placeholder #0d0d0d `colors.background.primary` |

![Partner email field default](components/crops/partner-email-field-default.png) ![Partner email field focused](components/crops/partner-email-field-focused.png) ![Partner email field filled](components/crops/partner-email-field-filled.png)

#### Sort select
The "Sort by" native select over the results list. Read as `lp-sort-select` on the LP browse page.

Not on the page when it was captured.

#### Hidden password input
An off-viewport input[type=password] (x≈-1278) in the partner sign-in form — a browser-autocomplete decoy, not a painted control. The real flow is email + verification code. Read as `partner-decoy-password` on the partner sign-in page.

**Values (default).** size 183 x 22.09; padding 1px 2px; border 2px inset #767676 `colors.foreground.neutralFaded`; background #ffffff `colors.background.base`; text Roobert 14/16.1 400, #000000 `colors.app.black`; placeholder #000000 `colors.app.black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Venue page

A public venue profile (/a/<slug>): breadcrumb, gallery, venue title and tabs, the service list with per-service Book buttons, the Book now bar, opening-hours table, staff and review cards. Booking a service was never pressed.

#### Breadcrumb
The category/location breadcrumb over the venue title. Read as `breadcrumb` on the venue page.

**Values (default).** size 1376 x 36; padding 0px 0px 16px 0px; background transparent; text Roobert 14/20 400, #767676 `colors.foreground.neutralFaded`.

Child layers that carry the look: a::before 38.6094pxx16px radius 4px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; a::before 70.9062pxx16px radius 4px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; a::before 67.1094pxx16px radius 4px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px.

![Breadcrumb default](components/crops/breadcrumb-default.png)

#### Venue section tab
The sticky section nav (Services / Team / Reviews / About / Photos) — anchor links that scroll the page. Measured, never followed. Read as `venue-tab` on the venue page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48.41 x 52; radius 2px; background rgba(19, 19, 19, 0) `colors.background.transparent`; outline 2px solid transparent, offset 2px; pseudo ::after 48.40pxx4px: bg #0d0d0d `colors.background.primary`, radius 4px 4px 0px 0px, opacity 1; text Roobert 14/20 500, #0d0d0d `colors.background.primary` |
| focus-visible | pseudo ::before 64.40pxx48px: shadow #ffffff 0px 0px 0px 2px inset; border 2px solid #0d0d0d `colors.background.primary`, radius 8px, opacity 1 + ::after 48.40pxx4px: bg #0d0d0d `colors.background.primary`, radius 4px 4px 0px 0px, opacity 1 |

![Venue section tab default](components/crops/venue-tab-default.png) ![Venue section tab focus-visible](components/crops/venue-tab-focus-visible.png)

#### Book now button
The venue page's primary CTA — the primary button style. Never pressed: a press starts the booking wizard. Read as `book-now` on the venue page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 388 x 48; radius 999px; background transparent; text Roobert 16/22 600, #ffffff `colors.background.base`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 388pxx48px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: a::before 388pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 388x48 background #0d0d0d `colors.background.primary` border 1px #0d0d0d `colors.background.primary` radius 999px.

![Book now button default](components/crops/book-now-default.png) ![Book now button hover](components/crops/book-now-hover.png) ![Book now button focus-visible](components/crops/book-now-focus-visible.png) ![Book now button pressed](components/crops/book-now-pressed.png)

#### Gallery button
"See all images" over the photo grid. Measured only — opening it navigates to the gallery. Read as `gallery-button` on the venue page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 123.61 x 36; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 14/20 500, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 123.60pxx36px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: button 123.6x36 radius 999px; button::before 123.609pxx36px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 123.6x36 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Gallery button default](components/crops/gallery-button-default.png) ![Gallery button hover](components/crops/gallery-button-hover.png) ![Gallery button focus-visible](components/crops/gallery-button-focus-visible.png) ![Gallery button pressed](components/crops/gallery-button-pressed.png)

#### Venue title
The venue name heading. Read as `venue-title` on the venue page.

**Values (default).** size 1248 x 52; background transparent; text Roobert 48/52 700, #0d0d0d `colors.background.primary`.

![Venue title default](components/crops/venue-title-default.png)

#### Service row
A bookable service line: name, duration, price and a Select/Book control. Measured, never booked. Read as `service-row` on the venue page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 836 x 74; background transparent; text Roobert 16/22 500, #0d0d0d `colors.background.primary` |

Child layers that carry the look: button 65.6x36 radius 999px; button::before 65.6094pxx36px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 65.6x36 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Service row default](components/crops/service-row-default.png) ![Service row hover](components/crops/service-row-hover.png)

#### Service select button
The per-service select control. Never pressed. Read as `service-book-button` on the venue page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 65.61 x 36; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 14/20 500, #0d0d0d `colors.background.primary`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |
| focus-visible | pseudo ::before 65.60pxx36px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, radius 999px, opacity 1 |

Child layers that carry the look: button 65.6x36 radius 999px; button::before 65.6094pxx36px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 65.6x36 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Service select button default](components/crops/service-book-button-default.png) ![Service select button hover](components/crops/service-book-button-hover.png) ![Service select button focus-visible](components/crops/service-book-button-focus-visible.png) ![Service select button pressed](components/crops/service-book-button-pressed.png)

#### Review card
A venue review: star row, comment text, service and staff line, date. Read as `review-card` on the venue page.

**Values (default).** size 418 x 170; background transparent; text Roobert 22/28 600, #6950f3 `colors.background.accent`; icon 14 x 14, #ffc00a `colors.background.warning`.

Child layers that carry the look: div 64x64 background #f0f0ff `colors.background.accentFaded` border 1px #f0f0ff `colors.background.accentFaded` radius 999px; button 23.5x16 radius 4px; button::before 23.5156pxx16px radius 4px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px.

![Review card default](components/crops/review-card-default.png)

#### Opening times
The "Opening times" week schedule in the About section — green dot per open day, grey for closed. Read as `hours-table` on the venue page.

**Values (default).** size 418 x 250; background transparent; text Roobert 24/32 600, #0d0d0d `colors.background.primary`.

Child layers that carry the look: span 13x13 background #78d240 radius 999px; span 13x13 background #bfbfbf `colors.background.neutralActive` radius 999px; span 13x13 background #78d240 radius 999px.

![Opening times default](components/crops/hours-table-default.png)

#### Staff avatar
A Team circle: photo, name, "Top stylist" label and rating badge. Read as `staff-avatar` on the venue page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 120 x 180; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 14/20 600, #0d0d0d `colors.background.primary`; icon 16 x 16, #ffc00a `colors.background.warning` |

Child layers that carry the look: button 120x180 radius 8px; button::before 120pxx180px radius 8px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 120x120 background #f0f0ff `colors.background.accentFaded` border 1px #f0f0ff `colors.background.accentFaded` radius 999px.

![Staff avatar default](components/crops/staff-avatar-default.png) ![Staff avatar hover](components/crops/staff-avatar-hover.png)

#### Review score
The big "5.0 Best in Class" review block: display-size score with trophy badges. Read as `review-score` on the venue page.

**Values (default).** size 40.7 x 20; background transparent; text Roobert 14/20 600, #0d0d0d `colors.background.primary`; icon 16 x 16, #ffc00a `colors.background.warning`.

![Review score default](components/crops/review-score-default.png)

### Booking wizard

The /booking step the venue's Book controls lead to, captured at the service-selection boundary: the step header, category pills, service rows with their own Add checkboxes and the summary cart. One service was ticked then unticked to record both states; Continue was never pressed and nothing was booked.

#### Booking header
The wizard chrome: back arrow, the "Services › Professional › Time › Confirm" step trail and a close control. Read as `booking-header` on the booking wizard page.

**Values (default).** size 1440 x 72; padding 0px 32px; background transparent; text Roobert 19/24 600, #0d0d0d `colors.background.primary`.

Child layers that carry the look: button 48x48 radius 999px; button::before 48pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 48x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![Booking header default](components/crops/booking-header-default.png)

#### Wizard step
A step label in the "Services / Professional / Time / Confirm" trail — the current step emphasised. Read as `booking-step` on the booking wizard page.

**Values (default).** size 82.2 x 20; background transparent; text Roobert 14/20 500, #0d0d0d `colors.background.primary`.

![Wizard step default](components/crops/booking-step-default.png)

#### Booking service row
A selectable service card: name, duration, notes and price, with a round "+" add control. Adding only marks the service in the local cart; nothing is booked. Read as `booking-service-row` on the booking wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 596 x 124; background transparent; text Roobert 16/22 500, #0d0d0d `colors.background.primary`; icon 16 x 16, #0d0d0d `colors.background.primary` |

Child layers that carry the look: button 36x36 background #ffffff `colors.background.base` border 1px #e5e5e5 `colors.background.neutral` radius 999px shadow rgba(19, 19, 19, 0.12) 0px 2px 4px 0px.

![Booking service row default](components/crops/booking-service-row-default.png) ![Booking service row hover](components/crops/booking-service-row-hover.png)

#### Add-service button
The round "+" that selects a service for the cart. Its pressed state is captured for real: one press adds the service, then it is removed again — the wizard never advances. Read as `booking-add-button` on the booking wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 36 x 36; border 1px solid #e5e5e5 `colors.background.neutral`; radius 999px; background #ffffff `colors.background.base`; shadow rgba(19, 19, 19, 0.12) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Roobert 16/18.4 400, #0d0d0d `colors.background.primary`; icon 16 x 16, #0d0d0d `colors.background.primary` |
| hover | border 1px solid #d3d3d3 `colors.background.neutralFadedActive`; background #f5f5f5 `colors.app.dark.foreground.neutral` |
| pressed | border 1px solid #bfbfbf `colors.background.neutralActive`; background #f2f2f2 `colors.background.baseActive` |

![Add-service button default](components/crops/booking-add-button-default.png) ![Add-service button hover](components/crops/booking-add-button-hover.png) ![Add-service button focus-visible](components/crops/booking-add-button-focus-visible.png) ![Add-service button pressed](components/crops/booking-add-button-pressed.png)

#### Category pill
The service-category chips under "Select services" (Featured, Promotion, Set menu, CUT & TRIM …) — the active one is solid. Read as `booking-category-pill` on the booking wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 91.2 x 36; padding 0px 16px; radius 999px; background #0d0d0d `colors.background.primary`; outline 2px solid transparent, offset 2px; text Roobert 14/20 500, #ffffff `colors.background.base` |

![Category pill default](components/crops/booking-category-pill-default.png) ![Category pill hover](components/crops/booking-category-pill-hover.png)

#### Cart summary
The right-hand booking summary: venue card (photo, rating, address), the selected-services list, Total and the step button. Read as `booking-cart` on the booking wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: service-added) | size 444 x 756; padding 0px 32px; background transparent; text Roobert 16/22 600, #0d0d0d `colors.background.primary`; icon 16 x 16, #ffc00a `colors.background.warning` |

Child layers that carry the look: div 380x98 background #ffffff `colors.background.base`; a::before 64pxx64px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 64x64 background #ffffff `colors.background.base` border 1px #e5e5e5 `colors.background.neutral` radius 8px.

![Cart summary default](components/crops/booking-cart-default.png) ![Cart summary service-added](components/crops/booking-cart-service-added.png)

#### Continue button
The wizard's step button — grey while the cart is empty, dark once a service is selected. Measured, never pressed: a press advances to "Professional". The wizard never goes past step 1 in this capture. Read as `booking-continue` on the booking wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 380 x 48; radius 999px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/22 600, #ffffff `colors.background.base`; transition max-inline-size 0.2s cubic-bezier(0.85, 0, 0.15, 1) |

Child layers that carry the look: button 380x48 radius 999px; button::before 380pxx48px radius 999px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px; div 380x48 background #0d0d0d `colors.background.primary` border 1px #0d0d0d `colors.background.primary` radius 999px.

![Continue button default](components/crops/booking-continue-default.png) ![Continue button hover](components/crops/booking-continue-hover.png) ![Continue button pressed](components/crops/booking-continue-pressed.png)

### For-business marketing

The /for-business B2B landing (the same Panda system as the partner app): the nav with the Business types flyout button, the display hero, the Get a demo / Watch film buttons, the business-type grid and the stat row.

#### B2B top bar
The marketing app bar shared by /for-business, /pricing, /blog and /careers: product logo, Business types / Features flyouts, Marketplace, Pricing, Help, Blog, "Try for free". Read as `b2b-header` on the pricing page.

**Values (default).** size 1440 x 72; background transparent; text Roobert 17/24 600, #141414 `colors.app.background.primary`; transition all 0.3s cubic-bezier(0.4, 0, 0.2, 1); icon 75 x 22, #141414 `colors.app.background.primary`.

Child layers that carry the look: div 0x0 background #ffffff `colors.background.base` radius 24px shadow rgba(13, 22, 25, 0.16) 0px 8px 32px 0px; div 0x0 background #ffffff `colors.background.base` radius 24px shadow rgba(13, 22, 25, 0.16) 0px 8px 32px 0px; a 171.8x48 background #ffffff `colors.background.base` border 1px #d3d3d3 `colors.background.neutralFadedActive` radius 999px.

![B2B top bar default](components/crops/b2b-header-default.png)

#### Nav flyout button
"Business types" and "Features" in the marketing nav — each opens a mega-menu flyout on click/hover. Read as `nav-flyout-button` on the for-business page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160.2 x 48; padding 0px 20px; radius 999px; background transparent; text Roobert 17/24 600, #141414 `colors.app.background.primary`; transition color 0.2s cubic-bezier(0, 0.55, 0.45, 1), background-color 0.2s cubic-bezier(0, 0.55, 0.45, 1), border-color 0.2s cubic-bezier(0, 0.55, 0.45, 1), text-decoration-color 0.2s cubic-bezier(0, 0.55, 0.45, 1), fill 0.2s cubic-bezier(0, 0.55, 0.45, 1), stroke 0.2s cubic-bezier(0, 0.55, 0.45, 1) |
| hover | text Roobert 17/24 600, #6950f3 `colors.background.accent` |
| focus-visible | outline 2px solid transparent, offset 2px |

![Nav flyout button default](components/crops/nav-flyout-button-default.png) ![Nav flyout button hover](components/crops/nav-flyout-button-hover.png) ![Nav flyout button focus-visible](components/crops/nav-flyout-button-focus-visible.png)

#### Marketing hero title
The /for-business display heading. Read as `b2b-hero-title` on the for-business page.

**Values (default).** size 1028 x 156; padding 80px 0px 16px 0px; background transparent; text Roobert 56/60 700, #141414 `colors.app.background.primary`.

![Marketing hero title default](components/crops/b2b-hero-title-default.png)

#### Marketing CTA
The primary marketing button. Measured, never pressed. Read as `b2b-cta` on the for-business page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180.02 x 48; padding 0px 24px; radius 999px; background #141414 `colors.app.background.primary`; text Roobert 17/24 600, #ffffff `colors.background.base`; transition transform 0.2s cubic-bezier(0, 0.55, 0.45, 1) |
| hover | background #2f2f2f `colors.app.background.primaryHover` |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | background #2f2f2f `colors.app.background.primaryHover` |

![Marketing CTA default](components/crops/b2b-cta-default.png) ![Marketing CTA hover](components/crops/b2b-cta-hover.png) ![Marketing CTA focus-visible](components/crops/b2b-cta-focus-visible.png) ![Marketing CTA pressed](components/crops/b2b-cta-pressed.png)

#### Watch button
"Watch an overview" — the secondary media button. Read as `watch-button` on the for-business page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 227.61 x 48; padding 0px 24px; border 1px solid #d3d3d3 `colors.background.neutralFadedActive`; radius 999px; background #ffffff `colors.background.base`; text Roobert 17/24 600, #141414 `colors.app.background.primary`; transition transform 0.2s cubic-bezier(0, 0.55, 0.45, 1); icon 20 x 20, #141414 `colors.app.background.primary` |
| hover | border 1px solid #bfbfbf `colors.background.neutralActive`; background #f5f5f5 `colors.app.dark.foreground.neutral` |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | size 218.51 x 46.08; border 1px solid #acacac `colors.foreground.disabled`; background #f5f5f5 `colors.app.dark.foreground.neutral`; transform scale(0.96); icon 19.2 x 19.2, #141414 `colors.app.background.primary` |

![Watch button default](components/crops/watch-button-default.png) ![Watch button hover](components/crops/watch-button-hover.png) ![Watch button focus-visible](components/crops/watch-button-focus-visible.png) ![Watch button pressed](components/crops/watch-button-pressed.png)

#### Stat
A proof-point figure in the marketing stats row. Read as `stat` on the for-business page.

**Values (default).** size 193.02 x 52; background transparent; text Roobert 48/52 700, #ffffff `colors.background.base`.

![Stat default](components/crops/stat-default.png)

### Pricing

The /pricing page: plan cards with prices and CTAs, the feature rows, the small info icons and the FAQ disclosures (one was opened for its capture).

#### Plan card
A pricing plan column (Independent / Team / Enterprise): plan name, monthly price, "7 day trial" badge, feature list and its CTA. Read as `plan-card` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 277 x 368.5; background transparent; text Roobert 24/32 600, #141414 `colors.app.background.primary` |

Child layers that carry the look: div 98.9x30 background #f0f0ff `colors.background.accentFaded` border 1px #dbddff `colors.background.accentFadedHover` radius 999px.

![Plan card default](components/crops/plan-card-default.png) ![Plan card hover](components/crops/plan-card-hover.png)

#### Plan price
The price display inside a plan card (amount + period + commission line). Read as `plan-price` on the pricing page.

**Values (default).** size 277 x 44; background transparent; text Roobert 40/44 700, #141414 `colors.app.background.primary`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
The plan card's call to action. Measured, never pressed: a press starts sign-up. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 151.41 x 48; padding 0px 20px; radius 999px; background #141414 `colors.app.background.primary`; text Roobert 17/24 600, #ffffff `colors.background.base`; transition transform 0.2s cubic-bezier(0, 0.55, 0.45, 1) |
| hover | background #2f2f2f `colors.app.background.primaryHover` |
| focus-visible | outline 2px solid transparent, offset 2px |
| pressed | size 145.35 x 46.08; background #2f2f2f `colors.app.background.primaryHover`; transform scale(0.96) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Feature row
A line in a plan's feature list (label plus checkmark or info icon). Read as `feature-row` on the pricing page.

**Values (default).** size 277 x 22.5; background transparent; text Roobert 15/22.5 400, #767676 `colors.foreground.neutralFaded`.

![Feature row default](components/crops/feature-row-default.png)

#### Info icon
The "i" badge beside a feature — hovering opens a tooltip. Read as `info-icon` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 16 x 16; background transparent; text Roobert 15/20 400, #767676 `colors.foreground.neutralFaded`; icon 17 x 16, #767676 `colors.foreground.neutralFaded` |
| focus-visible | outline 1px auto #101010, offset 0px |

![Info icon default](components/crops/info-icon-default.png) ![Info icon hover](components/crops/info-icon-hover.png) ![Info icon focus-visible](components/crops/info-icon-focus-visible.png)

#### FAQ item
A pricing FAQ disclosure: question row with a chevron. The open state is captured by its own toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, open) | size 800 x 68; padding 20px 24px; background transparent; text Roobert 20/28 600, #141414 `colors.app.background.primary`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #141414 `colors.app.background.primary` |

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item hover](components/crops/faq-item-hover.png) ![FAQ item open](components/crops/faq-item-open.png)

### Marketplace browse (/lp)

The legacy /lp/ microsite (its own stylesheet, literal values, no token vars): the LP header, the category chip rail, browse venue cards, the Show on map button and pagination. The category page /lp/en/bt/hair-salons and the Singapore browse page were both captured.

#### LP top bar
The /lp microsite chrome: its own stylesheet, no Panda vars — every value here is measured. Read as `lp-header` on the LP browse page.

**Values (default).** size 1440 x 66; padding 8px 32px; background transparent; text Roobert 14/20 500, #0d0d0d `colors.background.primary`; icon 74.97 x 22, #0d1619.

Child layers that carry the look: div 720x48 background #ffffff `colors.background.base` border 1px #e5e5e5 `colors.background.neutral` radius 999px shadow rgba(20, 20, 20, 0.02) 0px 2px 3px 0px, rgba(20, 20, 20, 0.03) 0px 4px 6px 0px; a::before 1pxx20px background #e5e5e5 `colors.background.neutral`; a::before 1pxx20px background #e5e5e5 `colors.background.neutral`.

![LP top bar default](components/crops/lp-header-default.png)

#### Browse venue card
A venue result in the /lp list: photo, name, address, rating and review count, next-availability line. Read as `lp-venue-card` on the LP browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 381.33 x 543.5; background transparent; text Roobert 13/16 600, #0d0d0d `colors.background.primary`; icon 16 x 16, #0d1619 |

Child layers that carry the look: span 81.2x24 image linear-gradient(rgba(255, 255, 255, 0.7) `colors.background.glass`, rgba(255, 255, 255, 0. radius 999px shadow rgba(20, 20, 20, 0.12) 0px 1px 6px 0px, rgba(20, 20, 20, 0.04) `hashed.ewBjkr` 0px 0px 0px 1px; span::before 79.2031pxx22px image linear-gradient(135deg, rgba(255, 255, 255, 0.8) `hashed.fSeetX` 20%, rgba(255, 255, 255,  radius 999px; span 57.5x24 image linear-gradient(rgba(255, 255, 255, 0.7) `colors.background.glass`, rgba(255, 255, 255, 0. radius 999px shadow rgba(20, 20, 20, 0.12) 0px 1px 6px 0px, rgba(20, 20, 20, 0.04) `hashed.ewBjkr` 0px 0px 0px 1px.

![Browse venue card default](components/crops/lp-venue-card-default.png) ![Browse venue card hover](components/crops/lp-venue-card-hover.png)

#### See map button
Opens the map panel over the results. Measured at rest and opened by its own control where the overlay mounts. Read as `lp-map-button` on the LP browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 63.31 x 19; background transparent; text Roobert 16/22 400, #6950f3 `colors.background.accent` |
| focus-visible | outline 2px solid #0d0d0d `colors.background.primary`, offset 2px |

![See map button default](components/crops/lp-map-button-default.png) ![See map button hover](components/crops/lp-map-button-hover.png) ![See map button focus-visible](components/crops/lp-map-button-focus-visible.png) ![See map button pressed](components/crops/lp-map-button-pressed.png)

#### Pagination
The result-list pager. Measured, never followed. Read as `lp-pagination` on the LP browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.61 x 38; padding 8px 16px; border 1px solid #d3d3d3 `colors.background.neutralFadedActive`; radius 999px; background #ffffff `colors.background.base`; text Roobert 14/20 500, #0d0d0d `colors.background.primary` |
| hover | border 1px solid #bfbfbf `colors.background.neutralActive` |

![Pagination default](components/crops/lp-pagination-default.png) ![Pagination hover](components/crops/lp-pagination-hover.png)

#### Category chip
A category pill in the footer browse row (Beauty Salons, Barbers, Nail Salons …). A link; measured, never followed. Read as `lp-category-chip` on the LP browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126.7 x 36; padding 6px 16px; border 1px solid #e5e5e5 `colors.background.neutral`; radius 999px; background #ffffff `colors.background.base`; text Roobert 14/20 500, #0d0d0d `colors.background.primary`; transition border-color 0.25s cubic-bezier(0.42, 0, 0.58, 1) |
| hover | border 1px solid #b7babe |

![Category chip default](components/crops/lp-category-chip-default.png) ![Category chip hover](components/crops/lp-category-chip-hover.png)

#### See all services link
The "See all N services" link inside a venue card. Measured, never followed. Read as `lp-see-all` on the LP browse page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 381.33 x 19; background transparent; text Roobert 14/19 500, #6950f3 `colors.background.accent` |
| hover | text Roobert 14/19 500, #5c4ace `colors.background.accentHover` |

![See all services link default](components/crops/lp-see-all-default.png) ![See all services link hover](components/crops/lp-see-all-hover.png)

#### Card price
A service price inside a venue card ("$98", "from $0"). Read as `lp-price` on the LP browse page.

**Values (default).** size 26.7 x 20; background transparent; text Roobert 14/20 500, #0d0d0d `colors.background.primary`.

![Card price default](components/crops/lp-price-default.png)

### Help centre

The /help-center surface: the 654px search pill (focused only, nothing searched) and the topic/article cards.

#### Help search field
The help-centre search input (a 654x60 pill). Focused only — no query is sent. Read as `help-search` on the help centre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 654 x 60; background #ffffff `colors.background.base`; outline 2px solid transparent, offset 2px; text Roobert 16/16 400, #262627; placeholder #9ca3af |

![Help search field default](components/crops/help-search-default.png) ![Help search field focused](components/crops/help-search-focused.png)

#### Help topic card
A help topic tile linking to an article group. Measured, never followed. Read as `topic-card` on the help centre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 362.66 x 210; padding 32px; border 1px solid #e5e5e5 `colors.background.neutral`; radius 8px; background #ffffff `colors.background.base`; text Roobert 20/28 600, #0d0d0d `colors.background.primary`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #d3d3d3 `colors.background.neutralFadedActive`; background #f5f5f5 `colors.app.dark.foreground.neutral` |

![Help topic card default](components/crops/topic-card-default.png) ![Help topic card hover](components/crops/topic-card-hover.png)

#### Article link
A help article row. Measured, never followed. Read as `article-link` on the help centre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 362.67 x 234; padding 32px; border 1px solid #e5e5e5 `colors.background.neutral`; radius 8px; background #ffffff `colors.background.base`; text Roobert 20/28 600, #0d0d0d `colors.background.primary`; transition all 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #d3d3d3 `colors.background.neutralFadedActive`; background #f5f5f5 `colors.app.dark.foreground.neutral` |

![Article link default](components/crops/article-link-default.png) ![Article link hover](components/crops/article-link-hover.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 with an iPhone user agent: the mobile sticky header and menu button, the compact search field and a venue card.

#### Mobile top bar
The 390x72 sticky mobile bar: wordmark left, icon burger right. Read as `m-header` on the consumer home page at 390 wide.

**Values (default).** size 390 x 72; background transparent; text Roobert 16/18.4 400, #0d0d0d `colors.background.primary`; transition block-size 0.2s cubic-bezier(0.85, 0, 0.15, 1); icon 74.97 x 22, #0d0d0d `colors.background.primary`.

![Mobile top bar default](components/crops/m-header-default.png)

#### Mobile menu button
The 32x32 icon-only burger (aria-label "Menu") in the mobile bar. Read as `m-menu-button` on the consumer home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/18.4 400, #0d0d0d `colors.background.primary`; icon 32 x 32, #0d0d0d `colors.background.primary` |
| focus-visible | pseudo ::before 32pxx32px: shadow #ffffff 0px 0px 0px 2px, #0d0d0d 0px 0px 0px 4px, opacity 1 |

Child layers that carry the look: button 32x32; button::before 32pxx32px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px.

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile search field
Read as `m-search-field` on the consumer home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 238 x 24; padding 1px 2px; background transparent; outline 2px solid transparent, offset 2px; text Roobert 16/22 500, #000000 `colors.app.black`; placeholder #0d0d0d `colors.background.primary` |

Child layers that carry the look: input 238x24.

![Mobile search field default](components/crops/m-search-field-default.png) ![Mobile search field focused](components/crops/m-search-field-focused.png)

#### Mobile venue card
Read as `m-venue-card` on the consumer home page at 390 wide.

**Values (default).** size 236 x 227.33; background transparent; text Roobert 16/18.4 400, #0d0d0d `colors.background.primary`.

Child layers that carry the look: a::before 236pxx227.328px shadow #ffffff `colors.background.base` 0px 0px 0px 2px, #0d0d0d `colors.background.primary` 0px 0px 0px 4px.

![Mobile venue card default](components/crops/m-venue-card-default.png)

## Gaps

### Pages

- **Everything behind sign-in.** Nothing in the customer account (booking history, favourites, wallet, gift cards, settings), nothing in the partner app past its sign-in form (the calendar, sales, client list and marketing screens the B2B pages advertise), and no OAuth or SSO flow was started — those pages were never reached.
- **Anything that submits.** No search was run, no venue was booked (the wizard stops at service selection; Continue was never pressed), no sign-in, sign-up, demo or contact form was sent, no newsletter was joined and no app-store link was followed.
- **The venue map.** The LP browse page's Show on map button and the venue pages' map blocks were measured but the map overlays were not opened; their tiles load live data.
- **Blog and careers articles.** The index pages are captured; individual articles and job postings were not opened.
- **terms.fresha.com** was identified as the legal-documents host; the /cookies page was captured but the terms pages were not screenshotted.

### States

- **Pressed** was forced with DevTools, so a state a script adds on mousedown (if any) is missing.
- **Hover on the menu item and the venue tab** could not be applied (the elements unmount or move when the pointer leaves); those entries hold the states that did take.
- **The LP browse sort select** does not exist on the captured page — its only `<select>` is the header's language picker; `lp-sort-select` is recorded missing rather than measured on the wrong control.
- **Disabled, loading and error states** do not exist on the captured controls (sign-in forms disable Continue until an email is present, but no disabled example was recorded).

### Themes

Fresha ships three declared scopes. **Light** is the only theme the consumer and B2B pages paint: no signed-out page sets a data-theme, and emulating prefers-color-scheme: dark changes nothing there. **Dark** is genuinely painted on the partners.fresha.com sign-in, which sets `data-theme="auto"` (screenshot partner-signin-dark-default.png). **Accent** (`[data-theme=accent]`, a violet section theme) is declared in the partner and B2B sheets but no signed-out element was observed carrying it. The consumer/B2B dark and every accent declaration are kept in tokens.json as declared-but-unpainted evidence and marked so in their $extensions.

### Fonts

- **Roobert and AktivGroteskVF** are self-hosted variable faces the site serves itself; the style guide falls back to the system font.
- **Tartuffo, Changa and PlayfairDisplay** make up the display stack (`--font-display`); Tartuffo is a commercial face not on Google Fonts.

### Screenshots

- Venue photos, hero photography and map tiles are Fresha's and its venues' content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Venue, review and staff names in the captures are Fresha's public content, recorded as the product renders them.
- No personal data was captured: every page was read signed out, the only text ever typed was a placeholder address that was cleared, and the reCAPTCHA badge (a widget, not page content) was hidden in captures.
