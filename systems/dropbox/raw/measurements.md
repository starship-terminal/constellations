# Component measurements

Computed styles read from dropbox.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /plans, /business, /features, /sign and the signed-out /login and /register cards — with any consent layer hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky dwg-nav bar (dwg-theme--coconut, z 120): the Dropbox mark, the Products / Solutions flyout triggers, the Business / Pricing / Contact sales links, the Get app trigger and Sign up / Log in / Get started.

Page: home. Selector: `nav.dwg-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 16px 24px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 500, #1e1919 |
| Transition | none |
| Icon | 32 x 27, colour #0000ee |
| ::after | 1440px x 1px, absolute, bg #a69171 @ 0.2, radius 0px |
| Painted layers | nav.dwg-nav.dwg-nav--sticky 1440.0x72.0 bg #ffffff; nav::after.dwg-nav.dwg-nav--sticky 1440pxx1px bg #a69171 @ 0.2; div.dwg-nav__dropdown-background.dwg-box 1440.0x0.0 bg #ffffff; div.dwg-nav__content.dwg-box 1344.0x40.0 bg #ffffff; span.dwg-nav-logo-button__glyph.dwg-nav-logo-button__glyph--updated 32.0x40.0 bg #ffffff; a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Dropbox mark anchor in the nav.

Page: home. Selector: `nav a.dwg-nav-logo-button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 154.5 x 40 |
| Padding | 0px |
| Gap | 5.5px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Icon | 32 x 27, colour #0000ee |
| Painted layers | span.dwg-nav-logo-button__glyph.dwg-nav-logo-button__glyph--updated 32.0x40.0 bg #ffffff |
| Ancestor paint | 1 up div.dwg-nav__content.dwg-box bg #ffffff |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Products button that opens the mega-menu; toggled, never followed.

Page: home. Selector: `nav button Products`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.48 x 72 | = | = | = |
| Padding | 16px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px inset | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | #0061fe | = | #0061fe |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 500, #1e1919 | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 500, #0061fe | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 500, #0061fe |
| Transition | color 0.125s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #524a3e @ 0.82 | 16 x 16, colour #0061fe | = | 16 x 16, colour #0061fe |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 105.5x72.0 shadow #428bff 0px 0px 0px 3px inset | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The Pricing link in the nav; measured, never followed.

Page: home. Selector: `nav a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.48 x 72 | = | = | = |
| Padding | 16px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px inset | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | #0061fe | = | #0061fe |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 500, #1e1919 | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 500, #0061fe | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 500, #0061fe |
| Transition | color 0.125s linear | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 72.5x72.0 shadow #428bff 0px 0px 0px 3px inset | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-contact

Nav contact link. The Contact sales link in the nav; measured, never followed.

Page: home. Selector: `nav a Contact sales`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114.47 x 72 | = | = | = |
| Padding | 16px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px inset | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | #0061fe | = | #0061fe |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #1e1919 | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #0061fe | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #0061fe |
| Transition | color 0.125s linear | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 114.5x72.0 shadow #428bff 0px 0px 0px 3px inset | = |

Crops: `nav-contact-default.png`, `nav-contact-hover.png`, `nav-contact-focus-visible.png`, `nav-contact-pressed.png`.

#### nav-signup

Sign-up link. The header Sign up link; measured, never followed.

Page: home. Selector: `nav a Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75.83 x 72 | = | = | = |
| Padding | 16px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px inset | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | #0061fe | = | #0061fe |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #1e1919 | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #0061fe | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #0061fe |
| Transition | color 0.125s linear | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 75.8x72.0 shadow #428bff 0px 0px 0px 3px inset | = |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

#### nav-login

Log-in link. The header Log in link; measured, never followed.

Page: home. Selector: `nav a Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.42 x 72 | = | = | = |
| Padding | 16px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px inset | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | #0061fe | = | #0061fe |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #1e1919 | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #0061fe | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #0061fe |
| Transition | color 0.125s linear | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 65.4x72.0 shadow #428bff 0px 0px 0px 3px inset | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Get-started action. The header Get started action (the blue pill); measured, never followed.

Page: home. Selector: `nav a Get started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.13 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 2px solid #0061fe | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0061fe | #0057e5 | = | #0050d0 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #f7f5f2 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0057e5 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px shadow #428bff 0px 0px 0px 3px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0050d0 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Nav mega-menu. The Products mega-menu panel (Dropbox / Replay / Sign / Reclaim.ai / Dash / DocSend / Early access), opened by its own trigger.

Page: home. Selector: `opened Products panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 400 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/20px 500, #1e1919 |
| Transition | max-height, opacity 0.2s, 0.2s cubic-bezier(0.785, 0.135, 0.15, 0.86), cubic-bezier(0.785, 0.135, 0.15, 0.86) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 72) |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Mega-menu link. A product link inside the opened Products mega-menu (pointer-driven; the menu closes on keyboard focus).

Page: home. Selector: `flyout link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 240 x 92 | = |
| Padding | 16px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #a79272 @ 0.14 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Times 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1e1919 | #0061fe |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/20px 500, #1e1919 | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/20px 500, #0061fe |
| Transition | background-color, color 0.125s, 0.125s linear, linear delay 0s, 0s | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | a.dwg-dropdown-list-item.dwg-dropdown-list-item--link 240.0x92.0 bg #a79272 @ 0.14 r 12px |

