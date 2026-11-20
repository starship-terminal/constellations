# Deezer component measurements

Computed styles read from deezer.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the light home hero, the dark marketing offers/features/download pages, the dark Chakra-UI catalog app on /en/artist|album|playlist and the dark account.deezer.com forms — with the GDPR cookie modal hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### App shell and navigation

#### a-sidebar

App sidebar. The left rail: DEEZER wordmark, Home/Explore, the Playlists promo card with Create-a-playlist.

Page: artist. Selector: `sidebar rail (Home-link ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 243 x 900 |
| Padding | 0px 0px 80px 0px |
| Border | none |
| Radius | 0px |
| Background | #141216 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.chakra-heading.css-1625w3j: Inter 15px/18.75px 550, #ffffff |
| Transition | padding-bottom 0.5s cubic-bezier(0.77, 0, 0.175, 1) |
| Icon | 127 x 16, colour #ffffff |
| Painted layers | div.BKfE_.css-80628b 243.0x900.0 bg #141216; div.css-1sb63b3 243.0x154.0 bg #141216; a.chakra-link.css-2yr2kp 127.0x32.0 outline 2px solid #000000 @ 0 offset 2px; button.chakra-button.css-pdp9k3 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; a.chakra-link.css-qiubdp 227.0x40.0 r 16px outline 2px solid #000000 @ 0 offset 2px; a.chakra-link.css-qiubdp 227.0x40.0 r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `a-sidebar-default.png`.

#### a-logo

Sidebar logo. The DEEZER wordmark at the top of the rail.

Page: artist. Selector: `sidebar logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 127 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 127 x 16, colour #ffffff |
| Painted layers | a.chakra-link.css-2yr2kp 127.0x32.0 outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `a-logo-default.png`.

#### a-nav-home

Sidebar link. The "Home" nav item (icon + label); measured, never followed.

Page: artist. Selector: `a.chakra-link Home`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 227 x 40 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | #242326 | = | #2e2c30 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #ad47ff offset -2px | none |
| Font | Inter 16px/21.328px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | h2.chakra-heading.css-1625w3j: Inter 15px/18.75px 550, #ffffff | = | = | = |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #a19fa4 | 24 x 24, colour #f5f2f8 | = | = |
| Painted layers | a.chakra-link.css-qiubdp 227.0x40.0 r 16px outline 2px solid #000000 @ 0 offset 2px | a.chakra-link.css-qiubdp 227.0x40.0 bg #242326 r 16px outline 2px solid #000000 @ 0 offset 2px | a.chakra-link.css-qiubdp 227.0x40.0 r 16px outline 2px solid #ad47ff offset -2px | a.chakra-link.css-qiubdp 227.0x40.0 bg #2e2c30 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `a-nav-home-default.png`, `a-nav-home-hover.png`, `a-nav-home-focus-visible.png`, `a-nav-home-pressed.png`.

#### a-nav-explore

Sidebar link 2. The "Explore" nav item; measured, never followed.

Page: artist. Selector: `a.chakra-link Explore`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 227 x 40 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | #242326 | = | #2e2c30 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #ad47ff offset -2px | none |
| Font | Inter 16px/21.328px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | h2.chakra-heading.css-1625w3j: Inter 15px/18.75px 550, #ffffff | = | = | = |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #a19fa4 | 24 x 24, colour #f5f2f8 | = | = |
| Painted layers | a.chakra-link.css-qiubdp 227.0x40.0 r 16px outline 2px solid #000000 @ 0 offset 2px | a.chakra-link.css-qiubdp 227.0x40.0 bg #242326 r 16px outline 2px solid #000000 @ 0 offset 2px | a.chakra-link.css-qiubdp 227.0x40.0 r 16px outline 2px solid #ad47ff offset -2px | a.chakra-link.css-qiubdp 227.0x40.0 bg #2e2c30 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `a-nav-explore-default.png`, `a-nav-explore-hover.png`, `a-nav-explore-focus-visible.png`, `a-nav-explore-pressed.png`.

#### a-playlist-promo

Playlist promo card. The sidebar "Create your first playlist" card — an upsell/empty-state nudge.

Page: artist. Selector: `sidebar promo card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 203 x 188.69 |
| Padding | 16px |
| Gap | 12px |
| Border | none |
| Radius | 8px |
| Background | #242326 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.chakra-text.css-aj9pqj: Inter 15px/22.5px 550, #ffffff |
| Transition | none |
| Painted layers | div.css-ofmpdz 203.0x188.7 bg #242326 r 8px; button.chakra-button.css-stlvch 141.0x32.0 bg #ffffff r 12px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest |

Crops: `a-playlist-promo-default.png`.

#### a-create-playlist

Create playlist button. The promo card's white "Create a playlist" action; measured, never clicked (it would need an account).

Page: artist. Selector: `Create a playlist`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 141 x 32 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #ad47ff offset 0px | = |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #141216 | = | #242326 |
| Text node | span: Inter 13px/18.5718px 550, #000000 | span: Inter 13px/18.5718px 550, #141216 | = | span: Inter 13px/18.5718px 550, #242326 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.chakra-button.css-stlvch 141.0x32.0 bg #ffffff r 12px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-stlvch 141.0x32.0 bg #f5f2f8 r 12px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-stlvch 141.0x32.0 bg #ffffff r 12px outline 2px solid #ad47ff offset 0px | button.chakra-button.css-stlvch 141.0x32.0 bg #e2dfe6 r 12px outline 2px solid #000000 @ 0 offset 0px |
| Ancestor paint | 1 up div.css-ofmpdz bg #242326 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `a-create-playlist-default.png`, `a-create-playlist-hover.png`, `a-create-playlist-focus-visible.png`, `a-create-playlist-pressed.png`.

#### a-search

Search field. The "Artists, tracks, podcasts..." header search; focused and typed into then cleared — never submitted. Typing into it navigates to a search-results page, which is why it is measured last here.

Page: artist. Selector: `input.chakra-input[aria-label=Search]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 375 x 48 | = | = |
| Padding | 0px 44px | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #ad47ff | 2px solid #ad47ff |
| Radius | 16px | = | = |
| Background | #242326 | #2e2c30 | #2e2c30 |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset -2px | = | = |
| Font | Inter 15px/22.5px 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | #f5f2f8 | #f5f2f8 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #706e73, opacity 1 | = | = |
| Painted layers | input.chakra-input.css-2f7jqd 375.0x48.0 bg #242326 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px outline 2px solid #000000 @ 0 offset -2px | input.chakra-input.css-2f7jqd 375.0x48.0 bg #2e2c30 border T:2px solid #ad47ff / R:2px solid #ad47ff / B:2px solid #ad47ff / L:2px solid #ad47ff r 16px outline 2px solid #000000 @ 0 offset -2px | input.chakra-input.css-2f7jqd 375.0x48.0 bg #2e2c30 border T:2px solid #ad47ff / R:2px solid #ad47ff / B:2px solid #ad47ff / L:2px solid #ad47ff r 16px outline 2px solid #000000 @ 0 offset -2px |
| How | at rest | clicked into the field | typed "daft punk", then deleted; nothing sent |

