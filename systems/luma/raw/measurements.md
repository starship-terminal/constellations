# Component measurements: Luma

Computed styles read from luma.com on 2026-11-21 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). Marketing pages paint `html.theme-root.light`; the public event page paints `html.theme-root.dark` on its own. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Landing header. The marketing landing header: a spark mark and the Sign In pill. Inner pages add the wordmark and Discover Events.

Page: home. Selector: `header.landing-topnav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 58 |
| Padding | 14px 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #151515 |
| Text node | div.label: -apple-system 14px/14px 500, #151515 @ 0.64 |
| Transition | none |
| Icon | 20 x 20, colour #151515 @ 0.36 |
| Painted layers | a.btn.lux-button 67.0x30.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.jsx-938331401.page-wrapper bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### nav-signin

Sign In pill. The landing Sign In pill (light, round). It links to /signin; measured, never followed.

Page: home. Selector: `header a.lux-button "Sign In"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.95 x 30 | = | = | = |
| Padding | 7px 10px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #151515 @ 0 | = | 1px solid #151515 @ 0 |
| Radius | 15px | = | = | = |
| Background | #151515 @ 0.04 | #151515 @ 0.64 | = | #151515 @ 0.64 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #151515 @ 0.64 offset 2px | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.64 | #ffffff | = | #ffffff |
| Text node | div.label: -apple-system 14px/14px 500, #151515 @ 0.64 | div.label: -apple-system 14px/14px 500, #ffffff | = | div.label: -apple-system 14px/14px 500, #ffffff |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.lux-button 67.0x30.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | a.btn.lux-button 67.0x30.0 bg #151515 @ 0.64 border T:1px solid #151515 @ 0 / R:1px solid #151515 @ 0 / B:1px solid #151515 @ 0 / L:1px solid #151515 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | a.btn.lux-button 67.0x30.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #151515 @ 0.64 offset 2px | a.btn.lux-button 67.0x30.0 bg #151515 @ 0.64 border T:1px solid #151515 @ 0 / R:1px solid #151515 @ 0 / B:1px solid #151515 @ 0 / L:1px solid #151515 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### spark

Spark mark. The four-point spark in the landing header. It is not a link.

