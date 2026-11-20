# Component measurements

Computed styles read from refero.design and styles.refero.design on 2026-11-02 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `video` is a 3-second hover so the card’s scroll-preview loads; `selected` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Home and research

#### research-box

Research box. The centred search card refero.design opens every page with: a prompt field with a Search by Image upload affordance, mode chips (Research mode, Web apps, iOS apps) and a submit.

Page: home. Selector: `the centred card holding the prompt field, upload and mode chips`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 752 x 102 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #f7f8fb |
| Box shadow | #0c297e @ 0.07 0px 0px 0px 1px inset |
| Outline | none |
| Font | Base-Variable 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | div: Base-Variable 14px/20px 600, #13151b, ls -0.28px |
| Transition | none |
| Icon | 20 x 20, colour #13151b |
| Painted layers | form 752.0x102.0 bg #f7f8fb r 24px shadow #0c297e @ 0.07 0px 0px 0px 1px inset; label 36.0x36.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px; div 154.0x36.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px; div 119.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div 113.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div 0.0x0.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px |
| How | at rest |

Crops: `research-box-default.png`.

#### research-input

Research prompt field.

Page: home. Selector: `the centred card holding the prompt field, upload and mode chips textarea`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 720 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Base-Variable 16px/24px 500 | = |
| Letter spacing | -0.32px | = |
| Colour | #13151b | = |
| Transition | padding-bottom, padding-left, border-width 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #011158 @ 0.24, opacity 1 | = |
| Ancestor paint | 2 up form bg #f7f8fb shadow #0c297e @ 0.07 0px 0px 0px 1px inset | = |
| How | at rest | Shift+Tab, Tab |

Crops: none.

#### research-box-state

Research box, field active. The same card with the prompt clicked into and sample text typed, then deleted; nothing was submitted.

Page: home. Selector: `the centred card holding the prompt field, upload and mode chips`. States: focused, filled.

| Property | focused | filled |
|---|---|---|
| Size (w x h) | 752 x 102 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | #f7f8fb | = |
| Box shadow | #0c297e @ 0.07 0px 0px 0px 1px inset | = |
| Outline | none | = |
| Font | Base-Variable 16px/24px 500 | = |
| Letter spacing | -0.32px | = |
| Colour | #000000 | = |
| Text node | div: Base-Variable 14px/20px 600, #13151b, ls -0.28px | textarea: Base-Variable 16px/24px 500, #13151b, ls -0.32px |
| Transition | none | = |
| Icon | 20 x 20, colour #13151b | = |
| Painted layers | form 752.0x102.0 bg #f7f8fb r 24px shadow #0c297e @ 0.07 0px 0px 0px 1px inset; label 36.0x36.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px; div 154.0x36.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px; div 119.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div 113.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div 0.0x0.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px | = |
| How | clicked into the field | typed "a calm banking app dashboard", then deleted; nothing sent |

Crops: `research-box-state-focused.png`, `research-box-state-filled.png`.

#### research-chip

Mode chip. One of the research-box scope chips (Research mode / Web apps / iOS apps). Pressed states are forced, not clicked: a real press switches the corpus.

Page: home. Selector: `a mode chip in the research box`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119 x 36 | = | = | = |
| Padding | 0px 16px 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 18px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #011158 @ 0.24 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Base-Variable 14px/20px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #030e31 @ 0.54 | #13151b | = | #13151b |
| Text node | div: Base-Variable 14px/20px 500, #030e31 @ 0.54, ls -0.28px | div: Base-Variable 14px/20px 500, #13151b, ls -0.28px | = | div: Base-Variable 14px/20px 500, #13151b, ls -0.28px |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #030e31 @ 0.54 | 20 x 20, colour #13151b | = | 20 x 20, colour #13151b |
| Painted layers | div 119.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px | = | div 119.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px shadow #011158 @ 0.24 0px 0px 0px 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `research-chip-default.png`, `research-chip-hover.png`, `research-chip-focus-visible.png`, `research-chip-pressed.png`.

#### hero-title

Hero title. "Design Research for the AI Era" — the display line the home page opens with.

