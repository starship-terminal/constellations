# Component measurements

Computed styles read from www.headspace.com, organizations.headspace.com, checkout.headspace.com and auth.headspace.com on 2026-11-17 by `tools/capture/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Marketing chrome

#### nav-promo-strip

Promo strip. The banner over the header ("Feel your best for 50% off →").

Page: home. Selector: `header + div / [data-testid*="promo" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 18px/26px 500 |
| Letter spacing | -0.18px |
| Colour | #2d2c2b |
| Text node | nobr: Headspace Apercu 18px/26px 500, #2d2c2b, ls -0.18px |
| Transition | none |
| Cursor | pointer |
| How | resting state |

Crops: `nav-promo-strip-default.png`.

#### nav-header

Header bar. The top bar: logo, the For You / For Business / For Providers / Our Plans / Resources / About categories, Log in, Help and the Get-50%-off CTA.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px 48px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #4b4c4d |
| Text node | a.css-1cajptc: Headspace Apercu 16px/18.4px 400, #2d2c2b |
| Transition | none |
| Icon | 16 x 16, colour #2d2c2b |
| Painted layers | header.css-75xqdg 1440.0x80.0 bg #ffffff; dialog.css-1rhcoa3 1440.0x335.2 bg #ffffff r 0px 0px 24px 24px shadow #141313 @ 0.2 0px 1px 8px 0px; div.css-15t8m5e 280.0x213.0 bg #f9f4f2 r 24px; div.css-1gr7t27 280.0x175.0 bg #0061ef r 24px 24px 0px 0px; dialog.css-1rhcoa3 1440.0x298.4 bg #ffffff r 0px 0px 24px 24px shadow #141313 @ 0.2 0px 1px 8px 0px; div.css-15t8m5e 280.0x213.0 bg #f9f4f2 r 24px |
| How | resting state |

Crops: `nav-header-default.png`.

#### nav-logo

Logo link. The headspace wordmark image in the header.

Page: home. Selector: `header a[data-testid="logo-link"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 152 x 80 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | Headspace Apercu 16px/18.4px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0000ee | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.css-kq5vqx 152.0x80.0 outline 1px auto #101010 offset 1px |

Crops: `nav-logo-default.png`, `nav-logo-hover.png`, `nav-logo-focus-visible.png`.

#### nav-category

Nav category link. A top-level header link ("For You"): hovering it opens the mega-menu.

Page: home. Selector: `header a[data-testid="navbar-category-link"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 52 x 18.39 | 56 x 18.39 | 56 x 18.39 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | Headspace Apercu 16px/18.4px 400 | Headspace Apercu 16px/18.4px 700 | Headspace Apercu 16px/18.4px 700 |
| Letter spacing | normal | = | = |
| Colour | #2d2c2b | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.css-ccg2ra 56.0x18.4 outline 1px auto #101010 offset 1px |

Crops: `nav-category-default.png`, `nav-category-hover.png`, `nav-category-focus-visible.png`.

#### nav-mega-menu

Mega-menu pane (open). The dropdown pane of subcategory links under a hovered category. "opened" is a real pointer hover on the category link; the pane is read while the pointer rests inside it.

Page: home. Selector: `header a[data-testid="navbar-subcategory-link"] pane`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 223.52 x 204.78 |
| Padding | 0px |
| Gap | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.css-1q01dj5: Headspace Apercu 16px/20.8px 400, #44423f |
| Transition | none |
| Icon | 16 x 16, colour #2d2c2b |
| Ancestor paint | 3 up dialog.css-1rhcoa3 bg #ffffff shadow #141313 @ 0.2 0px 1px 8px 0px |
| How | a real pointer hover on the header category link — the pane's links were never followed |

Crops: `nav-mega-menu-opened.png`.

#### nav-subcategory

Mega-menu link. One link inside the open mega-menu ("Meditation" under For You).

Page: home. Selector: `header a[data-testid="navbar-subcategory-link"]`. States: opened, hover.

| Property | opened | hover |
|---|---|---|
| Size (w x h) | 94 x 20.8 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Headspace Apercu 16px/20.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #44423f | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #2d2c2b | = |
| How | the category link's own hover state, menu open | mouse hover over the element |

Crops: `nav-subcategory-opened.png`, `nav-subcategory-hover.png`.

#### nav-cta

Header CTA ("Get 50% off"). The pill call-to-action in the header, measured, never followed.

Page: home. Selector: `header a (text Get 50% off/Get started)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 125 x 48 | = | = | = |
| Padding | 14.3px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 32px | = | = | = |
| Background | #0061ef | #0040ea | #0040ea | = |
| Box shadow | #413d45 @ 0.2 0px 2px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #0040ea offset 1px | = |
| Font | Headspace Apercu 14px/15.4px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.css-1fvtd4u: Headspace Apercu 14px/15.4px 700, #ffffff | = | = | = |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-11fbkag 125.0x48.0 bg #0061ef border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px | a.css-11fbkag 125.0x48.0 bg #0040ea border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px | a.css-11fbkag 125.0x48.0 bg #0040ea border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px outline 2px solid #0040ea offset 1px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-login

"Log in" link. The sign-in link in the header, measured, never followed.

Page: home. Selector: `header a (text Log in)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 46 x 48 | 48 x 48 | = |
| Padding | 0px | = | = |
| Gap | 8px | = | = |
| Border | 2px solid #000000 @ 0 | = | = |
| Radius | 32px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #0040ea offset 1px |
| Font | Headspace Apercu 16px/17.6px 400 | Headspace Apercu 16px/17.6px 700 | = |
| Letter spacing | normal | = | = |
| Colour | #2d2c2b | #44423f | #44423f |
| Text node | span.css-1fvtd4u: Headspace Apercu 16px/17.6px 400, #2d2c2b | span.css-1fvtd4u: Headspace Apercu 16px/17.6px 700, #44423f | span.css-1fvtd4u: Headspace Apercu 16px/17.6px 400, #44423f |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.css-1ko1g75 46.0x48.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px | a.css-1ko1g75 48.0x48.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px | a.css-1ko1g75 46.0x48.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px outline 2px solid #0040ea offset 1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`.

#### footer

Footer. The page footer: link columns, app-store badges, the language selector and legal links.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1360 x 534.14 |
| Padding | 0px 0px 40px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #4b4c4d |
| Text node | h4.css-qjjilk: Headspace Apercu 24px/32px 700, #4b4c4d, ls -0.6px |
| Transition | none |
| Icon | 0 x 0, colour #2d2c2b |
| Painted layers | a.css-17qam0w 108.0x48.0 bg #0061ef border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px; button.css-h34ow8 0.0x0.0 bg #f9f4f2 border T:2px solid #44423f / R:2px solid #44423f / B:2px solid #44423f / L:2px solid #44423f r 32px; div.css-1v3qhkq 0.0x0.0 bg #44423f r 8px shadow #413d45 @ 0.2 0px 2px 0px 0px; button.css-1ja5a3o 0.0x0.0 bg #2d2c2b border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px; button.css-qtic42 0.0x0.0 bg #63605d border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 8px; button.css-1ja5a3o 0.0x0.0 bg #2d2c2b border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px |
| How | resting state |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in a footer column.

Page: home. Selector: `footer a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 228.2 x 13.8 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | Headspace Apercu 12px/13.8px 500 | = | = |
| Letter spacing | -0.12px | = | = |
| Colour | #44423f | = | = |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = | = |
| Opacity | 0.7 | - | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.css-xawbvs 228.2x13.8 outline 1px auto #101010 offset 1px |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`.

#### footer-language

Language selector. The footer's locale button ("English"). Measured at rest — its option list was never opened.

Page: home. Selector: `footer button/a (text English)`. States: .

Not found on the page at capture time.

#### footer-app-badge

App-store badge. The App Store / Google Play badge links in the footer.

Page: home. Selector: `footer a[href*="apple"], footer a[href*="play.google"], footer img[alt*="app" i]`. States: .

Not found on the page at capture time.

### Hero and type

#### hero-h1

Hero headline (h1). The page's display headline in Headspace Apercu.

Page: share. Selector: `main h1, h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 429.13 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 64px/72px 700 |
| Letter spacing | -1.92px |
| Colour | #4b4c4d |
| Transition | none |
| How | resting state |

Crops: `hero-h1-default.png`.

#### hero-lede

Hero lede. The paragraph under the hero headline.

Page: article. Selector: `main h1 + p / first main p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.42 x 38.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 16px/19.2px 700 |
| Letter spacing | -0.48px |
| Colour | #44423f |
| Transition | none |
| How | resting state |

Crops: `hero-lede-default.png`.

#### hero-cta

Hero primary CTA. The pill call-to-action inside the hero ("Get 50% off" / "Get started"), measured, never followed.

Page: article. Selector: `main a/button (text Get 50% off/Get started/Try)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136 x 48 | = | = | = |
| Padding | 13.2px 24px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 32px | = | = | = |
| Background | #0061ef | #0040ea | #0040ea | = |
| Box shadow | #413d45 @ 0.2 0px 2px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #0040ea offset 1px | = |
| Font | Headspace Apercu 16px/17.6px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.css-1fvtd4u: Headspace Apercu 16px/17.6px 700, #ffffff | = | = | = |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.css-akbn6o 136.0x48.0 bg #0061ef border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px | a.css-akbn6o 136.0x48.0 bg #0040ea border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px | a.css-akbn6o 136.0x48.0 bg #0040ea border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px outline 2px solid #0040ea offset 1px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### prose-h2

Section heading (h2). A mid-page section headline.

Page: article. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 780.86 x 38.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 32px/38.4px 700 |
| Letter spacing | -0.96px |
| Colour | #4b4c4d |
| Transition | none |
| How | resting state |

Crops: `prose-h2-default.png`.

#### prose-h3

Card heading (h3). A card or feature heading.

Page: article. Selector: `main h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 301.31 x 27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 18px/27px 400 |
| Letter spacing | normal |
| Colour | #141313 |
| Transition | none |
| How | resting state |

Crops: `prose-h3-default.png`.

#### prose-body

Body copy. A body paragraph.

Page: article. Selector: `main p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 18px/26px 500 |
| Letter spacing | -0.18px |
| Colour | #2d2c2b |
| Text node | nobr: Headspace Apercu 18px/26px 500, #2d2c2b, ls -0.18px |
| Transition | none |
| Cursor | pointer |
| How | resting state |

Crops: `prose-body-default.png`.

#### prose-link

Inline text link. A link inside body copy.

Page: article. Selector: `main p a, main li a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 277 x 42 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | Headspace Apercu 14px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2d2c2b | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.css-hl8alb 277.0x42.0 outline 1px auto #101010 offset 1px |

Crops: `prose-link-default.png`, `prose-link-hover.png`, `prose-link-focus-visible.png`.

### Marketing widgets

#### feature-card

Feature/benefit card. A rounded card on the home page (benefit or content tile).

Page: home. Selector: `main [class*="card" i], main article`. States: .

Not found on the page at capture time.

#### testimonial

Testimonial/press quote. A quote or press-mention block on the home page.

Page: home. Selector: `main blockquote, [class*="testimonial" i], [class*="quote" i]`. States: .

Not found on the page at capture time.

#### app-tab

Feature tab. A numbered feature tab on /app ("1 Guided meditations", "2 AI guidance", ...). Its own activation is a local UI toggle.

Page: app. Selector: `main button (text Guided meditations/AI guidance)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 205 x 30 | = |
| Padding | 0px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Headspace Apercu 18px/26px 700 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.css-gcq92y: Headspace Apercu 18px/26px 700, #ffffff, ls -0.54px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.css-gcq92y 30.0x30.0 bg #0061ef r 50% | = |
| How | resting state | mouse hover over the element |

Crops: `app-tab-default.png`, `app-tab-hover.png`.

#### faq-item

FAQ accordion row. A frequently-asked-questions row near the foot of a topic page (a details/summary or button accordion). Measured at rest and opened by its own toggle.

Page: meditation. Selector: `details, [class*="accordion" i] button, [class*="faq" i] button`. States: .

Not found on the page at capture time.

#### subscribe-button

"Subscribe" button. The subscribe action on a plan/upsell card, measured, never pressed.

Page: content. Selector: `button/a (text Subscribe)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 151 x 57.8 | = | = | - |
| Padding | 16px 32px | = | = | - |
| Border | 2px solid #000000 @ 0 | = | = | - |
| Radius | 32px | = | = | - |
| Background | #2d2c2b | #141313 | #141313 | - |
| Box shadow | #413d45 @ 0.2 0px 2px 0px 0px | = | = | - |
| Outline | none | = | 2px solid #0040ea offset 0px | - |
| Font | Headspace Apercu 18px/19.8px 700 | = | = | - |
| Letter spacing | normal | = | = | - |
| Colour | #ffffff | = | = | - |
| Text node | span.css-1ss1hc4: Headspace Apercu 18px/19.8px 700, #ffffff | = | = | - |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = | = | - |
| Cursor | pointer | = | = | - |
| Painted layers | button.css-pifwmv 151.0x57.8 bg #2d2c2b border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px | button.css-pifwmv 151.0x57.8 bg #141313 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px | button.css-pifwmv 151.0x57.8 bg #141313 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px outline 2px solid #0040ea offset 0px | - |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | - |
| Error | - | = | = | cdpSession.send: Protocol error (DOM.getNodeForLocation): No node found at given location |

Crops: `subscribe-button-default.png`, `subscribe-button-hover.png`, `subscribe-button-focus-visible.png`.

#### content-tile

Content preview tile. A meditation/music/sleep preview tile on /content. Never played.

Page: content. Selector: `main [class*="card" i], main article, main [class*="tile" i]`. States: .

Not found on the page at capture time.

#### play-button

Preview play button. A play control on a preview tile or audio row. Never pressed — previews were not played.

Page: content. Selector: `button[aria-label*="play" i], [class*="play" i] button`. States: .

Not found on the page at capture time.

#### plan-card

Plan card. A subscription plan card on /subscriptions (radius 12, cream fill).

Page: subscriptions. Selector: `main [class*="card" i], main li`. States: .

Not found on the page at capture time.

#### plan-switch

Billing switch. The monthly/annual switch control on /subscriptions (role switch or checkbox name="switch"), measured at rest — never toggled.

Page: subscriptions. Selector: `input[name="switch"], [role="switch"]`. States: .

Not found on the page at capture time.

#### plan-slider

Seat slider. A range input on the plans page (member-count slider), measured at rest — never dragged.

Page: subscriptions. Selector: `input[type="range"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 406.47 x 8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #9d968e |
| Transition | none |
| Opacity | 0 |
| Cursor | pointer |
| Placeholder | #9d968e, opacity 1 |
| Painted layers | input.css-gc0072 406.5x8.0 bg #ffffff |
| How | resting state |

Crops: `plan-slider-default.png`.

### Forms

#### newsletter-field

Newsletter email field. The footer's email input, clicked into — nothing typed.

Page: home. Selector: `input[type="email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 281 x 58 | = |
| Padding | 24px 16px 8px 16px | = |
| Border | 1px solid #d2d5de | = |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #101010 offset 0px |
| Font | Headspace Apercu 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input.css-onqfi8 281.0x58.0 bg #ffffff border T:1px solid #d2d5de / R:1px solid #d2d5de / B:1px solid #d2d5de / L:1px solid #d2d5de r 8px | input.css-onqfi8 281.0x58.0 bg #ffffff border T:1px solid #d2d5de / R:1px solid #d2d5de / B:1px solid #d2d5de / L:1px solid #d2d5de r 8px outline 1px auto #101010 offset 0px |
| How | resting state | the field clicked into — nothing typed |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`.

#### redeem-field

Redeem-code field. The "Enter your code" text input on /code, clicked into — nothing typed.

Page: redeem. Selector: `input[name="Redeem Field"], input[placeholder*="code" i]`. States: default, focused, focus-visible.

| Property | default | focused | focus-visible |
|---|---|---|---|
| Size (w x h) | 344 x 50 | = | = |
| Padding | 12px 32px 12px 12px | = | = |
| Border | none | = | = |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | 1px auto #101010 offset 0px | 1px auto #101010 offset 0px |
| Font | Headspace Apercu 18px/26px 500 | = | = |
| Letter spacing | -0.18px | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 0.7 | = | = |
| Painted layers | input.css-1stc5ub 344.0x50.0 bg #ffffff r 4px | input.css-1stc5ub 344.0x50.0 bg #ffffff r 4px outline 1px auto #101010 offset 0px | input.css-1stc5ub 344.0x50.0 bg #ffffff r 4px outline 1px auto #101010 offset 0px |
| How | resting state | the field clicked into — nothing typed | keyboard focus (Shift+Tab, Tab) |

Crops: `redeem-field-default.png`, `redeem-field-focused.png`, `redeem-field-focus-visible.png`.

#### redeem-button

"Redeem code" button. The submit on /code, measured, never pressed.

Page: redeem. Selector: `button (text Redeem)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 165 x 52 | = | = |
| Padding | 14px 32px | = | = |
| Border | none | = | = |
| Radius | 32px | = | = |
| Background | #0061ef | #0040ea | #0040ea |
| Box shadow | #413d45 @ 0.2 0px 2px 0px 0px | = | = |
| Outline | none | = | 2px solid #0040ea offset 0px |
| Font | Headspace Apercu 16px/17.6px 700 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.css-1ss1hc4: Headspace Apercu 16px/17.6px 700, #ffffff | = | = |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.css-fmb5k8 165.0x52.0 bg #0061ef r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px | button.css-fmb5k8 165.0x52.0 bg #0040ea r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px | button.css-fmb5k8 165.0x52.0 bg #0040ea r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px outline 2px solid #0040ea offset 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `redeem-button-default.png`, `redeem-button-hover.png`, `redeem-button-focus-visible.png`.

### Auth surface

#### auth-card

Auth card. The centred card on auth.headspace.com (the universal login).

Page: signup. Selector: `main, [class*="widget" i], form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 870.39 |
| Padding | 48px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MyCustomFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e212a |
| Text node | h1.css-1105om2: Headspace Apercu 24px/28.8px 700, #1e212a, ls -0.72px |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | div.bg-card.text-card-foreground 400.0x774.4 bg #ffffff r 32px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 12px 40px 0px; div.css-ikm396 336.0x56.0 bg #ffffff border T:2px solid #e2ded9 / R:2px solid #e2ded9 / B:2px solid #e2ded9 / L:2px solid #e2ded9 r 12px; button.!w-full.!max-w-full 336.0x48.0 bg #0061ef border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px; div.flex-grow.border-t 153.5x1.0 border T:1px solid #c9cace; div.flex-grow.border-t 153.5x1.0 border T:1px solid #c9cace; button.focus-visible:ring-ring.aria-invalid:ring-destructive/20 75.8x44.0 bg #4678e3 r 3.35544e+07px |
| Ancestor paint | 1 up div.relative.flex bg #f9f4f2 |
| How | resting state |

Crops: none.

#### auth-email

Email field. The email input on the universal login, clicked into — nothing typed.

Page: signup. Selector: `input[type="email"], input[name="username"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 300 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | MyCustomFont 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #2d2c2b | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #2d2c2b, opacity 1 | = |
| Ancestor paint | 1 up div.css-ikm396 bg #ffffff | = |
| How | resting state | the field clicked into — nothing typed |

Crops: `auth-email-default.png`, `auth-email-focused.png`.

#### auth-continue

"Continue" button. The primary submit on the universal login, measured, never pressed.

Page: login. Selector: `button (text Continue)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 336 x 48 | = | = |
| Padding | 13.2px 24px | = | = |
| Border | 2px solid #000000 @ 0 | = | = |
| Radius | 32px | = | = |
| Background | #0061ef | #0040ea | #0040ea |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #0040ea offset 2px |
| Font | MyCustomFont 16px/17.6px 700 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.css-1ss1hc4: MyCustomFont 16px/17.6px 700, #ffffff | = | = |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.!w-full.!max-w-full 336.0x48.0 bg #0061ef border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px | button.!w-full.!max-w-full 336.0x48.0 bg #0040ea border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px | button.!w-full.!max-w-full 336.0x48.0 bg #0040ea border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px outline 2px solid #0040ea offset 2px |
| Ancestor paint | 3 up div.bg-card.text-card-foreground bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 12px 40px 0px | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `auth-continue-default.png`, `auth-continue-hover.png`, `auth-continue-focus-visible.png`.

#### auth-sso

"Continue with SSO" button. The secondary SSO submit, measured, never pressed.

Page: login. Selector: `button (text SSO)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 336 x 48 | = |
| Padding | 13.2px 24px | = |
| Border | 2px solid #000000 @ 0 | = |
| Radius | 32px | = |
| Background | #f9f4f2 | #e5e7ec |
| Box shadow | none | = |
| Outline | none | = |
| Font | MyCustomFont 16px/17.6px 700 | = |
| Letter spacing | normal | = |
| Colour | #44423f | = |
| Text node | span.flex.items-center: MyCustomFont 16px/17.6px 700, #44423f | = |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #44423f | = |
| Painted layers | button.css-16j8mil 336.0x48.0 bg #f9f4f2 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px | button.css-16j8mil 336.0x48.0 bg #e5e7ec border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px |
| Ancestor paint | 2 up div.bg-card.text-card-foreground bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.12 0px 12px 40px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `auth-sso-default.png`, `auth-sso-hover.png`.

### Checkout

#### checkout-form

Checkout panel. The self-serve checkout surface (plan picker or payment form) as it paints without a voucher — viewed only, nothing filled or submitted.

Page: checkout. Selector: `main, form`. States: .

Not found on the page at capture time.

#### checkout-field

Checkout field. An input on the checkout surface (email or plan option), measured at rest.

Page: checkout. Selector: `main input`. States: .

Not found on the page at capture time.

#### checkout-button

Checkout button. The primary action on the checkout surface, measured, never pressed.

Page: checkout. Selector: `main button`. States: .

Not found on the page at capture time.

### B2B surface

#### org-h1

B2B hero headline. The organizations.headspace.com hero h1.

Page: org-employers. Selector: `main h1, h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 624 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | HS Apercu Bold 48px/48px 700 |
| Letter spacing | -1px |
| Colour | #ffffff |
| Transition | none |
| How | resting state |

Crops: `org-h1-default.png`.

#### org-cta

B2B CTA. The business-surface call-to-action ("Request a demo" / "Get started"), measured, never followed.

Page: org-employers. Selector: `a/button (text demo/Get started/Contact)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 183 x 50.16 | = | = |
| Padding | 14.08px 32px | = | = |
| Border | 1px solid #ffffff | 1px solid #ff7e1d | = |
| Radius | 800px | = | = |
| Background | #ffffff | #ff7e1d | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px solid #000000 offset 5px |
| Font | HS Apercu Medium 16px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2d2c2b | #ffffff | = |
| Transition | all 0.2s ease | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.button.is-white 183.0x50.2 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 800px | a.button.is-white 183.0x50.2 bg #ff7e1d border T:1px solid #ff7e1d / R:1px solid #ff7e1d / B:1px solid #ff7e1d / L:1px solid #ff7e1d r 800px | a.button.is-white 183.0x50.2 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 800px outline 1px solid #000000 offset 5px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `org-cta-default.png`, `org-cta-hover.png`, `org-cta-focus-visible.png`.

#### org-card

B2B card. A card on the B2B surface (stat, benefit or customer logo tile).

Page: org-home. Selector: `main [class*="card" i], main article`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 340 x 430 |
| Padding | 32px 40px |
| Gap | 96px |
| Border | none |
| Radius | 8px |
| Background | #ffce00 |
| Box shadow | none |
| Outline | none |
| Font | system-ui 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.heading-style-small.ver-two: HS Apercu Bold 14px/21px 700, #2d2c2b, ls 0.84px |
| Transition | none |
| Painted layers | div.outcomes-slider_cms_card 340.0x430.0 bg #ffce00 r 8px |
| How | resting state |

Crops: `org-card-default.png`.

### Marketing chrome (mobile)

#### m-nav-header

Mobile header. The bar at 390px: logo and the nav button.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Headspace Apercu 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #4b4c4d |
| Text node | span.css-1fvtd4u: Headspace Apercu 14px/15.4px 700, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #2d2c2b |
| Painted layers | header.css-75xqdg 390.0x64.0 bg #ffffff; dialog.css-1rhcoa3 0.0x0.0 bg #ffffff r 0px 0px 24px 24px shadow #141313 @ 0.2 0px 1px 8px 0px; div.css-15t8m5e 0.0x0.0 bg #f9f4f2 r 24px; div.css-1gr7t27 0.0x0.0 bg #0061ef r 24px 24px 0px 0px; dialog.css-1rhcoa3 0.0x0.0 bg #ffffff r 0px 0px 24px 24px shadow #141313 @ 0.2 0px 1px 8px 0px; div.css-15t8m5e 0.0x0.0 bg #f9f4f2 r 24px |
| How | resting state |

Crops: `m-nav-header-default.png`.

#### m-nav-button

Nav button. The button that opens the nav sheet.

Page: home. Selector: `header button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 28 x 28 | = |
| Padding | 0px | = |
| Border | 2px solid #000000 @ 0 | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Headspace Apercu 16px/17.6px 700 | = |
| Letter spacing | normal | = |
| Colour | #44423f | = |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #44423f | = |
| Painted layers | button.css-v74ccp 28.0x28.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 | = |
| How | resting state | mouse hover over the element |

Crops: `m-nav-button-default.png`, `m-nav-button-hover.png`.

#### m-nav-sheet

Nav sheet (open). The opened navigation sheet. The nav button's own press happens in find(); the state itself is a no-op.

Page: home. Selector: `header nav sheet`. States: .

Not found on the page at capture time.

### Marketing widgets (mobile)

#### m-hero-cta

Mobile hero CTA. The hero call-to-action at 390px, measured, never followed.

Page: home. Selector: `main a/button (text Get 50% off/Get started)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 125 x 32.59 |
| Padding | 14.3px 24px |
| Border | 2px solid #000000 @ 0 |
| Radius | 32px |
| Background | #0061ef |
| Box shadow | #413d45 @ 0.2 0px 2px 0px 0px |
| Outline | none |
| Font | Headspace Apercu 14px/15.4px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.css-1fvtd4u: Headspace Apercu 14px/15.4px 700, #ffffff |
| Transition | color, background-color, border-color, box-shadow, transform 0.15s, 0.15s, 0.15s, 0.15s, 0.15s cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1), cubic-bezier(0.32, 0.94, 0.6, 1) delay 0s, 0s, 0s, 0s, 0s |
| Cursor | pointer |
| Painted layers | a.css-11fbkag 125.0x32.6 bg #0061ef border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 32px shadow #413d45 @ 0.2 0px 2px 0px 0px |
| How | resting state |

Crops: `m-hero-cta-default.png`.

## Transitions declared in the readable stylesheets

Headspace compiles its CSS to generated Emotion classes inline, so this list holds what the CSSOM could read on each page; the per-state Transition rows above are computed values and cover the site's own rules.

- about: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- anxiety: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `opacity 0.3s ease-in-out`, `opacity 400ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 400ms cubic-bezier(0.32, `, `border 0.3s`, `0.3s`, `0.1s`

- app: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `opacity 400ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 400ms cubic-bezier(0.32, `, `border 0.3s`, `0.3s`, `0.1s`

- article: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `0.3s`, `box-shadow 0.1s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- articles: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `box-shadow 0.1s`, `transform ease-out`, `transform 100ms ease-out`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- checkout: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- coaching: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `opacity 400ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 400ms cubic-bezier(0.32, `, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- content: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `border-bottom 0.2s ease-in-out`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- ebb: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `opacity 0.3s ease-in-out`, `opacity 400ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 400ms cubic-bezier(0.32, `, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- family: `opacity 0.3s, height 0.3s, background-position 0.3s`, `0.2s ease-in-out`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`, `background-color 0.3s`

- gift: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- home: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `border 0.3s`, `0.3s`

- login: `border-color 0.15s`, `font-size 0.15s, top 0.15s, transform 0.15s`, `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`

- meditation: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `transform ease-out`, `transform 100ms ease-out`, `box-shadow 0.1s`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`

- mental-health: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `transform ease-out`, `transform 100ms ease-out`, `box-shadow 0.1s`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- mindful-families: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `opacity 400ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 400ms cubic-bezier(0.32, `, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- org-employers: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `color 0.2s, background-color 0.2s`, `opacity 0.2s`, `2s ease-out`, `transform 0.2s`, `color 0.2s`, `0.4ms`

- org-home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `color 0.2s, background-color 0.2s`, `opacity 0.2s`, `2s ease-out`, `transform 0.2s`, `color 0.2s`, `0.4ms`

- redeem: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- science: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `opacity 0.1s 0.3s`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- share: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `box-shadow 0.1s`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`

- signup: `border-color 0.15s`, `font-size 0.15s, top 0.15s, transform 0.15s`, `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`

- sleep: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `transform ease-out`, `transform 100ms ease-out`, `box-shadow 0.1s`, `0.3s`, `0.1s`

- subscriptions: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `transform ease-out`, `transform 100ms ease-out`, `opacity 500ms, top 500ms`, `0.3s`

- therapy: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `opacity 0.3s ease-in-out`, `opacity 400ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 400ms cubic-bezier(0.32, `, `0.3s`

- topic: `color 150ms cubic-bezier(0.32, 0.94, 0.6, 1), background-color 150ms cubic-bezier(0.32, 0.`, `box-shadow 0.1s`, `0.3s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`
