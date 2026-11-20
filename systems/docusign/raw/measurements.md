# Component measurements

Computed styles read from docusign.com (the marketing site, the signature generator, the ecom storefront and the account.docusign.com sign-in card) on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### utilitynav

Utility bar. The top strip over the main nav: the announcement link, sales phone, Search, Support, Access Documents and Log In.

Page: home. Selector: `nav[data-cy=utilitynav]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | div.css-4ebx1o: DSIndigo 12px/18px 500, #ffffff, ls 0.2px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.css-1qdnkw1.e1p96sfz1 1440.0x30.0 bg #26065d; a::before.css-8vbptu.e1tasy2f0 23.5pxx14px bg #cbc2ff border T:1px solid #cbc2ff r 4px; div::after.css-g4mfjf.e1tasy2f1 0pxx1px bg #ffffff; div::after.css-g4mfjf.e1tasy2f1 0pxx1px bg #ffffff; div::after.css-g4mfjf.e1tasy2f1 0pxx1px bg #ffffff; div::after.css-g4mfjf.e1tasy2f1 0pxx1px bg #ffffff |
| Ancestor paint | 1 up div.css-z3jndn.er28sow2 bg #ffffff |
| How | at rest |

Crops: `utilitynav-default.png`.

#### header

Header. The primary nav inside the sticky chrome: wordmark, the Products/Solutions/Resources dropdown triggers, Enterprise and Plans & Pricing links, and the Contact-sales/Buy-now/Try-for-free actions.

Page: home. Selector: `nav[data-cy=navbar]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 69 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | button.css-qscr5r: DSIndigo 14px/21px 500, #130032 @ 0.75, ls 0.2px |
| Transition | none |
| Icon | 0 x 0, colour #130032 |
| Painted layers | nav.css-b9x1zj 1440.0x69.0 bg #ffffff; div.css-19njzqs.e1p96sfz1 1440.0x69.0 bg #ffffff; div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #4c00ff; section.css-1crqsg9.e1p96sfz1 1440.0x459.0 bg #ffffff r 0px 0px 16px 16px shadow #130032 @ 0.2 0px 32px 64px 0px; span.css-11bm945 885.3x40.0 border B:1px solid #cbc2ff; div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032 |
| Ancestor paint | 1 up div.css-z3jndn.er28sow2 bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Docusign wordmark anchor (aria-label "Docusign").

Page: home. Selector: `navbar a[aria-label=Docusign]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132 x 26.55 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 132 x 26.55, colour #0000ee, fill #000000 | = | = | 132 x 26.55, colour #ff0000, fill #000000 |
| Painted layers | div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #4c00ff | = | a.css-dmyhku.e1tasy2f0 132.0x26.5 r 4px outline 2px solid #4c00ff offset 2px; div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #4c00ff | div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #130032 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `logo-default.png`, `logo-hover.png`, `logo-focus-visible.png`, `logo-pressed.png`.

#### nav-trigger

Nav trigger. The Products button that opens the full-width mega-menu; toggled, never followed.

Page: home. Selector: `navbar button "Products"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75.73 x 69 | = | = | = |
| Padding | 24px 0px | = | = | = |
| Gap | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 14px/21px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #130032 @ 0.75 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #130032 @ 0.75 | = | = | = |
| ::after | 75.7344px x 2px, absolute, bg #000000 @ 0, radius 0px | 75.7344px x 2px, absolute, bg #4c00ff, radius 0px | 75.7344px x 2px, absolute, bg #4c00ff, radius 0px | 75.7344px x 2px, absolute, bg #4c00ff, radius 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button::after.css-qscr5r 75.7344pxx2px bg #4c00ff | button.css-qscr5r 75.7x69.0 r 4px outline 2px solid #4c00ff offset 2px; button::after.css-qscr5r 75.7344pxx2px bg #4c00ff | button::after.css-qscr5r 75.7344pxx2px bg #4c00ff |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The plain Plans-&-Pricing header link.

Page: home. Selector: `navbar a "Plans & Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.61 x 69 | = | = | = |
| Padding | 24px 0px | = | = | = |
| Gap | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 14px/21px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #130032 @ 0.75 | = | = | = |
| Text node | div.css-1eg020q.e1tasy2f1: DSIndigo 14px/21px 500, #130032 @ 0.75, ls 0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 95.6094px x 2px, absolute, bg #000000 @ 0, radius 0px | 95.6094px x 2px, absolute, bg #4c00ff, radius 0px | 95.6094px x 2px, absolute, bg #4c00ff, radius 0px | 95.6094px x 2px, absolute, bg #4c00ff, radius 0px |
| Painted layers | div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75 | a::after.css-17gi7l6.e1tasy2f0 95.6094pxx2px bg #4c00ff; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75 | a.css-17gi7l6.e1tasy2f0 95.6x69.0 r 4px outline 2px solid #4c00ff offset 2px; a::after.css-17gi7l6.e1tasy2f0 95.6094pxx2px bg #4c00ff; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75 | a::after.css-17gi7l6.e1tasy2f0 95.6094pxx2px bg #4c00ff; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-contact

Contact-sales link. The uppercase Contact-sales text action; measured never followed.

Page: home. Selector: `navbar a "CONTACT SALES"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145.83 x 45 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 1px inset | #130032 @ 0.15 0px 0px 0px 1px inset | #130032 @ 0.15 0px 0px 0px 1px inset | #130032 @ 0.15 0px 0px 0px 1px inset |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 14px/21px 600 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #4c00ff | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-5lds31.evij40y0 145.8x45.0 r 8px shadow #000000 @ 0 0px 0px 0px 1px inset | a.css-5lds31.evij40y0 145.8x45.0 r 8px shadow #130032 @ 0.15 0px 0px 0px 1px inset | a.css-5lds31.evij40y0 145.8x45.0 r 8px shadow #130032 @ 0.15 0px 0px 0px 1px inset outline 2px solid #4c00ff offset 2px | a.css-5lds31.evij40y0 145.8x45.0 r 8px shadow #130032 @ 0.15 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-contact-default.png`, `nav-contact-hover.png`, `nav-contact-focus-visible.png`, `nav-contact-pressed.png`.

#### nav-buy

Buy-now link. The uppercase Buy-now text action; measured never followed.

Page: home. Selector: `navbar a "BUY NOW"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.14 x 45 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 1px inset | #130032 @ 0.15 0px 0px 0px 1px inset | #130032 @ 0.15 0px 0px 0px 1px inset | #130032 @ 0.15 0px 0px 0px 1px inset |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 14px/21px 600 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #4c00ff | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-5lds31.evij40y0 97.1x45.0 r 8px shadow #000000 @ 0 0px 0px 0px 1px inset | a.css-5lds31.evij40y0 97.1x45.0 r 8px shadow #130032 @ 0.15 0px 0px 0px 1px inset | a.css-5lds31.evij40y0 97.1x45.0 r 8px shadow #130032 @ 0.15 0px 0px 0px 1px inset outline 2px solid #4c00ff offset 2px | a.css-5lds31.evij40y0 97.1x45.0 r 8px shadow #130032 @ 0.15 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-buy-default.png`, `nav-buy-hover.png`, `nav-buy-focus-visible.png`, `nav-buy-pressed.png`.

#### nav-cta

Try-for-free CTA. The filled purple Try-for-free pill; measured never followed.

Page: home. Selector: `navbar "TRY FOR FREE"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128.09 x 45 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #4c00ff | #4000cc | = | #4000cc |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 14px/21px 600 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-2llxql.evij40y0 128.1x45.0 bg #4c00ff r 8px | a.css-2llxql.evij40y0 128.1x45.0 bg #4000cc r 8px | a.css-2llxql.evij40y0 128.1x45.0 bg #4c00ff r 8px outline 2px solid #4c00ff offset 2px | a.css-2llxql.evij40y0 128.1x45.0 bg #4000cc r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-search

Search button. The Search button in the utility bar.

Page: home. Selector: `utilitybar Search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.33 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #cbc2ff offset 2px | = |
| Font | DSIndigo 12px/18px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | #cbc2ff | #cbc2ff | #cbc2ff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.css-1jjw43b 39.3x18.0 r 4px outline 2px solid #cbc2ff offset 2px | = |

