# Component measurements

Computed styles read from www.krea.ai on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home, /pricing, /enterprise, /blog, /plugins, /login and /image, and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### App shell

#### sidebar

Sidebar. The signed-out app sidebar: Home, Agent, Train, Nodes, Assets, tool links, Pricing, Enterprise, Sign in. About 256px, near-black.

Page: home. Selector: `sidebar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 255 x 622 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.985 0 0) |
| Text node | span.truncate: Suisse Intl 14px/20px 400, oklch(0.985 0 0) |
| Transition | none |
| Icon | 12 x 12, colour oklch(0.985 0 0) |
| Painted layers | a.peer/menu-button.ring-sidebar-ring 239.0x36.0 bg oklch(0.269 0 0) r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 0.5px inset, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest |

Crops: `sidebar-default.png`.

#### sidebar-toggle

Sidebar toggle. The "Toggle Sidebar" icon button. A local fold control.

Page: home. Selector: `button[aria-label="Toggle Sidebar"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | oklch(0.269 0 0) | = | oklch(0.269 0 0) |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 14px/20px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.708 0 0) | oklch(0.985 0 0) | = | oklch(0.985 0 0) |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour oklch(0.708 0 0) | 20 x 20, colour oklch(0.985 0 0) | = | 20 x 20, colour oklch(0.985 0 0) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.focus-visible:border-ring.focus-visible:ring-ring/50 36.0x36.0 bg oklch(0.269 0 0) r 10px | button.focus-visible:border-ring.focus-visible:ring-ring/50 36.0x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.focus-visible:border-ring.focus-visible:ring-ring/50 36.0x36.0 bg oklch(0.269 0 0) r 10px |

Crops: `sidebar-toggle-default.png`, `sidebar-toggle-hover.png`, `sidebar-toggle-focus-visible.png`, `sidebar-toggle-pressed.png`.

#### nav-home

Sidebar home link. The Home item in the sidebar. Selected at rest (data-active).

