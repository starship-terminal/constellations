# Component measurements

Computed styles read from editorx.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844). editorx.com is a redirect shell: every path 301s to wix.com/studio except /pricing, which still serves a Wix plans page on the domain itself — it answered with its "Couldn't load Premium plans" error pane at capture time (measured as such; the plan components come from wix.com/studio/plans). Readings cover the home, features, design, plans, pricing, inspiration, templates, academy and enterprise pages plus the mobile nav — with the cookie banner hidden (never answered) — and were written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Nav bar. The fixed top bar (57px): the Wix Studio wordmark, the Product / Resources / Enterprise dropdown triggers, Pricing, the language selector, Log In and the black Start Creating button.

Page: home. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 989.06 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.ErVudj: Madefor-Display 16px/normal 400, #000000 |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | span.ErVudj 62.5x56.0 border B:4px solid #000000 @ 0; div.aD6GhG 1440.0x0.0 bg #ffffff; div.U79u0Z.zEDyqc 1440.0x588.0 image linear-gradient(#f5f5f5 @ 0.74, #e2efff); ul.D_XV1R 1267.2x357.0 border T:1px solid #d8e2ec; div.CGPrIB 0.0x0.0 image linear-gradient(#f5f5f5 @ 0.74, #e2efff); div.omadZW.xYoOe1 0.0x0.0 image linear-gradient(0deg, #f7f7f8, #daeaff) r 50% |
| Ancestor paint | 1 up div.dsyWYg.oqZt9m bg #ffffff |
| How | at rest |

Crops: `nav-bar-default.png`.

#### logo

Logo. The Wix Studio wordmark anchor.

Page: home. Selector: `nav a /studio`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 83.95 x 56 |
| Padding | 0px 15px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Madefor-Display 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| ::after | 53.9531px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Product button that opens the nav dropdown; toggled, never followed.

Page: home. Selector: `nav button "Product"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.53 x 56 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Gap | 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Madefor-Display 16px/normal 400 | Madefor-Display-Bold 16px/normal 700 | = | Madefor-Display-Bold 16px/normal 700 |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.ErVudj: Madefor-Display 16px/normal 400, #000000 | span.ErVudj: Madefor-Display-Bold 16px/normal 700, #000000 | = | span.ErVudj: Madefor-Display-Bold 16px/normal 700, #000000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| Painted layers | span.ErVudj 62.5x56.0 border B:4px solid #000000 @ 0 | span.ErVudj 62.5x56.0 border B:4px solid #000000 | button.Q3cjxA 117.5x56.0 shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px; span.ErVudj 62.5x56.0 border B:4px solid #000000 @ 0 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The plain Pricing nav link; measured, never followed.

Page: home. Selector: `nav a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.95 x 56 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Madefor-Display 16px/normal 400 | Madefor-Display-Bold 16px/normal 700 | = | Madefor-Display-Bold 16px/normal 700 |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 53.9531px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.twLEiD 84.0x56.0 shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-lang

Language selector. The globe language control ("language selector, english selected"); never opened.

Page: home. Selector: `button[aria-label*=language]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Madefor-Display 16px/normal 400 | Madefor-Display-Bold 16px/normal 700 | = | Madefor-Display-Bold 16px/normal 700 |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.pGUFRX 24.0x24.0 shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |

Crops: `nav-lang-default.png`, `nav-lang-hover.png`, `nav-lang-focus-visible.png`, `nav-lang-pressed.png`.

#### nav-login

Log-in link. The Log In header action; measured, never followed (it leaves for users.wix.com).

Page: home. Selector: `#WIX_STUDIO_HEADER a "Log In"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46.66 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Madefor-Display 16px/normal 400 | Madefor-Display-Bold 16px/normal 700 | = | Madefor-Display-Bold 16px/normal 700 |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 46.6562px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.oQY31L 46.7x20.0 shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The black Start Creating action in the header; measured, never followed.