Crops: `nav-search-default.png`, `nav-search-hover.png`, `nav-search-focus-visible.png`, `nav-search-pressed.png`.

#### login-link

Log-in link. The utility-bar Log In link; measured never followed.

Page: home. Selector: `utilitynav a "Log In"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 33.83 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #cbc2ff offset 2px | = |
| Font | DSIndigo 12px/18px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | #cbc2ff | #cbc2ff | #cbc2ff |
| Text node | div.css-g4mfjf.e1tasy2f1: DSIndigo 12px/18px 500, #ffffff, ls 0.2px | div.css-g4mfjf.e1tasy2f1: DSIndigo 12px/18px 500, #cbc2ff, ls 0.2px | div.css-g4mfjf.e1tasy2f1: DSIndigo 12px/18px 500, #cbc2ff, ls 0.2px | div.css-g4mfjf.e1tasy2f1: DSIndigo 12px/18px 500, #cbc2ff, ls 0.2px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div::after.css-g4mfjf.e1tasy2f1 0pxx1px bg #ffffff | = | a.css-121l1fb.e1tasy2f0 33.8x18.0 r 4px outline 2px solid #cbc2ff offset 2px; div::after.css-g4mfjf.e1tasy2f1 0pxx1px bg #ffffff | div::after.css-g4mfjf.e1tasy2f1 0pxx1px bg #ffffff @ 0.8 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### nav-dropdown

Nav dropdown. The Products mega-menu panel, opened by its own trigger (a full-width white sheet).

Page: home. Selector: `mega-menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1360 x 379 |
| Padding | 0px |
| Gap | 64px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/24px 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | span.css-11bm945: DSIndigo 18px/27px 500, #130032 |
| Transition | none |
| Icon | 16 x 16, colour #4c00ff |
| Painted layers | span.css-11bm945 885.3x40.0 border B:1px solid #cbc2ff; div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032; div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032; div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032; div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032; div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032 |
| Ancestor paint | 2 up section.css-1crqsg9.e1p96sfz1 bg #ffffff shadow #130032 @ 0.2 0px 32px 64px 0px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A product link inside the opened mega-menu (bold label over a grey description).

