# Component measurements

Computed styles read from www.dopper.com and shop.dopper.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the marketing home, /en/mission/story, /en/products/insulated, /en/blog/just-refill and the storefront's /, /bottles, /dopper-original-pacific-blue, /checkout/cart/ and /customer/account/login/ — with the Cookiebot consent dialog hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The transparent-then-solid top bar (the DOPPER-NAVIGATION custom element): flyout triggers (Bottle / Travel Mug / Tap / Mission / Get Involved), the dopper. wordmark, right links (Impact report / Find a Store / For Businesses / EN) and the bag button.

Page: home. Selector: `dopper-navigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 110 |
| Padding | 0px 70px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Gilroy 16px/20.8px 700, #0c1a37 |
| Transition | none |
| Icon | 12 x 8, colour #0c1a37 |
| Painted layers | ul.languagePopup.hidden 0.0x0.0 bg #fcfaf2 r 20px shadow #000000 @ 0.1 0px 4px 20px 0px; button.menuToggle 0.0x0.0 bg #efefef r 50% |
| Ancestor paint | 1 up nav.dopper-nav bg #fcfaf2 @ 0.95 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The dopper. wordmark anchor (svg, centred in the bar).

Page: home. Selector: `dopper-navigation a svg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 200 x 47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/16px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Icon | 200 x 45, colour #0000ee |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Bottle flyout trigger in the header; toggled, never followed.

Page: home. Selector: `dopper-navigation button Bottle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.16 x 20.8 | = | - | - |
| Padding | 0px | = | - | - |
| Gap | 12px | = | - | - |
| Border | none | = | - | - |
| Radius | 0px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Gilroy 16px/20.8px 700 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #000f2e | #0067e5 | - | - |
| Text node | span: Gilroy 16px/20.8px 700, #000f2e | span: Gilroy 16px/20.8px 700, #0067e5 | - | - |
| Transition | color 0.3s ease | = | - | - |
| Icon | 12 x 8, colour #000f2e | 12.9 x 9.43, colour #0067e5 | - | - |
| How | at rest | mouse hover | - | - |
| Cursor | - | pointer | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Error | - | = | = | cdpSession.send: Protocol error (CSS.forcePseudoState): Could not find node with given id |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`.

#### nav-link

Nav link. A right-side header link (Impact report).

Page: home. Selector: `dopper-navigation a Impact report`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.91 x 20.8 | = | - | - |
| Padding | 0px | = | - | - |
| Gap | 12px | = | - | - |
| Border | none | = | - | - |
| Radius | 0px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Gilroy 16px/20.8px 500 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #000f2e | #0067e5 | - | - |
| Text node | span: Gilroy 16px/20.8px 500, #000f2e | span: Gilroy 16px/20.8px 500, #0067e5 | - | - |
| Transition | color 0.3s ease | = | - | - |
| Cursor | pointer | = | - | - |
| How | at rest | mouse hover | - | - |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |
| Error | - | = | = | cdpSession.send: Protocol error (CSS.forcePseudoState): Could not find node with given id |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`.

#### bag-button

Bag button. The shopping-bag icon button, right end of the header (light-blue circle); links to the cart, never followed.

Page: home. Selector: `dopper-navigation a[href*=cart]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60 x 62 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 60.0x62.0 outline 1px auto #005fcc offset 1px | = |

Crops: `bag-button-default.png`, `bag-button-hover.png`, `bag-button-focus-visible.png`, `bag-button-pressed.png`.

#### flyout

Mega-menu. The yellow Bottle flyout (tab pills across the top, feature columns, CTAs and a product photo).

Page: home. Selector: `opened Bottle menu`. States: default.

Not found on the page at capture time.

#### flyout-tab

Flyout tab. A pill tab across the top of the opened menu (Bottle active on yellow).

Page: home. Selector: `flyout tab pill`. States: default, hover, focus-visible, pressed.

Not found on the page at capture time.

#### flyout-card

Flyout card. An option card inside the flyout carousel ("Bottle — A range of reusable bottles…").

Page: home. Selector: `flyout option card`. States: default, hover, focus-visible, pressed.

Not found on the page at capture time.

### Home (www)

#### hero-display

Hero display. The h1 over the full-bleed video hero ("Whatever the season") — Dopper display type on media.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 425.36 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dopper 72px/72px 400 |
| Letter spacing | normal |
| Colour | #f6ecc8 |
| Text node | span.SplitText_word__C3WPI: Dopper 72px/72px 400, #f6ecc8 |
| Transition | none |
| How | at rest |

Crops: `hero-display-default.png`.

#### btn-dark

Button, dark. The deep-sea filled pill CTA ("Watch now") on the video hero.

Page: home. Selector: `hero dark pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173.73 x 51.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6ecc8 | = | = | = |
| Text node | span: Gilroy 18px/23.4px 600, #f6ecc8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.burstButton_fakeButton__B8btS 165.0x38.5 bg #000f2e r 20px; div.link_link__JtDHX.link_background__vwwg3 173.7x51.4 bg #000f2e r 20px | div.burstButton_fakeButton__B8btS 165.0x38.5 bg #000f2e r 20px; div.burstButton_bubble__N2Lo3 24.2x24.2 bg #000f2e r 9999px; div.burstButton_bubble__N2Lo3 13.1x13.1 bg #000f2e r 9999px; div.burstButton_bubble__N2Lo3 20.4x20.4 bg #000f2e r 9999px; div.burstButton_bubble__N2Lo3 21.6x21.6 bg #000f2e r 9999px; div.burstButton_bubble__N2Lo3 13.0x13.0 bg #000f2e r 9999px | a.burstButton_wrapper__JRFOg 173.7x51.4 outline 1px auto #005fcc offset 1px; div.burstButton_fakeButton__B8btS 165.0x38.5 bg #000f2e r 20px; div.link_link__JtDHX.link_background__vwwg3 173.7x51.4 bg #000f2e r 20px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-dark-default.png`, `btn-dark-hover.png`, `btn-dark-focus-visible.png`, `btn-dark-pressed.png`.

