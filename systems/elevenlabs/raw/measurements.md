# Component measurements

Computed styles read from elevenlabs.io on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /pricing, /text-to-speech, /api, /docs and the signed-out /app/sign-in and /app/sign-up cards — with the Cookiebot consent layer hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### announcement

Announcement bar. The promo strip above the nav (the V4 "Meet Eleven v4" bar on home, the $1-credits countdown on product pages).

Page: home. Selector: `promo strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 48 |
| Padding | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.tw-hidden.md:tw-inline: Inter 14px/18px 400, #000000, ls 0.14px |
| Transition | none |
| Icon | 20 x 22, colour #f5f3f1, fill #000000 |
| Painted layers | div.tw-absolute.tw-inset-0 1440.0x48.0 bg #f5f3f1; div.tw-absolute.tw-inset-x-0 1440.0x0.5 bg #000000 @ 0.1; a.tw-inline-flex.tw-items-center 77.9x32.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px; a.tw-inline-flex.tw-items-center 0.0x0.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `announcement-default.png`.

#### nav

Nav bar. The top nav: the ElevenLabs wordmark, the Products/Solutions/Customers/Resources flyout triggers, Enterprise and Pricing links, and the Log in / Sign up actions.

Page: home. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672.3 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.tw-py-2.tw-px-3: Inter 14px/20px 400, #000000 |
| Transition | none |
| Icon | 117 x 15, colour #000000 |
| Painted layers | a.tw-group.tw-outline-none 141.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; button.tw-group.tw-flex 83.1x36.0 outline 2px solid #000000 @ 0 offset 2px; button.tw-group.tw-flex 85.1x36.0 outline 2px solid #000000 @ 0 offset 2px; a.tw-group.tw-flex 95.8x36.0 outline 2px solid #000000 @ 0 offset 2px; button.tw-group.tw-flex 93.6x36.0 outline 2px solid #000000 @ 0 offset 2px; a.tw-group.tw-flex 91.7x36.0 outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `nav-default.png`.

#### logo

Logo. The ElevenLabs wordmark anchor (aria-label "ElevenLabs").

Page: home. Selector: `a[aria-label=ElevenLabs]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 141 x 36 |
| Padding | 0px 12px |
| Gap | 4px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 117 x 15, colour #000000 |
| Painted layers | a.tw-group.tw-outline-none 141.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Products button that opens the nav flyout; toggled, never followed.

Page: home. Selector: `nav button Products`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.06 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-py-2.tw-px-3: Inter 14px/20px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.tw-group.tw-flex 83.1x36.0 outline 2px solid #000000 @ 0 offset 2px | button.tw-group.tw-flex 83.1x36.0 outline 2px solid #000000 @ 0 offset 2px; div.tw-py-2.tw-px-3 83.1x36.0 bg #292524 @ 0.05 r 18px | button.tw-group.tw-flex 83.1x36.0 outline 2px solid #000000 @ 0 offset 2px; div.tw-py-2.tw-px-3 83.1x36.0 r 18px outline 1px solid #2b7fff offset 2px | button.tw-group.tw-flex 83.1x36.0 outline 2px solid #000000 @ 0 offset 2px; div.tw-py-2.tw-px-3 83.1x36.0 bg #292524 @ 0.05 r 18px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. A plain nav link (Pricing); measured, never followed.

Page: home. Selector: `nav a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-px-3.tw-py-2: Inter 14px/20px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-group.tw-flex 70.0x36.0 outline 2px solid #000000 @ 0 offset 2px | a.tw-group.tw-flex 70.0x36.0 outline 2px solid #000000 @ 0 offset 2px; div.tw-px-3.tw-py-2 70.0x36.0 bg #292524 @ 0.05 r 18px | a.tw-group.tw-flex 70.0x36.0 outline 2px solid #000000 @ 0 offset 2px; div.tw-px-3.tw-py-2 70.0x36.0 r 18px outline 1px solid #2b7fff offset 2px | a.tw-group.tw-flex 70.0x36.0 outline 2px solid #000000 @ 0 offset 2px; div.tw-px-3.tw-py-2 70.0x36.0 bg #292524 @ 0.05 r 18px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### signup-cta

Sign-up action. The header Sign up action (the black pill); measured, never followed.

Page: home. Selector: `header Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.03 x 36 | = | = | 76.47 x 35.28 |
| Padding | 0px 14px | = | = | = |
| Gap | normal 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #44403b | = | #44403b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 78.0x36.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 78.0x36.0 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 78.0x36.0 bg #000000 r 9999px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 76.5x35.3 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `signup-cta-default.png`, `signup-cta-hover.png`, `signup-cta-focus-visible.png`, `signup-cta-pressed.png`.

#### login-link

Log-in action. The header Log in action; measured, never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.5 x 36 | = | = | 67.13 x 35.28 |
| Padding | 0px 14px | = | = | = |
| Gap | normal 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #fdfcfc | = | #fdfcfc |
| Box shadow | #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-items-center.tw-whitespace-nowrap 68.5x36.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.tw-items-center.tw-whitespace-nowrap 68.5x36.0 bg #fdfcfc r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.tw-items-center.tw-whitespace-nowrap 68.5x36.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 1px solid #2b7fff offset 2px | a.tw-items-center.tw-whitespace-nowrap 67.1x35.3 bg #fdfcfc r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### nav-dropdown

Nav flyout. The Products mega-menu panel (Overview / ElevenCreative / ElevenAgents / ElevenAPI columns), opened by its own trigger.

Page: home. Selector: `opened Products flyout`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 940 x 565.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.tw-type-2xs.tw-px-2.5: Inter 13px/18px 500, #777169 |
| Transition | none |
| Painted layers | a.tw-block.tw-font-medium 226.0x12.5 outline 2px solid #000000 @ 0 offset 2px; a.tw-block.tw-font-medium 226.0x12.5 outline 2px solid #000000 @ 0 offset 2px; a.tw-block.tw-font-medium 226.0x12.5 outline 2px solid #000000 @ 0 offset 2px; div.tw-h-px.tw-bg-gray-100 226.0x1.0 bg #f5f3f1; a.tw-block.tw-font-medium 226.0x11.0 outline 2px solid #000000 @ 0 offset 2px; a.tw-block.tw-font-medium 226.0x11.0 outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 3 up div.tw-w-full.tw-bg-white bg #ffffff shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 3px 6px -1.5px, #000000 @ 0.04 0px 12px 12px -6px, #000000 @ 0.04 0px 48px 48px -24px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Flyout link. A link inside the opened Products flyout (Text to Speech).

