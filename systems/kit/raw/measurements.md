# Component measurements

Computed styles read from kit.com and app.kit.com/users/login on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Announcement bar

#### announce-bar

Announcement bar. The blue announcement strip above the nav ("See Kit’s newest features in action"). Measured, never followed.

Page: home. Selector: `announcement strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 48 |
| Padding | 8px 16px |
| Border | none |
| Radius | 0px |
| Background | #44b1ff |
| Box shadow | none |
| Outline | none |
| Font | Libre Franklin 16px/24px 400 |
| Letter spacing | -0.16px |
| Colour | #1e1e1e |
| Text node | span.font-semibold.text-soft-black: Libre Franklin 14px/21px 600, #1e1e1e, ls -0.14px |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.hidden.w-full 1440.0x48.0 bg #44b1ff; a.font-sans.transition-all 110.0x32.0 bg #1e1e1e r 8px |
| How | at rest |

Crops: `announce-bar-default.png`.

### Site chrome

#### mega-nav

Site nav. The fixed #mega-nav: wordmark, Features / Use Cases / Resources menus, Pricing, Log in, Request a demo, and the blue Start free trial pill.

Page: home. Selector: `#mega-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 58 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Libre Franklin 16px/24px 400 |
| Letter spacing | -0.16px |
| Colour | #1e1e1e |
| Text node | span.px-1: Libre Franklin 14px/24.003px 600, #f2efe9, ls -0.14px |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 53 x 24.53, colour #1e1e1e |
| Painted layers | a.font-sans.transition-all 131.1x34.0 border T:1px solid #f2efe9 / R:1px solid #f2efe9 / B:1px solid #f2efe9 / L:1px solid #f2efe9 r 8px; a.font-sans.transition-all 115.8x32.0 bg #44b1ff r 8px; span 0.0x0.0 bg #ffffff; span::before 100%x2px bg #ffffff r 999px; span::after 100%x2px bg #ffffff r 999px; span 0.0x0.0 bg #ffffff |
| Ancestor paint | 1 up div.relative.min-h-screen bg #ffffff |
| How | at rest |

Crops: `mega-nav-default.png`.

#### nav-logo

Wordmark. The Kit wordmark linking home.

Page: home. Selector: `#mega-nav a[href=/]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 53 x 24.53 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Libre Franklin 16px/24px 400 |
| Letter spacing | -0.16px |
| Colour | #1e1e1e |
| Transition | none |
| Cursor | pointer |
| Icon | 53 x 24.53, colour #1e1e1e |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-menu

Nav menu button. The Features button (aria-haspopup) that opens the mega menu. The opened state was measured after clicking it. Menu links were never followed.

Page: home. Selector: `#mega-nav button Features`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 105.23 x 32 | = | = | = | = |
| Padding | 4px 8px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #f2efe9 @ 0.08 | #f2efe9 @ 0.08 | #f2efe9 @ 0.08 | #1e1e1e @ 0.08 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | Libre Franklin 14px/24.003px 600 | = | = | = | = |
| Letter spacing | -0.14px | = | = | = | = |
| Colour | #f2efe9 | = | = | = | #1e1e1e |
| Text node | span.px-1: Libre Franklin 14px/24.003px 600, #f2efe9, ls -0.14px | = | = | = | span.px-1: Libre Franklin 14px/24.003px 600, #1e1e1e, ls -0.14px |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | default | = | = | = | = |
| Icon | 20 x 20, colour #f2efe9 | = | = | = | 20 x 20, colour #1e1e1e |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.font-sans.transition-all 105.2x32.0 bg #f2efe9 @ 0.08 r 8px | button.font-sans.transition-all 105.2x32.0 bg #f2efe9 @ 0.08 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.font-sans.transition-all 105.2x32.0 bg #f2efe9 @ 0.08 r 8px | button.font-sans.transition-all 105.2x32.0 bg #1e1e1e @ 0.08 r 8px |