Page: home. Selector: `#WIX_STUDIO_HEADER a "Start Creating"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 175.28 x 57 | = | = | = |
| Padding | 0px 35px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #3910ed | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Madefor-Text 16px/57px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color 0.4s, 0.4s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.Xu2OUa 175.3x57.0 bg #3910ed | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Nav dropdown. The Product dropdown panel, opened by its own trigger.

Page: home. Selector: `opened Product dropdown`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 510 |
| Padding | 47px 72px 66px 100.797px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.MxW9I3: Madefor-Display 16px/normal 400, #000000 |
| Transition | none |
| Painted layers | ul.D_XV1R 1267.2x357.0 border T:1px solid #d8e2ec |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A link inside the opened Product mega-menu.

Page: home. Selector: `mega-menu link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.03 x 23 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px |
| Outline | none | = | = | = |
| Font | Madefor-Display-Bold 18px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #3910ed | #3910ed | #3910ed |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.eXGFEo 81.0x23.0 shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | a.eXGFEo 81.0x23.0 shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home

#### hero-title

Hero headline. The "Design with impact / Deliver at scale" display headline, madefor-display.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 869.25 x 176.53 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | wix-madefor-display-v2 80.2485px/88.2733px 400 |
| Letter spacing | -2.40745px |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: wix-madefor-display-v2 80.2485px/88.2733px 400, #000000, ls -2.40745px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the display headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 586.13 x 23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | wix-madefor-text-v2 18px/28.8px 400 |
| Letter spacing | -0.18px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The purple "Start creating" pill under the hero copy (the header CTA shares the label, so the header is excluded); measured, never followed.

Page: home. Selector: `"Start creating" pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 221.25 x 56.23 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 1123.88px | = | = | = |
| Background | #ffffff @ 0 | #3910ed @ 0 | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Arial 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.Gf1CuA.wixui-button__label: wix-madefor-text-v2 23.25px/32.5499px 400, #ffffff, ls -0.9px | = | = | = |
| Transition | border-color, background-color 0.4s, 0.4s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 25.4844px x 56.2344px, static, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 0px x 56.2344px, static, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.PoVCDy.wixui-button 221.3x56.2 bg #ffffff @ 0 r 1123.88px | a.PoVCDy.wixui-button 221.3x56.2 bg #3910ed @ 0 r 1123.88px | a.PoVCDy.wixui-button 221.3x56.2 bg #ffffff @ 0 r 1123.88px shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### section-h2

Section heading. A feature-section heading below the hero.

Page: home. Selector: `section h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 751.11 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | wix-madefor-display-v2 54px/54px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: wix-madefor-display-v2 54px/54px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### section-link

Section link. An inline "learn more" link inside a feature section; measured, never followed.

Page: home. Selector: `section link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 218.47 x 32 | = | = | = |
| Padding | 0px 22px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Arial 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.StylableButton2545352419__label.wixui-button__label: madefor-text-mediumbold 16px/normal 400, #000000 | = | = | = |
| Transition | all, visibility 0.2s, 0s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 218.5x32.0 r 50px shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |

Crops: `section-link-default.png`, `section-link-hover.png`, `section-link-focus-visible.png`, `section-link-pressed.png`.

#### showcase-card

Showcase section. The "Site of the week" scroll-jacked showcase (a pinned media scene); measured mid-scroll state may sit between animation frames.

Page: home. Selector: `sticky showcase scene`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: wix-madefor-display-v2 18px/normal 400, #000000 |
| Transition | none |
| Icon | 17 x 17, colour #000000 |
| Painted layers | div.jdJeEr.NYfD3h 1440.0x900.0 bg #455466 @ 0; div.jdJeEr.NYfD3h 648.3x314.7 bg #eeeeee @ 0; div.jdJeEr.NYfD3h 341.3x52.0 bg #ffffff @ 0; div.jdJeEr.NYfD3h 181.0x52.0 bg #ffffff @ 0; a.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 181.0x52.0 bg #000000 r 50px; div.jdJeEr.NYfD3h 137.8x30.0 bg #ffffff @ 0 |
| How | at rest |

Crops: `showcase-card-default.png`.

#### faq-question

FAQ question. A Wix Studio FAQ repeater item (question row); toggled open once for the opened state (local UI).

Page: home. Selector: `FAQ listitem`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 1327.66 x 131.19 | = | = | = | 1327.66 x 442.33 |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Arial 10px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | span.wixui-rich-text__text: wix-madefor-text-v2 24px/31.2001px 500, #000000, ls -0.480001px | = | = | = | = |
| Transition | none | = | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = | = |
| Painted layers | div.jdJeEr.NYfD3h 1327.7x131.2 bg #dce8ff @ 0; div.jdJeEr.NYfD3h 1327.7x1.0 bg #000000; div.jdJeEr.NYfD3h 0.0x0.0 bg #eeeeee @ 0 | = | div.jdJeEr.NYfD3h 1327.7x131.2 bg #dce8ff @ 0; button.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 1327.6x131.2 r 3px shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px; div.jdJeEr.NYfD3h 1327.7x1.0 bg #000000; div.jdJeEr.NYfD3h 0.0x0.0 bg #eeeeee @ 0 | = | div.jdJeEr.NYfD3h 1327.7x442.3 bg #dce8ff @ 0; button.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 1327.6x131.2 r 3px shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px; div.jdJeEr.NYfD3h 1327.7x1.0 bg #000000; div.jdJeEr.NYfD3h 1327.7x311.1 bg #eeeeee @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-pressed.png`, `faq-question-opened.png`.

