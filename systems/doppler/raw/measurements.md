# Doppler component measurements

Computed styles read from doppler.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's single painted dark surface (warm-black #1c1624) — home, /platform/secrets-manager, /pricing, /demo, /integrations, /customers, /blog and /agents — with the cookie-preferences banner hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky marketing header: a 72px warm-black bar with a 1px glow-stroke border and 16px bottom radii — wordmark, the Platform/Solutions/Resources dropdowns, Doppler for Agents, Customers, Pricing, Get Demo, the green Start-for-Free pill and Sign In.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1412 x 72 |
| Padding | 0px 20px |
| Border | T: none; R: 1px solid #55505b; B: 1px solid #55505b; L: 1px solid #55505b |
| Radius | 0px 0px 16px 16px |
| Background | #1c1624 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | span: __DopplerRepro_a18e76 15px/15px 700, #d0c9c4, ls 0.15px |
| Transition | none |
| Icon | 14 x 9, colour #d0c9c4 |
| Painted layers | header.flex.h-[72px] 1412.0x72.0 bg #1c1624 border R:1px solid #55505b / B:1px solid #55505b / L:1px solid #55505b r 0px 0px 16px 16px; div.transition-transform.duration-[350ms] 0.0x0.0 bg #f1f0ec; div.transition-transform.duration-[350ms] 0.0x0.0 bg #f1f0ec; div.transition-transform.duration-[350ms] 0.0x0.0 bg #f1f0ec; div.absolute.left-[10%] 0.0x0.0 bg #1c1624 border R:1px solid #55505b / B:1px solid #55505b / L:1px solid #55505b r 0px 0px 20px 20px; div.absolute.left-[10%] 0.0x0.0 bg #1c1624 border R:1px solid #55505b / B:1px solid #55505b / L:1px solid #55505b r 0px 0px 20px 20px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Doppler wordmark anchor.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 156 x 31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Platform button that opens the header mega-menu; toggled, never followed.

Page: home. Selector: `header nav button "Platform"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.8 x 71 | = | = | = |
| Padding | 28px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 15px/15px 700 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #d0c9c4 | #f1f0ec | #f1f0ec | #f1f0ec |
| Text node | span: __DopplerRepro_a18e76 15px/15px 700, #d0c9c4, ls 0.15px | span: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px | span: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px | span: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 9, colour #d0c9c4 | 14 x 9, colour #f1f0ec | 14 x 9, colour #f1f0ec | 14 x 9, colour #f1f0ec |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.items-center 105.8x71.0 outline 1px auto #005fcc offset 0px | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The plain Pricing header link.

Page: home. Selector: `header nav a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.08 x 71 | = | = | = |
| Padding | 28px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 15px/15px 700 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #d0c9c4 | #f1f0ec | #f1f0ec | #f1f0ec |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.p-8.py-28 71.1x71.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-demo

Demo link. The Get-Demo header action; measured never followed.

Page: home. Selector: `header a "Get Demo"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.91 x 31 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 15px/15px 700 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #d0c9c4 | #f1f0ec | #f1f0ec | #f1f0ec |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.p-8.text-link 91.9x31.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-cta

Nav CTA. The fluorescent-green Start-for-Free pill (points off-site to dashboard.doppler.com/register); measured never followed.

Page: home. Selector: `header a "Start for Free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 156.31 x 36.05 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #00f575 | #00bf5b | = | #00bf5b |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1624 | = | = | = |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #1c1624, ls 0.15px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 12, colour #1c1624 | = | = | = |
| Painted layers | a.group.inline-flex 156.3x36.0 bg #00f575 r 12px | a.group.inline-flex 156.3x36.0 bg #00bf5b r 12px | a.group.inline-flex 156.3x36.0 bg #00f575 r 12px outline 1px auto #005fcc offset 1px | a.group.inline-flex 156.3x36.0 bg #00bf5b r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-signin

Sign-in link. The bordered Sign-In header action (points off-site to dashboard.doppler.com/login); measured never followed.

Page: home. Selector: `header a "Sign In"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.75 x 37 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #f1f0ec | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #f2f1ed @ 0.08 | = | #f2f1ed @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.inline-flex 86.8x37.0 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px | a.group.inline-flex 86.8x37.0 bg #f2f1ed @ 0.08 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px | a.group.inline-flex 86.8x37.0 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px outline 1px auto #005fcc offset 1px | a.group.inline-flex 86.8x37.0 bg #f2f1ed @ 0.08 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-dropdown

Nav dropdown. The Platform mega-menu panel, opened by its own trigger.

Page: home. Selector: `header platform panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 372 |
| Padding | 30px |
| Border | T: none; R: 1px solid #55505b; B: 1px solid #55505b; L: 1px solid #55505b |
| Radius | 0px 0px 20px 20px |
| Background | #1c1624 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 15px/15px 700 |
| Letter spacing | 0.15px |
| Colour | #f1f0ec |
| Text node | div.text-navLink.ease: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px |
| Transition | none |
| Icon | 32 x 32, colour #f1f0ec |
| Painted layers | div.absolute.left-[10%] 720.0x372.0 bg #1c1624 border R:1px solid #55505b / B:1px solid #55505b / L:1px solid #55505b r 0px 0px 20px 20px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A feature link inside the opened mega-menu.

