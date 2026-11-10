# Component measurements

Computed styles read from aboardhr.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Top navigation bar. The floating nav: logo, Product / Price / Resources links and the Sign-in / Book-a-demo actions.

Page: home. Selector: `[data-framer-name=Desktop]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 90 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #171717 @ 0.08 0px 0px 0px 0px |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: system-ui 15px/30px 500, #3c3c3f @ 0.7, ls -0.15px |
| Transition | none |
| Icon | 83 x 29, colour #0000ee, fill #000000 |
| Painted layers | nav.framer-tBKbW.framer-1mi7pyh 1440.0x90.0 shadow #171717 @ 0.08 0px 0px 0px 0px; div.framer-j9s7nw 1440.0x64.0 bg #ffffff @ 0 image linear-gradient(#ffffff @ 0 0%, #ffffff @ 0 100%) |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-logo

Logo. The Aboard wordmark linking home.

Page: home. Selector: `nav logo a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111 x 29 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 83 x 29, colour #0000ee, fill #000000 | = | = | 83 x 29, colour #ff0000, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-11t902d.framer-1r3p545 111.0x29.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-logo-default.png`, `nav-logo-hover.png`, `nav-logo-focus-visible.png`, `nav-logo-pressed.png`.

#### nav-link

Nav link. A section link in the top bar.

Page: home. Selector: `nav a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.55 x 38 | = | - | = |
| Padding | 4px 10px | = | - | = |
| Gap | 10px | = | - | = |
| Border | none | = | - | = |
| Radius | 12px | = | - | = |
| Background | transparent | #707079 @ 0.08 | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sans-serif 12px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | p.framer-text: system-ui 15px/30px 500, #3c3c3f @ 0.7, ls -0.15px | p.framer-text: system-ui 15px/30px 500, #262626 @ 0.996, ls -0.15px | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Painted layers | - | a.framer-1tXqu.framer-1a3dznk 74.5x38.0 bg #707079 @ 0.08 r 12px | = | = |
| Error | - | = | keyboard focus failed | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-pressed.png`.

#### nav-cta

Nav CTA. The boxed action at the right of the nav (Sign in / Book a demo). Hovered and focused only; app.aboardhr.com is never opened.

Page: home. Selector: `nav cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.86 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | color(display-p3 0.89 0.946 0.99) | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, color(display-p3 0.0014 0.5301 0.8827), ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 bg color(display-p3 0.89 0.946 0.99) r 99px | = | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 bg color(display-p3 0.89 0.946 0.99) r 99px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### footer

Footer. The "Smooth sailing" footer band: link columns (Price / What's new / Help center / legal) and the Teamtailor credit row.

Page: home. Selector: `footer band`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 128 |
| Padding | 0px 0px 40px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h5.framer-text: system-ui 20px/30px 600, #3c3c3f @ 0.7 |
| Transition | none |
| ::after | 976px x 128px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div::after.framer-h8w7wy 976pxx128px border B:1px solid #171717 @ 0.1 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-heading

Footer heading. The "Smooth sailing." sign-off heading in the footer.

Page: home. Selector: `footer heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 566 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h5.framer-text: system-ui 20px/30px 600, #3c3c3f @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `footer-heading-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.2 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #777777 | #555555 | = | #555555 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-57rakp 86.2x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Home

#### hero-title

Hero title. "Run people operations. With clarity." — the display headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subtitle. The paragraph under the hero title.

Page: home. Selector: `hero p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 20px/32px 500 |
| Letter spacing | normal |
| Colour | #3c3c3f @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### cta-demo

Primary CTA. The "Book a demo" button under the hero. Hovered and focused only.

Page: home. Selector: `Book a demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.86 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, #ffffff, ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0.153509 0.661327 1) | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 r 99px outline 1px auto #005fcc offset 1px; div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-demo-default.png`, `cta-demo-hover.png`, `cta-demo-focus-visible.png`, `cta-demo-pressed.png`.

#### cta-try