Page: home. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1074 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Title 50px/60px 400 |
| Letter spacing | -1px |
| Colour | #000000 |
| Text node | span: Title 50px/60px 400, #000000 @ 0, ls -1px |
| Transition | none |
| Painted layers | span 639.2x76.0 image linear-gradient(110deg, #ffffff @ 0 5.33%, #ffffff @ 0 32.81%, #00aaff 41.22%, #e1e1fe 45.; span 1074.0x64.0 image linear-gradient(-70deg, #ffffff @ 0 5.33%, #ffffff @ 0 32.81%, #00aaff 41.22%, #e1e1fe 45. |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subline.

Page: home. Selector: `the paragraph under main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 424 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Base-Variable 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #030e31 @ 0.54 |
| Transition | none |
| How | at rest |

Crops: none.

#### section-title

Section title. A home section head (Page Types, Flows, UX Patterns, UI Elements, Sites).

Page: home. Selector: `h2 "Page Types"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 151.75 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Base-Variable 32px/40px 500 |
| Letter spacing | -0.88px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### result-card

Result card. A gallery card on the home page: a screenshot tile in a rounded padded card with a title under it. Measured, never followed.

Page: home. Selector: `first card under the Page Types section`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 369.98 x 228.52 | = | = | = |
| Padding | 0px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Base-Variable 16px/24px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div: Base-Variable 16px/24px 500, #000000, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Icon | 24 x 24, colour #021249 @ 0.38 | = | = | = |
| Painted layers | div.Y_CTf 334.0x184.5 bg #eef0f6 r 8px; div 32.0x32.0 bg #2d313f @ 0.2 r 50% shadow #f7f8fb 0px 0px 0px 2px inset, #2d313f @ 0.2 0px 0px 0px 2px; div 24.0x24.0 bg #eef0f6 @ 0.78 r 6px; div 88.0x32.0 image linear-gradient(to right, #ffffff @ 0 0px, #ffffff 15%) | div.Y_CTf 334.0x184.5 bg #eef0f6 r 8px shadow #07191f @ 0.1 0px 10px 20px 0px; div 32.0x32.0 bg #2d313f @ 0.2 r 50% shadow #f7f8fb 0px 0px 0px 2px inset, #2d313f @ 0.2 0px 0px 0px 2px; div 88.0x32.0 image linear-gradient(to right, #ffffff @ 0 0px, #ffffff 15%) | div.Y_CTf 334.0x184.5 bg #eef0f6 r 8px shadow #07191f @ 0.1 0px 10px 20px 0px; div 32.0x32.0 bg #2d313f @ 0.2 r 50% shadow #f7f8fb 0px 0px 0px 2px inset, #2d313f @ 0.2 0px 0px 0px 2px; div 88.0x32.0 image linear-gradient(to right, #ffffff @ 0 0px, #ffffff 15%) | div.Y_CTf 334.0x184.5 bg #eef0f6 r 8px; div 32.0x32.0 bg #2d313f @ 0.2 r 50% shadow #f7f8fb 0px 0px 0px 2px inset, #2d313f @ 0.2 0px 0px 0px 2px; div 88.0x32.0 image linear-gradient(to right, #ffffff @ 0 0px, #ffffff 15%) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `result-card-default.png`, `result-card-hover.png`, `result-card-focus-visible.png`, `result-card-pressed.png`.

#### result-card-title

Result card label.

Page: home. Selector: `text under the card tile`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 72.23 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Base-Variable 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Transition | all 0.2s ease |
| Cursor | pointer |
| How | at rest |

Crops: none.

### Search and galleries

#### search-box

Search box (results page). The same research card pinned above the results on /search.

Page: search. Selector: `research card on /search`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 1170 x 128 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Base-Variable 16px/24px 500 | = |
| Letter spacing | -0.32px | = |
| Colour | #000000 | = |
| Text node | span: Base-Variable 20px/24px 500, #777d90, ls -0.45px | div: Base-Variable 20px/28px 500, #000000, ls -0.45px |
| Transition | none | = |
| Icon | 24 x 24, colour #030e31 @ 0.54 | 24 x 24, colour #000000 |
| Painted layers | div 16.0x16.0 bg #eef0f6 r 50%; div 36.0x36.0 bg #f7f8fb r 50% shadow #0c297e @ 0.07 0px 8px 16px 0px; div 1074.0x64.0 bg #f7f8fb border T:1px solid #0c297e @ 0.07 / R:1px solid #0c297e @ 0.07 / B:1px solid #0c297e @ 0.07 / L:1px solid #0c297e @ 0.07 r 24px; div 0.0x0.0 bg #ffffff r 16px shadow #07191f @ 0.1 0px 0px 2px 0px, #07191f @ 0.1 0px 0px 2px 0px; div.O_M3g.ZF_q4 0.0x0.0 border T:1px solid #0c1a69 @ 0.14 / R:1px solid #0c1a69 @ 0.14 / B:1px solid #0c1a69 @ 0.14 / L:1px solid #0c1a69 @ 0.14 r 8px; div 172.0x40.0 bg #ffffff border T:1px solid #0c297e @ 0.07 / R:1px solid #0c297e @ 0.07 / B:1px solid #0c297e @ 0.07 / L:1px solid #0c297e @ 0.07 r 20px | div 1440.0x900.0 bg #0c297e @ 0.07; div 1090.0x824.0 bg #f7f8fb r 30px; li 230.0x64.0 bg #37509b @ 0.04 r 16px shadow #37509b @ 0.04 0px 0px 0px 1px inset; div 30.5x17.0 bg #1eb45d @ 0.08 r 2px; a 230.0x80.0 bg #37509b @ 0.04 r 16px; div 1090.0x37.0 border T:1px solid #0c297e @ 0.07 |
| Ancestor paint | 1 up div bg #ffffff | = |
| How | at rest | clicked into the field |

Crops: `search-box-default.png`, `search-box-focused.png`.

#### search-tile

Search result tile. A result card in the /search grid: a padded tile with a screen image and a favicon-and-name label. Hovered only.

Page: search. Selector: `first result tile in the grid`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 347.33 x 235.91 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Base-Variable 16px/24px 500 | = |
| Letter spacing | -0.32px | = |
| Colour | #000000 | = |
| Text node | div: Base-Variable 16px/24px 500, #000000, ls -0.32px | = |
| Transition | none | = |
| Icon | 24 x 24, colour #021249 @ 0.38 | = |
| Painted layers | div.Y_CTf 347.3x191.9 bg #eef0f6 r 8px; div 32.0x32.0 bg #2d313f @ 0.2 r 50% shadow #f7f8fb 0px 0px 0px 2px inset, #2d313f @ 0.2 0px 0px 0px 2px; div 88.0x32.0 image linear-gradient(to right, #ffffff @ 0 0px, #ffffff 15%) | = |
| How | at rest | mouse hover |

Crops: `search-tile-default.png`, `search-tile-hover.png`.

#### ios-tile

iOS app tile. A phone-shaped app card in the iOS gallery: a tall rounded screenshot tile. Hovered only.

Page: apps. Selector: `first app card in the iOS grid`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 256.5 x 599.05 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Base-Variable 16px/24px 500 | = |
| Letter spacing | -0.32px | = |
| Colour | #000000 | = |
| Text node | div: Base-Variable 16px/24px 500, #000000, ls -0.32px | = |
| Transition | none | = |
| Icon | 24 x 24, colour #021249 @ 0.38 | = |
| Painted layers | div.Y_CTf 256.5x555.0 bg #eef0f6 r 19% / 9.2%; div 32.0x32.0 bg #2d313f @ 0.2 r 50% shadow #f7f8fb 0px 0px 0px 2px inset, #2d313f @ 0.2 0px 0px 0px 2px; div 88.0x32.0 image linear-gradient(to right, #ffffff @ 0 0px, #ffffff 15%) | div.Y_CTf 256.5x555.0 bg #eef0f6 r 19% / 9.2% shadow #07191f @ 0.1 0px 10px 20px 0px; div 32.0x32.0 bg #2d313f @ 0.2 r 50% shadow #f7f8fb 0px 0px 0px 2px inset, #2d313f @ 0.2 0px 0px 0px 2px; div 88.0x32.0 image linear-gradient(to right, #ffffff @ 0 0px, #ffffff 15%) |
| How | at rest | mouse hover |

Crops: `ios-tile-default.png`, `ios-tile-hover.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1 "Pricing"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 730 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Title 50px/60px 400 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-card

Plan card. A pricing plan card: name, price, feature list and a call-to-action button.

Page: pricing. Selector: `first pricing plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 349.19 x 413 |
| Padding | 30px |
| Border | none |
| Radius | 16px 16px 0px 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Base-Variable 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | div: Base-Variable 16px/24px 500, #777d90, ls -0.32px |
| Transition | none |
| Icon | 46 x 18, colour #000000 |
| ::before | 349.188px x 413px, absolute, bg #f7f8fb, radius 0px |
| Painted layers | div::before 349.188pxx413px bg #f7f8fb; div 289.2x56.0 image conic-gradient(from 180deg, #ff8475 0deg, #ff8475 5.52deg, #ff5c78 34.14deg, #ff87c6 60.76 r 28px; div 289.2x56.0 bg #000000 r 28px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA button. The call-to-action inside a plan card. Pressed state is forced; a real press would start checkout.

Page: pricing. Selector: `button in the plan card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 289.19 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 28px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Base-Variable 16px/24px 600 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #f7f8fb | = | = | = |
| Text node | span: Base-Variable 16px/24px 600, #f7f8fb, ls -0.32px | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div 289.2x56.0 image conic-gradient(from 180deg, #ff8475 0deg, #ff8475 5.52deg, #ff5c78 34.14deg, #ff87c6 60.76 r 28px; div 289.2x56.0 bg #000000 r 28px | div 294.1x59.8 image conic-gradient(from 180deg, #ff8475 0deg, #ff8475 5.52deg, #ff5c78 34.14deg, #ff87c6 60.76 r 28px; div 289.2x56.0 bg #000000 r 28px | button 289.2x56.0 r 28px outline 1px auto #005fcc offset 0px; div 289.2x56.0 image conic-gradient(from 180deg, #ff8475 0deg, #ff8475 5.52deg, #ff5c78 34.14deg, #ff87c6 60.76 r 28px; div 289.2x56.0 bg #000000 r 28px | div 297.3x61.3 image conic-gradient(from 180deg, #ff8475 0deg, #ff8475 5.52deg, #ff5c78 34.14deg, #ff87c6 60.76 r 28px; div 289.2x56.0 bg #000000 r 28px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### discount-card

Student discount card. The info card beside the plans (Student discount / Enterprise / Integrate Refero).

Page: pricing. Selector: `the Student discount card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1167 x 132 |
| Padding | 0px 16px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Base-Variable 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | h2._632i: Base-Variable 16px/24px 600, #000000, ls -0.32px |
| Transition | none |
| Painted layers | div 71.5x40.0 bg #eef0f6 r 12px; div 124.7x40.0 bg #eef0f6 r 12px; div 109.6x40.0 bg #eef0f6 r 12px |
| How | at rest |

Crops: `discount-card-default.png`.

### MCP page

#### mcp-title

MCP title. "Give your AI agent design taste" — the /mcp hero.

Page: mcp. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 860 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Title 50px/60px 400 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `mcp-title-default.png`.

### Promos and overlays

#### mcp-card

Refero MCP promo card. The floating card pinned over the content: "Refero MCP connects your agent to a curated library…" with an Explore MCP button and a Close.

Page: home. Selector: `the fixed MCP promo card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 445 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #07191f @ 0.1 0px 20px 40px 0px, #07191f @ 0.1 0px 10px 30px 0px |
| Outline | none |
| Font | Base-Variable 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | div: Base-Variable 14px/20px 500, #777d90, ls -0.32px |
| Transition | none |
| Painted layers | div 320.0x445.0 bg #ffffff r 16px shadow #07191f @ 0.1 0px 20px 40px 0px, #07191f @ 0.1 0px 10px 30px 0px; div.O_M3g.ZF_q4 87.5x48.0 border T:1px solid #0c1a69 @ 0.14 / R:1px solid #0c1a69 @ 0.14 / B:1px solid #0c1a69 @ 0.14 / L:1px solid #0c1a69 @ 0.14 r 8px; div.O_M3g.ZF_q4 178.5x48.0 bg #000000 r 8px |
| How | at rest |

Crops: `mcp-card-default.png`.

#### mcp-card-cta

Explore MCP button. The dark button in the promo card. Measured and focused, never pressed.

Page: home. Selector: `"Explore MCP" in the promo card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 178.47 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Base-Variable 16px/24px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | div.O_M3g.ZF_q4: Base-Variable 16px/24px 600, #f7f8fb, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.O_M3g.ZF_q4 178.5x48.0 bg #000000 r 8px | div.O_M3g.ZF_q4 178.5x48.0 bg #2d313f r 8px | a 178.5x48.0 outline 1px auto #005fcc offset 1px; div.O_M3g.ZF_q4 178.5x48.0 bg #000000 r 8px | = |
| Ancestor paint | 3 up div bg #ffffff shadow #07191f @ 0.1 0px 20px 40px 0px, #07191f @ 0.1 0px 10px 30px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mcp-card-cta-default.png`, `mcp-card-cta-hover.png`, `mcp-card-cta-focus-visible.png`, `mcp-card-cta-pressed.png`.

#### mcp-card-close

Promo card Close button. Dismisses the card (a styled div, not a button). Measured, never pressed: closing happens after the measurements.

Page: home. Selector: `"Close" in the promo card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.53 x 48 | = | - | = |
| Padding | 0px 16px | = | - | = |
| Border | 1px solid #0c1a69 @ 0.14 | 1px solid #dddfea | - | 1px solid #dddfea |
| Radius | 8px | = | - | = |
| Background | transparent | #dddfea | - | #dddfea |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Base-Variable 16px/24px 600 | = | - | = |
| Letter spacing | -0.32px | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | all 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | div.O_M3g.ZF_q4 87.5x48.0 border T:1px solid #0c1a69 @ 0.14 / R:1px solid #0c1a69 @ 0.14 / B:1px solid #0c1a69 @ 0.14 / L:1px solid #0c1a69 @ 0.14 r 8px | div.O_M3g.ZF_q4 87.5x48.0 bg #dddfea border T:1px solid #dddfea / R:1px solid #dddfea / B:1px solid #dddfea / L:1px solid #dddfea r 8px | - | div.O_M3g.ZF_q4 87.5x48.0 bg #dddfea border T:1px solid #dddfea / R:1px solid #dddfea / B:1px solid #dddfea / L:1px solid #dddfea r 8px |
| Ancestor paint | 3 up div bg #ffffff shadow #07191f @ 0.1 0px 20px 40px 0px, #07191f @ 0.1 0px 10px 30px 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `mcp-card-close-default.png`, `mcp-card-close-hover.png`, `mcp-card-close-pressed.png`.

#### coach-box

Research-mode coach box. The "Meet new research mode" coach a fresh profile shows once over the research input.

Page: home. Selector: `the research-mode coach box`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 752 x 93 |
| Padding | 12px 14px 36px 14px |
| Gap | 9px |
| Border | T: 1px solid #0c297e @ 0.07; R: 1px solid #0c297e @ 0.07; B: none; L: 1px solid #0c297e @ 0.07 |
| Radius | 24px 24px 0px 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Base-Variable 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | div: Base-Variable 16px/24px 600, #000000, ls -0.32px |
| Transition | all 0.4s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Icon | 24 x 24, colour #000000 |
| Painted layers | div 752.0x93.0 bg #ffffff border T:1px solid #0c297e @ 0.07 / R:1px solid #0c297e @ 0.07 / L:1px solid #0c297e @ 0.07 r 24px 24px 0px 0px |
| How | at rest |

Crops: `coach-box-default.png`.

#### coach-close

Coach close X. The dismissal: a bare 24px svg with cursor:pointer, not a button. Measured and hovered, never clicked.

Page: home. Selector: `the X svg in the coach box`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Base-Variable 16px/24px 500 | = |
| Letter spacing | -0.32px | = |
| Colour | #000000 | #030e31 @ 0.54 |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #000000 | 24 x 24, colour #030e31 @ 0.54 |
| Ancestor paint | 1 up div bg #ffffff | = |
| How | at rest | mouse hover |

Crops: `coach-close-default.png`, `coach-close-hover.png`.

### Styles gallery

#### styles-header

Styles header. The sticky translucent bar: logo, section links and the sign-in on styles.refero.design.

Page: styles. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 81 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid oklab(0.909998 -0.00000914931 -0.00797832 / 0.5); L: none |
| Radius | 0px |
| Background | oklab(0.999998 -0.00000980496 0.0000234246 / 0.9) |
| Box shadow | none |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | neueMontreal 16px/24px 530 |
| Letter spacing | -0.32px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Text node | span.w-2.5.shrink-0: neueMontreal 25px/32px 530, lab(4.38504 0.200026 -3.38308), ls -0.625px |
| Transition | none |
| Painted layers | header.sticky.top-0 1440.0x81.0 bg oklab(0.999998 -0.00000980496 0.0000234246 / 0.9) border B:1px solid oklab(0.909998 -0.00000914931 -0.00797832 / 0.5) |
| Ancestor paint | 1 up body.min-h-full.flex bg lab(100 0 0) |
| How | at rest |

Crops: `styles-header-default.png`.

#### styles-hero

Gallery hero. The serif violet display headline and search the index opens with.

Page: styles. Selector: `index hero block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1100 x 495.22 |
| Padding | 79px 24px 32px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neueMontreal 16px/24px 530 |
| Letter spacing | -0.32px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Text node | div.flex.h-5: neueMontreal 12px/16px 500, lab(4.38504 0.200026 -3.38308), ls -0.18px |
| Transition | none |
| Icon | 18 x 18, colour lab(98.84 0.0000298023 -0.0000119209) |
| Painted layers | div.flex.h-5 37.7x20.0 border T:1px solid lab(4.38504 0.200026 -3.38308) / R:1px solid lab(4.38504 0.200026 -3.38308) / B:1px solid lab(4.38504 0.200026 -3.38308) / L:1px solid lab(4.38504 0.200026 -3.38308) r 4px; span.size-1.5.rounded-full 6.0x6.0 bg #10b981 r 3.35544e+07px; span.rotating-headline-module__DCI50q__text.rotating-headline-module__DCI50q__outgoing 960.3x92.0 image linear-gradient(110deg, #000000 @ 0 5.33%, #000000 @ 0 32.81%, #00aaff 41.22%, #e1e1fe 45.; span.rotating-headline-module__DCI50q__text.rotating-headline-module__DCI50q__incoming 782.7x92.0 image linear-gradient(-70deg, #000000 @ 0 5.33%, #000000 @ 0 32.81%, #00aaff 41.22%, #e1e1fe 45.; div.flex.h-14 752.0x64.0 bg oklab(0.977997 -0.00000995398 -0.00397688 / 0.7) border T:1px solid oklab(0.909998 -0.00000914931 -0.00797832 / 0.7) / R:1px solid oklab(0.909998 -0.00000914931 -0.00797832 / 0.7) / B:1px solid oklab(0.909998 -0.00000914931 -0.00797832 / 0.7) / L:1px solid oklab(0.909998 -0.00000914931 -0.00797832 / 0.7) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, lab(89.5164 0.0511706 -3.03215) 0px 0px 0px 0.5px inset; button.inline-flex.size-10 40.0x40.0 bg lab(4.38504 0.200026 -3.38308) r 3.35544e+07px |
| How | at rest |

Crops: `styles-hero-default.png`.

#### styles-hero-title

Gallery headline. The kalice serif display line, set in violet.

Page: styles. Selector: `index h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1052 x 74.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | kalice 64px/69.12px 400 |
| Letter spacing | normal |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Text node | span.rotating-headline-module__DCI50q__text.rotating-headline-module__DCI50q__outgoing: kalice 64px/69.12px 400, #000000 @ 0 |
| Transition | none |
| Painted layers | span.rotating-headline-module__DCI50q__text.rotating-headline-module__DCI50q__outgoing 960.3x92.0 image linear-gradient(110deg, #000000 @ 0 5.33%, #000000 @ 0 32.81%, #00aaff 41.22%, #e1e1fe 45.; span.rotating-headline-module__DCI50q__text.rotating-headline-module__DCI50q__incoming 782.7x92.0 image linear-gradient(-70deg, #000000 @ 0 5.33%, #000000 @ 0 32.81%, #00aaff 41.22%, #e1e1fe 45. |
| How | at rest |

Crops: `styles-hero-title-default.png`.

#### styles-search

Search field. The rounded search pill under the headline. Sample text was typed and deleted.

Page: styles. Selector: `the search input and its pill`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 671 x 46 | = | 631 x 46 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | neueMontreal 16px/24px 530 | = | = |
| Letter spacing | -0.24px | = | = |
| Colour | lab(4.38504 0.200026 -3.38308) | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | oklab(0.549998 -0.00000569224 -0.0119864 / 0.6), opacity 1 | = | = |
| Ancestor paint | 1 up div.flex.h-14 bg oklab(0.977997 -0.00000995398 -0.00397688 / 0.7) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, lab(89.5164 0.0511706 -3.03215) 0px 0px 0px 0.5px inset | 1 up div.flex.h-14 bg lab(97.4265 0.0201464 -1.51933) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, lab(89.5164 0.0511706 -3.03215) 0px 0px 0px 0.5px inset, #37509b @ 0.04 0px 0px 0px 3px | 1 up div.flex.h-14 bg lab(97.4265 0.0201464 -1.51933) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, lab(89.5164 0.0511706 -3.03215) 0px 0px 0px 0.5px inset, #37509b @ 0.04 0px 0px 0px 3px |
| How | at rest | clicked into the field | typed "linear", then deleted; nothing sent |

Crops: `styles-search-default.png`, `styles-search-focused.png`, `styles-search-filled.png`.

#### styles-card

Style card. A gallery card: a padded rounded tile holding the site screenshot, a footer with the site’s favicon, name and tagline.

Page: styles. Selector: `a[href^="/style/"]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 394.66 x 338.66 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 32px | = |
| Background | transparent | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklab(0.549998 -0.00000569224 -0.0119864 / 0.5) 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | neueMontreal 16px/24px 530 | = |
| Letter spacing | -0.32px | = |
| Colour | lab(4.38504 0.200026 -3.38308) | = |
| Text node | h3.text-xl.font-semibold: neueMontreal 20px/28px 600, lab(4.38504 0.200026 -3.38308), ls -0.5px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.bg-secondary.overflow-hidden 394.7x282.7 bg lab(97.4265 0.0201464 -1.51933) r 32px; div.relative.w-full 298.7x186.7 border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 8px; div.relative.h-full 296.7x184.7 bg lab(100 0 0) | a.rounded-4xl 394.7x338.7 r 32px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklab(0.549998 -0.00000569224 -0.0119864 / 0.5) 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; div.bg-secondary.overflow-hidden 394.7x282.7 bg lab(97.4265 0.0201464 -1.51933) r 32px; div.relative.w-full 298.7x186.7 border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 8px; div.relative.h-full 296.7x184.7 bg lab(100 0 0) |
| How | at rest | Shift+Tab, Tab |

Crops: `styles-card-default.png`, `styles-card-focus-visible.png`.

#### styles-card-video

Style card, video playing. On hover the tile’s screenshot gives way to a scroll-through video of the site, streamed from images.refero.design.

Page: styles. Selector: `a[href^="/style/"] on hover`. States: video.

| Property | video |
|---|---|
| Size (w x h) | 394.66 x 338.66 |
| Padding | 0px |
| Border | none |
| Radius | 32px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neueMontreal 16px/24px 530 |
| Letter spacing | -0.32px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Text node | h3.text-xl.font-semibold: neueMontreal 20px/28px 600, lab(4.38504 0.200026 -3.38308), ls -0.5px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.bg-secondary.overflow-hidden 394.7x282.7 bg lab(94.1676 0.0340343 -2.27666) r 32px; div.relative.w-full 304.6x190.4 border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 8px; div.relative.h-full 302.6x188.3 bg lab(100 0 0) |
| How | mouse hover, 3s, so the scroll-preview video loads |

Crops: `styles-card-video-video.png`.

#### styles-card-favicon

Card footer favicon. The site’s favicon in the card footer, ~32px in a small rounded tile.

Page: styles. Selector: `favicon img in the card footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neueMontreal 16px/24px 530 |
| Letter spacing | -0.32px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `styles-card-favicon-default.png`.

#### styles-chip

Filter chip. A prompt/filter chip under the search. Pressed state is forced, not clicked: a real press applies the filter.

Page: styles. Selector: `a chip under the search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 182 x 36 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | oklab(0.977997 -0.00000995397 -0.00397688 / 0.6) | = | oklab(0.977997 -0.00000995397 -0.00397688 / 0.6) |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto oklab(0.549998 -0.00000569224 -0.0119864 / 0.5) offset 0px | = |
| Font | neueMontreal 13px/24px 500 | = | = | = |
| Letter spacing | 0.13px | = | = | = |
| Colour | lab(47.7319 0.122339 -4.52256) | lab(4.38504 0.200026 -3.38308) | = | lab(4.38504 0.200026 -3.38308) |
| Text node | span.max-w-full.truncate: neueMontreal 13px/24px 500, lab(47.7319 0.122339 -4.52256), ls 0.13px | span.max-w-full.truncate: neueMontreal 13px/24px 500, lab(4.38504 0.200026 -3.38308), ls 0.13px | = | span.max-w-full.truncate: neueMontreal 13px/24px 500, lab(4.38504 0.200026 -3.38308), ls 0.13px |
| Transition | background-color, color, filter, opacity, transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 14 x 14, colour oklab(0.549998 -0.00000569224 -0.0119864 / 0.7) | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.flex.h-9 182.0x36.0 bg oklab(0.977997 -0.00000995397 -0.00397688 / 0.6) r 12px | button.flex.h-9 182.0x36.0 r 12px outline 1px auto oklab(0.549998 -0.00000569224 -0.0119864 / 0.5) offset 0px | button.flex.h-9 182.0x36.0 bg oklab(0.977997 -0.00000995397 -0.00397688 / 0.6) r 12px |

Crops: `styles-chip-default.png`, `styles-chip-hover.png`, `styles-chip-focus-visible.png`, `styles-chip-pressed.png`.

### Style entity page

#### entity-frame

Media frame. The large rounded frame over the page: the site’s scroll video fades in over the poster still, border and shadow around it.

Page: entity. Selector: `the video and its rounded frame`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 630 x 393.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neueMontreal 16px/24px 530 |
| Letter spacing | -0.32px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Transition | opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1) |
| Ancestor paint | 1 up div.relative.h-full bg lab(100 0 0); 3 up div.overflow-hidden.rounded-2xl shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0c297e @ 0.09 0px 8px 20px 0px, #0c297e @ 0.03 0px 0px 0px 0.5px |
| How | at rest |

