# Epic Games component measurements

Computed styles read from store.epicgames.com and www.epicgames.com on 2026-11-13 20:45 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the painted public surfaces — the dark EGS v2 store (Discover, Browse, product, Free Games, News, Download), the Epic account sign-in dialog, the OpenSans marketing home and the support centre — with any consent layer hidden (never answered) and the store's React app given explicit waits rather than networkidle, and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Global navigation

#### egs-nav

Global nav. The <egs-navigation> web component over every store page: Epic Games mark, STORE, Support, Distribute, the globe locale picker, Sign in and the blue Download pill. Shadow-DOM host; children measured through it.

Page: discover. Selector: `egs-navigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| How | at rest |

Crops: `egs-nav-default.png`.

#### nav-signin

Sign in button. The dark Sign-in pill in the global nav; links to the sign-in flow, measured never followed.

Page: discover. Selector: `nav Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.97 x 32 | = | - | = |
| Padding | 4px 12px | = | - | = |
| Gap | normal 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 6px | = | - | = |
| Background | #ffffff @ 0.15 | #ffffff @ 0.35 | - | #ffffff @ 0.35 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span.label: Inter 14px/24px 500, #ffffff, ls 0.28px | = | - | = |
| Transition | color, background-color 0.12s cubic-bezier(0.65, 0, 0.35, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.dropdown__button.secondary-cta 72.0x32.0 bg #ffffff @ 0.15 r 6px | a.dropdown__button.secondary-cta 72.0x32.0 bg #ffffff @ 0.35 r 6px | - | a.dropdown__button.secondary-cta 72.0x32.0 bg #ffffff @ 0.35 r 6px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-pressed.png`.

#### nav-download

Download button. The blue Download pill in the global nav; measured never followed.

Page: discover. Selector: `nav Download`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.25 x 32 | = | - | = |
| Padding | 4px 12px | = | - | = |
| Gap | normal 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 6px | = | - | = |
| Background | #26bbff | #72d3ff | - | #72d3ff |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span.label: Inter 14px/24px 500, #000000, ls 0.28px | = | - | = |
| Transition | color, background-color 0.12s cubic-bezier(0.65, 0, 0.35, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.cta-button.cta-button-primary 95.3x32.0 bg #26bbff r 6px | a.cta-button.cta-button-primary 95.3x32.0 bg #72d3ff r 6px | - | a.cta-button.cta-button-primary 95.3x32.0 bg #72d3ff r 6px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-download-default.png`, `nav-download-hover.png`, `nav-download-pressed.png`.

#### nav-distribute

Distribute menu. The Distribute dropdown in the global nav; measured, never opened.

Page: discover. Selector: `nav Distribute`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116.81 x 41 | = | - | = |
| Padding | 10px 16px | = | - | = |
| Gap | normal 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | #ffffff @ 0.65 | - | #ffffff @ 0.65 |
| Text node | span.label: Inter 14px/21px 400, #ffffff, ls 0.28px | span.label: Inter 14px/21px 400, #ffffff @ 0.65, ls 0.28px | - | span.label: Inter 14px/21px 400, #ffffff @ 0.65, ls 0.28px |
| Transition | color, background-color 0.12s cubic-bezier(0.65, 0, 0.35, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 12 x 12, colour #ffffff | 12 x 12, colour #ffffff @ 0.65 | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-distribute-default.png`, `nav-distribute-hover.png`, `nav-distribute-pressed.png`.

#### nav-locale

Locale button. The globe locale picker in the global nav; measured, never opened.

Page: discover. Selector: `nav globe`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | - | = |
| Padding | 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff @ 0.95 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #ffffff @ 0.65 | - | 24 x 24, colour #ffffff @ 0.65 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-locale-default.png`, `nav-locale-hover.png`, `nav-locale-pressed.png`.

#### m-egs-nav

Global nav (mobile). The <egs-navigation> at 390px.

Page: mobile. Selector: `egs-navigation (390)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| How | at rest |

Crops: `m-egs-nav-default.png`.

### Store shell

#### store-tabs

Store tab bar. The second bar under the global nav: search field plus Discover/Browse/News.

Page: discover. Selector: `nav._topNav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 100 |
| Padding | 5px 0px |
| Border | none |
| Radius | 0px |
| Background | #101014 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.95 |
| Text node | span: Inter 14px/23.1px 400, #ffffff @ 0.95, ls 0.28px |
| Transition | none |
| Icon | 0 x 0, colour #ffffff @ 0.95, fill #000000 |
| Painted layers | nav._topNav_mrobj_25 1425.0x100.0 bg #101014; input.eds_370_lhwwra6.eds_370_j232ue2 0.0x0.0 bg #202024 r 9999px; input.eds_370_lhwwra6.eds_370_j232ue2 230.0x40.0 bg #202024 r 9999px |
| Ancestor paint | 1 up body.eds_370_m0fvud0.isDesktopUa bg #101014 |
| How | at rest |

Crops: `store-tabs-default.png`.

#### store-tab

Store tab. The active "Discover" tab link; measured, never followed.

Page: discover. Selector: `a.navLink Discover`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.25 x 43.09 | = | = | = |
| Padding | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff @ 0.95 offset 2px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Text node | span: Inter 14px/23.1px 400, #ffffff @ 0.95, ls 0.28px | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | default | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._navLink_mrobj_135.active 81.3x43.1 r 2px outline 1px solid #ffffff @ 0.95 offset 2px | = |

Crops: `store-tab-default.png`, `store-tab-hover.png`, `store-tab-focus-visible.png`, `store-tab-pressed.png`.

#### search-field

Search field. The "Search store" field in the store tab bar; focused and typed into then cleared — never submitted.

Page: discover. Selector: `store search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 230 x 40 | = | = |
| Padding | 0px 13.6px 0px 39.95px | = | 0px 40px 0px 39.95px |
| Border | none | = | = |
| Radius | 9999px | = | = |
| Background | #202024 | #404044 | #404044 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Arial 13.3333px/18.6666px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff @ 0.65, opacity 1 | = | = |
| Painted layers | input.eds_370_lhwwra6.eds_370_j232ue2 230.0x40.0 bg #202024 r 9999px | input.eds_370_lhwwra6.eds_370_j232ue2 230.0x40.0 bg #404044 r 9999px | input.eds_370_lhwwra6.eds_370_j232ue2 230.0x40.0 bg #404044 r 9999px |
| How | at rest | clicked into the field | typed "fort", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

### Discover

#### hero-slide

Hero slide. The giant carousel slide (art + promo copy + Save Now) on Discover; measured, never followed.

Page: discover. Selector: `a.slideLink`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 868.75 x 488.67 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div::before.eds_370_127iqd00.eds_370_127iqd01 695pxx488.672px image linear-gradient(270deg, #0b0b0b @ 0 0%, #0b0b0b 100%) r 0px 16px 16px 0px; button.eds_370_3ezmi30.eds_370_3ezmi31 111.3x48.0 bg #ffffff r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 119.25pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px |
| How | at rest |

Crops: none.

#### hero-cta

Hero CTA. The white "Save Now" pill on the hero slide; measured, never followed.

Page: discover. Selector: `hero Save Now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111.25 x 48 | = | - | = |
| Padding | 0px 20px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 10px | = | - | = |
| Background | #ffffff | #a6a6a6 | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/19.6px 500 | = | - | = |
| Letter spacing | 0.28px | = | - | = |
| Colour | #000000 @ 0.95 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| ::before | 119.25px x 56px, absolute, bg #000000 @ 0, radius 14px | = | - | = |
| ::after | 111.25px x 48px, absolute, bg #000000 @ 0, radius 0px | = | - | = |
| Painted layers | button.eds_370_3ezmi30.eds_370_3ezmi31 111.3x48.0 bg #ffffff r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 119.25pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | button.eds_370_3ezmi30.eds_370_3ezmi31 111.3x48.0 bg #a6a6a6 r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 119.25pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Text node | - | span.eds_370_3ezmi3f: Inter 14px/19.6px 500, #000000 @ 0.95, ls 0.28px | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `hero-cta-hover.png`, `hero-cta-pressed.png`.

#### carousel-thumb

Carousel rail item. A thumbnail button in the hero carousel rail ("Go to slide N"); measured, its own slide state pressed by hover only.

Page: discover. Selector: `button.carouselButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 78.95 | = | = | = |
| Padding | 0px 10px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #28282c | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 400 | Arial 13.3333px/normal 400 | Arial 13.3333px/normal 400 | Arial 13.3333px/normal 400 |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.95 | #000000 | #000000 | #000000 |
| Text node | span.eds_370_cbt6nt0.eds_370_j232ue1: Inter 14px/19.6px 400, #ffffff @ 0.95, ls 0.28px | = | = | = |
| Transition | transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a._carouselButton_1cvo7_522._activeCarouselButton_1cvo7_542 180.0x79.0 bg #28282c r 8px; div._progressBar_1cvo7_615 141.0x79.0 bg #404044 | button._carouselButton_1cvo7_522 180.0x79.0 bg #28282c r 8px | button._carouselButton_1cvo7_522 180.0x79.0 bg #28282c r 8px | button._carouselButton_1cvo7_522 180.0x79.0 bg #28282c r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-thumb-default.png`, `carousel-thumb-hover.png`, `carousel-thumb-focus-visible.png`, `carousel-thumb-pressed.png`.

#### pager-next

Carousel pager. The right-chevron "Next page" rail control under a card shelf.

Page: discover. Selector: `button[aria-label="Next page"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.15 | #ffffff @ 0.35 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff @ 0.95 | = | = | = |
| ::before | 38px x 38px, absolute, bg #000000 @ 0, radius 9999px | = | = | = |
| ::after | 30px x 30px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.eds_370_3ezmi30.eds_370_3ezmi33 30.0x30.0 bg #ffffff @ 0.15 r 9999px; button::before.eds_370_3ezmi30.eds_370_3ezmi33 38pxx38px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 9999px | button.eds_370_3ezmi30.eds_370_3ezmi33 30.0x30.0 bg #ffffff @ 0.35 r 9999px; button::before.eds_370_3ezmi30.eds_370_3ezmi33 38pxx38px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 9999px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pager-next-default.png`, `pager-next-hover.png`, `pager-next-focus-visible.png`, `pager-next-pressed.png`.

#### game-card

Game card. A store card (cover, title, price line, wishlist corner) in a Discover shelf; measured, never followed.

Page: discover. Selector: `a.cardLink`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 335.38 x 100 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset -1px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._cardLink_1k614_83 335.4x100.0 r 8px outline 1px solid #ffffff offset -1px | = |

Crops: `game-card-default.png`, `game-card-hover.png`, `game-card-focus-visible.png`, `game-card-pressed.png`.

#### card-price

Price line. The price/Free/Coming-Soon line inside a game card (region-priced, SGD on this run).

Page: discover. Selector: `card price span`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32.13 x 19.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/19.6px 500 |
| Letter spacing | 0.28px |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `card-price-default.png`.

#### card-wishlist

Card wishlist button. The plus-corner "Add … to wishlist" icon button on a card; measured, never toggled.

Page: discover. Selector: `button[aria-label*="wishlist"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 10px | = | - | = |
| Background | #ffffff @ 0.15 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/19.6px 500 | = | - | = |
| Letter spacing | 0.28px | = | - | = |
| Colour | #ffffff @ 0.95 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 20 x 20, colour #ffffff @ 0.95 | = | - | = |
| ::before | 56px x 56px, absolute, bg #000000 @ 0, radius 14px | = | - | = |
| ::after | 48px x 48px, absolute, bg #000000 @ 0, radius 0px | = | - | = |
| Painted layers | button.eds_370_3ezmi30.eds_370_3ezmi31 48.0x48.0 bg #ffffff @ 0.15 r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 56pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `card-wishlist-hover.png`, `card-wishlist-pressed.png`.

#### view-more

View More. The shelf "View More" ghost button; measured, never followed.

Page: discover. Selector: `View More`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.53 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #ffffff | #a6a6a6 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #000000 @ 0.95 | = | = | = |
| Text node | span.eds_370_3ezmi3f: Inter 14px/19.6px 500, #000000 @ 0.95, ls 0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 125.531px x 56px, absolute, bg #000000 @ 0, radius 14px | = | = | = |
| ::after | 117.531px x 48px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.eds_370_3ezmi30.eds_370_3ezmi31 117.5x48.0 bg #ffffff r 10px; a::before.eds_370_3ezmi30.eds_370_3ezmi31 125.531pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | a.eds_370_3ezmi30.eds_370_3ezmi31 117.5x48.0 bg #a6a6a6 r 10px; a::before.eds_370_3ezmi30.eds_370_3ezmi31 125.531pxx56px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `view-more-default.png`, `view-more-hover.png`, `view-more-focus-visible.png`, `view-more-pressed.png`.

### Footer

#### egs-footer

Global footer. The <egs-footer> web component at the bottom of every store page.

Page: discover. Selector: `egs-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 878 |
| Padding | 80px 64px |
| Gap | 40px |
| Border | none |
| Radius | 0px |
| Background | #18181c |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.65 |
| Transition | none |
| Painted layers | footer.global-footer 1425.0x878.0 bg #18181c; hr 1297.0x1.0 bg #ffffff @ 0.15; hr 1297.0x1.0 bg #ffffff @ 0.15 |
| How | at rest |

Crops: `egs-footer-default.png`.

### Browse (legacy grid)

#### b-h1

Browse heading. "Popular Genres" — the display heading on the legacy browse page (a second "Browse" h1 is screen-reader-only).

Page: browse. Selector: `h1 Popular Genres`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 237 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 32px/40px 900 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Inter Tight 32px/40px 900, #ffffff |
| Transition | none |
| How | at rest |

Crops: `b-h1-default.png`.

#### b-genre-card

Genre card. A "Popular Genres" tile (art + label) linking to a filtered browse; measured, never followed.

Page: browse. Selector: `a genre tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 255 x 229.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.css-1wdw11k: Inter 16px/26.4px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 255px x 229.797px, absolute, bg #000000 @ 0, radius 4px | = | = | = |
| Painted layers | a::before.css-c255xm 255pxx229.797px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div.css-1u94dle 255.0x229.8 bg #18181c r 12px; div::before.css-1u94dle 255pxx229.797px bg #202024; div.css-np40za 102.0x136.0 bg #18181c r 4px; div.css-np40za 102.0x136.0 bg #18181c r 4px; div::before.css-np40za 102pxx135.984px image linear-gradient(270deg, #000000 0%, #000000 @ 0 100%) | a::before.css-c255xm 255pxx229.797px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div.css-1u94dle 255.0x229.8 bg #18181c r 12px; div::before.css-1u94dle 255pxx229.797px bg #404044; div.css-np40za 102.0x136.0 bg #18181c r 4px; div.css-np40za 102.0x136.0 bg #18181c r 4px; div::before.css-np40za 102pxx135.984px image linear-gradient(270deg, #000000 0%, #000000 @ 0 100%) | a::before.css-c255xm 255pxx229.797px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 4px; div.css-1u94dle 255.0x229.8 bg #18181c r 12px; div::before.css-1u94dle 255pxx229.797px bg #202024; div.css-np40za 102.0x136.0 bg #18181c r 4px; div.css-np40za 102.0x136.0 bg #18181c r 4px; div::before.css-np40za 102pxx135.984px image linear-gradient(270deg, #000000 0%, #000000 @ 0 100%) | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `b-genre-card-default.png`, `b-genre-card-hover.png`, `b-genre-card-focus-visible.png`, `b-genre-card-pressed.png`.

#### b-sort

Sort dropdown. The "New Release" sort control above the grid; opened with its own toggle for the listbox state — an option was never picked.

Page: browse. Selector: `sort button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 126.09 x 30 | = | = | = | = |
| Padding | 0px 5px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ffffff | = | 1px solid #ffffff |
| Radius | 0px | = | 4px | = | 4px |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Inter 14px/20px 400 | = | = | = | = |
| Letter spacing | 0.2px | = | = | = | = |
| Colour | #ffffff | = | = | #ffffff @ 0.65 | = |
| Text node | span: Inter 14px/19.6px 400, #ffffff, ls 0.28px | = | = | = | = |
| Transition | color, border 0s, 0.2s ease, ease delay 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | 18 x 18, colour #ffffff @ 0.65 | = |
| Painted layers | button.css-1nhz626 126.1x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | = | button.css-1nhz626 126.1x30.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 4px | = | button.css-1nhz626 126.1x30.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `b-sort-default.png`, `b-sort-hover.png`, `b-sort-focus-visible.png`, `b-sort-pressed.png`, `b-sort-opened.png`.

#### b-sort-item

Sort option. An option inside the opened sort menu (button[role=menuitem]); measured, never picked.

Page: browse. Selector: `sort menuitem`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 150.05 x 40.59 |
| Padding | 10px 12px |
| Border | none |
| Radius | 8px |
| Background | #ffffff @ 0.15 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Inter 14px/19.6px 400, #ffffff, ls 0.28px |
| Transition | background-color 0.125s ease-in-out |
| Cursor | pointer |
| ::before | 150.047px x 40.5938px, absolute, bg #000000 @ 0, radius 4px |
| Painted layers | button.css-1htphds 150.0x40.6 bg #ffffff @ 0.15 r 8px; button::before.css-1htphds 150.047pxx40.5938px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| Ancestor paint | 2 up ul.css-w8t11w.egs-menu-dense bg #303034 shadow #000000 @ 0.1 0px 2px 1px 0px, #000000 @ 0.1 0px 4px 2px 0px, #000000 @ 0.1 0px 8px 4px 0px, #000000 @ 0.1 0px 16px 8px 0px, #000000 @ 0.1 0px 32px 16px 0px; 3 up div.eds_xd1k8g0.css-r84oom bg #303034 shadow #000000 @ 0.1 0px 2px 1px 0px, #000000 @ 0.1 0px 4px 2px 0px, #000000 @ 0.1 0px 8px 4px 0px, #000000 @ 0.1 0px 16px 8px 0px, #000000 @ 0.1 0px 32px 16px 0px |
| How | at rest |

Crops: `b-sort-item-default.png`.

#### b-card

Grid game card. A game card in the legacy browse grid (cover, title, price, wishlist corner); measured, never followed.

Page: browse. Selector: `browse grid card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 193.75 x 370.42 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span: Inter 12px/18px 400, #ffffff @ 0.65, ls 0.24px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 193.75px x 370.422px, absolute, bg #000000 @ 0, radius 4px | = | = | = |
| Painted layers | a::before.css-1k3j1r9 193.75pxx370.422px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div.css-3f7x5i 193.8x258.3 image linear-gradient(#202024, #18181c) r 8px; div::after.css-3f7x5i 193.75pxx258.328px bg #ffffff; div.eds_1xxntt80.eds_1be5iuz0 47.0x20.0 bg #26bbff r 9999px | = | a::before.css-1k3j1r9 193.75pxx370.422px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 4px; div.css-3f7x5i 193.8x258.3 image linear-gradient(#202024, #18181c) r 8px; div::after.css-3f7x5i 193.75pxx258.328px bg #ffffff; div.eds_1xxntt80.eds_1be5iuz0 47.0x20.0 bg #26bbff r 9999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `b-card-default.png`, `b-card-hover.png`, `b-card-focus-visible.png`, `b-card-pressed.png`.

#### b-wishlist

Grid wishlist button. The "Add to Wishlist" corner button on a grid card; measured, never toggled.

Page: browse. Selector: `button[aria-label="Add to Wishlist"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #ffffff | = | = | = |
| Painted layers | div.css-8gd9c6 20.0x20.0 bg #101014 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 50% | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `b-wishlist-default.png`, `b-wishlist-hover.png`, `b-wishlist-focus-visible.png`, `b-wishlist-pressed.png`.

#### b-filters

Filters rail. The right-hand Filters aside: Events/Genre/Features/Types/Platform/Subscriptions accordions over a filter search.

Page: browse. Selector: `aside Filters`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 240 x 4509.72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.eds_1ypbntd0.eds_1ypbntd7: Inter Tight 16px/20px 700, #ffffff, ls 0.32px |
| Transition | none |
| Icon | 13 x 13, colour #ffffff, fill #000000 |
| Painted layers | div.css-15uavpg 240.0x500.0 bg #202024 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 12px; div::after.css-1n0v0ym 238pxx1px bg #ffffff @ 0.15; input.css-7bziss 206.0x40.0 bg #303034 r 4px; input::before.css-7bziss 100%x100% border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div::after.css-1n0v0ym 238pxx1px bg #ffffff @ 0.15; button.css-x5dpzf 238.0x62.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest |

Crops: `b-filters-default.png`.

#### b-filter-group

Filter accordion. The "Genre" collapsible in the Filters rail; opened with its own toggle for the checkbox group — nothing was checked.

Page: browse. Selector: `Genre accordion button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 238 x 62 | = | = | = | = |
| Padding | 20px 16px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ffffff | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | #ffffff @ 0.15 | = | #ffffff @ 0.15 | #ffffff @ 0.15 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff @ 0.65 | = | = | = | = |
| Text node | span.eds_1ypbntd0.eds_1ypbntdc: Inter 14px/19.6px 400, #ffffff, ls 0.28px | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #ffffff @ 0.65 | = | = | = | = |
| Painted layers | button.css-x5dpzf 238.0x62.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | button.css-x5dpzf 238.0x62.0 bg #ffffff @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | button.css-x5dpzf 238.0x62.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff | button.css-x5dpzf 238.0x62.0 bg #ffffff @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 | button.css-x5dpzf 238.0x62.0 bg #ffffff @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `b-filter-group-default.png`, `b-filter-group-hover.png`, `b-filter-group-focus-visible.png`, `b-filter-group-pressed.png`, `b-filter-group-opened.png`.

#### b-checkbox

Filter checkbox. A checkbox row inside the opened Genre group (the control is a styled div, the input is visually hidden); never checked.

Page: browse. Selector: `genre checkbox row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 206 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.eds_1ypbntd0.eds_1ypbntdc: Inter 14px/19.6px 400, #ffffff @ 0.65, ls 0.28px |
| Transition | none |
| Painted layers | button.eds_52a16m7.eds_52a16m8 20.0x20.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.35 / R:1px solid #ffffff @ 0.35 / B:1px solid #ffffff @ 0.35 / L:1px solid #ffffff @ 0.35 r 4px |
| How | at rest |

Crops: `b-checkbox-default.png`.

#### b-filter-search

Filter search. The "Filters" keyword field at the top of the rail; focused, never submitted.

Page: browse. Selector: `filters input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 206 x 40 | = |
| Padding | 0px 30px 0px 40px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | #303034 | #28282c |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | background 0.125s ease-in-out |
| Cursor | text | = |
| Placeholder | #ffffff @ 0.65, opacity 1 | = |
| ::before | 100% x 100%, absolute, bg #000000 @ 0, radius 4px | = |
| Painted layers | input.css-7bziss 206.0x40.0 bg #303034 r 4px; input::before.css-7bziss 100%x100% border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | input.css-7bziss 206.0x40.0 bg #28282c r 4px; input::before.css-7bziss 100%x100% border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 4px |
| How | at rest | clicked into the field |

Crops: `b-filter-search-default.png`, `b-filter-search-focused.png`.

#### b-pagination

Pagination. The numbered pagination under the grid.

Page: browse. Selector: `pagination nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 823 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/19.6px 400 |
| Letter spacing | 0.2px |
| Colour | #ffffff |
| Text node | a.eds_wy6w1n0.eds_1be5iuz0: Inter 14px/19.6px 400, #ffffff, ls 0.2px |
| Transition | none |
| Icon | 12 x 12, colour #ffffff, fill #000000 |
| Painted layers | button::before.css-bp4ej3 30pxx30px bg #ffffff @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100% |
| How | at rest |

Crops: `b-pagination-default.png`.

#### b-page-link

Page number. A page number inside the pagination; measured, never followed.

Page: browse. Selector: `pagination item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 27.2 x 19.59 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 4px | = |
| Font | Inter 14px/19.6px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.eds_wy6w1n0.eds_1be5iuz0 27.2x19.6 r 4px outline 2px solid #ffffff offset 4px | = |

Crops: `b-page-link-default.png`, `b-page-link-hover.png`, `b-page-link-focus-visible.png`, `b-page-link-pressed.png`.

### Product page

#### p-title

Product title. The game title heading (Fortnite) at the top of the product page.

Page: product. Selector: `product h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1068.75 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/48px 700 |
| Letter spacing | -1px |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| How | at rest |

Crops: `p-title-default.png`.

#### p-rating

Rating block. The "4.3" Epic Player Ratings strip with its audience descriptors.

Page: product. Selector: `rating block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 535.73 x 20 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.95 |
| Text node | span.eds_370_cbt6nt0.eds_370_j232ue1: Inter 14px/19.6px 400, #ffffff @ 0.95, ls 0.28px |
| Transition | none |
| Icon | 15 x 14, colour #ffffff @ 0.95, fill #000000 |
| How | at rest |

Crops: `p-rating-default.png`.

#### p-subnav

Product tab. The active "Overview" tab in the product subnav (Overview/Add-Ons/Experiences/FAQ); measured, never followed.

Page: product. Selector: `subnav Overview`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69 x 28 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff @ 0.95 | = | - | = |
| Text node | a._navLink_1x0oj_41._active_1x0oj_62: Inter 16px/28px 400, #ffffff @ 0.95 | = | - | = |
| Transition | none | = | - | = |
| Painted layers | a::after._navLink_1x0oj_41._active_1x0oj_62 69pxx2px bg #33bfff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `p-subnav-default.png`, `p-subnav-hover.png`, `p-subnav-pressed.png`.

#### p-stage-next

Gallery arrow. The right "Next image" arrow over the media stage; measured, never pressed.

Page: product. Selector: `button[aria-label="Next image"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | = | = | = |
| Padding | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset -2px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 36 x 36, colour #ffffff @ 0.95 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button._stageButton_1361s_127 56.0x56.0 r 4px outline 2px solid #ffffff offset -2px | = |

Crops: `p-stage-next-default.png`, `p-stage-next-hover.png`, `p-stage-next-focus-visible.png`, `p-stage-next-pressed.png`.

#### p-thumb

Gallery thumbnail. A thumbnail button in the media strip ("Slide N of 9"); measured, never pressed.

Page: product. Selector: `button.thumbnail`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 88.78 x 49.94 |
| Padding | 0px |
| Border | 2px solid #ffffff |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | border-color 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | pointer |
| Painted layers | button._thumbnail_1361s_231._thumbnailActive_1361s_294 88.8x49.9 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 4px |
| How | at rest |

Crops: `p-thumb-default.png`.

#### p-get

Get button. The blue "Get" primary action in the buy panel; measured, never pressed.

Page: product. Selector: `buy panel Get`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 270 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #33bfff | #69d0ff | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #0a2633 | = | = | = |
| Text node | span.eds_370_3ezmi3f: Inter 14px/19.6px 500, #0a2633, ls 0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 278px x 48px, absolute, bg #000000 @ 0, radius 12px | = | = | = |
| ::after | 270px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.eds_370_3ezmi30.eds_370_3ezmi32 270.0x40.0 bg #33bfff r 8px; button::before.eds_370_3ezmi30.eds_370_3ezmi32 278pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | button.eds_370_3ezmi30.eds_370_3ezmi32 270.0x40.0 bg #69d0ff r 8px; button::before.eds_370_3ezmi30.eds_370_3ezmi32 278pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `p-get-default.png`, `p-get-hover.png`, `p-get-focus-visible.png`, `p-get-pressed.png`.

#### p-cart

Add to Cart. The square "Add to Cart" icon button beside Get; measured, never pressed.

Page: product. Selector: `buy panel Add to Cart`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 311.66 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #33bfff | #69d0ff | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #0a2633 | = | = | = |
| Text node | span.eds_370_3ezmi3f: Inter 14px/19.6px 500, #0a2633, ls 0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 319.656px x 48px, absolute, bg #000000 @ 0, radius 12px | = | = | = |
| ::after | 311.656px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.eds_370_3ezmi30.eds_370_3ezmi32 311.7x40.0 bg #33bfff r 8px; button::before.eds_370_3ezmi30.eds_370_3ezmi32 319.656pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | button.eds_370_3ezmi30.eds_370_3ezmi32 311.7x40.0 bg #69d0ff r 8px; button::before.eds_370_3ezmi30.eds_370_3ezmi32 319.656pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `p-cart-default.png`, `p-cart-hover.png`, `p-cart-focus-visible.png`, `p-cart-pressed.png`.

#### p-wishlist

Wishlist button. The outlined "Wishlist" button under the buy panel; measured, never pressed.

Page: product. Selector: `buy panel Wishlist`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff @ 0.15 | #ffffff @ 0.35 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Text node | span.eds_370_3ezmi3f: Inter 14px/19.6px 500, #ffffff @ 0.95, ls 0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff @ 0.95 | = | = | = |
| ::before | 328px x 48px, absolute, bg #000000 @ 0, radius 12px | = | = | = |
| ::after | 320px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.eds_370_3ezmi30.eds_370_3ezmi32 320.0x40.0 bg #ffffff @ 0.15 r 8px; button::before.eds_370_3ezmi30.eds_370_3ezmi32 328pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | button.eds_370_3ezmi30.eds_370_3ezmi32 320.0x40.0 bg #ffffff @ 0.35 r 8px; button::before.eds_370_3ezmi30.eds_370_3ezmi32 328pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `p-wishlist-default.png`, `p-wishlist-hover.png`, `p-wishlist-focus-visible.png`, `p-wishlist-pressed.png`.

#### p-price

Buy price. The "Free"/price line above the buy actions.

Page: product. Selector: `buy price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36.64 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 700 |
| Letter spacing | 0.16px |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| How | at rest |

Crops: `p-price-default.png`.

#### p-share

Share button. The "Share" ghost button beside Report in the buy rail; measured, never pressed.

Page: product. Selector: `buy rail Share`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff @ 0.15 | #ffffff @ 0.35 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Text node | span.eds_370_3ezmi3f: Inter 14px/19.6px 500, #ffffff @ 0.95, ls 0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff @ 0.95 | = | = | = |
| ::before | 163px x 40px, absolute, bg #000000 @ 0, radius 10px | = | = | = |
| ::after | 155px x 32px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.eds_370_3ezmi30.eds_370_3ezmi33 155.0x32.0 bg #ffffff @ 0.15 r 6px; button::before.eds_370_3ezmi30.eds_370_3ezmi33 163pxx40px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 10px | button.eds_370_3ezmi30.eds_370_3ezmi33 155.0x32.0 bg #ffffff @ 0.35 r 6px; button::before.eds_370_3ezmi30.eds_370_3ezmi33 163pxx40px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 10px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `p-share-default.png`, `p-share-hover.png`, `p-share-focus-visible.png`, `p-share-pressed.png`.

#### p-tag

Tag chip. A genre tag chip under the description; links to a filtered browse, measured never followed.

Page: product. Selector: `tag chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.38 x 24 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.15 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 12px/15.6px 400 | = | = | = |
| Letter spacing | 0.36px | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Text node | span.eds_370_19um2dp20: Inter 12px/15.6px 400, #ffffff @ 0.95, ls 0.36px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.eds_370_19um2dp0.eds_370_j232ue2 58.4x24.0 bg #ffffff @ 0.15 r 9999px | = | a.eds_370_19um2dp0.eds_370_j232ue2 58.4x24.0 bg #ffffff @ 0.15 r 9999px; a::before.eds_370_19um2dp0.eds_370_j232ue2 66.375pxx32px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 9999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::before | - | = | 66.375px x 32px, absolute, bg #000000 @ 0, radius 9999px | = |

Crops: `p-tag-default.png`, `p-tag-hover.png`, `p-tag-focus-visible.png`, `p-tag-pressed.png`.

#### p-ratings-badge

Ratings badge. The age-ratings badge link (globalratings.com); measured, never followed.

Page: product. Selector: `ratings badge link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 78.78 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._imageSlot_l9bj1_58._imageSlot_lg_l9bj1_63 46.0x78.8 outline 1px auto #101010 offset 1px | = |

Crops: `p-ratings-badge-default.png`, `p-ratings-badge-hover.png`, `p-ratings-badge-focus-visible.png`, `p-ratings-badge-pressed.png`.

#### p-h2

Section heading. A section heading inside the product overview.

Page: product. Selector: `product h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 684.75 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/24px 700 |
| Letter spacing | -0.3px |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| How | at rest |

Crops: `p-h2-default.png`.

#### p-addon-row

Add-on row. An Add-Ons/Experiences row (art, title, Add-to-Cart, wishlist); measured, never followed.

Page: product. Selector: `add-on row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 367.66 x 44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff @ 0.95 | = |
| Text node | span.eds_370_cbt6nt0.eds_370_j232ue1: Inter 12px/15.6px 400, #ffffff @ 0.65, ls 0.36px | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `p-addon-row-default.png`, `p-addon-row-hover.png`.

#### p-sysreq-tab

Requirements tab. A platform tab in System Requirements; measured, never switched.

Page: product. Selector: `sysreq tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61.97 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 400 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 61.9688px x 2px, absolute, bg #33bfff, radius 2px | = | = | = |
| Painted layers | button::before.eds_370_1lstq850.eds_370_j232ue0 61.9688pxx2px bg #33bfff r 2px | = | button::before.eds_370_1lstq850.eds_370_j232ue0 61.9688pxx2px bg #33bfff r 2px; button::after.eds_370_1lstq850.eds_370_j232ue0 69.9688pxx24px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 5px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 69.9688px x 24px, absolute, bg #000000 @ 0, radius 5px | = |

Crops: `p-sysreq-tab-default.png`, `p-sysreq-tab-hover.png`, `p-sysreq-tab-focus-visible.png`, `p-sysreq-tab-pressed.png`.

#### p-follow

Follow icon. A social icon link in Follow Us (Discord/homepage); measured, never followed.

Page: product. Selector: `follow icon link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 28.64 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 1px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 4px | = |
| Font | Inter 16px/26.4px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Transition | color, transform 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 28 x 28, colour #ffffff @ 0.95 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | matrix(1, 0, 0, 1, 0, -1) | matrix(1, 0, 0, 1, 0, -1) |
| Painted layers | - | = | a.eds_370_eifnjs0.eds_370_j232ue0 32.0x28.6 r 1px outline 2px solid #ffffff offset 4px | = |

Crops: `p-follow-default.png`, `p-follow-hover.png`, `p-follow-focus-visible.png`, `p-follow-pressed.png`.

### Free games

#### fg-h1

Free Games heading. The "Free Games" display heading (the h1 itself is screen-reader-only).

Page: freegames. Selector: `free-games heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 226 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 40px/50px 900 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `fg-h1-default.png`.

#### fg-cta

Giveaway CTA. The blue "Install Mobile and Claim Now" action in the Free Giveaway panel; links out to the mobile app, measured never followed.

Page: freegames. Selector: `free giveaway CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264.84 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #26bbff | #72d3ff | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.css-qkjsuf: Inter 14px/19.6px 500, #000000, ls 0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| Painted layers | a.eds_14hl3lj9.eds_14hl3ljb 264.8x40.0 bg #26bbff r 8px | a.eds_14hl3lj9.eds_14hl3ljb 264.8x40.0 bg #72d3ff r 8px | a.eds_14hl3lj9.eds_14hl3ljb 264.8x40.0 bg #26bbff r 8px; a::before.eds_14hl3lj9.eds_14hl3ljb 272.844pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::before | - | = | 272.844px x 48px, absolute, bg #000000 @ 0, radius 12px | = |

Crops: `fg-cta-default.png`, `fg-cta-hover.png`, `fg-cta-focus-visible.png`, `fg-cta-pressed.png`.

#### fg-card

Free game card. A "Free Now"/"Coming Soon" game card on the free-games shelf; measured, never followed.

Page: freegames. Selector: `free-games card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 346.67 x 301.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter 12px/15.9996px 700, #000000, ls 0.5px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a::before.css-1k3j1r9 346.672pxx291.406px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div.css-u3z0tz 346.7x195.0 image linear-gradient(#202024, #18181c) r 8px; div::after.css-u3z0tz 346.672pxx195px bg #ffffff; div.css-82y1uz 346.7x26.0 bg #26bbff | = | a::before.css-1k3j1r9 346.672pxx291.406px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 4px; div.css-u3z0tz 346.7x195.0 image linear-gradient(#202024, #18181c) r 8px; div::after.css-u3z0tz 346.672pxx195px bg #ffffff; div.css-82y1uz 346.7x26.0 bg #26bbff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `fg-card-default.png`, `fg-card-hover.png`, `fg-card-focus-visible.png`, `fg-card-pressed.png`.

#### fg-badge

Free-now badge. The "Free Now - <date>" status label on a free-games card.

Page: freegames. Selector: `Free Now badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 240 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/26.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.65 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `fg-badge-default.png`.

### News

#### n-h1

News heading. The "Epic Games News" heading.

Page: news. Selector: `news heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 25.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/25.2px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Inter 18px/25.2px 700, #ffffff |
| Transition | none |
| How | at rest |

Crops: `n-h1-default.png`.

#### n-card

Article card. A news article card (hero image, "Nd ago", headline, Read more); measured, never followed.

Page: news. Selector: `news article card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 530 x 438.94 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.css-2jxatg: Inter 9px/normal 500, #ffffff @ 0.65, ls 1px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div::after.css-1kqz5m5 530pxx298.125px image linear-gradient(0deg, #ffffff @ 0.2, #ffffff @ 0.2); span.css-6xq2vb 81.0x21.0 border B:1px solid #ffffff @ 0.2 | = | a 530.0x298.1 outline 1px auto #101010 offset 1px; div::after.css-1kqz5m5 530pxx298.125px image linear-gradient(0deg, #ffffff @ 0.2, #ffffff @ 0.2); span.css-6xq2vb 81.0x21.0 border B:1px solid #ffffff @ 0.2 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `n-card-default.png`, `n-card-hover.png`, `n-card-focus-visible.png`, `n-card-pressed.png`.

#### n-readmore

Read more link. The "Read more" caption link inside an article card; measured, never followed.

Page: news. Selector: `Read more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.css-6xq2vb: Inter 16px/normal 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.css-6xq2vb 81.0x21.0 border B:1px solid #ffffff @ 0.2 | span.css-6xq2vb 81.0x21.0 border B:1px solid #ffffff @ 0.996 | a.css-1wb6qud 81.0x21.0 outline 1px auto #101010 offset 1px; span.css-6xq2vb 81.0x21.0 border B:1px solid #ffffff @ 0.2 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `n-readmore-default.png`, `n-readmore-hover.png`, `n-readmore-focus-visible.png`, `n-readmore-pressed.png`.

### Launcher download

#### d-h1

Download heading. The "Download the Epic Games Launcher" heading (the h1 itself is screen-reader-only).

Page: download. Selector: `download heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 52px/65px 900 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `d-h1-default.png`.

#### d-cta

Download CTA. The launcher download action (Windows/Mac); measured, never followed.

Page: download. Selector: `download CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 176.48 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.eds_14hl3lj6: Inter 14px/19.6px 500, #000000, ls 0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| Painted layers | button.eds_14hl3lj9.eds_14hl3ljb 176.5x40.0 bg #26bbff r 8px | button.eds_14hl3lj9.eds_14hl3ljb 176.5x40.0 bg #72d3ff r 8px | a 176.5x20.0 outline 1px auto #101010 offset 1px; button.eds_14hl3lj9.eds_14hl3ljb 176.5x40.0 bg #26bbff r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-cta-default.png`, `d-cta-hover.png`, `d-cta-focus-visible.png`, `d-cta-pressed.png`.

### Sign-in dialog

#### s-dialog

Sign-in dialog. The "Sign in to Epic Games" MUI modal (the MuiPaper card): Epic mark, e-mail field, Continue, console and social providers. Measured as a form, never submitted.

Page: signin. Selector: `signin MuiPaper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 562 x 972.19 |
| Padding | 0px |
| Border | 1px solid #ffffff @ 0.1 |
| Radius | 24px |
| Background | #18181c |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/19.6px 400 |
| Letter spacing | 0.28px |
| Colour | #ffffff @ 0.65 |
| Text node | h1.MuiTypography-root.MuiTypography-h1: Inter Tight 24px/30px 400, #ffffff |
| Transition | box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 45 x 45, colour #ffffff |
| Painted layers | div.MuiPaper-root.MuiPaper-outlined 562.0x972.2 bg #18181c border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 24px; div.MuiInputBase-root.MuiOutlinedInput-root 464.0x48.0 bg #ffffff @ 0.05 r 10px; fieldset.MuiOutlinedInput-notchedOutline.mui-1bhnjrf 464.0x53.0 border T:1px solid #ffffff @ 0.35 / R:1px solid #ffffff @ 0.35 / B:1px solid #ffffff @ 0.35 / L:1px solid #ffffff @ 0.35 r 10px; div.MuiInputBase-root.MuiOutlinedInput-root 1.0x48.0 bg #ffffff @ 0.05 r 10px; fieldset.MuiOutlinedInput-notchedOutline.mui-1bhnjrf 18.0x53.0 border T:1px solid #ffffff @ 0.35 / R:1px solid #ffffff @ 0.35 / B:1px solid #ffffff @ 0.35 / L:1px solid #ffffff @ 0.35 r 10px; button.MuiButtonBase-root.MuiButton-root 464.0x48.0 bg #26bbff r 10px |
| How | at rest |

Crops: `s-dialog-default.png`.

#### s-title

Sign-in title. "Sign in to Epic Games" in the dialog.

Page: signin. Selector: `signin title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 237 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Tight 24px/30px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `s-title-default.png`.

#### s-field-email

Email field. The "Email address" input; focused and typed into then cleared — never submitted.

Page: signin. Selector: `signin email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 463 x 48 | 461 x 48 | 461 x 48 |
| Padding | 13px 20px 12px 20px | = | = |
| Border | none | = | = |
| Radius | 10px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/22.4px 400 | = | = |
| Letter spacing | 0.32px | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #aaaaae, opacity 1 | = | = |
| Ancestor paint | 1 up div.MuiInputBase-root.MuiOutlinedInput-root bg #ffffff @ 0.05 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `s-field-email-default.png`, `s-field-email-focused.png`, `s-field-email-filled.png`.

#### s-continue

Continue button. The blue "Continue" submit; its states were measured but it was never clicked — nothing was submitted.

Page: signin. Selector: `signin Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 464 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #26bbff | #61cdff | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/22.4px 500 | = | = | = |
| Letter spacing | 0.32px | = | = | = |
| Colour | #101014 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 464px x 48px, absolute, bg #000000 @ 0, radius 14px | = | 474px x 58px, absolute, bg #000000 @ 0, radius 14px | = |
| Painted layers | button.MuiButtonBase-root.MuiButton-root 464.0x48.0 bg #26bbff r 10px; button::before.MuiButtonBase-root.MuiButton-root 464pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | button.MuiButtonBase-root.MuiButton-root 464.0x48.0 bg #61cdff r 10px; button::before.MuiButtonBase-root.MuiButton-root 464pxx48px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | button.MuiButtonBase-root.MuiButton-root 464.0x48.0 bg #26bbff r 10px; button::before.MuiButtonBase-root.MuiButton-root 474pxx58px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `s-continue-default.png`, `s-continue-hover.png`, `s-continue-focus-visible.png`, `s-continue-pressed.png`.

#### s-create

Create-account link. The "Create an account" link; measured, never followed.

Page: signin. Selector: `signin Create an account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.77 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 4px | = |
| Font | Inter 14px/23.1px 400 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #26bbff | = | = | #61cdff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.MuiTypography-root.MuiTypography-inherit 130.8x17.0 r 4px outline 2px solid #ffffff offset 4px | = |

Crops: `s-create-default.png`, `s-create-hover.png`, `s-create-focus-visible.png`, `s-create-pressed.png`.

#### s-console

Console provider. A console sign-in tile (PlayStation/Xbox/Nintendo, MuiListItemButton divs); measured, never followed.

Page: signin. Selector: `console provider tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149.33 x 102 | = | = | = |
| Padding | 12px 0px | = | = | = |
| Border | 1px solid #ffffff @ 0.05 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff @ 0.05 | #ffffff @ 0.16 | #ffffff @ 0.16 | #ffffff @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 400 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #ffffff @ 0.65 | = | = | = |
| Text node | p.MuiTypography-root.MuiTypography-body1: Inter 10px/14px 500, #ffffff, ls 0.2px | = | = | = |
| Transition | background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| Painted layers | div.MuiButtonBase-root.MuiListItemButton-root 149.3x102.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px; div.MuiListItemIcon-root.mui-ea0tfe 40.0x40.0 bg #003791 r 50% | div.MuiButtonBase-root.MuiListItemButton-root 149.3x102.0 bg #ffffff @ 0.16 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px; div.MuiListItemIcon-root.mui-ea0tfe 40.0x40.0 bg #003791 r 50% | div.MuiButtonBase-root.MuiListItemButton-root 149.3x102.0 bg #ffffff @ 0.16 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px; div.MuiListItemIcon-root.mui-ea0tfe 40.0x40.0 bg #003791 r 50% | div.MuiButtonBase-root.MuiListItemButton-root 149.3x102.0 bg #ffffff @ 0.16 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px; div.MuiListItemIcon-root.mui-ea0tfe 40.0x40.0 bg #003791 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `s-console-default.png`, `s-console-hover.png`, `s-console-focus-visible.png`, `s-console-pressed.png`.

#### s-social

Social provider. A "Other ways to sign in" provider tile (Google/Steam/Disney/Apple/Facebook/LEGO); measured, never followed.

Page: signin. Selector: `social provider tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149.33 x 88 | = | = | = |
| Padding | 12px 0px | = | = | = |
| Border | 1px solid #ffffff @ 0.05 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff @ 0.05 | #ffffff @ 0.16 | #ffffff @ 0.16 | #ffffff @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 400 | = | = | = |
| Letter spacing | 0.28px | = | = | = |
| Colour | #ffffff @ 0.65 | = | = | = |
| Text node | p.MuiTypography-root.MuiTypography-body1: Inter 10px/14px 500, #ffffff, ls 0.2px | = | = | = |
| Transition | background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 23.86 x 23.72, colour #ffffff @ 0.65 | = | = | = |
| Painted layers | div.MuiButtonBase-root.MuiListItemButton-root 149.3x88.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px; div.MuiListItemIcon-root.mui-141ya6x 40.0x40.0 bg #fefdfd r 50% | div.MuiButtonBase-root.MuiListItemButton-root 149.3x88.0 bg #ffffff @ 0.16 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px; div.MuiListItemIcon-root.mui-141ya6x 40.0x40.0 bg #fefdfd r 50% | div.MuiButtonBase-root.MuiListItemButton-root 149.3x88.0 bg #ffffff @ 0.16 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px; div.MuiListItemIcon-root.mui-141ya6x 40.0x40.0 bg #fefdfd r 50% | div.MuiButtonBase-root.MuiListItemButton-root 149.3x88.0 bg #ffffff @ 0.16 border T:1px solid #ffffff @ 0.05 / R:1px solid #ffffff @ 0.05 / B:1px solid #ffffff @ 0.05 / L:1px solid #ffffff @ 0.05 r 16px; div.MuiListItemIcon-root.mui-141ya6x 40.0x40.0 bg #fefdfd r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `s-social-default.png`, `s-social-hover.png`, `s-social-focus-visible.png`, `s-social-pressed.png`.

### Marketing home

#### w-tile

Product tile. A giant product tile (UNREAL ENGINE / FORTNITE / ROCKET LEAGUE / STORE) with its EXPLORE action on the OpenSans marketing home; measured, never followed.

Page: sitehome. Selector: `marketing tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 480 x 868.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | OpenSans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter_Bold 53.2px/46.55px 600, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-primary 137.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff shadow #000000 @ 0.2 2px 2px 2px 0px | = | a.btn.btn-primary 137.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff shadow #000000 @ 0.2 2px 2px 2px 0px outline 5px auto #101010 offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### w-explore

Explore link. The EXPLORE caption on a product tile; measured, never followed.

Page: sitehome. Selector: `EXPLORE`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137.05 x 32 | = | = | = |
| Padding | 15px 25px | = | = | = |
| Border | 1px solid #ffffff | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #ffffff | = | #ffffff |
| Box shadow | #000000 @ 0.2 2px 2px 2px 0px | = | = | = |
| Outline | none | = | 5px auto #101010 offset -2px | = |
| Font | Helvetica Neue 18px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #222222 | = | #222222 |
| Transition | none | = | = | = |
| Opacity | 0 | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-primary 137.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff shadow #000000 @ 0.2 2px 2px 2px 0px | a.btn.btn-primary 137.0x32.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff shadow #000000 @ 0.2 2px 2px 2px 0px | a.btn.btn-primary 137.0x32.0 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff shadow #000000 @ 0.2 2px 2px 2px 0px outline 5px auto #101010 offset -2px | a.btn.btn-primary 137.0x32.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff shadow #000000 @ 0.2 2px 2px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### w-wordmark

Wordmark. The Epic Games mark on the marketing page.

Page: sitehome. Selector: `marketing wordmark`. States: .

Not found on the page at capture time.

### Support centre

#### h-h1

Help heading. "How can we help?" on the dark support centre.

Page: help. Selector: `help h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 524.17 x 76.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 64px/76.8px 700 |
| Letter spacing | -2.24px |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| How | at rest |

Crops: `h-h1-default.png`.

#### h-search

Support search. The "Search support..." field; focused and typed into then cleared — never submitted.

Page: help. Selector: `help search input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 784 x 40 | = | = |
| Padding | 0px 40px 0px 44px | = | = |
| Border | 1px solid #ffffff @ 0.35 | = | = |
| Radius | 9999px | = | = |
| Background | #ffffff @ 0.05 | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #ffffff offset 2px | 2px solid #ffffff offset 2px |
| Font | Inter 14px/19.6px 400 | = | = |
| Letter spacing | 0.28px | = | = |
| Colour | #ffffff @ 0.95 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff @ 0.65, opacity 1 | = | = |
| Painted layers | input.eds_2111_1malhmw6.eds_2111_1v2sczy2 784.0x40.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.35 / R:1px solid #ffffff @ 0.35 / B:1px solid #ffffff @ 0.35 / L:1px solid #ffffff @ 0.35 r 9999px | input.eds_2111_1malhmw6.eds_2111_1v2sczy2 784.0x40.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.35 / R:1px solid #ffffff @ 0.35 / B:1px solid #ffffff @ 0.35 / L:1px solid #ffffff @ 0.35 r 9999px outline 2px solid #ffffff offset 2px | input.eds_2111_1malhmw6.eds_2111_1v2sczy2 784.0x40.0 bg #ffffff @ 0.05 border T:1px solid #ffffff @ 0.35 / R:1px solid #ffffff @ 0.35 / B:1px solid #ffffff @ 0.35 / L:1px solid #ffffff @ 0.35 r 9999px outline 2px solid #ffffff offset 2px |
| How | at rest | clicked into the field | typed "refund", then deleted; nothing sent |

Crops: `h-search-default.png`, `h-search-focused.png`, `h-search-filled.png`.

#### h-tile

Help tile. A support-category tile (Self-service/Explore topics/Games/Enterprise, a.Tile); measured, never followed.

Page: help. Selector: `help a.Tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 276.23 x 120 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | h5.eds_2111_1ypbntd0.eds_2111_1v2sczy1: Inter 20px/24px 700, #ffffff @ 0.95, ls -0.3px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff @ 0.95 | = | = | = |
| ::before | 284.234px x 128px, absolute, bg #000000 @ 0, radius 20px | = | = | = |
| Painted layers | a::before.Tile.GoToTile 284.234pxx128px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 20px; div.Tile__card.Tile__card--bottom 276.2x120.0 bg #ffffff @ 0.05 r 16px; div.Tile__inside-children 276.2x73.5 image linear-gradient(0deg, #000000, #000000 @ 0.55 67.5%, #000000 @ 0) | a::before.Tile.GoToTile 284.234pxx128px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 20px; div.Tile__card.Tile__card--bottom 276.2x120.0 bg #ffffff @ 0.1 r 16px; div.Tile__inside-children 276.2x73.5 image linear-gradient(0deg, #000000, #000000 @ 0.55 67.5%, #000000 @ 0) | a::before.Tile.GoToTile 284.234pxx128px border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 20px; div.Tile__card.Tile__card--bottom 276.2x120.0 bg #ffffff @ 0.1 r 16px; div.Tile__inside-children 276.2x73.5 image linear-gradient(0deg, #000000, #000000 @ 0.55 67.5%, #000000 @ 0) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `h-tile-default.png`, `h-tile-hover.png`, `h-tile-focus-visible.png`, `h-tile-pressed.png`.

#### h-status

Server status chip. The "Server status" indicator, top right; measured never followed.

Page: help. Selector: `server status`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 98.92 x 19.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/19.6px 400 |
| Letter spacing | 0.28px |
| Colour | #ffffff @ 0.95 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up a.ServerStatus bg #000000 @ 0.35 |
| How | at rest |

Crops: `h-status-default.png`.

#### h-chat

Chat launcher. The round chat button bottom right; measured, never pressed.

Page: help. Selector: `chat bubble`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150.09 x 48 | = | - | = |
| Padding | 12px 20px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | #ffffff @ 0.15 | #ffffff @ 0.35 | - | #ffffff @ 0.35 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/21px 400 | = | - | = |
| Letter spacing | 0.28px | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span.label: Inter 14px/21px 400, #ffffff, ls 0.28px | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | button.footer-button.footer-button-variant-secondary 150.1x48.0 bg #ffffff @ 0.15 r 8px | button.footer-button.footer-button-variant-secondary 150.1x48.0 bg #ffffff @ 0.35 r 8px | - | button.footer-button.footer-button-variant-secondary 150.1x48.0 bg #ffffff @ 0.35 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `h-chat-default.png`, `h-chat-hover.png`, `h-chat-pressed.png`.

### Mobile (390 wide)

#### m-hamburger

Hamburger. The mobile menu button; measured, the drawer itself is captured in screenshots.

Page: mobile. Selector: `mobile menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 32 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 2px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff @ 0.95 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 12 x 12, colour #ffffff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-pressed.png`.

#### m-hero

Mobile hero card. The first card of the mobile store home.

Page: mobile. Selector: `mobile first card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 278.16 x 370.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.95 |
| Text node | span.eds_370_cbt6nt0.eds_370_j232ue1: Inter 10px/12px 700, #ffffff @ 0.95, ls 0.4px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div::before.eds_370_127iqd00.eds_370_127iqd01 278.156pxx370.875px image linear-gradient(#000000 @ 0 30%, #0b0b0b @ 0.4 60%, #0b0b0b @ 0.9 100%) r 16px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 bg #ffffff r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-card

Mobile game card. A game card on the mobile discover feed.

Page: mobile. Selector: `mobile card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 278.16 x 370.88 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Inter 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.95 | = | = | = |
| Text node | span.eds_370_cbt6nt0.eds_370_j232ue1: Inter 10px/12px 700, #ffffff @ 0.95, ls 0.4px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #ffffff @ 0.95 | = | = | = |
| Painted layers | div::before.eds_370_127iqd00.eds_370_127iqd01 278.156pxx370.875px image linear-gradient(#000000 @ 0 30%, #0b0b0b @ 0.4 60%, #0b0b0b @ 0.9 100%) r 16px 0px 0px 16px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 bg #ffffff r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 bg #ffffff @ 0.15 r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px; div.eds_370_127iqd00.eds_370_127iqd01 24.0x24.0 bg #101014 border T:1px solid #ffffff @ 0.95 / R:1px solid #ffffff @ 0.95 / B:1px solid #ffffff @ 0.95 / L:1px solid #ffffff @ 0.95 r 50% shadow #000000 @ 0.6 0px 0px 6px 0px | = | a._slideLink_1cvo7_107._slideLinkActive_1cvo7_124 278.2x370.9 outline 1px auto #e59700 offset 1px; div::before.eds_370_127iqd00.eds_370_127iqd01 278.156pxx370.875px image linear-gradient(#000000 @ 0 30%, #0b0b0b @ 0.4 60%, #0b0b0b @ 0.9 100%) r 16px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 bg #ffffff r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 bg #ffffff @ 0.15 r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px | div::before.eds_370_127iqd00.eds_370_127iqd01 278.156pxx370.875px image linear-gradient(#000000 @ 0 30%, #0b0b0b @ 0.4 60%, #0b0b0b @ 0.9 100%) r 16px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 bg #ffffff r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px; button.eds_370_3ezmi30.eds_370_3ezmi31 0.0x0.0 bg #ffffff @ 0.15 r 10px; button::before.eds_370_3ezmi30.eds_370_3ezmi31 autoxauto border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 14px; div.eds_370_127iqd00.eds_370_127iqd01 24.0x24.0 bg #101014 border T:1px solid #ffffff @ 0.95 / R:1px solid #ffffff @ 0.95 / B:1px solid #ffffff @ 0.95 / L:1px solid #ffffff @ 0.95 r 50% shadow #000000 @ 0.6 0px 0px 6px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-card-default.png`, `m-card-hover.png`, `m-card-focus-visible.png`, `m-card-pressed.png`.

#### m-search

Mobile search. The mobile search field; focused and typed into then cleared — never submitted.

Page: mobile. Selector: `mobile search input`. States: .

Not found on the page at capture time.

## Transitions declared in the readable stylesheets

store.epicgames.com serves its EGS v2 CSS bundle same-origin and the <egs-navigation>/<egs-footer> web components expose their adopted stylesheets, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- browse: `color 0.3s ease-in-out`, `color 0.2s ease-in-out`, `border 0.3s ease-in-out`, `opacity 0.2s`, `0.3s ease-in`, `opacity 0.3s`, `transform 0.2s, right 0.2s`, `visibility, opacity 0.3s ease-in-out`, `0.2s ease-out`, `max-height 350ms, margin 350ms, opacity 350ms, ease-in-out`, `opacity 125ms ease-in-out`, `backgroundColor 125ms ease-in-out`

- discover: `opacity 0.15s ease-in-out`, `gap 0.125s ease-in-out`, `opacity 0.125s ease-in-out`, `grid-template-rows var(--eds_370_adnoafkx) var(--eds_370_adnoafl2)`, `transform var(--eds_370_adnoafkx) var(--eds_370_adnoafl2)`, `none`, `background-color 0.125s ease-in-out`, `height var(--eds_370_adnoafky) var(--eds_370_adnoafl3)`, `opacity 0.4s linear`, `opacity 0.2s`, `filter 0.3s`, `transform 0.2s`

- download: `color 0.3s ease-in-out`, `color 0.2s ease-in-out`, `border 0.3s ease-in-out`, `opacity 0.2s`, `0.3s ease-in`, `opacity 0.3s`, `transform 0.2s, right 0.2s`, `visibility, opacity 0.3s ease-in-out`, `0.2s ease-out`, `opacity 125ms ease-in-out`, `background 125ms ease-in-out`, `border 125ms ease-in-out`

- freegames: `color 0.3s ease-in-out`, `color 0.2s ease-in-out`, `border 0.3s ease-in-out`, `opacity 0.2s`, `0.3s ease-in`, `opacity 0.3s`, `transform 0.2s, right 0.2s`, `visibility, opacity 0.3s ease-in-out`, `0.2s ease-out`, `opacity 125ms ease-in-out`, `backgroundColor 125ms ease-in-out`, `background 125ms ease-in-out`

- help: `background-color 0.3s ease-in-out, padding 0.3s ease-in-out`, `background 0.2s linear, border-color 0.2s linear, color 0.2s linear`, `width 0.3s, height 0.3s`, `opacity 0.4s linear`, `unset`, `border-color 0.2s ease-in-out`, `opacity 0.15s ease-in-out, transform 0.15s ease-in-out`, `0.4s ease-in-out`, `background-color 125ms ease-in-out`

- news: `color 0.3s ease-in-out`, `color 0.2s ease-in-out`, `border 0.3s ease-in-out`, `opacity 0.2s`, `0.3s ease-in`, `opacity 0.3s`, `transform 0.2s, right 0.2s`, `visibility, opacity 0.3s ease-in-out`, `0.2s ease-out`, `background 125ms ease-in-out`, `border 125ms ease-in-out`, `opacity 125ms ease-in-out`

- product: `opacity 0.15s ease-in-out`, `gap 0.125s ease-in-out`, `opacity 0.125s ease-in-out`, `grid-template-rows var(--eds_370_adnoafkx) var(--eds_370_adnoafl2)`, `transform var(--eds_370_adnoafkx) var(--eds_370_adnoafl2)`, `none`, `background-color 0.125s ease-in-out`, `height var(--eds_370_adnoafky) var(--eds_370_adnoafl3)`, `opacity 0.4s linear`, `opacity 0.2s`, `filter 0.3s`, `transform 0.2s`

- signin: `box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)`, `opacity 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `top 100ms, right 100ms, bottom 100ms, left 100ms, border-width 100ms, border-radius 100ms, border-color 100ms`, `width 150ms cubic-bezier(0, 0, 0.2, 1)`, `color 200ms cubic-bezier(0, 0, 0.2, 1), transform 200ms cubic-bezier(0, 0, 0.2, 1), max-width 200ms cubic-bezier(0, 0, 0.2, 1)`, `max-width 50ms cubic-bezier(0, 0, 0.2, 1)`, `none`, `opacity 100ms, top 100ms, right 100ms, bottom 100ms, left 100ms`, `color 200ms`, `background-color 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `0.1s`

- sitehome: `0.2s ease-in-out`, `background-color 0.3s ease-in-out, padding 0.3s ease-in-out`, `background 0.2s linear, border-color 0.2s linear, color 0.2s linear`, `opacity 0.18s ease-in-out, font-size 0.18s ease-in-out`, `font-size 0.18s ease-in-out`, `opacity 0.75s cubic-bezier(0.19, 1, 0.22, 1), transform 0.75s cubic-bezier(0.19, 1, 0.22, 1), -webkit-transform 0.75s cubic-bezier(0.19, 1, 0.22, 1)`, `opacity 0.3s ease-in-out`, `opacity 0.3s ease-in-out 0.7s`, `0.7s`, `opacity 1s`, `1s`, `color 0.2s ease-in-out`
