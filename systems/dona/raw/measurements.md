# Component measurements

Computed styles read from dona.ai on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /about, /privacy-policy and /terms-of-service — with the cookie banner hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### cookie-banner

Cookie banner. The "This website uses cookies." consent notice (Learn more / Accept); measured, then hidden — Accept was never clicked.

Page: home. Selector: `fixed cookie banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 496.28 x 76 |
| Padding | 18px |
| Border | none |
| Radius | 40px |
| Background | #ffffff |
| Box shadow | #0c1442 @ 0.03 0px 1px 3px 0px, #0c1442 @ 0.04 0px 8px 16px 0px, #0c1442 @ 0.04 0px 16px 40px 0px |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | div.Cookie__CookieText-sc-17bvojm-3.iIPEOD: Inter 16px/23.2px 400, #19191b |
| Transition | none |
| Icon | 40 x 40, colour #19191b |
| Painted layers | div.Cookie__Wrapper-sc-17bvojm-0.kduAzZ 496.3x76.0 bg #ffffff r 40px shadow #0c1442 @ 0.03 0px 1px 3px 0px, #0c1442 @ 0.04 0px 8px 16px 0px, #0c1442 @ 0.04 0px 16px 40px 0px; a::before 85.625pxx1px bg #19191b; button.Button__ButtonWrapper-sc-1eaeu1c-0.khZmSx 87.7x36.0 bg #eceff2 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset |
| How | at rest |

Crops: `cookie-banner-default.png`.

#### cookie-learn

Cookie "Learn more". The Learn more link inside the cookie banner (to /privacy-policy); measured, never followed.

Page: home. Selector: `cookie banner a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.63 x 23.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #19191b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 85.625px x 1px, absolute, bg #19191b, radius 0px | = | = | = |
| Painted layers | a::before 85.625pxx1px bg #19191b | = | a 85.6x23.2 outline 1px auto #005fcc offset 1px; a::before 85.625pxx1px bg #19191b | = |
| Ancestor paint | 3 up div.Cookie__Wrapper-sc-17bvojm-0.kduAzZ bg #ffffff shadow #0c1442 @ 0.03 0px 1px 3px 0px, #0c1442 @ 0.04 0px 8px 16px 0px, #0c1442 @ 0.04 0px 16px 40px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cookie-learn-default.png`, `cookie-learn-hover.png`, `cookie-learn-focus-visible.png`, `cookie-learn-pressed.png`.

#### cookie-accept

Cookie accept. The banner's Accept action; measured, never clicked — no consent was ever posted.

Page: home. Selector: `cookie banner Accept`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.66 x 36 | = | = | = |
| Padding | 6px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #eceff2 | #e9ecef | = | = |
| Background image | linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none | = | = | = |
| Box shadow | #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #19191b | = | = | = |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.dAKTtu: Inter 14px/24px 500, #19191b | = | = | = |
| Transition | color, background-color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.khZmSx 87.7x36.0 bg #eceff2 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | button.Button__ButtonWrapper-sc-1eaeu1c-0.fRmOnp 87.7x36.0 bg #e9ecef image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | = | = |
| Ancestor paint | 1 up div.Cookie__Wrapper-sc-17bvojm-0.kduAzZ bg #ffffff shadow #0c1442 @ 0.03 0px 1px 3px 0px, #0c1442 @ 0.04 0px 8px 16px 0px, #0c1442 @ 0.04 0px 16px 40px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cookie-accept-default.png`, `cookie-accept-hover.png`, `cookie-accept-focus-visible.png`, `cookie-accept-pressed.png`.

#### header

Header. The top bar: the About button, the centred dona wordmark and the Login action.