Crops: `entity-frame-default.png`.

#### entity-title

Style name. The site’s name in the kalice display serif, next to its round favicon.

Page: entity. Selector: `entity h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 361.45 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | kalice 48px/48px 530 |
| Letter spacing | -1.68px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Transition | none |
| How | at rest |

Crops: `entity-title-default.png`.

#### entity-favicon

Style favicon. The site’s favicon in a bordered circle beside the name.

Page: entity. Selector: `favicon beside h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 64 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neueMontreal 16px/24px 530 |
| Letter spacing | -0.32px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Transition | none |
| How | at rest |

Crops: `entity-favicon-default.png`.

#### entity-tab

Doc tab. A tab in the documentation pane (DESIGN.md, Tailwind v4, CSS Variables, Design Tokens). Pressed is forced; a real press switches the document.

Page: entity. Selector: `a tab in the doc pane`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84.41 x 44 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklab(0.549998 -0.00000569224 -0.0119864 / 0.4) 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | neueMontreal 13px/24px 500 | = | = | = |
| Letter spacing | 0.26px | = | = | = |
| Colour | lab(47.7319 0.122339 -4.52256) | lab(4.38504 0.200026 -3.38308) | = | lab(4.38504 0.200026 -3.38308) |
| Transition | color, background-color, border-color, box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| ::after | 64.4062px x 1.5px, absolute, bg lab(4.38504 0.200026 -3.38308), radius 3.35544e+07px | = | = | = |
| Painted layers | button::after.relative.inline-flex 64.4062pxx1.5px bg lab(4.38504 0.200026 -3.38308) r 3.35544e+07px | = | button.relative.inline-flex 84.4x44.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklab(0.549998 -0.00000569224 -0.0119864 / 0.4) 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; button::after.relative.inline-flex 64.4062pxx1.5px bg lab(4.38504 0.200026 -3.38308) r 3.35544e+07px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `entity-tab-default.png`, `entity-tab-hover.png`, `entity-tab-focus-visible.png`, `entity-tab-pressed.png`.