Crops: `a-search-default.png`, `a-search-focused.png`, `a-search-filled.png`.

#### a-plans-link

Plans link. The header "Plans" link to /en/offers; measured, never followed.

Page: artist. Selector: `header Plans`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43 x 21.31 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | none | none |
| Font | Inter 16px/21.328px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | #bb73ff |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.chakra-link.css-rwg70c 43.0x21.3 outline 2px solid #000000 @ 0 offset 2px | = | - | - |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `a-plans-link-default.png`, `a-plans-link-hover.png`, `a-plans-link-focus-visible.png`, `a-plans-link-pressed.png`.

#### a-login

Log in button (app). The dark-outline Log-in pill in the app header; links to account.deezer.com, measured never followed.

Page: artist. Selector: `a.chakra-button Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73 x 32 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | 1px solid #4e4c51 | 1px solid #59575c | 1px solid #ad47ff | 1px solid #656367 |
| Radius | 12px | = | = | = |
| Background | transparent | #2e2c30 | = | #38373b |
| Box shadow | none | = | = | = |
| Outline | 1px solid #000000 @ 0 offset 0px | = | none | none |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Text node | span: Inter 13px/18.5718px 550, #ffffff | span: Inter 13px/18.5718px 550, #f5f2f8 | = | span: Inter 13px/18.5718px 550, #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.chakra-button.css-12sw6v1 73.0x32.0 border T:1px solid #4e4c51 / R:1px solid #4e4c51 / B:1px solid #4e4c51 / L:1px solid #4e4c51 r 12px outline 1px solid #000000 @ 0 offset 0px | a.chakra-button.css-12sw6v1 73.0x32.0 bg #2e2c30 border T:1px solid #59575c / R:1px solid #59575c / B:1px solid #59575c / L:1px solid #59575c r 12px outline 1px solid #000000 @ 0 offset 0px | a.chakra-button.css-12sw6v1 73.0x32.0 border T:1px solid #ad47ff / R:1px solid #ad47ff / B:1px solid #ad47ff / L:1px solid #ad47ff r 12px | a.chakra-button.css-12sw6v1 73.0x32.0 bg #38373b border T:1px solid #656367 / R:1px solid #656367 / B:1px solid #656367 / L:1px solid #656367 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `a-login-default.png`, `a-login-hover.png`, `a-login-focus-visible.png`, `a-login-pressed.png`.

#### a-signup

Sign up button (app). The purple Sign-up pill in the app header; measured never followed.

Page: artist. Selector: `a.chakra-button Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 32 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ad47ff | #bb73ff | = | #ca97ff |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | none | none |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Text node | span: Inter 13px/18.5718px 550, #ffffff | span: Inter 13px/18.5718px 550, #f5f2f8 | = | span: Inter 13px/18.5718px 550, #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.chakra-button.css-eo14fd 81.0x32.0 bg #ad47ff r 12px outline 2px solid #000000 @ 0 offset 0px | a.chakra-button.css-eo14fd 81.0x32.0 bg #bb73ff r 12px outline 2px solid #000000 @ 0 offset 0px | a.chakra-button.css-eo14fd 81.0x32.0 bg #ad47ff r 12px | a.chakra-button.css-eo14fd 81.0x32.0 bg #ca97ff r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `a-signup-default.png`, `a-signup-hover.png`, `a-signup-focus-visible.png`, `a-signup-pressed.png`.

#### mkt-header

Marketing header. The dark top bar over the light hero: wordmark, Plans/Features/Music, Log in and the purple Sign up pill.

Page: home. Selector: `header / .topbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px 112px |
| Border | T: none; R: none; B: 1px solid #555257; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfcfe |
| Text node | a.tempo-link: Inter 16px/normal 700, #fdfcfe |
| Transition | none |
| Painted layers | nav.tempo-topbar 1440.0x80.0 border B:1px solid #555257; a.topbar-action.tempo-btn 84.0x37.0 border T:1px solid #555257 / R:1px solid #555257 / B:1px solid #555257 / L:1px solid #555257 r 12px; a.topbar-action.tempo-btn 95.0x37.0 bg #a238ff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; span.burger-line 0.0x0.0 bg #f8f8f9; span.burger-line 0.0x0.0 bg #f8f8f9; span.burger-line 0.0x0.0 bg #f8f8f9 |
| Ancestor paint | 1 up body.unlogged-root-page.dir-ltr bg #0f0d13 |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Deezer heart-and-wordmark in the header.

Page: home. Selector: `a.tempo-topbar-deezer-logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 106.66 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfcfe |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### mkt-nav-link

Nav link. A marketing header link (Plans/Features/Music); measured, never followed.

Page: home. Selector: `a.tempo-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fdfcfe | #a238ff | = | #a238ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-nav-link-default.png`, `mkt-nav-link-hover.png`, `mkt-nav-link-focus-visible.png`, `mkt-nav-link-pressed.png`.

#### mkt-login

Log in button. The dark-outline Log-in pill; links to account.deezer.com, measured never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 37 | = | = | 79.8 x 35.15 |
| Padding | 9px 20px | = | = | = |
| Gap | 14px | = | = | = |
| Border | 1px solid #555257 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #29282d | = | #29282d |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fdfcfe | = | = | = |
| Transition | background-color, border-color, color, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.topbar-action.tempo-btn 84.0x37.0 border T:1px solid #555257 / R:1px solid #555257 / B:1px solid #555257 / L:1px solid #555257 r 12px | a.topbar-action.tempo-btn 84.0x37.0 bg #29282d border T:1px solid #555257 / R:1px solid #555257 / B:1px solid #555257 / L:1px solid #555257 r 12px | = | a.topbar-action.tempo-btn 79.8x35.1 bg #29282d border T:1px solid #555257 / R:1px solid #555257 / B:1px solid #555257 / L:1px solid #555257 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `mkt-login-default.png`, `mkt-login-hover.png`, `mkt-login-focus-visible.png`, `mkt-login-pressed.png`.

#### mkt-signup

Sign up button. The purple Sign-up pill in the header; measured never followed.

Page: home. Selector: `a.topbar-action Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95 x 37 | = | = | 90.25 x 35.15 |
| Padding | 9px 20px | = | = | = |
| Gap | 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 12px | = | = | = |
| Background | #a238ff | #9333e8 | = | #9333e8 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, color, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.topbar-action.tempo-btn 95.0x37.0 bg #a238ff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px | a.topbar-action.tempo-btn 95.0x37.0 bg #9333e8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px | = | a.topbar-action.tempo-btn 90.3x35.1 bg #9333e8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `mkt-signup-default.png`, `mkt-signup-hover.png`, `mkt-signup-focus-visible.png`, `mkt-signup-pressed.png`.

### Artist page (dark app)

#### artist-avatar

Artist image. The artist's round photo in the page header (the first large chakra-image on the page).

Page: artist. Selector: `img.chakra-image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 278 x 278 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `artist-avatar-default.png`.

