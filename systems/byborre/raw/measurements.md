# Component measurements

Computed styles read from byborre.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public marketing pages, the /collection Textile Room, the textile detail page, the signed-out /login dialog and the contact form — with the newsletter modal hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### marquee

Marquee bar. The top ticker (ORDER FREE SAMPLES — WORLDWIDE SHIPPING) that scrolls continuously; measured as the outer bar, whose inner strip translates.

Page: home. Selector: `marquee bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 2834.22 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 11px/12px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.animate-marquee.float-left: Helvetica Neue 11px/12px 500, #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `marquee-default.png`.

#### header

Header. The sticky cream header: wordmark, Textile Room/Design Studio links, the Collaborations and About flyout triggers, Contact, Cart and account icons, the Go-to-the-platform pill.

Page: home. Selector: `header.sticky`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 57 |
| Padding | 0px 16px |
| Border | T: none; R: none; B: 1px solid #1b1b1b; L: none |
| Radius | 0px |
| Background | #f5f5f0 |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span: Helvetica Neue 16px/20px 400, #1b1b1b |
| Transition | none |
| Painted layers | header.sticky.left-0 1440.0x57.0 bg #f5f5f0 border B:1px solid #1b1b1b; nav.container.flex 1408.0x56.0 border R:1px solid #1b1b1b / L:1px solid #1b1b1b; div.flex.w-full 815.4x32.0 bg #f5f5f0; div.absolute.left-0 92.5x1.0 bg #1b1b1b; div.flex.h-[18px] 40.2x18.0 bg #fae210 r 8px; div.absolute.left-0 100.5x1.0 bg #1b1b1b |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The BYBORRE wordmark anchor (an img inside the home link).

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 98.66 x 15.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. The Textile Room header link (with the New badge inside it).

Page: home. Selector: `header a Textile Room`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152.67 x 28 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Helvetica Neue 16px/20px 400, #1b1b1b | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.absolute.left-0 92.5x1.0 bg #1b1b1b; div.flex.h-[18px] 40.2x18.0 bg #fae210 r 8px | = | a.relative.group 152.7x28.0 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 92.5x1.0 bg #1b1b1b; div.flex.h-[18px] 40.2x18.0 bg #fae210 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-badge

Nav badge. The yellow "New" chip inside the Textile Room link.

Page: home. Selector: `header .bg-yellow chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 24.22 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 12px/12px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up div.flex.h-[18px] bg #fae210 |
| How | at rest |

Crops: `nav-badge-default.png`.

#### nav-trigger

Nav trigger. The About button that opens the header flyout; toggled, never followed.

Page: home. Selector: `header button About`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84.98 x 28 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Helvetica Neue 16px/20px 400, #1b1b1b | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.absolute.left-0 69.0x1.0 bg #1b1b1b; span.iconify.i-mdi:plus 18.0x18.0 bg #1b1b1b | = | button.relative.group 85.0x28.0 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 69.0x1.0 bg #1b1b1b; span.iconify.i-mdi:plus 18.0x18.0 bg #1b1b1b | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### cart-button

Cart button. The icon-only cart action; opens the cart drawer (a local toggle).

Page: home. Selector: `header button[aria-label=Cart]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 4px | = | = | = |
| Border | 1px solid #ccccc4 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #ccccc4 | = | #000000 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Helvetica Neue 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.flex 32.0x32.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.iconify.i-mdi:shopping-outline 18.0x18.0 bg #1b1b1b; span.absolute.bottom-[6px] 0.0x0.0 bg #4caf50 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 9999px | button.relative.flex 32.0x32.0 bg #ccccc4 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.iconify.i-mdi:shopping-outline 18.0x18.0 bg #1b1b1b; span.absolute.bottom-[6px] 0.0x0.0 bg #4caf50 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 9999px | button.relative.flex 32.0x32.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px outline 1px auto #005fcc offset 0px; span.iconify.i-mdi:shopping-outline 18.0x18.0 bg #1b1b1b; span.absolute.bottom-[6px] 0.0x0.0 bg #4caf50 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 9999px | button.relative.flex 32.0x32.0 bg #000000 @ 0.1 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.iconify.i-mdi:shopping-outline 18.0x18.0 bg #1b1b1b; span.absolute.bottom-[6px] 0.0x0.0 bg #4caf50 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cart-button-default.png`, `cart-button-hover.png`, `cart-button-focus-visible.png`, `cart-button-pressed.png`.

