# Gumroad components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Read from gumroad.com and ichigo.gumroad.com on 2026-11-17, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Later recaptures merge into the same file, so every entry names the date its own states were read; a state a re-read missed keeps its earlier date and says so. Nothing was signed into, bought, searched or submitted; the only presses were local UI toggles the page's own chrome provides — the Discover carousel arrow, the product page's billing-term select and Share popover, the checkout gift toggle and the phone's navigation menu; every link was measured, never followed.

**Where this was read.** Two surfaces, both public and signed-out: gumroad.com itself — the landing, Discover and a category page, features, pricing, about, blog, Gumclaw, help, terms and the login/signup cards — and one creator subdomain, ichigo.gumroad.com, for a real product page, its creator profile and the public checkout its 'Subscribe' link opens. The signed-in product (the seller dashboard, the buyer library, payout and settings) is listed under Gaps, not captured.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (50 components, 111 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `ABC Favorit 16/22 400, #000000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (107 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where `{theme}` is the surface the page painted at capture: every page loads `light`, and `{page}-dark-*` shots are the same page under `prefers-color-scheme: dark` emulation — gumroad.com's own dark theme, verified by the painted background before the shot; there is no in-page toggle. The product and creator pages pin a light palette, so no `product-dark-*` or `creator-dark-*` exists. Desktop shots are 1440 x 900 at 1x; `-full` shots are the whole document at 1x, bounded at eight chunks with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Landing | `/` | [dark default](screenshots/home-dark-default.png), [dark full](screenshots/home-dark-full.png), [light default](screenshots/home-light-default.png), [light full](screenshots/home-light-full.png) |
| Discover | `/discover` | [dark default](screenshots/discover-dark-default.png), [light carousel](screenshots/discover-light-carousel.png), [light default](screenshots/discover-light-default.png), [light full](screenshots/discover-light-full.png) |
| Category (Design) | `/design` | [dark default](screenshots/category-dark-default.png), [light default](screenshots/category-light-default.png), [light full](screenshots/category-light-full.png) |
| Features | `/features` | [dark default](screenshots/features-dark-default.png), [light default](screenshots/features-light-default.png), [light full](screenshots/features-light-full.png) |
| Pricing | `/pricing` | [dark default](screenshots/pricing-dark-default.png), [light default](screenshots/pricing-light-default.png), [light full](screenshots/pricing-light-full.png) |
| About | `/about` | [light default](screenshots/about-light-default.png), [light full](screenshots/about-light-full.png) |
| Blog | `/blog` | [light default](screenshots/blog-light-default.png), [light full](screenshots/blog-light-full.png) |
| Gumclaw | `/gumclaw` | [light default](screenshots/gumclaw-light-default.png), [light full](screenshots/gumclaw-light-full.png) |
| Help | `/help` | [dark default](screenshots/help-dark-default.png), [light default](screenshots/help-light-default.png), [light full](screenshots/help-light-full.png) |
| Terms | `/terms` | [light default](screenshots/terms-light-default.png), [light full](screenshots/terms-light-full.png) |
| Log in | `/login` | [dark default](screenshots/login-dark-default.png), [light default](screenshots/login-light-default.png), [light full](screenshots/login-light-full.png) |
| Sign up | `/signup` | [dark default](screenshots/signup-dark-default.png), [light default](screenshots/signup-light-default.png) |
| Product page | `ichigo.gumroad.com/l/ichigo-reader` | [light checkout](screenshots/product-light-checkout.png), [light default](screenshots/product-light-default.png), [light full](screenshots/product-light-full.png), [light share](screenshots/product-light-share.png) |
| Creator profile | `ichigo.gumroad.com` | [light default](screenshots/creator-light-default.png), [light full](screenshots/creator-light-full.png) |
| Landing, phone | `/` | [light default](screenshots/mobile-home-light-default.png), [light full](screenshots/mobile-home-light-full.png), [light menu](screenshots/mobile-home-light-menu.png) |
| Discover, phone | `/discover` | [light default](screenshots/mobile-discover-light-default.png), [light full](screenshots/mobile-discover-light-full.png) |
| Log in, phone | `/login` | [light default](screenshots/mobile-login-light-default.png), [light full](screenshots/mobile-login-light-full.png) |
| Product page, phone | `ichigo.gumroad.com/l/ichigo-reader` | [light default](screenshots/mobile-product-light-default.png), [light full](screenshots/mobile-product-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Featured-products carousel | Discover | the pager's own next arrow — an unlabelled 24px SVG button beside the '1 / 8' counter; the slide it advanced to was captured, no slide link followed | [discover-light-carousel](screenshots/discover-light-carousel.png), [discover-pager-arrow](#carousel-pager-arrow) |
| Mobile nav menu | landing, phone width | the header menu button's own press — the nav panel opened, captured and closed | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-nav-menu-button](#menu-button) |
| Share popover | product page | the product's own 'Share' button — the popover opened and was captured; none of its share targets was followed | [product-light-share](screenshots/product-light-share.png), [product-share](#share-button--popover) |
| Billing term | product page | the tier card's own term select — switched to Yearly, captured, switched back to Monthly | [product-term-select](#billing-term-select) |
| Checkout | product page → gumroad.com/checkout | the product page's own 'Subscribe' link target, opened as navigation — the last step of the pass; the form was captured empty and never submitted | [product-light-checkout](screenshots/product-light-checkout.png), [checkout-summary](#order-summary-card) |
| Dark theme | every gumroad.com page | `prefers-color-scheme: dark` emulation — the product's own media-query theme; the painted surface was verified before each shot | [home-dark-default](screenshots/home-dark-default.png), [nav-bar](#header-bar) |
| Signed-in surfaces | gumroad.com dashboard, buyer library | behind login — the capture was signed out; never reached | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 11 components were given a real keyboard focus. 10 draw an outline ring: `nav-start-selling` (1px auto #101010, offset 1px), `nav-category` (1px auto #101010, offset 1px), `discover-card` (on a child: 1px auto rgb(16, 16, 16) offset 1px), `discover-load-more` (1px auto #101010, offset 0px), `home-search-button` (1px auto #101010, offset 0px), `login-oauth` (1px auto #101010, offset 0px), `login-submit` (1px auto #101010, offset 0px), `product-term-select` (2px solid #36a9ae, offset 0px), `product-buy` (1px auto #101010, offset 1px), `checkout-country` (2px solid #36a9ae, offset 0px). The other 1 show no measured change: `discover-pager-arrow`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, rotate, scale, transform, translate | checkout-gift-toggle, discover-card, discover-featured-card, discover-load-more, login-oauth, login-submit, m-discover-card, nav-category and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Featured product card](#featured-product-card) | 704 x 380 | 1px solid #000000 `light.role.border` | 4px | #ffffff `light.role.background` | none | 0 |
| [Product card (market grid)](#product-card-market-grid) | 301.33 x 522.33 | 1px solid #000000 `light.role.border` | 4px | #ffffff `light.role.background` | none | 0 |
| [Hero section](#hero-section) | 1440 x 776 | - | - | #f4f4f0 `light.ground.bodyBg` | none | 0 |
| [Login form card](#login-form-card) | 736 x 738 | - | - | transparent | none | 0 |
| [Tier option (radio)](#tier-option-radio) | 331.34 x 100 | 1px solid #36a9ae | 4px | #ffffff `light.role.background` | #36a9ae 0px 0px 0px 1px | 12px 16px |
| [Order summary card](#order-summary-card) | 832 x 567 | - | - | transparent | none | 0 |
| [Product card, phone](#product-card-phone) | 234 x 498 | 1px solid #000000 `light.role.border` | 4px | #ffffff `light.role.background` | none | 0 |

## Components

### Site chrome

The header every gumroad.com page carries: the GUMROAD wordmark, the marketplace search field, 'Log in' and the black 'Start selling' button, and the category pill row under it.

#### Header bar
The hero header over Discover: wordmark, search, the auth buttons and the category nav. Read as `nav-bar` on the Discover page.
States read on 2026-11-17T07:51:44.585Z (default); 2026-11-17T07:52:02.965Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 217; padding 32px 64px; border B: 1px solid #000000 `light.role.border`; background #f4f4f0 `light.ground.bodyBg`; text ABC Favorit 16/22 400, #000000 `light.role.border`; icon 20 x 20, #000000 `light.role.border` |
| dark | border B: 1px solid rgba(221, 221, 221, 0.35); background #242423 `core.color.scale.darkGray`; text ABC Favorit 16/22 400, #dddddd; icon 20 x 20, #dddddd |

![Header bar default](components/crops/nav-bar-default.png) ![Header bar dark](components/crops/nav-bar-dark.png)

#### Wordmark link
The GUMROAD wordmark, uppercased display type, linking home. Read as `nav-logo` on the Discover page.
States read on 2026-11-17T07:52:04.910Z (default); 2026-11-17T07:52:07.148Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 245 x 46.86; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; layers span.inline-block.aspect-115/22 245.0x46.9 rgb(0, 0, 0) |

Child layers that carry the look: span 245x46.9 background #000000 `light.role.border`.

![Wordmark link default](components/crops/nav-logo-default.png) ![Wordmark link hover](components/crops/nav-logo-hover.png)

#### Search combobox
The "Search products" field — a combobox that opens a suggestion menu; "focused" is the field clicked into, nothing typed. Read as `nav-search` on the Discover page.
States read on 2026-11-17T07:52:08.382Z (default); 2026-11-17T07:52:10.419Z (focused); 2026-11-17T07:52:12.466Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 789 x 46; padding 12px 16px; radius 4px; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; placeholder rgba(0, 0, 0, 0.5) `light.role.muted`; layers up1 div.inline-flex.items-center rgb(255, 255, 255); input.font-[inherit].py-3 789.0x46.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 4px |
| focused | layers up1 div.inline-flex.items-center rgb(255, 255, 255) 2px solid rgb(255, 144, 232); input.font-[inherit].py-3 789.0x46.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 4px |
| dark | text ABC Favorit 16/22 400, #dddddd; placeholder rgba(221, 221, 221, 0.5); layers up1 div.inline-flex.items-center rgb(0, 0, 0); input.font-[inherit].py-3 789.0x46.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 4px |

![Search combobox default](components/crops/nav-search-default.png) ![Search combobox focused](components/crops/nav-search-focused.png) ![Search combobox dark](components/crops/nav-search-dark.png)

#### "Log in" button
The bordered auth button beside the primary CTA. Read as `nav-login` on the Discover page.
States read on 2026-11-17T07:52:13.336Z (focus-visible); 2026-11-17T07:52:14.803Z (default); 2026-11-17T07:52:21.535Z (hover). `focus-visible` failed at capture (keyboard focus never reached the target — focus-visible state not measurable).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | shadow #000000 4px 4px 0px 0px; layers ::after rgba(0, 0, 0, 0) 0px none 1 |

!["Log in" button default](components/crops/nav-login-default.png) !["Log in" button hover](components/crops/nav-login-hover.png)

#### "Start selling" button
The filled primary auth CTA — primary background, contrast-primary text. Read as `nav-start-selling` on the Discover page.
States read on 2026-11-17T07:52:27.533Z (default); 2026-11-17T07:52:29.548Z (hover); 2026-11-17T07:52:34.787Z (focus-visible); 2026-11-17T07:52:38.771Z (pressed); 2026-11-17T07:52:53.835Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #000000 `light.role.border`; text ABC Favorit 16/22 400, #ffffff `light.role.background`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #ff90e8 `light.role.accent`; shadow #000000 4px 4px 0px 0px; text ABC Favorit 16/22 400, #000000 `light.role.border`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #ff90e8 `light.role.accent`; text ABC Favorit 16/22 400, #000000 `light.role.border`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| dark | border 1px solid rgba(221, 221, 221, 0.35); background #dddddd; text ABC Favorit 16/22 400, #000000 `light.role.border` |

!["Start selling" button default](components/crops/nav-start-selling-default.png) !["Start selling" button hover](components/crops/nav-start-selling-hover.png) !["Start selling" button focus-visible](components/crops/nav-start-selling-focus-visible.png) !["Start selling" button pressed](components/crops/nav-start-selling-pressed.png) !["Start selling" button dark](components/crops/nav-start-selling-dark.png)

#### Category nav link
A link in the categories nav ("Design") — underlined text links on the header bar. Read as `nav-category` on the Discover page.
States read on 2026-11-17T07:53:00.963Z (default); 2026-11-17T07:53:10.073Z (hover); 2026-11-17T07:53:33.508Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76 x 40; padding 8px 12px; border 1px solid transparent; radius 3.35544e+07px; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #000000 `light.role.border`; background #ffffff `light.role.background`; shadow #000000 4px 4px 0px 0px; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #101010, offset 1px |

![Category nav link default](components/crops/nav-category-default.png) ![Category nav link hover](components/crops/nav-category-hover.png) ![Category nav link focus-visible](components/crops/nav-category-focus-visible.png)

#### Category nav link, current
"All" — the current category, painted with the active marker. Read as `nav-category-active` on the Discover page.
Read on 2026-11-17T07:53:35.208Z.

**Values (default).** size 45 x 40; padding 8px 12px; border 1px solid #000000 `light.role.border`; radius 3.35544e+07px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Category nav link, current default](components/crops/nav-category-active-default.png)

### Site chrome (mobile)

The 390px header: the wordmark and the menu button that opens the phone's nav panel.

#### Mobile header
The header at 390px: wordmark, search and the menu button. Read as `m-nav-bar` on the Discover page.
Read on 2026-11-17T08:00:24.165Z.

**Values (default).** size 390 x 243.86; padding 32px 16px; border B: 1px solid #000000 `light.role.border`; background #f4f4f0 `light.ground.bodyBg`; text ABC Favorit 16/22 400, #000000 `light.role.border`; icon 20 x 20, #000000 `light.role.border`.

![Mobile header default](components/crops/m-nav-bar-default.png)

#### Menu button
The button that opens the mobile nav panel. Read as `m-nav-menu-button` on the Discover page.
States read on 2026-11-17T08:00:28.623Z (default); 2026-11-17T08:00:34.071Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 24 x 24; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; icon 24 x 24, #000000 `light.role.border` |

![Menu button default](components/crops/m-nav-menu-button-default.png) ![Menu button hover](components/crops/m-nav-menu-button-hover.png)

### Discover

The marketplace grid page: the featured-product carousel with its unlabelled pager arrows, the trending/best-sellers tabs, the tag filters, product cards (cover, title, rating, price flag), 'Load more' and the currency selector.

#### Featured product card
A large card in the Featured products carousel: cover, title, blurb, creator, rating and the price flag. Read as `discover-featured-card` on the Discover page.
States read on 2026-11-17T07:53:36.550Z (default); 2026-11-17T07:53:41.827Z (hover); 2026-11-17T07:53:47.183Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 704 x 380; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 20/26 400, #000000 `light.role.border`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #000000 `light.role.border` |
| hover | shadow #000000 4px 4px 0px 0px |
| dark | border 1px solid rgba(221, 221, 221, 0.35); background #000000 `light.role.border`; text ABC Favorit 20/26 400, #dddddd; icon 20 x 20, #dddddd |

![Featured product card default](components/crops/discover-featured-card-default.png) ![Featured product card hover](components/crops/discover-featured-card-hover.png) ![Featured product card dark](components/crops/discover-featured-card-dark.png)

#### Carousel pager arrow
The small square arrow button beside the "1 / 8" counter in the Featured header. Read as `discover-pager-arrow` on the Discover page.
States read on 2026-11-17T07:54:05.902Z (default); 2026-11-17T07:54:07.853Z (hover); 2026-11-17T07:54:09.296Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 24 x 24; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; icon 24 x 24, #000000 `light.role.border` |

![Carousel pager arrow default](components/crops/discover-pager-arrow-default.png) ![Carousel pager arrow hover](components/crops/discover-pager-arrow-hover.png) ![Carousel pager arrow focus-visible](components/crops/discover-pager-arrow-focus-visible.png)

#### Product card (market grid)
A card in the "On the market" grid: cover block, title, creator, rating row and the price cell in the footer. Read as `discover-card` on the Discover page.
States read on 2026-11-17T07:54:11.573Z (default); 2026-11-17T07:54:13.783Z (hover); 2026-11-17T07:54:16.611Z (focus-visible); 2026-11-17T07:54:19.069Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 301.33 x 522.33; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 20/28 400, #000000 `light.role.border`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #000000 `light.role.border` |
| hover | shadow #000000 4px 4px 0px 0px |
| dark | border 1px solid rgba(221, 221, 221, 0.35); background #000000 `light.role.border`; text ABC Favorit 20/28 400, #dddddd; icon 20 x 20, #dddddd |

![Product card (market grid) default](components/crops/discover-card-default.png) ![Product card (market grid) hover](components/crops/discover-card-hover.png) ![Product card (market grid) focus-visible](components/crops/discover-card-focus-visible.png) ![Product card (market grid) dark](components/crops/discover-card-dark.png)

#### Price flag
The price cell in a card footer — the accent flag tag ("SGD 47.67"). Read as `discover-card-price` on the Discover page.
States read on 2026-11-17T07:54:25.081Z (default); 2026-11-17T07:54:27.442Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: dark) | size 102 x 30; padding 4px 8px; background #ff90e8 `light.role.accent`; text ABC Favorit 16/22 400, #000000 `light.role.border` |

![Price flag default](components/crops/discover-card-price-default.png) ![Price flag dark](components/crops/discover-card-price-dark.png)

#### Rating stars row
The star rating in a card footer ("5.0 (6)"). Read as `discover-card-rating` on the Discover page.
Read on 2026-11-17T07:54:29.507Z.

**Values (default).** size 24 x 22; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`.

![Rating stars row default](components/crops/discover-card-rating-default.png)

#### Market tab
A tab in the market switcher ("Trending" / "Best Sellers" / "Hot & New") — a bordered pill link. Read as `discover-tab` on the Discover page.
States read on 2026-11-17T07:54:29.516Z (focus-visible); 2026-11-17T07:54:30.455Z (default); 2026-11-17T07:54:33.347Z (hover). `focus-visible` failed at capture (keyboard focus never reached the target — focus-visible state not measurable).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 114 x 40; padding 8px 12px; border 1px solid transparent; radius 3.35544e+07px; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border` |
| hover | border 1px solid #000000 `light.role.border` |

![Market tab default](components/crops/discover-tab-default.png) ![Market tab hover](components/crops/discover-tab-hover.png)

#### Market tab, selected
"Trending" — the selected tab, filled with the inverted colours. Read as `discover-tab-active` on the Discover page.
States read on 2026-11-17T07:54:37.982Z (default); 2026-11-17T07:55:12.180Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91 x 40; padding 8px 12px; border 1px solid #000000 `light.role.border`; radius 3.35544e+07px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border` |
| dark | border 1px solid rgba(221, 221, 221, 0.35); background #000000 `light.role.border`; text ABC Favorit 16/22 400, #dddddd |

![Market tab, selected default](components/crops/discover-tab-active-default.png) ![Market tab, selected dark](components/crops/discover-tab-active-dark.png)

#### Filters disclosure
The "Filters" details/summary panel — "opened" is its own disclosure press. Read as `discover-filters` on the Discover page.
States read on 2026-11-17T07:55:13.963Z (default); 2026-11-17T07:55:17.556Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 310 x 55; padding 16px; border B: 1px solid #000000 `light.role.border`; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; icon 20 x 20, #000000 `light.role.border`; layers up1 div.grid.divide-y rgb(255, 255, 255); details.flex-wrap.items-center 310.0x55.0 B:1px solid; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 rgb(255, 144, 232) T:1px solid / R:1px solid / B:1px solid / L:1px solid 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 8px; input.appearance-none.size-[cal |
| opened | size 310 x 277; layers up1 div.grid.divide-y rgb(255, 255, 255); details.flex-wrap.items-center 310.0x277.0 B:1px solid; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 rgb(255, 144, 232) T:1px solid / R:1px solid / B:1px solid / L:1px solid 8px; input.appearance-none.size-[calc(1lh+0.125rem)] 24.0x24.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 8px; input.appearance-none.size-[ca |

Child layers that carry the look: details 310x55 border 1px solid; input 24x24 background #ff90e8 `light.role.accent` border 1px solid radius 8px; input 24x24 background #ffffff `light.role.background` border 1px solid radius 8px.

![Filters disclosure default](components/crops/discover-filters-default.png) ![Filters disclosure opened](components/crops/discover-filters-opened.png)

#### Filter checkbox
A checkbox row inside the open Filters panel (the square box with the tick). Read as `discover-filter-checkbox` on the Discover page.
States read on 2026-11-17T07:55:24.015Z (default); 2026-11-17T07:55:26.837Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 24 x 24; border 1px solid #000000 `light.role.border`; radius 8px; background #ff90e8 `light.role.accent`; text Arial 16/22 400, #545454; opacity 0.3; placeholder #545454 |

![Filter checkbox default](components/crops/discover-filter-checkbox-default.png) ![Filter checkbox hover](components/crops/discover-filter-checkbox-hover.png)

#### "Load more" button
The bordered pagination button under the market grid. Read as `discover-load-more` on the Discover page.
States read on 2026-11-17T07:55:26.847Z (pressed); 2026-11-17T07:55:29.805Z (default); 2026-11-17T07:55:38.025Z (hover); 2026-11-17T07:55:41.313Z (focus-visible). `pressed` failed at capture (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | shadow #000000 4px 4px 0px 0px; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #101010, offset 0px |

!["Load more" button default](components/crops/discover-load-more-default.png) !["Load more" button hover](components/crops/discover-load-more-hover.png) !["Load more" button focus-visible](components/crops/discover-load-more-focus-visible.png)

#### Currency select
The currency picker at the foot of the page ("$ (US Dollars)"). Read as `discover-currency-select` on the Discover page.
States read on 2026-11-17T07:55:50.677Z (default); 2026-11-17T07:55:55.802Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 338 x 48; padding 12px 44px 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border` |

![Currency select default](components/crops/discover-currency-select-default.png) ![Currency select hover](components/crops/discover-currency-select-hover.png)

### Discover (mobile)

The product card as the Discover grid draws it at 390 wide.

#### Product card, phone
A market-grid card at 390px — the grid collapses to a single column. Read as `m-discover-card` on the Discover page.
Read on 2026-11-17T08:00:38.894Z.

**Values (default).** size 234 x 498; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 20/26 400, #000000 `light.role.border`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #000000 `light.role.border`.

![Product card, phone default](components/crops/m-discover-card-default.png)

### Home

The landing page hero: the 'Go from 0 to $1' display heading, the marketplace search and the footer email-capture form — measured, never submitted.

#### Hero section
The landing hero ("Go from 0 to $1") — display heading over the brand illustration. Read as `home-hero` on the landing page.
States read on 2026-11-17T07:56:30.470Z (default); 2026-11-17T07:56:32.742Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 776; background #f4f4f0 `light.ground.bodyBg`; text ABC Favorit 96/96 400, #000000 `light.role.border`; icon 24 x 24, #242423 `core.color.scale.darkGray`; layers up1 div.bg-gray.dark:bg-black rgb(244, 244, 240) |
| dark | background #000000 `light.role.border`; text ABC Favorit 96/96 400, #ffffff `light.role.background`; icon 24 x 24, oklab(0.999994 0.0000455677 0.0000200868 / 0.7); layers up1 div.bg-gray.dark:bg-black rgb(0, 0, 0) |

![Hero section default](components/crops/home-hero-default.png) ![Hero section dark](components/crops/home-hero-dark.png)

#### Hero heading
The display headline in ABC Favorit. Read as `home-h1` on the landing page.
States read on 2026-11-17T07:56:34.647Z (default); 2026-11-17T07:56:36.550Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 672.02 x 96; background transparent; text ABC Favorit 96/96 400, #000000 `light.role.border` |
| dark | text ABC Favorit 96/96 400, #ffffff `light.role.background` |

![Hero heading default](components/crops/home-h1-default.png) ![Hero heading dark](components/crops/home-h1-dark.png)

#### Marketplace search field
The hero's "Search marketplace" input with its own search button. Read as `home-search` on the landing page.
States read on 2026-11-17T07:56:47.373Z (default); 2026-11-17T07:56:58.649Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 64; padding 0px 80px 0px 32px; border 1px solid #242423 `core.color.scale.darkGray`; radius 4px; background #f4f4f0 `light.ground.bodyBg`; text ABC Favorit 20/28 400, #000000 `light.role.border`; placeholder #757575 |
| focused | shadow #ff90e8 0px 0px 0px 2px |

![Marketplace search field default](components/crops/home-search-default.png) ![Marketplace search field focused](components/crops/home-search-focused.png)

#### Search button
The square button attached to the hero search field. Read as `home-search-button` on the landing page.
States read on 2026-11-17T07:57:01.797Z (default); 2026-11-17T07:57:03.670Z (hover); 2026-11-17T07:57:06.480Z (focus-visible); 2026-11-17T07:57:17.371Z (pressed).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 42 x 42; padding 8px; border 1px solid #242423 `core.color.scale.darkGray`; radius 6px; background #ffffff `light.role.background`; text Arial 13.33/normal 400, #000000 `light.role.border`; icon 24 x 24, #242423 `core.color.scale.darkGray` |
| focus-visible | outline 1px auto #101010, offset 0px |

![Search button default](components/crops/home-search-button-default.png) ![Search button hover](components/crops/home-search-button-hover.png) ![Search button focus-visible](components/crops/home-search-button-focus-visible.png) ![Search button pressed](components/crops/home-search-button-pressed.png)

#### Email capture field
The footer email field of the "subscribe" form. Read as `home-subscribe-input` on the landing page.
Read on 2026-11-17T07:57:18.517Z.

**Values (default).** size 560.41 x 48; padding 0px 16px; border 1px solid oklab(0.999994 0.0000455678 0.0000200868 / 0.3); radius 4px; background transparent; text ABC Favorit 16/24 400, #ffffff `light.role.background`; placeholder oklab(0.999994 0.0000455678 0.0000200868 / 0.5).

![Email capture field default](components/crops/home-subscribe-input-default.png)

#### Page footer
The footer strip with the link columns. Read as `home-footer` on the landing page.

Not on the page when it was captured.

#### Subscribe form
The email capture form row at the foot of the landing page — the field plus its arrow submit. Read as `home-subscribe-form` on the landing page.
States read on 2026-11-17T07:57:19.418Z (default); 2026-11-17T07:57:26.049Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: dark) | size 630.41 x 48; background transparent; text Arial 16/24 400, #000000 `light.role.border`; layers input.w-full.h-12 560.4x48.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; div.absolute.inset-0 66.0x48.0 rgb(241, 243, 51) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; div.absolute.inset-0 66.0x48.0 rgb(220, 52, 30) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; button.relative.inline-flex 66.0x48.0 rgb(255, 144, 232) T:1px solid / R:1px solid / B:1px solid  |

Child layers that carry the look: input 560.4x48 border 1px solid radius 4px; div 66x48 background #f1f333 `light.role.yellow` border 1px solid radius 4px; div 66x48 background #dc341e `light.role.danger` border 1px solid radius 4px.

![Subscribe form default](components/crops/home-subscribe-form-default.png) ![Subscribe form dark](components/crops/home-subscribe-form-dark.png)

### Auth

The log-in card: OAuth buttons (Apple, Google, X, Stripe), the email and password fields, submit and the 'Forgot your password?' link — measured, never filled or sent.

#### Login form card
The centred card: OAuth buttons, the divider, the email/password fieldset and the submit. Read as `login-card` on the log in page.
States read on 2026-11-17T07:58:03.349Z (default); 2026-11-17T07:58:06.110Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: dark) | size 736 x 738; background transparent; text ABC Favorit 16/22 400, #ffffff `light.role.background`; icon 20 x 20, #ffffff `light.role.background`; layers button.inline-flex.items-center 736.0x48.0 rgb(0, 0, 0) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; button.inline-flex.items-center 736.0x48.0 rgb(83, 131, 236) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; button.inline-flex.items-center 736.0x48.0 rgb(0, 0, 0) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; button.inline-flex.items-center 736.0x48.0 rgb(98, |

Child layers that carry the look: button 736x48 background #000000 `light.role.border` border 1px solid radius 4px; button 736x48 background #5383ec border 1px solid radius 4px; button 736x48 background #000000 `light.role.border` border 1px solid radius 4px.

![Login form card default](components/crops/login-card-default.png) ![Login form card dark](components/crops/login-card-dark.png)

#### OAuth button
An identity-provider button ("Apple" / "Google" / "X" / "Stripe") — full-width bordered. Read as `login-oauth` on the log in page.
States read on 2026-11-17T07:58:07.825Z (default); 2026-11-17T07:58:11.199Z (hover); 2026-11-17T07:58:12.550Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 736 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #000000 `light.role.border`; text ABC Favorit 16/22 400, #ffffff `light.role.background`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #ffffff `light.role.background` |
| hover | shadow #000000 4px 4px 0px 0px; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #101010, offset 0px |

![OAuth button default](components/crops/login-oauth-default.png) ![OAuth button hover](components/crops/login-oauth-hover.png) ![OAuth button focus-visible](components/crops/login-oauth-focus-visible.png)

#### Email input
The labelled email field — measured, never typed into. Read as `login-email` on the log in page.
States read on 2026-11-17T07:58:13.557Z (default); 2026-11-17T07:58:14.918Z (focused); 2026-11-17T07:58:17.658Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 736 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border`; placeholder #000000 `light.role.border` |
| focused | outline 2px solid #ff90e8 `light.role.accent`, offset 0px |
| dark | border 1px solid rgba(221, 221, 221, 0.35); background #000000 `light.role.border`; text ABC Favorit 16/22 400, #dddddd; placeholder #dddddd |

![Email input default](components/crops/login-email-default.png) ![Email input focused](components/crops/login-email-focused.png) ![Email input dark](components/crops/login-email-dark.png)

#### Password input
The password field with its "Show password" eye button. Read as `login-password` on the log in page.
Read on 2026-11-17T07:58:44.458Z.

**Values (default).** size 702 x 46; padding 12px 16px; radius 4px; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; placeholder #000000 `light.role.border`; layers up1 div.inline-flex.items-center rgb(255, 255, 255); input.font-[inherit].py-3 702.0x46.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 4px.

![Password input default](components/crops/login-password-default.png)

#### "Login" button
The filled submit — measured and hovered only, never pressed for real. Read as `login-submit` on the log in page.
States read on 2026-11-17T07:58:51.300Z (default); 2026-11-17T07:58:56.758Z (hover); 2026-11-17T07:59:13.098Z (focus-visible); 2026-11-17T07:59:34.367Z (pressed); 2026-11-17T07:59:36.165Z (dark).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 736 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #000000 `light.role.border`; text ABC Favorit 16/22 400, #ffffff `light.role.background`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #ff90e8 `light.role.accent`; shadow #000000 4px 4px 0px 0px; text ABC Favorit 16/22 400, #000000 `light.role.border`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #101010, offset 0px |
| dark | border 1px solid rgba(221, 221, 221, 0.35); background #dddddd; text ABC Favorit 16/22 400, #000000 `light.role.border` |

!["Login" button default](components/crops/login-submit-default.png) !["Login" button hover](components/crops/login-submit-hover.png) !["Login" button focus-visible](components/crops/login-submit-focus-visible.png) !["Login" button pressed](components/crops/login-submit-pressed.png) !["Login" button dark](components/crops/login-submit-dark.png)

#### "Forgot your password?" link
The muted recovery link inside the password fieldset. Read as `login-forgot` on the log in page.
States read on 2026-11-17T07:59:38.016Z (default); 2026-11-17T07:59:40.327Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 168 x 22; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border` |

!["Forgot your password?" link default](components/crops/login-forgot-default.png) !["Forgot your password?" link hover](components/crops/login-forgot-hover.png)

### Product page

A product page on a creator subdomain (ichigo.gumroad.com): the title block, the membership tier card, the billing-term select, the 'Subscribe' buy button, wishlist and share, the ratings/review rail and the 'Powered by Gumroad' footer.

#### Product header
The title block over the buy panel on a <creator>.gumroad.com/l/ page. Read as `product-header` on the https://ichigo.gumroad.com/l/ichigo-reader page.
Read on 2026-11-17T07:15:03.764Z.

**Values (default).** size 758.66 x 96; padding 24px; border R: 1px solid #000000 `light.role.border`; background transparent; text ABC Favorit 40/48 400, #000000 `light.role.border`; layers up1 article.relative.grid rgb(255, 255, 255); header.grid.gap-4 758.7x96.0 R:1px solid.

Child layers that carry the look: header 758.7x96 border 1px solid.

![Product header default](components/crops/product-header-default.png)

#### Tier option (radio)
A priced tier card — a radio-style button carrying the price and tier emoji label. Read as `product-tier` on the https://ichigo.gumroad.com/l/ichigo-reader page.
States read on 2026-11-17T07:15:26.844Z (default); 2026-11-17T07:15:50.164Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 331.34 x 100; padding 12px 16px; border 1px solid #36a9ae; radius 4px; background #ffffff `light.role.background`; shadow #36a9ae 0px 0px 0px 1px; text ABC Favorit 16/22 400, #000000 `light.role.border`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | shadow #36a9ae 0px 0px 0px 1px, #000000 4px 4px 0px 0px; layers ::after rgba(0, 0, 0, 0) 0px none 1 |

![Tier option (radio) default](components/crops/product-tier-default.png) ![Tier option (radio) hover](components/crops/product-tier-hover.png)

#### Billing term select
The "Monthly | Yearly" select in the buy controls. Read as `product-term-select` on the https://ichigo.gumroad.com/l/ichigo-reader page.
States read on 2026-11-17T07:15:51.294Z (default); 2026-11-17T07:15:53.243Z (hover); 2026-11-17T07:16:02.205Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 331.34 x 48; padding 12px 44px 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border` |
| focus-visible | outline 2px solid #36a9ae, offset 0px |

![Billing term select default](components/crops/product-term-select-default.png) ![Billing term select hover](components/crops/product-term-select-hover.png) ![Billing term select focus-visible](components/crops/product-term-select-focus-visible.png)

#### Purchase link
The "Subscribe"/"I want this" link that navigates to gumroad.com/checkout — measured, never followed in this run. Read as `product-buy` on the https://ichigo.gumroad.com/l/ichigo-reader page.
States read on 2026-11-17T07:16:05.372Z (pressed); 2026-11-17T07:16:08.204Z (default); 2026-11-17T07:16:13.726Z (hover); 2026-11-17T07:16:18.851Z (focus-visible). `pressed` failed at capture (cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 109 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #36a9ae; text ABC Favorit 16/22 400, #000000 `light.role.border`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto #101010, offset 1px |

![Purchase link default](components/crops/product-buy-default.png) ![Purchase link hover](components/crops/product-buy-hover.png) ![Purchase link focus-visible](components/crops/product-buy-focus-visible.png)

#### "Add to wishlist" control
The combobox-shaped wishlist picker beside the purchase link. Read as `product-wishlist` on the https://ichigo.gumroad.com/l/ichigo-reader page.
States read on 2026-11-17T07:16:21.741Z (default); 2026-11-17T07:16:25.608Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 219.34 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border`; icon 20 x 20, #000000 `light.role.border` |

!["Add to wishlist" control default](components/crops/product-wishlist-default.png) !["Add to wishlist" control hover](components/crops/product-wishlist-hover.png)

#### "Share" button + popover
The Share button; "opened" is its own popover state. Read as `product-share` on the https://ichigo.gumroad.com/l/ichigo-reader page.
States read on 2026-11-17T07:16:29.120Z (default); 2026-11-17T07:16:31.933Z (hover); 2026-11-17T07:16:37.894Z (opened).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 104 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; transition transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #000000 `light.role.border` |
| hover | shadow #000000 4px 4px 0px 0px; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| opened | layers ::after rgba(0, 0, 0, 0) 0px none 1 |

!["Share" button + popover default](components/crops/product-share-default.png) !["Share" button + popover hover](components/crops/product-share-hover.png) !["Share" button + popover opened](components/crops/product-share-opened.png)

#### Ratings + reviews
The ratings column beside the buy panel — the 4.1 summary, the star histogram and the review feed under it. Read as `product-ratings` on the https://ichigo.gumroad.com/l/ichigo-reader page.
Read on 2026-11-17T07:16:40.889Z.

**Values (default).** size 379.34 x 1783.3; padding 24px; border T: 1px solid #000000 `light.role.border`; background transparent; text ABC Favorit 18.4/25.3 400, #000000 `light.role.border`; icon 20 x 20, #000000 `light.role.border`.

![Ratings + reviews default](components/crops/product-ratings-default.png)

#### "Load more" reviews
The underlined reviews pagination button. Read as `product-review-load` on the https://ichigo.gumroad.com/l/ichigo-reader page.
States read on 2026-11-17T07:16:41.824Z (default); 2026-11-17T07:16:43.642Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 331.34 x 22; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border` |

!["Load more" reviews default](components/crops/product-review-load-default.png) !["Load more" reviews hover](components/crops/product-review-load-hover.png)

#### "Powered by Gumroad" footer
The slim footer under the product page — the brand link and currency select. Read as `product-footer` on the https://ichigo.gumroad.com/l/ichigo-reader page.
Read on 2026-11-17T07:16:44.659Z.

**Values (default).** size 1440 x 176; padding 64px 16px; background transparent; text ABC Favorit 16/22 400, #000000 `light.role.border`; icon 20 x 20, rgba(0, 0, 0, 0.5) `light.role.muted`; layers span.inline-block.aspect-115/22 115.0x22.0 rgb(0, 0, 0); select.font-[inherit].py-3 338.0x48.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px.

Child layers that carry the look: span 115x22 background #000000 `light.role.border`; select 338x48 background #ffffff `light.role.background` border 1px solid radius 4px.

!["Powered by Gumroad" footer default](components/crops/product-footer-default.png)

### Checkout

The public checkout the product page's 'Subscribe' link targets — gumroad.com/checkout with the product's option key: the order summary, gift toggle, email/name/country/currency fields and the pay methods. Fields were measured empty; nothing was filled or submitted.

#### Order summary card
The cart block: item thumbnail with quantity badge, Edit/Remove, the "Give as a gift?" toggle and the totals. Read as `checkout-summary` on the https://gumroad.com/checkout page.
Read on 2026-11-17T07:19:09.049Z.

**Values (default).** size 832 x 567; background transparent; text ABC Favorit 12/16 400, #ffffff `light.role.background`; icon 20 x 20, rgba(0, 0, 0, 0.5) `light.role.muted`; layers div.rounded-sm.border 832.0x257.0 rgb(255, 255, 255) T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; figure.tailwind-override.overflow-hidden 120.0x120.0 T:1px solid / R:1px solid / B:1px solid / L:1px solid 4px; div.absolute.top-0 24.0x24.0 rgb(0, 0, 0) T:1px solid / R:1px solid / B:1px solid / L:1px solid 3.35544e+07px; button.inline-flex.items-center 60.0x32.0 T:1px solid / R:1px sol.

Child layers that carry the look: div 832x257 background #ffffff `light.role.background` border 1px solid radius 4px; figure 120x120 border 1px solid radius 4px; div 24x24 background #000000 `light.role.border` border 1px solid radius 3.35544e+07px.

![Order summary card default](components/crops/checkout-summary-default.png)

#### "Give as a gift?" switch
The iOS-style switch — measured, never toggled. Read as `checkout-gift-toggle` on the https://gumroad.com/checkout page.
States read on 2026-11-17T07:19:11.285Z (default); 2026-11-17T07:19:13.162Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 34 x 20; border 1px solid #000000 `light.role.border`; radius 3.35544e+07px; background #ffffff `light.role.background`; text Arial 13.33/normal 400, #000000 `light.role.border`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder #000000 `light.role.border`; layers ::after rgb(0, 0, 0) 0px none 1 |

!["Give as a gift?" switch default](components/crops/checkout-gift-toggle-default.png) !["Give as a gift?" switch hover](components/crops/checkout-gift-toggle-hover.png)

#### Email field
The labelled Email address input — measured as found, never typed into. Read as `checkout-email` on the https://gumroad.com/checkout page.
States read on 2026-11-17T07:19:14.472Z (default); 2026-11-17T07:19:18.784Z (focused).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 374 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border`; placeholder #000000 `light.role.border` |
| focused | outline 2px solid #36a9ae, offset 0px |

![Email field default](components/crops/checkout-email-default.png) ![Email field focused](components/crops/checkout-email-focused.png)

#### Full name field
The labelled Full name input. Read as `checkout-name` on the https://gumroad.com/checkout page.
Read on 2026-11-17T07:19:19.949Z.

**Values (default).** size 374 x 48; padding 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border`; placeholder #000000 `light.role.border`.

![Full name field default](components/crops/checkout-name-default.png)

#### Country select
The country picker, pre-detected to the visitor's region. Read as `checkout-country` on the https://gumroad.com/checkout page.
States read on 2026-11-17T07:19:24.228Z (default); 2026-11-17T07:19:29.449Z (hover); 2026-11-17T07:19:30.778Z (focus-visible).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 790 x 48; padding 12px 44px 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border` |
| focus-visible | outline 2px solid #36a9ae, offset 0px |

![Country select default](components/crops/checkout-country-default.png) ![Country select hover](components/crops/checkout-country-hover.png) ![Country select focus-visible](components/crops/checkout-country-focus-visible.png)

#### Currency select
The "SGD$ (Singapore Dollars) — detected" select in the totals column. Read as `checkout-currency` on the https://gumroad.com/checkout page.
Read on 2026-11-17T07:19:31.915Z.

**Values (default).** size 374 x 48; padding 12px 44px 12px 16px; border 1px solid #000000 `light.role.border`; radius 4px; background #ffffff `light.role.background`; text ABC Favorit 16/22 400, #000000 `light.role.border`.

![Currency select default](components/crops/checkout-currency-default.png)

#### Pay button
The filled pay submit at the foot of the payment column — measured, never pressed. Read as `checkout-pay` on the https://gumroad.com/checkout page.
States read on 2026-11-17T07:19:33.726Z (default); 2026-11-17T07:19:36.811Z (hover).

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 374 x 56; padding 16px; border 1px solid #000000 `light.role.border`; radius 4px; background transparent; text ABC Favorit 16/22 500, #000000 `light.role.border`; icon 20 x 20, #000000 `light.role.border` |

![Pay button default](components/crops/checkout-pay-default.png) ![Pay button hover](components/crops/checkout-pay-hover.png)

## Icons

34 distinct inline-SVG icons were collected from the live pages into [icons/](icons) by `tools/capture/icons.mjs`, indexed in [icons/INDEX.tsv](icons/INDEX.tsv): a file is named from `tools/capture/icon-names.tsv` where its geometry hash is listed, else the label or class of the control it sits in, else `icon-<hash>`; colour is kept as `currentColor` wherever it matched the text colour, so each icon recolours from CSS `color` the way it does on the site. The icons are the product's artwork — borrow the set's grammar (sizes, stroke-vs-fill, naming roles), never the artwork itself.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [visit-gumroad-on-github](icons/visit-gumroad-on-github-1b5fde90.svg) | 18x18 20x20 | 0 0 24 24 | fill | home; discover; category; features; pricing; about; terms; nav; dark | Visit Gumroad on GitHub / 4.5 (4) / 4.9 (1.4K) |
| [visit-gumroad-on-github](icons/visit-gumroad-on-github-405925f1.svg) | 20x20 | 0 0 98 96 | fill | home; features; pricing; about; terms; nav; dark | Visit Gumroad on GitHub |
| [icon-5a8f7800](icons/icon-5a8f7800.svg) | 33x25 | 0 0 33 25 | fill | home; features; pricing; about; terms; nav; dark |  |
| [icon-65fbd336](icons/icon-65fbd336.svg) | 14x25 | 0 0 14 25 | fill | home; features; pricing; about; terms; nav; dark |  |
| [icon-8a5f7c9e](icons/icon-8a5f7c9e.svg) | 25x25 | 0 0 25 25 | fill | home; features; pricing; about; terms; nav; dark |  |
| [icon-b69755a4](icons/icon-b69755a4.svg) | 24x25 | 0 0 24 25 | fill | home; features; pricing; about; terms; nav; dark |  |
| [icon-bb373c52](icons/icon-bb373c52.svg) | 24x24 | 0 0 1200 1227 | fill | home; features; pricing; about; terms; nav; dark |  |
| [search](icons/search.svg) | 24x24 | 0 0 24 24 | stroke | home; about; nav; dark | Search |
| [icon-9f754683](icons/icon-9f754683.svg) | 20x12 | 0 0 24 24 | fill | home; about; nav; dark |  |
| [github](icons/github.svg) | 16x16 | 0 0 16 16 | fill | home; about; nav; dark | GitHub |
| [check](icons/check.svg) | 24x24 |  | fill | home; about; nav; dark | Check |
| [show-password](icons/show-password.svg) | 24x24 |  | stroke | login; signup | Show password |
| [icon-13f8d2b5](icons/icon-13f8d2b5.svg) | 24x24 | 0 0 1200 1227 | fill | discover; category |  |
| [icon-232cd378](icons/icon-232cd378.svg) | 14x25 | 0 0 14 25 | fill | discover; category |  |
| [icon-3174f24f](icons/icon-3174f24f.svg) | 24x25 | 0 0 24 25 | fill | discover; category |  |
| [icon-49899297](icons/icon-49899297.svg) | 25x25 | 0 0 25 25 | fill | discover; category |  |
| [icon-4b5d9032](icons/icon-4b5d9032.svg) | 24x24 | 0 0 24 24 | fill | discover; category |  |
| [follow](icons/follow.svg) | 20x20 | 0 0 24 24 | fill | discover; category | Follow |
| [icon-7a6b334e](icons/icon-7a6b334e.svg) | 16x16 | 3.5 5 17 17 | fill | discover; category | Mads Hagbarth Damsbo Top creator / Mark N. Rogers, MBA Top c |
| [icon-95024b78](icons/icon-95024b78.svg) | 33x25 | 0 0 33 25 | fill | discover; category |  |
| [tags](icons/tags.svg) | 20x20 | 0 0 24 24 | fill | discover; category | Tags / Contains / Price |
| [icon-a64b3f5f](icons/icon-a64b3f5f.svg) | 20x20 | 0 0 24 24 | fill | discover; category |  |
| [icon-a9978225](icons/icon-a9978225.svg) | 24x24 | 0 0 24 24 | fill | discover; category |  |
| [icon-ac55fd95](icons/icon-ac55fd95.svg) | 20x20 | 0 0 24 24 | fill | discover; category |  |
| [google](icons/google.svg) | 20x20 | 0 0 24 24 | fill | login; signup | Google |
| [icon-b8d97b8d](icons/icon-b8d97b8d.svg) | 20x20 | 0 0 24 24 | fill | discover; category |  |
| [69-products](icons/69-products.svg) | 20x20 | 0 0 24 24 | fill | discover; category | 69 products / 554 products / 98 products |
| [993-followers](icons/993-followers.svg) | 20x20 | 0 0 24 24 | fill | discover; category | 993 followers / 2.4K followers / 746 followers |
| [more-categories](icons/more-categories.svg) | 20x20 | 0 0 24 24 | fill | discover; category | More Categories / $ (US Dollars) £ (British Pounds) € (Eur |
| [x](icons/x.svg) | 20x20 | 0 0 24 24 | fill | login; signup | X |
| [apple](icons/apple.svg) | 20x20 | 0 0 24 24 | fill | login | Apple |
| [icon-9708776e](icons/icon-9708776e.svg) | 48x48 | 0 0 32 32 | fill | pricing |  |
| [stripe](icons/stripe.svg) | 20x20 | 0 0 24 24 | fill | login | Stripe |
| [icon-ebc13bf4](icons/icon-ebc13bf4.svg) | 28x19 | 0 0 28 19 | fill | features |  |

## Gaps

### The blocked product surfaces

Every signed-in surface stays behind the login the way it should: the **seller dashboard** (products, sales, payouts, analytics), the **buyer library** and **settings** are post-login surfaces and were never reached. The capture was signed out end to end — no account was created, no login submitted.

### Pages

- **The seller dashboard and buyer library** — post-login surfaces, see above. The login/signup cards were measured as far as their fields; neither was submitted.
- **Other category pages** — the 17 sibling category routes share the Discover template; only /design was measured.
- **Other creators' product pages** — every <creator>.gumroad.com page runs the same template with a per-creator palette; one representative product page was captured.
- **The Help centre's inner articles** — the help landing was captured; article bodies share the marketing chrome.

### States

- **Pressed** was forced with DevTools on the controls that carry it, so a state a script adds on mousedown (if any) is missing.
- **Search was never run** — the marketplace search fields on the landing and Discover were measured empty; no query was submitted, so results states are uncaptured.
- **The billing-term select** was switched once (Monthly → Yearly → back); every option's own pricing was not enumerated.
- **The checkout form** was captured empty — email, name, country and currency fields measured without a keystroke; 'Pay' was never pressed, so payment and post-purchase screens are uncaptured.
- **The gift toggle** was measured at rest; its opened state (the recipient fields) is uncaptured.
- **The carousel** was advanced once; slides 2–8's content is uncaptured.

### Themes

gumroad.com declares `color-scheme: light dark` and repaints through `@media (prefers-color-scheme: dark)` — there is no in-page toggle, so OS-level colour-scheme emulation is the product's own theme mechanism. `light` is the painted default; `dark` states and `{page}-dark-*` shots were verified by the painted background (and `matchMedia`) after emulation. The product subdomain's inline styles pin a light palette over the shared sheet: product and creator pages do not repaint under dark emulation — recorded as observed behaviour (`product-light`/`product-dark` profiles in raw/css-vars.json), not a third token theme.

### Fonts

- **ABC Favorit** is the product face — `--font-family`, driving everything from the wordmark to form controls; code falls back to the system mono stack. The woff2 files are served from assets.gumroad.com, proprietary to Gumroad — declared and measured, not shipped. The style guide falls back to system sans.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The rendered brand strings on the captured pages (the wordmark and copy) are the product's published content.

### Content left out

- Product copy, prices, ratings and creator names are the product's content; only frames and components were measured. The captured checkout URL's product/option parameters are the public values the product page's own link carries.
