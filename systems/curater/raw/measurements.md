# Component measurements

Computed styles read from curater.org on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home, /feed, /taste, a /curation/<id> detail, a /ravi profile and /terms (the Mobile group on the home and /feed) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-rail

Nav rail. The 48px-wide vertical icon rail (Home / Taste / Notifications / Profile / Create / Settings).

Page: home. Selector: `nav._nav_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 328 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| Icon | 20 x 20, colour oklch(0.552 0.016 285.938) |
| Painted layers | div._newDigestIndicator_1psr6_136 8.0x8.0 bg #e20000 r 9999px |
| How | at rest |

Crops: `nav-rail-default.png`.

#### nav-button

Nav button. A 48x48 rail icon button (Home); measured, never followed.

Page: home. Selector: `nav button._navButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | oklch(0.967 0.001 286.375) | = | oklch(0.967 0.001 286.375) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.552 0.016 285.938) | oklch(0.141 0.005 285.823) | = | oklch(0.141 0.005 285.823) |
| Transition | background-color, color 0.15s, 0.15s cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour oklch(0.552 0.016 285.938) | 20 x 20, colour oklch(0.141 0.005 285.823) | = | 20 x 20, colour oklch(0.141 0.005 285.823) |
| Painted layers | div._newDigestIndicator_1psr6_136 8.0x8.0 bg #e20000 r 9999px | a._navButton_1psr6_88 48.0x48.0 bg oklch(0.967 0.001 286.375) r 9999px; div._newDigestIndicator_1psr6_136 8.0x8.0 bg #e20000 r 9999px | a._navButton_1psr6_88 48.0x48.0 r 9999px outline 2px solid oklch(0.871 0.006 286.286) offset 2px; div._newDigestIndicator_1psr6_136 8.0x8.0 bg #e20000 r 9999px | a._navButton_1psr6_88 48.0x48.0 bg oklch(0.967 0.001 286.375) r 9999px; div._newDigestIndicator_1psr6_136 8.0x8.0 bg #e20000 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-button-default.png`, `nav-button-hover.png`, `nav-button-focus-visible.png`, `nav-button-pressed.png`.

#### nav-button-active

Nav button, active. The active rail button (the .active sibling) — its highlighted state.

Page: feed. Selector: `nav a.active`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #f2f2f2 |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | background-color, color 0.15s, 0.15s cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1) delay 0s, 0s |
| Cursor | pointer |
| Icon | 20 x 20, colour oklch(0.141 0.005 285.823) |
| Painted layers | a._navButton_1psr6_88.active 48.0x48.0 bg #f2f2f2 r 9999px |
| How | at rest |

Crops: `nav-button-active-default.png`.

#### settings-btn

Settings button. The 48x48 settings gear at the rail foot; measured, never followed.

Page: home. Selector: `button._settingsButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | oklch(0.967 0.001 286.375) | = | oklch(0.967 0.001 286.375) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.552 0.016 285.938) | oklch(0.141 0.005 285.823) | = | oklch(0.141 0.005 285.823) |
| Transition | background-color, color 0.15s, 0.15s cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour oklch(0.552 0.016 285.938) | 20 x 20, colour oklch(0.141 0.005 285.823) | = | 20 x 20, colour oklch(0.141 0.005 285.823) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button._settingsButton_1psr6_89 48.0x48.0 bg oklch(0.967 0.001 286.375) r 9999px | button._settingsButton_1psr6_89 48.0x48.0 r 9999px outline 2px solid oklch(0.871 0.006 286.286) offset 2px | button._settingsButton_1psr6_89 48.0x48.0 bg oklch(0.967 0.001 286.375) r 9999px |

Crops: `settings-btn-default.png`, `settings-btn-hover.png`, `settings-btn-focus-visible.png`, `settings-btn-pressed.png`.

#### signin-btn

Sign-in button. "Sign in or create account" — the 259x58 auth CTA; measured, never followed.

Page: home. Selector: `sign-in button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 259.45 x 58 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid oklch(0.95 0.004 286.32) | = | = | = |
| Radius | 9999px | = | = | = |
| Background | oklch(1 0 0) | #f2f2f2 | = | #f2f2f2 |
| Box shadow | #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | oklch(0.21 0.006 285.885) | = | oklch(0.21 0.006 285.885) |
| Transition | all 0.15s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823), fill #000000 | 16 x 16, colour oklch(0.21 0.006 285.885), fill #000000 | = | 16 x 16, colour oklch(0.21 0.006 285.885), fill #000000 |
| Painted layers | button.w-full 259.5x58.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | button.w-full 259.5x58.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | = | button.w-full 259.5x58.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 2) |

