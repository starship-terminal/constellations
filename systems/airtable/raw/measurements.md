# Component measurements

Computed styles read from www.airtable.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-bar

Promo bar. The dismissible strip above the nav ("Bring your Airtable data into Claude. Try it now").

Page: platform. Selector: `the top promo strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 42.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f0f6ff |
| Box shadow | none |
| Outline | none |
| Font | ATSeasonSans 20px/25px 400 |
| Letter spacing | normal |
| Colour | #333840 |
| Text node | div.flex.flex-col: ATSeasonSans 14px/17.5px 400, #333840 |
| Transition | none |
| Icon | 18 x 12, colour #254fad |
| Painted layers | div.jQt14.aOvF2 1440.0x42.5 bg #f0f6ff; a.X2isC 82.3x18.2 r 10px outline 2px solid #000000 @ 0 offset 4px |
| Ancestor paint | 2 up nav.HmlLk bg #ffffff shadow #0f306a @ 0.05 0px 0px 20px 0px |
| How | at rest |

Crops: `promo-bar-default.png`.

#### promo-link

Promo link. The "Try it now" link in the promo bar. Measured and focused, never followed.

Page: platform. Selector: `the promo link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82.28 x 18.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 4px | = | 2px solid #254fad offset 4px | = |
| Font | ATSeasonSans 14px/18.2px 650 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #254fad | = | = | = |
| Text node | span: ATSeasonSans 14px/18.2px 650, #254fad, ls 0.14px | = | = | = |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 12, colour #254fad | = | = | = |
| Painted layers | a.X2isC 82.3x18.2 r 10px outline 2px solid #000000 @ 0 offset 4px | = | a.X2isC 82.3x18.2 r 10px outline 2px solid #254fad offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.75 | 0.75 | 0.75 |

Crops: `promo-link-default.png`, `promo-link-hover.png`, `promo-link-focus-visible.png`, `promo-link-pressed.png`.

#### promo-close

Promo close button. The × that dismisses the promo bar; a local dismissal, measured and focused, never pressed.

Page: platform. Selector: `aria-label "Close promo banner"`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 12 x 12 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #333840 offset 0px |
| Font | ATSeasonSans 14px/17.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #333840 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 12 x 12, colour #333840, fill #000000 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.absolute.cursor-pointer 12.0x12.0 outline 1px auto #333840 offset 0px |

Crops: `promo-close-default.png`, `promo-close-hover.png`, `promo-close-focus-visible.png`.

#### nav-bar

Top navigation bar. The header on every marketing page: the Airtable wordmark, Platform/Solutions/Resources triggers, Enterprise, Pricing, What's new, and Book Demo / Sign up for free / Log in.

Page: platform. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 121.3 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ATSeasonSans 20px/25px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.flex.flex-col: ATSeasonSans 14px/17.5px 400, #333840 |
| Transition | all 0.15s ease-in |
| Icon | 18 x 12, colour #254fad |
| Painted layers | nav.HmlLk 1440.0x121.3 bg #ffffff shadow #0f306a @ 0.05 0px 0px 20px 0px; div.jQt14.aOvF2 1440.0x42.5 bg #f0f6ff; a.X2isC 82.3x18.2 r 10px outline 2px solid #000000 @ 0 offset 4px; nav.NKCPB 794.6x900.0 bg #ffffff; nav::before.NKCPB 794.594pxx900px bg #ffffff; nav::after.NKCPB 20pxx900px shadow #0f306a @ 0.05 15px 0px 15px -15px inset |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-trigger

Nav dropdown trigger. A section trigger in the header (Platform); opens the section drawer on click. Measured, never followed.

Page: platform. Selector: `the Platform trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.97 x 20.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #040e20 @ 0.69 offset 0px | = |
| Font | ATSeasonSans 16px/20.8px 650 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #181d26 | #254fad | #254fad | #254fad |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #181d26, fill #000000 | 12 x 12, colour #254fad, fill #000000 | 12 x 12, colour #254fad, fill #000000 | 12 x 12, colour #254fad, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.jGXoe 78.0x20.8 outline 2px solid #040e20 @ 0.69 offset 0px | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. A direct link in the header (Enterprise, Pricing, What's new). Measured, never followed.

Page: platform. Selector: `a header link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.25 x 20.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #040e20 @ 0.69 offset 2px | = |
| Font | ATSeasonSans 16px/20.8px 650 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #181d26 | #254fad | #254fad | #254fad |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.S7Fvz.6cWfX 50.3x20.8 outline 2px solid #040e20 @ 0.69 offset 2px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-demo

Book Demo button. The outline "Book Demo" button in the header. Measured and focused, never followed (it leaves for the demo form).

Page: platform. Selector: `the Book Demo button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134.64 x 54.8 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #181d26 | 1px solid #040e20 @ 0.69 | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | #f9fcff @ 0.97 | #0f306a @ 0.05 |
| Box shadow | none | = | #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #040e20 @ 0.69 offset 2px | = |
| Font | ATSeasonSans 16px/20.8px 650 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #181d26 | #040e20 @ 0.69 | = | #040e20 @ 0.69 |
| Text node | span: ATSeasonSans 16px/20.8px 650, #181d26, ls 0.16px | span: ATSeasonSans 16px/20.8px 650, #040e20 @ 0.69, ls 0.16px | = | span: ATSeasonSans 16px/20.8px 650, #040e20 @ 0.69, ls 0.16px |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.sZl5R.kHO9k 134.6x54.8 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px | a.sZl5R.kHO9k 134.6x54.8 border T:1px solid #040e20 @ 0.69 / R:1px solid #040e20 @ 0.69 / B:1px solid #040e20 @ 0.69 / L:1px solid #040e20 @ 0.69 r 12px | a.sZl5R.kHO9k 134.6x54.8 bg #f9fcff @ 0.97 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px shadow #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px outline 2px solid #040e20 @ 0.69 offset 2px | a.sZl5R.kHO9k 134.6x54.8 bg #0f306a @ 0.05 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px |
| Ancestor paint | 2 up nav.HmlLk bg #ffffff shadow #0f306a @ 0.05 0px 0px 20px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-signup

Sign up button. The dark "Sign up for free" pill in the header. Measured and focused, never followed.

Page: platform. Selector: `the Sign up button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160.06 x 54.8 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #181d26 | 1px solid #040e20 @ 0.69 | = | 1px solid #070c14 @ 0.82 |
| Radius | 12px | = | = | = |
| Background | #181d26 | #040e20 @ 0.69 | = | #070c14 @ 0.82 |
| Box shadow | none | = | #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #040e20 @ 0.69 offset 2px | = |
| Font | ATSeasonSans 16px/20.8px 650 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.AVOAo: ATSeasonSans 16px/20.8px 650, #ffffff, ls 0.16px | = | = | = |
| Transition | all 0.2s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.sZl5R.s-Wsr 160.1x54.8 bg #181d26 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px | a.sZl5R.s-Wsr 160.1x54.8 bg #040e20 @ 0.69 border T:1px solid #040e20 @ 0.69 / R:1px solid #040e20 @ 0.69 / B:1px solid #040e20 @ 0.69 / L:1px solid #040e20 @ 0.69 r 12px | a.sZl5R.s-Wsr 160.1x54.8 bg #181d26 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px shadow #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px outline 2px solid #040e20 @ 0.69 offset 2px | a.sZl5R.s-Wsr 160.1x54.8 bg #070c14 @ 0.82 border T:1px solid #070c14 @ 0.82 / R:1px solid #070c14 @ 0.82 / B:1px solid #070c14 @ 0.82 / L:1px solid #070c14 @ 0.82 r 12px |
| Ancestor paint | 2 up nav.HmlLk bg #ffffff shadow #0f306a @ 0.05 0px 0px 20px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

#### nav-login

Log in link. The "Log in" text link in the header. Measured and focused, never followed.