Secondary CTA. The "Try for free" button. Hovered and focused only.

Page: home. Selector: `Try for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139.03 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | color(display-p3 0.89 0.946 0.99) | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, color(display-p3 0.0014 0.5301 0.8827), ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-1tXqu.framer-1a3dznk 139.0x48.0 bg color(display-p3 0.89 0.946 0.99) r 99px | = | a.framer-1tXqu.framer-1a3dznk 139.0x48.0 bg color(display-p3 0.89 0.946 0.99) r 99px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-try-default.png`, `cta-try-hover.png`, `cta-try-focus-visible.png`, `cta-try-pressed.png`.

#### copilot-demo

Co-pilot demo panel. The animated AI-assistant chat mock in the hero (a marketing demo, not a live product): the "Ask me anything" prompt inside the chat panel.

Page: home. Selector: `copilot prompt`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 267.3 x 313.2 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: system-ui 12px/16.8px 400, #262626 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1.00288, 0, 0.499997) |
| Painted layers | div.framer-jk2tl6 236.2x37.8 bg color(display-p3 0.89 0.946 0.99) r 3.81111% 3.81111% 1.52444% / 23.8095% 23.8095% 9.52381%; h1.sc-bcXHqe.NoxDJ 127.9x15.1 image linear-gradient(90deg, #000000 @ 0 0%, #000000 @ 0 23%, #ffffff 50%, #000000 @ 0 77%, #000; p.sc-gswNZR.kkRwZG 43.6x15.1 image linear-gradient(90deg, #000000 @ 0 0%, #000000 @ 0 20%, #ffffff 50%, #000000 @ 0 80%, #000 |
| Ancestor paint | 1 up div.framer-GHp4n.framer-zaxhmr shadow #000000 @ 0.06 0px 0.48175px 0.86715px -1.25px, #000000 @ 0.05 0px 1.83083px 3.29549px -2.5px, #000000 @ 0.02 0px 8px 14.4px -3.75px, #000000 @ 0.02 0px 0px 0px 1px, #000000 @ 0.05 0px 0px 15px 0px |
| How | at rest |

Crops: `copilot-demo-default.png`.

#### section-title

Section title. A section heading ("Built for people, not just the process").

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 680 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 56px/56px 600 |
| Letter spacing | -0.28px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### feature-card

Feature card. A product-area card (Everyday HR / Team culture / Growth & feedback).

Page: home. Selector: `feature card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 476 x 620 | = |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | color(display-p3 0.73 0.89 0.99) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.framer-text.framer-styles-preset-12lj5ox: system-ui 44px/48.4px 600, #262626, ls -0.28px | = |
| Transition | none | = |
| Icon | 62 x 56, colour #000000 | = |
| Painted layers | div.framer-cthjdz 476.0x620.0 bg color(display-p3 0.73 0.89 0.99) r 24px; div.framer-1qip43p 444.0x339.6 r 16px 0px 0px shadow #000000 @ 0.18 0px 0.602187px 0.602187px -1.25px, #000000 @ 0.16 0px 2.28853px 2.28853px -2.5px, #000000 @ 0.06 0px 10px 10px -3.75px, #171717 @ 0.1 0px 0px 0px 1px | = |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### feature-item

Feature list item. A feature row inside a product card (People directory, Time off, Contracts & documents).

Page: home. Selector: `feature item`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 278 x 30 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.framer-text.framer-styles-preset-qhpfxb: system-ui 20px/30px 600, #262626 | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `feature-item-default.png`, `feature-item-hover.png`.

#### learn-more

Learn-more link. The text link inside a feature card.

Page: home. Selector: `Learn more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 141.2 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | #ffffff @ 0.6 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, #262626, ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-1tXqu.framer-1a3dznk 141.2x48.0 bg #ffffff @ 0.6 r 99px; div.framer-14owhvr 141.2x48.0 bg color(display-p3 0.86 0.83 0.99) | = | a.framer-1tXqu.framer-1a3dznk 141.2x48.0 bg #ffffff @ 0.6 r 99px outline 1px auto #005fcc offset 1px; div.framer-14owhvr 141.2x48.0 bg color(display-p3 0.86 0.83 0.99) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `learn-more-default.png`, `learn-more-hover.png`, `learn-more-focus-visible.png`, `learn-more-pressed.png`.

### Product pages

#### everyday-hr-title

Page title.

Page: everyday-hr. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `everyday-hr-title-default.png`.

#### everyday-hr-section

Section title.

Page: everyday-hr. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 680 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 56px/56px 600 |
| Letter spacing | -0.28px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `everyday-hr-section-default.png`.

#### everyday-hr-card

Feature card.

Page: everyday-hr. Selector: `feature card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 476 x 620 | = |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | #8df1ed | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.framer-text.framer-styles-preset-12lj5ox: system-ui 44px/48.4px 600, #262626, ls -0.28px | = |
| Transition | none | = |
| Icon | 50 x 61, colour #000000 | = |
| Painted layers | div.framer-1caqrec 476.0x620.0 bg #8df1ed r 24px | = |
| How | at rest | mouse hover |

Crops: `everyday-hr-card-default.png`, `everyday-hr-card-hover.png`.

#### everyday-hr-item

Feature item.

Page: everyday-hr. Selector: `feature item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 278 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 20px/30px 600 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `everyday-hr-item-default.png`.

#### everyday-hr-cta

Page CTA.

Page: everyday-hr. Selector: `page cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.86 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, #ffffff, ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0.153509 0.661327 1) | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 r 99px outline 1px auto #005fcc offset 1px; div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `everyday-hr-cta-default.png`, `everyday-hr-cta-hover.png`, `everyday-hr-cta-focus-visible.png`, `everyday-hr-cta-pressed.png`.

#### growth-feedback-title

Page title.

Page: growth-feedback. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 140.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `growth-feedback-title-default.png`.

#### growth-feedback-section

Section title.

Page: growth-feedback. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 680 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 56px/56px 600 |
| Letter spacing | -0.28px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `growth-feedback-section-default.png`.

#### growth-feedback-card

Feature card.

Page: growth-feedback. Selector: `feature card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 476 x 620 | = |
| Padding | 32px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.framer-text.framer-styles-preset-12lj5ox: system-ui 44px/48.4px 600, #ffffff, ls -0.28px | = |
| Transition | none | = |
| Icon | 62 x 62, colour #ffffff | = |
| Painted layers | div.framer-ae02ms 476.0x620.0 image linear-gradient(#000000 @ 0 50%, #000000 @ 0.5 100%) | = |
| How | at rest | mouse hover |

Crops: `growth-feedback-card-default.png`, `growth-feedback-card-hover.png`.

#### growth-feedback-item

Feature item. A feature row inside a product card.

Page: growth-feedback. Selector: `feature item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 20px/32px 500 |
| Letter spacing | normal |
| Colour | #3c3c3f @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `growth-feedback-item-default.png`.

#### growth-feedback-cta

Page CTA.

Page: growth-feedback. Selector: `page cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.86 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, #ffffff, ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0.153509 0.661327 1) | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 r 99px outline 1px auto #005fcc offset 1px; div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `growth-feedback-cta-default.png`, `growth-feedback-cta-hover.png`, `growth-feedback-cta-focus-visible.png`, `growth-feedback-cta-pressed.png`.

#### team-culture-title

Page title.

Page: team-culture. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 140.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `team-culture-title-default.png`.

#### team-culture-section

Section title.

Page: team-culture. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 680 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 56px/56px 600 |
| Letter spacing | -0.28px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `team-culture-section-default.png`.

#### team-culture-card

Feature card.

Page: team-culture. Selector: `feature card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 476 x 620 | = |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | color(display-p3 0.956 0.817 0.904) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.framer-text.framer-styles-preset-12lj5ox: system-ui 44px/48.4px 600, #262626, ls -0.28px | = |
| Transition | none | = |
| Icon | 75 x 58, colour #000000 | = |
| Painted layers | div.framer-1h29mr8 476.0x620.0 bg color(display-p3 0.956 0.817 0.904) r 24px | = |
| How | at rest | mouse hover |

Crops: `team-culture-card-default.png`, `team-culture-card-hover.png`.

#### team-culture-item

Feature item. A feature row inside a product card.

Page: team-culture. Selector: `feature item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 20px/32px 500 |
| Letter spacing | normal |
| Colour | #3c3c3f @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `team-culture-item-default.png`.

#### team-culture-cta

Page CTA.

Page: team-culture. Selector: `page cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.86 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, #ffffff, ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0.153509 0.661327 1) | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 r 99px outline 1px auto #005fcc offset 1px; div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `team-culture-cta-default.png`, `team-culture-cta-hover.png`, `team-culture-cta-focus-visible.png`, `team-culture-cta-pressed.png`.

### Pricing

#### pricing-title

Page title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 147.59 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### price-card

Plan card. A pricing plan card.

Page: pricing. Selector: `plan card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 976 x 750.41 | = |
| Padding | 48px | = |
| Gap | 56px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h1.framer-text.framer-styles-preset-3nqyhf: system-ui 64px/70.4px 600, #262626, ls -0.6px | = |
| Transition | none | = |
| Icon | 16 x 23, colour #000000 | = |
| ::after | 976px x 750.406px, absolute, bg #000000 @ 0, radius 24px | = |
| Painted layers | div.framer-q59g8t 976.0x750.4 bg #ffffff r 24px; div::after.framer-q59g8t 976pxx750.406px border T:1px solid #171717 @ 0.1 / R:1px solid #171717 @ 0.1 / B:1px solid #171717 @ 0.1 / L:1px solid #171717 @ 0.1 r 24px; div.framer-1czg8b5 147.6x166.4 bg #ffffff; div.framer-158e6bx 123.3x48.0 bg #ffffff r 99px; div::after.framer-158e6bx 123.25pxx48px border T:1px solid #171717 @ 0.1 / R:1px solid #171717 @ 0.1 / B:1px solid #171717 @ 0.1 / L:1px solid #171717 @ 0.1 r 99px; a.framer-1tXqu.framer-1a3dznk 154.9x48.0 bg color(display-p3 0.89 0.946 0.99) r 99px | = |
| How | at rest | mouse hover |

Crops: `price-card-default.png`, `price-card-hover.png`.

#### price-amount

Plan price. The "80 kr / user / month" price figure.

Page: pricing. Selector: `price amount`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 147.59 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `price-amount-default.png`.

#### plan-cta

Plan CTA.

Page: pricing. Selector: `plan cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.86 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | color(display-p3 0.89 0.946 0.99) | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, color(display-p3 0.0014 0.5301 0.8827), ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 bg color(display-p3 0.89 0.946 0.99) r 99px | = | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 bg color(display-p3 0.89 0.946 0.99) r 99px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### billing-toggle

Billing toggle. The monthly/yearly switch, if rendered (never toggled).

Page: pricing. Selector: `billing toggle`. States: .

Not found on the page at capture time.

### Book a demo (resting only)

#### demo-title

Page title. "Request a demo" — the form page heading.

Page: book-demo. Selector: `h1,h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 680 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 56px/56px 600 |
| Letter spacing | -0.28px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `demo-title-default.png`.

#### demo-form

Demo form. The book-a-demo form or scheduler embed. Measured at rest; nothing typed or sent.

Page: book-demo. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 280 x 638.84 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Inter 12px/14.4px 500, #888888 |
| Transition | none |
| Painted layers | div.framer-form-text-input.framer-form-input-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px; div.framer-form-text-input.framer-form-input-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px; div.framer-form-text-input.framer-form-input-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px; div.framer-form-text-input.framer-form-input-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px; div.framer-form-input-wrapper.framer-form-select-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px; div::before.framer-form-input-wrapper.framer-form-select-wrapper 16pxx16px bg #999999 |
| Ancestor paint | 1 up div.framer-nFDAM.framer-dSxla bg #ffffff |
| How | at rest |

Crops: `demo-form-default.png`.

#### demo-field

Demo field. A text field of the demo form. Clicked into for the focus style; nothing typed.

Page: book-demo. Selector: `form field`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 256 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/16px 500 | = |
| Letter spacing | normal | = |
| Colour | #262626 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #3c3c3f @ 0.4, opacity 1 | = |
| Ancestor paint | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #171717 @ 0.05 | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #171717 @ 0.05 shadow #0ea5e9 @ 0.5 0px 0px 0px 2px |
| How | at rest | clicked into the field |

Crops: `demo-field-default.png`, `demo-field-focused.png`.

#### demo-submit

Demo submit. The "Let’s talk" form submit button. Measured in every state, never pressed.

Page: book-demo. Selector: `form submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280 x 40 | = | = | = |
| Padding | 5px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#ffffff 0%, #fbfaf9 100%) | = | = | = |
| Box shadow | #171717 @ 0.1 0px 0px 0px 2px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.framer-text: Inter 15px/30px 600, #262626, ls -0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.framer-xPTn1.framer-1jlpbfk 280.0x40.0 image linear-gradient(#ffffff 0%, #fbfaf9 100%) r 12px shadow #171717 @ 0.1 0px 0px 0px 2px | = | button.framer-xPTn1.framer-1jlpbfk 280.0x40.0 image linear-gradient(#ffffff 0%, #fbfaf9 100%) r 12px shadow #171717 @ 0.1 0px 0px 0px 2px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-submit-default.png`, `demo-submit-hover.png`, `demo-submit-focus-visible.png`, `demo-submit-pressed.png`.

### What's new

#### whatsnew-title

Page title.

Page: whats-new. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `whatsnew-title-default.png`.

#### release-row

Release row. A dated changelog entry on the Whats-new page.

Page: whats-new. Selector: `release row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 240 x 44 | = |
| Padding | 10px 0px | = |
| Gap | 10px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | time: system-ui 16px/24px 500, #3c3c3f @ 0.7 | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `release-row-default.png`, `release-row-hover.png`.

#### release-title

Release title. The dated headline of a changelog detail page (June 2026).

Page: release. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 140.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `release-title-default.png`.

#### release-back

Back link. The "Link back" anchor returning to the What's new index.

Page: release. Selector: `back link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.25 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | system-ui 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3c3c3f @ 0.7 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-1iscjdd 86.3x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: `release-back-default.png`, `release-back-hover.png`, `release-back-focus-visible.png`, `release-back-pressed.png`.

#### release-post

Release body. The changelog post body on a detail page.

Page: release. Selector: `release post`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 6677.86 |
| Padding | 132px 24px 0px 24px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.framer-text.framer-styles-preset-1iscjdd: system-ui 16px/24px 500, #3c3c3f @ 0.7 |
| Transition | none |
| Ancestor paint | 1 up div.framer-ysVa4.framer-MvUYa bg #ffffff |
| How | at rest |

Crops: `release-post-default.png`.

### Legal text

#### dataprotection-title

Page title.

Page: dataprotection. Selector: `h1-h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 44px/48.4px 600 |
| Letter spacing | -0.28px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `dataprotection-title-default.png`.

#### dataprotection-body

Body text.

Page: dataprotection. Selector: `legal p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 20px/32px 500 |
| Letter spacing | normal |
| Colour | #3c3c3f @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `dataprotection-body-default.png`.

#### terms-title

Page title.

Page: terms. Selector: `h1-h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 48.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 44px/48.4px 600 |
| Letter spacing | -0.28px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `terms-title-default.png`.

#### terms-body

Body text.

Page: terms. Selector: `legal p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 20px/32px 500 |
| Letter spacing | normal |
| Colour | #3c3c3f @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `terms-body-default.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile top bar. The mobile header: logo left, menu trigger right.

Page: home. Selector: `mobile nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 37 x 16 |
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
| Ancestor paint | 1 up div.framer-d1Hbe.framer-FDHpM bg #fafafa |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-menu-trigger

Mobile menu trigger. The menu button. Pressed once below to open the menu; a local disclosure.

Page: home. Selector: `navtrigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 37 x 16 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sans-serif 12px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | none | = | - | = |
| Ancestor paint | 1 up div.framer-d1Hbe.framer-FDHpM bg #fafafa | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Error | - | = | keyboard focus failed | = |

Crops: `m-menu-trigger-default.png`, `m-menu-trigger-hover.png`, `m-menu-trigger-pressed.png`.

#### m-nav-panel

Mobile menu (open). The opened mobile menu panel; pressed once, nothing navigated.

Page: home. Selector: `mobile menu open`. States: .

Not found on the page at capture time.

#### m-hero-title

Mobile hero title.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 105.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 48px/52.8px 600 |
| Letter spacing | -0.1px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

### Teamtailor partner page

#### teamtailor-title

Page title. "The best candidate experience deserves an equally great employee experience."

Page: teamtailor. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 880 x 211.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 64px/70.4px 600 |
| Letter spacing | -0.6px |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `teamtailor-title-default.png`.

#### teamtailor-card

Partner card.

Page: teamtailor. Selector: `partner card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 976 x 799 | = |
| Padding | 48px 0px | = |
| Gap | 48px | = |
| Border | none | = |
| Radius | 32px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.framer-text: Inter 12px/14.4px 500, #888888 | = |
| Transition | none | = |
| Painted layers | div.framer-nFDAM.framer-dSxla 340.0x703.0 bg #ffffff r 24px; div::after.framer-nFDAM.framer-dSxla 340pxx703px border T:1px solid #171717 @ 0.1 / R:1px solid #171717 @ 0.1 / B:1px solid #171717 @ 0.1 / L:1px solid #171717 @ 0.1 r 24px; div.framer-form-text-input.framer-form-input-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px; div.framer-form-text-input.framer-form-input-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px; div.framer-form-text-input.framer-form-input-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px; div.framer-form-text-input.framer-form-input-wrapper 280.0x40.0 bg #171717 @ 0.05 r 10px | = |
| How | at rest | mouse hover |

Crops: `teamtailor-card-default.png`, `teamtailor-card-hover.png`.

#### teamtailor-cta

Page CTA.

Page: teamtailor. Selector: `page cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.86 x 48 | = | = | = |
| Padding | 10px 24px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 99px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: system-ui 18px/28px 600, #ffffff, ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | div.framer-14owhvr 154.9x48.0 bg color(display-p3 0.153509 0.661327 1) | a.framer-1tXqu.framer-1a3dznk 154.9x48.0 r 99px outline 1px auto #005fcc offset 1px; div.framer-14owhvr 154.9x48.0 bg color(display-p3 0 0.599909 1) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `teamtailor-cta-default.png`, `teamtailor-cta-hover.png`, `teamtailor-cta-focus-visible.png`, `teamtailor-cta-pressed.png`.

## Transitions declared in the readable stylesheets

aboardhr.com is a Framer site: its inline stylesheets are same-origin readable and declare 133 custom properties, of which 62 resolve at :root (hashed --token-<uuid> design tokens and the --framer-* typography variables; see css-vars.json). The values below are computed styles read off the running pages; the per-state Transition rows are computed values.

- book-demo: `color 0.15s`, `opacity 0.4s ease-out`, `unset`

- everyday-hr: `opacity 0.4s ease-out`, `unset`

- growth-feedback: `opacity 0.4s ease-out`, `unset`

- home: `opacity 0.4s ease-out`, `unset`

- pricing: `opacity 0.4s ease-out`, `unset`

- team-culture: `opacity 0.4s ease-out`, `unset`

- teamtailor: `color 0.15s`, `opacity 0.4s ease-out`, `unset`

- whats-new: `opacity 0.4s ease-out`, `unset`