Crops: `signin-btn-default.png`, `signin-btn-hover.png`, `signin-btn-focus-visible.png`, `signin-btn-pressed.png`.

#### tab-button

Feed tab. A 40px feed tab (Featured / For You / More); measured, never activated.

Page: feed. Selector: `._tabButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.39 x 40 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Transition | color 0.15s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button._tabButton_n5s4s_56 64.4x40.0 outline 2px solid oklch(0.871 0.006 286.286) offset 2px | = |

Crops: `tab-button-default.png`, `tab-button-hover.png`, `tab-button-focus-visible.png`, `tab-button-pressed.png`.

#### search-toggle

Search toggle. The 20x20 search icon that reveals the search field.

Page: feed. Selector: `._searchToggle_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.552 0.016 285.938) | oklch(0.141 0.005 285.823) | = | oklch(0.141 0.005 285.823) |
| Transition | color 0.15s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour oklch(0.552 0.016 285.938) | 14 x 14, colour oklch(0.141 0.005 285.823) | = | 14 x 14, colour oklch(0.141 0.005 285.823) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button._searchToggle_n5s4s_139 20.0x20.0 outline 2px solid oklch(0.871 0.006 286.286) offset 2px | = |

Crops: `search-toggle-default.png`, `search-toggle-hover.png`, `search-toggle-focus-visible.png`, `search-toggle-pressed.png`.

#### login-btn

Login button. "Log in or sign up" — the header auth link; measured, never followed.

Page: feed. Selector: `._signInButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102.08 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #7c7c7c | oklch(0.141 0.005 285.823) | = | oklch(0.141 0.005 285.823) |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._signInButton_n5s4s_215 102.1x21.0 outline 2px solid oklch(0.871 0.006 286.286) offset 2px | = |

Crops: `login-btn-default.png`, `login-btn-hover.png`, `login-btn-focus-visible.png`, `login-btn-pressed.png`.

#### search-field

Search field. The "Search curations..." input revealed by the toggle; focused locally, never submitted.

Page: feed. Selector: `._searchField_*`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 170 x 30 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABCDiatype 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | oklch(0.141 0.005 285.823) | = |
| Transition | opacity 0.15s cubic-bezier(0.19, 1, 0.22, 1) | = |
| Cursor | text | = |
| Placeholder | #afafaf, opacity 1 | = |
| Ancestor paint | 1 up div._search_n5s4s_112 shadow oklch(0.871 0.006 286.286 / 0.5) 0px 0px 0px 3px | = |
| How | at rest | clicked into the field |

Crops: `search-field-default.png`, `search-field-focused.png`.

### Home

#### trend-header

Trending header. "Trending on Curater / What our community has been sharing lately" + the sign-in CTA.

Page: home. Selector: `._header_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 544 x 196 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Text node | span: ABCDiatype 24px/30px 500, oklch(0.141 0.005 285.823) |
| Transition | none |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823), fill #000000 |
| Painted layers | button.w-full 259.5x58.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `trend-header-default.png`.

#### trend-card

Trend card. A 544x570 trending curation card: thumbnails, headline, description, curator avatars; measured, never followed.