#### entity-tab-active

Doc tab, current. The selected tab (DESIGN.md) is measured at rest: it is the tab the page opens on.

Page: entity. Selector: `the selected doc tab`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 91.39 x 44 | = |
| Padding | 0px 10px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklab(0.549998 -0.00000569224 -0.0119864 / 0.4) 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | neueMontreal 13px/24px 600 | = |
| Letter spacing | 0.26px | = |
| Colour | lab(4.38504 0.200026 -3.38308) | = |
| Transition | color, background-color, border-color, box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) | = |
| Cursor | default | = |
| ::after | 71.3906px x 1.5px, absolute, bg lab(4.38504 0.200026 -3.38308), radius 3.35544e+07px | = |
| Painted layers | button::after.relative.inline-flex 71.3906pxx1.5px bg lab(4.38504 0.200026 -3.38308) r 3.35544e+07px | button.relative.inline-flex 91.4x44.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklab(0.549998 -0.00000569224 -0.0119864 / 0.4) 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; button::after.relative.inline-flex 71.3906pxx1.5px bg lab(4.38504 0.200026 -3.38308) r 3.35544e+07px |
| How | at rest | Shift+Tab, Tab |

Crops: `entity-tab-active-default.png`, `entity-tab-active-focus-visible.png`.

#### entity-copy