Crops: `menu-link-default.png`, `menu-link-hover.png`.

### Home

#### hero-title

Hero headline. The "One place to store, share, and collaborate" display heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1072 x 143.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 66.24px/71.5392px 500 |
| Letter spacing | -0.9936px |
| Colour | #ffffff |
| Text node | span.cf-h1__line: Sharp Grotesk 66.24px/71.5392px 500, #ffffff, ls -0.9936px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the hero headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 513.22 x 90 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Atlas Grotesk Web 20px/30px 400 |
| Letter spacing | normal |
| Colour | #524a3e @ 0.82 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The "Try Dropbox free" primary action on the hero; measured, never followed.

Page: home. Selector: `hero primary CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 230.52 x 71.19 | = | = | = |
| Padding | 24px | = | = | = |
| Gap | 24px | = | = | = |
| Border | 2px solid #ffffff | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | #ffffff @ 0.12 | = | #ffffff @ 0.12 |
| Box shadow | none | = | #428bff 0px 0px 0px 9px | = |
| Outline | none | = | 3px solid #ffffff offset 3px | = |
| Font | Atlas Grotesk Web 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Atlas Grotesk Web 16px/19.2px 500, #ffffff | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) delay 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| Painted layers | a.cf-cta.cf-rise 230.5x71.2 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px | a.cf-cta.cf-rise 230.5x71.2 bg #ffffff @ 0.12 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px | a.cf-cta.cf-rise 230.5x71.2 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px shadow #428bff 0px 0px 0px 9px outline 3px solid #ffffff offset 3px | a.cf-cta.cf-rise 230.5x71.2 bg #ffffff @ 0.12 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### transparent-btn

Transparent button. A dwg-button2 transparent-variant action (See all integrations / Connect now / Learn more); measured, never followed.

Page: home. Selector: `a.dwg-button2--button-style-transparent`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 179.5 x 19.2 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #428bff offset 3px | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #f7f5f2 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #f7f5f2 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-button2.dwg-button2--button-style-transparent 179.5x19.2 outline 3px solid #428bff offset 3px | = |

Crops: `transparent-btn-default.png`, `transparent-btn-hover.png`, `transparent-btn-focus-visible.png`, `transparent-btn-pressed.png`.

#### text-link

Text link. A dwg-text-link inline link (the AI-integration names); measured, never followed.

Page: home. Selector: `a.dwg-text-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.94 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #428bff offset 3px | = |
| Font | Atlas Grotesk Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-text.dwg-font-family--atlas-grotesk 68.9x20.0 outline 3px solid #428bff offset 3px | = |

Crops: `text-link-default.png`, `text-link-hover.png`, `text-link-focus-visible.png`, `text-link-pressed.png`.

#### icon-button

Icon button. A dwg-icon-button glyph action on the page (a carousel arrow).

Page: home. Selector: `button.dwg-icon-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 32 x 32, colour #1e1919 | = | = | = |
| ::before | 1px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | 32px x 32px, absolute, bg #000000 @ 0.08, radius 0px | = | 32px x 32px, absolute, bg #000000 @ 0.08, radius 0px |
| Painted layers | - | button::after.dwg-icon-button.dwg-icon-button--hoverActiveFilter 32pxx32px bg #000000 @ 0.08 | button.dwg-icon-button.dwg-icon-button--hoverActiveFilter 32.0x32.0 shadow #428bff 0px 0px 0px 3px | button::after.dwg-icon-button.dwg-icon-button--hoverActiveFilter 32pxx32px bg #000000 @ 0.08 |

Crops: `icon-button-default.png`, `icon-button-hover.png`, `icon-button-focus-visible.png`, `icon-button-pressed.png`.

#### section-h2

Section heading. A section heading below the hero.

Page: home. Selector: `section h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 886.14 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Atlas Grotesk Web 20px/24px 500 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### graphite-band

Graphite band. A dark dwg-theme--graphite section painted inside the light page.

Page: home. Selector: `.dwg-theme--graphite section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 2988 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f7f5f2 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #f7f5f2 |
| Text node | p.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #f7f5f2 |
| Transition | none |
| Icon | 24 x 24, colour #f7f5f2 |
| Painted layers | section.dwg-theme--graphite 1440.0x2988.0 bg #f7f5f2; div.cf-ai__panel-bg 1440.0x748.0 bg #1e1919; article.cf-ai__card 484.3x395.5 bg #242121 r 12px; a.dwg-button2.dwg-button2--button-style-transparent 185.4x55.7 bg #3080ff border T:2px solid #3080ff / R:2px solid #3080ff / B:2px solid #3080ff / L:2px solid #3080ff r 16px; article.cf-ai__card 470.9x384.6 bg #242121 r 12px; a.dwg-button2.dwg-button2--button-style-transparent 180.3x54.2 bg #3080ff border T:2px solid #3080ff / R:2px solid #3080ff / B:2px solid #3080ff / L:2px solid #3080ff r 16px |
| How | at rest |

Crops: `graphite-band-default.png`.

#### coconut-band

Coconut band. A cream dwg-theme--coconut section.

Page: home. Selector: `.dwg-theme--coconut section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 120 |
| Padding | 0px 0px 72px 0px |
| Border | none |
| Radius | 0px |
| Background | #f7f5f2 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.dwg-text.dwg-font-family--inherit: Atlas Grotesk Web 16px/24px 400, #1e1919 |
| Transition | none |
| ::before | 1440px x 48px, absolute, bg #f7f5f2, radius 0px |
| ::after | 1440px x 72px, absolute, bg #f7f5f2, radius 0px |
| Painted layers | div.dwg-rich-text-plank.dwg-plank-frame 1440.0x120.0 bg #f7f5f2; div::before.dwg-rich-text-plank.dwg-plank-frame 1440pxx48px bg #f7f5f2; div::after.dwg-rich-text-plank.dwg-plank-frame 1440pxx72px bg #f7f5f2 |
| How | at rest |

