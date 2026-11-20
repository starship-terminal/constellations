# Component measurements

Computed styles read from endlesstools.io and app.endlesstools.io on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the two public surfaces — the dark marketing one-pager on the apex domain and the app host's dark /login card and /legal/* document pages — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky top bar over a fade gradient: the logomark, the Log-in outline pill and the white Start-for-free pill.

Page: home. Selector: `div.nav-gradient`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#000000 14.73%, #000a0a @ 0 100%) |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.hidden.md:inline-flex: Inter 12px/14px 500, #959595 |
| Transition | none |
| Cursor | default |
| Painted layers | div.sticky.inset-x-0 1440.0x80.0 image linear-gradient(#000000 14.73%, #000a0a @ 0 100%); a.hidden.md:inline-flex 74.9x35.0 bg #1e1e1e @ 0.8 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #959595 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; a.hidden.md:inline-flex 113.2x35.0 bg #ffffff r 3.35544e+07px; button.md:hidden.inline-flex 0.0x0.0 bg #ffffff r 3.35544e+07px |
| Ancestor paint | 1 up body.inter_fe4d0f8a-module__6kuHYW__variable.font-inter bg #000000 |
| How | at rest |

Crops: none.

#### logo

Logo. The Endless Tools dot-grid logomark anchor.

Page: home. Selector: `.nav-gradient img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 130 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### nav-login

Log in link. The Log-in header action (secondary pill on a blurred #1e1e1e fill); measured never followed.

Page: home. Selector: `.nav-gradient a "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.91 x 35 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #1e1e1e @ 0.8 | #1e1e1e | = | #1e1e1e |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #959595 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Backdrop filter | blur(16px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 12px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #959595 | #ffffff | = | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hidden.md:inline-flex 74.9x35.0 bg #1e1e1e @ 0.8 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #959595 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.hidden.md:inline-flex 74.9x35.0 bg #1e1e1e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | a.hidden.md:inline-flex 74.9x35.0 bg #1e1e1e @ 0.8 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #959595 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px outline 1px auto #005fcc offset 1px | a.hidden.md:inline-flex 74.9x35.0 bg #1e1e1e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### nav-cta

Nav CTA. The Start-for-free white pill; measured never followed (it opens the app host).

Page: home. Selector: `"Start for free" pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.22 x 35 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #373737 | = | #373737 |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(16px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 12px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | #ffffff | = | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hidden.md:inline-flex 113.2x35.0 bg #ffffff r 3.35544e+07px | a.hidden.md:inline-flex 113.2x35.0 bg #373737 r 3.35544e+07px | a.hidden.md:inline-flex 113.2x35.0 bg #ffffff r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.hidden.md:inline-flex 113.2x35.0 bg #373737 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Home hero

#### hero-title

Hero headline. The 42px title-primary headline; "exploration" and "graphic designers" carry hand-drawn circle/underline marks painted by masked white spans.

Page: home. Selector: `hero h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 820 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/46px 500 |
| Letter spacing | -1.26px |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | span.block.bg-current 0.0x0.0 bg #ffffff; span.block.bg-current 230.0x62.2 bg #ffffff; span.block.bg-current 0.0x0.0 bg #ffffff; span.block.bg-current 210.0x7.8 bg #ffffff |
| How | at rest |

Crops: none.

#### hero-mark

Annotation mark. One of the aria-hidden white spans behind the headline words, masked (via CSS mask-image) into the hand-drawn circle and underline — the signature annotation style repeated on every section heading.

Page: home. Selector: `h1 span[aria-hidden]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 230 x 62.23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/46px 500 |
| Letter spacing | -1.26px |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | span.block.bg-current 230.0x62.2 bg #ffffff |
| How | at rest |

Crops: none.

#### hero-lede

Hero copy. The 14px grey-4 lede under the headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/18px 400 |
| Letter spacing | normal |
| Colour | #959595 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### hero-cta

Hero CTA. The Start-exploring pill — the only pink (#FF13B1) action on the site; measured never followed.

Page: home. Selector: `"Start exploring"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 124.41 x 36 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff13b1 | #ff4bc4 | = | #ff4bc4 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 12px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hidden.md:inline-flex 124.4x36.0 bg #ff13b1 r 3.35544e+07px | a.hidden.md:inline-flex 124.4x36.0 bg #ff4bc4 r 3.35544e+07px | a.hidden.md:inline-flex 124.4x36.0 bg #ff13b1 r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.hidden.md:inline-flex 124.4x36.0 bg #ff4bc4 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Asset inputs

#### asset-title

Asset input title. An input-source heading (Use a library) inside a hand-drawn circle mark.

Page: home. Selector: `hero_inputs h2 "Use a library"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 135.05 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/26px 500 |
| Letter spacing | -0.72px |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### asset-thumb

Asset thumbnail. A floating asset tile: a looping muted video in a 16px-radius rounded box.

Page: home. Selector: `hero_inputs video tile`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 144 x 144 |
| Padding | 0px |
| Border | 1px solid #343434 |
| Radius | 16px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | div.relative.h-full 144.0x144.0 border T:1px solid #343434 / R:1px solid #343434 / B:1px solid #343434 / L:1px solid #343434 r 16px |
| How | at rest |

Crops: none.

### Statement sections

#### section-title

Section heading. A statement heading ("The hard part isn't making it.") — title-primary inside an underline mark.

Page: home. Selector: `"The hard part" heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 820 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/46px 500 |
| Letter spacing | -1.26px |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | span.block.bg-current 0.0x0.0 bg #ffffff; span.block.bg-current 200.0x28.2 bg #ffffff |
| How | at rest |

Crops: none.

#### editor-shot

Product shot. The embedded product-workspace image/video in the "One workspace" band (marketing content, not the app).

Page: home. Selector: `workspace section media`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1300 x 700 |
| Padding | 0px |
| Border | none |
| Radius | 10px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `editor-shot-default.png`.

### Pricing

#### billing-yearly

Billing toggle, yearly. The Yearly option of the billing toggle (selected by default — the chosen option renders disabled).

Page: home. Selector: `button "Yearly"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.48 x 26 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/24px 500 | = | - | = |
| Letter spacing | -0.4px | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | span.text-[12px].inline-flex 71.8x25.0 bg #ff3dae r 3.35544e+07px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: none.

#### billing-monthly

Billing toggle, monthly. The Monthly option; toggled for the monthly screenshot state, never checked out.

Page: home. Selector: `button "Monthly"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59.53 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | -0.4px | = | = | = |
| Colour | #ffffff @ 0.3 | #ffffff @ 0.75 | = | #ffffff @ 0.75 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.text-white/30.disabled:text-white 59.5x26.0 outline 1px auto #005fcc offset 0px | = |

Crops: none.

#### save-pill

Save badge. The pink "Save 17%" pill inside the Yearly option.

Page: home. Selector: `"Save 17%" badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 71.84 x 25 |
| Padding | 0px 10px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #ff3dae |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/25px 500 |
| Letter spacing | -0.4px |
| Colour | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | span.text-[12px].inline-flex 71.8x25.0 bg #ff3dae r 3.35544e+07px |
| How | at rest |

Crops: none.

#### plan-card

Plan card. A pricing plan card: 33px radius, #121212 fill, 1px #222 ring, hover lifts to #1D1D1D.

Page: home. Selector: `div.rounded-[33px]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 356.66 x 562 | = |
| Padding | 15px | = |
| Border | none | = |
| Radius | 33px | = |
| Background | #121212 | #1d1d1d |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | div.ring-1.ring-[#222222]: Inter 14px/35px 500, #ffffff | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | default | pointer |
| Painted layers | div.ring-1.ring-[#222222] 356.7x562.0 bg #121212 r 33px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; div.ring-1.ring-[#222222] 64.2x35.0 bg #121212 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.block.bg-current 0.0x0.0 bg #ffffff; span.block.bg-current 350.0x139.7 bg #ffffff; a.hidden.md:inline-flex 326.7x36.0 bg #ffffff r 3.35544e+07px; button.inline-flex.md:hidden 0.0x0.0 bg #ffffff r 3.35544e+07px | div.ring-1.ring-[#222222] 356.7x562.0 bg #1d1d1d r 33px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; div.ring-1.ring-[#222222] 64.2x35.0 bg #121212 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.block.bg-current 0.0x0.0 bg #ffffff; span.block.bg-current 350.0x139.7 bg #ffffff; a.hidden.md:inline-flex 326.7x36.0 bg #ffffff r 3.35544e+07px; button.inline-flex.md:hidden 0.0x0.0 bg #ffffff r 3.35544e+07px |
| How | at rest | mouse hover |

Crops: none.

#### plan-chip

Plan chip. The FREE plan chip — a dark pill on the card header.

Page: home. Selector: `"FREE" chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 64.22 x 35 |
| Padding | 0px 15px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #121212 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 14px/35px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | div.ring-1.ring-[#222222] 64.2x35.0 bg #121212 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 2 up div.ring-1.ring-[#222222] bg #121212 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### plan-chip-pro

Plan chip, PRO. The PRO chip — the inverted white pill.

Page: home. Selector: `"PRO" chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 58.8 x 35 |
| Padding | 0px 15px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/35px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Cursor | default |
| Painted layers | div.bg-white.text-black 58.8x35.0 bg #ffffff r 3.35544e+07px |
| Ancestor paint | 2 up div.ring-1.ring-[#222222] bg #121212 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### plan-chip-edu

Plan chip, EDUCATION. The EDUCATION chip — the one blue element on the surface.

Page: home. Selector: `"EDUCATION" chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 111.88 x 35 |
| Padding | 0px 15px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #2c5cff |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/35px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | div.text-white.leading-[35px] 111.9x35.0 bg #2c5cff r 3.35544e+07px |
| Ancestor paint | 2 up div.ring-1.ring-[#222222] bg #121212 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### plan-price

Plan price. A plan price figure at title-primary size.

Page: home. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 51.72 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/42px 500 |
| Letter spacing | -1.26px |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| Ancestor paint | 2 up div.ring-1.ring-[#222222] bg #121212 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### plan-feature

Plan feature row. A feature row on the PRO card: a 15px SVG glyph plus a bold white key and grey detail text.

Page: home. Selector: `plan feature row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 303.67 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/14px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.text-white: Inter 12px/14px 500, #ffffff |
| Transition | none |
| Cursor | default |
| Ancestor paint | 3 up div.ring-1.ring-[#222222] bg #121212 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### plan-cta

Plan CTA. A plan card action (white pill); measured never followed.

Page: home. Selector: `"Try for free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 326.66 x 36 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #c4c4c4 | = | #c4c4c4 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 12px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hidden.md:inline-flex 326.7x36.0 bg #ffffff r 3.35544e+07px | a.hidden.md:inline-flex 326.7x36.0 bg #c4c4c4 r 3.35544e+07px | a.hidden.md:inline-flex 326.7x36.0 bg #ffffff r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.hidden.md:inline-flex 326.7x36.0 bg #c4c4c4 r 3.35544e+07px |
| Ancestor paint | 2 up div.ring-1.ring-[#222222] bg #121212 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | 2 up div.ring-1.ring-[#222222] bg #1d1d1d shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Team and education

#### team-cta

Team CTA. The Create-team action under the shared-workspace section; measured never followed.

Page: home. Selector: `"Create team"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110 x 36 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #c4c4c4 | = | #c4c4c4 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 12px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hidden.md:inline-flex 110.0x36.0 bg #ffffff r 3.35544e+07px | a.hidden.md:inline-flex 110.0x36.0 bg #c4c4c4 r 3.35544e+07px | a.hidden.md:inline-flex 110.0x36.0 bg #ffffff r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.hidden.md:inline-flex 110.0x36.0 bg #c4c4c4 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### edu-cta

Education CTA. The Request-Education-access mailto link; measured never followed.

Page: home. Selector: `"Request Education access"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 191.23 x 36 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #2c5cff | #5a65ff | = | #5a65ff |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 12px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 191.2x36.0 bg #2c5cff r 3.35544e+07px | a.inline-flex.items-center 191.2x36.0 bg #5a65ff r 3.35544e+07px | a.inline-flex.items-center 191.2x36.0 bg #2c5cff r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.inline-flex.items-center 191.2x36.0 bg #5a65ff r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Testimonials

#### social-card

Testimonial card. A "Created with Endless Tools" social post card in the carousel.

Page: home. Selector: `testimonial card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 355.38 |
| Padding | 15px |
| Border | none |
| Radius | 12px |
| Background | #080808 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #373737 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.flex.items-center: Inter 12px/14px 500, #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | div.w-full.p-[15px] 390.0x355.4 bg #080808 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #373737 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; div.w-[54px].h-[54px] 54.0x54.0 bg #373737 r 3.35544e+07px; div.relative.ring-1 360.0x210.4 r 7px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #373737 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `social-card-default.png`.

#### carousel-prev

Carousel prev. The round 40px Previous arrow of the testimonial carousel.

Page: home. Selector: `button[aria-label=Previous]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #0a0a0a @ 0.5 | #0a0a0a @ 0.8 | = | #0a0a0a @ 0.8 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hidden.md:flex 40.0x40.0 bg #0a0a0a @ 0.5 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.hidden.md:flex 40.0x40.0 bg #0a0a0a @ 0.8 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.hidden.md:flex 40.0x40.0 bg #0a0a0a @ 0.5 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.15 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #005fcc offset 0px | button.hidden.md:flex 40.0x40.0 bg #0a0a0a @ 0.8 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.4 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: none.

#### promo-card

Floating promo card. The fixed bottom-centre testimonial pill ("Endless Tools great tool for designers by designers.").

Page: home. Selector: `fixed bottom card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 365.58 x 54 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.truncate.max-w-full: Inter 14px/20px 400, #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | div.pointer-events-auto.relative 365.6x54.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.relative.w-[38px] 38.0x38.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a0a0a 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up body.inter_fe4d0f8a-module__6kuHYW__variable.font-inter bg #000000 |
| How | at rest |

Crops: none.

### Newsletter

#### news-title

Newsletter heading. The "Stay in the loop" heading.

Page: home. Selector: `"Stay in the loop"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 289.8 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/46px 500 |
| Letter spacing | -1.26px |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### news-field

Newsletter field. The "Your email" input; sample text was typed and deleted, nothing sent.

Page: home. Selector: `newsletter email field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 310 x 35 | = | = |
| Padding | 0px 20px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #1e1e1e | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #373737 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = |
| Font | Inter 12px/14px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff @ 0.5, opacity 1 | = | = |
| Painted layers | input.h-[35px].text-[16px] 310.0x35.0 bg #1e1e1e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #373737 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: none.

#### news-consent

Consent checkbox. The "I agree to the Privacy Policy" checkbox (peer-checked swaps its fill white); checked as a local toggle — the form was never submitted.

Page: home. Selector: `label[aria-invalid] consent box`. States: default, selected.

| Property | default | selected |
|---|---|---|
| Size (w x h) | 18 x 18 | = |
| Padding | 0px | = |
| Border | 1px solid #959595 | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | #ffffff |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #959595 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | label.border-current.border 18.0x18.0 border T:1px solid #959595 / R:1px solid #959595 / B:1px solid #959595 / L:1px solid #959595 r 3.35544e+07px | label.border-current.border 18.0x18.0 bg #ffffff border T:1px solid #959595 / R:1px solid #959595 / B:1px solid #959595 / L:1px solid #959595 r 3.35544e+07px |
| How | at rest | own toggle |

Crops: none.

#### news-submit

Newsletter submit. The "Stay updated" submit; measured, never pressed (a press would subscribe).

Page: home. Selector: `"Stay updated"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 310 x 35 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #ffffff @ 0.85 | = | #ffffff @ 0.85 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 12px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.h-[35px].text-[16px] 310.0x35.0 bg #ffffff r 3.35544e+07px | button.h-[35px].text-[16px] 310.0x35.0 bg #ffffff @ 0.85 r 3.35544e+07px | button.h-[35px].text-[16px] 310.0x35.0 bg #ffffff r 3.35544e+07px outline 1px auto #005fcc offset 0px | button.h-[35px].text-[16px] 310.0x35.0 bg #ffffff @ 0.85 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Footer

#### footer

Footer. The page footer: social links, legal links, contact mailto and the ©EndlessTools line.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 319 |
| Padding | 150px 0px 75px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/18px 400 |
| Letter spacing | normal |
| Colour | #959595 |
| Text node | a.hover:text-white.transition: Inter 14px/18px 400, #959595 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### footer-link

Footer link. A legal link in the footer.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.28 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #959595 | #ffffff | = | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.hover:text-white.transition 92.3x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: none.

#### social-link

Social link. A social link in the footer Get-in-touch block; measured never followed.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.92 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #959595 | #ffffff | = | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.hover:text-white.transition 65.9x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: none.

### Log in (app host)

#### login-card

Login card. The centred 450px login card: a 5%-white fill at a 20px radius on the #0a0a0a field; never filled or submitted.

Page: login. Selector: `login card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 497 |
| Padding | 50px |
| Border | none |
| Radius | 20px |
| Background | #efefef @ 0.05 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.text-white.text-center: Inter 23px/25px 500, #efefef |
| Transition | none |
| Cursor | default |
| Icon | 50 x 50, colour #efefef |
| Painted layers | div.w-full.sm:max-w-[450px] 450.0x497.0 bg #efefef @ 0.05 r 20px; input.h-[35px].px-[15px] 350.0x35.0 bg #1e1e1e border T:1px solid #2a2a2a / R:1px solid #2a2a2a / B:1px solid #2a2a2a / L:1px solid #2a2a2a r 10px; button.bg-white.w-full 350.0x35.0 bg #efefef r 10px |
| How | at rest |

Crops: none.

#### login-logo

Login logo. The dot-grid Endless Tools mark above the card title (inline SVG, currentColor).

Page: login. Selector: `login svg mark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 50 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #efefef |
| Transition | none |
| Cursor | default |
| Icon | 50 x 50, colour #efefef |
| How | at rest |

Crops: none.

#### login-title

Login title. "Welcome to Endless Tools!" plus the sign-in-or-create lede.

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 190 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 23px/25px 500 |
| Letter spacing | normal |
| Colour | #efefef |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### login-field

Email field. The email input (secondary fill, grey-2 border); sample text was typed and deleted, nothing sent.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 350 x 35 | = | = |
| Padding | 0px 15px | = | = |
| Border | 1px solid #2a2a2a | 1px solid #373737 | 1px solid #373737 |
| Radius | 10px | = | = |
| Background | #1e1e1e | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 14px/15px 500 | = | = |
| Letter spacing | -0.35px | = | = |
| Colour | #efefef | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #959595, opacity 1 | = | = |
| Painted layers | input.h-[35px].px-[15px] 350.0x35.0 bg #1e1e1e border T:1px solid #2a2a2a / R:1px solid #2a2a2a / B:1px solid #2a2a2a / L:1px solid #2a2a2a r 10px | input.h-[35px].px-[15px] 350.0x35.0 bg #1e1e1e border T:1px solid #373737 / R:1px solid #373737 / B:1px solid #373737 / L:1px solid #373737 r 10px outline 2px solid #000000 @ 0 offset 2px | input.h-[35px].px-[15px] 350.0x35.0 bg #1e1e1e border T:1px solid #373737 / R:1px solid #373737 / B:1px solid #373737 / L:1px solid #373737 r 10px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: none.

#### send-code

Send Code button. The Send-Code submit (white fill); measured, never pressed (a press would send a login code).

Page: login. Selector: `"Send Code"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 35 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #efefef | #efefef @ 0.9 | = | #efefef @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 14px/15px 500 | = | = | = |
| Letter spacing | -0.35px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Inter 14px/15px 500, #000000, ls -0.35px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.bg-white.w-full 350.0x35.0 bg #efefef r 10px | button.bg-white.w-full 350.0x35.0 bg #efefef @ 0.9 r 10px | button.bg-white.w-full 350.0x35.0 bg #efefef r 10px outline 2px solid #000000 @ 0 offset 2px | button.bg-white.w-full 350.0x35.0 bg #efefef @ 0.9 r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### login-switch

Password switch. The "Log in with password" ghost button that swaps the OTP form for the password form; toggled for the password-field reading.

Page: login. Selector: `"Log in with password"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184.98 x 35 | = | = | = |
| Padding | 0px 25px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #2a2a2a | = | #2a2a2a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 14px/15px 500 | = | = | = |
| Letter spacing | -0.35px | = | = | = |
| Colour | #efefef | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.font-medium.tracking-tight 185.0x35.0 bg #2a2a2a r 10px | button.font-medium.tracking-tight 185.0x35.0 r 10px outline 2px solid #000000 @ 0 offset 2px | button.font-medium.tracking-tight 185.0x35.0 bg #2a2a2a r 10px |

Crops: none.

#### login-password-field

Password field. The password input on the password form (after the local switch); focused only, never filled or submitted.

Page: login. Selector: `input[type=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 350 x 35 | = |
| Padding | 0px 15px | = |
| Border | 1px solid #2a2a2a | 1px solid #373737 |
| Radius | 10px | = |
| Background | #1e1e1e | = |
| Box shadow | none | = |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 15px/20px 500 | = |
| Letter spacing | -0.375px | = |
| Colour | #efefef | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #959595, opacity 1 | = |
| Painted layers | input.h-[35px].px-[15px] 350.0x35.0 bg #1e1e1e border T:1px solid #2a2a2a / R:1px solid #2a2a2a / B:1px solid #2a2a2a / L:1px solid #2a2a2a r 10px | input.h-[35px].px-[15px] 350.0x35.0 bg #1e1e1e border T:1px solid #373737 / R:1px solid #373737 / B:1px solid #373737 / L:1px solid #373737 r 10px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: none.

#### login-submit

Log in button. The password form's Log-in submit; measured, never pressed.

Page: login. Selector: `"Log in" submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 35 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #efefef | #efefef @ 0.9 | = | #efefef @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 14px/15px 500 | = | = | = |
| Letter spacing | -0.35px | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Inter 14px/15px 500, #000000, ls -0.35px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.bg-white.w-full 350.0x35.0 bg #efefef r 10px | button.bg-white.w-full 350.0x35.0 bg #efefef @ 0.9 r 10px | button.bg-white.w-full 350.0x35.0 bg #efefef r 10px outline 2px solid #000000 @ 0 offset 2px | button.bg-white.w-full 350.0x35.0 bg #efefef @ 0.9 r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### login-forgot

Forgot password link. The "Forgot your password?" link; measured never followed.

Page: login. Selector: `"Forgot your password?"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 125.39 x 13 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 12px/13px 500 | = | = | = |
| Letter spacing | -0.3px | = | = | = |
| Colour | #959595 | #efefef | = | #efefef |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.font-medium.tracking-tight 125.4x13.0 outline 2px solid #000000 @ 0 offset 2px | = |

Crops: none.

#### login-legal

Legal line. The agree-to-terms line with its underlined Terms and Privacy links.

Page: login. Selector: `login legal line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/13px 400 |
| Letter spacing | normal |
| Colour | #959595 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `login-legal-default.png`.

### Legal documents (app host)

#### legal-header

Legal header. The fixed top bar on the legal pages: logomark left, Sign-in pill right, over a nav gradient.

Page: privacy. Selector: `legal top bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 100 |
| Padding | 0px 15px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#0a0a0a, #0a0a0a @ 0) |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.h-[30px].sm:h-[40px]: Inter 12px/13px 400, #efefef |
| Transition | none |
| Cursor | default |
| Icon | 132 x 40, colour #efefef |
| Painted layers | div.fixed.top-0 1440.0x100.0 image linear-gradient(#0a0a0a, #0a0a0a @ 0); a.h-[30px].sm:h-[40px] 98.4x40.0 bg #2a2a2a r 10px |
| How | at rest |

Crops: none.

#### legal-signin

Sign in link. The Sign-in pill in the legal header; measured never followed.

Page: privacy. Selector: `"Sign in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98.44 x 40 | = | = | = |
| Padding | 0px 30px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #2a2a2a | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 12px/13px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #efefef | #efefef @ 0.75 | = | #efefef @ 0.75 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.h-[30px].sm:h-[40px] 98.4x40.0 bg #2a2a2a r 10px | = | a.h-[30px].sm:h-[40px] 98.4x40.0 bg #2a2a2a r 10px outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### legal-title

Legal title. The document title ("Privacy Policy").

Page: privacy. Selector: `legal h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656.09 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 42px/40px 400 |
| Letter spacing | normal |
| Colour | #efefef |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### legal-content

Legal content. The document body (the .et-content column): 14px grey-4 text with white emphasis spans.

Page: privacy. Selector: `.et-content`. States: .

Not found on the page at capture time.

#### legal-link

Legal link. An inline document link (underlined); measured never followed.

Page: privacy. Selector: `legal doc a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171.05 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #efefef @ 0.75 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 171.0x20.0 outline 2px solid #000000 @ 0 offset 2px | = |

Crops: none.

### Mobile (390 wide)

#### m-header

Mobile header. The sticky bar at 390: logomark plus the white Start-for-free pill (the Log-in link hides at this width).

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#000000 14.73%, #000a0a @ 0 100%) |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | button.md:hidden.inline-flex: Inter 12px/14px 500, #0a0a0a |
| Transition | none |
| Cursor | default |
| Painted layers | div.sticky.inset-x-0 390.0x78.0 image linear-gradient(#000000 14.73%, #000a0a @ 0 100%); a.hidden.md:inline-flex 0.0x0.0 bg #1e1e1e @ 0.8 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #959595 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; a.hidden.md:inline-flex 0.0x0.0 bg #ffffff r 3.35544e+07px; button.md:hidden.inline-flex 113.2x38.0 bg #ffffff r 3.35544e+07px |
| Ancestor paint | 1 up body.inter_fe4d0f8a-module__6kuHYW__variable.font-inter bg #000000 |
| How | at rest |

Crops: none.

#### m-cta

Mobile nav CTA. The Start-for-free button at 390 (a button, not an anchor, at this width).

Page: mobile. Selector: `"Start for free" at 390`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.22 x 38 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(16px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Inter 12px/14px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.md:hidden.inline-flex 113.2x38.0 bg #ffffff r 3.35544e+07px | = | button.md:hidden.inline-flex 113.2x38.0 bg #ffffff r 3.35544e+07px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### m-hero

Mobile headline. The hero at 390: title-secondary size with the same circle/underline marks.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 330 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/26px 500 |
| Letter spacing | -0.72px |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | span.block.bg-current 135.0x36.5 bg #ffffff; span.block.bg-current 0.0x0.0 bg #ffffff; span.block.bg-current 150.0x5.5 bg #ffffff; span.block.bg-current 0.0x0.0 bg #ffffff |
| How | at rest |

Crops: none.

#### m-asset-card

Mobile asset title. An input-source heading in the stacked mobile layout.

Page: mobile. Selector: `asset h2 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 135.05 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 24px/26px 500 |
| Letter spacing | -0.72px |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: none.

#### m-plan-card

Mobile plan card. A plan card in the horizontally scrolling pricing row at 390.

Page: mobile. Selector: `plan card at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 331.5 x 576 |
| Padding | 15px |
| Border | none |
| Radius | 33px |
| Background | #121212 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.ring-1.ring-[#222222]: Inter 14px/35px 500, #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Painted layers | div.ring-1.ring-[#222222] 331.5x576.0 bg #121212 r 33px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; div.ring-1.ring-[#222222] 64.2x35.0 bg #121212 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #222222 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.block.bg-current 350.0x139.7 bg #ffffff; span.block.bg-current 0.0x0.0 bg #ffffff; a.hidden.md:inline-flex 0.0x0.0 bg #ffffff r 3.35544e+07px; button.inline-flex.md:hidden 301.5x36.0 bg #ffffff r 3.35544e+07px |
| How | at rest |

Crops: none.

## Transitions declared in the readable stylesheets

endlesstools.io and app.endlesstools.io serve their Next.js CSS bundles same-origin, so this list holds the transitions and keyframe animations the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- home: none

- login: none