Page: home. Selector: `div._card_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 544 x 492.39 | = | = | = |
| Padding | 80px 72px | = | = | = |
| Gap | 32px | = | = | = |
| Border | 1px solid #e8e7e7 | = | = | = |
| Radius | 24px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.02 0px 14px 54px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Text node | h2._headline_hilw7_350: ABCDiatype 24px/30px 500, oklch(0.141 0.005 285.823) | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div._card_hilw7_153 544.0x492.4 bg #ffffff border T:1px solid #e8e7e7 / R:1px solid #e8e7e7 / B:1px solid #e8e7e7 / L:1px solid #e8e7e7 r 24px shadow #000000 @ 0.02 0px 14px 54px 0px; a._thumbnail_hilw7_189 100.8x100.8 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px; a::before._thumbnail_hilw7_189 96.7969pxx96.7969px bg #000000 @ 0.05; a._thumbnail_hilw7_189 100.8x100.8 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px; a::before._thumbnail_hilw7_189 96.7969pxx96.7969px bg #000000 @ 0.05; a._thumbnail_hilw7_189 100.8x100.8 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px | = | div._card_hilw7_153 544.0x492.4 bg #ffffff border T:1px solid #e8e7e7 / R:1px solid #e8e7e7 / B:1px solid #e8e7e7 / L:1px solid #e8e7e7 r 24px shadow #000000 @ 0.02 0px 14px 54px 0px; a._thumbnail_hilw7_189 100.8x100.8 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px outline 2px solid oklch(0.871 0.006 286.286) offset 2px; a::before._thumbnail_hilw7_189 96.7969pxx96.7969px bg #000000 @ 0.05; a._thumbnail_hilw7_189 100.8x100.8 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px; a::before._thumbnail_hilw7_189 96.7969pxx96.7969px bg #000000 @ 0.05; a._thumbnail_hilw7_189 100.8x100.8 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `trend-card-default.png`, `trend-card-hover.png`, `trend-card-focus-visible.png`, `trend-card-pressed.png`.

#### card-thumb

Card thumbnail. A 100x100 curation thumbnail tile.

Page: home. Selector: `a._thumbnail_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 100.8 x 100.8 |
| Padding | 0px |
| Border | 2px solid #ffffff |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | transform 0.15s cubic-bezier(0.19, 1, 0.22, 1) |
| Cursor | pointer |
| ::before | 96.7969px x 96.7969px, absolute, bg #000000 @ 0.05, radius 0px |
| Painted layers | a._thumbnail_hilw7_189 100.8x100.8 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px; a::before._thumbnail_hilw7_189 96.7969pxx96.7969px bg #000000 @ 0.05 |
| Ancestor paint | 2 up div._card_hilw7_153 bg #ffffff shadow #000000 @ 0.02 0px 14px 54px 0px |
| How | at rest |

Crops: `card-thumb-default.png`.

#### card-headline

Card headline. The curation headline (h2, 398px wide).

Page: home. Selector: `._headline_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 398 x 90 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 24px/30px 500 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| Ancestor paint | 2 up div._card_hilw7_153 bg #ffffff shadow #000000 @ 0.02 0px 14px 54px 0px |
| How | at rest |

Crops: `card-headline-default.png`.

#### card-desc

Card description. The curator's description copy under the headline.

Page: home. Selector: `._description_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 398 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | #7c7c7c |
| Transition | none |
| Ancestor paint | 2 up div._card_hilw7_153 bg #ffffff shadow #000000 @ 0.02 0px 14px 54px 0px |
| How | at rest |

Crops: `card-desc-default.png`.

#### curated-label

Curated-by label. The "CURATED BY" micro-label.

Page: home. Selector: `._curatorsLabel_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 73.88 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 12px/12px 500 |
| Letter spacing | normal |
| Colour | #afafaf |
| Transition | none |
| Ancestor paint | 2 up div._card_hilw7_153 bg #ffffff shadow #000000 @ 0.02 0px 14px 54px 0px |
| How | at rest |

Crops: `curated-label-default.png`.

#### card-avatar

Curator avatar. A 24x24 curator avatar in the card.

Page: home. Selector: `._avatarItem_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | 2px solid #ffffff |
| Radius | 1600px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| Cursor | pointer |
| Painted layers | a._avatarItem_hilw7_400 24.0x24.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 1600px |
| Ancestor paint | 3 up div._card_hilw7_153 bg #ffffff shadow #000000 @ 0.02 0px 14px 54px 0px |
| How | at rest |

Crops: `card-avatar-default.png`.

### Feed

#### feed-heading

Feed heading. "Browse by themes" — the feed section heading.

Page: feed. Selector: `._heading_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1264 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 500 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| How | at rest |

Crops: `feed-heading-default.png`.

#### theme-card

Theme card. A 224x271 theme tile ("Visual Identity / 16 curations"); measured, never followed.

Page: feed. Selector: `a._card_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 271 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Text node | span._name_2m4ag_126: ABCDiatype 14px/14px 500, oklch(0.141 0.005 285.823) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div._thumb_2m4ag_63 224.0x224.0 bg #f9f6f6 r 20px; img 112.0x112.0 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px; img 82.8x128.0 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px; img 112.0x112.0 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px; img 112.0x112.0 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px; img 112.0x111.9 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px | = | a._card_2m4ag_36 224.0x271.0 outline 2px solid oklch(0.871 0.006 286.286) offset 2px; div._thumb_2m4ag_63 224.0x224.0 bg #f9f6f6 r 20px; img 112.0x112.0 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px; img 82.8x128.0 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px; img 112.0x112.0 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px; img 112.0x112.0 bg #f2f2f2 r 8px shadow #000000 @ 0.16 0px 2px 12px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `theme-card-default.png`, `theme-card-hover.png`, `theme-card-focus-visible.png`, `theme-card-pressed.png`.