Copy button. Copies the open document. Measured, never pressed.

Page: entity. Selector: `"Copy" in the doc pane`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.44 x 28 | = | = | = |
| Padding | 0px 10px 0px 6px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid lab(89.5164 0.0511706 -3.03215) | = | 1px solid lab(47.7319 0.122339 -4.52256) | = |
| Radius | 6px | = | = | = |
| Background | lab(100 0 0) | lab(94.1676 0.0340343 -2.27666) | = | lab(94.1676 0.0340343 -2.27666) |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklab(0.549998 -0.00000569224 -0.0119864 / 0.5) 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | neueMontreal 12.8px/24px 500 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | lab(4.38504 0.200026 -3.38308) | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour lab(4.38504 0.200026 -3.38308) | = | = | = |
| Painted layers | button.group/button.inline-flex 66.4x28.0 bg lab(100 0 0) border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 6px | button.group/button.inline-flex 66.4x28.0 bg lab(94.1676 0.0340343 -2.27666) border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 6px | button.group/button.inline-flex 66.4x28.0 bg lab(100 0 0) border T:1px solid lab(47.7319 0.122339 -4.52256) / R:1px solid lab(47.7319 0.122339 -4.52256) / B:1px solid lab(47.7319 0.122339 -4.52256) / L:1px solid lab(47.7319 0.122339 -4.52256) r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklab(0.549998 -0.00000569224 -0.0119864 / 0.5) 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 66.4x28.0 bg lab(94.1676 0.0340343 -2.27666) border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `entity-copy-default.png`, `entity-copy-hover.png`, `entity-copy-focus-visible.png`, `entity-copy-pressed.png`.

