# Component measurements

Computed styles read from endel.io and app.endel.io on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one dark theme (no consent overlay mounts on these routes), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The fixed dark bar: the Endel mark, the nav links (ADHD, Sleep, Focus, Relax, Activity), the More flyout, Try Today and Sign In.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#000000 0%, #000000 @ 0.65 50%, #000000 @ 0 100%) |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | header.HeaderWrap-module__xM7-Ra__header 1440.0x72.0 image linear-gradient(#000000 0%, #000000 @ 0.65 50%, #000000 @ 0 100%); button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 94.0x44.0 bg #262626 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #ffffff 0px 0px 15px 0px; button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 73.6x44.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px; button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 0.0x0.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px |
| Ancestor paint | 1 up body.apercupro_72fda48b-module__wz2VEq__className bg #000000 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The 40x40 Endel mark, a link home.

Page: home. Selector: `header a:first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | undefined: apercuPro 22px/28px 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link.

Page: home. Selector: `header a:has-text("Focus")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.77 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff, underline | = | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff, underline |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Link-module__QL15TW__link.Link-module__QL15TW__color-white 56.8x28.0 shadow #666666 0px 0px 0px 6px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-more

More button. The nav overflow toggle; its press opens the flyout inside the header.

Page: home. Selector: `MenuButton-module button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.66 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 22px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |
| Painted layers | - | = | button.MenuButton-module__hXokYa__button.MenuButton-module__hXokYa__closed 81.7x28.0 shadow #666666 0px 0px 0px 6px | = |

Crops: `nav-more-default.png`, `nav-more-hover.png`, `nav-more-focus-visible.png`, `nav-more-pressed.png`.

#### btn-try

Try Today button. The primary header CTA. Measured, never followed.

Page: home. Selector: `header Button-module button:has-text("Try Today")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 12px | = | = | = |
| Background | #262626 | #808080 | = | #808080 |
| Box shadow | #ffffff 0px 0px 15px 0px | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Button-module__zg_LDG__text: apercuPro 16px/16px 400, #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 94.0x44.0 bg #262626 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #ffffff 0px 0px 15px 0px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 94.0x44.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px shadow #ffffff 0px 0px 15px 0px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 94.0x44.0 bg #262626 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #666666 0px 0px 0px 6px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 94.0x44.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px shadow #ffffff 0px 0px 15px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-try-default.png`, `btn-try-hover.png`, `btn-try-focus-visible.png`, `btn-try-pressed.png`.

#### btn-signin

Sign In button. The header auth link. Measured, never followed.

Page: home. Selector: `header Button-module button:has-text("Sign In")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.58 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #262626 | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 12px | = | = | = |
| Background | #262626 | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Button-module__zg_LDG__text: apercuPro 16px/16px 400, #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 73.6x44.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 73.6x44.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 73.6x44.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px shadow #666666 0px 0px 0px 6px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 73.6x44.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-signin-default.png`, `btn-signin-hover.png`, `btn-signin-focus-visible.png`, `btn-signin-pressed.png`.

#### menu-flyout

More flyout. The expanded nav groups inside the header after More is pressed (Company, Technology, the store links). Read while held open.

Page: home. Selector: `header a:has-text("Manifesto") while the flyout is open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 172 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `menu-flyout-default.png`.

#### nav-more-open

More button, open. The trigger after its own toggle; the open flyout shows in the crop.

Page: home. Selector: `MenuButton-module button, open`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 81.66 x 28 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 22px/28px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #ffffff |
| How | menu held open by opts.open |

Crops: `nav-more-open-opened.png`.

### Marketing sections

#### hero-title

Hero title. The "Endel" display wordmark at the top of the home page.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 149.42 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 60px/72px 400 |
| Letter spacing | 0.35px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### page-ground

Page ground. The near-black every page paints on.

Page: home. Selector: `body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 12092.14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | body.apercupro_72fda48b-module__wz2VEq__className 1440.0x12092.1 bg #000000; header.HeaderWrap-module__xM7-Ra__header 1440.0x72.0 image linear-gradient(#000000 0%, #000000 @ 0.65 50%, #000000 @ 0 100%); button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 94.0x44.0 bg #262626 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #ffffff 0px 0px 15px 0px; button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 73.6x44.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px; button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 0.0x0.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px; div.HeaderDesktopDropdown-module__JpJt_q__dropdown 725.0x312.0 bg #000000 image linear-gradient(#181818 0%, #000000 @ 0 100%), none r 12px |
| How | at rest |

