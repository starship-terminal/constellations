# Component measurements

Computed styles read from aaply.app on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Nav bar. The floating rounded-white bar: aaply logo left, Features / Value / Pricing / Reviews links centre, Log in ghost button and the black Sign up pill right.

Page: home. Selector: `shape nav bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 166 |
| Padding | 0px |
| Border | none |
| Radius | 40px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| Painted layers | div.tn-atom 1200.0x166.0 bg #ffffff r 40px |
| How | at rest |

Crops: `nav-bar-default.png`.

#### logo

Logo. The aaply wordmark with the lime chevron-roof mark, top-left of the nav bar.

Page: home. Selector: `logo atom`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119 x 31.72 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff8562 | = | = | = |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.tn-atom 119.0x31.7 outline 3px auto #2015ff offset 4px | = |

Crops: `logo-default.png`, `logo-hover.png`, `logo-focus-visible.png`, `logo-pressed.png`.

#### nav-link

Nav link. A text link in the nav bar (Features / Value / Pricing / Reviews), Inter 18px.

Page: home. Selector: `nav link atom`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68 x 34 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 30px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Inter 18px/27.9px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #494949 | = | #494949 |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #000000 | span.tn-atom__button-text: Inter 18px/27.9px 400, #494949 | = | span.tn-atom__button-text: Inter 18px/27.9px 400, #494949 |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px, shadow #000000 0px 0px 0px 0px inset | 100% x 100%, absolute, bg #000000 @ 0, radius 0px, shadow #494949 0px 0px 0px 0px inset | = | 100% x 100%, absolute, bg #000000 @ 0, radius 0px, shadow #494949 0px 0px 0px 0px inset |
| Painted layers | a::after.tn-atom 100%x100% shadow #000000 0px 0px 0px 0px inset | a::after.tn-atom 100%x100% shadow #494949 0px 0px 0px 0px inset | a.tn-atom 68.0x34.0 r 30px outline 3px auto #2015ff offset 4px; a::after.tn-atom 100%x100% shadow #000000 0px 0px 0px 0px inset | a::after.tn-atom 100%x100% shadow #494949 0px 0px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in button. The ghost pill in the nav bar; links to the app host (go.aaply.app). Hovered and focused only — pressing leaves for auth.

Page: home. Selector: `nav Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #cccccc | = | = | = |
| Radius | 30px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Inter 18px/27.9px 300 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #494949 | = | #494949 |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 300, #000000 | span.tn-atom__button-text: Inter 18px/27.9px 300, #494949 | = | span.tn-atom__button-text: Inter 18px/27.9px 300, #494949 |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.tn-atom 90.0x44.0 border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 30px | = | a.tn-atom 90.0x44.0 border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 30px outline 3px auto #2015ff offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

Sign up button. The black Sign up pill in the nav bar; links to go.aaply.app/signup. Hovered and focused only.

Page: home. Selector: `nav Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 | 1px solid #e6e51e | = | 1px solid #e6e51e |
| Radius | 30px | = | = | = |
| Background | #000000 | #e6e51e | = | #e6e51e |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Inter 18px/27.9px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #000000 | = | #000000 |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.tn-atom 134.0x44.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 30px | a.tn-atom 134.0x44.0 bg #e6e51e border T:1px solid #e6e51e / R:1px solid #e6e51e / B:1px solid #e6e51e / L:1px solid #e6e51e r 30px | a.tn-atom 134.0x44.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 30px outline 3px auto #2015ff offset 4px | a.tn-atom 134.0x44.0 bg #e6e51e border T:1px solid #e6e51e / R:1px solid #e6e51e / B:1px solid #e6e51e / L:1px solid #e6e51e r 30px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

#### footer

Footer. The black footer band: "Made remotely with love", the aaply@aaply.app mail link, social icons (Twitter, Medium, LinkedIn, Discord, YouTube, Instagram) and the second nav list.

Page: home. Selector: `footer band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1088 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| Painted layers | div.tn-atom 1440.0x1088.0 bg #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer mail link. The aaply@aaply.app contact link in the footer.