#### account-button

Account button. The icon-only account action that opens the login dialog; measured, never followed.

Page: home. Selector: `header account icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 31.36 x 31.36 |
| Padding | 0px | = | = | = |
| Border | 1px solid #ccccc4 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #000000 @ 0.1 | = | #000000 @ 0.1 |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.group 32.0x32.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.iconify.i-mdi:account-outline 18.0x18.0 bg #1b1b1b | button.relative.group 32.0x32.0 bg #000000 @ 0.1 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.iconify.i-mdi:account-outline 18.0x18.0 bg #1b1b1b | button.relative.group 32.0x32.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; span.iconify.i-mdi:account-outline 18.0x18.0 bg #1b1b1b | button.relative.group 31.4x31.4 bg #000000 @ 0.1 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.iconify.i-mdi:account-outline 17.6x17.6 bg #1b1b1b |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `account-button-default.png`, `account-button-hover.png`, `account-button-focus-visible.png`, `account-button-pressed.png`.

#### nav-dropdown

Nav flyout. The About flyout panel (link column plus the two image cards), opened by hovering its own trigger.

Page: home. Selector: `header flyout panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1408 x 210 |
| Padding | 24px |
| Border | 1px solid #888888 |
| Radius | 0px |
| Background | #f5f5f0 |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span: Helvetica Neue 16px/20px 400, #1b1b1b |
| Transition | none |
| Painted layers | div.left-0.top-0 1408.0x210.0 bg #f5f5f0 border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888; div.absolute.left-0 107.0x1.0 bg #1b1b1b; div.absolute.left-0 99.9x1.0 bg #1b1b1b; div.absolute.left-0 115.9x1.0 bg #1b1b1b; a.relative.group 154.4x32.0 bg #f5f5f0 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 10px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #1b1b1b |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Flyout link. A link inside the opened About flyout.

Page: home. Selector: `flyout link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123 x 28 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Helvetica Neue 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Helvetica Neue 16px/20px 400, #1b1b1b | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.absolute.left-0 107.0x1.0 bg #1b1b1b | = | a.relative.group 123.0x28.0 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 107.0x1.0 bg #1b1b1b | a.relative.group 123.0x28.0 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 107.0x1.0 bg #1b1b1b |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

#### flyout-card

Flyout card. An image card inside the About flyout (the card whose caption is "Go to Textile Room"); measured, never followed.

Page: home. Selector: `flyout image card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280 x 160 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Helvetica Neue 13px/19.5px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1b1b1b | = | - | = |
| Text node | p.mb-4.text-base: Helvetica Neue 16px/24px 400, #e5e5e1 | = | - | = |
| Transition | none | = | - | = |
| Painted layers | a.relative.group 154.4x32.0 bg #f5f5f0 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 10px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #1b1b1b | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `flyout-card-default.png`, `flyout-card-hover.png`, `flyout-card-pressed.png`.

### Home

#### hero-title

Hero headline. The "Your brand's DNA in every stitch" display headline over the dark hero media.

Page: home. Selector: `display headline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 679 x 168 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 80px/84px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero copy. The lede under the hero headline (white on the dark hero media).

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 679 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 24px/32px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta

Hero CTA. The "Explore samples →" action on the dark hero; measured, never followed.

Page: home. Selector: `hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 182.44 x 48 | = | = | 178.79 x 47.04 |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #f5f5f0 | 1px solid #fae210 | = | 1px solid #fae210 |
| Radius | 10px | = | = | = |
| Background | #f5f5f0 | #fae210 | = | #fae210 |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Helvetica Neue 16px/24px 500, #1b1b1b | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.relative.group 182.4x48.0 bg #f5f5f0 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 10px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #1b1b1b | a.relative.group 182.4x48.0 bg #fae210 border T:1px solid #fae210 / R:1px solid #fae210 / B:1px solid #fae210 / L:1px solid #fae210 r 10px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #1b1b1b | a.relative.group 182.4x48.0 bg #f5f5f0 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 10px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #1b1b1b | a.relative.group 178.8x47.0 bg #fae210 border T:1px solid #fae210 / R:1px solid #fae210 / B:1px solid #fae210 / L:1px solid #fae210 r 10px; span.iconify.i-mdi:arrow-right 17.6x17.6 bg #1b1b1b |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### section-h2

