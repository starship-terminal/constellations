# Visual (designstripe) component measurements

Computed styles read from visual.app on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — home, /assets, /assets/avatars/replicants, /tools, /contact and /blog/branding-consistency — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and navigation

#### mkt-nav

Site nav. The fixed top nav: VISUAL wordmark, section links (WHY VISUAL? / ASSETS / TOOLS / BLOG) and the WAITLIST button.

Page: assets. Selector: `nav.fixed`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 32 |
| Padding | 0px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontMono 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.ui:inline-flex.ui:items-center: fontMono 12px/12px 500, #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | a.ui:inline-flex.ui:items-center 88.0x32.0 bg #2c2c26 r 4px; ul.items-center.ml-auto 256.0x32.0 bg #ffffff border T:1px solid #d0d0c8 / R:1px solid #d0d0c8 / B:1px solid #d0d0c8 / L:1px solid #d0d0c8 r 4px; a.whitespace-nowrap.flex 93.0x24.0 bg #ffffff r 3px; a.whitespace-nowrap.flex 58.0x24.0 bg #ffffff r 3px; a.whitespace-nowrap.flex 51.0x24.0 bg #ffffff r 3px; a.whitespace-nowrap.flex 44.0x24.0 bg #ffffff r 3px |
| Ancestor paint | 1 up body.__variable_776c64.__variable_8888f9 bg #ffffff |
| How | at rest |

Crops: `mkt-nav-default.png`.

#### mkt-logo

Logo. The VISUAL wordmark at the left of the nav.

Page: assets. Selector: `nav VISUAL`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 88 x 32 |
| Padding | 0px 12px |
| Gap | 6px |
| Border | none |
| Radius | 4px |
| Background | #2c2c26 |
| Box shadow | none |
| Outline | none |
| Font | fontMono 12px/12px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | a.ui:inline-flex.ui:items-center 88.0x32.0 bg #2c2c26 r 4px |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-link

Nav link. A section link in the top nav ("WHY VISUAL?"); measured, never followed.

Page: assets. Selector: `nav WHY VISUAL?`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93 x 24 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | #ffffff | #f6f6f4 | = | #f6f6f4 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.whitespace-nowrap.flex 93.0x24.0 bg #ffffff r 3px | a.whitespace-nowrap.flex 93.0x24.0 bg #f6f6f4 r 3px | a.whitespace-nowrap.flex 93.0x24.0 bg #ffffff r 3px outline 1px auto #101010 offset 1px | a.whitespace-nowrap.flex 93.0x24.0 bg #f6f6f4 r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### waitlist-btn

Waitlist CTA. The nav WAITLIST button — the product’s only conversion CTA on this surface; measured, never pressed (it joins a waitlist).

Page: assets. Selector: `nav WAITLIST`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #aaa674 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #e8e7d9 | #414238 | = | #414238 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2c2c26 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 1px solid #ffffff offset -1px | = |
| Font | fontMono 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2c2c26 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ui:inline-flex.ui:items-center 82.0x32.0 bg #e8e7d9 border T:1px solid #aaa674 / R:1px solid #aaa674 / B:1px solid #aaa674 / L:1px solid #aaa674 r 3.35544e+07px | button.ui:inline-flex.ui:items-center 82.0x32.0 bg #414238 border T:1px solid #aaa674 / R:1px solid #aaa674 / B:1px solid #aaa674 / L:1px solid #aaa674 r 3.35544e+07px | button.ui:inline-flex.ui:items-center 82.0x32.0 bg #e8e7d9 border T:1px solid #aaa674 / R:1px solid #aaa674 / B:1px solid #aaa674 / L:1px solid #aaa674 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2c2c26 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 1px solid #ffffff offset -1px | button.ui:inline-flex.ui:items-center 82.0x32.0 bg #414238 border T:1px solid #aaa674 / R:1px solid #aaa674 / B:1px solid #aaa674 / L:1px solid #aaa674 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `waitlist-btn-default.png`, `waitlist-btn-hover.png`, `waitlist-btn-focus-visible.png`, `waitlist-btn-pressed.png`.

### Home

#### hero-h1

Hero headline. "Design Agents for Revenue Teams" — the serif display heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 708 x 180 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 96px/90px 400 |
| Letter spacing | -4.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: none.

