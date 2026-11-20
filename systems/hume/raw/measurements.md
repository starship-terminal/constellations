# Component measurements

Computed styles read from hume.ai's signed-out surfaces (the www.hume.ai marketing/product site, the dev.hume.ai docs, the demo.hume.ai invitation gate, the app.hume.ai /log-in) on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a field clicked into (nothing typed); `dark` is the same element after the docs header's own Theme menu (Light / Dark / System) repainted html.dark — dev.hume.ai is the only captured surface with a theme control, so www/demo/app components carry no dark state; `playing` is the home player's own Play press (a scripted sample-call player — a media control, not a submission); `opened`, `selected` and the rest are resting states reached by a component's own UI toggle. Nothing was typed, sent, queried, submitted or signed into: the contact form, newsletter Subscribe, log-in button and the docs API playground's Send were measured, never used.

## Components

### Site chrome

#### site-nav

Site navigation bar. The top nav on www.hume.ai: the wordmark, Emotion Science, the Products / Solutions / Benchmarks / Resources menu buttons and the "See a Demo" action.

Page: www.hume.ai/. Selector: `header nav, nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 585 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.bg-linear-to-r.from-violet-100: Inter 14px/20px 400, #000000 @ 0 |
| Transition | none |
| Icon | 16 x 16, colour #ffffff @ 0.65 |
| Painted layers | span.bg-linear-to-r.from-violet-100 110.0x20.0 image linear-gradient(to right, #ede9fe 0%, #ddd6ff 100%) |
| How | resting state |

Crops: `site-nav-default.png`.

#### nav-menu-button

Nav menu button ("Products"). A top-level nav menu button — the product/solution picker.

Page: www.hume.ai/. Selector: `button (text Products)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 105 x 32 | = | = |
| Padding | 0px 10px | = | = |
| Gap | 10px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #fdfdfc | = | = |
| Transition | opacity 0.25s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #ffffff @ 0.65 | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | button.group.gap-2.5 105.0x32.0 outline 1px auto #101010 offset 0px |

Crops: `nav-menu-button-default.png`, `nav-menu-button-hover.png`, `nav-menu-button-focus-visible.png`.

#### nav-cta

"See a Demo" button. The solid primary button in the nav — measured, never followed.

Page: www.hume.ai/. Selector: `button, a (text See a Demo)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 149 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #f0efed | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Inter 17px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1918 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.group/button.inline-flex 149.0x40.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | button.group/button.inline-flex 149.0x40.0 bg #f0efed r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | button.group/button.inline-flex 149.0x40.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px outline 1px auto #101010 offset 0px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### site-footer

Site footer. The page footer: link columns, the newsletter form, the social links.

Page: www.hume.ai/. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 501 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #191917 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.font-serif.text-2xl: Martina Plantijn 24px/30px 300, #fdfdfc @ 0.65, ls -0.6px |
| Transition | none |
| Icon | 141.33 x 32, colour #ffffff, fill #000000 |
| Painted layers | footer.on-dark.bg-gray-925 1440.0x501.0 bg #191917; div.flex.h-10 295.0x40.0 bg #222220 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.05 0px 1px 2px 1px, #ffffff @ 0.25 0px 0px 1px 0px; button.group/button.inline-flex 98.0x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px; div.flex.flex-col 1296.0x65.0 border T:1px solid |
| Ancestor paint | 1 up body.bg-background.text-foreground bg #fdfdfc |
| How | resting state |

Crops: `site-footer-default.png`.

#### social-link

Social link. A footer social link ("X/Twitter") — measured, never followed.

Page: www.hume.ai/. Selector: `footer a (social icon)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 4px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff @ 0.5 | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #ffffff @ 0.5 | 16 x 16, colour #ffffff |
| How | resting state | mouse hover over the element |

Crops: `social-link-default.png`, `social-link-hover.png`.

### Home

#### hero-headline

Hero headline. The home hero h1 — the product's largest display style.

Page: www.hume.ai/. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 669 x 133.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Martina Plantijn 58px/66.7px 300 |
| Letter spacing | -1px |
| Colour | #ffffff |
| Text node | span.relative.data-[char=scramble]:text-transparent: Martina Plantijn 58px/66.7px 300, #ffffff, ls -1px |
| Transition | none |
| How | resting state |

