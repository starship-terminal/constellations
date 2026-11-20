# Descript component measurements

Computed styles read from www.descript.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — home, /pricing, /video-editing, /templates, /customers/saastr, /underlord and the web.descript.com sign-in card, and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and navigation

#### mkt-header

Site header. The top bar: Descript wordmark, nav (Features / Pricing / Contact sales), Sign in and the Sign up button.

Page: home. Selector: `nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1400 x 102.08 |
| Padding | 24px |
| Border | none |
| Radius | 12px |
| Background | #fff7fa |
| Box shadow | none |
| Backdrop filter | blur(16px) |
| Outline | none |
| Font | booton 16px/24px 600 |
| Letter spacing | normal |
| Colour | #26171d |
| Text node | span: booton 16px/24px 600, #26171d |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -700, 0) |
| Painted layers | nav.p-6.w-full 1400.0x102.1 bg #fff7fa r 12px; div.flex.flex-col 0.0x0.0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #583f4a @ 0.14 0px 16px 38px 0px, #583f4a @ 0.12 0px 120px 136px 0px; div.bg-[var(--Neutral-0)].min-[1200px]:bg-[var(--Neutral-0)] 0.0x0.0 bg #fff7fa; div.relative.bg-[var(--Neutral-0)] 0.0x0.0 bg #f1eaed; a.p-4.border 0.0x0.0 border T:1px solid #b8a5ad / R:1px solid #b8a5ad / B:1px solid #b8a5ad / L:1px solid #b8a5ad r 4px; a.p-4.border 0.0x0.0 border T:1px solid #b8a5ad / R:1px solid #b8a5ad / B:1px solid #b8a5ad / L:1px solid #b8a5ad r 4px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Descript wordmark at the left of the header.

Page: home. Selector: `header logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 98 x 23.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | booton 16px/24px 600 |
| Letter spacing | normal |
| Colour | #26171d |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-link

Nav link. A header nav link ("Pricing"); measured, never followed.

Page: home. Selector: `nav Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f1eaed | = | #f1eaed |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | booton 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #26171d | = | = | = |
| Text node | span: booton 16px/24px 600, #26171d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.gap-2 76.0x32.0 bg #f1eaed r 4px | a.flex.gap-2 76.0x32.0 r 4px outline 1px auto #101010 offset 1px | a.flex.gap-2 76.0x32.0 bg #f1eaed r 4px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### signin-link

Sign in. The header "Sign in" link; measured, never followed (it leads to the auth card measured on the auth page).

Page: home. Selector: `Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f1eaed | = | #f1eaed |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | booton 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #26171d | = | = | = |
| Text node | span: booton 16px/24px 600, #26171d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.gap-2 73.0x32.0 bg #f1eaed r 4px | a.flex.gap-2 73.0x32.0 r 4px outline 1px auto #101010 offset 1px | a.flex.gap-2 73.0x32.0 bg #f1eaed r 4px |

Crops: `signin-link-default.png`, `signin-link-hover.png`, `signin-link-focus-visible.png`, `signin-link-pressed.png`.

#### signup-cta

Sign up button. The maroon "Sign up" button in the header; measured, never followed.

Page: home. Selector: `Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 108 x 54.08 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #772a4d | #5b142e | = | #5b142e |
| Box shadow | #000000 @ 0.16 0px 2px 4px 0px | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | booton 16px/22.08px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.bg-[var(--Maroon-700)].hover:bg-[var(--Maroon-800)] 108.0x54.1 bg #772a4d r 12px shadow #000000 @ 0.16 0px 2px 4px 0px | a.bg-[var(--Maroon-700)].hover:bg-[var(--Maroon-800)] 108.0x54.1 bg #5b142e r 12px shadow #000000 @ 0.16 0px 2px 4px 0px | a.bg-[var(--Maroon-700)].hover:bg-[var(--Maroon-800)] 108.0x54.1 bg #772a4d r 12px shadow #000000 @ 0.16 0px 2px 4px 0px outline 1px auto #101010 offset 1px | a.bg-[var(--Maroon-700)].hover:bg-[var(--Maroon-800)] 108.0x54.1 bg #5b142e r 12px shadow #000000 @ 0.16 0px 2px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-cta-default.png`, `signup-cta-hover.png`, `signup-cta-focus-visible.png`, `signup-cta-pressed.png`.

### Home

#### hero-eyebrow

Eyebrow. The small uppercase red eyebrow above the display headline ("AI VIDEO EDITOR").

Page: home. Selector: `h1 eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 892 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | brett 18px/18px 400 |
| Letter spacing | 0.72px |
| Colour | #f73b3b |
| Transition | none |
| How | at rest |

Crops: `hero-eyebrow-default.png`.

#### hero-display

Display headline. The gamuthDisplay display headline on the home hero.

Page: home. Selector: `hero h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 892 x 210 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 88px/normal 400 |
| Letter spacing | normal |
| Colour | #fff8f4 |
| Transition | none |
| How | at rest |

Crops: `hero-display-default.png`.

#### flow-tabs

Workflow tabs. The Record / Edit / Refine / Share / Multiply workflow tab strip in "The whole workflow, right here".

