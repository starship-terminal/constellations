# Component measurements

Computed styles read from b150.ai on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chrome at 1440 x 900 (the Mobile group at 390 x 844) in the site's one painted theme — no join, submission or login was ever performed and any consent or promo layer was hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The top bar: wordmark, VIBEATHON/EVENTS/JOBS/MARKETPLACE/TALENT/FREE RESOURCES nav, LOGIN, SIGN UP.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 10px/15px 500 |
| Letter spacing | -0.3px |
| Colour | #1f1915 |
| Text node | span.vibeathon-char: Fragment Mono 10px/13.33px 700, #a3b2af, ls 0.3px |
| Transition | none |
| Icon | 30 x 10, colour #fffdf6 |
| Painted layers | a.label.ml-1 79.4x40.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px; div.border-t.border-rule 0.0x0.0 bg #f2efe9 border T:1px solid #e6e3dd; a.label.mt-3 0.0x0.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px |
| Ancestor paint | 1 up body.min-h-dvh.bg-paper bg #f2efe9 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The wordmark link back to /.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 30 x 10 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 10px/15px 500 |
| Letter spacing | -0.3px |
| Colour | #fffdf6 |
| Transition | none |
| Cursor | pointer |
| Icon | 30 x 10, colour #fffdf6 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A top-level nav link (EVENTS). Measured, never followed.