Crops: `nav-menu-default.png`, `nav-menu-hover.png`, `nav-menu-focus-visible.png`, `nav-menu-pressed.png`, `nav-menu-opened.png`.

#### nav-panel

Nav menu panel. The panel opened by Features. Its links were never followed.

Page: home. Selector: `Features panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 287.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Outline | none |
| Font | Libre Franklin 16px/24px 400 |
| Letter spacing | -0.16px |
| Colour | #1e1e1e |
| Text node | span.text-sm.font-semibold: Libre Franklin 14px/20px 600, #1e1e1e, ls -0.16px |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 24 x 24, colour #1e1e1e |
| Painted layers | div.absolute.left-0 1440.0x287.9 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; div.order-6.rounded-2xl 176.0x231.9 bg #1e1e1e @ 0.06 r 16px; a.font-sans.transition-all 118.6x32.0 bg #1e1e1e r 8px; a.font-sans.transition-all 158.4x40.0 bg #1e1e1e @ 0.08 r 10px; a.font-sans.transition-all 142.5x40.0 bg #1e1e1e @ 0.08 r 10px |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-link

Nav link. The Pricing link in the nav. Measured, never followed.

Page: home. Selector: `#mega-nav a[href=/pricing]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70.48 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f2efe9 @ 0.08 | #f2efe9 @ 0.08 | #f2efe9 @ 0.08 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Libre Franklin 14px/24.003px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #f2efe9 | = | = | = |
| Text node | span.px-1: Libre Franklin 14px/24.003px 600, #f2efe9, ls -0.14px | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.font-sans.transition-all 70.5x32.0 bg #f2efe9 @ 0.08 r 8px | a.font-sans.transition-all 70.5x32.0 bg #f2efe9 @ 0.08 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.font-sans.transition-all 70.5x32.0 bg #f2efe9 @ 0.08 r 8px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in link. The Log in link to app.kit.com. Measured, never followed.

Page: home. Selector: `#mega-nav login link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 63.38 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f2efe9 @ 0.08 | #f2efe9 @ 0.08 | #f2efe9 @ 0.08 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Libre Franklin 14px/24.003px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #f2efe9 | = | = | = |
| Text node | span.px-1: Libre Franklin 14px/24.003px 600, #f2efe9, ls -0.14px | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.font-sans.transition-all 63.4x32.0 bg #f2efe9 @ 0.08 r 8px | a.font-sans.transition-all 63.4x32.0 bg #f2efe9 @ 0.08 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.font-sans.transition-all 63.4x32.0 bg #f2efe9 @ 0.08 r 8px |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-trial

Start free trial. The blue Start free trial pill. Measured, never followed.

Page: home. Selector: `#mega-nav Start free trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115.8 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #44b1ff | #a2d1f1 | = | #a2d1f1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Libre Franklin 14px/24.003px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.px-1: Libre Franklin 14px/24.003px 600, #1e1e1e, ls -0.14px | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-sans.transition-all 115.8x32.0 bg #44b1ff r 8px | a.font-sans.transition-all 115.8x32.0 bg #a2d1f1 r 8px | a.font-sans.transition-all 115.8x32.0 bg #44b1ff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.font-sans.transition-all 115.8x32.0 bg #a2d1f1 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-trial-default.png`, `nav-trial-hover.png`, `nav-trial-focus-visible.png`, `nav-trial-pressed.png`.

### Home

#### hero-h1

Hero headline. The home masthead, set in KitSansFont on the dark hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 152 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | KitSansFont 80px/76px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. A Start free trial button. Measured, never followed.

