# Component measurements

Computed styles read from www.hitchd.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the mobile entries at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per measured part or state, a row per property. A cell that repeats the first column's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Chrome

#### marketing-nav

Marketing nav. the home header bar and its logo + Log In link

Page: https://www.hitchd.com/. Selector: `see tools/capture/public/measure.mjs`. States: header, logo, loginLink.

| Property | header | logo | loginLink |
|---|---|---|---|
| Size (w x h) | 1440 x 96 | 74 x 27.02 | 70 x 48 |
| Padding | 24px 56px | 0px | 12px 0px 12px 24px |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/normal 400 | Inter Variable 16px/24px 400 | Inter Variable 16px/24px 400 |
| Letter spacing | normal | = | = |
| Colour | #000000 | #2c2e2f | #ffffff |
| Text node | a.closure-login: Inter Variable 16px/24px 400, #ffffff | - | - |
| Transition | none | = | = |
| Ancestor paint | 1 up section.hero.home bg #2f2e1a | - | - |
| How |  |  |  |
| Cursor | - | pointer | pointer |

Crops: `nav.png`.

#### announcement-banner

Closure announcement banner. the full-width "Hitchd is closing on 31 December 2026" strip above the header

Page: https://www.hitchd.com/. Selector: `see tools/capture/public/measure.mjs`. States: banner, text.

| Property | banner | text |
|---|---|---|
| Size (w x h) | 1440 x 98 | 705 x 58 |
| Padding | 20px 24px | 0px |
| Border | none | = |
| Radius | 0px | = |
| Background | #f6f3ef | transparent |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111212 | #000000 |
| Text node | strong: Inter Variable 20px/30px 500, #111212 | = |
| Transition | none | = |
| Painted layers | div.top-banner 1440.0x98.0 bg #f6f3ef | - |
| How |  |  |
| Ancestor paint | - | 1 up div.top-banner bg #f6f3ef |

Crops: `announcement.png`.

#### marketing-footer

Footer. the marketing footer and its links (the closure home has no footer; read on the destination page)

Page: https://www.hitchd.com/trips/australia. Selector: `see tools/capture/public/measure.mjs`. States: footer, link.

| Property | footer | link |
|---|---|---|
| Size (w x h) | 1440 x 370 | 0 x 0 |
| Padding | 64px 24px 40px 24px | 0px |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff | transparent |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | Inter Variable 17px/22px 400 |
| Letter spacing | normal | = |
| Colour | #000000 | #111212 |
| Text node | span: Inter Variable 15px/26px 600, #000000, ls 0.36px | - |
| Transition | none | = |
| Painted layers | footer 1440.0x370.0 bg #ffffff; a 95.0x21.0 border B:1px solid #000000 @ 0; a 67.0x21.0 border B:1px solid #000000 @ 0; a 32.0x21.0 border B:1px solid #000000 @ 0; a 33.0x21.0 border B:1px solid #000000 @ 0; a 54.0x21.0 border B:1px solid #000000 @ 0 | - |
| How |  |  |
| Cursor | - | pointer |

Crops: `footer.png`.

#### registry-nav

Registry nav. the registry top bar, #hashtag link and Try It Free CTA

Page: https://www.hitchd.com/zoeandnoah. Selector: `see tools/capture/public/measure.mjs`. States: bar, cta, hashtag.

| Property | bar | cta | hashtag |
|---|---|---|---|
| Size (w x h) | 1440 x 80 | 117 x 40 | 137 x 28.39 |
| Padding | 0px | 0px 20px | = |
| Border | none | = | T: none; R: none; B: 2px solid #000000 @ 0; L: none |
| Radius | 0px | 100px | = |
| Background | #ffffff @ 0.92 | #111212 | transparent |
| Box shadow | #000000 @ 0.08 0px -1px 0px 0px | none | none |
| Backdrop filter | saturate(1.8) blur(20px) | - | - |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | Inter Variable 16px/40px 500 | Inter Variable 22px/26.4px 500 |
| Letter spacing | normal | = | = |
| Colour | #545759 | #ffffff | #ffffff |
| Text node | p.demo-reg-p: Inter Variable 17px/80px 500, #111212 | - | - |
| Transition | none | = | = |
| Painted layers | div.top-registry-sample-banner 1440.0x80.0 bg #ffffff @ 0.92 shadow #000000 @ 0.08 0px -1px 0px 0px; a.direct 117.0x40.0 bg #111212 r 100px | a.direct 117.0x40.0 bg #111212 r 100px | a.hashtag-link 137.0x28.4 border B:2px solid #000000 @ 0 |
| How |  |  |  |
| Cursor | - | pointer | pointer |