Page: home. Selector: `header a:has-text("EVENTS")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 38.89 x 13.33 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Fragment Mono 10px/13.33px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #fffdf6 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.6 | = | 0.6 |
| Painted layers | - | = | a.label.transition-opacity 38.9x13.3 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### login-link

Login link. LOGIN in the header, pointing at app.b150.ai — the app gate rate-limits; measured, never followed.

Page: home. Selector: `a[href="https://app.b150.ai"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32.41 x 13.33 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Fragment Mono 10px/13.33px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #fffdf6 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.6 | = | 0.6 |
| Painted layers | - | = | a.label.transition-opacity 32.4x13.3 outline 1px auto #005fcc offset 1px | = |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### signup-btn

Sign Up button. The SIGN UP pill to app.b150.ai/auth/signup. Measured, never followed.

Page: home. Selector: `header a:has-text("SIGN UP")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.38 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #e6e3dd | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #f2efe9 | = | #f2efe9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Fragment Mono 10px/13.33px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #1f1915 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.label.ml-1 79.4x40.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | a.label.ml-1 79.4x40.0 bg #f2efe9 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | a.label.ml-1 79.4x40.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.label.ml-1 79.4x40.0 bg #f2efe9 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-btn-default.png`, `signup-btn-hover.png`, `signup-btn-focus-visible.png`, `signup-btn-pressed.png`.

### Home

#### hero

Hero heading. "Don't wait for the future. Build it."

Page: home. Selector: `main h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 740 x 335.86 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 120px/111.96px 400 |
| Letter spacing | -8px |
| Colour | #f7f5f1 |
| Transition | none |
| How | at rest |

Crops: `hero-default.png`.

#### hero-cta

Hero CTA. JOIN THE BETA — the primary call-to-action. Measured, never followed.

Page: home. Selector: `:has-text("JOIN THE BETA")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 126.25 x 41 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #e6e3dd | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fffdf6 | #e6e3dd | = | #e6e3dd |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Fragment Mono 10px/13.33px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #1f1915 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.label.inline-flex 126.3x41.0 bg #fffdf6 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | a.label.inline-flex 126.3x41.0 bg #e6e3dd border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | a.label.inline-flex 126.3x41.0 bg #fffdf6 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.label.inline-flex 126.3x41.0 bg #e6e3dd border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### home-section

Home section. A content section below the hero.

Page: home. Selector: `main section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 968.98 |
| Padding | 80px 0px |
| Gap | 40px |
| Border | none |
| Radius | 0px |
| Background | #f2efe9 |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 10px/15px 500 |
| Letter spacing | -0.3px |
| Colour | #1f1915 |
| Text node | span.label.leading-3: Fragment Mono 10px/12px 400, #1f1915, ls 0.3px |
| Transition | none |
| Icon | 15 x 15, colour #1f1915 |
| Painted layers | section.relative.z-[2] 1440.0x969.0 bg #f2efe9; div.inline-flex.items-center 181.1x34.0 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 24px; img.block.h-auto 1024.0x519.0 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.03 0px 7px 20px 20px |
| How | at rest |

Crops: `home-section-default.png`.

### Vibeathon

#### vibe-title

Vibeathon title.

Page: vibeathon. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1220 x 439.61 |
| Padding | 0px |
| Gap | normal 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 10px/15px 500 |
| Letter spacing | -0.3px |
| Colour | #1f1915 |
| Text node | span.block.text-[32px]: Geist Variable 96px/87.936px 500, #1f1915, ls -3px |
| Transition | none |
| Icon | 100 x 100, colour #fa725a |
| How | at rest |

Crops: `vibe-title-default.png`.

#### vibe-card

Vibeathon block. The first card/section on the vibeathon page.

Page: vibeathon. Selector: `main [class*="card"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 920.61 |
| Padding | 103px 0px 80px 0px |
| Border | none |
| Radius | 0px |
| Background | #f2efe9 |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 10px/15px 500 |
| Letter spacing | -0.3px |
| Colour | #1f1915 |
| Text node | span.label.leading-3: Fragment Mono 10px/12px 400, #1f1915, ls 0.3px |
| Transition | none |
| Icon | 15 x 15, colour #1f1915 |
| Painted layers | section.bg-paper.pt-[55px] 1440.0x920.6 bg #f2efe9; div.inline-flex.items-center 116.3x34.0 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 24px |
| How | at rest |

Crops: `vibe-card-default.png`.

#### vibe-cta

Vibeathon CTA. The first call-to-action on /vibeathon. Measured, never followed.

Page: vibeathon. Selector: `main a:has-text("join")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52.53 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Geist Variable 12px/20.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1f1915 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-ink.underline 52.5x16.0 outline 1px auto #005fcc offset 1px | = |

Crops: `vibe-cta-default.png`, `vibe-cta-hover.png`, `vibe-cta-focus-visible.png`, `vibe-cta-pressed.png`.

### Talent

#### talent-title

Talent title.

Page: talent. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 740 x 334.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 120px/111.6px 400 |
| Letter spacing | -8px |
| Colour | #f7f5f1 |
| Transition | none |
| How | at rest |

Crops: `talent-title-default.png`.

#### talent-card

Talent card. A talent/profile card on the talent surface. Measured, never followed.

Page: talent. Selector: `main [class*="card"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 512 x 700 | = |
| Padding | 40px | = |
| Gap | 40px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #e6e3dd | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist Variable 10px/15px 500 | = |
| Letter spacing | -0.3px | = |
| Colour | #1f1915 | = |
| Text node | p.label.leading-3: Fragment Mono 10px/12px 400, #1f1915, ls 0.3px | = |
| Transition | none | = |
| Painted layers | article.flex.w-full 512.0x700.0 bg #e6e3dd r 8px; div.relative.w-full 432.0x403.2 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 16px; div.pointer-events-none.absolute 430.0x200.6 image linear-gradient(to top, #e6e3dd 0%, #000000 @ 0 100%) | = |
| How | at rest | mouse hover |

Crops: `talent-card-default.png`, `talent-card-hover.png`.

#### talent-cta

Talent CTA. The first call-to-action on /talent. Measured, never followed.

Page: talent. Selector: `main a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.81 x 41 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #e6e3dd | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fffdf6 | #e6e3dd | = | #e6e3dd |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Fragment Mono 10px/13.33px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #1f1915 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.label.inline-flex 106.8x41.0 bg #fffdf6 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | a.label.inline-flex 106.8x41.0 bg #e6e3dd border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | a.label.inline-flex 106.8x41.0 bg #fffdf6 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.label.inline-flex 106.8x41.0 bg #e6e3dd border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.h-full bg #fffdf6 @ 0.64 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `talent-cta-default.png`, `talent-cta-hover.png`, `talent-cta-focus-visible.png`, `talent-cta-pressed.png`.

### Free resources

#### res-title

Resources title.

Page: resources. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1220 x 263.77 |
| Padding | 0px |
| Gap | normal 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 96px/87.936px 500 |
| Letter spacing | -3px |
| Colour | #1f1915 |
| Text node | span.is-in: Geist Variable 96px/87.936px 500, #1f1915, ls -3px |
| Transition | none |
| How | at rest |

Crops: `res-title-default.png`.

#### res-card

Resource card. A free-resource card. Measured, never followed.

Page: resources. Selector: `main [class*="card"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 412.8 x 595.72 | = |
| Padding | 0px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist Variable 10px/15px 500 | = |
| Letter spacing | -0.3px | = |
| Colour | #1f1915 | = |
| Text node | h2.label: Fragment Mono 10px/13.33px 400, #1f1915, ls 0.3px | = |
| Transition | none | = |
| Painted layers | div.h-[360px].overflow-hidden 412.8x493.0 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 16px; a.label.inline-flex 123.8x41.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | = |
| How | at rest | mouse hover |

Crops: `res-card-default.png`, `res-card-hover.png`.

### About

#### about-title

About title.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1220 x 263.77 |
| Padding | 0px |
| Gap | normal 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 96px/87.936px 500 |
| Letter spacing | -3px |
| Colour | #1f1915 |
| Text node | span.is-in: Geist Variable 96px/87.936px 500, #1f1915, ls -3px |
| Transition | none |
| How | at rest |

Crops: `about-title-default.png`.

#### about-body

About body. A body-copy block on /about.

Page: about. Selector: `main p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 540 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 32px/36px 500 |
| Letter spacing | -1px |
| Colour | #1f1915 |
| Transition | opacity, transform 0.9s, 0.9s cubic-bezier(0.25, 1, 0.5, 1), cubic-bezier(0.25, 1, 0.5, 1) |
| How | at rest |

Crops: `about-body-default.png`.

### Contact

#### contact-title

Contact title.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300.13 x 111.95 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 120px/111.96px 400 |
| Letter spacing | -8px |
| Colour | #1f1915 |
| Transition | opacity, transform 0.9s, 0.9s cubic-bezier(0.25, 1, 0.5, 1), cubic-bezier(0.25, 1, 0.5, 1) delay 0.1s |
| How | at rest |

Crops: `contact-title-default.png`.

#### contact-input

Contact field. A contact form field; focused only, never submitted.

Page: contact. Selector: `input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 300 x 56 | = |
| Padding | 0px 16px | = |
| Border | 1px solid #e6e3dd | 1px solid #1f1915 @ 0.32 |
| Radius | 8px | = |
| Background | #e6e3dd | #f7f5f1 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist Variable 12px/18px 500 | = |
| Letter spacing | -0.3px | = |
| Colour | #1f1915 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #1f1915 @ 0.48, opacity 1 | = |
| Painted layers | input.block.w-full 300.0x56.0 bg #e6e3dd border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 8px | input.block.w-full 300.0x56.0 bg #f7f5f1 border T:1px solid #1f1915 @ 0.32 / R:1px solid #1f1915 @ 0.32 / B:1px solid #1f1915 @ 0.32 / L:1px solid #1f1915 @ 0.32 r 8px |
| How | at rest | clicked into the field |

Crops: `contact-input-default.png`, `contact-input-focused.png`.

#### contact-button

Contact button. The submit; measured except a real press — the form was never submitted.

Page: contact. Selector: `button[type="submit"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 111.77 x 40 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #e6e3dd | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #ffffff | #f2efe9 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | Fragment Mono 10px/13.33px 400 | = | = |
| Letter spacing | 0.3px | = | = |
| Colour | #1f1915 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.label.inline-flex 111.8x40.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | button.label.inline-flex 111.8x40.0 bg #f2efe9 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | button.label.inline-flex 111.8x40.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px outline 1px auto #005fcc offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `contact-button-default.png`, `contact-button-hover.png`, `contact-button-focus-visible.png`.

#### contact-email

Contact email field. The email input; focused only, never submitted.

Page: contact. Selector: `input[type="email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 300 x 56 | = |
| Padding | 0px 16px | = |
| Border | 1px solid #e6e3dd | 1px solid #1f1915 @ 0.32 |
| Radius | 8px | = |
| Background | #e6e3dd | #f7f5f1 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist Variable 12px/18px 500 | = |
| Letter spacing | -0.3px | = |
| Colour | #1f1915 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #1f1915 @ 0.48, opacity 1 | = |
| Painted layers | input.block.w-full 300.0x56.0 bg #e6e3dd border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 8px | input.block.w-full 300.0x56.0 bg #f7f5f1 border T:1px solid #1f1915 @ 0.32 / R:1px solid #1f1915 @ 0.32 / B:1px solid #1f1915 @ 0.32 / L:1px solid #1f1915 @ 0.32 r 8px |
| How | at rest | clicked into the field |

Crops: `contact-email-default.png`, `contact-email-focused.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1063.78 |
| Padding | 0px 0px 48px 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 10px/15px 500 |
| Letter spacing | -0.3px |
| Colour | #fffdf6 |
| Text node | p.mt-12.max-w-[230px]: Geist Variable 12px/20.4px 400, #fffdf6, ls -0.3px |
| Transition | none |
| Icon | 30 x 10, colour #fffdf6 |
| Painted layers | footer.relative.z-[2] 1440.0x1063.8 bg #000000; div.border-b.border-light/16 1376.0x1.0 border B:1px solid #fffdf6 @ 0.16; a.label.mt-6 100.3x41.0 bg #fffdf6 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px |
| Ancestor paint | 1 up body.min-h-dvh.bg-paper bg #f2efe9 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.33 x 41 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | 1px solid #e6e3dd | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fffdf6 | #e6e3dd | = | #e6e3dd |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Fragment Mono 10px/13.33px 400 | = | = | = |
| Letter spacing | 0.3px | = | = | = |
| Colour | #1f1915 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.label.mt-6 100.3x41.0 bg #fffdf6 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | a.label.mt-6 100.3x41.0 bg #e6e3dd border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px | a.label.mt-6 100.3x41.0 bg #fffdf6 border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.label.mt-6 100.3x41.0 bg #e6e3dd border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 65 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 10px/15px 500 |
| Letter spacing | -0.3px |
| Colour | #1f1915 |
| Transition | none |
| Icon | 30 x 10, colour #1f1915 |
| Painted layers | a.label.ml-1 0.0x0.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px; div.border-t.border-rule 0.0x0.0 bg #f2efe9 border T:1px solid #e6e3dd; a.label.mt-3 0.0x0.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px |
| Ancestor paint | 1 up body.min-h-dvh.bg-paper bg #f2efe9 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `header button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | Geist Variable 10px/15px 500 | = | = | = |
| Letter spacing | -0.3px | = | = | = |
| Colour | #1f1915 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #1f1915 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.grid.size-10 40.0x40.0 outline 1px auto #e59700 offset 0px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The menu button after its own toggle; the crop is the open menu layer.

Page: home. Selector: `header button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 10px/15px 500 |
| Letter spacing | -0.3px |
| Colour | #1f1915 |
| Transition | none |
| Cursor | default |
| Icon | 0 x 0, colour #1f1915 |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. A row inside the opened menu.

Page: home. Selector: `nav a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 29.33 |
| Padding | 8px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fragment Mono 10px/13.33px 700 |
| Letter spacing | 0.3px |
| Colour | #1f1915 |
| Text node | span.vibeathon-char: Fragment Mono 10px/13.33px 700, #9ea4a8, ls 0.3px |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-nav-link-default.png`.

#### m-cta

Mobile CTA. A JOIN/SIGN UP button on mobile.

Page: home. Selector: `a:has-text("JOIN")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 79.38 x 40 |
| Padding | 0px 16px |
| Border | 1px solid #e6e3dd |
| Radius | 3.35544e+07px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Fragment Mono 10px/13.33px 400 |
| Letter spacing | 0.3px |
| Colour | #1f1915 |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.label.mt-3 79.4x40.0 bg #ffffff border T:1px solid #e6e3dd / R:1px solid #e6e3dd / B:1px solid #e6e3dd / L:1px solid #e6e3dd r 3.35544e+07px |
| How | at rest |

Crops: `m-cta-default.png`.

## Transitions declared in the readable stylesheets

b150.ai serves its stylesheets from b150.ai itself, so the CSSOM could read nearly every rule on each page. The per-state Transition rows above are computed values and cover those rules too.

- home: `opacity 0.3s`, `transform 0.3s`, `none`