#### artist-name

Artist name. The artist's display name heading.

Page: artist. Selector: `artist h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 644 x 64 |
| Padding | 8px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Deezer Headline VF 56px/56px 640 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `artist-name-default.png`.

#### artist-fans

Fan count. The "5,237,122 fans" muted count under the name.

Page: artist. Selector: `fans text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 144 x 18.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 13px/18.5718px 450 |
| Letter spacing | normal |
| Colour | #a19fa4 |
| Transition | none |
| How | at rest |

Crops: `artist-fans-default.png`.

#### mix-btn

Mix button. The purple "▶ Mix" primary action; measured, never pressed (it would start playback and, signed out, a paywall).

Page: artist. Selector: `button[aria-label=Mix]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95 x 48 | = | = | = |
| Padding | 12px 24px 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ad47ff | #bb73ff | = | #ca97ff |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #f5f2f8 offset 0px | = |
| Font | Inter 15px/22.5px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Text node | span.states-button-label: Inter 15px/22.5px 550, #ffffff | span.states-button-label: Inter 15px/22.5px 550, #f5f2f8 | = | span.states-button-label: Inter 15px/22.5px 550, #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-oes4qb 95.0x48.0 bg #ad47ff r 16px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-oes4qb 95.0x48.0 bg #bb73ff r 16px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-oes4qb 95.0x48.0 bg #ad47ff r 16px outline 2px solid #f5f2f8 offset 0px | button.chakra-button.css-oes4qb 95.0x48.0 bg #ca97ff r 16px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mix-btn-default.png`, `mix-btn-hover.png`, `mix-btn-focus-visible.png`, `mix-btn-pressed.png`.

#### fav-btn

Favourite icon button. The heart "Add" icon button beside Mix; measured, never toggled (it needs an account).

Page: artist. Selector: `button[aria-label=Add]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | transparent | #2e2c30 | = | #38373b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #ad47ff offset 0px | = |
| Font | Inter 15px/22.5px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-15ctxfi 48.0x48.0 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-15ctxfi 48.0x48.0 bg #2e2c30 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-15ctxfi 48.0x48.0 r 256px outline 2px solid #ad47ff offset 0px | button.chakra-button.css-15ctxfi 48.0x48.0 bg #38373b r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `fav-btn-default.png`, `fav-btn-hover.png`, `fav-btn-focus-visible.png`, `fav-btn-pressed.png`.

#### menu-btn

Track overflow button. The "..." ("View menu") icon button — a Chakra popover trigger; the opened state was measured after clicking it, its items never followed.

Page: artist. Selector: `button[aria-label="View menu"]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 256px | = | = | = | = |
| Background | transparent | #2e2c30 | = | #38373b | #2e2c30 |
| Box shadow | none | = | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #ad47ff offset 0px | = | = |
| Font | Inter 15px/22.5px 550 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 | #f5f2f8 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 | 24 x 24, colour #f5f2f8 |
| Painted layers | button.chakra-button.popper-wrapper 48.0x48.0 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.popper-wrapper 48.0x48.0 bg #2e2c30 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.popper-wrapper 48.0x48.0 r 256px outline 2px solid #ad47ff offset 0px | button.chakra-button.popper-wrapper 48.0x48.0 bg #38373b r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.popper-wrapper 48.0x48.0 bg #2e2c30 r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `menu-btn-default.png`, `menu-btn-hover.png`, `menu-btn-focus-visible.png`, `menu-btn-pressed.png`, `menu-btn-opened.png`.

#### menu-popover

Overflow popover. The track overflow menu opened by its own trigger (a Chakra popper panel); its items were never followed.

Page: artist. Selector: `popper panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.36 x 208.14 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #141216 |
| Box shadow | #000000 @ 0.4 0px 0px 25px 10px, #000000 @ 0.04 0px 10px 10px -5px |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.chakra-text.css-j29fat: Inter 13px/18.5718px 450, #ffffff |
| Transition | none |
| Transform | matrix(0.963613, 0, 0, 0.963613, 0, 0) |
| Opacity | 0.258889 |
| Icon | 23.13 x 23.13, colour #ffffff |
| Painted layers | section.chakra-popover__content.css-j0r7v1 308.4x208.1 bg #141216 r 24px shadow #000000 @ 0.4 0px 0px 25px 10px, #000000 @ 0.04 0px 10px 10px -5px; div.css-d2nqmu 308.4x208.1 bg #141216 r 24px shadow #000000 @ 0.24 0px 4px 20px 0px; button.chakra-stack.css-kcvewa 292.9x38.5 bg #141216 r 16px; button.chakra-stack.css-kcvewa 292.9x38.5 bg #141216 r 16px; button.chakra-stack.css-kcvewa 292.9x38.5 bg #141216 r 16px; button.chakra-stack.css-kcvewa 292.9x38.5 bg #141216 r 16px |
| How | at rest |

Crops: `menu-popover-default.png`.

#### menu-item

Overflow menu item. An item inside the opened overflow popover; measured, never followed.

Page: artist. Selector: `popper item`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 313.16 x 39.15 | - |
| Padding | 0px 8px | - |
| Border | none | - |
| Radius | 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | Inter 16px/21.328px 400 | - |
| Letter spacing | normal | - |
| Colour | #ffffff | - |
| Text node | span.chakra-text.css-j29fat: Inter 13px/18.5718px 450, #ffffff | - |
| Transition | none | - |
| Icon | 23.49 x 23.49, colour #ffffff | - |
| Painted layers | button.chakra-stack.css-kcvewa 297.5x39.1 bg #141216 r 16px | - |
| Ancestor paint | 2 up div.css-d2nqmu bg #141216 shadow #000000 @ 0.24 0px 4px 20px 0px; 3 up section.chakra-popover__content.css-j0r7v1 bg #141216 shadow #000000 @ 0.4 0px 0px 25px 10px, #000000 @ 0.04 0px 10px 10px -5px | - |
| How | at rest | - |
| Error | - | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('.chakra-popover__content li, .chakra-popover__content button, .chakra-popover__content a, [role="menuitem"]').filter({ has |

Crops: `menu-item-default.png`.

#### tabs-nav

Tab strip. The Discography/Top-tracks/Similar-artists/Playlists/Bio tab bar under the artist header.

Page: artist. Selector: `nav.navbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1117 x 43 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #4e4c51; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #191922 @ 0.16 0px 2px 6px -4px |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.chakra-text.navbar-link: Inter 15px/27px 600, #ffffff |
| Transition | none |
| Painted layers | nav.navbar 1117.0x43.0 border B:1px solid #4e4c51 shadow #191922 @ 0.16 0px 2px 6px -4px; a.chakra-text.navbar-link 96.0x42.0 border B:3px solid #ad47ff; a.chakra-text.navbar-link 83.0x42.0 border B:3px solid #000000 @ 0; a.chakra-text.navbar-link 106.0x42.0 border B:3px solid #000000 @ 0; a.chakra-text.navbar-link 65.0x42.0 border B:3px solid #000000 @ 0; a.chakra-text.navbar-link 24.0x42.0 border B:3px solid #000000 @ 0 |
| How | at rest |

