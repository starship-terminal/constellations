# Component measurements

Computed styles read from amie.so on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (no consent overlay mounts on these routes), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The floating bar: logo, Features flyout, Pricing, Login, Get started.

Page: home. Selector: `header/nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1024 x 59 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | -0.003px |
| Colour | #000000 |
| Text node | button.group.hidden: Inter 14px/14px 500, #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #000000 |
| Painted layers | button.group.hidden 78.2x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px; a.group.flex 66.7x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px; a.group.text-secondary 57.0x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px; a.text-sm.px-4 106.6x32.0 bg #11a8ff r 8px |
| Ancestor paint | 1 up div.w-full.h-15 bg #fafafa @ 0.8 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `header a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | -0.003px |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-flyout-button

Nav flyout button. A Radix dropdown trigger; opens the Features panel.

Page: home. Selector: `button:has-text("Features")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.16 x 32 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | none | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group.hidden 78.2x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px | button.group.hidden 78.2x32.0 bg #000000 @ 0.05 r 8px outline 2px solid #000000 @ 0 offset 2px | - | button.group.hidden 78.2x32.0 bg #000000 @ 0.05 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-flyout-button-default.png`, `nav-flyout-button-hover.png`, `nav-flyout-button-focus-visible.png`, `nav-flyout-button-pressed.png`.

#### nav-flyout-open

Features flyout, open. The Features button after its own toggle; the crop is the opened panel.

Page: home. Selector: `button:has-text("Features")`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 78.16 x 32 |
| Padding | 6px 10px |
| Border | none |
| Radius | 8px |
| Background | #000000 @ 0.05 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/14px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | button.group.hidden 78.2x32.0 bg #000000 @ 0.05 r 8px |
| How | own toggle |

Crops: `nav-flyout-open-opened.png`.

#### nav-link

Nav link.

Page: home. Selector: `a:has-text("Pricing")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.72 x 32 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.flex 66.7x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px | a.group.flex 66.7x32.0 bg #000000 @ 0.05 r 8px outline 2px solid #000000 @ 0 offset 2px | = | a.group.flex 66.7x32.0 bg #000000 @ 0.05 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Login link. The secondary nav link. Measured, never followed.

Page: home. Selector: `a:has-text("Login")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.98 x 32 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = | = |
| Font | Inter 14px/14px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #5c5c5c | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.text-secondary 57.0x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px | a.group.text-secondary 57.0x32.0 bg #000000 @ 0.05 r 8px outline 2px solid #000000 @ 0 offset 2px | = | a.group.text-secondary 57.0x32.0 bg #000000 @ 0.05 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Nav CTA. The small blue Get started. Measured, never followed.

Page: home. Selector: `a:has-text("Get started")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.63 x 32 | = | = | = |
| Padding | 6px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #11a8ff | #218fcd | = | #218fcd |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.text-sm.px-4 106.6x32.0 bg #11a8ff r 8px | a.text-sm.px-4 106.6x32.0 bg #218fcd r 8px | a.text-sm.px-4 106.6x32.0 bg #11a8ff r 8px outline 1px auto #005fcc offset 1px | a.text-sm.px-4 106.6x32.0 bg #218fcd r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title.

Page: home. Selector: `h1`. States: .

Not found on the page at capture time.

#### changelog-pill

Changelog pill. The "what's new" link under the hero.

Page: home. Selector: `a:has-text(":")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 391.95 x 15.83 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 12px/15.84px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #5c5c5c | = | = | = |
| Text node | span.flex.items-center: Inter 12px/15.84px 500, #5c5c5c, ls -0.003px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #a0a0a0 | = | = | = |
| Painted layers | a.shadow-none.gap-1.5 392.0x15.8 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | a.shadow-none.gap-1.5 392.0x15.8 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `changelog-pill-default.png`, `changelog-pill-hover.png`, `changelog-pill-focus-visible.png`, `changelog-pill-pressed.png`.

#### cta-primary

Primary CTA. The hero blue Get started. Measured, never followed.

Page: home. Selector: `a:has-text("Get started")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 140.23 x 49.59 | = | = | = |
| Padding | 12px 28px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #11a8ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/25.6px 600 | = | = | = |
| Letter spacing | -0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.text-sm.sm:text-md 140.2x49.6 bg #11a8ff r 12px | = | a.text-sm.sm:text-md 140.2x49.6 bg #11a8ff r 12px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-primary-default.png`, `cta-primary-hover.png`, `cta-primary-focus-visible.png`, `cta-primary-pressed.png`.