Page: home. Selector: `mega-menu product link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 410.67 x 47 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 | = | = | = |
| Text node | span.css-llpyjt: DSIndigo 16px/24px 500, #130032 | span.css-llpyjt: DSIndigo 16px/24px 500, #4c00ff | span.css-llpyjt: DSIndigo 16px/24px 500, #4c00ff | span.css-llpyjt: DSIndigo 16px/24px 500, #4c00ff |
| Transition | color 0.15s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032 | div::after.css-aknfkn.e1tasy2f1 100%x1px bg #130032 | a.css-1itjty0.e1tasy2f0 410.7x47.0 r 4px outline 2px solid #4c00ff offset 2px; div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032 | div::after.css-aknfkn.e1tasy2f1 100%x1px bg #130032 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home hero

#### hero-section

Hero section. The painted #26065d deep-purple hero band.

Page: home. Selector: `first painted ancestor of h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 570.39 |
| Padding | 96px 80px 80px 80px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | radial-gradient(100% 100% at 50% 0%, #4c00ff 0%, #26065d 100%) |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.eeb3xhj27.css-1izp4uh: DSIndigo 80px/86.4px 300, #ffffff, ls -1.5px |
| Transition | none |
| Icon | 14.4 x 14.4, colour #ffffff |
| Painted layers | section.css-ejzn5p.e1p96sfz1 1440.0x570.4 image radial-gradient(100% 100% at 50% 0%, #4c00ff 0%, #26065d 100%); span.styledCheckbox.css-ci2u9i 20.0x20.0 border T:2px solid #ffffff @ 0.35 / R:2px solid #ffffff @ 0.35 / B:2px solid #ffffff @ 0.35 / L:2px solid #ffffff @ 0.35 r 2px; input.fs-mask.css-1czprqx 472.5x61.0 bg #ffffff border T:1px solid #130032 @ 0.15 / R:1px solid #130032 @ 0.15 / B:1px solid #130032 @ 0.15 / L:1px solid #130032 @ 0.15 r 8px 0px 0px 8px; button.elk0b8n5.css-1db2ago 119.5x61.0 bg #130032 r 0px 8px 8px 0px; select.fs-mask.css-p8qupu 189.5x22.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 |
| How | at rest |

Crops: `hero-section-default.png`.

#### hero-title

Hero headline. The 80px DSIndigo-300 white headline on the purple band.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 990.56 x 86.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 80px/86.4px 300 |
| Letter spacing | -1.5px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero copy. The lede under the hero headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 412.02 x 27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 18px/27px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-cta

Hero CTA. The filled Get-Started pill in the hero; measured never followed.

Page: home. Selector: `"Get Started"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.47 x 61 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px 8px 8px 0px | = | = | = |
| Background | #130032 | = | = | #4e4067 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | default | = | = | pointer |
| Painted layers | button.elk0b8n5.css-1db2ago 119.5x61.0 bg #130032 r 0px 8px 8px 0px | = | button.elk0b8n5.css-1db2ago 119.5x61.0 bg #130032 r 0px 8px 8px 0px outline 2px solid #ffffff offset 2px | button.elk0b8n5.css-1db2ago 119.5x61.0 bg #4e4067 r 0px 8px 8px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-link

Hero link. The Explore-Docusign-IAM arrow link under the hero CTA; measured never followed.

Page: home. Selector: `"Explore Docusign IAM"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171.95 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4c00ff | = | = | #130032 |
| Text node | span.css-n219vx.e201y4g1: DSIndigo 16px/24px 500, #4c00ff | = | = | span.css-n219vx.e201y4g1: DSIndigo 16px/24px 500, #130032 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #4c00ff | = | = | 16 x 16, colour #130032 |
| Painted layers | span::after.css-n219vx.e201y4g1 0pxx1px bg #4c00ff | = | a.css-1bhha0e.e201y4g0 172.0x24.0 r 4px outline 2px solid #4c00ff offset 2px; span::after.css-n219vx.e201y4g1 0pxx1px bg #4c00ff | span::after.css-n219vx.e201y4g1 0pxx1px bg #130032 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-link-default.png`, `hero-link-hover.png`, `hero-link-focus-visible.png`, `hero-link-pressed.png`.

#### hero-field

Hero email field. The hero work-email input on the purple band; sample text was typed and deleted, nothing sent.

Page: home. Selector: `input[name=workEmail]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 472.53 x 61 | = | = |
| Padding | 24px 16px 8px 16px | = | = |
| Border | 1px solid #130032 @ 0.15 | 1px solid #4c00ff | 1px solid #4c00ff |
| Radius | 8px 0px 0px 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #4c00ff 0px 0px 0px 1px inset | #4c00ff 0px 0px 0px 1px inset |
| Outline | none | = | = |
| Font | DSIndigo 18px/27px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #130032 | = | = |
| Transition | border-color 0.2s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #130032, opacity 1 | = | = |
| Painted layers | input.fs-mask.css-1czprqx 472.5x61.0 bg #ffffff border T:1px solid #130032 @ 0.15 / R:1px solid #130032 @ 0.15 / B:1px solid #130032 @ 0.15 / L:1px solid #130032 @ 0.15 r 8px 0px 0px 8px | input.fs-mask.css-1czprqx 472.5x61.0 bg #ffffff border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px 0px 0px 8px shadow #4c00ff 0px 0px 0px 1px inset | input.fs-mask.css-1czprqx 472.5x61.0 bg #ffffff border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px 0px 0px 8px shadow #4c00ff 0px 0px 0px 1px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `hero-field-default.png`, `hero-field-focused.png`, `hero-field-filled.png`.

#### hero-checkbox

Hero consent checkbox. The painted square of the marketing-opt-in checkbox on the purple band (the real input is a 1x1 inside it); measured, never toggled on this surface.

Page: home. Selector: `hero checkbox painted square`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 592 x 37 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | DSIndigo 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | p: DSIndigo 12px/18px 400, #ffffff, ls 0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.styledCheckbox.css-ci2u9i 20.0x20.0 border T:2px solid #ffffff @ 0.35 / R:2px solid #ffffff @ 0.35 / B:2px solid #ffffff @ 0.35 / L:2px solid #ffffff @ 0.35 r 2px | span.styledCheckbox.css-ci2u9i 20.0x20.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 2px; span::before.styledCheckbox.css-ci2u9i 32pxx32px bg #130032 @ 0.15 r 4px | input.css-5w2lwp 1.0x1.0 outline 1px auto #005fcc offset 2px; span.styledCheckbox.css-ci2u9i 20.0x20.0 border T:2px solid #ffffff @ 0.35 / R:2px solid #ffffff @ 0.35 / B:2px solid #ffffff @ 0.35 / L:2px solid #ffffff @ 0.35 r 2px outline 2px solid #cbc2ff offset 4px | span.styledCheckbox.css-ci2u9i 20.0x20.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 2px; span::before.styledCheckbox.css-ci2u9i 32pxx32px bg #130032 @ 0.15 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-checkbox-default.png`, `hero-checkbox-hover.png`, `hero-checkbox-focus-visible.png`, `hero-checkbox-pressed.png`.

#### hero-country

Country picker. The Country/region labelled control under the hero form (a native select at opacity 0 inside its painted label; reads Singapore on this vantage); measured, never opened.

Page: home. Selector: `label:has(select)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 189.5 x 21 | = | = | = |
| Padding | 0px 3.2px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #cbc2ff 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | DSIndigo 14px/21px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: DSIndigo 14px/21px 400, #ffffff, ls 0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 14.4 x 14.4, colour #ffffff | = | = | = |
| Painted layers | select.fs-mask.css-p8qupu 189.5x22.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 | = | label.elk0b8n0.css-iao6pr 189.5x21.0 r 4px shadow #cbc2ff 0px 0px 0px 2px; select.fs-mask.css-p8qupu 189.5x22.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-country-default.png`, `hero-country-hover.png`, `hero-country-focus-visible.png`, `hero-country-pressed.png`.

### Home

#### h2-section

Section heading. A marketing section h2 (DSIndigo).

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1080 x 62.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(97.84deg, #4c00ff -38.62%, #ff5252 141.03%) |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 58px/62.64px 300 |
| Letter spacing | -1.25px |
| Colour | #130032 |
| Transition | none |
| Painted layers | h2.ef7x3124.css-8u7x1f 1080.0x62.6 image linear-gradient(97.84deg, #4c00ff -38.62%, #ff5252 141.03%) |
| How | at rest |

Crops: `h2-section-default.png`.

#### blog-card

Card link. A marketing card link (blog-teaser or resource card); measured never followed.

Page: home. Selector: `card link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #130032 @ 0.75 | = | = | = |
| Text node | span.css-llpyjt: DSIndigo 14px/21px 500, #130032, ls 0.2px | span.css-llpyjt: DSIndigo 14px/21px 500, #130032 @ 0.75, ls 0.2px | span.css-llpyjt: DSIndigo 14px/21px 500, #130032 @ 0.75, ls 0.2px | span.css-llpyjt: DSIndigo 14px/21px 500, #130032 @ 0.75, ls 0.2px |
| Transition | color 0.15s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75 | div::after.css-1eg020q.e1tasy2f1 100%x1px bg #130032 @ 0.75 | a.css-1po7wbl.e1tasy2f0 184.0x24.0 r 4px outline 2px solid #4c00ff offset 2px; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75 | div::after.css-1eg020q.e1tasy2f1 100%x1px bg #130032 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `blog-card-default.png`, `blog-card-hover.png`, `blog-card-focus-visible.png`, `blog-card-pressed.png`.

#### assistant

Assistant launcher. The floating Docusign-Assistant chat pill; measured, never opened.

Page: home. Selector: `"Docusign Assistant"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 227.59 x 54 | = | - | - |
| Padding | 16px 24px | = | - | - |
| Gap | 8px | = | - | - |
| Border | 1px solid #4014ea | = | - | - |
| Radius | 9999px | = | - | - |
| Background | #4014ea | #ffffff | - | - |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = | - | - |
| Outline | none | = | - | - |
| Font | -apple-system 16px/normal 700 | = | - | - |
| Letter spacing | normal | = | - | - |
| Colour | #ffffff | #4014ea | - | - |
| Text node | span.relative.shrink-0: -apple-system 16px/normal 700, #ffffff | span.relative.shrink-0: -apple-system 16px/normal 700, #4014ea | - | - |
| Transition | all 0.1s ease | = | - | - |
| Cursor | pointer | = | - | - |
| Icon | 20 x 20, colour #ffffff | 20 x 20, colour #4014ea | - | - |
| Painted layers | button.z-overlay.fixed 227.6x54.0 bg #4014ea border T:1px solid #4014ea / R:1px solid #4014ea / B:1px solid #4014ea / L:1px solid #4014ea r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | button.z-overlay.fixed 227.6x54.0 bg #ffffff border T:1px solid #4014ea / R:1px solid #4014ea / B:1px solid #4014ea / L:1px solid #4014ea r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | - | - |
| How | at rest | mouse hover | - | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Error | - | = | = | cdpSession.send: Protocol error (CSS.forcePseudoState): Could not find node with given id |

Crops: `assistant-default.png`, `assistant-hover.png`.

### eSignature page

#### e-title

eSignature title. The product page display heading.

Page: esignature. Selector: `h1 on /products/electronic-signature`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 948 x 103.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 48px/51.84px 300 |
| Letter spacing | -1px |
| Colour | #130032 |
| Transition | none |
| How | at rest |

Crops: `e-title-default.png`.

#### e-cta

eSignature CTA. A plan/trial call to action; measured never followed.

Page: esignature. Selector: `page CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128.09 x 45 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #4c00ff | #4000cc | = | #4000cc |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 14px/21px 600 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-2llxql.evij40y0 128.1x45.0 bg #4c00ff r 8px | a.css-2llxql.evij40y0 128.1x45.0 bg #4000cc r 8px | a.css-2llxql.evij40y0 128.1x45.0 bg #4c00ff r 8px outline 2px solid #4c00ff offset 2px | a.css-2llxql.evij40y0 128.1x45.0 bg #4000cc r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `e-cta-default.png`, `e-cta-hover.png`, `e-cta-focus-visible.png`, `e-cta-pressed.png`.

#### video-expand

Video expand button. An expand-video icon button on a customer-story tile; one was pressed to open the dialog below.

Page: esignature. Selector: `button[aria-label="Expand Customer Story Video"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 816 x 459 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | span.css-1p8odxa.e1nf4qrp1 40.0x40.0 bg #130032 @ 0.25 r 100% | span.css-1p8odxa.e1nf4qrp1 40.0x40.0 bg #4c00ff r 100% | button.css-8mph9b.e1nf4qrp0 816.0x459.0 outline 2px solid #4c00ff offset 2px; span.css-1p8odxa.e1nf4qrp1 40.0x40.0 bg #4c00ff r 100% | span.css-1p8odxa.e1nf4qrp1 40.0x40.0 bg #4c00ff r 100% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `video-expand-default.png`, `video-expand-hover.png`, `video-expand-focus-visible.png`, `video-expand-pressed.png`.

#### video-dialog

Video dialog. The modal a video Expand button opens (scrim + framed player); opened and closed with the product's own controls.

Page: esignature. Selector: `dialog / modal_scrim`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #130032 @ 0.898 |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Transition | none |
| Opacity | 0.9 |
| Painted layers | div.css-7gkdmf.e1xd2tg63 1440.0x900.0 bg #130032 @ 0.898 |
| How | at rest |

Crops: `video-dialog-default.png`.

#### faq-button

FAQ row. A collapsed FAQ accordion row in the page footer; toggled open once for the panel below.

Page: esignature. Selector: `FAQ accordion button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1280 x 93.75 | = | = | = |
| Padding | 32px 0px | = | = | = |
| Gap | 48px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 0px | = |
| Font | DSIndigo 24px/29.76px 500 | = | = | = |
| Letter spacing | -0.25px | = | = | = |
| Colour | #130032 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | pointer | = | pointer |
| Icon | 16 x 16, colour #130032 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.css-1yg0mla.e1mn5vlf1 1280.0x93.8 outline 2px solid #4c00ff offset 0px | = |

Crops: `faq-button-default.png`, `faq-button-hover.png`, `faq-button-focus-visible.png`, `faq-button-pressed.png`.

#### faq-open

FAQ row, open. The same accordion row after its own toggle (aria-expanded).

Page: esignature. Selector: `FAQ button open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 93.75 |
| Padding | 32px 0px |
| Gap | 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 24px/29.76px 500 |
| Letter spacing | -0.25px |
| Colour | #130032 |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #130032 |
| How | at rest |

Crops: `faq-open-default.png`.

#### faq-panel

FAQ panel. The answer text revealed under an open FAQ row.

Page: esignature. Selector: `FAQ answer region`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 165.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | button.css-1yg0mla.e1mn5vlf1: DSIndigo 24px/29.76px 500, #130032, ls -0.25px |
| Transition | none |
| Icon | 16 x 16, colour #130032 |
| How | at rest |

Crops: `faq-panel-default.png`.

### Free trial

#### trial-card

Trial form band. The painted free-trial form band; never submitted.

Page: trial. Selector: `trial form section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1408 x 303 |
| Padding | 0px 0px 24px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | h1.css-1oe0uc1.e1et20720: DSIndigo 40px/48px 400, #130032, ls -0.5px |
| Transition | none |
| Painted layers | input.fs-mask.css-1czprqx 488.0x61.0 bg #ffffff border T:1px solid #130032 @ 0.15 / R:1px solid #130032 @ 0.15 / B:1px solid #130032 @ 0.15 / L:1px solid #130032 @ 0.15 r 8px; span.styledCheckbox.css-lnan8r 20.0x20.0 border T:2px solid #130032 @ 0.15 / R:2px solid #130032 @ 0.15 / B:2px solid #130032 @ 0.15 / L:2px solid #130032 @ 0.15 r 2px |
| How | at rest |

Crops: `trial-card-default.png`.

#### trial-field

Work-email field. The work-email input; sample text was typed and deleted, nothing sent.

Page: trial. Selector: `input[name=workEmail]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 488 x 61 | = | = |
| Padding | 24px 16px 8px 16px | = | = |
| Border | 1px solid #130032 @ 0.15 | 1px solid #4c00ff | 1px solid #4c00ff |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #4c00ff 0px 0px 0px 1px inset | #4c00ff 0px 0px 0px 1px inset |
| Outline | none | = | = |
| Font | DSIndigo 18px/27px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #130032 | = | = |
| Transition | border-color 0.2s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #130032, opacity 1 | = | = |
| Painted layers | input.fs-mask.css-1czprqx 488.0x61.0 bg #ffffff border T:1px solid #130032 @ 0.15 / R:1px solid #130032 @ 0.15 / B:1px solid #130032 @ 0.15 / L:1px solid #130032 @ 0.15 r 8px | input.fs-mask.css-1czprqx 488.0x61.0 bg #ffffff border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px shadow #4c00ff 0px 0px 0px 1px inset | input.fs-mask.css-1czprqx 488.0x61.0 bg #ffffff border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px shadow #4c00ff 0px 0px 0px 1px inset |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `trial-field-default.png`, `trial-field-focused.png`, `trial-field-filled.png`.

#### trial-checkbox

Consent checkbox. The painted square of the opt-in marketing checkbox (the real input is a 1x1 inside it); measured, never toggled.

Page: trial. Selector: `trial checkbox painted square`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 805.5 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | DSIndigo 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 | = | = | = |
| Text node | p: DSIndigo 12px/18px 400, #130032, ls 0.2px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.styledCheckbox.css-lnan8r 20.0x20.0 border T:2px solid #130032 @ 0.15 / R:2px solid #130032 @ 0.15 / B:2px solid #130032 @ 0.15 / L:2px solid #130032 @ 0.15 r 2px | span.styledCheckbox.css-lnan8r 20.0x20.0 border T:2px solid #130032 / R:2px solid #130032 / B:2px solid #130032 / L:2px solid #130032 r 2px; span::before.styledCheckbox.css-lnan8r 32pxx32px bg #130032 @ 0.15 r 4px | input.css-xrchdt 1.0x1.0 outline 1px auto #005fcc offset 2px; span.styledCheckbox.css-lnan8r 20.0x20.0 border T:2px solid #130032 @ 0.15 / R:2px solid #130032 @ 0.15 / B:2px solid #130032 @ 0.15 / L:2px solid #130032 @ 0.15 r 2px outline 2px solid #4c00ff offset 4px | span.styledCheckbox.css-lnan8r 20.0x20.0 border T:2px solid #130032 / R:2px solid #130032 / B:2px solid #130032 / L:2px solid #130032 r 2px; span::before.styledCheckbox.css-lnan8r 32pxx32px bg #130032 @ 0.15 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `trial-checkbox-default.png`, `trial-checkbox-hover.png`, `trial-checkbox-focus-visible.png`, `trial-checkbox-pressed.png`.

#### trial-cta

Trial submit. The Get-Started submit button; measured, never pressed (a press submits the form).

Page: trial. Selector: `button "Get Started"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 488 x 40 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #4c00ff | #4000cc | = | #4000cc |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.e8s5rbc4.css-12qqw96 488.0x40.0 bg #4c00ff r 4px | button.e8s5rbc4.css-12qqw96 488.0x40.0 bg #4000cc r 4px | button.e8s5rbc4.css-12qqw96 488.0x40.0 bg #4c00ff r 4px outline 2px solid #4c00ff offset 2px | button.e8s5rbc4.css-12qqw96 488.0x40.0 bg #4000cc r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `trial-cta-default.png`, `trial-cta-hover.png`, `trial-cta-focus-visible.png`, `trial-cta-pressed.png`.

#### help-button

Help button. The floating Help launcher; measured, never opened.

Page: trial. Selector: `button "Help"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.61 x 40 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f8f3f0 | = | #f8f3f0 |
| Box shadow | #000000 @ 0 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #130032 | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | default | pointer | = | pointer |
| Icon | 16 x 16, colour #130032 | = | = | = |
| Painted layers | button.eu93iue3.css-1dlkjwh 85.6x40.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 1px inset | button.eu93iue3.css-1dlkjwh 85.6x40.0 bg #f8f3f0 r 8px shadow #000000 @ 0 0px 0px 0px 1px inset | button.eu93iue3.css-1dlkjwh 85.6x40.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 1px inset outline 2px solid #4c00ff offset 2px | button.eu93iue3.css-1dlkjwh 85.6x40.0 bg #f8f3f0 r 8px shadow #000000 @ 0 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `help-button-default.png`, `help-button-hover.png`, `help-button-focus-visible.png`, `help-button-pressed.png`.

### Signature generator

#### sg-title

Generator title. The signature-generator display heading.

Page: signgen. Selector: `h1 on /signature-generator`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 864 x 155.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DS Indigo 72px/77.76px 300 |
| Letter spacing | -1.44px |
| Colour | #130032 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `sg-title-default.png`.

#### sg-tab-draw

Draw tab. The Draw half of the Draw/Type mode toggle.

Page: signgen. Selector: `button "Draw"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 122.72 x 45 | = | = | = |
| Padding | 12px 32px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #cbc2ff | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.04 0px 1px 3px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | DS Indigo 14px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4c00ff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #4c00ff | = | = | = |
| Painted layers | button.css-1e1zqut.eznxeq530 122.7x45.0 bg #ffffff border T:1px solid #cbc2ff / R:1px solid #cbc2ff / B:1px solid #cbc2ff / L:1px solid #cbc2ff r 6px shadow #000000 @ 0.04 0px 1px 3px 0px | = | button.css-1e1zqut.eznxeq530 122.7x45.0 bg #ffffff border T:1px solid #cbc2ff / R:1px solid #cbc2ff / B:1px solid #cbc2ff / L:1px solid #cbc2ff r 6px shadow #000000 @ 0.04 0px 1px 3px 0px outline 1px auto #005fcc offset 0px | = |
| Ancestor paint | 1 up div.css-1iihvd7.eznxeq531 bg #ede5ff; 3 up div.css-ugve7o.eznxeq533 bg #ffffff shadow #4c00ff @ 0.05 0px 4px 24px 0px, #cbc2ff @ 0.4 0px 20px 40px -10px, #4c00ff @ 0.15 0px 30px 60px -15px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sg-tab-draw-default.png`, `sg-tab-draw-hover.png`, `sg-tab-draw-focus-visible.png`, `sg-tab-draw-pressed.png`.

#### sg-tab-type

Type tab. The Type half of the mode toggle; its own click revealed the name field below.

Page: signgen. Selector: `button "Type"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.48 x 45 | = | = | = |
| Padding | 12px 32px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | DS Indigo 14px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 | #4c00ff | = | #4c00ff |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #130032 | 16 x 16, colour #4c00ff | = | 16 x 16, colour #4c00ff |
| Painted layers | button.css-1hijut9.eznxeq530 119.5x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | = | button.css-1hijut9.eznxeq530 119.5x45.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px outline 1px auto #005fcc offset 0px | = |
| Ancestor paint | 1 up div.css-1iihvd7.eznxeq531 bg #ede5ff; 3 up div.css-ugve7o.eznxeq533 bg #ffffff shadow #4c00ff @ 0.05 0px 4px 24px 0px, #cbc2ff @ 0.4 0px 20px 40px -10px, #4c00ff @ 0.15 0px 30px 60px -15px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sg-tab-type-default.png`, `sg-tab-type-hover.png`, `sg-tab-type-focus-visible.png`, `sg-tab-type-pressed.png`.

#### sg-canvas

Signature canvas. The signature preview surface in Draw mode.

Page: signgen. Selector: `signature canvas`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 888 x 260 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Transition | none |
| Cursor | crosshair |
| Ancestor paint | 1 up div.css-1qlzyv3.eiwfxt55 bg #ffffff |
| How | at rest |

Crops: `sg-canvas-default.png`.

#### sg-color

Colour swatch. A signature colour swatch button (Cobalt); toggled, which re-inks the preview.

Page: signgen. Selector: `button "Cobalt"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | 35.2 x 35.2 | = | 30.4 x 30.4 |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #4c00ff | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | DSIndigo 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | transform, box-shadow 0.15s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-134lfn8.eatuid90 32.0x32.0 bg #4c00ff r 50% | button.css-134lfn8.eatuid90 35.2x35.2 bg #4c00ff r 50% | button.css-134lfn8.eatuid90 32.0x32.0 bg #4c00ff r 50% shadow #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px | button.css-134lfn8.eatuid90 30.4x30.4 bg #4c00ff r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.1, 0, 0, 1.1, 0, 0) | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `sg-color-default.png`, `sg-color-hover.png`, `sg-color-focus-visible.png`, `sg-color-pressed.png`.

#### sg-clear

Clear button. The Clear action on the draw canvas.

Page: signgen. Selector: `button "Clear"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.48 x 35 | = | - | = |
| Padding | 8px 12px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | DS Indigo 14px/normal 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #26065d @ 0.3 | = | - | = |
| Transition | all 0.2s ease | = | - | = |
| Cursor | not-allowed | = | - | = |
| Icon | 18 x 18, colour #26065d @ 0.3 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `sg-clear-default.png`, `sg-clear-hover.png`, `sg-clear-pressed.png`.

#### sg-download

Download button. The Download-as-PNG action; measured, never pressed (a press downloads a file).

Page: signgen. Selector: `button "Download as PNG"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 438 x 48 | = | - | = |
| Padding | 0px 24px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | #cbc2ff | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | DS Indigo 16px/normal 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #26065d @ 0.5 | = | - | = |
| Transition | all 0.3s ease | = | - | = |
| Cursor | not-allowed | = | - | = |
| Icon | 18 x 18, colour #26065d @ 0.5 | = | - | = |
| Painted layers | button.css-1dchwxh.e1s1awzv0 438.0x48.0 bg #cbc2ff r 8px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `sg-download-default.png`, `sg-download-hover.png`, `sg-download-pressed.png`.

#### sg-field

Name field. The "Your name" input in Type mode; a sample name (Alex Sample) was typed to render the script previews, nothing sent.

Page: signgen. Selector: `input#signature-name`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 888 x 52 | = |
| Padding | 0px 16px | = |
| Border | 1px solid #cbc2ff | 1px solid #4c00ff |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | none | #4c00ff @ 0.1 0px 0px 0px 3px |
| Outline | none | = |
| Font | DS Indigo 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #130032 | = |
| Transition | all 0.2s ease | = |
| Cursor | text | = |
| Placeholder | #26065d @ 0.4, opacity 1 | = |
| Painted layers | input.css-1gbgv7m.e6qbbsq11 888.0x52.0 bg #ffffff border T:1px solid #cbc2ff / R:1px solid #cbc2ff / B:1px solid #cbc2ff / L:1px solid #cbc2ff r 8px | input.css-1gbgv7m.e6qbbsq11 888.0x52.0 bg #ffffff border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px shadow #4c00ff @ 0.1 0px 0px 0px 3px |
| How | at rest | clicked into the field |

Crops: `sg-field-default.png`, `sg-field-focused.png`.

#### sg-font

Script-face option. A signature script-face picker option (The Curator et al.); toggled, which re-renders the preview.

Page: signgen. Selector: `script face option`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 438 x 85 | = | = | = |
| Padding | 14px 16px 16px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #4c00ff | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | DSIndigo 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.css-16cwh7d.e6qbbsq7: DS Indigo 11px/normal 400, #26065d @ 0.5, ls 0.11px | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #ffffff | = | = | = |
| Painted layers | button.css-1xgs5ey.e6qbbsq9 438.0x85.0 bg #ffffff border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px; div.css-10eia79.e6qbbsq8 20.0x20.0 bg #4c00ff r 50% | = | button.css-1xgs5ey.e6qbbsq9 438.0x85.0 bg #ffffff border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px outline 1px auto #005fcc offset 0px; div.css-10eia79.e6qbbsq8 20.0x20.0 bg #4c00ff r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sg-font-default.png`, `sg-font-hover.png`, `sg-font-focus-visible.png`, `sg-font-pressed.png`.

### Customer stories

#### st-title

Stories title. The customer-stories page heading.

Page: stories. Selector: `h1 on /customer-stories`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 123.89 x 56 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/24px 500 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | span.css-oa7nr3.e1kahpgs1: DSIndigo 16px/24px 500, #130032 |
| Transition | none |
| Painted layers | span::after.css-oa7nr3.e1kahpgs1 0%x1px bg #4c00ff |
| How | at rest |

Crops: `st-title-default.png`.

#### filter-button

Filter dropdown. A stories filter dropdown trigger (Products used/Industry/Department); measured, never opened.

Page: stories. Selector: `stories filter button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.02 x 53 | = | = | = |
| Padding | 16px 0px | = | = | = |
| Gap | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 14px/21px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #130032 @ 0.75 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #130032 @ 0.75 | = | = | = |
| ::after | 97.0156px x 2px, absolute, bg #000000 @ 0, radius 0px | 97.0156px x 2px, absolute, bg #4c00ff, radius 0px | 97.0156px x 2px, absolute, bg #4c00ff, radius 0px | 97.0156px x 2px, absolute, bg #4c00ff, radius 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button::after.css-1lg64h2.e1fdzuzw15 97.0156pxx2px bg #4c00ff | button.css-1lg64h2.e1fdzuzw15 97.0x53.0 r 4px outline 2px solid #4c00ff offset 2px; button::after.css-1lg64h2.e1fdzuzw15 97.0156pxx2px bg #4c00ff | button::after.css-1lg64h2.e1fdzuzw15 97.0156pxx2px bg #4c00ff |

Crops: `filter-button-default.png`, `filter-button-hover.png`, `filter-button-focus-visible.png`, `filter-button-pressed.png`.

#### story-card

Story card. A customer-story card link; measured never followed.

Page: stories. Selector: `story card link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 328 x 445.75 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 | = | = | = |
| Text node | h2.css-uuneru.e1et20720: DSIndigo 24px/29.76px 500, #130032, ls -0.25px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.css-7m64jd 328.0x164.0 bg #f8f3f0 r 16px; h2.css-uuneru.e1et20720 286.1x152.0 image linear-gradient(#000000 @ 0 calc(100% - 1px), #130032 1px); p.css-10gbszt.e11vtv6p0 311.6x59.0 border T:1px solid #130032 @ 0.15 | = | a.e1c0i0370.css-1cvxahv 328.0x445.8 r 4px outline 2px solid #4c00ff offset 2px; div.css-7m64jd 328.0x164.0 bg #f8f3f0 r 16px; h2.css-uuneru.e1et20720 286.1x152.0 image linear-gradient(#000000 @ 0 calc(100% - 1px), #130032 1px); p.css-10gbszt.e11vtv6p0 311.6x59.0 border T:1px solid #130032 @ 0.15 | = |
| Ancestor paint | 1 up article.css-nqyne5 bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `story-card-default.png`, `story-card-hover.png`, `story-card-focus-visible.png`, `story-card-pressed.png`.

#### story-logo

Story logo. A customer logo tile on the stories page.

Page: stories. Selector: `story logo img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 328 x 328 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #f8f3f0 |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `story-logo-default.png`.

### Pricing storefront (ecom)

#### ec-header

Storefront header. The ecom storefront chrome (its own header, Log In).

Page: pricing. Selector: `ecom header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 69 |
| Padding | 0px 80px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DS Indigo 16px/24px 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | span.css-1avyp1d: DS Indigo 16px/24px 400, #130032 @ 0.9 |
| Transition | none |
| Icon | 128 x 32, colour #000000 |
| Painted layers | a.css-1azp2gh 128.0x34.0 r 2px outline 2px solid #000000 @ 0 offset 2px; button.css-144qxs6 77.0x40.0 border T:1px solid #130032 @ 0.5 / R:1px solid #130032 @ 0.5 / B:1px solid #130032 @ 0.5 / L:1px solid #130032 @ 0.5 r 4px |
| How | at rest |

Crops: `ec-header-default.png`.

#### ec-title

Pricing title. The storefront page heading.

Page: pricing. Selector: `h1 on ecom pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 762.98 x 149.13 |
| Padding | 80px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DS Indigo 64px/69.12px 300 |
| Letter spacing | -1.5px |
| Colour | #130032 @ 0.9 |
| Transition | none |
| How | at rest |

Crops: `ec-title-default.png`.

#### ec-billing-annual

Annual toggle. The Annual half of the billing-period toggle.

Page: pricing. Selector: `button "Annual"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 28 | = | = | = |
| Padding | 2px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #130032 @ 0.05 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | DS Indigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 @ 0.9 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-w0848l 81.0x28.0 bg #130032 @ 0.05 r 4px | = | button.css-w0848l 81.0x28.0 bg #130032 @ 0.05 r 4px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ec-billing-annual-default.png`, `ec-billing-annual-hover.png`, `ec-billing-annual-focus-visible.png`, `ec-billing-annual-pressed.png`.

#### ec-billing-monthly

Monthly toggle. The Monthly half of the billing toggle; its own click re-priced the cards (the monthly shot).

Page: pricing. Selector: `button "Monthly"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 28 | = | = | = |
| Padding | 2px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | DS Indigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 @ 0.7 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.css-gqscow bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.css-18x2esv 81.0x28.0 r 4px outline 1px auto #005fcc offset 0px | = |

Crops: `ec-billing-monthly-default.png`, `ec-billing-monthly-hover.png`, `ec-billing-monthly-focus-visible.png`, `ec-billing-monthly-pressed.png`.

#### plan-name

Plan name. A plan card's name.

Page: pricing. Selector: `plan name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 251 x 37.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DS Indigo 30px/37.2px 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. A plan card's price figure (SGD on the /en-SG/ route).

Page: pricing. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 194.88 x 72 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DS Indigo 16px/24px 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | div.css-my4xgf: DS Indigo 20px/28px 400, #130032 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-card

Plan card. A pricing plan card (the painted section ancestor of a Buy-now action).

Page: pricing. Selector: `plan card section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 301 x 922.2 |
| Padding | 0px |
| Border | 1px solid #130032 @ 0.5 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | DS Indigo 16px/24px 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | h3.css-13eh761: DS Indigo 30px/37.2px 400, #130032 |
| Transition | none |
| Painted layers | section.css-1c8yk0d 301.0x922.2 bg #ffffff border T:1px solid #130032 @ 0.5 / R:1px solid #130032 @ 0.5 / B:1px solid #130032 @ 0.5 / L:1px solid #130032 @ 0.5 r 16px; div.css-bqy4c5 299.0x320.2 bg #ffffff r 16px; a.css-14boon 251.0x56.0 bg #4c00ff r 8px; div.dxp-pricing-plans__bottomText.css-1gdxv9c 251.0x51.0 border B:1px solid #e1dbdd; button.css-1av88hh 251.0x51.8 border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px |
| How | at rest |

Crops: `plan-card-default.png`.

#### buy-now

Buy-now CTA. A plan's Buy-Now action; measured never followed.

Page: pricing. Selector: `"Buy Now"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 251 x 56 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #4c00ff | #4000cc | = | #330099 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | DS Indigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.css-1avyp1d: DS Indigo 16px/24px 500, #ffffff | = | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 1, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-14boon 251.0x56.0 bg #4c00ff r 8px | a.css-14boon 251.0x56.0 bg #4000cc r 8px | a.css-14boon 251.0x56.0 bg #4c00ff r 8px shadow #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | a.css-14boon 251.0x56.0 bg #330099 r 8px |
| Ancestor paint | 1 up div.css-bqy4c5 bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `buy-now-default.png`, `buy-now-hover.png`, `buy-now-focus-visible.png`, `buy-now-pressed.png`.

#### contact-sales

Contact-sales CTA. The enterprise plan's Contact-Sales action; measured never followed.

Page: pricing. Selector: `"Contact Sales"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 249 x 56 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #130032 | 1px solid #130032 @ 0.9 | = | 1px solid #130032 @ 0.75 |
| Radius | 8px | = | = | = |
| Background | #130032 | #130032 @ 0.9 | = | #130032 @ 0.75 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | DS Indigo 16px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | #ffffff @ 0.8 |
| Text node | span.css-1avyp1d: DS Indigo 16px/16px 500, #ffffff | = | = | span.css-1avyp1d: DS Indigo 16px/16px 500, #ffffff @ 0.8 |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 1, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-ii9jrq 249.0x56.0 bg #130032 border T:1px solid #130032 / R:1px solid #130032 / B:1px solid #130032 / L:1px solid #130032 r 8px | a.css-ii9jrq 249.0x56.0 bg #130032 @ 0.9 border T:1px solid #130032 @ 0.9 / R:1px solid #130032 @ 0.9 / B:1px solid #130032 @ 0.9 / L:1px solid #130032 @ 0.9 r 8px | a.css-ii9jrq 249.0x56.0 bg #130032 border T:1px solid #130032 / R:1px solid #130032 / B:1px solid #130032 / L:1px solid #130032 r 8px shadow #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | a.css-ii9jrq 249.0x56.0 bg #130032 @ 0.75 border T:1px solid #130032 @ 0.75 / R:1px solid #130032 @ 0.75 / B:1px solid #130032 @ 0.75 / L:1px solid #130032 @ 0.75 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `contact-sales-default.png`, `contact-sales-hover.png`, `contact-sales-focus-visible.png`, `contact-sales-pressed.png`.

#### feature-row

Feature row. An expandable feature row on a plan card; toggled open once.

Page: pricing. Selector: `feature accordion row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 176.3 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | DS Indigo 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 | = | = | = |
| Text node | span: DS Indigo 14px/20px 400, #130032 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.css-1wo266l 176.3x20.0 outline 1px auto #005fcc offset 0px | = |

Crops: `feature-row-default.png`, `feature-row-hover.png`, `feature-row-focus-visible.png`, `feature-row-pressed.png`.

#### see-all

See-all-features. The See-All-Features expander; measured, never expanded.

Page: pricing. Selector: `"See All Features"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 251 x 51.77 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | 1px solid #4c00ff | 1px solid #ede5ff | = | 1px solid #ede5ff |
| Radius | 8px | = | = | = |
| Background | transparent | #ede5ff | = | #ede5ff |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | DS Indigo 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4c00ff | = | = | #130032 |
| Text node | span.css-1avyp1d: DS Indigo 16px/24px 400, #4c00ff | = | = | span.css-1avyp1d: DS Indigo 16px/24px 400, #130032 |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 1, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-1av88hh 251.0x51.8 border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px | button.css-1av88hh 251.0x51.8 bg #ede5ff border T:1px solid #ede5ff / R:1px solid #ede5ff / B:1px solid #ede5ff / L:1px solid #ede5ff r 8px | button.css-1av88hh 251.0x51.8 border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 8px shadow #ffffff 0px 0px 0px 2px, #4c00ff 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | button.css-1av88hh 251.0x51.8 bg #ede5ff border T:1px solid #ede5ff / R:1px solid #ede5ff / B:1px solid #ede5ff / L:1px solid #ede5ff r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `see-all-default.png`, `see-all-hover.png`, `see-all-focus-visible.png`, `see-all-pressed.png`.

### Log in

#### auth-card

Login card. The centred OAuth login card on account.docusign.com; never filled or submitted.

Page: login. Selector: `login card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 556 x 439.59 |
| Padding | 64px 0px |
| Border | 1px solid #191823 @ 0.15 |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | DS Indigo 16px/24px 400 |
| Letter spacing | normal |
| Colour | #130032 @ 0.9 |
| Text node | span.css-114jwlx: DS Indigo 24px/30px 400, #130032 @ 0.9 |
| Transition | none |
| Painted layers | div.ink-auth-main 556.0x439.6 bg #ffffff border T:1px solid #191823 @ 0.15 / R:1px solid #191823 @ 0.15 / B:1px solid #191823 @ 0.15 / L:1px solid #191823 @ 0.15 r 4px; div.input-text-box-wrapper.css-19cp9qb 426.0x40.0 bg #ffffff border T:1px solid #130032 @ 0.5 / R:1px solid #130032 @ 0.5 / B:1px solid #130032 @ 0.5 / L:1px solid #130032 @ 0.5 r 4px outline 1px solid #000000 @ 0 offset -2px; button.olv-button.olv-ignore-transform 426.0x40.0 bg #260559 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; a.olv-button.olv-ignore-transform 426.0x40.0 bg #130032 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| Ancestor paint | 1 up div.ink-body bg #f7f6f7 |
| How | at rest |

Crops: `auth-card-default.png`.

#### auth-field

Email field. The Enter-email input; sample text was typed and deleted, nothing sent.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 424 x 38 | = | = |
| Padding | 8px 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | DS Indigo 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #130032 @ 0.9 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #130032 @ 0.7, opacity 1 | = | #130032 @ 0.9, opacity 1 |
| Ancestor paint | 1 up div.input-text-box-wrapper.css-19cp9qb bg #ffffff outline 1px solid #000000 @ 0 | 1 up div.input-text-box-wrapper.css-183veqb bg #ffffff outline 2px solid #37039e | 1 up div.input-text-box-wrapper.css-183veqb bg #ffffff outline 2px solid #37039e |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `auth-field-default.png`, `auth-field-focused.png`, `auth-field-filled.png`.

#### auth-next

Next button. The Next submit; measured, never pressed (a press continues sign-in).

Page: login. Selector: `button "Next"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 426 x 40 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #260559 | #2b047f | = | #37039e |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #130032 offset 2px | = |
| Font | DS Indigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.css-16hz1ch: DS Indigo 16px/24px 500, #ffffff | = | = | = |
| Transition | background-color, border-color, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.olv-button.olv-ignore-transform 426.0x40.0 bg #260559 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.olv-button.olv-ignore-transform 426.0x40.0 bg #2b047f border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.olv-button.olv-ignore-transform 426.0x40.0 bg #260559 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #130032 offset 2px | button.olv-button.olv-ignore-transform 426.0x40.0 bg #37039e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-next-default.png`, `auth-next-hover.png`, `auth-next-focus-visible.png`, `auth-next-pressed.png`.

#### auth-lang

Language picker. The English-(US) language menu trigger; measured, never opened.

Page: login. Selector: `language button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.64 x 20 | = | = | = |
| Padding | 0px 0px 0px 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #130032 @ 0.05 | #130032 @ 0.1 | = | #130032 @ 0.15 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #130032 offset 2px | = |
| Font | DS Indigo 10px/12px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 @ 0.9 | = | = | = |
| Text node | span.css-16hz1ch: DS Indigo 10px/12px 500, #130032 @ 0.9 | = | = | = |
| Transition | background-color, border-color, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #130032 @ 0.9 | = | = | = |
| Painted layers | button.olv-button.olv-ignore-transform 85.6x20.0 bg #130032 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.olv-button.olv-ignore-transform 85.6x20.0 bg #130032 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.olv-button.olv-ignore-transform 85.6x20.0 bg #130032 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #130032 offset 2px | button.olv-button.olv-ignore-transform 85.6x20.0 bg #130032 @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-lang-default.png`, `auth-lang-hover.png`, `auth-lang-focus-visible.png`, `auth-lang-pressed.png`.

#### auth-signup

Signup link. The Sign-Up-for-Free link under the card; measured never followed.

Page: login. Selector: `"Sign Up for Free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 426 x 40 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #130032 @ 0.05 | #130032 @ 0.1 | = | #130032 @ 0.15 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #130032 offset 2px | = |
| Font | DS Indigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 @ 0.9 | = | = | = |
| Text node | span.css-16hz1ch: DS Indigo 16px/24px 500, #130032 @ 0.9 | = | = | = |
| Transition | background-color, border-color, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.olv-button.olv-ignore-transform 426.0x40.0 bg #130032 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | a.olv-button.olv-ignore-transform 426.0x40.0 bg #130032 @ 0.1 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | a.olv-button.olv-ignore-transform 426.0x40.0 bg #130032 @ 0.05 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px outline 2px solid #130032 offset 2px | a.olv-button.olv-ignore-transform 426.0x40.0 bg #130032 @ 0.15 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-signup-default.png`, `auth-signup-hover.png`, `auth-signup-focus-visible.png`, `auth-signup-pressed.png`.

### Footer

#### footer

Footer. The marketing footer: link columns, locale selector, legal and social.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 974 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 14px/21px 400 |
| Letter spacing | 0.2px |
| Colour | #130032 |
| Text node | p.css-1tum30j: DSIndigo 12px/18px 600, #130032, ls 0.8px |
| Transition | none |
| Icon | 16 x 16, colour #130032 @ 0.75 |
| Painted layers | section.css-29n46u.e1p96sfz1 1440.0x746.0 bg #f8f3f0; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #130032 @ 0.75 | = | = | = |
| Text node | span.css-llpyjt: DSIndigo 14px/21px 500, #130032, ls 0.2px | span.css-llpyjt: DSIndigo 14px/21px 500, #130032 @ 0.75, ls 0.2px | span.css-llpyjt: DSIndigo 14px/21px 500, #130032 @ 0.75, ls 0.2px | span.css-llpyjt: DSIndigo 14px/21px 500, #130032 @ 0.75, ls 0.2px |
| Transition | color 0.15s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75 | div::after.css-1eg020q.e1tasy2f1 100%x1px bg #130032 @ 0.75 | a.css-1po7wbl.e1tasy2f0 184.0x44.0 r 4px outline 2px solid #4c00ff offset 2px; div::after.css-1eg020q.e1tasy2f1 0pxx1px bg #130032 @ 0.75 | div::after.css-1eg020q.e1tasy2f1 100%x1px bg #130032 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### locale-button

Locale button. The United-States locale menu trigger; measured, never opened.

Page: home. Selector: `footer locale button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200 x 40 | = | = | = |
| Padding | 8px 48px 8px 16px | = | = | = |
| Border | 1px solid #130032 @ 0.15 | 1px solid #4c00ff | 1px solid #4c00ff | 1px solid #4c00ff |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | DSIndigo 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-71e3p0.e1pjg5h24 200.0x40.0 border T:1px solid #130032 @ 0.15 / R:1px solid #130032 @ 0.15 / B:1px solid #130032 @ 0.15 / L:1px solid #130032 @ 0.15 r 2px | button.css-71e3p0.e1pjg5h24 200.0x40.0 border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 2px | button.css-71e3p0.e1pjg5h24 200.0x40.0 border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 2px | button.css-71e3p0.e1pjg5h24 200.0x40.0 border T:1px solid #4c00ff / R:1px solid #4c00ff / B:1px solid #4c00ff / L:1px solid #4c00ff r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `locale-button-default.png`, `locale-button-hover.png`, `locale-button-focus-visible.png`, `locale-button-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `navbar at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | a.css-2llxql.evij40y0: DSIndigo 14px/21px 600, #ffffff, ls 0.2px |
| Transition | none |
| Icon | 24 x 24, colour #130032 |
| Painted layers | nav.css-b9x1zj 390.0x77.0 bg #ffffff; div.css-19njzqs.e1p96sfz1 390.0x77.0 bg #ffffff; div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #4c00ff; section.css-1crqsg9.e1p96sfz1 0.0x0.0 bg #ffffff r 0px 0px 16px 16px shadow #130032 @ 0.2 0px 32px 64px 0px; span.css-11bm945 0.0x0.0 border B:1px solid #cbc2ff; div::after.css-aknfkn.e1tasy2f1 0pxx1px bg #130032 |
| Ancestor paint | 1 up div.css-z3jndn.er28sow2 bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header hamburger toggle.

Page: mobile. Selector: `hamburger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | DSIndigo 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #130032 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.css-kkuep2 24.0x30.0 outline 1px auto #005fcc offset 0px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The header menu opened by its own toggle.

Page: mobile. Selector: `mobile menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 16px/normal 400 |
| Letter spacing | normal |
| Colour | #130032 |
| Text node | button.css-15xalk.e1yg1y6k0: DSIndigo 18px/normal 500, #130032 @ 0.75 |
| Transition | none |
| Icon | 24 x 24, colour #4c00ff |
| Painted layers | nav.css-b9x1zj 390.0x77.0 bg #ffffff; div.css-135fn6v 390.0x844.0 bg #ffffff; div.css-1p9p3rd 390.0x93.0 border B:1px solid #130032 @ 0.15; button.css-17xia4k.e1r5rlla1 44.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50%; button.css-17xia4k.e1r5rlla1 44.0x44.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 50%; button.css-15xalk.e1yg1y6k0 91.4x73.0 r 4px outline 2px solid #4c00ff offset 2px |
| Ancestor paint | 1 up div.css-z3jndn.er28sow2 bg #ffffff |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened header menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.36 x 73 | = | = | = |
| Padding | 24px 0px | = | = | = |
| Gap | 3.2px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 18px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #130032 @ 0.75 | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #130032 @ 0.75 | = | = | = |
| ::after | 91.3594px x 2px, absolute, bg #000000 @ 0, radius 0px | 91.3594px x 2px, absolute, bg #4c00ff, radius 0px | 91.3594px x 2px, absolute, bg #4c00ff, radius 0px | 91.3594px x 2px, absolute, bg #4c00ff, radius 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button::after.css-15xalk.e1yg1y6k0 91.3594pxx2px bg #4c00ff | button.css-15xalk.e1yg1y6k0 91.4x73.0 r 4px outline 2px solid #4c00ff offset 2px; button::after.css-15xalk.e1yg1y6k0 91.3594pxx2px bg #4c00ff | button::after.css-15xalk.e1yg1y6k0 91.3594pxx2px bg #4c00ff |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 187.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DSIndigo 58px/62.64px 300 |
| Letter spacing | -1.25px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-cta

Mobile CTA. The hero call to action at phone width.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 56 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #4c00ff | #4000cc | = | #4000cc |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #4c00ff offset 2px | = |
| Font | DSIndigo 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.css-1ra4uzk.e1tasy2f1: DSIndigo 16px/24px 500, #ffffff | = | = | = |
| Transition | background-color, border-color, box-shadow, color 0.1s cubic-bezier(0.33, 0, 0.67, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-4djp8s.e1tasy2f0 358.0x56.0 bg #4c00ff r 8px; div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #4c00ff | a.css-4djp8s.e1tasy2f0 358.0x56.0 bg #4000cc r 8px; div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #4c00ff | a.css-4djp8s.e1tasy2f0 358.0x56.0 bg #4c00ff r 8px outline 2px solid #4c00ff offset 2px; div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #4c00ff | a.css-4djp8s.e1tasy2f0 358.0x56.0 bg #4000cc r 8px; div::after.css-1ra4uzk.e1tasy2f1 0pxx1px bg #130032 |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (the inline Emotion blocks and same-origin sheets; cross-origin vendor sheets are skipped); the per-state Transition rows above are computed values and cover every rule.

- esignature: `0.4s`, `all`, `none`, `visibility 0.1s, opacity 0.1s`, `visibility 1s, opacity 1s`, `0.2s`, `width 1s`, `visibility 0.1s, opacity 0.1s, height 0.1s, width 0.1s, left, top`, `left`, `width 0.1s`, `visibility 1s, opacity 1s, height 1s 1s, width 1s 1s, left 1s 1s, top 1s 1s`, `visibility 1s, opacity 1s, height 1s 1s, width 1s, left 1s 1s, top 1s 1s`

- home: `width 300ms ease-in-out`, `opacity 200ms ease-out`, `background-color 200ms ease-in-out`, `transform 200ms linear`, `color 150ms ease-in-out`, `background-color 150ms ease-in-out, box-shadow 150ms ease-in-out`, `color 100ms cubic-bezier(0.33, 0, 0.67, 1)`, `opacity 500ms ease-in-out`, `none`, `opacity 600ms`, `opacity 600ms, transform 600ms`, `width 300ms ease-out, background-color 100ms ease-out`

- login: `opacity 300ms`, `opacity 350ms`, `fill 0.2s`

- pricing: `0.1s`, `300ms ease-in`, `color 150ms ease-in-out`, `transform 300ms ease-in-out`, `background-color 150ms ease-in-out`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- signgen: `0.2s`, `opacity 0.3s, transform 0.3s`, `opacity 0.3s ease-out`, `transform 0.15s, box-shadow 0.2s`, `font-size 0.15s`, `0.3s`, `color 0.2s`, `transform 0.3s`, `max-height 0.3s, opacity 0.25s, padding 0.3s`, `opacity 0.2s`, `transform 0.2s, box-shadow 0.2s`, `opacity 150ms`

- stories: `0.4s`, `all`, `none`, `visibility 0.1s, opacity 0.1s`, `visibility 1s, opacity 1s`, `0.2s`, `width 1s`, `visibility 0.1s, opacity 0.1s, height 0.1s, width 0.1s, left, top`, `left`, `width 0.1s`, `visibility 1s, opacity 1s, height 1s 1s, width 1s 1s, left 1s 1s, top 1s 1s`, `visibility 1s, opacity 1s, height 1s 1s, width 1s, left 1s 1s, top 1s 1s`

- trial: `width 300ms ease-in-out`, `transform 200ms linear`, `color 150ms ease-in-out`, `font-size 200ms ease-in-out, top 200ms ease-in-out`, `border-color 200ms ease-in-out`, `background-color 600000s, color 600000s`, `background-color 200ms ease-in-out`, `0.1s`, `300ms ease-in`, `transform 300ms ease-in-out`, `background-color 150ms ease-in-out`, `0.2s ease-in`