Page: home. Selector: `Start free trial link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115.8 x 32 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #44b1ff | #a2d1f1 | = | #a2d1f1 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Libre Franklin 14px/24.003px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.px-1: Libre Franklin 14px/24.003px 600, #1e1e1e, ls -0.14px | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-sans.transition-all 115.8x32.0 bg #44b1ff r 8px | a.font-sans.transition-all 115.8x32.0 bg #a2d1f1 r 8px | a.font-sans.transition-all 115.8x32.0 bg #44b1ff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.font-sans.transition-all 115.8x32.0 bg #a2d1f1 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-secondary

Request demo button. The Request demo button. Measured, never followed. The demo form sits behind a Chili Piper embed and was not submitted.

Page: home. Selector: `Request demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.61 x 32 | = | - | = |
| Padding | 4px 8px | = | - | = |
| Gap | 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | #1e1e1e | = | - | #3d3d3d |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Libre Franklin 14px/24.003px 600 | = | - | = |
| Letter spacing | -0.14px | = | - | = |
| Colour | #f2efe9 | = | - | = |
| Text node | span.px-1: Libre Franklin 14px/24.003px 600, #f2efe9, ls -0.14px | = | - | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.font-sans.transition-all 118.6x32.0 bg #1e1e1e r 8px | = | - | a.font-sans.transition-all 118.6x32.0 bg #3d3d3d r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `hero-secondary-default.png`, `hero-secondary-hover.png`, `hero-secondary-pressed.png`.

### Footer

#### footer

Footer. The page footer: sitemap columns and legal links, including the published help@kit.com address.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1177 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Libre Franklin 16px/24px 400 |
| Letter spacing | -0.16px |
| Colour | #1e1e1e |
| Text node | a.transition-colors.duration-100: Libre Franklin 16px/24px 600, #ffffff, ls -0.16px |
| Transition | none |
| Icon | 106 x 49.06, colour #ffffff |
| Painted layers | section.relative.bg-soft-black 1440.0x1010.0 bg #1e1e1e; a.font-sans.transition-all 145.2x48.0 bg #44b1ff r 12px; section.relative.bg-soft-black 1440.0x167.0 bg #1e1e1e |
| Ancestor paint | 1 up div.relative.min-h-screen bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link. Measured, never followed.

Page: home. Selector: `footer a[href=/pricing]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.77 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Libre Franklin 14px/20px 400 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #ffffff | #6e6e6e | #6e6e6e | #6e6e6e |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.relative.text-sm 44.8x17.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

### Pricing

#### price-h1

Pricing headline. The /pricing masthead, "Pricing and plans".

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1312 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | KitSansFont 64px/64px 500 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-cta

Plan trial button. A plan card "Start 14-day free trial" link. Measured, never followed.

Page: pricing. Selector: `pricing 14-day free trial`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 394.67 x 48 | = | = | = |
| Padding | 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #1e1e1e @ 0.08 | #1e1e1e @ 0.16 | #1e1e1e @ 0.16 | #1e1e1e @ 0.16 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Libre Franklin 16px/16px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.px-1: Libre Franklin 16px/16px 600, #1e1e1e, ls -0.14px | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-sans.transition-all 394.7x48.0 bg #1e1e1e @ 0.08 r 12px | a.font-sans.transition-all 394.7x48.0 bg #1e1e1e @ 0.16 r 12px | a.font-sans.transition-all 394.7x48.0 bg #1e1e1e @ 0.16 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.font-sans.transition-all 394.7x48.0 bg #1e1e1e @ 0.16 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-cta-default.png`, `price-cta-hover.png`, `price-cta-focus-visible.png`, `price-cta-pressed.png`.

#### price-free

Sign up free. The Free plan Sign up free link. Measured, never followed.

Page: pricing. Selector: `pricing Sign up free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 242.55 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #1e1e1e @ 0.08 | #1e1e1e @ 0.16 | #1e1e1e @ 0.16 | #1e1e1e @ 0.16 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Libre Franklin 14px/40.012px 600 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | span.px-1: Libre Franklin 14px/40.012px 600, #1e1e1e, ls -0.14px | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.font-sans.transition-all 242.5x40.0 bg #1e1e1e @ 0.08 r 10px | a.font-sans.transition-all 242.5x40.0 bg #1e1e1e @ 0.16 r 10px | a.font-sans.transition-all 242.5x40.0 bg #1e1e1e @ 0.16 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #44b1ff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.font-sans.transition-all 242.5x40.0 bg #1e1e1e @ 0.16 r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-free-default.png`, `price-free-hover.png`, `price-free-focus-visible.png`, `price-free-pressed.png`.

