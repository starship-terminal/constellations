# Component measurements

Computed styles read from jace.ai and app.jace.ai/signin on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky marketing header: wordmark, Log In and Get started.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 170 |
| Padding | 16px 16px 100px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GeistSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| Icon | 60 x 28.5, colour #2d2d2d |
| Painted layers | div.w-full.max-w-[400px] 400.0x54.0 bg #ffffff border T:1px solid #d1d5dc / R:1px solid #d1d5dc / B:1px solid #d1d5dc / L:1px solid #d1d5dc r 9999.01px; a.inline-flex.items-center 68.1x36.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 9999.01px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Wordmark. The Jace AI home link in the header.

Page: home. Selector: `header a[href="/"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 60 x 28.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GeistSans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2d2d | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 60 x 28.5, colour #2d2d2d | = |
| How | at rest | mouse hover |

Crops: `logo-default.png`, `logo-hover.png`.

#### nav-login

Log In. The white pill linking to app.jace.ai/signin. Measured, never followed.

Page: home. Selector: `header a Log In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.14 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e7e7e7 | = | = | = |
| Radius | 9999.01px | = | = | = |
| Background | #ffffff | #f6f6f6 | = | #f6f6f6 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | GeistSans 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 68.1x36.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 9999.01px | a.inline-flex.items-center 68.1x36.0 bg #f6f6f6 border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 9999.01px | a.inline-flex.items-center 68.1x36.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 9999.01px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 68.1x36.0 bg #f6f6f6 border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 9999.01px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-cta

Header CTA. The dark pill linking to signup. Measured, never followed.

Page: home. Selector: `header Get started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.92 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999.01px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(in oklab, #2d2d2d 10%, #000000 100%) | linear-gradient(in oklab, #2d2d2d 100%, #000000 100%) | = | linear-gradient(in oklab, #2d2d2d 100%, #000000 100%) |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | GeistSans 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6f6f6 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.inline-flex.items-center 96.9x36.0 r 9999.01px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. The Gelica display headline, 88px light.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 908.34 x 108 |
| Padding | 0px 0px 20px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gelica 88px/88px 300 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The hero "Get started for free" control. Links toward signup; never followed.

Page: home. Selector: `button Get started for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 243.22 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | GeistSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 28.28 x 28.28, colour #000000 | = | = | = |
| ::before | 251.219px x 64px, absolute, bg #000000 @ 0 linear-gradient(135deg, #d1c2f4, #edc2e7, #ffdc61), radius 9999.01px | = | = | = |
| Painted layers | div.relative.flex 243.2x56.0 bg #1c1c1c r 9999.01px; span.flex.items-center 48.0x48.0 bg #ffffff r 9999.01px | div.relative.flex 243.2x56.0 bg #2c2c2c r 9999.01px; span.flex.items-center 48.0x48.0 bg #ffffff r 9999.01px | button.cursor-pointer.relative 243.2x56.0 outline 1px auto #005fcc offset 0px; div.relative.flex 243.2x56.0 bg #1c1c1c r 9999.01px; span.flex.items-center 48.0x48.0 bg #ffffff r 9999.01px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### chip

Demo chip. A white pill that switches the public inbox demo. A local toggle, not a submit.