Section heading. A section display heading ("We reprogram tradition" / "BYBORRE is a textile innovation…").

Page: home. Selector: `section display-text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 412.66 x 106 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 48px/53px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Textile Room

#### page-title

Page title. The "Textile Room" display title.

Page: collection. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 592 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 80px/84px 500 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| How | at rest |

Crops: `page-title-default.png`.

#### filter-bar

Filter bar. The sticky colour-filter bar (Select colors, max 3) under the header.

Page: collection. Selector: `div.sticky filter bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 124 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f5f5f0 |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | p.mb-4.text-xs: Helvetica Neue 12px/16px 500, #1b1b1b |
| Transition | none |
| Painted layers | div.sticky.top-0 1440.0x124.0 bg #f5f5f0; div.container.h-full 1408.0x124.0 border R:1px solid #1b1b1b / L:1px solid #1b1b1b; div.relative.flex 1406.0x124.0 border B:1px solid #e5e5e1; label::before.relative.mb-2 32pxx32px border T:1px solid #1b1b1b / R:1px solid #1b1b1b / B:1px solid #1b1b1b / L:1px solid #1b1b1b r 9999px; span.relative.inline-block 26.0x26.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.absolute.left-1/2 22.5x22.5 bg #c94c00 |
| How | at rest |

Crops: `filter-bar-default.png`.

#### colour-chip

Colour filter chip. A colour-filter circle (the label wrapping a colour-select checkbox); a BLUE selection was toggled for the filtered screenshot state, never submitted.

