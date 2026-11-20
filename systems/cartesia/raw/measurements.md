# Component measurements

Computed styles read from cartesia.ai on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's signed-out surfaces — the light marketing pages (with .dark islands declared but unbound), the sign-in card on play.cartesia.ai and the Mintlify docs app — with the consent island hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky marketing header: wordmark, the Products/Solutions/Resources menu triggers, Customers, Pricing, Sign in, Contact Sales and the Try-Cartesia pill.

Page: home. Selector: `header[data-site-nav-header]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #e4e3db; L: none |
| Radius | 0px |
| Background | #fefefe |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Text node | button.group/navigation-menu-trigger.inline-flex: ABC Diatype-75f05108b2d5df75 14px/20px 500, #1e1c1a |
| Transition | none |
| Icon | 139.52 x 20, colour #1e1c1a |
| Painted layers | header.sticky.top-0 1440.0x64.0 bg #fefefe border B:1px solid #e4e3db; div.mx-auto.w-[calc(100%-32px)] 1280.0x63.0 border R:1px solid #e4e3db / L:1px solid #e4e3db; button.group/navigation-menu-trigger.inline-flex 91.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; button.group/navigation-menu-trigger.inline-flex 93.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; button.group/navigation-menu-trigger.inline-flex 100.1x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; a.gap-2.p-2 86.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Cartesia wordmark anchor (verdant mark over the neutral wordmark paths).

Page: home. Selector: `header a[aria-label=Cartesia]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 139.52 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Transition | none |
| Cursor | pointer |
| Icon | 139.52 x 20, colour #1e1c1a |
| How | at rest |

Crops: `logo-default.png`.

#### banner

Announcement banner. The full-width announcement strip above the header; measured never followed.

Page: home. Selector: `a "Introducing Cartesia…"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1440 x 36.8 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #a1a1a1 @ 0.5 offset 1px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.text-xs.font-medium: ABC Diatype-75f05108b2d5df75 14px/16.8px 500, #1e1c1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 16, colour #309d4b | = | = | = |
| Ancestor paint | 1 up div.col-[full].border-border bg #f4faef | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.flex 1440.0x36.8 outline 1px auto #a1a1a1 @ 0.5 offset 1px | = |

Crops: `banner-default.png`, `banner-hover.png`, `banner-focus-visible.png`, `banner-pressed.png`.

#### nav-trigger

Nav trigger. The Products button that opens the header mega-menu; toggled, never followed.

Page: home. Selector: `header button "Products"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90.95 x 36 | = | = | = |
| Padding | 6px 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f3f2ef | #f3f2ef | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 12 x 12, colour #1e1c1a | = | = | = |
| Painted layers | button.group/navigation-menu-trigger.inline-flex 91.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.group/navigation-menu-trigger.inline-flex 91.0x36.0 bg #f3f2ef border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button.group/navigation-menu-trigger.inline-flex 91.0x36.0 bg #f3f2ef border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 4px | button.group/navigation-menu-trigger.inline-flex 91.0x36.0 bg #f3f2ef border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The plain Pricing header link.

Page: home. Selector: `header nav a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62.19 x 36 | = | = | = |
| Padding | 6px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f3f2ef | #f3f2ef | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.gap-2.p-2 62.2x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | a.gap-2.p-2 62.2x36.0 bg #f3f2ef border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | a.gap-2.p-2 62.2x36.0 bg #f3f2ef border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 4px | a.gap-2.p-2 62.2x36.0 bg #f3f2ef border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signin

Sign-in link. The Sign-in header action (ghost pill); measured never followed.

Page: home. Selector: `header a "Sign in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.67 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 44.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 44.7x36.0 border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-sales

Sales link. The Contact-Sales header action (outlined pill); measured never followed.

Page: home. Selector: `header a "Contact Sales"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 122.08 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e4e3db | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | #fefefe | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 122.1x36.0 bg #fefefe border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 122.1x36.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 122.1x36.0 bg #fefefe border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 122.1x36.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-sales-default.png`, `nav-sales-hover.png`, `nav-sales-focus-visible.png`, `nav-sales-pressed.png`.

#### nav-cta

Nav CTA. The Try-Cartesia solid pill; measured never followed.

Page: home. Selector: `header a "Try Cartesia"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | #309d4b | #309d4b @ 0.9 | = | #309d4b @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f9f9f8 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 120.0x36.0 bg #309d4b border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 120.0x36.0 bg #309d4b @ 0.9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 120.0x36.0 bg #309d4b border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 120.0x36.0 bg #309d4b @ 0.9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Nav dropdown. The Products mega-menu panel (navigation-menu-content), opened by its own trigger.

Page: home. Selector: `[data-slot=navigation-menu-content]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 624 x 161.75 |
| Padding | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Text node | span.font-display.text-lg: PP Kyoto-b14c6ebb315b725b 18px/24.75px 500, #1e1c1a |
| Transition | opacity, transform, translate 0.35s cubic-bezier(0.22, 1, 0.36, 1) |
| Icon | 16 x 16, colour #525150 |
| Painted layers | a.border.border-transparent 197.3x64.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; a.border.border-transparent 197.3x64.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; a.border.border-transparent 197.3x64.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; div.mx-3.border-t 576.0x1.0 border T:1px solid #e4e3db @ 0.6; a.border.border-transparent 197.3x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px; a.border.border-transparent 197.3x56.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px |
| Ancestor paint | 2 up nav.data-[ending-style]:easing-[ease].xs:w-(--popup-width) bg #fefefe shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1e1c1a @ 0.1 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A product link inside the opened mega-menu.