#### btn-outline

Button, outline. The outline pill CTA ("Shop our collection") on the video hero.

Page: home. Selector: `hero outline pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 244.63 x 51.39 | = | = | = |
| Padding | 12px 40px | = | = | = |
| Border | 2px solid #f6ecc8 | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | #f6ecc8 | = | #f6ecc8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Gilroy 18px/23.4px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6ecc8 | #0067e5 | = | #0067e5 |
| Transition | background 0.25s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.link_link__JtDHX.link_background__vwwg3 244.6x51.4 border T:2px solid #f6ecc8 / R:2px solid #f6ecc8 / B:2px solid #f6ecc8 / L:2px solid #f6ecc8 r 20px | a.link_link__JtDHX.link_background__vwwg3 244.6x51.4 bg #f6ecc8 border T:2px solid #f6ecc8 / R:2px solid #f6ecc8 / B:2px solid #f6ecc8 / L:2px solid #f6ecc8 r 20px | a.link_link__JtDHX.link_background__vwwg3 244.6x51.4 border T:2px solid #f6ecc8 / R:2px solid #f6ecc8 / B:2px solid #f6ecc8 / L:2px solid #f6ecc8 r 20px outline 1px auto #005fcc offset 1px | a.link_link__JtDHX.link_background__vwwg3 244.6x51.4 bg #f6ecc8 border T:2px solid #f6ecc8 / R:2px solid #f6ecc8 / B:2px solid #f6ecc8 / L:2px solid #f6ecc8 r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-outline-default.png`, `btn-outline-hover.png`, `btn-outline-focus-visible.png`, `btn-outline-pressed.png`.

#### collection-tab

Collection tab. A product tab inside "The collections" showcase; toggled to swap the card below.

Page: home. Selector: `collections tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 250 x 445 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | -apple-system 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3.intro.tabsVariation_cardItemHeading__ClkPi: Gilroy 27px/32.4px 400, #000f2e | = | = | = |
| Transition | opacity 0.4s cubic-bezier(0.83, 0, 0.17, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 20, 0) | = | = | = |
| Opacity | 0 | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | article.tabsVariation_card__lZivw 267.5x476.2 bg #8ab1e6 r 20px | = | button.keen-slider__slide.tabsVariation_cardItem__G2SQa 250.0x445.0 r 20px outline 1px auto #005fcc offset 0px; article.tabsVariation_card__lZivw 267.5x476.2 bg #8ab1e6 r 20px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `collection-tab-default.png`, `collection-tab-hover.png`, `collection-tab-focus-visible.png`, `collection-tab-pressed.png`.

#### collections-heading

Section heading. A section heading ("The collections") — Gilroy bold, deep-sea.

Page: home. Selector: `collections heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1324 x 58 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dopper 58px/58px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.SplitText_word__C3WPI: Dopper 58px/58px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `collections-heading-default.png`.

#### content-card

Content card. A home split card (copy + CTA beside a photo tile).

Page: home. Selector: `home content card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 786 x 596.94 |
| Padding | 0px 16px 0px 70px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.h2.RoiCalculator_heading__IxzrP: Gilroy 43px/47.3px 600, #000f2e |
| Transition | none |
| Icon | 133 x 133, colour #000000 |
| Painted layers | span.RangeSlider_track__Ma03Q 700.0x16.0 bg #cce2ff r 9999px; span.RangeSlider_progress__KeNcI 20.0x16.0 image linear-gradient(90deg, #0067e5 0px, #4183d9 100%) r 20px; span.RangeSlider_thumb__cji3q 40.0x40.0 bg #0067e5 r 50% shadow #0067e5 @ 0.2 0px 2px 8px 0px; span::before.RangeSlider_thumb__cji3q 8pxx8px bg #000f2e border T:4px solid #fcfaf2 / R:4px solid #fcfaf2 / B:4px solid #fcfaf2 / L:4px solid #fcfaf2 r 50%; div.B2CRangeSliderPopoverContent_content__nslL1 129.0x46.0 bg #ffffff r 16px shadow #000000 @ 0.1 5px 4px 17.4px 0px; div.RoiProductItem_radioButton__W9SVQ 16.0x16.0 border T:2px solid #000f2e / R:2px solid #000f2e / B:2px solid #000f2e / L:2px solid #000f2e r 50% |
| How | at rest |

Crops: `content-card-default.png`.

### Footer

#### footer

Footer. The sand footer: newsletter band, "Just refill" columns, social icons, certification and payment logos.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 736.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.form-title: Gilroy 22px/26.18px 600, #000000 |
| Transition | none |
| Icon | 60 x 60, colour #000000 |
| Painted layers | div.main-section 1440.0x630.6 bg #f6ecc8; a.link.social 0.0x0.0 bg #f9f3df r 42px; a.link.social 0.0x0.0 bg #f9f3df r 42px; a.link.social 0.0x0.0 bg #f9f3df r 42px; a.link.social 0.0x0.0 bg #f9f3df r 42px; input 245.0x54.0 bg #fcfaf2 r 20px |
| How | at rest |

Crops: `footer-default.png`.

#### newsletter-input

Newsletter input. The email field in the footer newsletter band; focused, never submitted.

Page: home. Selector: `footer email input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 400 x 54 | = |
| Padding | 12px 20px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | #fcfaf2 | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 0px |
| Font | Gilroy 18px/23.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #000f2e | = |
| Transition | opacity 0.3s linear | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| Painted layers | input 400.0x54.0 bg #fcfaf2 r 20px | input 400.0x54.0 bg #fcfaf2 r 20px outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field |

