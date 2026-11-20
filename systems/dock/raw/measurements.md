# Component measurements

Computed styles read from dock.us on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the home page, /pricing, /customers, /templates, /demo and the signed-out auth cards on auth.dock.us — with any consent or chat overlay hidden (never answered) — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky marketing header: the Dock logo, the Product and Resources <details> dropdowns, Pricing and Customers links, Log in, Request demo and the Start-for-free primary action.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1328 x 70.19 |
| Padding | 16px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowNavigation 16px/24px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | summary.nav-trigger: DockWebflowNavigation 16px/19.2px 500, #121722 |
| Transition | none |
| Icon | 0 x 0, colour #121722 |
| Painted layers | summary.button.navigation-toggle 0.0x0.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px inset; div.menu-viewport 0.0x0.0 bg #ffffff r 19.1px shadow #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px; a.button 137.0x38.2 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px inset; a.button.button--primary 124.3x38.2 bg #0068f9 r 100px shadow #0b4493 @ 0.4 0px 0px 0px 0.5px inset |
| Ancestor paint | 1 up div.header-bar bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Dock wordmark anchor.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 85.84 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowNavigation 16px/24px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The Product <summary> that opens the header mega-menu; toggled, never followed.

Page: home. Selector: `summary.nav-trigger "Product"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.7 x 38.19 | = | - | = |
| Padding | 9px 14px 10px 16px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 100px | = | - | = |
| Background | transparent | #f8f8f8 | - | #f8f8f8 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | DockWebflowNavigation 16px/19.2px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #121722 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 12 x 12, colour #121722 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Painted layers | - | summary.nav-trigger 105.7x38.2 bg #f8f8f8 r 100px | = | summary.nav-trigger 105.7x38.2 bg #f8f8f8 r 100px |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-link

Nav link. The plain Pricing header link.

Page: home. Selector: `header a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.98 x 38.19 | = | - | = |
| Padding | 9px 16px 10px 16px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 100px | = | - | = |
| Background | transparent | #f8f8f8 | - | #f8f8f8 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | DockWebflowNavigation 16px/19.2px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #121722 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav-trigger.nav-direct 82.0x38.2 bg #f8f8f8 r 100px | = | a.nav-trigger.nav-direct 82.0x38.2 bg #f8f8f8 r 100px |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log-in link. The Log-in header action (to auth.dock.us); measured, never followed.

Page: home. Selector: `header a "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75.8 x 38.19 | = | - | = |
| Padding | 9px 16px 10px 16px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 100px | = | - | = |
| Background | transparent | #f8f8f8 | - | #f8f8f8 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | DockWebflowNavigation 16px/19.2px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #121722 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav-trigger.nav-direct 75.8x38.2 bg #f8f8f8 r 100px | = | a.nav-trigger.nav-direct 75.8x38.2 bg #f8f8f8 r 100px |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-demo

Demo button. The Request-demo header action; measured, never followed.

Page: home. Selector: `header a "Request demo"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137 x 38.19 | = | - | = |
| Padding | 9px 16px 10px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 100px | = | - | = |
| Background | #ffffff | #f8f8f8 | - | #f2f2f3 |
| Box shadow | #121722 @ 0.2 0px 0px 0px 0.5px inset | = | - | = |
| Outline | none | = | - | = |
| Font | DockWebflowNavigation 16px/19.2px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #121722 | = | - | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease, ease delay 0s, 0s | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.button 137.0x38.2 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px inset | a.button 137.0x38.2 bg #f8f8f8 r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px inset | - | a.button 137.0x38.2 bg #f2f2f3 r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px inset |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |

Crops: `nav-demo-default.png`, `nav-demo-hover.png`, `nav-demo-focus-visible.png`, `nav-demo-pressed.png`.

#### nav-cta

Nav CTA. The Start-for-free primary header action; measured, never followed.

Page: home. Selector: `header a "Start for free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 124.25 x 38.19 | = | - | = |
| Padding | 9px 16px 10px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 100px | = | - | = |
| Background | #0068f9 | #0060eb | - | #005fe4 |
| Box shadow | #0b4493 @ 0.4 0px 0px 0px 0.5px inset | = | - | = |
| Outline | none | = | - | = |
| Font | DockWebflowNavigation 16px/19.2px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease, ease delay 0s, 0s | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.button.button--primary 124.3x38.2 bg #0068f9 r 100px shadow #0b4493 @ 0.4 0px 0px 0px 0.5px inset | a.button.button--primary 124.3x38.2 bg #0060eb r 100px shadow #0b4493 @ 0.4 0px 0px 0px 0.5px inset | - | a.button.button--primary 124.3x38.2 bg #005fe4 r 100px shadow #0b4493 @ 0.4 0px 0px 0px 0.5px inset |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Nav dropdown. The Product mega-menu panel inside dock-site-header, opened by its own <summary> trigger.

Page: home. Selector: `.menu-viewport`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1083 x 258 |
| Padding | 0px |
| Border | none |
| Radius | 19.1px |
| Background | #ffffff |
| Box shadow | #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px |
| Outline | none |
| Font | DockWebflowNavigation 16px/24px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | h2.menu-heading: DockWebflowNavigation 14.5px/20px 400, #121722 |
| Transition | translate, scale, width, height, opacity, visibility 0.24s, 0.24s, 0.24s, 0.24s, 0.24s, 0s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1), ease |
| Icon | 0 x 0, colour #121722 |
| Painted layers | div.menu-viewport 1083.0x258.0 bg #ffffff r 19.1px shadow #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-group

Menu group heading. A group heading inside the opened mega-menu (Sales / Customer success / Content / Learning / AI / Integrations).

Page: home. Selector: `h2.menu-heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 148.83 x 19.07 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowNavigation 14.5px/20px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Transition | none |
| Opacity | 0.6 |
| How | at rest |