#### cta-band

CTA band. The closing "Unleash your creations. Rein in the chaos. / Start creating" band.

Page: home. Selector: `closing CTA band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1269 x 171 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #deff00 |
| Box shadow | none |
| Outline | none |
| Font | Arial 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.jdJeEr.NYfD3h 1269.0x171.0 bg #deff00 |
| How | at rest |

Crops: `cta-band-default.png`.

### Features and design

#### feat-h1

Features title. The features page display heading.

Page: features. Selector: `h1 on /studio/features`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 722.83 x 152 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | madefor-display 60.9px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: madefor-display 60.9px/normal 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `feat-h1-default.png`.

#### feat-card

Feature card. A feature card on the features index (a title over its blurb).

Page: features. Selector: `feature card box`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 312 x 116.75 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 16px normal | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Arial 10px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.wixui-rich-text__text: madefor-text-bold 18px/25.2px 400, #000000 | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.jdJeEr.NYfD3h 312.0x116.8 bg #eeeeee @ 0 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `feat-card-default.png`, `feat-card-hover.png`, `feat-card-pressed.png`.

#### feat-link

Feature link. A "learn more" link on the features page; measured, never followed.

Page: features. Selector: `features link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84.78 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Arial 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.StylableButton2545352419__label.wixui-button__label: madefor-text 16px/normal 400, #000000 | = | = | = |
| Transition | all, visibility 0.2s, 0s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.StylableButton2545352419__root.style-lw3lh0ls1__root 84.8x36.0 r 50px shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |

Crops: `feat-link-default.png`, `feat-link-hover.png`, `feat-link-focus-visible.png`, `feat-link-pressed.png`.

#### design-h1

Design title. The design-features page display heading — the page closest to Editor X's old positioning.

Page: design. Selector: `h1 on /studio/design`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1319.53 x 315 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | madefor-display 157.5px/157.5px 400 |
| Letter spacing | -4.72499px |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: madefor-display 157.5px/157.5px 400, #000000, ls -4.72499px |
| Transition | none |
| How | at rest |

Crops: `design-h1-default.png`.

#### design-cta

Design CTA. A call-to-action on the design page; measured, never followed.