Crops: `newsletter-input-default.png`, `newsletter-input-focused.png`.

### Shop

#### shop-header

Shop header. The same dopper header on the Magento storefront, plus the catalog nav row below it.

Page: shop. Selector: `dopper-navigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 110 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfaf2 |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Transition | none |
| Painted layers | header.page-header 1440.0x110.0 bg #fcfaf2; span.counter.qty 0.0x0.0 bg #0abeaa r 100% shadow #000000 @ 0 0px 0px 1px 0px; span.counter.qty 0.0x0.0 bg #0abeaa r 100% shadow #000000 @ 0 0px 0px 1px 0px |
| How | at rest |

Crops: `shop-header-default.png`.

#### shop-nav

Shop nav. The catalog nav row (All products / Mugs / Bottles / Accessories / Spare parts / E-Gift Card / Last chance).

Page: shop. Selector: `.navigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1360 x 27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 16px/26px 800 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | a.level-top: Gilroy 20px/25px 600, #0067e5 |
| Transition | none |
| Painted layers | ul.level0.submenu 0.0x0.0 bg #fcfaf2 border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc shadow #000000 @ 0.19 0px 5px 5px 0px; ul.level0.submenu 0.0x0.0 bg #fcfaf2 border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc shadow #000000 @ 0.19 0px 5px 5px 0px; ul.level0.submenu 0.0x0.0 bg #fcfaf2 border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc shadow #000000 @ 0.19 0px 5px 5px 0px |
| How | at rest |

Crops: `shop-nav-default.png`.

#### shop-nav-link

Shop nav link. A catalog nav item; "All products" paints the active darkBlue.

Page: shop. Selector: `.navigation a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109.56 x 25 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 20px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 20px/25px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0067e5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.level-top 109.6x25.0 r 20px outline 2px solid #000f2e offset 4px | = |

Crops: `shop-nav-link-default.png`, `shop-nav-link-hover.png`, `shop-nav-link-focus-visible.png`, `shop-nav-link-pressed.png`.

#### shop-hero-button

Shop CTA. The darkBlue pill CTA on a shop hero tile ("Shop now").

Page: shop. Selector: `shop hero Shop now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 172.98 x 54 | = | = | = |
| Padding | 13px 40px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | #cccccc @ 0.8 0px 1px 0px 0px inset, #cccccc @ 0.3 0px -1px 0px 0px inset |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 20px/26px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0067e5 | = | = | = |
| Text node | span: Gilroy 20px/26px 600, #f6ecc8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 170.984px x 54px, absolute, bg #0067e5, radius 20px | = | = | = |
| Painted layers | button.action.js-button-animate 173.0x54.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px; button::before.action.js-button-animate 170.984pxx54px bg #0067e5 r 20px | = | button.action.js-button-animate 173.0x54.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px outline 2px solid #000f2e offset 4px; button::before.action.js-button-animate 170.984pxx54px bg #0067e5 r 20px | button.action.js-button-animate 173.0x54.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px shadow #cccccc @ 0.8 0px 1px 0px 0px inset, #cccccc @ 0.3 0px -1px 0px 0px inset; button::before.action.js-button-animate 170.984pxx54px bg #0067e5 r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shop-hero-button-default.png`, `shop-hero-button-hover.png`, `shop-hero-button-focus-visible.png`, `shop-hero-button-pressed.png`.

### Product list (PLP)

#### plp-h1

PLP title. "Bottles" — Dopper display type, deep-sea, centred over the sand field.

Page: category. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 259.36 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dopper 80px/80px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | span.base: Dopper 72px/72px 400, #000f2e |
| Transition | none |
| How | at rest |

Crops: `plp-h1-default.png`.

#### plp-sub

PLP subtitle. The one-line lede under the title ("End packaged water. Just refill your Dopper bottle.").

Page: category. Selector: `.category-payoff`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 24 |
| Padding | 0px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dopper 20px/24px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Transition | none |
| How | at rest |

Crops: `plp-sub-default.png`.

#### filters-button

Filters button. The teal "+ Filters" pill that opens the filter sheet (open by default on desktop).