Crops: `hero-headline-default.png`.

#### player-card

Customer-call player. The scripted sample-call player on the home hero ("Live answers from the call"): transport, emotion labels, the audio-pipeline diagram.

Page: www.hume.ai/. Selector: `div (player with transport)`. States: default, playing.

| Property | default | playing |
|---|---|---|
| Size (w x h) | 546 x 154 | = |
| Padding | 28px 16px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1918 | = |
| Text node | p.flex.items-center: PP Fraktion Mono 12px/16px 400, #6b6b66, ls 1px | = |
| Transition | none | = |
| Painted layers | span.grid.place-items-center 18.0x18.0 image conic-gradient(from 180deg, #7635fc @ 0.35 -23%, #6e50aa @ 0.35 17%, #baa1ed @ 0.35 47%, # r 3.35544e+07px; span.rounded-full.border 12.0x12.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | = |
| Ancestor paint | 1 up article.flex.min-w-0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.25 0px 0px 1px 0px | = |
| How | resting state | the player's own Play press (a scripted sample-call player — a media control, not a submission); Stop ended it |

Crops: `player-card-default.png`, `player-card-playing.png`.

#### player-transport

Player transport button. The player's Play button — pressed for the playing state, stopped after; a media control, not a submission.

Page: www.hume.ai/. Selector: `button[aria-label="Play"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 30 x 30 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1a1a1a | = |
| Transition | background-color, transform 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #1a1a1a | = |
| Painted layers | button.grid.size-7.5 30.0x30.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | = |
| Ancestor paint | 3 up div.relative.h-65 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.25 0px 0px 1px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `player-transport-default.png`, `player-transport-hover.png`.

#### scenario-button

Player scenario button. A "Show …" scenario chip inside the call player — its own press swaps the scripted scene.

Page: www.hume.ai/. Selector: `button[aria-label^="Show "]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 148 x 461 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1918 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `scenario-button-default.png`, `scenario-button-hover.png`.

#### benchmark-tab

Benchmark category tab. A benchmark category control ("Voice naturalness") — "selected" is its own activation.

Page: www.hume.ai/. Selector: `button (text Voice naturalness)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 155 x 32 | = | = |
| Padding | 0px 14px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | #ffffff |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #6b6b66 | #1b1918 | #1b1918 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 1 up div.flex.gap-1 bg #f6f4f1 | = | = |
| How | resting state | mouse hover over the element | the tab's own activation — a local UI toggle |
| Painted layers | - | = | button.h-8.flex-none 155.0x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px |

Crops: `benchmark-tab-default.png`, `benchmark-tab-hover.png`, `benchmark-tab-selected.png`.

#### newsletter-input

Newsletter email input. The "Email address" field of the footer newsletter form. "focused" is the field clicked into — nothing is typed, the form is never submitted.

Page: www.hume.ai/. Selector: `input[type="email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 159 x 40 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #ffffff @ 0.65, opacity 1 | = |
| Ancestor paint | 1 up div.flex.h-10 bg #222220 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.05 0px 1px 2px 1px, #ffffff @ 0.25 0px 0px 1px 0px | 1 up div.flex.h-10 bg #222220 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.35 0px 0px 0px 1px, #ffffff @ 0.05 0px 1px 2px 1px, #ffffff @ 0.25 0px 0px 1px 0px |
| How | resting state | the field clicked into |

Crops: `newsletter-input-default.png`, `newsletter-input-focused.png`.

#### newsletter-button

Newsletter "Subscribe" button. The newsletter form's submit — measured, never pressed.

Page: www.hume.ai/. Selector: `button (text Subscribe)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 98 x 32 | = |
| Padding | 0px 14px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | #f0efed |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | = |
| Outline | none | = |
| Font | Inter 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #1b1918 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.group/button.inline-flex 98.0x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | button.group/button.inline-flex 98.0x32.0 bg #f0efed r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px |
| Ancestor paint | 1 up div.flex.h-10 bg #222220 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.05 0px 1px 2px 1px, #ffffff @ 0.25 0px 0px 1px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `newsletter-button-default.png`, `newsletter-button-hover.png`.

#### section-heading

Section heading. A home section heading (an h2).

Page: www.hume.ai/. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 242 x 73.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Martina Plantijn 32px/36.8px 300 |
| Letter spacing | -1px |
| Colour | #1b1918 |
| Transition | none |
| How | resting state |

Crops: `section-heading-default.png`.

### Product pages

#### product-hero

Product hero headline. The product page h1 — the display face at its working size.

Page: www.hume.ai/products/decision-model-api. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 387 x 133.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Martina Plantijn 58px/66.7px 300 |
| Letter spacing | -1px |
| Colour | #ffffff |
| Text node | span.relative.data-[char=scramble]:text-transparent: Martina Plantijn 58px/66.7px 300, #ffffff, ls -1px |
| Transition | none |
| How | resting state |

Crops: `product-hero-default.png`.

#### product-cta

Product "Contact sales" button. The product page's primary action — measured, never followed.

Page: www.hume.ai/products/decision-model-api. Selector: `button, a (text Contact sales)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 120 x 32 | = | = |
| Padding | 0px 14px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #ffffff | #f0efed | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1918 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.group/button.items-center 120.0x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | a.group/button.items-center 120.0x32.0 bg #f0efed r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px | a.group/button.items-center 120.0x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px outline 1px auto #101010 offset 1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `product-cta-default.png`, `product-cta-hover.png`, `product-cta-focus-visible.png`.

#### product-card

Decision demo tab control. The Audio Fact / Listener Judgment / Interaction Decisions segmented tablist in the product page's decision demo.

Page: www.hume.ai/products/decision-model-api. Selector: `[role="tablist"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 447.83 x 40 |
| Padding | 4px |
| Gap | 4px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #f6f4f1 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1918 |
| Text node | button.relative.h-8: Inter 14px/20px 500, #1b1918, ls -0.15px |
| Transition | none |
| Painted layers | div.scrollbar-hide.relative 447.8x40.0 bg #f6f4f1 r 3.35544e+07px; span.absolute.left-(--active-tab-left) 100.5x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px |
| How | resting state |

Crops: `product-card-default.png`.

### Blog

#### post-card

Post preview card. A blog index post card: title, excerpt, meta.

Page: www.hume.ai/blog. Selector: `main a (post card)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1152 x 500 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1918 | = |
| Text node | span.text-gray-600: PP Fraktion Mono 12px/16px 400, #474644, ls 1px | = |
| Transition | none | = |
| Icon | 24 x 24, colour #1b1918, fill #000000 | = |
| Painted layers | div.flex.flex-col 576.0x500.0 bg #ffffff; div.w-full.h-full 40.0x40.0 bg #f9f9f9 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1e1e1d @ 0.1 0px 0px 0px 1.67px inset, #000000 @ 0 0px 0px 0px 0px; p.@container.absolute 576.0x500.0 bg #191917 @ 0.12 | = |
| How | resting state | mouse hover over the element |

Crops: `post-card-default.png`, `post-card-hover.png`.

#### post-title-link

Post title link. The post's title link inside an index card.

Page: www.hume.ai/blog. Selector: `main a (post title)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 403 x 133.38 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Martina Plantijn 38px/43.7px 300 | = |
| Letter spacing | -1px | = |
| Colour | #1b1918 | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::after | 1152px x 500px, absolute, bg #000000 @ 0, radius 0px | = |
| How | resting state | mouse hover over the element |

Crops: `post-title-link-default.png`, `post-title-link-hover.png`.

#### blog-filter

Blog category filter. A blog category chip ("Research"). "selected" is its own activation; the All filter restores.

Page: www.hume.ai/blog. Selector: `button, a (text Research)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 94 x 32 | = | = |
| Padding | 0px 14px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | #ffffff |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px |
| Outline | none | = | = |
| Font | Inter 14px/32px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #6b6b66 | #1b1918 | #1b1918 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 1 up nav.flex.gap-1 bg #f6f4f1 | = | = |
| How | resting state | mouse hover over the element | the filter's own activation — a local UI toggle (All restored after) |
| Painted layers | - | = | a.h-8.shrink-0 94.0x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px |

Crops: `blog-filter-default.png`, `blog-filter-hover.png`, `blog-filter-selected.png`.

### Prose

#### prose-h1

Article title (h1). The blog post title.

Page: www.hume.ai/blog/hume-audio-decision-benchmarks. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 790 x 43.69 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Martina Plantijn 38px/43.7px 300 |
| Letter spacing | -1px |
| Colour | #1b1918 |
| Transition | none |
| How | resting state |

Crops: `prose-h1-default.png`.

#### prose-p

Body paragraph. A paragraph of article prose.

Page: www.hume.ai/blog/hume-audio-decision-benchmarks. Selector: `main p (sentence)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 582 x 115.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/23.2px 400 |
| Letter spacing | normal |
| Colour | #474644 |
| Transition | none |
| How | resting state |

Crops: `prose-p-default.png`.

#### prose-link

Prose link. A body-text link inside the article.

Page: www.hume.ai/blog/hume-audio-decision-benchmarks. Selector: `main p a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 160 x 18 | = |
| Padding | 0px 0px 0px 14px | = |
| Border | T: none; R: none; B: none; L: 1px solid #1e1e1d | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/18px 400 | = |
| Letter spacing | -0.35px | = |
| Colour | #1b1918 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | a.-ml-px.block 160.0x18.0 border L:1px solid | = |
| How | resting state | mouse hover over the element |

Crops: `prose-link-default.png`, `prose-link-hover.png`.

#### prose-code

Inline code. An inline code span in prose.

Page: www.hume.ai/blog/hume-audio-decision-benchmarks. Selector: `main p code`. States: .

Not found on the page at capture time.

#### prose-pre

Code block. A fenced code block in the article.

Page: www.hume.ai/blog/hume-audio-decision-benchmarks. Selector: `main pre`. States: .

Not found on the page at capture time.

#### prose-table

Prose table. A data table in the article (the benchmark post tabulates results).

Page: www.hume.ai/blog/hume-audio-decision-benchmarks. Selector: `main table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 239 x 194.08 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20.3px 400 |
| Letter spacing | normal |
| Colour | #474644 |
| Text node | th: Inter 14px/20.3px 700, #474644 |
| Transition | none |
| Ancestor paint | 1 up figure bg #ffffff |
| How | resting state |

Crops: `prose-table-default.png`.

### Contact form

#### contact-field

Contact form field. A text field of the "Talk to Hume" form — clicked into for the focus look, never typed.

Page: www.hume.ai/contact-form. Selector: `input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 214 x 38 | = |
| Padding | 6px 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | #353535 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Inter 14px/normal 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | border-color, box-shadow 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #ffffff @ 0.5, opacity 1 | = |
| Painted layers | input.css-14aefq 214.0x38.0 r 8px shadow #353535 0px 0px 0px 0px | = |
| Ancestor paint | 1 up div.css-1449vgc bg #ffffff @ 0 | = |
| How | resting state | the field clicked into |

Crops: `contact-field-default.png`, `contact-field-focused.png`.

#### contact-textarea

Contact form textarea. The message textarea, if the form carries one.

Page: www.hume.ai/contact-form. Selector: `textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 448 x 120 | = |
| Padding | 8px 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | #353535 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Inter 14px/normal 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0 | #ffffff |
| Transition | border-color, box-shadow 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0, opacity 1 | #ffffff @ 0.5, opacity 1 |
| Painted layers | textarea.css-1px7gbw 448.0x120.0 r 8px shadow #353535 0px 0px 0px 0px | textarea.css-1xfrjtn 448.0x120.0 r 8px shadow #353535 0px 0px 0px 0px |
| Ancestor paint | 1 up div.css-1wlfnkz bg #ffffff @ 0 | 1 up div.css-itrmmz bg #ffffff @ 0 |
| How | resting state | the field clicked into |

Crops: `contact-textarea-default.png`, `contact-textarea-focused.png`.

#### contact-select

Contact interest select. The interest/topic select or radio group the form carries — its menu never opened.

Page: www.hume.ai/contact-form. Selector: `select, [role="combobox"], button (interest)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 4 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/normal 500 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Cursor | text |
| Placeholder | #333333, opacity 1 |
| How | resting state |

Crops: `contact-select-default.png`.

#### contact-submit

Contact submit button. The form's submit — measured at rest and hover only, never pressed.

Page: www.hume.ai/contact-form. Selector: `button (submit)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 448 x 40 | = |
| Padding | 0px 10px | = |
| Border | none | = |
| Radius | 30px | = |
| Background | #ffffff | #e8e8e8 |
| Box shadow | #353535 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Inter 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #353535 | = |
| Text node | span.css-11rtfye: Inter 17px/normal 500, #1e1e1e | = |
| Transition | all 0.2s ease | = |
| Cursor | pointer | = |
| Painted layers | button.css-1a0d635 448.0x40.0 bg #ffffff r 30px shadow #353535 0px 0px 0px 0px | button.css-1a0d635 448.0x40.0 bg #e8e8e8 r 30px shadow #353535 0px 0px 0px 0px |
| How | resting state | mouse hover over the element |

Crops: `contact-submit-default.png`, `contact-submit-hover.png`.

### Docs

#### docs-nav

Docs sidebar. The left navigation rail on dev.hume.ai (a Fern docs shell).

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `aside, nav`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 272 x 6350.52 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Fellix 16px/24px 350 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #ffffff |
| Transition | none | = |
| How | resting state | same element after the docs header Theme menu's own Dark item repaints html.dark (the only real theme control on any captured surface) |

Crops: `docs-nav-default.png`, `docs-nav-dark.png`.

#### docs-side-link

Docs nav section link. A section link in the docs left nav ("Authentication").

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `aside a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 222 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Fellix 14px/20px 350 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `docs-side-link-default.png`, `docs-side-link-hover.png`.

#### docs-search-button

Docs "Search /" button. The header search field button — its dialog was never queried.

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `button (text Search)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 552.34 x 36 | = |
| Padding | 8px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e7e5e4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Fellix 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #79716b | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | text | wait |
| Icon | 16 x 16, colour #79716b | = |
| Painted layers | button.focus-visible:ring-(color:--accent).rounded-2 552.3x36.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e7e5e4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; kbd.fern-kbd 21.0x22.0 bg #ffffff @ 0.8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 6px | = |
| How | resting state | mouse hover over the element |

Crops: `docs-search-button-default.png`, `docs-search-button-hover.png`.

#### docs-theme-button

Docs Theme button. The header's Theme button — the only real theme control on any captured surface. "opened" is its own press painting the Light / Dark / System menu.

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `button[aria-label="Theme" i]`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 36 x 36 | = | 118 x 96 |
| Padding | 0px | = | = |
| Gap | 8px | = | - |
| Border | none | = | 1px solid #e7e5e4 |
| Radius | 8px | = | = |
| Background | transparent | #000000 @ 0.063 | #ffffff |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| Outline | none | = | = |
| Font | Fellix 14px/20px 500 | = | Fellix 16px/24px 350 |
| Letter spacing | normal | = | = |
| Colour | #79716b | #000000 | #000000 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none |
| Cursor | pointer | = | - |
| Icon | 16 x 16, colour #79716b | 16 x 16, colour #000000 | 16 x 16, colour #000000 |
| How | resting state | mouse hover over the element | the Theme button's own press (the Light / Dark / System menu open; Escape restores) |
| Painted layers | - | button.focus-visible:ring-(color:--accent).rounded-2 36.0x36.0 bg #000000 @ 0.063 r 8px | div.fern-dropdown.[&_svg]:size-icon 118.0x96.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| Backdrop filter | - | = | blur(8px) |
| Text node | - | = | div: Fellix 14px/20px 350, #000000 |

Crops: `docs-theme-button-default.png`, `docs-theme-button-hover.png`, `docs-theme-button-opened.png`.

#### docs-cta

Docs "Get access" button. The header's primary action — measured, never followed.

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `a, button (text Get access)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 113 x 32 | = |
| Padding | 4px 12px | = |
| Border | none | = |
| Radius | 9999px | = |
| Background | transparent | #201000 @ 0.063 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e7e5e4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Fellix 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #2a2a2a | = |
| Text node | span.fern-button-text: Fellix 14px/20px 500, #2a2a2a | = |
| Transition | box-shadow, background 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer | = |
| Painted layers | a.group.cursor-pointer 113.0x32.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e7e5e4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.group.cursor-pointer 113.0x32.0 bg #201000 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e7e5e4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | mouse hover over the element |

Crops: `docs-cta-default.png`, `docs-cta-hover.png`.

#### docs-code-block

Docs code block. A fenced code block in the docs article — the surface the docs' --code-background and syntax palette paint.

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `pre`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 704 x 410.75 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px 0px 4px 4px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Fraktion 16px/28px 350 | = |
| Letter spacing | normal | = |
| Colour | #24292e | = |
| Text node | span: Fraktion 14px/22.75px 350, #6f42c1 | span: Fraktion 14px/22.75px 350, #ffcb6b |
| Transition | none | = |
| Ancestor paint | 1 up div.fern-code.fern-code-group bg #ffffff | 1 up div.fern-code.fern-code-group bg #0c0a09 |
| How | resting state | same element after the docs header Theme menu's own Dark item repaints html.dark (the only real theme control on any captured surface) |

Crops: `docs-code-block-default.png`, `docs-code-block-dark.png`.

#### docs-inline-code

Docs inline code. An inline code span inside the docs article.

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 160 x 21 |
| Padding | 2px 4px |
| Border | none |
| Radius | 6px |
| Background | #201000 @ 0.063 |
| Box shadow | none |
| Outline | none |
| Font | Fraktion 14px/24.5px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | code 160.0x21.0 bg #201000 @ 0.063 r 6px |
| How | resting state |

Crops: `docs-inline-code-default.png`.

#### docs-toc

Docs "On this page" rail. The right-rail table of contents.

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `aside, nav (toc)`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 272 x 390.14 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Fellix 16px/24px 350 | = |
| Letter spacing | normal | = |
| Colour | #000000 | #ffffff |
| Text node | div.text-(color:--grayscale-a11).m-0: Fraktion 12px/17.1429px 500, #79716b, ls 0.6px | div.text-(color:--grayscale-a11).m-0: Fraktion 12px/17.1429px 500, #e7e5e4, ls 0.6px |
| Transition | none | = |
| Icon | 16 x 16, colour #79716b | 16 x 16, colour #e7e5e4 |
| Painted layers | ul.toc-root.not-prose 236.0x216.0 border L:2px solid; span.toc-track 2.0x28.0 bg #1f1800 @ 0.13 r 1px 1px 0px 0px; span.toc-fill 2.0x28.0 bg #000000; span.toc-track 2.0x28.0 bg #1f1800 @ 0.13; span.toc-fill 2.0x28.0 bg #000000; span.toc-track 2.0x28.0 bg #1f1800 @ 0.13 | ul.toc-root.not-prose 236.0x216.0 border L:2px solid; span.toc-track 2.0x28.0 bg #fbfbeb @ 0.137 r 1px 1px 0px 0px; span.toc-fill 2.0x28.0 bg #ffffff; span.toc-track 2.0x28.0 bg #fbfbeb @ 0.137; span.toc-fill 2.0x28.0 bg #ffffff; span.toc-track 2.0x28.0 bg #fbfbeb @ 0.137 |
| How | resting state | same element after the docs header Theme menu's own Dark item repaints html.dark (the only real theme control on any captured surface) |

Crops: `docs-toc-default.png`, `docs-toc-dark.png`.

#### docs-lang-tab

Docs language tab. A code-sample language tab ("Python"). "selected" is its own activation.

Page: dev.hume.ai/audio-decisions/docs/overview. Selector: `button (text Python)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 58 x 34 | = | = |
| Padding | 2px 10px | = | = |
| Border | none | = | = |
| Radius | 3px | = | = |
| Background | transparent | = | #1f1500 @ 0.098 |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Fellix 12px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #79716b | #000000 | #000000 |
| Text node | span.fern-code-label.fern-code-group-tab-label: Fellix 12px/20px 500, #79716b | span.fern-code-label.fern-code-group-tab-label: Fellix 12px/20px 500, #000000 | span.fern-code-label.fern-code-group-tab-label: Fellix 12px/20px 500, #000000 |
| Transition | none | = | = |
| Cursor | default | = | = |
| Ancestor paint | 1 up div.fern-x-overflow.fern-code-group-tabs bg #ffffff | = | = |
| How | resting state | mouse hover over the element | the tab's own activation — a local UI toggle |
| Painted layers | - | = | button.fern-code-group-tab.data-[state=active]:shadow-(color:--accent) 58.0x34.0 bg #1f1500 @ 0.098 r 3px |

Crops: `docs-lang-tab-default.png`, `docs-lang-tab-hover.png`, `docs-lang-tab-selected.png`.

### Demo gate

#### demo-gate-card

Invitation gate card. The demo.hume.ai gate: "Start from your invitation — the Audio Decision Model playground opens from the link in your invitation email". The playground itself is a documented boundary.

Page: demo.hume.ai/decision-model/file. Selector: `main, div (gate card)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 855 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fellix 16px/24px 350 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.text-2xl.text-text-primary: fellix 24px/32px 350, #000000 |
| Transition | none |
| Icon | 22.34 x 22.34, colour #ffffff |
| Painted layers | a.box-border.inline-flex 123.0x36.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.h-dvh bg #ffffff |
| How | resting state |

Crops: `demo-gate-card-default.png`.

#### demo-gate-cta

Gate "Contact sales" link. The gate's only action — measured, never followed.

Page: demo.hume.ai/decision-model/file. Selector: `a (text Contact sales)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 123 x 36 | = |
| Padding | 0px 14px | = |
| Gap | 6px | = |
| Border | 1px solid #000000 | = |
| Radius | 3.35544e+07px | = |
| Background | #000000 | #000000 @ 0.9 |
| Box shadow | none | = |
| Outline | none | = |
| Font | fellix 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.[grid-area:1_/_1].opacity-100: fellix 14px/20px 500, #ffffff | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 21.15 x 21.15, colour #ffffff | 17.53 x 17.53, colour #ffffff |
| Painted layers | a.box-border.inline-flex 123.0x36.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | a.box-border.inline-flex 123.0x36.0 bg #000000 @ 0.9 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state | mouse hover over the element |

Crops: `demo-gate-cta-default.png`, `demo-gate-cta-hover.png`.

### Log-in

#### login-card

Log-in card. The app.hume.ai sign-in card — the platform's public boundary page; nothing past it was entered.

Page: app.hume.ai/log-in. Selector: `main, div (login card)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 511 x 608 |
| Padding | 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fellix 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.text-xl.font-medium: Fellix 20px/28px 500, #000000 |
| Transition | none |
| Icon | 431 x 24, colour #000000 |
| Painted layers | button.box-border.inline-flex 431.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; button.box-border.inline-flex 431.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; hr.grow.border-border 128.0x1.0 border T:1px solid; hr.grow.border-border 128.0x1.0 border T:1px solid; div.[&_input]:text-inherit.h-10 431.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px; div.[&_input]:text-inherit.h-10 431.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px |
| Ancestor paint | 1 up div.my-auto.grid bg #ffffff |
| How | resting state |

Crops: `login-card-default.png`.

#### login-email-field

Email field. The log-in Email field — clicked into for the focus look, never typed.

Page: app.hume.ai/log-in. Selector: `input[type="email"], input (Email)`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 421 x 30 | = |
| Padding | 4px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Fellix 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| How | resting state | the field clicked into |

Crops: `login-email-field-default.png`, `login-email-field-focused.png`.

#### login-password-field

Password field. The log-in Password field — clicked into, never typed.

Page: app.hume.ai/log-in. Selector: `input[type="password"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 389 x 30 | = |
| Padding | 4px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Fellix 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| How | resting state | the field clicked into |

Crops: `login-password-field-default.png`, `login-password-field-focused.png`.

#### login-submit

"LOG IN" button. The sign-in submit — measured at rest and hover only, never pressed (no credentials exist to submit).

Page: app.hume.ai/log-in. Selector: `button (text LOG IN)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 431 x 36 | = |
| Padding | 0px 14px | = |
| Gap | 6px | = |
| Border | 1px solid #000000 | = |
| Radius | 3.35544e+07px | = |
| Background | #000000 | #000000 @ 0.9 |
| Box shadow | none | = |
| Outline | none | = |
| Font | PP Fraktion Mono 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.text-left: PP Fraktion Mono 14px/20px 400, #ffffff | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 18.9 x 18.9, colour #ffffff | 17.48 x 17.48, colour #ffffff |
| Painted layers | button.box-border.inline-flex 431.0x36.0 bg #000000 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | button.box-border.inline-flex 431.0x36.0 bg #000000 @ 0.9 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state | mouse hover over the element |

Crops: `login-submit-default.png`, `login-submit-hover.png`.

#### login-oauth

"SIGN IN WITH GOOGLE" button. An OAuth button — measured, never pressed.

Page: app.hume.ai/log-in. Selector: `button (text SIGN IN WITH GOOGLE)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 431 x 36 | = |
| Padding | 0px 14px | = |
| Gap | 6px | = |
| Border | 1px solid #000000 @ 0.1 | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | #000000 @ 0.05 |
| Box shadow | none | = |
| Outline | none | = |
| Font | PP Fraktion Mono 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.[grid-area:1_/_1].opacity-100: PP Fraktion Mono 14px/20px 400, #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 21.9 x 21.9, colour #000000 | 16.13 x 16.13, colour #000000 |
| Painted layers | button.box-border.inline-flex 431.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | button.box-border.inline-flex 431.0x36.0 bg #000000 @ 0.05 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state | mouse hover over the element |

Crops: `login-oauth-default.png`, `login-oauth-hover.png`.

#### login-show-password

"Show password" toggle. The password visibility toggle — measured; its own press would reveal a (never-typed) field.

Page: app.hume.ai/log-in. Selector: `button[aria-label="Show password"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 32 x 30 | = |
| Padding | 0px 8px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Fellix 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #000000 | = |
| How | resting state | mouse hover over the element |

Crops: `login-show-password-default.png`, `login-show-password-hover.png`.

### Site chrome (mobile)

#### m-nav

Mobile nav. The sticky header bar at 390px — the desktop nav links hide behind "Open menu".

Page: www.hume.ai/. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #1e1e1d |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Icon | 106 x 24, colour #ffffff, fill #000000 |
| Painted layers | header.on-dark.sticky 390.0x56.0 bg #1e1e1d; span.bg-linear-to-r.from-violet-100 0.0x0.0 image linear-gradient(to right, #ede9fe 0%, #ddd6ff 100%); a.group/button.items-center 0.0x0.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px |
| Ancestor paint | 1 up body.bg-background.text-foreground bg #fdfdfc |
| How | resting state |

Crops: `m-nav-default.png`.

#### m-menu-button

"Open menu" button. The mobile menu trigger. "opened" is its own press painting the drawer; Escape closes it.

Page: www.hume.ai/. Selector: `button[aria-label="Open menu"]`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 36 x 36 | 390 x 329 |
| Padding | 0px | = |
| Border | none | T: 1px solid #ffffff @ 0.05; R: none; B: none; L: none |
| Radius | 0px | = |
| Background | transparent | #1e1e1d |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff @ 0.65 | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none |
| Cursor | pointer | - |
| Icon | 20 x 20, colour #ffffff @ 0.65 | 16 x 16, colour #ffffff @ 0.65 |
| How | resting state | the Open menu button's own press (the drawer open; Escape restores) |
| Text node | - | span.bg-linear-to-r.from-violet-100: Inter 16px/24px 400, #000000 @ 0 |
| Painted layers | - | nav.on-dark.max-h-(--available-height) 390.0x329.0 bg #1e1e1d border T:1px solid; span.bg-linear-to-r.from-violet-100 127.0x24.0 image linear-gradient(to right, #ede9fe 0%, #ddd6ff 100%); a.group/button.inline-flex 342.0x40.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 1px, #000000 @ 0.35 0px 0px 1px 0px |

Crops: `m-menu-button-default.png`, `m-menu-button-opened.png`.

## Transitions declared in the readable stylesheets

Each surface serves its own CSS same-origin, so this list is the product's own transition declarations the CSSOM could read on each page.

- app.hume.ai/log-in: `height 0.2s`, `left 0.2s, top 0.2s, width 0.2s, height 0.2s`, `none`, `background 0.2s`, `background-color 600000s, color 600000s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `opacity 0.2s, transform 0.2s`

- demo.hume.ai/decision-model/file: none

- dev.hume.ai/audio-decisions/docs/overview: `max-width 500ms ease-out`, `transform 200ms linear, opacity 200ms linear`, `transform 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 0.5s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 450ms cubic-bezier(0.4, 0, 0.2, 1)`, `border-color 120ms, background-color 120ms`

- www.hume.ai/: none

- www.hume.ai/blog: none

- www.hume.ai/blog/hume-audio-decision-benchmarks: `background 0.15s`

- www.hume.ai/contact-form: `0.2s`, `border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out`, `100ms`, `color 150ms`

- www.hume.ai/products/decision-model-api: none