Crops: `coconut-band-default.png`.

### Plans and pricing

#### plans-title

Plans title. The plans-page heading (the markup carries no h1; the first heading element is read).

Page: plans. Selector: `first h1/h2 on /plans`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 827.06 x 38.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 32px/38.4px 400 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Transition | none |
| How | at rest |

Crops: `plans-title-default.png`.

#### billing-radio

Billing radio. A Monthly/Yearly billing-period radio label (the input is a real radio — dwg-input-radio__input); the Yearly side was toggled for the screenshot, never checked out.

Page: plans. Selector: `billing radio label`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.11 x 24 | = | - | = |
| Padding | 0px 0px 0px 28px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Atlas Grotesk Web 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1e1919 | = | - | = |
| Transition | none | = | - | = |
| Cursor | default | = | - | = |
| Painted layers | input::before.dwg-input-radio__input 20pxx20px border T:1px solid #1e1919 / R:1px solid #1e1919 / B:1px solid #1e1919 / L:1px solid #1e1919 r 50% | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `billing-radio-default.png`, `billing-radio-hover.png`, `billing-radio-pressed.png`.

#### plan-card

Plan card. A pricing plan card (plan name, price and its action).

Page: plans. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 416 x 1079.41 |
| Padding | 24px 48px 48px 48px |
| Border | none |
| Radius | 12px |
| Background | #faf9f7 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Text node | h3.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/16.8px 400, #524a3e @ 0.82 |
| Transition | none |
| Icon | 24 x 24, colour #f7f5f2 |
| Painted layers | div._dwg-plan-card-v2__section_1cptg_35.dwg-box 416.0x1079.4 bg #faf9f7 r 12px; button.dwg-button2.dwg-button2--button-style-primary 320.0x55.2 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px; span.dwg-text.dwg-font-family--atlas-grotesk 101.8x18.0 border B:1px dashed #1e1919; span.dwg-text.dwg-font-family--atlas-grotesk 171.2x18.0 border B:1px dashed #1e1919; span.dwg-text.dwg-font-family--atlas-grotesk 203.5x18.0 border B:1px dashed #1e1919; span._dwg-plan-card-v2__feature-inline-logo_1cptg_163 0.0x0.0 bg #ffffff border T:1px solid #000000 @ 0.14 / R:1px solid #000000 @ 0.14 / B:1px solid #000000 @ 0.14 / L:1px solid #000000 @ 0.14 r 50% |
| Ancestor paint | 1 up div._dwg-plan-card-v2_1cptg_1.dwg-box bg #ffffff |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-name

Plan name. A plan card's plan name.

Page: plans. Selector: `plan name text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 61.92 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Atlas Grotesk Web 14px/20px 500 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. A plan card's price figure (US$ in the region the capture was served).

Page: plans. Selector: `plan $ figure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 142.23 x 25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Atlas Grotesk Web 20px/24px 500 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's primary action (Try for free / Buy now); measured, never followed.

Page: plans. Selector: `plan card primary CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 55.2 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 2px solid #0061fe | = | = | = |
| Radius | 16px | = | = | = |
| Background | #0061fe | #0057e5 | = | #0050d0 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #f7f5f2 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #f7f5f2 | = | = | = |
| Painted layers | button.dwg-button2.dwg-button2--button-style-primary 320.0x55.2 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px | button.dwg-button2.dwg-button2--button-style-primary 320.0x55.2 bg #0057e5 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px | button.dwg-button2.dwg-button2--button-style-primary 320.0x55.2 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px shadow #428bff 0px 0px 0px 3px | button.dwg-button2.dwg-button2--button-style-primary 320.0x55.2 bg #0050d0 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-cta-alt

Plan secondary CTA. The "or buy now" transparent action under a plan CTA; measured, never followed.

Page: plans. Selector: `plan transparent CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114.2 x 19.2 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #1e1919 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1e1919 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.dwg-button2.dwg-button2--button-style-transparent 114.2x19.2 shadow #428bff 0px 0px 0px 3px | = |

Crops: `plan-cta-alt-default.png`, `plan-cta-alt-hover.png`, `plan-cta-alt-focus-visible.png`, `plan-cta-alt-pressed.png`.

#### plan-outline

Outline button. A dwg-button2 outline-variant action (Get Basic / Contact us); measured, never followed.