Page: category. Selector: `+ Filters`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 156.23 x 52 | = | = | = |
| Padding | 12px 40px 12px 60px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | #cccccc @ 0.8 0px 1px 0px 0px inset, #cccccc @ 0.3 0px -1px 0px 0px inset |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 20px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | strong.text: Gilroy 20px/26px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 156.234px x 54px, absolute, bg #0abeaa, radius 20px | = | = | = |
| Painted layers | button::before.action.cta 156.234pxx54px bg #0abeaa r 20px | = | button.action.cta 156.2x52.0 r 20px outline 2px solid #000f2e offset 4px; button::before.action.cta 156.234pxx54px bg #0abeaa r 20px | button.action.cta 156.2x52.0 r 20px shadow #cccccc @ 0.8 0px 1px 0px 0px inset, #cccccc @ 0.3 0px -1px 0px 0px inset; button::before.action.cta 156.234pxx54px bg #0abeaa r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filters-button-default.png`, `filters-button-hover.png`, `filters-button-focus-visible.png`, `filters-button-pressed.png`.

#### filter-panel

Filter panel. The light-blue (darkBlue-3) filter sheet: Collection/Size radio groups, Colour swatches, Bundle checkbox.

Page: category. Selector: `filter sheet`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1360 x 347.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | div.filter-options-title: Gilroy 24px/28.56px 700, #000f2e |
| Transition | none |
| Painted layers | div.swatch-option.color 24.0x24.0 bg #f0f0f0 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #949494 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #000000 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #3562a1 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #629431 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #f3d54e image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100% |
| How | at rest |

Crops: `filter-panel-default.png`.

#### filter-radio

Filter radio. A Collection/Size option row: ring + name + muted item count.

Page: category. Selector: `filter option row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 184.14 x 26 |
| Padding | 0px 0px 0px 30px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 700 |
| Letter spacing | normal |
| Colour | #000f2e |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `filter-radio-default.png`.

#### filter-swatch

Colour swatch. A colour-dot swatch filter option.

Page: category. Selector: `colour swatch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155 x 129 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Gilroy 20px/26px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000f2e | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.swatch-option.color 24.0x24.0 bg #f0f0f0 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #949494 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #000000 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #3562a1 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #629431 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #f3d54e image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100% | = | div.swatch-option.color 24.0x24.0 bg #f0f0f0 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100% outline 2px solid #000f2e offset 4px; div.swatch-option.color 24.0x24.0 bg #949494 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #000000 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #3562a1 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #629431 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 24.0x24.0 bg #f3d54e image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-swatch-default.png`, `filter-swatch-hover.png`, `filter-swatch-focus-visible.png`, `filter-swatch-pressed.png`.

#### filter-checkbox

Filter checkbox. The Bundle option: box checkbox + "Flip Straw Bundle" + count.

Page: category. Selector: `filter checkbox row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 291.38 x 28.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 24px/28.56px 700 |
| Letter spacing | normal |
| Colour | #000f2e |
| Transition | none |
| How | at rest |

Crops: `filter-checkbox-default.png`.

#### filter-close

Filter close. The deep-sea circle × button closing the filter sheet.

Page: category. Selector: `filter X button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 54 x 54 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 20px/26px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0067e5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 54px x 54px, static, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.filter-close 54.0x54.0 r 20px outline 2px solid #000f2e offset 4px | = |

Crops: `filter-close-default.png`, `filter-close-hover.png`, `filter-close-focus-visible.png`, `filter-close-pressed.png`.

#### product-card

Product card. A PLP card: product photo, optional badge chip, name, price in EUR.

Page: category. Selector: `.product-item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 340 x 655.52 | = |
| Padding | 0px 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Gilroy 14px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000f2e | = |
| Text node | a.product-item-link: Gilroy 20px/26px 400, #999cba | a.product-item-link: Gilroy 20px/26px 400, #000f2e |
| Transition | none | = |
| Painted layers | div.drop.drop-hover 0.0x0.0 bg #a7bfb7 r 63% 37% 54% 46% / 55% 48% 52% 45%; div.product-item-inner 308.0x40.0 bg #ffffff; div.product.actions 308.0x40.0 bg #fdfaf3; button.action.tocart 105.6x40.0 bg #045cdc r 10px; a.action.personalize 139.0x40.0 border T:2px solid #011128 / R:2px solid #011128 / B:2px solid #011128 / L:2px solid #011128 r 10px | div.drop.drop-hover 246.4x246.4 bg #a7bfb7 r 62.8153% 37.1847% 54% 46% / 54.9518% 48.0964% 51.9036% 45.0482%; div.product-item-inner 308.0x40.0 bg #ffffff; div.product.actions 308.0x40.0 bg #fdfaf3; button.action.tocart 105.6x40.0 bg #045cdc r 10px; a.action.personalize 139.0x40.0 border T:2px solid #011128 / R:2px solid #011128 / B:2px solid #011128 / L:2px solid #011128 r 10px |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### product-price

Price. The EUR price on a product card.

Page: category. Selector: `.price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 14px/normal 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | span.price: Gilroy 16px/24px 600, #999cba |
| Transition | none |
| How | at rest |

Crops: `product-price-default.png`.

#### product-badge

Badge chip. The outlined "New" chip on a product card.

Page: category. Selector: `product badge`. States: .

Not found on the page at capture time.

### Product page (PDP)

#### breadcrumb

Breadcrumb. Home > Original - Pacific Blue trail above the gallery.

Page: pdp. Selector: `.breadcrumbs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1394 x 26 |
| Padding | 0px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | a: Gilroy 16px/26px 400, #000f2e |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -697, 0) |
| How | at rest |

Crops: `breadcrumb-default.png`.

#### pdp-title

PDP title. The product name ("Original - Pacific Blue").

Page: pdp. Selector: `PDP h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 415 x 83 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dopper 80px/80px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | span.base: Dopper 30px/46px 400, #000f2e |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