Page: platform. Selector: `the Log in link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42.69 x 20.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #040e20 @ 0.69 offset 2px | = |
| Font | ATSeasonSans 16px/20.8px 650 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #181d26 | #254fad | #254fad | #254fad |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 2 up nav.HmlLk bg #ffffff shadow #0f306a @ 0.05 0px 0px 20px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.S7Fvz.6cWfX 42.7x20.8 outline 2px solid #040e20 @ 0.69 offset 2px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-dropdown

Nav drawer. The full-height drawer the Platform trigger opens (product areas and a promo card). Shown click-open; a local disclosure.

Page: platform. Selector: `the open navDrawerMenu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 710.59 x 900 |
| Padding | 121.297px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | ATSeasonSans 20px/25px 400 |
| Letter spacing | normal |
| Colour | #444444 |
| Text node | span.bNbXu: ATSeasonSans 14px/18.9px 650, #040e20 @ 0.69, ls 0.12px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 0 x 0, colour #333333 |
| ::before | 710.594px x 900px, absolute, bg #ffffff, radius 0px |
| ::after | 20px x 900px, absolute, bg #000000 @ 0, radius 0px, shadow #0f306a @ 0.05 15px 0px 15px -15px inset |
| Painted layers | nav.NKCPB.fncgA 710.6x900.0 bg #ffffff; nav::before.NKCPB.fncgA 710.594pxx900px bg #ffffff; nav::after.NKCPB.fncgA 20pxx900px shadow #0f306a @ 0.05 15px 0px 15px -15px inset; hr.--1b5 427.6x2.0 bg #181d26; div.xOoYx 480.0x778.7 bg #f8fafc; hr.--1b5 292.2x2.0 bg #181d26 |
| How | clicked the Platform trigger |

Crops: `nav-dropdown-default.png`.

#### footer

Footer. The site footer: link columns (Platform, Solutions, Resources, Learn, Company), social icons, legal row.

Page: platform. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1248 x 307.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas Groot Disp 20px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | p.pnUGO.rEl6J: ATSeasonSans 16px/21.6px 650, #333333, ls 0.16px |
| Transition | none |
| Icon | 0 x 0, colour #333333 |
| Painted layers | a.AdEPz.cwxsV 112.6x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; a.AdEPz.cwxsV 72.5x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; a.AdEPz.cwxsV 126.0x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; a.AdEPz.cwxsV 54.0x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; a.AdEPz.cwxsV 43.3x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; a.AdEPz.cwxsV 96.7x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in the footer columns. Measured, never followed.

Page: home. Selector: `a footer link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.2 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Haas Groot Disp 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #333333 | = | = | = |
| Text node | p.pnUGO.rEl6J: Haas 16px/21.6px 400, #333840, ls 0.16px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a.AdEPz.cwxsV 38.4x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 | = | a.AdEPz.cwxsV 38.4x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 6px shadow #000000 @ 0.5 0px 0px 0px 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### nav-dropdown-link

Drawer link. An item in the open nav drawer (Airtable Platform).

Page: platform. Selector: `a link inside navDrawerMenu`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 710.59 x 74.8 | = |
| Padding | 12px 48px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | #0f306a @ 0.05 |
| Box shadow | none | = |
| Outline | none | = |
| Font | ATSeasonSans 20px/26px 650 | = |
| Letter spacing | 0.2px | = |
| Colour | #181d26 | = |
| Text node | div.UCgvU.-C6Vh: ATSeasonSans 20px/26px 650, #181d26, ls 0.2px | = |
| Transition | all 0.15s ease-in | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | a.0w0Vt.fh50Q 710.6x74.8 bg #0f306a @ 0.05 |

Crops: `nav-dropdown-link-default.png`, `nav-dropdown-link-hover.png`.

### Home

#### hero-title

Hero title. The home h1 ("All your teams, all their workflows — connected in one workspace").

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 906.67 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 40px/48px 400 |
| Letter spacing | normal |
| Colour | #333840 |
| Transition | all 0.25s ease-in |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta-primary

Hero primary CTA. The dark "Get started for free" pill under the hero title.

Page: home. Selector: `the first primary button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200.59 x 55.59 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #181d26 | 1px solid #040e20 @ 0.69 | = | 1px solid #070c14 @ 0.82 |
| Radius | 12px | = | = | = |
| Background | #181d26 | #040e20 @ 0.69 | = | #070c14 @ 0.82 |
| Box shadow | #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #2d7ff9 @ 0.28 0px 1px 3px 0px, #000000 @ 0.06 0px 0px 0px 0.5px inset | none | #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px | none |
| Outline | none | = | = | = |
| Font | Haas 16px/21.6px 500 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.b-zy-W_bkButton.lpxhIa_typeShortSm 200.6x55.6 bg #181d26 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #2d7ff9 @ 0.28 0px 1px 3px 0px, #000000 @ 0.06 0px 0px 0px 0.5px inset | a.b-zy-W_bkButton.lpxhIa_typeShortSm 200.6x55.6 bg #040e20 @ 0.69 border T:1px solid #040e20 @ 0.69 / R:1px solid #040e20 @ 0.69 / B:1px solid #040e20 @ 0.69 / L:1px solid #040e20 @ 0.69 r 12px | a.b-zy-W_bkButton.lpxhIa_typeShortSm 200.6x55.6 bg #181d26 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px shadow #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px | a.b-zy-W_bkButton.lpxhIa_typeShortSm 200.6x55.6 bg #070c14 @ 0.82 border T:1px solid #070c14 @ 0.82 / R:1px solid #070c14 @ 0.82 / B:1px solid #070c14 @ 0.82 / L:1px solid #070c14 @ 0.82 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-primary-default.png`, `hero-cta-primary-hover.png`, `hero-cta-primary-focus-visible.png`, `hero-cta-primary-pressed.png`.

#### hero-cta-secondary

Hero secondary CTA. The outline "Book demo" pill beside the primary CTA.

Page: home. Selector: `the secondary button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.33 x 55.59 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 1px solid #181d26 | 1px solid #040e20 @ 0.69 | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | #f9fcff @ 0.97 | #0f306a @ 0.05 |
| Box shadow | #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 1px 3px 0px, #011435 @ 0.12 0px 0px 0px 1px inset | none | #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px | none |
| Backdrop filter | blur(6px) | = | - | - |
| Outline | none | = | = | = |
| Font | Haas 16px/21.6px 500 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #181d26 | #040e20 @ 0.69 | = | #040e20 @ 0.69 |
| Transition | all 0.2s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.b-zy-W_bkButton.lpxhIa_typeShortSm 138.3x55.6 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 1px 3px 0px, #011435 @ 0.12 0px 0px 0px 1px inset | a.b-zy-W_bkButton.lpxhIa_typeShortSm 138.3x55.6 border T:1px solid #040e20 @ 0.69 / R:1px solid #040e20 @ 0.69 / B:1px solid #040e20 @ 0.69 / L:1px solid #040e20 @ 0.69 r 12px | a.b-zy-W_bkButton.lpxhIa_typeShortSm 138.3x55.6 bg #f9fcff @ 0.97 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px shadow #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px | a.b-zy-W_bkButton.lpxhIa_typeShortSm 138.3x55.6 bg #0f306a @ 0.05 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-secondary-default.png`, `hero-cta-secondary-hover.png`, `hero-cta-secondary-focus-visible.png`, `hero-cta-secondary-pressed.png`.

#### feature-card

Feature card. The large red "Sophisticated workflows" feature card.

Page: home. Selector: `the big feature card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1312 x 371.14 | = |
| Padding | 0px | = |
| Gap | 48px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333840 | = |
| Text node | p.lpxhIa_typeShortLg.lpxhIa_bkText: Haas 18px/21.6px 500, #181d26 | = |
| Transition | none | = |
| Painted layers | div.ZxeOkq_card.ZxeOkq_imageTop 405.3x371.1 bg #f8fafc border T:1px solid #e0e2e6 / R:1px solid #e0e2e6 / B:1px solid #e0e2e6 / L:1px solid #e0e2e6 r 16px; div.ZxeOkq_card.ZxeOkq_imageTop 405.3x371.1 bg #f8fafc border T:1px solid #e0e2e6 / R:1px solid #e0e2e6 / B:1px solid #e0e2e6 / L:1px solid #e0e2e6 r 16px; div.ZxeOkq_card.ZxeOkq_imageTop 405.3x371.1 bg #f8fafc border T:1px solid #e0e2e6 / R:1px solid #e0e2e6 / B:1px solid #e0e2e6 / L:1px solid #e0e2e6 r 16px | = |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### ai-card

AI feature card. The light-blue "Say hello to Omni" card.

Page: home. Selector: `the Omni media card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 683.3 x 107 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #181d26 | = |
| Text node | span._4x3unq_block: Haas 24px/39px 400, #181d26 | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `ai-card-default.png`, `ai-card-hover.png`.

#### tile-card

Coloured tile card. A coloured tile in the "path to 10x" grid (orange, blue, green surfaces).