Page: plans. Selector: `dwg-button2--button-style-outline`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.48 x 39.2 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | 2px solid #1e1919 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #000000 @ 0.08 | = | #000000 @ 0.08 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #1e1919 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dwg-button2.dwg-button2--button-style-outline 127.5x39.2 border T:2px solid #1e1919 / R:2px solid #1e1919 / B:2px solid #1e1919 / L:2px solid #1e1919 r 12px | a.dwg-button2.dwg-button2--button-style-outline 127.5x39.2 bg #000000 @ 0.08 border T:2px solid #1e1919 / R:2px solid #1e1919 / B:2px solid #1e1919 / L:2px solid #1e1919 r 12px | a.dwg-button2.dwg-button2--button-style-outline 127.5x39.2 border T:2px solid #1e1919 / R:2px solid #1e1919 / B:2px solid #1e1919 / L:2px solid #1e1919 r 12px shadow #428bff 0px 0px 0px 3px | a.dwg-button2.dwg-button2--button-style-outline 127.5x39.2 bg #000000 @ 0.08 border T:2px solid #1e1919 / R:2px solid #1e1919 / B:2px solid #1e1919 / L:2px solid #1e1919 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-outline-default.png`, `plan-outline-hover.png`, `plan-outline-focus-visible.png`, `plan-outline-pressed.png`.

#### diff-toggle

Difference toggle. The "Show only differences" comparison-table toggle; measured, never toggled.

Page: plans. Selector: `cf-diff-toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 223.53 x 32 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0061fe offset 4px | = |
| Font | Atlas Grotesk Web 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.cf-diff-toggle__label: Atlas Grotesk Web 16px/24px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.cf-diff-toggle__track 44.0x24.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 12px; span.cf-diff-toggle__knob 16.0x16.0 bg #000000 r 50% | = | button.cf-diff-toggle 223.5x32.0 r 4px outline 2px solid #0061fe offset 4px; span.cf-diff-toggle__track 44.0x24.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 12px; span.cf-diff-toggle__knob 16.0x16.0 bg #000000 r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `diff-toggle-default.png`, `diff-toggle-hover.png`, `diff-toggle-focus-visible.png`, `diff-toggle-pressed.png`.

#### help-choose

Help-me-choose. The "? Help me choose" assistant trigger; measured, never pressed.

Page: plans. Selector: `cf-help-choose-trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 168.94 x 38 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #1e1919 @ 0.65 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff @ 0.9 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0061fe offset 2px | = |
| Font | Atlas Grotesk Web 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | = | = | = |
| Text node | span: Atlas Grotesk Web 12px/12px 700, #1e1919 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cf-help-choose-trigger.cf:inline-flex 168.9x38.0 bg #ffffff @ 0.9 border T:1px solid #1e1919 @ 0.65 / R:1px solid #1e1919 @ 0.65 / B:1px solid #1e1919 @ 0.65 / L:1px solid #1e1919 @ 0.65 r 3.35544e+07px; span 21.0x21.0 bg #b4dc19 r 9999px | = | button.cf-help-choose-trigger.cf:inline-flex 168.9x38.0 bg #ffffff @ 0.9 border T:1px solid #1e1919 @ 0.65 / R:1px solid #1e1919 @ 0.65 / B:1px solid #1e1919 @ 0.65 / L:1px solid #1e1919 @ 0.65 r 3.35544e+07px outline 2px solid #0061fe offset 2px; span 21.0x21.0 bg #b4dc19 r 9999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-choose-default.png`, `help-choose-hover.png`, `help-choose-focus-visible.png`, `help-choose-pressed.png`.

### Features and products

#### biz-title

Business headline. The /business display heading ("Everything your business needs to work efficiently, all in one place").

Page: business. Selector: `h1 on /business`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 240 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 40px/48px 400 |
| Letter spacing | normal |
| Colour | #f7f5f2 |
| Transition | none |
| How | at rest |

Crops: `biz-title-default.png`.

#### biz-cta

Business CTA. A primary dwg-button2 action on /business; measured, never followed.

Page: business. Selector: `dwg-button2--button-style-primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.13 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 2px solid #0061fe | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0061fe | #0057e5 | = | #0050d0 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #f7f5f2 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0057e5 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px shadow #428bff 0px 0px 0px 3px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0050d0 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `biz-cta-default.png`, `biz-cta-hover.png`, `biz-cta-focus-visible.png`, `biz-cta-pressed.png`.

#### navy-band

Navy band. A dwg-theme--navy coloured section.

Page: business. Selector: `.dwg-theme--navy section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 720 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #283750 |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.dwg-text.dwg-font-family--sharp-grotesk-20-book: Sharp Grotesk 24px/28.8px 400, #f7f5f2 |
| Transition | none |
| Icon | 24 x 24, colour #f7f5f2 |
| ::before | 1440px x 0px, absolute, bg #283750, radius 0px |
| ::after | 1440px x 0px, absolute, bg #283750, radius 0px |
| Painted layers | div.dwg-media-text-plank.dwg-media-text-plank--stackable--navy 1440.0x720.0 bg #283750; div::before.dwg-media-text-plank.dwg-media-text-plank--stackable--navy 1440pxx0px bg #283750; div::after.dwg-media-text-plank.dwg-media-text-plank--stackable--navy 1440pxx0px bg #283750; div.dwg-box.dwg-display--flex 443.1x720.0 bg #283750; a.dwg-button2.dwg-button2--button-style-outline 210.0x71.2 border T:2px solid #f7f5f2 / R:2px solid #f7f5f2 / B:2px solid #f7f5f2 / L:2px solid #f7f5f2 r 16px; div.dwg-media-frame.dwg-box 886.1x720.0 bg #d8d3cb |
| How | at rest |