PDP price. €14.95 under the title.

Page: pdp. Selector: `.price-box .price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 44.69 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 16px/16px 600 |
| Letter spacing | normal |
| Colour | #000f2e |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### add-to-cart

Add to cart. The darkBlue pill buy button; measured, never pressed for real (pressed state is CDP-forced).

Page: pdp. Selector: `.tocart`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 203.34 x 54 | = | = | = |
| Padding | 13px 25px | = | = | = |
| Border | 1px solid #0067e5 | = | = | = |
| Radius | 20px | = | = | = |
| Background | #0067e5 | = | = | = |
| Box shadow | none | = | #fcfaf2 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 20px/26px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f9f3df | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.action.primary 203.3x54.0 bg #0067e5 border T:1px solid #0067e5 / R:1px solid #0067e5 / B:1px solid #0067e5 / L:1px solid #0067e5 r 20px | = | button.action.primary 203.3x54.0 bg #0067e5 border T:1px solid #0067e5 / R:1px solid #0067e5 / B:1px solid #0067e5 / L:1px solid #0067e5 r 20px shadow #fcfaf2 0px 0px 0px 4px outline 2px solid #000f2e offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-cart-default.png`, `add-to-cart-hover.png`, `add-to-cart-focus-visible.png`, `add-to-cart-pressed.png`.

#### pdp-option

Configurator row. A collapsed configurator row in the buy box; the "opened" state presses its own toggle (a local expand).

Page: pdp. Selector: `pdp option row`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 106.83 x 25 | - |
| Padding | 0px | - |
| Border | none | - |
| Radius | 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Gilroy 20px/25px 600 | - |
| Letter spacing | normal | - |
| Colour | #000f2e | - |
| Text node | span: Gilroy 20px/25px 600, #000f2e | - |
| Transition | none | - |
| Cursor | pointer | - |
| How | at rest | - |
| Error | - | toggle refused: A "Accessories" |

Crops: `pdp-option-default.png`.

#### pdp-swatch

PDP swatch. A colour dot in "Choose your colour" (the selected ring vs the rest).

Page: pdp. Selector: `pdp swatch`. States: .

Not found on the page at capture time.

#### pdp-feature

Feature line. An icon + claim row in the buy box (Lightweight and extremely tough).

Page: pdp. Selector: `pdp feature`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 415 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | td: Gilroy 20px/26px 400, #000f2e |
| Transition | none |
| How | at rest |

Crops: `pdp-feature-default.png`.

### Cart

#### cart-title

Cart title. "Your cart" — darkBlue Dopper display on sand.

Page: cart. Selector: `cart h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dopper 80px/80px 400 |
| Letter spacing | normal |
| Colour | #0067e5 |
| Text node | span.base: Dopper 80px/80px 400, #0067e5 |
| Transition | none |
| How | at rest |

Crops: `cart-title-default.png`.

#### cart-empty

Empty cart. The empty-basket block: "Be my hero" illustration, copy and a Back to shop CTA. A filled cart was not exercised (nothing is added).

Page: cart. Selector: `empty cart block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dopper 80px/80px 400 |
| Letter spacing | normal |
| Colour | #0067e5 |
| Text node | span.base: Dopper 80px/80px 400, #0067e5 |
| Transition | none |
| How | at rest |

Crops: `cart-empty-default.png`.

#### cart-cta

Cart CTA. The darkBlue pill "Back to shop" in the empty state.

Page: cart. Selector: `Back to shop`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 202.17 x 54 | = | = | = |
| Padding | 13px 40px | = | = | = |
| Border | 1px solid #0067e5 | = | = | = |
| Radius | 20px | = | = | = |
| Background | #0067e5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 20px/26px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f9f3df | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.action.primary 202.2x54.0 bg #0067e5 border T:1px solid #0067e5 / R:1px solid #0067e5 / B:1px solid #0067e5 / L:1px solid #0067e5 r 20px | = | a.action.primary 202.2x54.0 bg #0067e5 border T:1px solid #0067e5 / R:1px solid #0067e5 / B:1px solid #0067e5 / L:1px solid #0067e5 r 20px outline 2px solid #000f2e offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-cta-default.png`, `cart-cta-hover.png`, `cart-cta-focus-visible.png`, `cart-cta-pressed.png`.

#### cart-strip

Cart strip. The darkBlue-3 band under the header: ← Continue shopping left, Customer Service right.

Page: cart. Selector: `cart strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 93 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #cce2ff |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | a: Gilroy 16px/20px 400, #000f2e |
| Transition | none |
| Painted layers | div.cart-top 1440.0x93.0 bg #cce2ff |
| How | at rest |

Crops: `cart-strip-default.png`.

### Login and signup

#### login-card

Login card. The darkBlue "Registered Customers" card: Email + Password fields, Sign in, Show password, Remember Me, Forgot link.

Page: login. Selector: `login card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 534.09 x 489 |
| Padding | 40px 44px 53px 44px |
| Border | none |
| Radius | 20px |
| Background | #0067e5 |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #fcfaf2 |
| Text node | strong: Gilroy 40px/42px 500, #fcfaf2 |
| Transition | none |
| Painted layers | div.block.block-customer-login 534.1x489.0 bg #0067e5 r 20px; input.input-text.input--large 357.0x54.0 bg #fcfaf2 border T:2px solid #fcfaf2 / R:2px solid #fcfaf2 / B:2px solid #fcfaf2 / L:2px solid #fcfaf2 r 20px; input.input-text.input--large 197.6x54.0 bg #fcfaf2 border T:2px solid #fcfaf2 / R:2px solid #fcfaf2 / B:2px solid #fcfaf2 / L:2px solid #fcfaf2 r 20px; button.action.js-button-animate 143.4x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px; button::before.action.js-button-animate 139.391pxx54px bg #000f2e border T:1px solid #000f2e / R:1px solid #000f2e / B:1px solid #000f2e / L:1px solid #000f2e r 20px; span.tooltip.content 0.0x0.0 bg #ffffff border T:1px solid #bbbbbb / R:1px solid #bbbbbb / B:1px solid #bbbbbb / L:1px solid #bbbbbb |
| How | at rest |

