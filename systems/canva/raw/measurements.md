# Component measurements

Computed styles read from canva.com on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /pricing, /templates and the signed-out /login card — with the cookie banner hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The dark header bar (.theme.dark): the Canva logo, the Design/Product/Plans/Business/Education/Help flyout triggers and the Sign up / Log in actions.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.LbzErQ: Canva Sans 14px/22px 500, #ffffff @ 0.898 |
| Transition | none |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | button 0.0x0.0 bg #ffffff @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset; button.n156ng 62.1x32.0 bg #ffffff @ 0 r 12px; button.n156ng 70.5x32.0 bg #ffffff @ 0 r 12px; button.n156ng 52.9x32.0 bg #ffffff @ 0 r 12px; button.n156ng 75.9x32.0 bg #ffffff @ 0 r 12px; button.n156ng 84.8x32.0 bg #ffffff @ 0 r 12px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The "Canva home" wordmark anchor.

Page: home. Selector: `header a Canva home`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 90 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Design button that opens the header mega-menu; toggled, never followed.

Page: home. Selector: `header button Design`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62.13 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff @ 0 | #a370fc @ 0.2 | = | #ffffff @ 0.15 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #99c8ff offset -2px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.LbzErQ: Canva Sans 14px/22px 500, #ffffff @ 0.898 | span.LbzErQ: Canva Sans 14px/22px 500, #ffffff | = | = |
| Transition | background-color, border-color, color 0.1s, 0.1s, 0.1s linear, linear, linear delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.n156ng 62.1x32.0 bg #ffffff @ 0 r 12px | button.n156ng.mAyX2Q 62.1x32.0 bg #a370fc @ 0.2 r 12px | button.n156ng 62.1x32.0 bg #ffffff @ 0 r 12px outline 2px auto #99c8ff offset -2px | button.n156ng 62.1x32.0 bg #ffffff @ 0.15 r 12px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### signup-cta

Sign-up action. The header Sign up action (the purple pill); measured, never followed.

Page: home. Selector: `header Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #ffffff @ 0 | #ffffff @ 0.07 | = | #ffffff @ 0.15 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.khPe7Q: Canva Sans 14px/22px 500, #ffffff | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.UB5XWg 74.0x32.0 bg #ffffff @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset | a.UB5XWg 74.0x32.0 bg #ffffff @ 0.07 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset | a.UB5XWg 74.0x32.0 bg #ffffff @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset outline 1px auto #99c8ff offset 1px | a.UB5XWg 74.0x32.0 bg #ffffff @ 0.15 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.2 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-cta-default.png`, `signup-cta-hover.png`, `signup-cta-focus-visible.png`, `signup-cta-pressed.png`.

#### login-link

Log-in action. The header Log in action; measured, never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.42 x 32 | = | = | 63.78 x 31.68 |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #ffffff @ 0.898 | #ffffff | = | #ffffff @ 0.8 |
| Box shadow | #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | span.khPe7Q: Canva Sans 14px/22px 500, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.t61TJQ 64.4x32.0 bg #ffffff @ 0.898 r 10px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | a.t61TJQ 64.4x32.0 bg #ffffff r 10px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | a.t61TJQ 64.4x32.0 bg #ffffff @ 0.898 r 10px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #99c8ff offset 1px | a.t61TJQ 63.8x31.7 bg #ffffff @ 0.8 r 10px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.99, 0, 0, 0.99, 0, 0) |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### nav-dropdown

Nav flyout. The Design mega-menu panel (Digital design / Print design / Images / Videos columns), opened by its own trigger.

Page: home. Selector: `opened Design flyout`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 870 x 478 |
| Padding | 0px |
| Gap | 2px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.LbzErQ: Canva Sans 14px/22px 400, #101219 @ 0.698 |
| Transition | none |
| Painted layers | div.M7FgEA 216.0x478.0 bg #ffffff r 32px 0px 0px 32px; a.Yx3HJA 200.0x38.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset; a.Yx3HJA 200.0x38.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset; a.Yx3HJA 200.0x38.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset; a.Yx3HJA 200.0x38.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset; a.Yx3HJA 200.0x38.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Flyout link. A link inside the opened Design flyout.