Page: home. Selector: `header menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 314 x 73 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | 1px auto #005fcc offset 1px |
| Font | __DopplerRepro_a18e76 15px/15px 700 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | div.text-navLink.ease: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px | div.text-navLink.ease: __DopplerRepro_a18e76 15px/15px 700, #00f575, ls 0.15px | = | div.text-navLink.ease: __DopplerRepro_a18e76 15px/15px 700, #00f575, ls 0.15px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 12, colour #00f575 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.flex 314.0x73.0 outline 1px auto #005fcc offset 1px | a.group.flex 314.0x73.0 outline 1px auto #005fcc offset 1px |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home hero

#### hero-title

Hero headline. The display headline ("One platform. Every secret. Human or AI.") with a lilac-to-carmine gradient line.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 304.86 x 172.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 48px/57.6px 450 |
| Letter spacing | -0.96px |
| Colour | #f1f0ec |
| Text node | span.block: __DopplerRepro_a18e76 48px/57.6px 450, #f1f0ec, ls -0.96px |
| Transition | none |
| Painted layers | span.inline.bg-clip-text 281.6x71.0 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%) |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede paragraph under the headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 100.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 18px/25.2px 400 |
| Letter spacing | -0.18px |
| Colour | #d0c9c4 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The green Start-for-Free button in the hero; measured never followed.

Page: home. Selector: `hero "Start for Free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136.31 x 45 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #f1f0ec | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #f2f1ed @ 0.08 | = | #f2f1ed @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.inline-flex 136.3x45.0 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px | a.group.inline-flex 136.3x45.0 bg #f2f1ed @ 0.08 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px | a.group.inline-flex 136.3x45.0 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px outline 1px auto #005fcc offset 1px | a.group.inline-flex 136.3x45.0 bg #f2f1ed @ 0.08 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

### Home

#### h2-section

Section heading. A gradient-text section heading ("Built for every identity").

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 315.63 x 38.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 32px/38.4px 450 |
| Letter spacing | -0.64px |
| Colour | #b997ff |
| Transition | none |
| How | at rest |

Crops: `h2-section-default.png`.

#### feature-card

Feature card. A .interactive-card tile under a section heading (the "Built for every identity" cards).

Page: home. Selector: `.interactive-card on /`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 396 x 287.84 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #f2f1ed @ 0.04 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | div.text-p1.font-bold: __DopplerRepro_a18e76 24px/33.6px 700, #f1f0ec, ls -0.24px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 14 x 12, colour #d0c9c4 |
| ::before | 396px x 287.844px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67%), radius 20px |
| ::after | 396px x 287.844px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.24 -6.99%, #ffffff @ 0.06 27.95%, #ffffff @ 0.24 87.67%), radius 20px |
| Painted layers | div.interactive-card.with-link 396.0x287.8 bg #f2f1ed @ 0.04 r 20px; div::before.interactive-card.with-link 396pxx287.844px image linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67 r 20px; div::after.interactive-card.with-link 396pxx287.844px image linear-gradient(100.03deg, #ffffff @ 0.24 -6.99%, #ffffff @ 0.06 27.95%, #ffffff @ 0.24 87 r 20px; div.ease.pointer-events-none 435.6x435.6 image linear-gradient(#8b877d 0%, #f1f0ec 100%) r 9999px |
| How | at rest |

Crops: `feature-card-default.png`.

#### platform-h1

Platform title. The secrets-manager product-page heading.

Page: platform. Selector: `h1 on /platform/secrets-manager`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 470.59 x 115.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 48px/57.6px 450 |
| Letter spacing | -0.96px |
| Colour | #f1f0ec |
| Text node | span.inline.bg-clip-text: __DopplerRepro_a18e76 48px/57.6px 450, #000000 @ 0, ls -0.96px |
| Transition | none |
| Painted layers | span.inline.bg-clip-text 470.6x71.0 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%) |
| How | at rest |

Crops: `platform-h1-default.png`.

#### platform-card

Platform feature card. A .interactive-card feature tile on the secrets-manager page.

Page: platform. Selector: `.interactive-card on /platform/secrets-manager`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 610 x 516.25 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #f2f1ed @ 0.04 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | div.text-p1.font-bold: __DopplerRepro_a18e76 24px/33.6px 700, #f1f0ec, ls -0.24px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 14 x 12, colour #d0c9c4 |
| ::before | 610px x 516.25px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67%), radius 20px |
| ::after | 610px x 516.25px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.24 -6.99%, #ffffff @ 0.06 27.95%, #ffffff @ 0.24 87.67%), radius 20px |
| Painted layers | div.interactive-card.with-link 610.0x516.3 bg #f2f1ed @ 0.04 r 20px; div::before.interactive-card.with-link 610pxx516.25px image linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67 r 20px; div::after.interactive-card.with-link 610pxx516.25px image linear-gradient(100.03deg, #ffffff @ 0.24 -6.99%, #ffffff @ 0.06 27.95%, #ffffff @ 0.24 87 r 20px; div.ease.pointer-events-none 500.0x500.0 image linear-gradient(#8b877d 0%, #f1f0ec 100%) r 9999px |
| How | at rest |

Crops: `platform-card-default.png`.

### Pricing

#### pricing-h1

Pricing title. The "One bill. No surprises." display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 572.94 x 201.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 96px/100.8px 450 |
| Letter spacing | -1.92px |
| Colour | #f1f0ec |
| Text node | span.block: __DopplerRepro_a18e76 96px/100.8px 450, #f1f0ec, ls -1.92px |
| Transition | none |
| Painted layers | span.inline.bg-clip-text 572.9x130.0 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%) |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### seat-slider

Seat slider. The seats range input in the pricing calculator; focused, never dragged past a checkout.