Page: home. Selector: `a[aria-label="Home"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 239 x 36 | = | = | 234.22 x 35.28 |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | oklch(0.269 0 0) | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 0.5px inset, #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.985 0 0) | = | = | = |
| Text node | span.truncate: Suisse Intl 14px/20px 400, oklch(0.985 0 0) | = | = | = |
| Transition | width, height, padding, transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.peer/menu-button.ring-sidebar-ring 239.0x36.0 bg oklch(0.269 0 0) r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 0.5px inset, #000000 @ 0.05 0px 1px 2px 0px | = | = | a.peer/menu-button.ring-sidebar-ring 234.2x35.3 bg oklch(0.269 0 0) r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 0.5px inset, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `nav-home-default.png`, `nav-home-hover.png`, `nav-home-focus-visible.png`, `nav-home-pressed.png`.

#### nav-pricing

Pricing link. The sidebar Pricing link, including the yearly-discount badge. Measured, never followed from this spec.

Page: home. Selector: `a[href="/pricing"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 239 x 36 | = | = | 234.22 x 35.28 |
| Padding | 0px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | T: 1px solid #ffffff @ 0.5; R: none; B: none; L: none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | oklch(0.269 0 0) | = | oklch(0.269 0 0) |
| Background image | linear-gradient(to right, oklch(0.932 0.032 255.585) 0%, oklch(0.809 0.105 251.813) 50%, oklch(0.424 0.199 265.638) 100%) | = | = | = |
| Box shadow | #7e70db @ 0.3 0px 0px 12px -2px, #70a0db @ 0.2 0px 0px 20px -4px, #ffffff @ 0.2 0px 0px 6px 0px inset | = | = | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.379 0.146 265.522) | = | = | = |
| Text node | span.min-w-0.flex-1: Suisse Intl 14px/20px 400, oklch(0.379 0.146 265.522) | = | = | = |
| Transition | margin, opacity, transform 0.15s cubic-bezier(0.2, 0, 0, 1) delay 0.075s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 239px x 35px, absolute, bg #000000 @ 0, radius 10px, shadow #8b7de8 @ 0.5 0px 0px 10px 0px, #7e70db @ 0.3 0px 0px 20px 0px, #ffffff @ 0.3 0px 0px 8px 0px inset | = | = | = |
| Painted layers | a.ring-sidebar-ring.flex 239.0x36.0 image linear-gradient(to right, oklch(0.932 0.032 255.585) 0%, oklch(0.809 0.105 251.813) 50%, o border T:1px solid #ffffff @ 0.5 r 10px shadow #7e70db @ 0.3 0px 0px 12px -2px, #70a0db @ 0.2 0px 0px 20px -4px, #ffffff @ 0.2 0px 0px 6px 0px inset; a::after.ring-sidebar-ring.flex 239pxx35px r 10px shadow #8b7de8 @ 0.5 0px 0px 10px 0px, #7e70db @ 0.3 0px 0px 20px 0px, #ffffff @ 0.3 0px 0px 8px 0px inset; span.focus-visible:border-ring.focus-visible:ring-ring/50 90.6x21.0 bg #103a93 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a.ring-sidebar-ring.flex 239.0x36.0 bg oklch(0.269 0 0) image linear-gradient(to right, oklch(0.932 0.032 255.585) 0%, oklch(0.809 0.105 251.813) 50%, o border T:1px solid #ffffff @ 0.5 r 10px shadow #7e70db @ 0.3 0px 0px 12px -2px, #70a0db @ 0.2 0px 0px 20px -4px, #ffffff @ 0.2 0px 0px 6px 0px inset; a::after.ring-sidebar-ring.flex 239pxx35px r 10px shadow #8b7de8 @ 0.5 0px 0px 10px 0px, #7e70db @ 0.3 0px 0px 20px 0px, #ffffff @ 0.3 0px 0px 8px 0px inset; span.focus-visible:border-ring.focus-visible:ring-ring/50 90.6x21.0 bg #103a93 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | a.ring-sidebar-ring.flex 234.2x35.3 bg oklch(0.269 0 0) image linear-gradient(to right, oklch(0.932 0.032 255.585) 0%, oklch(0.809 0.105 251.813) 50%, o border T:1px solid #ffffff @ 0.5 r 10px shadow #7e70db @ 0.3 0px 0px 12px -2px, #70a0db @ 0.2 0px 0px 20px -4px, #ffffff @ 0.2 0px 0px 6px 0px inset; a::after.ring-sidebar-ring.flex 239pxx35px r 10px shadow #8b7de8 @ 0.5 0px 0px 10px 0px, #7e70db @ 0.3 0px 0px 20px 0px, #ffffff @ 0.3 0px 0px 8px 0px inset; span.focus-visible:border-ring.focus-visible:ring-ring/50 88.8x20.6 bg #103a93 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### nav-signin

Sign in. The white sidebar Sign in button. Measured, never followed. It opens /login.

Page: home. Selector: `button Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 239 x 48 | = | = | 234.22 x 47.04 |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | oklch(0.985 0 0) | #e5e5e5 | = | #e5e5e5 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.145 0 0) | = | = | = |
| Text node | span.block.truncate: Suisse Intl 14px/20px 400, oklch(0.145 0 0) | = | = | = |
| Transition | background-color, transform 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour oklch(0.145 0 0) | = | = | = |
| Painted layers | button.peer/menu-button.text-foreground 239.0x48.0 bg oklch(0.985 0 0) r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px | button.peer/menu-button.text-foreground 239.0x48.0 bg #e5e5e5 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px | button.peer/menu-button.text-foreground 239.0x48.0 bg oklch(0.985 0 0) r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.peer/menu-button.text-foreground 234.2x47.0 bg #e5e5e5 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### tools-button

Tools menu button. The Tools button that opens the tool list. A local menu toggle.

Page: home. Selector: `button Tools`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 239 x 36 | = | = | 234.22 x 35.28 | = |
| Padding | 0px 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 10px | = | = | = | = |
| Background | transparent | oklch(0.269 0 0) | = | oklch(0.269 0 0) | oklch(0.269 0 0) |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.439 0 0) 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | Suisse Intl 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #fafafa @ 0.3 | = | = | = | = |
| Transition | margin, opacity, transform 0.15s cubic-bezier(0.2, 0, 0, 1) delay 0.075s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | button.text-sidebar-foreground/30.ring-sidebar-ring 239.0x36.0 bg oklch(0.269 0 0) r 10px | button.text-sidebar-foreground/30.ring-sidebar-ring 239.0x36.0 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.439 0 0) 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.text-sidebar-foreground/30.ring-sidebar-ring 234.2x35.3 bg oklch(0.269 0 0) r 10px | button.text-sidebar-foreground/30.ring-sidebar-ring 239.0x36.0 bg oklch(0.269 0 0) r 10px |
| Transform | - | = | = | matrix(0.98, 0, 0, 0.98, 0, 0) | = |

Crops: `tools-button-default.png`, `tools-button-hover.png`, `tools-button-focus-visible.png`, `tools-button-pressed.png`, `tools-button-opened.png`.

#### search-button

Search button. The sidebar Search control. Measured at rest. Opening the command palette and submitting a query are not done here.

Page: home. Selector: `button Search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | 19 x 19 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | oklch(0.269 0 0) | = | oklch(0.269 0 0) |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.439 0 0) 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.985 0 0) | = | = | = |
| Transition | transform 0.15s ease-out | = | = | = |
| Opacity | 0 | - | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour oklch(0.985 0 0) | = | = | 11.4 x 11.4, colour oklch(0.985 0 0) |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.text-sidebar-foreground.ring-sidebar-ring 20.0x20.0 bg oklch(0.269 0 0) r 6px | button.text-sidebar-foreground.ring-sidebar-ring 20.0x20.0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, oklch(0.439 0 0) 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.text-sidebar-foreground.ring-sidebar-ring 19.0x19.0 bg oklch(0.269 0 0) r 6px |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `search-button-default.png`, `search-button-hover.png`, `search-button-focus-visible.png`, `search-button-pressed.png`.