Page: home. Selector: `Header__Wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1100 x 68 |
| Padding | 32px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.dAKTtu: Inter 14px/24px 500, #19191b |
| Transition | none |
| Icon | 95.19 x 28, colour #0000ee, fill #000000 |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.cPTtUr 80.5x36.0 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px; button.Button__ButtonWrapper-sc-1eaeu1c-0.khZmSx 76.8x36.0 bg #eceff2 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The centred dona logo (ring mark + wordmark), inside an anchor to / whose own box is 0 wide.

Page: home. Selector: `Header__LogoLink svg`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.19 x 28 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/23.2px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0000ee | = | - | = |
| Transition | none | = | - | = |
| Transform | matrix(1, 0, 0, 1, -47.5938, 0) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 95.19 x 28, colour #0000ee, fill #000000 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `logo-default.png`, `logo-hover.png`, `logo-pressed.png`.

#### nav-about

About button. The header About action (routes to /about).

Page: home. Selector: `header button About`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.53 x 36 | = | = | = |
| Padding | 6px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | #f2f4f8 | = | = |
| Background image | linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #19191b | = | = | = |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.dAKTtu: Inter 14px/24px 500, #19191b | = | = | = |
| Transition | color, background-color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.cPTtUr 80.5x36.0 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px | button.Button__ButtonWrapper-sc-1eaeu1c-0.iMakCC 80.5x36.0 bg #f2f4f8 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-about-default.png`, `nav-about-hover.png`, `nav-about-focus-visible.png`, `nav-about-pressed.png`.

#### nav-login

Login button. The header Login action — opens https://app.dona.ai in a new tab; measured, never pressed.

Page: home. Selector: `header button Login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.83 x 36 | = | = | = |
| Padding | 6px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #eceff2 | #e9ecef | = | = |
| Background image | linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none | = | = | = |
| Box shadow | #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #19191b | = | = | = |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.dAKTtu: Inter 14px/24px 500, #19191b | = | = | = |
| Transition | color, background-color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.khZmSx 76.8x36.0 bg #eceff2 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | button.Button__ButtonWrapper-sc-1eaeu1c-0.fRmOnp 76.8x36.0 bg #e9ecef image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

### Home

#### hero-h1

Hero headline. The "A more humane / to-do list" display — the first line paints muted, the second ink.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 715 x 184.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 84px/92.4px 700 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | span: Inter 84px/92.4px 700, #19191b |
| Transition | opacity, transform 1s, 1s cubic-bezier(0.17, 0.17, 0, 1) delay 0s, 0s |
| Painted layers | span 644.8x101.0 bg #788088 image linear-gradient(to right, #d3d7db 50%, #b3cfff @ 0.7 100%) |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-lede

Hero lede. The "back to basic to-do list" paragraph under the headline.

Page: home. Selector: `Hero__Text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 660 x 69.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/34.8px 500 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | opacity, transform 1s, 1s cubic-bezier(0.17, 0.17, 0, 1) delay 0.05s |
| How | at rest |

Crops: `hero-lede-default.png`.

#### watch-video

Watch video button. The secondary pill with the play-triangle icon; opens the video modal.

Page: home. Selector: `button Watch video`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170.81 x 52 | = | = | = |
| Padding | 14px 26px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #eceff2 | #e9ecef | = | = |
| Background image | linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none | = | = | = |
| Box shadow | #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #19191b | = | = | = |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.bSJiAQ: Inter 16px/24px 500, #19191b | = | = | = |
| Transition | color, background-color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #19191b | = | = | = |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.fMSgPa 170.8x52.0 bg #eceff2 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | button.Button__ButtonWrapper-sc-1eaeu1c-0.fgBaeW 170.8x52.0 bg #e9ecef image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `watch-video-default.png`, `watch-video-hover.png`, `watch-video-focus-visible.png`, `watch-video-pressed.png`.

#### try-cta

Try for free button. The blue primary pill — opens https://app.dona.ai in a new tab; measured, never pressed.