Page: home. Selector: `menu content a "Sonic"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 197.33 x 64.75 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 2px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | 1px solid #a1a1a1 |
| Radius | 6px | = | = | = |
| Background | transparent | #f3f2ef @ 0.5 | #f3f2ef @ 0.5 | #f3f2ef @ 0.5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1e1c1a 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1e1c1a 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.font-display.text-lg: PP Kyoto-b14c6ebb315b725b 18px/24.75px 500, #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.border.border-transparent 197.3x64.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | a.border.border-transparent 197.3x64.8 bg #f3f2ef @ 0.5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 6px | a.border.border-transparent 197.3x64.8 bg #f3f2ef @ 0.5 border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1e1c1a 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | a.border.border-transparent 197.3x64.8 bg #f3f2ef @ 0.5 border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1e1c1a 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home hero

#### hero-title

Hero headline. The display headline (PP Kyoto / font-display) under the header.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 864.95 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PP Kyoto-b14c6ebb315b725b 40px/46px 500 |
| Letter spacing | -0.4px |
| Colour | #1e1c1a @ 0.7 |
| Text node | span.md:block: PP Kyoto-b14c6ebb315b725b 40px/46px 500, #1e1c1a @ 0.7, ls -0.4px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero copy. The lede under the headline, ABC Diatype / font-sans.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 520 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #525150 |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-orb

Talk-to-Skylar orb. The large round voice-agent button in the hero (icon-only, aria-labelled); measured, never pressed (a press starts a call).

Page: home. Selector: `button[aria-label*="Talk to Skylar"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 244.8 x 244.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #309d4b offset 4px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | none | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 21.59 x 21.59, colour #004e23 | = | = | = |
| Painted layers | span.flex.items-center 48.0x48.0 bg #fefefe @ 0.85 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.16 0px 1px 8px 0px | = | button.cursor-pointer.rounded-full 244.8x244.8 r 3.35544e+07px outline 2px solid #309d4b offset 4px; span.flex.items-center 48.0x48.0 bg #fefefe @ 0.85 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.16 0px 1px 8px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-orb-default.png`, `hero-orb-hover.png`, `hero-orb-focus-visible.png`, `hero-orb-pressed.png`.

#### voice-choose

Voice chooser. A round "Choose <voice>, <role>" button around the orb (icon-only, aria-labelled).

Page: home. Selector: `button[aria-label^="Choose"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.75 x 58.75 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1e1c1a | = | - | = |
| Transition | none | = | - | = |
| Transform | matrix(0.24, 0, 0, 0.24, -526.32, 0) | = | - | = |
| Opacity | 0 | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `voice-choose-default.png`, `voice-choose-hover.png`, `voice-choose-pressed.png`.

#### voice-nav

Voice carousel arrow. A previous/next-voice arrow button in the hero voice carousel.

Page: home. Selector: `button[aria-label*="voice"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fefefe @ 0.8 | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #309d4b offset 2px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a @ 0.7 | #1e1c1a | = | #1e1c1a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #1e1c1a @ 0.7 | 20 x 20, colour #1e1c1a | = | 20 x 20, colour #1e1c1a |
| ::before | 48px x 48px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.relative.z-20 40.0x40.0 bg #fefefe @ 0.8 r 3.35544e+07px | button.relative.z-20 40.0x40.0 bg #f3f2ef r 3.35544e+07px | button.relative.z-20 40.0x40.0 bg #fefefe @ 0.8 r 3.35544e+07px outline 2px solid #309d4b offset 2px | button.relative.z-20 40.0x40.0 bg #f3f2ef r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `voice-nav-default.png`, `voice-nav-hover.png`, `voice-nav-focus-visible.png`, `voice-nav-pressed.png`.

#### media-frame

Media frame. A customer-story media tile with a play affordance; measured, never pressed.

Page: home. Selector: `button "Play with sound"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 559 x 559 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #e4e3db | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f3f2ef | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #a1a1a1 offset -2px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.body-3-medium: ABC Diatype-75f05108b2d5df75 14px/19.6px 500, #1e1c1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1e1c1a | = | = | = |
| Painted layers | button.group.media-frame 559.0x559.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px; span.absolute.right-4 162.2x43.6 bg #fefefe @ 0.9 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | button.group.media-frame 559.0x559.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px; span.absolute.right-4 162.2x43.6 bg #fefefe r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | button.group.media-frame 559.0x559.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px outline 2px solid #a1a1a1 offset -2px; span.absolute.right-4 162.2x43.6 bg #fefefe @ 0.9 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | button.group.media-frame 559.0x559.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px; span.absolute.right-4 162.2x43.6 bg #fefefe r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `media-frame-default.png`, `media-frame-hover.png`, `media-frame-focus-visible.png`, `media-frame-pressed.png`.

#### story-card

Customer story tile. The customer-story media tile behind the play affordance.

Page: home. Selector: `story media frame`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 559 x 559 |
| Padding | 0px |
| Border | 1px solid #e4e3db |
| Radius | 8px |
| Background | #f3f2ef |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Text node | span.body-3-medium: ABC Diatype-75f05108b2d5df75 14px/19.6px 500, #1e1c1a |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #1e1c1a |
| Painted layers | button.group.media-frame 559.0x559.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px; span.absolute.right-4 162.2x43.6 bg #fefefe @ 0.9 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest |

Crops: `story-card-default.png`.

### Home

#### h2-display

Section heading (display). A PP-Kyoto display section heading in the light sections.

Page: home. Selector: `h2.font-display`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 559 x 67.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PP Kyoto-b14c6ebb315b725b 26px/33.8px 500 |
| Letter spacing | normal |
| Colour | #1e1c1a @ 0.7 |
| Text node | span.text-foreground: PP Kyoto-b14c6ebb315b725b 26px/33.8px 500, #1e1c1a |
| Transition | none |
| How | at rest |

Crops: `h2-display-default.png`.

#### product-card

Product card. A product card link (Ink/Sonic) in the full-stack section; measured never followed.

Page: home. Selector: `a product card "Ink."`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 571 x 377.59 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #a1a1a1 @ 0.5 offset 1px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.text-foreground: ABC Diatype-75f05108b2d5df75 16px/16px 500, #1e1c1a, ls 0.16px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #525150 | = | = | = |
| Painted layers | video.h-75.w-full 571.0x300.0 bg #f3f2ef | = | a.group.flex 571.0x377.6 outline 1px auto #a1a1a1 @ 0.5 offset 1px; video.h-75.w-full 571.0x300.0 bg #f3f2ef | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-card-default.png`, `product-card-hover.png`, `product-card-focus-visible.png`, `product-card-pressed.png`.

#### cta-link

Text CTA. The "Our research" pill link in the research section; measured never followed.

Page: home. Selector: `a "Our research"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e4e3db | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | #fefefe | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 120.0x36.0 bg #fefefe border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 120.0x36.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 120.0x36.0 bg #fefefe border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 120.0x36.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-link-default.png`, `cta-link-hover.png`, `cta-link-focus-visible.png`, `cta-link-pressed.png`.

#### accordion-trigger

Accordion trigger. A Cloud/On-premise deployment accordion header; toggled for its collapsed/expanded state.

Page: home. Selector: `button accordion "Cloud"`. States: default, hover, focus-visible, pressed, selected.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 514 x 74 | = | = | = | = |
| Padding | 24px 0px | = | = | = | = |
| Gap | 16px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1e1c1a | = | = | = | = |
| Text node | span.text-muted-foreground.group-aria-expanded/accordion-trigger:text-foreground: ABC Diatype-75f05108b2d5df75 16px/24px 500, #1e1c1a | = | = | = | span.text-muted-foreground.group-aria-expanded/accordion-trigger:text-foreground: ABC Diatype-75f05108b2d5df75 16px/24px 500, #525150 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = | = |
| Cursor | default | = | = | = | = |
| Icon | 24 x 24, colour #1e1c1a | = | = | = | 24 x 24, colour #525150 |
| Painted layers | button.focus-visible:border-focus.focus-visible:after:border-focus 514.0x74.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | button.focus-visible:border-focus.focus-visible:after:border-focus 514.0x74.0 border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| ::after | - | = | 0px x 0px, static, bg #000000 @ 0, radius 0px | = | = |

Crops: `accordion-trigger-default.png`, `accordion-trigger-hover.png`, `accordion-trigger-focus-visible.png`, `accordion-trigger-pressed.png`, `accordion-trigger-selected.png`.

#### accordion-content

Accordion content. The expanded accordion region beside the deployment triggers.

Page: home. Selector: `accordion content region`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 514 x 224 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Text node | span.text-muted-foreground.group-aria-expanded/accordion-trigger:text-foreground: ABC Diatype-75f05108b2d5df75 16px/24px 500, #525150 |
| Transition | none |
| Icon | 24 x 24, colour #525150 |
| Painted layers | div.border-border.not-last:border-b 514.0x75.0 border B:1px solid #e4e3db; button.focus-visible:border-focus.focus-visible:after:border-focus 514.0x74.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; div.border-border.not-last:border-b 514.0x75.0 border B:1px solid #e4e3db; button.focus-visible:border-focus.focus-visible:after:border-focus 514.0x74.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.focus-visible:border-focus.focus-visible:after:border-focus 514.0x74.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `accordion-content-default.png`.

#### product-row

Product row. The wide Managed-Agents product row link; measured never followed.

Page: home. Selector: `a "Managed Agents."`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1182 x 53.59 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #a1a1a1 @ 0.5 offset 1px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.text-foreground: ABC Diatype-75f05108b2d5df75 16px/16px 500, #1e1c1a, ls 0.16px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #525150 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.flex 1182.0x53.6 outline 1px auto #a1a1a1 @ 0.5 offset 1px | = |

Crops: `product-row-default.png`, `product-row-hover.png`, `product-row-focus-visible.png`, `product-row-pressed.png`.

### Product pages

#### pd-h1

Product headline. The Sonic product-page display headline.

Page: sonic. Selector: `h1 on /sonic`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 745.33 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PP Kyoto-b14c6ebb315b725b 40px/46px 500 |
| Letter spacing | normal |
| Colour | #1e1c1a @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `pd-h1-default.png`.

#### pd-cta

Product CTA. The "Try Sonic-3.6" hero action; measured never followed.

Page: sonic. Selector: `a "Try Sonic-3.6"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 124.38 x 40 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | #309d4b | #309d4b @ 0.9 | = | #309d4b @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f9f9f8 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 124.4x40.0 bg #309d4b border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 124.4x40.0 bg #309d4b @ 0.9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 124.4x40.0 bg #309d4b border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 124.4x40.0 bg #309d4b @ 0.9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pd-cta-default.png`, `pd-cta-hover.png`, `pd-cta-focus-visible.png`, `pd-cta-pressed.png`.

#### pd-secondary

Secondary CTA. The Contact-Sales hero action; measured never followed.

Page: sonic. Selector: `a "Contact Sales" hero`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.08 x 40 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e4e3db | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | #fefefe | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 130.1x40.0 bg #fefefe border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 130.1x40.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 130.1x40.0 bg #fefefe border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 130.1x40.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pd-secondary-default.png`, `pd-secondary-hover.png`, `pd-secondary-focus-visible.png`, `pd-secondary-pressed.png`.

#### usecase-chip

Use-case chip. A demo use-case chip in the voice demo; toggled for its selected state (switches the demo script, nothing sent).

Page: sonic. Selector: `button "Customer Support"`. States: default, hover, focus-visible, pressed, selected.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 144.13 x 30 | = | = | = | = |
| Padding | 6px 12px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | 1px solid #e4e3db | = | = | = | = |
| Radius | 3.35544e+07px | = | = | = | = |
| Background | #fefefe | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #a1a1a1 @ 0.5 offset 0px | = | = |
| Font | ABC Diatype-75f05108b2d5df75 12px/16px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #525150 | #1e1c1a | = | #1e1c1a | #1e1c1a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | default | = | = | = | = |
| Icon | 14 x 14, colour #525150 | 14 x 14, colour #1e1c1a | = | 14 x 14, colour #1e1c1a | 14 x 14, colour #1e1c1a |
| Painted layers | button.shrink-0.inline-flex 144.1x30.0 bg #fefefe border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 3.35544e+07px | = | button.shrink-0.inline-flex 144.1x30.0 bg #fefefe border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 3.35544e+07px outline 1px auto #a1a1a1 @ 0.5 offset 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `usecase-chip-default.png`, `usecase-chip-hover.png`, `usecase-chip-focus-visible.png`, `usecase-chip-pressed.png`, `usecase-chip-selected.png`.

#### voice-chip

Voice/locale chip. A rounded-full locale or voice picker chip in the demo bar.

Page: sonic. Selector: `button "American English" / "Jacqueline"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118.19 x 34 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e4e3db | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #f9f9f8 @ 0.5 | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | 1px auto #a1a1a1 @ 0.5 offset 0px | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.max-w-48.truncate: ABC Diatype-75f05108b2d5df75 14px/20px 500, #1e1c1a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #1e1c1a | = | = | = |
| Painted layers | button.inline-flex.items-center 118.2x34.0 bg #f9f9f8 @ 0.5 border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 3.35544e+07px | button.inline-flex.items-center 118.2x34.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 3.35544e+07px | button.inline-flex.items-center 118.2x34.0 bg #f9f9f8 @ 0.5 border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 3.35544e+07px outline 1px auto #a1a1a1 @ 0.5 offset 0px | button.inline-flex.items-center 118.2x34.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `voice-chip-default.png`, `voice-chip-hover.png`, `voice-chip-focus-visible.png`, `voice-chip-pressed.png`.

#### play-btn

Play button. The demo Play action; measured, never pressed.

Page: sonic. Selector: `button "Play"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59.91 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | #309d4b | #309d4b @ 0.9 | = | #309d4b @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f9f9f8 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 59.9x36.0 bg #309d4b border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 59.9x36.0 bg #309d4b @ 0.9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 59.9x36.0 bg #309d4b border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 59.9x36.0 bg #309d4b @ 0.9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `play-btn-default.png`, `play-btn-hover.png`, `play-btn-focus-visible.png`, `play-btn-pressed.png`.

#### word-play

Sample play button. A 32px square play button on a pronunciation/clone sample (icon-only, aria-labelled); measured, never pressed.

Page: sonic. Selector: `button[aria-label^="Play"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #f3f2ef | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fefefe | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #309d4b offset 2px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #1e1c1a | = | = | = |
| Painted layers | button.flex.shrink-0 32.0x32.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px | button.flex.shrink-0 32.0x32.0 bg #f3f2ef border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px | button.flex.shrink-0 32.0x32.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px outline 2px solid #309d4b offset 2px | button.flex.shrink-0 32.0x32.0 bg #f3f2ef border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `word-play-default.png`, `word-play-hover.png`, `word-play-focus-visible.png`, `word-play-pressed.png`.

#### voice-row

Voice row. A "voice — locale" row in the voice list (group flex row with a play affordance).

Page: sonic. Selector: `button "Emma - American English"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 329.33 x 48 | = | = | = |
| Padding | 12px 8px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #309d4b offset 2px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.block.leading-snug: ABC Diatype-75f05108b2d5df75 16px/22px 400, #1e1c1a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #1e1c1a | = | = | = |
| Painted layers | span.flex.shrink-0 24.0x24.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px | button.group.flex 329.3x48.0 bg #f3f2ef; span.flex.shrink-0 24.0x24.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px | button.group.flex 329.3x48.0 outline 2px solid #309d4b offset 2px; span.flex.shrink-0 24.0x24.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px | button.group.flex 329.3x48.0 bg #f3f2ef; span.flex.shrink-0 24.0x24.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `voice-row-default.png`, `voice-row-hover.png`, `voice-row-focus-visible.png`, `voice-row-pressed.png`.

#### voices-h1

Voices headline. The "Find your voice." display headline.

Page: voices. Selector: `h1 on /voices`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 315.7 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PP Kyoto-b14c6ebb315b725b 40px/46px 500 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Transition | none |
| How | at rest |

Crops: `voices-h1-default.png`.

#### globe-dot

Globe locale dot. A locale dot on the voices globe; toggled, never dragged.

Page: voices. Selector: `button.voices-globe-dot`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 19.08 x 19.08 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #c5c2bc @ 0.9 | = | = | = |
| Radius | 50% | = | = | = |
| Background | #1e1c1a @ 0.7 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #a1a1a1 offset 2px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 17.0781px x 17.0781px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.voices-globe-dot 19.1x19.1 bg #1e1c1a @ 0.7 border T:1px solid #c5c2bc @ 0.9 / R:1px solid #c5c2bc @ 0.9 / B:1px solid #c5c2bc @ 0.9 / L:1px solid #c5c2bc @ 0.9 r 50% | = | button.voices-globe-dot 19.1x19.1 bg #1e1c1a @ 0.7 border T:1px solid #c5c2bc @ 0.9 / R:1px solid #c5c2bc @ 0.9 / B:1px solid #c5c2bc @ 0.9 / L:1px solid #c5c2bc @ 0.9 r 50% outline 2px solid #a1a1a1 offset 2px | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `globe-dot-default.png`, `globe-dot-hover.png`, `globe-dot-focus-visible.png`, `globe-dot-pressed.png`.

#### globe-play

Globe play. The round play button inside the voices globe; measured, never pressed.

Page: voices. Selector: `button.voices-globe-play`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81 x 81 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #a1a1a1 offset 2px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1e1c1a | = | = | = |
| Painted layers | span.voices-globe-play-ring 81.0x81.0 border T:1px solid #fefefe / R:1px solid #fefefe / B:1px solid #fefefe / L:1px solid #fefefe r 50%; span.voices-globe-play-disc 64.2x64.2 bg #fefefe r 50% | = | button.voices-globe-play 81.0x81.0 outline 2px solid #a1a1a1 offset 2px; span.voices-globe-play-ring 81.0x81.0 border T:1px solid #fefefe / R:1px solid #fefefe / B:1px solid #fefefe / L:1px solid #fefefe r 50%; span.voices-globe-play-disc 64.2x64.2 bg #fefefe r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `globe-play-default.png`, `globe-play-hover.png`, `globe-play-focus-visible.png`, `globe-play-pressed.png`.

#### globe-arrow

Locale arrow. A previous/next-locale arrow in the globe panel.

Page: voices. Selector: `button.voices-globe-arrow`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #a1a1a1 offset 2px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1e1c1a | = | = | = |
| ::before | 32px x 32px, static, bg #fefefe, radius 50% | 32px x 32px, static, bg #f3f2ef, radius 50% | = | 32px x 32px, static, bg #f3f2ef, radius 50% |
| Painted layers | button::before.voices-globe-arrow 32pxx32px bg #fefefe r 50% | button::before.voices-globe-arrow 32pxx32px bg #f3f2ef r 50% | button.voices-globe-arrow 32.0x32.0 outline 2px solid #a1a1a1 offset 2px; button::before.voices-globe-arrow 32pxx32px bg #fefefe r 50% | button::before.voices-globe-arrow 32pxx32px bg #f3f2ef r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `globe-arrow-default.png`, `globe-arrow-hover.png`, `globe-arrow-focus-visible.png`, `globe-arrow-pressed.png`.

#### globe-voice

Globe voice row. A "voice + persona" row in the globe voice list.

Page: voices. Selector: `button.voices-globe-voice`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 244.09 x 38 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #a1a1a1 offset 2px | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.voices-globe-voice-name.text-muted-foreground: ABC Diatype-75f05108b2d5df75 14px/19.6px 400, #525150 | span.voices-globe-voice-name.text-muted-foreground: ABC Diatype-75f05108b2d5df75 14px/19.6px 400, #1e1c1a | = | span.voices-globe-voice-name.text-muted-foreground: ABC Diatype-75f05108b2d5df75 14px/19.6px 400, #1e1c1a |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #1e1c1a | = | = | = |
| Painted layers | span.flex.rounded-full 26.0x26.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px | button.voices-globe-voice.flex 244.1x38.0 bg #f3f2ef r 4px; span.flex.rounded-full 26.0x26.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px | button.voices-globe-voice.flex 244.1x38.0 r 4px outline 2px solid #a1a1a1 offset 2px; span.flex.rounded-full 26.0x26.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px | button.voices-globe-voice.flex 244.1x38.0 bg #f3f2ef r 4px; span.flex.rounded-full 26.0x26.0 bg #fefefe border T:1px solid #f3f2ef / R:1px solid #f3f2ef / B:1px solid #f3f2ef / L:1px solid #f3f2ef r 3.35544e+07px |
| Ancestor paint | 2 up div.hidden.flex-col bg #fefefe shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2px 8px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `globe-voice-default.png`, `globe-voice-hover.png`, `globe-voice-focus-visible.png`, `globe-voice-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The pricing page display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 745.33 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PP Kyoto-b14c6ebb315b725b 40px/46px 500 |
| Letter spacing | normal |
| Colour | #1e1c1a @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-name

Plan group name. A plan group heading (Text to Speech / Speech to Text / Voice Agents).

Page: pricing. Selector: `h3 plan group`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 132.16 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 20px/26px 465 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-cta

Plan CTA. A plan card's "Start free" action; measured never followed.

Page: pricing. Selector: `a "Start free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 206.8 x 36 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e4e3db | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | #fefefe | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/19.25px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #fefefe border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #fefefe border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px |
| Ancestor paint | 1 up div.relative.bg-background bg #fefefe shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e4e3db 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-cta-alt

Plan CTA alt. A secondary plan action ("Select Startup"/"Contact us"); measured never followed.

Page: pricing. Selector: `a "Select Startup"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 206.8 x 36 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e4e3db | = | 1px solid #a1a1a1 | = |
| Radius | 8px | = | = | = |
| Background | #fefefe | #f3f2ef | = | #f3f2ef |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/19.25px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #fefefe border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #fefefe border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #f3f2ef border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px |
| Ancestor paint | 1 up div.relative.bg-background bg #fefefe shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e4e3db 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-alt-default.png`, `plan-cta-alt-hover.png`, `plan-cta-alt-focus-visible.png`, `plan-cta-alt-pressed.png`.

#### plan-card

Plan card. A pricing plan card (the painted cell holding the plan CTA, ring-1 bg-background).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 254.8 x 543.25 |
| Padding | 40px 24px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | #fefefe |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e4e3db 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Text node | p.eyebrow.text-cartesia-neutral-600: IBM Plex Mono-1f31a4fbe8ce28fa 12px/16.5px 500, #a7a6a2 |
| Transition | none |
| Icon | 14 x 14, colour #309d4b |
| Painted layers | div.relative.bg-background 254.8x543.3 bg #fefefe shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e4e3db 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; a.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.8x36.0 bg #fefefe border T:1px solid #e4e3db / R:1px solid #e4e3db / B:1px solid #e4e3db / L:1px solid #e4e3db r 8px; div.space-y-3.border-t 206.8x71.5 border T:1px solid #e4e3db |
| How | at rest |

Crops: `plan-card-default.png`.

#### faq-trigger

FAQ item. An FAQs details/summary row (the summary toggles its own answer).

Page: pricing. Selector: `summary.faq-summary`. States: default, hover, focus-visible, pressed, selected.

| Property | default | hover | focus-visible | pressed | selected |
|---|---|---|---|---|---|
| Size (w x h) | 852.02 x 102.75 | = | = | = | = |
| Padding | 56px 48px 24px 48px | = | = | = | = |
| Gap | 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #a1a1a1 offset -2px | = | = |
| Font | ABC Diatype-75f05108b2d5df75 14px/22.75px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #1e1c1a | = | = | = | = |
| Text node | span: ABC Diatype-75f05108b2d5df75 14px/22.75px 500, #1e1c1a | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #525150 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | summary.faq-summary.flex 852.0x102.8 outline 2px solid #a1a1a1 offset -2px | = | = |

Crops: `faq-trigger-default.png`, `faq-trigger-hover.png`, `faq-trigger-focus-visible.png`, `faq-trigger-pressed.png`, `faq-trigger-selected.png`.

#### plan-tab

Plan tab. A plan tab in the compare strip (Free/Pro/Startup/Scale/Enterprise); toggled for its selected state, never checked out.

Page: pricing. Selector: `button plan tab "Pro"`. States: .

Not found on the page at capture time.

#### plan-slider

Usage slider. The "Minutes of generated audio per month" range input in the cost calculator; focused only, never dragged.

Page: pricing. Selector: `input[aria-label*=minutes]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 556.5 x 46 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #1e1c1a | = |
| Transition | none | = |
| Opacity | 0 | = |
| Cursor | pointer | = |
| Placeholder | #1e1c1a, opacity 1 | = |
| Ancestor paint | 1 up div.relative.h-12 bg #f3f2ef | = |
| How | at rest | clicked into the field |

Crops: `plan-slider-default.png`, `plan-slider-focused.png`.

### Playground sign-in boundary

#### login-card

Sign-in card. The centred sign-in column on play.cartesia.ai (the boundary before the gated playground); never filled or submitted.

Page: signin. Selector: `sign-in main column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 727.5 |
| Padding | 144px 0px 40px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #39342f |
| Text node | h1.text-2xl.font-medium: sans 30px/36px 500, #39342f, ls -0.75px |
| Transition | none |
| Icon | 20 x 20, colour #39342f, fill #000000 |
| Painted layers | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 bg #f9f9f8 border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 12px; button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 bg #f9f9f8 border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 12px; span.h-px.flex-1 192.5x1.0 bg #dfdcd7; span.h-px.flex-1 192.5x1.0 bg #dfdcd7; input.bg-field.dark:bg-input/30 420.0x44.0 bg #ffffff border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 8px; button.focus-visible:border-focus.aria-invalid:ring-destructive/20 420.0x44.0 bg #004e23 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest |

Crops: `login-card-default.png`.

#### email-field

Email field. The email-address input; sample text was typed and deleted, nothing sent.

Page: signin. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 420 x 44 | = | = |
| Padding | 4px 14px | = | = |
| Border | 1px solid #dfdcd7 | 1px solid #a1a1a1 | 1px solid #a1a1a1 |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sans 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #39342f | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #636260 @ 0.55, opacity 1 | = | = |
| Painted layers | input.bg-field.dark:bg-input/30 420.0x44.0 bg #ffffff border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 8px | input.bg-field.dark:bg-input/30 420.0x44.0 bg #ffffff border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px | input.bg-field.dark:bg-input/30 420.0x44.0 bg #ffffff border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### continue-btn

Continue button. The Continue submit; measured, never pressed (a press would submit the form).

Page: signin. Selector: `button "Continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 420 x 44 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 12px | = | = | = |
| Background | #004e23 | #004e23 @ 0.9 | = | #004e23 @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sans 15px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fefefe | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 420.0x44.0 bg #004e23 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 420.0x44.0 bg #004e23 @ 0.9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 420.0x44.0 bg #004e23 border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 12px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 420.0x44.0 bg #004e23 @ 0.9 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `continue-btn-default.png`, `continue-btn-hover.png`, `continue-btn-focus-visible.png`, `continue-btn-pressed.png`.

#### sso-btn

SSO button. An OAuth button beside the form (labelled "Continue with Google"/"Continue with GitHub" when the labels render); measured, never followed.

Page: signin. Selector: `sso button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 206 x 44 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #dfdcd7 | = | 1px solid #a1a1a1 | = |
| Radius | 12px | = | = | = |
| Background | #f9f9f8 | #f1f0ec | = | #f1f0ec |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sans 15px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #39342f | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 20 x 20, colour #39342f, fill #000000 | = | = | = |
| Painted layers | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 bg #f9f9f8 border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 12px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 bg #f1f0ec border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 12px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 bg #f9f9f8 border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 12px | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 bg #f1f0ec border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-btn-default.png`, `sso-btn-hover.png`, `sso-btn-focus-visible.png`, `sso-btn-pressed.png`.

#### passkey-btn

Passkey button. The "Sign in with a passkey" text action; measured, never pressed.

Page: signin. Selector: `button "Sign in with a passkey"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137.3 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #636260 | #39342f | = | #39342f |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.relative.[@media(pointer:coarse)]:after:absolute 137.3x22.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | = | button.relative.[@media(pointer:coarse)]:after:absolute 137.3x22.0 border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `passkey-btn-default.png`, `passkey-btn-hover.png`, `passkey-btn-focus-visible.png`, `passkey-btn-pressed.png`.

#### signup-card

Signup card. The centred create-account column (/sign-in/create); never filled or submitted.

Page: signup. Selector: `signup main column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 727.5 |
| Padding | 144px 0px 40px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #39342f |
| Text node | h1.text-2xl.font-medium: sans 30px/36px 500, #39342f, ls -0.75px |
| Transition | none |
| Icon | 20 x 20, colour #39342f, fill #000000 |
| Painted layers | button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 bg #f9f9f8 border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 12px; button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 bg #f9f9f8 border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 12px; span.h-px.flex-1 192.5x1.0 bg #dfdcd7; span.h-px.flex-1 192.5x1.0 bg #dfdcd7; input.bg-field.dark:bg-input/30 420.0x44.0 bg #ffffff border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 8px; button.focus-visible:border-focus.aria-invalid:ring-destructive/20 420.0x44.0 bg #004e23 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest |

Crops: `signup-card-default.png`.

#### signup-field

Signup email field. The signup email input; focused only, never filled or submitted.

Page: signup. Selector: `signup input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 420 x 44 | = |
| Padding | 4px 14px | = |
| Border | 1px solid #dfdcd7 | 1px solid #a1a1a1 |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans 14px/21px 400 | = |
| Letter spacing | normal | = |
| Colour | #39342f | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #636260 @ 0.55, opacity 1 | = |
| Painted layers | input.bg-field.dark:bg-input/30 420.0x44.0 bg #ffffff border T:1px solid #dfdcd7 / R:1px solid #dfdcd7 / B:1px solid #dfdcd7 / L:1px solid #dfdcd7 r 8px | input.bg-field.dark:bg-input/30 420.0x44.0 bg #ffffff border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 8px |
| How | at rest | clicked into the field |

Crops: `signup-field-default.png`, `signup-field-focused.png`.

### Docs (Mintlify surface)

#### docs-header

Docs header. The Mintlify docs top bar (wordmark, Search ⌘K, Log In / Playground links).

Page: docs. Selector: `docs header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #717472 |
| Text node | span.truncate.max-w-[12.5rem]: Inter 14px/20px 500, #181b19 |
| Transition | none |
| Icon | 12 x 12, colour #9fa3a0, fill #000000 |
| Painted layers | div.z-10.absolute 1440.0x96.0 border B:1px solid #eff2f0; div.z-0.absolute 1440.0x96.0 bg #f9f9f8; button.group/search.flex 277.6x36.0 bg #0b0e0c @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa3a0 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button.group/ai.flex-none 157.8x36.0 bg #0b0e0c @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa3a0 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.flex.items-center 69.0x36.0 bg #0b0e0c @ 0.03 r 12px; a.flex.items-center 0.0x0.0 bg #0b0e0c @ 0.03 r 12px |
| How | at rest |

Crops: `docs-header-default.png`.

#### docs-search

Search button. The "Search… ⌘K" docs search input; measured, never opened.

Page: docs. Selector: `button "Search…"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 277.56 x 36 | = | = | = |
| Padding | 0px 12px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #0b0e0c @ 0.03 | #0b0e0c @ 0.1 | = | #0b0e0c @ 0.1 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa3a0 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #515452 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #515452 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px auto #309d4b offset 0px | = |
| Font | Inter 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #717472 | = | = | = |
| Text node | div.truncate.min-w-0: Inter 14px/24px 400, #717472 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #404340, fill #000000 | 16 x 16, colour #262a27, fill #000000 | = | 16 x 16, colour #262a27, fill #000000 |
| Painted layers | button.group/search.flex 277.6x36.0 bg #0b0e0c @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa3a0 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 277.6x36.0 bg #0b0e0c @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #515452 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.group/search.flex 277.6x36.0 bg #0b0e0c @ 0.03 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #9fa3a0 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #309d4b offset 0px | button.group/search.flex 277.6x36.0 bg #0b0e0c @ 0.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #515452 @ 0.3 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-nav-item

Docs nav item. A sidebar navigation link in the docs app.

Page: docs. Selector: `aside a "Text-to-Speech"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 268 x 32 | = | = | = |
| Padding | 6px 12px 6px 16px | = | = | = |
| Gap | normal 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #515452 @ 0.05 | = | #515452 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #309d4b offset -2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #404340 | #181b19 | = | #181b19 |
| Text node | span.min-w-0.max-w-full: Inter 14px/20px 400, #404340 | span.min-w-0.max-w-full: Inter 14px/20px 400, #181b19 | = | span.min-w-0.max-w-full: Inter 14px/20px 400, #181b19 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #404340, fill #000000 | 16 x 16, colour #181b19, fill #000000 | = | 16 x 16, colour #181b19, fill #000000 |
| Painted layers | svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #9fa3a0 | a.group.flex 268.0x32.0 bg #515452 @ 0.05 r 12px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #9fa3a0 | a.group.flex 268.0x32.0 r 12px outline 1px auto #309d4b offset -2px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #9fa3a0 | a.group.flex 268.0x32.0 bg #515452 @ 0.05 r 12px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #9fa3a0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-nav-item-default.png`, `docs-nav-item-hover.png`, `docs-nav-item-focus-visible.png`, `docs-nav-item-pressed.png`.

#### docs-h1

Docs title. The docs page title (Inter, docs-platform type — a separate surface from the marketing fonts).

Page: docs. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 343.19 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 600 |
| Letter spacing | -0.9px |
| Colour | #181b19 |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

### Footer

#### footer

Footer. The footer: link columns (Products/Company/Capabilities/Use cases/Industries/Resources), legal and social.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1278 x 767 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Text node | p.text-[15px].leading-6: ABC Diatype-75f05108b2d5df75 15px/24px 400, #525150 |
| Transition | none |
| Icon | 144 x 20, colour #1e1c1a |
| Painted layers | div.flex.flex-col 304.3x684.0 border R:1px solid #e4e3db; a.rounded-sm.border 146.0x22.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; a.flex.size-6 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; a.flex.size-6 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; a.flex.size-6 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div.relative.bg-background 242.7x684.0 bg #fefefe shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e4e3db 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 39.88 x 30 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #a1a1a1 | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ABC Diatype-75f05108b2d5df75 15px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #525150 | #1e1c1a | = | #1e1c1a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-block.max-w-full 39.9x30.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | = | a.inline-block.max-w-full 39.9x30.0 border T:1px solid #a1a1a1 / R:1px solid #a1a1a1 / B:1px solid #a1a1a1 / L:1px solid #a1a1a1 r 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-col-head

Footer column head. A footer column heading (17px font-sans medium).

Page: home. Selector: `footer h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 146.67 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 17px/24px 465 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Transition | none |
| Ancestor paint | 2 up div.relative.bg-background bg #fefefe shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e4e3db 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `footer-col-head-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #e4e3db; L: none |
| Radius | 0px |
| Background | #fefefe |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Text node | a.focus-visible:border-focus.aria-invalid:ring-destructive/20: ABC Diatype-75f05108b2d5df75 14px/20px 500, #f9f9f8 |
| Transition | none |
| Icon | 0 x 0, colour #1e1c1a |
| Painted layers | header.sticky.top-0 390.0x64.0 bg #fefefe border B:1px solid #e4e3db; div.mx-auto.w-[calc(100%-32px)] 358.0x63.0 border R:1px solid #e4e3db / L:1px solid #e4e3db; button.group/navigation-menu-trigger.inline-flex 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; button.group/navigation-menu-trigger.inline-flex 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; button.group/navigation-menu-trigger.inline-flex 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; a.gap-2.p-2 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header "Open menu" toggle.

Page: mobile. Selector: `header button "Open menu"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #1e1c1a |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The header menu panel opened by its own toggle.

Page: mobile. Selector: `mobile menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 64px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #fefefe |
| Box shadow | none |
| Outline | none |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1e1c1a |
| Text node | span.text-lg.font-medium: ABC Diatype-75f05108b2d5df75 18px/28px 500, #1e1c1a |
| Transition | opacity, translate, visibility 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 16 x 16, colour #525150 |
| Painted layers | div.fixed.inset-0 390.0x844.0 bg #fefefe; div.mx-auto.w-[calc(100%-32px)] 358.0x780.0 border R:1px solid #e4e3db / L:1px solid #e4e3db; div.border-b.border-border 356.0x57.0 border B:1px solid #e4e3db; div.mt-1.flex 324.0x137.0 border T:1px solid #e4e3db; div.border-b.border-border 356.0x57.0 border B:1px solid #e4e3db; div.border-b.border-border 356.0x57.0 border B:1px solid #e4e3db |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened header menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 356 x 56 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #a1a1a1 @ 0.5 offset 0px | = |
| Font | ABC Diatype-75f05108b2d5df75 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1c1a | = | = | = |
| Text node | span.text-lg.font-medium: ABC Diatype-75f05108b2d5df75 18px/28px 500, #1e1c1a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #525150 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.px-4.md:px-8 356.0x56.0 outline 1px auto #a1a1a1 @ 0.5 offset 0px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308 x 183.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PP Kyoto-b14c6ebb315b725b 32px/36.8px 500 |
| Letter spacing | normal |
| Colour | #1e1c1a @ 0.7 |
| Text node | span.md:block: PP Kyoto-b14c6ebb315b725b 32px/36.8px 500, #1e1c1a @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

cartesia.ai serves its Astro CSS bundles same-origin (the play.cartesia.ai and docs.cartesia.ai bundles were read from network responses), so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- docs: `top 0.16s cubic-bezier(0.25, 0.75, 0.2, 1)`, `width var(--duration-long)var(--timing),height var(--duration-long)var(--timing),background var(--duration-short)ease,scale var(--duration-short)var(--timing)`, `none`, `border-color 0.3s`, `filter 0.35s, opacity 0.35s`, `opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `opacity var(--lightbox-pull-snap-duration,var(--lightbox-vt-duration))var(--lightbox-pull-snap-easing,var(--lightbox-vt-root-easing))`, `opacity var(--lightbox-vt-duration)var(--lightbox-vt-root-easing)`, `opacity 0.2s, visibility linear`, `opacity 0.2s, visibility linear 0.2s`, `opacity 0.2s`

- home: `height var(--site-accordion-duration) var(--site-accordion-ease)`, `opacity 0.35s, top 0.5s cubic-bezier(0.4, 0, 0.2, 1)`, `height var(--motion-disclosure-enter-duration) var(--motion-disclosure-ease)`, `none`, `fill .2s var(--fp-ease)`, `stroke .2s var(--fp-ease)`

- pricing: `rotate var(--site-accordion-duration) var(--site-accordion-ease)`, `height var(--site-accordion-duration) var(--site-accordion-ease), content-visibility var(--site-accordion-duration) allow-discrete`, `height var(--motion-disclosure-enter-duration) var(--motion-disclosure-ease)`, `none`, `fill .2s var(--fp-ease)`, `stroke .2s var(--fp-ease)`

- signin: `height var(--motion-disclosure-enter-duration) var(--motion-disclosure-ease)`, `none`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `opacity 0.2s, transform 0.2s`, `opacity 0.7s ease-out`, `transform 0.14s`, `transform 0.14s ease-out, background-color 0.14s ease-out, box-shadow 0.14s ease-out`

- sonic: `rotate var(--site-accordion-duration) var(--site-accordion-ease)`, `height var(--site-accordion-duration) var(--site-accordion-ease), content-visibility var(--site-accordion-duration) allow-discrete`, `height var(--motion-disclosure-enter-duration) var(--motion-disclosure-ease)`, `none`, `fill .2s var(--fp-ease)`, `stroke .2s var(--fp-ease)`, `grid-template-rows 0.25s`, `opacity 0.7s ease-out`, `background-color 0.14s`

- voices: `height var(--motion-disclosure-enter-duration) var(--motion-disclosure-ease)`, `none`, `fill .2s var(--fp-ease)`, `stroke .2s var(--fp-ease)`, `opacity 0.7s ease-out`, `background-color 0.14s`