#### cta-secondary

Secondary CTA. The ghost Download beside it. Measured, never pressed.

Page: home. Selector: `:has-text("Download")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155.94 x 49.59 | = | = | = |
| Padding | 12px 28px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/25.6px 600 | = | = | = |
| Letter spacing | -0.2px | = | = | = |
| Colour | #5c5c5c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a0a0a0 | = | = | = |
| Painted layers | button.text-sm.sm:text-md 155.9x49.6 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`, `cta-secondary-pressed.png`.

#### section-title

Section title.

Page: home. Selector: `h2/h3 below the hero`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 260.67 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/28px 600 |
| Letter spacing | -0.003px |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| Ancestor paint | 3 up div.flex.w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px |
| How | at rest |

Crops: `section-title-default.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 128 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 56px/64px 700 |
| Letter spacing | -0.7px |
| Colour | #171717 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-monthly

Billing toggle, monthly.

Page: pricing. Selector: `button:has-text("Bill monthly")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.8 x 28 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `billing-monthly-default.png`, `billing-monthly-hover.png`, `billing-monthly-focus-visible.png`, `billing-monthly-pressed.png`.

#### billing-yearly

Billing toggle, yearly.

Page: pricing. Selector: `button:has-text("Bill yearly")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98.19 x 28 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `billing-yearly-default.png`, `billing-yearly-hover.png`, `billing-yearly-focus-visible.png`, `billing-yearly-pressed.png`.

#### billing-yearly-on

Billing toggle, yearly on. The yearly side after its own toggle; plan prices flip and the trial button is re-rendered.

Page: pricing. Selector: `button:has-text("Bill yearly")`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 98.19 x 28 |
| Padding | 0px 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/28px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Opacity | 0.8 |
| Cursor | pointer |
| How | own toggle |

Crops: `billing-yearly-on-opened.png`.

#### plan-select

Select button. The white plan row action. Measured, never pressed.

Page: pricing. Selector: `button:has-text("Select")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 253.11 x 32 | = | = | = |
| Padding | 6px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #fafafa | = | #fafafa |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.flex.h-8 253.1x32.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | button.flex.h-8 253.1x32.0 bg #fafafa r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | button.flex.h-8 253.1x32.0 bg #fafafa r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-select-default.png`, `plan-select-hover.png`, `plan-select-focus-visible.png`, `plan-select-pressed.png`.

#### plan-card

Plan card.

Page: pricing. Selector: `card ancestor of trial button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 431 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | -0.003px |
| Colour | #000000 |
| Text node | span.text-xl.tracking-[-0.0125em]: Inter 20px/28px 500, #000000, ls -0.25px |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #fe6600 |
| Painted layers | div.flex.flex-col 480.0x431.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; div.h-px.w-[calc(100%+40px)] 480.0x1.0 bg #ebebeb; button.flex.w-full 440.0x36.0 bg #000000 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Trial button. "Start 7 day free trial": the black plan CTA. Measured, never pressed.

Page: pricing. Selector: `button:has-text("trial")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 440 x 36 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.flex.w-full 440.0x36.0 bg #000000 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | = | = |
| Ancestor paint | 2 up div.flex.flex-col bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-question

FAQ accordion button.

Page: pricing. Selector: `button[aria-expanded]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 976 x 68 | = | = | = |
| Padding | 20px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a0a0a0 | = | = | = |
| Ancestor paint | 2 up div.flex.flex-col bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-pressed.png`.

#### faq-open

FAQ accordion, open. The same item after its own toggle.

Page: pricing. Selector: `button[aria-expanded]`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 976 x 68 |
| Padding | 20px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/28px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #a0a0a0 |
| Ancestor paint | 2 up div.flex.flex-col bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px |
| How | own toggle |

Crops: `faq-open-opened.png`.

### Download

#### download-title

Download title.

Page: download. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 245.16 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 32px/28px 700 |
| Letter spacing | -0.003px |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `download-title-default.png`.

#### download-button

Download button. The app download action. Measured, never pressed.