Page: home. Selector: `flyout link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200 x 38 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0f1015 @ 0 | #404f6d @ 0.06 | #404f6d @ 0.06 | #394660 @ 0.14 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | 1px auto #005fcc offset 1px |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | span.LbzErQ: Canva Sans 14px/22px 500, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.Yx3HJA 200.0x38.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset | a.Yx3HJA 200.0x38.0 bg #404f6d @ 0.06 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset | a.Yx3HJA 200.0x38.0 bg #404f6d @ 0.06 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #005fcc offset 1px | a.Yx3HJA 200.0x38.0 bg #394660 @ 0.14 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #005fcc offset 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home

#### hero-title

Hero headline. The "What will you design today?" headline, white on the gradient hero band.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1044.42 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Canva Sans 24px/32px 600 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.898 |
| Text node | span.dIH_FQ: Canva Sans 80px/88px 400, #ffffff, ls -0.8px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the headline on the gradient hero.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 866.11 x 33.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Canva Sans 24px/33.6px 400 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.898 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The "Start designing" action on the dark hero; measured, never followed.

Page: home. Selector: `hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 192 x 56 | = | = | 190.08 x 55.44 |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | #ffffff @ 0.898 | #ffffff | = | #ffffff @ 0.8 |
| Box shadow | #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 0px | = |
| Font | Canva Sans 16px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | span.khPe7Q: Canva Sans 16px/22px 600, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Eeun9Q 192.0x56.0 bg #ffffff @ 0.898 r 20px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | button.Eeun9Q 192.0x56.0 bg #ffffff r 20px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | button.Eeun9Q 192.0x56.0 bg #ffffff @ 0.898 r 20px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #99c8ff offset 0px | button.Eeun9Q 190.1x55.4 bg #ffffff @ 0.8 r 20px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.99, 0, 0, 0.99, 0, 0) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### tool-tab

Tool tab. A tools-showcase tab (AI / Presentations / Social / Video / Print Shop); measured unselected — the selected state is the screenshot toggle.