Crops: `login-card-default.png`.

#### login-email

Email field. The white rounded Email field on the blue card; focused and typed into, then cleared — nothing sent.

Page: login. Selector: `#email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 357 x 54 | = | = |
| Padding | 0px 20px | = | = |
| Border | 2px solid #fcfaf2 | 2px solid #000f2e | 2px solid #000f2e |
| Radius | 20px | = | = |
| Background | #fcfaf2 | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #000f2e offset 4px | 2px solid #000f2e offset 4px |
| Font | Gilroy 20px/28.5714px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000f2e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000f2e, opacity 1 | = | = |
| Painted layers | input.input-text.input--large 357.0x54.0 bg #fcfaf2 border T:2px solid #fcfaf2 / R:2px solid #fcfaf2 / B:2px solid #fcfaf2 / L:2px solid #fcfaf2 r 20px | input.input-text.input--large 357.0x54.0 bg #fcfaf2 border T:2px solid #000f2e / R:2px solid #000f2e / B:2px solid #000f2e / L:2px solid #000f2e r 20px outline 2px solid #000f2e offset 4px | input.input-text.input--large 357.0x54.0 bg #fcfaf2 border T:2px solid #000f2e / R:2px solid #000f2e / B:2px solid #000f2e / L:2px solid #000f2e r 20px outline 2px solid #000f2e offset 4px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-password

Password field. The Password field beside the Sign in button.

Page: login. Selector: `#pass`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 197.61 x 54 | = |
| Padding | 0px 20px | = |
| Border | 2px solid #fcfaf2 | 2px solid #000f2e |
| Radius | 20px | = |
| Background | #fcfaf2 | = |
| Box shadow | none | = |
| Outline | none | 2px solid #000f2e offset 4px |
| Font | Gilroy 20px/28.5714px 400 | = |
| Letter spacing | normal | = |
| Colour | #000f2e | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000f2e, opacity 1 | = |
| Painted layers | input.input-text.input--large 197.6x54.0 bg #fcfaf2 border T:2px solid #fcfaf2 / R:2px solid #fcfaf2 / B:2px solid #fcfaf2 / L:2px solid #fcfaf2 r 20px | input.input-text.input--large 197.6x54.0 bg #fcfaf2 border T:2px solid #000f2e / R:2px solid #000f2e / B:2px solid #000f2e / L:2px solid #000f2e r 20px outline 2px solid #000f2e offset 4px |
| How | at rest | clicked into the field |

Crops: `login-password-default.png`, `login-password-focused.png`.

#### login-button

Sign in button. The deep-sea pill Sign in inside the blue card; never pressed (pressed state is CDP-forced).

Page: login. Selector: `#send2`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143.39 x 56 | = | = | = |
| Padding | 14px 40px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | #cccccc @ 0.8 0px 1px 0px 0px inset, #cccccc @ 0.3 0px -1px 0px 0px inset |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 20px/26px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6ecc8 | = | = | = |
| Text node | span: Gilroy 20px/26px 600, #f6ecc8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 139.391px x 54px, absolute, bg #000f2e, radius 20px | = | = | = |
| Painted layers | button.action.js-button-animate 143.4x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px; button::before.action.js-button-animate 139.391pxx54px bg #000f2e border T:1px solid #000f2e / R:1px solid #000f2e / B:1px solid #000f2e / L:1px solid #000f2e r 20px | = | button.action.js-button-animate 143.4x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px outline 2px solid #000f2e offset 4px; button::before.action.js-button-animate 139.391pxx54px bg #000f2e border T:1px solid #000f2e / R:1px solid #000f2e / B:1px solid #000f2e / L:1px solid #000f2e r 20px | button.action.js-button-animate 143.4x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px shadow #cccccc @ 0.8 0px 1px 0px 0px inset, #cccccc @ 0.3 0px -1px 0px 0px inset; button::before.action.js-button-animate 139.391pxx54px bg #000f2e border T:1px solid #000f2e / R:1px solid #000f2e / B:1px solid #000f2e / L:1px solid #000f2e r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-button-default.png`, `login-button-hover.png`, `login-button-focus-visible.png`, `login-button-pressed.png`.

#### login-label

Field label. The small sand label above a field on the blue card.

Page: login. Selector: `label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 56.94 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #fcfaf2 |
| Text node | span: Gilroy 20px/26px 400, #fcfaf2 |
| Transition | none |
| Cursor | default |
| ::after | auto x auto, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `login-label-default.png`.

#### login-checkbox

Checkbox row. The Remember Me / Show password checkbox rows under the password field.

Page: login. Selector: `checkbox label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 197.61 x 27 |
| Padding | 0px 0px 0px 30px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #fcfaf2 |
| Text node | span: Gilroy 20px/26px 600, #fcfaf2 |
| Transition | all 0.2s ease-in-out |
| Cursor | default |
| ::before | 16px x 16px, absolute, bg #000000 @ 0 url(…), radius 0px |
| How | at rest |