Crops: `navy-band-default.png`.

#### feat-title

Features headline. The /features display heading ("What is Dropbox?").

Page: features. Selector: `h1 on /features`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 40px/48px 400 |
| Letter spacing | normal |
| Colour | #f7f5f2 |
| Transition | none |
| How | at rest |

Crops: `feat-title-default.png`.

#### feat-card

Feature card. A dwg-card / dwg-nav-card feature tile on /features; the link was measured, never followed.

Page: features. Selector: `dwg-card/dwg-nav-card tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 413.53 x 517.55 | = | - | = |
| Padding | 0px 24px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Times 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | h3.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 20px/24px 500, #1e1919 | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.dwg-media-frame.dwg-box 365.5x365.5 bg #eee9e2 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `feat-card-default.png`, `feat-card-hover.png`, `feat-card-pressed.png`.

#### sign-title

Sign headline. The /sign product-page heading ("Sign paperwork without all the paperwork").

Page: sign. Selector: `h1 on /sign`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 40px/48px 400 |
| Letter spacing | normal |
| Colour | #f7f5f2 |
| Transition | none |
| How | at rest |

Crops: `sign-title-default.png`.

#### sign-cta

Sign CTA. A primary dwg-button2 action on /sign; measured, never followed.

Page: sign. Selector: `dwg-button2--button-style-primary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.13 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 2px solid #0061fe | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0061fe | #0057e5 | = | #0050d0 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #f7f5f2 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0057e5 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px shadow #428bff 0px 0px 0px 3px | a.dwg-button2.dwg-button2--button-style-primary 117.1x40.0 bg #0050d0 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sign-cta-default.png`, `sign-cta-hover.png`, `sign-cta-focus-visible.png`, `sign-cta-pressed.png`.

### Login and signup

#### auth-card

Auth card. The log-in card (Continue with Apple / Google / Microsoft + the email field and terms); captured, never used.

Page: login. Selector: `auth card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 368 x 272.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Atlas Grotesk Web 13px/normal 400 |
| Letter spacing | normal |
| Colour | #050505 |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/16px 400, #1e1919 |
| Transition | none |
| Icon | 0 x 0, colour #3c4043, fill #000000 |
| Painted layers | div.nsm7Bb-HzV7m-LgbsSe.TzA9Ye-LgbsSe 0.0x0.0 bg #ffffff border T:1px solid #dadce0 / R:1px solid #dadce0 / B:1px solid #dadce0 / L:1px solid #dadce0 r 4px; button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #ffffff border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px; button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #ffffff border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px; div::before._hr-label_s08ka_4 184pxx1px bg #a69e92 @ 0.3; div::after._hr-label_s08ka_4 184pxx1px bg #a69e92 @ 0.3; input._field-input_1osti_50._field-input-ltr_1osti_105 368.0x48.0 bg #ffffff border T:1px solid #b0b4ba / R:1px solid #b0b4ba / B:1px solid #b0b4ba / L:1px solid #b0b4ba |
| How | at rest |

Crops: `auth-card-default.png`.

#### sso-button

SSO button. The "Continue with Apple" SSO action; measured, never pressed — it would leave for the provider flow.

Page: login. Selector: `Continue with Apple`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #cac5be | = | = | 1px solid #a69e92 @ 0.6 |
| Radius | 4px | = | = | = |
| Background | #ffffff | #000000 @ 0.08 | = | #000000 @ 0.08 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | lucida grande 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | = | = | #524a3e @ 0.82 |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/16px 400, #1e1919 | = | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/16px 400, #524a3e @ 0.82 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 32 x 32, colour #000000 | = | = | 32 x 32, colour #524a3e @ 0.82 |
| Painted layers | button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #ffffff border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px | button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #000000 @ 0.08 border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px | button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #ffffff border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px shadow #428bff 0px 0px 0px 3px | button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #000000 @ 0.08 border T:1px solid #a69e92 @ 0.6 / R:1px solid #a69e92 @ 0.6 / B:1px solid #a69e92 @ 0.6 / L:1px solid #a69e92 @ 0.6 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-button-default.png`, `sso-button-hover.png`, `sso-button-focus-visible.png`, `sso-button-pressed.png`.

#### sso-button-alt

SSO button (alt). A second SSO action (Google or Microsoft); measured, never pressed.

Page: login. Selector: `Continue with Google/Microsoft`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #cac5be | = | = | 1px solid #a69e92 @ 0.6 |
| Radius | 4px | = | = | = |
| Background | #ffffff | #000000 @ 0.08 | = | #000000 @ 0.08 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | lucida grande 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | = | = | #524a3e @ 0.82 |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/16px 400, #1e1919 | = | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/16px 400, #524a3e @ 0.82 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #ffffff border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px | button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #000000 @ 0.08 border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px | button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #ffffff border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px shadow #428bff 0px 0px 0px 3px | button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #000000 @ 0.08 border T:1px solid #a69e92 @ 0.6 / R:1px solid #a69e92 @ 0.6 / B:1px solid #a69e92 @ 0.6 / L:1px solid #a69e92 @ 0.6 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-button-alt-default.png`, `sso-button-alt-hover.png`, `sso-button-alt-focus-visible.png`, `sso-button-alt-pressed.png`.