#### hero-sub

Hero subcopy. The supporting paragraph under the hero heading.

Page: home. Selector: `hero p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 39.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontMono 14px/19.796px 500 |
| Letter spacing | normal |
| Colour | #6d6e5e |
| Transition | none |
| How | at rest |

Crops: none.

#### feature-acc

Feature accordion. A monospace feature accordion row on the dark panel ("Chat-driven for everyone on the team"); its opened state is the already-expanded first row, measured as painted.

Page: home. Selector: `feature accordion button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 568.66 x 60.27 | - | = | = | = |
| Padding | 16px 0px 16px 32px | - | = | = | = |
| Border | none | - | = | = | = |
| Radius | 0px | - | = | = | = |
| Background | transparent | - | = | = | = |
| Box shadow | none | - | = | = | = |
| Outline | none | - | 1px auto #101010 offset 0px | = | = |
| Font | fontMono 20px/28.28px 500 | - | = | = | = |
| Letter spacing | normal | - | = | = | = |
| Colour | #ffffff | - | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | - | = | = | = |
| Cursor | default | - | = | = | = |
| Icon | 16 x 16, colour #aaab9c | - | = | = | = |
| ::before | 14px x 20px, absolute, bg #000000 @ 0, radius 0px | - | = | = | = |
| How | at rest | - | Shift+Tab, Tab | CDP forcePseudoState :active:hover | held open by an earlier toggle |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('button').filter({ hasText: /Chat-driven for everyone/i }).and(locator(':visible')).first().and(locator(':visible')).first().a | = | = | = |
| Painted layers | - | = | button.ui:flex.ui:flex-1 568.7x60.3 outline 1px auto #101010 offset 0px | = | = |

Crops: `feature-acc-focus-visible.png`, `feature-acc-pressed.png`, `feature-acc-opened.png`.

#### sec-h2

Section heading. A serif section heading ("Keep every slide on-brand").

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312.39 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 48px/48px 300 |
| Letter spacing | -1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `sec-h2-default.png`.

#### dark-h2

Dark-panel heading. The white serif heading inside the dark feature panel ("Every agent is an endpoint").

Page: home. Selector: `dark h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 312.39 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 48px/48px 300 |
| Letter spacing | -1.2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: none.

#### feature-acc2

Accordion (closed). The closed "Quickly personalize every presentation" accordion row; its opened state is toggled locally to reveal the panel copy.

Page: home. Selector: `feature accordion button 2`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 568.66 x 60.27 | - | - | - | = |
| Padding | 16px 0px 16px 32px | - | - | - | = |
| Border | none | - | - | - | = |
| Radius | 0px | - | - | - | = |
| Background | transparent | - | - | - | = |
| Box shadow | none | - | - | - | = |
| Outline | none | - | - | - | = |
| Font | fontMono 20px/28.28px 500 | - | - | - | = |
| Letter spacing | normal | - | - | - | = |
| Colour | #ffffff | - | - | - | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | - | - | - | = |
| Cursor | default | - | - | - | = |
| Icon | 16 x 16, colour #aaab9c | - | - | - | = |
| ::before | 14px x 20px, absolute, bg #000000 @ 0, radius 0px | - | - | - | = |
| How | at rest | - | - | - | own toggle |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('button').filter({ hasText: /Quickly personalize/i }).and(locator(':visible')).first().and(locator(':visible')).first().and(lo | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('button').filter({ hasText: /Quickly personalize/i }).and(locator(':visible')).first().and(locator(':visible')).first().and | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('button').filter({ hasText: /Quickly personalize/i }).and(locator(':visible')).first().and(locator(':visible')).first().and | = |

Crops: `feature-acc2-default.png`, `feature-acc2-opened.png`.

### Footer

#### site-footer

Site footer. The sitemap footer (BLOG / ASSET LIBRARY / DESIGN TOOLS / ABOUT / CONTACT / LINKEDIN).

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 320 |
| Padding | 32px 24px |
| Border | none |
| Radius | 0px |
| Background | #2c2c26 |
| Box shadow | none |
| Outline | none |
| Font | fontMono 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.hover:underline.text-xs: fontMono 12px/12px 500, #ffffff |
| Transition | none |
| Painted layers | footer.bg-foreground.px-4 1440.0x320.0 bg #2c2c26; button.ui:inline-flex.ui:items-center 80.0x32.0 bg #ffffff r 3.35544e+07px |
| Ancestor paint | 1 up body.__variable_776c64.__variable_8888f9 bg #ffffff |
| How | at rest |

Crops: none.

### Asset library

#### ast-h1

Library heading. "Asset Library" — the 96px serif page heading in the olive ink.

Page: assets. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 684 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 96px/96px 400 |
| Letter spacing | -4.8px |
| Colour | #2c2c26 |
| Transition | none |
| How | at rest |

Crops: `ast-h1-default.png`.

#### ast-tile-hero

Hero category tile. The featured category tile (569px rounded-xl square, "/ REPLICANTS" label over a preview); measured, never followed.

Page: assets. Selector: `a.aspect-square`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 568.66 x 568.66 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Background image | linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de), linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.inline-flex.items-center: fontMono 10px/10px 500, #6d6e5e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6d6e5e | = | = | = |
| Painted layers | a.flex.aspect-square 568.7x568.7 bg #ffffff image linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de r 8px; div.inline-flex.items-center 106.0x24.0 bg #e3e3de @ 0.5 r 3px | = | a.flex.aspect-square 568.7x568.7 bg #ffffff image linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de r 8px outline 1px auto #101010 offset 1px; div.inline-flex.items-center 106.0x24.0 bg #e3e3de @ 0.5 r 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ast-tile-hero-default.png`, `ast-tile-hero-hover.png`, `ast-tile-hero-focus-visible.png`, `ast-tile-hero-pressed.png`.

