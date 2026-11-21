# Component measurements

Computed styles read from asana.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the light theme every captured route paints (the OneTrust consent banner was dismissed, never clicked or answered beyond dismissal), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The top nav: logo, Pricing link, Log in, Contact sales, Get started.

Page: home. Selector: `header/nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 16px/28px 400 |
| Letter spacing | normal |
| Colour | #646f79 |
| Text node | button.styles_nav-group-left__dropdown__Ororl: TWK Lausanne 14px/36px 500, #0d0d0d |
| Transition | none |
| Cursor | default |
| Icon | 112 x 22, colour #0d0e10 |
| Painted layers | nav.styles_main-navigation__U3pgX 1440.0x68.0 bg #ffffff; svg.styles_icon__VHmtA 28.0x28.0 border T:4px solid #000000 @ 0 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0; div.css-1sa3o1x-p3.e1huxitw1 209.9x55.0 bg #ffffff r 6px shadow #000000 @ 0.15 0px 2px 8px 0px; div::after.css-1sa3o1x-p3.e1huxitw1 10pxx10px border T:5px solid #000000 @ 0 / R:5px solid #000000 @ 0 / B:5px solid #ffffff / L:5px solid #000000 @ 0; a.styles_button-cta__K_nHI.styles_button-cta--secondary__MoBjP 120.4x44.0 bg #ffffff r 100px shadow #0d0d0d 0px 0px 0px 1px inset; a.styles_button-cta__K_nHI.styles_hide-on-logged-in__71yBl 104.6x44.0 bg #0d0d0d r 100px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `a[class*=logo-link]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 136 x 44 |
| Padding | 0px 12px |
| Border | none |
| Radius | 100px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 16px/24px 500 |
| Letter spacing | normal |
| Colour | #0d0e10 |
| Transition | color, border 0.3s ease |
| Cursor | pointer |
| Icon | 112 x 22, colour #0d0e10 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A top-level nav link. Measured, never followed.