Page: home. Selector: `workflow tab strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 610 x 44 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | booton 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | button.shrink-0.flex: booton 16px/16px 600, #fff7fd |
| Transition | none |
| Painted layers | button.shrink-0.flex 121.0x44.0 bg #5b142e r 8px; span.absolute.inset-0 16.0x16.0 bg #d597bf; span.absolute.inset-0 16.0x16.0 bg #d597bf; span.absolute.inset-0 16.0x16.0 bg #d597bf; span.absolute.inset-0 16.0x16.0 bg #d597bf; span.absolute.inset-0 16.0x16.0 bg #d597bf |
| How | at rest |

Crops: `flow-tabs-default.png`.

#### flow-tab

Workflow tab. A workflow tab ("Edit"); its opened state is a local tab selection, never a navigation.

Page: home. Selector: `workflow tab`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 97 x 44 | = | = | = | 98 x 44 |
| Padding | 14px 24px 14px 16px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #26171d | = | #26171d | #5b142e |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | booton 16px/16px 400 | = | = | = | booton 16px/16px 600 |
| Letter spacing | normal | = | = | = | = |
| Colour | #c4b5bb | = | = | = | #fff7fd |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | span.absolute.inset-0 16.0x16.0 bg #d597bf | button.shrink-0.flex 97.0x44.0 bg #26171d r 8px; span.absolute.inset-0 16.0x16.0 bg #d597bf | button.shrink-0.flex 97.0x44.0 r 8px outline 1px auto #101010 offset 0px; span.absolute.inset-0 16.0x16.0 bg #d597bf | button.shrink-0.flex 97.0x44.0 bg #26171d r 8px; span.absolute.inset-0 16.0x16.0 bg #d597bf | button.shrink-0.flex 98.0x44.0 bg #5b142e r 8px; span.absolute.inset-0 16.0x16.0 bg #d597bf |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `flow-tab-default.png`, `flow-tab-hover.png`, `flow-tab-focus-visible.png`, `flow-tab-pressed.png`, `flow-tab-opened.png`.

#### flow-tab-rest

Workflow tab (rest). A second workflow tab measured at rest for the unselected style.

Page: home. Selector: `workflow tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 133 x 44 | = | = | = |
| Padding | 14px 24px 14px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #26171d | = | #26171d |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | booton 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #c4b5bb | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.absolute.inset-0 16.0x16.0 bg #d597bf | button.shrink-0.flex 133.0x44.0 bg #26171d r 8px; span.absolute.inset-0 16.0x16.0 bg #d597bf | button.shrink-0.flex 133.0x44.0 r 8px outline 1px auto #101010 offset 0px; span.absolute.inset-0 16.0x16.0 bg #d597bf | button.shrink-0.flex 133.0x44.0 bg #26171d r 8px; span.absolute.inset-0 16.0x16.0 bg #d597bf |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `flow-tab-rest-default.png`, `flow-tab-rest-hover.png`, `flow-tab-rest-focus-visible.png`, `flow-tab-rest-pressed.png`.

#### section-h2

Section heading. A home section heading ("The whole workflow, right here").

Page: home. Selector: `section h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 61.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 56px/61.6px 700 |
| Letter spacing | normal |
| Colour | #fff7fa |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Footer

#### site-footer

Site footer. The sitemap footer (product links, resources, company).

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1145.81 |
| Padding | 86px 64px 104px 64px |
| Border | none |
| Radius | 0px |
| Background | #110a0d |
| Box shadow | none |
| Outline | none |
| Font | booton 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | p.text-[18px].leading-[1.4]: booton 18px/25.2px 400, #d1c7cb |
| Transition | none |
| Painted layers | footer.w-full.bg-[var(--Neutral-950)] 1440.0x1145.8 bg #110a0d; div.bg-[var(--Neutral-900)].rounded-[8px] 916.0x307.0 bg #26171d r 8px |
| How | at rest |

Crops: `site-footer-default.png`.

### Pricing

#### pr-eyebrow

Page eyebrow. The uppercase "PRICING" eyebrow heading.

Page: pricing. Selector: `pricing h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1396 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | brett 18px/18px 400 |
| Letter spacing | 0.72px |
| Colour | #f73b3b |
| Transition | none |
| How | at rest |

Crops: `pr-eyebrow-default.png`.

#### pr-display

Pricing headline. The display heading "A plan for whatever you create".

Page: pricing. Selector: `pricing h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1396 x 61.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 56px/61.6px 400 |
| Letter spacing | normal |
| Colour | #390a1a |
| Transition | none |
| How | at rest |

Crops: `pr-display-default.png`.

#### pr-toggle

Billing toggle. The Monthly / Annual billing switch above the plan cards.

Page: pricing. Selector: `billing toggle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 228 x 50 |
| Padding | 8px |
| Border | none |
| Radius | 42px |
| Background | #f1eaed |
| Box shadow | none |
| Outline | none |
| Font | booton 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | span: booton 16px/24px 400, #1a1a1a |
| Transition | none |
| Painted layers | div.relative.mx-auto 228.0x50.0 bg #f1eaed r 42px; div.absolute.inset-y-2 106.0x34.0 bg #fffafc r 28px |
| How | at rest |

Crops: `pr-toggle-default.png`.

#### pr-toggle-month

