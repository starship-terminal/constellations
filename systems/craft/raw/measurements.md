# Component measurements

Computed styles read from craft.do on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /pricing, /download, /imagine, /learn and /write — no consent banner exists (generic overlay-hiding stayed as defence-in-depth) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The floating pill header: the CRAFT wordmark, Product / Imagine / Community / Pricing / Learn / Download links, Log in and the black Try Craft Free pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 920 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 26px |
| Background | transparent |
| Background image | linear-gradient(#ffffff @ 0.4 10%, #ffffff @ 0.8) |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px |
| Backdrop filter | blur(4px) |
| Outline | none |
| Font | UntitledSansFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #030302 |
| Text node | button.small.transition-colors: UntitledSansFont 16px/22.4px 400, #030302, ls -0.32px |
| Transition | -webkit-backdrop-filter, backdrop-filter 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 100 x 20, colour #030302 |
| ::before | 920px x 52px, absolute, bg #000000 @ 0 linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64), radius 24px |
| Painted layers | header.fixed.right-0 920.0x52.0 image linear-gradient(#ffffff @ 0.4 10%, #ffffff @ 0.8) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px; header::before.fixed.right-0 920pxx52px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; a.inline-flex.items-center 134.6x36.0 bg #030302 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; a.inline-flex.items-center 0.0x0.0 bg #030302 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The CRAFT wordmark anchor.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 108 x 28 |
| Padding | 4px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSansFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #030302 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 100 x 20, colour #030302 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A header nav link; measured, never followed.

Page: home. Selector: `header Product link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.92 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 3.35544e+07px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | UntitledSansFont 16px/22.4px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #030302 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.small.transition-colors 57.9x20.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### try-cta

Try Craft Free pill. The black "Try Craft Free" header pill (leads to /download); measured, never followed.

Page: home. Selector: `header Try Craft Free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134.61 x 36 | = | = | = |
| Padding | 8px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #030302 | #030302 @ 0.75 | = | #030302 @ 0.75 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | = | = |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 1px | = |
| Font | UntitledSansFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: UntitledSansFont 16px/24px 500, #ffffff | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 134.6x36.0 bg #030302 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | a.inline-flex.items-center 134.6x36.0 bg #030302 @ 0.75 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | a.inline-flex.items-center 134.6x36.0 bg #030302 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px outline 1px auto #030302 @ 0.0607843 offset 1px | a.inline-flex.items-center 134.6x36.0 bg #030302 @ 0.75 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `try-cta-default.png`, `try-cta-hover.png`, `try-cta-focus-visible.png`, `try-cta-pressed.png`.

#### login-link

Log-in link. The "Log in" header link (points at docs.craft.do); measured, never followed.

Page: home. Selector: `header Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.13 x 22.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 3.35544e+07px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | UntitledSansFont 16px/22.4px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #030302 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.small.hidden 44.1x22.4 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

### Home

#### hero-h1

Hero headline. The 66px Untitled Serif hero ("Your space for notes, tasks, and big ideas") over the sky collage.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 666 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSerifFont 66px/66px 400 |
| Letter spacing | -1.98px |
| Colour | #030302 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The white 48px "Try Craft Free" hero pill (leads to /download); measured, never followed.

Page: home. Selector: `hero Try Craft Free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170.61 x 48 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 19.9568px 24.9298px 3.9892px, #000000 @ 0.04 0px 9.95681px 9.96761px -4.97841px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 19.7526px 24.598px 3.93816px, #000000 @ 0.04 0px 9.75263px 9.81447px -4.87632px |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 1px | = |
| Font | UntitledSansFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #030302 | = | = | = |
| Text node | span: UntitledSansFont 16px/24px 500, #030302 | = | = | = |
| Transition | all 0.5s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 170.609px x 48px, absolute, bg #000000 @ 0 linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64), radius 24px | = | = | = |
| Painted layers | a.inline-flex.items-center 170.6x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px; a::before.inline-flex.items-center 170.609pxx48px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; div.glass-button-gradient-bg.absolute 170.6x48.0 image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.59 25%, #ffffff @ 0.6 50%, #ffffff @ 0.84 75%) | a.inline-flex.items-center 170.6x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 19.9568px 24.9298px 3.9892px, #000000 @ 0.04 0px 9.95681px 9.96761px -4.97841px; a::before.inline-flex.items-center 170.609pxx48px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; div.glass-button-gradient-bg.absolute 170.6x48.0 image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.59 25%, #ffffff @ 0.6 50%, #ffffff @ 0.84 75%) | a.inline-flex.items-center 170.6x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px outline 1px auto #030302 @ 0.0607843 offset 1px; a::before.inline-flex.items-center 170.609pxx48px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; div.glass-button-gradient-bg.absolute 170.6x48.0 image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.59 25%, #ffffff @ 0.6 50%, #ffffff @ 0.84 75%) | a.inline-flex.items-center 170.6x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 19.7526px 24.598px 3.93816px, #000000 @ 0.04 0px 9.75263px 9.81447px -4.87632px; a::before.inline-flex.items-center 170.609pxx48px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; div.glass-button-gradient-bg.absolute 170.6x48.0 image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.59 25%, #ffffff @ 0.6 50%, #ffffff @ 0.84 75%) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

### Pricing

#### price-h1

Pricing headline. "Choose The Plan That’s Right For You".

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1160 x 59.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSerifFont 54px/59.4px 400 |
| Letter spacing | -1.08px |
| Colour | #030302 |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### billing-toggle

Billing toggle. A segment of the Yearly/Monthly billing switch (112x40 inside a pill); toggled locally for the shot, never submitted.

Page: pricing. Selector: `Yearly button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 3.35544e+07px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 0px | = |
| Font | UntitledSansFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.205 0 0) | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 2 up div.glass-toggle-bg.glass-toggle-border shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative.flex 112.0x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #030302 @ 0.0607843 offset 0px | = |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-focus-visible.png`, `billing-toggle-pressed.png`.

#### plan-card

Plan card. The PLUS plan card (name, serif price, /month, feature list, CTA); measured, never used.

Page: pricing. Selector: `PLUS card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 273.05 x 462.69 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | UntitledSansFont 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #030302 | = | = | = |
| Text node | h4.h4.text-black-900: UntitledSansFont 16px/24px 500, #030302, ls 0.16px | = | = | = |
| Transition | none | = | = | = |
| Painted layers | span.bg-black-900.self-center 0.0x0.0 bg #030302 r 3.35544e+07px; a.inline-flex.items-center 153.8x40.0 bg #030302 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = | span.bg-black-900.self-center 0.0x0.0 bg #030302 r 3.35544e+07px; a.inline-flex.items-center 153.8x40.0 bg #030302 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px auto #030302 @ 0.0607843 offset 1px | = |
| Ancestor paint | 2 up div.text-card-foreground.shadow-block bg #fcf9f7 shadow #000000 @ 0.01 0px 50px 40px 0px, #000000 @ 0.02 0px 50px 40px 0px, #000000 @ 0.05 0px 20px 40px 0px, #000000 @ 0.08 0px 3px 10px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-card-default.png`, `plan-card-hover.png`, `plan-card-focus-visible.png`, `plan-card-pressed.png`.

#### plan-price

Plan price. A 54px Untitled Serif price figure on a plan card.

Page: pricing. Selector: `serif price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 409.91 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSansFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #030302 |
| Text node | p.text-black-900.font-serif: UntitledSerifFont 54px/59.4px 400, #030302, ls -1.62px |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### team-card

Team card. The TEAM plan card — the shadow-block variant.

Page: pricing. Selector: `.shadow-block card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1400 x 1545.86 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | transparent |
| Box shadow | #000000 @ 0.01 0px 50px 40px 0px, #000000 @ 0.02 0px 50px 40px 0px, #000000 @ 0.05 0px 20px 40px 0px, #000000 @ 0.08 0px 3px 10px 0px |
| Outline | none |
| Font | UntitledSansFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #030302 |
| Text node | h1.h2.text-center: UntitledSerifFont 54px/59.4px 400, #030302, ls -1.08px |
| Transition | none |
| Icon | 170 x 34, colour #030302 |
| Painted layers | section.shadow-block.relative 1400.0x1545.9 r 24px shadow #000000 @ 0.01 0px 50px 40px 0px, #000000 @ 0.02 0px 50px 40px 0px, #000000 @ 0.05 0px 20px 40px 0px, #000000 @ 0.08 0px 3px 10px 0px; div.shadow-block.absolute 1400.0x1545.9 r 24px shadow #000000 @ 0.01 0px 50px 40px 0px, #000000 @ 0.02 0px 50px 40px 0px, #000000 @ 0.05 0px 20px 40px 0px, #000000 @ 0.08 0px 3px 10px 0px; div.from-blue-2.to-blue-1 1400.0x1545.9 image linear-gradient(in oklab, #9ed4ef 0px, #d1eef9 100%) r 4px; div.absolute.inset-0 1400.0x1545.9 image linear-gradient(in oklab, #000000 @ 0 0px, #ffffff 100%); div.glass-toggle-bg.glass-toggle-border 232.0x56.0 image linear-gradient(#75abc7 @ 0.24 60%, #ffffff @ 0.8 90%) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; div::before.glass-toggle-bg.glass-toggle-border 232pxx56px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 56px |
| How | at rest |

Crops: `team-card-default.png`.

#### faq-row

FAQ row. A pricing FAQ accordion row (shadcn-style ring on focus-visible); toggled locally.

Page: pricing. Selector: `FAQ accordion row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1000 x 57.2 | = | = | = |
| Padding | 16px 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #030302 @ 0.0607843 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | UntitledSerifFont 14px/20px 500 | = | = | = |
| Letter spacing | -1.38px | = | = | = |
| Colour | #030302 | = | = | = |
| Text node | div: UntitledSansFont 18px/25.2px 500, #030302, ls -0.36px | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #030302 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.focus-visible:border-ring.focus-visible:ring-ring/50 1000.0x57.2 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #030302 @ 0.0607843 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `faq-row-default.png`, `faq-row-hover.png`, `faq-row-focus-visible.png`, `faq-row-pressed.png`.

### Download

#### dl-h1

Download headline. "Get Craft for Free".

Page: download. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 386.56 x 59.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSerifFont 54px/59.4px 400 |
| Letter spacing | -1.08px |
| Colour | #030302 |
| Transition | none |
| How | at rest |

Crops: `dl-h1-default.png`.

#### dl-btn

Platform button. A platform download action; measured, never followed.

Page: download. Selector: `download platform button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 226.42 x 48 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 19.9566px 24.9295px 3.98916px, #000000 @ 0.04 0px 9.95664px 9.96748px -4.97832px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 19.8201px 24.7077px 3.95503px, #000000 @ 0.04 0px 9.8201px 9.86508px -4.91005px |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 1px | = |
| Font | UntitledSansFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #030302 | = | = | = |
| Text node | span: UntitledSansFont 16px/24px 500, #030302 | = | = | = |
| Transition | all 0.5s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 226.422px x 48px, absolute, bg #000000 @ 0 linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64), radius 24px | = | = | = |
| Painted layers | a.inline-flex.items-center 226.4x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px; a::before.inline-flex.items-center 226.422pxx48px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; div.glass-button-gradient-bg.absolute 226.4x48.0 image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.59 25%, #ffffff @ 0.6 50%, #ffffff @ 0.84 75%) | a.inline-flex.items-center 226.4x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 19.9566px 24.9295px 3.98916px, #000000 @ 0.04 0px 9.95664px 9.96748px -4.97832px; a::before.inline-flex.items-center 226.422pxx48px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; div.glass-button-gradient-bg.absolute 226.4x48.0 image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.59 25%, #ffffff @ 0.6 50%, #ffffff @ 0.84 75%) | a.inline-flex.items-center 226.4x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px outline 1px auto #030302 @ 0.0607843 offset 1px; a::before.inline-flex.items-center 226.422pxx48px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; div.glass-button-gradient-bg.absolute 226.4x48.0 image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.59 25%, #ffffff @ 0.6 50%, #ffffff @ 0.84 75%) | a.inline-flex.items-center 226.4x48.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 19.8201px 24.7077px 3.95503px, #000000 @ 0.04 0px 9.8201px 9.86508px -4.91005px; a::before.inline-flex.items-center 226.422pxx48px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; div.glass-button-gradient-bg.absolute 226.4x48.0 image linear-gradient(#ffffff @ 0.6, #ffffff @ 0.59 25%, #ffffff @ 0.6 50%, #ffffff @ 0.84 75%) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dl-btn-default.png`, `dl-btn-hover.png`, `dl-btn-focus-visible.png`, `dl-btn-pressed.png`.

### Product pages

#### imagine-h1

Imagine headline. The imagine page heading.

Page: imagine. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 832.33 x 118.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSerifFont 54px/59.4px 400 |
| Letter spacing | -1.08px |
| Colour | #030302 |
| Text node | span.italic: UntitledSerifFont 54px/59.4px 400, #030302, ls -1.08px |
| Transition | none |
| Ancestor paint | 3 up section.shadow-block.relative shadow #000000 @ 0.01 0px 50px 40px 0px, #000000 @ 0.02 0px 50px 40px 0px, #000000 @ 0.05 0px 20px 40px 0px, #000000 @ 0.08 0px 3px 10px 0px |
| How | at rest |

Crops: `imagine-h1-default.png`.

#### learn-h1

Learn headline. The learn page heading.

Page: learn. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 475.23 x 126 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSerifFont 70px/63px 400 |
| Letter spacing | -2px |
| Colour | #030302 |
| Transition | none |
| How | at rest |

Crops: `learn-h1-default.png`.

#### write-h1

Write headline. The write page heading.

Page: write. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 647.28 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSerifFont 66px/66px 400 |
| Letter spacing | -1.98px |
| Colour | #030302 |
| Transition | none |
| Ancestor paint | 2 up section.shadow-block.relative shadow #000000 @ 0.01 0px 50px 40px 0px, #000000 @ 0.02 0px 50px 40px 0px, #000000 @ 0.05 0px 20px 40px 0px, #000000 @ 0.08 0px 3px 10px 0px |
| How | at rest |

Crops: `write-h1-default.png`.

#### imagine-card

Template card. A template card on /imagine (Blog Publisher, Reading Tracker); measured, never followed.

Page: imagine. Selector: `imagine template card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 712 x 398.78 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 1px | = |
| Font | UntitledSansFont 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #030302 @ 0.75 | #030302 @ 0.9 | = | #030302 @ 0.9 |
| Text node | div.text-black-900.h3: UntitledSerifFont 46px/56.12px 400, #030302, ls -1.38px | = | = | = |
| Transition | opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #030302 | = | = | = |
| Painted layers | div.bg-card.text-card-foreground 712.0x398.8 bg #ffffff border T:1px solid #030302 @ 0.09 / R:1px solid #030302 @ 0.09 / B:1px solid #030302 @ 0.09 / L:1px solid #030302 @ 0.09 r 24px shadow #000000 @ 0.01 0px 50px 40px 0px, #000000 @ 0.02 0px 50px 40px 0px, #000000 @ 0.05 0px 20px 40px 0px, #000000 @ 0.08 0px 3px 10px 0px; div.relative.flex 339.0x372.8 bg #faf8f4 r 10px; div.relative.h-[24px] 24.0x24.0 r 6px shadow #000000 @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.relative.h-[24px] 24.0x24.0 r 6px shadow #000000 @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; img.z-1.max-h-full 158.9x199.0 r 13px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px outline 2px solid #030302 @ 0.05 offset 0px; img.justifty-self-start.z-2 188.2x210.3 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px outline 1px solid #030302 @ 0.05 offset 0px | = | a.group.block 712.0x398.8 outline 1px auto #030302 @ 0.0607843 offset 1px; div.bg-card.text-card-foreground 712.0x398.8 bg #ffffff border T:1px solid #030302 @ 0.09 / R:1px solid #030302 @ 0.09 / B:1px solid #030302 @ 0.09 / L:1px solid #030302 @ 0.09 r 24px shadow #000000 @ 0.01 0px 50px 40px 0px, #000000 @ 0.02 0px 50px 40px 0px, #000000 @ 0.05 0px 20px 40px 0px, #000000 @ 0.08 0px 3px 10px 0px; div.relative.flex 339.0x372.8 bg #faf8f4 r 10px; div.relative.h-[24px] 24.0x24.0 r 6px shadow #000000 @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.relative.h-[24px] 24.0x24.0 r 6px shadow #000000 @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; img.z-1.max-h-full 158.9x199.0 r 13px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px outline 2px solid #030302 @ 0.05 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `imagine-card-default.png`, `imagine-card-hover.png`, `imagine-card-focus-visible.png`, `imagine-card-pressed.png`.

### Footer

#### footer

Footer. The footer: link columns, the app badges and the legal row.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1408 x 562.5 |
| Padding | 0px 24px |
| Border | none |
| Radius | 24px |
| Background | #030302 |
| Box shadow | none |
| Outline | none |
| Font | UntitledSansFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #030302 |
| Text node | h4.text-white.text-[14px]: UntitledSansFont 14px/21px 500, #ffffff, ls 0.14px |
| Transition | none |
| Icon | 24 x 24, colour #ffffff, fill #000000 |
| Painted layers | footer.relative.flex 1408.0x562.5 bg #030302 r 24px; div.my-2.h-[0.5px] 160.0x0.5 bg #ffffff; span.absolute.bottom-0 0.0x1.0 bg #ffffff; span.absolute.bottom-0 0.0x1.0 bg #ffffff; span.absolute.bottom-0 0.0x1.0 bg #ffffff; span.absolute.bottom-0 0.0x1.0 bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link; measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114.28 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 1px | = |
| Font | UntitledSansFont 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-white 114.3x17.0 outline 1px auto #030302 @ 0.0607843 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.38 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 1px | = |
| Font | UntitledSansFont 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-white 69.4x17.0 outline 1px auto #030302 @ 0.0607843 offset 1px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 26px |
| Background | transparent |
| Background image | linear-gradient(#ffffff @ 0.4 10%, #ffffff @ 0.8) |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px |
| Backdrop filter | blur(4px) |
| Outline | none |
| Font | UntitledSansFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #030302 |
| Text node | span: UntitledSansFont 13px/19.5px 500, #ffffff |
| Transition | -webkit-backdrop-filter, backdrop-filter 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 100 x 20, colour #030302 |
| ::before | 342px x 52px, absolute, bg #000000 @ 0 linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64), radius 24px |
| Painted layers | header.fixed.right-0 342.0x52.0 image linear-gradient(#ffffff @ 0.4 10%, #ffffff @ 0.8) r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px; header::before.fixed.right-0 342pxx52px image linear-gradient(#ffffff @ 0.64 40%, #ffffff @ 0 75%, #ffffff @ 0 95%, #ffffff @ 0.64) r 24px; a.inline-flex.items-center 0.0x0.0 bg #030302 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; a.inline-flex.items-center 117.0x36.0 bg #030302 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; li.flex.h-full 310.0x0.0 bg #ffffff @ 0.5 r 16px; div.bg-black-200.h-px 286.0x0.4 bg #030302 @ 0.12 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header menu button that opens the nav overlay.

Page: home. Selector: `header menu button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 0px | = |
| Font | UntitledSansFont 15px/21px 400 | = | = | = |
| Letter spacing | -0.3px | = | = | = |
| Colour | #030302 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #030302 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.small.text-black-900 24.0x24.0 outline 1px auto #030302 @ 0.0607843 offset 0px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The opened nav overlay: the Product / Imagine / Pricing rows with Try Craft Free and Log in.

Page: home. Selector: `opened mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 617.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSansFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #030302 |
| Text node | p.small.text-black-900: UntitledSansFont 15px/21px 400, #030302, ls -0.3px |
| Transition | grid-template-rows, opacity, max-height 0.4s, 0.4s, 0.4s cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s, 0s |
| Opacity | 0.914931 |
| Icon | 24.76 x 24.76, colour #030302 |
| Painted layers | li.flex.h-full 310.0x304.6 bg #ffffff @ 0.5 r 16px; div.bg-black-200.h-px 286.0x0.4 bg #030302 @ 0.12; div.absolute.inset-0 286.0x22.6 bg #000000 @ 0 r 14px; div.h-2.w-2 8.0x8.0 bg #fde99b r 3.35544e+07px; div.absolute.inset-0 286.0x22.5 bg #000000 @ 0 r 14px; div.h-2.w-2 8.0x8.0 bg #b8caf5 r 3.35544e+07px |
| Ancestor paint | 2 up header.fixed.right-0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 12px 12px 2px, #000000 @ 0.06 0px 2px 4px -1px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile menu row. A row inside the opened nav overlay.

Page: home. Selector: `mobile menu row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 310 x 46 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 0px | = |
| Font | UntitledSansFont 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #030302 | = | = | = |
| Text node | p.small.text-black-900: UntitledSansFont 15px/21px 400, #030302, ls -0.3px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #030302 | = | = | = |
| Ancestor paint | 1 up li.flex.h-full bg #ffffff @ 0.5 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.w-full 310.0x46.0 outline 1px auto #030302 @ 0.0607843 offset 0px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 318 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSerifFont 48px/48px 400 |
| Letter spacing | -1.92px |
| Colour | #030302 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-download

Mobile download CTA. The black "Download for iOS" pill at the foot of the mobile menu; measured, never followed.

Page: home. Selector: `mobile menu Download for iOS`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 310 x 46 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #030302 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | = | = |
| Outline | none | = | 1px auto #030302 @ 0.0607843 offset 1px | = |
| Font | UntitledSansFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: UntitledSansFont 16px/24px 500, #ffffff | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 310.0x46.0 bg #030302 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | a.inline-flex.items-center 310.0x46.0 bg #030302 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px outline 1px auto #030302 @ 0.0607843 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-download-default.png`, `m-download-hover.png`, `m-download-focus-visible.png`, `m-download-pressed.png`.

## Transitions declared in the readable stylesheets

craft.do serves its Next.js sheets same-origin; this list covers the transition rules the page itself exposes, and the per-state Transition rows above are the computed values the page paints.

- home: `0.5s ease-in-out`, `background-position 0.5s`, `none`, `transform 0.2s linear`

- pricing: `0.5s ease-in-out`, `background-position 0.5s`, `none`
