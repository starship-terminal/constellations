# Component measurements

Computed styles read from cosmos.so on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across `www.cosmos.so/`, `www.cosmos.so/explore`, `www.cosmos.so/login`, `www.cosmos.so/sequence`, with generic overlay-hiding in place — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky app header (hidden until painted): the flower mark, Explore / Sequence / Shop links, the search pill, Log in and Sign up.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 92 |
| Padding | 24px 32px |
| Gap | 72px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.relative.inline-flex: cosmosOracle 15px/22px 500, #6e6a69, ls -0.28125px |
| Transition | none |
| Icon | 0 x 0, colour #0d0d0d, fill #000000 |
| Painted layers | div.pointer-events-none.absolute 1440.0x168.0 image linear-gradient(#f7f5f3 0%, #f7f5f3 15%, #f7f5f3 @ 0.92 26%, #f7f5f3 @ 0.78 36%, color(srg; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px |
| Ancestor paint | 1 up main.min-h-dvh.bg-paper bg #f7f5f3 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Cosmos flower mark anchor.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Cursor | pointer |
| Painted layers | span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A header nav link (Explore / Sequence / Shop); measured, never followed.

Page: home. Selector: `header a Explore`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 51.7 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 15px/22px 500 | = | = | = |
| Letter spacing | -0.28125px | = | = | = |
| Colour | #6e6a69 | #0d0d0d | = | #0d0d0d |
| Text node | span.relative.inline-flex: cosmosOracle 15px/22px 500, #6e6a69, ls -0.28125px | span.relative.inline-flex: cosmosOracle 15px/22px 500, #0d0d0d, ls -0.28125px | = | span.relative.inline-flex: cosmosOracle 15px/22px 500, #0d0d0d, ls -0.28125px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### signup-cta

Sign-up pill. The black "Sign up" header pill; measured, never followed.

Page: home. Selector: `header Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.84 x 48 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #0d0d0d | #232323 | = | #232323 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 15px/22px 500 | = | = | = |
| Letter spacing | -0.28125px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.inline-flex 100.8x48.0 bg #0d0d0d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.relative.inline-flex 100.8x48.0 bg #232323 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | = | a.relative.inline-flex 100.8x48.0 bg #232323 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-cta-default.png`, `signup-cta-hover.png`, `signup-cta-focus-visible.png`, `signup-cta-pressed.png`.

#### login-link

Log-in pill. The light "Log in" header pill; measured, never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 89.92 x 48 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 15px/22px 500 | = | = | = |
| Letter spacing | -0.28125px | = | = | = |
| Colour | #6e6a69 | #0d0d0d | = | #0d0d0d |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.inline-flex 89.9x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

### Home

#### hero-h1

Hero headline. The 72px display ("Find your next go-to outfit" — the object word rotates through saved categories).

Page: home. Selector: `h1.text-display`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 160 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 72px/72px 700 |
| Letter spacing | -2.88px |
| Colour | #0d0d0d |
| Text node | span.block.whitespace-nowrap: cosmosOracle 72px/72px 700, #0d0d0d, ls -2.88px |
| Transition | none |
| Painted layers | span.block.size-9 70.3x70.3 bg #f2f1f0 border T:1px solid #f7f5f3 / R:1px solid #f7f5f3 / B:1px solid #f7f5f3 / L:1px solid #f7f5f3 r 16px; span.block.size-9 70.3x70.3 bg #f2f1f0 border T:1px solid #f7f5f3 / R:1px solid #f7f5f3 / B:1px solid #f7f5f3 / L:1px solid #f7f5f3 r 16px |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-search

Hero search. The hero search pill ("Search for outfits"); measured, never used — it would open the search surface.

Page: home. Selector: `hero search pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204.77 x 58 | = | = | = |
| Padding | 4px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Painted layers | div.pointer-events-auto.flex 204.8x58.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px; a.relative.inline-flex 89.9x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px; a.relative.inline-flex 100.8x48.0 bg #0d0d0d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | div.pointer-events-auto.flex 204.8x58.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px; a.relative.inline-flex 89.9x48.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px; a.relative.inline-flex 100.8x48.0 bg #232323 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-search-default.png`, `hero-search-hover.png`, `hero-search-focus-visible.png`, `hero-search-pressed.png`.

#### join-cta

Join CTA. The black "Join Cosmos for free" pill; measured, never followed.

Page: home. Selector: `Join Cosmos for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200.83 x 56 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #0d0d0d | #232323 | = | #232323 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 700 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.cursor-pointer 200.8x56.0 bg #0d0d0d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | a.relative.cursor-pointer 200.8x56.0 bg #232323 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | = | a.relative.cursor-pointer 200.8x56.0 bg #232323 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `join-cta-default.png`, `join-cta-hover.png`, `join-cta-focus-visible.png`, `join-cta-pressed.png`.

#### qr-card

Get-the-app card. The "Get the app" QR card fixed bottom-right.

Page: home. Selector: `Get the app card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 208.78 x 242 |
| Padding | 12px 4px 0px 4px |
| Border | 1px solid oklch(0.1591 0.00000406586 none / 0.12) |
| Radius | 25% |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 2px 12px 0px, #000000 @ 0.1 0px 4px 16px 0px |
| Outline | none |
| Font | cosmosOracle 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.text-pretty.font-medium: cosmosOracle 16px/22.4px 500, #0d0d0d, ls -2% |
| Transition | scale 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 20 x 20, colour #0d0d0d |
| Painted layers | div.force-light.pointer-events-auto 208.8x242.0 bg #ffffff border T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklch(0.1591 0.00000406586 none / 0.12) / L:1px solid oklch(0.1591 0.00000406586 none / 0.12) r 25% shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 2px 12px 0px, #000000 @ 0.1 0px 4px 16px 0px |
| How | at rest |

Crops: `qr-card-default.png`.

### Explore and search

#### search-pill

Search field. The header search field (a suggested query in the placeholder); focused, never searched.

Page: explore. Selector: `header search input`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 456 x 56 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 8px 0px | = | - | = |
| Outline | none | = | - | = |
| Font | cosmosOracle 16px/24px 500 | = | - | = |
| Letter spacing | -0.32px | = | - | = |
| Colour | #0d0d0d | = | - | = |
| Text node | span: cosmosOracle 14px/19.6px 400, #9a9796, ls -2% | span: cosmosOracle 14px/19.6px 400, #6e6a69, ls -2% | - | = |
| Transition | width 0.5s cubic-bezier(0.22, 1, 0.36, 1) | = | - | = |
| Icon | 20 x 20, colour #9a9796 | = | - | = |
| Painted layers | div.pointer-events-auto.flex 456.0x56.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 8px 0px; div.relative.-mr-[0.5px] 456.5x56.0 bg #fcfbfa border T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklch(0.1591 0.00000406586 none / 0.12) / L:1px solid oklch(0.1591 0.00000406586 none / 0.12) r 3.35544e+07px shadow #ffffff @ 0.7 0px 1px 1.5px 0px inset, #000000 @ 0.03 0px -1px 1.5px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.truncate.Yd-VhW_searchPlaceholder 165.3x19.6 image linear-gradient(90deg, #000000 @ 0 calc(50% - 54px), #0d0d0d, #000000 @ 0 calc(50% + 54px) | div.pointer-events-auto.flex 456.0x56.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 8px 0px; div.relative.-mr-[0.5px] 456.5x56.0 bg #f9f8f8 border T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklch(0.1591 0.00000406586 none / 0.12) / L:1px solid oklch(0.1591 0.00000406586 none / 0.12) r 3.35544e+07px shadow #ffffff @ 0.7 0px 1px 1.5px 0px inset, #000000 @ 0.03 0px -1px 1.5px 0px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.truncate.Yd-VhW_searchPlaceholder 165.3x19.6 image linear-gradient(90deg, #000000 @ 0 calc(50% - 54px), #0d0d0d, #000000 @ 0 calc(50% + 54px) | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `search-pill-default.png`, `search-pill-hover.png`, `search-pill-pressed.png`.

#### cat-tab

Category tab. A category chip in the explore rail (Fashion/Interiors/...); measured, never followed.

Page: explore. Selector: `category chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.73 x 40.02 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 14px/20.02px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #9a9796 | #0d0d0d | = | #0d0d0d |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cat-tab-default.png`, `cat-tab-hover.png`, `cat-tab-focus-visible.png`, `cat-tab-pressed.png`.

#### section-h2

Section heading. A section heading on /explore ("Selected by Cosmos" / "Explore elements").

Page: explore. Selector: `explore section heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 20px/23px 400 |
| Letter spacing | -2% |
| Colour | #0d0d0d |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### selected-card

Selected card. A "Selected by Cosmos" carousel card (artwork, title, @handle and element count); measured, never followed.

Page: explore. Selector: `selected carousel card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 365 x 200.98 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px normal | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | div.text-balance.font-extrabold: cosmosOracle 32px/48px 800, #ffffff, ls -1.6px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.relative.flex 365.0x151.0 bg #f2f1f0 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.02 0px 2px 12px 0px, #000000 @ 0.1 0px 4px 16px 0px; div.absolute.inset-0 365.0x151.0 bg #000000 @ 0.35 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `selected-card-default.png`, `selected-card-hover.png`, `selected-card-focus-visible.png`, `selected-card-pressed.png`.

#### element-tile

Element tile. A masonry tile in the Explore elements grid (rounded-element corners over the image); measured, never followed — opening it goes to the element.

Page: explore. Selector: `.rounded-element tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1376 x 3500 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | #f7f5f3 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | button.cursor-pointer.rounded-[1.25rem]: cosmosOracle 12px/18px 500, #ffffff, ls -0.24px | = | = | = |
| Transition | none | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | div.relative.max-h-[calc(3400px+100vh)] 1376.0x3500.0 bg #f7f5f3 r 3px; div.relative.block 249.6x284.4 border T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklch(0.1591 0.00000406586 none / 0.12) / L:1px solid oklch(0.1591 0.00000406586 none / 0.12) r 3px; div.absolute.inset-0 247.6x282.4 bg oklch(0.1591 0.00000406586 none / 0.4); button.relative.inline-flex 65.3x34.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px; div.relative.block 249.6x283.3 border T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklch(0.1591 0.00000406586 none / 0.12) / L:1px solid oklch(0.1591 0.00000406586 none / 0.12) r 3px; div.absolute.inset-0 247.6x281.3 bg oklch(0.1591 0.00000406586 none / 0.4) | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `element-tile-focus-visible.png`, `element-tile-pressed.png`.

### Sequence

#### seq-h1

Sequence title. The "Sequence" page heading.

Page: sequence. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 451.19 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 88px/132px 700 |
| Letter spacing | -4.4px |
| Colour | #0d0d0d |
| Transition | none |
| How | at rest |

Crops: none.

#### seq-card

Sequence card. An article card in the Sequence editorial list; measured, never followed.

Page: sequence. Selector: `main a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px; span._O9AMq_dot 6.5x6.5 bg #0d0d0d r 999px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Login

#### auth-card

Auth panel. The "Welcome back" sign-in panel (username/email + password fields, the disabled-then-enabled Next, Forgot password, the sign up link) over the image collage; captured, never used.

Page: login. Selector: `auth panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 344 x 289.02 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.text-balance.font-medium: cosmosOracle 20px/23px 500, #000000, ls -2% |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | label.group.flex 344.0x52.0 border T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklch(0.1591 0.00000406586 none / 0.12) / L:1px solid oklch(0.1591 0.00000406586 none / 0.12) r 16px; label.group.flex 344.0x52.0 border T:1px solid oklch(0.1591 0.00000406586 none / 0.12) / R:1px solid oklch(0.1591 0.00000406586 none / 0.12) / B:1px solid oklch(0.1591 0.00000406586 none / 0.12) / L:1px solid oklch(0.1591 0.00000406586 none / 0.12) r 16px; button.relative.inline-flex 344.0x56.0 bg #f2f1f0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px |
| How | at rest |

Crops: none.

#### auth-input

Username field. The "Username or email" input; focused and given sample text that was deleted again — nothing sent.

Page: login. Selector: `Username or email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 310 x 18 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | cosmosOracle 15px/22px 400 | = | = |
| Letter spacing | -0.28125px | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #9a9796, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: none.

#### auth-pass

Password field. The Password input (with the reveal-eye button); focused and given sample text that was deleted again — nothing sent.

Page: login. Selector: `input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 310 x 18 | = | = |
| Padding | 0px 32px 0px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | cosmosOracle 15px/22px 400 | = | = |
| Letter spacing | -0.28125px | = | = |
| Colour | #0d0d0d | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #9a9796, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: none.

#### auth-next

Next button. The "Next" submit — greyed and disabled until both fields hold text (the enabled state is measured with the fields filled); never pressed.

Page: login. Selector: `Next button`. States: default, enabled, focus-visible, pressed.

| Property | default | enabled | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344 x 56 | = | - | = |
| Padding | 16px 24px | = | - | = |
| Gap | normal 4px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | #f2f1f0 | #0d0d0d | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | cosmosOracle 14px/21px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #9a9796 | #ffffff | - | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | default | pointer | - | = |
| Painted layers | button.relative.inline-flex 344.0x56.0 bg #f2f1f0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | button.relative.inline-flex 344.0x56.0 bg #0d0d0d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | - | = |
| How | at rest | both fields typed (name@example.com, sample-pass), never submitted | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: none.

#### forgot-link

Forgot-password link. The "Forgot password?" link; measured, never followed.

Page: login. Selector: `Forgot password`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.45 x 20.02 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 14px/20.02px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #adadad | #0d0d0d | = | #0d0d0d |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### auth-signup

Sign-up link. The "sign up" link on the auth panel; measured, never followed.

Page: login. Selector: `sign up link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 45.23 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 14px/22px 400 | = | = | = |
| Letter spacing | -2% | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Footer

#### footer

Footer. The footer (force-light): Discover links, the app badges, Follow-us socials and the Info legal row.

Page: explore. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 276 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | a.text-tertiary.transition-colors: cosmosOracle 16px/24px 500, #9a9796, ls -0.32px |
| Transition | none |
| Icon | 1257.86 x 212, colour #0d0d0d |
| Painted layers | span._O9AMq_dot 13.0x13.0 bg #0d0d0d r 999px; span._O9AMq_dot 13.0x13.0 bg #0d0d0d r 999px; span._O9AMq_dot 13.0x13.0 bg #0d0d0d r 999px; span._O9AMq_dot 13.0x13.0 bg #0d0d0d r 999px; span._O9AMq_dot 13.0x13.0 bg #0d0d0d r 999px; span._O9AMq_dot 13.0x13.0 bg #0d0d0d r 999px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link (Download app / Careers / Terms); measured, never followed.

Page: explore. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.56 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #9a9796 | #0d0d0d | = | #0d0d0d |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer (Instagram/TikTok/X).

Page: explore. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.56 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #9a9796 | #0d0d0d | = | #0d0d0d |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 68 |
| Padding | 12px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none |
| Icon | 100 x 16.84, colour #0d0d0d |
| Painted layers | div.pointer-events-none.absolute 390.0x112.0 image linear-gradient(#f7f5f3 0%, #f7f5f3 15%, #f7f5f3 @ 0.92 26%, #f7f5f3 @ 0.78 36%, color(srg; a.relative.inline-flex 97.8x34.0 bg #0d0d0d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px; span.absolute.block 14.0x1.5 bg #9a9796; span.absolute.block 14.0x1.5 bg #9a9796 |
| Ancestor paint | 1 up main.min-h-dvh.bg-paper bg #f7f5f3 |
| How | at rest |

Crops: none.

#### m-menu-button

Menu button. The header menu button (xl:hidden) that opens the full overlay.

Page: home. Selector: `header menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | background-color, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.absolute.block 14.0x1.5 bg #9a9796; span.absolute.block 14.0x1.5 bg #9a9796 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### m-menu-open

Mobile menu, open. The opened nav overlay: the Home / Explore / Sequence / Careers rows over the page with the Sign up pill at the foot.

Page: home. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.1591 0.00000406586 none / 0.12) 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 8px 0px |
| Outline | none |
| Font | cosmosOracle 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | span.text-balance.font-medium: cosmosOracle 32px/35.2px 500, #0d0d0d, ls -3% |
| Transition | transform, translate, scale, rotate 0.3s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 100 x 16.84, colour #0d0d0d |
| Painted layers | div.z-modal.fixed 390.0x844.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.1591 0.00000406586 none / 0.12) 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 8px 0px; span.absolute.block 11.0x11.0 bg #9a9796; span.absolute.block 11.0x11.0 bg #9a9796; a.border-primary.border-b 358.0x69.0 border B:1px solid oklch(0.1591 0.00000406586 none / 0.12); a.border-primary.border-b 358.0x69.0 border B:1px solid oklch(0.1591 0.00000406586 none / 0.12); a.border-primary.border-b 358.0x69.0 border B:1px solid oklch(0.1591 0.00000406586 none / 0.12) |
| How | at rest |

Crops: none.

#### m-nav-item

Mobile menu row. A row inside the opened nav overlay.

Page: home. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 69 | = | = | = |
| Padding | 16px 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid oklch(0.1591 0.00000406586 none / 0.12); L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | #f2f1f0 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Text node | span.text-balance.font-medium: cosmosOracle 32px/35.2px 500, #0d0d0d, ls -3% | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.border-primary.border-b 358.0x69.0 border B:1px solid oklch(0.1591 0.00000406586 none / 0.12) | = | a.border-primary.border-b 358.0x69.0 bg #f2f1f0 border B:1px solid oklch(0.1591 0.00000406586 none / 0.12) | = |
| Ancestor paint | 2 up div.z-modal.fixed bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.1591 0.00000406586 none / 0.12) 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### m-signup

Mobile sign-up. The Sign up pill inside the mobile menu; measured, never followed.

Page: home. Selector: `mobile menu Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 56 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #0d0d0d | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | cosmosOracle 16px/24px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.inline-flex 358.0x56.0 bg #0d0d0d border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px | = | = | = |
| Ancestor paint | 2 up div.z-modal.fixed bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.1591 0.00000406586 none / 0.12) 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### m-hero

Mobile headline.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 104 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | cosmosOracle 32px/32px 700 |
| Letter spacing | -1.28px |
| Colour | #0d0d0d |
| Text node | span.block.whitespace-nowrap: cosmosOracle 32px/32px 700, #0d0d0d, ls -1.28px |
| Transition | none |
| Painted layers | span.block.size-9 39.6x39.6 bg #f2f1f0 border T:1px solid #f7f5f3 / R:1px solid #f7f5f3 / B:1px solid #f7f5f3 / L:1px solid #f7f5f3 r 12px; span.block.size-9 39.6x39.6 bg #f2f1f0 border T:1px solid #f7f5f3 / R:1px solid #f7f5f3 / B:1px solid #f7f5f3 / L:1px solid #f7f5f3 r 12px |
| How | at rest |

Crops: none.

## Transitions declared in the readable stylesheets

The transition rules each page exposes in its readable stylesheets, by page; the per-state Transition rows above are the computed values the page paints.

- explore: `transform 0.25s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.25s, height 0.15s`, `transform 0.72s cubic-bezier(0.32, 0.72, 0, 1)`, `color 0.15s`, `background 0.2s`, `background 0.15s`, `color 0.15s, border-color 0.15s`, `background 0.15s, color 0.15s`, `transform 0.15s`, `opacity 0.15s`, `color 0.15s, background 0.15s`, `transform 0.18s`, `top 0.12s`

- home: `transform 0.25s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.25s, height 0.15s`, `transform 0.72s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 0.2s`, `color 0.15s`, `background 0.2s`, `background 0.15s`, `color 0.15s, border-color 0.15s`, `background 0.15s, color 0.15s`, `transform 0.15s`, `opacity 0.15s`, `color 0.15s, background 0.15s`, `transform 0.18s`

- login: `transform 0.25s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.25s, height 0.15s`, `transform 0.72s cubic-bezier(0.32, 0.72, 0, 1)`, `color 0.15s`, `background 0.2s`, `background 0.15s`, `color 0.15s, border-color 0.15s`, `background 0.15s, color 0.15s`, `transform 0.15s`, `opacity 0.15s`, `color 0.15s, background 0.15s`, `transform 0.18s`, `top 0.12s`