Monthly option. The "Monthly" toggle option; measured, the Annual side is toggled below.

Page: pricing. Selector: `Monthly`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106 x 34 | = | = | = |
| Padding | 5px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | booton 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Text node | span: booton 16px/24px 400, #1a1a1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.relative.mx-auto bg #f1eaed | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative.z-20 106.0x34.0 outline 1px auto #101010 offset 0px | = |

Crops: `pr-toggle-month-default.png`, `pr-toggle-month-hover.png`, `pr-toggle-month-focus-visible.png`, `pr-toggle-month-pressed.png`.

#### pr-toggle-annual

Annual option. The "Annual" toggle option — a local billing switch; its opened state is the selected-annual style, never a purchase.

Page: pricing. Selector: `Annual`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 106 x 34 | = | = | = | = |
| Padding | 5px 20px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | booton 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1a1a1a | = | = | = | = |
| Text node | span.font-semibold: booton 16px/24px 600, #1a1a1a | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Ancestor paint | 1 up div.relative.mx-auto bg #f1eaed | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.relative.z-20 106.0x34.0 outline 1px auto #101010 offset 0px | = | = |

Crops: `pr-toggle-annual-default.png`, `pr-toggle-annual-hover.png`, `pr-toggle-annual-focus-visible.png`, `pr-toggle-annual-pressed.png`, `pr-toggle-annual-opened.png`.

#### pr-card

Plan card. A pricing plan card (name, price, feature list, CTA).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 284 x 708.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | booton 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | a.flex.w-full: booton 16px/24px 600, #fff7fa |
| Transition | none |
| Painted layers | a.flex.w-full 284.0x56.0 bg #390a1a r 12px |
| Ancestor paint | 1 up div.relative.row-span-2 bg #f1eaed |
| How | at rest |

Crops: `pr-card-default.png`.

#### pr-cta

Plan CTA. A plan card’s CTA; measured, never followed (it starts signup/checkout).

Page: pricing. Selector: `plan CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 284 x 56 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #390a1a | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | booton 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fff7fa | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.w-full 284.0x56.0 bg #390a1a r 12px | = | a.flex.w-full 284.0x56.0 bg #390a1a r 12px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pr-cta-default.png`, `pr-cta-hover.png`, `pr-cta-focus-visible.png`, `pr-cta-pressed.png`.

#### pr-compare-h2

Comparison heading. The "What’s the difference?" heading over the plan comparison table.

Page: pricing. Selector: `compare h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1400 x 61.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 56px/61.6px 400 |
| Letter spacing | normal |
| Colour | #390a1a |
| Transition | none |
| How | at rest |

Crops: `pr-compare-h2-default.png`.

#### pr-faq

FAQ heading. The "Frequently asked questions" section heading.

Page: pricing. Selector: `faq h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 651.97 x 123.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 56px/61.6px 400 |
| Letter spacing | normal |
| Colour | #190308 |
| Transition | none |
| How | at rest |

Crops: `pr-faq-default.png`.

### Video editing page

#### vid-h1

Page headline. The "All-in-one video editing" display heading.

Page: video. Selector: `video h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 500 x 158.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 72px/79.2px 600 |
| Letter spacing | normal |
| Colour | #390a1a |
| Transition | none |
| How | at rest |

Crops: `vid-h1-default.png`.

#### vid-cta

Page CTA. The video page hero CTA; measured, never followed.

Page: video. Selector: `video CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 222 x 56 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #f73b3b | #b81b1e | = | #8f0c10 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | booton 16px/32px 570 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fff7fd | = | = | = |
| Text node | span.font-semibold.leading-[1.5]: booton 16px/24px 600, #fff7fd | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.sm:inline-flex 222.0x56.0 bg #f73b3b r 12px | a.flex.sm:inline-flex 222.0x56.0 bg #b81b1e r 12px | a.flex.sm:inline-flex 222.0x56.0 bg #f73b3b r 12px outline 1px auto #101010 offset 1px | a.flex.sm:inline-flex 222.0x56.0 bg #8f0c10 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `vid-cta-default.png`, `vid-cta-hover.png`, `vid-cta-focus-visible.png`, `vid-cta-pressed.png`.

#### vid-h2

Section heading. A feature section heading on the video page.

Page: video. Selector: `video h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1006 x 61.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 56px/61.6px 400 |
| Letter spacing | normal |
| Colour | #fff8f4 |
| Transition | none |
| How | at rest |

Crops: `vid-h2-default.png`.

### Templates gallery

#### tpl-h1

Gallery heading. The templates gallery heading.

Page: templates. Selector: `templates h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 158.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 72px/79.2px 600 |
| Letter spacing | normal |
| Colour | #3f2a32 |
| Transition | none |
| How | at rest |

Crops: `tpl-h1-default.png`.

#### tpl-card

Template card. A template card in the gallery grid (thumbnail, name, category); the overlay link was measured, never followed.

