# Component measurements

Computed styles read from blog.blueapron.com on 2026-11-21 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (the footer paints a dark-bold section theme), with any promo popup hidden (never answered; the cookie banner is disabled sitewide), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### announcement-bar

Announcement bar. The thin promo strip above the header; its close is a UI toggle, measured never pressed.

Page: home. Selector: `.sqs-announcement-bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 44.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: Almarai 14.272px/21.408px 700, #ffffff |
| Transition | none |
| Painted layers | div.sqs-announcement-bar.yui3-widget 1440.0x44.2 bg #002856 |
| How | at rest |

Crops: `announcement-bar-default.png`.

#### announcement-close

Announcement close.

Page: home. Selector: `.sqs-announcement-bar-close`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.95 x 39.67 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset -2px | = |
| Font | Almarai 14.272px/21.408px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 39.9531px x 38.5312px, static, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | span.sqs-announcement-bar-close 40.0x39.7 outline 2px solid #ffffff offset -2px | = |

Crops: `announcement-close-default.png`, `announcement-close-hover.png`, `announcement-close-focus-visible.png`, `announcement-close-pressed.png`.

#### header

Header. The header bar: logo wordmark, nav, cart and the CTA.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 166.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: Almarai 14.272px/21.408px 700, #ffffff |
| Transition | background, padding, transform 0.3s, 0.14s, 0.14s ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0.14s |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.sqs-announcement-bar.yui3-widget 1440.0x44.2 bg #002856; a.header-skip-link.sqs-button-element--primary 176.1x65.0 bg #2959e0 r 300px; a 31.5x27.2 image linear-gradient(#000000, #000000); a.btn.btn--border 141.4x65.0 bg #2959e0 r 300px; div.top-bun 0.0x0.0 bg #000000; div.patty 0.0x0.0 bg #000000 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `.header-title-logo a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 232.81 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 0px/0px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A header nav item (Guides, the Blue Apron shop links).

Page: home. Selector: `.header-nav-item a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 31.45 x 27.19 | = | = | = |
| Padding | 1.6px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#000000, #000000) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 31.5x27.2 image linear-gradient(#000000, #000000) | = | a 31.5x27.2 image linear-gradient(#000000, #000000) outline 2px solid #000000 offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### header-cta

Header CTA. The button in the header actions (join/shop); links off the blog host, measured and never followed.

Page: home. Selector: `.header-actions-action--cta .btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 141.44 x 65 | = | = | = |
| Padding | 24px 35.2px | = | = | = |
| Border | none | = | = | = |
| Radius | 300px | = | = | = |
| Background | #2959e0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.1s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn--border 141.4x65.0 bg #2959e0 r 300px | = | a.btn.btn--border 141.4x65.0 bg #2959e0 r 300px outline 2px solid #000000 offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `header-cta-default.png`, `header-cta-hover.png`, `header-cta-focus-visible.png`, `header-cta-pressed.png`.

#### cart-icon

Cart icon. The Squarespace commerce cart control (the cart stays empty).

Page: home. Selector: `.floating-cart / .icon--cart`. States: .

Not found on the page at capture time.

### Blog home and cards

#### search-field

Search field. The blog search input; focused and filled with sample text that was deleted, never submitted.