#### faq-summary

FAQ summary. A pricing FAQ disclosure. Opened locally; nothing was submitted.

Page: pricing. Selector: `pricing summary`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 752 x 83 | = |
| Padding | 28px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Libre Franklin 16px/24px 400 | = |
| Letter spacing | -0.16px | = |
| Colour | #1e1e1e | = |
| Text node | span.text-4.5.flex-1: Libre Franklin 18px/27px 600, #1e1e1e, ls -0.16px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 24 x 24, colour #1e1e1e | = |
| How | at rest | own toggle |

Crops: `faq-summary-default.png`, `faq-summary-opened.png`.

### Features

#### feat-h1

Features headline. The /features masthead.

Page: features. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 748.42 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | KitSansFont 64px/64px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `feat-h1-default.png`.

#### feat-search

Feature search. The feature explorer search field. Focused and typed into, then cleared. Nothing was submitted.

Page: features. Selector: `#feature-explorer-search`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 976 x 45 | = | = |
| Padding | 8px 8px 8px 48px | = | = |
| Border | 1px solid #e3e3e3 | = | = |
| Radius | 8px | = | = |
| Background | #f7f7f7 | = | = |
| Box shadow | none | = | = |
| Outline | none | 1px auto #1e1e1e offset 0px | 1px auto #1e1e1e offset 0px |
| Font | Libre Franklin 18px/27px 400 | = | = |
| Letter spacing | -0.16px | = | = |
| Colour | #1e1e1e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #b8b8b8, opacity 1 | = | = |
| Painted layers | input.w-full.rounded-lg 976.0x45.0 bg #f7f7f7 border T:1px solid #e3e3e3 / R:1px solid #e3e3e3 / B:1px solid #e3e3e3 / L:1px solid #e3e3e3 r 8px | input.w-full.rounded-lg 976.0x45.0 bg #f7f7f7 border T:1px solid #e3e3e3 / R:1px solid #e3e3e3 / B:1px solid #e3e3e3 / L:1px solid #e3e3e3 r 8px outline 1px auto #1e1e1e offset 0px | input.w-full.rounded-lg 976.0x45.0 bg #f7f7f7 border T:1px solid #e3e3e3 / R:1px solid #e3e3e3 / B:1px solid #e3e3e3 / L:1px solid #e3e3e3 r 8px outline 1px auto #1e1e1e offset 0px |
| How | at rest | clicked into the field | typed "sponsorships", then deleted; nothing sent |

Crops: `feat-search-default.png`, `feat-search-focused.png`. The filled crop was not stored.

### Compare

#### compare-h1

Compare headline. The Kit vs Mailchimp masthead.

Page: compare. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 632 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | KitSansFont 64px/64px 500 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `compare-h1-default.png`.

#### compare-table

Comparison table. The feature comparison table on /compare/mailchimp.