Crops: `tabs-nav-default.png`.

#### tab-item

Tab item. The selected "Discography" tab (a real link with an underline indicator); measured, never followed.

Page: artist. Selector: `a[role=tab].navbar-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96 x 42 | = | = | = |
| Padding | 0px 0px 12px 0px | = | = | = |
| Border | T: none; R: none; B: 3px solid #ad47ff; L: none | T: none; R: none; B: 3px solid #bb73ff; L: none | = | T: none; R: none; B: 3px solid #bb73ff; L: none |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ad47ff 0px -1px 0px 0px inset | = |
| Outline | none | = | = | = |
| Font | Inter 15px/27px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #f5f2f8 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.chakra-text.navbar-link 96.0x42.0 border B:3px solid #ad47ff | a.chakra-text.navbar-link 96.0x42.0 border B:3px solid #bb73ff | a.chakra-text.navbar-link 96.0x42.0 border B:3px solid #ad47ff shadow #ad47ff 0px -1px 0px 0px inset | a.chakra-text.navbar-link 96.0x42.0 border B:3px solid #bb73ff |
| Ancestor paint | 3 up nav.navbar shadow #191922 @ 0.16 0px 2px 6px -4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tab-item-default.png`, `tab-item-hover.png`, `tab-item-focus-visible.png`, `tab-item-pressed.png`.

#### track-list

Track list. The "Top tracks" numbered list under the tab bar.

Page: artist. Selector: `tracklist (row ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 789 x 224 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.chakra-heading.NkGZL: Inter 15px/18.75px 550, #bb73ff |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.css-1f88yyt 40.0x40.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; div.css-1f88yyt 40.0x40.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px |
| Ancestor paint | 1 up div.top-content.content-top bg #141216 |
| How | at rest |

Crops: `track-list-default.png`.

#### track-row

Track row. A numbered track row (play button, title, heart, "...") in Top tracks.

Page: artist. Selector: `div[role=row].JR0qJ`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 789 x 56 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/21.328px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | h2.chakra-heading.NkGZL: Inter 15px/18.75px 550, #bb73ff | = | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Icon | 24 x 24, colour #ffffff | = | = |
| Painted layers | div.css-1f88yyt 40.0x40.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | div.JIYRe.Fp81z 789.0x56.0 bg #141216 r 16px; div.css-1f88yyt 40.0x40.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | div.css-1f88yyt 40.0x40.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #f5f2f8 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `track-row-default.png`, `track-row-hover.png`, `track-row-focus-visible.png`.

#### track-play

Track play button. A row's purple circular play button ("Play Instant Crush ..."); measured, never pressed.

Page: artist. Selector: `button[aria-label^=Play]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | #ad47ff | #bb73ff | = | #ca97ff |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #f5f2f8 offset 0px | = |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-3yg119 32.0x32.0 bg #bb73ff r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #f5f2f8 offset 0px | button.chakra-button.css-3yg119 32.0x32.0 bg #ca97ff r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `track-play-default.png`, `track-play-hover.png`, `track-play-focus-visible.png`, `track-play-pressed.png`.

#### track-fav

Track favourite button. A row's heart icon button; measured, never toggled.

Page: artist. Selector: `button[aria-label="Add to Favourite tracks"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | transparent | #2e2c30 | = | #38373b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #ad47ff offset 0px | = |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-5xmo61 32.0x32.0 bg #2e2c30 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #ad47ff offset 0px | button.chakra-button.css-5xmo61 32.0x32.0 bg #38373b r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `track-fav-default.png`, `track-fav-hover.png`, `track-fav-focus-visible.png`, `track-fav-pressed.png`.

#### view-all

View all button. The section's "View all" ghost action; measured, never followed.

Page: artist. Selector: `View all`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 20px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Inter 13px/18.5718px 550, #ffffff | span: Inter 13px/18.5718px 550, #f5f2f8 | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.chakra-button.css-r7fpo3 85.0x32.0 border T:1px solid #4e4c51 / R:1px solid #4e4c51 / B:1px solid #4e4c51 / L:1px solid #4e4c51 r 12px outline 1px solid #000000 @ 0 offset 0px | button.chakra-button.css-r7fpo3 85.0x32.0 bg #2e2c30 border T:1px solid #59575c / R:1px solid #59575c / B:1px solid #59575c / L:1px solid #59575c r 12px outline 1px solid #000000 @ 0 offset 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `view-all-default.png`, `view-all-hover.png`, `view-all-focus-visible.png`, `view-all-pressed.png`.

#### a-section-h2

Section heading (app). A catalog section heading ("Top tracks"/"Playlists").

Page: artist. Selector: `section h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 240 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/24px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.label: Inter 20px/24px 700, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | a.chakra-link.header-link 103.0x24.0 outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `a-section-h2-default.png`.

#### playlist-card

Playlist card. A "Playlists" aside card (cover, title, fan count, heart); measured, never followed.

Page: artist. Selector: `aside playlist card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 240 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/21.328px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | a.chakra-link.css-ttnijr: Inter 15px/18.75px 550, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Icon | 0 x 0, colour #ffffff | 24 x 24, colour #ffffff | = | 24 x 24, colour #ffffff |
| Painted layers | div.css-1f88yyt 48.0x48.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; a.chakra-link.css-ttnijr 118.0x19.0 outline 2px solid #000000 @ 0 offset 2px; button.chakra-button.popper-wrapper 0.0x0.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | div.css-1f88yyt 48.0x48.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; a.chakra-link.css-ttnijr 100.0x37.8 outline 2px solid #000000 @ 0 offset 2px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | = | div.css-1f88yyt 48.0x48.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; a.chakra-link.css-ttnijr 100.0x37.8 outline 2px solid #000000 @ 0 offset 2px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `playlist-card-default.png`, `playlist-card-hover.png`, `playlist-card-focus-visible.png`, `playlist-card-pressed.png`.

#### album-cover

Album cover. The album's square cover art in the page header (the first large chakra-image).

Page: album. Selector: `img.chakra-image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 278 x 278 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `album-cover-default.png`.

#### album-title

Album title. The album's title heading.

Page: album. Selector: `album title h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 805 x 64 |
| Padding | 8px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Deezer Headline VF 56px/56px 640 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `album-title-default.png`.

#### album-play

Track play button. The first track row's purple circular play button; measured, never pressed.

Page: album. Selector: `button[aria-label^=Play]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | #ad47ff | #bb73ff | = | #ca97ff |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #f5f2f8 offset 0px | = |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-3yg119 32.0x32.0 bg #bb73ff r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #f5f2f8 offset 0px | button.chakra-button.css-3yg119 32.0x32.0 bg #ca97ff r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `album-play-default.png`, `album-play-hover.png`, `album-play-focus-visible.png`, `album-play-pressed.png`.