Page: pricing. Selector: `input[type=range]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 1252 x 10 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 35px | = |
| Background | transparent | = |
| Background image | linear-gradient(to right, #7d6ea3 9.45674%, #3e384b 9.45674%) | linear-gradient(to right, #7d6ea3 50.1006%, #3e384b 50.1006%) |
| Box shadow | none | = |
| Outline | none | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f1f0ec | = |
| Transition | none | = |
| Cursor | pointer | = |
| Placeholder | #f1f0ec, opacity 1 | = |
| Painted layers | input 1252.0x10.0 image linear-gradient(to right, #7d6ea3 9.45674%, #3e384b 9.45674%) r 35px | input 1252.0x10.0 image linear-gradient(to right, #7d6ea3 50.1006%, #3e384b 50.1006%) r 35px |
| How | at rest | clicked into the field |

Crops: `seat-slider-default.png`, `seat-slider-focused.png`.

#### seat-field

Spend field. The "$100,000" currency field beside the seats slider; focused only.

Page: pricing. Selector: `pricing calculator input[type=text]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 332 x 52 | = |
| Padding | 10px 20px | = |
| Border | 1px solid #44403c | 1px solid #b997ff |
| Radius | 6px | = |
| Background | #f2f1ed @ 0.04 | = |
| Box shadow | none | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | __DopplerRepro_a18e76 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #f1f0ec | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #f1f0ec, opacity 1 | = |
| Painted layers | input.mt-10.rounded-6 332.0x52.0 bg #f2f1ed @ 0.04 border T:1px solid #44403c / R:1px solid #44403c / B:1px solid #44403c / L:1px solid #44403c r 6px outline 2px solid #000000 @ 0 offset 2px | input.mt-10.rounded-6 332.0x52.0 bg #f2f1ed @ 0.04 border T:1px solid #b997ff / R:1px solid #b997ff / B:1px solid #b997ff / L:1px solid #b997ff r 6px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `seat-field-default.png`, `seat-field-focused.png`.

#### plan-name

Plan name. A plan card's name.

Page: pricing. Selector: `plan name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332 x 38.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 32px/38.4px 450 |
| Letter spacing | -0.64px |
| Colour | #f1f0ec |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. A plan card's price figure (e.g. "$8/mo per additional user").

Page: pricing. Selector: `plan price leaf`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332 x 33.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 24px/33.6px 400 |
| Letter spacing | -0.24px |
| Colour | #f1f0ec |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-badge

Plan badge. The MOST POPULAR chip on the Team card.

Page: pricing. Selector: `"MOST POPULAR" chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 10px/10px 700 |
| Letter spacing | 1px |
| Colour | #f1f0ec |
| Text node | span.ease.z-1: __DopplerRepro_a18e76 10px/10px 700, #f1f0ec, ls 1px |
| Transition | none |
| Icon | 17.36 x 22, colour #f1f0ec |
| Painted layers | span.ease.z-1 96.8x22.0 bg #302c37 |
| How | at rest |

Crops: `plan-badge-default.png`.

#### plan-card

Plan card. A pricing plan card (the painted ancestor of the plan name).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 396 x 938.55 |
| Padding | 32px |
| Border | none |
| Radius | 20px |
| Background | #f2f1ed @ 0.04 |
| Box shadow | none |
| Backdrop filter | blur(10px) |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | h2.text-h4Mobile.md:text-h4: __DopplerRepro_a18e76 32px/38.4px 450, #f1f0ec, ls -0.64px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 14 x 14, colour #f1f0ec |
| ::before | 396px x 938.547px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67%), radius 20px |
| Painted layers | div.interactive-card.group 396.0x938.5 bg #f2f1ed @ 0.04 r 20px; div::before.interactive-card.group 396pxx938.547px image linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67 r 20px; div.ease.pointer-events-none 435.6x435.6 image linear-gradient(120deg, #9f5bff 0%, #9f5bff 100%) r 9999px; a.group.inline-flex 332.0x45.0 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px |
| How | at rest |

Crops: `plan-card-default.png`.

#### faq-item

FAQ accordion. A closed FAQ row (aria-expanded=false); the open state below is a row expanded by its own toggle.

Page: pricing. Selector: `pricing FAQ button, closed`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 892 x 57.2 | = | = | = |
| Padding | 16px 0px | = | = | = |
| Gap | 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | div.text-p2.max-w-[700px]: __DopplerRepro_a18e76 18px/25.2px 500, #f1f0ec, ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 25, colour #8b877d | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.w-full 892.0x57.2 outline 1px auto #005fcc offset 0px | = |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`.

#### faq-open

FAQ accordion, open. An expanded FAQ row container (question plus revealed answer).

Page: pricing. Selector: `aria-expanded=true FAQ row container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 892 x 181.98 |
| Padding | 16px 0px |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.08; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | div.text-p2.max-w-[700px]: __DopplerRepro_a18e76 18px/25.2px 500, #f1f0ec, ls -0.18px |
| Transition | none |
| Icon | 34.65 x 34.65, colour #f1f0ec |
| Painted layers | div.w-full.border-b-1 892.0x182.0 border B:1px solid #ffffff @ 0.08; span.absolute.-bottom-1 0.0x2.0 bg #b997ff |
| How | at rest |

Crops: `faq-open-default.png`.

#### plan-cta

Plan CTA. A plan card's action; measured never followed.

Page: pricing. Selector: `.interactive-card CTA on /pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 332 x 45 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #f1f0ec | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #f2f1ed @ 0.08 | = | #f2f1ed @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.inline-flex 332.0x45.0 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px | a.group.inline-flex 332.0x45.0 bg #f2f1ed @ 0.08 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px | a.group.inline-flex 332.0x45.0 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px outline 1px auto #005fcc offset 1px | a.group.inline-flex 332.0x45.0 bg #f2f1ed @ 0.08 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

### Demo request

#### demo-h1

Demo title. The demo-request display heading.