Crops: none.

#### section-title

Section title.

Page: home. Selector: `first visible h2, marked where it mounts`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 44px/56px 400 |
| Letter spacing | 0.35px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### body-text

Body text.

Page: home. Selector: `first visible marketing paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 564 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 22px/28px 400 |
| Letter spacing | normal |
| Colour | #bfbfbf |
| Transition | none |
| How | at rest |

Crops: `body-text-default.png`.

#### learn-more

Learn More link.

Page: home. Selector: `main a:has-text("Learn More")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 238 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #ffffff | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #ffffff, underline | = | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #ffffff, underline |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Link-module__QL15TW__link.Link-module__QL15TW__color-white 238.0x24.0 shadow #666666 0px 0px 0px 6px | = |

Crops: `learn-more-default.png`, `learn-more-hover.png`, `learn-more-focus-visible.png`, `learn-more-pressed.png`.

#### try-now

Try Now link.

Page: home. Selector: `main a:has-text("Try Now")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 516 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff, underline | = | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 22px/28px 400, #ffffff, underline |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Link-module__QL15TW__link.Link-module__QL15TW__color-white 516.0x28.0 shadow #666666 0px 0px 0px 6px | = |

Crops: `try-now-default.png`, `try-now-hover.png`, `try-now-focus-visible.png`, `try-now-pressed.png`.

#### play-button

Round media button. The 72x72 circular play control over the product imagery. Measured, never pressed.

Page: home. Selector: `Button-module button[class*="border-radius-full"] (72px, icon only)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72 x 72 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 100px | = | = | = |
| Background | #ffffff | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 22px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 36 x 36, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-full 72.0x72.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-full 72.0x72.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 100px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-full 72.0x72.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 100px shadow #666666 0px 0px 0px 6px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-full 72.0x72.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `play-button-default.png`, `play-button-hover.png`, `play-button-focus-visible.png`, `play-button-pressed.png`.

#### show-more

Show More button. Loads more press quotes into the reviews waterfall; a local toggle, never pressed for real beyond states.

Page: home. Selector: `main button:has-text("Show More")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 56 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 12px | = | = | = |
| Background | #262626 | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 22px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Button-module__zg_LDG__text: apercuPro 22px/22px 400, #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 368.0x56.0 bg #262626 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 368.0x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 368.0x56.0 bg #262626 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px shadow #666666 0px 0px 0px 6px | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 368.0x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `show-more-default.png`, `show-more-hover.png`, `show-more-focus-visible.png`, `show-more-pressed.png`.

#### accordion-title

FAQ accordion item. A question row in the FAQ; its own press expands the answer. Opened once for the reading.

Page: home. Selector: `AccordionTitle-module button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 1152 x 76 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 12px | = | = | = | = |
| Background | #191919 | #262626 | = | #262626 | #262626 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = | = |
| Outline | none | = | = | = | = |
| Font | apercuPro 16px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Text node | div.AccordionTitle-module__8AYIsW__text: apercuPro 22px/28px 400, #ffffff | = | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = | = |
| Painted layers | button.AccordionTitle-module__8AYIsW__button 1152.0x76.0 bg #191919 r 12px | button.AccordionTitle-module__8AYIsW__button 1152.0x76.0 bg #262626 r 12px | button.AccordionTitle-module__8AYIsW__button 1152.0x76.0 bg #191919 r 12px shadow #666666 0px 0px 0px 6px | button.AccordionTitle-module__8AYIsW__button 1152.0x76.0 bg #262626 r 12px | button.AccordionTitle-module__8AYIsW__button.AccordionTitle-module__8AYIsW__open 1152.0x76.0 bg #262626 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `accordion-title-default.png`, `accordion-title-hover.png`, `accordion-title-focus-visible.png`, `accordion-title-pressed.png`, `accordion-title-opened.png`.