Page: compare. Selector: `table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1312 x 3567 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Libre Franklin 16px/24px 400 |
| Letter spacing | -0.16px |
| Colour | #1e1e1e |
| Text node | h6.text-5.leading-[1.25]: Libre Franklin 20px/25px 700, #1e1e1e, ls -0.16px |
| Transition | none |
| Icon | 24 x 24, colour #1e1e1e |
| Painted layers | th.hidden.xs:block 437.3x74.0 bg #ffffff border B:1px solid #d4d4d4; th.sticky.top-12 437.3x74.0 bg #ffffff border B:1px solid #d4d4d4 / L:1px solid #d4d4d4; th.sticky.top-12 437.3x74.0 bg #ffffff border B:1px solid #d4d4d4 / L:1px solid #d4d4d4; td.col-span-full.border-b 1312.0x74.0 bg #f2efe9 @ 0.5 border B:1px solid #1e1e1e; th.col-span-2.xs:col-span-1 437.3x57.0 bg #f2efe9 @ 0.3 border B:1px solid #d4d4d4; td.flex.items-center 437.3x57.0 border B:1px solid #d4d4d4 / L:1px solid #d4d4d4 |
| How | at rest |

Crops: `compare-table-default.png`.

### App log-in

#### login-panel

Log-in card. The signed-out log-in card on app.kit.com/users/login. A separate app from the marketing site. Nothing was submitted.

Page: login. Selector: `login card`. States: .

Not found on the page at capture time.

#### login-email

Email field. The Email field. Focused and typed into with a placeholder address, then cleared. Nothing was submitted.

Page: login. Selector: `input[name=user[email]]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 470 x 40 | = | = |
| Padding | 8px 12px | = | = |
| Border | none | = | = |
| Radius | 10px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #d4d4d4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #c4c4c4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #c4c4c4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | 2px solid #000000 @ 0 offset 2px | 2px solid #1e1e1e offset 2px | 2px solid #1e1e1e offset 2px |
| Font | Inter 14px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1e1e1e | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #919191, opacity 1 | = | = |
| Painted layers | input.w-full.min-w-0 470.0x40.0 bg #ffffff r 10px shadow #000000 @ 0 0px 0px 0px 0px, #d4d4d4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.w-full.min-w-0 470.0x40.0 bg #ffffff r 10px shadow #000000 @ 0 0px 0px 0px 0px, #c4c4c4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #1e1e1e offset 2px | input.w-full.min-w-0 470.0x40.0 bg #ffffff r 10px shadow #000000 @ 0 0px 0px 0px 0px, #c4c4c4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #1e1e1e offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`. Focused and filled crops were not stored. The empty field paints an email placeholder, and the image scan treats any address as personal data.

#### login-password

Password field. The Password field. Focused and typed into, then cleared. Nothing was submitted.

Page: login. Selector: `input[name=user[password]]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 414 x 40 | = | = |
| Padding | 8px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1e1e1e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #919191, opacity 1 | = | = |
| Ancestor paint | 1 up div.flex.w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #d4d4d4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 | 1 up div.flex.w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #c4c4c4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #1e1e1e | 1 up div.flex.w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #c4c4c4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #1e1e1e |
| How | at rest | clicked into the field | typed "not-a-real-password", then deleted; nothing sent |

Crops: `login-password-default.png`. Focused and filled crops were not stored, for the same reason as the email field.

#### login-show

Show password. The Show password control. Measured, never used to reveal a real password.

Page: login. Selector: `Show password`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 4px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #1e1e1e @ 0.06 | = | #1e1e1e @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #1e1e1e offset 2px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #3d3d3d | = | = | = |
| Painted layers | button.shrink-0.group/button 32.0x32.0 r 8px outline 2px solid #000000 @ 0 offset 2px | button.shrink-0.group/button 32.0x32.0 bg #1e1e1e @ 0.06 r 8px outline 2px solid #000000 @ 0 offset 2px | button.shrink-0.group/button 32.0x32.0 r 8px outline 2px solid #1e1e1e offset 2px | button.shrink-0.group/button 32.0x32.0 bg #1e1e1e @ 0.06 r 8px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 2 up div.flex.w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #d4d4d4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 | 2 up div.flex.w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #c4c4c4 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-show-default.png`, `login-show-hover.png`, `login-show-focus-visible.png`, `login-show-pressed.png`.

#### login-remember

Remember me. The Keep me logged in checkbox. Measured at rest, never toggled into a session.

