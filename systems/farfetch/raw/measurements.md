# Component measurements — farfetch.com

Computed styles read on 2026-11-14 by `tools/capture/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

farfetch.com refuses every automated request (Akamai 403 on www.farfetch.com, 429 on both farfetch-contents.com CDNs, headless and headed alike), so the DOM is Wayback Machine SSR snapshots served locally — the real markup painted by the real archived Emotion CSS, with every script removed. Elements hydrate normally would own — dropdown panels, menus, accordion animation — cannot open, so those states are absent rather than faked.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and site chrome

#### header

Header. The full top chrome: the TopBar (department links, locale flag, account, wishlist, bag) over the NavBar row (wordmark, category links, search field).

Page: set-women. Selector: `first header/TopBar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 124 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a.ltr-y1u2i0.e8ed8bx0: Farfetch Basis 15px/19.9995px 700, #222222 |
| Transition | transform 0.2s ease-in-out |
| Icon | 0 x 0, colour #222222 |
| ::after | 1440px x 0px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | header.ltr-9h8nxx.e10qbpdu0 1440.0x124.0 bg #ffffff; header::after.ltr-9h8nxx.e10qbpdu0 1440pxx0px border B:1px solid #e6e6e6; div.ltr-sy4rkd 1392.0x44.0 bg #ffffff @ 0; button.ey6fkr80.ltr-q2sk4i 0.0x0.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; a.ltr-y1u2i0.e8ed8bx0 121.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; a.ltr-y1u2i0.e8ed8bx0 94.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| Ancestor paint | 1 up div bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### topbar-dept

Department link. A TopBar department link ("Womenswear" / "Menswear" / "Kidswear"); measured, never followed.

Page: set-women. Selector: `header-department-* a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121 x 44 | = | = | = |
| Padding | 10px 12px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff @ 0 | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ltr-y1u2i0.e8ed8bx0 121.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-y1u2i0.e8ed8bx0 121.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-y1u2i0.e8ed8bx0 121.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | a.ltr-y1u2i0.e8ed8bx0 121.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topbar-dept-default.png`, `topbar-dept-hover.png`, `topbar-dept-focus-visible.png`, `topbar-dept-pressed.png`.

#### topbar-locale

Locale control. The "Language and region" flag IconButtonGhostDark in the TopBar; measured, never toggled (its picker needs hydration).

Page: set-women. Selector: `button[aria-label*=Language and region]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff @ 0 | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222 | = | = | 24 x 24, colour #727272 |
| Painted layers | button.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | button.ltr-14262k3 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | button.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | button.ltr-14262k3 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topbar-locale-default.png`, `topbar-locale-hover.png`, `topbar-locale-focus-visible.png`, `topbar-locale-pressed.png`.

#### topbar-account

Account icon. The account/sign-in icon button in the TopBar; measured, never followed.