Page: home. Selector: `button Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 157.58 x 52 | = | = | = |
| Padding | 14px 26px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #008ffd | #0087fd | = | = |
| Background image | linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none | = | = | = |
| Box shadow | #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.1 0px -1px 2px 0px inset | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.bSJiAQ: Inter 16px/24px 500, #ffffff | = | = | = |
| Transition | color, background-color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.iZlSaX 157.6x52.0 bg #008ffd image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.1 0px -1px 2px 0px inset | button.Button__ButtonWrapper-sc-1eaeu1c-0.HVeBd 157.6x52.0 bg #0087fd image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.1 0px -1px 2px 0px inset | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `try-cta-default.png`, `try-cta-hover.png`, `try-cta-focus-visible.png`, `try-cta-pressed.png`.

#### hero-video

Hero app frame. The autoplay product video under the CTAs (the Dona task UI in a rounded frame).

Page: home. Selector: `pages__Screen`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1100 x 688.52 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #eff2f5 |
| Box shadow | #0c1442 @ 0.02 0px 4px 12px 0px, #0c1442 @ 0.08 0px 30px 80px 0px, #e6e9ed 0px 0px 0px 1px inset |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | none |
| Painted layers | div.pages__Screen-sc-vcj8q7-0.epicbj 1100.0x688.5 bg #eff2f5 r 20px shadow #0c1442 @ 0.02 0px 4px 12px 0px, #0c1442 @ 0.08 0px 30px 80px 0px, #e6e9ed 0px 0px 0px 1px inset |
| How | at rest |

Crops: `hero-video-default.png`.

#### section-h2

Section heading. The "Fast & delightful user experience" section title.

Page: home. Selector: `h2 Fast & delightful`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 86.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/43.2px 600 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### section-h3

Feature heading. A feature tile's h3 ("Light, dark & black UI theme" / "Details matter").

Page: home. Selector: `h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 35.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 26px/35.1px 600 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | none |
| How | at rest |

Crops: `section-h3-default.png`.

#### section-para

Feature paragraph. A feature tile's body copy.

Page: home. Selector: `pages__Paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 104.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/26.1px 400 |
| Letter spacing | normal |
| Colour | #616870 |
| Transition | none |
| How | at rest |

Crops: `section-para-default.png`.

#### feature-tile

Feature tile. A half-width feature tile (headline + autoplay video).

Page: home. Selector: `pages__GridHalf`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 534 x 534 |
| Padding | 0px 0px 534px 0px |
| Border | none |
| Radius | 20px |
| Background | #f4f4f5 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | h3.Headline__Wrapper-sc-1nuat49-0.fcJpeS: Inter 26px/35.1px 600, #19191b |
| Transition | none |
| ::before | 534px x 106.797px, absolute, bg #008ffd, radius 75% |
| Painted layers | div.pages__GridHalf-sc-vcj8q7-4.iGOFBg 534.0x534.0 bg #f4f4f5 r 20px; div::before.pages__GridHalf-sc-vcj8q7-4.iGOFBg 534pxx106.797px bg #008ffd r 75%; div::before.pages__VideoTop-sc-vcj8q7-6.pages__VideoBottom-sc-vcj8q7-7 536pxx20px image linear-gradient(#f4f4f5, #f4f4f5 @ 0) |
| How | at rest |

Crops: `feature-tile-default.png`.

#### newsletter

Newsletter form. The email capture: the "Enter your email" field plus the "Join our newsletter" submit with the arrow-circle icon; measured, never submitted.

Page: home. Selector: `Newsletter__Wrapper form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1100 x 140 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | div.Submit__ButtonInner-sc-193h5k4-2.bpOavs: Inter 16px/24px 500, #ffffff |
| Transition | none |
| Icon | 30 x 30, colour #ffffff |
| ::before | 1650px x 42px, absolute, bg #008ffd, radius 75% |
| Painted layers | form::before.Newsletter__Wrapper-sc-1ivl8su-0.ePfgSy 1650pxx42px bg #008ffd r 75%; div::before.Submit__SubmitWrapper-sc-193h5k4-0.epAaVt 199.219pxx52px r 32px shadow #6fabff 0px 8px 140px 0px; button.Submit__ButtonWrapper-sc-193h5k4-1.fvJKjf 199.2x52.0 bg #19191b r 32px shadow #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.08 0px -1px 2px 0px inset, #000000 @ 0 0px 0px 0px 999px inset; span.inline 214.1x59.0 bg #788088 image linear-gradient(to right, #d3d7db 50%, #b3cfff @ 0.7 100%); button.Button__ButtonWrapper-sc-1eaeu1c-0.iZlSaX 228.9x52.0 bg #008ffd image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.1 0px -1px 2px 0px inset; button.Button__ButtonWrapper-sc-1eaeu1c-0.iZlSaX 289.8x52.0 bg #7289da image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.1 0px -1px 2px 0px inset |
| How | at rest |