Page: home. Selector: `button Draft e-mails`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137.72 x 38 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #d1d5dc | 1px solid #d1c2f4 | = | 1px solid #d1c2f4 |
| Radius | 9999.01px | = | = | = |
| Background | #ffffff | #d1c2f4 | = | #d1c2f4 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | GeistSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | button.bg-white.text-black 137.7x38.0 bg #ffffff border T:1px solid #d1d5dc / R:1px solid #d1d5dc / B:1px solid #d1d5dc / L:1px solid #d1d5dc r 9999.01px | button.bg-white.text-black 137.7x38.0 bg #d1c2f4 border T:1px solid #d1c2f4 / R:1px solid #d1c2f4 / B:1px solid #d1c2f4 / L:1px solid #d1c2f4 r 9999.01px | button.bg-white.text-black 137.7x38.0 bg #ffffff border T:1px solid #d1d5dc / R:1px solid #d1d5dc / B:1px solid #d1d5dc / L:1px solid #d1d5dc r 9999.01px outline 1px auto #005fcc offset 0px | button.bg-white.text-black 137.7x38.0 bg #d1c2f4 border T:1px solid #d1c2f4 / R:1px solid #d1c2f4 / B:1px solid #d1c2f4 / L:1px solid #d1c2f4 r 9999.01px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `chip-default.png`, `chip-hover.png`, `chip-focus-visible.png`, `chip-pressed.png`.

#### integration-pill

Integration pill. The Gmail works-with pill. Links to /integrations/gmail.

Page: home. Selector: `a Gmail`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84.77 x 42 | = | = | = |
| Padding | 8px 12px 8px 8px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999.01px | = | = | = |
| Background | #ffffff | #ffffff @ 0.8 | = | #ffffff @ 0.8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | GeistSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #2d2d2d | = | = | = |
| Painted layers | a.bg-white.rounded-full 84.8x42.0 bg #ffffff r 9999.01px | a.bg-white.rounded-full 84.8x42.0 bg #ffffff @ 0.8 r 9999.01px | a.bg-white.rounded-full 84.8x42.0 bg #ffffff r 9999.01px outline 1px auto #005fcc offset 1px | a.bg-white.rounded-full 84.8x42.0 bg #ffffff @ 0.8 r 9999.01px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `integration-pill-default.png`, `integration-pill-hover.png`, `integration-pill-focus-visible.png`, `integration-pill-pressed.png`.

#### feature-card

Feature card. A product card linking to a public integration page.

Page: home. Selector: `card Jace for Gmail`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 434.66 x 90 | = |
| Padding | 16px | = |
| Gap | 4px | = |
| Border | 1px solid #e5e5e5 | 1px solid #2d2d2d @ 0.65 |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GeistSans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2d2d | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.group.flex 434.7x90.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 16px | a.group.flex 434.7x90.0 border T:1px solid #2d2d2d @ 0.65 / R:1px solid #2d2d2d @ 0.65 / B:1px solid #2d2d2d @ 0.65 / L:1px solid #2d2d2d @ 0.65 r 16px |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### section-title

Section title. The first section heading under the hero.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 612.06 x 58.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gelica 56px/58.8px 400 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### page-ground

Page ground. The body fill and type the marketing page paints.

Page: home. Selector: `body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 14966.83 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GeistSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| Icon | 60 x 28.5, colour #2d2d2d |
| Painted layers | div.w-full.max-w-[400px] 400.0x54.0 bg #ffffff border T:1px solid #d1d5dc / R:1px solid #d1d5dc / B:1px solid #d1d5dc / L:1px solid #d1d5dc r 9999.01px; a.inline-flex.items-center 68.1x36.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 9999.01px; div.relative.flex 243.2x56.0 bg #1c1c1c r 9999.01px; span.flex.items-center 48.0x48.0 bg #ffffff r 9999.01px; a.bg-white.rounded-full 84.8x42.0 bg #ffffff r 9999.01px; a.bg-white.rounded-full 101.1x42.0 bg #ffffff r 9999.01px |
| How | at rest |

Crops: none.

#### pager

Pager button. The next-testimonial control. A local carousel toggle.

Page: home. Selector: `button Next testimonial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #f6f6f6 @ 0.1 | = | #f6f6f6 @ 0.1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | GeistSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #2d2d2d | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.items-center 16.0x16.0 bg #f6f6f6 @ 0.1 | button.inline-flex.items-center 16.0x16.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 16.0x16.0 bg #f6f6f6 @ 0.1 |

Crops: `pager-default.png`, `pager-hover.png`, `pager-focus-visible.png`, `pager-pressed.png`.

