# Component measurements

Computed styles read from www.bezi.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one dark theme (no consent overlay mounts on these routes), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The floating dark pill bar: the Bezi mark, the nav links (Studios, Product, Pricing, Blog, Docs, Discord) and nothing else on it.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1124 x 80 |
| Padding | 12px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-rawiid: Inter 16px/22.4px 400, #ffffff, ls -0.32px |
| Transition | none |
| Painted layers | div.framer-1fwn1h2 1100.0x56.0 bg #1f1f1f @ 0.84 r 144px; div.framer-y8aqqb 154.0x39.0 bg #f84503 r 102.93px; div.framer-78e73s 9.0x6.0 image url(data:…)%22></path></svg>") |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `header a:first`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 107 x 18.92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link.

Page: home. Selector: `a:has-text("Pricing")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.42 x 38.41 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | h6.framer-text.framer-styles-preset-rawiid: Inter 16px/22.4px 400, #ffffff, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-Ae6d7.framer-t46sH 66.4x38.4 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-discord

Discord link.

Page: home. Selector: `a:has-text("Discord")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.92 x 38.41 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | h6.framer-text.framer-styles-preset-rawiid: Inter 16px/22.4px 400, #ffffff, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-Ae6d7.framer-t46sH 71.9x38.4 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-discord-default.png`, `nav-discord-hover.png`, `nav-discord-focus-visible.png`, `nav-discord-pressed.png`.

#### hero-title

Hero title. "AI for building real games" in the display face.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 51.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | The Future Medium 53px/51.94px 500 |
| Letter spacing | -1.59px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subcopy.

Page: home. Selector: `first long paragraph under h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1100 x 43.19 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 16px/21.6px 400, #ffffff @ 0.5 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### cta

TRY FOR FREE button. The orange CTA repeated across the page. Measured, never followed.

Page: home. Selector: `ancestor of the TRY FOR FREE text that holds the orange fill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154 x 39 | = | = | = |
| Padding | 14.04px | = | = | = |
| Gap | 7.8px | = | = | = |
| Border | none | = | = | = |
| Radius | 102.93px | = | = | = |
| Background | #f84503 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Space Mono 14px/14px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.framer-y8aqqb 154.0x39.0 bg #f84503 r 102.93px; div.framer-78e73s 9.0x6.0 image url(data:…)%22></path></svg>") | = | div.framer-y8aqqb 154.0x39.0 bg #f84503 r 102.93px; a 102.8x14.0 outline 1px auto #005fcc offset 1px; div.framer-78e73s 9.0x6.0 image url(data:…)%22></path></svg>") | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-default.png`, `cta-hover.png`, `cta-focus-visible.png`, `cta-pressed.png`.

#### announcement

Announcement line. The "NEW · Bezi for Unreal Engine is now publicly available" strip under the header.

