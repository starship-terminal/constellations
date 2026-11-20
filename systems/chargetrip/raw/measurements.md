# Component measurements

Computed styles read from www.chargetrip.com (plus the public account.chargetrip.io sign-in card) on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (the "Cookie Settings" card was hidden, never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The white 64px top bar: wordmark, the Products/Use-cases/Developers/Pricing/Company menu triggers, and the Contact-sales + Sign-in buttons.

Page: home. Selector: `div[data-framer-name="Content"] at y=0`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 16px 0px 0px 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #efede5 |
| Transition | none |
| Icon | 106 x 24, colour #000000 |
| Painted layers | a.framer-SWyCz.framer-i5yBN 139.0x40.0 bg #262322 r 8px; a::after.framer-SWyCz.framer-i5yBN 83pxx40px border T:1px solid #262322 / R:1px solid #262322 / B:1px solid #262322 / L:1px solid #262322 r 8px; a.framer-39qt1e.framer-152olpk 453.3x776.0 bg #efede5 r 8px; a.framer-2ndwuz.framer-152olpk 453.3x776.0 bg #efede5 r 8px; a.framer-vb2o8e.framer-152olpk 453.3x776.0 bg #efede5 r 8px; div.framer-1m7ojrj 16.0x16.0 image url(data:…)%22 stroke-linecap=%22square%22 stroke-linejoin=%22round%22 stroke-dasharray=%2 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The chargetrip wordmark anchor.

Page: home. Selector: `first header a holding an svg/img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 106 x 24 |
| Padding | 0px |
| Gap | 10px |
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
| Icon | 106 x 24, colour #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav item. The "Products" menu trigger; its own press opens the mega menu (opened state, then the menu stays up for the next two entries).

Page: home. Selector: `div[text=Products] inside the bar`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 99 x 32 | = | - | = | = |
| Padding | 0px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | sans-serif 12px/normal 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #000000 | = | - | = | = |
| Text node | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #262322 | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #dc3b04 | - | = | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #dd3b00 |
| Transition | none | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | div.framer-tBbOV.framer-i5yBN 99.0x32.0 bg #dd3b00 @ 0.15 r 24px | = | = | div.framer-tBbOV.framer-i5yBN 99.0x32.0 bg #dd3b00 @ 0.15 r 24px |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-pressed.png`, `nav-item-opened.png`.

#### menu-panel

Mega menu. The Products mega-menu card row (No-code / API / Integration Partners photo cards), held open by the nav-item toggle.

Page: home. Selector: `card-row ancestor of the in-menu a[href="./no-code"] (top < 800, not the footer copy)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1376 x 816 |
| Padding | 0px 0px 40px 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-472in1: Geist Medium 22px/26px 400, #efede5 |
| Transition | none |
| Painted layers | a.framer-39qt1e.framer-152olpk 453.3x776.0 bg #efede5 r 8px; a.framer-2ndwuz.framer-152olpk 453.3x776.0 bg #efede5 r 8px; a.framer-vb2o8e.framer-152olpk 453.3x776.0 bg #efede5 r 8px |
| How | at rest |

Crops: `menu-panel-default.png`.

#### menu-card

Menu card. The No-code photo card inside the open mega menu.

Page: home. Selector: `card ancestor of the in-menu a[href="./no-code"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 453.33 x 776 |
| Padding | 16px |
| Gap | 0px |
| Border | none |
| Radius | 8px |
| Background | #efede5 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | p.framer-text.framer-styles-preset-472in1: Geist Medium 22px/26px 400, #efede5 |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.framer-39qt1e.framer-152olpk 453.3x776.0 bg #efede5 r 8px |
| How | at rest |

Crops: `menu-card-default.png`.

#### nav-cta

Nav CTA. The dark "Contact sales" button; links to /contact/sales, measured never followed.

Page: home. Selector: `a.Background Dark Primary / Fill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 40 | - | = | = |
| Padding | 0px 12px | - | = | = |
| Gap | 4px | - | = | = |
| Border | none | - | = | = |
| Radius | 8px | - | = | = |
| Background | #262322 | - | = | = |
| Box shadow | none | - | = | = |
| Outline | none | - | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | - | = | = |
| Letter spacing | normal | - | = | = |
| Colour | #0000ee | - | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #efede5 | - | = | = |
| Transition | none | - | = | = |
| Cursor | pointer | - | = | = |
| Painted layers | a.framer-SWyCz.framer-i5yBN 139.0x40.0 bg #262322 r 8px | - | a.framer-SWyCz.framer-i5yBN 139.0x40.0 bg #262322 r 8px outline 1px auto #101010 offset 1px | = |
| How | at rest | - | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Error | - | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('a[data-framer-name="Background Dark Primary / Fill"]').filter({ visible: true }).first().filter({ visible: true }).first() | = | = |

Crops: `nav-cta-default.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-signin

Sign-in button. The outlined "Sign in" button; links to account.chargetrip.com, measured never followed.

Page: home. Selector: `a.Background Dark Primary / Outline`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83 x 40 | - | = | = |
| Padding | 0px 12px | - | = | = |
| Gap | 4px | - | = | = |
| Border | none | - | = | = |
| Radius | 8px | - | = | = |
| Background | transparent | - | = | = |
| Box shadow | none | - | = | = |
| Outline | none | - | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | - | = | = |
| Letter spacing | normal | - | = | = |
| Colour | #0000ee | - | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #262322 | - | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #282322 | = |
| Transition | none | - | = | = |
| Cursor | pointer | - | = | = |
| ::after | 83px x 40px, absolute, bg #000000 @ 0, radius 8px | - | = | = |
| Painted layers | a::after.framer-SWyCz.framer-i5yBN 83pxx40px border T:1px solid #262322 / R:1px solid #262322 / B:1px solid #262322 / L:1px solid #262322 r 8px | - | a.framer-SWyCz.framer-i5yBN 83.0x40.0 r 8px outline 1px auto #101010 offset 1px; a::after.framer-SWyCz.framer-i5yBN 83pxx40px border T:1px solid #282322 / R:1px solid #282322 / B:1px solid #282322 / L:1px solid #282322 r 8px | = |
| How | at rest | - | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Error | - | locator.evaluate: Timeout 8000ms exceeded. Call log:   - waiting for locator('a[data-framer-name="Background Dark Primary / Outline"]').filter({ visible: true }).first().filter({ visible: true }).firs | = | = |

Crops: `nav-signin-default.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

### Home

#### hero-title

Hero title. The 88px Cirka display headline on the dark hero card.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 855.34 x 156 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Cirka Regular 88px/78px 400 |
| Letter spacing | -0.5px |
| Colour | #f4f3f2 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subcopy. The muted lede under the display headline.

Page: home. Selector: `the lede paragraph under h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 647.98 x 86.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #fffffb @ 0.52 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-card

Hero band. The dark rounded hero card the headline sits on.

Page: home. Selector: `dark ancestor of h1 (marked in-page)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1391.98 x 1086 |
| Padding | 72px 48px 0px 48px |
| Gap | 0px |
| Border | none |
| Radius | 24px |
| Background | transparent |
| Background image | radial-gradient(103% 223% at 49.2% 170.8%, #38312f 35%, #262321 67.3371%) |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.framer-text: Cirka Regular 88px/78px 400, #f4f3f2, ls -0.5px |
| Transition | none |
| Icon | 8 x 8, colour #0000ee, fill #000000 |
| Painted layers | div.framer-pl228f 1392.0x1086.0 image radial-gradient(103% 223% at 49.2% 170.8%, #38312f 35%, #262321 67.3371%) r 24px; a.framer-0phDM.framer-npPic 148.0x48.0 bg #f94d00 r 8px; div.framer-144aqy4 164.0x164.0 bg #fc652d r 999px; div.framer-e7hcqw 164.0x164.0 bg #dd3b00 r 999px; a.framer-0phDM.framer-npPic 179.0x48.0 bg #44403f r 8px; a::after.framer-0phDM.framer-npPic 179pxx48px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `hero-card-default.png`.

#### cta-accent

Accent CTA. The orange "Book a demo" button (links to a HubSpot meeting page, never followed).

Page: home. Selector: `a.Large / Accent`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 148 x 48 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f94d00 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-phy7qs: Geist Variable 16px/24px 400, #f4f3f2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 8 x 8, colour #0000ee, fill #000000 | = | = | 8 x 8, colour #ff0000, fill #000000 |
| Painted layers | a.framer-0phDM.framer-npPic 148.0x48.0 bg #f94d00 r 8px; div.framer-144aqy4 164.0x164.0 bg #fc652d r 999px; div.framer-e7hcqw 164.0x164.0 bg #dd3b00 r 999px | = | a.framer-0phDM.framer-npPic 148.0x48.0 bg #f94d00 r 8px outline 1px auto #101010 offset 1px; div.framer-144aqy4 164.0x164.0 bg #fc652d r 999px; div.framer-e7hcqw 164.0x164.0 bg #dd3b00 r 999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-accent-default.png`, `cta-accent-hover.png`, `cta-accent-focus-visible.png`, `cta-accent-pressed.png`.

#### cta-dark

Dark CTA. The dark "Plan a route" button with its map thumbnail (links to go.chargetrip.com, never followed).

Page: home. Selector: `a.Large / Dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 179 x 48 | = | = | = |
| Padding | 8px 12px 8px 4px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #44403f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-phy7qs: Geist Variable 16px/24px 400, #f4f3f2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 8 x 8, colour #0000ee, fill #000000 | = | = | 8 x 8, colour #ff0000, fill #000000 |
| ::after | 179px x 48px, absolute, bg #000000 @ 0, radius 8px | = | = | = |
| Painted layers | a.framer-0phDM.framer-npPic 179.0x48.0 bg #44403f r 8px; a::after.framer-0phDM.framer-npPic 179pxx48px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; div::after.framer-133laaa 40pxx40px border T:1px solid #44403f / R:1px solid #44403f / B:1px solid #44403f / L:1px solid #44403f r 4px; div.framer-144aqy4 195.0x195.0 bg #524c4a r 999px; div.framer-e7hcqw 195.0x195.0 bg #4d4846 r 999px | = | a.framer-0phDM.framer-npPic 179.0x48.0 bg #44403f r 8px outline 1px auto #101010 offset 1px; a::after.framer-0phDM.framer-npPic 179pxx48px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; div::after.framer-133laaa 40pxx40px border T:1px solid #44403f / R:1px solid #44403f / B:1px solid #44403f / L:1px solid #44403f r 4px; div.framer-144aqy4 195.0x195.0 bg #524c4a r 999px; div.framer-e7hcqw 195.0x195.0 bg #4d4846 r 999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-dark-default.png`, `cta-dark-hover.png`, `cta-dark-focus-visible.png`, `cta-dark-pressed.png`.

#### section-title

Section title.

Page: home. Selector: `first visible h2, marked where it mounts`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 619.98 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Cirka Regular 48px/48px 400 |
| Letter spacing | normal |
| Colour | #262322 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### page-ground

Page ground. The body element's own painted fill — the warm-cream ground under every section.

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 8274.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #efede5 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.framer-text: Cirka Regular 88px/78px 400, #f4f3f2, ls -0.5px |
| Transition | none |
| Icon | 8 x 8, colour #0000ee, fill #000000 |
| Painted layers | body 1440.0x8274.8 bg #efede5; div.framer-Up5El.framer-SVSxo 1440.0x8274.8 bg #efede5; div.framer-pl228f 1392.0x1086.0 image radial-gradient(103% 223% at 49.2% 170.8%, #38312f 35%, #262321 67.3371%) r 24px; a.framer-0phDM.framer-npPic 148.0x48.0 bg #f94d00 r 8px; div.framer-144aqy4 164.0x164.0 bg #fc652d r 999px; div.framer-e7hcqw 164.0x164.0 bg #dd3b00 r 999px |
| How | at rest |

Crops: none.

### Pricing

#### pricing-h1

Pricing title. "Build for free and go live with the best plan for you." in 88px Cirka.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 998.38 x 234 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Cirka Regular 88px/78px 400 |
| Letter spacing | -0.5px |
| Colour | #262322 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### logo-chip

Customer chip. A dark customer-logo chip under the headline (Plugsurfing).

Page: pricing. Selector: `a:has-text("Plugsurfing")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1247.98 x 93.5 | = | = | = |
| Padding | 24px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #262322 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Geist Variable 18px/25.2px 400, #f4f3f2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 1247.98px x 93.5px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.framer-CVbmc.framer-ubeCh 1248.0x93.5 bg #262322; a::after.framer-CVbmc.framer-ubeCh 1247.98pxx93.5px border B:1px dashed #44403f; div.framer-9a57hs 40.0x40.0 bg #44403f r 12px; div.framer-Vgwwe.framer-1sjuhqf 24.0x24.0 bg #f4f3f2; div.framer-myy7E.framer-axcmfe 24.0x24.0 bg #f4f3f2 | a.framer-CVbmc.framer-ubeCh 1248.0x93.5 bg #262322; a::after.framer-CVbmc.framer-ubeCh 1247.98pxx93.5px border B:1px dashed #44403f; div.framer-9a57hs 40.0x40.0 bg #44403f r 12px; div.framer-Vgwwe.framer-1sjuhqf 24.0x24.0 bg #f4f3f2 | a.framer-CVbmc.framer-ubeCh 1248.0x93.5 bg #262322 outline 1px auto #005fcc offset 1px; a::after.framer-CVbmc.framer-ubeCh 1247.98pxx93.5px border B:1px dashed #44403f; div.framer-9a57hs 40.0x40.0 bg #44403f r 12px; div.framer-Vgwwe.framer-1sjuhqf 24.0x24.0 bg #f4f3f2; div.framer-myy7E.framer-axcmfe 24.0x24.0 bg #f4f3f2 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Icon | - | 24 x 24, colour #0000ee, fill #000000 | = | = |

Crops: `logo-chip-default.png`, `logo-chip-hover.png`, `logo-chip-focus-visible.png`, `logo-chip-pressed.png`.

#### plan-card

Plan card (light). The white Lite plan card.

Page: pricing. Selector: `div.Card:has-text("Lite")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 458.66 x 628.84 |
| Padding | 72px |
| Gap | 10px |
| Border | none |
| Radius | 24px |
| Background | #fffffb |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-1u582e4: Cirka Regular 48px/48px 400, #262322 |
| Transition | none |
| Painted layers | div.framer-1q156o4 458.7x628.8 bg #fffffb r 24px; div::after.framer-1hrim8r 314.656pxx116.797px border B:1px dashed #e4e1d5; div.framer-venfcs 12.0x10.0 image url(data:…)%22></path></svg>"); div.framer-l7tzaq 12.0x10.0 image url(data:…)%22></path></svg>"); div.framer-95yikx 12.0x10.0 image url(data:…)%22></path></svg>"); div.framer-1lvoy7t 12.0x10.0 image url(data:…)%22></path></svg>") |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-dark

Plan card (dark). The dark Standard card under the "Most popular" banner.

Page: pricing. Selector: `div.Card:has-text("Standard")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 442.67 x 586.84 |
| Padding | 38px 72px 72px 72px |
| Gap | 10px |
| Border | none |
| Radius | 16px |
| Background | #262322 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.framer-text.framer-styles-preset-1u582e4: Cirka Regular 48px/48px 400, #f4f3f2 |
| Transition | none |
| Painted layers | div.framer-1vei20d 442.7x586.8 bg #262322 r 16px; div::after.framer-1x0l4n6 298.672pxx276.641px border T:1px dashed #4d4846; div.framer-1ce9gwh 12.0x10.0 image url(data:…)%22></path></svg>"); div.framer-v4cdqv 12.0x10.0 image url(data:…)%22></path></svg>"); div.framer-lykg9p 12.0x10.0 image url(data:…)%22></path></svg>"); div.framer-1ml34m8 12.0x10.0 image url(data:…)%22></path></svg>") |
| Ancestor paint | 1 up div.framer-1qo2rg7 bg #44403f |
| How | at rest |

Crops: `plan-card-dark-default.png`.

#### plan-cta

Plan CTA (accent). The orange "Get started" inside the Standard card; links to the sign-up, never followed.

Page: pricing. Selector: `a.Default / Accent`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 107.78 x 40 | 132.91 x 40 | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f94d00 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-phy7qs: Geist Variable 16px/24px 400, #f4f3f2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | a.framer-0phDM.framer-npPic 107.8x40.0 bg #f94d00 r 8px; div.framer-144aqy4 123.8x123.8 bg #fc652d r 999px; div.framer-e7hcqw 123.8x123.8 bg #dd3b00 r 999px | a.framer-0phDM.framer-npPic 132.9x40.0 bg #f94d00 r 8px; div.framer-144aqy4 148.9x148.9 bg #fc652d r 999px; div.framer-e7hcqw 148.9x148.9 bg #dd3b00 r 999px | a.framer-0phDM.framer-npPic 107.8x40.0 bg #f94d00 r 8px outline 1px auto #005fcc offset 1px; div.framer-144aqy4 123.8x123.8 bg #fc652d r 999px; div.framer-e7hcqw 123.8x123.8 bg #dd3b00 r 999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Icon | - | 8 x 8, colour #0000ee, fill #000000 | = | = |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-cta-dark

Plan CTA (dark). A dark "Get started"/"Get a quote" plan action; never followed.

Page: pricing. Selector: `a.Default / Dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 107.78 x 40 | 110.14 x 40 | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #44403f | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-phy7qs: Geist Variable 16px/24px 400, #f4f3f2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | a.framer-0phDM.framer-npPic 107.8x40.0 bg #44403f r 8px; div.framer-144aqy4 123.8x123.8 bg #524c4a r 999px; div.framer-e7hcqw 123.8x123.8 bg #4d4846 r 999px | a.framer-0phDM.framer-npPic 110.1x40.0 bg #44403f r 8px; div.framer-144aqy4 126.1x126.1 bg #524c4a r 999px; div.framer-e7hcqw 126.1x126.1 bg #4d4846 r 999px | a.framer-0phDM.framer-npPic 107.8x40.0 bg #44403f r 8px outline 1px auto #005fcc offset 1px; div.framer-144aqy4 123.8x123.8 bg #524c4a r 999px; div.framer-e7hcqw 123.8x123.8 bg #4d4846 r 999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-dark-default.png`, `plan-cta-dark-hover.png`, `plan-cta-dark-focus-visible.png`, `plan-cta-dark-pressed.png`.

#### popular-tag

Popular tag. The "Most popular" label above the Standard card.

Page: pricing. Selector: `leaf text "Most popular"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 442.67 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text: Geist 16px/16px 500, #f4f3f2 |
| Transition | none |
| Ancestor paint | 1 up div.framer-1qo2rg7 bg #44403f |
| How | at rest |

Crops: `popular-tag-default.png`.

#### check-item

Feature row. An Includes list row with its orange check glyph.

Page: pricing. Selector: `leaf "All API services"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 294.66 x 22.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Variable 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #262322 |
| Transition | none |
| How | at rest |

Crops: `check-item-default.png`.

#### range-slider

Range slider. The price calculator's usage slider (0-3 steps); focused only, never dragged.

Page: pricing. Selector: `input[type=range]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 313.33 x 12 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | transparent | = |
| Background image | linear-gradient(to right, #f94d00 0%, #f94d00 0%, #44403f 0%, #44403f 100%) | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 0px |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #101010 | = |
| Transition | none | = |
| Cursor | default | = |
| Placeholder | #101010, opacity 1 | = |
| Painted layers | input 313.3x12.0 image linear-gradient(to right, #f94d00 0%, #f94d00 0%, #44403f 0%, #44403f 100%) r 24px | input 313.3x12.0 image linear-gradient(to right, #f94d00 0%, #f94d00 0%, #44403f 0%, #44403f 100%) r 24px outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field |

Crops: `range-slider-default.png`, `range-slider-focused.png`.

### Contact sales form

#### contact-h1

Contact title. "Grow your business with routing." in 64px Cirka.

Page: sales. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 622 x 128 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Cirka Regular 64px/64px 400 |
| Letter spacing | -0.5px |
| Colour | #262322 |
| Transition | none |
| How | at rest |

Crops: `contact-h1-default.png`.

#### form-input

Text field. The First-name text field; filled with sample text then deleted, never submitted.

Page: sales. Selector: `input[name=firstname]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 283 x 16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geist Regular 14px/16.8px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #071c1f | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #59524f, opacity 1 | = | = |
| Ancestor paint | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #efede5 | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #fffffb | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #fffffb |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `form-input-default.png`, `form-input-focused.png`, `form-input-filled.png`.

#### form-email

E-mail field. The required E-mail field.

Page: sales. Selector: `form input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 283 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist Regular 14px/16.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #071c1f | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #59524f, opacity 1 | = |
| Ancestor paint | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #efede5 | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #fffffb |
| How | at rest | clicked into the field |

Crops: `form-email-default.png`, `form-email-focused.png`.

#### form-tel

Phone field. The optional Phone-number field.

Page: sales. Selector: `form input[type=tel]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 283 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist Regular 14px/16.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #071c1f | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #59524f, opacity 1 | = |
| Ancestor paint | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #efede5 | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #fffffb |
| How | at rest | clicked into the field |

Crops: `form-tel-default.png`, `form-tel-focused.png`.

#### form-select

Select. The Job-function native select; focused only, its dropdown never opened.

Page: sales. Selector: `form select`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 295 x 40 | = |
| Padding | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist Regular 14px/16.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #262322 | = |
| Text node | undefined: Geist Regular 14px/16.8px 400, #000000 | = |
| Transition | none | = |
| Cursor | default | = |
| Ancestor paint | 1 up div.framer-form-input-wrapper.framer-form-select-wrapper bg #efede5 | 1 up div.framer-form-input-wrapper.framer-form-select-wrapper bg #fffffb |
| How | at rest | clicked into the field |

Crops: `form-select-default.png`, `form-select-focused.png`.

#### form-textarea

Textarea. The Message textarea.

Page: sales. Selector: `form textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 622 x 112 | = |
| Padding | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist Regular 14px/16.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #071c1f | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #59524f, opacity 1 | = |
| Ancestor paint | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #efede5 | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #fffffb |
| How | at rest | clicked into the field |

Crops: `form-textarea-default.png`, `form-textarea-focused.png`.

#### form-submit

Submit button. The dark "Submit" button; measured in all non-submitting states, never pressed for real.

Page: sales. Selector: `form [type=submit]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 622 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #262322 | #59524f | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.framer-text.framer-styles-preset-mawagq: Geist Medium 16px/24px 400, #efede5 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.framer-siKYy.framer-Kue87 622.0x40.0 bg #262322 r 10px | button.framer-siKYy.framer-Kue87 622.0x40.0 bg #59524f r 10px | button.framer-siKYy.framer-Kue87 622.0x40.0 bg #262322 r 10px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `form-submit-default.png`, `form-submit-hover.png`, `form-submit-focus-visible.png`, `form-submit-pressed.png`.

#### demo-card

Book-a-demo card. The white "Book a demo · 30 minutes" card beside the form; never followed.

Page: sales. Selector: `a:has-text("Book a demo 30 minutes")`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 205.3 x 65.09 | = |
| Padding | 8px 12px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | #fffffb | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #0000ee | = |
| Text node | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #262322 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.framer-nnmcH.framer-i5yBN 205.3x65.1 bg #fffffb r 12px; div.framer-18p49kd 32.0x32.0 r 6px shadow #fffffb 0px 0px 0px 1.5px; div.framer-150syir 10.0x10.0 image url(data:…)%22></path></svg>") | a.framer-nnmcH.framer-i5yBN 205.3x65.1 bg #fffffb r 12px; div.framer-18p49kd 32.0x32.0 r 6px shadow #fffffb 0px 0px 0px 1.5px; div.framer-150syir 14.1x14.1 image url(data:…)%22></path></svg>") |
| How | at rest | mouse hover |

Crops: `demo-card-default.png`, `demo-card-hover.png`.

### Sign-in page (boundary)

#### signin-h1

Sign-in title. "Sign in to your account." in 48px Cirka.

Page: signin. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Cirka 48px/48px 400 |
| Letter spacing | -0.5px |
| Colour | oklch(0.2591 0.0049 39.4) |
| Transition | none |
| Ancestor paint | 3 up div.card.rounded-4xl bg oklch(0.997 0.0041 91.45) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.9046 0.0199 87.52 / 0.32) 0px 0px 0px 1px, oklch(0 0 0 / 0.16) 0px 0px 1px 0px |
| How | at rest |

Crops: `signin-h1-default.png`.

#### signin-input

E-mail field. The E-mail-address field on the sign-in card; filled with sample text then deleted, Continue never pressed.

Page: signin. Selector: `sign-in input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 358 x 46 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Geist 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | oklch(0.2591 0.0049 39.4) | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s ease-out | = | = |
| Placeholder | oklch(0.6015 0.0143 63.78), opacity 1 | = | = |
| Painted layers | input.h-full.flex-1 358.0x46.0 outline 2px solid #000000 @ 0 offset 2px | = | = |
| Ancestor paint | 1 up div.input-form-control.will-change-color bg oklch(0.9492 0.0111 89.72) outline 0px solid oklch(0.4444 0.0105 44.76) | 1 up div.input-form-control.will-change-color bg #f1eee6 outline 0px solid oklch(0.4444 0.0105 44.76) | 1 up div.input-form-control.will-change-color bg oklch(0.997 0.0041 91.45) outline 0px solid oklch(0.4444 0.0105 44.76) |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-input-default.png`, `signin-input-focused.png`.

#### signin-continue

Continue button. The dark Continue button; measured in all non-submitting states, never pressed for real.

Page: signin. Selector: `button:has-text("Continue")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 40 | = | = | 372.48 x 38.8 |
| Padding | 0px 12px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 12px | = | = | = |
| Background | oklch(0.2591 0.0049 39.4) | oklch(0.3751 0.0058 34.3) | = | #262322 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid oklch(0.5152 0.0118 58.04) offset 1px | = |
| Font | Geist 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.995 0.0034 67.78) | = | = | = |
| Text node | span.font-medium: Geist 14px/20px 500, oklch(0.995 0.0034 67.78) | = | = | = |
| Transition | color, background-color, border-color, scale 0.15s cubic-bezier(0.2, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ct-link.base-button 384.0x40.0 bg oklch(0.2591 0.0049 39.4) border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px | button.ct-link.base-button 384.0x40.0 bg oklch(0.3751 0.0058 34.3) border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px | button.ct-link.base-button 384.0x40.0 bg oklch(0.2591 0.0049 39.4) border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px outline 1px solid oklch(0.5152 0.0118 58.04) offset 1px | button.ct-link.base-button 372.5x38.8 bg #262322 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px |
| Ancestor paint | 3 up div.card.rounded-4xl bg oklch(0.997 0.0041 91.45) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.9046 0.0199 87.52 / 0.32) 0px 0px 0px 1px, oklch(0 0 0 / 0.16) 0px 0px 1px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `signin-continue-default.png`, `signin-continue-hover.png`, `signin-continue-focus-visible.png`, `signin-continue-pressed.png`.

#### signin-create

Create-account button. The secondary Create-account action; never followed.

Page: signin. Selector: `:has-text("Create account")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 40 | = | = | 372.48 x 38.8 |
| Padding | 0px 12px | = | = | = |
| Gap | normal 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 12px | = | = | = |
| Background | oklch(0.9492 0.0111 89.72) | #f1eee6 | = | #f1eee6 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid oklch(0.5152 0.0118 58.04) offset 1px | = |
| Font | Geist 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.2591 0.0049 39.4) | = | = | = |
| Text node | span.font-medium: Geist 14px/20px 500, oklch(0.2591 0.0049 39.4) | = | = | = |
| Transition | color, background-color, border-color, scale 0.15s cubic-bezier(0.2, 0, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ct-link.base-button 384.0x40.0 bg oklch(0.9492 0.0111 89.72) border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px | a.ct-link.base-button 384.0x40.0 bg #f1eee6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px | a.ct-link.base-button 384.0x40.0 bg oklch(0.9492 0.0111 89.72) border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px outline 1px solid oklch(0.5152 0.0118 58.04) offset 1px | a.ct-link.base-button 372.5x38.8 bg #f1eee6 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 12px |
| Ancestor paint | 3 up div.card.rounded-4xl bg oklch(0.997 0.0041 91.45) shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.9046 0.0199 87.52 / 0.32) 0px 0px 0px 1px, oklch(0 0 0 / 0.16) 0px 0px 1px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `signin-create-default.png`, `signin-create-hover.png`, `signin-create-focus-visible.png`, `signin-create-pressed.png`.