Page: demo. Selector: `h1 on /demo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 563.39 x 172.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 48px/57.6px 450 |
| Letter spacing | -0.96px |
| Colour | #f1f0ec |
| Text node | span.block: __DopplerRepro_a18e76 48px/57.6px 450, #f1f0ec, ls -0.96px |
| Transition | none |
| Painted layers | span.inline.bg-clip-text 538.6x128.6 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%) |
| How | at rest |

Crops: `demo-h1-default.png`.

#### demo-card

Demo card. The "See Doppler in action" form panel; never submitted.

Page: demo. Selector: `demo form panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 628.61 x 541.41 |
| Padding | 20px 32px |
| Gap | 14px |
| Border | none |
| Radius | 20px |
| Background | #f2f1ed @ 0.04 |
| Box shadow | none |
| Backdrop filter | blur(10px) |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | h2.text-h5Mobile.md:text-h5: __DopplerRepro_a18e76 24px/33.6px 450, #b997ff, ls -0.48px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| ::before | 628.609px x 541.406px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67%), radius 20px |
| Painted layers | div.interactive-card.group 628.6x541.4 bg #f2f1ed @ 0.04 r 20px; div::before.interactive-card.group 628.609pxx541.406px image linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67 r 20px; div.ease.pointer-events-none 500.0x500.0 image linear-gradient(120deg, #ff9efa 0%, #6b13f5 100%) r 9999px; input.w-full.rounded-16 276.3x43.2 border T:1px solid #8b877d / R:1px solid #8b877d / B:1px solid #8b877d / L:1px solid #8b877d r 16px; input.w-full.rounded-16 276.3x43.2 border T:1px solid #8b877d / R:1px solid #8b877d / B:1px solid #8b877d / L:1px solid #8b877d r 16px; input.w-full.rounded-16 564.6x43.2 border T:1px solid #8b877d / R:1px solid #8b877d / B:1px solid #8b877d / L:1px solid #8b877d r 16px |
| How | at rest |

Crops: `demo-card-default.png`.

#### demo-field

Text field. The First-name input; sample text was typed and deleted, nothing sent.

Page: demo. Selector: `demo input[type=text]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 276.3 x 43.2 | = | = |
| Padding | 8px 16px | = | = |
| Border | 1px solid #8b877d | 1px solid #b997ff | 1px solid #b997ff |
| Radius | 16px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | __DopplerRepro_a18e76 18px/25.2px 400 | = | = |
| Letter spacing | -0.18px | = | = |
| Colour | #f1f0ec | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #f1f0ec, opacity 1 | = | = |
| Painted layers | input.w-full.rounded-16 276.3x43.2 border T:1px solid #8b877d / R:1px solid #8b877d / B:1px solid #8b877d / L:1px solid #8b877d r 16px | input.w-full.rounded-16 276.3x43.2 border T:1px solid #b997ff / R:1px solid #b997ff / B:1px solid #b997ff / L:1px solid #b997ff r 16px outline 2px solid #000000 @ 0 offset 2px | input.w-full.rounded-16 276.3x43.2 border T:1px solid #b997ff / R:1px solid #b997ff / B:1px solid #b997ff / L:1px solid #b997ff r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `demo-field-default.png`, `demo-field-focused.png`, `demo-field-filled.png`.

#### demo-email

Email field. The company-email input; focused only, never filled or submitted.

Page: demo. Selector: `input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 564.61 x 43.2 | = |
| Padding | 8px 16px | = |
| Border | 1px solid #8b877d | 1px solid #b997ff |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | __DopplerRepro_a18e76 18px/25.2px 400 | = |
| Letter spacing | -0.18px | = |
| Colour | #f1f0ec | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #f1f0ec, opacity 1 | = |
| Painted layers | input.w-full.rounded-16 564.6x43.2 border T:1px solid #8b877d / R:1px solid #8b877d / B:1px solid #8b877d / L:1px solid #8b877d r 16px | input.w-full.rounded-16 564.6x43.2 border T:1px solid #b997ff / R:1px solid #b997ff / B:1px solid #b997ff / L:1px solid #b997ff r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `demo-email-default.png`, `demo-email-focused.png`.

#### demo-select

Select. The Company-Size select; focused, never opened (a native list would paint).

Page: demo. Selector: `select`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 276.3 x 43.2 | = |
| Padding | 8px 16px | = |
| Border | 1px solid #8b877d | 1px solid #b997ff |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | __DopplerRepro_a18e76 18px/25.2px 400 | = |
| Letter spacing | -0.18px | = |
| Colour | #f1f0ec | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | default | = |
| Painted layers | select.w-full.rounded-16 276.3x43.2 border T:1px solid #8b877d / R:1px solid #8b877d / B:1px solid #8b877d / L:1px solid #8b877d r 16px | select.w-full.rounded-16 276.3x43.2 border T:1px solid #b997ff / R:1px solid #b997ff / B:1px solid #b997ff / L:1px solid #b997ff r 16px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `demo-select-default.png`, `demo-select-focused.png`.

#### demo-submit

Submit button. The Choose-a-Time submit; measured, never pressed (a press would submit).

Page: demo. Selector: `button "Choose a Time"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146.02 x 43 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #00f575 | = | = | #00bf5b |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1624 | = | = | = |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #1c1624, ls 0.15px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 146.0x43.0 bg #00f575 r 12px | = | button.inline-flex.items-center 146.0x43.0 bg #00f575 r 12px outline 1px auto #005fcc offset 0px | button.inline-flex.items-center 146.0x43.0 bg #00bf5b r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-submit-default.png`, `demo-submit-hover.png`, `demo-submit-focus-visible.png`, `demo-submit-pressed.png`.

#### check-item

Checklist row. A green-check benefit row beside the form.

