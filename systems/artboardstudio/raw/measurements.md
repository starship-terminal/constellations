# Component measurements

Computed styles read from arcade.software on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (the Finsweet consent banner, the Intercom launcher and the custom play cursor were hidden, never clicked or answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The top nav: wordmark, Mockup Library and Figma plugin links, Signup.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 106 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d1400 |
| Text node | div.text-block-2: system-ui 18px/27px 700, #0d1400 |
| Transition | none |
| Painted layers | div.div-block 40.0x40.0 bg #aaff00 border T:1px solid #dfff9f / R:1px solid #dfff9f / B:1px solid #dfff9f / L:1px solid #dfff9f r 8px; nav.nav-dropdown-list.shadow-three 0.0x0.0 bg #ffffff r 12px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `nav brand`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 179.31 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d1400 |
| Text node | div.text-block-2: system-ui 18px/27px 700, #0d1400 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.div-block 40.0x40.0 bg #aaff00 border T:1px solid #dfff9f / R:1px solid #dfff9f / B:1px solid #dfff9f / L:1px solid #dfff9f r 8px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A .button.is-link nav item. Measured, never followed.

Page: home. Selector: `a.button.is-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.95 x 42 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d1400 | #aaaaaa | = | #aaaaaa |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.button.is-link 113.0x42.0 r 8px outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signup

Signup link. The signup nav action. Measured, never followed.

Page: home. Selector: `a:has-text("Signup")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.47 x 42 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d1400 | #aaaaaa | = | #aaaaaa |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.button.is-link 50.5x42.0 r 8px outline 1px auto #005fcc offset 1px | = |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

#### version-card

Version card. The New version / Legacy version picker card.

Page: home. Selector: `a.div-block-236`. States: .

Not found on the page at capture time.

### Home

#### hero-title

Hero title.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 145.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Vend Sans 60.8px/72.96px 600 |
| Letter spacing | -2px |
| Colour | #0d1400 |
| Text node | strong: Vend Sans 60.8px/72.96px 700, #0d1400, ls -2px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### tab

Category tab. A mockup-category tab (Most Popular is the selected one).

Page: home. Selector: `.tab-button.w-tab-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200.27 x 50 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 1px solid #0d1400 @ 0.1 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #0d1400 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | system-ui 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.text-block-20: system-ui 16px/24px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tab-button.w-inline-block 200.3x50.0 bg #0d1400 border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tab-default.png`, `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`.

#### tab-selected

Tab, selected.

Page: home. Selector: `.w-tab-link.w--current`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 200.27 x 50 |
| Padding | 12px 24px |
| Border | 1px solid #0d1400 @ 0.1 |
| Radius | 8px |
| Background | #0d1400 |
| Box shadow | none |
| Outline | none |
| Font | system-ui 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.text-block-20: system-ui 16px/24px 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.tab-button.w-inline-block 200.3x50.0 bg #0d1400 border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px |
| How | at rest |

Crops: `tab-selected-default.png`.

#### tab-switched

Tab, switched. A tab after its own toggle; the selection moves locally.

Page: home. Selector: `.w-tab-link`. States: selected.

| Property | selected |
|---|---|
| Size (w x h) | 200.27 x 50 |
| Padding | 12px 24px |
| Border | 1px solid #0d1400 @ 0.1 |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | system-ui 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d1400 |
| Text node | div.text-block-20: system-ui 16px/24px 400, #0d1400 |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.tab-button.w-inline-block 200.3x50.0 bg #ffffff border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px |
| How | own toggle, pressed once; a local UI state, never submitted |

Crops: `tab-switched-selected.png`.

#### section-title

Section heading.

Page: home. Selector: `h2 mockup section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 154.73 x 23.03 |
| Padding | 0px 0px 0px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Vend Sans 19.2px/23.04px 600 |
| Letter spacing | normal |
| Colour | #0d1400 |
| Transition | none |
| Ancestor paint | 1 up div.div-block-23 bg #ffffff |
| How | at rest |

Crops: `section-title-default.png`.

#### mockup-card

Mockup card. A mockup preview tile link.

Page: home. Selector: `.div-block-19.w-dyn-item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 199.27 x 199.27 | = |
| Padding | 0px | = |
| Border | 1px solid #0d1400 @ 0.1 | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | system-ui 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d1400 | = |
| Transition | none | = |
| Painted layers | div.div-block-19.w-dyn-item 199.3x199.3 border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px | = |
| How | at rest | mouse hover |

Crops: `mockup-card-default.png`, `mockup-card-hover.png`.

#### plugin-cta

Plugin CTA. The "Install Figma plugin" icon action. Measured, never followed.

Page: home. Selector: `a.button.is-icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 229.58 x 42 | = | = | = |
| Padding | 8px 19.2px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #0d1400 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #0d1400 | #222222 | = | #222222 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/24px 400 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: system-ui 16px/24px 400, #ffffff, ls 0.5px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13 x 20, colour #ffffff | = | = | = |
| Painted layers | a.button.is-icon 229.6x42.0 bg #0d1400 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px | a.button.is-icon 229.6x42.0 bg #222222 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px | a.button.is-icon 229.6x42.0 bg #0d1400 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px outline 1px auto #005fcc offset 1px | a.button.is-icon 229.6x42.0 bg #222222 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plugin-cta-default.png`, `plugin-cta-hover.png`, `plugin-cta-focus-visible.png`, `plugin-cta-pressed.png`.

#### contact-cta

Contact CTA. The Contact icon action. Measured, never followed.

Page: home. Selector: `a:has-text("Contact")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 133.5 x 42 | = | = | = |
| Padding | 8px 19.2px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #0d1400 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #0d1400 | #222222 | = | #222222 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/24px 400 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: system-ui 16px/24px 400, #ffffff, ls 0.5px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | a.button.is-icon 133.5x42.0 bg #0d1400 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px | a.button.is-icon 133.5x42.0 bg #222222 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px | a.button.is-icon 133.5x42.0 bg #0d1400 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px outline 1px auto #005fcc offset 1px | a.button.is-icon 133.5x42.0 bg #222222 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `contact-cta-default.png`, `contact-cta-hover.png`, `contact-cta-focus-visible.png`, `contact-cta-pressed.png`.

### Mockup library

#### lib-title

Library title.

Page: mockup. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 852.94 x 67.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Vend Sans 56px/67.2px 700 |
| Letter spacing | normal |
| Colour | #0d1400 |
| Transition | none |
| How | at rest |

Crops: `lib-title-default.png`.

#### search-field

Library search field. Focused only; nothing typed or sent.

Page: mockup. Selector: `search input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 1005 x 64.69 | = |
| Padding | 16px 16px 16px 44px | = |
| Border | 1px solid #0d1400 @ 0.1 | = |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | system-ui 19.2px/30.72px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d1400 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0.6, opacity 1 | = |
| Painted layers | input.form_input-2.is-icon-left 1005.0x64.7 bg #ffffff border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px | = |
| How | at rest | clicked into the field |

Crops: `search-field-default.png`, `search-field-focused.png`.

#### filter-chip

Filter chip. A category filter on the library. Measured, never selected.

Page: mockup. Selector: `filter chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 317 x 50 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0d1400 | #222222 | = | #222222 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.text-block-26.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870: Vend Sans 16px/24px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.category-buttons-link.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870 317.0x50.0 bg #0d1400 r 12px; div.not-active-category 317.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; div.not-active-thumbnail.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870 40.0x40.0 bg #ffffff @ 0.1 border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px | a.category-buttons-link.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870 317.0x50.0 bg #222222 r 12px; div.not-active-category 317.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; div.not-active-thumbnail.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870 40.0x40.0 bg #ffffff @ 0.1 border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px | a.category-buttons-link.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870 317.0x50.0 bg #0d1400 r 12px outline 1px auto #005fcc offset 1px; div.not-active-category 317.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; div.not-active-thumbnail.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870 40.0x40.0 bg #ffffff @ 0.1 border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px | a.category-buttons-link.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870 317.0x50.0 bg #222222 r 12px; div.not-active-category 317.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; div.not-active-thumbnail.w-variant-bf70768e-f7f0-0350-91d8-7fc795fc2870 40.0x40.0 bg #ffffff @ 0.1 border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-chip-default.png`, `filter-chip-hover.png`, `filter-chip-focus-visible.png`, `filter-chip-pressed.png`.

#### lib-card

Library card. A mockup thumbnail tile.

Page: mockup. Selector: `library tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 317 x 50 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #f4f3f2 |
| Box shadow | none | = |
| Outline | none | = |
| Font | system-ui 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0d1400 | = |
| Text node | div.text-block-11: system-ui 16px/24px 400, #0d1400 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.not-active-category 317.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; div.not-active-thumbnail 40.0x40.0 bg #ffffff border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px | a.category-buttons-link.w-inline-block 317.0x50.0 bg #f4f3f2 r 12px; div.not-active-category 317.0x50.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px; div.not-active-thumbnail 40.0x40.0 bg #ffffff border T:1px solid #0d1400 @ 0.1 / R:1px solid #0d1400 @ 0.1 / B:1px solid #0d1400 @ 0.1 / L:1px solid #0d1400 @ 0.1 r 8px |
| How | at rest | mouse hover |

Crops: `lib-card-default.png`, `lib-card-hover.png`.

### Figma plugin page

#### figma-title

Figma page title.

Page: figma. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 145.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Vend Sans 60.8px/72.96px 600 |
| Letter spacing | -2px |
| Colour | #0d1400 |
| Text node | strong.bold-text: Vend Sans 60.8px/72.96px 700, #0d1400, ls -2px |
| Transition | none |
| How | at rest |

Crops: `figma-title-default.png`.

#### figma-cta

Figma install CTA. The page primary action. Measured, never followed.

Page: figma. Selector: `install CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 206.45 x 42 | = | = | = |
| Padding | 8px 19.2px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #0d1400 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #0d1400 | #222222 | = | #222222 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/24px 400 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: system-ui 16px/24px 400, #ffffff, ls 0.5px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | a.button.is-icon 206.5x42.0 bg #0d1400 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px | a.button.is-icon 206.5x42.0 bg #222222 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px | a.button.is-icon 206.5x42.0 bg #0d1400 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px outline 1px auto #005fcc offset 1px | a.button.is-icon 206.5x42.0 bg #222222 border T:1px solid #0d1400 / R:1px solid #0d1400 / B:1px solid #0d1400 / L:1px solid #0d1400 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `figma-cta-default.png`, `figma-cta-hover.png`, `figma-cta-focus-visible.png`, `figma-cta-pressed.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1102 |
| Padding | 48px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | system-ui 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d1400 |
| Text node | div.text-block-2: system-ui 18px/27px 700, #0d1400 |
| Transition | none |
| Icon | 24 x 24, colour #0d1400 |
| Painted layers | div.footer 1440.0x1102.0 bg #ffffff; div.div-block 40.0x40.0 bg #aaff00 border T:1px solid #dfff9f / R:1px solid #dfff9f / B:1px solid #dfff9f / L:1px solid #dfff9f r 8px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.95 x 42 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d1400 | #aaaaaa | = | #aaaaaa |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.button.is-link 113.0x42.0 r 8px outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0d1400 |
| Text node | div.text-block-2: system-ui 18px/27px 700, #0d1400 |
| Transition | none |
| Painted layers | div.div-block 0.0x0.0 bg #aaff00 border T:1px solid #dfff9f / R:1px solid #dfff9f / B:1px solid #dfff9f / L:1px solid #dfff9f r 8px; ul.nav-menu-3.w-list-unstyled 0.0x0.0 bg #ffffff; nav.nav-dropdown-list.shadow-three 0.0x0.0 bg #ffffff r 12px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `.w-nav-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4d65ff offset 2px | = |
| Font | system-ui 24px/36px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d1400 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | div.menu-button-2.w-nav-button 48.0x48.0 outline 2px solid #4d65ff offset 2px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The bar after its own toggle; the crop is the opened nav panel.

Page: home. Selector: `.w-nav-button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 12px |
| Border | none |
| Radius | 0px |
| Background | #a6b1bf |
| Box shadow | none |
| Outline | none |
| Font | system-ui 24px/36px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.menu-button-2.w-nav-button 48.0x48.0 bg #a6b1bf |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. Read inside the open menu.

Page: home. Selector: `nav link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 112.95 x 42 |
| Padding | 4px 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 16px/16px 400 |
| Letter spacing | normal |
| Colour | #0d1400 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-nav-link-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `font-size 0.2s`, `width 0.2s cubic-bezier(0.455, 0.03, 0.515, 0.955), box-shadow 0.3s cubic-bezier(0.455, 0.03, 0.515, 0.955)`, `box-shadow 0.3s`, `0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `padding 0.2s cubic-bezier(0.6, -0.28, 0.735, 0.045)`, `0.2s cubic-bezier(0.55, 0.085, 0.68, 0.53)`, `0.2s cubic-bezier(0.55, 0.055, 0.675, 0.19)`, `opacity 0.4s`