Crops: `newsletter-default.png`.

#### email-input

Email field. The newsletter email input; focused and given sample text that was deleted again — the form was never submitted.

Page: home. Selector: `input[placeholder="Enter your email"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 1100 x 60 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 40px/60px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #19191b | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #bfc3c8, opacity 1 | #b0b5ba, opacity 1 | #b0b5ba, opacity 1 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-input-default.png`, `email-input-focused.png`, `email-input-filled.png`.

#### join-btn

Newsletter submit. The "Join our newsletter" submit button; measured — pressed state forced via DevTools, the button itself was never really pressed.

Page: home. Selector: `button Join our newsletter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 199.22 x 52 | = | = | = |
| Padding | 14px 26px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #19191b | = | = | = |
| Box shadow | #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.08 0px -1px 2px 0px inset, #000000 @ 0 0px 0px 0px 999px inset | #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.08 0px -1px 2px 0px inset, #000000 @ 0.5 0px 0px 0px 999px inset | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.Submit__ButtonInner-sc-193h5k4-2.bpOavs: Inter 16px/24px 500, #ffffff | = | = | = |
| Transition | background-color, box-shadow, padding 0.25s, 0.15s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 30 x 30, colour #ffffff | = | = | = |
| Painted layers | button.Submit__ButtonWrapper-sc-193h5k4-1.fvJKjf 199.2x52.0 bg #19191b r 32px shadow #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.08 0px -1px 2px 0px inset, #000000 @ 0 0px 0px 0px 999px inset | button.Submit__ButtonWrapper-sc-193h5k4-1.kjmZCj 199.2x52.0 bg #19191b r 32px shadow #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.08 0px -1px 2px 0px inset, #000000 @ 0.5 0px 0px 0px 999px inset | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `join-btn-default.png`, `join-btn-hover.png`, `join-btn-focus-visible.png`, `join-btn-pressed.png`.

#### video-modal

Video modal. The fixed overlay the Watch video button mounts: a YouTube iframe ("Say hello to Dona") on a dimmed page with a close button.

Page: home. Selector: `pages__Modal`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | #bfc3c8 @ 0.8 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | opacity 0.3s ease |
| Icon | 18 x 18, colour #ffffff |
| Painted layers | div.pages__Modal-sc-vcj8q7-9.fFVDGS 1440.0x900.0 bg #bfc3c8 @ 0.8; button.pages__Close-sc-vcj8q7-11.geCrA-D 56.0x56.0 bg #b0b5ba r 50%; div.pages__ModalInner-sc-vcj8q7-10.enpNFz 1140.0x641.3 r 11px shadow #000000 @ 0.05 0px 30px 130px 0px |
| How | at rest |

Crops: `video-modal-default.png`.

#### modal-close

Modal close. The close (x) control on the video modal.

Page: home. Selector: `modal close`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 50% | = | - | = |
| Background | #b0b5ba | #a8adb3 | - | #a8adb3 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/23.2px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | background-color 0.15s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 18 x 18, colour #ffffff | = | - | = |
| Painted layers | button.pages__Close-sc-vcj8q7-11.geCrA-D 56.0x56.0 bg #b0b5ba r 50% | button.pages__Close-sc-vcj8q7-11.geCrA-D 56.0x56.0 bg #a8adb3 r 50% | - | button.pages__Close-sc-vcj8q7-11.geCrA-D 56.0x56.0 bg #a8adb3 r 50% |
| Ancestor paint | 1 up div.pages__Modal-sc-vcj8q7-9.fFVDGS bg #bfc3c8 @ 0.8 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Error | - | = | contaminated reading: the pointer stayed over the button from the hover state (the spec ran noReset), so this measured the #a8adb3 hover fill, not a real focus style — re-measure queued | = |

Crops: `modal-close-default.png`, `modal-close-hover.png`, `modal-close-pressed.png`.

### About

#### about-h1

About headline. The "We’re building / to-do list you’ll enjoy using" display — muted first line, ink continuation.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 715 x 277.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 84px/92.4px 700 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | span: Inter 84px/92.4px 700, #19191b |
| Transition | opacity, transform 1s, 1s cubic-bezier(0.17, 0.17, 0, 1) delay 0s, 0s |
| Painted layers | span 584.4x101.0 bg #788088 image linear-gradient(to right, #d3d7db 50%, #b3cfff @ 0.7 100%) |
| How | at rest |

Crops: `about-h1-default.png`.

#### mission-text

Mission text. The mission paragraph; its second sentence paints muted (a span inside the paragraph).

Page: about. Selector: `Hero__Text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 660 x 173.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/34.8px 600 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | opacity, transform 1s, 1s cubic-bezier(0.17, 0.17, 0, 1) delay 0.05s |
| How | at rest |