Page: demo. Selector: `demo checklist li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 563.39 x 61.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __Inter_516c7b 18px/30.6px 400 |
| Letter spacing | normal |
| Colour | #d0c9c4 |
| Transition | none |
| How | at rest |

Crops: `check-item-default.png`.

### Integrations

#### integrations-h1

Integrations title. The integrations display heading.

Page: integrations. Selector: `h1 on /integrations`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 981.7 x 201.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 96px/100.8px 450 |
| Letter spacing | -1.92px |
| Colour | #f1f0ec |
| Text node | span.inline.bg-clip-text: __DopplerRepro_a18e76 96px/100.8px 450, #000000 @ 0, ls -1.92px |
| Transition | none |
| Painted layers | span.inline.bg-clip-text 916.8x130.0 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%) |
| How | at rest |

Crops: `integrations-h1-default.png`.

#### search-field

Search field. The integrations search input; sample text was typed and deleted, nothing sent.

Page: integrations. Selector: `input "Search"`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 300 x 46.8 | = | = |
| Padding | 14px 20px 14px 40px | = | = |
| Border | 1px solid #f1f0ec | = | = |
| Radius | 12px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | __DopplerRepro_a18e76 14px/16.8px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #f1f0ec | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #f1f0ec, opacity 1 | = | = |
| Painted layers | input.w-full.appearance-none 300.0x46.8 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px | input.w-full.appearance-none 300.0x46.8 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px outline 2px solid #000000 @ 0 offset 2px | input.w-full.appearance-none 300.0x46.8 border T:1px solid #f1f0ec / R:1px solid #f1f0ec / B:1px solid #f1f0ec / L:1px solid #f1f0ec r 12px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### filter-chip

Filter chip. An integration-category filter button; measured, never toggled (a toggle would filter the grid).

Page: integrations. Selector: `category filter button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.88 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 10px/10px 700 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | span.ease.z-1: __DopplerRepro_a18e76 10px/10px 700, #f1f0ec, ls 1px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17.36 x 22, colour #f1f0ec | = | = | = |
| Painted layers | span.ease.z-1 71.0x22.0 bg #2d2734 | span.ease.z-1 71.0x22.0 bg #b997ff | button.group.relative 106.9x22.0 outline 1px auto #005fcc offset 0px; span.ease.z-1 71.0x22.0 bg #2d2734 | span.ease.z-1 71.0x22.0 bg #b997ff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-chip-default.png`, `filter-chip-hover.png`, `filter-chip-focus-visible.png`, `filter-chip-pressed.png`.

#### integration-card

Integration card. An integration tile (a provider name and glyph) in the grid; never followed.

Page: integrations. Selector: `integration tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 289 x 181.2 | = |
| Padding | 32px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | #f2f1ed @ 0.04 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f1f0ec | = |
| Text node | div.text-p2: __DopplerRepro_a18e76 18px/25.2px 400, #f1f0ec, ls -0.18px | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| ::before | 289px x 181.203px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67%), radius 20px | = |
| Painted layers | div.interactive-card.group 289.0x181.2 bg #f2f1ed @ 0.04 r 20px; div::before.interactive-card.group 289pxx181.203px image linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67 r 20px; div.ease.pointer-events-none 317.9x317.9 image linear-gradient(120deg, #00f575 0%, #3822f1 100%) r 9999px | = |
| How | at rest | mouse hover |

Crops: `integration-card-default.png`, `integration-card-hover.png`.

#### request-integration

Request link. The Request-Integration action; measured, never followed.

Page: integrations. Selector: `"Request Integration"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 207.75 x 44.05 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #00f575 | #00bf5b | = | #00bf5b |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1624 | = | = | = |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #1c1624, ls 0.15px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 12, colour #1c1624 | = | = | = |
| Painted layers | button.inline-flex.items-center 207.8x44.0 bg #00f575 r 12px | button.inline-flex.items-center 207.8x44.0 bg #00bf5b r 12px | button.inline-flex.items-center 207.8x44.0 bg #00f575 r 12px outline 1px auto #005fcc offset 0px | button.inline-flex.items-center 207.8x44.0 bg #00bf5b r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `request-integration-default.png`, `request-integration-hover.png`, `request-integration-focus-visible.png`, `request-integration-pressed.png`.

### Blog

#### blog-h1

Blog title. The blog index heading.

Page: blog. Selector: `h1 on /blog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 302.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 96px/100.8px 450 |
| Letter spacing | -1.92px |
| Colour | #f1f0ec |
| Text node | span.block: __DopplerRepro_a18e76 96px/100.8px 450, #f1f0ec, ls -1.92px |
| Transition | none |
| How | at rest |

Crops: `blog-h1-default.png`.

#### cat-chip

Category chip. A blog-category filter chip; measured, never toggled. Labels are sentence-case in the DOM, painted uppercase by text-transform.

Page: blog. Selector: `blog category button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98.77 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 10px/10px 700 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | span.ease.z-1: __DopplerRepro_a18e76 10px/10px 700, #f1f0ec, ls 1px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17.36 x 22, colour #f1f0ec | = | = | = |
| Painted layers | span.ease.z-1 62.9x22.0 bg #2d2734 | span.ease.z-1 62.9x22.0 bg #b997ff | button.group.relative 98.8x22.0 outline 1px auto #005fcc offset 0px; span.ease.z-1 62.9x22.0 bg #2d2734 | span.ease.z-1 62.9x22.0 bg #b997ff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cat-chip-default.png`, `cat-chip-hover.png`, `cat-chip-focus-visible.png`, `cat-chip-pressed.png`.

#### cat-chip-active

Category chip, active. The ALL filter chip, selected at rest (no toggle needed for the selected state).

Page: blog. Selector: `blog "ALL" chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.47 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 10px/10px 700 | = | = | = |
| Letter spacing | 1px | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | span.ease.z-1: __DopplerRepro_a18e76 10px/10px 700, #1c1624, ls 1px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 17.36 x 22, colour #f1f0ec | = | = | = |
| Painted layers | span.ease.z-1 22.6x22.0 bg #b997ff | = | button.group.relative 58.5x22.0 outline 1px auto #005fcc offset 0px; span.ease.z-1 22.6x22.0 bg #b997ff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cat-chip-active-default.png`, `cat-chip-active-hover.png`, `cat-chip-active-focus-visible.png`, `cat-chip-active-pressed.png`.

#### post-card

Post card. A blog post card in the index grid; never followed.