### Pricing

#### pricing-title

Pricing title. The pricing headline in Gelica.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 204 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gelica 56px/68px 300 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### billing-yearly

Yearly toggle. The selected yearly billing control. A local toggle; the monthly sibling is measured separately.

Page: pricing. Selector: `button Bill yearly`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 175.3 x 36 | = | = | = |
| Padding | 6px 6px 6px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999.01px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | GeistSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.text-sm.font-medium 175.3x36.0 bg #ffffff r 9999.01px; div.inline-flex.items-center 72.4x28.0 bg #fafafa border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999.01px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | button.text-sm.font-medium 175.3x36.0 bg #ffffff r 9999.01px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.inline-flex.items-center 72.4x28.0 bg #fafafa border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 9999.01px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-yearly-default.png`, `billing-yearly-hover.png`, `billing-yearly-focus-visible.png`, `billing-yearly-pressed.png`.

#### billing-monthly

Monthly toggle. The unselected monthly billing control, measured at rest (not switched, so the yearly table stays).

Page: pricing. Selector: `button Bill monthly`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 115.69 x 36 | = | = |
| Padding | 8px 12px 8px 14px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 9999.01px | = | = |
| Background | transparent | #ffffff | #ffffff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GeistSans 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2d2d2d | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Opacity | 0.73 | = | = |
| Cursor | default | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |
| Painted layers | - | button.items-center.justify-center 115.7x36.0 bg #ffffff r 9999.01px | button.items-center.justify-center 115.7x36.0 bg #ffffff r 9999.01px |

Crops: `billing-monthly-default.png`, `billing-monthly-hover.png`, `billing-monthly-pressed.png`.

#### price-card

Plus plan card. The Plus plan card on the white pricing surface.

Page: pricing. Selector: `div Plus Plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 386 x 588 |
| Padding | 24px |
| Gap | 24px |
| Border | 1px solid #2d2d2d @ 0.05 |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| Outline | none |
| Font | GeistSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| Painted layers | div.border.border-solid 386.0x588.0 bg #ffffff border T:1px solid #2d2d2d @ 0.05 / R:1px solid #2d2d2d @ 0.05 / B:1px solid #2d2d2d @ 0.05 / L:1px solid #2d2d2d @ 0.05 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.relative.w-2.5 14.1x14.1 bg #edc2e7 r 2px; div.relative.w-2.5 14.1x14.1 bg #edc2e7 r 2px; div.relative.w-2.5 14.1x14.1 bg #edc2e7 r 2px; div.relative.w-2.5 14.1x14.1 bg #edc2e7 r 2px |
| How | at rest |

Crops: `price-card-default.png`.

#### price-cta

Plan CTA. The Pro plan trial button. Links toward signup; never followed.

Page: pricing. Selector: `Try Pro`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 338 x 44 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(in oklab, #2d2d2d 10%, #000000 100%) | linear-gradient(in oklab, #2d2d2d 100%, #000000 100%) | = | linear-gradient(in oklab, #2d2d2d 100%, #000000 100%) |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | GeistSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f6f6f6 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.inline-flex.items-center 338.0x44.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `price-cta-default.png`, `price-cta-hover.png`, `price-cta-focus-visible.png`, `price-cta-pressed.png`.

#### price-secondary

Secondary CTA. The white "Get in touch" link to the sales form. Never followed from this measurement.

Page: pricing. Selector: `a Get in touch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 44 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e7e7e7 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f6f6f6 | = | #f6f6f6 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | GeistSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 336.0x44.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 8px | a.inline-flex.items-center 336.0x44.0 bg #f6f6f6 border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 8px | a.inline-flex.items-center 336.0x44.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 336.0x44.0 bg #f6f6f6 border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-secondary-default.png`, `price-secondary-hover.png`, `price-secondary-focus-visible.png`, `price-secondary-pressed.png`.

#### faq

FAQ row. A closed FAQ accordion trigger.