Page: home. Selector: `footer mailto`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.28 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Inter 15px/23px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e6e51e | #c4c4c4 | = | #c4c4c4 |
| Transition | all 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 121.3x19.0 outline 3px auto #2015ff offset 4px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social icon. One of the social-icon links in the footer.

Page: home. Selector: `social icon a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Times New Roman 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff8562 | = | = | = |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.tn-atom 32.0x32.0 outline 3px auto #2015ff offset 4px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

#### early-birds

Early birds heading. "Join the early birds" — the Poppins display heading of the pre-footer CTA band ("Be the first to try").

Page: home. Selector: `early birds heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 52px/81px 700 |
| Letter spacing | -1px |
| Colour | #ffffff |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `early-birds-default.png`.

### Home

#### hero-title

Hero title. The Poppins 700 display headline with inline emoji/avatar atoms inside the sentence flow ("Tool that helps teams design mobile apps…").

Page: home. Selector: `hero text atom`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 792 x 240 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 57px/60px 700 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-emoji

Hero inline image. One of the inline emoji/squiggle/avatar atoms set inside the headline flow — the design's signature move.

Page: home. Selector: `inline emoji atom`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 144 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `hero-emoji-default.png`.

#### cta-signup-free

Sign up free CTA. The lime "Sign up fo free →" pill (the typo is the product's own). Links to go.aaply.app/signup; hovered and focused only.

Page: home. Selector: `lime hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 286 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 30px | = | = | = |
| Background | #e6e51e | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Inter 18px/27.9px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #000000 | = | = | = |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.tn-atom 286.0x60.0 bg #e6e51e r 30px | = | a.tn-atom 286.0x60.0 bg #e6e51e r 30px outline 3px auto #2015ff offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-signup-free-default.png`, `cta-signup-free-hover.png`, `cta-signup-free-focus-visible.png`, `cta-signup-free-pressed.png`.

#### cta-demo

Try demo CTA. The black "Try demo project" pill beside the lime CTA. Links to the app host's demo workspace; hovered and focused only.

Page: home. Selector: `black hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 286 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 30px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Inter 18px/27.9px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #ffffff | = | = | = |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.tn-atom 286.0x60.0 bg #000000 r 30px | = | a.tn-atom 286.0x60.0 bg #000000 r 30px outline 3px auto #2015ff offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-demo-default.png`, `cta-demo-hover.png`, `cta-demo-focus-visible.png`, `cta-demo-pressed.png`.

#### hero-mock

Hero product mockup. The product canvas inside a browser-chrome frame: the aaply workspace with screen tiles, connection arrows and collaborator cursors.

Page: home. Selector: `hero mockup`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 695 x 521.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `hero-mock-default.png`.

#### chat-bubble

Chat annotation bubble. One of the fake-chat bubbles annotating the page (Have you seen this? / Looks nice! / I wanna try too) — rounded white bubbles with avatar stamps.

Page: home. Selector: `chat bubble atom`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 371 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 31px/48px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `chat-bubble-default.png`.

#### step-number

Step number. The circled step numeral opening the "how it works" sequence.

Page: home. Selector: `step numeral`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 60 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 27px/42px 700 |
| Letter spacing | -2px |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `step-number-default.png`.

### Pricing

#### pricing-title

Pricing title. The page heading in Poppins 700.

Page: pricing. Selector: `pricing title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 851 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 57px/60px 700 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-toggle

Billing toggle. The Monthly / Yearly segment pair: 152x60 pills, the held segment filled lime.

Page: pricing. Selector: `billing segment`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f2f2f2 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #000000 |
| Transition | none |
| Painted layers | div.t396__artboard.rendered 1440.0x75.0 bg #f2f2f2; div.tn-atom 316.0x66.0 border T:1px solid #1a1a1a / R:1px solid #1a1a1a / B:1px solid #1a1a1a / L:1px solid #1a1a1a r 64px; div.tn-atom 152.0x60.0 bg #e7e51e r 30px; div.tn-atom 87.0x34.0 bg #fa3e3e r 30px |
| How | at rest |

Crops: `billing-toggle-default.png`.

#### billing-yearly

Yearly option. The Yearly segment pill; selected by default.

Page: pricing. Selector: `Yearly pill`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 152 x 60 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 30px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 18px/27.9px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #000000 | = | = |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = |
| Cursor | pointer | = | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `billing-yearly-default.png`, `billing-yearly-hover.png`, `billing-yearly-pressed.png`.

#### billing-monthly

Monthly option. The Monthly segment pill.

Page: pricing. Selector: `Monthly pill`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 152 x 60 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 30px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 18px/27.9px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #000000 | = |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = |
| How | at rest | mouse hover |

Crops: `billing-monthly-default.png`, `billing-monthly-hover.png`.

#### billing-monthly-on

Monthly option (selected). The Monthly segment after pressing it: client-side state swap, nothing posted.

Page: pricing. Selector: `Monthly pill on`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 152 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 30px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/27.9px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #000000 |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| Cursor | pointer |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `billing-monthly-on-open.png`.

#### plan-price-monthly

Plan price (monthly). The plan price after switching to Monthly (the price is split across sibling atoms: a "$" atom and a ".1 /month" numeral atom).

Page: pricing. Selector: `price monthly`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 308 x 47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 35px/47px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `plan-price-monthly-open.png`.

#### save-badge

Save badge. The coral "Save 30%" badge beside the billing toggle.

Page: pricing. Selector: `save badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 87 x 34 |
| Padding | 0px |
| Border | none |
| Radius | 30px |
| Background | #fa3e3e |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/23.25px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.tn-atom__button-text: Inter 15px/23.25px 400, #ffffff |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.tn-atom 87.0x34.0 bg #fa3e3e r 30px |
| How | at rest |

Crops: `save-badge-default.png`.

#### plan-card-free

Plan card (Free). The white Free plan card: $0, "Easy start for mobile creators", feature list, 3D character render.

Page: pricing. Selector: `free card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 561 x 618 |
| Padding | 0px |
| Border | none |
| Radius | 36px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| Painted layers | div.tn-atom 561.0x618.0 bg #ffffff r 36px |
| How | at rest |

Crops: `plan-card-free-default.png`.

#### plan-card-plus

Plan card (Plus). The lime Plus card: $11.1 /month billed yearly, "Full access for the price of a cup of coffee", 3D character render.

Page: pricing. Selector: `plus card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 561 x 618 |
| Padding | 0px |
| Border | none |
| Radius | 36px |
| Background | #e6e51e |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| Painted layers | div.tn-atom 561.0x618.0 bg #e6e51e r 36px |
| How | at rest |

Crops: `plan-card-plus-default.png`.

#### plan-name

Plan name. A plan name (Free / Plus) on the card.

Page: pricing. Selector: `plan name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 88 x 47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 35px/47px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. The large price numeral with the /month suffix.

Page: pricing. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308 x 47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 35px/47px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The Get started / Start for free button inside a plan card. Hovered and focused only.

Page: pricing. Selector: `plan cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 227 x 60 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 30px | = | = | = |
| Background | #e6e51e | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Inter 18px/27.9px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #000000 | = | = | = |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.tn-atom 227.0x60.0 bg #e6e51e r 30px | = | a.tn-atom 227.0x60.0 bg #e6e51e r 30px outline 3px auto #2015ff offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### compare-cta

Compare features link. The "Compare features →" link under the cards.

Page: pricing. Selector: `compare link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 851 x 60 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Poppins 57px/60px 700 | = | - | = |
| Letter spacing | -1px | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `compare-cta-default.png`, `compare-cta-hover.png`, `compare-cta-pressed.png`.

#### feature-table

Feature table. The feature-comparison table card: rows of features with checkmarks, "+" and "soon" pills.

Page: pricing. Selector: `feature table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 527 x 1166 |
| Padding | 0px |
| Border | none |
| Radius | 40px |
| Background | #e6e51e |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| Painted layers | div.tn-atom 527.0x1166.0 bg #e6e51e r 40px |
| How | at rest |

Crops: `feature-table-default.png`.

### Features

#### features-title

Features title. "Here's what aaply workflow looks like" — Poppins display with an inline squiggle.

Page: features. Selector: `features title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 792 x 180 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 57px/60px 700 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `features-title-default.png`.

#### step-title

Step title. A numbered step heading in the workflow sequence ("Start your new mobile app design project").

Page: features. Selector: `step title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 156 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 47px/52px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `step-title-default.png`.

#### step-card

Step card. A workflow step's product panel: the browser-chrome-framed app screenshot beside the chat annotation bubble.

Page: features. Selector: `step panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1131 x 642.86 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `step-card-default.png`.

#### mega-demo-cta

Mega demo CTA. The oversized "Try DEMO project →" button (520x96) closing the features page. Links to the demo workspace; hovered and focused only.

Page: features. Selector: `mega demo cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 520 x 96 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #2015ff offset 4px | = |
| Font | Inter 18px/27.9px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.tn-atom__button-text: Inter 18px/27.9px 400, #ffffff | = | = | = |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.tn-atom 520.0x96.0 bg #000000 r 50px | = | a.tn-atom 520.0x96.0 bg #000000 r 50px outline 3px auto #2015ff offset 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mega-demo-cta-default.png`, `mega-demo-cta-hover.png`, `mega-demo-cta-focus-visible.png`, `mega-demo-cta-pressed.png`.

### Value

#### value-title

Value title. "Aaply is here to boost your creativity" — the Poppins display heading.

Page: value. Selector: `value title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 605 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 57px/60px 700 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `value-title-default.png`.

#### value-card

Value card. A square value-proposition cell in the Value grid (lime/white rounded shape with icon and caption atoms).

Page: value. Selector: `value cell`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 271 x 272 |
| Padding | 0px |
| Border | none |
| Radius | 40px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| Painted layers | div.tn-atom 271.0x272.0 bg #ffffff r 40px |
| How | at rest |

Crops: `value-card-default.png`.

### Reviews

#### review-card

Review card. A testimonial card in the grid (370x580): quote text, an embedded image or chat screenshot.

Page: reviews. Selector: `review card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 370 x 580 |
| Padding | 0px |
| Border | none |
| Radius | 40px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.tn-atom 370.0x580.0 bg #ffffff r 40px |
| How | at rest |

Crops: `review-card-default.png`.

#### review-text

Review quote. The quote text inside a review card or the featured slide.

Page: reviews. Selector: `review text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 951 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 35px/42px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `review-text-default.png`.

#### review-slide

Review slide. The wide lime featured-review slide at the top: avatar, name and role, the quote in Poppins, a "Try it for free" ghost pill; carousel dots below.

Page: reviews. Selector: `review slide`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1157 x 418 |
| Padding | 0px |
| Border | none |
| Radius | 40px |
| Background | #e7e51e |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.tn-atom 1157.0x418.0 bg #e7e51e r 40px |
| How | at rest |

Crops: `review-slide-default.png`.

### Our story

#### story-block

Story paragraph. A long-form body paragraph in the story.

Page: story. Selector: `story text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 565 x 230 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 35px/46px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `story-block-default.png`.

#### story-lead

Story lead. "Our story started with a wish!" — the page's opening editorial block.

Page: story. Selector: `story lead`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 851 x 420 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 57px/60px 700 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `story-lead-default.png`.

### Team

#### team-title

Team title. "Our Team" — the Poppins display heading.

Page: team. Selector: `team title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 851 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 57px/60px 700 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `team-title-default.png`.

#### member-card

Member card. A team-member card (359x479): 3D character avatar, name, role.

Page: team. Selector: `member card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 359 x 479 |
| Padding | 0px |
| Border | 1px solid #cccccc |
| Radius | 36px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.tn-atom 359.0x479.0 border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 36px |
| How | at rest |

Crops: `member-card-default.png`.

### Figma plugin

#### figma-title

Figma plugin title. "Aaply Figma Plugin" display heading.

Page: figma. Selector: `figma title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 605 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 57px/60px 700 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `figma-title-default.png`.

#### figma-step

Export step card. A numbered step card in the export instructions (Design your app in Aaply → Click the export button → Follow the link).

Page: figma. Selector: `figma step card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 561 x 273 |
| Padding | 0px |
| Border | 1px solid #cccccc |
| Radius | 36px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div.tn-atom 561.0x273.0 border T:1px solid #cccccc / R:1px solid #cccccc / B:1px solid #cccccc / L:1px solid #cccccc r 36px |
| How | at rest |

Crops: `figma-step-default.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile nav bar. The mobile header: logo left, hamburger right.

Page: home. Selector: `mobile nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 370.5 x 166 |
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
| Painted layers | div.tn-atom 370.5x166.0 bg #ffffff r 40px |
| Ancestor paint | 3 up div.r.t-rec shadow #000000 @ 0 0px 1px 3px 0px |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-burger

Hamburger. The mobile menu button at the top right. Not opened — the menu overlays the measured content.

Page: home. Selector: `burger`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 92 x 24.53 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Times 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #ff8562 | = |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-burger-default.png`, `m-burger-pressed.png`.

#### m-hero-title

Mobile hero title. The first painted line of the mobile Poppins headline — the mobile title splits one atom per line.

Page: home. Selector: `mobile hero`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 264 x 27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 27px/27px 700 |
| Letter spacing | -1px |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-cta-signup

Mobile sign up CTA. The full-width lime pill.

Page: home. Selector: `mobile lime cta`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 280 x 55 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 30px | = |
| Background | #e6e51e | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 15px/23.25px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.tn-atom__button-text: Inter 15px/23.25px 400, #000000 | = |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | a.tn-atom 280.0x55.0 bg #e6e51e r 30px | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-cta-signup-default.png`, `m-cta-signup-pressed.png`.

#### m-cta-demo

Mobile demo CTA. The full-width black pill.

Page: home. Selector: `mobile black cta`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 280 x 55 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 30px | = |
| Background | #000000 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 15px/23.25px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.tn-atom__button-text: Inter 15px/23.25px 400, #ffffff | = |
| Transition | background-color, color, border-color, box-shadow 0.2s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| ::after | 100% x 100%, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | a.tn-atom 280.0x55.0 bg #000000 r 30px | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-cta-demo-default.png`, `m-cta-demo-pressed.png`.

#### m-step-number

Mobile step number. The circled step numeral in the mobile how-it-works column.

Page: home. Selector: `mobile step numeral`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 30 x 23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Poppins 15px/23px 700 |
| Letter spacing | -2px |
| Colour | #000000 |
| Transition | background-color, color, border-color, box-shadow 0s, 0s, 0s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s |
| How | at rest |

Crops: `m-step-number-default.png`.

## Transitions declared in the readable stylesheets

aaply.app is a Tilda build: its stylesheets are same-origin and readable, but they declare almost no design tokens (the --w* layout widths and --anim-nav) — the design values live in per-elem inline styles, read as computed styles above; the per-state Transition rows are computed values.

- features: `opacity 0.2s ease-in-out`, `background-color var(--t396-speedhover,0s) ease-in-out,color var(--t396-speedhover,0s) ease-in-out,border-color var(--t396-speedhover,0s) ease-in-out,box-shadow var(--t396-shadowshoverspeed,0.2s) ease-in-out`, `color var(--t396-speedhover,0s) ease-in-out`, `color 0.3s ease-in-out, opacity 0.3s ease-in-out`, `0.3s`, `background-color 0.3s linear, transition 0.3s linear, opacity 0.3s linear`, `opacity var(--anim-nav) ease`, `all var(--anim-nav) ease`, `opacity 0.7s ease-in-out`, `0.1s ease-in-out`, `0.3s ease-in-out`

- figma: `opacity 0.2s ease-in-out`, `background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out`, `color 0.3s ease-in-out, opacity 0.3s ease-in-out`, `0.3s`, `background-color 0.3s linear, transition 0.3s linear, opacity 0.3s linear`, `opacity var(--anim-nav) ease`, `all var(--anim-nav) ease`, `opacity 0.7s ease-in-out`, `0.1s ease-in-out`, `0.3s ease-in-out`

- home: `opacity 0.2s ease-in-out`, `background-color var(--t396-speedhover,0s) ease-in-out,color var(--t396-speedhover,0s) ease-in-out,border-color var(--t396-speedhover,0s) ease-in-out,box-shadow var(--t396-shadowshoverspeed,0.2s) ease-in-out`, `color var(--t396-speedhover,0s) ease-in-out`, `color 0.3s ease-in-out, opacity 0.3s ease-in-out`, `0.3s`, `background-color 0.3s linear, transition 0.3s linear, opacity 0.3s linear`, `opacity var(--anim-nav) ease`, `all var(--anim-nav) ease`, `opacity 0.7s ease-in-out`, `0.1s ease-in-out`, `0.3s ease-in-out`

- pricing: `opacity 0.2s ease-in-out`, `background-color var(--t396-speedhover,0s) ease-in-out,color var(--t396-speedhover,0s) ease-in-out,border-color var(--t396-speedhover,0s) ease-in-out,box-shadow var(--t396-shadowshoverspeed,0.2s) ease-in-out`, `color var(--t396-speedhover,0s) ease-in-out`, `color 0.3s ease-in-out, opacity 0.3s ease-in-out`, `0.3s`, `background-color 0.3s linear, transition 0.3s linear, opacity 0.3s linear`, `opacity var(--anim-nav) ease`, `all var(--anim-nav) ease`, `opacity 0.7s ease-in-out`, `0.1s ease-in-out`, `0.3s ease-in-out`

- reviews: `opacity 0.2s ease-in-out`, `background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out`, `color 0.3s ease-in-out, opacity 0.3s ease-in-out`, `0.3s`, `background-color 0.3s linear, transition 0.3s linear, opacity 0.3s linear`, `opacity var(--anim-nav) ease`, `all var(--anim-nav) ease`, `opacity 0.7s ease-in-out`, `0.1s`, `0.3s ease-in-out`

- story: `opacity 0.2s ease-in-out`, `background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out`, `color 0.3s ease-in-out, opacity 0.3s ease-in-out`, `0.3s`, `background-color 0.3s linear, transition 0.3s linear, opacity 0.3s linear`, `opacity var(--anim-nav) ease`, `all var(--anim-nav) ease`, `opacity 0.7s ease-in-out`, `0.1s ease-in-out`, `0.3s ease-in-out`

- team: `opacity 0.2s ease-in-out`, `background-color 0.2s ease-in-out, color 0.2s ease-in-out, border-color 0.2s ease-in-out`, `color 0.3s ease-in-out, opacity 0.3s ease-in-out`, `0.3s`, `background-color 0.3s linear, transition 0.3s linear, opacity 0.3s linear`, `opacity var(--anim-nav) ease`, `all var(--anim-nav) ease`, `opacity 0.7s ease-in-out`, `0.1s ease-in-out`, `0.3s ease-in-out`

- value: `opacity 0.2s ease-in-out`, `background-color var(--t396-speedhover,0s) ease-in-out,color var(--t396-speedhover,0s) ease-in-out,border-color var(--t396-speedhover,0s) ease-in-out,box-shadow var(--t396-shadowshoverspeed,0.2s) ease-in-out`, `color var(--t396-speedhover,0s) ease-in-out`, `color 0.3s ease-in-out, opacity 0.3s ease-in-out`, `0.3s`, `background-color 0.3s linear, transition 0.3s linear, opacity 0.3s linear`, `opacity var(--anim-nav) ease`, `all var(--anim-nav) ease`, `opacity 0.7s ease-in-out`, `0.2s ease-in-out`, `0.1s ease-in-out`, `0.3s ease-in-out`