Page: blog. Selector: `post card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 396 x 570 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 20px | = |
| Background | #f2f1ed @ 0.04 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f1f0ec | = |
| Text node | span.ease.z-1: __DopplerRepro_a18e76 10px/10px 700, #f1f0ec, ls 1px | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Icon | 17.36 x 22, colour #f1f0ec | = |
| ::before | 396px x 570px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67%), radius 20px | = |
| ::after | 396px x 570px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.24 -6.99%, #ffffff @ 0.06 27.95%, #ffffff @ 0.24 87.67%), radius 20px | = |
| Painted layers | div.interactive-card.with-link 396.0x570.0 bg #f2f1ed @ 0.04 r 20px; div::before.interactive-card.with-link 396pxx570px image linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67 r 20px; div::after.interactive-card.with-link 396pxx570px image linear-gradient(100.03deg, #ffffff @ 0.24 -6.99%, #ffffff @ 0.06 27.95%, #ffffff @ 0.24 87 r 20px; div.ease.pointer-events-none 435.6x435.6 image linear-gradient(120deg, #ff9efa 0%, #6b13f5 100%) r 9999px; span.ease.z-1 84.1x22.0 bg #2d2734 | = |
| How | at rest | mouse hover |

Crops: `post-card-default.png`, `post-card-hover.png`.

#### page-number

Pagination button. A numbered pagination control; measured, never followed.

Page: blog. Selector: `pagination "2"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #f2f1ed @ 0.04 | = | #f2f1ed @ 0.04 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f1f0ec | #00bf5b | = | #00bf5b |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.z-2.flex 30.0x30.0 bg #f2f1ed @ 0.04 r 9999px | button.z-2.flex 30.0x30.0 r 9999px outline 1px auto #005fcc offset 0px | button.z-2.flex 30.0x30.0 bg #f2f1ed @ 0.04 r 9999px |

Crops: `page-number-default.png`, `page-number-hover.png`, `page-number-focus-visible.png`, `page-number-pressed.png`.

#### read-more

Read-More link. The Read-More card link under each post; measured never followed.

Page: blog. Selector: `a "Read More"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.44 x 15.25 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 15px/15px 700 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #d0c9c4 | #f1f0ec | #f1f0ec | #f1f0ec |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 12, colour #d0c9c4 | 14 x 12, colour #f1f0ec | 14 x 12, colour #f1f0ec | 14 x 12, colour #f1f0ec |
| ::after | 396px x 570px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.card-link.static 106.4x15.3 outline 1px auto #005fcc offset 1px | = |

Crops: `read-more-default.png`, `read-more-hover.png`, `read-more-focus-visible.png`, `read-more-pressed.png`.

### Customers

#### customers-h1

Customers title. The "Doppler effect" customers heading.

Page: customers. Selector: `h1 on /customers`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 825.42 x 100.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 96px/100.8px 450 |
| Letter spacing | -1.92px |
| Colour | #f1f0ec |
| Transition | none |
| How | at rest |

Crops: `customers-h1-default.png`.

#### industry-chip

Industry chip. A customer-industry filter chip; measured, never toggled.

Page: customers. Selector: `industry filter button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.14 x 37.2 | = | = | = |
| Padding | 6px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | span.text-p2.ease: __DopplerRepro_a18e76 18px/25.2px 500, #00f575, ls -0.18px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #f1f0ec | = | = | = |
| Painted layers | div.absolute.inset-0 58.1x37.2 bg #2d2734 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 20px 20px 0px 0px | = | button.relative.snap-start 58.1x37.2 outline 1px auto #005fcc offset 0px; div.absolute.inset-0 58.1x37.2 bg #2d2734 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 20px 20px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `industry-chip-default.png`, `industry-chip-hover.png`, `industry-chip-focus-visible.png`, `industry-chip-pressed.png`.

#### case-card

Case-study card. A customer case-study card; never followed.

Page: customers. Selector: `case-study card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1224 x 590.16 | = |
| Padding | 0px | = |
| Border | 1px solid #ffffff @ 0.08 | = |
| Radius | 20px | = |
| Background | #2d2734 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f1f0ec | = |
| Text node | div.text-h5Mobile.md:text-h5: __DopplerRepro_a18e76 24px/33.6px 450, #f1f0ec, ls -0.48px | = |
| Transition | none | = |
| Icon | 16 x 16, colour #cccccc | = |
| Painted layers | div.rounded-t-0.relative 1224.0x590.2 bg #2d2734 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 20px; div.z-0.aspect-square 279.2x279.2 image radial-gradient(78.16% 78.1% at 77.15% 26.77%, #ff9efa 0%, #6b13f5 50%, #231736 100%) r 80px; div.flex.flex-col 1222.0x169.0 border T:1px solid #ffffff @ 0.08 | = |
| How | at rest | mouse hover |

Crops: `case-card-default.png`, `case-card-hover.png`.

### Agents

#### agents-h1

Agents title. The "Run AI coding agents with Doppler" heading.

Page: agents. Selector: `h1 on /agents`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 563.39 x 115.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 48px/57.6px 450 |
| Letter spacing | -0.96px |
| Colour | #f1f0ec |
| Text node | span.block: __DopplerRepro_a18e76 48px/57.6px 450, #f1f0ec, ls -0.96px |
| Transition | none |
| Painted layers | span.inline.bg-clip-text 179.3x71.0 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%) |
| How | at rest |

Crops: `agents-h1-default.png`.

#### agents-cta

Agents CTA. The "Pick Your Tool" hero call-to-action on the agents landing (an in-page scroll link); measured never followed.

Page: agents. Selector: `a "Pick Your Tool"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 161.2 x 44.05 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #00f575 | #00bf5b | = | #00bf5b |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1624 | = | = | = |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #1c1624, ls 0.15px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 12, colour #1c1624 | = | = | = |
| Painted layers | a.group.inline-flex 161.2x44.0 bg #00f575 r 12px | a.group.inline-flex 161.2x44.0 bg #00bf5b r 12px | a.group.inline-flex 161.2x44.0 bg #00f575 r 12px outline 1px auto #005fcc offset 1px | a.group.inline-flex 161.2x44.0 bg #00bf5b r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `agents-cta-default.png`, `agents-cta-hover.png`, `agents-cta-focus-visible.png`, `agents-cta-pressed.png`.

#### agents-card

Agents card. A "Why Doppler for agents" / "Pick your tool" .interactive-card tile.