#### ast-tile

Category tile. A standard category tile (280px rounded-xl square); measured, never followed.

Page: assets. Selector: `a.aspect-square small`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280.33 x 280.33 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Background image | linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de), linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.inline-flex.items-center: fontMono 10px/10px 500, #6d6e5e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6d6e5e | = | = | = |
| Painted layers | a.flex.aspect-square 280.3x280.3 bg #ffffff image linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de r 8px; div.inline-flex.items-center 100.0x24.0 bg #e3e3de @ 0.5 r 3px | = | a.flex.aspect-square 280.3x280.3 bg #ffffff image linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de r 8px outline 1px auto #101010 offset 1px; div.inline-flex.items-center 100.0x24.0 bg #e3e3de @ 0.5 r 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ast-tile-default.png`, `ast-tile-hover.png`, `ast-tile-focus-visible.png`, `ast-tile-pressed.png`.

#### ast-tile-img

Tile preview. A category tile’s preview image (object-cover inside the rounded square).

Page: assets. Selector: `tile img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 568.66 x 568.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontMono 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up a.flex.aspect-square bg #ffffff |
| How | at rest |

Crops: `ast-tile-img-default.png`.

#### ast-kind-link

Kind link. A library kind link ("Illustrations" / "Avatars") that sections the grid; measured, never followed.

Page: assets. Selector: `kind link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 20px/28.28px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2c2c26 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-primary 84.0x22.0 outline 1px auto #101010 offset 1px | = |

Crops: `ast-kind-link-default.png`, `ast-kind-link-hover.png`, `ast-kind-link-focus-visible.png`, `ast-kind-link-pressed.png`.

### Avatar set gallery

#### av-h1

Set heading. The avatar-set page heading.

Page: avatars. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 684 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 96px/96px 400 |
| Letter spacing | -4.8px |
| Colour | #2c2c26 |
| Transition | none |
| How | at rest |

Crops: `av-h1-default.png`.

#### av-back

Back link. The link back to the asset library; measured, never followed.