Page: home. Selector: `.sqs-block-search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 434.28 x 43 | = | = |
| Padding | 12px 12px 12px 45px | = | = |
| Border | 1px solid #aaaaaa | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Background image | url(…) | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #000000 offset 4px | 2px solid #000000 offset 4px |
| Font | Almarai 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | background-image 0.2s ease-out | = | = |
| Opacity | 0.7 | = | = |
| Cursor | text | = | = |
| Placeholder | #666666, opacity 1 | = | = |
| Painted layers | input.search-input 434.3x43.0 border T:1px solid #aaaaaa / R:1px solid #aaaaaa / B:1px solid #aaaaaa / L:1px solid #aaaaaa | input.search-input 434.3x43.0 border T:1px solid #aaaaaa / R:1px solid #aaaaaa / B:1px solid #aaaaaa / L:1px solid #aaaaaa outline 2px solid #000000 offset 4px | input.search-input 434.3x43.0 border T:1px solid #aaaaaa / R:1px solid #aaaaaa / B:1px solid #aaaaaa / L:1px solid #aaaaaa outline 2px solid #000000 offset 4px |
| How | at rest | clicked into the field | typed "dinner ideas", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### search-button

Search button. The search submit; measured at rest, never pressed (it would run a search).

Page: home. Selector: `.sqs-block-search button`. States: .

Not found on the page at capture time.

#### blog-card

Blog card. One post summary in the masonry list: image, categories, title, excerpt, meta.

Page: home. Selector: `.blog-item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 392 x 766.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | time.blog-date: Almarai 16px/24px 400, #000000 |
| Transition | opacity 1s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | a::after.blog-more-link 68.0469pxx1px bg #2959e0 |
| How | at rest |

Crops: `blog-card-default.png`.

#### card-image

Card image. The post thumbnail frame.

Page: home. Selector: `.blog-item .blog-image-wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 392 x 456.55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `card-image-default.png`.

#### card-title

Card title. The post title link; measured, never followed.

Page: home. Selector: `.blog-item .blog-title`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 352.8 x 132.23 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Ovo 36.736px/44.0832px 400 | = | = | = |
| Letter spacing | -0.73472px | = | = | = |
| Colour | #2959e0 | = | = | = |
| Text node | a: Ovo 36.736px/44.0832px 400, #2959e0, ls -0.73472px | = | = | = |
| Transition | none | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 341.6x130.2 outline 2px solid #000000 offset 4px | = |

Crops: `card-title-default.png`, `card-title-hover.png`, `card-title-focus-visible.png`, `card-title-pressed.png`.

#### card-category

Category link. A category link on the card meta row.

Page: home. Selector: `.blog-categories a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 54.91 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.blog-categories 54.9x17.0 outline 2px solid #000000 offset 4px | = |

Crops: `card-category-default.png`, `card-category-hover.png`, `card-category-focus-visible.png`, `card-category-pressed.png`.

#### card-excerpt

Card excerpt. The summary paragraph under the title.

Page: home. Selector: `.blog-excerpt`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352.8 x 96.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 14.272px/21.408px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p: Almarai 14.272px/21.408px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `card-excerpt-default.png`.

#### card-more

Read-more link.

Page: home. Selector: `.blog-more-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.05 x 22.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 14.272px/21.408px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2959e0 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 68.0469px x 1px, static, bg #2959e0, radius 0px | = | = | = |
| Painted layers | a::after.blog-more-link 68.0469pxx1px bg #2959e0 | = | a.blog-more-link 68.0x22.4 outline 2px solid #000000 offset 4px; a::after.blog-more-link 68.0469pxx1px bg #2959e0 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-more-default.png`, `card-more-hover.png`, `card-more-focus-visible.png`, `card-more-pressed.png`.

#### card-meta

Card meta. The date/author row under the excerpt.

Page: home. Selector: `.blog-meta-section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352.8 x 24 |
| Padding | 0px |
| Gap | 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | time.blog-date: Almarai 16px/24px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `card-meta-default.png`.

#### pagination

List pagination. The older/newer posts pager under the list.

Page: home. Selector: `.blog-list-pagination`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1324.81 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.next-label: Almarai 16px/24px 400, #000000 |
| Transition | none |
| Icon | 0 x 0, colour #000000, fill #000000 @ 0 |
| How | at rest |

Crops: `pagination-default.png`.

#### pagination-link

Pagination link.

Page: home. Selector: `.blog-list-pagination a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 662.41 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.next-label: Almarai 16px/24px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #000000, fill #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 662.4x24.0 outline 2px solid #000000 offset 4px | = |

Crops: `pagination-link-default.png`, `pagination-link-hover.png`, `pagination-link-focus-visible.png`, `pagination-link-pressed.png`.

#### button-primary

Primary button. A primary Squarespace button block on the page.