Page: agents. Selector: `.interactive-card on /agents`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 396 x 168.59 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #f2f1ed @ 0.04 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | div.text-p1.font-bold: __DopplerRepro_a18e76 24px/33.6px 700, #f1f0ec, ls -0.24px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| ::before | 396px x 168.594px, absolute, bg #000000 @ 0 linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67%), radius 20px |
| Painted layers | div.interactive-card.group 396.0x168.6 bg #f2f1ed @ 0.04 r 20px; div::before.interactive-card.group 396pxx168.594px image linear-gradient(100.03deg, #ffffff @ 0.16 -6.99%, #ffffff @ 0 27.95%, #ffffff @ 0.16 87.67 r 20px; div.ease.pointer-events-none 435.6x435.6 image linear-gradient(#8b877d 0%, #f1f0ec 100%) r 9999px |
| How | at rest |

Crops: `agents-card-default.png`.

#### code-chip

Inline code chip. An inline span.text-code ("doppler run") painted as a rounded black4 mono chip; the only real code element on the public pages — CLI samples elsewhere are baked into mock imagery.

Page: agents. Selector: `span.text-code on /agents`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 56.97 x 29.59 |
| Padding | 2px 8px |
| Border | none |
| Radius | 6px |
| Background | #f2f1ed @ 0.04 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerReproMono_e3cbb4 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #f55c15 |
| Transition | none |
| Painted layers | span.text-code.mx-4 57.0x29.6 bg #f2f1ed @ 0.04 r 6px |
| How | at rest |

Crops: `code-chip-default.png`.

### Footer

#### footer

Footer. The marketing footer: link columns, legal, social icons and the Cookie Preferences button.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1400 x 718.38 |
| Padding | 32px |
| Border | none |
| Radius | 20px |
| Background | #1c1624 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | span: __DopplerRepro_a18e76 12px/12px 400, #f1f0ec, ls 0.36px |
| Transition | none |
| Painted layers | footer.rounded-b-0.rounded-t-20 1400.0x718.4 bg #1c1624 r 20px; a.ease.flex 201.0x40.0 bg #f2f1ed @ 0.04 border T:2px solid #ffffff @ 0.08 / R:2px solid #ffffff @ 0.08 / B:2px solid #ffffff @ 0.08 / L:2px solid #ffffff @ 0.08 r 20px; div.h-20.w-20 20.0x20.0 bg #00f575 r 9999px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200.98 x 40 | = | = | = |
| Padding | 8px 10px | = | = | = |
| Gap | 10px | = | = | = |
| Border | 2px solid #ffffff @ 0.08 | = | = | = |
| Radius | 20px | = | = | = |
| Background | #f2f1ed @ 0.04 | #f2f1ed @ 0.08 | #f2f1ed @ 0.08 | #f2f1ed @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 12px/12px 400 | = | = | = |
| Letter spacing | 0.36px | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Text node | span: __DopplerRepro_a18e76 12px/12px 400, #f1f0ec, ls 0.36px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ease.flex 201.0x40.0 bg #f2f1ed @ 0.04 border T:2px solid #ffffff @ 0.08 / R:2px solid #ffffff @ 0.08 / B:2px solid #ffffff @ 0.08 / L:2px solid #ffffff @ 0.08 r 20px; div.h-20.w-20 20.0x20.0 bg #00f575 r 9999px | a.ease.flex 201.0x40.0 bg #f2f1ed @ 0.08 border T:2px solid #ffffff @ 0.08 / R:2px solid #ffffff @ 0.08 / B:2px solid #ffffff @ 0.08 / L:2px solid #ffffff @ 0.08 r 20px; div.h-20.w-20 20.0x20.0 bg #00f575 r 9999px | a.ease.flex 201.0x40.0 bg #f2f1ed @ 0.08 border T:2px solid #ffffff @ 0.08 / R:2px solid #ffffff @ 0.08 / B:2px solid #ffffff @ 0.08 / L:2px solid #ffffff @ 0.08 r 20px outline 1px auto #005fcc offset 1px; div.h-20.w-20 20.0x20.0 bg #00f575 r 9999px | a.ease.flex 201.0x40.0 bg #f2f1ed @ 0.08 border T:2px solid #ffffff @ 0.08 / R:2px solid #ffffff @ 0.08 / B:2px solid #ffffff @ 0.08 / L:2px solid #ffffff @ 0.08 r 20px; div.h-20.w-20 20.0x20.0 bg #00f575 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### cookie-button

Cookie button. The footer Cookie-Preferences button; measured, never pressed (it would open the consent panel).

Page: home. Selector: `"Cookie Preferences" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 307.3 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #d0c9c4 | #f1f0ec | = | #f1f0ec |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #d0c9c4, ls 0.15px | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px | = | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #f1f0ec, ls 0.15px |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.inline-flex.items-center 307.3x15.0 outline 1px auto #005fcc offset 0px | = |

Crops: `cookie-button-default.png`, `cookie-button-hover.png`, `cookie-button-focus-visible.png`, `cookie-button-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 16px |
| Border | T: none; R: 1px solid #55505b; B: 1px solid #55505b; L: 1px solid #55505b |
| Radius | 0px 0px 16px 16px |
| Background | #1c1624 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Transition | none |
| Icon | 0 x 0, colour #d0c9c4 |
| Painted layers | header.flex.h-[72px] 390.0x72.0 bg #1c1624 border R:1px solid #55505b / B:1px solid #55505b / L:1px solid #55505b r 0px 0px 16px 16px; div.transition-transform.duration-[350ms] 18.0x2.0 bg #f1f0ec; div.transition-transform.duration-[350ms] 18.0x2.0 bg #f1f0ec; div.transition-transform.duration-[350ms] 18.0x2.0 bg #f1f0ec; div.absolute.left-[10%] 0.0x0.0 bg #1c1624 border R:1px solid #55505b / B:1px solid #55505b / L:1px solid #55505b r 0px 0px 20px 20px; div.absolute.left-[10%] 0.0x0.0 bg #1c1624 border R:1px solid #55505b / B:1px solid #55505b / L:1px solid #55505b r 0px 0px 20px 20px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header hamburger toggle.