#### email-field

Email field. The email input on the auth card; focused and given sample text that was deleted again — nothing sent.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 368 x 48 | = | = |
| Padding | 16px | = | = |
| Border | 1px solid #b0b4ba | 1px solid #050505 | 1px solid #050505 |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #428bff 0px 0px 0px 3px | #428bff 0px 0px 0px 3px |
| Outline | none | = | = |
| Font | lucida grande 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #65696e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #65696e, opacity 1 | = | = |
| Painted layers | input._field-input_1osti_50._field-input-ltr_1osti_105 368.0x48.0 bg #ffffff border T:1px solid #b0b4ba / R:1px solid #b0b4ba / B:1px solid #b0b4ba / L:1px solid #b0b4ba | input._field-input_1osti_50._field-input-ltr_1osti_105 368.0x48.0 bg #ffffff border T:1px solid #050505 / R:1px solid #050505 / B:1px solid #050505 / L:1px solid #050505 shadow #428bff 0px 0px 0px 3px | input._field-input_1osti_50._field-input-ltr_1osti_105 368.0x48.0 bg #ffffff border T:1px solid #050505 / R:1px solid #050505 / B:1px solid #050505 / L:1px solid #050505 shadow #428bff 0px 0px 0px 3px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### continue-button

Continue button. The auth card's Continue action; measured, never pressed.

Page: login. Selector: `form Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 55.2 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 2px solid #0061fe | = | = | = |
| Radius | 16px | = | = | = |
| Background | #0061fe | #0057e5 | = | #0050d0 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | lucida grande 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #f7f5f2 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.email-submit-button.dwg-button2 368.0x55.2 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px | button.email-submit-button.dwg-button2 368.0x55.2 bg #0057e5 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px | button.email-submit-button.dwg-button2 368.0x55.2 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px shadow #428bff 0px 0px 0px 3px | button.email-submit-button.dwg-button2 368.0x55.2 bg #0050d0 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `continue-button-default.png`, `continue-button-hover.png`, `continue-button-focus-visible.png`, `continue-button-pressed.png`.

#### register-card

Register card. The "Get started with Dropbox" sign-up card; captured, never used.

Page: register. Selector: `register card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 368 x 272.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Atlas Grotesk Web 13px/normal 400 |
| Letter spacing | normal |
| Colour | #050505 |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/16px 400, #1e1919 |
| Transition | none |
| Icon | 0 x 0, colour #3c4043, fill #000000 |
| Painted layers | div.nsm7Bb-HzV7m-LgbsSe.TzA9Ye-LgbsSe 0.0x0.0 bg #ffffff border T:1px solid #dadce0 / R:1px solid #dadce0 / B:1px solid #dadce0 / L:1px solid #dadce0 r 4px; button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #ffffff border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px; button.dwg-sso-button.dwg-sso-button-v2 368.0x40.0 bg #ffffff border T:1px solid #cac5be / R:1px solid #cac5be / B:1px solid #cac5be / L:1px solid #cac5be r 4px; div::before._hr-label_s08ka_4 184pxx1px bg #a69e92 @ 0.3; div::after._hr-label_s08ka_4 184pxx1px bg #a69e92 @ 0.3; input._field-input_1osti_50._field-input-ltr_1osti_105 368.0x48.0 bg #ffffff border T:1px solid #b0b4ba / R:1px solid #b0b4ba / B:1px solid #b0b4ba / L:1px solid #b0b4ba |
| How | at rest |

Crops: `register-card-default.png`.

#### register-email

Register email field. The name@company.com email input on the sign-up card; focused and given sample text that was deleted again — nothing sent.