Page: home. Selector: `a coloured tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 437.34 x 427 | = |
| Padding | 24px 0px 0px 0px | = |
| Border | none | = |
| Radius | 32px | = |
| Background | #c7e5f2 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a2e0e | = |
| Text node | p.lpxhIa_typeShortMd.lpxhIa_bkText: Haas 32px/40px 500, #0a2e0e, ls 0.16px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.SnWS4q_boxWrapper.wSLgcW_card 437.3x427.0 bg #c7e5f2 r 32px; div.SnWS4q_bentoBoxText 202.3x54.0 bg #0a2e0e r 32px | = |
| How | at rest | mouse hover |

Crops: `tile-card-default.png`, `tile-card-hover.png`.

#### about-title

About page title. The h1 on /about.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 741.97 x 55.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ATSeasonSans 48px/55.2px 500 |
| Letter spacing | normal |
| Colour | #181d26 |
| Transition | none |
| How | at rest |

Crops: `about-title-default.png`.

#### about-card

About page card. A card on the about page (values, offices, news).

Page: about. Selector: `a card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1342 x 116.19 | = |
| Padding | 0px | = |
| Border | T: 1px solid #e0dcdb; R: none; B: none; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | h3._8-XBpW_cardTitle: ATSeasonSans 18px/24.3px 600, #181d26, ls 0.18px | = |
| Transition | none | = |
| Painted layers | ul._8-XBpW_cardGrid 1342.0x116.2 border T:1px solid #e0dcdb; li._8-XBpW_cardCell 447.3x115.2 bg #f8f6f6 border R:1px solid #e0dcdb; li._8-XBpW_cardCell 447.3x115.2 bg #f8f6f6 border R:1px solid #e0dcdb; li._8-XBpW_cardCell 447.3x115.2 bg #f8f6f6 | = |
| How | at rest | mouse hover |

Crops: `about-card-default.png`, `about-card-hover.png`.

#### resource-card

Resource card. A card in the "Resources to inspire" row (Builders & Breakthroughs).

Page: home. Selector: `a resource card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 906.66 x 427 | = |
| Padding | 24px 0px 0px 0px | = |
| Border | none | = |
| Radius | 32px | = |
| Background | #fcab79 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #aa2d00 | = |
| Text node | p.lpxhIa_typeShortMd.lpxhIa_bkText: Haas 32px/40px 500, #aa2d00, ls 0.16px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.SnWS4q_boxWrapper.wSLgcW_card 906.7x427.0 bg #fcab79 r 32px; div.SnWS4q_bentoBoxText 202.3x54.0 bg #aa2d00 r 32px | = |
| How | at rest | mouse hover |

Crops: `resource-card-default.png`, `resource-card-hover.png`.

#### carousel-control

Carousel control. A round control of the home feature carousel (the pause or next button).

Page: home. Selector: `a carousel control button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #181d26 | #040e20 @ 0.69 | = | #020d20 @ 0.43 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Haas 20px/0px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.A_bFna_root.A_bFna_dark 40.0x40.0 bg #181d26 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.A_bFna_root.A_bFna_dark 40.0x40.0 bg #040e20 @ 0.69 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.A_bFna_root.A_bFna_dark 40.0x40.0 bg #181d26 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px | button.A_bFna_root.A_bFna_dark 40.0x40.0 bg #020d20 @ 0.43 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-control-default.png`, `carousel-control-hover.png`, `carousel-control-focus-visible.png`, `carousel-control-pressed.png`.

### Platform pages

#### platform-title

Platform page title. The h1 on https://www.airtable.com/platform.

Page: platform. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1184 x 174.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ATSeasonSans 79.2px/87.12px 550 |
| Letter spacing | normal |
| Colour | #161616 |
| Text node | span.gOrYkG_headingLine: ATSeasonSans 79.2px/87.12px 550, #161616 |
| Transition | none |
| How | at rest |

Crops: `platform-title-default.png`.

#### platform-cta

Platform CTA. A primary button on the platform page. Measured and focused, never followed.

Page: platform. Selector: `the first CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 131.8 x 47.59 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 1px solid #161616 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | #f5f5f5 | #f5f5f5 | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #161616 offset 2px | = |
| Font | ATSeasonSans 16px/21.6px 650 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #161616 | = | = | = |
| Transition | background-color, color, border-color 0.15s, 0.15s, 0.15s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.gOrYkG_cta.gOrYkG_ctaSecondary 131.8x47.6 bg #ffffff border T:1px solid #161616 / R:1px solid #161616 / B:1px solid #161616 / L:1px solid #161616 r 4px | a.gOrYkG_cta.gOrYkG_ctaSecondary 131.8x47.6 bg #f5f5f5 border T:1px solid #161616 / R:1px solid #161616 / B:1px solid #161616 / L:1px solid #161616 r 4px | a.gOrYkG_cta.gOrYkG_ctaSecondary 131.8x47.6 bg #f5f5f5 border T:1px solid #161616 / R:1px solid #161616 / B:1px solid #161616 / L:1px solid #161616 r 4px outline 2px solid #161616 offset 2px | a.gOrYkG_cta.gOrYkG_ctaSecondary 131.8x47.6 bg #f5f5f5 border T:1px solid #161616 / R:1px solid #161616 / B:1px solid #161616 / L:1px solid #161616 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `platform-cta-default.png`, `platform-cta-hover.png`, `platform-cta-focus-visible.png`, `platform-cta-pressed.png`.

#### platform-card

Platform feature card. A linked card on /platform (a "Ways to start building with agents" tile).

Page: platform. Selector: `a cardLink`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 670 x 540.97 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff | #f8f6f6 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | h3.GboOzG_cardTitle: ATSeasonSans 24px/31.2px 550, #161616 | = |
| Transition | background-color 0.15s ease | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #161616 | = |
| Painted layers | a.GboOzG_cardLink 670.0x541.0 bg #ffffff; div.GboOzG_visual 670.0x360.0 bg #f8f6f6 | a.GboOzG_cardLink 670.0x541.0 bg #f8f6f6; div.GboOzG_visual 670.0x360.0 bg #f8f6f6 |
| How | at rest | mouse hover |

Crops: `platform-card-default.png`, `platform-card-hover.png`.

#### feature-tablist

Feature tab list. The vertical tab strip ("Data that fits your business": Shared data, Durable workflows, Open surfaces, Governance).

Page: platform. Selector: `the tablist`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 425 x 700 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Haas 20px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | p.yG6H1q_panelTitle: ATSeasonSans 16px/21.6px 650, #181d26 |
| Transition | none |
| Painted layers | div.yG6H1q_tablist 425.0x700.0 bg #ffffff; div.yG6H1q_media.yG6H1q_mediaActive 916.0x700.0 bg #7a015c; button.yG6H1q_tab.yG6H1q_tabActive 425.0x80.2 bg #ffffff border B:1px solid #181d26; span.yG6H1q_tabMarker 12.0x12.0 bg #161616; div.yG6H1q_media 916.0x700.0 bg #47008f; button.yG6H1q_tab 425.0x80.2 bg #f8f6f6 border B:1px solid #e0dcdb |
| Ancestor paint | 1 up div.yG6H1q_left bg #ffffff |
| How | at rest |

Crops: `feature-tablist-default.png`.

#### feature-tab

Feature tab. One segment of the feature tab strip.

Page: platform. Selector: `a _tab button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 425 x 80.19 | = | = | = |
| Padding | 24px 40px | = | = | = |
| Gap | 8px | = | = | = |
| Border | T: none; R: none; B: 1px solid #181d26; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #161616 offset -2px | = |
| Font | Haas 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #181d26 | = | = | = |
| Text node | span.yG6H1q_tabLabel: ATSeasonSans 24px/31.2px 550, #181d26 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.yG6H1q_tab.yG6H1q_tabActive 425.0x80.2 bg #ffffff border B:1px solid #181d26; span.yG6H1q_tabMarker 12.0x12.0 bg #161616 | = | button.yG6H1q_tab.yG6H1q_tabActive 425.0x80.2 bg #ffffff border B:1px solid #181d26 outline 2px solid #161616 offset -2px; span.yG6H1q_tabMarker 12.0x12.0 bg #161616 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `feature-tab-default.png`, `feature-tab-hover.png`, `feature-tab-focus-visible.png`, `feature-tab-pressed.png`.

#### feature-tab-active

Feature tab, selected. The selected segment of the tab strip.