Crops: `mission-text-default.png`.

#### team-h2

Team heading. The "Team" section title.

Page: about. Selector: `h2 Team`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 980 x 43.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/43.2px 600 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | none |
| Ancestor paint | 1 up div.about__About-sc-xipocs-0.hyzuIO bg #eff2f5 |
| How | at rest |

Crops: `team-h2-default.png`.

#### team-card

Team card. A team-member card: photo, name, one-line bio and social links (Jakub Antalik / Aaron Iker / Nisarg Patel).

Page: about. Selector: `about__Box`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 286.66 x 330.05 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/23.2px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #19191b | = | - | = |
| Text node | h4.Headline__Wrapper-sc-1nuat49-0.eeXSSv: Inter 18px/24.3px 600, #19191b | = | - | = |
| Transition | none | = | - | = |
| Icon | 16 x 16, colour #0000ee | = | - | = |
| Painted layers | a.about__Social-sc-xipocs-7.kgPcWG 40.0x40.0 bg #e0e3e7 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset; a.about__Social-sc-xipocs-7.kgPcWG 40.0x40.0 bg #e0e3e7 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `team-card-default.png`, `team-card-hover.png`, `team-card-pressed.png`.

#### team-avatar

Team avatar. A member photo inside the team card.

Page: about. Selector: `about__Avatar img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 125 x 125 |
| Padding | 0px |
| Border | none |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | none |
| How | at rest |

Crops: `team-avatar-default.png`.

#### social-link

Social link. A social link inside a team card (twitter / dribbble glyphs); measured, never followed.

Page: about. Selector: `about__Social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 14px | = | = | = |
| Background | #e0e3e7 | #dde0e4 | = | #dadde1 |
| Box shadow | #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | background-color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0000ee | = | = | 16 x 16, colour #ff0000 |
| Painted layers | a.about__Social-sc-xipocs-7.kgPcWG 40.0x40.0 bg #e0e3e7 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset | a.about__Social-sc-xipocs-7.kgPcWG 40.0x40.0 bg #dde0e4 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset | a.about__Social-sc-xipocs-7.kgPcWG 40.0x40.0 bg #e0e3e7 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset outline 1px auto #005fcc offset 1px | a.about__Social-sc-xipocs-7.kgPcWG 40.0x40.0 bg #dadde1 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-link-default.png`, `social-link-hover.png`, `social-link-focus-visible.png`, `social-link-pressed.png`.

### Legal pages

#### legal-h1

Legal heading. The "Privacy / policy" display on /privacy-policy; /terms-of-service is the same layout.

Page: privacy. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 624 x 184.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 84px/92.4px 700 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | span: Inter 84px/92.4px 700, #19191b |
| Transition | opacity, transform 1s, 1s cubic-bezier(0.17, 0.17, 0, 1) delay 0s, 0s |
| Painted layers | span 306.8x101.0 bg #788088 image linear-gradient(to right, #d3d7db 50%, #b3cfff @ 0.7 100%); span 248.9x101.0 bg #788088 image linear-gradient(to right, #d3d7db 50%, #b3cfff @ 0.7 100%) |
| How | at rest |

Crops: `legal-h1-default.png`.

#### legal-text

Legal paragraph. A body paragraph of the legal copy.