Crops: `registry-nav.png`.

### Type

#### hero

Hero heading. the home hero — "Tie the knot, without tangles." set in DDNR

Page: https://www.hitchd.com/. Selector: `see tools/capture/public/measure.mjs`. States: h1, lead.

| Property | h1 | lead |
|---|---|---|
| Size (w x h) | 576 x 184.78 | 576 x 114.17 |
| Padding | 0px | 26px 0px 0px 0px |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | DDNR 88px/92.4px 100 | Inter Variable 21px/29.4px 400 |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| How |  |  |

Crops: `hero.png`.

#### marketing-h2

Marketing H2. a section heading on the marketing surface (the closure home carries no h2, so this was read on the destination page)

Page: https://www.hitchd.com/trips/australia. Selector: `see tools/capture/public/measure.mjs`. States: h2.

| Property | h2 |
|---|---|
| Size (w x h) | 672 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 56px/60px 600 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How |  |

Crops: `h2.png`.

#### article-type

Article type. the blog post H1, body copy and inline link

Page: https://www.hitchd.com/blog/what-is-a-honeymoon-registry. Selector: `see tools/capture/public/measure.mjs`. States: h1, body, link.

| Property | h1 | body | link |
|---|---|---|---|
| Size (w x h) | 680 x 168 | 1208 x 54 | 45 x 17 |
| Padding | 48px 0px 0px 24px | 0px | 0px |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 56px/60.0001px 700 | Inter Variable 19px/27.0009px 400 | Inter Variable 14px/17.9998px 500 |
| Letter spacing | normal | = | = |
| Colour | #111212 | = | #6e6e73 |
| Transition | none | = | = |
| How |  |  |  |
| Cursor | - | = | pointer |

Crops: none.

#### prose-h2

Legal prose. a terms page heading and paragraph

Page: https://www.hitchd.com/terms. Selector: `see tools/capture/public/measure.mjs`. States: h2, body.

| Property | h2 | body |
|---|---|---|
| Size (w x h) | 118 x 36 | 700 x 24 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 32px/36px 600 | Inter Variable 16px/24px 400 |
| Letter spacing | normal | = |
| Colour | #000000 | #333333 |
| Transition | none | = |
| How |  |  |

Crops: none.

#### registry-hero

Registry hero. the demo registry heading and couple names

Page: https://www.hitchd.com/zoeandnoah. Selector: `see tools/capture/public/measure.mjs`. States: heading, names.

| Property | heading | names |
|---|---|---|
| Size (w x h) | 1392 x 192 | 685 x 173.95 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | classic 96px/96px 400 | Inter Variable 16px/24px 400 |
| Letter spacing | normal | = |
| Colour | #ffffff | #545759 |
| Transition | none | = |
| How |  |  |
| Text node | - | p: Inter Variable 22px/26.4px 400, #ffffff |
| Painted layers | - | a.hashtag-link 137.0x28.4 border B:2px solid #000000 @ 0 |

Crops: `registry-hero.png`.

### Cards

#### blog-card

Blog index card. a post row on /blog

Page: https://www.hitchd.com/blog. Selector: `see tools/capture/public/measure.mjs`. States: card, title.

| Property | card | title |
|---|---|---|
| Size (w x h) | 386.66 x 600 | 328.66 x 96 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | Inter Variable 26px/32px 600 |
| Letter spacing | normal | = |
| Colour | #000000 | #2c2e2f |
| Text node | h6.left: Inter Variable 15px/20px 400, #737373 | - |
| Transition | none | = |
| Painted layers | div.body 386.7x299.0 bg #ffffff; span 3.0x3.0 bg #737373 r 50%; a::after.primary 102pxx1px bg #000000 | - |
| How |  |  |
| Cursor | - | pointer |