Page: mobile. Selector: `header menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.transition-transform.duration-[350ms] 18.0x2.0 bg #f1f0ec; div.transition-transform.duration-[350ms] 18.0x2.0 bg #f1f0ec; div.transition-transform.duration-[350ms] 18.0x2.0 bg #f1f0ec |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The header menu panel opened by its own toggle.

Page: mobile. Selector: `mobile menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 789 |
| Padding | 30px 16px |
| Border | T: none; R: 1px solid #55505b; B: 1px solid #55505b; L: 1px solid #55505b |
| Radius | 0px |
| Background | #1c1624 |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 16px/24px 400 |
| Letter spacing | normal |
| Colour | #f1f0ec |
| Text node | span: __DopplerRepro_a18e76 24px/33.6px 700, #f1f0ec, ls -0.24px |
| Transition | none |
| Icon | 16 x 10.28, colour #f1f0ec |
| Painted layers | div.flex.scrollbar-hidden 390.0x789.0 bg #1c1624 border R:1px solid #55505b / B:1px solid #55505b / L:1px solid #55505b; div.relative.border-b-1 356.0x50.6 border B:1px solid #ffffff @ 0.08; div.flex.flex-col 0.0x0.0 border T:1px solid #ffffff @ 0.08; div.relative.border-b-1 356.0x50.6 border B:1px solid #ffffff @ 0.08; div.flex.flex-col 0.0x0.0 border T:1px solid #ffffff @ 0.08; div.relative.border-b-1 356.0x50.6 border B:1px solid #ffffff @ 0.08 |
| Ancestor paint | 1 up div.jsx-3454204684.overflow-x-clip bg #1c1624 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened header menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 356 x 50.59 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.08; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 24px/33.6px 700 | = | = | = |
| Letter spacing | -0.24px | = | = | = |
| Colour | #f1f0ec | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.items-center 356.0x50.6 border B:1px solid #ffffff @ 0.08 | = | a.flex.items-center 356.0x50.6 border B:1px solid #ffffff @ 0.08 outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 228.64 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | __DopplerRepro_a18e76 36px/36px 450 |
| Letter spacing | -0.72px |
| Colour | #f1f0ec |
| Text node | span.block: __DopplerRepro_a18e76 36px/36px 450, #f1f0ec, ls -0.72px |
| Transition | none |
| Painted layers | span.inline.bg-clip-text 211.2x56.0 image linear-gradient(91deg, #855aff 14.92%, #ff5632 90.53%) |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-cta

Mobile CTA. The hero Start-for-Free button at phone width; measured never followed.

Page: mobile. Selector: `mobile "Start for Free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 156.31 x 36.05 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #00f575 | = | = | #00bf5b |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | __DopplerRepro_a18e76 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1624 | = | = | = |
| Text node | span.text-navLink: __DopplerRepro_a18e76 15px/15px 700, #1c1624, ls 0.15px | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 12, colour #1c1624 | = | = | = |
| Painted layers | a.group.inline-flex 156.3x36.0 bg #00f575 r 12px | = | a.group.inline-flex 156.3x36.0 bg #00f575 r 12px outline 1px auto #005fcc offset 1px | a.group.inline-flex 156.3x36.0 bg #00bf5b r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

## Transitions declared in the readable stylesheets

doppler.com serves its Next.js CSS bundles same-origin under /_next/static/css, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- agents: `opacity 0.5s`, `border-color 0.3s`, `background-color 0.3s`, `transform 0.3s cubic-bezier(0.8, 0.01, 0.11, 0.9)`, `opacity 0.3s`, `0.2s ease-in-out`, `0.3s cubic-bezier(0.75, -0.02, 0.2, 0.97)`

- blog: `opacity 0.5s`, `border-color 0.3s`, `background-color 0.3s`, `transform 0.3s cubic-bezier(0.8, 0.01, 0.11, 0.9)`, `opacity 0.3s`, `0.2s ease-in-out`, `0.3s cubic-bezier(0.75, -0.02, 0.2, 0.97)`

- customers: `opacity 0.5s`, `border-color 0.3s`, `background-color 0.3s`, `transform 0.3s cubic-bezier(0.8, 0.01, 0.11, 0.9)`, `opacity 0.3s`, `0.2s ease-in-out`, `0.3s cubic-bezier(0.75, -0.02, 0.2, 0.97)`

- demo: `opacity 0.5s`, `border-color 0.3s`, `background-color 0.3s`, `transform 0.3s cubic-bezier(0.8, 0.01, 0.11, 0.9)`, `opacity 0.3s`, `0.2s ease-in-out`

- home: `opacity 0.5s`, `border-color 0.3s`, `background-color 0.3s`, `transform 0.3s cubic-bezier(0.8, 0.01, 0.11, 0.9)`, `opacity 0.3s`, `0.2s ease-in-out`

- integrations: `opacity 0.5s`, `border-color 0.3s`, `background-color 0.3s`, `transform 0.3s cubic-bezier(0.8, 0.01, 0.11, 0.9)`, `opacity 0.3s`, `0.2s ease-in-out`

- platform: `opacity 0.5s`, `border-color 0.3s`, `background-color 0.3s`, `transform 0.3s cubic-bezier(0.8, 0.01, 0.11, 0.9)`, `opacity 0.3s`, `0.2s ease-in-out`

- pricing: `opacity 0.5s`, `border-color 0.3s`, `background-color 0.3s`, `transform 0.3s cubic-bezier(0.8, 0.01, 0.11, 0.9)`, `opacity 0.3s`, `0.2s ease-in-out`, `0.3s cubic-bezier(0.75, -0.02, 0.2, 0.97)`