Crops: `menu-group-default.png`.

#### menu-link

Menu link. A feature link inside the opened mega-menu.

Page: home. Selector: `a.menu-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 172.06 x 40 | = | - | = |
| Padding | 8px | = | - | = |
| Gap | 12px | = | - | = |
| Border | none | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | 2px solid #121722 @ 0.6 offset 4px |
| Font | DockWebflowNavigation 15.5px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #121722 | = | - | = |
| Text node | span: DockWebflowNavigation 15.5px/20px 500, #121722 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #121722 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |
| Painted layers | - | = | = | a.menu-link 172.1x40.0 r 8px outline 2px solid #121722 @ 0.6 offset 4px |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home

#### hero-title

Hero headline. The "Build high-performing sales teams" display headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 140.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowHome 62px/70.4px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero copy. The lede under the hero headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 202.23 x 38.19 |
| Padding | 9px 16px 10px 16px |
| Border | none |
| Radius | 100px |
| Background | #002fa6 |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowHome 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | p.hero-eyebrow 202.2x38.2 bg #002fa6 r 100px; span.hero-eyebrow-border 202.2x38.2 image conic-gradient(from 190.436deg, #002fa6 0deg, #002fa6 234deg, #4db5ff 360deg) r 100px |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-cta

Hero CTA. The primary Start-for-free action in the hero; measured, never followed.

Page: home. Selector: `a.dock-home-button "Start for free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 151.78 x 44.59 | = | = | = |
| Padding | 10px 24px 13px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #0068f9 | #0060eb | = | #005fe4 |
| Box shadow | #4db5ff @ 0.3 0px 0px 0px 0.5px inset | = | = | = |
| Outline | none | = | 2px solid #121722 @ 0.6 offset 4px | = |
| Font | DockWebflowHome 18px/21.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dock-home-button.dock-home-button--primary 151.8x44.6 bg #0068f9 r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset | a.dock-home-button.dock-home-button--primary 151.8x44.6 bg #0060eb r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset | a.dock-home-button.dock-home-button--primary 151.8x44.6 bg #0068f9 r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset outline 2px solid #121722 @ 0.6 offset 4px | a.dock-home-button.dock-home-button--primary 151.8x44.6 bg #005fe4 r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-demo

Hero demo action. The secondary Request-demo action in the hero; measured, never followed.

Page: home. Selector: `a.dock-home-button "Request demo"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 166.13 x 44.59 | = | = | = |
| Padding | 10px 24px 13px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | #ffffff @ 0.06 | = | #ffffff @ 0.1 |
| Box shadow | #4db5ff @ 0.4 0px 0px 0px 0.5px inset | = | = | = |
| Outline | none | = | 2px solid #121722 @ 0.6 offset 4px | = |
| Font | DockWebflowHome 18px/21.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.dock-home-button 166.1x44.6 r 100px shadow #4db5ff @ 0.4 0px 0px 0px 0.5px inset | a.dock-home-button 166.1x44.6 bg #ffffff @ 0.06 r 100px shadow #4db5ff @ 0.4 0px 0px 0px 0.5px inset | a.dock-home-button 166.1x44.6 r 100px shadow #4db5ff @ 0.4 0px 0px 0px 0.5px inset outline 2px solid #121722 @ 0.6 offset 4px | a.dock-home-button 166.1x44.6 bg #ffffff @ 0.1 r 100px shadow #4db5ff @ 0.4 0px 0px 0px 0.5px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-demo-default.png`, `hero-demo-hover.png`, `hero-demo-focus-visible.png`, `hero-demo-pressed.png`.

#### hero-card

Hero artwork. The painted product-scene layer behind the hero copy (the sales-room artwork panel).

Page: home. Selector: `.hero-screen`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 951.45 x 598.47 |
| Padding | 0px |
| Border | none |
| Radius | 18.93px |
| Background | #ffffff |
| Box shadow | #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px |
| Outline | none |
| Font | DockWebflowHome 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.room-medium: DockWebflowHome 16px/19.2px 500, #121722 |
| Transition | none |
| Icon | 15.86 x 15.86, colour #121722 @ 0.8, fill #000000 |
| Painted layers | div.hero-screen 951.5x598.5 bg #ffffff r 18.93px shadow #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px; div.sales-room.learning-room 951.5x598.5 bg #ffffff; div.organize-sidebar 55.5x598.5 border R:1px solid #dedfe0; span.room-tab.room-tab--active 35.7x35.7 bg #f2f2f3 r 8px; span.room-workspace-mark.room-user-portrait 19.8x19.8 bg #dedfe0 r 100px; div::after.room-header.learning-header 904pxx0.5px bg #dedfe0 |
| How | at rest |

Crops: `hero-card-default.png`.

#### section-h2