Page: home. Selector: `flyout a[href=/text-to-speech]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173.45 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 15px/22px 400 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #777169 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #777169 | = | = | = |
| Painted layers | a.tw-outline-none.tw-inline-flex 173.5x22.0 outline 2px solid #000000 @ 0 offset 2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

#### voice-chat

Voice-chat launcher. The fixed "Voice chat" launcher bottom-right (the ElevenAgents widget); measured, never opened.

Page: home. Selector: `Voice chat launcher`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 157.09 x 56 | = | = | = |
| Padding | 10px 20px 10px 56px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-text-black.tw-type-sm: Inter 16px/24px 400, #000000, ls 0.16px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.tw-py-1.5.sm:tw-py-2.5 157.1x56.0 outline 2px solid #000000 @ 0 offset 2px | = | = | = |
| Ancestor paint | 1 up div.tw-relative.tw-w-full bg #ffffff shadow #000000 @ 0.04 0px 2px 4px 0px, #000000 @ 0.04 0px 6px 16px 0px | 1 up div.tw-relative.tw-w-full bg #fdfcfc shadow #000000 @ 0.04 0px 2px 4px 0px, #000000 @ 0.04 0px 6px 16px 0px | 1 up div.tw-relative.tw-w-full bg #ffffff shadow #000000 @ 0.04 0px 2px 4px 0px, #000000 @ 0.04 0px 6px 16px 0px; 2 up div.tw-pointer-events-auto.tw-relative bg #000000 @ 0.15 outline 1px solid #2b7fff | 1 up div.tw-relative.tw-w-full bg #fdfcfc shadow #000000 @ 0.04 0px 2px 4px 0px, #000000 @ 0.04 0px 6px 16px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `voice-chat-default.png`, `voice-chat-hover.png`, `voice-chat-focus-visible.png`, `voice-chat-pressed.png`.

### Home

#### hero-title

Hero headline. The "Bringing technology to life" display headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 563 x 86.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 48px/52px 300 |
| Letter spacing | -0.96px |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the hero headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 563 x 59.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | 0.16px |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The hero "Sign up" black pill; measured, never followed.

Page: home. Selector: `hero Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.59 x 40 | = | = | 83.88 x 39.2 |
| Padding | 0px 16px | = | = | = |
| Gap | normal 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #44403b | = | #44403b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 15px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 85.6x40.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 85.6x40.0 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 85.6x40.0 bg #000000 r 9999px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 83.9x39.2 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### contact-sales

Secondary CTA. The hero "Contact sales" ghost pill; measured, never followed.

Page: home. Selector: `hero Contact sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.13 x 36 | = | = | 115.76 x 35.28 |
| Padding | 0px 14px | = | = | = |
| Gap | normal 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #fdfcfc | = | #fdfcfc |
| Box shadow | #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 118.1x36.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 118.1x36.0 bg #fdfcfc r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 118.1x36.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 115.8x35.3 bg #fdfcfc r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `contact-sales-default.png`, `contact-sales-hover.png`, `contact-sales-focus-visible.png`, `contact-sales-pressed.png`.

#### product-tab

Product tab. A hero product tab (ElevenCreative / ElevenAgents / ElevenAPI); measured unselected — the selected state is the screenshot toggle.

Page: home. Selector: `hero role=tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 389.33 x 44 | = | = | = |
| Padding | 0px 21px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-type-base.tw-hidden: Inter 16px/24px 400, #44403b, ls 0.16px | div.tw-type-base.tw-hidden: Inter 16px/24px 400, #000000, ls 0.16px | = | div.tw-type-base.tw-hidden: Inter 16px/24px 400, #000000, ls 0.16px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.tw-group/tab.tw-isolate 389.3x44.0 r 12px outline 2px solid #000000 @ 0 offset 2px; div.tw-relative.tw-mr-0.5 12.0x12.0 bg #f5f3f1 r 12px; div.tw-absolute.tw-mix-blend-overlay 12.0x12.0 image image-set(url(…) 1dppx type("image/avif"), url(…) 1dppx type("image/png")); div.tw-absolute.-tw-z-10 383.3x40.0 bg #ebe8e4 r 12px; div.tw-absolute.-tw-z-10 383.3x40.0 bg #ffffff r 12px shadow #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | div.tw-group/tab.tw-isolate 389.3x44.0 r 12px outline 1px solid #2b7fff offset 2px; div.tw-relative.tw-mr-0.5 12.0x12.0 bg #f5f3f1 r 12px; div.tw-absolute.tw-mix-blend-overlay 12.0x12.0 image image-set(url(…) 1dppx type("image/avif"), url(…) 1dppx type("image/png")); div.tw-absolute.-tw-z-10 383.3x40.0 bg #ebe8e4 r 12px; div.tw-absolute.-tw-z-10 383.3x40.0 bg #ffffff r 12px shadow #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-tab-default.png`, `product-tab-hover.png`, `product-tab-focus-visible.png`, `product-tab-pressed.png`.

#### tool-tab

Tool tab. A product-showcase tab (AI Voice Generator / Text to Speech / Music / Speech to Text / Voice Cloning / Dubbing).

Page: home. Selector: `tools role=tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 142.34 x 40 | = | = | = |
| Padding | 0px 17px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-type-sm: Inter 15px/22px 400, #44403b, ls 0.15px | div.tw-type-sm: Inter 15px/22px 400, #000000, ls 0.15px | = | div.tw-type-sm: Inter 15px/22px 400, #000000, ls 0.15px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.tw-group/tab.tw-isolate 142.3x40.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; div.tw-absolute.-tw-z-10 136.3x36.0 bg #ebe8e4 r 9999px; div.tw-absolute.-tw-z-10 136.3x36.0 bg #ffffff r 9999px shadow #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | div.tw-group/tab.tw-isolate 142.3x40.0 r 9999px outline 1px solid #2b7fff offset 2px; div.tw-absolute.-tw-z-10 136.3x36.0 bg #ebe8e4 r 9999px; div.tw-absolute.-tw-z-10 136.3x36.0 bg #ffffff r 9999px shadow #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tool-tab-default.png`, `tool-tab-hover.png`, `tool-tab-focus-visible.png`, `tool-tab-pressed.png`.

#### voice-play

Voice preview. A "Play <voice> preview" button on the voice-orb carousel; measured, the audio itself was never played here.