Page: templates. Selector: `template card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 338 x 382.56 |
| Padding | 0px |
| Border | 1px solid #b8a5ad |
| Radius | 8px |
| Background | #f1eaed |
| Box shadow | none |
| Outline | none |
| Font | booton 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | p.text-gray-500.text-sm: booton 14px/20px 400, #6b7280 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.group.relative 338.0x382.6 bg #f1eaed border T:1px solid #b8a5ad / R:1px solid #b8a5ad / B:1px solid #b8a5ad / L:1px solid #b8a5ad r 8px; div.relative.w-full 336.0x189.0 bg #f3f4f6; div.relative.w-full 336.0x189.0 bg #f3f4f6; div.absolute.inset-0 336.0x189.0 bg #e5e7eb; button.relative.z-10 123.0x40.4 bg #fff7fa border T:1px solid #b8a5ad / R:1px solid #b8a5ad / B:1px solid #b8a5ad / L:1px solid #b8a5ad r 8px |
| How | at rest |

Crops: `tpl-card-default.png`.

#### tpl-link

Template link. A template card’s overlay link; measured, never followed.

Page: templates. Selector: `template overlay link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 336 x 380.56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #f73b3b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | booton 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.group.relative bg #f1eaed | 1 up div.group.relative bg #e4dde0 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.absolute.inset-0 336.0x380.6 r 8px shadow #ffffff 0px 0px 0px 0px inset, #f73b3b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | = |

Crops: `tpl-link-default.png`, `tpl-link-hover.png`, `tpl-link-focus-visible.png`, `tpl-link-pressed.png`.

### Customer story

#### st-h1

Story headline. The SaaStr customer story headline.

Page: story. Selector: `story h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 604 x 246.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 56px/61.6px 400 |
| Letter spacing | normal |
| Colour | #390a1a |
| Transition | none |
| How | at rest |

Crops: `st-h1-default.png`.

#### st-prose

Story prose. Body copy in the customer story.

Page: story. Selector: `story p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 600 x 216 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | booton 18px/27px 400 |
| Letter spacing | normal |
| Colour | #fff7fa |
| Transition | none |
| How | at rest |

Crops: `st-prose-default.png`.

#### st-cta

Story CTA. The "Request a demo" CTA in the customer story; measured, never followed.

Page: story. Selector: `Request a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 191 x 56 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #f73b3b | #b81b1e | = | #8f0c10 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | booton 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fff7fd | = | = | = |
| Text node | span.font-semibold.leading-[1.5]: booton 16px/24px 600, #fff7fd | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.sm:inline-flex 191.0x56.0 bg #f73b3b r 12px | a.flex.sm:inline-flex 191.0x56.0 bg #b81b1e r 12px | a.flex.sm:inline-flex 191.0x56.0 bg #f73b3b r 12px outline 1px auto #101010 offset 1px | a.flex.sm:inline-flex 191.0x56.0 bg #8f0c10 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-cta-default.png`, `st-cta-hover.png`, `st-cta-focus-visible.png`, `st-cta-pressed.png`.

### Underlord

#### ul-h1

Underlord headline. The Underlord AI co-editor page headline.

Page: underlord. Selector: `underlord h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 158.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 72px/79.2px 600 |
| Letter spacing | normal |
| Colour | #390a1a |
| Transition | none |
| How | at rest |

Crops: `ul-h1-default.png`.

#### ul-cta

Underlord CTA. The Underlord page CTA; measured, never followed.

Page: underlord. Selector: `underlord CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 222 x 56 | = | = | = |
| Padding | 16px 32px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #f73b3b | #b81b1e | = | #8f0c10 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | booton 16px/32px 570 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fff7fd | = | = | = |
| Text node | span.font-semibold.leading-[1.5]: booton 16px/24px 600, #fff7fd | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.sm:inline-flex 222.0x56.0 bg #f73b3b r 12px | a.flex.sm:inline-flex 222.0x56.0 bg #b81b1e r 12px | a.flex.sm:inline-flex 222.0x56.0 bg #f73b3b r 12px outline 1px auto #101010 offset 1px | a.flex.sm:inline-flex 222.0x56.0 bg #8f0c10 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ul-cta-default.png`, `ul-cta-hover.png`, `ul-cta-focus-visible.png`, `ul-cta-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone top bar: wordmark and sign-in/sign-up actions.

Page: mobile. Selector: `mobile nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 84 |
| Padding | 84px 18.75px 0px 18.75px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | booton 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #343434 |
| Text node | a.bg-[var(--Maroon-750)].hover:bg-[var(--Maroon-800)]: booton 15px/22.5px 600, #ffffff |
| Transition | none |
| Painted layers | ul.flex.gap-6 390.0x84.5 bg #fff7fa border B:2px solid #f1eaed; a.bg-[var(--Maroon-750)].hover:bg-[var(--Maroon-800)] 104.0x52.5 bg #651a39 r 11.25px shadow #000000 @ 0.16 0px 2px 4px 0px; div.h-[calc(100dvh-84px)].sm:h-[calc(100dvh-90px)] 0.0x0.0 bg #fff7fa; a.mt-4.bg-[var(--Maroon-750)] 0.0x0.0 bg #651a39 r 11.25px shadow #000000 @ 0.16 0px 2px 4px 0px |
| Ancestor paint | 1 up section.lg:h-[92px].relative bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-eyebrow

Mobile eyebrow. The phone hero eyebrow heading.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | brett 18px/18px 400 |
| Letter spacing | 0.72px |
| Colour | #f73b3b |
| Transition | none |
| How | at rest |

Crops: `m-eyebrow-default.png`.

#### m-display

Mobile display. The phone display headline.

Page: mobile. Selector: `mobile h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 171 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gamuthDisplay 48px/normal 400 |
| Letter spacing | normal |
| Colour | #fff8f4 |
| Transition | none |
| How | at rest |