### Home feed

#### promo-banner

Offer banner. The top offer strip ("Unlimited Nano Banana for 7 days"). A campaign surface, hidden from other shots by closePromo when it is a dismiss overlay. Measured, never claimed.

Page: home. Selector: `offer banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 119.22 x 40 |
| Padding | 0px 24px |
| Gap | 8px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #101010 @ 0.4 |
| Box shadow | none |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | Suisse Intl 14px/20px 450 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| ::after | 119.219px x 40px, absolute, bg #000000 @ 0, radius 3.35544e+07px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0px inset, #ffffff @ 0.25 0px -1px 1px 0px inset, #ffffff @ 0.25 0px 1px 1px 0px inset |
| Painted layers | a.focus-visible:border-ring.focus-visible:ring-ring/50 119.2x40.0 bg #101010 @ 0.4 r 3.35544e+07px; a::after.focus-visible:border-ring.focus-visible:ring-ring/50 119.219pxx40px r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0px inset, #ffffff @ 0.25 0px -1px 1px 0px inset, #ffffff @ 0.25 0px 1px 1px 0px inset |
| Ancestor paint | 3 up div.@container.relative shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.85 0px 0px 32px 0px |
| How | at rest |

Crops: `promo-banner-default.png`.

#### feed-card

Feed card. A published generation card on the signed-out home feed. A public demo, not a signed-in asset.

Page: home. Selector: `a[href^="/feed/"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 362 x 649 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #df9443 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.group/card.relative 362.0x649.0 bg #df9443; div.bg-layer.absolute 362.0x649.0 image image-set(url(…) 1dppx, url(…) 2dppx) | a.group/card.relative 362.0x649.0 bg #df9443; div.bg-layer.absolute 362.0x649.0 image image-set(url(…) 1dppx, url(…) 2dppx); div.eased-gradient-down.pointer-events-none! 362.0x256.0 image linear-gradient(#000000 @ 0.6 0%, #000000 @ 0.592 8.1%, #000000 @ 0.573 15.5%, #000000 @ 0; button.focus-visible:border-ring.focus-visible:ring-ring/50 91.1x36.0 bg oklch(1 0 0) r 3.35544e+07px; button.focus-visible:border-ring.focus-visible:ring-ring/50 36.0x36.0 bg #101010 @ 0.4 r 3.35544e+07px; button::after.focus-visible:border-ring.focus-visible:ring-ring/50 36pxx36px r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0px inset, #ffffff @ 0.25 0px -1px 1px 0px inset, #ffffff @ 0.25 0px 1px 1px 0px inset |
| Ancestor paint | 2 up div.relative.w-full shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.85 0px 0px 32px 0px | = |
| How | at rest | mouse hover |
| Text node | - | span.truncate: Suisse Intl 14px/20px 450, oklch(0 0 0) |
| Icon | - | 16 x 16, colour #ffffff |

Crops: `feed-card-default.png`, `feed-card-hover.png`.

#### announce-card

Announcement card. A model-announcement card on the home feed.

Page: home. Selector: `announcement`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 143.95 x 40 | - |
| Padding | 0px 40px | - |
| Gap | 8px | - |
| Border | none | - |
| Radius | 3.35544e+07px | - |
| Background | #101010 @ 0.4 | - |
| Box shadow | none | - |
| Backdrop filter | blur(8px) | - |
| Outline | none | - |
| Font | Suisse Intl 14px/20px 450 | - |
| Letter spacing | normal | - |
| Colour | #ffffff | - |
| Transition | opacity, scale, background-color 0.5s, 0.15s, 0.15s cubic-bezier(0, 0, 0.2, 1) | - |
| Opacity | 0 | - |
| Cursor | pointer | - |
| ::after | 143.953px x 40px, absolute, bg #000000 @ 0, radius 3.35544e+07px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0px inset, #ffffff @ 0.25 0px -1px 1px 0px inset, #ffffff @ 0.25 0px 1px 1px 0px inset | - |
| Painted layers | button.focus-visible:border-ring.focus-visible:ring-ring/50 144.0x40.0 bg #101010 @ 0.4 r 3.35544e+07px; button::after.focus-visible:border-ring.focus-visible:ring-ring/50 143.953pxx40px r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0px inset, #ffffff @ 0.25 0px -1px 1px 0px inset, #ffffff @ 0.25 0px 1px 1px 0px inset | - |
| How | at rest | - |
| Error | - | locator.hover: Element is outside of the viewport Call log: [2m  - waiting for locator('button, a').filter({ hasText: /Try Krea 3/Read more/ }).filter({ visible: true }).first().filter({ visible: tru |

Crops: `announce-card-default.png`.

#### composer

Home composer. The signed-out prompt ("Describe an idea or upload an image to edit it"). Sample text is typed and deleted. The generate control is never pressed.

Page: home. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 822 x 48 | = | = |
| Padding | 6px 10px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Suisse Intl 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff @ 0.5, opacity 1 | = | = |
| Ancestor paint | 3 up div.group/promptbox.bg-primary-100/85 shadow #000000 @ 0.25 0px 0px 0px 0.5px, #ffffff @ 0.3 0px 0px 0px 0.5px inset, #000000 @ 0.5 0px 18px 50px 0px | 3 up div.group/promptbox.bg-primary-100/85 bg #000000 @ 0.34 shadow #000000 @ 0.25 0px 0px 0px 0.5px, #ffffff @ 0.3 0px 0px 0px 0.5px inset, #000000 @ 0.5 0px 18px 50px 0px | 3 up div.group/promptbox.bg-primary-100/85 bg #000000 @ 0.35 shadow #000000 @ 0.25 0px 0px 0px 0.5px, #ffffff @ 0.3 0px 0px 0px 0.5px inset, #000000 @ 0.5 0px 18px 50px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |
| Painted layers | - | textarea.min-h-[2lh]!.w-full 822.0x48.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | textarea.min-h-[2lh]!.w-full 822.0x48.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |

Crops: `composer-default.png`, `composer-focused.png`, `composer-filled.png`.

#### composer-send

Composer generate. The circular Generate control on the home composer (aria-label Generate). Measured, never clicked. Sending a prompt is a gated generation.

Page: home. Selector: `button[aria-label="Generate"]`. States: .

Not found on the page at capture time.

### Pricing

#### mkt-nav

Marketing nav. The pricing-page top nav: App, Features, Plugins, Image, Video, API, MCP, Pricing, Enterprise, Sign up, Log in.

Page: pricing. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 79.5 |
| Padding | 16px 64px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.15; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.nav-link.rounded-md: Suisse Intl 15px/22.5px 400, #ffffff, ls 0.15px |
| Transition | transform, color, background-color 0.7s, 0.2s, 0.2s cubic-bezier(0.4, 0, 0.2, 1), ease-out, ease-out delay 0s, 0s, 0s |
| Icon | 22 x 22, colour #ffffff |
| Painted layers | header.header.section-container 1440.0x79.5 border B:1px solid #000000 @ 0.15; button.focus-visible:border-ring.focus-visible:ring-ring/50 132.8x36.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 3.35544e+07px; button.focus-visible:border-ring.focus-visible:ring-ring/50 71.6x36.0 bg #262626 r 3.35544e+07px; div.glass-edge.relative 1045.0x514.0 bg #202020 r 24px shadow #000000 @ 0.3 0px 24px 48px -20px; div::after.glass-edge.relative 1100pxx541px r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0px inset, #ffffff @ 0.18 0px -1px 1px 0px inset, #ffffff @ 0.18 0px 1px 1px 0px inset; span::after.tool-icon.glass-edge 40pxx40px r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0px inset, #ffffff @ 0.25 0px -1px 1px 0px inset, #ffffff @ 0.25 0px 1px 1px 0px inset |
| How | at rest |

Crops: `mkt-nav-default.png`.

#### mkt-login

Log in. The marketing Log in control. Measured, never followed. Destination is /login.

Page: pricing. Selector: `Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.61 x 36 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #262626 | #202020 | = | #202020 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 14px/20px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.focus-visible:border-ring.focus-visible:ring-ring/50 71.6x36.0 bg #262626 r 3.35544e+07px | button.focus-visible:border-ring.focus-visible:ring-ring/50 71.6x36.0 bg #202020 r 3.35544e+07px | button.focus-visible:border-ring.focus-visible:ring-ring/50 71.6x36.0 bg #262626 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.focus-visible:border-ring.focus-visible:ring-ring/50 71.6x36.0 bg #202020 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-login-default.png`, `mkt-login-hover.png`, `mkt-login-focus-visible.png`, `mkt-login-pressed.png`.

#### mkt-signup

Sign up for free. The marketing Sign up control. Measured, never followed.

Page: pricing. Selector: `Sign up for free`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132.81 x 36 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #000000 @ 0.2 | = | 1px solid oklch(0.556 0 0) | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 14px/20px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.focus-visible:border-ring.focus-visible:ring-ring/50 132.8x36.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 3.35544e+07px | button.focus-visible:border-ring.focus-visible:ring-ring/50 132.8x36.0 bg #f5f5f5 border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 3.35544e+07px | button.focus-visible:border-ring.focus-visible:ring-ring/50 132.8x36.0 bg #ffffff border T:1px solid oklch(0.556 0 0) / R:1px solid oklch(0.556 0 0) / B:1px solid oklch(0.556 0 0) / L:1px solid oklch(0.556 0 0) r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.focus-visible:border-ring.focus-visible:ring-ring/50 132.8x36.0 bg #f5f5f5 border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mkt-signup-default.png`, `mkt-signup-hover.png`, `mkt-signup-focus-visible.png`, `mkt-signup-pressed.png`.

#### price-h1

Pricing heading. "Pick your plan".

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1184 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 36px/40px 450 |
| Letter spacing | -0.9px |
| Colour | oklch(0.985 0 0) |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-card

Free plan card. The Free plan column on /pricing: $0/month, Get Free.

Page: pricing. Selector: `plan card`. States: .

Not found on the page at capture time.

#### price-pro

Pro plan heading. The Pro plan name.

Page: pricing. Selector: `h2 Pro`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 37.64 x 17.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 24px/32px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 2 up div.home-card.flex bg #000000 @ 0.45 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.85 0px 0px 32px 0px |
| How | at rest |

Crops: `price-pro-default.png`.

#### price-interval

Billing interval. The monthly/yearly toggle on pricing. A local UI toggle, never a checkout.

Page: pricing. Selector: `interval button`. States: default, hover, pressed.

| Property | default | hover | pressed |
|---|---|---|---|
| Size (w x h) | 118 x 36 | = | = |
| Padding | 0px 12px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Suisse Intl 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 1 up div.relative.flex bg #ffffff @ 0.15 | = | = |
| How | at rest | mouse hover | CDP forcePseudoState :active:hover |

Crops: `price-interval-default.png`, `price-interval-hover.png`, `price-interval-pressed.png`.

#### price-cta

Get Pro. The Pro plan button. Measured, never followed. Checkout and account creation sit behind this control.

Page: pricing. Selector: `button Get Pro`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 280 x 40 | = | = | 277.2 x 39.6 |
| Padding | 0px 32px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #ffffff @ 0.9 | = | #ffffff @ 0.9 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 14px/20px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | 15.84 x 15.84, colour #000000 |
| Painted layers | button.focus-visible:border-ring.focus-visible:ring-ring/50 280.0x40.0 bg #ffffff r 3.35544e+07px | button.focus-visible:border-ring.focus-visible:ring-ring/50 280.0x40.0 bg #ffffff @ 0.9 r 3.35544e+07px | button.focus-visible:border-ring.focus-visible:ring-ring/50 280.0x40.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.focus-visible:border-ring.focus-visible:ring-ring/50 277.2x39.6 bg #ffffff @ 0.9 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-cta-default.png`, `price-cta-hover.png`, `price-cta-focus-visible.png`, `price-cta-pressed.png`.

#### price-badge

Yearly discount badge. The blue "40% off" chip on the Yearly interval.

Page: pricing. Selector: `40% off`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 55.45 x 21 |
| Padding | 4px 6px |
| Gap | 4px |
| Border | 1px solid #000000 @ 0 |
| Radius | 8px |
| Background | oklch(0.579 0.2497 257.07) |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 11px/11px 450 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | span.focus-visible:border-ring.focus-visible:ring-ring/50 55.5x21.0 bg oklch(0.579 0.2497 257.07) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `price-badge-default.png`.

#### price-popular

Most popular badge. The badge on the Pro card.

Page: pricing. Selector: `Most popular`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 86.5 x 17.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 14px/17.5px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Ancestor paint | 1 up span.focus-visible:border-ring.focus-visible:ring-ring/50 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `price-popular-default.png`.

#### faq-item

FAQ row. A pricing FAQ summary. Opened with its own toggle.

Page: pricing. Selector: `faq button`. States: .

Not found on the page at capture time.

### Enterprise

#### ent-h1

Enterprise heading. The enterprise hero heading.

Page: enterprise. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 539.13 x 191.66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 74.88px/65.8944px 500 |
| Letter spacing | -1.404px |
| Colour | #ffffff |
| Text node | span.block.max-w-[7.2em]: Suisse Intl 74.88px/65.8944px 500, #ffffff, ls -1.404px |
| Transition | none |
| How | at rest |

Crops: `ent-h1-default.png`.

#### ent-cta

Book a call. The sales CTA. Measured, never followed. The booking form is a gated surface.

Page: enterprise. Selector: `Book a call`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119.06 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #007aff offset 1px | = |
| Font | Suisse Intl 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.bg-primary-1000.text-primary-0 119.1x40.0 bg #ffffff r 3.35544e+07px | = | a.bg-primary-1000.text-primary-0 119.1x40.0 bg #ffffff r 3.35544e+07px outline 1px auto #007aff offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ent-cta-default.png`, `ent-cta-hover.png`, `ent-cta-focus-visible.png`, `ent-cta-pressed.png`.

### Blog

#### blog-h1

Blog heading. The blog index heading.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | system-ui 36px/40px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `blog-h1-default.png`.

#### blog-card

Blog card. A published blog card. Measured, not opened in this pass.

Page: blog. Selector: `blog a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 409.72 x 18.89 | = |
| Padding | 0px | = |
| Gap | 6px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | system-ui 14px/18.9px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.announce-label: system-ui 12px/16.2px 600, #ffffff, ls 0.24px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.announce-label 42.7x18.2 bg #ffffff @ 0.2 r 999px | = |
| Ancestor paint | 1 up div.announce bg #2b5cff | = |
| How | at rest | mouse hover |

Crops: `blog-card-default.png`, `blog-card-hover.png`.

### Plugins

#### plug-h1

Plugins heading. The plugins marketing heading.

Page: plugins. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 135.34 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 72px/67.68px 500 |
| Letter spacing | -3.4px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `plug-h1-default.png`.

#### plug-link

Plugin link. A plugin product link. Measured, never followed into an install flow.

Page: plugins. Selector: `a[href*="/plugins/"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 72 x 72 | 111.59 x 111.59 | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 22% | = | = |
| Background | #ffffff @ 0.3 | = | = |
| Box shadow | #ffffff @ 0.85 0px 1px 0px 0px inset, #ffffff @ 0.35 0px 0px 0px 1px inset, #000000 @ 0.06 0px 1px 2px 0px | = | = |
| Backdrop filter | blur(20px) saturate(1.8) | = | = |
| Outline | none | = | 1px auto #007aff offset 1px |
| Font | Suisse Intl 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | span.tip.opacity-0: Suisse Intl 13px/19.5px 500, #ffffff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.app.grid 72.0x72.0 bg #ffffff @ 0.3 r 22% shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #ffffff @ 0.35 0px 0px 0px 1px inset, #000000 @ 0.06 0px 1px 2px 0px; span.tip.opacity-0 85.8x29.5 bg #111111 r 999px | a.app.grid 111.6x111.6 bg #ffffff @ 0.3 r 22% shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #ffffff @ 0.35 0px 0px 0px 1px inset, #000000 @ 0.06 0px 1px 2px 0px; span.tip.opacity-0 85.8x29.5 bg #111111 r 999px | a.app.grid 72.0x72.0 bg #ffffff @ 0.3 r 22% shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #ffffff @ 0.35 0px 0px 0px 1px inset, #000000 @ 0.06 0px 1px 2px 0px outline 1px auto #007aff offset 1px; span.tip.opacity-0 85.8x29.5 bg #111111 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `plug-link-default.png`, `plug-link-hover.png`, `plug-link-focus-visible.png`.

### Login boundary

#### login-h1

Login heading. "Welcome to Krea" / "Log in or sign up". The auth boundary. Nothing is submitted.

Page: login. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 34px/40px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `login-h1-default.png`.

#### login-google

Continue with Google. OAuth button. Measured, never clicked through. Following it is an OAuth flow.

Page: login. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 352 x 46 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #ffffff | = | = | = |
| Radius | 14px | = | = | = |
| Background | #ffffff | #e5e5e5 | = | #e5e5e5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Suisse Intl 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.svelte-xweaza: Suisse Intl 14px/20px 500, #000000 | = | = | = |
| Transition | all 0.35s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | button.hover:bg-primary-800.dark:hover:bg-primary-200 352.0x46.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 14px | button.hover:bg-primary-800.dark:hover:bg-primary-200 352.0x46.0 bg #e5e5e5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 14px | button.hover:bg-primary-800.dark:hover:bg-primary-200 352.0x46.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 14px outline 1px auto #101010 offset 0px | button.hover:bg-primary-800.dark:hover:bg-primary-200 352.0x46.0 bg #e5e5e5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 14px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-apple

Continue with Apple. OAuth button. Measured, never followed.

Page: login. Selector: `Continue with Apple`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 352 x 46 | = |
| Padding | 12px 16px | = |
| Gap | 12px | = |
| Border | 1px solid #ffffff | = |
| Radius | 14px | = |
| Background | #ffffff | #e5e5e5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.svelte-xweaza: Suisse Intl 14px/20px 500, #000000 | = |
| Transition | all 0.35s cubic-bezier(0, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 18 x 18, colour #000000 | = |
| Painted layers | button.hover:bg-primary-800.dark:hover:bg-primary-200 352.0x46.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 14px | button.hover:bg-primary-800.dark:hover:bg-primary-200 352.0x46.0 bg #e5e5e5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 14px |
| How | at rest | mouse hover |

Crops: `login-apple-default.png`, `login-apple-hover.png`.

#### login-sso

SSO. SSO button. Measured, never followed.

Page: login. Selector: `SSO`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 352 x 46 | = |
| Padding | 12px 16px | = |
| Gap | 12px | = |
| Border | 1px solid #ffffff | = |
| Radius | 14px | = |
| Background | #ffffff | #e5e5e5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.svelte-xweaza: Suisse Intl 14px/20px 500, #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #000000 | = |
| Painted layers | button.hover:bg-primary-800.dark:hover:bg-primary-200 352.0x46.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 14px | button.hover:bg-primary-800.dark:hover:bg-primary-200 352.0x46.0 bg #e5e5e5 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 14px |
| How | at rest | mouse hover |

Crops: `login-sso-default.png`, `login-sso-hover.png`.

#### login-email

Email field. The email field on the login boundary. Sample text is typed and deleted. Enter is never pressed, and Continue with Email is never clicked.

Page: login. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 352 x 46 | = | = |
| Padding | 12px 12px 12px 44px | = | = |
| Border | 1px solid #404040 | = | = |
| Radius | 14px | = | = |
| Background | #000000 @ 0.25 | #000000 | #000000 |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | Suisse Intl 14px/20px 450 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #737373, opacity 1 | = | = |
| Painted layers | input.font-book.text-primary-600 352.0x46.0 bg #000000 @ 0.25 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 14px | input.font-book.text-primary-600 352.0x46.0 bg #000000 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | input.font-book.text-primary-600 352.0x46.0 bg #000000 border T:1px solid #404040 / R:1px solid #404040 / B:1px solid #404040 / L:1px solid #404040 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-email-btn

Continue with Email. The email submit control. Measured at rest and hover only. Never clicked, so no account is created and no code is sent.

Page: login. Selector: `Continue with Email`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 352 x 46 | = |
| Padding | 13px 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 14px | = |
| Background | #006eff @ 0.15 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Suisse Intl 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | oklch(0.579 0.2497 257.07) | = |
| Transition | colors, opacity, saturate 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Opacity | 0.75 | = |
| Cursor | not-allowed | = |
| Painted layers | button.group.disabled:bg-action/15 352.0x46.0 bg #006eff @ 0.15 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| How | at rest | mouse hover |

Crops: `login-email-btn-default.png`, `login-email-btn-hover.png`.

#### login-terms

Terms link. The Terms of Service link on the login page.

Page: login. Selector: `a[href="/terms"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 93 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Suisse Intl 12px/16px 450 | = |
| Letter spacing | normal | = |
| Colour | #e5e5e5 | #ffffff |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `login-terms-default.png`, `login-terms-hover.png`.

### Image tool (signed out)

#### image-shell

Image tool shell. The signed-out /image tool. Generation is gated: the prompt is measured if present, never submitted.

Page: image. Selector: `main`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Suisse Intl 16px/24px 400 |
| Letter spacing | normal |
| Colour | oklch(0.985 0 0) |
| Text node | span.truncate: Suisse Intl 16px/24px 500, oklch(0.708 0 0) |
| Transition | none |
| Icon | 20 x 20, colour oklch(0.708 0 0) |
| Painted layers | div.bg-primary-0.sm:bg-primary-150 1440.0x900.0 bg #000000; div.fixed.inset-y-0 256.0x900.0 border R:1px solid oklch(1 0 0 / 0.1); div.bg-sidebar.group-data-[variant=floating]:border-sidebar-border 255.0x900.0 bg oklch(0 0 0); a.peer/menu-button.ring-sidebar-ring 239.0x36.0 bg oklch(0.269 0 0) r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 0.5px inset, #000000 @ 0.05 0px 1px 2px 0px; button.peer/menu-button.text-foreground 239.0x48.0 bg oklch(0.985 0 0) r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 0.5px, #000000 @ 0 0px 0px 0px 0px; span.bg-border.group-focus-visible/resize:bg-foreground/30 1.0x900.0 bg oklch(1 0 0 / 0.1) |
| How | at rest |

Crops: `image-shell-default.png`.

#### image-prompt

Prompt field. The image prompt, if the signed-out page paints one. Sample text is typed and deleted. Generate is never pressed.

Page: image. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 870 x 48 | = | = |
| Padding | 6px 10px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | 2px solid #000000 @ 0 offset 2px | 2px solid #000000 @ 0 offset 2px |
| Font | Suisse Intl 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff @ 0.5, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |
| Painted layers | - | textarea.min-h-[2lh]!.w-full 870.0x48.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | textarea.min-h-[2lh]!.w-full 870.0x48.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, oklch(0.546 0.245 262.881) 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px |

Crops: `image-prompt-default.png`, `image-prompt-focused.png`, `image-prompt-filled.png`.

#### image-generate

Generate. The generate control on /image (aria-label Generate). Measured, never clicked. Submitting a generation is a gated action.

Page: image. Selector: `button[aria-label="Generate"]`. States: .

Not found on the page at capture time.

### Mobile (390 wide)

#### m-sidebar

Mobile shell. The app shell at 390px.

Page: home. Selector: `nav at 390`. States: .

Not found on the page at capture time.

#### m-menu

Mobile menu button. The sidebar toggle at 390px. A local control.

Page: home. Selector: `Toggle Sidebar`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52 x 64 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #262626 @ 0.5 | = | #262626 @ 0.5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Suisse Intl 14px/20px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.985 0 0) | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour oklch(0.985 0 0) | = | = | = |
| Ancestor paint | 1 up header.bg-background.fixed bg oklch(0.145 0 0) | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.focus-visible:border-ring.focus-visible:ring-ring/50 52.0x64.0 bg #262626 @ 0.5 | button.focus-visible:border-ring.focus-visible:ring-ring/50 52.0x64.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #737373 @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.focus-visible:border-ring.focus-visible:ring-ring/50 52.0x64.0 bg #262626 @ 0.5 |

Crops: `m-menu-default.png`, `m-menu-hover.png`, `m-menu-focus-visible.png`, `m-menu-pressed.png`.

#### m-signin

Mobile Sign in. Sign in at 390px. Measured, never followed.

Page: home. Selector: `Sign in`. States: .

Not found on the page at capture time.

## Transitions declared in the readable stylesheets

www.krea.ai paints the public app as html.dark. Consent overlays were hidden, never answered. The sidebar toggle and pricing interval are local UI toggles. Sign in, Sign up, Continue with Google, Continue with Apple, Single Sign-On, Continue with Email, Book a call, Get Pro and Generate were measured, never followed. Every value above is the computed value the page paints.

- home: `opacity 0.42s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 1.1s ease-in-out`, `none`, `scale 80ms ease-in-out, opacity 80ms ease-in-out`, `transform 0.42s cubic-bezier(0.2, 0, 0, 1)`, `transform var(--genius-hover-float-speed)var(--ease-genius-soft-bounce),box-shadow .52s ease-out`, `box-shadow 0.2s ease-out`, `transform 0.2s ease-out, translate 0.2s ease-out, background-color 0.15s, color 0.15s`, `transform .25s var(--ease-genius-soft-bounce)`, `transform 0.15s ease-out`, `left 90ms linear, top 90ms linear, scale 0.4s cubic-bezier(0.34, 1.5, 0.64, 1)`, `scale 0.3s cubic-bezier(0, 0, 0.5, 1.2) 0.5s, opacity 0.3s cubic-bezier(0, 0, 0.5, 1.2) 0.5s`

- pricing: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `opacity 0.42s cubic-bezier(0.32, 0.72, 0, 1)`, `opacity 1.1s ease-in-out`, `none`, `scale 80ms ease-in-out, opacity 80ms ease-in-out`, `transform 0.42s cubic-bezier(0.2, 0, 0, 1)`, `transform var(--genius-hover-float-speed)var(--ease-genius-soft-bounce),box-shadow .52s ease-out`, `box-shadow 0.2s ease-out`, `transform 0.2s ease-out, translate 0.2s ease-out, background-color 0.15s, color 0.15s`
