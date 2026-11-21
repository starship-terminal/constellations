# Blue Apron components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from blog.blueapron.com on 2026-11-21, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the search field was filled with sample text and cleared, never run. www.blueapron.com itself is edge-blocked for this client — see Gaps.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (43 components, 85 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (84 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme (the footer is a dark-bold section style). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Blog home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Recipes category | `/guides/category/Recipes` | [default](screenshots/category-light-default.png), [full](screenshots/category-light-full.png) |
| Guide article | `/guides/15-budget-friendly-quick-dinner-ideas-for-busy-weeknights` | [default](screenshots/article-light-default.png), [full](screenshots/article-light-full.png) |
| Membership/Autoship FAQ | `/guides/membership-autoship-faq` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Cart (empty) | `/cart` | [default](screenshots/cart-light-default.png), [full](screenshots/cart-light-full.png) |
| Blog home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Guide article, phone | `/guides/15-budget-friendly-quick-dinner-ideas-for-busy-weeknights` | [default](screenshots/mobile-article-light-default.png), [full](screenshots/mobile-article-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | every page, phone width | the burger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| Cookie banner | nowhere | disabled sitewide (isCookieBannerEnabled:false in the page config) | not present |
| Comments | article page | the site runs no comments on this template | specs recorded as missing |
| Article images | article page | this guide is text-only; no lede or inline image mounts | spec recorded as missing |
| www.blueapron.com | the shop, menu, sign-in and checkout | hard-blocked at the Cloudflare edge for this client (403 on every route, reproduced in curl, headless and headed Chromium and real Chrome) | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 15 components were given a real keyboard focus. 15 draw an outline ring: `announcement-close` (2px solid #ffffff `color.neutral.white`, offset -2px), `nav-link` (2px solid #000000 `color.neutral.ink`, offset 4px), `header-cta` (2px solid #000000 `color.neutral.ink`, offset 4px), `card-title` (on a child: 2px solid rgb(0, 0, 0) offset 4px), `card-category` (2px solid #000000 `color.neutral.ink`, offset 4px), `card-more` (2px solid #000000 `color.neutral.ink`, offset 4px), `pagination-link` (2px solid #000000 `color.neutral.ink`, offset 4px), `button-primary` (2px solid #000000 `color.neutral.ink`, offset 4px), `button-secondary` (2px solid #000000 `color.neutral.ink`, offset 4px), `body-link` (2px solid #000000 `color.neutral.ink`, offset 4px), `article-pager` (2px solid #000000 `color.neutral.ink`, offset 4px), `footer-link` (2px solid #2959e0 `color.brand.accent`, offset 4px), `social-icon` (2px solid #2959e0 `color.brand.accent`, offset 4px), `m-menu-button` (2px solid #000000 `color.neutral.ink`, offset 4px), `m-nav-item` (2px solid #000000 `color.neutral.ink`, offset 4px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): the secondary button takes its hover fill when pressed; links and the CTA stay put. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `linear` | background-color, color, opacity | button-primary, button-secondary, header-cta |
| 0.14s | `ease-in-out` | padding, transform | header, m-header |
| 0.17s | `ease-in-out` | background-color, opacity | social-icon |
| 0.2s | `ease-out` | background-image | search-field |
| 0.25s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity | m-nav-item |
| 0.3s | `ease-in-out` | background | header, m-header |
| 1s | `ease` | opacity | blog-card, cat-card, m-blog-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Blog card](#blog-card) | 392 x 766.41 | - | - | transparent | none | 0 |
| [Category card](#category-card) | 392 x 733.75 | - | - | transparent | none | 0 |
| [Mobile blog card](#mobile-blog-card) | 343 x 679.47 | - | - | transparent | none | 0 |
| [Cart page](#cart-page) | 1440 x 900 | - | - | #f2f0e5 `color.brand.cream` | none | 0 |
| [Article pager](#article-pager) | 662.41 x 73.47 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The navy announcement bar, the header with its wordmark, nav and pill CTA.

#### Announcement bar
The thin promo strip above the header; its close is a UI toggle, measured never pressed. Read as `announcement-bar` on the blog home page.

**Values (default).** size 1440 x 44.22; background transparent; text Almarai 14.27/21.40 700, #ffffff `color.neutral.white`; layers div.sqs-announcement-bar.yui3-widget 1440.0x44.2 rgb(0, 40, 86).

Child layers that carry the look: div 1440x44.2 background #002856 `color.brand.navy`.

![Announcement bar default](components/crops/announcement-bar-default.png)

#### Announcement close
Read as `announcement-close` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 39.95 x 39.67; background transparent; text Almarai 14.27/21.40 400, #ffffff `color.neutral.white`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 2px solid #ffffff `color.neutral.white`, offset -2px; layers ::after rgba(0, 0, 0, 0) 0px none 1; span.sqs-announcement-bar-close 40.0x39.7 2px solid rgb(255, 255, 255) offset -2px |

![Announcement close default](components/crops/announcement-close-default.png) ![Announcement close hover](components/crops/announcement-close-hover.png) ![Announcement close focus-visible](components/crops/announcement-close-focus-visible.png) ![Announcement close pressed](components/crops/announcement-close-pressed.png)

#### Header
The header bar: logo wordmark, nav, cart and the CTA. Read as `header` on the blog home page.

**Values (default).** size 1440 x 166.81; background transparent; text Almarai 14.27/21.40 700, #ffffff `color.neutral.white`; transition background 0.3s ease-in-out, padding 0.14s ease-in-out, transform 0.14s ease-in-out; layers div.sqs-announcement-bar.yui3-widget 1440.0x44.2 rgb(0, 40, 86); a.header-skip-link.sqs-button-element--primary 176.1x65.0 rgb(41, 89, 224) 300px; a 31.5x27.2; a.btn.btn--border 141.4x65.0 rgb(41, 89, 224) 300px; div.top-bun 0.0x0.0 rgb(0, 0, 0); div.patty 0.0x0.0 rgb(0, 0, 0).

Child layers that carry the look: div 1440x44.2 background #002856 `color.brand.navy`; a 176.1x65 background #2959e0 `color.brand.accent` radius 300px; a 31.5x27.2 image linear-gradient(#000000 `color.neutral.ink`, #000000 `color.neutral.ink`).

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the blog home page.

**Values (default).** size 232.81 x 50; background transparent; text Almarai 0/0 400, #000000 `color.neutral.ink`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A header nav item (Guides, the Blue Apron shop links). Read as `nav-link` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 31.45 x 27.19; padding 1.6px 0px; background transparent; image linear-gradient(#000000 `color.neutral.ink`, #000000 `color.neutral.ink`); text Almarai 16/24 400, #000000 `color.neutral.ink` |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Header CTA
The button in the header actions (join/shop); links off the blog host, measured and never followed. Read as `header-cta` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 141.44 x 65; padding 24px 35.2px; radius 300px; background #2959e0 `color.brand.accent`; text Almarai 16/normal 400, #ffffff `color.neutral.white`; transition opacity 0.1s linear |
| hover | opacity 0.8 |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px |
| pressed | opacity 0.8 |

![Header CTA default](components/crops/header-cta-default.png) ![Header CTA hover](components/crops/header-cta-hover.png) ![Header CTA focus-visible](components/crops/header-cta-focus-visible.png) ![Header CTA pressed](components/crops/header-cta-pressed.png)

#### Cart icon
The Squarespace commerce cart control (the cart stays empty). Read as `cart-icon` on the blog home page.

Not on the page when it was captured.

### Blog home and cards

The search field, the masonry blog cards and the pagination, plus the button blocks on the page.

#### Search field
The blog search input; focused and filled with sample text that was deleted, never submitted. Read as `search-field` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 434.28 x 43; padding 12px 12px 12px 45px; border 1px solid #aaaaaa `color.neutral.line`; background transparent; image url(…); text Almarai 16/normal 400, #000000 `color.neutral.ink`; transition background-image 0.2s ease-out; opacity 0.7; placeholder #666666 |
| focused, filled | outline 2px solid #000000 `color.neutral.ink`, offset 4px |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png) ![Search field filled](components/crops/search-field-filled.png)

#### Search button
The search submit; measured at rest, never pressed (it would run a search). Read as `search-button` on the blog home page.

Not on the page when it was captured.

#### Blog card
One post summary in the masonry list: image, categories, title, excerpt, meta. Read as `blog-card` on the blog home page.

**Values (default).** size 392 x 766.41; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`; transition opacity 1s ease; layers a::after.blog-more-link 68.0469pxx1px rgb(41, 89, 224).

Child layers that carry the look: a::after 68.0469pxx1px background #2959e0 `color.brand.accent`.

![Blog card default](components/crops/blog-card-default.png)

#### Card image
The post thumbnail frame. Read as `card-image` on the blog home page.

**Values (default).** size 392 x 456.55; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`.

![Card image default](components/crops/card-image-default.png)

#### Card title
The post title link; measured, never followed. Read as `card-title` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 352.8 x 132.23; background transparent; text Ovo 36.73/44.08 400, #2959e0 `color.brand.accent` |
| focus-visible | layers a 341.6x130.2 2px solid rgb(0, 0, 0) offset 4px |

![Card title default](components/crops/card-title-default.png) ![Card title hover](components/crops/card-title-hover.png) ![Card title focus-visible](components/crops/card-title-focus-visible.png) ![Card title pressed](components/crops/card-title-pressed.png)

#### Category link
A category link on the card meta row. Read as `card-category` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 54.91 x 17; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink` |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px; layers a.blog-categories 54.9x17.0 2px solid rgb(0, 0, 0) offset 4px |

![Category link default](components/crops/card-category-default.png) ![Category link hover](components/crops/card-category-hover.png) ![Category link focus-visible](components/crops/card-category-focus-visible.png) ![Category link pressed](components/crops/card-category-pressed.png)

#### Card excerpt
The summary paragraph under the title. Read as `card-excerpt` on the blog home page.

**Values (default).** size 352.8 x 96.22; background transparent; text Almarai 14.27/21.40 400, #000000 `color.neutral.ink`.

![Card excerpt default](components/crops/card-excerpt-default.png)

#### Read-more link
Read as `card-more` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 68.05 x 22.41; background transparent; text Almarai 14.27/21.40 400, #2959e0 `color.brand.accent`; layers ::after rgb(41, 89, 224) 0px none 1; a::after.blog-more-link 68.0469pxx1px rgb(41, 89, 224) |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px; layers ::after rgb(41, 89, 224) 0px none 1; a.blog-more-link 68.0x22.4 2px solid rgb(0, 0, 0) offset 4px; a::after.blog-more-link 68.0469pxx1px rgb(41, 89, 224) |

Child layers that carry the look: a::after 68.0469pxx1px background #2959e0 `color.brand.accent`.

![Read-more link default](components/crops/card-more-default.png) ![Read-more link hover](components/crops/card-more-hover.png) ![Read-more link focus-visible](components/crops/card-more-focus-visible.png) ![Read-more link pressed](components/crops/card-more-pressed.png)

#### Card meta
The date/author row under the excerpt. Read as `card-meta` on the blog home page.

**Values (default).** size 352.8 x 24; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`.

![Card meta default](components/crops/card-meta-default.png)

#### List pagination
The older/newer posts pager under the list. Read as `pagination` on the blog home page.

**Values (default).** size 1324.81 x 24; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`.

![List pagination default](components/crops/pagination-default.png)

#### Pagination link
Read as `pagination-link` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 662.41 x 24; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink` |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px; layers a 662.4x24.0 2px solid rgb(0, 0, 0) offset 4px |

![Pagination link default](components/crops/pagination-link-default.png) ![Pagination link hover](components/crops/pagination-link-hover.png) ![Pagination link focus-visible](components/crops/pagination-link-focus-visible.png) ![Pagination link pressed](components/crops/pagination-link-pressed.png)

#### Primary button
A primary Squarespace button block on the page. Read as `button-primary` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 176.11 x 65; padding 24px 35.2px; radius 300px; background #2959e0 `color.brand.accent`; text Almarai 16/normal 400, #ffffff `color.neutral.white`; transition opacity 0.1s linear |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px |
| pressed | opacity 0.8 |

![Primary button default](components/crops/button-primary-default.png) ![Primary button focus-visible](components/crops/button-primary-focus-visible.png) ![Primary button pressed](components/crops/button-primary-pressed.png)

#### Secondary button
A secondary (border) Squarespace button block. Read as `button-secondary` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 267.28 x 67.94; padding 0px 35.2px; border 1px solid #2959e0 `color.brand.accent`; radius 300px; background transparent; text Almarai 16/normal 400, #2959e0 `color.brand.accent`; transition background-color 0.1s linear, color 0.1s linear |
| hover | background #2959e0 `color.brand.accent`; text Almarai 16/normal 400, #ffffff `color.neutral.white` |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px |
| pressed | background #2959e0 `color.brand.accent`; text Almarai 16/normal 400, #ffffff `color.neutral.white` |

![Secondary button default](components/crops/button-secondary-default.png) ![Secondary button hover](components/crops/button-secondary-hover.png) ![Secondary button focus-visible](components/crops/button-secondary-focus-visible.png) ![Secondary button pressed](components/crops/button-secondary-pressed.png)

#### Content image
An image block inside a content section. Read as `content-image` on the blog home page.

**Values (default).** size 656.92 x 704.91; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`.

![Content image default](components/crops/content-image-default.png)

### Category list

The category listing pages.

#### Category heading
The Recipes category listing heading. Read as `cat-title` on the category list page.

**Values (default).** size 352.8 x 176.31; background transparent; text Ovo 36.73/44.08 400, #2959e0 `color.brand.accent`.

![Category heading default](components/crops/cat-title-default.png)

#### Category card
A post card on the category listing. Read as `cat-card` on the category list page.

**Values (default).** size 392 x 733.75; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`; transition opacity 1s ease; transform translate(933px, 0px); opacity 0.999848; layers a::after.blog-more-link 68.0469pxx1px rgb(41, 89, 224).

Child layers that carry the look: a::after 68.0469pxx1px background #2959e0 `color.brand.accent`.

![Category card default](components/crops/cat-card-default.png)

### Article page

A guide page: headline, meta, body and the older/newer pager.

#### Article title
The guide headline in Ivory. Read as `article-title` on the article page.

**Values (default).** size 662.41 x 244.22; background transparent; text Ovo 67.84/81.40 400, #2959e0 `color.brand.accent`.

![Article title default](components/crops/article-title-default.png)

#### Article meta
The author/date row under the title. Read as `article-meta` on the article page.

**Values (default).** size 662.41 x 24; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`.

![Article meta default](components/crops/article-meta-default.png)

#### Body paragraph
A body-text paragraph in the guide. Read as `article-body` on the article page.

**Values (default).** size 662.41 x 72; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`.

![Body paragraph default](components/crops/article-body-default.png)

#### Article image
The lede/inline image in the guide body. Read as `article-lede` on the article page.

Not on the page when it was captured.

#### Body link
An inline link inside body text; measured, never followed. Read as `body-link` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 266.91 x 17; background transparent; text Almarai 16/24 400, #2959e0 `color.brand.accent` |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px; layers a 266.9x17.0 2px solid rgb(0, 0, 0) offset 4px |

![Body link default](components/crops/body-link-default.png) ![Body link hover](components/crops/body-link-hover.png) ![Body link focus-visible](components/crops/body-link-focus-visible.png) ![Body link pressed](components/crops/body-link-pressed.png)

#### Article pager
The older/newer guide pager under the article. Read as `article-pager` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 662.41 x 73.47; background transparent; text Ovo 36.73/36.73 400, #000000 `color.neutral.ink`; icon 18 x 32, #000000 `color.neutral.ink` |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px; layers a.item-pagination-link.item-pagination-link--prev 662.4x73.5 2px solid rgb(0, 0, 0) offset 4px |

![Article pager default](components/crops/article-pager-default.png) ![Article pager hover](components/crops/article-pager-hover.png) ![Article pager focus-visible](components/crops/article-pager-focus-visible.png) ![Article pager pressed](components/crops/article-pager-pressed.png)

#### Comments toggle
The comments header; a UI toggle measured in all states. Read as `comments-toggle` on the article page.

Not on the page when it was captured.

#### Comments toggle, open
After its own toggle; the opened comments list shows in the crop of the comments area. Read as `comments-open` on the article page.

Not on the page when it was captured.

#### FAQ title
The membership/Autoship FAQ headline. Read as `faq-title` on the FAQ guide page.

**Values (default).** size 662.41 x 162.81; background transparent; text Ovo 67.84/81.40 400, #2959e0 `color.brand.accent`.

![FAQ title default](components/crops/faq-title-default.png)

#### FAQ heading
A question heading inside the FAQ body. Read as `faq-heading` on the FAQ guide page.

**Values (default).** size 662.41 x 41.97; background transparent; text Ivory 36.73/41.96 400, #2959e0 `color.brand.accent`.

![FAQ heading default](components/crops/faq-heading-default.png)

#### FAQ paragraph
Read as `faq-body` on the FAQ guide page.

**Values (default).** size 662.41 x 72; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`.

![FAQ paragraph default](components/crops/faq-body-default.png)

### Cart

The Squarespace commerce cart, empty.

#### Cart page
The Squarespace commerce cart, empty as this client sees it — nothing was ever added. Read as `cart-page` on the cart page.

**Values (default).** size 1440 x 900; background #f2f0e5 `color.brand.cream`; text Almarai 14.27/21.40 700, #ffffff `color.neutral.white`.

![Cart page default](components/crops/cart-page-default.png)

### Footer

The navy dark-bold footer: sitemap columns, social icons, legal.

#### Footer
The dark-bold footer sections: sitemap links, social icons, legal. Read as `footer` on the blog home page.

**Values (default).** size 1440 x 412.47; background transparent; text Almarai 16/24 400, #ffffff `color.neutral.white`; icon 40 x 40, #ffffff `color.neutral.white`; layers div.section-border 1440.0x412.5 rgb(0, 40, 86); div.section-background 1440.0x412.5 rgb(0, 40, 86); div.fluidImageOverlay 156.0x33.5 rgba(0, 0, 0, 0.5); button.background-pause-button 0.0x0.0 rgba(0, 0, 0, 0.5) 50%; button::before.background-pause-button 42pxx42px T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0) 50%; button::.

Child layers that carry the look: div 1440x412.5 background #002856 `color.brand.navy`; div 1440x412.5 background #002856 `color.brand.navy`; div 156x33.5 background rgba(0, 0, 0, 0.5).

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 39.3 x 24; background transparent; text Almarai 16/24 400, #ffffff `color.neutral.white` |
| focus-visible | outline 2px solid #2959e0 `color.brand.accent`, offset 4px; layers a 39.3x24.0 2px solid rgb(41, 89, 224) offset 4px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon
A social link icon in the footer. Read as `social-icon` on the blog home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 20 x 20; background transparent; text Almarai 16/24 400, #ffffff `color.neutral.white`; transition background-color 0.17s ease-in-out, opacity 0.17s ease-in-out; icon 40 x 40, #ffffff `color.neutral.white` |
| hover | opacity 0.8 |
| focus-visible | outline 2px solid #2959e0 `color.brand.accent`, offset 4px; layers a.sqs-svg-icon--wrapper.instagram-unauth 20.0x20.0 2px solid rgb(41, 89, 224) offset 4px |
| pressed | opacity 0.8 |

![Social icon default](components/crops/social-icon-default.png) ![Social icon hover](components/crops/social-icon-hover.png) ![Social icon focus-visible](components/crops/social-icon-focus-visible.png) ![Social icon pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu overlay open.

#### Mobile header
Read as `m-header` on the blog home page at 390 wide.

**Values (default).** size 390 x 143.56; background transparent; text Almarai 13/19.5 700, #ffffff `color.neutral.white`; transition background 0.3s ease-in-out, padding 0.14s ease-in-out, transform 0.14s ease-in-out; layers div.sqs-announcement-bar.yui3-widget 390.0x59.8 rgb(0, 40, 86); a.header-skip-link.sqs-button-element--primary 176.1x65.0 rgb(41, 89, 224) 300px; div::after.header-background.theme-bg--primary 343.219pxx37px rgba(0, 0, 0, 0.15) 0px 0px 10px 0px; a 0.0x0.0; a.btn.btn--border 0.0x0.0 rgb(41, 89, 224) 300px; div.top-bun 0.0x0.0 rgb(0, 0, 0).

Child layers that carry the look: div 390x59.8 background #002856 `color.brand.navy`; a 176.1x65 background #2959e0 `color.brand.accent` radius 300px; div::after 343.219pxx37px shadow rgba(0, 0, 0, 0.15) 0px 0px 10px 0px.

![Mobile header default](components/crops/m-header-default.png)

#### Burger button
The hamburger that opens the mobile menu. Read as `m-menu-button` on the blog home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 47 x 37; padding 1px 6px; background transparent; text Almarai 16/normal 400, #000000 `color.neutral.ink`; layers div.top-bun 35.0x1.0 rgb(0, 0, 0); div.patty 0.0x0.0 rgb(0, 0, 0); div.bottom-bun 35.0x1.0 rgb(0, 0, 0) |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px; layers button.header-burger-btn.burger 47.0x37.0 2px solid rgb(0, 0, 0) offset 4px; div.top-bun 35.0x1.0 rgb(0, 0, 0); div.patty 0.0x0.0 rgb(0, 0, 0); div.bottom-bun 35.0x1.0 rgb(0, 0, 0) |

Child layers that carry the look: div 35x1 background #000000 `color.neutral.ink`; div 0x0 background #000000 `color.neutral.ink`; div 35x1 background #000000 `color.neutral.ink`.

![Burger button default](components/crops/m-menu-button-default.png) ![Burger button hover](components/crops/m-menu-button-hover.png) ![Burger button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Burger button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The burger after its own toggle; the opened menu overlay shows in the crop of the whole menu panel. Read as `m-menu-open` on the blog home page at 390 wide.

**Values (opened).** size 47 x 37; padding 1px 6px; background transparent; text Almarai 16/normal 400, #000000 `color.neutral.ink`; layers div.top-bun 20.5x20.5 rgb(0, 0, 0); div.patty 0.0x0.0 rgb(0, 0, 0); div.bottom-bun 20.5x20.5 rgb(0, 0, 0).

Child layers that carry the look: div 20.5x20.5 background #000000 `color.neutral.ink`; div 0x0 background #000000 `color.neutral.ink`; div 20.5x20.5 background #000000 `color.neutral.ink`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav item
A nav link inside the opened menu overlay. Read as `m-nav-item` on the blog home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 65.14 x 33.16; background transparent; text Almarai 33.15/33.15 400, #000000 `color.neutral.ink`; transition opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid #000000 `color.neutral.ink`, offset 4px; layers a 65.1x33.2 2px solid rgb(0, 0, 0) offset 4px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile blog card
Read as `m-blog-card` on the blog home page at 390 wide.

**Values (default).** size 343 x 679.47; background transparent; text Almarai 16/24 400, #000000 `color.neutral.ink`; transition opacity 1s ease; opacity 0.575844; layers a::after.blog-more-link 71.4375pxx1px rgb(41, 89, 224).

Child layers that carry the look: a::after 71.4375pxx1px background #2959e0 `color.brand.accent`.

![Mobile blog card default](components/crops/m-blog-card-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (cart, search, social glyphs, the Blue Apron wordmark) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The Cloudflare edge block on www.blueapron.com

www.blueapron.com serves a Cloudflare "Sorry, you have been blocked" 403 on every route this client requests — home, /menu, /pages/*, /users/sign_in, robots.txt and sitemap.xml alike — reproduced with curl, headless Chromium, headed Chromium and the real Chrome channel. The egress address is a non-US residential IP and the shop is US-only; the block is at the edge, not a headless fingerprint a patch can clear. blog.blueapron.com (Squarespace) does not block, so it is the whole capturable surface: the package is Blue Apron's editorial surface, with the shop, sign-in and checkout recorded as a boundary, not measured.

### Pages

- **The shop front end.** blueapron.com, /menu, /membership, /autoship, /gifts, /cookbook, the sign-in and every page the header nav and CTAs point at are behind the edge block. Nothing there is public to this client and nothing was measured.
- **Comments.** The article template mounts no comments list on this site; the toggle specs are recorded as missing.
- **Article images.** The captured guide is text-only; the lede spec is recorded as missing.
- **Search results.** The field was focused and filled with sample text (deleted after); no query was ever run.
- **Cart checkout.** The cart was captured empty; nothing was added and the Squarespace checkout was never reached.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme; Squarespace ships ten section palettes (white/dark/black/bright and their -bold inverses, recorded in raw/css-vars.json) and the footer uses the dark-bold one. No user dark mode is offered.

### Fonts

- **Ovo** is the display face on headlines and card titles, configured in the site's heading vars and served from the Squarespace CDN.
- **Ivory** (custom.css @font-face) overrides h1-h4 in the body content.
- **Almarai** is the body/nav face. None is distributed with this package; the style guide falls back to system fonts.

### Screenshots

- Photography, the Blue Apron wordmark and the recipe content in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Recipe photography is the product's content; only the frames and components were measured.