#### curator-label

Curator label. A curator chip ("Ravi", "Glauber") over a feed entry; measured, never followed.

Page: feed. Selector: `._curatorLabel_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.8 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Text node | span._curatorName_njeuw_68: ABCDiatype 14px/21px 500, oklch(0.141 0.005 285.823) | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._curatorLabel_njeuw_60 66.8x32.0 outline 2px solid oklch(0.871 0.006 286.286) offset 2px | = |

Crops: `curator-label-default.png`, `curator-label-hover.png`, `curator-label-focus-visible.png`, `curator-label-pressed.png`.

#### title-link

Curation title. The large editorial curation title link; measured, never followed.

Page: feed. Selector: `._titleLink_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 415.45 x 212 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 24px/30px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Painted layers | - | = | a._titleLink_1l58y_93 415.5x212.0 outline 2px solid oklch(0.871 0.006 286.286) offset 2px | = |

Crops: `title-link-default.png`, `title-link-hover.png`, `title-link-focus-visible.png`, `title-link-pressed.png`.

#### save-btn

Save button. The save/bookmark control ("1", "Add to my taste"); measured, never pressed.

Page: feed. Selector: `._saveButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42.55 x 28 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid oklch(0.95 0.004 286.32) | = | = | = |
| Radius | 9999px | = | = | = |
| Background | oklch(1 0 0) | #f2f2f2 | = | #f2f2f2 |
| Box shadow | #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 12px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | oklch(0.21 0.006 285.885) | = | oklch(0.21 0.006 285.885) |
| Text node | span: ABCDiatype 12px/18px 500, oklch(0.141 0.005 285.823) | span: ABCDiatype 12px/18px 500, oklch(0.21 0.006 285.885) | = | span: ABCDiatype 12px/18px 500, oklch(0.21 0.006 285.885) |
| Transition | all 0.15s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823) | 16 x 16, colour oklch(0.21 0.006 285.885) | = | 16 x 16, colour oklch(0.21 0.006 285.885) |
| Painted layers | button._saveButton_11e54_1 42.5x28.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | button._saveButton_11e54_1 42.5x28.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | button._saveButton_11e54_1 42.5x28.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px outline 2px solid oklch(0.871 0.006 286.286) offset 2px | button._saveButton_11e54_1 42.5x28.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 2) |

Crops: `save-btn-default.png`, `save-btn-hover.png`, `save-btn-focus-visible.png`, `save-btn-pressed.png`.

#### media-item

Media tile. A large media tile in the entry's mosaic (up to 1080x540).

Page: feed. Selector: `._mediaItem_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 540 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `media-item-default.png`.

#### album-link

Album tile. A 540x540 album tile ("ALBUM / 8 TRACKS"); measured, never followed.