Page: home. Selector: `button[aria-label*=preview]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 108.94 x 108.94 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | - | = |
| Font | Inter 18px/28.8px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | none | = | - | = |
| Cursor | default | = | - | = |
| Painted layers | button.tw-absolute.tw-inset-0 108.9x108.9 r 9999px outline 2px solid #000000 @ 0 offset 2px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `voice-play-default.png`, `voice-play-hover.png`, `voice-play-pressed.png`.

#### voice-prev

Carousel previous. The "Previous voice" carousel icon button.

Page: home. Selector: `button[aria-label=Previous voice]`. States: .

Not found on the page at capture time.

#### section-h2

Section heading. A section heading below the hero (the "Create, edit, and localize in one AI platform" block).

Page: home. Selector: `section h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 563 x 11.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | 0.16px |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `section-h2-default.png`.

#### tts-card

Playground card. The "Ultra-realistic speech" playground card — the signed-out TTS demo widget (textarea, language and voice selects, Play).

Page: home. Selector: `playground card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 530 x 208 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.tw-px-5.tw-text-base/base: Inter 16px/24px 400, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #a59f97 |
| Painted layers | div.tw-px-5.tw-text-base/base 530.0x136.0 outline 2px solid #000000 @ 0 offset 2px; textarea.tw-px-5.tw-text-base/base 530.0x136.0 outline 2px solid #000000 @ 0 offset 2px; div.tw-flex-none.tw-sticky 529.0x24.0 image linear-gradient(to top, #ffffff, #ffffff @ 0); button.tw-w-full.tw-font-medium 120.0x36.0 r 12px outline 2px solid #000000 @ 0 offset 2px; select 180.0x23.0 bg #ffffff; button.tw-w-full.tw-font-medium 158.1x36.0 r 12px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 2 up div.tw-relative.tw-isolate bg #ffffff shadow #ffffff 0px 0px 0px 0px inset, #ebe8e4 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `tts-card-default.png`.

#### tts-textarea

Playground textarea. The playground's text field; focused and given sample text that was deleted again — nothing generated in this pass.

Page: home. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 530 x 136 | = | = |
| Padding | 16px 20px 0px 20px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0, opacity 1 | = | = |
| Painted layers | textarea.tw-px-5.tw-text-base/base 530.0x136.0 outline 2px solid #000000 @ 0 offset 2px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `tts-textarea-default.png`, `tts-textarea-focused.png`, `tts-textarea-filled.png`.

#### tts-language

Language select. The playground language combobox (the flag + "English" button).

Page: home. Selector: `language button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.03 x 36 | = | = | = |
| Padding | 0px 8px 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #2b7fff offset 2px | = |
| Font | Inter 15px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-min-w-0.tw-truncate: Inter 15px/22px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a59f97 | 16 x 16, colour #000000 | = | = |
| Painted layers | button.tw-w-full.tw-font-medium 120.0x36.0 r 12px outline 2px solid #000000 @ 0 offset 2px | = | button.tw-w-full.tw-font-medium 120.0x36.0 r 12px outline 2px solid #2b7fff offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tts-language-default.png`, `tts-language-hover.png`, `tts-language-focus-visible.png`, `tts-language-pressed.png`.

#### tts-voice

Voice select. The playground voice combobox (the orb + voice-name button).

Page: home. Selector: `voice button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 158.14 x 36 | = | = | = |
| Padding | 0px 8px 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #2b7fff offset 2px | = |
| Font | Inter 15px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-min-w-0.tw-truncate: Inter 15px/22px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a59f97 | 16 x 16, colour #000000 | = | = |
| Painted layers | button.tw-w-full.tw-font-medium 158.1x36.0 r 12px outline 2px solid #000000 @ 0 offset 2px | = | button.tw-w-full.tw-font-medium 158.1x36.0 r 12px outline 2px solid #2b7fff offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tts-voice-default.png`, `tts-voice-hover.png`, `tts-voice-focus-visible.png`, `tts-voice-pressed.png`.

#### tts-play

Play button. The playground Play action; states forced — the public shot pass pressed it once and it generated without an account (see README).

Page: home. Selector: `Play button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.86 x 36 | = | - | = |
| Padding | 0px 14px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | #000000 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | - | = |
| Font | Inter 15px/15px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.tw-flex-none.tw-ml-auto 57.9x36.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `tts-play-default.png`, `tts-play-hover.png`, `tts-play-pressed.png`.

#### learn-more

Learn more. The "Learn more" black pill in the product section.

Page: home. Selector: `Learn more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.44 x 44 | = | = | 123.91 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #44403b | = | #44403b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 126.4x44.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 126.4x44.0 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 126.4x44.0 bg #000000 r 9999px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 123.9x43.1 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `learn-more-default.png`, `learn-more-hover.png`, `learn-more-focus-visible.png`, `learn-more-pressed.png`.

#### feature-card