Page: download. Selector: `a/button:has-text("Download")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 259.53 x 56 | = | = | = |
| Padding | 8px 16px 8px 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #2e2e2e | #454545 | = | #454545 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | #ffffff 0px 0px 0px 0px, #93c5fd @ 0.5 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = |
| Outline | none | = | = | = |
| Font | Inter 18px/28px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.justify-center.transition-colors 259.5x56.0 bg #2e2e2e r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | button.justify-center.transition-colors 259.5x56.0 bg #454545 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | button.justify-center.transition-colors 259.5x56.0 bg #2e2e2e r 12px shadow #ffffff 0px 0px 0px 0px, #93c5fd @ 0.5 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | button.justify-center.transition-colors 259.5x56.0 bg #454545 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `download-button-default.png`, `download-button-hover.png`, `download-button-focus-visible.png`, `download-button-pressed.png`.

### Contact

#### contact-title

Contact title.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 944 x 54.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 40px/54.4px 700 |
| Letter spacing | -0.5px |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `contact-title-default.png`.

#### contact-link

Contact link.

Page: contact. Selector: `mailto link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.44 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.font-medium.whitespace-nowrap 72.4x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `contact-link-default.png`, `contact-link-hover.png`, `contact-link-focus-visible.png`, `contact-link-pressed.png`.

#### contact-field

Contact field. Focused only; nothing was typed.

Page: contact. Selector: `input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 554.67 x 54 | = |
| Padding | 12px 16px | = |
| Border | 1px solid #afafaf | 1px solid #11a8ff |
| Radius | 12px | = |
| Background | #ffffff | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #11a8ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 16px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #919191, opacity 1 | = |
| Painted layers | input.w-full.px-4 554.7x54.0 bg #ffffff border T:1px solid #afafaf / R:1px solid #afafaf / B:1px solid #afafaf / L:1px solid #afafaf r 12px outline 2px solid #000000 @ 0 offset 2px | input.w-full.px-4 554.7x54.0 bg #ffffff border T:1px solid #11a8ff / R:1px solid #11a8ff / B:1px solid #11a8ff / L:1px solid #11a8ff r 12px shadow #ffffff 0px 0px 0px 0px, #11a8ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 3 up div.bg-white.rounded-2xl bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = |
| How | at rest | clicked into the field |

Crops: `contact-field-default.png`, `contact-field-focused.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 577 |
| Padding | 40px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | -0.003px |
| Colour | #000000 |
| Text node | a.font-medium.whitespace-nowrap: Inter 14px/20px 500, #000000, ls -0.003px |
| Transition | none |
| Cursor | default |
| Icon | 165 x 21, colour #000000 |
| Painted layers | div.flex.w-full 976.0x469.0 border T:1px solid #000000 @ 0.04 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.2 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.font-medium.whitespace-nowrap 154.2x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.94 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.font-medium.whitespace-nowrap 66.9x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-legal

Legal link.

Page: home. Selector: `footer a:has-text("Privacy")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109.78 x 28 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Opacity | 0.4 | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.font-medium.opacity-[0.4] 109.8x28.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-legal-default.png`, `footer-legal-hover.png`, `footer-legal-focus-visible.png`, `footer-legal-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header/nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 59 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/28px 400 |
| Letter spacing | -0.003px |
| Colour | #000000 |
| Text node | a.group.flex: Inter 14px/14px 500, #000000, ls -0.003px |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #000000 |
| Painted layers | button.group.hidden 0.0x0.0 r 8px outline 2px solid #000000 @ 0 offset 2px; a.group.flex 66.7x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px; a.text-sm.px-4 106.6x32.0 bg #11a8ff r 8px |
| Ancestor paint | 1 up div.w-full.h-15 bg #fafafa @ 0.8 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `header button`. States: .

Not found on the page at capture time.

#### m-menu-open

Mobile menu, open. The button after its own toggle; the open panel shows in the crop.

Page: home. Selector: `header button`. States: .

Not found on the page at capture time.

#### m-nav-link

Mobile nav link.

Page: home. Selector: `a:has-text("Pricing")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 66.72 x 32 |
| Padding | 6px 10px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 14px/14px 500 |
| Letter spacing | -0.003px |
| Colour | #000000 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | a.group.flex 66.7x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `m-nav-link-default.png`.

#### m-cta

Mobile CTA.

Page: home. Selector: `a:has-text("Get started")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.63 x 32 | = | = | = |
| Padding | 6px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #11a8ff | #218fcd | = | #218fcd |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | -0.003px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.text-sm.px-4 106.6x32.0 bg #11a8ff r 8px | a.text-sm.px-4 106.6x32.0 bg #218fcd r 8px | a.text-sm.px-4 106.6x32.0 bg #11a8ff r 8px outline 1px auto #e59700 offset 1px | a.text-sm.px-4 106.6x32.0 bg #218fcd r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `none`
