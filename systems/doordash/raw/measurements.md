# Component measurements

Computed styles read from www.doordash.com pages rendered from Internet Archive snapshots on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). Live *.doordash.com Cloudflare-blocks this capture client, so every reading is archival evidence from the product's own SSR pages (routes and snapshot ids in [archive-urls.json](archive-urls.json)) — not a live capture. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### App shell and navigation

#### logo

Wordmark. The DoorDash wordmark anchor (svg + visually-hidden label).

Page: home. Selector: `wordmark anchor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 170.7 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Text-sc-yxnz5n-0.sc-6c4a270f-13: DD Norms 14px/20px 500, #c4c4c4, ls -0.01px |
| Transition | filter 0.2s ease |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### signin-btn

Sign-in button. kind="BUTTON/PRIMARY" anchor to identity.doordash.com; measured, never followed.

Page: home. Selector: `[data-testid=signInButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82.44 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #eb1700 | #d91400 | = | #b71000 |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Text-sc-yxnz5n-0.huQgjs: DD Norms 18px/22px 800, #ffffff, ls -0.2px | = | = | = |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Painted layers | a.ButtonRoot-sc-j2wkqj-0.iLCINK 82.4x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | a.ButtonRoot-sc-j2wkqj-0.iLCINK 82.4x40.0 bg #d91400 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | a.ButtonRoot-sc-j2wkqj-0.iLCINK 82.4x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset outline 1px auto #005fcc offset 1px | a.ButtonRoot-sc-j2wkqj-0.iLCINK 82.4x40.0 bg #b71000 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-btn-default.png`, `signin-btn-hover.png`, `signin-btn-focus-visible.png`, `signin-btn-pressed.png`.

#### signup-btn

Sign-up button. kind="BUTTON/PLAIN" red pill to the signup URL; measured, never followed.

Page: home. Selector: `[data-testid=signUpButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.55 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191919 | #242424 | = | #313131 |
| Text node | span.Text-sc-yxnz5n-0.bkWmod: DD Norms 18px/22px 800, #606060, ls -0.2px | = | = | = |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Painted layers | a.ButtonRoot-sc-j2wkqj-0.iLCINK 90.5x40.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | = | a.ButtonRoot-sc-j2wkqj-0.iLCINK 90.5x40.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-btn-default.png`, `signup-btn-hover.png`, `signup-btn-focus-visible.png`, `signup-btn-pressed.png`.

#### language-select

Language select. The footer/top-bar native <select> of locales (data-size="small").

Page: home. Selector: `[data-testid=LanguageDropdown]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 94 x 20 | = |
| Padding | 0px 24px 0px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f1f1f1 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | DD Norms 14px/20px 500 | = |
| Letter spacing | -0.01px | = |
| Colour | #191919 | = |
| Transition | none | = |
| Cursor | default | = |
| Painted layers | select.SelectElementContent-sc-5yzsia-3.fnohMZ 94.0x20.0 bg #f1f1f1 | = |
| Ancestor paint | 1 up div.SelectContainer-sc-1wilwzz-0.khtfio bg #f1f1f1; 3 up div.InputContainer-sc-5yzsia-1.futmdp bg #f1f1f1 shadow #e4e4e4 0px 0px 0px 1px inset | 1 up div.SelectContainer-sc-1wilwzz-0.khtfio bg #f1f1f1; 3 up div.InputContainer-sc-5yzsia-1.futmdp bg #f1f1f1 shadow #191919 0px 0px 0px 2px inset |
| How | at rest | clicked into the field |

Crops: `language-select-default.png`, `language-select-focused.png`.

#### app-header

App header. The consumer app shell header — HomeLogo, address button, side-nav toggle, cart and bell.

Page: dashpass. Selector: `[data-testid=Header]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 64px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Text-sc-yxnz5n-0.gqHgNr: DD Norms 14px/20px 700, #191919, ls -0.01px |
| Transition | none |
| Icon | 32 x 18, colour #0000ee, fill #eb1700 |
| Painted layers | div.sc-51f7ae22-5.CiCuB 1440.0x0.0 bg #ffffff; div.sc-51f7ae22-6.jtIgLU 1440.0x64.0 bg #ffffff border B:1px solid #e4e4e4; div.sc-51f7ae22-8.icwqCe 152.0x18.0 image linear-gradient(90deg, #ffffff @ 0 0%, #ffffff 5%, #ffffff 50%, #ffffff 95%, #ffffff @ 0 1; button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 150.3x32.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset; button.ButtonRootInternal-sc-j2wkqj-0.dxDIIR 32.0x32.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset; button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 57.7x32.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest |

Crops: `app-header-default.png`.

#### app-logo

App wordmark.

Page: dashpass. Selector: `[data-testid=HomeLogo]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 152 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(90deg, #ffffff @ 0 0%, #ffffff 5%, #ffffff 50%, #ffffff 95%, #ffffff @ 0 100%) |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 32 x 18, colour #0000ee, fill #eb1700 |
| Painted layers | div.sc-51f7ae22-8.icwqCe 152.0x18.0 image linear-gradient(90deg, #ffffff @ 0 0%, #ffffff 5%, #ffffff 50%, #ffffff 95%, #ffffff @ 0 1 |
| How | at rest |

Crops: `app-logo-default.png`.

#### address-btn

Address button. The header address/destination control — an address gate, never pressed.

Page: dashpass. Selector: `[data-testid=addressTextButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150.27 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #f1f1f1 | #d6d6d6 | = | #c4c4c4 |
| Box shadow | #f1f1f1 0px 0px 0px 1px inset | #d6d6d6 0px 0px 0px 1px inset | = | #c4c4c4 0px 0px 0px 1px inset |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191919 | #242424 | = | #313131 |
| Text node | span.Text-sc-yxnz5n-0.gqHgNr: DD Norms 14px/20px 700, #191919, ls -0.01px | = | = | = |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Icon | 16 x 24, colour #191919 | 16 x 24, colour #242424 | = | 16 x 24, colour #313131 |
| Painted layers | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 150.3x32.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 150.3x32.0 bg #d6d6d6 r 9999px shadow #d6d6d6 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 150.3x32.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset outline 1px auto #005fcc offset 0px | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 150.3x32.0 bg #c4c4c4 r 9999px shadow #c4c4c4 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `address-btn-default.png`, `address-btn-hover.png`, `address-btn-focus-visible.png`, `address-btn-pressed.png`.

#### sidenav-toggle

Side-nav toggle. The hamburger that opens the side navigation; toggled on mobile only.

Page: dashpass. Selector: `[data-testid=side-nav] / hamburger`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 221 x 836 |
| Padding | 0px |
| Border | T: none; R: 1px solid #e4e4e4; B: none; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Text-sc-yxnz5n-0.StyledText-sc-4qjl8j-0: DD Norms 14px/20px 500, #191919, ls -0.01px |
| Transition | box-shadow 0.225s cubic-bezier(0.83, 0, 0.17, 1) |
| Icon | 24 x 24, colour #0000ee |
| Painted layers | div.sc-71aa3b15-0.dJJlEa 221.0x836.0 bg #ffffff border R:1px solid #e4e4e4; a.sc-db8c6f48-0.jalJCf 196.0x40.0 bg #ffffff r 8px; div.sc-5f6dc190-3.cNQfXQ 24.0x24.0 bg #e7e7e7 r 50%; a.sc-db8c6f48-0.jalJCf 196.0x40.0 bg #ffffff r 8px; div.sc-5f6dc190-4.gyEGLc 24.0x24.0 bg #191919; a.sc-db8c6f48-0.jalJCf 196.0x40.0 bg #ffffff r 8px |
| How | at rest |

Crops: `sidenav-toggle-default.png`.

#### cart-btn

Cart button. The header cart (icon button with badge); measured, never pressed.

Page: dashpass. Selector: `[data-testid=OrderCartIconButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.66 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #eb1700 | #d91400 | = | #b71000 |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: DD Norms 14px/20px 700, #ffffff, ls -0.01px | = | = | = |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 57.7x32.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 57.7x32.0 bg #d91400 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 57.7x32.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset outline 1px auto #005fcc offset 0px | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 57.7x32.0 bg #b71000 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-btn-default.png`, `cart-btn-hover.png`, `cart-btn-focus-visible.png`, `cart-btn-pressed.png`.

#### bell-btn

Bell button. The header notifications bell; measured, never pressed.

Page: dashpass. Selector: `[data-testid=NotificationBell]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 32 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Times 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #191919 | 24 x 24, colour #242424 | - | = |
| Painted layers | button.ButtonRootInternal-sc-j2wkqj-0.dxDIIR 32.0x32.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.dxDIIR 32.0x32.0 bg #d6d6d6 r 9999px shadow #d6d6d6 0px 0px 0px 1px inset | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `bell-btn-default.png`, `bell-btn-hover.png`, `bell-btn-pressed.png`.

#### hero-band

Hero band. The marketing hero region the top bar floats on: wordmark, Sign in and Sign Up over the campaign field (the bar has no separate paint).

Page: home. Selector: `painted ancestor of [data-testid=signInButton] (the hero)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 650 |
| Padding | 0px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.Text-sc-yxnz5n-0.sc-4e5f74df-13: TTNormsProCond-Blk 40px/40px 900, #ffffff, ls -0.8px |
| Transition | none |
| Icon | 42 x 24, colour #000000, fill #ffffff |
| Painted layers | a.ButtonRoot-sc-j2wkqj-0.iLCINK 82.4x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset; a.ButtonRoot-sc-j2wkqj-0.iLCINK 90.5x40.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset; button.ButtonRoot-sc-j2wkqj-0.jcvtZg 204.5x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px; button.ButtonRoot-sc-j2wkqj-0.jcvtZg 179.8x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px |
| How | at rest |

Crops: `hero-band-default.png`.

### Marketing hero

#### hero-title

Hero headline. The campaign h1 — TTNormsProCond-Blk 900, uppercase.

Page: home. Selector: `[data-testid=HomePageHeroHeader]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 646.88 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TTNormsProCond-Blk 40px/40px 900 |
| Letter spacing | -0.8px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subcopy. The line under the hero headline ("Other fees apply").

Page: home. Selector: `span under HomePageHeroHeader`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 92.69 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD Norms 12px/22px 600 |
| Letter spacing | -0.01px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### address-pill

Address pill (sign-in gate). The "Sign in for saved address" hero pill — an authentication gate, never pressed.

Page: home. Selector: `hero pill "Sign in for saved address"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204.55 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191919 | #242424 | = | #313131 |
| Text node | span.Text-sc-yxnz5n-0.lajzwX: DD Norms 14px/20px 700, #191919, ls -0.01px | span.Text-sc-yxnz5n-0.lajzwX: DD Norms 14px/20px 700, #242424, ls -0.01px | = | span.Text-sc-yxnz5n-0.lajzwX: DD Norms 14px/20px 700, #313131, ls -0.01px |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Icon | 16 x 24, colour #191919 | 16 x 24, colour #242424 | = | 16 x 24, colour #313131 |
| Painted layers | button.ButtonRoot-sc-j2wkqj-0.jcvtZg 204.5x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px | = | button.ButtonRoot-sc-j2wkqj-0.jcvtZg 204.5x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `address-pill-default.png`, `address-pill-hover.png`, `address-pill-focus-visible.png`, `address-pill-pressed.png`.

#### location-pill

Location pill. The "Use current Location" hero pill — a geolocation prompt, never pressed.

Page: home. Selector: `hero pill "Use current Location"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 179.81 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191919 | #242424 | = | #313131 |
| Text node | span.Text-sc-yxnz5n-0.lajzwX: DD Norms 14px/20px 700, #191919, ls -0.01px | span.Text-sc-yxnz5n-0.lajzwX: DD Norms 14px/20px 700, #242424, ls -0.01px | = | span.Text-sc-yxnz5n-0.lajzwX: DD Norms 14px/20px 700, #313131, ls -0.01px |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Icon | 16 x 24, colour #191919 | 16 x 24, colour #242424 | = | 16 x 24, colour #313131 |
| Painted layers | button.ButtonRoot-sc-j2wkqj-0.jcvtZg 179.8x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px | = | button.ButtonRoot-sc-j2wkqj-0.jcvtZg 179.8x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `location-pill-default.png`, `location-pill-hover.png`, `location-pill-focus-visible.png`, `location-pill-pressed.png`.

### CTA bands and cards

#### cta-band

CTA band. A mid-page CTA section (CTASplash) — tinted band with headline, copy and a primary action.

Page: home. Selector: `[data-testid=CTASplash]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 600 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.Text-sc-yxnz5n-0.sc-45188105-8: DD Norms 40px/40px 800, #ffffff, ls -0.8px |
| Transition | none |
| Painted layers | div.sc-45188105-25.cDyXaW 1440.0x600.0 bg #1e1e1e @ 0.6; a.ButtonRoot-sc-j2wkqj-0.iLCINK 138.4x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest |

Crops: `cta-band-default.png`.

#### cta-band-title

CTA band headline.

Page: home. Selector: `[data-testid=CTAContentHeader]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 240.97 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD Norms 40px/40px 800 |
| Letter spacing | -0.8px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `cta-band-title-default.png`.

#### cta-band-copy

CTA band copy.

Page: home. Selector: `[data-testid=CTAContentDescription]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 267.75 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD Norms 16px/22px 500 |
| Letter spacing | -0.01px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `cta-band-copy-default.png`.

#### cta-btn

CTA button. kind="BUTTON/PRIMARY" red pill in the CTA band; measured, never followed.

Page: home. Selector: `[data-testid=CTAContentCTAButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145.42 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #eb1700 | #d91400 | = | #b71000 |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Text-sc-yxnz5n-0.iXwtTf: DD Norms 16px/22px 700, #ffffff, ls -0.01px | = | = | = |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Painted layers | a.ButtonRoot-sc-j2wkqj-0.iLCINK 145.4x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | a.ButtonRoot-sc-j2wkqj-0.iLCINK 145.4x40.0 bg #d91400 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | a.ButtonRoot-sc-j2wkqj-0.iLCINK 145.4x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset outline 1px auto #005fcc offset 1px | a.ButtonRoot-sc-j2wkqj-0.iLCINK 145.4x40.0 bg #b71000 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-btn-default.png`, `cta-btn-hover.png`, `cta-btn-focus-visible.png`, `cta-btn-pressed.png`.

#### value-prop-card

Value-prop card. A "Become a Dasher"-style card: illustration, heading, copy and a link.

Page: home. Selector: `[data-testid=value-prop-card-wrapper]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 410 | = | = | = |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h2.Text-sc-yxnz5n-0.sc-aa1b7056-0: DD Norms 32px/40px 800, #191919, ls -0.8px | = | = | = |
| Transition | none | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `value-prop-card-default.png`, `value-prop-card-hover.png`, `value-prop-card-focus-visible.png`, `value-prop-card-pressed.png`.

#### card-cta

Card CTA. The arrow/action inside a value-prop card.

Page: home. Selector: `[data-testid=card-cta-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 250 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.Text-sc-yxnz5n-0.sc-27837b95-1: DD Norms 14px/20px 700, #eb1700, ls -0.01px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-cta-default.png`, `card-cta-hover.png`, `card-cta-focus-visible.png`, `card-cta-pressed.png`.

#### biz-h1

Business hero. The DoorDash for Business headline.

Page: business. Selector: `h1 on /en-US/business/`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD-TTNorms 40px/normal 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Ancestor paint | 1 up div.sc-c8323bc1-0.hOMVEt bg #e6ebfd |
| How | at rest |

Crops: `biz-h1-default.png`.

#### biz-cta

Business CTA. The business page primary action; measured, never followed.

Page: business. Selector: `business page CTA`. States: .

Not found on the page at capture time.

#### biz-merchant

Merchant link. A merchant-name entry in the business directory lists.

Page: business. Selector: `merchant entry`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 211.41 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD Norms 16px/40px 500 |
| Letter spacing | -0.01px |
| Colour | #191919 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `biz-merchant-default.png`.

#### dp-h1

DashPass headline. The DashPass student page headline.

Page: dashpass. Selector: `h1 on /en-US/dashpass/student`. States: .

Not found on the page at capture time.

#### dp-cta

DashPass CTA. A DashPass signup action; measured, never followed (signup gated).

Page: dashpass. Selector: `dashpass CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 196 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f7f7f7 | = | #f1f1f1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.Text-sc-yxnz5n-0.StyledText-sc-4qjl8j-0: DD Norms 14px/20px 500, #191919, ls -0.01px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| Painted layers | button.FrameElement-sc-1cj8rsf-2.QEeom 196.0x40.0 bg #ffffff r 8px | button.FrameElement-sc-1cj8rsf-2.QEeom 196.0x40.0 bg #f7f7f7 r 8px | button.FrameElement-sc-1cj8rsf-2.QEeom 196.0x40.0 bg #ffffff r 8px outline 1px auto #005fcc offset 0px | button.FrameElement-sc-1cj8rsf-2.QEeom 196.0x40.0 bg #f1f1f1 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dp-cta-default.png`, `dp-cta-hover.png`, `dp-cta-focus-visible.png`, `dp-cta-pressed.png`.

### Directory lists and tabs

#### section-title

Section title. A "Get more from your neighborhood" h2.

Page: home. Selector: `h2 section title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1130 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD Norms 32px/40px 800 |
| Letter spacing | -0.8px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### tab-selected

Directory tab, selected. The selected tab (Top Cities) — 3px bottom border in the selected colour.

Page: home. Selector: `[role=tab][data-testid$=-selected]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376.63 x 40 | = | - | = |
| Padding | 0px | = | - | = |
| Border | T: none; R: none; B: 3px solid #191919; L: none | = | - | = |
| Radius | 0px | = | - | = |
| Background | #ffffff | #f7f7f7 | - | #f7f7f7 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Times 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.i3ez6m5: DD Norms 16px/22px 700, #191919, ls -0.01px | = | - | = |
| Transition | background-color, box-shadow 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | - | = |
| Painted layers | div.s2g7gtm 376.6x40.0 bg #ffffff border B:3px solid #191919 | div.s2g7gtm 376.6x40.0 bg #f7f7f7 border B:3px solid #191919 | - | div.s2g7gtm 376.6x40.0 bg #f7f7f7 border B:3px solid #191919 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Cursor | - | pointer | = | pointer |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `tab-selected-default.png`, `tab-selected-hover.png`, `tab-selected-pressed.png`.

#### tab-idle

Directory tab, idle. An idle tab (Top Cuisines / Top Chains).

Page: home. Selector: `[role=tab][data-testid$=-not-selected]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376.63 x 40 | = | - | = |
| Padding | 0px | = | - | = |
| Border | T: none; R: none; B: 2px solid #e4e4e4; L: none | = | - | = |
| Radius | 0px | = | - | = |
| Background | #ffffff | #f7f7f7 | - | #f7f7f7 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Times 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.i3ez6m5: DD Norms 16px/22px 500, #606060, ls -0.01px | = | - | = |
| Transition | background-color, box-shadow 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | - | = |
| Painted layers | div.s2g7gtm 376.6x40.0 bg #ffffff border B:2px solid #e4e4e4 | div.s2g7gtm 376.6x40.0 bg #f7f7f7 border B:2px solid #e4e4e4 | - | div.s2g7gtm 376.6x40.0 bg #f7f7f7 border B:2px solid #e4e4e4 |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Cursor | - | pointer | = | pointer |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `tab-idle-default.png`, `tab-idle-hover.png`, `tab-idle-pressed.png`.

#### dir-link

Directory link. A city/cuisine/chain link in the tabbed directory lists.

Page: home. Selector: `directory a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.16 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.i3ez6m5: DD Norms 16px/22px 500, #191919, ls -0.01px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.c1gxzxj 90.2x22.0 outline 1px auto #005fcc offset 1px | = |

Crops: `dir-link-default.png`, `dir-link-hover.png`, `dir-link-focus-visible.png`, `dir-link-pressed.png`.

#### show-more

Show-more toggle. The expand/collapse control on a directory list; measured, not pressed here (toggled in the shot pass).

Page: home. Selector: `[data-testid=rest-items-toggle]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1130 x 60 | = | = | = |
| Padding | 10px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.t1xxdzwp.i3ez6m5: DD Norms 20px/24px 800, #191919, ls -0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #191919 | = | = | = |
| Painted layers | button.b11usoxu 40.0x40.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset | = | button.b11usoxu 40.0x40.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `show-more-default.png`, `show-more-hover.png`, `show-more-focus-visible.png`, `show-more-pressed.png`.

#### cross-link

Cross link. A cross-category link tile (e.g. grocery → convenience).

Page: home. Selector: `[data-testid=cross-link-anchor]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.16 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.i3ez6m5: DD Norms 16px/22px 500, #191919, ls -0.01px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.c1gxzxj 90.2x22.0 outline 1px auto #005fcc offset 1px | = |

Crops: `cross-link-default.png`, `cross-link-hover.png`, `cross-link-focus-visible.png`, `cross-link-pressed.png`.

#### fd-h1

Page title. The food-delivery page headline.

Page: food-delivery. Selector: `h1 on /food-delivery/`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 460 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD-TTNorms 32px/40px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Ancestor paint | 1 up div.StyledStackChildren-sc-1cimee4-0.evYmEf bg #ffffff |
| How | at rest |

Crops: `fd-h1-default.png`.

#### city-link

City link. A city directory entry (per-city data-testid); measured, never followed.

Page: food-delivery. Selector: `city link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.39 x 40 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | DD Norms 16px/40px 500 | = | - | = |
| Letter spacing | -0.01px | = | - | = |
| Colour | #191919 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `city-link-default.png`, `city-link-hover.png`, `city-link-pressed.png`.

#### fd-faq

FAQ block. The SEO FAQ accordion block, if published on this route.

Page: food-delivery. Selector: `seo-faq-block`. States: .

Not found on the page at capture time.

### Restaurant directory

#### rest-card

Restaurant card. A restaurant tile: image, name, rating/ETA and an offer badge.

Page: restaurants. Selector: `a[href*=/store/] ancestor with img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 447.98 x 274 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Text-sc-yxnz5n-0.sc-2f781850-19: DD Norms 16px/22px 700, #191919, ls -0.01px |
| Transition | none |
| Icon | 12 x 12, colour #606060 |
| Painted layers | div.sc-ab0469c2-0.QkeXV 448.0x172.0 bg #f7f7f7 r 12px; div.TagWrapperInternal-sc-1l2oqbc-2.eYQCgy 118.3x20.0 bg #f1f1f1 r 9999px shadow #f7f7f7 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `rest-card-default.png`.

#### rest-card-title

Card title.

Page: restaurants. Selector: `a[href*=/store/] with text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 447.98 x 94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | span.Text-sc-yxnz5n-0.sc-2f781850-19: DD Norms 16px/22px 700, #191919, ls -0.01px |
| Transition | none |
| Cursor | pointer |
| Icon | 12 x 12, colour #606060 |
| Painted layers | div.TagWrapperInternal-sc-1l2oqbc-2.eYQCgy 118.3x20.0 bg #f1f1f1 r 9999px shadow #f7f7f7 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `rest-card-title-default.png`.

#### rest-card-sub

Card subtitle. The rating · ETA · fee line under the restaurant name (a single styled leaf of the row).

Page: restaurants. Selector: `rating/ETA leaf under a card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 38.38 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD Norms 14px/20px 500 |
| Letter spacing | -0.01px |
| Colour | #606060 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `rest-card-sub-default.png`.

#### offer-badge

Offer badge. A promo chip on a restaurant card ("20% off on $40+").

Page: restaurants. Selector: `[data-testid^=offer:]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 109.17 x 20 |
| Padding | 0px 8px |
| Border | none |
| Radius | 9999px |
| Background | #fff0ed |
| Box shadow | #f7f7f7 @ 0 0px 0px 0px 0px inset |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | span.Text-sc-yxnz5n-0.YTkSD: DD Norms 12px/18px 700, #d91400, ls -0.01px |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.TagWrapperInternal-sc-1l2oqbc-2.lozNJK 109.2x20.0 bg #fff0ed r 9999px shadow #f7f7f7 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `offer-badge-default.png`.

#### leaderboard-badge

Leaderboard badge. A "Top 10%"-style tag on a restaurant card.

Page: restaurants. Selector: `[data-testid^=top_rated_leaderboard]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 118.33 x 20 |
| Padding | 0px 8px |
| Border | none |
| Radius | 9999px |
| Background | #f1f1f1 |
| Box shadow | #f7f7f7 @ 0 0px 0px 0px 0px inset |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | span.Text-sc-yxnz5n-0.gFyiPO: DD Norms 12px/18px 700, #191919, ls -0.01px |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #0000ee |
| Painted layers | div.TagWrapperInternal-sc-1l2oqbc-2.eYQCgy 118.3x20.0 bg #f1f1f1 r 9999px shadow #f7f7f7 @ 0 0px 0px 0px 0px inset |
| How | at rest |

Crops: `leaderboard-badge-default.png`.

#### popular-btn

Popular-items button.

Page: restaurants. Selector: `[data-testid=PopularItemsButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.14 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #191919 @ 0 | = | = | = |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191919 | #242424 | = | #313131 |
| Text node | span.Text-sc-yxnz5n-0.gRUsPU: DD Norms 14px/20px 700, #191919, ls -0.01px | span.Text-sc-yxnz5n-0.gRUsPU: DD Norms 14px/20px 700, #242424, ls -0.01px | = | span.Text-sc-yxnz5n-0.gRUsPU: DD Norms 14px/20px 700, #313131, ls -0.01px |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Painted layers | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 90.1x32.0 bg #191919 @ 0 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | = | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 90.1x32.0 bg #191919 @ 0 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `popular-btn-default.png`, `popular-btn-hover.png`, `popular-btn-focus-visible.png`, `popular-btn-pressed.png`.

#### nearby-cta

Location CTA. The "search nearby"/sign-in call at the end of the directory; measured, never pressed (address/sign-in gate).

Page: restaurants. Selector: `LocationPage*CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 758.56 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #eb1700 | #d91400 | = | #b71000 |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.Text-sc-yxnz5n-0.eBJDEX: DD Norms 16px/22px 700, #ffffff, ls -0.01px | = | = | = |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Painted layers | button.ButtonRootInternal-sc-j2wkqj-0.eEJPyN 758.6x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.eEJPyN 758.6x40.0 bg #d91400 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.eEJPyN 758.6x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset outline 1px auto #005fcc offset 0px | button.ButtonRootInternal-sc-j2wkqj-0.eEJPyN 758.6x40.0 bg #b71000 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nearby-cta-default.png`, `nearby-cta-hover.png`, `nearby-cta-focus-visible.png`, `nearby-cta-pressed.png`.

#### pagination

Pagination loader.

Page: restaurants. Selector: `[data-testid=lego-pagination-loader]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1440 x 584 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.sc-f98a4c4c-0.gTFInR 240.0x20.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 8px; div.sc-f98a4c4c-0.foUEsd 28.0x28.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 50%; div.sc-f98a4c4c-0.foUEsd 28.0x28.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 50%; div.sc-f98a4c4c-0.hoBkdx 448.0x172.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 8px; div.sc-f98a4c4c-0.gXJfPn 96.0x14.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 8px; div.sc-f98a4c4c-0.gEHuWJ 184.0x14.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 8px | = | div.sc-f98a4c4c-0.gTFInR 240.0x20.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 8px; div.sc-f98a4c4c-0.foUEsd 28.0x28.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 50%; div.sc-f98a4c4c-0.foUEsd 28.0x28.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 50%; div.sc-297d2f35-0.sc-e4dee18e-0 1376.0x228.0 outline 1px auto #005fcc offset 0px; div.sc-f98a4c4c-0.hoBkdx 448.0x172.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 8px; div.sc-f98a4c4c-0.gXJfPn 96.0x14.0 bg #f1f1f1 image linear-gradient(90deg, #f1f1f1, #f7f7f7, #f1f1f1) r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pagination-default.png`, `pagination-hover.png`, `pagination-focus-visible.png`, `pagination-pressed.png`.

#### faq-block

FAQ block. The SEO FAQ accordion under the listings.

Page: restaurants. Selector: `[data-testid=seo-faq-block]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 610 |
| Padding | 0px 0px 100px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD-TTNorms 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Text-sc-yxnz5n-0.sc-6edd2c8c-7: DD Norms 32px/24px 800, #191919, ls -0.2px |
| Transition | none |
| Icon | 24 x 24, colour #191919, fill #000000 |
| Painted layers | hr.Border-sc-i9okij-1.hGZdZM 1152.0x1.0 bg #e4e4e4; div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 shadow #e7e7e7 0px -1px 0px 0px inset; div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 shadow #e7e7e7 0px -1px 0px 0px inset; div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 shadow #e7e7e7 0px -1px 0px 0px inset; div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 shadow #e7e7e7 0px -1px 0px 0px inset; div.sc-6edd2c8c-4.dIWIRl 1152.0x81.0 shadow #e7e7e7 0px -1px 0px 0px inset |
| How | at rest |

Crops: `faq-block-default.png`.

#### internal-link

Internal link. A related-cuisine link in the footer SEO block.

Page: restaurants. Selector: `internal-links-section a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.98 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | DD-TTNorms 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.Text-sc-yxnz5n-0.kFFNGs: DD Norms 16px/22px 500, #191919, ls -0.01px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.itninwi 92.0x22.0 outline 1px auto #005fcc offset 1px | = |

Crops: `internal-link-default.png`, `internal-link-hover.png`, `internal-link-focus-visible.png`, `internal-link-pressed.png`.

### Fields, search and gates

#### cookie-banner

Cookie banner. The consent strip, measured then re-hidden — never answered.

Page: store. Selector: `[data-testid=cookie-banner]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 98 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #f7f7f7 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Text-sc-yxnz5n-0.bvDNvo: DD Norms 16px/22px 500, #191919, ls -0.01px |
| Transition | none |
| Icon | 24 x 24, colour #000000 |
| Painted layers | div.BannerWrapper-sc-1qg04qc-0.bLWzhm 1440.0x98.0 bg #f7f7f7; button.ButtonRoot-sc-j2wkqj-0.jcvtZg 61.0x32.0 bg #191919 @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 1px inset; button.ButtonRoot-sc-j2wkqj-0.jcvtZg 113.8x32.0 bg #191919 @ 0 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest |

Crops: `cookie-banner-default.png`.

#### hsa-search

Search input. The catalog search field on the HSA/FSA store; focused only, nothing submitted.

Page: hsa. Selector: `[data-testid=SearchInput]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 788.78 x 32 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Times 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Icon | 24 x 24, colour #191919 | = |
| Painted layers | div::before.sc-b40f2357-2.fsoSKH calc(100% - 16px)x64px bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 20px 20px 0px 0px; div.InputContainer-sc-5yzsia-1.cIaZpF 756.8x32.0 bg #f7f7f7 r 20px shadow #f7f7f7 0px 0px 0px 1px inset; div.InputContentContainerInternal-sc-5yzsia-2.gUKLGr 698.8x20.0 bg #f7f7f7; input.InputContent-sc-5yzsia-4.fswBYl 698.8x20.0 bg #f7f7f7 | div::before.sc-b40f2357-2.fsoSKH calc(100% - 16px)x64px bg #ffffff border T:1px solid #d6d6d6 / R:1px solid #d6d6d6 / L:1px solid #d6d6d6 r 20px 20px 0px 0px; div.InputContainer-sc-5yzsia-1.cIaZpF 756.8x32.0 bg #f7f7f7 r 20px shadow #191919 0px 0px 0px 2px inset; div.InputContentContainerInternal-sc-5yzsia-2.gUKLGr 698.8x20.0 bg #f7f7f7; input.InputContent-sc-5yzsia-4.fswBYl 698.8x20.0 bg #f7f7f7 |
| How | at rest | clicked into the field |

Crops: `hsa-search-default.png`, `hsa-search-focused.png`.

#### hsa-toggle

Delivery/Pickup toggle.

Page: hsa. Selector: `[data-testid=OrderMethodToggle]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155.3 x 38 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.StyledInset-sc-1tdtpkk-0.fhkROy: DD Norms 14px/20px 700, #191919, ls -0.01px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | div.SelectGroupContainer-sc-pcky6n-3.ia-DbeS 155.3x38.0 bg #f1f1f1 border T:1px solid #f1f1f1 / R:1px solid #f1f1f1 / B:1px solid #f1f1f1 / L:1px solid #f1f1f1 r 9999px; div.SelectGroupButtonIndicator-sc-pcky6n-1.VcJuC 78.5x32.0 bg #ffffff r 9999px shadow #e4e4e4 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px | div.SelectGroupContainer-sc-pcky6n-3.ia-DbeS 155.3x38.0 bg #f1f1f1 border T:1px solid #f1f1f1 / R:1px solid #f1f1f1 / B:1px solid #f1f1f1 / L:1px solid #f1f1f1 r 9999px; button.SelectGroupButton-sc-pcky6n-2.hnRBpa 78.5x32.0 bg #f1f1f1 r 9999px; div.SelectGroupButtonIndicator-sc-pcky6n-1.VcJuC 78.5x32.0 bg #f1f1f1 r 9999px shadow #d6d6d6 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px | div.SelectGroupContainer-sc-pcky6n-3.ia-DbeS 155.3x38.0 bg #f1f1f1 border T:1px solid #f1f1f1 / R:1px solid #f1f1f1 / B:1px solid #f1f1f1 / L:1px solid #f1f1f1 r 9999px; button.SelectGroupButton-sc-pcky6n-2.hnRBpa 78.5x32.0 r 9999px outline 1px auto #005fcc offset 0px; div.SelectGroupButtonIndicator-sc-pcky6n-1.VcJuC 78.5x32.0 bg #ffffff r 9999px shadow #e4e4e4 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hsa-toggle-default.png`, `hsa-toggle-hover.png`, `hsa-toggle-focus-visible.png`, `hsa-toggle-pressed.png`.

#### hsa-h1

Promo page title. The HSA/FSA store headline.

Page: hsa. Selector: `h1 on /en-US/p/hsa-fsa-store`. States: .

Not found on the page at capture time.

#### address-field

Address field (gate). The landing-page address search — the entry point the whole consumer flow is gated behind. Focused only; nothing typed or submitted.

Page: promos. Selector: `[data-testid=LandingPageAddressSearch]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 408 x 56 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | DD-TTNorms 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Icon | 24 x 24, colour #191919 | = |
| Painted layers | div.InputContainer-sc-5yzsia-1.gBQgMf 408.0x56.0 bg #f7f7f7 r 32px shadow #f7f7f7 0px 0px 0px 1px inset; div.InputContentContainer-sc-5yzsia-2.cKgGCJ 292.0x22.0 bg #f7f7f7; input.InputContent-sc-5yzsia-4.eLKfvL 292.0x22.0 bg #f7f7f7; button.ButtonRootInternal-sc-j2wkqj-0.bHBHib 40.0x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | div.InputContainer-sc-5yzsia-1.gBQgMf 408.0x56.0 bg #f7f7f7 r 32px shadow #191919 0px 0px 0px 2px inset; div.InputContentContainer-sc-5yzsia-2.cKgGCJ 292.0x22.0 bg #f7f7f7; input.InputContent-sc-5yzsia-4.eLKfvL 292.0x22.0 bg #f7f7f7; button.ButtonRootInternal-sc-j2wkqj-0.bHBHib 40.0x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest | clicked into the field |

Crops: `address-field-default.png`, `address-field-focused.png`.

#### identity-btn

Identity button. The header Sign-in/sign-up identity control; measured, never followed.

Page: promos. Selector: `[data-testid=identityButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 204.55 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #f1f1f1 | #d6d6d6 | = | #c4c4c4 |
| Box shadow | #f1f1f1 0px 0px 0px 1px inset | #d6d6d6 0px 0px 0px 1px inset | = | #c4c4c4 0px 0px 0px 1px inset |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191919 | #242424 | = | #313131 |
| Text node | span.Text-sc-yxnz5n-0.gDygb: DD Norms 14px/20px 700, #191919, ls -0.01px | span.Text-sc-yxnz5n-0.gDygb: DD Norms 14px/20px 700, #242424, ls -0.01px | = | span.Text-sc-yxnz5n-0.gDygb: DD Norms 14px/20px 700, #313131, ls -0.01px |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Icon | 16 x 24, colour #191919 | 16 x 24, colour #242424 | = | 16 x 24, colour #313131 |
| Painted layers | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 204.5x32.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 204.5x32.0 bg #d6d6d6 r 9999px shadow #d6d6d6 0px 0px 0px 1px inset | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 204.5x32.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset outline 1px auto #005fcc offset 0px | button.ButtonRootInternal-sc-j2wkqj-0.gAhkoD 204.5x32.0 bg #c4c4c4 r 9999px shadow #c4c4c4 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `identity-btn-default.png`, `identity-btn-hover.png`, `identity-btn-focus-visible.png`, `identity-btn-pressed.png`.

#### landing-link

Landing link.

Page: promos. Selector: `[data-testid=LandingLinks]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1120 x 318 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | DD-TTNorms 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h2.Text-sc-yxnz5n-0.beEppk: DD Norms 16px/22px 500, #ffffff, ls -0.01px | = | = | = |
| Transition | none | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.sc-6c4a270f-12.hhhwiM 176.7x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `landing-link-default.png`, `landing-link-hover.png`, `landing-link-focus-visible.png`, `landing-link-pressed.png`.

### Storefront (menu page)

#### store-head

Store header. The storefront header: hero image, name, rating and delivery info.

Page: store. Selector: `[data-testid=storeInfo] / HeroImageContainer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 210 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.sc-9c44606c-5.eznBjt 0.0x0.0 border T:60px solid #000000 @ 0 / L:480px solid #ffffff; div.sc-9c44606c-6.joKFnE 80.0x80.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 50% shadow #000000 @ 0.2 0px 2px 8px 0px; div.sc-9c44606c-7.dgRYDA 1200.0x110.0 image linear-gradient(#000000 @ 0 0%, #000000 @ 0.6 75%) r 0px 0px 12px 12px |
| How | at rest |

Crops: `store-head-default.png`.

#### store-name

Store name.

Page: store. Selector: `h1 on store page`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 836 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DD Norms 24px/28px 800 |
| Letter spacing | -0.5px |
| Colour | #191919 |
| Transition | none |
| How | at rest |

Crops: `store-name-default.png`.

#### store-meta

Store meta. The rating/distance/delivery-fee detail line under the store name.

Page: store. Selector: `infoBoxDetail / MenuHeaderDeliveryFee`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 222.5 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Text-sc-yxnz5n-0.djTcAA: DD Norms 14px/20px 700, #191919, ls -0.01px |
| Transition | none |
| Icon | 12 x 12, colour #191919 |
| Painted layers | button.ButtonRoot-sc-j2wkqj-0.iLCINK 12.0x22.0 bg #191919 @ 0 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest |

Crops: `store-meta-default.png`.

#### fulfil-toggle

Fulfilment toggle. The Delivery/Pickup segmented toggle in the menu header; measured, not pressed (a press re-queries the menu).

Page: store. Selector: `MenuOrderMethodToggle*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94.45 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f1f1f1 | = | #d6d6d6 |
| Box shadow | #e4e4e4 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px | #d6d6d6 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px | = | #c4c4c4 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191919 | #242424 | = | #313131 |
| Text node | span.Text-sc-yxnz5n-0.cPDsok: DD Norms 14px/20px 700, #191919, ls -0.01px | span.Text-sc-yxnz5n-0.cPDsok: DD Norms 14px/20px 700, #242424, ls -0.01px | = | span.Text-sc-yxnz5n-0.cPDsok: DD Norms 14px/20px 700, #313131, ls -0.01px |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Painted layers | button.ButtonRoot-sc-j2wkqj-0.hJTtSn 94.5x32.0 bg #ffffff r 9999px shadow #e4e4e4 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px | button.ButtonRoot-sc-j2wkqj-0.hJTtSn 94.5x32.0 bg #f1f1f1 r 9999px shadow #d6d6d6 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px | button.ButtonRoot-sc-j2wkqj-0.hJTtSn 94.5x32.0 bg #ffffff r 9999px shadow #e4e4e4 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px outline 1px auto #005fcc offset 0px | button.ButtonRoot-sc-j2wkqj-0.hJTtSn 94.5x32.0 bg #d6d6d6 r 9999px shadow #c4c4c4 0px 0px 0px 2px inset, #191919 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.SelectGroupContainer-sc-pcky6n-3.kQrTwg bg #f7f7f7 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `fulfil-toggle-default.png`, `fulfil-toggle-hover.png`, `fulfil-toggle-focus-visible.png`, `fulfil-toggle-pressed.png`.

#### group-order

Group-order button. The group-cart action; measured, never pressed.

Page: store. Selector: `CreateGroupCartModalButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 107.63 x 38 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Times 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span: DD Norms 14px/20px 700, #191919, ls -0.01px | span: DD Norms 14px/20px 700, #242424, ls -0.01px | - | = |
| Transition | none | = | - | = |
| Painted layers | button.ButtonRoot-sc-j2wkqj-0.jcvtZg 107.6x38.0 bg #f1f1f1 r 9999px shadow #f1f1f1 0px 0px 0px 1px inset | button.ButtonRoot-sc-j2wkqj-0.jcvtZg 107.6x38.0 bg #d6d6d6 r 9999px shadow #d6d6d6 0px 0px 0px 1px inset | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `group-order-default.png`, `group-order-hover.png`, `group-order-pressed.png`.

#### search-input

Store search field. The in-store menu search input; focused only, never submitted.

Page: store. Selector: `[data-testid=SearchInput]`. States: .

Not found on the page at capture time.

#### menu-item

Menu item card. A menu item in the virtualised grid: image, name, price.

Page: store. Selector: `VirtualGridContainer > item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 944 x 450 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #f7f7f7 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.sc-c2a9fd7b-1.ctxhrq 944.0x450.0 bg #f7f7f7 r 16px |
| How | at rest |

Crops: `menu-item-default.png`.

#### quick-add

Quick-add button. The + quick-add circle on a menu item; measured, NEVER pressed — a press starts a cart.

Page: store. Selector: `[data-testid=quick-add-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191919 | #242424 | = | #313131 |
| Transition | background-color, box-shadow 0.2s, 0.2s cubic-bezier(0.4, 0.4, 0, 1), cubic-bezier(0.4, 0.4, 0, 1) delay 0s, 0s | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s | = | background-color, box-shadow 0.05s, 0.05s linear, linear delay 0s, 0s |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #191919 | 24 x 24, colour #242424 | = | 24 x 24, colour #313131 |
| Painted layers | button.ButtonRoot-sc-j2wkqj-0.kLnbCu 32.0x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px | = | button.ButtonRoot-sc-j2wkqj-0.kLnbCu 32.0x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `quick-add-default.png`, `quick-add-hover.png`, `quick-add-focus-visible.png`, `quick-add-pressed.png`.

#### rec-section

Recommended carousel. The "Recommended items for you" carousel rail.

Page: store. Selector: `recommended_items_for_you`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 944 x 302 |
| Padding | 20px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.Text-sc-yxnz5n-0.jdFLVM: DD Norms 20px/24px 800, #191919, ls -0.2px |
| Transition | none |
| Icon | 24 x 24, colour #191919 |
| Painted layers | div.sc-6d5ee6a2-0.kQKwOO 177.0x168.0 bg #f7f7f7; button.ButtonRoot-sc-j2wkqj-0.kLnbCu 32.0x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px; div.sc-6d5ee6a2-0.kQKwOO 177.0x168.0 bg #f7f7f7; button.ButtonRoot-sc-j2wkqj-0.kLnbCu 32.0x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px; div.sc-6d5ee6a2-0.kQKwOO 177.0x168.0 bg #f7f7f7; button.ButtonRoot-sc-j2wkqj-0.kLnbCu 32.0x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px |
| How | at rest |

Crops: `rec-section-default.png`.

#### breadcrumb

Breadcrumb. The SEO breadcrumb trail at the foot of the store page.

Page: store. Selector: `[data-testid=seo-breadcrumb]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.i3ez6m5: DD Norms 12px/12px 700, #606060, ls -0.01px |
| Transition | none |
| How | at rest |

Crops: `breadcrumb-default.png`.

#### address-nux

Missing-address nux. The new-user "add an address" prompt shown without a saved address — the documented address gate, never answered.

Page: store. Selector: `[data-testid=nuxStoreMissingAddress]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 222.5 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Text-sc-yxnz5n-0.knXmhr: DD Norms 16px/22px 700, #191919, ls -0.01px |
| Transition | none |
| Painted layers | div.sc-59edd6a5-0.hsMxDv 222.5x52.0 bg #ffffff r 8px; button.ButtonRoot-sc-j2wkqj-0.iLCINK 222.5x22.0 bg #191919 @ 0 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset |
| How | at rest |

Crops: `address-nux-default.png`.

### Careers site (WordPress stack)

#### car-header

Careers header. The careersatdoordash.com header — a separate WordPress/Tailwind stack (bg-pinot-noir, .btn), not the prism consumer system.

Page: careers. Selector: `careers header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Tt norms pro 16px/24px 400 |
| Letter spacing | normal |
| Colour | #4c0c3a |
| Text node | a.menu-link: Tt norms pro 14px/21px 700, #4c0c3a |
| Transition | none |
| Painted layers | header.bg-white.relative 1440.0x80.0 bg #ffffff; div.mobile-button.mlg:hidden 0.0x0.0 bg #000000 r 3.35544e+07px; span.hamburger-inner 0.0x0.0 bg #ffffff r 4px; span::before.hamburger-inner 40pxx4px bg #ffffff r 4px; span::after.hamburger-inner 40pxx4px bg #ffffff r 4px; ul.w-full.opacity-0 925.2x37.0 bg #ffffff |
| How | at rest |

Crops: `car-header-default.png`.

#### car-h1

Careers headline.

Page: careers. Selector: `careers h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 181 x 21.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TT Norms Pro Cond 16px/24px 900 |
| Letter spacing | -1px |
| Colour | #4c0c3a |
| Transition | none |
| How | at rest |

Crops: `car-h1-default.png`.

#### car-btn

Careers button. A .btn pill on the WordPress careers theme.

Page: careers. Selector: `a.btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.27 x 42 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Border | 1px solid #ff3008 | 1px solid #cc0000 | = | 1px solid #cc0000 |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff3008 | #cc0000 | = | #cc0000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Tt norms pro 16px/16px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn 127.3x42.0 bg #ff3008 border T:1px solid #ff3008 / R:1px solid #ff3008 / B:1px solid #ff3008 / L:1px solid #ff3008 r 3.35544e+07px | a.btn 127.3x42.0 bg #cc0000 border T:1px solid #cc0000 / R:1px solid #cc0000 / B:1px solid #cc0000 / L:1px solid #cc0000 r 3.35544e+07px | a.btn 127.3x42.0 bg #ff3008 border T:1px solid #ff3008 / R:1px solid #ff3008 / B:1px solid #ff3008 / L:1px solid #ff3008 r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.btn 127.3x42.0 bg #cc0000 border T:1px solid #cc0000 / R:1px solid #cc0000 / B:1px solid #cc0000 / L:1px solid #cc0000 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `car-btn-default.png`, `car-btn-hover.png`, `car-btn-focus-visible.png`, `car-btn-pressed.png`.

#### car-nav-link

Careers nav link.

Page: careers. Selector: `careers nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.75 x 37 | = | = | = |
| Padding | 8px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff3008 | #cc0000 | = | #cc0000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Tt norms pro 14px/21px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.menu-link 117.8x37.0 bg #ff3008 r 3.35544e+07px | a.menu-link 117.8x37.0 bg #cc0000 r 3.35544e+07px | a.menu-link 117.8x37.0 bg #ff3008 r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.menu-link 117.8x37.0 bg #cc0000 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `car-nav-link-default.png`, `car-nav-link-hover.png`, `car-nav-link-focus-visible.png`, `car-nav-link-pressed.png`.

### Footer

#### footer

Footer. The footer: link columns, store badges, language select, socials, legal.

Page: home. Selector: `[data-testid=Footer]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1160 x 952 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.Text-sc-yxnz5n-0.jRvnUE: DD Norms 16px/22px 500, #ffffff, ls -0.01px |
| Transition | none |
| Icon | 144 x 48, colour #000000, fill #ffffff |
| Painted layers | div.sc-6c4a270f-15.behXqC 160.0x52.0 bg #494949 r 8px; div.sc-6c4a270f-15.behXqC 160.0x52.0 bg #494949 r 8px; div.InputContainer-sc-5yzsia-1.futmdp 150.0x32.0 bg #f1f1f1 r 16px shadow #e4e4e4 0px 0px 0px 1px inset; div.InputContentContainerInternal-sc-5yzsia-2.gUKLGr 94.0x20.0 bg #f1f1f1; div.SelectContainer-sc-1wilwzz-0.khtfio 94.0x20.0 bg #f1f1f1; select.SelectElementContent-sc-5yzsia-3.fnohMZ 94.0x20.0 bg #f1f1f1 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114.11 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Text node | span.Text-sc-yxnz5n-0.sc-6c4a270f-13: DD Norms 14px/20px 500, #c4c4c4, ls -0.01px | span.Text-sc-yxnz5n-0.sc-6c4a270f-13: DD Norms 14px/20px 500, #ffffff, ls -0.01px | = | = |
| Transition | filter 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.sc-6c4a270f-12.hhhwiM 114.1x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### appstore-badge

Store badge. The App Store / Google Play badge links.

Page: home. Selector: `[data-testid=AppStoreButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | opacity 0.2s ease | = | = | = |
| Opacity | 0.7 | - | = | - |
| Cursor | pointer | = | = | = |
| Icon | 144 x 48, colour #000000, fill #ffffff | = | = | = |
| Painted layers | div.sc-6c4a270f-15.behXqC 160.0x52.0 bg #494949 r 8px | = | a.sc-6c4a270f-14.fSugZ 160.0x52.0 outline 1px auto #005fcc offset 1px; div.sc-6c4a270f-15.behXqC 160.0x52.0 bg #494949 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `appstore-badge-default.png`, `appstore-badge-hover.png`, `appstore-badge-focus-visible.png`, `appstore-badge-pressed.png`.

#### social-btn

Social button. A social-media icon link in the footer.

Page: home. Selector: `[data-testid$=SocialMediaButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | opacity 0.2s ease | = | = | = |
| Opacity | 0.7 | - | = | - |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.sc-6c4a270f-14.fSugZ 24.0x32.0 outline 1px auto #005fcc offset 1px | = |

Crops: `social-btn-default.png`, `social-btn-hover.png`, `social-btn-focus-visible.png`, `social-btn-pressed.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar.

Page: mobile. Selector: `top bar at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 600 |
| Padding | 0px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.Text-sc-yxnz5n-0.sc-4e5f74df-13: TTNormsProCond-Blk 22px/28px 900, #ffffff |
| Transition | none |
| Icon | 42 x 24, colour #000000, fill #ffffff |
| Painted layers | a.ButtonRoot-sc-j2wkqj-0.iLCINK 82.4x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset; a.ButtonRoot-sc-j2wkqj-0.iLCINK 90.5x40.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset; button.ButtonRoot-sc-j2wkqj-0.jcvtZg 204.5x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px; button.ButtonRoot-sc-j2wkqj-0.jcvtZg 179.8x32.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset, #191919 @ 0.2 0px 2px 8px 0px |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-identity-btn

Mobile identity button. The combined sign-in/sign-up control at 390 wide.

Page: mobile. Selector: `identity button at 390`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 40 | = | - | = |
| Padding | 0px 24px 0px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Times 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.Text-sc-yxnz5n-0.huQgjs: DD Norms 18px/22px 800, #ffffff, ls -0.2px | = | - | = |
| Transition | none | = | - | = |
| Painted layers | a.ButtonRoot-sc-j2wkqj-0.iLCINK 82.4x40.0 bg #eb1700 r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset; a.ButtonRoot-sc-j2wkqj-0.iLCINK 90.5x40.0 bg #ffffff r 9999px shadow #191919 @ 0 0px 0px 0px 1px inset | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `m-identity-btn-default.png`, `m-identity-btn-hover.png`, `m-identity-btn-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TTNormsProCond-Blk 22px/28px 900 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

DoorDash's styles are readable on the archived pages (styled-components and the prism token sheets plus inline style attributes); this list holds what the CSSOM exposed per page, and the per-state Transition rows above are computed values.

- business: `unset`, `var(--press-transition-exit)`, `none`, `var(--press-transition-enter)`, `opacity 0.15s ease-in-out`, `background-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `opacity 0.3s ease-out`, `transform 0.3s`, `filter 0.2s`, `opacity 0.2s`

- careers: `opacity 0.2s`, `opacity 0.1s linear`, `transform 0.1s`, `200ms`, `none`, `transform 0.15s cubic-bezier(0.645, 0.045, 0.355, 1), background-color cubic-bezier(0.645, 0.045, 0.355, 1) 0.1s`, `transform cubic-bezier(0.645, 0.045, 0.355, 1) 0.1s`, `top 0.1s 0.1s, transform 0.1s cubic-bezier(0.165, 0.84, 0.44, 1)`, `bottom 0.1s 0.1s, transform 0.1s cubic-bezier(0.165, 0.84, 0.44, 1)`, `top 0.1s, transform 0.1s cubic-bezier(0.895, 0.03, 0.685, 0.22) 0.1s`, `bottom 0.1s, transform 0.1s cubic-bezier(0.895, 0.03, 0.685, 0.22) 0.1s`, `top 0.2s cubic-bezier(0.33333, 0.66667, 0.66667, 1) 0.2s, opacity 0.1s linear`

- dashpass: `unset`, `var(--press-transition-exit)`, `none`, `var(--press-transition-enter)`, `opacity 0.15s ease-in-out`, `box-shadow 225ms cubic-bezier(0.83, 0, 0.17, 1)`, `0.3s ease-in-out`, `opacity 150ms ease-in-out`, `filter 0.2s`, `opacity 0.2s`

- food-delivery: `var(--press-transition-exit)`, `none`, `var(--press-transition-enter)`, `opacity 0.15s ease-in-out`, `background-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `opacity 0.3s ease-out`, `transform 0.3s`, `filter 0.2s`, `opacity 0.2s`

- home: `unset`, `background-color 0.15s linear`, `margin-inline-end 0.4s cubic-bezier(0.2, 0.6, 0.4, 1), -webkit-margin-end 0.4s cubic-bezier(0.2, 0.6, 0.4, 1)`, `transform 0.1s ease-in`, `max-width 0.2s`, `opacity 0.2s`, `width 0.2s, transform 0.2s`, `opacity 0.22s`, `transform 0.3s ease-in-out`, `opacity 0.5s ease-out`, `transform 0.2s`, `opacity 0.2s linear`

- hsa: `background-color 0.15s linear`, `margin-inline-end 0.4s cubic-bezier(0.2, 0.6, 0.4, 1), -webkit-margin-end 0.4s cubic-bezier(0.2, 0.6, 0.4, 1)`, `transform 0.1s ease-in`, `unset`, `max-width 0.2s`, `opacity 0.2s`, `width 0.2s`, `opacity 0.22s`, `transform 0.3s ease-in-out`, `var(--press-transition-exit)`, `none`, `var(--press-transition-enter)`

- promos: `var(--press-transition-exit)`, `none`, `var(--press-transition-enter)`, `opacity 0.15s ease-in-out`, `filter 0.2s`, `opacity 0.2s`, `0.25s`, `max-height 0.15s ease-out`

- restaurants: `var(--press-transition-exit)`, `none`, `var(--press-transition-enter)`, `opacity 0.15s ease-in-out`, `background-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `opacity 0.3s ease-out`, `transform 0.3s`, `0.3s ease-in-out`, `filter 0.2s`, `opacity 0.2s`, `0.25s`, `max-height 0.15s ease-out`

- store: `unset`, `background-color 0.15s linear`, `margin-inline-end 0.4s cubic-bezier(0.2, 0.6, 0.4, 1), -webkit-margin-end 0.4s cubic-bezier(0.2, 0.6, 0.4, 1)`, `transform 0.1s ease-in`, `max-width 0.2s`, `opacity 0.2s`, `width 0.2s, transform 0.2s`, `opacity 0.22s`, `transform 0.3s ease-in-out`, `opacity 0.5s ease-out`, `transform 0.2s`, `opacity 0.2s linear`