Crops: `login-checkbox-default.png`.

#### login-link

Form link. "Forgot Your Password?" — sand text link on the blue card.

Page: login. Selector: `forgot link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 187.03 x 24.13 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 20px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 18px/24.12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6ecc8 | = | = | = |
| Text node | span: Gilroy 18px/24.12px 400, #f6ecc8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.action.remind 187.0x24.1 r 20px outline 2px solid #000f2e offset 4px | = |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### new-card

New customers card. The darkBlue-3 "New Customers" card with benefits copy and a Create an Account CTA.

Page: login. Selector: `new customers card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 534.09 x 489 |
| Padding | 40px 44px 53px 44px |
| Border | none |
| Radius | 20px |
| Background | #cce2ff |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | strong: Gilroy 40px/42px 500, #000f2e |
| Transition | none |
| ::before | 0px x 0px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.block.block-new-customer 534.1x489.0 bg #cce2ff r 20px; a.action.create 256.5x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px; a::before.action.create 252.531pxx54px bg #0067e5 border T:1px solid #0067e5 / R:1px solid #0067e5 / B:1px solid #0067e5 / L:1px solid #0067e5 r 20px |
| How | at rest |

Crops: `new-card-default.png`.

#### create-button

Create account. The darkBlue pill in the New Customers card; a link, never followed.

Page: login. Selector: `create account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256.53 x 56 | = | = | = |
| Padding | 14px 40px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000f2e offset 4px | = |
| Font | Gilroy 20px/26px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6ecc8 | = | = | = |
| Text node | span: Gilroy 20px/26px 600, #f6ecc8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 252.531px x 54px, absolute, bg #0067e5, radius 20px | = | = | = |
| Painted layers | a.action.create 256.5x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px; a::before.action.create 252.531pxx54px bg #0067e5 border T:1px solid #0067e5 / R:1px solid #0067e5 / B:1px solid #0067e5 / L:1px solid #0067e5 r 20px | = | a.action.create 256.5x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 20px outline 2px solid #000f2e offset 4px; a::before.action.create 252.531pxx54px bg #0067e5 border T:1px solid #0067e5 / R:1px solid #0067e5 / B:1px solid #0067e5 / L:1px solid #0067e5 r 20px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `create-button-default.png`, `create-button-hover.png`, `create-button-focus-visible.png`, `create-button-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The 390 bar: dopper. wordmark left-centre and the sand burger circle.

Page: mobile. Selector: `dopper-navigation @390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 125 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 0 x 0, colour #f9f3df |
| Painted layers | ul.languagePopup.hidden 0.0x0.0 bg #fcfaf2 r 20px shadow #000000 @ 0.1 0px 4px 20px 0px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-burger

Burger button. The sand-circle hamburger opening the full-screen menu.

Page: mobile. Selector: `burger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 45 x 45 | = | - | - |
| Padding | 15px | = | - | - |
| Border | none | = | - | - |
| Radius | 0px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Arial 13.3333px/normal 400 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #000000 | = | - | - |
| Transition | none | = | - | - |
| Cursor | default | = | - | - |
| Icon | 51 x 51, colour #000000 | = | - | - |
| How | at rest | mouse hover | - | - |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |
| Error | - | = | = | cdpSession.send: Protocol error (CSS.forcePseudoState): Could not find node with given id |

Crops: `m-burger-default.png`, `m-burger-hover.png`, `m-burger-focus-visible.png`.

#### m-hero

Mobile display. The hero h1 at 390.

Page: mobile. Selector: `h1 @390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 105.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Dopper 44px/52.8px 400 |
| Letter spacing | normal |
| Colour | #f6ecc8 |
| Text node | span.SplitText_word__C3WPI: Dopper 44px/52.8px 400, #f6ecc8 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-menu-open

Mobile menu, open. The darkBlue full-screen menu: large white rows, outline pills, bag and × controls.

Page: mobile. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px 20px 20px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.mobile-link: Gilroy 34px/37.4px 700, #fcfaf2 |
| Transition | none |
| Icon | 12 x 8, colour #fcfaf2 |
| Painted layers | div.dialog__background 390.0x844.0 bg #0067e5 r 0px 0px 0% 0%; span.underline 0.0x0.0 image linear-gradient(#000000 @ 0 calc(100% - 1px), #fcfaf2 1px); span.underline 0.0x0.0 image linear-gradient(#000000 @ 0 calc(100% - 1px), #fcfaf2 1px); span.underline 0.0x0.0 image linear-gradient(#000000 @ 0 calc(100% - 1px), #fcfaf2 1px); span.underline 0.0x0.0 image linear-gradient(#000000 @ 0 calc(100% - 1px), #fcfaf2 1px); span.underline 0.0x0.0 image linear-gradient(#000000 @ 0 calc(100% - 1px), #fcfaf2 1px) |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A large row inside the opened menu.

Page: mobile. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.81 x 37.41 | = | - | - |
| Padding | 0px | = | - | - |
| Gap | 15px | = | - | - |
| Border | none | = | - | - |
| Radius | 0px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Gilroy 34px/37.4px 700 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #fcfaf2 | = | - | - |
| Transition | opacity, transform 0.3s, 0.7s ease, ease delay 0.3s | = | - | - |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | - | - |
| Cursor | pointer | = | - | - |
| Icon | 12 x 8, colour #fcfaf2 | = | - | - |
| How | at rest | mouse hover | - | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Error | - | = | = | cdpSession.send: Protocol error (CSS.forcePseudoState): Could not find node with given id |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`.