Page: platform. Selector: `the _tabActive`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 425 x 80.19 |
| Padding | 24px 40px |
| Gap | 8px |
| Border | T: none; R: none; B: 1px solid #181d26; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Haas 20px/30px 400 |
| Letter spacing | normal |
| Colour | #181d26 |
| Text node | span.yG6H1q_tabLabel: ATSeasonSans 24px/31.2px 550, #181d26 |
| Transition | none |
| Cursor | pointer |
| Painted layers | button.yG6H1q_tab.yG6H1q_tabActive 425.0x80.2 bg #ffffff border B:1px solid #181d26; span.yG6H1q_tabMarker 12.0x12.0 bg #161616 |
| How | at rest |

Crops: `feature-tab-active-default.png`.

#### stories-prev

Stories previous button. The previous-arrow of the customer-stories carousel, shown after the carousel leaves its first slide.

Page: platform. Selector: `the prev arrowButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0.23 | 1px solid #ffffff @ 0.5 | 1px solid #ffffff @ 0.5 | 1px solid #ffffff @ 0.5 |
| Radius | 50% | = | = | = |
| Background | transparent | #ffffff @ 0.08 | #ffffff @ 0.08 | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | Haas 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.xoaFjW_arrowButton 40.0x40.0 border T:1px solid #ffffff @ 0.23 / R:1px solid #ffffff @ 0.23 / B:1px solid #ffffff @ 0.23 / L:1px solid #ffffff @ 0.23 r 50% | button.xoaFjW_arrowButton 40.0x40.0 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 50% | button.xoaFjW_arrowButton 40.0x40.0 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 50% outline 2px solid #ffffff offset 2px | button.xoaFjW_arrowButton 40.0x40.0 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `stories-prev-default.png`, `stories-prev-hover.png`, `stories-prev-focus-visible.png`, `stories-prev-pressed.png`.

#### stories-next

Stories next button. The next-arrow of the customer-stories carousel.

Page: platform. Selector: `the next arrow button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0.23 | 1px solid #ffffff @ 0.5 | 1px solid #ffffff @ 0.5 | 1px solid #ffffff @ 0.5 |
| Radius | 50% | = | = | = |
| Background | transparent | #ffffff @ 0.08 | #ffffff @ 0.08 | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | Haas 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.xoaFjW_arrowButton 40.0x40.0 border T:1px solid #ffffff @ 0.23 / R:1px solid #ffffff @ 0.23 / B:1px solid #ffffff @ 0.23 / L:1px solid #ffffff @ 0.23 r 50% | button.xoaFjW_arrowButton 40.0x40.0 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 50% | button.xoaFjW_arrowButton 40.0x40.0 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 50% outline 2px solid #ffffff offset 2px | button.xoaFjW_arrowButton 40.0x40.0 bg #ffffff @ 0.08 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `stories-next-default.png`, `stories-next-hover.png`, `stories-next-focus-visible.png`, `stories-next-pressed.png`.

#### stories-pause

Stories pause button. The pause-autoplay button of the customer-stories carousel; measured and focused, never pressed.

Page: platform-ai. Selector: `the pause button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #000000 @ 0 | = | = |
| Radius | 9999px | = | = |
| Background | #181d26 | #040e20 @ 0.69 | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px |
| Outline | none | = | = |
| Font | Haas 20px/0px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | background-color, border-color, color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #ffffff | = | = |
| Painted layers | button.A_bFna_root.A_bFna_dark 40.0x40.0 bg #181d26 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.A_bFna_root.A_bFna_dark 40.0x40.0 bg #040e20 @ 0.69 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px | button.A_bFna_root.A_bFna_dark 40.0x40.0 bg #181d26 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `stories-pause-default.png`, `stories-pause-hover.png`, `stories-pause-focus-visible.png`.

#### platform-ai-title

Platform page title. The h1 on https://www.airtable.com/platform/ai.

Page: platform-ai. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 884 x 110.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ATSeasonSans 48px/55.2px 500 |
| Letter spacing | normal |
| Colour | #181d26 |
| Transition | none |
| How | at rest |

Crops: `platform-ai-title-default.png`.

#### platform-ai-cta

Platform CTA. A primary button on the platform page. Measured and focused, never followed.

Page: platform-ai. Selector: `the first CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 131.42 x 47.59 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #181d26 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f2f4f7 @ 0.92 | #f2f4f7 @ 0.92 | #f2f4f7 @ 0.92 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | ATSeasonSans 16px/21.6px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #181d26 | = | = | = |
| Transition | background-color, border-color, color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.jqKb6a_root.jqKb6a_secondary 131.4x47.6 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 4px | a.jqKb6a_root.jqKb6a_secondary 131.4x47.6 bg #f2f4f7 @ 0.92 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 4px | a.jqKb6a_root.jqKb6a_secondary 131.4x47.6 bg #f2f4f7 @ 0.92 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0768f8 0px 0px 0px 2px | a.jqKb6a_root.jqKb6a_secondary 131.4x47.6 bg #f2f4f7 @ 0.92 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `platform-ai-cta-default.png`, `platform-ai-cta-hover.png`, `platform-ai-cta-focus-visible.png`, `platform-ai-cta-pressed.png`.

#### solutions-card-title

Solutions page title.

Page: solutions. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 620.73 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 40px/48px 400 |
| Letter spacing | normal |
| Colour | #333840 |
| Transition | all 0.25s ease-in |
| How | at rest |

Crops: `solutions-card-title-default.png`.

#### solutions-card

Solutions card. Solutions card: a team tile in the solutions grid (Marketing teams, Product teams, ...).

Page: solutions. Selector: `a cardIconCard tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 437.33 x 207.59 | = |
| Padding | 24px | = |
| Border | 1px solid #e0e2e6 | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | h3.Bxw3OW_heading: Haas 16px/21.6px 500, #181d26 | = |
| Transition | none | = |
| Icon | 16 x 12, colour #0768f8 | = |
| Painted layers | div.Bxw3OW_cardIconCardV2 437.3x207.6 bg #ffffff border T:1px solid #e0e2e6 / R:1px solid #e0e2e6 / B:1px solid #e0e2e6 / L:1px solid #e0e2e6 r 16px | = |
| How | at rest | mouse hover |

Crops: `solutions-card-default.png`, `solutions-card-hover.png`.

#### enterprise-card-title

Enterprise page title.

Page: enterprise. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1184 x 174.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ATSeasonSans 79.2px/87.12px 550 |
| Letter spacing | normal |
| Colour | #161616 |
| Text node | span.gOrYkG_headingLine: ATSeasonSans 79.2px/87.12px 550, #161616 |
| Transition | none |
| How | at rest |

Crops: `enterprise-card-title-default.png`.

#### enterprise-card

Enterprise card. Enterprise card: a linked capability card on the enterprise page.

Page: enterprise. Selector: `a cardLink`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 335.5 x 351 | = |
| Padding | 0px | = |
| Border | T: 1px solid #e0dcdb; R: none; B: 1px solid #e0dcdb; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | span.jWOJtq_titleLine: ATSeasonSans 24px/31.2px 550, #181d26 | = |
| Transition | none | = |
| Icon | 16 x 16, colour #161616 | = |
| Painted layers | li.jWOJtq_card 335.5x351.0 border T:1px solid #e0dcdb / B:1px solid #e0dcdb; a.jWOJtq_cardLink 335.5x349.0 bg #ffffff; div.jWOJtq_accent 12.0x12.0 bg #6f9fff; div.jWOJtq_proof 335.5x64.0 border T:1px solid #e0dcdb | li.jWOJtq_card 335.5x351.0 border T:1px solid #e0dcdb / B:1px solid #e0dcdb; a.jWOJtq_cardLink 335.5x349.0 bg #f8f6f6; div.jWOJtq_accent 12.0x12.0 bg #6f9fff; div.jWOJtq_proof 335.5x64.0 border T:1px solid #e0dcdb |
| How | at rest | mouse hover |

Crops: `enterprise-card-default.png`, `enterprise-card-hover.png`.

#### faq-item

FAQ item. An accordion question in the "You have questions? We have answers." section.

Page: platform-ai. Selector: `an accordion question`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 814 x 32 | = |
| Padding | 0px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | span.N0p0YG_question: ATSeasonSans 16px/21.6px 600, #181d26, ls 0.16px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 32 x 32, colour #9297a0 | = |
| How | at rest | mouse hover |

Crops: `faq-item-default.png`, `faq-item-hover.png`.

#### faq-item-open

FAQ item, open. The same accordion item clicked open; a local expand.

Page: platform-ai. Selector: `the open accordion item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 814 x 110.78 |
| Padding | 0px 0px 24px 0px |
| Border | T: none; R: none; B: 1px solid #e0dcdb; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 20px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.N0p0YG_question: ATSeasonSans 16px/21.6px 600, #181d26, ls 0.16px |
| Transition | none |
| Icon | 32 x 32, colour #9297a0 |
| Painted layers | div.N0p0YG_root 814.0x110.8 border B:1px solid #e0dcdb |
| How | clicked the question open |