Page: home. Selector: `tools role=tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 213.53 x 64 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #404f6d @ 0.06 | = | #404f6d @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 3px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span._69zyRA: Canva Sans 18px/24px 600, #0f1015 | = | span._69zyRA: Canva Sans 18px/24px 600, #ffffff | span._69zyRA: Canva Sans 18px/24px 600, #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 40 x 40, colour #ff6105 | = | 40 x 40, colour #ffffff | 40 x 40, colour #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.u0WslQ 213.5x64.0 bg #404f6d @ 0.06 r 9999px | button.rAZblw.u0WslQ 213.5x64.0 image linear-gradient(98deg, #00c4cc -9%, #5a32fa 78%, #7630d7 158%) r 9999px outline 1px auto #005fcc offset 3px | button.rAZblw.u0WslQ 213.5x64.0 bg #404f6d @ 0.06 image linear-gradient(98deg, #00c4cc -9%, #5a32fa 78%, #7630d7 158%) r 9999px |
| Background image | - | = | linear-gradient(98deg, #00c4cc -9%, #5a32fa 78%, #7630d7 158%) | linear-gradient(98deg, #00c4cc -9%, #5a32fa 78%, #7630d7 158%) |

Crops: `tool-tab-default.png`, `tool-tab-hover.png`, `tool-tab-focus-visible.png`, `tool-tab-pressed.png`.

#### tool-panel

Tool panel. The tools-showcase panel under the tabs (the selected tool's artwork and copy).

Page: home. Selector: `role=tabpanel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1332 x 1063.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.iC_8gw: Canva Sans 28px/35px 500, #ffffff, ls -0.28px |
| Transition | height 0.25s ease-in-out |
| Painted layers | div._3tJw4g 850.7x519.8 image linear-gradient(#f25e07 0%, #d97218 28%, #ffc94f 100%); a 181.5x40.0 bg #ffffff @ 0.898 r 12px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset; div._3tJw4g 413.3x519.8 image linear-gradient(#ffdac4 0%, #ffdac4 0%); a 155.8x40.0 bg #ffffff @ 0.898 r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset; div._3tJw4g 413.3x519.8 image linear-gradient(#ffdac4 0%, #ffdac4 0%); a 150.4x40.0 bg #ffffff @ 0.898 r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `tool-panel-default.png`.

#### feature-card

Feature card. A dark feature card on the home page (the Magic-Layers card with an "Explore" link); the link was measured, never followed.

Page: home. Selector: `.theme.dark feature card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 850.66 x 166 | = | = | = |
| Padding | 32px 32px 0px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times New Roman 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.iC_8gw: Canva Sans 28px/35px 500, #ffffff, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a 175.3x40.0 bg #ffffff @ 0.898 r 12px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | a 175.3x40.0 bg #ffffff @ 0.898 r 12px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #99c8ff offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`, `feature-card-focus-visible.png`, `feature-card-pressed.png`.

#### explore-link

Explore link. An "Explore X" link inside a dark feature card; measured, never followed.

Page: home. Selector: `explore link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 175.28 x 40 | = | = | 173.53 x 39.6 |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff @ 0.898 | #ffffff | = | #ffffff @ 0.8 |
| Box shadow | #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #99c8ff offset 1px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | span.khPe7Q: Canva Sans 14px/22px 600, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 175.3x40.0 bg #ffffff @ 0.898 r 12px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | a 175.3x40.0 bg #ffffff r 12px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | a 175.3x40.0 bg #ffffff @ 0.898 r 12px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #99c8ff offset 1px | a 173.5x39.6 bg #ffffff @ 0.8 r 12px shadow #ffffff @ 0.08 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #000000 @ 0.25 0px -1px 0.5px 0px inset, #000000 @ 0.14 0px 1px 2px 0px, #000000 @ 0.07 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.99, 0, 0, 0.99, 0, 0) |

Crops: `explore-link-default.png`, `explore-link-hover.png`, `explore-link-focus-visible.png`, `explore-link-pressed.png`.

#### section-h2

Section heading. A section heading below the dark band (the light part of the page).

Page: home. Selector: `section h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1288 x 61.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Canva Sans 24px/32px 600 |
| Letter spacing | normal |
| Colour | #0f1015 |
| Text node | span._809hyA: Canva Sans 56px/61.6px 400, #0f1015, ls -0.56px |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Pricing

#### pricing-h1

Pricing title. The "Plans and pricing" display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Canva Sans 64px/70.4px 400 |
| Letter spacing | normal |
| Colour | #0f1015 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-tab

Plan tab. A plan-audience tab (Individuals and business / Education); keyboard focus auto-activates it, which swaps the pricing view — measured last so the tab switch cannot contaminate the other components.

Page: pricing. Selector: `plans role=tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 142.08 x 64 | = | 143.05 x 64 | 143.05 x 64 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Canva Sans 16px/24px 400, #0f1015 | = | span.nX6v3g: Canva Sans 16px/24px 600, #ffffff | span.nX6v3g: Canva Sans 16px/24px 600, #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div::before.MRLK3w._LBjXA 142.078pxx48px image linear-gradient(90deg, #476cdc, #7e2be8) r 9999px; div::after.MRLK3w._LBjXA 142.078pxx48px bg #394660 @ 0.14 r 9999px; div::before.MRLK3w._LBjXA 142.078pxx48px image linear-gradient(90deg, #476cdc, #7e2be8) r 9999px; div::after.MRLK3w._LBjXA 142.078pxx48px bg #394660 @ 0.14 r 9999px | = | span 151.0x64.0 r 8px outline 3px auto #005fcc offset -1px; div::before.MRLK3w.IpBcsg 143.047pxx48px image linear-gradient(90deg, #476cdc, #7e2be8) r 9999px; div::after.MRLK3w.IpBcsg 143.047pxx48px bg #394660 @ 0.14 r 9999px; div::before.MRLK3w.IpBcsg 143.047pxx48px image linear-gradient(90deg, #476cdc, #7e2be8) r 9999px; div::after.MRLK3w.IpBcsg 143.047pxx48px bg #394660 @ 0.14 r 9999px | div::before.MRLK3w.IpBcsg 143.047pxx48px image linear-gradient(90deg, #476cdc, #7e2be8) r 9999px; div::after.MRLK3w.IpBcsg 143.047pxx48px bg #394660 @ 0.14 r 9999px; div::before.MRLK3w.IpBcsg 143.047pxx48px image linear-gradient(90deg, #476cdc, #7e2be8) r 9999px; div::after.MRLK3w.IpBcsg 143.047pxx48px bg #394660 @ 0.14 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-tab-default.png`, `plan-tab-hover.png`, `plan-tab-focus-visible.png`, `plan-tab-pressed.png`.

#### billing-switch

Billing switch. The Monthly/Yearly billing switch next to "Save from 16%"; toggled for the billing screenshot, never checked out.

Page: pricing. Selector: `button[role=switch]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 24 | = | = | = |
| Padding | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #8b3dff | #7630d7 | = | #7630d7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 2px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Transition | background-color 0.2s linear, linear, linear delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #8b3dff | = | = | = |
| Painted layers | button 40.0x24.0 bg #8b3dff r 9999px; span 20.0x20.0 bg #ffffff r 9999px shadow #404f6d @ 0.06 0px 0px 0px 0.5px, #151e82 @ 0.12 0px 1px 2px 0px, #151e82 @ 0.06 0px 2px 4px 0px | button 40.0x24.0 bg #7630d7 r 9999px; span 20.0x20.0 bg #ffffff r 9999px shadow #404f6d @ 0.06 0px 0px 0px 0.5px, #151e82 @ 0.12 0px 1px 2px 0px, #151e82 @ 0.06 0px 2px 4px 0px | button 40.0x24.0 bg #8b3dff r 9999px outline 1px auto #005fcc offset 2px; span 20.0x20.0 bg #ffffff r 9999px shadow #404f6d @ 0.06 0px 0px 0px 0.5px, #151e82 @ 0.12 0px 1px 2px 0px, #151e82 @ 0.06 0px 2px 4px 0px | button 40.0x24.0 bg #7630d7 r 9999px; span 20.0x20.0 bg #ffffff r 9999px shadow #404f6d @ 0.06 0px 0px 0px 0.5px, #151e82 @ 0.12 0px 1px 2px 0px, #151e82 @ 0.06 0px 2px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-switch-default.png`, `billing-switch-hover.png`, `billing-switch-focus-visible.png`, `billing-switch-pressed.png`.

#### plan-card

Plan card. A pricing plan card (plan name, price in S$ — the capture was served the Singapore region — and its action).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 262 x 353 |
| Padding | 0px |
| Gap | 16px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.WyPhWw.dIH_FQ: Canva Sans 12px/20px 600, #101219 @ 0.698 |
| Transition | none |
| Icon | 16 x 16, colour #101219 @ 0.698 |
| Painted layers | button 262.0x40.0 bg #8b3dff r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. A plan card's price figure (S$ in the Singapore region the capture was served).

Page: pricing. Selector: `plan S$ figure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 63.44 x 49 |
| Padding | 0px |
| Gap | 2px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span._1dBmpQ.sGmgew: Canva Sans 28.8px/normal 500, #0f1015 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's action (Get started / Try for free / Start a free trial); measured, never followed.

Page: pricing. Selector: `plan card CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 262 x 40 | = | = | 259.38 x 39.6 |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #8b3dff | #7630d7 | = | #612dae |
| Box shadow | #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 3px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.khPe7Q: Canva Sans 14px/22px 600, #ffffff | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button 262.0x40.0 bg #8b3dff r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | button 262.0x40.0 bg #7630d7 r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | button 262.0x40.0 bg #8b3dff r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #005fcc offset 3px | button 259.4x39.6 bg #612dae r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.99, 0, 0, 0.99, 0, 0) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### feature-accordion

Feature row. A feature-comparison row in the plan table; measured closed, never expanded.

Page: pricing. Selector: `comparison row button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1286 x 64 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 14px 14px 0px 0px | = | = | = |
| Background | #394660 @ 0.14 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Times 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h4: Canva Sans 18px/24px 600, #0f1015 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #0d1216 | = | = | = |
| Painted layers | button._4l5m7w 1286.0x64.0 bg #394660 @ 0.14 r 14px 14px 0px 0px | = | button._4l5m7w 1286.0x64.0 bg #394660 @ 0.14 r 14px 14px 0px 0px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feature-accordion-default.png`, `feature-accordion-hover.png`, `feature-accordion-focus-visible.png`, `feature-accordion-pressed.png`.

### Templates

#### templates-h1

Templates title. The "Free templates" display heading.

Page: templates. Selector: `h1 on /templates`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 565.23 x 79.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Canva Sans 64px/70.4px 400 |
| Letter spacing | -0.64px |
| Colour | #0f1015 |
| Transition | none |
| Painted layers | div.su2OzQ._8P8IGw 61.3x61.3 image linear-gradient(#c23dcf, #63046c) border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 12px shadow #182c59 @ 0.07 0px 0px 0px 0.5px; div.su2OzQ.KCtSjQ 61.3x61.3 image linear-gradient(#a21caf 0%, #63046c 100%) border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 12px shadow #182c59 @ 0.07 0px 0px 0px 0.5px |
| How | at rest |

Crops: `templates-h1-default.png`.

#### search-field

Search field. The "Search templates" input; focused only — typing was never sent so no live query ran.

Page: templates. Selector: `input[type=search]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 323 x 46 | = |
| Padding | 0px 0px 1px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff @ 0 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Canva Sans 14px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #0f1015 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #131620 @ 0.6, opacity 1 | = |
| Painted layers | input.LMU2Kg 323.0x46.0 bg #ffffff @ 0 | = |
| Ancestor paint | 1 up div._bpG9Q bg #ffffff | = |
| How | at rest | clicked into the field |

Crops: `search-field-default.png`, `search-field-focused.png`.

#### category-card

Category card. A template-category card (image tile + label linking /presentations/templates/ etc.); measured, never followed.

Page: templates. Selector: `a[href$="/templates/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 240 x 80 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 16px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #005fcc offset -3px | = |
| Font | Times 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 240.0x80.0 r 16px outline 3px auto #005fcc offset -3px | = |

Crops: `category-card-default.png`, `category-card-hover.png`, `category-card-focus-visible.png`, `category-card-pressed.png`.

### Login and signup

#### auth-card

Auth card. The sign-in card (Continue with Google / Facebook / email / another way + terms); captured, never used.

Page: login. Selector: `auth card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304 x 348 |
| Padding | 0px |
| Gap | 16px normal |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3: Canva Sans 24px/32px 600, #0f1015 |
| Transition | none |
| Icon | 24 x 24, colour #0f1015, fill #000000 |
| Painted layers | button.w_WokQ._7IvJg 304.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset; button.HvfyOw._7IvJg 304.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset; button.COAWQQ._7IvJg 304.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset; button.ZRijrQ 304.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `auth-card-default.png`.

#### oauth-button

OAuth button. The "Continue with Google" action; measured, never pressed — it would leave for the OAuth flow.

Page: login. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 304 x 40 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0f1015 @ 0 | #404f6d @ 0.06 | = | #394660 @ 0.14 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | p: Canva Sans 14px/22px 600, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #0f1015, fill #000000 | = | = | = |
| Painted layers | button.w_WokQ._7IvJg 304.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | button.w_WokQ._7IvJg 304.0x40.0 bg #404f6d @ 0.06 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | button.w_WokQ._7IvJg 304.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset outline 1px auto #005fcc offset 0px | button.w_WokQ._7IvJg 304.0x40.0 bg #394660 @ 0.14 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-button-default.png`, `oauth-button-hover.png`, `oauth-button-focus-visible.png`, `oauth-button-pressed.png`.

#### email-continue

Email continue. The "Continue with email" action that reveals the email form; pressed once below to open that form (a local step, still signed out).

Page: login. Selector: `Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 304 x 40 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0f1015 @ 0 | #404f6d @ 0.06 | = | #394660 @ 0.14 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | p: Canva Sans 14px/22px 600, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #0f1015, fill #000000 | = | = | = |
| Painted layers | button.COAWQQ._7IvJg 304.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | button.COAWQQ._7IvJg 304.0x40.0 bg #404f6d @ 0.06 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | button.COAWQQ._7IvJg 304.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset outline 1px auto #005fcc offset 0px | button.COAWQQ._7IvJg 304.0x40.0 bg #394660 @ 0.14 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `email-continue-default.png`, `email-continue-hover.png`, `email-continue-focus-visible.png`, `email-continue-pressed.png`.

#### username-input

Email field. The email/username input revealed by "Continue with email"; focused and given sample text that was deleted again — nothing sent.

Page: login. Selector: `input[name=username]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 278 x 38 | = | = |
| Padding | 0px 0px 1px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff @ 0 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Canva Sans 14px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0f1015 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #0f1015, opacity 1 | = | = |
| Painted layers | input.LMU2Kg 278.0x38.0 bg #ffffff @ 0 | = | = |
| Ancestor paint | 1 up div.f4qJng.fs-hide bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `username-input-default.png`, `username-input-focused.png`, `username-input-filled.png`.

#### continue-button

Continue button. The email form's Continue action; measured, never pressed.

Page: login. Selector: `form Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 304 x 40 | = | = | 300.96 x 39.6 |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #8b3dff | #7630d7 | = | #612dae |
| Box shadow | #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 3px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.khPe7Q: Canva Sans 14px/22px 600, #ffffff | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.a2l15A 304.0x40.0 bg #8b3dff r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | button.a2l15A 304.0x40.0 bg #7630d7 r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset | button.a2l15A 304.0x40.0 bg #8b3dff r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #005fcc offset 3px | button.a2l15A 301.0x39.6 bg #612dae r 12px shadow #ffffff @ 0.16 0px 24px 24px -18px inset, #ffffff @ 0.25 0px 1px 0.5px 0px inset, #151e82 @ 0.12 0px -1px 0.5px 0px inset, #151e82 @ 0.07 0px 1px 2px 0px, #151e82 @ 0.03 0px 3px 4px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.99, 0, 0, 0.99, 0, 0) |

Crops: `continue-button-default.png`, `continue-button-hover.png`, `continue-button-focus-visible.png`, `continue-button-pressed.png`.

### Footer

#### footer

Footer. The footer: download links, the Product/Plans/About columns, social icons and legal.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1420 |
| Padding | 48px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#000000 @ 0, #f6f7f8) |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.KC3q2Q: Canva Sans 16px/22.4px 500, #0f1015 @ 0.85 |
| Transition | none |
| Icon | 0 x 0, colour #0f1015 |
| Painted layers | footer.STbrdg.wZ3rOA 1440.0x1420.0 image linear-gradient(#000000 @ 0, #f6f7f8); a 93.5x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset; a 80.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset; button 0.0x0.0 bg #0f1015 @ 0 r 12px; a.Y6IZ1Q.yAP2vQ 0.0x0.0 bg #0f1015 @ 0 r 12px; a.Y6IZ1Q.yAP2vQ 0.0x0.0 bg #0f1015 @ 0 r 12px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.47 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0f1015 @ 0 | #404f6d @ 0.06 | = | #394660 @ 0.14 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | span.khPe7Q: Canva Sans 14px/22px 600, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a 93.5x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | a 93.5x40.0 bg #404f6d @ 0.06 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | a 93.5x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset outline 1px auto #005fcc offset 1px | a 93.5x40.0 bg #394660 @ 0.14 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #0f1015 @ 0 | #404f6d @ 0.06 | = | #394660 @ 0.14 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #0f1015, fill #000000 | = | = | = |
| Painted layers | a 32.0x32.0 bg #0f1015 @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset | a 32.0x32.0 bg #404f6d @ 0.06 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset | a 32.0x32.0 bg #0f1015 @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #005fcc offset 1px | a 32.0x32.0 bg #394660 @ 0.14 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.khPe7Q: Canva Sans 14px/22px 500, #0f1015 |
| Transition | none |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | button 32.0x32.0 bg #ffffff @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset; button.n156ng 0.0x0.0 bg #ffffff @ 0 r 12px; button.n156ng 0.0x0.0 bg #ffffff @ 0 r 12px; button.n156ng 0.0x0.0 bg #ffffff @ 0 r 12px; button.n156ng 0.0x0.0 bg #ffffff @ 0 r 12px; button.n156ng 0.0x0.0 bg #ffffff @ 0 r 12px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The "Open navigation menu" burger toggle.

Page: mobile. Selector: `button[aria-label*=navigation menu]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px 8px |
| Border | none |
| Radius | 10px |
| Background | #ffffff @ 0 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| Outline | none |
| Font | Canva Sans 14px/22px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease |
| Cursor | pointer |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | button 32.0x32.0 bg #ffffff @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The opened mobile navigation panel (the fixed overlay holding the menu links and the auth actions).

Page: mobile. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Canva Sans 21px/26px 500, #0f1015 |
| Transition | none |
| Icon | 24 x 24, colour #0f1015, fill #000000 |
| ::after | 1px x 1px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div._aTIuw 346.0x844.0 bg #ffffff shadow #404f6d @ 0.06 0px 0px 0px 0.5px, #151e82 @ 0.12 0px 8px 16px 0px, #151e82 @ 0.06 0px 24px 24px 0px; div.cLOwww 346.0x144.0 bg #cce1ff; div._46qB5w 346.0x144.0 bg #e7dbff; div._6Tlurw 346.0x144.0 bg #ffffff; button 32.0x32.0 bg #0f1015 @ 0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset; button.Yx3HJA 322.0x42.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A row inside the opened mobile menu (Design / Product / Plans / Business / Education / Help).

Page: mobile. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 322 x 42 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0f1015 @ 0 | = | = | #394660 @ 0.14 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | span: Canva Sans 21px/26px 500, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 21.61 x 24, colour #0f1015 | = | = | = |
| Painted layers | button.Yx3HJA 322.0x42.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset | = | button.Yx3HJA 322.0x42.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset outline 1px auto #e59700 offset 0px | button.Yx3HJA 322.0x42.0 bg #394660 @ 0.14 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-signup

Mobile sign-up. The Sign up action inside the mobile menu; measured, never followed.

Page: mobile. Selector: `mobile menu Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 322 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0f1015 @ 0 | = | = | #394660 @ 0.14 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Canva Sans 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0f1015 | = | = | = |
| Text node | span.khPe7Q: Canva Sans 14px/22px 500, #0f1015 | = | = | = |
| Transition | background-color, box-shadow, color, transform 0.1s, 0.1s, 0.1s, 0.07s linear, linear, linear, ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.UB5XWg 322.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset | = | a.UB5XWg 322.0x40.0 bg #0f1015 @ 0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset outline 1px auto #e59700 offset 1px | a.UB5XWg 322.0x40.0 bg #394660 @ 0.14 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #35415a @ 0.2 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-signup-default.png`, `m-signup-hover.png`, `m-signup-focus-visible.png`, `m-signup-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 270 x 148.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Canva Sans 21px/26px 600 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.898 |
| Text node | span.dIH_FQ: Canva Sans 45px/49.5px 400, #ffffff, ls -0.45px |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

canva.com serves its StyleX bundles cross-origin from static.canva.com, so the readable CSSOM holds only the inline styles; this list covers the transition rules the page itself exposes, and the per-state Transition rows above are the computed values the page paints.

- home: `opacity var(--n59-HQ) ease-in-out, transform var(--n59-HQ) ease-in-out`, `opacity 0.25s, box-shadow 0.1s linear`, `transform 0.2s`, `background-color 0.2s ease-in-out`, `transform 0.2s ease-in-out`, `background-color 0.2s cubic-bezier(0.68, 0, 0.23, 1)`, `opacity 0.3s linear`, `transform 0.2s ease-out`, `opacity 0.2s linear 10ms`, `color 0.2s`, `transform 0.65s cubic-bezier(0, 0, 0.13, 1), opacity 0.65s cubic-bezier(0, 0, 0.13, 1)`, `opacity 0.65s cubic-bezier(0, 0, 0.13, 1)`

- login: `opacity var(--n59-HQ) ease-in-out, transform var(--n59-HQ) ease-in-out`, `box-shadow 0.16s`, `transform 0.2s`, `background-color 0.2s ease-in-out`, `transform 0.2s ease-in-out`, `transform 0.2s ease-out, box-shadow 0.2s ease-out`, `transform 0.25s cubic-bezier(0, 0, 0.2, 1)`, `transform 0.2s cubic-bezier(0.4, 0, 1, 1)`, `opacity 0.15s ease-in-out`, `none`, `opacity 0.3s ease-in-out`, `background-color 0.1s linear`

- pricing: `opacity 0.2s linear 10ms`, `opacity 0.25s, box-shadow 0.1s linear`, `transform 0.2s`, `background-color 0.2s ease-in-out`, `transform 0.2s ease-in-out`, `height 0.1s ease-in`, `background-color 80ms ease-in, box-shadow 80ms ease-in`, `opacity 80ms ease-in`, `opacity 0.25s ease-in 0.166s`, `opacity 0.25s ease-in-out`, `opacity var(--n59-HQ) ease-in-out, transform var(--n59-HQ) ease-in-out`, `color 0.2s`

- templates: `opacity var(--n59-HQ) ease-in-out, transform var(--n59-HQ) ease-in-out`, `opacity 0.25s, box-shadow 0.1s linear`, `transform 0.2s`, `background-color 0.2s ease-in-out`, `transform 0.2s ease-in-out`, `color 0.2s`, `background-color 0.1s linear`, `color 0.1s ease-in-out`, `transform 0.18s cubic-bezier(0.2, 0, 0, 1)`, `grid-template-rows 0.3s cubic-bezier(0, 0, 0.2, 1), opacity 0.3s cubic-bezier(0, 0, 0.2, 1)`, `opacity 0.15s ease-in-out`, `box-shadow 0.2s, transform 0.1s`