#### signin-trust

Trust row. A check-marked reassurance row under the hero panel.

Page: signin. Selector: `leaf "No credit card needed"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 244 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 14px/20px 500 |
| Letter spacing | normal |
| Colour | oklch(0.2591 0.0049 39.4) |
| Transition | none |
| How | at rest |

Crops: `signin-trust-default.png`.

### Footer

#### footer

Footer. The footer band: link columns, the "chargetrip presents" newsletter block, badges, the legal subfooter.

Page: home. Selector: `ancestor of "chargetrip presents"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1391.98 x 481.17 |
| Padding | 24px 0px 0px 0px |
| Gap | 48px 2px |
| Border | none |
| Radius | 24px 24px 0px 0px |
| Background | #fffffb |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-phy7qs: Geist Variable 16px/24px 400, #877f78 |
| Transition | none |
| Icon | 94 x 20.02, colour #000000 |
| Painted layers | div.framer-PkeUF.framer-npPic 1392.0x481.2 bg #fffffb r 24px 24px 0px 0px; div 8.0x8.0 bg #278859 r 100%; a.framer-1vyggok.framer-1oqc6h7 98.0x32.0 bg #efede5 r 16px; div::after.framer-cuy8cf 462.672pxx316.031px border L:1px solid #c7c0aa @ 0.2; a.framer-0phDM.framer-npPic 106.0x40.0 bg #44403f r 8px; div.framer-144aqy4 122.0x122.0 bg #524c4a r 999px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a:has-text("No-code")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Geist Variable 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262322 | #f94d00 | = | #f94d00 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-zjjg3u 65.0x21.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Geist Variable 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262322 | #f94d00 | = | #f94d00 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-zjjg3u 61.0x21.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### newsletter-cta