Crops: `blog-card.png`.

#### gift-card

Gift card. a gift tile in the registry list

Page: https://www.hitchd.com/zoeandnoah. Selector: `see tools/capture/public/measure.mjs`. States: card, title, info.

| Property | card | title | info |
|---|---|---|---|
| Size (w x h) | 1416 x 472 | 616 x 40 | 708 x 472 |
| Padding | 0px | 0px 16px 0px 0px | 0px 12px 0px 80px |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 16px/24px 400 | Inter Variable 36px/40px 600 | = |
| Letter spacing | normal | = | = |
| Colour | #545759 | #111212 | = |
| Text node | span: Inter Variable 12px/24px 500, #ffffff | - | h3: Inter Variable 36px/40px 600, #111212 |
| Transition | none | = | = |
| ::before | 0px x 472px, static, bg #000000 @ 0, radius 0px | - | - |
| ::after | 0px x 472px, static, bg #000000 @ 0, radius 0px | - | - |
| Painted layers | div.small-12.medium-12 708.0x472.0 r 20px shadow #000000 @ 0.1 0px 0px 0px 1px inset; div.gift-featured-tag 123.0x28.0 image linear-gradient(#080c0c 0%, #0c1212 100%) border T:1px solid #080c0c / R:1px solid #080c0c / B:1px solid #080c0c / L:1px solid #080c0c r 50px shadow #000000 @ 0.1 0px 1px 2px 0px; div.view-gift 75.0x34.0 bg #ffffff r 50px shadow #111212 @ 0.12 0px 0px 0px 1px | - | div.view-gift 75.0x34.0 bg #ffffff r 50px shadow #111212 @ 0.12 0px 0px 0px 1px |
| How |  |  |  |
| Cursor | - | pointer | = |

Crops: `gift-card.png`.

#### mobile-gift-card

Gift card (mobile). a gift tile at 390 x 844

Page: https://www.hitchd.com/zoeandnoah. Selector: `see tools/capture/public/measure.mjs`. States: card.

| Property | card |
|---|---|
| Size (w x h) | 370 x 294.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #545759 |
| Text node | span: Inter Variable 12px/24px 500, #ffffff |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.small-12.medium-6 342.0x256.5 r 16px shadow #000000 @ 0.1 0px 0px 0px 1px inset; div.gift-featured-tag 123.0x28.0 image linear-gradient(#080c0c 0%, #0c1212 100%) border T:1px solid #080c0c / R:1px solid #080c0c / B:1px solid #080c0c / L:1px solid #080c0c r 50px shadow #000000 @ 0.1 0px 1px 2px 0px |
| How |  |

Crops: `mobile-gift-card.png`.

### Forms

#### auth-layout

Auth form card. the /login form container and heading, at rest

Page: https://www.hitchd.com/login. Selector: `see tools/capture/public/measure.mjs`. States: h1, card, page.

| Property | h1 | card | page |
|---|---|---|---|
| Size (w x h) | 450 x 32 | 450 x 437 | 1440 x 900 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | #ffffff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 28px/32px 600 | Inter Variable 16px/24px 400 | Inter Variable 16px/24px 400 |
| Letter spacing | normal | = | = |
| Colour | #111212 | #555555 | #545759 |
| Transition | none | = | = |
| How |  |  |  |
| Text node | - | label: Inter Variable 16px/20px 600, #111212 | h1: Inter Variable 28px/32px 600, #111212 |
| Painted layers | - | input 450.0x48.0 border T:1px solid #d2d2d7 / R:1px solid #d2d2d7 / B:1px solid #d2d2d7 / L:1px solid #d2d2d7 r 8px; a 125.0x21.0 border B:1px solid #000000 @ 0.12; input.pass 450.0x48.0 border T:1px solid #d2d2d7 / R:1px solid #d2d2d7 / B:1px solid #d2d2d7 / L:1px solid #d2d2d7 r 8px; button.primary.disabled 450.0x48.0 bg #cdcfd0 r 50px; h5 450.0x26.0 border B:1px solid #e7e8e9; span 54.0x19.0 bg #ffffff | body.non-mac 1440.0x900.0 bg #ffffff; div.modal-backdrop 0.0x0.0 bg #000000 @ 0.4; div.modal-core 0.0x0.0 bg #ffffff r 16px shadow #000000 @ 0.12 0px 20px 40px 0px; div.topheader 0.0x0.0 bg #ffffff border B:1px solid #000000 @ 0.1 r 16px 16px 0px 0px; div.reglink 0.0x0.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 8px; span 0.0x0.0 bg #ffffff r 4px shadow #111212 @ 0.16 0px 0px 0px 1px |
| Icon | - | = | 0 x 0, colour #2c2e2f |