Page: pricing. Selector: `button How much does Jace AI cost`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 568 x 92 | = | = |
| Padding | 32px 0px | = | = |
| Gap | 48px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | GeistSans 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2d2d2d | = | = |
| Transition | all 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Icon | 16 x 16, colour #a1a1aa | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | button.flex-1.justify-between 568.0x92.0 outline 1px auto #005fcc offset 0px |

Crops: `faq-default.png`, `faq-hover.png`, `faq-focus-visible.png`.

#### faq-open

FAQ row, open. The same FAQ trigger after its own press, with the answer open.

Page: pricing. Selector: `FAQ open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 568 x 92 |
| Padding | 32px 0px |
| Gap | 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GeistSans 14px/20px 500 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | all 0.075s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Icon | 16 x 16, colour #a1a1aa |
| How | at rest |

Crops: `faq-open-default.png`.

#### link

Inline link. An underlined body link.

Page: pricing. Selector: `a lawyers`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 50.45 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GeistSans 14px/26px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2d2d @ 0.8 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `link-default.png`, `link-hover.png`.

### Blog

#### blog-title

Blog title. The blog index headline.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1254 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gelica 64px/70.4px 500 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `blog-title-default.png`.

#### blog-nav

Docs nav link. A text nav link on the blog header (Learn).

Page: blog. Selector: `a Learn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43.67 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | GeistSans 16px/26px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | #d1c2f4 | = | #d1c2f4 |
| Transition | all 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.font-[family-name:var(--font-geist-sans)].font-normal 43.7x26.0 outline 1px auto #005fcc offset 1px | = |

Crops: `blog-nav-default.png`, `blog-nav-hover.png`, `blog-nav-focus-visible.png`, `blog-nav-pressed.png`.

#### blog-card

Blog card. A published post card. Public marketing content.