Page: home. Selector: `a:has-text("Pricing")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.81 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4786ff offset 2px | = |
| Font | TWK Lausanne 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | #6e6e6e | = | #6e6e6e |
| Transition | color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.styles_nav-group-left__link__LX4NT.show-desktop 68.8x44.0 r 100px outline 2px solid #4786ff offset 2px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in link. The Log in nav action. Measured, never followed.

Page: home. Selector: `a:has-text("Log in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 63.14 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4786ff offset 2px | = |
| Font | TWK Lausanne 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | #6e6e6e | #6e6e6e | #6e6e6e |
| Text node | span: TWK Lausanne 14px/21px 500, #0d0d0d | span: TWK Lausanne 14px/21px 500, #6e6e6e | span: TWK Lausanne 14px/21px 500, #6e6e6e | span: TWK Lausanne 14px/21px 500, #6e6e6e |
| Transition | none 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.styles_link-cta__ZVq_J.styles_hide-on-mobile__O4OKw 63.1x44.0 r 100px outline 2px solid #4786ff offset 2px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-sales

Contact sales button. The secondary CTA. Measured, never followed.

Page: home. Selector: `a:has-text("Contact sales")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.36 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff | #fafafa | = | #fafafa |
| Box shadow | #0d0d0d 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 2px solid #4786ff offset 2px | = |
| Font | TWK Lausanne 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | none 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.styles_button-cta__K_nHI.styles_button-cta--secondary__MoBjP 120.4x44.0 bg #ffffff r 100px shadow #0d0d0d 0px 0px 0px 1px inset | a.styles_button-cta__K_nHI.styles_button-cta--secondary__MoBjP 120.4x44.0 bg #fafafa r 100px shadow #0d0d0d 0px 0px 0px 1px inset | a.styles_button-cta__K_nHI.styles_button-cta--secondary__MoBjP 120.4x44.0 bg #ffffff r 100px shadow #0d0d0d 0px 0px 0px 1px inset outline 2px solid #4786ff offset 2px | a.styles_button-cta__K_nHI.styles_button-cta--secondary__MoBjP 120.4x44.0 bg #fafafa r 100px shadow #0d0d0d 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-sales-default.png`, `nav-sales-hover.png`, `nav-sales-focus-visible.png`, `nav-sales-pressed.png`.

#### nav-cta

Get started button. The primary CTA. Measured, never followed.

Page: home. Selector: `a:has-text("Get started")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104.56 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #0d0d0d | #6e6e6e | = | #6e6e6e |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4786ff offset 2px | = |
| Font | TWK Lausanne 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.styles_button-cta__K_nHI.styles_hide-on-logged-in__71yBl 104.6x44.0 bg #0d0d0d r 100px | a.styles_button-cta__K_nHI.styles_hide-on-logged-in__71yBl 104.6x44.0 bg #6e6e6e r 100px | a.styles_button-cta__K_nHI.styles_hide-on-logged-in__71yBl 104.6x44.0 bg #0d0d0d r 100px outline 2px solid #4786ff offset 2px | a.styles_button-cta__K_nHI.styles_hide-on-logged-in__71yBl 104.6x44.0 bg #6e6e6e r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### flyout-trigger

Flyout trigger. The nav item opening the product flyout.

Page: home. Selector: `nav flyout trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.91 x 44 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | TWK Lausanne 14px/36px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | #6e6e6e | = | #6e6e6e |
| Transition | none 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #0d0d0d | 10 x 10, colour #6e6e6e | = | 10 x 10, colour #6e6e6e |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.styles_nav-group-left__dropdown__Ororl 119.9x44.0 r 100px outline 1px auto #005fcc offset 0px | = |

Crops: `flyout-trigger-default.png`, `flyout-trigger-hover.png`, `flyout-trigger-focus-visible.png`, `flyout-trigger-pressed.png`.

#### flyout-open

Flyout, open. The nav after a hover opens the flyout; the crop is the opened panel.

Page: home. Selector: `nav flyout trigger`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 119.91 x 44 |
| Padding | 8px 24px |
| Gap | 4px |
| Border | none |
| Radius | 100px |
| Background | #f3f3f3 |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 14px/36px 500 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | none 0.3s ease |
| Cursor | pointer |
| Icon | 10 x 10, colour #0d0d0d, fill #6e6e6e |
| Painted layers | button.styles_nav-group-left__dropdown__Ororl.styles_nav-group-left__dropdown--selected__2I8Eo 119.9x44.0 bg #f3f3f3 r 100px |
| How | own toggle |

Crops: `flyout-open-opened.png`.

### Home

#### hero-title

Hero title.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 873.44 x 183.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 102px/91.8px 300 |
| Letter spacing | -2.55px |
| Colour | #0d0e10 |
| Transition | none |
| Cursor | default |
| Painted layers | span.css-109y0hf.ejkf9f22 589.6x113.0 image linear-gradient(90deg, #ff453e 0%, #f481f4 50%, #ff453e 100%) |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. A hero action. Measured, never followed.

Page: home. Selector: `hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 167.81 x 64 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | TWK Lausanne 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | color, border 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-9oncxd-link-3-link-2-link-1.e78bqlk1 167.8x64.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px | = | = | = |
| How | at rest | mouse hover | focus failed | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### caps-label

Caps label. A small-caps eyebrow label.

Page: home. Selector: `span[class*=caps]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 180.44 x 24.5 |
| Padding | 4px 8px |
| Gap | 4px |
| Border | none |
| Radius | 4px |
| Background | #f3f3f3 |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 11px/16.5px 500 |
| Letter spacing | 0.44px |
| Colour | #0d0d0d |
| Transition | none |
| Cursor | default |
| Painted layers | span.css-1hpazh9-caps-small.ej34ex42 180.4x24.5 bg #f3f3f3 r 4px |
| How | at rest |

Crops: `caps-label-default.png`.

#### section-title

Section heading.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 628 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 54px/54px 300 |
| Letter spacing | -1.08px |
| Colour | #0d0d0d |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `section-title-default.png`.

#### card

Card. A linked feature/customer card.

Page: home. Selector: `card link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 282.25 x 63.5 | = |
| Padding | 10px | = |
| Gap | 14px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | TWK Lausanne 16px/24px 500 | = |
| Letter spacing | normal | = |
| Colour | #0d0e10 | #cd4848 |
| Text node | span: TWK Lausanne 16px/24px 500, #0d0d0d | = |
| Transition | color, border 0.3s ease | = |
| Cursor | pointer | = |
| Icon | 10 x 10, colour #0d0d0d | = |
| How | at rest | mouse hover |

Crops: `card-default.png`, `card-hover.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 215.39 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 16px/24px 500 |
| Letter spacing | 0.64px |
| Colour | #0d0d0d |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-toggle

Billing toggle. The monthly/annual switch. Measured, never switched.

Page: pricing. Selector: `billing toggle`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62.31 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #f06a6a | = | #f06a6a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #24a651 offset 2px | = |
| Font | TWK Lausanne 16px/24px 500 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #6e6e6e | #0d0d0d | = | #0d0d0d |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.styles_billing-toggle__label__1mJ88 62.3x24.0 bg #f06a6a | button.styles_billing-toggle__label__1mJ88 62.3x24.0 outline 2px solid #24a651 offset 2px | button.styles_billing-toggle__label__1mJ88 62.3x24.0 bg #f06a6a |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-focus-visible.png`, `billing-toggle-pressed.png`.

#### plan-card

Plan card. A pricing plan column.

Page: pricing. Selector: `plan column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 298 x 974 |
| Padding | 32px |
| Border | 1px solid #cfcfcf |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 16px/28px 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | h3.css-1sy34zr.e13cy96x13: TWK Lausanne 36px/36px 400, #0d0d0d, ls -0.36px |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #0d0d0d, fill #22b455 |
| Painted layers | div.css-cs6pme.e13cy96x15 298.0x974.0 border T:1px solid #cfcfcf / R:1px solid #cfcfcf / B:1px solid #cfcfcf / L:1px solid #cfcfcf r 16px; a.css-9oncxd-link-3-link-2-link-1.e78bqlk1 232.0x58.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px; div.css-1lhktbk-p3.e1huxitw1 209.9x113.5 bg #3d3d3d r 6px shadow #000000 @ 0.15 0px 2px 8px 0px; div::after.css-1lhktbk-p3.e1huxitw1 10pxx10px border T:5px solid #3d3d3d / R:5px solid #000000 @ 0 / B:5px solid #000000 @ 0 / L:5px solid #000000 @ 0; div.css-1lhktbk-p3.e1huxitw1 209.9x113.5 bg #3d3d3d r 6px shadow #000000 @ 0.15 0px 2px 8px 0px; div::after.css-1lhktbk-p3.e1huxitw1 10pxx10px border T:5px solid #3d3d3d / R:5px solid #000000 @ 0 / B:5px solid #000000 @ 0 / L:5px solid #000000 @ 0 |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. The plan column's action. Measured, never followed.

Page: pricing. Selector: `plan column CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 232 x 58 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 100px | = | = | = |
| Background | #f3f3f3 | #e7e7e7 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | TWK Lausanne 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | color, border 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-9oncxd-link-3-link-2-link-1.e78bqlk1 232.0x58.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px | a.css-9oncxd-link-3-link-2-link-1.e78bqlk1 232.0x58.0 bg #e7e7e7 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px | a.css-9oncxd-link-3-link-2-link-1.e78bqlk1 232.0x58.0 bg #f3f3f3 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 100px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-question

FAQ question.

Page: pricing. Selector: `pricing FAQ accordion`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 738 x 92.8 | = | = | = |
| Padding | 32px 0px | = | = | = |
| Gap | 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4786ff offset 2px | = |
| Font | TWK Lausanne 24px/28.8px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | padding-bottom 0.8s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 26 x 13, colour #0d0d0d | = | = | = |
| Painted layers | span.rebrand-styles_chevronCircle__uYFfP 24.0x24.0 bg #f3f3f3 r 100% | = | button.rebrand-styles_accordionTrigger__hoff_ 738.0x92.8 outline 2px solid #4786ff offset 2px; span.rebrand-styles_chevronCircle__uYFfP 24.0x24.0 bg #f3f3f3 r 100% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-pressed.png`.

#### faq-open

FAQ, open. The row after its own toggle.

Page: pricing. Selector: `pricing FAQ accordion`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 738 x 76.8 |
| Padding | 32px 0px 16px 0px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 24px/28.8px 500 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | padding-bottom 0.8s ease |
| Cursor | pointer |
| Icon | 26 x 13, colour #0d0d0d |
| Painted layers | span.rebrand-styles_chevronCircle__uYFfP 24.0x24.0 bg #f3f3f3 r 100% |
| How | own toggle |

Crops: `faq-open-opened.png`.

### Create account gate

#### gate-title

Gate title.

Page: gate. Selector: `gate heading`. States: .

Not found on the page at capture time.

#### gate-field

Gate field. Focused only; nothing typed or sent.

Page: gate. Selector: `gate input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 251.33 x 50 | = |
| Padding | 0px 0px 0px 16px | = |
| Border | T: 1px solid #e0e6e8; R: none; B: 1px solid #e0e6e8; L: 1px solid #e0e6e8 | T: 1px solid #222b37; R: none; B: 1px solid #222b37; L: 1px solid #222b37 |
| Radius | 3px 0px 0px 3px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | TWK Lausanne 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #222b37 | = |
| Transition | border 0.15s ease | = |
| Cursor | text | = |
| Placeholder | #6e6e6e, opacity 1 | = |
| Painted layers | input.input.input--email 251.3x50.0 bg #ffffff border T:1px solid #e0e6e8 / B:1px solid #e0e6e8 / L:1px solid #e0e6e8 r 3px 0px 0px 3px | input.input.input--email 251.3x50.0 bg #ffffff border T:1px solid #222b37 / B:1px solid #222b37 / L:1px solid #222b37 r 3px 0px 0px 3px |
| How | at rest | clicked into the field |

Crops: `gate-field-default.png`, `gate-field-focused.png`.

#### gate-cta

Gate CTA. The form action. Measured, never pressed.

Page: gate. Selector: `gate CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173.67 x 50 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px 3px 3px 0px | = | = | = |
| Background | #0d0e10 | #f06a6a | = | #f06a6a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0d0d0d offset 2px | = |
| Font | TWK Lausanne 16px/50px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | #0d0e10 | = | #0d0e10 |
| Text node | span: TWK Lausanne 16px/50px 500, #ffffff, ls 0.5px | span: TWK Lausanne 16px/50px 500, #0d0e10, ls 0.5px | = | span: TWK Lausanne 16px/50px 500, #0d0e10, ls 0.5px |
| Transition | background-color, color 0.15s, 0.15s ease, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff, fill #000000 @ 0 | 20 x 20, colour #0d0e10, fill #000000 @ 0 | = | 20 x 20, colour #0d0e10, fill #000000 @ 0 |
| Painted layers | button.signupForm-submit.signupForm-submit-stacked-form-mobile 173.7x50.0 bg #0d0e10 r 0px 3px 3px 0px | button.signupForm-submit.signupForm-submit-stacked-form-mobile 173.7x50.0 bg #f06a6a r 0px 3px 3px 0px | button.signupForm-submit.signupForm-submit-stacked-form-mobile 173.7x50.0 bg #0d0e10 r 0px 3px 3px 0px outline 2px solid #0d0d0d offset 2px | button.signupForm-submit.signupForm-submit-stacked-form-mobile 173.7x50.0 bg #f06a6a r 0px 3px 3px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gate-cta-default.png`, `gate-cta-hover.png`, `gate-cta-focus-visible.png`, `gate-cta-pressed.png`.

#### gate-sso

SSO button. A single-sign-on option. Measured, never pressed.

Page: gate. Selector: `SSO button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 208.5 x 52 | = | = | = |
| Padding | 6px 10px 6px 4px | = | = | = |
| Border | 1px solid #cfcfcf | 1px solid #273240 | = | 1px solid #273240 |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | TWK Lausanne 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0e10 | #cd4848 | = | #cd4848 |
| Text node | span.gmail-button-text-continue.-white: TWK Lausanne 16px/24px 500, #0d0d0d | = | = | = |
| Transition | border-color 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.gmail-button-continue.exp-gmail-button-continue 208.5x52.0 bg #ffffff border T:1px solid #cfcfcf / R:1px solid #cfcfcf / B:1px solid #cfcfcf / L:1px solid #cfcfcf r 6px; div.google-sso-verification-button-background 40.0x40.0 bg #ffffff r 2px | a.gmail-button-continue.exp-gmail-button-continue 208.5x52.0 bg #ffffff border T:1px solid #273240 / R:1px solid #273240 / B:1px solid #273240 / L:1px solid #273240 r 6px; div.google-sso-verification-button-background 40.0x40.0 bg #ffffff r 2px | a.gmail-button-continue.exp-gmail-button-continue 208.5x52.0 bg #ffffff border T:1px solid #cfcfcf / R:1px solid #cfcfcf / B:1px solid #cfcfcf / L:1px solid #cfcfcf r 6px outline 1px auto #005fcc offset 0px; div.google-sso-verification-button-background 40.0x40.0 bg #ffffff r 2px | a.gmail-button-continue.exp-gmail-button-continue 208.5x52.0 bg #ffffff border T:1px solid #273240 / R:1px solid #273240 / B:1px solid #273240 / L:1px solid #273240 r 6px; div.google-sso-verification-button-background 40.0x40.0 bg #ffffff r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gate-sso-default.png`, `gate-sso-hover.png`, `gate-sso-focus-visible.png`, `gate-sso-pressed.png`.

### Contact sales

#### sales-title

Sales title.

Page: sales. Selector: `h1/h2/h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 408 x 402 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 30px/36px 400 |
| Letter spacing | normal |
| Colour | #0d0e10 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `sales-title-default.png`.

#### sales-field

Sales field. Focused only; nothing typed or sent.

Page: sales. Selector: `form input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 512 x 50 | = |
| Padding | 10px 32px 10px 16px | = |
| Border | 1px solid #cfcfcf | 2px solid #727272 |
| Radius | 2px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Helvetica 13px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #0d0d0d | = |
| Transition | border 0.15s ease | = |
| Cursor | text | = |
| Placeholder | #3d3d3d, opacity 1 | = |
| Painted layers | input.mktoField.mktoTextField 512.0x50.0 bg #ffffff border T:1px solid #cfcfcf / R:1px solid #cfcfcf / B:1px solid #cfcfcf / L:1px solid #cfcfcf r 2px | input.mktoField.mktoTextField 512.0x50.0 bg #ffffff border T:2px solid #727272 / R:2px solid #727272 / B:2px solid #727272 / L:2px solid #727272 r 2px |
| How | at rest | clicked into the field |

Crops: `sales-field-default.png`, `sales-field-focused.png`.

#### sales-select

Sales select. A form dropdown. Measured, never opened.

Page: sales. Selector: `form select`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 512 x 50 | = | = | = |
| Padding | 10px 64px 10px 16px | = | = | = |
| Border | 1px solid #cfcfcf | 2px solid #9e9e9e | 2px solid #727272 | 2px solid #9e9e9e |
| Radius | 2px | = | = | = |
| Background | #ffffff | = | = | = |
| Background image | url(data:…) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica 13px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0d0d | = | = | = |
| Transition | border 0.15s ease | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | select.mktoField.mktoHasWidth 512.0x50.0 bg #ffffff image url(data:…) border T:1px solid #cfcfcf / R:1px solid #cfcfcf / B:1px solid #cfcfcf / L:1px solid #cfcfcf r 2px | select.mktoField.mktoHasWidth 512.0x50.0 bg #ffffff image url(data:…) border T:2px solid #9e9e9e / R:2px solid #9e9e9e / B:2px solid #9e9e9e / L:2px solid #9e9e9e r 2px | select.mktoField.mktoHasWidth 512.0x50.0 bg #ffffff image url(data:…) border T:2px solid #727272 / R:2px solid #727272 / B:2px solid #727272 / L:2px solid #727272 r 2px | select.mktoField.mktoHasWidth 512.0x50.0 bg #ffffff image url(data:…) border T:2px solid #9e9e9e / R:2px solid #9e9e9e / B:2px solid #9e9e9e / L:2px solid #9e9e9e r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sales-select-default.png`, `sales-select-hover.png`, `sales-select-focus-visible.png`, `sales-select-pressed.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 845.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 14px/24.5px 400 |
| Letter spacing | normal |
| Colour | #646f79 |
| Text node | li.siteFooter__title: TWK Lausanne 14px/24.5px 500, #ffffff |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #ffffff, fill #ff584a |
| Painted layers | div.siteFooter__main__wrapper.py-2 1440.0x741.5 bg #0d0d0d; a.-white.css-0 126.2x19.0 border B:1px solid #000000 @ 0; a.-white.css-0 80.9x19.0 border B:1px solid #000000 @ 0; a.-white.css-0 155.7x19.0 border B:1px solid #000000 @ 0; a.-white.css-0 50.2x19.0 border B:1px solid #000000 @ 0; a.-white.css-0 84.0x19.0 border B:1px solid #000000 @ 0 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | TWK Lausanne 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0e10 | #cd4848 | = | #cd4848 |
| Transition | color, border 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff, fill #ff584a | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.siteFooter__logo-icon.css-0 40.0x40.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff | #0d0d0d | = | #0d0d0d |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | TWK Lausanne 22px/33px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0d0e10 | #cd4848 | = | #cd4848 |
| Transition | color, border 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0d0e10, fill #0d0d0d | 16 x 16, colour #cd4848, fill #ffffff | = | 16 x 16, colour #cd4848, fill #ffffff |
| Painted layers | a.css-1ubdndg.e1dfgc0i0 32.0x32.0 bg #ffffff r 16px | a.css-1ubdndg.e1dfgc0i0 32.0x32.0 bg #0d0d0d r 16px | a.css-1ubdndg.e1dfgc0i0 32.0x32.0 bg #ffffff r 16px outline 1px auto #005fcc offset 1px | a.css-1ubdndg.e1dfgc0i0 32.0x32.0 bg #0d0d0d r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 16px/28px 400 |
| Letter spacing | normal |
| Colour | #646f79 |
| Text node | a.styles_button-cta__K_nHI.styles_hide-on-logged-in__71yBl: TWK Lausanne 12px/18px 500, #ffffff |
| Transition | none |
| Cursor | default |
| Icon | 112 x 22, colour #0d0e10 |
| Painted layers | nav.styles_main-navigation__U3pgX 390.0x64.0 bg #ffffff; svg.styles_icon__VHmtA 0.0x0.0 border T:4px solid #000000 @ 0 / R:4px solid #000000 @ 0 / B:4px solid #000000 @ 0 / L:4px solid #000000 @ 0; div.css-1sa3o1x-p3.e1huxitw1 0.0x0.0 bg #ffffff r 6px shadow #000000 @ 0.15 0px 2px 8px 0px; div::after.css-1sa3o1x-p3.e1huxitw1 autoxauto border T:5px solid #000000 @ 0 / R:5px solid #000000 @ 0 / B:5px solid #ffffff / L:5px solid #000000 @ 0; a.styles_button-cta__K_nHI.styles_button-cta--secondary__MoBjP 0.0x0.0 bg #ffffff r 100px shadow #0d0d0d 0px 0px 0px 1px inset; a.styles_button-cta__K_nHI.styles_hide-on-logged-in__71yBl 94.2x40.0 bg #0d0d0d r 100px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4786ff offset 2px | = |
| Font | TWK Lausanne 14px/36px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | #0d0e10 | = | #0d0e10 |
| Transition | none 0.15s, 0.15s ease, ease-in-out delay 0s, 0s | = | outline, background 0.1s, 0.2s ease-in-out, ease-in-out delay 0s, 0s | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.styles_hamburger-button__icon__qeiIr 16.0x2.0 bg #0d0d0d r 1px; div::before.styles_hamburger-button__icon__qeiIr 16pxx2px bg #0d0d0d r 1px; div::after.styles_hamburger-button__icon__qeiIr 16pxx2px bg #0d0d0d r 1px | = | button.styles_hamburger-button__ZX4Kk 40.0x40.0 r 3px outline 2px solid #4786ff offset 2px; div.styles_hamburger-button__icon__qeiIr 16.0x2.0 bg #0d0d0d r 1px; div::before.styles_hamburger-button__icon__qeiIr 16pxx2px bg #0d0d0d r 1px; div::after.styles_hamburger-button__icon__qeiIr 16pxx2px bg #0d0d0d r 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The bar after its own toggle; the crop is the opened nav panel.

Page: home. Selector: `menu button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 0px 10px |
| Border | none |
| Radius | 3px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 14px/36px 500 |
| Letter spacing | 0.5px |
| Colour | #0d0e10 |
| Transition | none 0.15s, 0.15s ease, ease-in-out delay 0s, 0s |
| Cursor | pointer |
| Painted layers | div.styles_hamburger-button__icon__qeiIr.styles_hamburger-button__icon--state-open__PArpf 12.7x12.7 bg #0d0d0d r 1px; div::before.styles_hamburger-button__icon__qeiIr.styles_hamburger-button__icon--state-open__PArpf 16pxx2px bg #0d0d0d r 1px; div::after.styles_hamburger-button__icon__qeiIr.styles_hamburger-button__icon--state-open__PArpf 16pxx2px bg #0d0d0d r 1px |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. Read inside the open menu.

Page: home. Selector: `nav link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 61 |
| Padding | 20px |
| Border | T: none; R: none; B: 1px solid #e7e7e7; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TWK Lausanne 16px/20px 500 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Transition | color, border 0.3s ease |
| Cursor | pointer |
| Painted layers | a.styles_mobile-drawer__link__rKSd8 374.0x61.0 border B:1px solid #e7e7e7 |
| How | at rest |

Crops: `m-nav-link-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `background-color 150ms, color 150ms ease-in-out`, `width 150ms`, `border 150ms`, `fill 125ms`, `opacity 600ms ease-out`, `opacity 150ms ease-in-out`, `transform 300ms cubic-bezier(0.43, 1.48, 0.7, 1)`, `transform 400ms cubic-bezier(0.43, 1.48, 0.7, 1), opacity 400ms ease-in-out`, `transform 200ms ease-out`, `background-color 225ms`, `box-shadow 0.1s, margin 0.2s cubic-bezier(0.4, 0, 0.43, 0.88)`, `box-shadow 225ms`