Page: home. Selector: `.sqs-button-element--primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 176.11 x 65 | - | = | = |
| Padding | 24px 35.2px | - | = | = |
| Border | none | - | = | = |
| Radius | 300px | - | = | = |
| Background | #2959e0 | - | = | = |
| Box shadow | none | - | = | = |
| Outline | none | - | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/normal 400 | - | = | = |
| Letter spacing | normal | - | = | = |
| Colour | #ffffff | - | = | = |
| Transition | opacity 0.1s linear | - | = | = |
| Cursor | pointer | - | = | = |
| Painted layers | a.header-skip-link.sqs-button-element--primary 176.1x65.0 bg #2959e0 r 300px | - | a.header-skip-link.sqs-button-element--primary 176.1x65.0 bg #2959e0 r 300px outline 2px solid #000000 offset 4px | = |
| How | at rest | - | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is outside of the viewport Call log: [2m  - waiting for locator('.sqs-button-element--primary, a.sqs-block-button-element--primary').filter({ visible: true }).first().filter({  | = | = |
| Opacity | - | = | = | 0.8 |

Crops: `button-primary-default.png`, `button-primary-focus-visible.png`, `button-primary-pressed.png`.

#### button-secondary

Secondary button. A secondary (border) Squarespace button block.

Page: home. Selector: `.sqs-button-element--secondary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 267.28 x 67.94 | = | = | = |
| Padding | 0px 35.2px | = | = | = |
| Border | 1px solid #2959e0 | = | = | = |
| Radius | 300px | = | = | = |
| Background | transparent | #2959e0 | = | #2959e0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2959e0 | #ffffff | = | #ffffff |
| Transition | background-color, color 0.1s, 0.1s linear, linear delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.sqs-block-button-element--large.sqs-button-element--secondary 267.3x67.9 border T:1px solid #2959e0 / R:1px solid #2959e0 / B:1px solid #2959e0 / L:1px solid #2959e0 r 300px | a.sqs-block-button-element--large.sqs-button-element--secondary 267.3x67.9 bg #2959e0 border T:1px solid #2959e0 / R:1px solid #2959e0 / B:1px solid #2959e0 / L:1px solid #2959e0 r 300px | a.sqs-block-button-element--large.sqs-button-element--secondary 267.3x67.9 border T:1px solid #2959e0 / R:1px solid #2959e0 / B:1px solid #2959e0 / L:1px solid #2959e0 r 300px outline 2px solid #000000 offset 4px | a.sqs-block-button-element--large.sqs-button-element--secondary 267.3x67.9 bg #2959e0 border T:1px solid #2959e0 / R:1px solid #2959e0 / B:1px solid #2959e0 / L:1px solid #2959e0 r 300px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `button-secondary-default.png`, `button-secondary-hover.png`, `button-secondary-focus-visible.png`, `button-secondary-pressed.png`.

#### content-image

Content image. An image block inside a content section.

Page: home. Selector: `.sqs-block-image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.92 x 704.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `content-image-default.png`.

### Category list

#### cat-title

Category heading. The Recipes category listing heading.

Page: category. Selector: `h1/h2 on the category page`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352.8 x 176.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Ovo 36.736px/44.0832px 400 |
| Letter spacing | -0.73472px |
| Colour | #2959e0 |
| Text node | a: Ovo 36.736px/44.0832px 400, #2959e0, ls -0.73472px |
| Transition | none |
| How | at rest |

Crops: `cat-title-default.png`.

#### cat-card

Category card. A post card on the category listing.

Page: category. Selector: `.blog-item on /guides/category`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 392 x 733.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.blog-categories: Almarai 16px/24px 400, #000000 |
| Transition | opacity 1s ease |
| Transform | matrix(1, 0, 0, 1, 933, 0) |
| Opacity | 0.999848 |
| Painted layers | a::after.blog-more-link 68.0469pxx1px bg #2959e0 |
| How | at rest |

Crops: `cat-card-default.png`.

### Article page

#### article-title

Article title. The guide headline in Ivory.

Page: article. Selector: `h1.entry-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 662.41 x 244.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.entry-title.entry-title--large: Ovo 67.84px/81.408px 400, #2959e0, ls -1.3568px |
| Transition | none |
| How | at rest |