Page: home. Selector: `anchor of the leaf text "publicly available"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 643.88 x 32.2 |
| Padding | 8px 12px 8px 8px |
| Gap | 12px |
| Border | none |
| Radius | 2px |
| Background | #1c1c1c |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | p.framer-text: Space Mono 11px/13.2px 700, #ff9366, ls 0.22px |
| Transition | none |
| Cursor | pointer |
| Icon | 9 x 9, colour #0000ee, fill #000000 |
| ::after | 643.875px x 32.2031px, absolute, bg #000000 @ 0, radius 2px |
| Painted layers | a.framer-lLMlS.framer-1wm8qt7 643.9x32.2 bg #1c1c1c r 2px; a::after.framer-lLMlS.framer-1wm8qt7 643.875pxx32.2031px border T:1px solid #292929 / R:1px solid #292929 / B:1px solid #292929 / L:1px solid #292929 r 2px |
| How | at rest |

Crops: `announcement-default.png`.

#### section-title

Section title.

Page: home. Selector: `first visible h2, marked where it mounts`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 444 x 35.89 |
| Padding | 0px 0px 14px 0px |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.05; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 19px/20.9px 700 |
| Letter spacing | -0.57px |
| Colour | #f4f1ea |
| Transition | none |
| Painted layers | h2 444.0x35.9 border B:1px solid #ffffff @ 0.05 |
| How | at rest |

Crops: `section-title-default.png`.

#### tools-button

Connected tools chip. The "02. CONNECTED TOOLS" index button on the home page.

Page: home. Selector: `button:has-text("CONNECTED TOOLS")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.8 x 142.5 | 124 x 150 | 124 x 150 | 124 x 150 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 8px | = |
| Font | The Future Mono 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f2f1ec | = | = | = |
| Text node | span.pcfm-stage-number: The Future Mono 10px/10px 400, #f2f1ec @ 0.32, ls 1.35px | span.pcfm-stage-number: The Future Mono 10px/10px 400, #ffffff, ls 1.35px | span.pcfm-stage-number: The Future Mono 10px/10px 400, #ffffff, ls 1.35px | span.pcfm-stage-number: The Future Mono 10px/10px 400, #ffffff, ls 1.35px |
| Transition | opacity, transform, color 0.18s, 0.42s, 0.18s ease, cubic-bezier(0.2, 0.8, 0.2, 1), ease delay 0s, 0s, 0s | = | = | = |
| Transform | matrix(0.95, 0, 0, 0.95, 0, 0) | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, 0) | matrix(1, 0, 0, 1, 0, 0) |
| Opacity | 0.55 | - | - | - |
| Cursor | pointer | = | = | = |
| Icon | 23.75 x 23.75, colour #f2f1ec, fill #000000 | 25 x 25, colour #f2f1ec, fill #000000 | 25 x 25, colour #f2f1ec, fill #000000 | 25 x 25, colour #f2f1ec, fill #000000 |
| Painted layers | span.pcfm-corner.pcfm-tl 19.0x19.0 border T:1px solid #f2f1ec @ 0.32 / L:1px solid #f2f1ec @ 0.32; span.pcfm-corner.pcfm-tr 19.0x19.0 border T:1px solid #f2f1ec @ 0.32 / R:1px solid #f2f1ec @ 0.32; span.pcfm-corner.pcfm-bl 19.0x19.0 border B:1px solid #f2f1ec @ 0.32 / L:1px solid #f2f1ec @ 0.32; span.pcfm-corner.pcfm-br 19.0x19.0 border R:1px solid #f2f1ec @ 0.32 / B:1px solid #f2f1ec @ 0.32 | span.pcfm-corner.pcfm-tl 26.0x26.0 border T:1px solid #ffffff / L:1px solid #ffffff; span.pcfm-corner.pcfm-tr 26.0x26.0 border T:1px solid #ffffff / R:1px solid #ffffff; span.pcfm-corner.pcfm-bl 26.0x26.0 border B:1px solid #ffffff / L:1px solid #ffffff; span.pcfm-corner.pcfm-br 26.0x26.0 border R:1px solid #ffffff / B:1px solid #ffffff | button.pcfm-stage 124.0x150.0 outline 1px solid #ffffff offset 8px; span.pcfm-corner.pcfm-tl 26.0x26.0 border T:1px solid #ffffff / L:1px solid #ffffff; span.pcfm-corner.pcfm-tr 26.0x26.0 border T:1px solid #ffffff / R:1px solid #ffffff; span.pcfm-corner.pcfm-bl 26.0x26.0 border B:1px solid #ffffff / L:1px solid #ffffff; span.pcfm-corner.pcfm-br 26.0x26.0 border R:1px solid #ffffff / B:1px solid #ffffff | span.pcfm-corner.pcfm-tl 26.0x26.0 border T:1px solid #ffffff / L:1px solid #ffffff; span.pcfm-corner.pcfm-tr 26.0x26.0 border T:1px solid #ffffff / R:1px solid #ffffff; span.pcfm-corner.pcfm-bl 26.0x26.0 border B:1px solid #ffffff / L:1px solid #ffffff; span.pcfm-corner.pcfm-br 26.0x26.0 border R:1px solid #ffffff / B:1px solid #ffffff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tools-button-default.png`, `tools-button-hover.png`, `tools-button-focus-visible.png`, `tools-button-pressed.png`.

#### view-all

View all link. The blog index link.

Page: home. Selector: `a:has-text("View all")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110.34 x 43.2 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | #ffffff @ 0.2 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Space Mono 16px/19.2px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-18qb6ey.framer-ozzz8l 110.3x43.2 bg #ffffff @ 0.2 r 2px; div 110.3x43.2 bg #09090d @ 0; div 9.4x8.6 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 9.5x8.6 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 9.5x8.6 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 9.5x8.6 bg #f84503 shadow #f84503 0px 0px 0px 1px | a.framer-18qb6ey.framer-ozzz8l 110.3x43.2 bg #ffffff @ 0.2 r 2px; div 110.3x43.2 bg #09090d @ 0; div 15.8x14.4 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 15.8x14.4 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 15.8x14.4 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 15.8x14.4 bg #f84503 shadow #f84503 0px 0px 0px 1px | a.framer-18qb6ey.framer-ozzz8l 110.3x43.2 bg #ffffff @ 0.2 r 2px outline 1px auto #005fcc offset 1px; div 110.3x43.2 bg #09090d @ 0; div 9.4x8.6 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 9.5x8.6 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 9.5x8.6 bg #f84503 shadow #f84503 0px 0px 0px 1px; div 9.5x8.6 bg #f84503 shadow #f84503 0px 0px 0px 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `view-all-default.png`, `view-all-hover.png`, `view-all-focus-visible.png`, `view-all-pressed.png`.

#### page-ground

Page ground. The near-black the whole page paints on.

Page: home. Selector: `body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 7394.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #0d0d0d |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-rawiid: Inter 16px/22.4px 400, #ffffff, ls -0.32px |
| Transition | none |
| Icon | 6.91 x 6.91, colour #0000ee, fill #000000 |
| Painted layers | body 1440.0x7394.4 bg #0d0d0d; div.framer-JYlq6.framer-eFDMz 1440.0x7394.4 bg #0d0d0d; div.framer-1fwn1h2 1100.0x56.0 bg #1f1f1f @ 0.84 r 144px; div.framer-y8aqqb 154.0x39.0 bg #f84503 r 102.93px; div.framer-78e73s 9.0x6.0 image url(data:…)%22></path></svg>"); div.framer-jYJPn.framer-mge2a 0.0x0.0 bg #0d0d0d |
| How | at rest |