#### album-track-row

Album track row. A numbered track row on the album page.

Page: album. Selector: `div[role=row]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1117 x 56 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/21.328px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | h2.chakra-heading.NkGZL: Inter 15px/18.75px 550, #bb73ff | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 24 x 24, colour #ffffff | = |
| Painted layers | div.JIYRe.SiAe9 1117.0x56.0 bg #000000 r 16px; div.css-1f88yyt 40.0x40.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; span.jSAPr.llBv5 2.0x12.0 bg #ffffff r 1px | div.JIYRe.SiAe9 1117.0x56.0 bg #141216 r 16px; div.css-1f88yyt 40.0x40.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; button.chakra-button.css-3yg119 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.css-5xmo61 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; span.jSAPr.llBv5 2.0x12.0 bg #ffffff r 1px |
| How | at rest | mouse hover |

Crops: `album-track-row-default.png`, `album-track-row-hover.png`.

### Signup banner

#### signup-banner

Signup banner. The light-purple "Live the music with Deezer" upsell strip pinned above the player bar.

Page: artist. Selector: `signup banner (CTA ancestor)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 16px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | #ead1ff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.chakra-heading.css-18f9u6p: Inter 20px/24px 700, #000000 |
| Transition | none |
| Icon | 24 x 24, colour #8a22de |
| Painted layers | div.css-18x5i1s 1440.0x80.0 bg #ead1ff; div.css-t2xsmk 48.0x48.0 bg #a238ff @ 0.24 r 4px; a.chakra-button.css-1u7mkhp 166.0x48.0 bg #a238ff r 16px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest |

Crops: `signup-banner-default.png`.

#### banner-cta

Banner CTA. The banner's purple "Sign up for free" pill; measured never followed.

Page: artist. Selector: `Sign up for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 166 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #a238ff | #8a22de | = | #6908ae |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | none | none |
| Font | Inter 15px/22.5px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #e2dfe6 | = | #d5d2d8 |
| Text node | span: Inter 15px/22.5px 550, #ffffff | span: Inter 15px/22.5px 550, #e2dfe6 | = | span: Inter 15px/22.5px 550, #d5d2d8 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.chakra-button.css-1u7mkhp 166.0x48.0 bg #a238ff r 16px outline 2px solid #000000 @ 0 offset 0px | a.chakra-button.css-1u7mkhp 166.0x48.0 bg #8a22de r 16px outline 2px solid #000000 @ 0 offset 0px | a.chakra-button.css-1u7mkhp 166.0x48.0 bg #a238ff r 16px | a.chakra-button.css-1u7mkhp 166.0x48.0 bg #6908ae r 16px |
| Ancestor paint | 1 up div.css-18x5i1s bg #ead1ff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `banner-cta-default.png`, `banner-cta-hover.png`, `banner-cta-focus-visible.png`, `banner-cta-pressed.png`.

### Player bar

#### player-bar

Player bar. The bottom playback bar: track title/artists, heart and add, transport controls, queue and volume.

Page: artist. Selector: `fixed bar holding the transport buttons`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1416 x 80 |
| Padding | 0px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/21.328px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.chakra-link.css-o05beu: Inter 15px/18.75px 550, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.css-1f88yyt 48.0x48.0 border T:1px solid #000000 @ 0.12 / R:1px solid #000000 @ 0.12 / B:1px solid #000000 @ 0.12 / L:1px solid #000000 @ 0.12 r 8px; a.chakra-link.css-o05beu 301.0x19.0 outline 2px solid #000000 @ 0 offset 2px; a.chakra-link.css-o05beu 63.0x16.0 outline 2px solid #000000 @ 0 offset 2px; a.chakra-link.css-o05beu 123.0x16.0 outline 2px solid #000000 @ 0 offset 2px; button.chakra-button.css-n97h1w 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px; button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px |
| Ancestor paint | 1 up div.css-es9l8n bg #141216 |
| How | at rest |

Crops: `player-bar-default.png`.

#### player-track

Player track. The playing track's title in the player bar.

Page: artist. Selector: `player track title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 301 x 19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 15px/18.75px 550 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | a.chakra-link.css-o05beu 301.0x19.0 outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `player-track-default.png`.

#### player-play

Play button (player). The player's round purple play toggle; measured, never pressed.

Page: artist. Selector: `player Play`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | #ad47ff | #bb73ff | = | #ca97ff |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #f5f2f8 offset 0px | = |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-zv7ehe 32.0x32.0 bg #ad47ff r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-zv7ehe 32.0x32.0 bg #bb73ff r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-zv7ehe 32.0x32.0 bg #ad47ff r 256px outline 2px solid #f5f2f8 offset 0px | button.chakra-button.css-zv7ehe 32.0x32.0 bg #ca97ff r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `player-play-default.png`, `player-play-hover.png`, `player-play-focus-visible.png`, `player-play-pressed.png`.

#### player-prev

Previous button. The player’s back-track icon button (aria-label "Back"); measured, never pressed.

Page: artist. Selector: `player Back`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 256px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | - | = |
| Font | Inter 13px/18.5718px 550 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #706e73 | = | - | = |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | - | = |
| Cursor | not-allowed | = | - | = |
| Icon | 24 x 24, colour #706e73 | = | - | = |
| Painted layers | button.chakra-button.css-n97h1w 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `player-prev-default.png`, `player-prev-hover.png`, `player-prev-pressed.png`.

#### player-next

Next button. The player's next-track icon button; measured, never pressed.

Page: artist. Selector: `player Next`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | transparent | #2e2c30 | = | #38373b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #ad47ff offset 0px | = |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-n97h1w 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-n97h1w 32.0x32.0 bg #2e2c30 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-n97h1w 32.0x32.0 r 256px outline 2px solid #ad47ff offset 0px | button.chakra-button.css-n97h1w 32.0x32.0 bg #38373b r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `player-next-default.png`, `player-next-hover.png`, `player-next-focus-visible.png`, `player-next-pressed.png`.

#### player-shuffle

Shuffle button. The player's shuffle icon button; measured, never toggled.