Section heading. A section heading in the light sections.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 239.3 x 21.59 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowHome 18px/21.6px 500 |
| Letter spacing | normal |
| Colour | #121722 |
| Transition | none |
| Painted layers | h2 239.3x21.6 bg #ffffff |
| How | at rest |

Crops: `section-h2-default.png`.

#### agent-field

Prompt field. The read-only Dock-MCP setup prompt input; it paints inside the collapsed label.mcp-prompt-field, so only the hidden state is normally reachable.

Page: home. Selector: `input[aria-label*="prompt"]`. States: .

Not found on the page at capture time.

#### agent-area

Prompt area. The read-only selected-prompt textarea in the demo section.

Page: home. Selector: `textarea[aria-label*="prompt"]`. States: .

Not found on the page at capture time.

#### mcp-prompt

MCP prompt. The Dock-MCP "install the prompt" widget in the MCP section: a prompt field, an Explore link and the Copy action.

Page: home. Selector: `.mcp-prompt`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 381.2 x 44 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowHome 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.dock-home-button.mcp-explore: DockWebflowHome 16px/19.2px 500, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #ffffff, fill #000000 |
| Painted layers | a.dock-home-button.mcp-explore 161.5x44.0 r 100px shadow #4db5ff @ 0.4 0px 0px 0px 0.5px inset; button.dock-home-button.dock-home-button--primary 207.7x44.0 bg #0068f9 r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; label.mcp-prompt-field 0.0x0.0 bg #ffffff r 19.1px |
| How | at rest |

Crops: `mcp-prompt-default.png`.

#### mcp-copy

Copy prompt. The Copy-prompt action in the MCP widget; hover/focus/pressed read, the copy itself never clicked.

Page: home. Selector: `button.mcp-copy`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 207.7 x 44 | = | = | = |
| Padding | 10px 14px 10px 10px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #0068f9 | #0060eb | = | #005fe4 |
| Box shadow | #4db5ff @ 0.3 0px 0px 0px 0.5px inset | = | = | = |
| Outline | none | = | 2px solid #121722 @ 0.6 offset 4px | = |
| Font | DockWebflowHome 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: DockWebflowHome 16px/19.2px 500, #ffffff | = | = | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button.dock-home-button.dock-home-button--primary 207.7x44.0 bg #0068f9 r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px | button.dock-home-button.dock-home-button--primary 207.7x44.0 bg #0060eb r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px | button.dock-home-button.dock-home-button--primary 207.7x44.0 bg #0068f9 r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset outline 2px solid #121722 @ 0.6 offset 4px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px | button.dock-home-button.dock-home-button--primary 207.7x44.0 bg #005fe4 r 100px shadow #4db5ff @ 0.3 0px 0px 0px 0.5px inset; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px; span 24.0x24.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mcp-copy-default.png`, `mcp-copy-hover.png`, `mcp-copy-focus-visible.png`, `mcp-copy-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The "Dock Pricing" display heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376.95 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 60px/64px 600 |
| Letter spacing | -0.6px |
| Colour | #121722 |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### pr-sticky

Plan bar. The sticky plan summary bar that pins under the header while scrolling the plan comparison.

Page: pricing. Selector: `.pr-sticky`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 152 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #dedfe3 0px 0.5px 0px 0px |
| Outline | none |
| Font | Roobert 16px/normal 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | span.pr-sticky-name: Roobert 14px/20px 500, #121722 |
| Transition | transform 0.25s ease |
| Transform | matrix(1, 0, 0, 1, 0, -304) |
| Painted layers | div.pr-sticky 1440.0x152.0 bg #ffffff shadow #dedfe3 0px 0.5px 0px 0px; a.btn.btn-outline 193.8x40.0 bg #ffffff r 100px shadow #000000 @ 0.08 0px 0.5px 1px 0px, #121722 @ 0.1 0px -1px 0px 0px inset, #121722 @ 0.15 0px 0px 0px 0.5px inset; a.btn.btn-outline 193.8x40.0 bg #ffffff r 100px shadow #000000 @ 0.08 0px 0.5px 1px 0px, #121722 @ 0.1 0px -1px 0px 0px inset, #121722 @ 0.15 0px 0px 0px 0.5px inset; div.pr-sticky-col.pr-sticky-col--popular 225.8x144.0 bg #f7f7f8 r 12px 12px 0px 0px; span.pr-sticky-badge 76.9x14.0 bg #ffffff r 100px; span.pr-shine 64.9x10.0 image linear-gradient(110deg, #0068f9 42%, #8ec2ff 50%, #0068f9 58%) |
| Ancestor paint | 1 up main.ds-page bg #ffffff |
| How | at rest |

Crops: `pr-sticky-default.png`.

#### plan-card

Plan card. A pricing plan card (plan name, price and its action).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 225.75 x 300 |
| Padding | 44px 32px 32px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/normal 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | h2.plan-name: Roobert 20px/28px 500, #121722 |
| Transition | none |
| Painted layers | a.btn.btn-outline 161.8x40.0 bg #ffffff r 100px shadow #000000 @ 0.08 0px 0.5px 1px 0px, #121722 @ 0.1 0px -1px 0px 0px inset, #121722 @ 0.15 0px 0px 0px 0.5px inset |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-name

Plan name. A plan card's name (Free / Standard / Premium / Enterprise).