Crops: none.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1100 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 64px/70.4px 500 |
| Letter spacing | -2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-cta

Plan CTA. The action inside the Free trial band. Measured, never followed.

Page: pricing. Selector: `ancestor of the plan TRY FOR FREE text that holds the dark fill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.7 x 48 | = | - | = |
| Padding | 12px 20px | = | - | = |
| Gap | 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | #000000 @ 0.84 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sans-serif 12px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span: Space Mono 12px/14.4px 400, #ffffff, ls -0.12px | = | - | = |
| Transition | none | = | - | = |
| Painted layers | a.framer-10cmto.framer-hpy0rr 126.7x48.0 bg #000000 @ 0.84 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-pressed.png`.

#### plan-card

Plan card.

Page: pricing. Selector: `card ancestor of a plan CTA (marked in-page)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366 x 499 |
| Padding | 24px |
| Gap | 28px |
| Border | none |
| Radius | 0px |
| Background | #1a1a1a |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.framer-text: Inter Display 20px/28px 400, #e8e8e8, ls -0.4px |
| Transition | none |
| ::after | 366px x 499px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.framer-cs8h94 366.0x499.0 bg #1a1a1a; div::after.framer-cs8h94 366pxx499px border T:1px solid #ff4c00 / R:1px solid #ff4c00 / B:1px solid #ff4c00 / L:1px solid #ff4c00; div.framer-1j0dkil 109.2x24.0 bg #e34a12; div.framer-1oiror9 2.0x2.0 bg #f84503; div.framer-1kx2bko 2.0x2.0 bg #f84503; div.framer-58ly18 2.0x2.0 bg #f84503 |
| How | at rest |

Crops: `plan-card-default.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 538.31 |
| Padding | 72px 60px 50px 60px |
| Gap | 52px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0.05 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-koaeq7: P-DOT Regular 12px/18px 400, #f2f1ec @ 0.48, ls -0.24px |
| Transition | none |
| Icon | 20 x 20, colour #f2f1ec |
| Painted layers | footer.framer-3q17ch 1440.0x538.3 bg #ffffff @ 0.05 |
| Ancestor paint | 1 up div.framer-JYlq6.framer-eFDMz bg #0d0d0d |
| How | at rest |

Crops: none.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.42 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/22.4px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #f2f1ec | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text 50.4x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | 39.6 x 39.6 | = | = |
| Padding | 8px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #f2f1ec @ 0.08 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #f2f1ec | 22 x 22, colour #f2f1ec | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.1, 0, 0, 1.1, 0, 0) | = | = |
| Painted layers | - | a.framer-1sv7g11.framer-a97pow 39.6x39.6 bg #f2f1ec @ 0.08 | a.framer-1sv7g11.framer-a97pow 36.0x36.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-rating

G2 rating badge. The "4.6 Star Rating" badge linking the G2 review page. Measured, never followed.

Page: home. Selector: `footer a[href*="g2.com"]`. States: .

Not found on the page at capture time.

#### footer-legal

Legal link.

Page: home. Selector: `footer a:has-text("Privacy")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.2 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 16px/22.4px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #f2f1ec | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text 100.2x20.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-legal-default.png`, `footer-legal-hover.png`, `footer-legal-focus-visible.png`, `footer-legal-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 79 |
| Padding | 16px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 18px/21.6px 500, #ffffff |
| Transition | none |
| Painted layers | div.framer-1fwn1h2 358.0x54.0 bg #1f1f1f @ 0.84 r 24px; div.framer-e4qup6 14.0x1.0 bg #ffffff; div.framer-17jh2g6 14.0x1.0 bg #ffffff; div.framer-19mnz16 14.0x1.0 bg #ffffff; a.framer-1kb1wws.framer-5xbmuq 326.0x48.0 bg #ff4d00 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button. The 36px trigger at the right of the mobile bar; its own press opens the menu overlay.

Page: home. Selector: `header div[cursor=pointer] at right`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 14 x 14 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.framer-e4qup6 14.0x1.0 bg #ffffff; div.framer-17jh2g6 14.0x1.0 bg #ffffff; div.framer-19mnz16 14.0x1.0 bg #ffffff | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The trigger after its own toggle; the open overlay shows in the crop.

Page: home. Selector: `mobile menu trigger`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 14 x 14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.framer-e4qup6 10.6x10.6 bg #ffffff; div.framer-17jh2g6 14.0x1.0 bg #ffffff; div.framer-19mnz16 10.6x10.6 bg #ffffff |
| Ancestor paint | 2 up header.framer-UYLLm.framer-soqjxm shadow #000000 @ 0.1 0px 7.14px 20px 0px |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `opacity 0.4s ease-out`, `unset`, `opacity 600ms`, `opacity 180ms, transform 420ms cubic-bezier(0.2, 0.8, 0.2, 1), color 180ms`, `width 320ms, height 320ms, border-color 180ms`, `opacity 180ms, color 180ms`