#### accordion-content

FAQ answer. The answer panel under the open question.

Page: home. Selector: `AccordionContent-module wrap`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 1152 x 228 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.Text-module__0TXbEW__p.Text-module__0TXbEW__size-1: apercuPro 22px/28px 400, #bfbfbf |
| Transition | none |
| Painted layers | div.AccordionContent-module__FOEkQG__inner 1152.0x228.0 bg #191919 r 12px |
| How | menu held open by opts.open |

Crops: `accordion-content-opened.png`.

#### input-email

Newsletter email field. The newsletter signup input. Text was typed and deleted again; nothing was submitted.

Page: home. Selector: `main input`. States: .

Not found on the page at capture time.

#### btn-subscribe

Subscribe button. Submits the newsletter form. Measured in all states, never pressed for real.

Page: home. Selector: `main button:has-text("Subscribe")`. States: .

Not found on the page at capture time.

#### press-logo

Press logo. An outlet logo tile in the press wall. Measured, never followed.

Page: home. Selector: `PressWall-module a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.19 x 50.59 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #808080 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.PressWall-module__GcOYjq__item 211.2x50.6 r 8px shadow #808080 0px 0px 0px 4px | = |

Crops: `press-logo-default.png`, `press-logo-hover.png`, `press-logo-focus-visible.png`, `press-logo-pressed.png`.

#### page-title

Page title. The product page h1 ("Find your focus with Endel").

Page: focus. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 564 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 60px/72px 400 |
| Letter spacing | 0.35px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `page-title-default.png`.

#### soundscape-card

Soundscape card. A 270x270 soundscape tile linking its page (cover art, title, Try Now). Measured, never followed.

Page: focus. Selector: `a[class*="Card-module"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 270 x 270.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/0px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.Card-module__wjjOCW__icon-wrap 270.0x88.0 image linear-gradient(#000000 @ 0 0%, #000000 72.92%) | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `soundscape-card-default.png`, `soundscape-card-hover.png`, `soundscape-card-focus-visible.png`, `soundscape-card-pressed.png`.

#### scenario-card

Scenario card. A scenario tile from the Timed Scenarios band (same Card module, second row).

Page: focus. Selector: `a[class*="Card-module"] (timed scenarios row)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 270 x 270 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/0px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `scenario-card-default.png`.

### Web app (signed out)

#### app-header

App header. The signed-out web app bar: the FREEMIUM account chip and Sign In.

Page: app-explore. Selector: `app header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#000000, #000000 @ 0.65 50%, #000000 @ 0) |
| Box shadow | none |
| Outline | none |
| Font | apercuProRegular 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.UserButton-module__mw6o3a__text: apercuProRegular 12px/12px 400, #e0e0e0, ls 4px |
| Transition | none |
| Icon | 44 x 44, colour #ffffff |
| Painted layers | header.Header-module__iZZHxW__header 1440.0x72.0 image linear-gradient(#000000, #000000 @ 0.65 50%, #000000 @ 0); div.UserButton-module__mw6o3a__text 102.1x22.0 border T:1px solid #808080 / R:1px solid #808080 / B:1px solid #808080 / L:1px solid #808080 r 4px; button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 73.6x44.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px |
| How | at rest |

Crops: `app-header-default.png`.

#### user-button

FREEMIUM chip. The account state button; opens the account sheet. Measured, never opened (it gates on sign-in).

Page: app-explore. Selector: `UserButton-module button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 158.13 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.UserButton-module__mw6o3a__text: apercuProRegular 12px/12px 400, #e0e0e0, ls 4px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 44 x 44, colour #ffffff | = | = | = |
| Painted layers | div.UserButton-module__mw6o3a__text 102.1x22.0 border T:1px solid #808080 / R:1px solid #808080 / B:1px solid #808080 / L:1px solid #808080 r 4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `user-button-default.png`, `user-button-hover.png`, `user-button-focus-visible.png`, `user-button-pressed.png`.

#### app-btn-signin

Sign In button (app).

Page: app-explore. Selector: `app header button:has-text("Sign In")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.58 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #262626 | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 12px | = | = | = |
| Background | #262626 | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Button-module__LFCFwa__text: apercuProRegular 16px/16px 400, #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 73.6x44.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 73.6x44.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 73.6x44.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px shadow #666666 0px 0px 0px 6px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 73.6x44.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-btn-signin-default.png`, `app-btn-signin-hover.png`, `app-btn-signin-focus-visible.png`, `app-btn-signin-pressed.png`.

#### banner

Carousel banner. A promo card in the explore carousel (SPECIAL OFFER, product updates). Measured, never followed.

Page: app-explore. Selector: `a[class*="Banner-module"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 956 x 320 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #ffffff @ 0.15 offset -2px | = | none | = |
| Font | apercuProRegular 16px/0px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.TextLabel-module__i0u77G__label: apercuProMedium 12px/12px 400, #000000, ls 1px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.Banner-module__qXPcLq__banner.BannerCarousel-module__mk6V2G__slide 956.0x320.0 r 24px outline 2px solid #ffffff @ 0.15 offset -2px; div.TextLabel-module__i0u77G__label 121.7x21.0 bg #ffffff r 24px | = | div.TextLabel-module__i0u77G__label 121.7x21.0 bg #ffffff r 24px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `banner-default.png`, `banner-hover.png`, `banner-focus-visible.png`, `banner-pressed.png`.

#### banner-dot

Carousel dot. The selected pager dot under the banner carousel.

Page: app-explore. Selector: `BannerCarousel-module dot button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 12 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 50% |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | button.BannerCarousel-module__mk6V2G__dot.BannerCarousel-module__mk6V2G__selected 12.0x12.0 bg #ffffff r 50% |
| How | at rest |

Crops: `banner-dot-default.png`.

#### scenario-pill

Scenario pill. A rounded-full scenario tag in the explore grid (Focus Timer, ASMR, Meditate…). Selecting one gates on premium; never pressed for real.

Page: app-explore. Selector: `app Button-module pill:has-text("Focus Timer")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 202.52 x 56 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #262626 | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 100px | = | = | = |
| Background | #262626 | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 22px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Button-module__LFCFwa__text: apercuProRegular 22px/22px 400, #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| Painted layers | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 202.5x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 100px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 202.5x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 100px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 202.5x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 100px shadow #666666 0px 0px 0px 6px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 202.5x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `scenario-pill-default.png`, `scenario-pill-hover.png`, `scenario-pill-focus-visible.png`, `scenario-pill-pressed.png`.

#### soundscape-row

Soundscape row. A list row that opens a soundscape in the player (Focus, Colored Noises…). Measured; its destination is the public player.

Page: app-explore. Selector: `SoundscapeItem-module button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 956 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | p.Text-module__aznVca__p.Text-module__aznVca__size-h4: apercuProRegular 28px/28px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 56 x 56, colour #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `soundscape-row-default.png`, `soundscape-row-hover.png`, `soundscape-row-focus-visible.png`, `soundscape-row-pressed.png`.

#### mini-player

Mini player. The fixed bottom bar with the paused soundscape and transport. Audio was never started.

Page: app-explore. Selector: `MiniPlayer-module wrap`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 120 |
| Padding | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#000000 @ 0.05 0%, #000000 85%) |
| Box shadow | none |
| Outline | none |
| Font | apercuProRegular 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.Text-module__aznVca__p.Text-module__aznVca__size-4: apercuProRegular 14px/14px 400, #bfbfbf |
| Transition | none |
| Cursor | pointer |
| Icon | 56 x 56, colour #ffffff |
| Painted layers | div.MiniPlayer-module__sUQFsW__wrap 1440.0x120.0 image linear-gradient(#000000 @ 0.05 0%, #000000 85%); div.MiniPlayer-module__sUQFsW__player 400.0x88.0 bg #191919 r 100px; button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 56.0x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 100px |
| How | at rest |

Crops: `mini-player-default.png`.

### Player

#### player-header

Player header. The soundscape title bar over the visualizer (name + live energy state).

Page: app-player. Selector: `player header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 168 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuProRegular 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.Text-module__aznVca__p.Text-module__aznVca__size-h4: apercuProRegular 28px/28px 400, #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | div.GetAppBanner-module__TpEf9q__wrap 1440.0x56.0 bg #2b2b2b; button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 44.0x44.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px |
| How | at rest |

Crops: `player-header-default.png`.

#### player-title

Soundscape title.

Page: app-player. Selector: `player header h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 72.25 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuProRegular 28px/28px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `player-title-default.png`.

#### btn-close-player

Close button. The icon button that leaves the player for Explore. Measured, never pressed.

Page: app-player. Selector: `player header Button-module icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #2b2b2b | = | 2px solid #2b2b2b |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 44.0x44.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 44.0x44.0 border T:2px solid #2b2b2b / R:2px solid #2b2b2b / B:2px solid #2b2b2b / L:2px solid #2b2b2b r 12px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 44.0x44.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #666666 0px 0px 0px 6px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 44.0x44.0 border T:2px solid #2b2b2b / R:2px solid #2b2b2b / B:2px solid #2b2b2b / L:2px solid #2b2b2b r 12px |
| Ancestor paint | 1 up div.GetAppBanner-module__TpEf9q__wrap bg #2b2b2b | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-close-player-default.png`, `btn-close-player-hover.png`, `btn-close-player-focus-visible.png`, `btn-close-player-pressed.png`.

#### btn-set-timer

Set Timer button. Opens the shut-off timer dialog. Pressed once to read the dialog, closed again.

Page: app-player. Selector: `player footer button:has-text("Set Timer")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 144.88 x 56 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #262626 | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 100px | = | = | = |
| Background | transparent | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 22px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Button-module__LFCFwa__text: apercuProRegular 22px/22px 400, #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 144.9x56.0 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 100px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 144.9x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 100px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 144.9x56.0 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 100px shadow #666666 0px 0px 0px 6px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 144.9x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-set-timer-default.png`, `btn-set-timer-hover.png`, `btn-set-timer-focus-visible.png`, `btn-set-timer-pressed.png`.

#### button-mode

Mode button. One of the energy-mode icon buttons under the visualizer.

Page: app-player. Selector: `ButtonMode-module button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | apercuProRegular 16px/0px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | opacity 0.25s linear | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 56 x 56, colour #ffffff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `button-mode-default.png`, `button-mode-hover.png`, `button-mode-pressed.png`.

#### button-mode-active

Mode button, active. The engaged mode icon.

Page: app-player. Selector: `ButtonMode-module button.is-active`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 56 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 56px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuProRegular 16px/0px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 56 x 56, colour #ffffff |
| How | at rest |

Crops: `button-mode-active-default.png`.

#### player-control

Transport button. A round transport control (play/skip). Audio was never started.

Page: app-player. Selector: `player footer round icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #191919 | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 100px | = | = | = |
| Background | #191919 | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 22px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| Painted layers | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 56.0x56.0 bg #191919 border T:2px solid #191919 / R:2px solid #191919 / B:2px solid #191919 / L:2px solid #191919 r 100px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 56.0x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 100px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 56.0x56.0 bg #191919 border T:2px solid #191919 / R:2px solid #191919 / B:2px solid #191919 / L:2px solid #191919 r 100px shadow #666666 0px 0px 0px 6px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-full 56.0x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `player-control-default.png`, `player-control-hover.png`, `player-control-focus-visible.png`, `player-control-pressed.png`.

#### volume

Volume slider. The range control at the transport row's right end. Never dragged.

Page: app-player. Selector: `input[class*="InputRange-module"], input[type="range"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 129 x 5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | transparent | = |
| Background image | linear-gradient(to right, #ffffff 100%, #808080 100%) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #101010 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Placeholder | #101010, opacity 1 | = |
| Painted layers | input.InputRange-module__pr8DUW__range 129.0x5.0 image linear-gradient(to right, #ffffff 100%, #808080 100%) r 20px | = |
| How | at rest | DOM focus (no click: it would set the slider value) |

Crops: `volume-default.png`, `volume-focused.png`.

#### btn-explore

Explore button. The back-to-explore pill in the player footer. Measured, never followed.

Page: app-player. Selector: `ExploreButton-module button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 324 x 58 | = | = | = |
| Padding | 16px 0px 14px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px 20px 0px 0px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#191919 0%, #000000 100%) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 22px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ExploreButton-module__e38y8W__button 324.0x58.0 image linear-gradient(#191919 0%, #000000 100%) r 20px 20px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -8) | = | = |

Crops: `btn-explore-default.png`, `btn-explore-hover.png`, `btn-explore-focus-visible.png`, `btn-explore-pressed.png`.

#### timer-dialog

Shut-off timer dialog. The bottom sheet Set Timer opens: duration chips, the premium Unlock and Done rows. Unlock was measured, never pressed.

Page: app-player. Selector: `TimerForm-module wrap`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 1440 x 583 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.8 |
| Box shadow | none |
| Outline | none |
| Font | apercuProRegular 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.Text-module__aznVca__p.Text-module__aznVca__size-h4: apercuProRegular 28px/normal 400, #ffffff |
| Transition | none |
| Icon | 240 x 240, colour #ffffff, fill #000000 |
| ::before | 1440px x 128px, absolute, bg #000000 @ 0 linear-gradient(#000000 @ 0 0%, #000000 @ 0.8 85%), radius 0px |
| Painted layers | div.TimerForm-module__uf4ooq__wrap 1440.0x583.0 bg #000000 @ 0.8; div::before.TimerForm-module__uf4ooq__wrap 1440pxx128px image linear-gradient(#000000 @ 0 0%, #000000 @ 0.8 85%); div.TimerForm-module__uf4ooq__input-wrap 300.0x300.0 bg #191919 r 32px; input 0.0x0.0 bg #efefef @ 0.3 border T:2px inset #767676 @ 0.3 / R:2px inset #767676 @ 0.3 / B:2px inset #767676 @ 0.3 / L:2px inset #767676 @ 0.3; button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 300.0x56.0 bg #262626 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px; button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 300.0x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px |
| How | menu held open by opts.open |

Crops: `timer-dialog-opened.png`.

#### btn-unlock

Unlock button. The premium upsell inside the timer dialog. Measured, never pressed (it starts checkout).

Page: app-player. Selector: `TimerForm-module button:has-text("Unlock")`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 300 x 56 |
| Padding | 0px 24px |
| Gap | 8px |
| Border | 2px solid #ffffff |
| Radius | 12px |
| Background | #262626 |
| Box shadow | none |
| Outline | none |
| Font | apercuProRegular 22px/22px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.Button-module__LFCFwa__text: apercuProRegular 22px/22px 400, #ffffff |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s |
| Cursor | pointer |
| Painted layers | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 300.0x56.0 bg #262626 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px |
| How | menu held open by opts.open |

Crops: `btn-unlock-opened.png`.

### Sign-in card

#### login-card

Sign-in card. The "Sign In or Register" panel: email field, Continue and the OAuth buttons. Nothing was submitted.

Page: app-login. Selector: `card ancestor of the sign-in heading (marked in-page)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 564 x 665 |
| Padding | 88px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuProRegular 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.Text-module__aznVca__p.Text-module__aznVca__size-h2: apercuProRegular 44px/normal 400, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | input.Input-module__iEWt7a__input 564.0x62.0 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px; button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 564.0x56.0 bg #262626 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px; div::before.Divider-module__QZkn-a__divider.Divider-module__QZkn-a__with-text 258.156pxx2px image linear-gradient(90deg, #000000 @ 0 0%, #262626 100%) r 2px; div::after.Divider-module__QZkn-a__divider.Divider-module__QZkn-a__with-text 258.141pxx2px image linear-gradient(270deg, #000000 @ 0 0%, #262626 100%) r 2px; button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 180.0x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px; button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 180.0x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px |
| How | at rest |

Crops: `login-card-default.png`.

#### input-email-login

Email field (sign-in). Read default and focused; no address was ever typed on this page.

Page: app-login. Selector: `login input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 564 x 62 | = |
| Padding | 16px 12px 14px 12px | = |
| Border | 2px solid #808080 | 2px solid #ffffff |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | apercuProRegular 22px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | default | = |
| Placeholder | #757575, opacity 1 | = |
| Painted layers | input.Input-module__iEWt7a__input 564.0x62.0 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px | input.Input-module__iEWt7a__input 564.0x62.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px |
| How | at rest | clicked into the field |

Crops: `input-email-login-default.png`, `input-email-login-focused.png`.

#### btn-continue

Continue button. Submits the sign-in form. Measured in all states, never pressed for real.

Page: app-login. Selector: `login button:has-text("Continue")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 564 x 56 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 12px | = | = | = |
| Background | #262626 | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 22px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Button-module__LFCFwa__text: apercuProRegular 22px/22px 400, #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 564.0x56.0 bg #262626 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 564.0x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 564.0x56.0 bg #262626 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 12px shadow #666666 0px 0px 0px 6px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 564.0x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-continue-default.png`, `btn-continue-hover.png`, `btn-continue-focus-visible.png`, `btn-continue-pressed.png`.

#### btn-oauth

OAuth button. One of the icon-only provider buttons (Apple, Facebook). Measured, never pressed.

Page: app-login. Selector: `login icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 56 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #262626 | 2px solid #808080 | = | 2px solid #808080 |
| Radius | 12px | = | = | = |
| Background | #262626 | #808080 | = | #808080 |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuProRegular 22px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| Painted layers | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 180.0x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 180.0x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 180.0x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px shadow #666666 0px 0px 0px 6px | button.Button-module__LFCFwa__button.Button-module__LFCFwa__border-radius-basic 180.0x56.0 bg #808080 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-oauth-default.png`, `btn-oauth-hover.png`, `btn-oauth-focus-visible.png`, `btn-oauth-pressed.png`.

### Footer

#### footer

Footer. The big footer: Explore and product link columns, stores, legal and socials.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 569 |
| Padding | 0px 64px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.Text-module__0TXbEW__p.Text-module__0TXbEW__size-4: apercuPro 14px/20px 400, #bfbfbf |
| Transition | none |
| Painted layers | input.Input-module__bBjBWq__input 466.0x56.0 border T:2px solid #808080 / R:2px solid #808080 / B:2px solid #808080 / L:2px solid #808080 r 12px; button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 466.0x56.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px; div.FooterBig-module__VBcn9W__bottom 1152.0x73.0 border T:1px solid #191919 |
| Ancestor paint | 1 up body.apercupro_72fda48b-module__wz2VEq__className bg #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.69 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #ffffff | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #ffffff, underline | = | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #ffffff, underline |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Link-module__QL15TW__link.Link-module__QL15TW__color-white 103.7x24.0 shadow #666666 0px 0px 0px 6px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/0px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Painted layers | - | = | a.Link-module__QL15TW__link.Link-module__QL15TW__color-white 24.0x24.0 shadow #666666 0px 0px 0px 4px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-legal

Legal link.

Page: home. Selector: `footer a:has-text("Privacy")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.92 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = |
| Outline | none | = | = | = |
| Font | apercuPro 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #bfbfbf | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #ffffff, underline | = | span.Link-module__QL15TW__text.Text-module__0TXbEW__p: apercuPro 18px/24px 400, #ffffff, underline |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Link-module__QL15TW__link.Link-module__QL15TW__color-gray-4 106.9x24.0 shadow #666666 0px 0px 0px 6px | = |

Crops: `footer-legal-default.png`, `footer-legal-hover.png`, `footer-legal-focus-visible.png`, `footer-legal-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The 56px bar: mark, Try Today and the Menu trigger.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#000000 0%, #000000 @ 0.65 50%, #000000 @ 0 100%) |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.HeaderLogo-module__XFmZVG__text: apercuPro 16px/22px 400, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | header.HeaderWrap-module__xM7-Ra__header 390.0x56.0 image linear-gradient(#000000 0%, #000000 @ 0.65 50%, #000000 @ 0 100%); button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 77.5x36.0 bg #262626 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px shadow #ffffff 0px 0px 15px 0px; button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 0.0x0.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px; button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 81.1x36.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px |
| Ancestor paint | 1 up body.apercupro_72fda48b-module__wz2VEq__className bg #000000 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. Opens the full-screen nav inside the header; pressed once for the open reading, closed again.

Page: home. Selector: `header button:has-text("Menu")`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 81.11 x 36 | = | = | = | = |
| Padding | 0px 12px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 2px solid #262626 | = | = | = | = |
| Radius | 12px | = | = | = | = |
| Background | #262626 | = | = | = | = |
| Box shadow | none | = | #666666 0px 0px 0px 6px | = | = |
| Outline | none | = | = | = | = |
| Font | apercuPro 12px/12px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | = |
| Text node | div.Button-module__zg_LDG__text: apercuPro 12px/12px 400, #ffffff | = | = | = | = |
| Transition | background-color, border-color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = | = |
| Painted layers | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 81.1x36.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px | = | button.Button-module__zg_LDG__button.Button-module__zg_LDG__border-radius-basic 81.1x36.0 bg #262626 border T:2px solid #262626 / R:2px solid #262626 / B:2px solid #262626 / L:2px solid #262626 r 12px shadow #666666 0px 0px 0px 6px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`, `m-menu-button-opened.png`.

#### m-menu-flyout

Mobile menu, open. A promo row in the open menu (students / teams / gift cards). Read while held open.

Page: home. Selector: `header a while menu is open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 44 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.Text-module__0TXbEW__p.Text-module__0TXbEW__size-1: apercuPro 16px/22px 400, #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-menu-flyout-default.png`.

#### m-hero-title

Hero title (mobile).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 90.36 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | apercuPro 36px/42px 400 |
| Letter spacing | 0.35px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- app-explore: `unset`, `opacity 0.2s linear`, `opacity 0.4s linear`, `background-color 0.2s, border-color 0.2s`, `width 0.5s`, `opacity 0.25s linear`, `box-shadow 0.2s`, `border-color 0.2s`, `border 0.2s`, `border-color 0.15s`, `opacity 0.15s, transform 0.1s`, `background-color 0.3s`

- home: `unset`, `opacity 0.2s linear`, `opacity 0.4s linear`, `transform 0.3s`, `background-color 0.2s, border-color 0.2s`, `transform 0.2s`