Page: feed. Selector: `._albumLink_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 540 x 540 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Text node | span._albumEyebrowTop_1l58y_28: ABCDiatype 12px/12px 500, #afafaf | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div._albumDisc_1l58y_210 540.0x540.0 bg #f9f6f6 r 9999px; img._albumCover_1l58y_225 356.4x356.4 r 6px shadow #000000 @ 0.04 0px 2px 4px -1px, #000000 @ 0.12 0px 12px 32px -4px | div._albumDisc_1l58y_210 540.0x540.0 bg #f9f6f6 r 9999px; img._albumCover_1l58y_225 356.4x356.4 r 6px shadow #000000 @ 0.04 0px 2px 4px -1px, #000000 @ 0.12 0px 12px 32px -4px; span._albumOverlay_1l58y_240 356.4x356.4 bg #000000 @ 0.45 r 6px; div._bubble_x6xan_36 180.0x32.8 bg oklch(0.141 0.005 285.823) r 9999px shadow #000000 @ 0.04 0px 2px 4px -1px, #000000 @ 0.12 0px 12px 32px -4px | a._albumLink_1l58y_187 540.0x540.0 outline 2px solid oklch(0.871 0.006 286.286) offset 2px; div._albumDisc_1l58y_210 540.0x540.0 bg #f9f6f6 r 9999px; img._albumCover_1l58y_225 356.4x356.4 r 6px shadow #000000 @ 0.04 0px 2px 4px -1px, #000000 @ 0.12 0px 12px 32px -4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Icon | - | 20 x 20, colour oklch(0.141 0.005 285.823), fill #000000 | = | = |

Crops: `album-link-default.png`, `album-link-hover.png`, `album-link-focus-visible.png`, `album-link-pressed.png`.

### TasteScope

#### taste-desc

TasteScope panel. The "SOON / TasteScope — it captures all dimensions of your aesthetic identity" teaser panel.

Page: taste. Selector: `[class*="_mainDescription_"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 256 x 788 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 20px/27.5px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p._soonText_19p2q_106: ABCDiatype 12px/12px 500, #afafaf |
| Transition | none |
| Painted layers | p._soonText_19p2q_106 51.3x20.0 bg #333333 r 9999px |
| How | main-world query (locators never settle on this route) |

Crops: none.

#### taste-h4

TasteScope heading. The "TasteScope" teaser heading.

Page: taste. Selector: `js:[...document.querySelectorAll('h4')].find((h)=>/tastescope/i.test(h.innerText))`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 256 x 27.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 20px/27.5px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | main-world query (locators never settle on this route) |

Crops: none.

#### taste-canvas

BrandGlobe canvas. The 1360x900 WebGL globe canvas behind the teaser.

Page: taste. Selector: `js:[...document.querySelectorAll('canvas')].reduce((a,b)=>{const ra=a&&a.getBoundingClientRect(),rb=b.getBoundingClientRect();return (!a//rb.width>ra.width)?b:a;})`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1360 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| How | main-world query (locators never settle on this route) |

Crops: none.

### Curation

#### back-btn

Back button. The 36x36 back-arrow button; measured, never followed.

Page: curation. Selector: `._backButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823) | 16 x 16, colour oklch(0.21 0.006 285.885) | = | = |
| Painted layers | span 36.0x36.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | span 36.0x36.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | a._backButton_1fhe2_142 36.0x36.0 outline 2px solid oklch(0.871 0.006 286.286) offset 2px; span 36.0x36.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `back-btn-default.png`, `back-btn-hover.png`, `back-btn-focus-visible.png`, `back-btn-pressed.png`.

#### options-btn

Options button. The 32x32 options (…) button.

Page: curation. Selector: `._hiddenOptionsButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid oklch(0.95 0.004 286.32) | = | = | = |
| Radius | 9999px | = | = | = |
| Background | oklch(1 0 0) | oklch(0.967 0.001 286.375) | = | oklch(0.967 0.001 286.375) |
| Box shadow | #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823) | = | = | = |
| Painted layers | button._hiddenOptionsButton_1fhe2_218 32.0x32.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | button._hiddenOptionsButton_1fhe2_218 32.0x32.0 bg oklch(0.967 0.001 286.375) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | button._hiddenOptionsButton_1fhe2_218 32.0x32.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px outline 2px solid oklch(0.871 0.006 286.286) offset 2px | button._hiddenOptionsButton_1fhe2_218 32.0x32.0 bg oklch(0.967 0.001 286.375) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `options-btn-default.png`, `options-btn-hover.png`, `options-btn-focus-visible.png`, `options-btn-pressed.png`.

#### curation-h1

Curation title. The 350x240 editorial curation title (h1).

Page: curation. Selector: `h1._title_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 240 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 24px/30px 500 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Text node | span: ABCDiatype 24px/30px 500, oklch(0.141 0.005 285.823) |
| Transition | none |
| How | at rest |

Crops: `curation-h1-default.png`.

#### sso-btn

SSO button. "Continue with Google" — the 350x58 SSO button; measured, never pressed.

Page: curation. Selector: `._signInButtonContainer_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 58 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Text node | button.w-full: ABCDiatype 16px/24px 500, oklch(0.141 0.005 285.823) | button.w-full: ABCDiatype 16px/24px 500, oklch(0.21 0.006 285.885) | = | = |
| Transition | none | = | = | = |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823), fill #000000 | 16 x 16, colour oklch(0.21 0.006 285.885), fill #000000 | = | = |
| Painted layers | button.w-full 350.0x58.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | button.w-full 350.0x58.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | button.w-full 350.0x58.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px outline 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-btn-default.png`, `sso-btn-hover.png`, `sso-btn-focus-visible.png`, `sso-btn-pressed.png`.

#### similar-label

Similar label. The "SEARCH SIMILAR ON" micro-heading.

Page: curation. Selector: `h3 similar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 12px/12px 500 |
| Letter spacing | normal |
| Colour | #afafaf |
| Transition | none |
| How | at rest |