Page: login. Selector: `input[name=user[remember_me]]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1 x 1 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/normal 400 |
| Letter spacing | normal |
| Colour | #3d3d3d |
| Transition | none |
| Cursor | default |
| Placeholder | #3d3d3d, opacity 1 |
| How | at rest |

Crops: `login-remember-default.png`.

#### login-submit

Log in submit. The Log in submit. States were measured. The button was never clicked.

Page: login. Selector: `login submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 470 x 48 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #1e1e1e | #3d3d3d | = | #3d3d3d |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #1e1e1e offset 2px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.shrink-0.group/button 470.0x48.0 bg #1e1e1e r 12px outline 2px solid #000000 @ 0 offset 2px | button.shrink-0.group/button 470.0x48.0 bg #3d3d3d r 12px outline 2px solid #000000 @ 0 offset 2px | button.shrink-0.group/button 470.0x48.0 bg #1e1e1e r 12px outline 2px solid #1e1e1e offset 2px | button.shrink-0.group/button 470.0x48.0 bg #3d3d3d r 12px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-forgot

Forgot password. The I forgot my password link. Measured, never followed.

Page: login. Selector: `forgot password link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 470 x 48 | = | = | = |
| Padding | 12px 20px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #1e1e1e @ 0.06 | = | #1e1e1e @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #1e1e1e offset 2px | = |
| Font | Inter 14px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.shrink-0.group/button 470.0x48.0 r 12px outline 2px solid #000000 @ 0 offset 2px | a.shrink-0.group/button 470.0x48.0 bg #1e1e1e @ 0.06 r 12px outline 2px solid #000000 @ 0 offset 2px | a.shrink-0.group/button 470.0x48.0 r 12px outline 2px solid #1e1e1e offset 2px | a.shrink-0.group/button 470.0x48.0 bg #1e1e1e @ 0.06 r 12px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-forgot-default.png`, `login-forgot-hover.png`, `login-forgot-focus-visible.png`, `login-forgot-pressed.png`.

#### login-create

Create account. The Create account link. Signup is Cloudflare-gated and was not followed.

Page: login. Selector: `Create account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 235 x 38 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #e3e3e3; L: none | T: none; R: none; B: 1px solid #b8b8b8; L: none | = | T: none; R: none; B: 1px solid #b8b8b8; L: none |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #1e1e1e offset -2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3d3d3d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hover:border-gray-500.hover:no-underline 235.0x38.0 border B:1px solid #e3e3e3 outline 2px solid #000000 @ 0 offset 0px | a.hover:border-gray-500.hover:no-underline 235.0x38.0 border B:1px solid #b8b8b8 outline 2px solid #000000 @ 0 offset 0px | a.hover:border-gray-500.hover:no-underline 235.0x38.0 border B:1px solid #e3e3e3 outline 2px solid #1e1e1e offset -2px | a.hover:border-gray-500.hover:no-underline 235.0x38.0 border B:1px solid #b8b8b8 outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-create-default.png`, `login-create-hover.png`, `login-create-focus-visible.png`, `login-create-pressed.png`.

### Mobile (390 wide)

#### m-nav

Mobile nav. The phone nav bar.