Page: home. Selector: `header .logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 20 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #151515 @ 0.36 |
| Transition | none |
| Icon | 20 x 20, colour #151515 @ 0.36 |
| How | at rest |

Crops: `spark-default.png`.

### Public event

#### nav-discover

Discover link. The Discover Events link in the inner-page header. Measured, never followed.

Page: event. Selector: `header a[href="/discover"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.52 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff @ 0.5 offset 4px | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.5 | #ffffff | = | #ffffff |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.min-width-0.text-ellipses 105.5x17.0 r 100px outline 2px solid #ffffff @ 0.5 offset 4px | = |

Crops: `nav-discover-default.png`, `nav-discover-hover.png`, `nav-discover-focus-visible.png`, `nav-discover-pressed.png`.

#### event-title

Event title. The event page title. The page paints theme-root.dark on its own.

Page: event. Selector: `event h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 566 x 87.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 38px/43.7px 575 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `event-title-default.png`.

#### event-signin

Event Sign In. The header Sign In control on the dark event page. Measured, never pressed.

Page: event. Selector: `event header Sign In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.95 x 30 | = | = | = |
| Padding | 7px 10px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #ffffff @ 0 | = | 1px solid #ffffff @ 0 |
| Radius | 15px | = | = | = |
| Background | #ffffff @ 0.08 | #ffffff @ 0.64 | = | #ffffff @ 0.64 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #ffffff @ 0.64 offset 2px | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.64 | #151515 | = | #151515 |
| Text node | div.label: -apple-system 14px/14px 500, #ffffff @ 0.64 | div.label: -apple-system 14px/14px 500, #151515 | = | div.label: -apple-system 14px/14px 500, #151515 |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.lux-button 67.0x30.0 bg #ffffff @ 0.08 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 67.0x30.0 bg #ffffff @ 0.64 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 67.0x30.0 bg #ffffff @ 0.08 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #ffffff @ 0.64 offset 2px | button.btn.lux-button 67.0x30.0 bg #ffffff @ 0.64 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `event-signin-default.png`, `event-signin-hover.png`, `event-signin-focus-visible.png`, `event-signin-pressed.png`.

#### host-card

Host card. The presented-by host block beside the event title.

Page: event. Selector: `.content-card host`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 330 x 125.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.jsx-3132294da94d8470.fs-xxs: -apple-system 12px/15.6px 400, #ffffff @ 0.79 |
| Transition | none |
| Icon | 16 x 16, colour #ffffff @ 0.5 |
| Painted layers | img.square.rounded 32.0x32.0 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px; button.btn.lux-button 64.4x30.0 bg #ffffff @ 0.08 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `host-card-default.png`.

#### host-follow

Host Follow. The host Follow button. Measured, never pressed (it asks for sign-in).

Page: event. Selector: `button "Follow"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.42 x 30 | = | = | = |
| Padding | 7px 10px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #ffffff @ 0 | = | 1px solid #ffffff @ 0 |
| Radius | 15px | = | = | = |
| Background | #ffffff @ 0.08 | #ffffff @ 0.64 | = | #ffffff @ 0.64 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #ffffff @ 0.64 offset 2px | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.64 | #011036 | = | #011036 |
| Text node | div.label: -apple-system 14px/14px 500, #ffffff @ 0.64 | div.label: -apple-system 14px/14px 500, #011036 | = | div.label: -apple-system 14px/14px 500, #011036 |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.lux-button 64.4x30.0 bg #ffffff @ 0.08 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 64.4x30.0 bg #ffffff @ 0.64 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 64.4x30.0 bg #ffffff @ 0.08 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #ffffff @ 0.64 offset 2px | button.btn.lux-button 64.4x30.0 bg #ffffff @ 0.64 border T:1px solid #ffffff @ 0 / R:1px solid #ffffff @ 0 / B:1px solid #ffffff @ 0 / L:1px solid #ffffff @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `host-follow-default.png`, `host-follow-hover.png`, `host-follow-focus-visible.png`, `host-follow-pressed.png`.

#### event-meta

Location row. The place row. It links out to a map; measured, never followed.

Page: event. Selector: `location row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 233.31 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #e6efff |
| Text node | div.jsx-716bec2817eb1288.text-ellipses: Google Sans Flex 16px/24px 475, #ffffff |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 20 x 20, colour #ffffff @ 0.79, fill #000000 |
| Painted layers | div.jsx-100837539.icon-container 40.0x40.0 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px |
| How | at rest |

Crops: `event-meta-default.png`.

#### wordmark

Wordmark. The luma wordmark on an inner page. It links home; measured, never followed.

Page: event. Selector: `a[aria-label="Luma Home"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 43.88 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f98dbe |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 43.88 x 16, colour #ffffff @ 0.5, fill #000000 |
| How | at rest |

Crops: `wordmark-default.png`.

### Home hero

#### hero-title

Hero title. The 80px landing title, "Delightful events start here". A second painted copy ("Stellar") sits in a dark island and is not this atom.

Page: home. Selector: `h1.landing-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 365.25 x 273.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 80px/73.6px 500 |
| Letter spacing | -0.8px |
| Colour | #151515 |
| Text node | div.jsx-3564931177.landing-title-rise: -apple-system 80px/73.6px 500, #151515, ls -0.8px |
| Transition | none |
| Icon | 80 x 29.16, colour #151515 @ 0.36, fill #000000 |
| Painted layers | span.gradient-text 343.5x118.0 image radial-gradient(circle at 0.15em 0.15em, #ab46dd 0%, #f31a7c 36%, #f8712b 51%, #eaab26 77% |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero lede. The sentence under the landing title.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 20px/30px 400 |
| Letter spacing | normal |
| Colour | #151515 @ 0.36 |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### cta-create

Create event button. The black Create Your First Event pill. It links to /create, which opens a sign-in dialog; measured, never followed.

Page: home. Selector: `a.create-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 223.78 x 45 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | 2px solid #000000 @ 0 | 2px solid #ffffff @ 0.16 | = | 2px solid #ffffff @ 0.16 |
| Radius | 100px | = | = | = |
| Background | #151515 | #ffffff @ 0.16 | = | #ffffff @ 0.16 |
| Box shadow | #000000 @ 0.03 0px 3px 3px 0px, #000000 @ 0.04 0px 8px 7px 0px, #000000 @ 0.05 0px 17px 14px 0px, #000000 @ 0.06 0px 35px 29px 0px, #000000 @ 0.07 0px 96px 80px 0px | none | = | none |
| Backdrop filter | blur(16px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 18px/27px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.create-button 223.8x45.0 bg #151515 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 100px shadow #000000 @ 0.03 0px 3px 3px 0px, #000000 @ 0.04 0px 8px 7px 0px, #000000 @ 0.05 0px 17px 14px 0px, #000000 @ 0.06 0px 35px 29px 0px, #000000 @ 0.07 0px 96px 80px 0px | a.create-button 223.8x45.0 bg #ffffff @ 0.16 border T:2px solid #ffffff @ 0.16 / R:2px solid #ffffff @ 0.16 / B:2px solid #ffffff @ 0.16 / L:2px solid #ffffff @ 0.16 r 100px | a.create-button 223.8x45.0 bg #151515 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 100px shadow #000000 @ 0.03 0px 3px 3px 0px, #000000 @ 0.04 0px 8px 7px 0px, #000000 @ 0.05 0px 17px 14px 0px, #000000 @ 0.06 0px 35px 29px 0px, #000000 @ 0.07 0px 96px 80px 0px outline 1px auto #005fcc offset 1px | a.create-button 223.8x45.0 bg #ffffff @ 0.16 border T:2px solid #ffffff @ 0.16 / R:2px solid #ffffff @ 0.16 / B:2px solid #ffffff @ 0.16 / L:2px solid #ffffff @ 0.16 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-create-default.png`, `cta-create-hover.png`, `cta-create-focus-visible.png`, `cta-create-pressed.png`.

#### cta-discover

Discover Events button. The secondary Discover Events action under the hero.

Page: home. Selector: `a "Discover Events"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 141.02 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 6px | = | 2px solid #959595 offset 6px | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.36 | #151515 @ 0.64 | = | #151515 @ 0.64 |
| Text node | div.label: -apple-system 16px/16px 500, #151515 @ 0.36 | div.label: -apple-system 16px/16px 500, #151515 @ 0.64 | = | div.label: -apple-system 16px/16px 500, #151515 @ 0.64 |
| Transition | color 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14.53 x 14.53, colour #151515 @ 0.36, fill #000000 | 14.53 x 14.53, colour #151515 @ 0.64, fill #000000 | = | 14.53 x 14.53, colour #151515 @ 0.64, fill #000000 |
| Painted layers | a.btn.lux-button 141.0x16.0 outline 2px solid #000000 @ 0 offset 6px | = | a.btn.lux-button 141.0x16.0 outline 2px solid #959595 offset 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-discover-default.png`, `cta-discover-hover.png`, `cta-discover-focus-visible.png`, `cta-discover-pressed.png`.

### Home

#### event-card

Event row. A popular-events row on the home page. The row was measured, never opened.

Page: home. Selector: `home event row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 146.66 x 225.27 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #151515 | #6f802b |
| Text node | div.jsx-1763356283.lux-line-clamp: -apple-system 16px/20.8px 500, #151515 | div.jsx-1763356283.lux-line-clamp: -apple-system 16px/20.8px 500, #6f802b |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | div.jsx-1092221a26d8459c.cover 146.7x146.7 bg #151515 @ 0.04 r 24px; div.jsx-bf40f23d3e10e809.img-aspect-ratio 146.7x146.7 bg #151515 @ 0.04 r 16px | div.jsx-1092221a26d8459c.cover 150.3x150.3 bg #151515 @ 0.04 r 24px; div.jsx-bf40f23d3e10e809.img-aspect-ratio 150.3x150.3 bg #151515 @ 0.04 r 16px |
| How | at rest | mouse hover |

Crops: `event-card-default.png`, `event-card-hover.png`.

### Pricing

#### pricing-title

Pricing title. The 60px Pricing heading.

Page: pricing. Selector: `h1 "Pricing"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 186.36 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 60px/72px 600 |
| Letter spacing | normal |
| Colour | #151515 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-monthly

Monthly segment. The Monthly half of the billing segment. Toggled as local UI; nothing was purchased.

Page: pricing. Selector: `button.segment "Monthly"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.13 x 34 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.36 | #151515 | = | #151515 |
| Text node | div: -apple-system 16px/24px 500, #151515 @ 0.36 | div: -apple-system 16px/24px 500, #151515 | = | div: -apple-system 16px/24px 500, #151515 |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 84.125px x 32px, absolute, bg #000000 @ 0, radius 100px | = | = | = |
| Painted layers | button.btn.segment 86.1x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::after.btn.segment 84.125pxx32px r 100px outline 2px solid #000000 @ 0 offset 0px | = | button.btn.segment 86.1x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::after.btn.segment 84.125pxx32px r 100px outline 2px solid #151515 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-monthly-default.png`, `billing-monthly-hover.png`, `billing-monthly-focus-visible.png`, `billing-monthly-pressed.png`.

#### billing-annual

Annual segment. The Annual half of the billing segment, selected at rest on this load.

Page: pricing. Selector: `button.segment "Annual"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.13 x 34 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 | = | = | = |
| Text node | div: -apple-system 16px/24px 500, #151515 | = | = | = |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 0px x 24px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 84.125px x 32px, absolute, bg #000000 @ 0, radius 100px | = | = | = |
| Painted layers | button.btn.segment 86.1x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::after.btn.segment 84.125pxx32px r 100px outline 2px solid #000000 @ 0 offset 0px | = | button.btn.segment 86.1x34.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0; button::after.btn.segment 84.125pxx32px r 100px outline 2px solid #151515 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-annual-default.png`, `billing-annual-hover.png`, `billing-annual-focus-visible.png`, `billing-annual-pressed.png`.

#### plan-card

Free plan card. The free plan card: 24px radius, white surface.

Page: pricing. Selector: `.content-card free plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 448 x 845 |
| Padding | 18px 20px |
| Border | 1px solid #ffffff |
| Radius | 24px |
| Background | #ffffff @ 0.8 |
| Box shadow | #000000 @ 0.01 0px 0.7px 2.7px 0px, #000000 @ 0.016 0px 1.7px 6.9px 0px, #000000 @ 0.02 0px 3.5px 14.2px 0px, #000000 @ 0.024 0px 7.3px 29.2px 0px |
| Backdrop filter | blur(16px) |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #151515 |
| Text node | div.jsx-3541755089.title: -apple-system 18px/27px 600, #151515 |
| Transition | none |
| Icon | 16 x 16, colour #151515, fill #000000 |
| Painted layers | div.jsx-702bb7b3285aa34f.jsx-3763758620 448.0x845.0 bg #ffffff @ 0.8 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 24px shadow #000000 @ 0.01 0px 0.7px 2.7px 0px, #000000 @ 0.016 0px 1.7px 6.9px 0px, #000000 @ 0.02 0px 3.5px 14.2px 0px, #000000 @ 0.024 0px 7.3px 29.2px 0px; a.btn.lux-button 406.0x38.0 bg #353535 border T:1px solid #353535 / R:1px solid #353535 / B:1px solid #353535 / L:1px solid #353535 r 16px outline 2px solid #000000 @ 0 offset 2px; hr.jsx-3694859080 378.0x1.0 border B:1px solid #151515 @ 0.08; hr.jsx-3694859080 378.0x1.0 border B:1px solid #151515 @ 0.08 |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-plus

Plus plan card. The Luma Plus plan card. Get Luma Plus was measured, never followed (it is a sign-in checkout).

Page: pricing. Selector: `.content-card plus plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 448 x 845 |
| Padding | 18px 20px |
| Border | 1px solid #ffffff |
| Radius | 24px |
| Background | #ffffff @ 0.8 |
| Box shadow | #000000 @ 0.01 0px 0.7px 2.7px 0px, #000000 @ 0.016 0px 1.7px 6.9px 0px, #000000 @ 0.02 0px 3.5px 14.2px 0px, #000000 @ 0.024 0px 7.3px 29.2px 0px |
| Backdrop filter | blur(16px) |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #151515 |
| Text node | div.jsx-3694859080.luma-plus: -apple-system 18px/27px 600, #f31a7c |
| Transition | none |
| Icon | 16 x 16, colour #151515, fill #000000 |
| Painted layers | div.jsx-702bb7b3285aa34f.jsx-3763758620 448.0x845.0 bg #ffffff @ 0.8 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 24px shadow #000000 @ 0.01 0px 0.7px 2.7px 0px, #000000 @ 0.016 0px 1.7px 6.9px 0px, #000000 @ 0.02 0px 3.5px 14.2px 0px, #000000 @ 0.024 0px 7.3px 29.2px 0px; div.jsx-16ad4d648c7a0666.pill 82.4x24.0 bg #f31a7c @ 0.133 r 4px; a.btn.lux-button 406.0x38.0 bg #f31a7c border T:1px solid #f31a7c / R:1px solid #f31a7c / B:1px solid #f31a7c / L:1px solid #f31a7c r 16px outline 2px solid #000000 @ 0 offset 2px; hr.jsx-3694859080 378.0x1.0 border B:1px solid #151515 @ 0.08; hr.jsx-3694859080 378.0x1.0 border B:1px solid #151515 @ 0.08 |
| How | at rest |

Crops: `plan-card-plus-default.png`.

#### plan-cta

Get Started button. The primary plan button (near-black fill, 16px radius). It links to sign-in; measured, never followed.

Page: pricing. Selector: `a.lux-button.primary "Get Started"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 406 x 38 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Border | 1px solid #353535 | 1px solid #555555 | = | 1px solid #555555 |
| Radius | 16px | = | = | = |
| Background | #353535 | #555555 | = | #555555 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #353535 offset 2px | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.label: -apple-system 16px/16px 500, #ffffff | = | = | = |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.lux-button 406.0x38.0 bg #353535 border T:1px solid #353535 / R:1px solid #353535 / B:1px solid #353535 / L:1px solid #353535 r 16px outline 2px solid #000000 @ 0 offset 2px | a.btn.lux-button 406.0x38.0 bg #555555 border T:1px solid #555555 / R:1px solid #555555 / B:1px solid #555555 / L:1px solid #555555 r 16px outline 2px solid #000000 @ 0 offset 2px | a.btn.lux-button 406.0x38.0 bg #353535 border T:1px solid #353535 / R:1px solid #353535 / B:1px solid #353535 / L:1px solid #353535 r 16px outline 2px solid #353535 offset 2px | a.btn.lux-button 406.0x38.0 bg #555555 border T:1px solid #555555 / R:1px solid #555555 / B:1px solid #555555 / L:1px solid #555555 r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-cta-brand

Get Luma Plus button. The brand button (#f31a7c, 16px radius). It links to calendar checkout; measured, never followed.

Page: pricing. Selector: `a.lux-button.brand "Get Luma Plus"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 406 x 38 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Border | 1px solid #f31a7c | 1px solid #d5176d | = | 1px solid #d5176d |
| Radius | 16px | = | = | = |
| Background | #f31a7c | #d5176d | = | #d5176d |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #f31a7c offset 2px | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.label: -apple-system 16px/16px 500, #ffffff | = | = | = |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.lux-button 406.0x38.0 bg #f31a7c border T:1px solid #f31a7c / R:1px solid #f31a7c / B:1px solid #f31a7c / L:1px solid #f31a7c r 16px outline 2px solid #000000 @ 0 offset 2px | a.btn.lux-button 406.0x38.0 bg #d5176d border T:1px solid #d5176d / R:1px solid #d5176d / B:1px solid #d5176d / L:1px solid #d5176d r 16px outline 2px solid #000000 @ 0 offset 2px | a.btn.lux-button 406.0x38.0 bg #f31a7c border T:1px solid #f31a7c / R:1px solid #f31a7c / B:1px solid #f31a7c / L:1px solid #f31a7c r 16px outline 2px solid #f31a7c offset 2px | a.btn.lux-button 406.0x38.0 bg #d5176d border T:1px solid #d5176d / R:1px solid #d5176d / B:1px solid #d5176d / L:1px solid #d5176d r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-brand-default.png`, `plan-cta-brand-hover.png`, `plan-cta-brand-focus-visible.png`, `plan-cta-brand-pressed.png`.

### Discover

#### discover-title

Discover title. The Discover Events heading.

Page: discover. Selector: `h1 Discover`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 788 x 33.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 28px/33.6px 600 |
| Letter spacing | normal |
| Colour | #151515 |
| Transition | none |
| How | at rest |

Crops: `discover-title-default.png`.

#### category-card

Category card. A browse-by-category card (Family, Books, …). Measured, never followed.

Page: discover. Selector: `a.content-card category`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 252 x 66 | = |
| Padding | 8px 16px 8px 4px | = |
| Border | 1px solid #ffffff | 1px solid #151515 @ 0.16 |
| Radius | 24px | = |
| Background | #ffffff @ 0.8 | = |
| Box shadow | none | #000000 @ 0.004 0px 28px 17px 0px, #000000 @ 0.01 0px 12px 12px 0px, #000000 @ 0.01 0px 3px 7px 0px, #000000 @ 0.01 0px 0px 0px 0px |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #151515 | = |
| Text node | div.jsx-96134204.title: -apple-system 16px/24px 500, #151515 | = |
| Transition | border-color, box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.jsx-702bb7b3285aa34f.jsx-3763758620 252.0x66.0 bg #ffffff @ 0.8 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 24px | a.jsx-702bb7b3285aa34f.jsx-3763758620 252.0x66.0 bg #ffffff @ 0.8 border T:1px solid #151515 @ 0.16 / R:1px solid #151515 @ 0.16 / B:1px solid #151515 @ 0.16 / L:1px solid #151515 @ 0.16 r 24px shadow #000000 @ 0.004 0px 28px 17px 0px, #000000 @ 0.01 0px 12px 12px 0px, #000000 @ 0.01 0px 3px 7px 0px, #000000 @ 0.01 0px 0px 0px 0px |
| How | at rest | mouse hover |

Crops: `category-card-default.png`, `category-card-hover.png`.

#### follow-button

Follow button. A calendar Follow button. Measured, never pressed (pressing asks for sign-in).

Page: discover. Selector: `button "Follow"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.42 x 30 | = | = | = |
| Padding | 7px 10px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #151515 @ 0 | = | 1px solid #151515 @ 0 |
| Radius | 15px | = | = | = |
| Background | #151515 @ 0.04 | #151515 @ 0.64 | = | #151515 @ 0.64 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #151515 @ 0.64 offset 2px | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.64 | #ffffff | = | #ffffff |
| Text node | div.label: -apple-system 14px/14px 500, #151515 @ 0.64 | div.label: -apple-system 14px/14px 500, #ffffff | = | div.label: -apple-system 14px/14px 500, #ffffff |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.lux-button 64.4x30.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 64.4x30.0 bg #151515 @ 0.64 border T:1px solid #151515 @ 0 / R:1px solid #151515 @ 0 / B:1px solid #151515 @ 0 / L:1px solid #151515 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 64.4x30.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #151515 @ 0.64 offset 2px | button.btn.lux-button 64.4x30.0 bg #151515 @ 0.64 border T:1px solid #151515 @ 0 / R:1px solid #151515 @ 0 / B:1px solid #151515 @ 0 / L:1px solid #151515 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 2 up a.jsx-702bb7b3285aa34f.jsx-3763758620 bg #ffffff @ 0.8 shadow #000000 @ 0.004 0px 28px 17px 0px, #000000 @ 0.01 0px 12px 12px 0px, #000000 @ 0.01 0px 3px 7px 0px, #000000 @ 0.01 0px 0px 0px 0px | = | = |

Crops: `follow-button-default.png`, `follow-button-hover.png`, `follow-button-focus-visible.png`, `follow-button-pressed.png`.

### Sign in

#### signin-title

Sign-in title. The Welcome to Luma heading on the sign-in card. Nothing was submitted.

Page: signin. Selector: `h3 "Welcome to Luma"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 20px/24px 600 |
| Letter spacing | normal |
| Colour | #151515 |
| Transition | none |
| How | at rest |

Crops: `signin-title-default.png`.

#### email-field

Email field. The email input (8px radius). Sample text was typed and deleted. Continue was never pressed.

Page: signin. Selector: `input.lux-input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 320 x 38 | = | = |
| Padding | 10px 14px | = | = |
| Border | 1px solid #151515 @ 0.08 | 1px solid #151515 | 1px solid #151515 |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Background image | -webkit-linear-gradient(top, #ffffff @ 0, #ffffff @ 0) | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system 16px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #151515 | = | = |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #151515 @ 0.32, opacity 1 | = | = |
| Painted layers | input.lux-input 320.0x38.0 bg #ffffff image -webkit-linear-gradient(top, #ffffff @ 0, #ffffff @ 0) border T:1px solid #151515 @ 0.08 / R:1px solid #151515 @ 0.08 / B:1px solid #151515 @ 0.08 / L:1px solid #151515 @ 0.08 r 8px | input.lux-input 320.0x38.0 bg #ffffff image -webkit-linear-gradient(top, #ffffff @ 0, #ffffff @ 0) border T:1px solid #151515 / R:1px solid #151515 / B:1px solid #151515 / L:1px solid #151515 r 8px | input.lux-input 320.0x38.0 bg #ffffff image -webkit-linear-gradient(top, #ffffff @ 0, #ffffff @ 0) border T:1px solid #151515 / R:1px solid #151515 / B:1px solid #151515 / L:1px solid #151515 r 8px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### phone-toggle

Use Phone Number. The link-styled toggle that swaps the email field for a phone field. Measured, never pressed.

Page: signin. Selector: `button "Use Phone Number"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146.34 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 6px | = | 2px solid #959595 offset 6px | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.36 | #151515 @ 0.64 | = | #151515 @ 0.64 |
| Text node | div.label: -apple-system 14px/14px 500, #151515 @ 0.36 | div.label: -apple-system 14px/14px 500, #151515 @ 0.64 | = | div.label: -apple-system 14px/14px 500, #151515 @ 0.64 |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12.72 x 12.72, colour #151515 @ 0.36, fill #000000 | 12.72 x 12.72, colour #151515 @ 0.64, fill #000000 | = | 12.72 x 12.72, colour #151515 @ 0.64, fill #000000 |
| Painted layers | button.btn.lux-button 146.3x14.0 outline 2px solid #000000 @ 0 offset 6px | = | button.btn.lux-button 146.3x14.0 outline 2px solid #959595 offset 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `phone-toggle-default.png`, `phone-toggle-hover.png`, `phone-toggle-focus-visible.png`, `phone-toggle-pressed.png`.

#### continue-btn

Continue with Email. The primary submit. Measured with CDP :active only, so the form was never submitted.

Page: signin. Selector: `button[type=submit] "Continue with Email"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 38 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Border | 1px solid #353535 | 1px solid #555555 | = | 1px solid #555555 |
| Radius | 16px | = | = | = |
| Background | #353535 | #555555 | = | #555555 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #353535 offset 2px | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.label: -apple-system 16px/16px 500, #ffffff | = | = | = |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.lux-button 320.0x38.0 bg #353535 border T:1px solid #353535 / R:1px solid #353535 / B:1px solid #353535 / L:1px solid #353535 r 16px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 320.0x38.0 bg #555555 border T:1px solid #555555 / R:1px solid #555555 / B:1px solid #555555 / L:1px solid #555555 r 16px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 320.0x38.0 bg #353535 border T:1px solid #353535 / R:1px solid #353535 / B:1px solid #353535 / L:1px solid #353535 r 16px outline 2px solid #353535 offset 2px | button.btn.lux-button 320.0x38.0 bg #555555 border T:1px solid #555555 / R:1px solid #555555 / B:1px solid #555555 / L:1px solid #555555 r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `continue-btn-default.png`, `continue-btn-hover.png`, `continue-btn-focus-visible.png`, `continue-btn-pressed.png`.

#### google-btn

Sign in with Google. The Google button. Measured, never pressed.

Page: signin. Selector: `button "Sign in with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 38 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #151515 @ 0 | = | 1px solid #151515 @ 0 |
| Radius | 16px | = | = | = |
| Background | #151515 @ 0.04 | #151515 @ 0.64 | = | #151515 @ 0.64 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #151515 @ 0.64 offset 2px | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.64 | #ffffff | = | #ffffff |
| Text node | div.label: -apple-system 16px/16px 500, #151515 @ 0.64 | div.label: -apple-system 16px/16px 500, #ffffff | = | div.label: -apple-system 16px/16px 500, #ffffff |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #151515 @ 0.64, fill #000000 | 16 x 16, colour #ffffff, fill #000000 | = | 16 x 16, colour #ffffff, fill #000000 |
| Painted layers | button.btn.lux-button 320.0x38.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 320.0x38.0 bg #151515 @ 0.64 border T:1px solid #151515 @ 0 / R:1px solid #151515 @ 0 / B:1px solid #151515 @ 0 / L:1px solid #151515 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 320.0x38.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px outline 2px solid #151515 @ 0.64 offset 2px | button.btn.lux-button 320.0x38.0 bg #151515 @ 0.64 border T:1px solid #151515 @ 0 / R:1px solid #151515 @ 0 / B:1px solid #151515 @ 0 / L:1px solid #151515 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `google-btn-default.png`, `google-btn-hover.png`, `google-btn-focus-visible.png`, `google-btn-pressed.png`.

#### passkey-btn

Sign in with Passkey. The passkey button. Measured, never pressed.

Page: signin. Selector: `button "Sign in with Passkey"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 38 | = | = | = |
| Padding | 10px 14px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #151515 @ 0 | = | 1px solid #151515 @ 0 |
| Radius | 16px | = | = | = |
| Background | #151515 @ 0.04 | #151515 @ 0.64 | = | #151515 @ 0.64 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #151515 @ 0.64 offset 2px | = |
| Font | -apple-system 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.64 | #ffffff | = | #ffffff |
| Text node | div.label: -apple-system 16px/16px 500, #151515 @ 0.64 | div.label: -apple-system 16px/16px 500, #ffffff | = | div.label: -apple-system 16px/16px 500, #ffffff |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #151515 @ 0.64, fill #000000 | 16 x 16, colour #ffffff, fill #000000 | = | 16 x 16, colour #ffffff, fill #000000 |
| Painted layers | button.btn.lux-button 320.0x38.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 320.0x38.0 bg #151515 @ 0.64 border T:1px solid #151515 @ 0 / R:1px solid #151515 @ 0 / B:1px solid #151515 @ 0 / L:1px solid #151515 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px | button.btn.lux-button 320.0x38.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 16px outline 2px solid #151515 @ 0.64 offset 2px | button.btn.lux-button 320.0x38.0 bg #151515 @ 0.64 border T:1px solid #151515 @ 0 / R:1px solid #151515 @ 0 / B:1px solid #151515 @ 0 / L:1px solid #151515 @ 0 r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `passkey-btn-default.png`, `passkey-btn-hover.png`, `passkey-btn-focus-visible.png`, `passkey-btn-pressed.png`.

### Footer

#### footer

Footer. The page footer: Discover, Pricing, App, Help, Terms, Privacy.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 185.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #151515 |
| Text node | a: -apple-system 14px/21px 400, #151515 @ 0.64 |
| Transition | none |
| Icon | 43.88 x 16, colour #151515 @ 0.64, fill #000000 |
| Painted layers | div.jsx-1656054359.flex-start 928.0x54.0 border T:1px solid #151515 @ 0.08 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer text link.

Page: home. Selector: `footer a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60.63 x 37 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.64 | #151515 | = | #151515 |
| Transition | all 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 60.6x37.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The 390px header: wordmark and Sign In. There is no hamburger.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 58 |
| Padding | 14px 18px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #151515 |
| Text node | div.label: -apple-system 14px/14px 500, #151515 @ 0.64 |
| Transition | none |
| Icon | 20 x 20, colour #151515 @ 0.36 |
| Painted layers | a.btn.lux-button 67.0x30.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.jsx-938331401.page-wrapper bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-signin

Mobile Sign In. The header Sign In pill at 390. Measured, never followed.

Page: mobile. Selector: `header Sign In at 390`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.95 x 30 | = | = | = |
| Padding | 7px 10px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 15px | = | = | = |
| Background | #151515 @ 0.04 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #151515 @ 0.64 offset 2px | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #151515 @ 0.64 | = | = | = |
| Text node | div.label: -apple-system 14px/14px 500, #151515 @ 0.64 | = | = | = |
| Transition | all, outline 0.3s, 0s cubic-bezier(0.4, 0, 0.2, 1), ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.lux-button 67.0x30.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #000000 @ 0 offset 2px | = | a.btn.lux-button 67.0x30.0 bg #151515 @ 0.04 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 15px outline 2px solid #151515 @ 0.64 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-signin-default.png`, `m-signin-hover.png`, `m-signin-focus-visible.png`, `m-signin-pressed.png`.

#### m-hero

Mobile headline. The landing title at 390.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 206.34 x 154.02 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 40px/39.2px 500 |
| Letter spacing | -0.4px |
| Colour | #151515 |
| Text node | div.jsx-3564931177.landing-title-rise: -apple-system 40px/39.2px 500, #151515, ls -0.4px |
| Transition | none |
| Icon | 56 x 20.41, colour #151515 @ 0.36, fill #000000 |
| Painted layers | span.gradient-text 175.5x59.0 image radial-gradient(circle at 0.15em 0.15em, #ab46dd 0%, #f31a7c 36%, #f8712b 51%, #eaab26 77% |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

Luma serves its own CSS same-origin. This list is what the CSSOM could read on each page; the per-state Transition rows above are computed values.

- event: `color var(--transition-duration) var(--transition-fn)`, `background-color var(--transition-duration) var(--transition-fn)`, `var(--transition)`, `var(--fast-transition)`, `opacity var(--transition-duration) var(--transition-fn)`, `var(--transition),height 0s`, `background var(--transition-duration) var(--transition-fn)`, `var(--transition),outline 0s`

- home: `color var(--transition-duration) var(--transition-fn)`, `background-color var(--transition-duration) var(--transition-fn)`, `var(--transition)`, `var(--fast-transition)`, `opacity var(--transition-duration) var(--transition-fn)`, `var(--transition),height 0s`, `background var(--transition-duration) var(--transition-fn)`, `var(--transition),outline 0s`, `color .2s var(--transition-fn)`, `box-shadow var(--transition-duration) var(--transition-fn)`, `width 0.35s cubic-bezier(0.16, 1, 0.3, 1)`

- pricing: `color var(--transition-duration) var(--transition-fn)`, `background-color var(--transition-duration) var(--transition-fn)`, `var(--transition)`, `var(--fast-transition)`, `opacity var(--transition-duration) var(--transition-fn)`, `var(--transition),height 0s`, `background var(--transition-duration) var(--transition-fn)`, `var(--transition),outline 0s`

- signin: `color var(--transition-duration) var(--transition-fn)`, `background-color var(--transition-duration) var(--transition-fn)`, `var(--transition)`, `var(--fast-transition)`, `opacity var(--transition-duration) var(--transition-fn)`, `var(--transition),height 0s`, `background var(--transition-duration) var(--transition-fn)`, `var(--transition),outline 0s`