Crops: `similar-label-default.png`.

#### similar-btn

Similar-search button. A 132x45 outbound similar-search button (Pinterest / Cosmos); measured, never followed.

Page: curation. Selector: `a._button_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132.78 x 45 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | oklch(0.967 0.001 286.375) | oklch(0.32109 0.0000159743 none / 0.1) | = | oklch(0.32109 0.0000159743 none / 0.1) |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | oklch(0.21 0.006 285.885) | = | oklch(0.21 0.006 285.885) |
| Text node | span: ABCDiatype 14px/21px 500, #7c7c7c | span: ABCDiatype 14px/21px 500, oklch(0.141 0.005 285.823) | = | span: ABCDiatype 14px/21px 500, oklch(0.141 0.005 285.823) |
| Transition | background-color, color 0.15s, 0.15s cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823) | 16 x 16, colour oklch(0.21 0.006 285.885) | = | 16 x 16, colour oklch(0.21 0.006 285.885) |
| Painted layers | a._button_fs8oe_50 132.8x45.0 bg oklch(0.967 0.001 286.375) r 9999px | a._button_fs8oe_50 132.8x45.0 bg oklch(0.32109 0.0000159743 none / 0.1) r 9999px | a._button_fs8oe_50 132.8x45.0 bg oklch(0.967 0.001 286.375) r 9999px outline 2px solid oklch(0.871 0.006 286.286) offset 2px | a._button_fs8oe_50 132.8x45.0 bg oklch(0.32109 0.0000159743 none / 0.1) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `similar-btn-default.png`, `similar-btn-hover.png`, `similar-btn-focus-visible.png`, `similar-btn-pressed.png`.

#### pins-label

Pins label. The "PINS" micro-heading.

Page: curation. Selector: `h3 pins`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 28.02 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 12px/12px 500 |
| Letter spacing | normal |
| Colour | #afafaf |
| Transition | none |
| How | at rest |

Crops: `pins-label-default.png`.

### Profile

#### profile-name

Profile name. The "Ravi Vasavan" profile heading.

Page: profile. Selector: `h1._name_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 93.2 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 500 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| How | at rest |

Crops: `profile-name-default.png`.

#### profile-avatar

Profile avatar. The 28x28 profile avatar.

Page: profile. Selector: `._userAvatar_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 28 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| How | at rest |

Crops: `profile-avatar-default.png`.

#### tastescope-btn

TasteScope button. The 129x42 "TasteScope" header button; measured, never followed.

Page: profile. Selector: `._tasteScopeButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 129.84 x 42 | = | = | = |
| Padding | 20px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid oklch(0.95 0.004 286.32) | = | = | = |
| Radius | 9999px | = | = | = |
| Background | oklch(1 0 0) | #f2f2f2 | = | #f2f2f2 |
| Box shadow | #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | oklch(0.21 0.006 285.885) | = | oklch(0.21 0.006 285.885) |
| Transition | all 0.15s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823) | 16 x 16, colour oklch(0.21 0.006 285.885) | = | 16 x 16, colour oklch(0.21 0.006 285.885) |
| Painted layers | a._tasteScopeButton_12q4j_186 129.8x42.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | a._tasteScopeButton_12q4j_186 129.8x42.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | = | a._tasteScopeButton_12q4j_186 129.8x42.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 2) |

Crops: `tastescope-btn-default.png`, `tastescope-btn-hover.png`, `tastescope-btn-focus-visible.png`, `tastescope-btn-pressed.png`.

#### profile-bio

Profile bio. The curator's bio paragraph.

Page: profile. Selector: `._description_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 379.19 x 156.73 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/22.4px 500 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| How | at rest |

Crops: `profile-bio-default.png`.

#### profile-item

Profile item. A 268x380 profile curation item (category, title, saved mark, menu); measured, never followed.

Page: profile. Selector: `article._item_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 268.27 x 380.27 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | = | = | = |
| Text node | span._categoryBadge_19sub_281: ABCDiatype 12px/18px 500, #afafaf | = | = | = |
| Transition | none | = | = | = |
| Icon | 10 x 10, colour #afafaf | = | = | = |
| Painted layers | div._imageContainer_19sub_46 268.3x268.3 bg oklch(0.967 0.001 286.375) r 20px; span._userAvatar_19sub_325 16.0x16.0 bg #d4d4d4 r 9999px; button._menuButton_19sub_40 28.0x28.0 bg #000000 @ 0.2 r 9999px | = | a._link_19sub_50 268.3x380.3 outline 2px solid oklch(0.871 0.006 286.286) offset 2px; div._imageContainer_19sub_46 268.3x268.3 bg oklch(0.967 0.001 286.375) r 20px; span._userAvatar_19sub_325 16.0x16.0 bg #d4d4d4 r 9999px; button._menuButton_19sub_40 28.0x28.0 bg #000000 @ 0.2 r 9999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `profile-item-default.png`, `profile-item-hover.png`, `profile-item-focus-visible.png`, `profile-item-pressed.png`.