Page: avatars. Selector: `back link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58 x 24 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3px | = | = | = |
| Background | #ffffff | #f6f6f4 | = | #f6f6f4 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.whitespace-nowrap.flex 58.0x24.0 bg #ffffff r 3px | a.whitespace-nowrap.flex 58.0x24.0 bg #f6f6f4 r 3px | a.whitespace-nowrap.flex 58.0x24.0 bg #ffffff r 3px outline 1px auto #101010 offset 1px | a.whitespace-nowrap.flex 58.0x24.0 bg #f6f6f4 r 3px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `av-back-default.png`, `av-back-hover.png`, `av-back-focus-visible.png`, `av-back-pressed.png`.

#### av-item

Avatar item. An avatar tile in the set grid (links to its detail page); measured, never followed.

Page: avatars. Selector: `avatar tile`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 222.66 x 222.66 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Background image | linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de), linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.aspect-square 222.7x222.7 bg #ffffff image linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de r 8px | = | a.flex.aspect-square 222.7x222.7 bg #ffffff image linear-gradient(45deg, #e3e3de 25%, #000000 @ 0 25%, #000000 @ 0 75%, #e3e3de 75%, #e3e3de r 8px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `av-item-default.png`, `av-item-hover.png`, `av-item-focus-visible.png`, `av-item-pressed.png`.

#### av-thumb

Avatar image. An avatar preview image in the set grid.

Page: avatars. Selector: `avatar img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 222.66 x 222.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontMono 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up a.flex.aspect-square bg #ffffff |
| How | at rest |

Crops: `av-thumb-default.png`.

#### av-kind

Kind crumb. The AVATARS kind crumb over the set grid; measured, never followed.

Page: avatars. Selector: `kind crumb`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 49 x 12 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 12px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6d6e5e | #2c2c26 | = | #2c2c26 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.ui:text-neutral-700.ui:hover:text-foreground 49.0x12.0 outline 1px auto #101010 offset 1px | = |

Crops: `av-kind-default.png`, `av-kind-hover.png`, `av-kind-focus-visible.png`, `av-kind-pressed.png`.

### Design tools

#### tool-h1

Tools heading. "Design Tools" — the 96px serif page heading.

Page: tools. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 684 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 96px/96px 400 |
| Letter spacing | -4.8px |
| Colour | #2c2c26 |
| Transition | none |
| How | at rest |

Crops: `tool-h1-default.png`.

#### tool-card

Tool card. A tool card ("Color Wheel" — bordered white card with a breadcrumb label, title and copy); measured, never followed.

Page: tools. Selector: `tool card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 338 x 422.5 | = | = | = |
| Padding | 24px 24px 20px 24px | = | = | = |
| Border | 1px solid #d0d0c8 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-neutral-700: fontMono 12px/12px 500, #6d6e5e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-col 338.0x422.5 bg #ffffff border T:1px solid #d0d0c8 / R:1px solid #d0d0c8 / B:1px solid #d0d0c8 / L:1px solid #d0d0c8 r 6px | = | a.flex.flex-col 338.0x422.5 bg #ffffff border T:1px solid #d0d0c8 / R:1px solid #d0d0c8 / B:1px solid #d0d0c8 / L:1px solid #d0d0c8 r 6px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tool-card-default.png`, `tool-card-hover.png`.

#### tool-card2

Tool card 2. A second tool card ("Image Resizer"), sampled for consistency.

Page: tools. Selector: `tool card 2`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 338 x 422.5 | = | = | = |
| Padding | 24px 24px 20px 24px | = | = | = |
| Border | 1px solid #d0d0c8 | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontMono 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-neutral-700: fontMono 12px/12px 500, #6d6e5e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-col 338.0x422.5 bg #ffffff border T:1px solid #d0d0c8 / R:1px solid #d0d0c8 / B:1px solid #d0d0c8 / L:1px solid #d0d0c8 r 6px | = | a.flex.flex-col 338.0x422.5 bg #ffffff border T:1px solid #d0d0c8 / R:1px solid #d0d0c8 / B:1px solid #d0d0c8 / L:1px solid #d0d0c8 r 6px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tool-card2-default.png`, `tool-card2-hover.png`, `tool-card2-focus-visible.png`.

#### tool-crumb

Card breadcrumb. The "colors" kind crumb on a tool card (paired with its "Tools" label).

Page: tools. Selector: `card crumb`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontMono 12px/12px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `tool-crumb-default.png`.

### Contact

#### ct-h1

Contact heading. "Contact" — the 96px serif page heading.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 684 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 96px/96px 400 |
| Letter spacing | -4.8px |
| Colour | #2c2c26 |
| Transition | none |
| How | at rest |

Crops: `ct-h1-default.png`.

#### ct-copy

Contact copy. The supporting paragraph on the contact page.