Crops: `m-display-default.png`.

#### m-footer

Mobile footer. The phone footer.

Page: mobile. Selector: `mobile footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 1858.69 |
| Padding | 45px 18.75px 52.5px 18.75px |
| Border | none |
| Radius | 0px |
| Background | #110a0d |
| Box shadow | none |
| Outline | none |
| Font | booton 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #1a1a1a |
| Text node | p.text-[18px].leading-[1.4]: booton 18px/25.2px 400, #d1c7cb |
| Transition | none |
| Painted layers | footer.w-full.bg-[var(--Neutral-950)] 390.0x1858.7 bg #110a0d; div.bg-[var(--Neutral-900)].rounded-[8px] 352.5x629.3 bg #26171d r 8px |
| How | at rest |

Crops: `m-footer-default.png`.

#### mp-toggle

Mobile billing toggle. The Annual option of the billing toggle on the phone.

Page: mobile-pricing. Selector: `mobile Annual`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98.5 x 32.5 | = | = | = |
| Padding | 5px 18.75px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | booton 15px/22.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a1a1a | = | = | = |
| Text node | span.font-semibold: booton 15px/22.5px 600, #1a1a1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.relative.mx-auto bg #f1eaed | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative.z-20 98.5x32.5 outline 1px auto #e59700 offset 0px | = |

Crops: `mp-toggle-default.png`, `mp-toggle-hover.png`, `mp-toggle-focus-visible.png`, `mp-toggle-pressed.png`.

#### mp-cta

Mobile plan CTA. A plan CTA on the phone pricing page; measured, never followed.

Page: mobile-pricing. Selector: `mobile plan CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 307.5 x 52.5 | = | = | = |
| Padding | 15px 30px | = | = | = |
| Border | none | = | = | = |
| Radius | 11.25px | = | = | = |
| Background | #390a1a | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | booton 15px/22.5px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fff7fa | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.w-full 307.5x52.5 bg #390a1a r 11.25px | = | a.flex.w-full 307.5x52.5 bg #390a1a r 11.25px outline 1px auto #e59700 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mp-cta-default.png`, `mp-cta-hover.png`, `mp-cta-focus-visible.png`, `mp-cta-pressed.png`.

### Auth card

#### au-card

Auth card. The sign-in card on web.descript.com/authenticate (SSO buttons, email field, terms links).