Page: blog. Selector: `first blog card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 427.33 x 424 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GeistSans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2d2d | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `blog-card-default.png`, `blog-card-hover.png`.

### Docs

#### docs-title

Docs title. The getting-started headline.

Page: docs. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 930 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gelica 64px/70.4px 500 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `docs-title-default.png`.

#### docs-nav

Docs sidebar link. A link in the public docs navigation.

Page: docs. Selector: `a Billing & Plans`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 310 x 36 | = |
| Padding | 6px 8px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GeistSans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2d2d @ 0.8 | #2d2d2d |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `docs-nav-default.png`, `docs-nav-hover.png`.

### Sales contact (boundary)

#### form-title

Form title. The sales contact heading. The form is a boundary: nothing is submitted.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 478 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gelica 32px/40px 500 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `form-title-default.png`.

#### text-field

Text field. The first sales-form field, empty. Nothing is typed and nothing is submitted. A filled state was not captured.

Page: contact. Selector: `input first`. States: default, hover, focus-visible, focused.

| Property | default | hover | focus-visible | focused |
|---|---|---|---|---|
| Size (w x h) | 478 x 50 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | 1px solid #d1d5dc | = | 1px solid #000000 @ 0 | 1px solid #000000 @ 0 |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | GeistSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | all 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | text | = | = | = |
| Placeholder | #99a1af, opacity 1 | = | = | = |
| Painted layers | input.w-full.px-4 478.0x50.0 bg #ffffff border T:1px solid #d1d5dc / R:1px solid #d1d5dc / B:1px solid #d1d5dc / L:1px solid #d1d5dc r 8px | = | input.w-full.px-4 478.0x50.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | input.w-full.px-4 478.0x50.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | clicked into the field; nothing submitted |

Crops: `text-field-default.png`, `text-field-hover.png`, `text-field-focus-visible.png`, `text-field-focused.png`.

#### text-area

Text area. The message textarea, focused only. Nothing typed that would be sent.

Page: contact. Selector: `textarea`. States: .

Not found on the page at capture time.

#### form-submit

Submit button. The send button, measured with a forced pressed state. Never clicked, so the form is not submitted.

Page: contact. Selector: `button Send a request`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 478 x 44 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(in oklab, #2d2d2d 0%, #000000 100%) | linear-gradient(in oklab, #454545 0%, #454545 100%) | = | linear-gradient(in oklab, #454545 0%, #454545 100%) |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = |
| Outline | none | = | = | = |
| Font | GeistSans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 478.0x44.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | button.inline-flex.items-center 478.0x44.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #c4b5fd 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `form-submit-default.png`, `form-submit-hover.png`, `form-submit-focus-visible.png`, `form-submit-pressed.png`.

#### text-field-invalid

Required field. A required field at rest (empty). The form was not submitted, so this is the resting required style, not a posted error.

Page: contact. Selector: `input required`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 478 x 50 |
| Padding | 12px 16px |
| Border | 1px solid #d1d5dc |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | GeistSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | all 0.075s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | text |
| Placeholder | #99a1af, opacity 1 |
| Painted layers | input.w-full.px-4 478.0x50.0 bg #ffffff border T:1px solid #d1d5dc / R:1px solid #d1d5dc / B:1px solid #d1d5dc / L:1px solid #d1d5dc r 8px |
| How | at rest |

Crops: `text-field-invalid-default.png`.

### App sign-in (boundary)

#### signin-title

Sign-in title. The app sign-in headline. Boundary: no OAuth, no SSO, nothing typed.

Page: signin. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 400 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gelica 40px/40px 400 |
| Letter spacing | -0.8px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `signin-title-default.png`.

#### signin-oauth

Google button. Continue with Google. Measured, never pressed.

Page: signin. Selector: `button Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 40 | = | = | 388 x 38.8 |
| Padding | 8px 16px 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #27272a | = | = | = |
| Radius | 6px | = | = | = |
| Background | #222225 | #222225 @ 0.5 | = | #222225 @ 0.5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #c4b5fd offset 2px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f4f4f5 | = | = | = |
| Transition | background-color, border-color, color, scale 0.1s, 0.1s, 0.1s, 0.2s ease-out, ease-out, ease-out, ease-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #f4f4f5 | = | = | 19.4 x 19.4, colour #f4f4f5 |
| Painted layers | button.inline-flex.items-center 400.0x40.0 bg #222225 border T:1px solid #27272a / R:1px solid #27272a / B:1px solid #27272a / L:1px solid #27272a r 6px | button.inline-flex.items-center 400.0x40.0 bg #222225 @ 0.5 border T:1px solid #27272a / R:1px solid #27272a / B:1px solid #27272a / L:1px solid #27272a r 6px | button.inline-flex.items-center 400.0x40.0 bg #222225 border T:1px solid #27272a / R:1px solid #27272a / B:1px solid #27272a / L:1px solid #27272a r 6px outline 2px solid #c4b5fd offset 2px | button.inline-flex.items-center 388.0x38.8 bg #222225 @ 0.5 border T:1px solid #27272a / R:1px solid #27272a / B:1px solid #27272a / L:1px solid #27272a r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-oauth-default.png`, `signin-oauth-hover.png`, `signin-oauth-focus-visible.png`, `signin-oauth-pressed.png`.

#### signin-outlook

Outlook button. Continue with Outlook. Measured, never pressed.

Page: signin. Selector: `button Continue with Outlook`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 400 x 40 | = |
| Padding | 8px 16px 8px 12px | = |
| Gap | 8px | = |
| Border | 1px solid #27272a | = |
| Radius | 6px | = |
| Background | #222225 | #222225 @ 0.5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #f4f4f5 | = |
| Transition | background-color, border-color, color, scale 0.1s, 0.1s, 0.1s, 0.2s ease-out, ease-out, ease-out, ease-out delay 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #f4f4f5 | = |
| Painted layers | button.inline-flex.items-center 400.0x40.0 bg #222225 border T:1px solid #27272a / R:1px solid #27272a / B:1px solid #27272a / L:1px solid #27272a r 6px | button.inline-flex.items-center 400.0x40.0 bg #222225 @ 0.5 border T:1px solid #27272a / R:1px solid #27272a / B:1px solid #27272a / L:1px solid #27272a r 6px |
| How | at rest | mouse hover |