Page: contact. Selector: `contact p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 453.33 x 39.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontMono 14px/19.796px 500 |
| Letter spacing | normal |
| Colour | #6d6e5e |
| Transition | none |
| How | at rest |

Crops: `ct-copy-default.png`.

### Blog article

#### post-h1

Article heading. The article title heading.

Page: post. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 914.67 x 128 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 64px/64px 400 |
| Letter spacing | -3.2px |
| Colour | #2c2c26 |
| Transition | none |
| How | at rest |

Crops: `post-h1-default.png`.

#### post-para

Article paragraph. A body paragraph in the article.

Page: post. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 453.33 x 19.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontMono 14px/19.796px 500 |
| Letter spacing | normal |
| Colour | #6d6e5e |
| Transition | none |
| How | at rest |

Crops: `post-para-default.png`.

#### post-link

Article link. An inline link inside the article body; measured, never followed.

Page: post. Selector: `article a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36.63 x 25 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | fontSerif 20px/30px 400 | = | = | = |
| Letter spacing | -0.125px | = | = | = |
| Colour | #7e7b4e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 36.6x25.0 outline 1px auto #101010 offset 1px | = |

Crops: `post-link-default.png`, `post-link-hover.png`, `post-link-focus-visible.png`, `post-link-pressed.png`.

### Mobile (390 wide)

#### m-nav

Mobile nav. The phone top bar: VISUAL wordmark and the WAITLIST button.

Page: mobile. Selector: `mobile nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 40 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontMono 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.ui:inline-flex.ui:items-center: fontMono 12px/12px 500, #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #ffffff |
| Painted layers | a.ui:inline-flex.ui:items-center 88.0x32.0 bg #2c2c26 r 4px; a.whitespace-nowrap.flex 0.0x0.0 bg #ffffff r 3px; a.whitespace-nowrap.flex 0.0x0.0 bg #ffffff r 3px; a.whitespace-nowrap.flex 0.0x0.0 bg #ffffff r 3px; a.whitespace-nowrap.flex 0.0x0.0 bg #ffffff r 3px; button.ui:justify-center.ui:whitespace-nowrap 50.0x40.0 bg #ffffff border T:1px solid #d0d0c8 / R:1px solid #d0d0c8 / B:1px solid #d0d0c8 / L:1px solid #d0d0c8 r 3.35544e+07px |
| Ancestor paint | 1 up body.__variable_776c64.__variable_8888f9 bg #ffffff |
| How | at rest |

Crops: none.

#### m-h1

Mobile headline. The phone hero heading.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 90 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fontSerif 48px/45px 400 |
| Letter spacing | -2.4px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: none.

#### m-acc

Mobile accordion. A feature accordion row on the phone; measured, never toggled here.

Page: mobile. Selector: `mobile accordion`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 64 | = | = | = |
| Padding | 16px 0px 16px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | fontMono 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #aaab9c | = | = | = |
| ::before | 14px x 16px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.ui:flex.ui:flex-1 350.0x64.0 outline 1px auto #e59700 offset 0px | = |

Crops: `m-acc-hover.png`, `m-acc-focus-visible.png`, `m-acc-pressed.png`.

#### m-footer

Mobile footer. The phone footer.

Page: mobile. Selector: `mobile footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 316 |
| Padding | 32px 16px |
| Border | none |
| Radius | 0px |
| Background | #2c2c26 |
| Box shadow | none |
| Outline | none |
| Font | fontMono 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.hover:underline.text-xs: fontMono 12px/12px 500, #ffffff |
| Transition | none |
| Painted layers | footer.bg-foreground.px-4 390.0x316.0 bg #2c2c26; button.ui:inline-flex.ui:items-center 80.0x32.0 bg #ffffff r 3.35544e+07px |
| Ancestor paint | 1 up body.__variable_776c64.__variable_8888f9 bg #ffffff |
| How | at rest |

Crops: `m-footer-default.png`.

## Transitions declared in the readable stylesheets