#### m-menu-pill

Mobile menu pill. An outline pill inside the menu (Impact report / Find a Store).

Page: mobile. Selector: `menu outline pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 194.64 x 54 | = | - | - |
| Padding | 14px 31px | = | - | - |
| Gap | 12px | = | - | - |
| Border | 2px solid #f6ecc8 | = | - | - |
| Radius | 20px | = | - | - |
| Background | transparent | = | - | - |
| Box shadow | none | = | - | - |
| Outline | none | = | - | - |
| Font | Gilroy 20px/22px 700 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #f6ecc8 | = | - | - |
| Transition | opacity, transform 0.4s, 0.7s ease, ease delay 0.4s | = | - | - |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | - | - |
| Cursor | pointer | = | - | - |
| Painted layers | a.nav-link-mobile.secondary 194.6x54.0 border T:2px solid #f6ecc8 / R:2px solid #f6ecc8 / B:2px solid #f6ecc8 / L:2px solid #f6ecc8 r 20px | = | - | - |
| How | at rest | mouse hover | - | - |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |
| Error | - | = | = | cdpSession.send: Protocol error (CSS.forcePseudoState): Could not find node with given id |

Crops: `m-menu-pill-default.png`, `m-menu-pill-hover.png`, `m-menu-pill-focus-visible.png`.

#### m-filter-sheet

Filter sheet (mobile). The opened filter overlay at 390: Collection/Size radios, Colour swatches, × close.

Page: mobile-category. Selector: `mobile filter sheet`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 1063.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gilroy 20px/26px 400 |
| Letter spacing | normal |
| Colour | #000f2e |
| Text node | div.filter-options-title: Gilroy 22px/26.4px 700, #000f2e |
| Transition | none |
| Painted layers | div.swatch-option.color 32.0x32.0 bg #f0f0f0 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 32.0x32.0 bg #949494 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 32.0x32.0 bg #000000 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 32.0x32.0 bg #3562a1 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 32.0x32.0 bg #629431 image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100%; div.swatch-option.color 32.0x32.0 bg #f3d54e image linear-gradient(to left, #000000 @ 0.05, #000000 @ 0.05 50%, #000000 @ 0.1 50%, #000000 @  r 100% |
| How | at rest |

Crops: `m-filter-sheet-default.png`.

#### m-filter-radio

Mobile filter row. A radio row in the mobile filter sheet.

Page: mobile-category. Selector: `mobile filter radio`. States: default.

Not found on the page at capture time.

## Transitions declared in the readable stylesheets

www.dopper.com's Next.js bundles compile every class to a build hash (the names in the Selector rows are the spec's own description, not class names), and shop.dopper.com serves Magento's compiled stylesheets; this list covers the transition rules the readable stylesheets on each host expose, and the per-state Transition rows above are the computed values the page paints.

- category: `visibility 0.3s, opacity 0.3s`, `opacity 0.3s`, `transform 0.3s ease-in-out`, `transform 0.2s`, `background 0.3s`, `background-color 0.3s`, `background-color 0.3s, border 0.3s`, `background-color 0.3s ease-out`, `opacity 0.3s ease-out`, `background-color 0.3s ease-in`, `none`, `0.3s ease-in-out`

- home: `.25s linear,transform .4s var(--bounce-out)`, `0.25s linear`, `transform .4s var(--ease-in-out-quint)`, `background 0.25s linear`, `transform .65s var(--bounce-out) var(--delay),opacity .65s var(--ease-in-quint) var(--delay)`, `transform .7s var(--ease-out-quint),opacity .7s var(--ease-out-quint)`, `color 0.15s linear`, `initial`, `transform .4s var(--bounce-out)`, `height 0.5s`, `background-color 0.3s ease-in-out, border 0.3s ease-in-out`, `unset`

- login: `visibility 0.3s, opacity 0.3s`, `opacity 0.3s`, `transform 0.3s ease-in-out`, `transform 0.2s`, `background 0.3s`, `background-color 0.3s`, `background-color 0.3s, border 0.3s`, `background-color 0.3s ease-out`, `opacity 0.3s ease-out`, `background-color 0.3s ease-in`, `none`, `0.3s ease-in-out`

- pdp: `visibility 0.3s, opacity 0.3s`, `opacity 0.3s`, `transform 0.3s ease-in-out`, `transform 0.2s`, `background 0.3s`, `background-color 0.3s`, `background-color 0.3s, border 0.3s`, `background-color 0.3s ease-out`, `opacity 0.3s ease-out`, `background-color 0.3s ease-in`, `none`, `0.3s ease-in-out`

- shop: `visibility 0.3s, opacity 0.3s`, `opacity 0.3s`, `transform 0.3s ease-in-out`, `transform 0.2s`, `background 0.3s`, `background-color 0.3s`, `background-color 0.3s, border 0.3s`, `background-color 0.3s ease-out`, `opacity 0.3s ease-out`, `background-color 0.3s ease-in`, `none`, `0.3s ease-in-out`