Page: collection. Selector: `label colour chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 3px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Helvetica Neue 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 32px x 32px, absolute, bg #000000 @ 0, radius 9999px | = | = | = |
| Painted layers | label::before.relative.mb-2 32pxx32px border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.relative.inline-block 26.0x26.0 bg #0e4c92 r 9999px | label::before.relative.mb-2 32pxx32px border T:1px solid #999993 / R:1px solid #999993 / B:1px solid #999993 / L:1px solid #999993 r 9999px; span.relative.inline-block 26.0x26.0 bg #0e4c92 r 9999px | label::before.relative.mb-2 32pxx32px border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; input.sr-only 1.0x1.0 outline 1px auto #005fcc offset 2px; span.relative.inline-block 26.0x26.0 bg #0e4c92 r 9999px | label::before.relative.mb-2 32pxx32px border T:1px solid #999993 / R:1px solid #999993 / B:1px solid #999993 / L:1px solid #999993 r 9999px; span.relative.inline-block 26.0x26.0 bg #0e4c92 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `colour-chip-default.png`, `colour-chip-hover.png`, `colour-chip-focus-visible.png`, `colour-chip-pressed.png`.

#### filter-toggle

Filter toggle. The "Show all filters" expander on the filter bar; present in the DOM but rendered 0x0 at desktop width, so it records missing rather than a phantom measurement.

Page: collection. Selector: `button Show all filters`. States: .

Not found on the page at capture time.

#### textile-card

Textile card. A textile card in the Textile Room grid (name, price, Configure textile / Order actions); measured, never followed.

Page: collection. Selector: `a[href*="/collection/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 321.5 x 357.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #00e606 offset 1px | = |
| Font | Helvetica Neue 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span.text-xs.font-normal: Helvetica Neue 12px/16px 400, #f5f5f0 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.relative.mb-3 321.5x321.5 bg #d1d1d1 r 10px; div.inline-flex.items-center 87.8x24.0 bg #000000 @ 0.2 r 9999px outline 1px solid #999993 offset -1px; div.absolute.inset-0 321.5x321.5 bg #000000 @ 0.3; button.relative.group 32.0x32.0 bg #f5f5f0 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 9999px; span.iconify.i-mdi:shopping-outline 18.0x18.0 bg #1b1b1b | = | a 321.5x357.5 outline 1px auto #00e606 offset 1px; div.relative.mb-3 321.5x321.5 bg #d1d1d1 r 10px; div.inline-flex.items-center 87.8x24.0 bg #000000 @ 0.2 r 9999px outline 1px solid #999993 offset -1px; div.absolute.inset-0 321.5x321.5 bg #000000 @ 0.3; button.relative.group 32.0x32.0 bg #f5f5f0 border T:1px solid #f5f5f0 / R:1px solid #f5f5f0 / B:1px solid #f5f5f0 / L:1px solid #f5f5f0 r 9999px; span.iconify.i-mdi:shopping-outline 18.0x18.0 bg #1b1b1b | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `textile-card-default.png`, `textile-card-hover.png`, `textile-card-focus-visible.png`, `textile-card-pressed.png`.

#### pattern-dropdown

Pattern dropdown. The Pattern filter trigger on the collection filter bar; measured closed, never opened.

Page: collection. Selector: `button Pattern`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160 x 32 | = | = | 156.8 x 31.36 |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #ccccc4 | = | = | = |
| Radius | 10px | = | = | = |
| Background | #ffffff | #000000 @ 0.1 | = | #000000 @ 0.1 |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Helvetica Neue 12px/16px 500, #1b1b1b | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.group 160.0x32.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px; span.iconify.i-mdi:chevron-down 18.0x18.0 bg #1b1b1b | button.relative.group 160.0x32.0 bg #000000 @ 0.1 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px; span.iconify.i-mdi:chevron-down 18.0x18.0 bg #1b1b1b | button.relative.group 160.0x32.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; span.iconify.i-mdi:chevron-down 18.0x18.0 bg #1b1b1b | button.relative.group 156.8x31.4 bg #000000 @ 0.1 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px; span.iconify.i-mdi:chevron-down 17.6x17.6 bg #1b1b1b |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `pattern-dropdown-default.png`, `pattern-dropdown-hover.png`, `pattern-dropdown-focus-visible.png`, `pattern-dropdown-pressed.png`.

### Textile detail

#### textile-title

Textile name. The textile product title.

Page: textile. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 639 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 48px/48px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| How | at rest |

Crops: `textile-title-default.png`.

#### view-tab

View tab. A product-view tab (Sample / Textile repeat / Sofa / Couch / Room divider); the Room-divider state is toggled for the screenshot.

Page: textile. Selector: `view tab button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #ccccc4 | = | = | = |
| Radius | 10px | = | = | = |
| Background | #f5f5f0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Helvetica Neue 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span.mb-[-3px]: Helvetica Neue 13px/13px 400, #1b1b1b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.min-w-56 224.0x36.0 bg #f5f5f0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px; span.iconify.i-mdi:plus 18.0x18.0 bg #999993 | = | button.inline-flex.min-w-56 224.0x36.0 bg #f5f5f0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px outline 1px auto #005fcc offset 0px; span.iconify.i-mdi:plus 18.0x18.0 bg #999993 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `view-tab-default.png`, `view-tab-hover.png`, `view-tab-focus-visible.png`, `view-tab-pressed.png`.

#### order-cta

Order CTA. The "Order free sample" action; measured, never pressed — it would mutate the cart.

Page: textile. Selector: `button Order sample`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 425 x 48 | = | = | 416.5 x 47.04 |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #1b1b1b | 1px solid #c8b50d | = | 1px solid #c8b50d |
| Radius | 10px | = | = | = |
| Background | #1b1b1b | #fae210 | = | #fae210 |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f5f5f0 | #1b1b1b | = | #1b1b1b |
| Text node | span: Helvetica Neue 16px/24px 500, #f5f5f0 | span: Helvetica Neue 16px/24px 500, #1b1b1b | = | span: Helvetica Neue 16px/24px 500, #1b1b1b |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.group 425.0x48.0 bg #1b1b1b border T:1px solid #1b1b1b / R:1px solid #1b1b1b / B:1px solid #1b1b1b / L:1px solid #1b1b1b r 10px | button.relative.group 425.0x48.0 bg #fae210 border T:1px solid #c8b50d / R:1px solid #c8b50d / B:1px solid #c8b50d / L:1px solid #c8b50d r 10px | button.relative.group 425.0x48.0 bg #1b1b1b border T:1px solid #1b1b1b / R:1px solid #1b1b1b / B:1px solid #1b1b1b / L:1px solid #1b1b1b r 10px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | button.relative.group 416.5x47.0 bg #fae210 border T:1px solid #c8b50d / R:1px solid #c8b50d / B:1px solid #c8b50d / L:1px solid #c8b50d r 10px |
| Ancestor paint | 1 up div.textile-call-to-action.sticky bg #f5f5f0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `order-cta-default.png`, `order-cta-hover.png`, `order-cta-focus-visible.png`, `order-cta-pressed.png`.

#### swatch

Colourway swatch. A colourway selector (sr-only inputs behind swatch labels) on the detail page.

Page: textile. Selector: `colourway swatch`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145.7 x 28 | = | = | = |
| Padding | 4px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Helvetica Neue 16px/20px 400, #1b1b1b | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.absolute.left-0 129.7x1.0 bg #1b1b1b; span.iconify.i-mdi:plus 18.0x18.0 bg #1b1b1b | = | button.relative.group 145.7x28.0 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 129.7x1.0 bg #1b1b1b; span.iconify.i-mdi:plus 18.0x18.0 bg #1b1b1b | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `swatch-default.png`, `swatch-hover.png`, `swatch-focus-visible.png`, `swatch-pressed.png`.

#### spec-row

Spec row. A row in the Textile-details block (composition, weight, width).

Page: textile. Selector: `detail row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 84 x 200 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up button.group.relative shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 40px 0px |
| How | at rest |

Crops: `spec-row-default.png`.

### Login dialog

#### login-dialog

Login dialog. The "Log in to continue" dialog that gates the Design Studio; captured open, never filled or submitted.

Page: login. Selector: `login dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 648 |
| Padding | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | h3: Helvetica Neue 40px/42px 400, #1b1b1b |
| Transition | none |
| Painted layers | input.h-12.w-full 356.0x48.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px; input.h-12.w-full 356.0x48.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px; button.relative.group 356.0x48.0 bg #1b1b1b border T:1px solid #1b1b1b / R:1px solid #1b1b1b / B:1px solid #1b1b1b / L:1px solid #1b1b1b r 10px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #f5f5f0 |
| Ancestor paint | 3 up div.relative.text-left bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| How | at rest |

Crops: `login-dialog-default.png`.

#### login-email

Email field. The login email input; focused and given sample text that was deleted again — nothing sent.

Page: login. Selector: `input[name=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 356 x 48 | = | = |
| Padding | 0px 12px | = | = |
| Border | 1px solid #ccccc4 | 1px solid #888888 | 1px solid #888888 |
| Radius | 10px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Helvetica Neue 16px/45.712px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1b | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #646e69, opacity 1 | = | = |
| Painted layers | input.h-12.w-full 356.0x48.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px | input.h-12.w-full 356.0x48.0 bg #ffffff border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888 r 10px shadow #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.h-12.w-full 356.0x48.0 bg #ffffff border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888 r 10px shadow #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-password

Password field. The login password input; focused only, never typed into.

Page: login. Selector: `input[name=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 356 x 48 | = |
| Padding | 0px 12px | = |
| Border | 1px solid #ccccc4 | 1px solid #888888 |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | Helvetica Neue 16px/45.712px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1b | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #646e69, opacity 1 | = |
| Painted layers | input.h-12.w-full 356.0x48.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px | input.h-12.w-full 356.0x48.0 bg #ffffff border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888 r 10px shadow #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `login-password-default.png`, `login-password-focused.png`.

#### login-button

Login button. The dialog's Login action; measured, never pressed.

Page: login. Selector: `login submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 356 x 48 | = | = | 348.88 x 47.04 |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #1b1b1b | 1px solid #c8b50d | = | 1px solid #c8b50d |
| Radius | 10px | = | = | = |
| Background | #1b1b1b | #fae210 | = | #fae210 |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f5f5f0 | #1b1b1b | = | #1b1b1b |
| Text node | span: Helvetica Neue 16px/24px 500, #f5f5f0 | span: Helvetica Neue 16px/24px 500, #1b1b1b | = | span: Helvetica Neue 16px/24px 500, #1b1b1b |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.group 356.0x48.0 bg #1b1b1b border T:1px solid #1b1b1b / R:1px solid #1b1b1b / B:1px solid #1b1b1b / L:1px solid #1b1b1b r 10px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #f5f5f0 | button.relative.group 356.0x48.0 bg #fae210 border T:1px solid #c8b50d / R:1px solid #c8b50d / B:1px solid #c8b50d / L:1px solid #c8b50d r 10px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #1b1b1b | button.relative.group 356.0x48.0 bg #1b1b1b border T:1px solid #1b1b1b / R:1px solid #1b1b1b / B:1px solid #1b1b1b / L:1px solid #1b1b1b r 10px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; span.iconify.i-mdi:arrow-right 18.0x18.0 bg #f5f5f0 | button.relative.group 348.9x47.0 bg #fae210 border T:1px solid #c8b50d / R:1px solid #c8b50d / B:1px solid #c8b50d / L:1px solid #c8b50d r 10px; span.iconify.i-mdi:arrow-right 17.6x17.6 bg #1b1b1b |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `login-button-default.png`, `login-button-hover.png`, `login-button-focus-visible.png`, `login-button-pressed.png`.

#### signup-link

Sign-up link. The "Don't have an account? Sign up" link; measured, never followed.

Page: login. Selector: `sign up link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 54.84 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Helvetica Neue 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | #646e69 | = | #646e69 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.bg-transparent.underline 54.8x24.0 outline 1px auto #005fcc offset 0px | = |

Crops: `signup-link-default.png`, `signup-link-hover.png`, `signup-link-focus-visible.png`, `signup-link-pressed.png`.

#### forgot-link

Forgot-password link. The forgot-password link inside the dialog; measured, never followed.

Page: login. Selector: `forgot password link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 129.92 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Helvetica Neue 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #646e69 | #000000 | = | #000000 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.mt-4.bg-transparent 129.9x24.0 outline 1px auto #005fcc offset 0px | = |

Crops: `forgot-link-default.png`, `forgot-link-hover.png`, `forgot-link-focus-visible.png`, `forgot-link-pressed.png`.

### FAQ

#### faq-title

FAQ title. The FAQ page title and a section heading (Textile information).

Page: faq. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 592 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 80px/84px 500 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| How | at rest |

Crops: `faq-title-default.png`.

#### faq-question

FAQ question. An accordion question row; toggled open for the opened state and the screenshot.

Page: faq. Selector: `button question`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 719 x 56 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Helvetica Neue 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span.-mt-[5px].block: Helvetica Neue 16px/24px 400, #1b1b1b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.iconify.i-mdi:plus 24.0x24.0 bg #999993 | = | button.w-full.px-4 719.0x56.0 outline 1px auto #005fcc offset 0px; span.iconify.i-mdi:plus 24.0x24.0 bg #999993 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-pressed.png`.

### Contact form

#### contact-title

Contact title. The "Contact us" heading.

Page: contact. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 647 x 168 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 80px/84px 500 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| How | at rest |

Crops: `contact-title-default.png`.

#### text-field

Text field. The First-name input; focused and given sample text that was deleted again — nothing sent.

Page: contact. Selector: `input[name=firstname]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 623 x 48 | = | = |
| Padding | 0px 12px | = | = |
| Border | 1px solid #ccccc4 | 1px solid #888888 | 1px solid #888888 |
| Radius | 10px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Helvetica Neue 16px/45.712px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1b1b1b | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #646e69, opacity 1 | = | = |
| Painted layers | input.h-12.w-full 623.0x48.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px | input.h-12.w-full 623.0x48.0 bg #ffffff border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888 r 10px shadow #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | input.h-12.w-full 623.0x48.0 bg #ffffff border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888 r 10px shadow #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `text-field-default.png`, `text-field-focused.png`, `text-field-filled.png`.

#### email-field

Email field. The Email input on the contact form; focused only.

Page: contact. Selector: `input[name=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 623 x 48 | = |
| Padding | 0px 12px | = |
| Border | 1px solid #ccccc4 | 1px solid #888888 |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | Helvetica Neue 16px/45.712px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1b | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #646e69, opacity 1 | = |
| Painted layers | input.h-12.w-full 623.0x48.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px | input.h-12.w-full 623.0x48.0 bg #ffffff border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888 r 10px shadow #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `email-field-default.png`, `email-field-focused.png`.

#### select-field

Select. The inquiry-type select; focused only, never changed.

Page: contact. Selector: `select[name=inquiry]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 623 x 48 | = |
| Padding | 0px 12px | = |
| Border | 1px solid #ccccc4 | 1px solid #888888 |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | Helvetica Neue 16px/45.712px 400 | = |
| Letter spacing | normal | = |
| Colour | #646e69 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | select.h-12.w-full 623.0x48.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px | select.h-12.w-full 623.0x48.0 bg #ffffff border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888 r 10px shadow #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `select-field-default.png`, `select-field-focused.png`.

#### text-area

Text area. The project-description textarea; focused only, never typed into.

Page: contact. Selector: `textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 623 x 104 | = |
| Padding | 6px 12px 0px 12px | = |
| Border | 1px solid #ccccc4 | 1px solid #888888 |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px |
| Font | Helvetica Neue 16px/32px 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b1b | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #646e69, opacity 1 | = |
| Painted layers | textarea.w-full.rounded-[7px] 623.0x104.0 bg #ffffff border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 10px | textarea.w-full.rounded-[7px] 623.0x104.0 bg #ffffff border T:1px solid #888888 / R:1px solid #888888 / B:1px solid #888888 / L:1px solid #888888 r 10px shadow #ffffff 0px 0px 0px 0px, #888888 @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field |

Crops: `text-area-default.png`, `text-area-focused.png`.

#### submit-button

Submit button. The form's Send action; measured, never pressed.

Page: contact. Selector: `form submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.44 x 48 | = | = | 84.71 x 47.04 |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #1b1b1b | 1px solid #c8b50d | = | 1px solid #c8b50d |
| Radius | 10px | = | = | = |
| Background | #1b1b1b | #fae210 | = | #fae210 |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f5f5f0 | #1b1b1b | = | #1b1b1b |
| Text node | span: Helvetica Neue 16px/24px 500, #f5f5f0 | span: Helvetica Neue 16px/24px 500, #1b1b1b | = | span: Helvetica Neue 16px/24px 500, #1b1b1b |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.group 86.4x48.0 bg #1b1b1b border T:1px solid #1b1b1b / R:1px solid #1b1b1b / B:1px solid #1b1b1b / L:1px solid #1b1b1b r 10px | button.relative.group 86.4x48.0 bg #fae210 border T:1px solid #c8b50d / R:1px solid #c8b50d / B:1px solid #c8b50d / L:1px solid #c8b50d r 10px | button.relative.group 86.4x48.0 bg #1b1b1b border T:1px solid #1b1b1b / R:1px solid #1b1b1b / B:1px solid #1b1b1b / L:1px solid #1b1b1b r 10px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | button.relative.group 84.7x47.0 bg #fae210 border T:1px solid #c8b50d / R:1px solid #c8b50d / B:1px solid #c8b50d / L:1px solid #c8b50d r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `submit-button-default.png`, `submit-button-hover.png`, `submit-button-focus-visible.png`, `submit-button-pressed.png`.

#### person-card

Contact person. A named contact block (name, role) on the contact page.

Page: contact. Selector: `contact person block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 286.5 x 152 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | h2.mb-2.text-3xl: Helvetica Neue 40px/44px 400, #1b1b1b |
| Transition | none |
| How | at rest |

Crops: `person-card-default.png`.

### Footer

#### footer

Footer. The page footer: link columns, social links, legal and newsletter copy.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 537.14 |
| Padding | 0px |
| Border | none |
| Radius | 24px 24px 0px 0px |
| Background | #1b1b1b |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.pt-1: Helvetica Neue 10px/15px 400, #ffffff |
| Transition | none |
| Icon | 696 x 199.64, colour #ffffff, fill #000000 |
| Painted layers | footer.relative.z-10 1440.0x537.1 bg #1b1b1b r 24px 24px 0px 0px; div.container.flex 1440.0x292.6 border B:1px solid #454542; div.absolute.left-0 107.1x1.0 bg #1b1b1b; div.absolute.left-0 80.5x1.0 bg #1b1b1b; div.absolute.left-0 88.5x1.0 bg #1b1b1b; div.absolute.left-0 0.0x0.0 bg #1b1b1b |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 107.06 x 20.5 | = | = | = |
| Padding | 4px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 10px/12.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Helvetica Neue 10px/12.5px 400, #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.absolute.left-0 107.1x1.0 bg #1b1b1b | = | a.relative.group 107.1x20.5 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 107.1x1.0 bg #1b1b1b | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Helvetica Neue 16px/24px 400, #ffffff | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.absolute.left-0 0.0x0.0 bg #1b1b1b | = | a.relative.group 150.0x24.0 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 0.0x0.0 bg #1b1b1b | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | #f5f5f0 |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| Painted layers | header.sticky.left-0 390.0x64.0 bg #f5f5f0; div.flex.w-full 230.0x32.0 bg #f5f5f0; div.absolute.left-0 0.0x0.0 bg #1b1b1b; div.flex.h-[18px] 0.0x0.0 bg #fae210 r 8px; div.absolute.left-0 0.0x0.0 bg #1b1b1b; div.absolute.left-0 0.0x0.0 bg #1b1b1b |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The burger toggle that opens the mobile menu.

Page: mobile. Selector: `button[aria-label=Open menu]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | 1px solid #ccccc4 |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 12px/16px 500 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | button.relative.group 32.0x32.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 9999px; span.iconify.i-mdi:menu 18.0x18.0 bg #1b1b1b |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The opened mobile menu panel (the aside that slides over the page).

Page: mobile. Selector: `aside mobile menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 64px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | #f5f5f0 |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 13px/19.5px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span: Helvetica Neue 16px/24px 500, #1b1b1b |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | aside.fixed.inset-x-0 390.0x844.0 bg #f5f5f0; button.relative.group 358.0x50.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 8px; div.absolute.left-0 0.0x0.0 bg #1b1b1b; span.iconify.i-mdi:shopping-outline 18.0x18.0 bg #1b1b1b; button.relative.group 358.0x50.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 8px; div.absolute.left-0 0.0x0.0 bg #1b1b1b |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A link inside the opened mobile menu.

Page: mobile. Selector: `mobile menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 48 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Helvetica Neue 16px/24px 500, #1b1b1b | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.absolute.left-0 0.0x0.0 bg #1b1b1b; div.flex.h-[18px] 40.7x18.0 bg #fae210 r 8px | = | a.relative.group 358.0x48.0 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 0.0x0.0 bg #1b1b1b; div.flex.h-[18px] 40.7x18.0 bg #fae210 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `display headline at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Helvetica Neue 48px/48px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-login-button

Mobile login button. The Login/Sign-up row inside the mobile menu; opens the login dialog, measured never followed.

Page: mobile. Selector: `mobile menu login row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 358 x 50 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Border | 1px solid #ccccc4 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Helvetica Neue 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Helvetica Neue 16px/24px 500, #1b1b1b | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.relative.group 358.0x50.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 8px; div.absolute.left-0 0.0x0.0 bg #1b1b1b; span.iconify.i-mdi:account-outline 18.0x18.0 bg #1b1b1b | = | button.relative.group 358.0x50.0 border T:1px solid #ccccc4 / R:1px solid #ccccc4 / B:1px solid #ccccc4 / L:1px solid #ccccc4 r 8px shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; div.absolute.left-0 0.0x0.0 bg #1b1b1b; span.iconify.i-mdi:account-outline 18.0x18.0 bg #1b1b1b | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-login-button-default.png`, `m-login-button-hover.png`, `m-login-button-focus-visible.png`, `m-login-button-pressed.png`.

## Transitions declared in the readable stylesheets

byborre.com serves its Nuxt CSS bundle same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- collection: `opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, `0.5s ease-in-out`, `0.3s ease-in-out`, `opacity 0.3s`, `opacity 0.2s`, `max-height 0.3s ease-in-out`, `opacity 0.3s ease-out, transform 0.5s ease-out`, `opacity 0.3s ease-in, transform 0.5s ease-in`

- contact: `opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, `0.5s ease-in-out`, `0.3s ease-in-out`, `opacity 0.3s`, `0.2s`, `opacity 0.2s`

- faq: `opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, `0.5s ease-in-out`, `0.3s ease-in-out`, `opacity 0.3s`, `opacity 0.2s`

- home: `opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, `0.5s ease-in-out`, `0.3s ease-in-out`, `opacity 0.3s`, `opacity 0.2s`

- login: `opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, `0.5s ease-in-out`, `0.3s ease-in-out`, `opacity 0.3s`, `opacity 0.2s`

- textile: `opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1), transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1)`, `0.5s ease-in-out`, `0.3s ease-in-out`, `opacity 0.3s`, `opacity 0.3s ease-out, transform 0.5s ease-out`, `opacity 0.3s ease-in, transform 0.5s ease-in`, `max-height 0.3s ease-in-out`, `opacity 0.2s`