visual.app serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- assets: `background-color 1ms,outline-color 1ms,color var(--transition-duration-10) ease-in-out,dir 1ms`, `opacity var(--transition-duration-50) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out`, `opacity var(--transition-duration-10) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out,box-shadow var(--transition-duration-10) ease-out`, `border-radius 1ms`, `background-color var(--transition-duration-10),color var(--transition-duration-10)`, `background-color var(--transition-duration-10)`, `background-color var(--transition-duration-10) ease-in-out,color var(--transition-duration-10) ease-in-out,border-color var(--transition-duration-10) ease-in-out`, `filter var(--transition-duration-10) ease-out`, `stroke-dashoffset 0.5s linear, stroke-dasharray 0.5s linear`, `opacity 0.15s 0.25s`

- avatars: `background-color 1ms,outline-color 1ms,color var(--transition-duration-10) ease-in-out,dir 1ms`, `opacity var(--transition-duration-50) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out`, `opacity var(--transition-duration-10) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out,box-shadow var(--transition-duration-10) ease-out`, `border-radius 1ms`, `background-color var(--transition-duration-10),color var(--transition-duration-10)`, `background-color var(--transition-duration-10)`, `background-color var(--transition-duration-10) ease-in-out,color var(--transition-duration-10) ease-in-out,border-color var(--transition-duration-10) ease-in-out`, `filter var(--transition-duration-10) ease-out`, `stroke-dashoffset 0.5s linear, stroke-dasharray 0.5s linear`, `opacity 0.15s 0.25s`

- contact: `background-color 1ms,outline-color 1ms,color var(--transition-duration-10) ease-in-out,dir 1ms`, `opacity var(--transition-duration-50) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out`, `opacity var(--transition-duration-10) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out,box-shadow var(--transition-duration-10) ease-out`, `border-radius 1ms`, `background-color var(--transition-duration-10),color var(--transition-duration-10)`, `background-color var(--transition-duration-10)`, `background-color var(--transition-duration-10) ease-in-out,color var(--transition-duration-10) ease-in-out,border-color var(--transition-duration-10) ease-in-out`, `filter var(--transition-duration-10) ease-out`, `stroke-dashoffset 0.5s linear, stroke-dasharray 0.5s linear`, `opacity 0.15s 0.25s`

- home: `background-color 1ms,outline-color 1ms,color var(--transition-duration-10) ease-in-out,dir 1ms`, `opacity var(--transition-duration-50) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out`, `opacity var(--transition-duration-10) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out,box-shadow var(--transition-duration-10) ease-out`, `border-radius 1ms`, `background-color var(--transition-duration-10),color var(--transition-duration-10)`, `background-color var(--transition-duration-10)`, `background-color var(--transition-duration-10) ease-in-out,color var(--transition-duration-10) ease-in-out,border-color var(--transition-duration-10) ease-in-out`, `filter var(--transition-duration-10) ease-out`, `stroke-dashoffset 0.5s linear, stroke-dasharray 0.5s linear`, `opacity 0.15s 0.25s`

- post: `background-color 1ms,outline-color 1ms,color var(--transition-duration-10) ease-in-out,dir 1ms`, `opacity var(--transition-duration-50) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out`, `opacity var(--transition-duration-10) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out,box-shadow var(--transition-duration-10) ease-out`, `border-radius 1ms`, `background-color var(--transition-duration-10),color var(--transition-duration-10)`, `background-color var(--transition-duration-10)`, `background-color var(--transition-duration-10) ease-in-out,color var(--transition-duration-10) ease-in-out,border-color var(--transition-duration-10) ease-in-out`, `filter var(--transition-duration-10) ease-out`, `stroke-dashoffset 0.5s linear, stroke-dasharray 0.5s linear`, `opacity 0.15s 0.25s`

- tools: `background-color 1ms,outline-color 1ms,color var(--transition-duration-10) ease-in-out,dir 1ms`, `opacity var(--transition-duration-50) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out`, `opacity var(--transition-duration-10) ease-out`, `background-color var(--transition-duration-10) ease-out,color var(--transition-duration-10) ease-out,box-shadow var(--transition-duration-10) ease-out`, `border-radius 1ms`, `background-color var(--transition-duration-10),color var(--transition-duration-10)`, `background-color var(--transition-duration-10)`, `background-color var(--transition-duration-10) ease-in-out,color var(--transition-duration-10) ease-in-out,border-color var(--transition-duration-10) ease-in-out`, `filter var(--transition-duration-10) ease-out`, `stroke-dashoffset 0.5s linear, stroke-dasharray 0.5s linear`, `opacity 0.15s 0.25s`