Page: design. Selector: `design CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 175.28 x 57 | = | = | = |
| Padding | 0px 35px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #3910ed | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Madefor-Text 16px/57px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color 0.4s, 0.4s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.Xu2OUa 175.3x57.0 bg #3910ed | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `design-cta-default.png`, `design-cta-hover.png`, `design-cta-focus-visible.png`, `design-cta-pressed.png`.

#### design-h2

Design section heading. A section heading on the design page.

Page: design. Selector: `h2 on /studio/design`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 369 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | madefor-display 48px/48px 400 |
| Letter spacing | -0.959999px |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: madefor-display 48px/48px 400, #000000, ls -0.959999px |
| Transition | none |
| How | at rest |

Crops: `design-h2-default.png`.

### Plans and pricing

#### plans-h1

Plans title. The "Choose the right Studio plan for each project" heading.

Page: plans. Selector: `h1 on /studio/plans`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 687.61 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Madefor 32px/36px 700 |
| Letter spacing | normal |
| Colour | #000624 |
| Transition | none |
| How | at rest |

Crops: `plans-h1-default.png`.

#### plan-card

Plan card. A studio plan card (name, price, action).

Page: plans. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 202.02 x 574 |
| Padding | 0px |
| Gap | 0px |
| Border | T: 3px solid #0e106a; R: 1px solid #dfe5eb; B: 1px solid #dfe5eb; L: 1px solid #dfe5eb |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.wds_1_315_0_Heading__root.wds_1_315_0_Heading---appearance-2-H3: Madefor 18px/24px 700, #000624 |
| Transition | none |
| Painted layers | div.wds_1_315_0_Box__root.wds_1_315_0_Box---direction-8-vertical 202.0x574.0 bg #ffffff border T:3px solid #0e106a / R:1px solid #dfe5eb / B:1px solid #dfe5eb / L:1px solid #dfe5eb |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. A plan card's price figure (US$ in the region the capture was served).

Page: plans. Selector: `plan US$ figure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 146.3 x 48 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.wds_1_315_0_Text__root.wds_1_315_0_Text---size-5-small: Madefor 14px/18px 500, #000624 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's action; measured, never followed.

Page: plans. Selector: `plan card CTA`. States: .

Not found on the page at capture time.

#### pricing-h1

Pricing title (editorx.com). The heading editorx.com/pricing serves — on this run, the "Couldn't load Premium plans due to a technical issue" error title.

Page: pricing. Selector: `error title on editorx.com/pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 540 x 258 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.wds-heading.wds-heading--appearance-h3: Madefor 18px/24px 700, #000624 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-badge

Recommended badge. The lime RECOMMENDED badge on the highlighted plan column.

Page: plans. Selector: `"RECOMMENDED" badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 200 x 30 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.wds_1_315_0_Text__root.wds_1_315_0_Text---size-6-medium: Madefor 10px/24px 700, #000624 |
| Transition | none |
| Painted layers | div.wds_1_315_0_Box__root.wds_1_315_0_Box---direction-10-horizontal 200.0x30.0 bg #a6ffd8 |
| Ancestor paint | 1 up div.wds_1_315_0_Box__root.wds_1_315_0_Box---direction-8-vertical bg #ffffff shadow #000624 @ 0.05 0px 6px 6px 0px, #000624 @ 0.1 0px 0px 18px 0px |
| How | at rest |

Crops: `plan-badge-default.png`.

#### pricing-pane

Error pane (editorx.com). The pane the premium-plans widget paints when it fails headless; honest evidence of what the domain serves.

Page: pricing. Selector: `pricing error pane`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 540 x 54 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.wds-text.wds-text--skin-standard: Madefor 14px/18px 400, #868aa5 |
| Transition | none |
| How | at rest |

Crops: `pricing-pane-default.png`.

#### pricing-refresh

Refresh link (editorx.com). The Refresh action inside the error pane; measured, never followed.

Page: pricing. Selector: `error Refresh`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.25 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #116dff offset 1px | = |
| Font | Madefor 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #116dff | #0f62e6 | = | #084ebd |
| Text node | span.wds-button-core__content.wds_1_348_0-button-core__content: Madefor 16px/24px 400, #116dff | span.wds-button-core__content.wds_1_348_0-button-core__content: Madefor 16px/24px 400, #0f62e6 | = | span.wds-button-core__content.wds_1_348_0-button-core__content: Madefor 16px/24px 400, #084ebd |
| Transition | background-color, color, border-color 0.1s linear | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::before | - | = | 57.25px x 24px, absolute, bg #000000 @ 0, radius 2px | = |
| Painted layers | - | = | button.wds-button-core.wds_1_348_0-button-core 57.3x24.0 r 2px outline 3px solid #116dff offset 1px; button::before.wds-button-core.wds_1_348_0-button-core 57.25pxx24px r 2px outline 1px solid #ffffff offset 0px | = |