Page: artist. Selector: `player Shuffle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | transparent | #2e2c30 | = | #38373b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #ad47ff offset 0px | = |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-n97h1w 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-n97h1w 32.0x32.0 bg #2e2c30 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-n97h1w 32.0x32.0 r 256px outline 2px solid #ad47ff offset 0px | button.chakra-button.css-n97h1w 32.0x32.0 bg #38373b r 256px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `player-shuffle-default.png`, `player-shuffle-hover.png`, `player-shuffle-focus-visible.png`, `player-shuffle-pressed.png`.

#### player-more

Player overflow. The player's context-menu icon button; measured, never opened.

Page: artist. Selector: `player Open context menu`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | transparent | #2e2c30 | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #ad47ff offset 0px | = |
| Font | Inter 13px/18.5718px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #bb73ff |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #bb73ff |
| Painted layers | button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.popper-wrapper 32.0x32.0 bg #2e2c30 r 256px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.popper-wrapper 32.0x32.0 r 256px outline 2px solid #ad47ff offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `player-more-default.png`, `player-more-hover.png`, `player-more-focus-visible.png`, `player-more-pressed.png`.

### Home (light)

#### hero-h1

Hero headline. "WHERE MUSIC COMES TO LIFE" — the condensed display headline on the light hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 900 x 378 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Deezer Brand 140px/126px 800 |
| Letter spacing | normal |
| Colour | #0f0d13 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-sub

Hero sub. "Music streaming by Deezer" under the headline.

Page: home. Selector: `hero sub`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1384 x 56 |
| Padding | 0px 0px 14px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Deezer Brand 35px/42px 700 |
| Letter spacing | normal |
| Colour | #0f0d13 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The purple "Try for free" pill under the hero copy; measured never followed.

Page: home. Selector: `hero Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 162 x 42 | = | = | 153.9 x 39.9 |
| Padding | 8px 32px | = | = | = |
| Gap | 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #a238ff | #9333e8 | = | #9333e8 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, color, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tempo-btn.tempo-btn-m 162.0x42.0 bg #a238ff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px | a.tempo-btn.tempo-btn-m 162.0x42.0 bg #9333e8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px | = | a.tempo-btn.tempo-btn-m 153.9x39.9 bg #9333e8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### rating

Rating line. The five-star "Over 3 million 5-star ratings" strip under the hero.

Page: home. Selector: `rating block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/25px 400 |
| Letter spacing | normal |
| Colour | #0f0d13 |
| Transition | none |
| How | at rest |

Crops: `rating-default.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 880 x 150 |
| Padding | 0px 28px 28px 28px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Deezer Brand 56px/normal 700 |
| Letter spacing | 0.25px |
| Colour | #fdfcfe |
| Transition | none |
| Ancestor paint | 1 up section.bg-primary.tempo-section bg #0f0d13 |
| How | at rest |

Crops: `section-h2-default.png`.

### Offers (dark marketing)

#### offers-h1

Offers headline. "Get 1 month of Premium free" — the display heading on the dark offers page.

Page: offers. Selector: `h1 on /en/offers`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 860.75 x 85 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Deezer Product 78px/normal 700 |
| Letter spacing | 0.25px |
| Colour | #fdfcfe |
| Transition | none |
| How | at rest |

Crops: `offers-h1-default.png`.

#### notice

Region notice. The "Deezer Free is not available in your country" notice card — an info/alert surface.

Page: offers. Selector: `region notice`. States: .

Not found on the page at capture time.

#### billing-toggle

Billing toggle. The Monthly/Annual segmented control over the plan cards; toggled, never checked out.

Page: offers. Selector: `ul.toggle-premiumtab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 40 | = | - | = |
| Padding | 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 256px | = | - | = |
| Background | #29282d | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #fdfcfe | = | - | = |
| Text node | span: Inter 14px/20px 600, #000000 | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.toggle-container 180.0x40.0 bg #29282d r 256px; li::after 90pxx32px bg #f8f8f9 r 256px; li::after 82pxx32px bg #f8f8f9 r 256px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-pressed.png`.

#### toggle-option

Toggle option. The "Annual" option inside the billing toggle; clicked open for the annual shot, never checked out.

Page: offers. Selector: `ul.toggle-premiumtab li Annual`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 82 x 32 | = |
| Padding | 4px 16px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 600 | = |
| Letter spacing | normal | = |
| Colour | #a9a6aa | = |
| Text node | span: Inter 14px/20px 600, #a9a6aa | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::after | 82px x 32px, absolute, bg #f8f8f9, radius 256px | = |
| Painted layers | li::after 82pxx32px bg #f8f8f9 r 256px | = |
| How | at rest | Shift+Tab, Tab |

Crops: `toggle-option-default.png`, `toggle-option-focus-visible.png`.

#### plan-card

Plan card. A white plan card (PREMIUM) on the purple band: title chip, account count, free month, price, Try-for-free CTA and Learn more.

Page: offers. Selector: `li.card-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 258 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfcfe |
| Text node | h2.unlogged-card-title: Deezer Product 24px/24px 700, #ffffff |
| Transition | none |
| Painted layers | div.unlogged-card 600.0x258.0 bg #fdfcfe r 4px; h2.unlogged-card-title 98.0x32.0 bg #a238ff r 9px / 75%; span.unlogged-card-tag 84.0x25.6 bg #ebe7ee r 4px; a.tempo-btn.tempo-btn-l 552.0x54.0 bg #121216 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-title

Plan name chip. The purple "PREMIUM" chip on the plan card.

Page: offers. Selector: `.unlogged-card-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 98 x 32 |
| Padding | 4px 8px |
| Border | none |
| Radius | 9px 75% |
| Background | #a238ff |
| Box shadow | none |
| Outline | none |
| Font | Deezer Product 24px/24px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | h2.unlogged-card-title 98.0x32.0 bg #a238ff r 9px / 75% |
| How | at rest |

Crops: `plan-title-default.png`.

#### plan-price

Plan price line. "1 month free / then US$11.99/month" on the card.

Page: offers. Selector: `.unlogged-card-description`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 171 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0f0d13 |
| Text node | a.unlogged-card-caption: Inter 20px/24px 700, #0f0d13 |
| Transition | none |
| Ancestor paint | 1 up div.unlogged-card bg #fdfcfe |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The black "Try for free" action on the plan card — links to payment/go.php; measured never followed.

Page: offers. Selector: `a.tempo-btn Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 552 x 54 | = | = | 524.4 x 51.3 |
| Padding | 12px 32px | = | = | = |
| Gap | 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #121216 | #32323d | = | #32323d |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, color, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tempo-btn.tempo-btn-l 552.0x54.0 bg #121216 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px | a.tempo-btn.tempo-btn-l 552.0x54.0 bg #32323d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px | = | a.tempo-btn.tempo-btn-l 524.4x51.3 bg #32323d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### learn-more

Learn more link. The underlined caption link inside the plan card; measured never followed.

Page: offers. Selector: `a.unlogged-card-caption`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 20px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f0d13 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `learn-more-default.png`, `learn-more-hover.png`, `learn-more-focus-visible.png`, `learn-more-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone top bar: purple heart + DEEZER wordmark, Sign-up pill, hamburger.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfcfe |
| Text node | a.topbar-action.tempo-btn: Inter 14px/normal 700, #ffffff |
| Transition | none |
| Painted layers | a.topbar-action.tempo-btn 0.0x0.0 border T:1px solid #555257 / R:1px solid #555257 / B:1px solid #555257 / L:1px solid #555257 r 12px; a.topbar-action.tempo-btn 95.0x37.0 bg #a238ff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; span.burger-line 25.0x3.0 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; span.burger-line 25.0x3.0 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; span.burger-line 25.0x3.0 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; ul.nav.burger-menu-content 0.0x0.0 bg #0f0d13 |
| Ancestor paint | 1 up body.unlogged-root-page.dir-ltr bg #0f0d13 |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-signup