#### entity-similar

Similar style card. A card in the Similar styles row at the foot of the page.

Page: entity. Selector: `a similar-styles card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 308 x 260.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | neueMontreal 16px/24px 530 | = |
| Letter spacing | -0.32px | = |
| Colour | lab(4.38504 0.200026 -3.38308) | = |
| Text node | h3.text-xl.font-semibold: neueMontreal 20px/28px 600, lab(4.38504 0.200026 -3.38308), ls -0.5px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.bg-secondary.overflow-hidden 308.0x204.5 bg lab(97.4265 0.0201464 -1.51933) r 16px; div.relative.w-full 276.0x172.5 border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 8px; div.relative.h-full 274.0x170.5 bg lab(100 0 0) | div.bg-secondary.overflow-hidden 308.0x204.5 bg lab(94.1676 0.0340343 -2.27666) r 16px; div.relative.w-full 281.5x175.9 border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 8px; div.relative.h-full 279.5x173.9 bg lab(100 0 0) |
| How | at rest | mouse hover |

Crops: `entity-similar-default.png`, `entity-similar-hover.png`.

### Mobile (390 wide)

#### m-styles-card

Style card (mobile).

Page: styles. Selector: `a[href^="/style/"] at 390 wide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 293.75 |
| Padding | 0px |
| Border | none |
| Radius | 32px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neueMontreal 16px/24px 530 |
| Letter spacing | -0.32px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Text node | h3.text-xl.font-semibold: neueMontreal 20px/28px 600, lab(4.38504 0.200026 -3.38308), ls -0.5px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.bg-secondary.overflow-hidden 342.0x237.8 bg lab(97.4265 0.0201464 -1.51933) r 32px; div.relative.w-full 278.0x173.8 border T:1px solid lab(89.5164 0.0511706 -3.03215) / R:1px solid lab(89.5164 0.0511706 -3.03215) / B:1px solid lab(89.5164 0.0511706 -3.03215) / L:1px solid lab(89.5164 0.0511706 -3.03215) r 8px; div.relative.h-full 276.0x171.8 bg lab(100 0 0) |
| How | at rest |