Crops: `pricing-refresh-default.png`, `pricing-refresh-hover.png`, `pricing-refresh-focus-visible.png`, `pricing-refresh-pressed.png`.

#### pricing-support

Support link (editorx.com). The 'contact Customer Care.' support link inside the error pane's copy; measured, never followed.

Page: pricing. Selector: `error pane support link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.31 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Madefor 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #116dff | #0f62e6 | = | #0f62e6 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 154.3x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: `pricing-support-default.png`, `pricing-support-hover.png`, `pricing-support-focus-visible.png`, `pricing-support-pressed.png`.

### Galleries

#### inspo-h1

Inspiration title. The inspiration gallery heading.

Page: inspiration. Selector: `h1 on /studio/inspiration`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 683.39 x 145.13 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | wfont_1f4e5a_a4dab464d39a4954a3f7d14cdb48d3ed 72.5669px/72.5669px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `inspo-h1-default.png`.

#### inspo-card

Inspiration card. A showcase-site card in the inspiration gallery; measured, never followed.

Page: inspiration. Selector: `inspiration card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 633.77 x 432.34 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff @ 0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.font_8.wixui-rich-text__text: madefor-text 12px/19.2px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Icon | 9 x 9, colour #000000 | = | = | = |
| Painted layers | div.ArRNfA.comp-mcbtnftf 633.8x432.3 bg #ffffff @ 0; div.jdJeEr.NYfD3h 633.8x432.3 bg #eeeeee @ 0; div.jdJeEr.NYfD3h 633.8x432.3 bg #ffffff @ 0; div.jdJeEr.NYfD3h 633.8x34.4 bg #a9806f @ 0; div.jdJeEr.NYfD3h 162.5x34.4 bg #92b079 @ 0; div.jdJeEr.NYfD3h 32.0x32.3 bg #ffffff @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `inspo-card-default.png`, `inspo-card-hover.png`, `inspo-card-focus-visible.png`, `inspo-card-pressed.png`.

#### inspo-filter

Gallery filter. A category filter on the inspiration page; measured unselected.

Page: inspiration. Selector: `inspiration filter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 219.77 x 32 | = | = | = |
| Padding | 0px 22px 0px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.StylableButton2545352419__label.wixui-button__label: wix-madefor-text-v2 20px/normal 400, #ffffff | = | = | = |
| Transition | all, visibility 0.2s, 0s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 219.8x32.0 shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |

Crops: `inspo-filter-default.png`, `inspo-filter-hover.png`, `inspo-filter-focus-visible.png`, `inspo-filter-pressed.png`.

#### templates-h1

Templates title. The studio templates page heading.

Page: templates. Selector: `h1 on /studio/templates`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 215.48 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Madefor 18px/17px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `templates-h1-default.png`.

#### template-card

Template card. A template card in the gallery; measured, never followed.

Page: templates. Selector: `template card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 297.75 x 394.8 | = | - | = |
| Padding | 12px 12px 26px 12px | = | - | = |
| Border | none | = | - | = |
| Radius | 2px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Madefor 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.wds-button-core__content.wds_1_338_0-button-core__content: Madefor 16px/24px 530, #000000 | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.BejCEe 297.8x394.8 bg #ffffff r 2px; div::before.c6WCwF.PwfXtm 273.75pxx633.594px image linear-gradient(#dfe0ff @ 0, #dfe0ff 50%, #dfe0ff @ 0); div::after.c6WCwF.PwfXtm 273.75pxx633.594px image linear-gradient(#dfe0ff @ 0, #dfe0ff 50%, #dfe0ff @ 0); div.qKpTmT 273.8x316.8 bg #000000 @ 0.8; a.wds-button-core.wds_1_338_0-button-core 102.0x42.0 bg #ffffff r 21px outline 1px solid #000000 @ 0 offset -1px; a.wds-button-core.wds_1_338_0-button-core 102.0x42.0 r 21px outline 1px solid #ffffff @ 0.5 offset -1px | div.BejCEe 297.8x394.8 bg #ffffff r 2px; div::before.c6WCwF.PwfXtm 273.75pxx633.594px image linear-gradient(#dfe0ff @ 0, #dfe0ff 50%, #dfe0ff @ 0); div::after.c6WCwF.PwfXtm 273.75pxx633.594px image linear-gradient(#dfe0ff @ 0, #dfe0ff 50%, #dfe0ff @ 0); div.qKpTmT 273.8x316.8 bg #000000 @ 0.8; a.wds-button-core.wds_1_338_0-button-core 102.0x42.0 bg #ffffff r 21px outline 1px solid #000000 @ 0 offset -1px; a.wds-button-core.wds_1_338_0-button-core 102.0x42.0 bg #e7f0ff r 21px outline 1px solid #000000 @ 0 offset -1px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `template-card-default.png`, `template-card-hover.png`, `template-card-pressed.png`.