Page: register. Selector: `input[name=susi_email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 368 x 48 | = | = |
| Padding | 16px | = | = |
| Border | 1px solid #b0b4ba | 1px solid #050505 | 1px solid #050505 |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #428bff 0px 0px 0px 3px | #428bff 0px 0px 0px 3px |
| Outline | none | = | = |
| Font | lucida grande 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #65696e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #65696e, opacity 1 | = | = |
| Painted layers | input._field-input_1osti_50._field-input-ltr_1osti_105 368.0x48.0 bg #ffffff border T:1px solid #b0b4ba / R:1px solid #b0b4ba / B:1px solid #b0b4ba / L:1px solid #b0b4ba | input._field-input_1osti_50._field-input-ltr_1osti_105 368.0x48.0 bg #ffffff border T:1px solid #050505 / R:1px solid #050505 / B:1px solid #050505 / L:1px solid #050505 shadow #428bff 0px 0px 0px 3px | input._field-input_1osti_50._field-input-ltr_1osti_105 368.0x48.0 bg #ffffff border T:1px solid #050505 / R:1px solid #050505 / B:1px solid #050505 / L:1px solid #050505 shadow #428bff 0px 0px 0px 3px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `register-email-default.png`, `register-email-focused.png`, `register-email-filled.png`.

#### register-cta

Register CTA. The sign-up card's Continue action; measured, never pressed.

Page: register. Selector: `register Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 55.2 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | 2px solid #0061fe | = | = | = |
| Radius | 16px | = | = | = |
| Background | #0061fe | #0057e5 | = | #0050d0 |
| Box shadow | none | = | #428bff 0px 0px 0px 3px | = |
| Outline | none | = | = | = |
| Font | lucida grande 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 16px/19.2px 500, #f7f5f2 | = | = | = |
| Transition | background-color, border-color 0.1s, 0.1s cubic-bezier(0.4, 0, 0.6, 1), cubic-bezier(0.4, 0, 0.6, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.email-submit-button.dwg-button2 368.0x55.2 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px | button.email-submit-button.dwg-button2 368.0x55.2 bg #0057e5 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px | button.email-submit-button.dwg-button2 368.0x55.2 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px shadow #428bff 0px 0px 0px 3px | button.email-submit-button.dwg-button2 368.0x55.2 bg #0050d0 border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `register-cta-default.png`, `register-cta-hover.png`, `register-cta-focus-visible.png`, `register-cta-pressed.png`.

### Footer

#### footer

Footer. The footer: the product/company link columns, app links, the language and legal links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 619.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 20px/30px 500, #f7f5f2 |
| Transition | none |
| Icon | 32 x 32, colour #f7f5f2 |
| Painted layers | div.dwg-footer-plank.dwg-plank-frame 1440.0x478.0 bg #000000; div::before.dwg-footer-plank.dwg-plank-frame 1440pxx96px bg #000000; div::after.dwg-footer-plank.dwg-plank-frame 1440pxx0px bg #000000; div.warp-dwg-locale-selector-plank.dwg-plank-frame 1440.0x141.2 bg #000000; div::before.warp-dwg-locale-selector-plank.dwg-plank-frame 1440pxx0px bg #000000; div::after.warp-dwg-locale-selector-plank.dwg-plank-frame 1440pxx0px bg #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.66 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Atlas Grotesk Web 14px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-text.dwg-font-family--atlas-grotesk 83.7x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.03 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Atlas Grotesk Web 14px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f7f5f2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-text.dwg-font-family--atlas-grotesk 91.0x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `nav at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #1e1919 |
| Transition | none |
| Icon | 32 x 27, colour #0000ee |
| ::after | 390px x 1px, absolute, bg #a69171 @ 0.2, radius 0px |
| Painted layers | nav.dwg-nav.dwg-nav--sticky 390.0x48.0 bg #ffffff; nav::after.dwg-nav.dwg-nav--sticky 390pxx1px bg #a69171 @ 0.2; div.dwg-nav__dropdown-background.dwg-box 390.0x0.0 bg #ffffff; div.dwg-nav__content.dwg-box 390.0x48.0 bg #ffffff; span.dwg-nav-logo-button__glyph.dwg-nav-logo-button__glyph--updated 32.0x48.0 bg #ffffff; div.dwg-nav-dropdown.dwg-nav-dropdown--2-col 0.0x0.0 bg #faf9f7 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger toggle in the mobile nav.

Page: mobile. Selector: `dwg-nav hamburger button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 1px 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Transition | none |
| Cursor | pointer |
| Icon | 32 x 32, colour #1e1919 |
| Ancestor paint | 1 up div.dwg-nav__content.dwg-box bg #ffffff |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The opened mobile navigation panel (the overlay holding the menu items and the auth actions).

Page: mobile. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 708 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 24px/28.8px 500, #1e1919 |
| Transition | none |
| Icon | 24 x 24, colour #524a3e @ 0.82 |
| Painted layers | div.dwg-nav-mobile-dropdown__backdrop.dwg-box 390.0x844.0 bg #ffffff; div.dwg-nav-dropdown.dwg-nav-dropdown--2-col 390.0x624.0 bg #faf9f7; div.dwg-nav-dropdown.dwg-nav-dropdown--3-col 390.0x1098.0 bg #faf9f7; div.dwg-nav-dropdown.dwg-nav-dropdown--1-col 390.0x164.0 bg #faf9f7; div.dwg-nav-mobile-dropdown__cta-container.dwg-nav-mobile-dropdown--nav-redesign__cta-container 390.0x88.0 bg #ffffff; a.dwg-button2.dwg-button2--button-style-primary 358.0x55.2 bg #0061fe border T:2px solid #0061fe / R:2px solid #0061fe / B:2px solid #0061fe / L:2px solid #0061fe r 16px |
| Ancestor paint | 1 up nav.dwg-nav.dwg-nav--sticky bg #ffffff |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A row inside the opened mobile menu (Products / Solutions / Business / Pricing / Get app).

Page: mobile. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 382 x 76.8 | = | = | = |
| Padding | 24px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px inset | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | #0061fe | = | #0061fe |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 24px/28.8px 500, #1e1919 | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 24px/28.8px 500, #0061fe | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 24px/28.8px 500, #0061fe |
| Transition | color 0.125s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #524a3e @ 0.82 | 24 x 24, colour #0061fe | = | 24 x 24, colour #0061fe |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 382.0x76.8 shadow #428bff 0px 0px 0px 3px inset | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-signup

Mobile sign-up. The Sign up action in the mobile top bar, visible above the opened menu; measured, never followed.

Page: mobile. Selector: `mobile Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.83 x 48 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #428bff 0px 0px 0px 3px inset | = |
| Outline | none | = | = | = |
| Font | Times 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1919 | #0061fe | = | #0061fe |
| Text node | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #1e1919 | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #0061fe | = | span.dwg-text.dwg-font-family--atlas-grotesk: Atlas Grotesk Web 14px/20px 400, #0061fe |
| Transition | color 0.125s linear | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.dwg-nav-item-button.dwg-nav-item-button--nav-redesign 67.8x48.0 shadow #428bff 0px 0px 0px 3px inset | = |

Crops: `m-signup-default.png`, `m-signup-hover.png`, `m-signup-focus-visible.png`, `m-signup-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 115.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sharp Grotesk 32px/38.4px 500 |
| Letter spacing | normal |
| Colour | #1e1919 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

dropbox.com serves its warp and dwg-component bundles cross-origin from cfl.dropboxstatic.com, so the readable CSSOM holds only the inline styles; this list covers the transition rules the page itself exposes, and the per-state Transition rows above are the computed values the page paints.

- business: `var(--dwg-accordion-item__dropdown-animation--ease-in-out)`, `max-height var(--dwg-accordion-item__dropdown-animation--ease-in-out),opacity var(--dwg-accordion-item__dropdown-animation--ease-out)`, `visibility var(--dwg-accordion-item__dropdown-animation--ease-in-out)`, `var(--dwg-nav__fade-animation),color var(--dwg-nav__desktop-dropdown-animation)`, `var(--dwg-nav__fade-animation)`, `var(--dwg-plank-frame-pseudo-transition,none)`, `opacity var(--dwg-accordion-item__dropdown-animation--ease-out)`, `transform linear 0.3s`, `transform 0.3s ease-out`, `all .5s calc(.15s + var(--dwg-iteration-index, 0)*50ms) ease-in-out`, `none`, `background-color 0.2s`

- home: `var(--dwg-accordion-item__dropdown-animation--ease-in-out)`, `max-height var(--dwg-accordion-item__dropdown-animation--ease-in-out),opacity var(--dwg-accordion-item__dropdown-animation--ease-out)`, `visibility var(--dwg-accordion-item__dropdown-animation--ease-in-out)`, `var(--dwg-nav__fade-animation),color var(--dwg-nav__desktop-dropdown-animation)`, `var(--dwg-nav__fade-animation)`, `var(--dwg-plank-frame-pseudo-transition,none)`, `opacity var(--dwg-accordion-item__dropdown-animation--ease-out)`, `transform linear 0.3s`, `transform 0.3s ease-out`, `all .5s calc(.15s + var(--dwg-iteration-index, 0)*50ms) ease-in-out`, `none`, `background-color 0.2s`

- login: `transform var(--dig-motion__duration__xxfast, 100ms) var(--dig-motion__easing__exit, cubic-bezier(0.5, 0, 1, 1))`, `opacity var(--dig-motion__duration__xxfast, 100ms) var(--dig-motion__easing__linear, cubic-bezier(0, 0, 1, 1)),transform var(--dig-motion__duration__fast, 300ms) var(--dig-motion__easing__exit, cubic-bezier(0.5, 0, 1, 1))`, `opacity var(--dig-motion__duration__xxfast, 100ms) var(--dig-motion__easing__linear, cubic-bezier(0, 0, 1, 1)),transform var(--dig-motion__duration__fast, 300ms) var(--dig-motion__easing__enter, cubic-bezier(0, 0, 0.4, 1))`, `opacity 250ms`, `color 0.2s linear`, `var(--dwg-accordion-item__dropdown-animation--ease-in-out)`, `max-height var(--dwg-accordion-item__dropdown-animation--ease-in-out),opacity var(--dwg-accordion-item__dropdown-animation--ease-out)`, `visibility var(--dwg-accordion-item__dropdown-animation--ease-in-out)`, `var(--dwg-nav__fade-animation),color var(--dwg-nav__desktop-dropdown-animation)`, `var(--dwg-nav__fade-animation)`, `var(--dwg-plank-frame-pseudo-transition,none)`, `opacity var(--dwg-accordion-item__dropdown-animation--ease-out)`

- plans: `var(--dwg-accordion-item__dropdown-animation--ease-in-out)`, `max-height var(--dwg-accordion-item__dropdown-animation--ease-in-out),opacity var(--dwg-accordion-item__dropdown-animation--ease-out)`, `visibility var(--dwg-accordion-item__dropdown-animation--ease-in-out)`, `var(--dwg-nav__fade-animation),color var(--dwg-nav__desktop-dropdown-animation)`, `var(--dwg-nav__fade-animation)`, `var(--dwg-plank-frame-pseudo-transition,none)`, `opacity var(--dwg-accordion-item__dropdown-animation--ease-out)`, `transform linear 0.3s`, `transform 0.3s ease-out`, `all .5s calc(.15s + var(--dwg-iteration-index, 0)*50ms) ease-in-out`, `none`, `background-color 0.2s`