Page: privacy. Selector: `p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 46.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | none |
| How | at rest |

Crops: `legal-text-default.png`.

#### legal-h4

Legal subheading. A section subheading inside the legal copy ("Cookies", "Terms").

Page: privacy. Selector: `legal h3/h4`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 24.3 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/24.3px 600 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | none |
| How | at rest |

Crops: `legal-h4-default.png`.

#### legal-link

Legal link. A link inside the legal copy. The `div a` catch-all landed on the footer's 'Privacy policy' link (14px/20.3px), not a legal-body link, so no in-copy link was verified — the selector is now scoped to the legal content and the entry re-measures on the next capture.

Page: privacy. Selector: `legal a`. States: .

Not found on the page at capture time.

### Footer

#### footer

Footer. The footer: the copyright line, Terms of Service / Privacy policy links and the @getdona twitter link.

Page: home. Selector: `Footer__Wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 176.48 |
| Padding | 64px 0px |
| Border | T: 1px solid #eceff2; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | div.Footer__Info-sc-1jplr3t-2.kTiSaw: Inter 16px/23.2px 500, #616870 |
| Transition | none |
| Icon | 16 x 16, colour #0000ee |
| Painted layers | div.Footer__Wrapper-sc-1jplr3t-0.hXnCRd 1440.0x176.5 border T:1px solid #eceff2; a.Footer__Twitter-sc-1jplr3t-4.dAzrhN 40.0x40.0 bg #eceff2 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A legal link in the footer.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111.63 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20.3px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #19191b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 111.6x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-twitter

Twitter link. The @getdona icon link in the footer; measured, never followed.

Page: home. Selector: `footer twitter a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 14px | = | = | = |
| Background | #eceff2 | #e9ecef | = | #e6e9ed |
| Box shadow | #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/23.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | background-color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0000ee | = | = | 16 x 16, colour #ff0000 |
| Painted layers | a.Footer__Twitter-sc-1jplr3t-4.dAzrhN 40.0x40.0 bg #eceff2 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset | a.Footer__Twitter-sc-1jplr3t-4.dAzrhN 40.0x40.0 bg #e9ecef r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset | a.Footer__Twitter-sc-1jplr3t-4.dAzrhN 40.0x40.0 bg #eceff2 r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset outline 1px auto #005fcc offset 1px | a.Footer__Twitter-sc-1jplr3t-4.dAzrhN 40.0x40.0 bg #e6e9ed r 14px shadow #000000 @ 0.02 0px 2px 4px 0px, #000000 @ 0.03 0px -1px 2px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-twitter-default.png`, `footer-twitter-hover.png`, `footer-twitter-focus-visible.png`, `footer-twitter-pressed.png`.

### Mobile (390 wide)

#### m-cookie-banner

Cookie banner (mobile). The consent notice at 390 wide; hidden after its own reading, never answered. Note: the marked node read as a 555x64 fixed bar at top:1138px — offscreen in the 390x844 viewport and wider than it — and it never painted on the phone pass (the crop caught body text), so the real mobile placement is unverified.

Page: mobile. Selector: `fixed cookie banner at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 555 x 64 |
| Padding | 12px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #0c1442 @ 0.03 0px 1px 3px 0px, #0c1442 @ 0.04 0px -8px 16px 0px, #0c1442 @ 0.04 0px -16px 40px 0px |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | div.Cookie__CookieText-sc-17bvojm-3.iIPEOD: Inter 16px/23.2px 400, #19191b |
| Transition | none |
| Icon | 40 x 40, colour #19191b |
| Painted layers | div.Cookie__Wrapper-sc-17bvojm-0.kduAzZ 555.0x64.0 bg #ffffff shadow #0c1442 @ 0.03 0px 1px 3px 0px, #0c1442 @ 0.04 0px -8px 16px 0px, #0c1442 @ 0.04 0px -16px 40px 0px; a::before 85.625pxx1px bg #19191b; button.Button__ButtonWrapper-sc-1eaeu1c-0.khZmSx 87.7x36.0 bg #eceff2 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset |
| How | at rest |

Crops: `m-cookie-banner-default.png`.

#### m-header

Mobile header.

Page: mobile. Selector: `Header__Wrapper at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 68 |
| Padding | 32px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.dAKTtu: Inter 14px/24px 500, #19191b |
| Transition | none |
| Icon | 95.19 x 28, colour #0000ee, fill #000000 |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.cPTtUr 80.5x36.0 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px; button.Button__ButtonWrapper-sc-1eaeu1c-0.khZmSx 76.8x36.0 bg #eceff2 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/46px 700 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | span: Inter 40px/44px 700, #19191b |
| Transition | opacity, transform 1s, 1s cubic-bezier(0.17, 0.17, 0, 1) delay 0s, 0s |
| Painted layers | span 307.0x49.0 bg #788088 image linear-gradient(to right, #d3d7db 50%, #b3cfff @ 0.7 100%) |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-watch