Page: pricing. Selector: `.plan-name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 39.47 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 20px/28px 500 |
| Letter spacing | normal |
| Colour | #121722 |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. A plan card's price figure.

Page: pricing. Selector: `.plan-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 18.86 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 19px/24px 600 |
| Letter spacing | -0.19px |
| Colour | #121722 |
| Text node | sup: Roobert 12px/0px 600, #121722, ls -0.19px |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's Get-started action (not the fixed .pr-sticky summary bar); measured, never followed.

Page: pricing. Selector: `plan card CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 161.75 x 40 | = | = | = |
| Padding | 7px 20px 9px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #ffffff | #fafafb | = | #f2f2f3 |
| Box shadow | #000000 @ 0.08 0px 0.5px 1px 0px, #121722 @ 0.1 0px -1px 0px 0px inset, #121722 @ 0.15 0px 0px 0px 0.5px inset | = | = | #121722 @ 0.15 0px 0px 0px 0.5px inset, #121722 @ 0.12 0px 2px 4px 0px inset |
| Outline | none | = | 2px solid #0068f9 offset 4px | = |
| Font | Roobert 17px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121722 | = | = | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-outline 161.8x40.0 bg #ffffff r 100px shadow #000000 @ 0.08 0px 0.5px 1px 0px, #121722 @ 0.1 0px -1px 0px 0px inset, #121722 @ 0.15 0px 0px 0px 0.5px inset | a.btn.btn-outline 161.8x40.0 bg #fafafb r 100px shadow #000000 @ 0.08 0px 0.5px 1px 0px, #121722 @ 0.1 0px -1px 0px 0px inset, #121722 @ 0.15 0px 0px 0px 0.5px inset | a.btn.btn-outline 161.8x40.0 bg #ffffff r 100px shadow #000000 @ 0.08 0px 0.5px 1px 0px, #121722 @ 0.1 0px -1px 0px 0px inset, #121722 @ 0.15 0px 0px 0px 0.5px inset outline 2px solid #0068f9 offset 4px | a.btn.btn-outline 161.8x40.0 bg #f2f2f3 r 100px shadow #121722 @ 0.15 0px 0px 0px 0.5px inset, #121722 @ 0.12 0px 2px 4px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-item

FAQ item. A pricing FAQ <details>/<summary> row; toggled open once for the opened state, a local UI toggle.

Page: pricing. Selector: `main details.faq-item summary`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 706.23 x 80 | = | = | = | = |
| Padding | 26px 4px | = | = | = | = |
| Gap | 24px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #0068f9 offset 4px | = | = |
| Font | Roobert 20px/28px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #121722 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #000000 @ 0 | = | = | = | = |
| Painted layers | span::before.faq-toggle 14pxx1.5px bg #121722; span::after.faq-toggle 1.5pxx14px bg #121722 | = | summary 706.2x80.0 outline 2px solid #0068f9 offset 4px; span::before.faq-toggle 14pxx1.5px bg #121722; span::after.faq-toggle 1.5pxx14px bg #121722 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`, `faq-item-opened.png`.

### Customers

#### customers-h1

Customers title. The "Why revenue teams love Dock" display heading.

Page: customers. Selector: `h1 on /customers`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 580 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 70px/72px 700 |
| Letter spacing | normal |
| Colour | #121722 |
| Transition | none |
| How | at rest |

Crops: `customers-h1-default.png`.

#### filter-radio

Filter radio. A category filter pill on the testimonial wall ("💙 All Dock love" / Sales / Enablement …); a local UI filter, one was toggled for the selected state.

Page: customers. Selector: `label.filter--item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 159.84 x 36 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 60px | = | = | = |
| Background | #d5ecff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 16px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121722 | = | = | = |
| Text node | span.text--body.w-form-label: Roobert 18px/28px 400, #121722 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | label.filter--item.filter--active 159.8x36.0 bg #d5ecff r 60px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-radio-default.png`, `filter-radio-hover.png`, `filter-radio-focus-visible.png`, `filter-radio-pressed.png`.

#### customer-card

Customer card. A customer-story card in the grid; measured, never followed.

Page: customers. Selector: `.customers--grid a.link-block`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 580 x 375 | = | = | = |
| Padding | 0px 0px 1px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0068f9 | = | = | = |
| Text node | h2.library-title: Roobert 28px/30px 600, #121722 | = | = | = |
| Transition | opacity 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |

Crops: `customer-card-default.png`, `customer-card-hover.png`, `customer-card-focus-visible.png`, `customer-card-pressed.png`.

#### testimonial

Testimonial. A testimonial block in the wall of love.

Page: customers. Selector: `.testimonial`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 381.33 x 422.48 |
| Padding | 16px |
| Gap | 16px |
| Border | none |
| Radius | 16px |
| Background | #f4f0ff |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/20px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | div.text--body: Roobert 18px/28px 400, #121722 |
| Transition | none |
| Icon | 67.83 x 43.41, colour #ffffff |
| Painted layers | div.testimonial.w-dyn-item 381.3x422.5 bg #f4f0ff r 16px; div.wistia-container 349.3x198.5 bg #000000 border T:1px solid #efefef / R:1px solid #efefef / B:1px solid #efefef / L:1px solid #efefef r 8px; div 67.8x43.4 bg #2949e5; div 67.8x43.4 bg #2949e5 @ 0.7; button.w-vulcan-v2-button.click-for-sound-btn 0.0x0.0 bg #000000 @ 0.8 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 60px; button.w-vulcan-v2-button 0.0x0.0 bg #000000 @ 0.6 r 50% |
| How | at rest |