Crops: `auth-card.png`.

#### auth-field

Auth text field. the email input and its label, at rest

Page: https://www.hitchd.com/login. Selector: `see tools/capture/public/measure.mjs`. States: input, label.

| Property | input | label |
|---|---|---|
| Size (w x h) | 450 x 48 | 40 x 20 |
| Padding | 0px 16px | 0px |
| Border | 1px solid #d2d2d7 | none |
| Radius | 8px | 0px |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 17px/24px 400 | Inter Variable 16px/20px 600 |
| Letter spacing | normal | = |
| Colour | #111212 | = |
| Transition | all 0.15s ease-in-out | none |
| Cursor | text | - |
| Placeholder | #111212, opacity 1 | - |
| Painted layers | input 450.0x48.0 border T:1px solid #d2d2d7 / R:1px solid #d2d2d7 / B:1px solid #d2d2d7 / L:1px solid #d2d2d7 r 8px | - |
| How |  |  |

Crops: none.

#### auth-button

Auth submit button. the Continue button in its disabled-at-rest state

Page: https://www.hitchd.com/login. Selector: `see tools/capture/public/measure.mjs`. States: button.

| Property | button |
|---|---|
| Size (w x h) | 450 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 50px |
| Background | #cdcfd0 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/48px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | all 0.15s ease-in-out |
| Cursor | not-allowed |
| Painted layers | button.primary.disabled 450.0x48.0 bg #cdcfd0 r 50px |
| How |  |

Crops: `auth-button.png`.

#### auth-link

Auth links. the forgot-password link and helper copy

Page: https://www.hitchd.com/login. Selector: `see tools/capture/public/measure.mjs`. States: link, muted.

| Property | link | muted |
|---|---|---|
| Size (w x h) | 125 x 21 | 450 x 21 |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.12; L: none | none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 14px/20px 500 | Inter Variable 14px/20px 400 |
| Letter spacing | normal | = |
| Colour | #111212 | #575a5d |
| Transition | all 0.15s ease-in-out | none |
| Cursor | pointer | - |
| Painted layers | a 125.0x21.0 border B:1px solid #000000 @ 0.12 | a 79.0x21.0 border B:1px solid #000000 @ 0.12 |
| How |  |  |

Crops: none.

### Controls

#### sort-filter

Sort filter. the "Sort by" select in the registry header

Page: https://www.hitchd.com/zoeandnoah. Selector: `see tools/capture/public/measure.mjs`. States: control, select.

| Property | control | select |
|---|---|---|
| Size (w x h) | 158 x 48 | 111 x 24 |
| Padding | 0px | 0px 24px 0px 0px |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | Inter Variable 15px/17.25px 500 |
| Letter spacing | normal | = |
| Colour | #545759 | #393c3c |
| Text node | span: Inter Variable 13px/20px 500, #96999c | - |
| Transition | none | = |
| Painted layers | option.selected 0.0x0.0 shadow #111212 0px 0px 0px 1.5px inset | = |
| How |  |  |
| Background image | - | url(…) |
| Cursor | - | pointer |

Crops: `sort-filter.png`.

#### mobile-menu

Mobile menu. the registry .mobile-menu drawer at 390px — it exists (with owner links) but no guest-facing control opens it, so it was measured hidden at rest