### Academy and enterprise

#### academy-h1

Academy title. The studio academy heading.

Page: academy. Selector: `h1 on /studio/academy`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1222.5 x 75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | madefor-display 75px/75px 400 |
| Letter spacing | -1.5px |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: madefor-display 75px/75px 400, #000000, ls -1.5px |
| Transition | none |
| How | at rest |

Crops: `academy-h1-default.png`.

#### academy-card

Academy card. A course or tutorial card on the academy page; measured, never followed.

Page: academy. Selector: `academy card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 673.13 x 631.38 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.wixui-rich-text__text: madefor-display 26.6px/29.26px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Icon | 54.61 x 54.61, colour #000000 | = | = | = |
| Painted layers | div.jdJeEr.NYfD3h 673.1x631.4 bg #bed6ff r 34px; div.jdJeEr.NYfD3h 399.6x58.5 bg #ffffff @ 0; div.jdJeEr.NYfD3h 590.6x449.1 bg #ffffff @ 0; div.jdJeEr.NYfD3h 133.4x34.4 bg #ffffff @ 0; div.jdJeEr.NYfD3h 107.4x2.0 bg #000000 | div.jdJeEr.NYfD3h 673.1x631.4 bg #bed6ff r 34px; div.jdJeEr.NYfD3h 399.6x58.5 bg #ffffff @ 0; div.jdJeEr.NYfD3h 590.6x449.1 bg #ffffff @ 0; a.PoVCDy.wixui-button 590.6x449.1 bg #3910ed @ 0; div.jdJeEr.NYfD3h 133.4x34.4 bg #ffffff @ 0; div.jdJeEr.NYfD3h 107.4x2.0 bg #000000 | div.jdJeEr.NYfD3h 673.1x631.4 bg #bed6ff r 34px; div.jdJeEr.NYfD3h 399.6x58.5 bg #ffffff @ 0; div.UeoHYs 590.6x449.1 r 8px shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px; div.UCYv5s 0.0x11.0 shadow #ffffff 0px 0px 1px 2px outline 2px solid #116dff offset 1px; div.jdJeEr.NYfD3h 590.6x449.1 bg #ffffff @ 0; div.jdJeEr.NYfD3h 133.4x34.4 bg #ffffff @ 0 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `academy-card-default.png`, `academy-card-hover.png`, `academy-card-focus-visible.png`, `academy-card-pressed.png`.

#### ent-h1

Enterprise title. The enterprise page display heading.

Page: enterprise. Selector: `h1 on /studio/enterprise`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1222.52 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | wix-madefor-display-v2 60px/60px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: wix-madefor-display-v2 60px/60px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `ent-h1-default.png`.

#### ent-cta

Enterprise CTA. A Contact-sales-style action on the enterprise page; measured, never followed.

Page: enterprise. Selector: `enterprise CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 144.47 x 52 | = | = | = |
| Padding | 0px 4px 0px 30px | 0px 16px 0px 20px | = | 0px 16px 0px 20px |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Arial 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.StylableButton2545352419__label.wixui-button__label: madefor-text-mediumbold 16px/normal 400, #ffffff | = | = | = |
| Transition | all, visibility 0.2s, 0s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17 x 17, colour #000000 | 15 x 15, colour #000000, fill #ffffff | = | 15 x 15, colour #000000, fill #ffffff |
| Painted layers | a.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 144.5x52.0 bg #000000 r 50px | = | a.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 144.5x52.0 bg #000000 r 50px shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ent-cta-default.png`, `ent-cta-hover.png`, `ent-cta-focus-visible.png`, `ent-cta-pressed.png`.