Crops: `testimonial-default.png`.

### Templates

#### templates-h1

Templates title. The "Templates" display heading.

Page: templates. Selector: `h1 on /templates`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1062.41 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 38px/44px 700 |
| Letter spacing | normal |
| Colour | #121722 |
| Transition | none |
| How | at rest |

Crops: `templates-h1-default.png`.

#### templates-sidebar

Sidebar. The template category sidebar.

Page: templates. Selector: `.sidebar--sticky`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 264.59 x 202 |
| Padding | 0px 32px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/20px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | div: Roobert 16px/20px 400, #4058ff |
| Transition | none |
| Painted layers | a.sidebar--link.is--current 232.6x28.0 bg #e6ecfc @ 0.5 r 8px |
| How | at rest |

Crops: `templates-sidebar-default.png`.

#### sidebar-link

Sidebar link. A category link in the template sidebar; measured, never followed.

Page: templates. Selector: `sidebar a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 232.59 x 28 | = | = | = |
| Padding | 3px 3px 5px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #ededed @ 0.48 | = | #ededed @ 0.48 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121722 | = | = | = |
| Text node | div: Roobert 16px/20px 400, #121722 | = | = | = |
| Transition | opacity 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |
| Painted layers | - | a.sidebar--link.w-inline-block 232.6x28.0 bg #ededed @ 0.48 r 8px | = | a.sidebar--link.w-inline-block 232.6x28.0 bg #ededed @ 0.48 r 8px |

Crops: `sidebar-link-default.png`, `sidebar-link-hover.png`, `sidebar-link-focus-visible.png`, `sidebar-link-pressed.png`.

#### template-card

Template card. A template card in the gallery; measured, never followed.

Page: templates. Selector: `a[href^="/templates/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 338.13 x 307.67 | = | = | = |
| Padding | 0px 0px 1px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 18px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121722 | = | = | = |
| Text node | h4.browse-title: Roobert 18px/23.4px 500, #121722 | = | = | = |
| Transition | opacity 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |

Crops: `template-card-default.png`, `template-card-hover.png`, `template-card-focus-visible.png`, `template-card-pressed.png`.

### Demo request

#### demo-h1

Demo title. The "Request a Demo" display heading.

Page: demo. Selector: `h1 on /demo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 299.91 x 168.53 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 80.64px/84.2688px 600 |
| Letter spacing | -0.32256px |
| Colour | #121722 |
| Transition | none |
| How | at rest |

Crops: `demo-h1-default.png`.

#### demo-form

Demo form mount. The HubSpot scheduler mount on /demo; its fields paint inside the hsforms iframe, which is read through the frame below — nothing was ever submitted.

Page: demo. Selector: `#dock-demo-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 354 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/normal 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Transition | none |
| How | at rest |

Crops: `demo-form-default.png`.

#### demo-field

Demo field. A field inside the HubSpot demo form (read through the iframe); clicked into once for the focused state, never filled or submitted.

Page: demo. Selector: `hsform iframe input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 411 x 48 | = |
| Padding | 0px 18px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | #ffffff | = |
| Box shadow | #121722 @ 0.1 0px 0px 0px 1px inset | #0068f9 0px 0px 0px 1.5px inset |
| Outline | none | = |
| Font | Roobert 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #121722 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #121722 @ 0.5, opacity 1 | = |
| Painted layers | input.hs-input 411.0x48.0 bg #ffffff r 6px shadow #121722 @ 0.1 0px 0px 0px 1px inset | input.hs-input 411.0x48.0 bg #ffffff r 6px shadow #0068f9 0px 0px 0px 1.5px inset |
| How | at rest | clicked into the field |

Crops: `demo-field-default.png`, `demo-field-focused.png`.

#### demo-submit

Demo submit. The Schedule-demo submit inside the HubSpot iframe; measured, never pressed.

Page: demo. Selector: `hsform iframe submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 411 x 48 | = | = | = |
| Padding | 7px 14px 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #0068f9 | #005fe4 | = | #005fe4 |
| Box shadow | #000000 @ 0.25 0px 0.5px 1px 0px, #0b4493 @ 0.22 0px -1px 0px 0px inset, #0b4493 @ 0.25 0px 0px 0px 0.5px inset | = | = | = |
| Outline | none | = | 2px solid #0068f9 offset 4px | = |
| Font | Roobert 18px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | #ffffff, opacity 1 | = | = | = |
| Painted layers | input.hs-button.primary 411.0x48.0 bg #0068f9 r 6px shadow #000000 @ 0.25 0px 0.5px 1px 0px, #0b4493 @ 0.22 0px -1px 0px 0px inset, #0b4493 @ 0.25 0px 0px 0px 0.5px inset | input.hs-button.primary 411.0x48.0 bg #005fe4 r 6px shadow #000000 @ 0.25 0px 0.5px 1px 0px, #0b4493 @ 0.22 0px -1px 0px 0px inset, #0b4493 @ 0.25 0px 0px 0px 0.5px inset | input.hs-button.primary 411.0x48.0 bg #0068f9 r 6px shadow #000000 @ 0.25 0px 0.5px 1px 0px, #0b4493 @ 0.22 0px -1px 0px 0px inset, #0b4493 @ 0.25 0px 0px 0px 0.5px inset outline 2px solid #0068f9 offset 4px | input.hs-button.primary 411.0x48.0 bg #005fe4 r 6px shadow #000000 @ 0.25 0px 0.5px 1px 0px, #0b4493 @ 0.22 0px -1px 0px 0px inset, #0b4493 @ 0.25 0px 0px 0px 0.5px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-submit-default.png`, `demo-submit-hover.png`, `demo-submit-focus-visible.png`, `demo-submit-pressed.png`.

### Log in and sign up

#### login-card

Login card. The sign-in card on auth.dock.us (a workspace-subdomain field + Continue); captured, never used.

Page: login. Selector: `login card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 450 x 322.8 |
| Padding | 64px |
| Border | none |
| Radius | 4px |
| Background | #ffffff |
| Box shadow | #121722 @ 0.25 0px 20px 36px -18px, #121722 @ 0.1 0px 0px 0px 0.5px, #121722 @ 0.2 0px 1px 2px 0px |
| Outline | none |
| Font | Roobert 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a202c |
| Text node | h2.chakra-heading.css-1sqjcp5: -apple-system 24px/28.8px 600, #1a202c |
| Transition | none |
| Painted layers | div.css-1qltkmx 450.0x322.8 bg #ffffff r 4px shadow #121722 @ 0.25 0px 20px 36px -18px, #121722 @ 0.1 0px 0px 0px 0.5px, #121722 @ 0.2 0px 1px 2px 0px; div.css-5ipgv6 322.0x36.0 bg #ffffff border T:1px solid #c1c1c1 / R:1px solid #c1c1c1 / B:1px solid #c1c1c1 / L:1px solid #c1c1c1 r 4px shadow #000000 @ 0.15 0px 1px 2px 0px inset outline 2px solid #000000 @ 0 offset 2px; input.chakra-input.css-1l0bxyc 232.0x36.0 shadow #000000 @ 0.15 0px 1px 2px 0px inset outline 2px solid #000000 @ 0 offset 2px; div.css-b1bhe5 88.0x34.0 bg #f5f5f5 border L:1px solid #c1c1c1 r 0px 4px 4px 0px; button.chakra-button.css-w47b2f 322.0x36.0 bg #4058ff r 4px |
| How | at rest |

Crops: `login-card-default.png`.

#### subdomain-field

Subdomain field. The workspace-subdomain input; focused and given sample text that was deleted again — nothing sent.

Page: login. Selector: `input[name=subdomain]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 232 x 36 | = | = |
| Padding | 0px 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | #ffffff | #ffffff |
| Box shadow | #000000 @ 0.15 0px 1px 2px 0px inset | none | none |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Roobert 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1a202c | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #7d828e, opacity 1 | = | = |
| Painted layers | input.chakra-input.css-1l0bxyc 232.0x36.0 shadow #000000 @ 0.15 0px 1px 2px 0px inset outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-1l0bxyc 232.0x36.0 bg #ffffff outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-1653211 232.0x36.0 bg #ffffff outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.css-5ipgv6 bg #ffffff shadow #000000 @ 0.15 0px 1px 2px 0px inset outline 2px solid #000000 @ 0 | 1 up div.css-1xdpbo7 bg #ffffff shadow #233ced @ 0.17 0px 0px 0px 2px, #000000 @ 0.1 0px 1px 0px 0px inset outline 2px solid #000000 @ 0 | 1 up div.css-1jy84gg bg #ffffff outline 2px solid #000000 @ 0 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `subdomain-field-default.png`, `subdomain-field-focused.png`, `subdomain-field-filled.png`.

#### continue-btn

Continue button. The login form's Continue submit; measured, never pressed.

Page: login. Selector: `button "Continue"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 322 x 36 | = | - | = |
| Padding | 0px 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 4px | = | - | = |
| Background | #4058ff | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Roobert 14px/16.8px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | - | = |
| Opacity | 0.4 | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.chakra-button.css-w47b2f 322.0x36.0 bg #4058ff r 4px | = | - | = |
| Ancestor paint | 2 up div.css-1qltkmx bg #ffffff shadow #121722 @ 0.25 0px 20px 36px -18px, #121722 @ 0.1 0px 0px 0px 0.5px, #121722 @ 0.2 0px 1px 2px 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `continue-btn-default.png`, `continue-btn-hover.png`, `continue-btn-pressed.png`.

#### signup-card

Signup card. The create-account card on auth.dock.us; captured, never used.

Page: signup. Selector: `signup card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 209.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a202c |
| Text node | p.chakra-text.css-j7i18g: Roobert 13px/19.5px 400, #121722 |
| Transition | none |
| Painted layers | input.chakra-input.css-xw7nt4 300.0x36.0 bg #ffffff border T:1px solid #c1c1c1 / R:1px solid #c1c1c1 / B:1px solid #c1c1c1 / L:1px solid #c1c1c1 r 4px shadow #000000 @ 0.15 0px 1px 2px 0px inset outline 2px solid #000000 @ 0 offset 2px; button.chakra-button.css-4f35md 300.0x43.0 bg #4058ff border T:1px solid #3247cf / R:1px solid #3247cf / B:1px solid #3247cf / L:1px solid #3247cf r 6px |
| How | at rest |

Crops: `signup-card-default.png`.

#### signup-field

Signup email field. The signup email input; focused and given sample text that was deleted again — nothing sent.

Page: signup. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 300 x 36 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #c1c1c1 | 1px solid #4058ff | 1px solid #4058ff |
| Radius | 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0.15 0px 1px 2px 0px inset | #233ced @ 0.17 0px 0px 0px 2px, #000000 @ 0.1 0px 1px 0px 0px inset | #233ced @ 0.17 0px 0px 0px 2px, #000000 @ 0.1 0px 1px 0px 0px inset |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Roobert 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1a202c | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #7d828e, opacity 1 | = | = |
| Painted layers | input.chakra-input.css-xw7nt4 300.0x36.0 bg #ffffff border T:1px solid #c1c1c1 / R:1px solid #c1c1c1 / B:1px solid #c1c1c1 / L:1px solid #c1c1c1 r 4px shadow #000000 @ 0.15 0px 1px 2px 0px inset outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-xw7nt4 300.0x36.0 bg #ffffff border T:1px solid #4058ff / R:1px solid #4058ff / B:1px solid #4058ff / L:1px solid #4058ff r 4px shadow #233ced @ 0.17 0px 0px 0px 2px, #000000 @ 0.1 0px 1px 0px 0px inset outline 2px solid #000000 @ 0 offset 2px | input.chakra-input.css-xw7nt4 300.0x36.0 bg #ffffff border T:1px solid #4058ff / R:1px solid #4058ff / B:1px solid #4058ff / L:1px solid #4058ff r 4px shadow #233ced @ 0.17 0px 0px 0px 2px, #000000 @ 0.1 0px 1px 0px 0px inset outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signup-field-default.png`, `signup-field-focused.png`, `signup-field-filled.png`.

#### signup-check

Human check. The Cloudflare Turnstile "Verify you are human" widget on the signup card (an iframe; its inner checkbox cannot be read and was never toggled).

Page: signup. Selector: `turnstile iframe`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1 x 1 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Roobert 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1a202c |
| Transition | none |
| Opacity | 0 |
| Ancestor paint | 1 up body.chakra-ui-light bg #ffffff |
| How | at rest |

Crops: `signup-check-default.png`.

#### signup-submit

Signup submit. The signup submit action; measured, never pressed.

Page: signup. Selector: `signup submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #e2e8f0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #eff1ff @ 0.8 | = | #eff1ff @ 0.8 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Roobert 14px/16.8px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | button.chakra-button.css-14fky7z 300.0x36.0 border T:1px solid #e2e8f0 / R:1px solid #e2e8f0 / B:1px solid #e2e8f0 / L:1px solid #e2e8f0 r 4px | button.chakra-button.css-14fky7z 300.0x36.0 bg #eff1ff @ 0.8 border T:1px solid #e2e8f0 / R:1px solid #e2e8f0 / B:1px solid #e2e8f0 / L:1px solid #e2e8f0 r 4px | = | button.chakra-button.css-14fky7z 300.0x36.0 bg #eff1ff @ 0.8 border T:1px solid #e2e8f0 / R:1px solid #e2e8f0 / B:1px solid #e2e8f0 / L:1px solid #e2e8f0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-submit-default.png`, `signup-submit-hover.png`, `signup-submit-focus-visible.png`, `signup-submit-pressed.png`.

### Footer

#### footer

Footer. The marketing footer: link columns, legal, social and the trust badges.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 820.3 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowNavigation 16px/24px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | h2.menu-heading: DockWebflowNavigation 14.5px/20px 400, #121722 |
| Transition | none |
| Painted layers | footer.site-footer 1440.0x820.3 bg #ffffff; span.trust-badge-icon 16.0x16.0 bg #121722 @ 0.8; span.trust-badge-icon 16.0x16.0 bg #121722 @ 0.8; span.trust-badge-icon 16.0x16.0 bg #121722 @ 0.8 |
| Ancestor paint | 1 up div.dock-footer-surface bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.44 x 22.39 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | DockWebflowNavigation 16px/22.4px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #121722 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### trust-badge

Trust badge. A compliance badge in the footer (GDPR / SOC 2 …).

Page: home. Selector: `footer .trust-badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96.33 x 16 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowNavigation 12.5px/15px 400 |
| Letter spacing | normal |
| Colour | #121722 @ 0.8 |
| Transition | none |
| Painted layers | span.trust-badge-icon 16.0x16.0 bg #121722 @ 0.8 |
| How | at rest |

Crops: `trust-badge-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 76 |
| Padding | 16px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowNavigation 16px/24px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | summary.button.navigation-toggle: DockWebflowNavigation 16px/19.2px 500, #121722 |
| Transition | none |
| Icon | 16 x 16, colour #121722 |
| Painted layers | summary.button.navigation-toggle 94.5x44.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px inset; div.navigation-content 94.5x386.0 bg #ffffff r 19.1px shadow #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px; div.menu-panel.menu-panel--product 46.5x286.4 bg #ffffff; a.nav-trigger.nav-direct 46.5x56.0 border T:1px solid #dedfe0; a.nav-trigger.nav-direct 46.5x56.0 border T:1px solid #dedfe0; details.dropdown 46.5x57.0 border T:1px solid #dedfe0 |
| Ancestor paint | 1 up div.header-bar bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header Menu <summary> toggle inside dock-site-header.

Page: mobile. Selector: `summary.navigation-toggle`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 94.53 x 44 |
| Padding | 9px 14px 10px 16px |
| Gap | 8px |
| Border | none |
| Radius | 100px |
| Background | #ffffff |
| Box shadow | #121722 @ 0.2 0px 0px 0px 0.5px inset |
| Outline | none |
| Font | DockWebflowNavigation 16px/19.2px 500 |
| Letter spacing | normal |
| Colour | #121722 |
| Transition | background-color, box-shadow 0.14s, 0.14s ease, ease delay 0s, 0s |
| Cursor | pointer |
| Icon | 16 x 16, colour #121722 |
| Painted layers | summary.button.navigation-toggle 94.5x44.0 bg #ffffff r 100px shadow #121722 @ 0.2 0px 0px 0px 0.5px inset |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The opened mobile navigation panel inside dock-site-header (the expanded list of nav groups and actions).

Page: mobile. Selector: `details.navigation[open] .navigation-content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 386 |
| Padding | 8px 24px 24px 24px |
| Gap | 0px |
| Border | none |
| Radius | 19.1px |
| Background | #ffffff |
| Box shadow | #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px |
| Outline | none |
| Font | DockWebflowNavigation 16px/24px 400 |
| Letter spacing | normal |
| Colour | #121722 |
| Text node | summary.nav-trigger: DockWebflowNavigation 18px/21.6px 500, #121722 |
| Transition | none |
| Icon | 12 x 12, colour #121722 |
| Painted layers | div.navigation-content 350.0x386.0 bg #ffffff r 19.1px shadow #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px; div.menu-panel.menu-panel--product 302.0x276.0 bg #ffffff; a.nav-trigger.nav-direct 302.0x56.0 border T:1px solid #dedfe0; a.nav-trigger.nav-direct 302.0x56.0 border T:1px solid #dedfe0; details.dropdown 302.0x57.0 border T:1px solid #dedfe0; div.menu-panel.menu-panel--resources 302.0x188.0 bg #ffffff |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A nav item inside the opened mobile menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 302 x 56 | = | - | = |
| Padding | 16px 0px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | 2px solid #121722 @ 0.6 offset 4px |
| Font | DockWebflowNavigation 18px/21.6px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #121722 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 12 x 12, colour #121722 | = | - | = |
| Ancestor paint | 3 up div.navigation-content bg #ffffff shadow #121722 @ 0.2 0px 0px 0px 0.5px, #121722 @ 0.05 0px 1px 3px 0px, #121722 @ 0.05 0px 3px 7px 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed when captured; the via was later rewritten by hand, not re-measured | = |
| Painted layers | - | = | = | summary.nav-trigger 302.0x56.0 outline 2px solid #121722 @ 0.6 offset 4px |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 68.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | DockWebflowHome 29.25px/34.375px 600 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

dock.us serves its Webflow bundles same-origin (cdn.prod.website-files.com), so this list covers the transition rules the page itself exposes, and the per-state Transition rows above are the computed values the page paints.

- customers: `inherit`, `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `opacity 0.2s`, `0.2s ease-in-out, opacity 0.2s`, `0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `box-shadow 0.2s ease-in-out, top 0.2s ease-in-out`, `0.35s cubic-bezier(0.86, 0, 0.07, 1)`, `0.2s`, `transform 0.2s ease-in-out`, `0.4s cubic-bezier(0.645, 0.045, 0.355, 1)`

- demo: `inherit`, `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `opacity 0.2s`, `0.2s ease-in-out, opacity 0.2s`, `0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `box-shadow 0.2s ease-in-out, top 0.2s ease-in-out`, `0.35s cubic-bezier(0.86, 0, 0.07, 1)`, `0.2s`, `transform 0.2s ease-in-out`, `0.4s cubic-bezier(0.645, 0.045, 0.355, 1)`

- home: `inherit`, `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `opacity 0.2s`, `0.2s ease-in-out, opacity 0.2s`, `0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `box-shadow 0.2s ease-in-out, top 0.2s ease-in-out`, `0.35s cubic-bezier(0.86, 0, 0.07, 1)`, `0.2s`, `transform 0.2s ease-in-out`, `0.4s cubic-bezier(0.645, 0.045, 0.355, 1)`

- login: `border 250ms`, `width 200ms, height 200ms, max-height 200ms, transform 300ms cubic-bezier(0, 1.2, 1, 1), opacity 83ms ease-out`

- pricing: `inherit`, `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `opacity 0.2s`, `0.2s ease-in-out, opacity 0.2s`, `0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `box-shadow 0.2s ease-in-out, top 0.2s ease-in-out`, `0.35s cubic-bezier(0.86, 0, 0.07, 1)`, `0.2s`, `transform 0.2s ease-in-out`, `0.4s cubic-bezier(0.645, 0.045, 0.355, 1)`

- signup: `10ms`, `width 200ms, height 200ms, max-height 200ms, transform 300ms cubic-bezier(0, 1.2, 1, 1), opacity 83ms ease-out`

- templates: `inherit`, `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `opacity 0.2s`, `0.2s ease-in-out, opacity 0.2s`, `0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `box-shadow 0.2s ease-in-out, top 0.2s ease-in-out`, `0.35s cubic-bezier(0.86, 0, 0.07, 1)`, `0.2s`, `transform 0.2s ease-in-out`, `0.4s cubic-bezier(0.645, 0.045, 0.355, 1)`