Mobile Watch video.

Page: mobile. Selector: `Watch video at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 170.81 x 52 |
| Padding | 14px 26px |
| Border | none |
| Radius | 32px |
| Background | #eceff2 |
| Background image | linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none |
| Box shadow | #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | normal |
| Colour | #19191b |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.bSJiAQ: Inter 16px/24px 500, #19191b |
| Transition | color, background-color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | pointer |
| Icon | 16 x 16, colour #19191b |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.fMSgPa 170.8x52.0 bg #eceff2 image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.02 0px 2px 4px 0px, #0c1442 @ 0.03 0px -1px 2px 0px inset |
| How | at rest |

Crops: `m-watch-default.png`.

#### m-try

Mobile Try for free.

Page: mobile. Selector: `Try for free at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 157.58 x 52 |
| Padding | 14px 26px |
| Border | none |
| Radius | 32px |
| Background | #008ffd |
| Background image | linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none |
| Box shadow | #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.1 0px -1px 2px 0px inset |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.Button__ButtonInner-sc-1eaeu1c-1.bSJiAQ: Inter 16px/24px 500, #ffffff |
| Transition | color, background-color, box-shadow 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | pointer |
| Painted layers | button.Button__ButtonWrapper-sc-1eaeu1c-0.iZlSaX 157.6x52.0 bg #008ffd image linear-gradient(#ffffff @ 0.07 0%, #ffffff @ 0 100%), none r 32px shadow #0c1442 @ 0.1 0px 2px 4px 0px, #0c1442 @ 0.06 0px 10px 40px 0px, #0c1442 @ 0.1 0px -1px 2px 0px inset |
| How | at rest |

Crops: `m-try-default.png`.

#### m-email-input

Mobile email field.

Page: mobile. Selector: `newsletter input at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 28px/36px 400 |
| Letter spacing | normal |
| Colour | #19191b |
| Transition | none |
| Cursor | text |
| Placeholder | #bfc3c8, opacity 1 |
| How | at rest |

Crops: `m-email-input-default.png`.

## Transitions declared in the readable stylesheets

dona.ai is a Gatsby app styled with styled-components: its rules arrive as a same-origin linked bundle plus inline <style data-styled> tags, so the readable CSSOM holds everything the page paints. This list covers the transition rules the sheets declare; the per-state Transition rows above are the computed values.

- about: `color 0.15s, background-color 0.15s, box-shadow 0.15s`, `opacity 1s cubic-bezier(0.17, 0.17, 0, 1), transform 1s`, `opacity 1s cubic-bezier(0.17, 0.17, 0, 1) 50ms, transform 1s`, `background-color 0.15s`, `opacity 1s cubic-bezier(0.17, 0.17, 0, 1)`, `opacity 1.5s cubic-bezier(0.17, 0.17, 0, 1)`, `opacity 1s cubic-bezier(0.17, 0.17, 0, 1) 150ms, transform 1s`

- home: `stroke-dasharray 0.2s 0.15s, stroke-dashoffset 0.2s 0.15s`, `stroke-dasharray 0.3s, stroke-dashoffset 0.3s, opacity 0.3s`, `opacity 0.15s`, `color 0.15s, background-color 0.15s, box-shadow 0.15s`, `background-color 0.25s, box-shadow 0.15s, padding 0.3s`, `opacity 0.25s, transform 0.3s`, `opacity 1s cubic-bezier(0.17, 0.17, 0, 1), transform 1s`, `opacity 1s cubic-bezier(0.17, 0.17, 0, 1) 50ms, transform 1s`, `background-color 0.15s`, `opacity 1s cubic-bezier(0.17, 0.17, 0, 1)`, `opacity 1.5s cubic-bezier(0.17, 0.17, 0, 1)`, `color 0.15s`