Mobile Sign up. The purple Sign-up pill in the phone top bar; measured never followed.

Page: mobile. Selector: `mobile Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95 x 37 | = | = | 90.25 x 35.15 |
| Padding | 9px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 12px | = | = | = |
| Background | #a238ff | #9333e8 | = | #9333e8 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, color, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.topbar-action.tempo-btn 95.0x37.0 bg #a238ff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px | a.topbar-action.tempo-btn 95.0x37.0 bg #9333e8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px | = | a.topbar-action.tempo-btn 90.3x35.1 bg #9333e8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `m-signup-default.png`, `m-signup-hover.png`, `m-signup-focus-visible.png`, `m-signup-pressed.png`.

#### m-hamburger

Mobile hamburger. The burger icon that opens the phone nav overlay — a local UI toggle; the opened state was measured after clicking it.

Page: mobile. Selector: `.burger-menu`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 25 x 25 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Inter 16px/normal 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #fdfcfe | = | - | = | = |
| Transition | none | = | - | = | = |
| Painted layers | span.burger-line 25.0x3.0 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; span.burger-line 25.0x3.0 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; span.burger-line 25.0x3.0 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; ul.nav.burger-menu-content 0.0x0.0 bg #0f0d13 | = | - | = | span.burger-line 19.8x19.8 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; span.burger-line 25.0x3.0 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; span.burger-line 19.8x19.8 bg #f8f8f9 shadow #000000 @ 0.1 0px 4px 8px 0px, #000000 @ 0.1 0px 0px 4px 0px; ul.nav.burger-menu-content 390.0x844.0 bg #0f0d13 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |
| Text node | - | = | = | = | a.nav-main-link.backstage-header-link: Inter 20px/normal 600, #fdfcfe |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-pressed.png`, `m-hamburger-opened.png`.

#### m-drawer

Mobile drawer. The nav overlay opened by the burger toggle; its links were never followed.

Page: mobile. Selector: `ul.burger-menu-content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 89px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #0f0d13 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfcfe |
| Text node | a.nav-main-link.backstage-header-link: Inter 20px/normal 600, #fdfcfe |
| Transition | none |
| Painted layers | ul.nav.burger-menu-content 390.0x844.0 bg #0f0d13 |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-name

Mobile artist name. The artist name over the phone hero image.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 147 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Deezer Product 40px/44px 700 |
| Letter spacing | normal |
| Colour | #fdfcfe |
| Transition | none |
| How | at rest |

Crops: `m-hero-name-default.png`.

#### m-signup-card

Mobile signup card. The "Start listening on Deezer / Sign up to listen to this artist" card — the signed-out gate for playback.

Page: mobile. Selector: `mobile signup card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 221 x 46.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/16px 400 |
| Letter spacing | normal |
| Colour | #fdfcfe |
| Text node | p.catalog-embedded-section-cta-title.line-height-s: Inter 16px/19.2px 700, #ffffff |
| Transition | none |
| Ancestor paint | 1 up div.catalog-embedded-section-cta.w-full bg #29282d |
| How | at rest |

Crops: `m-signup-card-default.png`.

#### m-track-row

Mobile track row. A track row in the phone list (thumb, title, artists, duration).

Page: mobile. Selector: `div.stack-sm-horizontal`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 48 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfcfe |
| Text node | div.max-line-1.line-height-s: Inter 16px/19.2px 400, #fdfcfe |
| Transition | none |
| How | at rest |

Crops: `m-track-row-default.png`.

### Login and signup

#### login-logo

Login logo. The Deezer wordmark over the form; links back to deezer.com, measured never followed.

Page: login. Selector: `login logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 106.66 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 106.66 x 30, colour #ffffff |
| How | at rest |

Crops: `login-logo-default.png`.

#### login-field-email

Email field. The login e-mail input; focused and typed into then cleared — never submitted.

Page: login. Selector: `input.chakra-input (1st)`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 512 x 48 | = | = |
| Padding | 0px 12px 0px 16px | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #ad47ff | 2px solid #ad47ff |
| Radius | 16px | = | = |
| Background | #242326 | #2e2c30 | #2e2c30 |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Inter 15px/22.5px 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | #f5f2f8 | #f5f2f8 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff, opacity 1 | #f5f2f8, opacity 1 | #f5f2f8, opacity 1 |
| Painted layers | input.chakra-input.css-tbs8w4 512.0x48.0 bg #242326 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-tbs8w4 512.0x48.0 bg #2e2c30 border T:2px solid #ad47ff / R:2px solid #ad47ff / B:2px solid #ad47ff / L:2px solid #ad47ff r 16px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-tbs8w4 512.0x48.0 bg #2e2c30 border T:2px solid #ad47ff / R:2px solid #ad47ff / B:2px solid #ad47ff / L:2px solid #ad47ff r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-field-email-default.png`, `login-field-email-focused.png`, `login-field-email-filled.png`.

#### login-field-password

Password field. The login password input; focused and typed into then cleared — never submitted.

Page: login. Selector: `input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 512 x 48 | = | = |
| Padding | 0px 44px 0px 16px | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #ad47ff | 2px solid #ad47ff |
| Radius | 16px | = | = |
| Background | #242326 | #2e2c30 | #2e2c30 |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Inter 15px/22.5px 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | #f5f2f8 | #f5f2f8 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff, opacity 1 | #f5f2f8, opacity 1 | #f5f2f8, opacity 1 |
| Painted layers | input.chakra-input.css-xc97c3 512.0x48.0 bg #242326 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-xc97c3 512.0x48.0 bg #2e2c30 border T:2px solid #ad47ff / R:2px solid #ad47ff / B:2px solid #ad47ff / L:2px solid #ad47ff r 16px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-xc97c3 512.0x48.0 bg #2e2c30 border T:2px solid #ad47ff / R:2px solid #ad47ff / B:2px solid #ad47ff / L:2px solid #ad47ff r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "not-a-real-password", then deleted; nothing sent |

Crops: `login-field-password-default.png`, `login-field-password-focused.png`, `login-field-password-filled.png`.

#### login-show-password

Show-password button. The eye icon button inside the password field (a local reveal toggle); measured, never clicked.

Page: login. Selector: `button[aria-label=show-password]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 256px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | = | = |
| Font | Inter 15px/22.5px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.chakra-button.css-18xil4h 48.0x48.0 r 256px outline 2px solid #000000 @ 0 offset 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-show-password-default.png`, `login-show-password-hover.png`, `login-show-password-focus-visible.png`, `login-show-password-pressed.png`.

#### login-submit