### Footer

#### footer

Footer. The Wix Studio footer: the blurb, link columns, social icons, language and legal.

Page: home. Selector: `footer#WIX_STUDIO_FOOTER`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 793 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.DeaxD1: Madefor-Text 14px/20px 400, #f6f6f6 |
| Transition | none |
| Icon | 188 x 31, colour #f6f6f6 |
| Painted layers | nav.tuyyeT 1440.0x793.0 bg #0e0e0e; div.VK8FJF 0.0x0.0 bg #848280; div.fbTMfh 1296.0x56.0 shadow #848280 0px -1px 0px 0px; button.ZXBKx_ 36.0x36.0 border T:1px solid #f6f6f6 / R:1px solid #f6f6f6 / B:1px solid #f6f6f6 / L:1px solid #f6f6f6 r 50% |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52.22 x 34 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #828282 0px 0px 0px 1px, #828282 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Madefor-Text 16px/34px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6f6f6 | #828282 | #828282 | #828282 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Pllco1 52.2x34.0 shadow #828282 0px 0px 0px 1px, #828282 0px 0px 0px 3px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #828282 0px 0px 0px 1px, #828282 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Arial 10px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6f6f6 | #828282 | #828282 | #828282 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #f6f6f6, fill #000000 | 24 x 24, colour #828282, fill #000000 | 24 x 24, colour #828282, fill #000000 | 24 x 24, colour #828282, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Rv9f2H 24.0x24.0 shadow #828282 0px 0px 0px 1px, #828282 0px 0px 0px 3px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile nav. The fixed mobile top bar (the wordmark, the square Start Creating and the burger menu button) — the page header is not a <nav> at phone width.

Page: mobile. Selector: `fixed top bar at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 47 |
| Padding | 0px 0px 0px 20px |
| Border | T: none; R: none; B: 1px solid #d8e2ec; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Arial 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.cnoYcn: Madefor-Display 14px/normal 400, #ffffff |
| Transition | transform 0.3s linear |
| Icon | 145 x 24, colour #000000 |
| Painted layers | div.dsyWYg.oqZt9m 390.0x47.0 bg #ffffff border B:1px solid #d8e2ec; a.cnoYcn 124.5x46.0 bg #3910ed; nav.BrYaz7 0.0x0.0 bg #ffffff; div.U79u0Z.zEDyqc 0.0x0.0 image linear-gradient(#f5f5f5 @ 0.74, #e2efff); ul.D_XV1R 0.0x0.0 border T:1px solid #d8e2ec; div.CGPrIB 0.0x0.0 image linear-gradient(#f5f5f5 @ 0.74, #e2efff) |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The burger/menu toggle in the mobile nav.

Page: mobile. Selector: `nav menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 50 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 50 x 46, colour #000000 |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The opened mobile navigation panel.

Page: mobile. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 797 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Arial 10px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.ErVudj: Madefor-Display 16px/normal 400, #000000 |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | nav.BrYaz7.rrUKB6 390.0x797.0 bg #ffffff; div.U79u0Z.zEDyqc 0.0x0.0 image linear-gradient(#f5f5f5 @ 0.74, #e2efff); ul.D_XV1R 0.0x0.0 border T:1px solid #d8e2ec; div.CGPrIB 0.0x0.0 image linear-gradient(#f5f5f5 @ 0.74, #e2efff); div.omadZW.xYoOe1 0.0x0.0 image linear-gradient(0deg, #f7f7f8, #daeaff) r 50%; span.L47wCD 0.0x0.0 border B:1px solid #000000 |
| Ancestor paint | 1 up div.dsyWYg.oqZt9m bg #ffffff |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A row inside the opened mobile menu.

