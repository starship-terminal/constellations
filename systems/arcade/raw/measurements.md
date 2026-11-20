# Component measurements

Computed styles read from arcade.software on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (the Finsweet consent banner, the Intercom launcher and the custom play cursor were hidden, never clicked or answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The fixed top bar: logo, Product/Pricing/Blog/Enterprise links, Log in and Sign up.

Page: home. Selector: `.navbar.w-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div: Inter Variable 14px/20px 500, #000000 @ 0.7 |
| Transition | background-color 0.15s ease-in |
| Icon | 98 x 26, colour #333333 |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.navbar.w-nav 1440.0x72.0 bg #ffffff @ 0; div.product-dropdown-content 512.2x220.6 bg #ffffff r 24px shadow #000000 @ 0.03 0px 32px 32px 0px, #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -1px, #000000 @ 0.1 0px 0px 0px 1px; a.product-dropdown-link.product-dropdown-feature 244.3x204.9 bg #f4f4f4 r 16px; a.btn.w-inline-block 74.5x32.0 bg #000000 r 12px; a.btn.open-app-btn 0.0x0.0 bg #000000 r 12px; button 0.0x0.0 bg #efefef |
| Ancestor paint | 1 up body.we-are-different bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `.logo-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 106 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | all 0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| Cursor | pointer |
| Icon | 98 x 26, colour #333333 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link.

Page: home. Selector: `.nav-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70.73 x 32 | = | = | 68.61 x 31.04 |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #000000 @ 0.06 | = | #000000 @ 0.06 |
| Box shadow | none | = | #000000 @ 0.2 0px 0px 0px 2px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.7 | #000000 | = | #000000 |
| Text node | div: Inter Variable 14px/20px 500, #000000 @ 0.7 | div: Inter Variable 14px/20px 500, #000000 | = | div: Inter Variable 14px/20px 500, #000000 |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav-btn.w-inline-block 70.7x32.0 bg #000000 @ 0.06 r 12px | a.nav-btn.w-inline-block 70.7x32.0 r 12px shadow #000000 @ 0.2 0px 0px 0px 2px outline 1px auto #005fcc offset 1px | a.nav-btn.w-inline-block 68.6x31.0 bg #000000 @ 0.06 r 12px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in button. The ghost nav action. Measured, never followed.

Page: home. Selector: `a.btn.transparent-blend`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.73 x 32 | = | = | 62.79 x 31.04 |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #000000 @ 0.06 | = | #000000 @ 0.06 |
| Box shadow | none | = | #000000 @ 0.2 0px 0px 0px 2px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div: Inter Variable 14px/20px 500, #000000 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.btn.transparent-blend 64.7x32.0 bg #000000 @ 0.06 r 12px | a.btn.transparent-blend 64.7x32.0 r 12px shadow #000000 @ 0.2 0px 0px 0px 2px outline 1px auto #005fcc offset 1px | a.btn.transparent-blend 62.8x31.0 bg #000000 @ 0.06 r 12px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

Sign up button. The black pill nav action. Measured, never followed.

Page: home. Selector: `.navbar a.btn:has-text("Sign up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.48 x 32 | = | = | 72.25 x 31.04 |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #000000 | #404040 | = | #404040 |
| Box shadow | none | = | #000000 @ 0.2 0px 0px 0px 2px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: Inter Variable 14px/20px 500, #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.w-inline-block 74.5x32.0 bg #000000 r 12px | a.btn.w-inline-block 74.5x32.0 bg #404040 r 12px | a.btn.w-inline-block 74.5x32.0 bg #000000 r 12px shadow #000000 @ 0.2 0px 0px 0px 2px outline 1px auto #005fcc offset 1px | a.btn.w-inline-block 72.2x31.0 bg #404040 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

### Home

#### hero-title

Hero title. One of the animated .heading-1 lines.

Page: home. Selector: `h1.heading-1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 305.06 x 67.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 56px/67.2px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Inter Display 56px/67.2px 400, #000000 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-subtitle

Hero subtitle.

Page: home. Selector: `hero subline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 403.95 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.8 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Ancestor paint | 1 up section.hero-container.arcade-exact-hero bg #ffffff |
| How | at rest |

Crops: `hero-subtitle-default.png`.

#### prompt-box

Prompt box. The "describe your video" composer on the hero: textarea, plus and send.

Page: home. Selector: `.arcade-prompt`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 680 x 148 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -2px, #000000 @ 0.12 0px 0px 0px 1px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button: Inter Variable 12px/16px 500, #000000 @ 0.6 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.arcade-prompt 680.0x148.0 bg #ffffff r 16px shadow #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -2px, #000000 @ 0.12 0px 0px 0px 1px; button.arcade-prompt-send 32.0x32.0 bg #000000 r 12px; button 103.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px; button 88.3x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px; button 99.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px; button 112.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px |
| Ancestor paint | 1 up section.hero-container.arcade-exact-hero bg #ffffff |
| How | at rest |

Crops: `prompt-box-default.png`.

#### prompt-field

Prompt field. Focused only; nothing was sent.

Page: home. Selector: `.arcade-prompt textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 680 x 148 | = |
| Padding | 16px 16px 48px 16px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Placeholder | #a3a3a3, opacity 1 | = |
| Ancestor paint | 1 up div.arcade-prompt bg #ffffff shadow #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -2px, #000000 @ 0.12 0px 0px 0px 1px | = |
| How | at rest | clicked into the field |

Crops: `prompt-field-default.png`, `prompt-field-focused.png`.

#### prompt-send

Prompt send. The composer submit. Measured, never pressed.

Page: home. Selector: `.arcade-prompt-send`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 31.04 x 31.04 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter Variable 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, opacity, transform 0.16s, 0.16s, 0.16s ease, ease, cubic-bezier(0.2, 0.8, 0.2, 1) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | 17.46 x 17.46, colour #ffffff |
| Painted layers | button.arcade-prompt-send 32.0x32.0 bg #000000 r 12px | = | button.arcade-prompt-send 32.0x32.0 bg #000000 r 12px outline 2px solid #000000 offset 2px | button.arcade-prompt-send 31.0x31.0 bg #000000 r 12px |
| Ancestor paint | 3 up div.arcade-prompt bg #ffffff shadow #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -2px, #000000 @ 0.12 0px 0px 0px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `prompt-send-default.png`, `prompt-send-hover.png`, `prompt-send-focus-visible.png`, `prompt-send-pressed.png`.

#### prompt-plus

Prompt plus link. "Open Arcade" beside the composer. Measured, never followed.

Page: home. Selector: `.arcade-prompt-plus`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 31.04 x 31.04 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter Variable 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, opacity, transform 0.16s, 0.16s, 0.16s ease, ease, cubic-bezier(0.2, 0.8, 0.2, 1) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | 15.52 x 15.52, colour #000000 |
| Ancestor paint | 3 up div.arcade-prompt bg #ffffff shadow #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -2px, #000000 @ 0.12 0px 0px 0px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.arcade-prompt-plus 32.0x32.0 bg #f5f5f5 r 12px | a.arcade-prompt-plus 32.0x32.0 r 12px outline 2px solid #000000 offset 2px | a.arcade-prompt-plus 31.0x31.0 bg #f5f5f5 r 12px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `prompt-plus-default.png`, `prompt-plus-hover.png`, `prompt-plus-focus-visible.png`, `prompt-plus-pressed.png`.

#### suggestion-chip

Suggestion chip. A prompt preset pill under the composer. Tapped in screenshots only; never submitted.

Page: home. Selector: `.arcade-prompt-suggestions button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.02 x 32 | = | = | 99.93 x 31.04 |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #000000 @ 0.2 | 1px solid #000000 @ 0.35 | = | 1px solid #000000 @ 0.35 |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter Variable 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.6 | #000000 @ 0.8 | = | #000000 @ 0.8 |
| Transition | color, border-color, transform 0.16s, 0.16s, 0.16s ease, ease, cubic-bezier(0.2, 0.8, 0.2, 1) delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button 103.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px | button 103.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.35 / R:1px solid #000000 @ 0.35 / B:1px solid #000000 @ 0.35 / L:1px solid #000000 @ 0.35 r 12px | button 103.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px outline 2px solid #000000 offset 2px | button 99.9x31.0 bg #ffffff border T:1px solid #000000 @ 0.35 / R:1px solid #000000 @ 0.35 / B:1px solid #000000 @ 0.35 / L:1px solid #000000 @ 0.35 r 12px |
| Ancestor paint | 3 up div.arcade-prompt bg #ffffff shadow #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -2px, #000000 @ 0.12 0px 0px 0px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `suggestion-chip-default.png`, `suggestion-chip-hover.png`, `suggestion-chip-focus-visible.png`, `suggestion-chip-pressed.png`.

#### scatter-card

Scatter card. A "Play <title>" video card in the Made-to-be-seen wall. Measured, never followed.

Page: home. Selector: `.scatter-card-trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 276.65 x 168.8 | 291.56 x 198.52 | 274.8 x 171.97 | 272.22 x 175.34 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | none | = | = | = |
| Ancestor paint | 1 up div.scatter-card shadow #000000 @ 0.1 0px 16px 30px 0px, #000000 @ 0.08 0px 32px 70px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.scatter-card-trigger.w-inline-block 274.8x172.0 outline 1px auto #005fcc offset 1px | = |

Crops: `scatter-card-default.png`, `scatter-card-hover.png`, `scatter-card-focus-visible.png`, `scatter-card-pressed.png`.

#### spotlight-quote

Spotlight quote.

Page: home. Selector: `.spotlight-quote`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 204 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Inter Display 36px/40px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `spotlight-quote-default.png`.

#### spotlight-next

Spotlight next. The quote carousel arrow. Pressed once for the screenshot state.

Page: home. Selector: `.spotlight-next`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | 38.8 x 38.8 |
| Padding | 0px | = | = | = |
| Border | 1px solid #e5e7eb | = | = | = |
| Radius | 14px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | opacity, transform 0.15s, 0.15s cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | 19.4 x 19.4, colour #000000 |
| Painted layers | a.spotlight-next.w-button 40.0x40.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px | = | a.spotlight-next.w-button 40.0x40.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px outline 1px auto #005fcc offset 1px | a.spotlight-next.w-button 38.8x38.8 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `spotlight-next-default.png`, `spotlight-next-hover.png`, `spotlight-next-focus-visible.png`, `spotlight-next-pressed.png`.

#### cta-large

Large CTA. The black Get started pill mid-page. Measured, never followed.

Page: home. Selector: `a.btn.large`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.66 x 42 | = | = | 103.46 x 40.74 |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #000000 | #404040 | = | #404040 |
| Box shadow | none | = | #000000 @ 0.2 0px 0px 0px 2px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: Inter Variable 14px/20px 500, #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.large 106.7x42.0 bg #000000 r 16px | a.btn.large 106.7x42.0 bg #404040 r 16px | a.btn.large 106.7x42.0 bg #000000 r 16px shadow #000000 @ 0.2 0px 0px 0px 2px outline 1px auto #005fcc offset 1px | a.btn.large 103.5x40.7 bg #404040 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `cta-large-default.png`, `cta-large-hover.png`, `cta-large-focus-visible.png`, `cta-large-pressed.png`.

#### cta-secondary

Secondary CTA. The outlined Talk to sales. Measured, never followed.

Page: home. Selector: `a.btn.large.secondary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130 x 42 | = | = | 126.1 x 40.74 |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #e7e7e7 | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff | #fafafa | = | #fafafa |
| Box shadow | none | = | #000000 @ 0.2 0px 0px 0px 2px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div: Inter Variable 14px/20px 500, #000000 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.large 130.0x42.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 16px | a.btn.large 130.0x42.0 bg #fafafa border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 16px | a.btn.large 130.0x42.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 16px shadow #000000 @ 0.2 0px 0px 0px 2px outline 1px auto #005fcc offset 1px | a.btn.large 126.1x40.7 bg #fafafa border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`, `cta-secondary-pressed.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 664 x 57.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 48px/57.6px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-card-pro

Pro plan card.

Page: pricing. Selector: `.new-pricing-plan (Pro)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 437.33 x 522 |
| Padding | 2px |
| Border | none |
| Radius | 24px |
| Background | #f4f4f4 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.new-pricing-plan-title: Inter Display 20px/28px 400, #000000 |
| Transition | none |
| Painted layers | div.new-pricing-plan 437.3x522.0 bg #f4f4f4 r 24px; div.new-pricing-top-content 433.3x322.0 bg #ffffff r 22px; div.dropdown-pricing.w-dropdown-toggle 385.3x42.0 border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 12px; nav.dropdown-list.w-dropdown-list 0.0x0.0 bg #dddddd; a.dropdown-link.w-inline-block 0.0x0.0 bg #f4f4f4 r 8px; div.pricing-popular-badge 0.0x0.0 bg #fcff5d r 12px |
| How | at rest |

Crops: `plan-card-pro-default.png`.

#### plan-cta-pro

Choose Pro button. The primary plan CTA. Measured, never followed.

Page: pricing. Selector: `a.btn.new-pricing-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 385.33 x 42 | = | = | 373.77 x 40.74 |
| Padding | 9px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #000000 | #404040 | = | #404040 |
| Box shadow | none | = | #000000 @ 0.2 0px 0px 0px 2px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.new-pricing-btn 385.3x42.0 bg #000000 r 12px | a.btn.new-pricing-btn 385.3x42.0 bg #404040 r 12px | a.btn.new-pricing-btn 385.3x42.0 bg #000000 r 12px shadow #000000 @ 0.2 0px 0px 0px 2px outline 1px auto #005fcc offset 1px | a.btn.new-pricing-btn 373.8x40.7 bg #404040 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `plan-cta-pro-default.png`, `plan-cta-pro-hover.png`, `plan-cta-pro-focus-visible.png`, `plan-cta-pro-pressed.png`.

#### plan-cta-neutral

Choose Free button. The neutral plan CTA. Measured, never followed.

Page: pricing. Selector: `a.btn.neutral.new-pricing-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 385.33 x 42 | = | = | 373.77 x 40.74 |
| Padding | 9px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #f4f4f4 | #e7e7e7 | = | #e7e7e7 |
| Box shadow | none | = | #000000 @ 0.2 0px 0px 0px 2px | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.neutral 385.3x42.0 bg #f4f4f4 r 12px | a.btn.neutral 385.3x42.0 bg #e7e7e7 r 12px | a.btn.neutral 385.3x42.0 bg #f4f4f4 r 12px shadow #000000 @ 0.2 0px 0px 0px 2px outline 1px auto #005fcc offset 1px | a.btn.neutral 373.8x40.7 bg #e7e7e7 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `plan-cta-neutral-default.png`, `plan-cta-neutral-hover.png`, `plan-cta-neutral-focus-visible.png`, `plan-cta-neutral-pressed.png`.

#### plan-price

Plan price.

Page: pricing. Selector: `.new-pricing-plan-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 62.28 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 36px/36px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.sym.sym-currency: Inter Display 36px/36px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### model-radio

Credit calculator radio. A model option on the video cost calculator; the input is visually hidden, the label paints it.

Page: pricing. Selector: `input[name=avc-model] label`. States: default, selected.

| Property | default | selected |
|---|---|---|
| Size (w x h) | 168.66 x 32 | = |
| Padding | 4px 6px 4px 12px | = |
| Gap | 8px | = |
| Border | 1px solid #e5e5e5 | = |
| Radius | 12px | = |
| Background | #ffffff | #f5f5f5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #171717 | = |
| Text node | span.avc-model-name: Inter Variable 14px/20px 400, #171717 | = |
| Transition | background-color 0.15s ease | = |
| Cursor | pointer | = |
| Painted layers | label.avc-model 168.7x32.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px; span.avc-model-provider 63.6x20.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 6px | label.avc-model 168.7x32.0 bg #f5f5f5 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 12px; span.avc-model-provider 63.6x20.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 6px |
| How | at rest | own toggle, pressed once; a local UI state, never submitted |

Crops: `model-radio-default.png`, `model-radio-selected.png`.

#### faq-question

FAQ accordion button.

Page: pricing. Selector: `.avfaq-trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 700 x 56 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #171717 offset -2px | = |
| Font | Inter Variable 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span: Inter Variable 14px/20px 400, #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #a3a3a3 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.avfaq-trigger 700.0x56.0 r 16px outline 2px solid #171717 offset -2px | = |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-pressed.png`.

#### faq-open

FAQ accordion, open. The same item after its own toggle; the crop is the whole .avfaq-item, question and answer.

Page: pricing. Selector: `.avfaq-trigger`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 700 x 56 |
| Padding | 16px 24px |
| Gap | 16px |
| Border | none |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 14px/20px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span: Inter Variable 14px/20px 400, #171717 |
| Transition | none |
| Cursor | pointer |
| Icon | 0 x 0, colour #404040 |
| How | own toggle |

Crops: `faq-open-opened.png`.

#### ask-ai

Ask AI button. The icon pill that opens an AI answer for a FAQ. Measured, never pressed.

Page: pricing. Selector: `.ask-ai-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #f4f4f4 | #e7e7e7 | = | #e7e7e7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ask-ai-btn.w-inline-block 32.0x32.0 bg #f4f4f4 r 12px | a.ask-ai-btn.w-inline-block 32.0x32.0 bg #e7e7e7 r 12px | a.ask-ai-btn.w-inline-block 32.0x32.0 bg #f4f4f4 r 12px outline 1px auto #005fcc offset 1px | a.ask-ai-btn.w-inline-block 32.0x32.0 bg #e7e7e7 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ask-ai-default.png`, `ask-ai-hover.png`, `ask-ai-focus-visible.png`, `ask-ai-pressed.png`.

### Interactive demo page

#### demo-title

Demo title.

Page: demo. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342.28 x 116 |
| Padding | 6px 6px 6px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 48px/52px 600 |
| Letter spacing | -0.96px |
| Colour | #111827 |
| Transition | none |
| How | at rest |

Crops: `demo-title-default.png`.

#### demo-signup

Sign up for free. The page's nav CTA. Measured, never followed.

Page: demo. Selector: `.signup-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136.42 x 40 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #2142e7 | #4460ed | = | #4460ed |
| Box shadow | #111827 @ 0.04 0px 32px 32px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #182fa5 0px 0px 0px 1px | #111827 @ 0 0px 32px 32px 0px, #111827 @ 0 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px -4px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #2142e7 0px 0px 0px 1px | = | #111827 @ 0 0px 32px 32px 0px, #111827 @ 0 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px -4px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #2142e7 0px 0px 0px 1px |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.35s cubic-bezier(0.6, 0.6, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.is-nav-button 136.4x40.0 bg #2142e7 r 12px shadow #111827 @ 0.04 0px 32px 32px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #182fa5 0px 0px 0px 1px | a.button.is-nav-button 136.4x40.0 bg #4460ed r 12px shadow #111827 @ 0 0px 32px 32px 0px, #111827 @ 0 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px -4px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #2142e7 0px 0px 0px 1px | a.button.is-nav-button 136.4x40.0 bg #2142e7 r 12px shadow #111827 @ 0.04 0px 32px 32px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #182fa5 0px 0px 0px 1px outline 1px auto #005fcc offset 1px | a.button.is-nav-button 136.4x40.0 bg #4460ed r 12px shadow #111827 @ 0 0px 32px 32px 0px, #111827 @ 0 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px -4px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #2142e7 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-signup-default.png`, `demo-signup-hover.png`, `demo-signup-focus-visible.png`, `demo-signup-pressed.png`.

#### demo-tts

Talk to sales. The page's secondary nav CTA. Measured, never followed.

Page: demo. Selector: `.tts-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115.64 x 40 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | #f9fafb | = | #f9fafb |
| Box shadow | #111827 @ 0.04 0px 32px 32px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #111827 @ 0.16 0px 0px 0px 1px | #111827 @ 0 0px 32px 32px 0px, #111827 @ 0 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px -4px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #111827 @ 0.16 0px 0px 0px 1px | = | #111827 @ 0 0px 32px 32px 0px, #111827 @ 0 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px -4px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #111827 @ 0.16 0px 0px 0px 1px |
| Outline | none | = | 1px auto #005fcc offset 0.984375px | = |
| Font | Inter Variable 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111827 | = | = | = |
| Transition | all 0.35s cubic-bezier(0.6, 0.6, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.is-nav-button 115.6x40.0 bg #ffffff r 12px shadow #111827 @ 0.04 0px 32px 32px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #111827 @ 0.16 0px 0px 0px 1px | a.button.is-nav-button 115.6x40.0 bg #f9fafb r 12px shadow #111827 @ 0 0px 32px 32px 0px, #111827 @ 0 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px -4px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #111827 @ 0.16 0px 0px 0px 1px | a.button.is-nav-button 115.6x40.0 bg #ffffff r 12px shadow #111827 @ 0.04 0px 32px 32px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #111827 @ 0.16 0px 0px 0px 1px outline 1px auto #005fcc offset 0.984375px | a.button.is-nav-button 115.6x40.0 bg #f9fafb r 12px shadow #111827 @ 0 0px 32px 32px 0px, #111827 @ 0 0px 16px 16px 0px, #111827 @ 0.04 0px 8px 8px -4px, #111827 @ 0.04 0px 4px 4px -2px, #111827 @ 0.04 0px 2px 2px -1px, #111827 @ 0.16 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-tts-default.png`, `demo-tts-hover.png`, `demo-tts-focus-visible.png`, `demo-tts-pressed.png`.

#### url-field

URL-to-demo field. Focused only; nothing was typed or submitted.

Page: demo. Selector: `.url-to-demo-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 364.8 x 68.4 | 384 x 72 |
| Padding | 0px 8px 0px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 18px/72px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #9ca3af, opacity 1 | = |
| How | at rest | clicked into the field |

Crops: `url-field-default.png`, `url-field-focused.png`.

#### url-button

URL-to-demo button. The field's arrow submit. Measured, never pressed.

Page: demo. Selector: `.url-to-demo-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 34.2 x 34.2 | 36 x 36 | 36 x 36 | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 72px | = | = | = |
| Background | #2142e7 | #4460ed | #4460ed | #4460ed |
| Box shadow | #182fa5 0px 0px 0px 1px, #111827 @ 0.04 0px 2px 2px -2px, #111827 @ 0.04 0px 4px 4px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 32px 32px 0px | #2142e7 0px 0px 0px 1px, #111827 @ 0.04 0px 2px 2px -2px, #111827 @ 0.04 0px 4px 4px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 32px 32px 0px | #2142e7 0px 0px 0px 1px, #111827 @ 0.04 0px 2px 2px -2px, #111827 @ 0.04 0px 4px 4px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 32px 32px 0px | #2142e7 0px 0px 0px 1px, #111827 @ 0.04 0px 2px 2px -2px, #111827 @ 0.04 0px 4px 4px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 32px 32px 0px |
| Outline | none | = | = | = |
| Font | Inter Variable 18px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111827 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 19 x 19, colour #111827 | 20 x 20, colour #111827 | 20 x 20, colour #111827 | = |
| Painted layers | button.url-to-demo-button 34.2x34.2 bg #2142e7 r 72px shadow #182fa5 0px 0px 0px 1px, #111827 @ 0.04 0px 2px 2px -2px, #111827 @ 0.04 0px 4px 4px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 32px 32px 0px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px | button.url-to-demo-button 36.0x36.0 bg #4460ed r 72px shadow #2142e7 0px 0px 0px 1px, #111827 @ 0.04 0px 2px 2px -2px, #111827 @ 0.04 0px 4px 4px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 32px 32px 0px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px | button.url-to-demo-button 36.0x36.0 bg #4460ed r 72px shadow #2142e7 0px 0px 0px 1px, #111827 @ 0.04 0px 2px 2px -2px, #111827 @ 0.04 0px 4px 4px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 32px 32px 0px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px | button.url-to-demo-button 34.2x34.2 bg #4460ed r 72px shadow #2142e7 0px 0px 0px 1px, #111827 @ 0.04 0px 2px 2px -2px, #111827 @ 0.04 0px 4px 4px 0px, #111827 @ 0.04 0px 8px 8px 0px, #111827 @ 0.04 0px 16px 16px 0px, #111827 @ 0.04 0px 32px 32px 0px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px; div::before.line 100%x22% bg #ffffff r 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `url-button-default.png`, `url-button-hover.png`, `url-button-focus-visible.png`, `url-button-pressed.png`.

#### demo-card

Feature card.

Page: demo. Selector: `.card-text_wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 460 x 100 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 20px/28px 400 |
| Letter spacing | normal |
| Colour | #4b5563 |
| Text node | h3: Inter Variable 32px/36px 500, #111827, ls -0.32px |
| Transition | none |
| How | at rest |

Crops: `demo-card-default.png`.

#### newsletter-field

Newsletter field. Focused only; nothing was typed or submitted.

Page: demo. Selector: `.text-field.w-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 420 x 56 | = |
| Padding | 0px 114px 0px 16px | = |
| Border | 1px solid #e5e7eb | 1px solid #d1d5db |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 14px/14px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Transition | all 0.2s ease-out | = |
| Cursor | text | = |
| Placeholder | #999999, opacity 1 | = |
| Painted layers | input.text-field.w-input 420.0x56.0 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 16px | input.text-field.w-input 420.0x56.0 bg #ffffff border T:1px solid #d1d5db / R:1px solid #d1d5db / B:1px solid #d1d5db / L:1px solid #d1d5db r 16px |
| How | at rest | clicked into the field |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`.

### Contact sales

#### contact-title

Contact title.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 544 x 115.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 48px/57.6px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `contact-title-default.png`.

#### form-card

Form card.

Page: contact. Selector: `.contact-sales-form-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 697 |
| Padding | 8px |
| Border | 1px solid #e7e7e7 |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | label.ds-label: Inter Variable 14px/20px 500, #000000 |
| Transition | none |
| Painted layers | div.embed-wrapper.anim-slidefade-speed-1 480.0x697.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 24px; input.ds-input 199.0x40.0 bg #f4f4f4 border T:1px solid #f4f4f4 / R:1px solid #f4f4f4 / B:1px solid #f4f4f4 / L:1px solid #f4f4f4 r 12px; input.ds-input 199.0x40.0 bg #f4f4f4 border T:1px solid #f4f4f4 / R:1px solid #f4f4f4 / B:1px solid #f4f4f4 / L:1px solid #f4f4f4 r 12px; input.ds-input 414.0x40.0 bg #f4f4f4 border T:1px solid #f4f4f4 / R:1px solid #f4f4f4 / B:1px solid #f4f4f4 / L:1px solid #f4f4f4 r 12px; input.ds-input 414.0x40.0 bg #f4f4f4 border T:1px solid #f4f4f4 / R:1px solid #f4f4f4 / B:1px solid #f4f4f4 / L:1px solid #f4f4f4 r 12px; select.ds-input 414.0x40.0 bg #f4f4f4 image url(data:…) border T:1px solid #f4f4f4 / R:1px solid #f4f4f4 / B:1px solid #f4f4f4 / L:1px solid #f4f4f4 r 12px |
| How | at rest |

Crops: `form-card-default.png`.

#### field-text

Text field. One .ds-input (First name). A sample value was typed, measured, then deleted; the form was never submitted.

Page: contact. Selector: `input.ds-input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 199 x 40 | = | = |
| Padding | 0px 12px | = | = |
| Border | 1px solid #f4f4f4 | 1px solid #d4d4d4 | 1px solid #d4d4d4 |
| Radius | 12px | = | = |
| Background | #f4f4f4 | #ffffff | #ffffff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter Variable 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #404040 | #000000 | #000000 |
| Transition | background-color, border-color, color 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #a2a2a2, opacity 1 | = | = |
| Painted layers | input.ds-input 199.0x40.0 bg #f4f4f4 border T:1px solid #f4f4f4 / R:1px solid #f4f4f4 / B:1px solid #f4f4f4 / L:1px solid #f4f4f4 r 12px | input.ds-input 199.0x40.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 12px | input.ds-input 199.0x40.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 12px |
| How | at rest | clicked into the field | typed "Jane", then deleted; nothing sent |

Crops: `field-text-default.png`, `field-text-focused.png`, `field-text-filled.png`.

#### field-select

Select. Company-size select; focused only, never changed.

Page: contact. Selector: `select.ds-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 414 x 40 | = |
| Padding | 0px 42px 0px 12px | = |
| Border | 1px solid #f4f4f4 | 1px solid #d4d4d4 |
| Radius | 12px | = |
| Background | #f4f4f4 | #ffffff |
| Background image | url(data:…) | - |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #404040 | #000000 |
| Transition | background-color, border-color, color 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Painted layers | select.ds-input 414.0x40.0 bg #f4f4f4 image url(data:…) border T:1px solid #f4f4f4 / R:1px solid #f4f4f4 / B:1px solid #f4f4f4 / L:1px solid #f4f4f4 r 12px | select.ds-input 414.0x40.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 12px |
| How | at rest | clicked into the field |

Crops: `field-select-default.png`, `field-select-focused.png`.

#### field-textarea

Textarea. Focused only; nothing was typed.

Page: contact. Selector: `textarea.ds-input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 414 x 96 | = |
| Padding | 8px 12px | = |
| Border | 1px solid #f4f4f4 | 1px solid #d4d4d4 |
| Radius | 12px | = |
| Background | #f4f4f4 | #ffffff |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #404040 | #000000 |
| Transition | background-color, border-color, color 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #a2a2a2, opacity 1 | = |
| Painted layers | textarea.ds-input.ds-textarea 414.0x96.0 bg #f4f4f4 border T:1px solid #f4f4f4 / R:1px solid #f4f4f4 / B:1px solid #f4f4f4 / L:1px solid #f4f4f4 r 12px | textarea.ds-input.ds-textarea 414.0x96.0 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 12px |
| How | at rest | clicked into the field |

Crops: `field-textarea-default.png`, `field-textarea-focused.png`.

#### form-submit

Submit button. The Talk to sales submit. Measured, never pressed.

Page: contact. Selector: `.ds-submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 414 x 40 | = | - | = |
| Padding | 0px 12px | = | - | = |
| Border | none | = | - | = |
| Radius | 12px | = | - | = |
| Background | #000000 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter Variable 14px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | background-color 0.15s ease | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.ds-submit 414.0x40.0 bg #000000 r 12px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `form-submit-default.png`, `form-submit-hover.png`, `form-submit-pressed.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 670.09 |
| Padding | 80px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.12 0px -1px 0px 0px |
| Outline | none |
| Font | Inter Variable 14px/20px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.heading-4.new-pre-footer-title: Inter Display 24px/28.8px 400, #000000 |
| Transition | none |
| Painted layers | div.new-footer-brand 1440.0x670.1 bg #ffffff shadow #000000 @ 0.12 0px -1px 0px 0px; a.btn.large 130.0x42.0 bg #000000 r 16px; a.btn.large 130.0x42.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 16px; div.new-footer-sep 1344.0x1.0 bg #f3f4f6; a.new-footer-link.demos 169.8x34.0 bg #f1f3fe r 12px; a.new-social-link.w-inline-block 32.0x32.0 bg #f4f4f4 r 12px |
| Ancestor paint | 1 up body.we-are-different bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `.new-footer-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62.94 x 17.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/17.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #717171 | #000000 | = | #000000 |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.new-footer-link.w--current 62.9x17.5 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `.new-social-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #f4f4f4 | #e7e7e7 | = | #e7e7e7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/17.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.new-social-link.w-inline-block 32.0x32.0 bg #f4f4f4 r 12px | a.new-social-link.w-inline-block 32.0x32.0 bg #e7e7e7 r 12px | a.new-social-link.w-inline-block 32.0x32.0 bg #f4f4f4 r 12px outline 1px auto #005fcc offset 1px | a.new-social-link.w-inline-block 32.0x32.0 bg #e7e7e7 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-legal

Legal link.

Page: home. Selector: `.new-footer-link:has-text("Privacy")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.58 x 17.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Variable 14px/17.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #717171 | #000000 | = | #000000 |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.new-footer-link 92.6x17.5 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-legal-default.png`, `footer-legal-hover.png`, `footer-legal-focus-visible.png`, `footer-legal-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `.navbar.w-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0 |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Inter Variable 14px/24px 500, #000000 |
| Transition | background-color 0.15s ease-in |
| Icon | 98 x 26, colour #333333 |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.navbar.w-nav 390.0x72.0 bg #ffffff @ 0; div.product-dropdown-content 0.0x0.0 bg #ffffff r 24px shadow #000000 @ 0.03 0px 32px 32px 0px, #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -1px, #000000 @ 0.1 0px 0px 0px 1px; a.product-dropdown-link.product-dropdown-feature 0.0x0.0 bg #f4f4f4 r 16px; a.btn.w-inline-block 0.0x0.0 bg #000000 r 12px; a.btn.open-app-btn 0.0x0.0 bg #000000 r 12px; div 390.0x368.0 bg #f4f4f4 r 28px |
| Ancestor paint | 1 up body.we-are-different bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `.w-nav-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.03 x 32 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset -2px | = |
| Font | Inter Variable 14px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Inter Variable 14px/24px 500, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button 66.0x32.0 r 12px outline 2px solid #000000 offset -2px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The bar after its own toggle; the crop is the opened sheet (the nav panel's grandparent div) that holds the links and actions.

Page: home. Selector: `.w-nav-button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 66.03 x 32 |
| Padding | 0px 14px |
| Border | none |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 14px/24px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Inter Variable 14px/24px 500, #000000 |
| Transition | none |
| Cursor | pointer |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. Read inside the open menu.

Page: home. Selector: `a.nav-btn`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Variable 24px/26.4px 400 |
| Letter spacing | -0.48px |
| Colour | #717171 |
| Text node | div: Inter Variable 24px/26.4px 400, #717171, ls -0.48px |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | pointer |
| How | at rest |

Crops: `m-nav-link-default.png`.

#### m-prompt

Mobile prompt box.

Page: home. Selector: `.arcade-prompt`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 148 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -2px, #000000 @ 0.12 0px 0px 0px 1px |
| Outline | none |
| Font | Inter Variable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button: Inter Variable 12px/16px 500, #000000 @ 0.6 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.arcade-prompt 342.0x148.0 bg #ffffff r 16px shadow #000000 @ 0.03 0px 16px 16px 0px, #000000 @ 0.03 0px 8px 8px 0px, #000000 @ 0.03 0px 4px 4px 0px, #000000 @ 0.03 0px 2px 2px -2px, #000000 @ 0.12 0px 0px 0px 1px; button.arcade-prompt-send 32.0x32.0 bg #000000 r 12px; button 103.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px; button 88.3x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px; button 99.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px; button 112.0x32.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 12px |
| Ancestor paint | 1 up section.hero-container.arcade-exact-hero bg #ffffff |
| How | at rest |

Crops: `m-prompt-default.png`.

#### m-signup

Mobile Sign up. Read inside the open menu.

Page: home. Selector: `a.btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 175 x 48 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 14px | = | = | = |
| Background | #000000 | #404040 | = | #404040 |
| Box shadow | none | = | #000000 @ 0.2 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | Inter Variable 15px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: Inter Variable 15px/20px 500, #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.w-inline-block 175.0x48.0 bg #000000 r 14px | a.btn.w-inline-block 175.0x48.0 bg #404040 r 14px | a.btn.w-inline-block 175.0x48.0 bg #000000 r 14px shadow #000000 @ 0.2 0px 0px 0px 2px outline 2px solid #000000 offset 2px | a.btn.w-inline-block 175.0x48.0 bg #404040 r 14px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-signup-default.png`, `m-signup-hover.png`, `m-signup-focus-visible.png`, `m-signup-pressed.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.15s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `0.2s`, `border-color 0.1s`, `40ms`, `background-color 0.3s cubic-bezier(0.165, 0.84, 0.44, 1)`, `0.1s`, `0.2s ease-out`, `box-shadow 0.2s`, `opacity 0.3s ease-out`