Feature panel. A feature panel under the product grid (the Ultra-realistic speech showcase, the playground card's parent).

Page: home. Selector: `feature panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 530 x 208 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.tw-px-5.tw-text-base/base: Inter 16px/24px 400, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #a59f97 |
| Painted layers | div.tw-px-5.tw-text-base/base 530.0x40.0 outline 2px solid #000000 @ 0 offset 2px; textarea.tw-px-5.tw-text-base/base 530.0x136.0 outline 2px solid #000000 @ 0 offset 2px; div.tw-flex-none.tw-sticky 529.0x24.0 image linear-gradient(to top, #ffffff, #ffffff @ 0); button.tw-w-full.tw-font-medium 120.0x36.0 r 12px outline 2px solid #000000 @ 0 offset 2px; select 180.0x23.0 bg #ffffff; button.tw-w-full.tw-font-medium 158.1x36.0 r 12px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.tw-relative.tw-isolate bg #ffffff shadow #ffffff 0px 0px 0px 0px inset, #ebe8e4 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `feature-card-default.png`.

### Pricing

#### pricing-h1

Pricing title. The "Flexible pricing for your needs" display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 757.33 x 34.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 48px/52px 300 |
| Letter spacing | -0.96px |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### product-pill

Product pill. An ElevenCreative/ElevenAgents/ElevenAPI product pill (a link, not a tab — it navigates); measured, never followed.

Page: pricing. Selector: `product pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 169.05 x 44 | = | = | = |
| Padding | 0px 21px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-type-base.tw-hidden: Inter 16px/24px 400, #777169, ls 0.16px | div.tw-type-base.tw-hidden: Inter 16px/24px 400, #000000, ls 0.16px | = | div.tw-type-base.tw-hidden: Inter 16px/24px 400, #000000, ls 0.16px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-group/tab.tw-isolate 169.0x44.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; div.tw-relative.tw-mr-0.5 12.0x12.0 bg #f5f3f1 r 9999px; div.tw-absolute.tw-mix-blend-overlay 12.0x12.0 image image-set(url(…) 1dppx type("image/avif"), url(…) 1dppx type("image/png")); div.tw-absolute.-tw-z-10 161.0x38.0 bg #f5f3f1 r 9999px; div.tw-absolute.-tw-z-10 161.0x38.0 bg #ffffff r 9999px shadow #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | a.tw-group/tab.tw-isolate 169.0x44.0 r 9999px outline 1px solid #2b7fff offset 2px; div.tw-relative.tw-mr-0.5 12.0x12.0 bg #f5f3f1 r 9999px; div.tw-absolute.tw-mix-blend-overlay 12.0x12.0 image image-set(url(…) 1dppx type("image/avif"), url(…) 1dppx type("image/png")); div.tw-absolute.-tw-z-10 161.0x38.0 bg #f5f3f1 r 9999px; div.tw-absolute.-tw-z-10 161.0x38.0 bg #ffffff r 9999px shadow #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = |
| Ancestor paint | 1 up div.tw-grid.tw-rounded-full shadow #ffffff 0px 0px 0px 0px inset, #d7d2cc 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-pill-default.png`, `product-pill-hover.png`, `product-pill-focus-visible.png`, `product-pill-pressed.png`.

#### billing-select

Billing dropdown. The "Monthly billing" dropdown; opened for the billing screenshot, never changed.

Page: pricing. Selector: `billing dropdown`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 168.2 x 44 | = | = | 164.84 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #ffffff 0px 0px 0px 0px inset, #d7d2cc 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px inset, #a59f97 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px | = | #ffffff 0px 0px 0px 0px inset, #a59f97 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #777169 | #000000 | = | #000000 |
| Text node | span.tw-truncate: Inter 16px/24px 400, #777169 | span.tw-truncate: Inter 16px/24px 400, #000000 | = | span.tw-truncate: Inter 16px/24px 400, #000000 |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #777169 | 20 x 20, colour #000000 | = | 19.6 x 19.6, colour #000000 |
| Painted layers | button.tw-inline-flex.tw-items-center 168.2x44.0 r 9999px shadow #ffffff 0px 0px 0px 0px inset, #d7d2cc 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | button.tw-inline-flex.tw-items-center 168.2x44.0 r 9999px shadow #ffffff 0px 0px 0px 0px inset, #a59f97 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | button.tw-inline-flex.tw-items-center 168.2x44.0 r 9999px shadow #ffffff 0px 0px 0px 0px inset, #d7d2cc 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px outline 1px solid #2b7fff offset 2px | button.tw-inline-flex.tw-items-center 164.8x43.1 r 9999px shadow #ffffff 0px 0px 0px 0px inset, #a59f97 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `billing-select-default.png`, `billing-select-hover.png`, `billing-select-focus-visible.png`, `billing-select-pressed.png`.

#### plan-card

Plan card. A pricing plan card (Free / Starter / Creator / Pro — name, price and action).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 262 x 739 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.tw-mb-3.tw-transition-colors: Inter 24px/32px 400, #000000, ls -0.24px |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | div.tw-absolute.tw-inset-0 262.0x200.0 bg #f5f3f1; div.tw-absolute.tw-mix-blend-overlay 262.0x200.0 image image-set(url(…) 1dppx type("image/avif"), url(…) 1dppx type("image/png")) r 16px; div.tw-absolute.tw-pointer-events-none 262.0x200.0 r 16px shadow #ffffff 0px 0px 0px 0px inset, #000000 @ 0.075 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px; a.tw-inline-flex.tw-items-center 262.0x44.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px; div 262.0x2.0 image repeating-radial-gradient(circle, #000000 @ 0.15 0px, #000000 @ 0.15 1px, #000000 @ 0 1px,; div 262.0x2.0 image repeating-radial-gradient(circle, #000000 @ 0.15 0px, #000000 @ 0.15 1px, #000000 @ 0 1px, |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. A plan card's price figure.

Page: pricing. Selector: `plan $ figure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 25.45 x 14.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/27px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's action (Build for free / Choose X); measured, never followed.

Page: pricing. Selector: `plan card CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 262 x 44 | = | = | 256.76 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #44403b | = | #44403b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 262.0x44.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 262.0x44.0 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 262.0x44.0 bg #000000 r 9999px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 256.8x43.1 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-badge

Plan badge. A badge on a plan card ("Popular" on Creator, "Until Nov 16" on Starter).

Page: pricing. Selector: `plan badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 89.22 x 21 |
| Padding | 4px 8px |
| Border | none |
| Radius | 9999px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Inter 13px/13px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | span.tw-inline-flex.tw-items-center 89.2x21.0 bg #000000 r 9999px |
| How | at rest |

Crops: `plan-badge-default.png`.

#### feature-row

Feature row. An "Everything in X, plus" feature-group row inside a plan card.

Page: pricing. Selector: `plan card feature row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1440 x 5508.61 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | a.tw-inline-flex.tw-items-center: Inter 14px/21px 400, #ffffff | = | h1.tw-block.tw-text-black: Waldenburg 48px/52px 300, #000000, ls -0.96px | = |
| Transition | none | = | = | = |
| Icon | 116 x 15, colour #000000 | = | = | = |
| Painted layers | div.tw-fixed.tw-top-0 1440.0x64.0 bg #ffffff; div.tw-absolute.tw-inset-x-0 1440.0x1.0 bg #ebe8e4; a.tw-h-9.tw-flex 140.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a.tw-inline-flex.tw-items-center 78.0x36.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px; div.tw-grid.tw-rounded-full 0.0x0.0 r 9999px shadow #ffffff 0px 0px 0px 0px inset, #d7d2cc 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px; a.tw-group/tab.tw-isolate 0.0x0.0 r 9999px outline 2px solid #000000 @ 0 offset 2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feature-row-default.png`, `feature-row-hover.png`, `feature-row-focus-visible.png`, `feature-row-pressed.png`.

#### faq-item

FAQ accordion. A FAQ accordion row under Compare plans; measured closed, never expanded.

Page: pricing. Selector: `FAQ button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 724 x 52.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-py-5.tw-type-lg: Inter 17px/25px 400, #000000, ls 0.17px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #a59f97 | 20 x 20, colour #000000 | = | 20 x 20, colour #000000 |
| Painted layers | button.tw-group/trigger.tw-text-left 724.0x52.5 r 4px outline 2px solid #000000 @ 0 offset 2px | = | button.tw-group/trigger.tw-text-left 724.0x52.5 r 4px outline 1px solid #2b7fff offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`.

### Text to Speech

#### tts-h1

Page title. The h1 on /text-to-speech (the small "Text to Speech" eyebrow above the big display).

Page: tts. Selector: `h1 on /text-to-speech`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1178 x 11 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/22px 500 |
| Letter spacing | 0.15px |
| Colour | #777169 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `tts-h1-default.png`.

#### google-login

Google login CTA. The "Log in with Google" action on the product hero; measured, never pressed — it would leave for the OAuth flow.

Page: tts. Selector: `Log in with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 207.09 x 44 | = | = | 202.95 x 43.12 |
| Padding | 0px 20px 0px 18px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #44403b | = | #44403b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 207.1x44.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 207.1x44.0 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 207.1x44.0 bg #000000 r 9999px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 203.0x43.1 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `google-login-default.png`, `google-login-hover.png`, `google-login-focus-visible.png`, `google-login-pressed.png`.

#### convert-cta

Convert CTA. The "Convert Text to Speech" action; measured, never followed.

Page: tts. Selector: `Convert Text to Speech`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 217.84 x 44 | = | = | 213.49 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #fdfcfc | = | #fdfcfc |
| Box shadow | #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 217.8x44.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 217.8x44.0 bg #fdfcfc r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 217.8x44.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 213.5x43.1 bg #fdfcfc r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `convert-cta-default.png`, `convert-cta-hover.png`, `convert-cta-focus-visible.png`, `convert-cta-pressed.png`.

#### voice-card

Voice sample card. A voice-sample card (the photo card with a corner play button and the voice name).

Page: tts. Selector: `voice card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 724 x 54.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.tw-py-5.tw-type-lg: Inter 17px/25px 400, #000000, ls 0.17px |
| Transition | none |
| Icon | 20 x 20, colour #a59f97 |
| Painted layers | button.tw-group/trigger.tw-text-left 724.0x54.5 r 4px outline 2px solid #000000 @ 0 offset 2px; div 724.0x2.0 image repeating-radial-gradient(circle, #000000 @ 0.15 0px, #000000 @ 0.15 1px, #000000 @ 0 1px, |
| How | at rest |

Crops: `voice-card-default.png`.

#### card-play

Sample play button. The corner play button on a voice-sample card; measured, audio never played here.

Page: tts. Selector: `button[aria-label^=Play]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 338.4 x 439.92 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 11.28 x 11.28, colour #000000 | = | = | = |
| Painted layers | button.tw-group/preview-button.tw-absolute 338.4x439.9 r 16px outline 2px solid #000000 @ 0 offset 2px; div.tw-absolute.tw-inset-0 41.4x41.4 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | button.tw-group/preview-button.tw-absolute 338.4x439.9 r 16px outline 1px solid #2b7fff offset 2px; div.tw-absolute.tw-inset-0 38.3x38.3 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = |
| Ancestor paint | 1 up div.tw-group/card.tw-@container bg #f5f3f1 | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `card-play-default.png`, `card-play-hover.png`, `card-play-focus-visible.png`, `card-play-pressed.png`.

#### try-voice

Try voice CTA. The "Try this voice" action under the voice cards; measured, never followed.

Page: tts. Selector: `Try this voice`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 141.33 x 48 | = | = | 138.5 x 47.04 |
| Padding | 0px 20px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #44403b | = | #44403b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.tw-inline-flex.tw-items-center 141.3x48.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.tw-inline-flex.tw-items-center 141.3x48.0 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px | button.tw-inline-flex.tw-items-center 141.3x48.0 bg #000000 r 9999px outline 1px solid #2b7fff offset 2px | button.tw-inline-flex.tw-items-center 138.5x47.0 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `try-voice-default.png`, `try-voice-hover.png`, `try-voice-focus-visible.png`, `try-voice-pressed.png`.

#### tts-display

Display heading. The "Text to Speech with high quality, human-like AI voices" display heading.

Page: tts. Selector: `tts display`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 565 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 36px/42px 300 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `tts-display-default.png`.

### API

#### api-h1

Page title. The "Build production-ready audio AI in minutes" display heading.

Page: api. Selector: `h1 on /api`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 563 x 86.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 48px/52px 300 |
| Letter spacing | -0.96px |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `api-h1-default.png`.

#### apikey-cta

Get API key CTA. The "Get API key" black pill; measured, never followed (it leads to sign-up).

Page: api. Selector: `Get API key`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.48 x 44 | = | = | 124.93 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #44403b | = | #44403b |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 127.5x44.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 127.5x44.0 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 127.5x44.0 bg #000000 r 9999px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 124.9x43.1 bg #44403b r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `apikey-cta-default.png`, `apikey-cta-hover.png`, `apikey-cta-focus-visible.png`, `apikey-cta-pressed.png`.

#### explore-docs

Explore docs. The "Explore docs" ghost pill; measured, never followed.

Page: api. Selector: `Explore docs`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.19 x 44 | = | = | 135.42 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #fdfcfc | = | #fdfcfc |
| Box shadow | #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 138.2x44.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 138.2x44.0 bg #fdfcfc r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.tw-inline-flex.tw-items-center 138.2x44.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 135.4x43.1 bg #fdfcfc r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `explore-docs-default.png`, `explore-docs-hover.png`, `explore-docs-focus-visible.png`, `explore-docs-pressed.png`.

#### demo-tab

Demo/Code tab. The Demo/Code toggle on the Text to Speech API card.

Page: api. Selector: `Demo Code toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75.31 x 40 | = | = | = |
| Padding | 0px 17px 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.tw-type-sm: Inter 15px/22px 400, #000000, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.tw-group/tab.tw-isolate 75.3x40.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; div.tw-absolute.-tw-z-10 68.3x34.0 bg #ebe8e4 r 9999px; div.tw-absolute.-tw-z-10 74.3x40.0 bg #ffffff r 9999px shadow #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | div.tw-group/tab.tw-isolate 75.3x40.0 r 9999px outline 1px solid #2b7fff offset 2px; div.tw-absolute.-tw-z-10 68.3x34.0 bg #ebe8e4 r 9999px; div.tw-absolute.-tw-z-10 74.3x40.0 bg #ffffff r 9999px shadow #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = |
| Ancestor paint | 1 up div.tw-grid.tw-rounded-full shadow #ffffff 0px 0px 0px 0px inset, #d7d2cc 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-tab-default.png`, `demo-tab-hover.png`, `demo-tab-focus-visible.png`, `demo-tab-pressed.png`.

### Docs

#### docs-h1

Docs title. The "ElevenLabs Documentation" heading.

Page: docs. Selector: `h1 on /docs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 467.75 x 45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 36px/45px 800 |
| Letter spacing | normal |
| Colour | #2a2a2a |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-search

Docs search. The docs search trigger in the top bar.

Page: docs. Selector: `docs Search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 632.63 x 36 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.06 | #000000 @ 0.004 | #000000 @ 0.06 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #404040 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.608 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | text | = | wait | = |
| Icon | 16 x 16, colour #000000 @ 0.608 | = | = | = |
| Painted layers | button.focus-visible:ring-(color:--accent).rounded-2 632.6x36.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; kbd.fern-kbd 21.2x22.0 bg #ffffff @ 0.8 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 6px | button.focus-visible:ring-(color:--accent).rounded-2 632.6x36.0 bg #000000 @ 0.06 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; kbd.fern-kbd 21.2x22.0 bg #ffffff @ 0.8 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 6px | button.focus-visible:ring-(color:--accent).rounded-2 632.6x36.0 bg #000000 @ 0.004 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #404040 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; kbd.fern-kbd 21.2x22.0 bg #ffffff @ 0.8 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 6px | button.focus-visible:ring-(color:--accent).rounded-2 632.6x36.0 bg #000000 @ 0.06 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; kbd.fern-kbd 21.2x22.0 bg #ffffff @ 0.8 border T:1px solid #000000 @ 0.15 / R:1px solid #000000 @ 0.15 / B:1px solid #000000 @ 0.15 / L:1px solid #000000 @ 0.15 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-nav-item

Docs nav item. A sidebar capability link (Text to Speech).

Page: docs. Selector: `docs sidebar link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 195 x 36 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.06 | = | #000000 @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #404040 offset 2px | = |
| Font | ui-sans-serif 14px/17.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.875 | = | = | = |
| Text node | span: ui-sans-serif 14px/17.5px 400, #000000 @ 0.875 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 @ 0.447 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.fern-sidebar-link.fern-sidebar-level-1 195.0x36.0 bg #000000 @ 0.06 r 8px | a.fern-sidebar-link.fern-sidebar-level-1 195.0x36.0 r 8px outline 2px solid #404040 offset 2px | a.fern-sidebar-link.fern-sidebar-level-1 195.0x36.0 bg #000000 @ 0.06 r 8px |

Crops: `docs-nav-item-default.png`, `docs-nav-item-hover.png`, `docs-nav-item-focus-visible.png`, `docs-nav-item-pressed.png`.

#### docs-copy-page

Copy page. The "Copy page" dropdown on the doc header.

Page: docs. Selector: `Copy page`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110.56 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | T: none; R: 1px solid #000000 @ 0.12; B: none; L: none | = | = | = |
| Radius | 8px 0px 0px 8px | = | 4px 0px 0px 4px | = |
| Background | transparent | #000000 @ 0.06 | #000000 @ 0.06 | #000000 @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.608 | #2a2a2a | #2a2a2a | #2a2a2a |
| Text node | span.animate-in.fade-in: ui-sans-serif 14px/20px 400, #000000 @ 0.608 | span.animate-in.fade-in: ui-sans-serif 14px/20px 400, #2a2a2a | span.animate-in.fade-in: ui-sans-serif 14px/20px 400, #2a2a2a | span.animate-in.fade-in: ui-sans-serif 14px/20px 400, #2a2a2a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 @ 0.608 | 16 x 16, colour #2a2a2a | 16 x 16, colour #2a2a2a | 16 x 16, colour #2a2a2a |
| Painted layers | button.w-fit.px-2 110.6x32.0 border R:1px solid #000000 @ 0.12 r 8px 0px 0px 8px | button.w-fit.px-2 110.6x32.0 bg #000000 @ 0.06 border R:1px solid #000000 @ 0.12 r 8px 0px 0px 8px | button.w-fit.px-2 110.6x32.0 bg #000000 @ 0.06 border R:1px solid #000000 @ 0.12 r 4px 0px 0px 4px | button.w-fit.px-2 110.6x32.0 bg #000000 @ 0.06 border R:1px solid #000000 @ 0.12 r 8px 0px 0px 8px |
| Ancestor paint | 1 up div.fern-page-actions shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-copy-page-default.png`, `docs-copy-page-hover.png`, `docs-copy-page-focus-visible.png`, `docs-copy-page-pressed.png`.

### Sign in and sign up

#### signin-card

Sign-in card. The sign-in card (Sign in with Google / Apple / SSO, email + password, the disabled submit); captured, never used.

Page: signin. Selector: `sign-in card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 519 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0f0f10 |
| Text node | h1.font-waldenburg-ht.text-2xl: WaldenburgHF 24px/30px 600, #0f0f10, ls -0.15px |
| Transition | none |
| Icon | 20 x 20, colour #2e2e2e |
| Painted layers | div.flex.flex-col 360.0x519.0 bg #ffffff; button.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.border-b.w-full 180.0x1.0 border B:1px solid #000000 @ 0.075; div.border-b.w-full 180.0x1.0 border B:1px solid #000000 @ 0.075 |
| How | at rest |

Crops: `signin-card-default.png`.

#### oauth-google

OAuth button. The "Sign in with Google" action; measured, never pressed — it would leave for the OAuth flow.

Page: signin. Selector: `Sign in with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 46 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | 1px solid #000000 @ 0.16 | = | 1px solid #000000 @ 0.16 |
| Radius | 12px | = | = | = |
| Background | #ffffff | #000000 @ 0.02 | = | #000000 @ 0.043 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #0f0f10 0px 0px 0px 3.5px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2e2e2e | = | = | = |
| Text node | span: Inter 14px/20px 500, #2e2e2e | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #2e2e2e | = | = | = |
| Painted layers | button.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.whitespace-nowrap.font-medium 360.0x46.0 bg #000000 @ 0.02 border T:1px solid #000000 @ 0.16 / R:1px solid #000000 @ 0.16 / B:1px solid #000000 @ 0.16 / L:1px solid #000000 @ 0.16 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #0f0f10 0px 0px 0px 3.5px, #000000 @ 0 0px 0px 0px 0px | button.whitespace-nowrap.font-medium 360.0x46.0 bg #000000 @ 0.043 border T:1px solid #000000 @ 0.16 / R:1px solid #000000 @ 0.16 / B:1px solid #000000 @ 0.16 / L:1px solid #000000 @ 0.16 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-google-default.png`, `oauth-google-hover.png`, `oauth-google-focus-visible.png`, `oauth-google-pressed.png`.

#### oauth-sso

SSO button. The "Sign in with SSO" action; measured, never pressed.

Page: signin. Selector: `Sign in with SSO`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 46 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | 1px solid #000000 @ 0.16 | = | 1px solid #000000 @ 0.16 |
| Radius | 12px | = | = | = |
| Background | #ffffff | #000000 @ 0.02 | = | #000000 @ 0.043 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #0f0f10 0px 0px 0px 3.5px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2e2e2e | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | a.whitespace-nowrap.font-medium 360.0x46.0 bg #000000 @ 0.02 border T:1px solid #000000 @ 0.16 / R:1px solid #000000 @ 0.16 / B:1px solid #000000 @ 0.16 / L:1px solid #000000 @ 0.16 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | a.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #0f0f10 0px 0px 0px 3.5px, #000000 @ 0 0px 0px 0px 0px | a.whitespace-nowrap.font-medium 360.0x46.0 bg #000000 @ 0.043 border T:1px solid #000000 @ 0.16 / R:1px solid #000000 @ 0.16 / B:1px solid #000000 @ 0.16 / L:1px solid #000000 @ 0.16 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-sso-default.png`, `oauth-sso-hover.png`, `oauth-sso-focus-visible.png`, `oauth-sso-pressed.png`.

#### email-field

Email field. The email input; focused and given sample text that was deleted again — nothing sent.

Page: signin. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 360 x 46 | = | = |
| Padding | 4px 16px | = | = |
| Border | 1px solid #000000 @ 0.1 | 1px solid #0f0f10 | 1px solid #0f0f10 |
| Radius | 12px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #0f0f10 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #0f0f10 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0f0f10 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #0f0f10, opacity 1 | = | = |
| Painted layers | input.flex.w-full 360.0x46.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | input.flex.w-full 360.0x46.0 border T:1px solid #0f0f10 / R:1px solid #0f0f10 / B:1px solid #0f0f10 / L:1px solid #0f0f10 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #0f0f10 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px | input.flex.w-full 360.0x46.0 border T:1px solid #0f0f10 / R:1px solid #0f0f10 / B:1px solid #0f0f10 / L:1px solid #0f0f10 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #0f0f10 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### password-field

Password field. The password input (with the visibility toggle); focused only — nothing typed, nothing sent.

Page: signin. Selector: `input[type=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 360 x 46 | = |
| Padding | 4px 40px 4px 16px | = |
| Border | 1px solid #000000 @ 0.1 | 1px solid #0f0f10 |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #0f0f10 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #0f0f10 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #0f0f10, opacity 1 | = |
| Painted layers | input.flex.w-full 360.0x46.0 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | input.flex.w-full 360.0x46.0 border T:1px solid #0f0f10 / R:1px solid #0f0f10 / B:1px solid #0f0f10 / L:1px solid #0f0f10 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, #0f0f10 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: `password-field-default.png`, `password-field-focused.png`.

#### signin-submit

Sign-in submit. The Sign in submit — disabled until the fields validate; measured, never pressed.

Page: signin. Selector: `Sign in submit`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 46 |
| Padding | 0px 12px |
| Gap | 10px |
| Border | none |
| Radius | 12px |
| Background | #a3a3a3 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 14px/20px 500 |
| Letter spacing | normal |
| Colour | #e3e3e3 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Painted layers | button.whitespace-nowrap.font-medium 360.0x46.0 bg #a3a3a3 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `signin-submit-default.png`.

#### forgot-link

Forgot link. The "Forgot your password?" link; measured, never followed.

Page: signin. Selector: `forgot password link`. States: .

Not found on the page at capture time.

#### signup-link

Sign-up link. The "Sign up" link under the card; measured, never followed.

Page: signin. Selector: `Sign up link`. States: .

Not found on the page at capture time.

#### signup-card

Sign-up card. The create-account card (SSO / Google, email + password, the ToS checkbox, the disabled submit); captured, never used.

Page: signup. Selector: `sign-up card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 601 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0f0f10 |
| Text node | h1.font-waldenburg-ht.text-2xl: WaldenburgHF 24px/30px 600, #0f0f10, ls -0.15px |
| Transition | none |
| Icon | 20 x 20, colour #2e2e2e |
| Painted layers | a.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button.whitespace-nowrap.font-medium 360.0x46.0 bg #ffffff border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.underline.decoration-[1.5px] 325.6x31.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3c83f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.underline.decoration-[1.5px] 80.3x15.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #3c83f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.border-b.w-full 180.0x1.0 border B:1px solid #000000 @ 0.075; div.border-b.w-full 180.0x1.0 border B:1px solid #000000 @ 0.075 |
| How | at rest |

Crops: `signup-card-default.png`.

#### tos-checkbox

ToS checkbox. The "I agree to the Terms of Service" checkbox; measured unchecked, never toggled.

Page: signup. Selector: `checkbox`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 16 x 16 | = |
| Padding | 0px | = |
| Border | 1px solid #b8b8b8 | = |
| Radius | 6px | = |
| Background | transparent | #000000 @ 0.86 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Inter 12px/16px 500 | = |
| Letter spacing | 0.03px | = |
| Colour | #000000 @ 0.714 | #ffffff |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | button.group/checkbox.relative 16.0x16.0 border T:1px solid #b8b8b8 / R:1px solid #b8b8b8 / B:1px solid #b8b8b8 / L:1px solid #b8b8b8 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/checkbox.relative 16.0x16.0 bg #000000 @ 0.86 border T:1px solid #b8b8b8 / R:1px solid #b8b8b8 / B:1px solid #b8b8b8 / L:1px solid #b8b8b8 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |
| Icon | - | 16 x 12, colour #ffffff |

Crops: `tos-checkbox-default.png`, `tos-checkbox-focused.png`.

#### signup-submit

Sign-up submit. The Sign up submit — disabled until the form validates; measured, never pressed.

Page: signup. Selector: `Sign up submit`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 46 |
| Padding | 0px 16px |
| Gap | 10px |
| Border | none |
| Radius | 12px |
| Background | #a3a3a3 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 14px/20px 500 |
| Letter spacing | normal |
| Colour | #e3e3e3 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Painted layers | button.whitespace-nowrap.font-medium 360.0x46.0 bg #a3a3a3 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `signup-submit-default.png`.

#### signin-link

Sign-in link. The "Already registered? Sign in" link under the sign-up card; measured, never followed.

Page: signup. Selector: `a[href=/app/sign-in]`. States: .

Not found on the page at capture time.

### Footer

#### footer

Footer. The footer (a 0x0 <footer> shell whose children paint the product/company/resources columns, social icons, language selector and legal).

Page: home. Selector: `footer contents`. States: .

Not found on the page at capture time.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: .

Not found on the page at capture time.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: .

Not found on the page at capture time.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 117 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/23.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 117 x 15, colour #000000 |
| Painted layers | a.tw-group.tw-outline-none 141.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; button.tw-group.tw-flex 0.0x0.0 outline 2px solid #000000 @ 0 offset 2px; button.tw-group.tw-flex 0.0x0.0 outline 2px solid #000000 @ 0 offset 2px; a.tw-group.tw-flex 0.0x0.0 outline 2px solid #000000 @ 0 offset 2px; button.tw-group.tw-flex 0.0x0.0 outline 2px solid #000000 @ 0 offset 2px; a.tw-group.tw-flex 0.0x0.0 outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The burger toggle that opens the mobile navigation sheet.

Page: mobile. Selector: `menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 6px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 17px/23.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #000000 |
| Painted layers | button.nav-topbar-item.tw-relative 36.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The opened mobile navigation sheet (the overlay holding the menu links and the auth actions).

Page: mobile. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 732 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/23.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.tw-inline-flex.tw-items-center: Inter 14px/21px 400, #ffffff |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 98) |
| Icon | 117 x 15, colour #000000 |
| Painted layers | div.tw-relative.tw-w-full 390.0x732.0 outline 2px solid #000000 @ 0 offset 2px; a.tw-group.tw-outline-none 141.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a.tw-items-center.tw-whitespace-nowrap 0.0x0.0 bg #ffffff r 9999px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px; a.tw-inline-flex.tw-items-center 78.0x36.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px; button.tw-relative.tw-rounded-full 36.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; nav.tw-w-full.tw-flex 382.0x728.0 bg #ffffff r 12px shadow #ffffff 0px 0px 0px 0px, #000000 @ 0.125 0px 0px 0px 0.5px, #000000 @ 0.04 0px 3px 6px -1.5px, #000000 @ 0.04 0px 12px 12px -6px, #000000 @ 0.04 0px 48px 48px -24px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A row inside the opened mobile menu.

Page: mobile. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 366 x 44 | = | = | = |
| Padding | 12px 12px 12px 16px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #a59f97 | = | = | = |
| Painted layers | button.tw-group.tw-flex 366.0x44.0 r 8px outline 2px solid #000000 @ 0 offset 2px | = | button.tw-group.tw-flex 366.0x44.0 r 8px outline 1px solid #2b7fff offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-signup

Mobile sign-up. The Sign up action inside the mobile menu; measured, never followed.

Page: mobile. Selector: `mobile menu Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.03 x 36 | = | = | 76.47 x 35.28 |
| Padding | 0px 14px | = | = | = |
| Gap | normal 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 1px solid #2b7fff offset 2px | = |
| Font | Inter 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.tw-inline-flex.tw-items-center 78.0x36.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | = | a.tw-inline-flex.tw-items-center 78.0x36.0 bg #000000 r 9999px outline 1px solid #2b7fff offset 2px | a.tw-inline-flex.tw-items-center 76.5x35.3 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `m-signup-default.png`, `m-signup-hover.png`, `m-signup-focus-visible.png`, `m-signup-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 36px/42px 300 |
| Letter spacing | -0.72px |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

elevenlabs.io serves its Tailwind 4 bundles cross-origin from eleven-public-cdn.elevenlabs.io, so the readable CSSOM holds only what the page itself exposes; this list covers the transition rules the page declares, and the per-state Transition rows above are the computed values the page paints.

- api: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- docs: `max-width 500ms ease-out`, `filter 0.3s`, `transform 200ms linear, opacity 200ms linear`, `none`, `background-color 0.15s ease-in-out, color 0.15s ease-in-out`, `opacity 0.12s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.12s cubic-bezier(0.2, 0.8, 0.2, 1), visibility linear 0.12s`, `opacity 0.12s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.12s cubic-bezier(0.2, 0.8, 0.2, 1), visibility`, `transform 0.2s`, `--toc-fill-top 0.25s ease-out, --toc-fill-bottom 0.25s ease-out`, `background-color 0.3s`, `transform 0.3s`, `--mask-left-stop 0.2s, --mask-right-stop 0.2s`

- home: `opacity 0.25s linear`

- pricing: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `opacity 0.25s linear`

- signin: `--uhint-fill var(--underline-duration,.275s) cubic-bezier(.68, -.08, .2, 1), background-position-x var(--underline-duration,.275s) cubic-bezier(.68, -.08, .2, 1)`, `--uhint-fill var(--underline-duration,.275s) cubic-bezier(.68, -.08, .2, 1) var(--underline-delay,0s), background-position-x var(--underline-duration,.275s) cubic-bezier(.68, -.08, .2, 1) var(--underline-delay,0s)`, `none`, `0.22s`, `transform var(--motion-overlay,.3s) cubic-bezier(.2,0,0,1),opacity var(--motion-content,.18s),height var(--motion-feedback,.12s)`, `opacity 0.2s`, `opacity 0.11s cubic-bezier(0.32, 0.05, 0.19, 1) 0.55s, left 0.33s cubic-bezier(0.32, 0.05, 0.19, 1) 0.55s`, `transform calc(var(--theme-toggle__expand--duration) * .65) cubic-bezier(0,0,0,1.25) calc(var(--theme-toggle__expand--duration) * .35)`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`

- signup: `--uhint-fill var(--underline-duration,.275s) cubic-bezier(.68, -.08, .2, 1), background-position-x var(--underline-duration,.275s) cubic-bezier(.68, -.08, .2, 1)`, `--uhint-fill var(--underline-duration,.275s) cubic-bezier(.68, -.08, .2, 1) var(--underline-delay,0s), background-position-x var(--underline-duration,.275s) cubic-bezier(.68, -.08, .2, 1) var(--underline-delay,0s)`, `none`, `0.22s`, `transform var(--motion-overlay,.3s) cubic-bezier(.2,0,0,1),opacity var(--motion-content,.18s),height var(--motion-feedback,.12s)`, `opacity 0.2s`, `opacity 0.11s cubic-bezier(0.32, 0.05, 0.19, 1) 0.55s, left 0.33s cubic-bezier(0.32, 0.05, 0.19, 1) 0.55s`, `transform calc(var(--theme-toggle__expand--duration) * .65) cubic-bezier(0,0,0,1.25) calc(var(--theme-toggle__expand--duration) * .35)`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`

- tts: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `opacity 0.25s linear`