Newsletter CTA. The footer newsletter "Sign up" button; never followed.

Page: home. Selector: `footer a:has-text("Sign up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Geist Variable 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262322 | #f94d00 | = | #f94d00 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-zjjg3u 56.0x21.0 outline 1px auto #101010 offset 1px | = |

Crops: `newsletter-cta-default.png`, `newsletter-cta-hover.png`, `newsletter-cta-focus-visible.png`, `newsletter-cta-pressed.png`.

#### status-pill

Status pill. The "● Stable" status link in the footer (green dot; links to status.chargetrip.com, never followed).

Page: home. Selector: `footer "Stable" link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 208.33 x 171.22 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-phy7qs: Geist Variable 16px/24px 400, #877f78 |
| Transition | none |
| Painted layers | div 8.0x8.0 bg #278859 r 100% |
| How | at rest |

Crops: `status-pill-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `the mobile top bar at y=0`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px 8px |
| Gap | 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-ooof01: Geist Variable 18px/28.8px 400, #262322 |
| Transition | none |
| Icon | 106 x 24, colour #000000 |
| Painted layers | div.framer-1eg8t2t 374.0x64.0 bg #fcfcfb @ 0 r 12px; div::after.framer-1eg8t2t 374pxx64px border B:1px solid #efede5 r 12px; a::after.framer-SWyCz.framer-i5yBN 83pxx40px border T:1px solid #262322 / R:1px solid #262322 / B:1px solid #262322 / L:1px solid #262322 r 8px; div.framer-fp75hx 40.0x40.0 bg #071c1f r 8px; div.framer-dy9a3h 16.0x16.0 image url(data:…)%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 stroke-dasharray=%22; div.framer-12qdk4p 12.0x10.0 image url(data:…)%22></path></svg>") |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The dark-teal hamburger at the bar's right edge; its own press opens the menu overlay.

Page: home. Selector: `div[data-framer-name="Button Icon"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 12px |
| Gap | 8px |
| Border | none |
| Radius | 8px |
| Background | #071c1f |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.framer-fp75hx 40.0x40.0 bg #071c1f r 8px; div.framer-dy9a3h 16.0x16.0 image url(data:…)%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22 stroke-dasharray=%22; div.framer-12qdk4p 12.0x10.0 image url(data:…)%22></path></svg>") |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The full-screen menu overlay after the trigger's own toggle: orange No-code card, dark API card, Integration Partners, the Use-cases list.

Page: home. Selector: `fixed menu overlay ancestor of the in-menu a[href="./no-code"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 828 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-ldb0w0: Geist Regular 16px/24px 400, #fffffb |
| Transition | none |
| Icon | 106 x 24, colour #000000 |
| Painted layers | div.framer-1yyuo68 390.0x828.0 bg #000000 @ 0.2; div.framer-e2feec 373.9x828.0 bg #fffffb r 3.20856% / 1.44928% shadow #000000 @ 0.12 0px 0px 40px 0px; div.framer-10hg0ls 479.0x40.0 bg #262322 r 0px 0px 12px 12px; div.framer-1eg8t2t 374.0x64.0 bg #fffffb r 12px 12px 0px 0px; div::after.framer-1eg8t2t 374pxx64px border B:1px solid #efede5 r 12px 12px 0px 0px; a::after.framer-SWyCz.framer-i5yBN 83pxx40px border T:1px solid #262322 / R:1px solid #262322 / B:1px solid #262322 / L:1px solid #262322 r 8px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-card

Mobile menu card. The orange No-code card in the open mobile menu.

Page: home. Selector: `card ancestor of a[href="./no-code"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 86 |
| Padding | 16px |
| Gap | 0px |
| Border | none |
| Radius | 8px |
| Background | #f94d00 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | h4.framer-text.framer-styles-preset-1o67j2j: PP Cirka Medium 28px/30px 400, #efede5 |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.framer-39qt1e.framer-152olpk 350.0x86.0 bg #f94d00 r 8px |
| How | at rest |

Crops: `m-menu-card-default.png`.

#### m-hero

Mobile headline.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 208 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Cirka Regular 56px/52px 400 |
| Letter spacing | -0.2px |
| Colour | #f4f3f2 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `opacity 0.4s ease-out`, `unset`, `width 200ms, height 200ms, max-height 200ms, transform 300ms cubic-bezier(0, 1.2, 1, 1), opacity 83ms ease-out`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`, `transform 250ms cubic-bezier(0.33, 0, 0, 1)`, `transform 134ms cubic-bezier(0.45, 0, 0.2, 1)`, `none`, `opacity 400ms, width 400ms, transform 300ms`