Crops: `faq-item-open-default.png`.

#### platform-ai-card

Platform AI card. A card of the "Add AI to your workflows" grid on /platform/ai ("Generate high-impact campaign concepts").

Page: platform-ai. Selector: `a cardCell`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 447.33 x 224.97 | = |
| Padding | 0px | = |
| Border | T: none; R: 1px solid #e0dcdb; B: none; L: none | = |
| Radius | 0px | = |
| Background | #f8f6f6 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | h3._8-XBpW_cardTitle: ATSeasonSans 18px/24.3px 600, #181d26, ls 0.18px | = |
| Transition | none | = |
| Painted layers | li._8-XBpW_cardCell 447.3x225.0 bg #f8f6f6 border R:1px solid #e0dcdb | = |
| How | at rest | mouse hover |

Crops: `platform-ai-card-default.png`, `platform-ai-card-hover.png`.

### Pricing

#### pricing-title

Pricing title. The "A plan for every organization's needs" h1.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1250 x 55.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 44.8px/56px 475 |
| Letter spacing | -0.16px |
| Colour | #1d1f25 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-cta

Plan CTA. A button inside a plan card ("Contact Sales" pill). Measured and focused, never followed.

Page: pricing. Selector: `a plan card button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 246.5 x 56 | = | = | = |
| Padding | 16px | = | = | = |
| Border | 2px solid #1d1f25 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f2f4f8 | = | #f2f4f8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter Display 16px/20px 575 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #1d1f25 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.pill.mx-auto 246.5x56.0 bg #ffffff border T:2px solid #1d1f25 / R:2px solid #1d1f25 / B:2px solid #1d1f25 / L:2px solid #1d1f25 r 9999px | a.pill.mx-auto 246.5x56.0 bg #f2f4f8 border T:2px solid #1d1f25 / R:2px solid #1d1f25 / B:2px solid #1d1f25 / L:2px solid #1d1f25 r 9999px | a.pill.mx-auto 246.5x56.0 bg #ffffff border T:2px solid #1d1f25 / R:2px solid #1d1f25 / B:2px solid #1d1f25 / L:2px solid #1d1f25 r 9999px outline 1px auto #005fcc offset 1px | a.pill.mx-auto 246.5x56.0 bg #f2f4f8 border T:2px solid #1d1f25 / R:2px solid #1d1f25 / B:2px solid #1d1f25 / L:2px solid #1d1f25 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-see-more

See more link. The "See more" / "See all features and compare plans" expander. Measured, never followed.

Page: pricing. Selector: `a See more link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.19 x 25.59 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system 12.8px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1d1f25 | = | = | = |
| Text node | p.32U9z.2HumR: Haas 16px/21.6px 500, #1d1f25, ls 0.16px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | a.2Kqch.1AVi6 75.5x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 | = | a.2Kqch.1AVi6 75.5x25.6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 6px shadow #000000 @ 0.5 0px 0px 0px 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-see-more-default.png`, `plan-see-more-hover.png`, `plan-see-more-focus-visible.png`, `plan-see-more-pressed.png`.

#### pricing-faq-item

Pricing FAQ item. An accordion question in the pricing FAQ ("How does Airtable's pricing work?").

Page: pricing. Selector: `an accordion row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 768 x 25.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Display 12.8px/19.2px 400 | = |
| Letter spacing | -0.16px | = |
| Colour | #1d1f25 | = |
| Text node | p.flex-auto.heading-size-small: Inter Display 17px/25.5px 575, #1d1f25, ls -0.16px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #1d1f25, fill #000000 | = |
| How | at rest | mouse hover |

Crops: `pricing-faq-item-default.png`, `pricing-faq-item-hover.png`.

#### pricing-faq-item-open

Pricing FAQ item, open. The same accordion item clicked open; a local expand.

Page: pricing. Selector: `the open accordion row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 206.73 |
| Padding | 0px 0px 2.24px 0px |
| Border | T: none; R: none; B: 3px solid #000000 @ 0.1; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 12.8px/19.2px 400 |
| Letter spacing | -0.16px |
| Colour | #1d1f25 |
| Text node | p.flex-auto.heading-size-small: Inter Display 17px/25.5px 575, #1d1f25, ls -0.16px |
| Transition | none |
| Icon | 16 x 16, colour #1d1f25, fill #000000 |
| Painted layers | div.understroke.thick 768.0x206.7 border B:3px solid #000000 @ 0.1 |
| How | clicked the question open |

Crops: `pricing-faq-item-open-default.png`.

#### plan-card

Plan card. A plan column on the pricing grid (Free, Team $20, Business $45, Enterprise Scale).

Page: pricing. Selector: `a plan column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 296.5 x 454.5 |
| Padding | 0px 24px 16px 24px |
| Border | T: none; R: 1px solid #0d52ac; B: 1px solid #0d52ac; L: 1px solid #0d52ac |
| Radius | 0px 0px 12px 12px |
| Background | #f0f6ff @ 0.5 |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 16px/20px 400 |
| Letter spacing | -0.16px |
| Colour | #1d1f25 |
| Text node | p.font-weight-strong: Inter Display 16px/20px 475, #1d1f25, ls -0.16px |
| Transition | none |
| Icon | 20 x 20, colour #1d1f25, fill #000000 |
| Painted layers | div.flex-auto.flex 296.5x454.5 bg #f0f6ff @ 0.5 border R:1px solid #0d52ac / B:1px solid #0d52ac / L:1px solid #0d52ac r 0px 0px 12px 12px |
| How | at rest |

Crops: `plan-card-default.png`.

#### compare-table

Plan comparison table. The "Compare our plans" feature table: a div grid of plan columns against feature rows with checks (measured whole; no <table> element).

Page: pricing. Selector: `the comparison grid`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1250 x 5329 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 12.8px/16px 400 |
| Letter spacing | -0.16px |
| Colour | #1d1f25 |
| Text node | h2.huge.strong: Inter Display 32px/40px 475, #1d1f25, ls -0.16px |
| Transition | none |
| Icon | 24 x 24, colour #1d1f25, fill #000000 |
| Painted layers | div.sticky.z1 1250.0x161.0 bg #ffffff; a.pill.mx-auto 163.0x56.0 bg #ffffff border T:2px solid #1d1f25 / R:2px solid #1d1f25 / B:2px solid #1d1f25 / L:2px solid #1d1f25 r 9999px; a.pill.mx-auto 163.0x52.0 bg #166ee1 r 9999px; a.pill.mx-auto 163.0x56.0 bg #ffffff border T:2px solid #1d1f25 / R:2px solid #1d1f25 / B:2px solid #1d1f25 / L:2px solid #1d1f25 r 9999px; div.pill.mx-auto 163.0x56.0 bg #ffffff border T:2px solid #1d1f25 / R:2px solid #1d1f25 / B:2px solid #1d1f25 / L:2px solid #1d1f25 r 9999px; a.pointer 41.2x22.0 border B:2px dotted #dddddd |
| How | at rest |

Crops: `compare-table-default.png`.

#### compare-table-row

Comparison row. A feature row in the comparison table (a hover-container flex row).

Page: pricing. Selector: `a table row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1266 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 12.8px/16px 400 |
| Letter spacing | -0.16px |
| Colour | #1d1f25 |
| Text node | a.pointer: Inter Display 16px/20px 400, #1d1f25, ls -0.16px |
| Transition | none |
| Painted layers | a.pointer 41.2x22.0 border B:2px dotted #dddddd |
| How | at rest |

Crops: `compare-table-row-default.png`.

### Contact sales form

#### contact-title

Contact page title. The "Get in touch with us!" heading over the form.

Page: contact-sales. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 785.33 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 48px/60px 600 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| How | at rest |

Crops: `contact-title-default.png`.

#### contact-form

Contact form. The Marketo contact-sales form (a hidden mkto <form> with a visible React fields grid): First/Last name, Work Email, Phone with a country selector, Company Name, Job Title, Country, a message area and Submit. Photographed and focused, never submitted.