Page: https://www.hitchd.com/zoeandnoah. Selector: `see tools/capture/public/measure.mjs`. States: menu.

| Property | menu |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 12px 24px 24px 24px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/normal 400 |
| Letter spacing | normal |
| Colour | #545759 |
| Transition | all 0.15s ease-in |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Opacity | 0 |
| Icon | 24 x 24, colour #111212 |
| Painted layers | nav.show-for-small-only.mobile-menu 390.0x844.0 bg #ffffff; a 115.0x20.0 border B:1px solid #000000 @ 0.12; hr.new-div 342.0x1.0 border T:1px solid #000000 @ 0.08; hr.new-div 342.0x1.0 border T:1px solid #000000 @ 0.08; hr.new-div 342.0x1.0 border T:1px solid #000000 @ 0.08; hr.new-div 342.0x1.0 border T:1px solid #000000 @ 0.08 |
| How |  |

Crops: none.

### Dialogs

#### gift-modal

Gift modal. a gift card's modal, opened by its own tap and read at rest; the Give flow is never entered

Page: https://www.hitchd.com/zoeandnoah/<gift-slug>. Selector: `see tools/capture/public/measure.mjs`. States: modal, title, give, giveWrap.

| Property | modal | title | give | giveWrap |
|---|---|---|---|---|
| Size (w x h) | 1440 x 779.77 | 453.33 x 40.5 | 453.33 x 50 | 453.33 x 50 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | 100px |
| Background | #ffffff | transparent | transparent | #c5c8ca |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter Variable 16px/24px 400 | Inter Variable 36px/40.5px 600 | Inter Variable 17px/50px 500 | Inter Variable 17px/50px 500 |
| Letter spacing | normal | = | = | = |
| Colour | #545759 | #111212 | #ffffff | #ffffff |
| Text node | h1.gift-name-top.show-for-large-up: Inter Variable 36px/40.5px 600, #111212 | - | - | a: Inter Variable 17px/50px 500, #ffffff |
| Transition | none | = | = | all 0.15s ease-in-out |
| Icon | 32 x 32, colour #ffffff | - | - | - |
| Painted layers | div.modalDialog.container 1440.0x779.8 bg #ffffff; div.progress.medium-12 0.0x0.0 bg #ffffff; div.left-side-popup.columns 0.0x0.0 r 16px shadow #000000 @ 0.12 0px 0px 0px 1px inset; div.gift-featured-tag-gift 0.0x0.0 image linear-gradient(#080c0c 0%, #0c1212 100%) border T:1px solid #080c0c / R:1px solid #080c0c / B:1px solid #080c0c / L:1px solid #080c0c r 50px shadow #000000 @ 0.1 0px 1px 2px 0px; span.label 0.0x0.0 bg #008cba; div.left-side-popup.gift-intro-overlay 0.0x0.0 r 16px shadow #000000 @ 0.12 0px 0px 0px 1px inset | - | - | div.pay.disabled 453.3x50.0 bg #c5c8ca r 100px |
| How |  |  |  |  |
| Cursor | - | = | pointer | not-allowed |
| Ancestor paint | - | = | 1 up div.pay.disabled bg #c5c8ca | = |

Crops: `gift-modal.png`.

### Boundaries

#### internal-route-bounces

Registry internal routes. contributions / payment-methods / ask / quick-thanks each bounce the signed-out guest back to /

Page: https://www.hitchd.com/zoeandnoah. Selector: `see tools/capture/public/measure.mjs`. States: rest.

| Property | rest |
|---|---|
| Error | {"contributions":{"landedUrl":"https://www.hitchd.com/","bouncedToHome":true},"payment-methods":{"landedUrl":"https://www.hitchd.com/","bouncedToHome":true},"ask":{"landedUrl":"https://www.hitchd.com/","bouncedToHome":true},"quick-thanks":{"landedUrl":"https://www.hitchd.com/","bouncedToHome":true}} |

Crops: none.

## Transitions declared in the readable stylesheets

Hitchd's marketing CSS is same-origin and the Angular apps' styles mount as <style> blocks, so the CSSOM can read them; the per-state Transition rows above are computed values regardless.