Page: mobile. Selector: `mobile #mega-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Libre Franklin 16px/24px 400 |
| Letter spacing | -0.16px |
| Colour | #1e1e1e |
| Text node | span.px-1: Libre Franklin 14px/24.003px 600, #1e1e1e, ls -0.14px |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 53 x 24.53, colour #1e1e1e |
| Painted layers | a.font-sans.transition-all 0.0x0.0 border T:1px solid #f2efe9 / R:1px solid #f2efe9 / B:1px solid #f2efe9 / L:1px solid #f2efe9 r 8px; a.font-sans.transition-all 115.8x32.0 bg #44b1ff r 8px; span 20.0x2.0 bg #ffffff; span::before 20pxx2px bg #ffffff r 999px; span::after 20pxx2px bg #ffffff r 999px; span 20.0x2.0 bg #ffffff |
| Ancestor paint | 1 up div.relative.min-h-screen bg #ffffff |
| How | at rest |

Crops: `m-nav-default.png`.

#### m-menu

Mobile menu button. The icon-only Toggle mobile menu button. Opened locally. Links were never followed.

Page: mobile. Selector: `button[aria-label=Toggle mobile menu]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = | = |
| Padding | 18px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | Libre Franklin 0px/0px 400 | = | = | = | = |
| Letter spacing | -0.16px | = | = | = | = |
| Colour | #1e1e1e | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | span 20.0x2.0 bg #ffffff; span::before 20pxx2px bg #ffffff r 999px; span::after 20pxx2px bg #ffffff r 999px; span 20.0x2.0 bg #ffffff; span::before 20pxx2px bg #ffffff r 999px; span::after 20pxx2px bg #ffffff r 999px | = | button.MobileMenuToggle_MenuToggle__3DstI 36.0x36.0 outline 1px auto #e59700 offset 0px; span 20.0x2.0 bg #ffffff; span::before 20pxx2px bg #ffffff r 999px; span::after 20pxx2px bg #ffffff r 999px; span 20.0x2.0 bg #ffffff; span::before 20pxx2px bg #ffffff r 999px | = | span::before 20pxx2px bg #1e1e1e r 999px; span::after 20pxx2px bg #1e1e1e r 999px; span::before 20pxx2px bg #1e1e1e r 999px; span::after 20pxx2px bg #1e1e1e r 999px; span::before 20pxx2px bg #1e1e1e r 999px; span::after 20pxx2px bg #1e1e1e r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-default.png`, `m-menu-hover.png`, `m-menu-focus-visible.png`, `m-menu-pressed.png`, `m-menu-opened.png`.

#### m-hero

Mobile hero. The home masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | KitSansFont 48px/48px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only the rules the CSSOM could read on each page; the per-state Transition rows above are computed values.

- features: `transform 0.5s, opacity 0.5s, z-index 0.5s`, `opacity 0.5s`, `stroke 0.5s, color 2s`, `stroke 0.5s`, `opacity 0.3s`, `transform 0.2s, right 0.2s`, `0.3s`, `0.3s ease-in-out`, `max-height 0.3s ease-in-out`, `background var(--button-transition-duration)`, `background-color 0.2s ease-in, color 0.2s ease-in`

- home: `transform 0.5s, opacity 0.5s, z-index 0.5s`, `opacity 0.5s`, `stroke 0.5s, color 2s`, `stroke 0.5s`, `background var(--button-transition-duration)`, `opacity 0.3s`, `transform 0.2s, right 0.2s`, `background-color 0.2s ease-in, color 0.2s ease-in`

- login: `height 0.3s`, `background 0.15s ease-in-out`, `color 0.15s ease-in-out`, `0.3s linear`, `left 0.3s`, `0.15s ease-out`, `color 0.2s ease-in-out, background-color 0.2s ease-in-out, outline-color 0.2s ease-in-out`, `background 0.3s, border-color 0.3s, box-shadow 0.2s`, `transform var(--d-t,.3s) var(--d-t-e,ease), opacity var(--d-o,.2s)`, `visibility, opacity 0.3s ease-in-out`, `opacity 0.2s ease-out, transform 0.2s ease-out`, `transform 0.2s`

- pricing: `transform 0.5s, opacity 0.5s, z-index 0.5s`, `opacity 0.5s`, `stroke 0.5s, color 2s`, `stroke 0.5s`, `0.3s`, `outline 0.2s`, `background var(--button-transition-duration)`, `background-color 0.2s ease-in, color 0.2s ease-in`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`, `transform 250ms cubic-bezier(0.33, 0, 0, 1)`, `transform 134ms cubic-bezier(0.45, 0, 0.2, 1)`, `transform 100ms linear, opacity 80ms linear`