Page: contact-sales. Selector: `the fields grid`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 430.66 x 619.23 |
| Padding | 0px |
| Gap | normal 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 20px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | span.b4J7Yq_requiredText: Haas 12px/18px 500, #c2214c |
| Transition | none |
| Icon | 20 x 20, colour #cccccc |
| Painted layers | div._0-Izga_marketoCustomField.b4J7Yq_inputContainer 211.3x56.0 bg #ffffff border T:1px solid #000e26 @ 0.23 / R:1px solid #000e26 @ 0.23 / B:1px solid #000e26 @ 0.23 / L:1px solid #000e26 @ 0.23 r 8px; div._0-Izga_marketoCustomField.b4J7Yq_inputContainer 211.3x56.0 bg #ffffff border T:1px solid #000e26 @ 0.23 / R:1px solid #000e26 @ 0.23 / B:1px solid #000e26 @ 0.23 / L:1px solid #000e26 @ 0.23 r 8px; div.b4J7Yq_inputContainer.b4J7Yq_passive 430.7x53.6 bg #ffffff border T:1px solid #000e26 @ 0.23 / R:1px solid #000e26 @ 0.23 / B:1px solid #000e26 @ 0.23 / L:1px solid #000e26 @ 0.23 r 8px; div.IVLKlG_inputContainer.IVLKlG_hover 430.7x64.9 bg #ffffff border T:1px solid #000e26 @ 0.23 / R:1px solid #000e26 @ 0.23 / B:1px solid #000e26 @ 0.23 / L:1px solid #000e26 @ 0.23 r 8px; button.react-international-phone-country-selector-button 29.8x12.0 bg #ffffff r 4px 0px 0px 4px; div.dropdown-arrow 8.0x4.0 border T:4px solid #777777 / R:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 |
| Ancestor paint | 3 up div._5aDkOW_formContainer bg #ffffff shadow #1a1d26 @ 0.1 0px 30px 50px 0px |
| How | at rest |

Crops: `contact-form-default.png`.

#### field-label

Field label. A floating label inside a field of the form ("* First Name").

Page: contact-sales. Selector: `a label element`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 70.33 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 20px/30px 400 |
| Letter spacing | normal |
| Colour | #333840 |
| Text node | span.b4J7Yq_requiredText: Haas 12px/18px 500, #c2214c |
| Transition | all 0.25s ease |
| Cursor | default |
| How | at rest |

Crops: `field-label-default.png`.

#### text-field

Text field. A text input in the form (First name). Focused and filled with sample text that was deleted; nothing was sent.

Page: contact-sales. Selector: `the first text input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 185.33 x 21.59 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 1000px inset | #ffffff 0px 0px 0px 1000px inset |
| Outline | none | = | = |
| Font | Haas 16px/21.6px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #181d26 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #181d26, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "a workflow tracker for a studio", then deleted; nothing sent |
| Painted layers | - | input.b4J7Yq_input 185.3x21.6 shadow #ffffff 0px 0px 0px 1000px inset | input.b4J7Yq_input 185.3x21.6 shadow #ffffff 0px 0px 0px 1000px inset |

Crops: `text-field-default.png`, `text-field-focused.png`, `text-field-filled.png`.

#### text-field-box

Text field box. The same field measured at rest (default only).

Page: contact-sales. Selector: `the first text input`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 185.33 x 21.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 16px/21.6px 400 |
| Letter spacing | normal |
| Colour | #181d26 |
| Transition | none |
| Cursor | text |
| Placeholder | #181d26, opacity 1 |
| How | at rest |

Crops: none.

#### phone-field

Phone field. The phone input beside the country selector.

Page: contact-sales. Selector: `input[type=tel]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 375.91 x 18.89 | = |
| Padding | 0px 0px 0px 8px | = |
| Border | none | = |
| Radius | 0px 4px 4px 0px | = |
| Background | #ffffff | = |
| Box shadow | none | #ffffff 0px 0px 0px 1000px inset |
| Outline | none | = |
| Font | Haas 14px/18.9px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #222222, opacity 1 | = |
| Painted layers | input.react-international-phone-input 375.9x18.9 bg #ffffff r 0px 4px 4px 0px | input.react-international-phone-input 375.9x18.9 bg #ffffff r 0px 4px 4px 0px shadow #ffffff 0px 0px 0px 1000px inset |
| How | at rest | clicked into the field |

Crops: `phone-field-default.png`, `phone-field-focused.png`.

#### country-selector

Country selector. The phone country combobox button. Measured and focused, never opened (a choice posts a value).

Page: contact-sales. Selector: `the country selector button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 29.75 x 12 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 4px 0px 0px 4px | = | = |
| Background | #ffffff | transparent | transparent |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | Haas 20px/30px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #333333 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.react-international-phone-country-selector-button 29.8x12.0 bg #ffffff r 4px 0px 0px 4px; div.dropdown-arrow 8.0x4.0 border T:4px solid #777777 / R:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 | div.dropdown-arrow 8.0x4.0 border T:4px solid #777777 / R:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 | button.react-international-phone-country-selector-button 29.8x12.0 r 4px 0px 0px 4px outline 1px auto #005fcc offset 0px; div.dropdown-arrow 8.0x4.0 border T:4px solid #777777 / R:4px solid #000000 @ 0 / L:4px solid #000000 @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `country-selector-default.png`, `country-selector-hover.png`, `country-selector-focus-visible.png`.

#### email-field

Email field. The work-email input.

Page: contact-sales. Selector: `input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 404.66 x 21.59 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | #ffffff 0px 0px 0px 1000px inset |
| Outline | none | = |
| Font | Haas 16px/21.6px 400 | = |
| Letter spacing | normal | = |
| Colour | #181d26 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #181d26, opacity 1 | = |
| How | at rest | clicked into the field |
| Painted layers | - | input.b4J7Yq_input 404.7x21.6 shadow #ffffff 0px 0px 0px 1000px inset |

Crops: `email-field-default.png`, `email-field-focused.png`.

#### text-area

Text area. The "How can we help?" message textarea.

Page: contact-sales. Selector: `textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 398.66 x 48 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #333840 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #333840, opacity 1 | = |
| How | at rest | clicked into the field |

Crops: `text-area-default.png`, `text-area-focused.png`.

#### select-field

Select field. The "Country" dropdown in the form (a custom combobox, not a native select). Measured at rest; never submitted.

Page: contact-sales. Selector: `the Country field`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 430.66 x 56.59 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | span.GTBbWq_requiredIcon: Haas 20px/30px 400, #c2214c | = |
| Transition | none | = |
| Icon | 20 x 20, colour #cccccc | = |
| Painted layers | div.control.css-s16wi8-control 430.7x56.6 border T:1px solid #000e26 @ 0.23 / R:1px solid #000e26 @ 0.23 / B:1px solid #000e26 @ 0.23 / L:1px solid #000e26 @ 0.23 r 8px | div.control.css-s16wi8-control 430.7x56.6 border T:1px solid #b3b3b3 / R:1px solid #b3b3b3 / B:1px solid #b3b3b3 / L:1px solid #b3b3b3 r 8px |
| How | at rest | mouse hover |

Crops: `select-field-default.png`, `select-field-hover.png`.

#### select-field-open

Select field, open. The Country dropdown clicked open; a local disclosure, nothing chosen.

Page: contact-sales. Selector: `the open dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 430.66 x 300 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.1 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 11px 0px |
| Outline | none |
| Font | Haas 20px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.option.css-10wo9uf-option: Haas 16px/24px 400, #333333 |
| Transition | none |
| Painted layers | div.menu.css-1nmdiq5-menu 430.7x300.0 bg #ffffff r 4px shadow #000000 @ 0.1 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 11px 0px; div.option.option--is-focused 430.7x40.0 bg #deebff |
| How | clicked the field open; nothing chosen |

Crops: `select-field-open-default.png`.

#### submit-button

Submit button. The dark "Submit" of the sales form. Measured and focused, never pressed.