Page: auth. Selector: `auth card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #3f2a32 |
| Text node | span: Booton VF 15.75px/22.5px 500, #26171d |
| Transition | none |
| Icon | 20 x 20, colour #26171d |
| Painted layers | div.stack.h-screen 1440.0x900.0 bg #f4f1f0; div.rounded-xl.p-2 400.0x460.7 bg #fdfcfc border T:1px solid #583f4a @ 0.1 / R:1px solid #583f4a @ 0.1 / B:1px solid #583f4a @ 0.1 / L:1px solid #583f4a @ 0.1 r 12px shadow #26171d @ 0.12 0px 16px 38px 0px, #26171d @ 0.12 0px 120px 136px 0px; div.text-brand-logo-mark.icon-token 40.0x40.0 bg #f73b3b; div.text-brand-logo-type.icon-token 207.0x207.0 bg #651a39; div.MainContainer_module_container__d1278a0c.Root_module_root__870c11a1 382.0x360.7 bg #fdfcfc border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 24px; button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #110a0d @ 0.45 / R:1px solid #110a0d @ 0.45 / B:1px solid #110a0d @ 0.45 / L:1px solid #110a0d @ 0.45 r 8px shadow #26171d 0px 0px 0px 0px |
| Ancestor paint | 1 up div bg #ffffff |
| How | at rest |

Crops: `au-card-default.png`.

#### au-google

Google SSO. "Continue with Google" — the outline SSO button; measured, never pressed.

Page: auth. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 308 x 40.48 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #110a0d @ 0.45 | = | 1px solid #3434ab | = |
| Radius | 8px | = | = | = |
| Background | #fdfcfc | #f4f1f0 | = | #f4f1f0 |
| Box shadow | #26171d 0px 0px 0px 0px | = | #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Booton VF 15.75px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #26171d | = | = | = |
| Text node | span: Booton VF 15.75px/22.5px 500, #26171d | = | = | = |
| Transition | background-color, border-color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #26171d | = | = | = |
| Painted layers | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #110a0d @ 0.45 / R:1px solid #110a0d @ 0.45 / B:1px solid #110a0d @ 0.45 / L:1px solid #110a0d @ 0.45 r 8px shadow #26171d 0px 0px 0px 0px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #f4f1f0 border T:1px solid #110a0d @ 0.45 / R:1px solid #110a0d @ 0.45 / B:1px solid #110a0d @ 0.45 / L:1px solid #110a0d @ 0.45 r 8px shadow #26171d 0px 0px 0px 0px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #3434ab / R:1px solid #3434ab / B:1px solid #3434ab / L:1px solid #3434ab r 8px shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #f4f1f0 border T:1px solid #110a0d @ 0.45 / R:1px solid #110a0d @ 0.45 / B:1px solid #110a0d @ 0.45 / L:1px solid #110a0d @ 0.45 r 8px shadow #26171d 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `au-google-default.png`, `au-google-hover.png`, `au-google-focus-visible.png`, `au-google-pressed.png`.

#### au-sso

SSO button. "Use single sign-on" — the second outline auth option; measured, never pressed.

Page: auth. Selector: `Use single sign-on`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 308 x 40.48 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #110a0d @ 0.45 | = | 1px solid #3434ab | = |
| Radius | 8px | = | = | = |
| Background | #fdfcfc | #f4f1f0 | = | #f4f1f0 |
| Box shadow | #26171d 0px 0px 0px 0px | = | #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Booton VF 15.75px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #26171d | = | = | = |
| Text node | span: Booton VF 15.75px/22.5px 500, #26171d | = | = | = |
| Transition | background-color, border-color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #110a0d @ 0.45 / R:1px solid #110a0d @ 0.45 / B:1px solid #110a0d @ 0.45 / L:1px solid #110a0d @ 0.45 r 8px shadow #26171d 0px 0px 0px 0px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #f4f1f0 border T:1px solid #110a0d @ 0.45 / R:1px solid #110a0d @ 0.45 / B:1px solid #110a0d @ 0.45 / L:1px solid #110a0d @ 0.45 r 8px shadow #26171d 0px 0px 0px 0px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #3434ab / R:1px solid #3434ab / B:1px solid #3434ab / L:1px solid #3434ab r 8px shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #f4f1f0 border T:1px solid #110a0d @ 0.45 / R:1px solid #110a0d @ 0.45 / B:1px solid #110a0d @ 0.45 / L:1px solid #110a0d @ 0.45 r 8px shadow #26171d 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `au-sso-default.png`, `au-sso-hover.png`, `au-sso-focus-visible.png`, `au-sso-pressed.png`.

#### au-email

Email field. The auth email input; focused and typed into then cleared, never submitted.

Page: auth. Selector: `auth email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 308 x 40.48 | = | = |
| Padding | 8px 12px | = | = |
| Border | 1px solid #3f2a32 @ 0.16 | 1px solid #3434ab | 1px solid #3434ab |
| Radius | 8px | = | = |
| Background | #fdfcfc | = | = |
| Box shadow | #26171d 0px 0px 0px 0px | #26171d 0px 0px 0px 0px, #3434ab @ 0.5 0px 0px 0px 3px | #26171d 0px 0px 0px 0px, #3434ab @ 0.5 0px 0px 0px 3px |
| Outline | none | = | = |
| Font | Booton VF 15.75px/22.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #26171d | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #16050c @ 0.6, opacity 1 | = | = |
| Painted layers | input.Input_module_input__a0aad2f4.inputBase_module_inputBase__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #3f2a32 @ 0.16 / R:1px solid #3f2a32 @ 0.16 / B:1px solid #3f2a32 @ 0.16 / L:1px solid #3f2a32 @ 0.16 r 8px shadow #26171d 0px 0px 0px 0px | input.Input_module_input__a0aad2f4.inputBase_module_inputBase__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #3434ab / R:1px solid #3434ab / B:1px solid #3434ab / L:1px solid #3434ab r 8px shadow #26171d 0px 0px 0px 0px, #3434ab @ 0.5 0px 0px 0px 3px | input.Input_module_input__a0aad2f4.inputBase_module_inputBase__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #3434ab / R:1px solid #3434ab / B:1px solid #3434ab / L:1px solid #3434ab r 8px shadow #26171d 0px 0px 0px 0px, #3434ab @ 0.5 0px 0px 0px 3px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `au-email-default.png`, `au-email-focused.png`, `au-email-filled.png`.

#### au-email-btn

Email button. "Continue with email" — the primary auth button; measured, never pressed.