Crops: `m-styles-card-default.png`.

#### m-styles-header

Styles header (mobile).

Page: styles. Selector: `header at 390 wide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 81 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid oklab(0.909998 -0.00000914931 -0.00797832 / 0.5); L: none |
| Radius | 0px |
| Background | oklab(0.999998 -0.00000980496 0.0000234246 / 0.9) |
| Box shadow | none |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | neueMontreal 16px/24px 530 |
| Letter spacing | -0.32px |
| Colour | lab(4.38504 0.200026 -3.38308) |
| Text node | span.w-2.5.shrink-0: neueMontreal 25px/32px 530, lab(4.38504 0.200026 -3.38308), ls -0.625px |
| Transition | none |
| Painted layers | header.sticky.top-0 390.0x81.0 bg oklab(0.999998 -0.00000980496 0.0000234246 / 0.9) border B:1px solid oklab(0.909998 -0.00000914931 -0.00797832 / 0.5) |
| Ancestor paint | 1 up body.min-h-full.flex bg lab(100 0 0) |
| How | at rest |

Crops: `m-styles-header-default.png`.

#### m-research-box

Research box (mobile).

Page: home. Selector: `the research card at 390 wide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 102 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #f7f8fb |
| Box shadow | #0c297e @ 0.07 0px 0px 0px 1px inset |
| Outline | none |
| Font | Base-Variable 16px/24px 500 |
| Letter spacing | -0.32px |
| Colour | #000000 |
| Text node | div: Base-Variable 14px/20px 600, #13151b, ls -0.28px |
| Transition | none |
| Icon | 18 x 20, colour #13151b |
| Painted layers | form 358.0x102.0 bg #f7f8fb r 24px shadow #0c297e @ 0.07 0px 0px 0px 1px inset; label 36.0x36.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px; div 0.0x0.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px; div 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div 138.6x36.0 bg #ffffff border T:1px solid #011158 @ 0.24 / R:1px solid #011158 @ 0.24 / B:1px solid #011158 @ 0.24 / L:1px solid #011158 @ 0.24 r 18px shadow #0c297e @ 0.09 0px 1px 3px 0px, #0c297e @ 0.03 0px 0px 1px 0.4px |
| How | at rest |

Crops: `m-research-box-default.png`.

## Transitions declared in the readable stylesheets

refero.design’s atomic CSS and the styles site’s own bundle are same-origin, so this list covers most of what ships; the per-state Transition rows above are computed values and cover the rest.

- entity: none

- home: `0.2s`, `0.3s`, `background 0.3s`, `background 0.2s`, `box-shadow 0.15s`, `box-shadow 0.25s`, `background 0.1s`, `opacity 0.5s, outline-color 0.3s`, `0.6s`, `none`, `border-color 0.2s`, `background 0.2s, opacity 0.3s`

- styles-index: none