Page: contact-sales. Selector: `the submit button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 430.66 x 55.59 | = | = |
| Padding | 16px 24px | = | = |
| Border | 1px solid #181d26 | 1px solid #040e20 @ 0.69 | = |
| Radius | 12px | = | = |
| Background | #181d26 | #040e20 @ 0.69 | = |
| Box shadow | #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #2d7ff9 @ 0.28 0px 1px 3px 0px, #000000 @ 0.06 0px 0px 0px 0.5px inset | none | #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px |
| Outline | none | = | = |
| Font | Haas 16px/21.6px 500 | = | = |
| Letter spacing | 0.08px | = | = |
| Colour | #ffffff | = | = |
| Transition | all 0.2s linear | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.b-zy-W_bkButton.mktoReactButton 430.7x55.6 bg #181d26 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #2d7ff9 @ 0.28 0px 1px 3px 0px, #000000 @ 0.06 0px 0px 0px 0.5px inset | button.b-zy-W_bkButton.mktoReactButton 430.7x55.6 bg #040e20 @ 0.69 border T:1px solid #040e20 @ 0.69 / R:1px solid #040e20 @ 0.69 / B:1px solid #040e20 @ 0.69 / L:1px solid #040e20 @ 0.69 r 12px | button.b-zy-W_bkButton.mktoReactButton 430.7x55.6 bg #181d26 border T:1px solid #181d26 / R:1px solid #181d26 / B:1px solid #181d26 / L:1px solid #181d26 r 12px shadow #99a0ae @ 0.16 0px 0px 0px 4px, #ffffff 0px 0px 0px 2px |
| Ancestor paint | 3 up div._5aDkOW_formContainer bg #ffffff shadow #1a1d26 @ 0.1 0px 30px 50px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `submit-button-default.png`, `submit-button-hover.png`, `submit-button-focus-visible.png`.

### Cards and indexes

#### story-card-title

Customer stories title.

Page: customer-stories. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 766.38 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 32px/40px 400 |
| Letter spacing | normal |
| Colour | #41454d |
| Transition | all 0.25s ease-in |
| How | at rest |

Crops: `story-card-title-default.png`.

#### story-card

Story row. Story row: a linked customer story row on the index.

Page: customer-stories. Selector: `a story row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 876 x 492.75 | 902.28 x 507.53 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Haas 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333840 | = |
| Text node | p.lpxhIa_typeShort2xs.lpxhIa_bkText: Haas 14px/18.9px 500, #ffffff @ 0.8, ls 0.28px | = |
| Transition | transform 0.15s ease-in | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | matrix(1.03, 0, 0, 1.03, 0, 0) |
| Cursor | grab | = |
| Icon | 20 x 20, colour #ffffff @ 0.8 | 20.6 x 20.6, colour #ffffff @ 0.8 |
| Painted layers | div.dCt_iG_wistiaPlayer.dCt_iG_borderRadiusLG 876.0x492.8 bg #ffffff r 20px; div.w-ui-container 876.0x492.8 bg #000000 r 20px; div 0.0x0.0 bg #181d26 @ 0.8; div 0.0x0.0 image url(data:…) r 20px; div.C02IEq_background 876.0x492.8 image linear-gradient(#000000 @ 0 71.99%, #181d26 @ 0.9 100%, #000000 @ 0.9 100%), linear-gradie r 20px; a.b-zy-W_bkButton.C02IEq_button 134.7x55.6 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 12px | div.dCt_iG_wistiaPlayer.dCt_iG_borderRadiusLG 902.3x507.5 bg #ffffff r 20px; div.w-ui-container 902.3x507.5 bg #000000 r 20px; div 0.0x0.0 bg #181d26 @ 0.8; div 0.0x0.0 image url(data:…) r 20px; div.C02IEq_background 902.3x507.5 image linear-gradient(#000000 @ 0 71.99%, #181d26 @ 0.9 100%, #000000 @ 0.9 100%), linear-gradie r 20px; a.b-zy-W_bkButton.C02IEq_button 138.8x57.3 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 12px |
| How | at rest | mouse hover |

Crops: `story-card-default.png`, `story-card-hover.png`.

#### templates-title

Templates title. The "Templates" h1.

Page: templates. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1120 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas Groot Disp 64px/80px 700 |
| Letter spacing | normal |
| Colour | #101828 |
| Transition | none |
| How | at rest |

Crops: `templates-title-default.png`.

#### templates-search

Template search field. The "Search templates" field in the filter rail. Focused, nothing typed.

Page: templates. Selector: `input[type=search]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 224 x 36 | = |
| Padding | 6px 12px 6px 32px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 0px 0px 1px, #000000 @ 0.13 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.25 0px 0px 0px 2px, #000000 @ 0.13 0px 1px 2px 0px |
| Outline | none | = |
| Font | Haas Groot Disp 18px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #333333 @ 0.5, opacity 1 | = |
| Painted layers | input.w-full.rounded-full 224.0x36.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.13 0px 0px 0px 1px, #000000 @ 0.13 0px 1px 2px 0px | input.w-full.rounded-full 224.0x36.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.25 0px 0px 0px 2px, #000000 @ 0.13 0px 1px 2px 0px |
| How | at rest | clicked into the field |

Crops: `templates-search-default.png`, `templates-search-focused.png`.

#### filter-section

Filter section. A collapsible filter group in the templates rail (By Use Case / By Industry / By Feature).

Page: templates. Selector: `a filter group button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 224 x 27.23 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | Haas Groot Disp 20px/30px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #9ca3af | = | = |
| Text node | h3.font-bold: Haas Groot Disp 14.8px/19.24px 700, #9ca3af | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 14, colour #9ca3af | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.flex.w-full 224.0x27.2 outline 1px auto #005fcc offset 0px |

Crops: `filter-section-default.png`, `filter-section-hover.png`, `filter-section-focus-visible.png`.

#### filter-section-open

Filter section, open. The filter group clicked open; a local expand.

Page: templates. Selector: `the open filter group`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 224 x 286.92 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas Groot Disp 20px/30px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | h3.font-bold: Haas Groot Disp 14.8px/19.24px 700, #9ca3af |
| Transition | none |
| Icon | 14 x 14, colour #9ca3af |
| How | clicked the filter group open |

Crops: `filter-section-open-default.png`.

#### marketplace-title

Marketplace title. The "Marketplace" h1.

Page: marketplace. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 622.59 x 35 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GT Eesti Display 28px/35px 500 |
| Letter spacing | 0.28px |
| Colour | #1d1f25 |
| Transition | none |
| How | at rest |

Crops: `marketplace-title-default.png`.

#### marketplace-search

Marketplace search field. The "Find an extension" field. Focused, nothing typed.

Page: marketplace. Selector: `the search input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 280 x 24 | = |
| Padding | 1px 2px 1px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GT Eesti Display 19.2px/normal 400 | = |
| Letter spacing | 0.192px | = |
| Colour | #1d1f25 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #757575, opacity 1 | = |
| Ancestor paint | 1 up div.flex.items-center bg #ffffff | = |
| How | at rest | clicked into the field |

Crops: `marketplace-search-default.png`, `marketplace-search-focused.png`.

#### market-card

Marketplace category card. A category card on the marketplace ("For marketing teams", "Page designer", "Scripting").

Page: marketplace. Selector: `a coloured category tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 373.33 x 279.98 | = |
| Padding | 0px 0px 279.984px 0px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | = |
| Background image | url(…) | = |
| Box shadow | #000000 @ 0 0px 0px 0px 5px | #000000 @ 0.1 0px 0px 0px 5px |
| Outline | none | = |
| Font | -apple-system 12.8px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #1d1f25 | = |
| Transition | all 0.085s ease-in | = |
| Cursor | pointer | = |
| Painted layers | div.flex-auto.background-cover 373.3x280.0 r 12px shadow #000000 @ 0 0px 0px 0px 5px | div.flex-auto.background-cover 373.3x280.0 r 12px shadow #000000 @ 0.1 0px 0px 0px 5px |
| How | at rest | mouse hover |

Crops: `market-card-default.png`, `market-card-hover.png`.

#### market-cta

Marketplace CTA. A "View all …" button in the marketplace. Measured and focused, never followed.