Page: auth. Selector: `Continue with email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 308 x 40.48 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #3f2a32 | 1px solid #3f2a32 @ 0.9 | 1px solid #3434ab | 1px solid #3f2a32 @ 0.9 |
| Radius | 8px | = | = | = |
| Background | #3f2a32 | #3f2a32 @ 0.9 | = | #3f2a32 @ 0.9 |
| Box shadow | #ffffff 0px 0px 0px 0px | = | #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Booton VF 15.75px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Booton VF 15.75px/22.5px 500, #ffffff | = | = | = |
| Transition | background-color, border-color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #3f2a32 border T:1px solid #3f2a32 / R:1px solid #3f2a32 / B:1px solid #3f2a32 / L:1px solid #3f2a32 r 8px shadow #ffffff 0px 0px 0px 0px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #3f2a32 @ 0.9 border T:1px solid #3f2a32 @ 0.9 / R:1px solid #3f2a32 @ 0.9 / B:1px solid #3f2a32 @ 0.9 / L:1px solid #3f2a32 @ 0.9 r 8px shadow #ffffff 0px 0px 0px 0px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #3f2a32 border T:1px solid #3434ab / R:1px solid #3434ab / B:1px solid #3434ab / L:1px solid #3434ab r 8px shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #3f2a32 @ 0.9 border T:1px solid #3f2a32 @ 0.9 / R:1px solid #3f2a32 @ 0.9 / B:1px solid #3f2a32 @ 0.9 / L:1px solid #3f2a32 @ 0.9 r 8px shadow #ffffff 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `au-email-btn-default.png`, `au-email-btn-hover.png`, `au-email-btn-focus-visible.png`, `au-email-btn-pressed.png`.

#### au-password

Password link. "Use a password instead" — the ghost fallback; measured, never pressed.

Page: auth. Selector: `Use a password instead`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 308 x 40.48 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #fdfcfc | = | 1px solid #3434ab | = |
| Radius | 8px | = | = | = |
| Background | #fdfcfc | #f4f1f0 | = | #f4f1f0 |
| Box shadow | none | = | #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Booton VF 15.75px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #26171d | = | = | = |
| Text node | span: Booton VF 15.75px/22.5px 500, #26171d | = | = | = |
| Transition | background-color, border-color 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #fdfcfc / R:1px solid #fdfcfc / B:1px solid #fdfcfc / L:1px solid #fdfcfc r 8px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #f4f1f0 border T:1px solid #fdfcfc / R:1px solid #fdfcfc / B:1px solid #fdfcfc / L:1px solid #fdfcfc r 8px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #fdfcfc border T:1px solid #3434ab / R:1px solid #3434ab / B:1px solid #3434ab / L:1px solid #3434ab r 8px shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | button.Button_module_button__fba1165e.inputBase_module_focusRing__06c14ae4 308.0x40.5 bg #f4f1f0 border T:1px solid #fdfcfc / R:1px solid #fdfcfc / B:1px solid #fdfcfc / L:1px solid #fdfcfc r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `au-password-default.png`, `au-password-hover.png`, `au-password-focus-visible.png`, `au-password-pressed.png`.

#### au-terms

Terms link. The "Terms of Service" link under the auth card; measured, never followed.

Page: auth. Selector: `Terms of Service`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.03 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 6px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | Booton VF 12px/16px 475 | = | = | = |
| Letter spacing | 0.0012px | = | = | = |
| Colour | #16050c @ 0.6 | = | = | = |
| Transition | none | = | = | = |
| Cursor | url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='27' height='32' fill='none'%3E%3Cg filter='url(…)'%3E%3Cpath fill='%23fff' d='M17.006 15.975c-.685 0-1.24.447-1.24.998v1.757l-1.29-5.493a1 1 0 0 0-.136-.348c-.169-.254-.572-.701-1.262-.562-.883.177-.875 1.035-.87 1.153l.002.026c.03.328.094 1.364.38 2.913.29 1.57.775 3.073.775 4.216l-1.45-1.438c-.487-.483-1.118-.928-1.774-.738-.172.05-.339.135-.478.271a1.3 1.3 0 0 0-.346.7c-.093.514.155 1.007.448 1.438.601.888 1.67 2.469 2.263 3.372a6.8 6.8 0 0 0 1.762 1.807.55.55 0 0 1 .241.447v.958c0 .137.111.25.248.25h3.47s.215-1.498.972-1.498 1.011 1.497 1.011 1.497h1.488a.25.25 0 0 0 .248-.25v-1.833c0-.27.072-.534.209-.766l.84-1.42c.322-.542.51-1.153.551-1.783l.093-1.433.042-1.204-.032-.75a1.2 1.2 0 0 0-.092-.453c-.114-.24-.369-.591-.875-.591a1.14 1.14 0 0 0-.653.183c-.281.19-.35.555-.395.893l-.058.436-.124-1.18c-.024-.22-.07-.443-.207-.617a1.3 1.3 0 0 0-1.06-.514c-.465 0-.794.202-1.006.403-.241.228-.317.567-.336.9l-.057 1.008-.063-1.757c0-.551-.555-.998-1.24-.998'/%3E%3Cpath fill='%23000' fill-rule='evenodd' d='M14.587 12.722c-.191-.288-.698-.865-1.568-.69-.55.111-.842.447-.982.774a1.6 1.6 0 0 0-.126.687l.016.19c.036.438.117 1.415.37 2.79.101.549.227 1.094.347 1.61l.152.668c.087.395.16.764.21 1.106l-.882-.874c-.254-.252-.56-.51-.902-.677-.345-.17-.745-.257-1.164-.135-.207.06-.421.166-.603.344-.26.256-.379.579-.43.86-.117.64.197 1.223.494 1.662.602.887 1.67 2.467 2.261 3.367.643.98 1.44 1.61 1.84 1.889.075.052.114.13.114.2v.958c0 .303.244.549.545.549h3.47c.148 0 .274-.11.295-.257v-.002l.002-.01.007-.042a3.4 3.4 0 0 1 .175-.626c.067-.171.15-.321.242-.424.09-.1.17-.136.251-.136s.166.038.26.139c.097.104.183.256.256.427a3.4 3.4 0 0 1 .2.67l.002.01v.002a.3.3 0 0 0 .293.249h1.488a.547.547 0 0 0 .545-.549v-1.833c0-.216.058-.428.168-.613l.84-1.42c.345-.584.548-1.24.592-1.917l.093-1.433v-.009l.042-1.204V19l-.032-.75a1.4 1.4 0 0 0-.12-.57c-.136-.283-.469-.761-1.144-.761-.35 0-.62.1-.82.234a1 1 0 0 0-.15.127 1.3 1.3 0 0 0-.233-.532 1.6 1.6 0 0 0-1.295-.628 1.73 1.73 0 0 0-1.209.484l-.012.011c-.19-.573-.824-.939-1.48-.939-.623 0-1.228.331-1.448.858l-.79-3.366a1.4 1.4 0 0 0-.18-.445m2.918 14.68V27.4c.034-.15.088-.353.17-.559a2 2 0 0 1 .354-.605c.164-.181.394-.332.692-.332s.528.15.695.33c.164.175.283.398.368.6.087.207.147.41.185.558l.002.01h1.199v-1.784c0-.324.087-.641.251-.92l.841-1.42a3.7 3.7 0 0 0 .51-1.65l.092-1.427.04-1.188-.03-.739a.9.9 0 0 0-.062-.336c-.095-.197-.27-.421-.608-.421a.85.85 0 0 0-.488.132.48.48 0 0 0-.172.247c-.046.123-.071.27-.093.437l-.058.436a.298.298 0 0 1-.59-.008l-.125-1.18c-.022-.208-.063-.359-.145-.464-.14-.181-.394-.4-.827-.4-.37 0-.629.16-.802.323-.154.146-.224.386-.242.698l-.057 1.009a.3.3 0 0 1-.3.282.3.3 0 0 1-.294-.289l-.063-1.757v-.011c0-.327-.357-.698-.942-.698-.586 0-.942.371-.942.698v1.758a.298.298 0 0 1-.587.069l-1.29-5.494a.8.8 0 0 0-.094-.25c-.146-.22-.447-.538-.957-.435-.332.067-.478.249-.553.424a1 1 0 0 0-.078.422l.001.012.013.154c.037.438.116 1.388.363 2.731.099.536.22 1.059.338 1.57l.045.195.111.494c.158.715.287 1.405.287 2.012a.3.3 0 0 1-.183.277.3.3 0 0 1-.324-.063l-1.45-1.439c-.233-.23-.486-.438-.745-.565-.256-.126-.5-.167-.738-.098a.8.8 0 0 0-.352.198 1 1 0 0 0-.26.54c-.071.386.112.791.4 1.215.6.887 1.672 2.47 2.266 3.376a6.5 6.5 0 0 0 1.682 1.725.85.85 0 0 1 .37.693v.908z' clip-rule='evenodd'/%3E%3Cpath fill='%23000' fill-rule='evenodd' d='M19.888 24.92V20.9h.705v4.02zM17.865 24.92V20.9h.705v4.02zM15.85 24.92V20.9h.705v4.02z' clip-rule='evenodd'/%3E%3C/g%3E%3Cdefs%3E%3Cfilter id='a' width='30' height='34' x='-3' y='-2' color-interpolation-filters='sRGB' filterUnits='userSpaceOnUse'%3E%3CfeFlood flood-opacity='0' result='BackgroundImageFix'/%3E%3CfeColorMatrix in='SourceAlpha' result='hardAlpha' values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0'/%3E%3CfeOffset dy='1'/%3E%3CfeGaussianBlur stdDeviation='1.5'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.35 0'/%3E%3CfeBlend in2='BackgroundImageFix' result='effect1_dropShadow_133_35039'/%3E%3CfeBlend in='SourceGraphic' in2='effect1_dropShadow_133_35039' result='shape'/%3E%3C/filter%3E%3C/defs%3E%3C/svg%3E") 12 12, pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Link-module--Oc8GoN.cursor-pointer 103.0x16.0 r 6px shadow #a3a3ee 0px 0px 0px 1px, #3434ab 0px 0px 0px 2px | = |

Crops: `au-terms-default.png`, `au-terms-hover.png`, `au-terms-focus-visible.png`, `au-terms-pressed.png`.

## Transitions declared in the readable stylesheets

descript.com serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- auth: `opacity var(--duration-fast) var(--ease-productive)`, `transform var(--duration-fast) var(--ease-productive)`, `transform 0.15s ease-in-out`, `opacity 0.4s ease-out`, `color 1s var(--ease-productive)`, `transform 1s var(--ease-productive)`, `d 1s var(--ease-productive)`, `none`, `opacity var(--duration-faster) var(--ease-productive)`, `opacity 0.15s ease-in-out`, `background var(--duration-faster) var(--ease-productive)`, `background-color var(--duration-faster) var(--ease-productive)`

- home: `6s ease-out`, `opacity 0.2s ease-in`, `transform 0.1s`, `0.2s linear`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- pricing: `6s ease-out`, `opacity 0.2s ease-in`, `transform 0.1s`, `0.2s linear`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- story: `6s ease-out`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- templates: `6s ease-out`, `opacity 0.2s ease-in`, `transform 0.1s`, `0.2s linear`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- underlord: `6s ease-out`, `opacity 0.2s ease-in`, `transform 0.1s`, `0.2s linear`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- video: `6s ease-out`, `opacity 0.2s ease-in`, `transform 0.1s`, `0.2s linear`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`