#### item-title

Item title. The item's 268x60 title.

Page: profile. Selector: `h3._title_*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 268.27 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/20px 500 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `item-title-default.png`.

#### item-menu

Item menu. The 28x28 item overflow menu; opened locally, never an action taken.

Page: profile. Selector: `._menuButton_*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 @ 0.2 | #000000 @ 0.9 | = | #000000 @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity, background-color 0.15s, 0.15s cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1) delay 0s, 0s | = | = | = |
| Opacity | 0 | - | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button._menuButton_19sub_40 28.0x28.0 bg #000000 @ 0.2 r 9999px | button._menuButton_19sub_40 28.0x28.0 bg #000000 @ 0.9 r 9999px | button._menuButton_19sub_40 28.0x28.0 bg #000000 @ 0.2 r 9999px outline 2px solid oklch(0.871 0.006 286.286) offset 2px | button._menuButton_19sub_40 28.0x28.0 bg #000000 @ 0.9 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `item-menu-default.png`, `item-menu-hover.png`, `item-menu-focus-visible.png`, `item-menu-pressed.png`.

### Legal

#### legal-h1

Legal heading. "Terms of Use" — the legal page heading.

Page: terms. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 55.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 48px/55.2px 500 |
| Letter spacing | -1.28px |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| How | at rest |

Crops: `legal-h1-default.png`.

#### legal-body

Legal paragraph. A body paragraph of the terms text.

Page: terms. Selector: `legal p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 14px/21px 400 |
| Letter spacing | normal |
| Colour | oklch(0.552 0.016 285.938) |
| Transition | none |
| How | at rest |

Crops: `legal-body-default.png`.

### Mobile (390 wide)

#### m-nav-rail

Mobile nav rail.

Page: home. Selector: `nav at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 160 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Transition | none |
| Icon | 20 x 20, colour oklch(0.552 0.016 285.938) |
| Ancestor paint | 1 up header._mobileBar_1psr6_216 bg oklch(1 0 0) |
| How | at rest |

Crops: `m-nav-rail-default.png`.

#### m-nav-button

Mobile nav button. A rail icon button at 390px.

Page: home. Selector: `nav button at 390`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid oklch(0.871 0.006 286.286) offset 2px | = |
| Font | ABCDiatype 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.552 0.016 285.938) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour oklch(0.552 0.016 285.938) | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._mobileNavButton_1psr6_242 40.0x40.0 r 9999px outline 2px solid oklch(0.871 0.006 286.286) offset 2px | = |

Crops: `m-nav-button-default.png`, `m-nav-button-hover.png`, `m-nav-button-focus-visible.png`, `m-nav-button-pressed.png`.

#### m-signin-btn

Mobile sign-in. The mobile sign-in CTA; measured, never followed.

Page: home. Selector: `sign-in button at 390`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 259.45 x 58 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid oklch(0.95 0.004 286.32) | = | = | = |
| Radius | 9999px | = | = | = |
| Background | oklch(1 0 0) | #f2f2f2 | = | #f2f2f2 |
| Box shadow | #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | ABCDiatype 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.141 0.005 285.823) | oklch(0.21 0.006 285.885) | = | oklch(0.21 0.006 285.885) |
| Transition | all 0.15s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour oklch(0.141 0.005 285.823), fill #000000 | 16 x 16, colour oklch(0.21 0.006 285.885), fill #000000 | = | 16 x 16, colour oklch(0.21 0.006 285.885), fill #000000 |
| Painted layers | button.w-full 259.5x58.0 bg oklch(1 0 0) border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | button.w-full 259.5x58.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px | = | button.w-full 259.5x58.0 bg #f2f2f2 border T:1px solid oklch(0.95 0.004 286.32) / R:1px solid oklch(0.95 0.004 286.32) / B:1px solid oklch(0.95 0.004 286.32) / L:1px solid oklch(0.95 0.004 286.32) r 9999px shadow #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 2) |