Page: set-women. Selector: `userlogin`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #f5f5f5 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0 | = | = | #727272 |
| Transition | background-color, all, opacity, all 0.3s, 0s, 0.3s, 0s ease, cubic-bezier(0, 0, 0, 1), ease, cubic-bezier(0, 0, 0, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 30.86 x 30.86, colour #000000 @ 0, fill #727272 | 27.6 x 27.6, colour #000000 @ 0, fill #727272 | 33.78 x 33.78, colour #000000 @ 0, fill #727272 | 24.99 x 24.99, colour #727272 |
| Painted layers | button.ltr-1uez00j 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | = | button.ltr-1uez00j 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topbar-account-default.png`, `topbar-account-hover.png`, `topbar-account-focus-visible.png`, `topbar-account-pressed.png`.

#### topbar-wishlist

Wishlist icon. The heart icon link to /wishlist (gated); measured, never followed.

Page: set-women. Selector: `a[data-testid=wishlist]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff @ 0 | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222 | = | = | 24 x 24, colour #727272 |
| Painted layers | a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-14262k3 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | a.ltr-14262k3 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topbar-wishlist-default.png`, `topbar-wishlist-hover.png`, `topbar-wishlist-focus-visible.png`, `topbar-wishlist-pressed.png`.

#### topbar-bag

Bag icon. The shopping-bag icon link to checkout (gated); measured, never followed.

Page: set-women. Selector: `a[data-testid=bag]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff @ 0 | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222 | = | = | 24 x 24, colour #727272 |
| Painted layers | a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-14262k3 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | a.ltr-14262k3 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topbar-bag-default.png`, `topbar-bag-hover.png`, `topbar-bag-focus-visible.png`, `topbar-bag-pressed.png`.

#### logo

Wordmark. The FARFETCH wordmark lockup linking home; measured, never followed.

Page: set-women. Selector: `ff-logo-global`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 201 x 24.95 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222222 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 201 x 24.95, colour #222222, fill #000000 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `logo-default.png`, `logo-hover.png`, `logo-pressed.png`.

#### nav-link

Category link. A NavBar category link ("Clothing"); measured, never followed.

Page: set-women. Selector: `NavBarItemLink Clothing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58 x 19.98 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ltr-k0ippd.e3owdn51 58.0x20.0 outline 2px solid #101010 offset -2px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-sale

Sale link. The red "Sale" link in the NavBar — the one nav item painted in pos-sales red.

Page: set-women. Selector: `NavBarItemLink Sale`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 29 x 19.98 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e71d34 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ltr-k0ippd.e3owdn51 29.0x20.0 outline 2px solid #101010 offset -2px | = |

Crops: `nav-sale-default.png`, `nav-sale-hover.png`, `nav-sale-focus-visible.png`, `nav-sale-pressed.png`.

#### search-field

Search field. The header "What are you looking for?" search input; focused and typed into then cleared — never submitted.

Page: set-women. Selector: `search-input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 270 x 44 | = | = |
| Padding | 0px | = | = |
| Border | T: none; R: none; B: 1px solid #727272; L: none | T: none; R: none; B: 1px solid #222222; L: none | T: none; R: none; B: 1px solid #222222; L: none |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px -1px 0px 0px inset | #222222 0px -1px 0px 0px inset | #222222 0px -1px 0px 0px inset |
| Outline | none | = | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #222222 | = | = |
| Transition | box-shadow, border-color 0.3s cubic-bezier(0.66, 0, 0.2, 1) | = | = |
| Icon | 24 x 24, colour #b6b6b6, fill #727272 | = | = |
| Painted layers | div.ltr-qfqbf 270.0x44.0 bg #ffffff border B:1px solid #727272 shadow #000000 @ 0 0px -1px 0px 0px inset; button.ltr-1s8ja8e 32.0x32.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | div.ltr-qfqbf 270.0x44.0 bg #ffffff border B:1px solid #222222 shadow #222222 0px -1px 0px 0px inset; button.ltr-1s8ja8e 32.0x32.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | div.ltr-qfqbf 270.0x44.0 bg #ffffff border B:1px solid #222222 shadow #222222 0px -1px 0px 0px inset; button.ltr-1s8ja8e 32.0x32.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | clicked into the field | typed "trench coat", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### search-submit

Search icon button. The search-icon submit inside the header field; measured, never pressed.

Page: set-women. Selector: `SearchInputSubmitButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff @ 0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #b6b6b6 | = | = | = |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | none | = | = | = |
| Icon | 24 x 24, colour #b6b6b6, fill #727272 | = | = | = |
| ::before | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.ltr-1s8ja8e 32.0x32.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | = | button.ltr-1s8ja8e 32.0x32.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | = |
| Ancestor paint | 1 up div.ltr-qfqbf bg #ffffff shadow #000000 @ 0 0px -1px 0px 0px inset | = | 1 up div.ltr-qfqbf bg #ffffff shadow #222222 0px -1px 0px 0px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-submit-default.png`, `search-submit-hover.png`, `search-submit-focus-visible.png`, `search-submit-pressed.png`.

### New-in edit page

#### breadcrumb

Breadcrumbs. The category breadcrumb trail (Home > Women > …).

Page: set-women. Selector: `BreadcrumbsNavigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a.ltr-1h8w6zn-Footnote: Farfetch Basis 13px/17.0001px 400, #222222 |
| Transition | none |
| Icon | 12 x 12, colour #222222, fill #000000 |
| How | at rest |

Crops: `breadcrumb-default.png`.

#### page-title

Page heading. The listing h1 (PageTitleHeading on the classic listing) or the hero module DisplayLarge title on the modular pages.

Page: set-women. Selector: `first h1/DisplayLarge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 928 x 38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 30px/38.001px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Ancestor paint | 1 up div.ltr-1md0mx1 bg #ffffff @ 0 |
| How | at rest |

Crops: `page-title-default.png`.

#### page-desc

Page description. The collapsible SEO body copy under the page heading.

Page: set-women. Selector: `PageTitleDescription`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 928 x 39.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.ltr-vvc7g1.e1fzggyg0: Farfetch Basis 15px/19.9995px 400, #222222 |
| Transition | none |
| How | at rest |

Crops: `page-desc-default.png`.

#### filter-button

All Filters button. The "All Filters" button in the listing toolbar; measured, never toggled (its panel needs hydration).

Page: set-women. Selector: `filter-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 129 x 44 | = | = | = |
| Padding | 10px 44px 10px 16px | = | = | = |
| Border | 1px solid #222222 | = | = | 1px solid #727272 |
| Radius | 0px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222 | = | = | 24 x 24, colour #727272 |
| Painted layers | button.ltr-8x09gq 129.0x44.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 | button.ltr-8x09gq 129.0x44.0 bg #f5f5f5 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 | button.ltr-8x09gq 129.0x44.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 outline 2px solid #101010 offset -2px | button.ltr-8x09gq 129.0x44.0 bg #f5f5f5 border T:1px solid #727272 / R:1px solid #727272 / B:1px solid #727272 / L:1px solid #727272 |
| Ancestor paint | 1 up div.ltr-1pvugye.e1deumxq0 bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-button-default.png`, `filter-button-hover.png`, `filter-button-focus-visible.png`, `filter-button-pressed.png`.

#### quick-filter

Quick filter scroller. The quick-filter chip scroller under the toolbar — the chips are lazy-rendered, so the SSR copy only paints their skeleton bar.

Page: set-women. Selector: `quick-filters-scroller > *`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 475 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Painted layers | div.ltr-naoiyt 75.0x44.0 bg #f5f5f5; div.ltr-naoiyt 80.0x44.0 bg #f5f5f5; div.ltr-naoiyt 120.0x44.0 bg #f5f5f5; div.ltr-naoiyt 80.0x44.0 bg #f5f5f5; div.ltr-naoiyt 90.0x44.0 bg #f5f5f5 |
| How | at rest |

Crops: `quick-filter-default.png`.

#### product-card

Product card. A listing product card: image, wishlist heart, brand name, description, price.

Page: set-women. Selector: `product-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 321 x 536.98 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | p.ltr-1qgaspf-Caption.enb1jb80: Farfetch Basis 13px/17.0001px 400, #727272 | = |
| Transition | none | = |
| Icon | 24 x 24, colour #222222 | = |
| Painted layers | div.ltr-mhoyab 321.0x537.0 bg #ffffff; div::before.ltr-1d9p1fi 281pxx376px bg #f5f5f5; div.ltr-1ismw06 321.0x103.0 bg #ffffff; button.ltr-o7d7sz 44.0x44.0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | = |
| Ancestor paint | 1 up ul.ltr-sjsjxu.eoq4d4w0 bg #ffffff | = |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### card-brand

Card brand. The brand-name line on a product card.

Page: set-women. Selector: `ProductCardBrandName`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 321 x 19.98 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::after | 100% x auto, static, bg #000000 @ 0, radius 0px | = |
| How | at rest | mouse hover |

Crops: `card-brand-default.png`, `card-brand-hover.png`.

#### card-desc

Card description. The product description line under the brand.

Page: set-women. Selector: `ProductCardDescription`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 321 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 13px/17.0001px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| ::after | 100% x auto, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `card-desc-default.png`.

#### card-price

Card price. The price block on a product card.

Page: set-women. Selector: `product-card-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 321 x 25.98 |
| Padding | 6px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p.ltr-5ab0e3-Body-BodyBold.e82sgrh6: Farfetch Basis 15px/19.9995px 700, #222222 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `card-price-default.png`.

#### card-wishlist

Card wishlist heart. The heart icon button floating on the card image (aria-pressed toggle); measured, never toggled — adding to a wishlist needs an account.

Page: set-women. Selector: `addToWishlist`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222 | 24 x 24, colour #222222, fill #727272 | = | 24 x 24, colour #727272 |
| Painted layers | button.ltr-o7d7sz 44.0x44.0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | button.ltr-o7d7sz 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | button.ltr-o7d7sz 44.0x44.0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | button.ltr-o7d7sz 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| Ancestor paint | 1 up div.ltr-mhoyab bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-wishlist-default.png`, `card-wishlist-hover.png`, `card-wishlist-focus-visible.png`, `card-wishlist-pressed.png`.

#### card-sizes

Card size hint. The size-availability hint under a card ("XS S M L" style).

Page: set-women. Selector: `ProductCardSizes`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 321 x 102.98 |
| Padding | 17.0001px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p.ltr-2pfgen-Body-BodyBold: Farfetch Basis 15px/19.9995px 700, #222222 |
| Transition | opacity 0.3s cubic-bezier(0.66, 0, 0.2, 1) |
| Opacity | 0 |
| Cursor | pointer |
| Painted layers | div.ltr-1ismw06 321.0x103.0 bg #ffffff |
| How | at rest |

Crops: `card-sizes-default.png`.

#### pagination

Pagination. The pagination control under the grid ("1 of 3" + next arrow).

Page: set-women. Selector: `Pagination`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 117 |
| Padding | 48px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.ltr-gq26dl: Farfetch Basis 15px/19.9995px 400, #222222 |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | hr.ltr-llidud 1392.0x1.0 border T:1px solid #e6e6e6; a.ltr-nlzw0a 93.0x44.0 bg #222222 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest |

Crops: `pagination-default.png`.

#### pagination-next

Pagination next. The next-page arrow in the pagination control; measured, never followed.

Page: set-women. Selector: `PaginationNextActionButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93 x 44 | = | = | = |
| Padding | 0px 12px 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #222222 | #727272 | = | #b6b6b6 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.ltr-8zv7vs: Farfetch Basis 15px/19.9995px 700, #ffffff | = | = | = |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| Painted layers | a.ltr-nlzw0a 93.0x44.0 bg #222222 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-nlzw0a 93.0x44.0 bg #727272 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-nlzw0a 93.0x44.0 bg #222222 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | a.ltr-nlzw0a 93.0x44.0 bg #b6b6b6 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pagination-next-default.png`, `pagination-next-hover.png`, `pagination-next-focus-visible.png`, `pagination-next-pressed.png`.

#### carousel-arrow

Carousel arrow. A showcase carousel next-arrow (small ghost-dark icon button); measured, never pressed.

Page: set-women. Selector: `CarouselArrowSmall`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | - | = |
| Padding | 0px | = | - | = |
| Border | 1px solid #222222 | = | - | 1px solid #727272 |
| Radius | 0px | = | - | = |
| Background | #ffffff | = | - | #f5f5f5 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Farfetch Basis 15px/normal 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222222 | = | - | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #222222 | = | - | 24 x 24, colour #727272 |
| ::before | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | - | = |
| Painted layers | button.ltr-1ifd9st 32.0x32.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 | = | - | button.ltr-1ifd9st 32.0x32.0 bg #f5f5f5 border T:1px solid #727272 / R:1px solid #727272 / B:1px solid #727272 / L:1px solid #727272 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `carousel-arrow-default.png`, `carousel-arrow-hover.png`, `carousel-arrow-pressed.png`.

#### brands-module

Brands module. "Brands of the moment" — the premium-brand tile module on the modular listing.

Page: plp-men. Selector: `premium-brands`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 722.64 |
| Padding | 48px 0px 24px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p.ltr-13a5og8-Title: Farfetch Basis 22px/27.9994px 400, #222222 |
| Transition | none |
| How | at rest |

Crops: `brands-module-default.png`.

#### editorial-card

Editorial card. A fashion-feed editorial card on the listing tail.

Page: plp-men. Selector: `editorial-post`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 329.98 x 483.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h2._d699d4._a937d7: Farfetch Basis 15px/19.9995px 400, #222222 |
| Transition | none |
| How | at rest |

Crops: `editorial-card-default.png`.

#### sale-price

Sale price mark. The "-40%" discount footnote on a sale card — content-primary-enabled-sale red (its sibling PriceOriginal strikes through).

Page: set-women. Selector: `PriceSaleDiscount`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 33.63 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 13px/17.0001px 400 |
| Letter spacing | normal |
| Colour | #e71d34 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `sale-price-default.png`.

#### sale-original

Original price. The struck-through pre-sale price beside the discount mark on a sale card (grey, line-through).

Page: set-women. Selector: `PriceOriginal`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 28.42 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 13px/17.0001px 400 |
| Letter spacing | normal |
| Colour | #727272 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `sale-original-default.png`.

### Footer

#### footer

Footer. The site footer: link columns, newsletter sign-up, socials, locale/legal line.

Page: set-women. Selector: `footerDesktop`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 508.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h2.ltr-1whb09d-Body-BodyBold: Farfetch Basis 15px/19.9995px 700, #222222 |
| Transition | none |
| Icon | 24 x 24, colour #222222 |
| Painted layers | footer.ltr-uw5qcq.e1pz0q6r0 1440.0x509.0 bg #ffffff; div.ltr-1gfezzb 1440.0x509.0 bg #e6e6e6; a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| Ancestor paint | 1 up div bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer column link; measured, never followed.

Page: set-women. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 330 x 34 | = | = | = |
| Padding | 6px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | text-decoration-color 0.15s cubic-bezier(0.66, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ltr-o5fwqn 330.0x34.0 outline 2px solid #101010 offset -2px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-heading

Footer column heading. A footer column heading (small caps label).

Page: set-women. Selector: `FooterSectionTitle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 330 x 19.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 700 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `footer-heading-default.png`.

#### news-field

Newsletter field. The footer "Get updates by Email" field; focused and typed into then cleared — never submitted.

Page: set-women. Selector: `newsletter email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 300 x 42 | = | = |
| Padding | 0px 0px 0px 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #222222 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #727272, opacity 1 | = | = |
| Painted layers | input.ltr-quftrk 300.0x42.0 bg #ffffff | = | = |
| Ancestor paint | 1 up div.ltr-6xvdur bg #ffffff | 1 up div.ltr-6xvdur bg #ffffff outline 2px solid #101010 | 1 up div.ltr-6xvdur bg #ffffff outline 2px solid #101010 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `news-field-default.png`, `news-field-focused.png`, `news-field-filled.png`.

#### news-submit

Sign Up button. The "Sign Up" newsletter button; measured, never pressed.

Page: set-women. Selector: `newsletter-submit-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90 x 44 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #222222 | #727272 | = | #b6b6b6 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset 1px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ltr-1ojpv6f 90.0x44.0 bg #222222 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | button.ltr-1ojpv6f 90.0x44.0 bg #727272 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | button.ltr-1ojpv6f 90.0x44.0 bg #222222 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset 1px | button.ltr-1ojpv6f 90.0x44.0 bg #b6b6b6 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `news-submit-default.png`, `news-submit-hover.png`, `news-submit-focus-visible.png`, `news-submit-pressed.png`.

#### footer-social

Social icon link. A social icon link in the footer; measured, never followed.

Page: set-women. Selector: `FooterSocialsGrouping a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff @ 0 | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222 | = | = | 24 x 24, colour #727272 |
| Painted layers | a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-14262k3 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | a.ltr-14262k3 44.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | a.ltr-14262k3 44.0x44.0 bg #f5f5f5 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

### Product detail page

#### pdp-breadcrumb

Breadcrumbs. The PDP breadcrumb trail (Women > Dolce & Gabbana > Shoes > …).

Page: pdp. Selector: `BreadcrumbsNavigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a.ltr-1h8w6zn-Footnote: Farfetch Basis 13px/17.0001px 400, #222222 |
| Transition | none |
| Icon | 12 x 12, colour #222222, fill #000000 |
| How | at rest |

Crops: `pdp-breadcrumb-default.png`.

#### pdp-arrow

Gallery arrow. A gallery next/previous arrow; measured, never pressed.

Page: pdp. Selector: `CarouselArrowSmall`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | - | = |
| Padding | 0px | = | - | = |
| Border | 1px solid #222222 | = | - | 1px solid #727272 |
| Radius | 0px | = | - | = |
| Background | #ffffff | = | - | #f5f5f5 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Farfetch Basis 15px/normal 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222222 | = | - | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #222222 | = | - | 24 x 24, colour #727272 |
| ::before | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | - | = |
| Painted layers | button.ltr-1ifd9st 32.0x32.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 | = | - | button.ltr-1ifd9st 32.0x32.0 bg #f5f5f5 border T:1px solid #727272 / R:1px solid #727272 / B:1px solid #727272 / L:1px solid #727272 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `pdp-arrow-default.png`, `pdp-arrow-pressed.png`.

#### pdp-brand

Brand link. The "Dolce & Gabbana" ghost-dark brand link over the PDP title; measured, never followed.

Page: pdp. Selector: `LinkGhostDark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 175 x 27.98 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 22px/27.9994px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | color, text-decoration 0.15s cubic-bezier(0.66, 0, 0.2, 1) | = | color 0.15s cubic-bezier(0.66, 0, 0.2, 1) | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ltr-1rkeqir-Body-Heading.e1h8dali1 175.0x28.0 outline 2px solid #101010 offset -2px | = |

Crops: `pdp-brand-default.png`, `pdp-brand-hover.png`, `pdp-brand-focus-visible.png`, `pdp-brand-pressed.png`.

#### pdp-title

Product title. The product description heading ("logo-embossed cut-out slides").

Page: pdp. Selector: `product-short-description`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 452 x 47.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 30px/39.999px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a.ltr-1rkeqir-Body-Heading.e1h8dali1: Farfetch Basis 22px/27.9994px 400, #222222 |
| Transition | none |
| How | at rest |

Crops: `pdp-title-default.png`.

#### pdp-price

Price callout. The "$345" price callout above the size selector.

Page: pdp. Selector: `PriceCallout`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 452 x 19.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p.ltr-137vk2a-Body.e17hktm27: Farfetch Basis 15px/19.9995px 400, #222222 |
| Transition | none |
| How | at rest |

Crops: `pdp-price-default.png`.

#### size-selector

Size selector. The "Select size" combobox (44px outlined field, chevron). Its listbox is hydration-rendered, so no opened state exists in the static copy.

Page: pdp. Selector: `ScaledSizeSelector`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 452 x 44 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222222 | = | - | = |
| Text node | span.ltr-1mhgg20: Farfetch Basis 15px/19.9995px 400, #727272 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #222222, fill #000000 | = | - | = |
| Painted layers | div.ltr-cubnbt 452.0x44.0 bg #ffffff border T:1px solid #727272 / R:1px solid #727272 / B:1px solid #727272 / L:1px solid #727272 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `size-selector-default.png`, `size-selector-hover.png`, `size-selector-pressed.png`.

#### add-to-bag

Add To Bag. The primary "Add To Bag" button — actions-primary dark surface; measured, never pressed.

Page: pdp. Selector: `addToBag`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 322 x 44 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | 1px solid #ffffff @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #222222 | #727272 | = | #959595 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Farfetch Basis 15px/19.9995px 700, #ffffff | = | = | = |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ltr-twjh4c 322.0x44.0 bg #222222 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | button.ltr-twjh4c 322.0x44.0 bg #727272 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | button.ltr-twjh4c 322.0x44.0 bg #222222 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 outline 2px solid #101010 offset -2px | button.ltr-twjh4c 322.0x44.0 bg #959595 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-bag-default.png`, `add-to-bag-hover.png`, `add-to-bag-focus-visible.png`, `add-to-bag-pressed.png`.

#### pdp-wishlist

PDP wishlist. The "Wishlist" secondary action beside Add To Bag (aria-pressed toggle); measured, never toggled.

Page: pdp. Selector: `WishlistIconsContainer`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118 x 44 | = | = | = |
| Padding | 10px 44px 10px 16px | = | = | = |
| Border | 1px solid #222222 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222 | = | = | = |
| Painted layers | button.ltr-egd9yz.e15yvx1f1 118.0x44.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 | = | button.ltr-egd9yz.e15yvx1f1 118.0x44.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 outline 2px solid #101010 offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-wishlist-default.png`, `pdp-wishlist-hover.png`, `pdp-wishlist-focus-visible.png`, `pdp-wishlist-pressed.png`.

#### pdp-accordion

Info accordion. "The Details / Composition / FARFETCH ID" accordion under the buy box.

Page: pdp. Selector: `product-information-accordion`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 484.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p.ltr-o2xu7v-Kicker: Farfetch Basis 15px/19.9995px 400, #222222 |
| Transition | none |
| Icon | 24 x 24, colour #222222 |
| Painted layers | section.ltr-t80gkb 1392.0x472.8 border B:1px solid #e6e6e6 |
| How | at rest |

Crops: `pdp-accordion-default.png`.

#### accordion-item

Accordion section. One accordion section (SSR ships the first panel expanded).

Page: pdp. Selector: `AccordionItem`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 472.78 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #e6e6e6; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p.ltr-o2xu7v-Kicker: Farfetch Basis 15px/19.9995px 400, #222222 |
| Transition | none |
| Icon | 24 x 24, colour #222222 |
| Painted layers | section.ltr-t80gkb 1392.0x472.8 border B:1px solid #e6e6e6 |
| How | at rest |

Crops: `accordion-item-default.png`.

#### accordion-button

Accordion toggle. An accordion section toggle; measured, never toggled (panels need hydration).

Page: pdp. Selector: `AccordionButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1392 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101010 offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | p.ltr-o2xu7v-Kicker: Farfetch Basis 15px/19.9995px 400, #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #222222 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.ltr-g3vsg 1392.0x44.0 outline 2px solid #101010 offset -2px | = |

Crops: `accordion-button-default.png`, `accordion-button-hover.png`, `accordion-button-focus-visible.png`, `accordion-button-pressed.png`.

#### skeleton-card

Card skeleton. A product-card loading skeleton in the related-products showcase (the showcase grid ships skeletonised in SSR).

Page: pdp. Selector: `ProductCardSkeleton`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288.88 x 501.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Painted layers | div.ltr-q6lfkw 288.9x385.2 bg #f5f5f5; div.ltr-7yf7ta 202.2x22.0 bg #f5f5f5; div.ltr-7yf7ta 260.0x22.0 bg #f5f5f5; div.ltr-7yf7ta 144.4x22.0 bg #f5f5f5 |
| How | at rest |

Crops: `skeleton-card-default.png`.

#### skeleton-showcase

Showcase skeleton. A related-products showcase in its SSR loading state.

Page: pdp. Selector: `showcase-skeleton`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 573.14 |
| Padding | 0px |
| Gap | 36px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Icon | 24 x 24, colour #222222 |
| Painted layers | div.ltr-vqy38v-TitleSkeleton 487.2x28.0 bg #f5f5f5 border B:2px solid #ffffff; div.ltr-q6lfkw 288.9x385.2 bg #f5f5f5; div.ltr-7yf7ta 202.2x22.0 bg #f5f5f5; div.ltr-7yf7ta 260.0x22.0 bg #f5f5f5; div.ltr-7yf7ta 144.4x22.0 bg #f5f5f5; div.ltr-q6lfkw 288.9x385.2 bg #f5f5f5 |
| How | at rest |

Crops: `skeleton-showcase-default.png`.

#### pdp-gallery

Image gallery. The PDP product-photo column (the stacked product shots left of the buy box; its arrow controls need hydration).

Page: pdp. Selector: `innermost multi-image block left of the buy box`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 904 x 1201.31 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `pdp-gallery-default.png`.

#### variant-tabs

Variant tabs. Colour/variant tabs in the variant selector. The archived PDP renders only the size combobox there, so none exist to measure.

Page: pdp. Selector: `variant-selector [role=tab]`. States: .

Not found on the page at capture time.

### Home (department chooser)

#### dept-heading

Chooser heading. "Choose a department" — the Title heading over the three department tiles.

Page: home. Selector: `Title Choose a department`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 928 x 27.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 22px/27.9994px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `dept-heading-default.png`.

#### dept-tile

Department tile. A department chooser tile — full-bleed image with the department Display name overlaid; measured, never followed.

Page: home. Selector: `a:has(Display WOMENSWEAR)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 447.98 x 251.92 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | p._bdc4ef.ltr-r4p3u0-Display: Farfetch Basis 30px/38.001px 400, #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div::before._eb25ab._f6155d 447.984pxx251.922px image linear-gradient(#222222 @ 0, #222222 @ 0.82) | = |
| How | at rest | mouse hover |

Crops: `dept-tile-default.png`, `dept-tile-hover.png`.

#### dept-kicker

Category kicker. The Kicker heading ("Clothing") over a category card in a department column; the card around it is the link, the heading itself is not interactive.

Page: home. Selector: `Kicker Clothing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 329.98 x 19.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `dept-kicker-default.png`.

#### home-category-card

Category card. A department-column category card (image with a Kicker label, e.g. NEW IN); measured, never followed.

Page: home. Selector: `editorial-post with Kicker`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 329.98 x 483.59 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | h2._d699d4._a937d7: Farfetch Basis 15px/19.9995px 400, #222222 | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `home-category-card-default.png`, `home-category-card-hover.png`.

#### home-editorial

Editorial card. A fashion-feed editorial card on the home tail. The archived home paints only department and category cards, so no feed card exists to measure (the listing pages carry the editorial-card component).

Page: home. Selector: `editorial-post without Kicker or Display`. States: .

Not found on the page at capture time.

### Type specimens

#### type-display

Display. A --typography-display / display-large specimen.

Page: plp-women. Selector: `Display/DisplayLarge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 588 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 38px/48.0016px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `type-display-default.png`.

#### type-kicker

Kicker. The uppercase --typography-kicker over a heading.

Page: plp-women. Selector: `Kicker`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 329.98 x 19.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `type-kicker-default.png`.

#### type-footnote

Footnote. The --typography-footnote micro-label.

Page: plp-women. Selector: `Footnote`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 13px/17.0001px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `type-footnote-default.png`.

#### type-label

Label. A small label style (LabelPrimarySmall).

Page: plp-women. Selector: `LabelPrimarySmall`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 336 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 13px/17.0001px 400 |
| Letter spacing | normal |
| Colour | #727272 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `type-label-default.png`.

#### type-editorial

Editorial. The Nimbus Roman D --typography-editorial serif.

Page: plp-women. Selector: `Editorial`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 588 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nimbus Roman D 20px/24px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `type-editorial-default.png`.

#### type-title

Title. A --typography-title specimen.

Page: plp-women. Selector: `Title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 928 x 27.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 22px/27.9994px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `type-title-default.png`.

#### type-body

Body. A --typography-body specimen.

Page: plp-women. Selector: `Body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 684 x 19.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| How | at rest |

Crops: `type-body-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The top chrome at 390: department links, wordmark, locale/account/wishlist/bag icons (the SSR markup paints the desktop chrome responsively; the hamburger needs hydration).

Page: home. Selector: `first header/TopBar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 100 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | button.ey6fkr80.ltr-1iz9vsw: Farfetch Basis 15px/19.9995px 700, #222222 |
| Transition | transform 0.2s ease-in-out |
| Icon | 24 x 24, colour #222222 |
| ::after | 390px x 0px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | header.ltr-9h8nxx.e10qbpdu0 390.0x100.0 bg #ffffff; header::after.ltr-9h8nxx.e10qbpdu0 390pxx0px border B:1px solid #e6e6e6; div.ltr-sy4rkd 382.0x44.0 bg #ffffff @ 0; button.ey6fkr80.ltr-1iz9vsw 215.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; a.ltr-y1u2i0.e8ed8bx0 0.0x0.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0; a.ltr-y1u2i0.e8ed8bx0 0.0x0.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| Ancestor paint | 1 up div bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-dept-menu

Mobile department menu. The "departments" DropdownMenuSelectorUncontrolled in the TopBar — visible only below 60em; measured, never toggled.

Page: home. Selector: `departments dropdown`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62 x 44 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Farfetch Basis 15px/19.9995px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222222 | = | - | = |
| Text node | button.ey6fkr80.ltr-1iz9vsw: Farfetch Basis 15px/19.9995px 700, #222222 | = | - | = |
| Transition | none | = | - | = |
| Icon | 24 x 24, colour #222222 | = | - | = |
| Painted layers | button.ey6fkr80.ltr-1iz9vsw 215.0x44.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `m-dept-menu-default.png`, `m-dept-menu-hover.png`, `m-dept-menu-pressed.png`.

#### m-search

Mobile search field. The search input at phone width.

Page: home. Selector: `search-input`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 270 x 44 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #727272; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px -1px 0px 0px inset |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | box-shadow, border-color 0.3s cubic-bezier(0.66, 0, 0.2, 1) |
| Icon | 24 x 24, colour #b6b6b6, fill #727272 |
| Painted layers | div.ltr-qfqbf 270.0x44.0 bg #ffffff border B:1px solid #727272 shadow #000000 @ 0 0px -1px 0px 0px inset; button.ltr-1s8ja8e 32.0x32.0 bg #ffffff @ 0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest |

Crops: `m-search-default.png`.

#### m-logo

Mobile wordmark. The FARFETCH wordmark at phone width.

Page: home. Selector: `ff-logo-global`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 124 x 15.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Cursor | pointer |
| Icon | 124 x 15.39, colour #222222, fill #000000 |
| How | at rest |

Crops: `m-logo-default.png`.

#### m-add-to-bag

Mobile Add To Bag. The primary buy button at phone width.

Page: pdp. Selector: `addToBag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 84.5 x 61.97 |
| Padding | 10px 16px |
| Border | 1px solid #ffffff @ 0 |
| Radius | 0px |
| Background | #222222 |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: Farfetch Basis 15px/19.9995px 700, #ffffff |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) |
| Cursor | pointer |
| Painted layers | button.ltr-twjh4c 84.5x62.0 bg #222222 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest |

Crops: `m-add-to-bag-default.png`.

#### m-size-selector

Mobile size selector. The "Select size" combobox at phone width.

Page: pdp. Selector: `ScaledSizeSelector`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 142.5 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.ltr-1mhgg20: Farfetch Basis 15px/19.9995px 400, #727272 |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #222222, fill #000000 |
| Painted layers | div.ltr-cubnbt 142.5x44.0 bg #ffffff border T:1px solid #727272 / R:1px solid #727272 / B:1px solid #727272 / L:1px solid #727272 |
| How | at rest |

Crops: `m-size-selector-default.png`.

#### m-dept-tile

Mobile department tile. A department chooser tile at phone width.

Page: home. Selector: `a:has(Display WOMENSWEAR)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 260 x 146.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p._bdc4ef.ltr-r4p3u0-Display: Farfetch Basis 30px/38.001px 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | div::before._eb25ab._f6155d 260pxx146.25px image linear-gradient(#222222 @ 0, #222222 @ 0.82) |
| How | at rest |

Crops: `m-dept-tile-default.png`.

#### m-product-card

Mobile product card. A listing product card at phone width.

Page: plp-women. Selector: `product-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 173 x 339.64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p.ltr-1qgaspf-Caption.ey751pk0: Farfetch Basis 13px/17.0001px 400, #727272 |
| Transition | none |
| Icon | 24 x 24, colour #222222 |
| Painted layers | div.ltr-mhoyab 173.0x339.6 bg #ffffff; div::before.ltr-1d9p1fi 133pxx178.656px bg #f5f5f5; button.ltr-o7d7sz 44.0x44.0 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 |
| How | at rest |

Crops: `m-product-card-default.png`.

#### m-filter

Mobile filter button. The All Filters control at phone width (plp modular page renders it post-hydration).

Page: plp-women. Selector: `filter-button`. States: .

Not found on the page at capture time.

### Product listing page

#### hero-module

Hero module. The content-module hero on the listing front: campaign image, Display title, dek and a "Shop Now" secondary button.

Page: plp-men. Selector: `hero-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 1007.64 |
| Padding | 48px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Farfetch Basis 15px/19.9995px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h2._d699d4._b6b946: Farfetch Basis 38px/48.0016px 400, #222222 |
| Transition | none |
| Painted layers | a.ltr-i5fx28 106.4x44.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 |
| Ancestor paint | 1 up div.ltr-wn2fdi bg #ffffff |
| How | at rest |

Crops: `hero-module-default.png`.

#### hero-cta

Hero CTA. The "Shop Now" secondary button inside the hero module (white surface, dark stroke); measured, never followed.

Page: plp-men. Selector: `hero-container a "Shop Now"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.44 x 44 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | 1px solid #222222 | = | = | 1px solid #727272 |
| Radius | 0px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #005fcc offset -2px | = |
| Font | Farfetch Basis 15px/19.9995px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | #727272 |
| Transition | background-color, border-color, opacity, color 0.3s cubic-bezier(0, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ltr-i5fx28 106.4x44.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 | a.ltr-i5fx28 106.4x44.0 bg #f5f5f5 border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 | a.ltr-i5fx28 106.4x44.0 bg #ffffff border T:1px solid #222222 / R:1px solid #222222 / B:1px solid #222222 / L:1px solid #222222 outline 2px solid #005fcc offset -2px | a.ltr-i5fx28 106.4x44.0 bg #f5f5f5 border T:1px solid #727272 / R:1px solid #727272 / B:1px solid #727272 / L:1px solid #727272 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

farfetch's sheets are all same-origin on the local mirror (the portal-core bundles plus the inline Emotion blocks), so this list holds every declared transition the CSSOM could read on each page.