Crops: `article-title-default.png`.

#### article-meta

Article meta. The author/date row under the title.

Page: article. Selector: `.blog-item-meta-wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 662.41 x 24 |
| Padding | 0px |
| Gap | 11px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Almarai 16px/24px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `article-meta-default.png`.

#### article-body

Body paragraph. A body-text paragraph in the guide.

Page: article. Selector: `.blog-item-content p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 662.41 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `article-body-default.png`.

#### article-lede

Article image. The lede/inline image in the guide body.

Page: article. Selector: `.blog-item-content img`. States: .

Not found on the page at capture time.

#### body-link

Body link. An inline link inside body text; measured, never followed.

Page: article. Selector: `.blog-item-content p a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 266.91 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2959e0 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 266.9x17.0 outline 2px solid #000000 offset 4px | = |

Crops: `body-link-default.png`, `body-link-hover.png`, `body-link-focus-visible.png`, `body-link-pressed.png`.

#### article-pager

Article pager. The older/newer guide pager under the article.

Page: article. Selector: `.item-pagination-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 662.41 x 73.47 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h2.item-pagination-title: Ovo 36.736px/36.736px 400, #000000, ls -0.73472px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 32, colour #000000, fill #000000 @ 0 | = | = | = |
| Ancestor paint | 1 up section.item-pagination.item-pagination--prev-next bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.item-pagination-link.item-pagination-link--prev 662.4x73.5 outline 2px solid #000000 offset 4px | = |

Crops: `article-pager-default.png`, `article-pager-hover.png`, `article-pager-focus-visible.png`, `article-pager-pressed.png`.

#### comments-toggle

Comments toggle. The comments header; a UI toggle measured in all states.

Page: article. Selector: `.blog-item-comments-toggle-wrapper`. States: .

Not found on the page at capture time.

#### comments-open

Comments toggle, open. After its own toggle; the opened comments list shows in the crop of the comments area.

Page: article. Selector: `.blog-item-comments-toggle-wrapper`. States: .

Not found on the page at capture time.

#### faq-title

FAQ title. The membership/Autoship FAQ headline.

Page: faq. Selector: `h1 on the FAQ guide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 662.41 x 162.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.entry-title.entry-title--large: Ovo 67.84px/81.408px 400, #2959e0, ls -1.3568px |
| Transition | none |
| How | at rest |

Crops: `faq-title-default.png`.

#### faq-heading

FAQ heading. A question heading inside the FAQ body.

Page: faq. Selector: `.blog-item-content h2/h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 662.41 x 41.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Ivory 36.736px/41.9672px 400 |
| Letter spacing | -0.73472px |
| Colour | #2959e0 |
| Transition | none |
| How | at rest |

Crops: `faq-heading-default.png`.

#### faq-body

FAQ paragraph.

Page: faq. Selector: `.blog-item-content p on the FAQ guide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 662.41 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `faq-body-default.png`.

### Cart

#### cart-page

Cart page. The Squarespace commerce cart, empty as this client sees it — nothing was ever added.

Page: cart. Selector: `.Cart-inner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f2f0e5 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: Almarai 14.272px/21.408px 700, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | body.primary-button-style-solid.primary-button-shape-pill 1440.0x900.0 bg #f2f0e5; div.floating-cart.hidden 0.0x0.0 bg #2959e0; div.sqs-announcement-bar.yui3-widget 1440.0x44.2 bg #002856; a.header-skip-link.sqs-button-element--primary 176.1x65.0 bg #2959e0 r 300px; a.btn.btn--border 141.4x65.0 bg #2959e0 r 300px; div.top-bun 0.0x0.0 bg #000000 |
| How | at rest |

Crops: `cart-page-default.png`.

### Footer

#### footer