Crops: `m-signin-btn-default.png`, `m-signin-btn-hover.png`, `m-signin-btn-focus-visible.png`, `m-signin-btn-pressed.png`.

#### m-heading

Mobile heading.

Page: home. Selector: `painted heading at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 90 |
| Padding | 0px 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABCDiatype 24px/30px 500 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Text node | span: ABCDiatype 24px/30px 500, oklch(0.141 0.005 285.823) |
| Transition | none |
| How | at rest |

Crops: `m-heading-default.png`.

#### m-trend-card

Mobile trend card. A trend card at 390px width.

Page: home. Selector: `div._card_* at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 455.59 |
| Padding | 48px 24px 8px 24px |
| Gap | 48px |
| Border | 1px solid #e8e7e7 |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.02 0px 14px 54px 0px |
| Outline | none |
| Font | ABCDiatype 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.141 0.005 285.823) |
| Text node | h2._headline_hilw7_350: ABCDiatype 20px/27px 500, oklch(0.141 0.005 285.823) |
| Transition | none |
| Painted layers | div._card_hilw7_153 358.0x455.6 bg #ffffff border T:1px solid #e8e7e7 / R:1px solid #e8e7e7 / B:1px solid #e8e7e7 / L:1px solid #e8e7e7 r 24px shadow #000000 @ 0.02 0px 14px 54px 0px; a._thumbnail_hilw7_189 0.0x0.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 8px; a::before._thumbnail_hilw7_189 100%x100% bg #000000 @ 0.05; a._avatarItem_hilw7_400 0.0x0.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 1600px; a._mobileListItem_hilw7_285 308.0x146.0 border T:1px solid oklch(0.95 0.004 286.32) |
| How | at rest |

Crops: `m-trend-card-default.png`.

## Transitions declared in the readable stylesheets

curater.org serves hashed Vite bundles; the /taste route client-side redirects to /taste/soon and Playwright locators never settle on it, so its components are measured through main-world DOM queries — the values above are the computed values the page paints.

- curation: `all var(--transition-fast)`, `opacity var(--transition-fast)`, `transform 0.3s ease-in-out`, `transform var(--transition-fast)`, `box-shadow var(--transition-fast)`, `background-color var(--transition-fast)`, `opacity 0.3s`, `none`, `background-color var(--transition-fast),color var(--transition-fast)`, `border-color var(--transition-fast),padding-bottom var(--transition-slower)`, `font-size var(--transition-slower)`, `color var(--transition-fast)`

- feed: `all var(--transition-fast)`, `opacity var(--transition-fast)`, `transform 0.3s ease-in-out`, `transform var(--transition-fast)`, `box-shadow var(--transition-fast)`, `background-color var(--transition-fast)`, `opacity 0.3s`, `none`, `background-color var(--transition-fast),color var(--transition-fast)`, `border-color var(--transition-fast),padding-bottom var(--transition-slower)`, `font-size var(--transition-slower)`, `color var(--transition-fast)`

- home: `all var(--transition-fast)`, `opacity var(--transition-fast)`, `transform 0.3s ease-in-out`, `transform var(--transition-fast)`, `box-shadow var(--transition-fast)`, `background-color var(--transition-fast)`, `opacity 0.3s`, `none`, `background-color var(--transition-fast),color var(--transition-fast)`, `border-color var(--transition-fast),padding-bottom var(--transition-slower)`, `font-size var(--transition-slower)`, `color var(--transition-fast)`

- profile: `all var(--transition-fast)`, `opacity var(--transition-fast)`, `transform 0.3s ease-in-out`, `transform var(--transition-fast)`, `box-shadow var(--transition-fast)`, `background-color var(--transition-fast)`, `opacity 0.3s`, `none`, `background-color var(--transition-fast),color var(--transition-fast)`, `border-color var(--transition-fast),padding-bottom var(--transition-slower)`, `font-size var(--transition-slower)`, `color var(--transition-fast)`

- taste: `all var(--transition-fast)`, `opacity var(--transition-fast)`, `transform 0.3s ease-in-out`, `transform var(--transition-fast)`, `box-shadow var(--transition-fast)`, `background-color var(--transition-fast)`, `opacity 0.3s`, `none`, `background-color var(--transition-fast),color var(--transition-fast)`, `border-color var(--transition-fast),padding-bottom var(--transition-slower)`, `font-size var(--transition-slower)`, `color var(--transition-fast)`