Log in submit. The login submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `login Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 512 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ad47ff | #bb73ff | = | #ca97ff |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #f5f2f8 offset 0px | = |
| Font | Inter 15px/22.5px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Text node | span: Inter 15px/22.5px 550, #ffffff | span: Inter 15px/22.5px 550, #f5f2f8 | = | span: Inter 15px/22.5px 550, #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.chakra-button.css-19vbpfx 512.0x48.0 bg #ad47ff r 16px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-19vbpfx 512.0x48.0 bg #bb73ff r 16px outline 2px solid #000000 @ 0 offset 0px | button.chakra-button.css-19vbpfx 512.0x48.0 bg #ad47ff r 16px outline 2px solid #f5f2f8 offset 0px | button.chakra-button.css-19vbpfx 512.0x48.0 bg #ca97ff r 16px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-forgot

Forgotten-password link. The "Forgotten password?" helper link; measured, never followed.

Page: login. Selector: `a.chakra-form__helper-text`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 512 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #ad47ff offset 1px | = |
| Font | Inter 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a19fa4 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.chakra-form__helper-text.css-1u9opuw 512.0x17.0 outline 1px auto #ad47ff offset 1px | = |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`, `login-forgot-focus-visible.png`, `login-forgot-pressed.png`.

#### login-signup

Signup link (login). The "Sign up" action beside the form; measured, never followed.

Page: login. Selector: `login Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | = | = |
| Font | Inter 14px/21px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ad47ff | = | = | #ca97ff |
| Text node | span: Inter 14px/21px 700, #ad47ff | = | = | span: Inter 14px/21px 700, #ca97ff |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.chakra-button.css-fo53qv 53.0x17.0 r 16px outline 2px solid #000000 @ 0 offset 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-signup-default.png`, `login-signup-hover.png`, `login-signup-focus-visible.png`, `login-signup-pressed.png`.

#### social-btn

Social login button. A Google/Facebook/Apple round social sign-in button; measured, never followed.

Page: login. Selector: `button[aria-label=google]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #4e4c51 | 1px solid #59575c | 1px solid #ad47ff | 1px solid #656367 |
| Radius | 256px | = | = | = |
| Background | transparent | #2e2c30 | = | #38373b |
| Box shadow | none | = | = | = |
| Outline | 1px solid #000000 @ 0 offset 0px | = | 1px solid #ad47ff offset 0px | = |
| Font | Inter 15px/22.5px 550 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #f5f2f8 | = | #e2dfe6 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | 24 x 24, colour #f5f2f8 | = | 24 x 24, colour #e2dfe6 |
| Painted layers | button.chakra-button.css-ogbv3a 48.0x48.0 border T:1px solid #4e4c51 / R:1px solid #4e4c51 / B:1px solid #4e4c51 / L:1px solid #4e4c51 r 256px outline 1px solid #000000 @ 0 offset 0px | button.chakra-button.css-ogbv3a 48.0x48.0 bg #2e2c30 border T:1px solid #59575c / R:1px solid #59575c / B:1px solid #59575c / L:1px solid #59575c r 256px outline 1px solid #000000 @ 0 offset 0px | button.chakra-button.css-ogbv3a 48.0x48.0 border T:1px solid #ad47ff / R:1px solid #ad47ff / B:1px solid #ad47ff / L:1px solid #ad47ff r 256px outline 1px solid #ad47ff offset 0px | button.chakra-button.css-ogbv3a 48.0x48.0 bg #38373b border T:1px solid #656367 / R:1px solid #656367 / B:1px solid #656367 / L:1px solid #656367 r 256px outline 1px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-btn-default.png`, `social-btn-hover.png`, `social-btn-focus-visible.png`, `social-btn-pressed.png`.

#### signup-field

Signup field. A signup form input; focused and typed into then cleared — never submitted.

Page: signup. Selector: `signup input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 512 x 48 | = | = |
| Padding | 0px 12px 0px 16px | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #ad47ff | 2px solid #ad47ff |
| Radius | 16px | = | = |
| Background | #242326 | #2e2c30 | #2e2c30 |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Inter 15px/22.5px 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | #f5f2f8 | #f5f2f8 |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #706e73, opacity 1 | = | = |
| Painted layers | input.chakra-input.css-tbs8w4 512.0x48.0 bg #242326 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-tbs8w4 512.0x48.0 bg #2e2c30 border T:2px solid #ad47ff / R:2px solid #ad47ff / B:2px solid #ad47ff / L:2px solid #ad47ff r 16px outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-tbs8w4 512.0x48.0 bg #2e2c30 border T:2px solid #ad47ff / R:2px solid #ad47ff / B:2px solid #ad47ff / L:2px solid #ad47ff r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-field-default.png`, `signup-field-focused.png`, `signup-field-filled.png`.

#### signup-cta

Signup action. The signup form's submit action; its states were measured but it was never clicked — nothing was submitted.

Page: signup. Selector: `signup submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 512 x 48 | = | - | = |
| Padding | 12px 24px | = | - | = |
| Gap | 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 16px | = | - | = |
| Background | #2e2c30 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | - | = |
| Font | Inter 15px/22.5px 550 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #706e73 | = | - | = |
| Text node | span: Inter 15px/22.5px 550, #706e73 | = | - | = |
| Transition | background-color, border-color, outline-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.chakra-button.css-19vbpfx 512.0x48.0 bg #2e2c30 r 16px outline 2px solid #000000 @ 0 offset 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `signup-cta-default.png`, `signup-cta-hover.png`, `signup-cta-pressed.png`.

## Transitions declared in the readable stylesheets

deezer.com serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- album: `opacity 0.2s ease-in-out`, `transform 0.2s`, `opacity 0.2s ease-out, transform 0.2s ease-out`, `opacity 0.3s`, `width 0.1s linear`, `background-color 0.3s cubic-bezier(0.4, 0, 0.23, 1)`, `none`, `opacity 0.5s`, `background-color 0.3s`, `color 0.3s`, `max-height 0.3s ease-in-out`

- artist: `opacity 0.2s ease-in-out`, `transform 0.2s`, `opacity 0.2s ease-out, transform 0.2s ease-out`, `opacity 0.3s`, `width 0.1s linear`, `background-color 0.3s cubic-bezier(0.4, 0, 0.23, 1)`, `none`, `opacity 0.5s`, `background-color 0.3s`, `color 0.3s`, `max-height 0.3s ease-in-out`

- home: `opacity 0.2s ease-in-out`, `transform 0.2s`, `opacity 0.2s ease-out, transform 0.2s ease-out`, `opacity 0.3s`, `width 0.1s linear`, `background-color 0.3s cubic-bezier(0.4, 0, 0.23, 1)`, `none`, `opacity 0.5s`, `background-color 0.3s`, `color 0.3s`, `max-height 0.3s ease-in-out`

- login: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- offers: `opacity 0.2s ease-in-out`, `transform 0.2s`, `opacity 0.2s ease-out, transform 0.2s ease-out`, `opacity 0.3s`, `width 0.1s linear`, `background-color 0.3s cubic-bezier(0.4, 0, 0.23, 1)`, `none`, `opacity 0.5s`, `background-color 0.3s`, `color 0.3s`, `max-height 0.3s ease-in-out`

- signup: `width 250ms cubic-bezier(0.16, 1, 0.3, 1)`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`