Footer. The dark-bold footer sections: sitemap links, social icons, legal.

Page: home. Selector: `footer#footer-sections`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 412.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p: Almarai 16px/24px 400, #ffffff |
| Transition | none |
| Icon | 40 x 40, colour #ffffff, fill #000000 @ 0 |
| Painted layers | div.section-border 1440.0x412.5 bg #002856; div.section-background 1440.0x412.5 bg #002856; div.fluidImageOverlay 156.0x33.5 bg #000000 @ 0.5; button.background-pause-button 0.0x0.0 bg #000000 @ 0.5 r 50%; button::before.background-pause-button 42pxx42px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 50%; button::after.background-pause-button 0pxx12px border L:10px double #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.3 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #2959e0 offset 4px | = |
| Font | Almarai 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2959e0 | = | = | = |
| Text node | span.sqsrte-text-color--white: Almarai 16px/24px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 39.3x24.0 outline 2px solid #2959e0 offset 4px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social icon. A social link icon in the footer.

Page: home. Selector: `.sqs-svg-icon--social`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #2959e0 offset 4px | = |
| Font | Almarai 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, opacity 0.17s, 0.17s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 40 x 40, colour #ffffff, fill #000000 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |
| Painted layers | - | = | a.sqs-svg-icon--wrapper.instagram-unauth 20.0x20.0 outline 2px solid #2959e0 offset 4px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 143.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: Almarai 13px/19.5px 700, #ffffff |
| Transition | background, padding, transform 0.3s, 0.14s, 0.14s ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0.14s |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.sqs-announcement-bar.yui3-widget 390.0x59.8 bg #002856; a.header-skip-link.sqs-button-element--primary 176.1x65.0 bg #2959e0 r 300px; div::after.header-background.theme-bg--primary 343.219pxx37px shadow #000000 @ 0.15 0px 0px 10px 0px; a 0.0x0.0 image linear-gradient(#000000, #000000); a.btn.btn--border 0.0x0.0 bg #2959e0 r 300px; div.top-bun 0.0x0.0 bg #000000 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Burger button. The hamburger that opens the mobile menu.

Page: mobile. Selector: `.header-burger-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47 x 37 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.top-bun 35.0x1.0 bg #000000; div.patty 0.0x0.0 bg #000000; div.bottom-bun 35.0x1.0 bg #000000 | = | button.header-burger-btn.burger 47.0x37.0 outline 2px solid #000000 offset 4px; div.top-bun 35.0x1.0 bg #000000; div.patty 0.0x0.0 bg #000000; div.bottom-bun 35.0x1.0 bg #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The burger after its own toggle; the opened menu overlay shows in the crop of the whole menu panel.

Page: mobile. Selector: `.header-burger-btn`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 47 x 37 |
| Padding | 1px 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.top-bun 20.5x20.5 bg #000000; div.patty 0.0x0.0 bg #000000; div.bottom-bun 20.5x20.5 bg #000000 |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-item

Mobile nav item. A nav link inside the opened menu overlay.

Page: mobile. Selector: `.header-menu-nav-item a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.14 x 33.16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 4px | = |
| Font | Almarai 33.15px/33.15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.header-menu-nav-item-content: Almarai 33.15px/33.15px 400, #000000 | = | = | = |
| Transition | opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 65.1x33.2 outline 2px solid #000000 offset 4px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-blog-card

Mobile blog card.

Page: mobile. Selector: `.blog-item at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 343 x 679.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Almarai 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | time.blog-date: Almarai 16px/24px 400, #000000 |
| Transition | opacity 1s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Opacity | 0.575844 |
| Painted layers | a::after.blog-more-link 71.4375pxx1px bg #2959e0 |
| How | at rest |

Crops: `m-blog-card-default.png`.

## Transitions declared in the readable stylesheets

blog.blueapron.com serves its Squarespace sheets cross-origin, so this list holds what the CSSOM could read on each page (cross-origin sheets stay unreadable there); the per-state Transition rows above are computed values and cover every rule the page paints.

- article: none

- category: none

- home: none