Page: mobile. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 50 | = | = | = |
| Padding | 15px 27.2969px | = | = | = |
| Gap | 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Madefor-Display 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.ErVudj: Madefor-Display 16px/normal 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.Q3cjxA 390.0x50.0 shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332.45 x 75.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | wix-madefor-display-v2 34.5313px/37.9844px 400 |
| Letter spacing | -0.345313px |
| Colour | #000000 |
| Text node | span.wixui-rich-text__text: wix-madefor-display-v2 34.5313px/37.9844px 400, #000000, ls -0.345313px |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

wix.com/studio is a thunderbolt build: the rules the inline styles expose are listed per page (the linked parastorage bundles are captured separately in raw/css-vars.json), and the per-state Transition rows above are the computed values the page paints.

- academy: `opacity 0.5s, visibility 0.5s`, `opacity var(--transition-duration) cubic-bezier(.37, 0, .63, 1)`, `opacity var(--transition-duration) cubic-bezier(.64, 0, .78, 0)`, `opacity var(--transition-duration) cubic-bezier(.22, 1, .36, 1)`, `transform var(--transition-duration) cubic-bezier(.87, 0, .13, 1)`, `0.2s, visibility`, `inherit`, `0.2s ease-in`, `0.2s`, `outline 10ms`, `filter 0.8s ease-in`, `var(--trans,color .4s ease 0s)`

- design: `opacity 0.5s, visibility 0.5s`, `opacity var(--transition-duration) cubic-bezier(.37, 0, .63, 1)`, `opacity var(--transition-duration) cubic-bezier(.64, 0, .78, 0)`, `opacity var(--transition-duration) cubic-bezier(.22, 1, .36, 1)`, `transform var(--transition-duration) cubic-bezier(.87, 0, .13, 1)`, `0.2s, visibility`, `inherit`, `0.2s ease-in`, `0.2s`, `outline 10ms`, `filter 0.8s ease-in`, `var(--trans,color .4s ease 0s)`

- features: `opacity 0.5s, visibility 0.5s`, `opacity var(--transition-duration) cubic-bezier(.37, 0, .63, 1)`, `opacity var(--transition-duration) cubic-bezier(.64, 0, .78, 0)`, `opacity var(--transition-duration) cubic-bezier(.22, 1, .36, 1)`, `transform var(--transition-duration) cubic-bezier(.87, 0, .13, 1)`, `0.2s, visibility`, `inherit`, `0.2s ease-in`, `0.2s`, `outline 10ms`, `filter 0.8s ease-in`, `var(--trans,color .4s ease 0s)`

- home: `opacity 0.5s, visibility 0.5s`, `opacity var(--transition-duration) cubic-bezier(.37, 0, .63, 1)`, `opacity var(--transition-duration) cubic-bezier(.64, 0, .78, 0)`, `opacity var(--transition-duration) cubic-bezier(.22, 1, .36, 1)`, `transform var(--transition-duration) cubic-bezier(.87, 0, .13, 1)`, `0.2s, visibility`, `inherit`, `0.2s ease-in`, `0.2s`, `outline 10ms`, `filter 0.8s ease-in`, `var(--trans,color .4s ease 0s)`

- inspiration: `opacity 0.5s, visibility 0.5s`, `opacity var(--transition-duration) cubic-bezier(.37, 0, .63, 1)`, `opacity var(--transition-duration) cubic-bezier(.64, 0, .78, 0)`, `opacity var(--transition-duration) cubic-bezier(.22, 1, .36, 1)`, `transform var(--transition-duration) cubic-bezier(.87, 0, .13, 1)`, `0.2s, visibility`, `inherit`, `0.2s ease-in`, `0.2s`, `outline 10ms`, `filter 0.8s ease-in`, `var(--trans,color .4s ease 0s)`

- plans: none

- pricing: none

- templates: none