Crops: `signin-outlook-default.png`, `signin-outlook-hover.png`.

#### signin-sso

SSO link. The enterprise SSO link. Never followed.

Page: signin. Selector: `a Launch the SSO portal`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 127.27 x 15 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter Variable 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `signin-sso-default.png`, `signin-sso-hover.png`.

#### signin-signup

Sign up link. The sign-up link on the sign-in card. Never followed.

Page: signin. Selector: `a Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.48 x 20 | = | = | 48.97 x 19.4 |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #c4b5fd offset 2px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | #f3e8ff | = | #f3e8ff |
| Transition | background-color, border-color, color, scale 0.1s, 0.1s, 0.1s, 0.2s ease-out, ease-out, ease-out, ease-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 50.4844px x 2px, absolute, bg #27272a, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.inline-flex.items-center 50.5x20.0 r 4px outline 2px solid #c4b5fd offset 2px | = |

Crops: `signin-signup-default.png`, `signin-signup-hover.png`, `signin-signup-focus-visible.png`, `signin-signup-pressed.png`.

#### signin-quote

Quote card. The published testimonial card beside the sign-in form.

Page: signin. Selector: `quote card`. States: .

Not found on the page at capture time.

### Mobile (390 wide)

#### m-header

Mobile header. The header at 390.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 130 |
| Padding | 16px 16px 60px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GeistSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| Icon | 50 x 23.75, colour #2d2d2d |
| Painted layers | div.w-full.max-w-[400px] 358.0x54.0 bg #ffffff border T:1px solid #d1d5dc / R:1px solid #d1d5dc / B:1px solid #d1d5dc / L:1px solid #d1d5dc r 9999.01px; a.inline-flex.items-center 68.1x36.0 bg #ffffff border T:1px solid #e7e7e7 / R:1px solid #e7e7e7 / B:1px solid #e7e7e7 / L:1px solid #e7e7e7 r 9999.01px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu

Menu button. The mobile menu button.

Page: home. Selector: `button Open main menu`. States: .

Not found on the page at capture time.

#### m-hero

Mobile headline. The hero headline at 390.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 116 |
| Padding | 0px 0px 20px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gelica 48px/48px 300 |
| Letter spacing | normal |
| Colour | #2d2d2d |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

### App signup (boundary)

#### signup-title

Signup title. The first signup headline (Join +10,000). Boundary: no OAuth.

Page: signup. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Gelica 30px/32px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `signup-title-default.png`.

#### signup-continue

Signup Continue. The landing Continue control; measured, never clicked (it opens a privacy notice).

Page: signup. Selector: `button Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.52 x 40 | = | = | 89.74 x 38.8 |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(135deg, #d1c2f4, #edc2e7, #ffdc61) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #c4b5fd offset 2px | = |
| Font | Inter Variable 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, border-color, color, scale 0.1s, 0.1s, 0.1s, 0.2s ease-out, ease-out, ease-out, ease-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 92.5156px x 40px, absolute, bg #000000 @ 0, radius 6px | 92.5156px x 40px, absolute, bg #000000 @ 0.1, radius 6px | = | 92.5156px x 40px, absolute, bg #000000 @ 0.1, radius 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.inline-flex.items-center 92.5x40.0 r 6px outline 2px solid #c4b5fd offset 2px | = |

Crops: `signup-continue-default.png`, `signup-continue-hover.png`, `signup-continue-focus-visible.png`, `signup-continue-pressed.png`.

## Transitions declared in the readable stylesheets

Transitions the CSSOM could read on each page. Per-state Transition rows above are computed values.