Page: marketplace. Selector: `a View all button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 108.23 x 32 | = | = | = |
| Padding | 1px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 1px 3px 0px | #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.11 0px 0px 3px 0px, #000000 @ 0.12 0px 1px 4px 0px | = | #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.11 0px 0px 3px 0px, #000000 @ 0.12 0px 1px 4px 0px |
| Outline | none | = | 2px solid #166ee1 offset 2px | = |
| Font | GT Eesti Display 13px/22px 400 | = | = | = |
| Letter spacing | 0.13px | = | = | = |
| Colour | #166ee1 | = | = | = |
| Text node | span.truncate.noevents: GT Eesti Display 13px/22px 400, #166ee1, ls 0.13px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.pointer.items-center 108.2x32.0 bg #ffffff r 6px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 1px 3px 0px | button.pointer.items-center 108.2x32.0 bg #ffffff r 6px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.11 0px 0px 3px 0px, #000000 @ 0.12 0px 1px 4px 0px | button.pointer.items-center 108.2x32.0 bg #ffffff r 6px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 1px 3px 0px outline 2px solid #166ee1 offset 2px | button.pointer.items-center 108.2x32.0 bg #ffffff r 6px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.11 0px 0px 3px 0px, #000000 @ 0.12 0px 1px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `market-cta-default.png`, `market-cta-hover.png`, `market-cta-focus-visible.png`, `market-cta-pressed.png`.

#### template-card

Template card. A template tile in the gallery (the "Project Management" use-case tiles and the featured cards below).

Page: templates. Selector: `a template card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 420 x 215 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 32px | = |
| Background | transparent | = |
| Background image | linear-gradient(to right bottom, #faf5ff, #ede9fe) | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px |
| Outline | none | = |
| Font | Haas Groot Disp 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | div.line-clamp-3.text-base: Haas Groot Disp 20px/27.5px 600, #101828 | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.group.flex 420.0x215.0 image linear-gradient(to right bottom, #faf5ff, #ede9fe) r 32px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; div.mt-4.w-1/2 210.0x199.0 r 32px 0px 0px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | a.group.flex 420.0x215.0 image linear-gradient(to right bottom, #faf5ff, #ede9fe) r 32px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px; div.mt-4.w-1/2 210.0x199.0 r 32px 0px 0px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest | mouse hover |

Crops: `template-card-default.png`, `template-card-hover.png`.

#### whatsnew-title

What's new title. The "Where Airtable is headed." heading.

Page: whatsnew. Selector: `the page heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 459.33 x 94.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 44px/47.08px 550 |
| Letter spacing | -1.6px |
| Colour | #161616 |
| Transition | none |
| How | at rest |

Crops: `whatsnew-title-default.png`.

#### whatsnew-item

What's new card. A release card in the embedded roadmap gallery (plan chips and a release-month chip), inside airtable.com/embed/appL2oaKxSWg9qz8y.

Page: whatsnew. Selector: `a card in the embed`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 387 x 565 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0.24 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 2px 4px 0px | #000000 @ 0.24 0px 0px 1px 0px, #000000 @ 0.16 0px 0px 2px 0px, #000000 @ 0.06 0px 3px 4px 0px, #000000 @ 0.06 0px 6px 8px 0px, #000000 @ 0.08 0px 12px 16px 0px, #000000 @ 0.06 0px 18px 32px 0px |
| Outline | none | = |
| Font | -apple-system 12.8px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #1d1f25 | = |
| Text node | h3.font-family-display-updated.heading-size-small: Inter Display 17px/25.5px 675, #1d1f25, ls -0.16px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.relative.rounded-big 387.0x565.0 bg #ffffff r 6px shadow #000000 @ 0.24 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 2px 4px 0px; div.colors-background-subtle.colors-border-default 387.0x371.0 bg #f2f4f8 border B:1px solid #000000 @ 0.1; span.css-j84x0o.border-box 46.8x22.0 bg #e5e9f0 r 9999px; span.css-j84x0o.border-box 52.6x22.0 bg #c4c7cd r 9999px; span.css-j84x0o.border-box 74.0x22.0 bg #616670 r 9999px; span.css-j84x0o.border-box 118.7x22.0 bg #41454d r 9999px | div.relative.rounded-big 387.0x565.0 bg #ffffff r 6px shadow #000000 @ 0.24 0px 0px 1px 0px, #000000 @ 0.16 0px 0px 2px 0px, #000000 @ 0.06 0px 3px 4px 0px, #000000 @ 0.06 0px 6px 8px 0px, #000000 @ 0.08 0px 12px 16px 0px, #000000 @ 0.06 0px 18px 32px 0px; div.colors-background-subtle.colors-border-default 387.0x371.0 bg #f2f4f8 border B:1px solid #000000 @ 0.1; span.css-j84x0o.border-box 46.8x22.0 bg #e5e9f0 r 9999px; span.css-j84x0o.border-box 52.6x22.0 bg #c4c7cd r 9999px; span.css-j84x0o.border-box 74.0x22.0 bg #616670 r 9999px; span.css-j84x0o.border-box 118.7x22.0 bg #41454d r 9999px |
| How | at rest | mouse hover |

Crops: `whatsnew-item-default.png`, `whatsnew-item-hover.png`.

#### whatsnew-filter

What's new filter. An "Available on" / "Release month" filter dropdown in the embedded release gallery. Measured and focused, never opened.

Page: whatsnew. Selector: `a filter button in the embed`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 112.22 x 28 | = | = |
| Padding | 0px 0px 0px 8px | = | = |
| Border | none | = | = |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 1px 3px 0px | #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.11 0px 0px 3px 0px, #000000 @ 0.12 0px 1px 4px 0px | = |
| Outline | none | = | 2px solid #166ee1 offset 0px |
| Font | -apple-system 13px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1d1f25 | = | = |
| Text node | div.flex.flex-auto: -apple-system 13px/22px 400, #1d1f25 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #1d1f25, fill #000000 | = | = |
| Painted layers | button.pointer.items-center 112.2x28.0 bg #ffffff r 6px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 1px 3px 0px | button.pointer.items-center 112.2x28.0 bg #ffffff r 6px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.11 0px 0px 3px 0px, #000000 @ 0.12 0px 1px 4px 0px | button.pointer.items-center 112.2x28.0 bg #ffffff r 6px shadow #000000 @ 0.32 0px 0px 1px 0px, #000000 @ 0.08 0px 0px 2px 0px, #000000 @ 0.08 0px 1px 3px 0px outline 2px solid #166ee1 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `whatsnew-filter-default.png`, `whatsnew-filter-hover.png`, `whatsnew-filter-focus-visible.png`.

### Mobile (390 wide)

#### m-nav-bar

Top navigation bar (mobile). The header at 390: wordmark and menu button.

Page: home. Selector: `the mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 143.69 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 20px/25px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.flex.flex-col: Haas 14px/17.5px 400, #333840 |
| Transition | all 0.15s ease-in |
| Icon | 18 x 12, colour #254fad |
| Painted layers | nav.HmlLk 390.0x143.7 bg #ffffff shadow #0f306a @ 0.05 0px 0px 20px 0px; div.jQt14.aOvF2 390.0x67.7 bg #f0f6ff; a.X2isC 88.3x18.2 r 10px outline 2px solid #000000 @ 0 offset 4px; div.naiCn 0.0x0.0 bg #ffffff; nav.NKCPB 0.0x0.0 bg #ffffff; nav::before.NKCPB 100%x100% bg #ffffff |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-nav-menu-btn

Nav menu button (mobile). The "Open side menu" button in the mobile header. Opened for the screenshot; nothing is followed.

Page: home. Selector: `the menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 6px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 20px/25px 400 |
| Letter spacing | normal |
| Colour | #181d26 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.SkNqG.IfjuF 24.0x2.0 bg #181d26 r 6px; span.SkNqG.IcEBt 24.0x2.0 bg #181d26 r 6px |
| Ancestor paint | 2 up nav.HmlLk bg #ffffff shadow #0f306a @ 0.05 0px 0px 20px 0px |
| How | at rest |

Crops: `m-nav-menu-btn-default.png`.

#### m-nav-sheet

Mobile nav sheet. The side drawer the "Open side menu" button opens at 390.

Page: mobile. Selector: `the open menu`. States: .

Not found on the page at capture time.

#### m-hero-title

Hero title (mobile). The h1 at 390.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Haas 32px/40px 400 |
| Letter spacing | normal |
| Colour | #333840 |
| Transition | all 0.25s ease-in |
| How | at rest |

Crops: `m-hero-title-default.png`.

## Transitions declared in the readable stylesheets

Airtable's site serves its stylesheets same-origin but as CSS modules with hashed prefixes, so this list holds the transition rules the CSSOM could read on each page; the per-state Transition rows above are computed values and cover the real rules.

- home: `0.15s ease-in`, `none`, `0.2s linear`, `opacity 0.3s ease-in-out`, `width 0.3s ease-in-out`, `opacity 0.2s ease-out`, `opacity 0.5s ease-out, transform 0.5s ease-out, filter 0.5s ease-out`, `transform 0.3s ease-in-out`, `color 0.2s`, `fill 0.2s`, `0.25s`, `0.1s linear`
