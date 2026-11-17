# Component measurements

Computed styles read from hashnode.com and townhall.hashnode.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is the search field clicked into (nothing typed); `dark` is the same element after the header's own "Switch to dark theme" button repainted html.dark; `opened` and the rest are resting states reached by a component's own UI toggle. Nothing was typed, sent or signed into.

## Components

### App chrome

#### app-sidebar

App sidebar. The left sidebar (bg-sidebar): logo, Home/Feed/Pro/Agents nav links, the Search / Theme / More menu buttons, sidebar footer with the resource links and the Sign-in link.

Page: /. Selector: `div[class*="bg-sidebar"]`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 64 x 876 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 28px | = |
| Background | #f7f8fa | #06070b |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #e6e8eb @ 0.06 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | #e6e8eb |
| Text node | a: Inter 16px/24px 400, #13161c | a: Inter 16px/24px 400, #e6e8eb |
| Transition | none | = |
| Icon | 16 x 16, colour #63666d | 16 x 16, colour #a2a5aa |
| Painted layers | div.bg-sidebar.group-data-[variant=floating]:border-sidebar-border 64.0x876.0 bg #f7f8fa r 28px shadow #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button.peer/menu-button.flex 40.0x40.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px; kbd.inline-flex.h-5 0.0x0.0 bg #f2f3f6 r 6px; kbd.inline-flex.h-5 0.0x0.0 bg #f2f3f6 r 6px; div.flex.min-h-0 64.0x608.0 image linear-gradient(#f7f8fa 30%, #000000 @ 0), linear-gradient(#000000 @ 0, #f7f8fa 70%), radi; a.peer/menu-button.flex 40.0x40.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | div.bg-sidebar.group-data-[variant=floating]:border-sidebar-border 64.0x876.0 bg #06070b r 28px shadow #000000 @ 0 0px 0px 0px 0px, #e6e8eb @ 0.06 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button.peer/menu-button.flex 40.0x40.0 bg #15171c r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #272a30 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.3 0px 1px 2px 0px; kbd.inline-flex.h-5 0.0x0.0 bg #191c21 r 6px; kbd.inline-flex.h-5 0.0x0.0 bg #191c21 r 6px; div.flex.min-h-0 64.0x608.0 image linear-gradient(#06070b 30%, #000000 @ 0), linear-gradient(#000000 @ 0, #06070b 70%), radi; a.peer/menu-button.flex 40.0x40.0 bg #15171c r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #272a30 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.3 0px 1px 2px 0px |
| How | resting state | same element after the header Theme menu repaints html.dark |

Crops: `app-sidebar-default.png`, `app-sidebar-dark.png`.

#### app-nav-link

Sidebar nav link. A primary nav link in the sidebar ("Feed"), a peer/menu-button row.

Page: /. Selector: `a[class*="peer/menu-button"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = |
| Padding | 12px | = | = |
| Gap | 10px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | #e9ebef | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1d65c8 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Transition | width, height, padding, color 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #63666d | 16 x 16, colour #13161c | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | a.peer/menu-button.flex 40.0x40.0 bg #e9ebef r 3.35544e+07px | a.peer/menu-button.flex 40.0x40.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1d65c8 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |

Crops: `app-nav-link-default.png`, `app-nav-link-hover.png`, `app-nav-link-focus-visible.png`.

#### app-nav-active

Sidebar active nav link. The link for the page being read ("Home"), painted with the active style.

Page: /. Selector: `a[class*="peer/menu-button"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 12px |
| Gap | 10px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px |
| Outline | none |
| Font | Inter 14px/20px 600 |
| Letter spacing | normal |
| Colour | #13161c |
| Transition | width, height, padding, color 0.15s cubic-bezier(0.16, 1, 0.3, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #13161c |
| Painted layers | a.peer/menu-button.flex 40.0x40.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px |
| How | resting state |

Crops: `app-nav-active-default.png`.

#### app-sidebar-toggle

"Toggle Sidebar" button. The sidebar footer control that collapses the rail — a local UI toggle. "opened" is its own press (the rail collapsed), restored afterwards.

Page: /. Selector: `button (text Toggle Sidebar)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 40 x 40 | = | - |
| Padding | 0px | = | - |
| Gap | 8px | = | - |
| Border | none | = | - |
| Radius | 3.35544e+07px | = | - |
| Background | transparent | #e9ebef | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Inter 14px/20px 600 | = | - |
| Letter spacing | normal | = | - |
| Colour | #63666d | #13161c | - |
| Transition | all 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | - |
| Cursor | pointer | = | - |
| Icon | 16 x 16, colour #63666d | 16 x 16, colour #13161c | - |
| Ancestor paint | 3 up div.bg-sidebar.group-data-[variant=floating]:border-sidebar-border bg #f7f8fa shadow #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | - |
| How | resting state | mouse hover over the element | - |
| Painted layers | - | button.inline-flex.cursor-pointer 40.0x40.0 bg #e9ebef r 3.35544e+07px | = |
| Error | - | = | locator.evaluate: Timeout 8000ms exceeded. |

Crops: `app-sidebar-toggle-default.png`, `app-sidebar-toggle-hover.png`.

#### app-search-button

Search button (Ctrl K). The sidebar "Search" menu-button carrying the ⌘K hint; opens the command search dialog.

Page: /. Selector: `button[class*="peer/menu-button"] (text Search)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 232 x 36 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 10px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #1d65c8 0px 0px 0px 2px, #13161c @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #63666d | = | = |
| Text node | span: Inter 14px/20px 400, #63666d | = | = |
| Transition | width, height, padding, color 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | default | = | = |
| Icon | 18 x 18, colour #63666d | 18 x 18, colour #13161c | = |
| Painted layers | button.peer/menu-button.flex 232.0x36.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px; kbd.inline-flex.h-5 40.8x20.0 bg #f2f3f6 r 6px; kbd.inline-flex.h-5 20.0x20.0 bg #f2f3f6 r 6px | = | button.peer/menu-button.flex 232.0x36.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #1d65c8 0px 0px 0px 2px, #13161c @ 0.05 0px 1px 2px 0px; kbd.inline-flex.h-5 40.8x20.0 bg #f2f3f6 r 6px; kbd.inline-flex.h-5 20.0x20.0 bg #f2f3f6 r 6px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `app-search-button-default.png`, `app-search-button-hover.png`, `app-search-button-focus-visible.png`.

#### app-theme-button

Theme menu button. The "Theme" menu-button that opens Light / Dark / System. "opened" is its own press; the menu is then closed with Escape.

Page: /. Selector: `button[class*="peer/menu-button"] (text Theme)`. States: default, opened, opened-menu.

| Property | default | opened | opened-menu |
|---|---|---|---|
| Size (w x h) | 99 x 32 | = | 300 x 120 |
| Padding | 8px 12px | = | 6px |
| Gap | 10px | = | - |
| Border | none | = | 1px solid #e2e4e8 |
| Radius | 3.35544e+07px | = | 12px |
| Background | transparent | = | #ffffff |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | Inter 16px/24px 400 |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Text node | span: Inter 14px/20px 400, #13161c | = | span.flex.items-center: Inter 14px/20px 400, #13161c |
| Transition | width, height, padding, color 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | none |
| Cursor | default | = | - |
| Icon | 18 x 18, colour #63666d | = | 16 x 16, colour #13161c |
| How | resting state | the "Theme" button's own press (menu open; Escape restores) | the open Light / Dark / System menu — Theme pressed, the painted [role="menu"] itself read; reset closes it with Escape |
| Painted layers | - | = | div.bg-popover.text-popover-foreground 300.0x120.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px; div.focus:bg-accent.focus:text-accent-foreground 90.0x98.0 bg #e9ebef r 8px; span.light.flex 78.0x58.0 bg #f7f8fa r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; span.h-1.5.w-10 40.0x6.0 bg #ced1d6 r 6px; span.flex-1.rounded-sm 62.0x32.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; span.dark.flex 78.0x58.0 bg #0d0f14 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #272a30 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |

Crops: `app-theme-button-default.png`, `app-theme-button-opened.png`, `app-theme-button-opened-menu.png`.

#### app-more-menu

"More" menu button. The "More" menu-button (carries a "New" badge) opening the overflow nav menu. "opened" is its own press, closed with Escape.

Page: /. Selector: `button[class*="peer/menu-button"] (text More)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 129 x 32 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 10px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | #e9ebef | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Text node | span: Inter 14px/20px 400, #13161c | = | = |
| Transition | width, height, padding, color 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | default | = | = |
| Icon | 16 x 16, colour #63666d | 16 x 16, colour #13161c | = |
| Painted layers | span.absolute.-right-1 0.0x0.0 bg #2962ff r 3.35544e+07px; span.ml-auto.inline-flex 41.0x18.0 bg #2962ff r 3.35544e+07px | button.peer/menu-button.flex 129.0x32.0 bg #e9ebef r 3.35544e+07px; span.absolute.-right-1 0.0x0.0 bg #2962ff r 3.35544e+07px; span.ml-auto.inline-flex 41.0x18.0 bg #2962ff r 3.35544e+07px | - |
| How | resting state | mouse hover over the element | the "More" button's own press (menu open; Escape restores) |

Crops: `app-more-menu-default.png`, `app-more-menu-hover.png`, `app-more-menu-opened.png`.

#### app-cta

"Start your blog, free" CTA. The solid sign-up call-to-action in the sidebar footer (bg-primary text-primary-foreground, rounded-full). Links to /login — measured, never followed.

Page: /. Selector: `a[href="/login"] (text Start your blog)`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 241 x 56 | = | = | = | = |
| Padding | 0px 28px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 3.35544e+07px | = | = | = | = |
| Background | #181b20 | #181b20 @ 0.9 | = | #181b20 @ 0.9 | #e6e8eb |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 1px 2px 0px, #000000 @ 0.6 0px 12px 32px -12px |
| Outline | none | = | = | = | = |
| Font | Inter 16px/24px 600 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | = | = | = | #15171c |
| Transition | all 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | = | 18 x 18, colour #15171c |
| Painted layers | a.inline-flex.cursor-pointer 241.0x56.0 bg #181b20 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px | a.inline-flex.cursor-pointer 241.0x56.0 bg #181b20 @ 0.9 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px | a.inline-flex.cursor-pointer 241.0x56.0 bg #181b20 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px | a.inline-flex.cursor-pointer 241.0x56.0 bg #181b20 @ 0.9 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px | a.inline-flex.cursor-pointer 241.0x56.0 bg #e6e8eb r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 1px 2px 0px, #000000 @ 0.6 0px 12px 32px -12px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press | same element after the header Theme menu repaints html.dark |

Crops: `app-cta-default.png`, `app-cta-hover.png`, `app-cta-focus-visible.png`, `app-cta-pressed.png`, `app-cta-dark.png`.

#### app-signin

"Sign in" link. The quiet sign-in link in the sidebar footer — measured, never followed.

Page: /. Selector: `a[href="/login"] (text Sign in)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 232 x 40 | = |
| Padding | 8px 12px | = |
| Gap | 10px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Inter 14px/20px 600 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Text node | span: Inter 14px/20px 600, #13161c | = |
| Transition | width, height, padding, color 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | pointer | = |
| Icon | 18 x 18, colour #13161c | = |
| Painted layers | a.peer/menu-button.flex 232.0x40.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `app-signin-default.png`, `app-signin-hover.png`.

### Feed

#### post-card

Feed post card. A post row in the feed (article.group/card, border-b separator): author avatar + name, time, title, excerpt, cover thumb, upvote/comments/bookmark actions.

Page: /. Selector: `article`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1020 x 293.16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | #e6e8eb |
| Text node | span.relative.inline-flex: Inter 12px/16px 600, #63666d | span.relative.inline-flex: Inter 12px/16px 600, #a2a5aa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Icon | 14 x 14, colour #63666d | 14 x 14, colour #a2a5aa |
| Painted layers | div.relative.aspect-[800/420] 558.4x293.2 bg #f2f3f6 r 12px; div.pointer-events-none.absolute 558.4x293.2 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex 24.0x24.0 bg #f2f3f6 r 3.35544e+07px; div.relative.aspect-[800/420] 0.0x0.0 bg #f2f3f6 r 12px; div.pointer-events-none.absolute 0.0x0.0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; button.inline-flex.h-8 53.0x32.0 bg #f2f3f6 r 3.35544e+07px | div.relative.aspect-[800/420] 558.4x293.2 bg #191c21 r 12px; div.pointer-events-none.absolute 558.4x293.2 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex 24.0x24.0 bg #191c21 r 3.35544e+07px; div.relative.aspect-[800/420] 0.0x0.0 bg #191c21 r 12px; div.pointer-events-none.absolute 0.0x0.0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; button.inline-flex.h-8 53.0x32.0 bg #191c21 r 3.35544e+07px |
| How | resting state | same element after the header Theme menu repaints html.dark |

Crops: `post-card-default.png`, `post-card-dark.png`.

#### post-title-link

Post title link. The post's title inside a feed card — the card's main link.

Page: /. Selector: `article a (title)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 429.56 x 185.16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #2962ff offset 2px |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Text node | h3.line-clamp-2.text-title-3: Inter 24px/32px 600, #13161c, ls -0.24px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.block.transition-colors 429.6x185.2 outline 2px solid #2962ff offset 2px |

Crops: `post-title-link-default.png`, `post-title-link-hover.png`, `post-title-link-focus-visible.png`.

#### post-upvote

Upvote button. The upvote action under a feed card (aria-label "Upvote"): count + arrow icon — measured, never pressed.

Page: /. Selector: `article button[aria-label*="Upvote" i]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53 x 32 | = | = | = |
| Padding | 0px 12px 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #f2f3f6 | #e9ebef | = | #e9ebef |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #2962ff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #13161c | = | = | = |
| Text node | span: Inter 14px/20px 400, #13161c | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #13161c | = | = | = |
| Painted layers | button.inline-flex.h-8 53.0x32.0 bg #f2f3f6 r 3.35544e+07px | button.inline-flex.h-8 53.0x32.0 bg #e9ebef r 3.35544e+07px | button.inline-flex.h-8 53.0x32.0 bg #f2f3f6 r 3.35544e+07px outline 2px solid #2962ff offset 2px | button.inline-flex.h-8 53.0x32.0 bg #e9ebef r 3.35544e+07px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `post-upvote-default.png`, `post-upvote-hover.png`, `post-upvote-focus-visible.png`, `post-upvote-pressed.png`.

#### post-bookmark

Bookmark icon button. The bookmark action under a feed card (aria-label "Bookmark this post") — an icon-only ghost button.

Page: /. Selector: `article button[aria-label*="Bookmark" i]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #f2f3f6 | #e9ebef | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #2962ff offset 2px |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | default | = | = |
| Icon | 16 x 16, colour #13161c | = | = |
| Painted layers | button.inline-flex.size-8 32.0x32.0 bg #f2f3f6 r 3.35544e+07px | button.inline-flex.size-8 32.0x32.0 bg #e9ebef r 3.35544e+07px | button.inline-flex.size-8 32.0x32.0 bg #f2f3f6 r 3.35544e+07px outline 2px solid #2962ff offset 2px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `post-bookmark-default.png`, `post-bookmark-hover.png`, `post-bookmark-focus-visible.png`.

#### post-comments-link

Comments link. The comments-count link under a feed card, pointing at the post's discussion page.

Page: /. Selector: `article a[aria-label*="comment" i]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 103 x 32 | = |
| Padding | 0px 6px 0px 10px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | #f2f3f6 | #e9ebef |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Text node | span: Inter 14px/20px 400, #13161c | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #13161c | = |
| Painted layers | a.inline-flex.h-8 103.0x32.0 bg #f2f3f6 r 3.35544e+07px; span.relative.inline-flex 20.0x20.0 bg #f2f3f6 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f2f3f6 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex 20.0x20.0 bg #f2f3f6 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f2f3f6 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex 20.0x20.0 bg #f2f3f6 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f2f3f6 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.h-8 103.0x32.0 bg #e9ebef r 3.35544e+07px; span.relative.inline-flex 20.0x20.0 bg #f2f3f6 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f2f3f6 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex 20.0x20.0 bg #f2f3f6 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f2f3f6 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.relative.inline-flex 20.0x20.0 bg #f2f3f6 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f2f3f6 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | mouse hover over the element |

Crops: `post-comments-link-default.png`, `post-comments-link-hover.png`.

#### post-author

Author link + avatar. The author row on a feed card: avatar image and profile link.

Page: /. Selector: `article a[href^="/@"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 162 x 24 | = |
| Padding | 0px | = |
| Gap | 10px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Text node | span.relative.inline-flex: Inter 12px/16px 600, #63666d | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.relative.inline-flex 24.0x24.0 bg #f2f3f6 r 3.35544e+07px | = |
| How | resting state | mouse hover over the element |

Crops: `post-author-default.png`, `post-author-hover.png`.

#### feed-load-more

"Load more" button. The feed's pagination button — measured, never pressed (it would grow the stream).

Page: /feed. Selector: `button[aria-label*="Load more" i]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 101 x 32 | = | = |
| Padding | 0px 12px | = | = |
| Gap | 6px | = | = |
| Border | 1px solid #ced1d6 | = | 1px solid #2962ff |
| Radius | 8px | = | = |
| Background | #ffffff | #e9ebef | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Text node | span: Inter 14px/20px 600, #13161c | = | = |
| Transition | all 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.inline-flex.cursor-pointer 101.0x32.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | button.inline-flex.cursor-pointer 101.0x32.0 bg #e9ebef border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | button.inline-flex.cursor-pointer 101.0x32.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.05 0px 1px 2px 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `feed-load-more-default.png`, `feed-load-more-hover.png`, `feed-load-more-focus-visible.png`.

#### feed-trending

Trending aside. The "Trending" rail beside the feed column (aria-label "Trending").

Page: /feed. Selector: `aside[aria-label*="Trending" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352 x 3861.77 |
| Padding | 0px |
| Border | none |
| Radius | 28px |
| Background | #f7f8fa |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | h3.min-w-0.text-title-3: Inter 20px/28px 600, #13161c |
| Transition | none |
| Icon | 14 x 14, colour #2962ff |
| Painted layers | aside.my-3.mr-3 352.0x3861.8 bg #f7f8fa r 28px shadow #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.rounded-xl.border 304.0x586.0 bg #fbfcfd border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; img.size-5.rounded-full 20.0x20.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; img.size-5.rounded-full 20.0x20.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; img.size-5.rounded-full 20.0x20.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; img.size-5.rounded-full 20.0x20.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state |

Crops: `feed-trending-default.png`.

### Discussion

#### comment-box

Comment textarea. The "Share your thoughts…" textarea on a discussion page. "focused" is the field clicked into — nothing is typed.

Page: /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed. Selector: `textarea[placeholder*="Share your thoughts" i]`. States: default, focused, dark.

| Property | default | focused | dark |
|---|---|---|---|
| Size (w x h) | 670 x 72 | - | = |
| Padding | 12px 16px | - | = |
| Border | none | - | = |
| Radius | 0px | - | = |
| Background | transparent | - | = |
| Box shadow | none | - | = |
| Outline | none | - | = |
| Font | -apple-system 14px/20px 400 | - | = |
| Letter spacing | normal | - | = |
| Colour | #13161c | - | #e6e8eb |
| Transition | none | - | = |
| Cursor | text | - | = |
| Placeholder | #63666d, opacity 1 | - | #a2a5aa, opacity 1 |
| Ancestor paint | 1 up div.overflow-hidden.rounded-xl bg #ffffff | - | 1 up div.overflow-hidden.rounded-xl bg #0d0f14 |
| How | resting state | - | same element after the header Theme menu repaints html.dark |
| Error | - | locator.evaluate: Timeout 8000ms exceeded. | = |

Crops: `comment-box-default.png`, `comment-box-dark.png`.

#### comment-submit

"Comment" button. The submit under the comment box — measured, never pressed.

Page: /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed. Selector: `button (text Comment)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 92.64 x 32 | = | = |
| Padding | 0px 12px | = | = |
| Gap | 6px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #f2f3f6 | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = |
| Font | -apple-system 14px/20px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #9a9da3 | = | = |
| Transition | all 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.inline-flex.cursor-pointer 92.6x32.0 bg #f2f3f6 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `comment-submit-default.png`, `comment-submit-hover.png`, `comment-submit-focus-visible.png`.

#### post-share

Share icon button. The "Share this post" icon button — measured, never pressed.

Page: /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed. Selector: `button[aria-label*="Share" i]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #f2f3f6 | #e9ebef | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #2962ff offset 2px |
| Font | -apple-system 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | default | = | = |
| Icon | 16 x 16, colour #13161c | = | = |
| Painted layers | button.inline-flex.size-8 32.0x32.0 bg #f2f3f6 r 3.35544e+07px | button.inline-flex.size-8 32.0x32.0 bg #e9ebef r 3.35544e+07px | button.inline-flex.size-8 32.0x32.0 bg #f2f3f6 r 3.35544e+07px outline 2px solid #2962ff offset 2px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `post-share-default.png`, `post-share-hover.png`, `post-share-focus-visible.png`.

#### post-more-options

"More options" icon button. The overflow action on a comment row (aria-label "More options") — measured, never pressed.

Page: /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed. Selector: `button[aria-label*="More options" i]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | #f2f3f6 |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #63666d | #13161c |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | default | = |
| Icon | 14 x 14, colour #63666d | 14 x 14, colour #13161c |
| How | resting state | mouse hover over the element |
| Painted layers | - | button.inline-flex.size-6 24.0x24.0 bg #f2f3f6 r 8px |

Crops: `post-more-options-default.png`, `post-more-options-hover.png`.

#### comment-reply

"Reply" button. The reply action under a comment — measured, never pressed.

Page: /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed. Selector: `button (text Reply)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 84.63 x 32 | = |
| Padding | 0px 12px | = |
| Gap | 4px | = |
| Border | 1px solid #e2e4e8 | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | #e9ebef |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 14px/20px 600 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #13161c | = |
| Painted layers | button.inline-flex.h-8 84.6x32.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | button.inline-flex.h-8 84.6x32.0 bg #e9ebef border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state | mouse hover over the element |

Crops: `comment-reply-default.png`, `comment-reply-hover.png`.

### Profile

#### profile-header

Profile header. The sticky profile bar (avatar, name, handle, Share button) above the sections nav.

Page: /@anish78. Selector: `header.sticky`. States: .

Not found on the page at capture time.

#### profile-nav

Profile sections nav. The "Profile sections" tab-like nav (Posts / Series / …) under the header.

Page: /@anish78. Selector: `nav[aria-label*="Profile sections" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 676 x 48 |
| Padding | 0px |
| Gap | 24px |
| Border | T: none; R: none; B: 1px solid #e2e4e8; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | a.-mb-px.inline-flex: -apple-system 14px/20px 600, #13161c |
| Transition | none |
| Painted layers | nav.flex.h-12 676.0x48.0 border B:1px solid; a.-mb-px.inline-flex 53.1x48.0 border B:2px solid; a.-mb-px.inline-flex 75.6x48.0 border B:2px solid |
| How | resting state |

Crops: `profile-nav-default.png`.

#### profile-share

Profile "Share" button. The outlined Share action in the profile header — measured, never pressed.

Page: /@anish78. Selector: `button (text Share)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 89.72 x 36 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #ced1d6 | = | 1px solid #2962ff |
| Radius | 8px | = | = |
| Background | #ffffff | #e9ebef | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | -apple-system 14px/20px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Text node | span: -apple-system 14px/20px 600, #13161c | = | = |
| Transition | all 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #13161c | = | = |
| Painted layers | button.inline-flex.cursor-pointer 89.7x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | button.inline-flex.cursor-pointer 89.7x36.0 bg #e9ebef border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | button.inline-flex.cursor-pointer 89.7x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.05 0px 1px 2px 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `profile-share-default.png`, `profile-share-hover.png`, `profile-share-focus-visible.png`.

### Pro

#### pro-plan-card

Plan card. A Pro / Growth pricing card on /pro.

Page: /pro. Selector: `main box (priced plan)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 233.72 x 92 |
| Padding | 8px 0px 0px 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | span.text-chapter.text-foreground: -apple-system 56px/60px 600, #13161c, ls -1.68px |
| Transition | none |
| How | resting state |

Crops: `pro-plan-card-default.png`.

#### pro-cta

"Get Pro" CTA. A plan call-to-action ("Get Pro, $5 a month") — links to /login, measured never followed.

Page: /pro. Selector: `a (text Get Pro)`. States: .

Not found on the page at capture time.

#### faq-question

FAQ accordion question. A question row in the /pro FAQ accordion. "opened" is its own press revealing the answer.

Page: /pro. Selector: `button (text What do I get with Pro)`. States: default, hover, focus-visible, opened.

| Property | default | hover | focus-visible | opened |
|---|---|---|---|---|
| Size (w x h) | 860 x 52 | = | = | 860 x 64 |
| Padding | 20px 0px 8px 0px | = | = | 20px 0px |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #13161c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #13161c | = | = | 16 x 16, colour #63666d |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | the question row's own press (answer visible; pressed again to close) |
| Painted layers | - | = | button.flex.flex-1 860.0x52.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-opened.png`.

### Changelog

#### changelog-tablist

Category tablist. The All / Features / Improvements / Fixes / Deprecated tablist.

Page: /changelog. Selector: `[role="tablist"], [class*="tabs-list"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 423.94 x 34 |
| Padding | 3px |
| Border | none |
| Radius | 8px |
| Background | #f2f3f6 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #63666d |
| Text node | button.text-muted-foreground.hover:text-foreground: -apple-system 14px/20px 600, #13161c |
| Transition | none |
| Painted layers | div.group/tabs-list.text-muted-foreground 423.9x34.0 bg #f2f3f6 r 8px; button.text-muted-foreground.hover:text-foreground 42.2x28.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px |
| How | resting state |

Crops: `changelog-tablist-default.png`.

#### changelog-tab

Category tab. One category tab. "selected" is the tab's own activation — a local UI toggle that re-filters the list.

Page: /changelog. Selector: `[role="tab"]`. States: default, hover, focus-visible, selected.

| Property | default | hover | focus-visible | selected |
|---|---|---|---|---|
| Size (w x h) | 85 x 28 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | #ffffff | #ffffff |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px |
| Outline | none | = | 1px solid #2962ff offset 2px | = |
| Font | -apple-system 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #63666d | #13161c | #13161c | #13161c |
| Transition | color, box-shadow, border-color 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | default | = | = | = |
| Ancestor paint | 1 up div.group/tabs-list.text-muted-foreground bg #f2f3f6 | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | the tab's own activation (aria-selected) |
| Painted layers | - | = | button.text-muted-foreground.hover:text-foreground 85.0x28.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.05 0px 1px 2px 0px outline 1px solid #2962ff offset 2px | button.text-muted-foreground.hover:text-foreground 85.0x28.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px |

Crops: `changelog-tab-default.png`, `changelog-tab-hover.png`, `changelog-tab-focus-visible.png`, `changelog-tab-selected.png`.

### Agents

#### agents-tab

Install-method tab. One of the MCP server / Agent skill / CLI tabs. "selected" is its own activation.

Page: /agents. Selector: `[role="tab"]`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 329.33 x 110 | = | = |
| Padding | 20px 24px | = | = |
| Gap | 6px | = | = |
| Border | none | = | = |
| Radius | 16px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px, #13161c @ 0.05 0px 1px 2px 0px | = | = |
| Outline | none | = | = |
| Font | -apple-system 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Text node | span.text-title-4.text-foreground: -apple-system 16px/24px 600, #13161c | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.flex.cursor-pointer 329.3x110.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px, #13161c @ 0.05 0px 1px 2px 0px | = | = |
| How | resting state | mouse hover over the element | the tab's own activation (aria-selected) |

Crops: `agents-tab-default.png`, `agents-tab-hover.png`, `agents-tab-selected.png`.

#### agents-copy

"Copy to clipboard" button. The copy icon-button beside an install command — pressed only with forcePseudoState.

Page: /agents. Selector: `button[aria-label*="Copy" i]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #23262c | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6293ff offset 2px | = |
| Font | -apple-system 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a2a5aa | #e6e8eb | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #a2a5aa | 14 x 14, colour #e6e8eb | = | = |
| Ancestor paint | 1 up div.dark.group/code bg #15171c | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Painted layers | - | button.absolute.top-1 32.0x32.0 bg #23262c r 8px | button.absolute.top-1 32.0x32.0 r 8px outline 2px solid #6293ff offset 2px | = |

Crops: `agents-copy-default.png`, `agents-copy-hover.png`, `agents-copy-focus-visible.png`, `agents-copy-pressed.png`.

### Onboarding form

#### onboard-input

Text input (name). The "Alex Johnson" placeholder name field — measured at rest; nothing is entered.

Page: /onboard. Selector: `input`. States: .

Not found on the page at capture time.

#### onboard-combobox

Combobox (city). The "City, Country" location combobox — measured at rest, never opened (it would fetch suggestions).

Page: /onboard. Selector: `[role="combobox"]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 386 x 40 | = |
| Padding | 4px 12px 4px 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | -apple-system 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | text | = |
| Placeholder | #63666d, opacity 1 | = |
| Painted layers | input.file:text-foreground.placeholder:text-muted-foreground 386.0x40.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | input.file:text-foreground.placeholder:text-muted-foreground 386.0x40.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Ancestor paint | 1 up div.group/input-group.border-input shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | 1 up div.group/input-group.border-input shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #13161c @ 0.05 0px 1px 2px 0px |
| How | resting state | keyboard focus (Shift+Tab, Tab) |

Crops: `onboard-combobox-default.png`, `onboard-combobox-focus-visible.png`.

#### onboard-textarea

Tagline textarea. The bio/tagline textarea — measured at rest.

Page: /onboard. Selector: `textarea`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 416 x 68 | = |
| Padding | 8px 12px | = |
| Border | 1px solid #ced1d6 | 1px solid #2962ff |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | -apple-system 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | text | = |
| Placeholder | #63666d, opacity 1 | = |
| Painted layers | textarea.border-input.placeholder:text-muted-foreground 416.0x68.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | textarea.border-input.placeholder:text-muted-foreground 416.0x68.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | keyboard focus (Shift+Tab, Tab) |

Crops: `onboard-textarea-default.png`, `onboard-textarea-focus-visible.png`.

#### onboard-upload

"Upload photo" button. The avatar upload control — measured, never pressed (it opens a file dialog).

Page: /onboard. Selector: `button (text Upload photo)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 120.81 x 32 | = |
| Padding | 0px 12px | = |
| Gap | 6px | = |
| Border | 1px solid #ced1d6 | = |
| Radius | 8px | = |
| Background | #ffffff | #e9ebef |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | -apple-system 14px/20px 600 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Transition | all 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.inline-flex.cursor-pointer 120.8x32.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | button.inline-flex.cursor-pointer 120.8x32.0 bg #e9ebef border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px |
| How | resting state | mouse hover over the element |

Crops: `onboard-upload-default.png`, `onboard-upload-hover.png`.

#### onboard-next

"Next" button. The form's primary action — measured, never pressed (it would submit).

Page: /onboard. Selector: `button (text Next)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 416 x 40 | = | = |
| Padding | 0px 16px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #181b20 | #181b20 @ 0.9 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 1px 0px 0px inset, #13161c @ 0.2 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #ffffff @ 0.12 0px 1px 0px 0px inset, #13161c @ 0.2 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | -apple-system 14px/20px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | all 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #ffffff | = | = |
| Painted layers | button.inline-flex.cursor-pointer 416.0x40.0 bg #181b20 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 1px 0px 0px inset, #13161c @ 0.2 0px 1px 2px 0px | button.inline-flex.cursor-pointer 416.0x40.0 bg #181b20 @ 0.9 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 1px 0px 0px inset, #13161c @ 0.2 0px 1px 2px 0px | button.inline-flex.cursor-pointer 416.0x40.0 bg #181b20 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 3px, #ffffff @ 0.12 0px 1px 0px 0px inset, #13161c @ 0.2 0px 1px 2px 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `onboard-next-default.png`, `onboard-next-hover.png`, `onboard-next-focus-visible.png`.

### Brand

#### brand-swatch

Palette swatch button. A named colour swatch on /brand (Graphite 500) — a button that copies the value.

Page: /brand. Selector: `button (text Graphite 500)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 257 x 173 | = |
| Padding | 16px | = |
| Gap | 4px | = |
| Border | T: none; R: none; B: 1px solid #e2e4e8; L: 1px solid #e2e4e8 | = |
| Radius | 0px | = |
| Background | transparent | #f2f3f6 |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Text node | span.pt-2.text-title-4: -apple-system 16px/24px 600, #13161c | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.flex.cursor-pointer 257.0x173.0 border B:1px solid / L:1px solid; span.h-14.w-full 224.0x56.0 bg #717379 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | button.flex.cursor-pointer 257.0x173.0 bg #f2f3f6 border B:1px solid / L:1px solid; span.h-14.w-full 224.0x56.0 bg #717379 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | mouse hover over the element |

Crops: `brand-swatch-default.png`, `brand-swatch-hover.png`.

### Blog chrome

#### th-header

Blog header bar. The sticky blog header (border-b, backdrop blur): wordmark, the pill main nav, Search (Ctrl K) and Toggle theme buttons.

Page: /. Selector: `header`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1440 x 72 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffffff @ 0.8 | #0d0f14 @ 0.8 |
| Box shadow | none | = |
| Backdrop filter | blur(12px) | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | #e6e8eb |
| Text node | span.col-start-1.row-start-1: -apple-system 14px/20px 400, #13161c | span.col-start-1.row-start-1: -apple-system 14px/20px 400, #e6e8eb |
| Transition | transform, translate, scale, rotate 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Icon | 22 x 22, colour #63666d | 22 x 22, colour #a2a5aa |
| Painted layers | header.sticky.top-0 1440.0x72.0 bg #ffffff @ 0.8; span.h-5.w-px 7.8x19.1 bg #ced1d6; ul.flex.h-9 468.6x36.0 bg #f7f8fa border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; button.hidden.h-9 128.3x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; kbd.font-keys.inline-flex 36.0x24.0 bg #f2f3f6 r 3.35544e+07px; a.items-center.justify-center 92.4x36.0 bg #181b20 r 3.35544e+07px | header.sticky.top-0 1440.0x72.0 bg #0d0f14 @ 0.8; span.h-5.w-px 7.8x19.1 bg #3a3d44; ul.flex.h-9 468.6x36.0 bg #121419 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; button.hidden.h-9 128.3x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; kbd.font-keys.inline-flex 36.0x24.0 bg #191c21 r 3.35544e+07px; a.items-center.justify-center 92.4x36.0 bg #e6e8eb r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.min-h-screen bg #ffffff | 1 up div.flex.min-h-screen bg #0d0f14 |
| How | resting state | same element after prefers-color-scheme repaints html.dark (the signal the blog engine honours; its own toggle produced no repaint headless) |

Crops: `th-header-default.png`.

#### th-nav

Main navigation pill. The centred pill nav (bg-surface, rounded-full border) holding the publication's nav links.

Page: /. Selector: `nav[aria-label="Main navigation"] [class*="rounded-full"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 468.59 x 36 |
| Padding | 2px |
| Gap | 2px |
| Border | 1px solid #e2e4e8 |
| Radius | 3.35544e+07px |
| Background | #f7f8fa |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | span.col-start-1.row-start-1: -apple-system 14px/20px 400, #13161c |
| Transition | none |
| Icon | 12 x 12, colour #63666d |
| Painted layers | ul.flex.h-9 468.6x36.0 bg #f7f8fa border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state |

Crops: `th-nav-default.png`.

#### th-nav-link

Nav link. A nav item in the pill ("News 📰"), hover:bg-background.

Page: /. Selector: `nav[aria-label="Main navigation"] a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 86.97 x 30 | = | = |
| Padding | 0px 14px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | #ffffff | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #2962ff offset 2px |
| Font | -apple-system 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Text node | span.col-start-1.row-start-1: -apple-system 14px/20px 400, #13161c | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | a.inline-flex.h-full 87.0x30.0 bg #ffffff r 3.35544e+07px | a.inline-flex.h-full 87.0x30.0 r 3.35544e+07px outline 2px solid #2962ff offset 2px |

Crops: `th-nav-link-default.png`, `th-nav-link-hover.png`, `th-nav-link-focus-visible.png`.

#### th-search-button

Search button (Ctrl K). The header search button (aria-label "Open search (press Control or Command and K)") carrying the ⌘K hint.

Page: /. Selector: `button[aria-label*="Open search" i]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 128.28 x 36 | = | = |
| Padding | 0px 6px 0px 12px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #e2e4e8 | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | #f7f8fa | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #2962ff offset 2px |
| Font | -apple-system 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #63666d | = | = |
| Text node | span: -apple-system 14px/20px 400, #63666d | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Icon | 12 x 12, colour #63666d | = | = |
| Painted layers | button.hidden.h-9 128.3x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; kbd.font-keys.inline-flex 36.0x24.0 bg #f2f3f6 r 3.35544e+07px | button.hidden.h-9 128.3x36.0 bg #f7f8fa border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; kbd.font-keys.inline-flex 36.0x24.0 bg #f2f3f6 r 3.35544e+07px | button.hidden.h-9 128.3x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px outline 2px solid #2962ff offset 2px; kbd.font-keys.inline-flex 36.0x24.0 bg #f2f3f6 r 3.35544e+07px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `th-search-button-default.png`, `th-search-button-hover.png`, `th-search-button-focus-visible.png`.

#### th-theme-toggle

"Toggle theme" button. The header theme toggle. Pressed headless it produced no repaint and no menu (verified 2026-11-17) — measured at rest and after the prefers-color-scheme repaint, which is how the engine shows dark.

Page: /. Selector: `button[aria-label*="theme" i], button:has-text("Toggle theme")`. States: default, darkblog.

| Property | default | darkblog |
|---|---|---|
| Size (w x h) | 36 x 36 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 3.35544e+07px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 14px/20px 600 | = |
| Letter spacing | normal | = |
| Colour | #63666d | #a2a5aa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #63666d | 0 x 0, colour #a2a5aa |
| How | resting state | same element after prefers-color-scheme repaints html.dark (the signal the blog engine honours; its own toggle produced no repaint headless) |

Crops: `th-theme-toggle-default.png`.

#### th-more-menu

"More" menu button. The header overflow menu. "opened" is its own press, closed with Escape.

Page: /. Selector: `button (text More)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 76.58 x 30 | = | = |
| Padding | 0px 12px 0px 14px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | transparent | #ffffff | #ffffff |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | -apple-system 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Icon | 12 x 12, colour #63666d | = | = |
| How | resting state | mouse hover over the element | the "More" button's own press (menu open; Escape restores) |
| Painted layers | - | button.inline-flex.h-full 76.6x30.0 bg #ffffff r 3.35544e+07px | button.inline-flex.h-full 76.6x30.0 bg #ffffff r 3.35544e+07px |

Crops: `th-more-menu-default.png`, `th-more-menu-hover.png`, `th-more-menu-opened.png`.

#### th-about

About-the-publication aside. The "About the publication" sidebar card on the index.

Page: /. Selector: `aside[aria-label*="About the publication" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1120 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | a.transition-colors.hover:text-muted-foreground: -apple-system 20px/28px 600, #13161c |
| Transition | none |
| Icon | 14 x 14, colour #13161c |
| Painted layers | div.flex.flex-col 1120.0x144.0 bg #f7f8fa r 20px; a.inline-flex.size-9 36.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; a.inline-flex.size-9 36.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; a.inline-flex.size-9 36.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state |

Crops: `th-about-default.png`.

#### th-footer

Blog footer. The footer (aria-label "Footer") with the publication's footer nav and "Powered by Hashnode" link.

Page: /. Selector: `footer`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1440 x 153 | = |
| Padding | 0px | = |
| Border | T: 1px solid #e2e4e8; R: none; B: none; L: none | T: 1px solid #272a30; R: none; B: none; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | #e6e8eb |
| Text node | time: -apple-system 14px/20px 400, #63666d | time: -apple-system 14px/20px 400, #a2a5aa |
| Transition | none | = |
| Icon | 14 x 14, colour #2962ff | 14 x 14, colour #6293ff |
| Painted layers | footer.mt-auto.border-t 1440.0x153.0 border T:1px solid; a.inline-flex.h-8 193.5x32.0 bg #f2f3f6 r 3.35544e+07px | footer.mt-auto.border-t 1440.0x153.0 border T:1px solid; a.inline-flex.h-8 193.5x32.0 bg #191c21 r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.min-h-screen bg #ffffff | 1 up div.flex.min-h-screen bg #0d0f14 |
| How | resting state | same element after prefers-color-scheme repaints html.dark (the signal the blog engine honours; its own toggle produced no repaint headless) |

Crops: `th-footer-default.png`, `th-footer-dark.png`.

### Blog feed

#### th-post-card

Post card. A post row on the blog index (li > article): cover thumb, title, excerpt, author + date.

Page: /. Selector: `li article, li[class*="py-5"]`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 651.59 x 514.08 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | #e6e8eb |
| Text node | span.absolute.left-3: -apple-system 12px/16px 600, #13161c | span.absolute.left-3: -apple-system 12px/16px 600, #e6e8eb |
| Transition | none | = |
| Icon | 12 x 12, colour #13161c | 12 x 12, colour #e6e8eb |
| Painted layers | div.relative.aspect-[800/420] 651.6x342.1 bg #f2f3f6 r 20px; div::after.relative.aspect-[800/420] 651.594pxx342.078px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px; span.absolute.left-3 79.7x24.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | div.relative.aspect-[800/420] 651.6x342.1 bg #191c21 r 20px; div::after.relative.aspect-[800/420] 651.594pxx342.078px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px; span.absolute.left-3 79.7x24.0 bg #0d0f14 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.3 0px 1px 2px 0px |
| How | resting state | same element after prefers-color-scheme repaints html.dark (the signal the blog engine honours; its own toggle produced no repaint headless) |

Crops: `th-post-card-default.png`, `th-post-card-dark.png`.

#### th-post-title

Post title link. The title link inside an index card.

Page: /. Selector: `article a, li a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 651.59 x 514.08 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Text node | span.absolute.left-3: -apple-system 12px/16px 600, #13161c | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #13161c | = |
| Painted layers | div.relative.aspect-[800/420] 651.6x342.1 bg #f2f3f6 r 20px; div::after.relative.aspect-[800/420] 651.594pxx342.078px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px; span.absolute.left-3 79.7x24.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `th-post-title-default.png`, `th-post-title-hover.png`.

#### th-load-more

"Load more posts" button. The index pagination button — measured, never pressed.

Page: /. Selector: `button[aria-label*="Load more" i]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 149.47 x 36 | = | = |
| Padding | 0px 16px | = | = |
| Gap | 8px | = | = |
| Border | 1px solid #ced1d6 | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #ffffff | #e9ebef | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | -apple-system 14px/20px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #13161c | = | = |
| Text node | span: -apple-system 14px/20px 600, #13161c | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Painted layers | button.inline-flex.items-center 149.5x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | button.inline-flex.items-center 149.5x36.0 bg #e9ebef border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | button.inline-flex.items-center 149.5x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #2962ff @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `th-load-more-default.png`, `th-load-more-hover.png`, `th-load-more-focus-visible.png`.

### Blog prose

#### th-article-header

Article header. The page-frame article header: title (text-article-title), meta, cover.

Page: /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps. Selector: `header.page-frame, header`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 1120 x 391 | = |
| Padding | 80px 0px 0px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | #e6e8eb |
| Text node | h1.text-article-title.text-pretty: -apple-system 36px/44px 600, #13161c, ls -0.54px | h1.text-article-title.text-pretty: -apple-system 36px/44px 600, #e6e8eb, ls -0.54px |
| Transition | none | = |
| Icon | 14 x 14, colour #63666d | 14 x 14, colour #a2a5aa |
| Painted layers | a.group.flex 680.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 16px | = |
| How | resting state | same element after prefers-color-scheme repaints html.dark (the signal the blog engine honours; its own toggle produced no repaint headless) |

Crops: `th-article-header-default.png`, `th-article-header-dark.png`.

#### th-prose-h1

Article title (h1). The post title, text-article-title.

Page: /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps. Selector: `main h1`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 680 x 132 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 36px/44px 600 | = |
| Letter spacing | -0.54px | = |
| Colour | #13161c | #e6e8eb |
| Transition | none | = |
| How | resting state | same element after prefers-color-scheme repaints html.dark (the signal the blog engine honours; its own toggle produced no repaint headless) |

Crops: `th-prose-h1-default.png`, `th-prose-h1-dark.png`.

#### th-prose-h2

Section heading (h2). An in-article heading.

Page: /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 680 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 24px/32px 600 |
| Letter spacing | -0.24px |
| Colour | #13161c |
| Transition | none |
| Icon | 16 x 16, colour #63666d |
| How | resting state |

Crops: `th-prose-h2-default.png`.

#### th-prose-p

Body paragraph. A paragraph of article prose (text-reading).

Page: /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps. Selector: `main p (sentence)`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 680 x 168 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 18px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #292b30 | #d5d7db |
| Transition | none | = |
| How | resting state | same element after prefers-color-scheme repaints html.dark (the signal the blog engine honours; its own toggle produced no repaint headless) |

Crops: `th-prose-p-default.png`, `th-prose-p-dark.png`.

#### th-prose-link

Prose link. A body-text link inside the article.

Page: /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps. Selector: `main p a, main li a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 60.02 x 24 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 2px solid #2962ff offset 2px |
| Font | -apple-system 18px/28px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2962ff | = | = |
| Transition | text-decoration-color 0.15s ease | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a 60.0x24.0 outline 2px solid #2962ff offset 2px |

Crops: `th-prose-link-default.png`, `th-prose-link-hover.png`, `th-prose-link-focus-visible.png`.

#### th-code-block

Code block. A fenced code block in the article (bg-code-block, tinted dark in both themes).

Page: /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps. Selector: `main pre, [class*="code"]`. States: .

Not found on the page at capture time.

#### th-toc

"On this page" TOC. The article's table-of-contents rail (aria-label "On this page").

Page: /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps. Selector: `nav[aria-label*="On this page" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 208 x 380 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | a.block.py-1: -apple-system 14px/20px 400, #63666d |
| Transition | none |
| How | resting state |

Crops: `th-toc-default.png`.

#### th-toc-link

TOC link. One entry in the table of contents.

Page: /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps. Selector: `nav[aria-label*="On this page" i] a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 208 x 28 | = |
| Padding | 4px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #63666d | #13161c |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `th-toc-link-default.png`, `th-toc-link-hover.png`.

### Blog archive

#### th-pagination

Pagination nav. The archive's Previous / Next pagination (aria-label "Pagination").

Page: /archive. Selector: `nav[aria-label*="Pagination" i]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1120 x 82 |
| Padding | 40px 0px 0px 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | span: -apple-system 14px/20px 600, #13161c |
| Transition | none |
| Icon | 16 x 16, colour #13161c |
| Painted layers | button.inline-flex.items-center 109.9x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; ol.hidden.list-none 217.1x42.0 bg #f7f8fa border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; span.inline-flex.size-8 32.0x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px; a.inline-flex.items-center 91.5x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px |
| How | resting state |

Crops: `th-pagination-default.png`.

#### th-page-prev

"Previous" button. The previous-page control — measured, never pressed.

Page: /archive. Selector: `button (text Previous)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 109.92 x 36 | = |
| Padding | 0px 16px | = |
| Gap | 8px | = |
| Border | 1px solid #ced1d6 | = |
| Radius | 3.35544e+07px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 14px/20px 600 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Text node | span: -apple-system 14px/20px 600, #13161c | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Opacity | 0.5 | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #13161c | = |
| Painted layers | button.inline-flex.items-center 109.9x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px | = |
| How | resting state | mouse hover over the element |

Crops: `th-page-prev-default.png`, `th-page-prev-hover.png`.

### App search

#### app-search-input

Search input. The command field in the open dialog; "focused" is the field clicked into — nothing is typed.

Page: /. Selector: `[role="dialog"] input, [cmdk-input], input[type="search"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 622 x 48 | = |
| Padding | 12px 48px 12px 0px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #63666d, opacity 1 | = |
| How | resting state | the field clicked into |

Crops: `app-search-input-default.png`, `app-search-input-focused.png`.

#### app-search-item

Suggestion row. A suggestion row in the open menu.

Page: /. Selector: `[cmdk-item], [role="option"], [role="dialog"] li`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 638 x 40 | = |
| Padding | 10px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #e9ebef | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #63666d | = |
| Painted layers | div.data-[selected=true]:bg-accent.data-[selected=true]:text-accent-foreground 638.0x40.0 bg #e9ebef r 8px | = |
| How | resting state | mouse hover over the element |

Crops: `app-search-item-default.png`, `app-search-item-hover.png`.

#### app-search-dialog

Search dialog. The ⌘K command dialog, painted by the page's own shortcut.

Page: /. Selector: `[role="dialog"], [cmdk-root]`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 672 x 594 | = |
| Padding | 0px | = |
| Gap | 16px | = |
| Border | 1px solid #e2e4e8 | 1px solid #272a30 |
| Radius | 12px | = |
| Background | #ffffff | #1b1e23 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 1px 2px 0px, #000000 @ 0.6 0px 12px 32px -12px |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | #e6e8eb |
| Text node | kbd.inline-flex.h-5: ui-monospace 12px/16px 600, #63666d | kbd.inline-flex.h-5: ui-monospace 12px/16px 600, #a2a5aa |
| Transition | all 0.2s ease | = |
| Icon | 16 x 16, colour #63666d | 16 x 16, colour #a2a5aa |
| Painted layers | div.bg-popover.data-[state=open]:animate-in 672.0x594.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px; div.bg-popover.text-popover-foreground 670.0x592.0 bg #ffffff r 8px; div.flex.h-9 670.0x48.0 border B:1px solid; kbd.inline-flex.h-5 33.6x20.0 bg #f2f3f6 r 6px; kbd.inline-flex.h-5 20.0x20.0 bg #f2f3f6 r 6px; kbd.inline-flex.h-5 20.0x20.0 bg #f2f3f6 r 6px | div.bg-popover.data-[state=open]:animate-in 672.0x594.0 bg #1b1e23 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 1px 2px 0px, #000000 @ 0.6 0px 12px 32px -12px; div.bg-popover.text-popover-foreground 670.0x592.0 bg #1b1e23 r 8px; div.flex.h-9 670.0x48.0 border B:1px solid; kbd.inline-flex.h-5 33.6x20.0 bg #191c21 r 6px; kbd.inline-flex.h-5 20.0x20.0 bg #191c21 r 6px; kbd.inline-flex.h-5 20.0x20.0 bg #191c21 r 6px |
| Ancestor paint | 1 up body.antialiased.bg-background bg #ffffff | 1 up body.antialiased.bg-background bg #0d0f14 |
| How | resting state | the dialog was closed, the Theme menu repainted html.dark, and the dialog was reopened |

Crops: `app-search-dialog-default.png`, `app-search-dialog-dark.png`.

### Blog search

#### th-search-input

Search input. The command field in the open dialog; "focused" is the field clicked into — nothing is typed.

Page: /. Selector: `[role="dialog"] input, [cmdk-input], input[type="search"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 510.03 x 56 | = |
| Padding | 12px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #63666d, opacity 1 | = |
| Ancestor paint | 3 up div.bg-popover.data-[state=open]:animate-in bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px | = |
| How | resting state | the field clicked into |

Crops: `th-search-input-default.png`, `th-search-input-focused.png`.

#### th-search-item

Suggestion row. A suggestion row in the open menu.

Page: /. Selector: `[cmdk-item], [role="option"], [role="dialog"] li`. States: .

Not found on the page at capture time.

#### th-search-dialog

Search dialog. The ⌘K command dialog, painted by the page's own shortcut.

Page: /. Selector: `[role="dialog"], [cmdk-root]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 460 |
| Padding | 0px |
| Gap | 16px |
| Border | 1px solid #e2e4e8 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | kbd.font-keys.inline-flex: system-ui 12px/16px 600, #63666d |
| Transition | all 0.2s ease |
| Icon | 16 x 16, colour #63666d |
| Painted layers | div.bg-popover.data-[state=open]:animate-in 672.0x460.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px; div.bg-popover.text-popover-foreground 670.0x458.0 bg #ffffff r 8px; div.flex.h-14 670.0x56.0 border B:1px solid; kbd.font-keys.inline-flex 36.0x24.0 bg #f2f3f6 r 3.35544e+07px |
| Ancestor paint | 1 up body.bg-background bg #ffffff |
| How | resting state |

Crops: `th-search-dialog-default.png`.

### App chrome (mobile)

#### m-app-header

Mobile header. The sticky bar at 390px (md:hidden): menu button, logo, search.

Page: /. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 52 |
| Padding | 0px 12px |
| Border | T: none; R: none; B: 1px solid #e2e4e8; L: none |
| Radius | 0px |
| Background | #ffffff @ 0.8 |
| Box shadow | none |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Transition | none |
| Icon | 16 x 16, colour #13161c |
| Painted layers | header.sticky.top-0 390.0x52.0 bg #ffffff @ 0.8 border B:1px solid |
| Ancestor paint | 1 up main.bg-background.relative bg #ffffff |
| How | resting state |

Crops: `m-app-header-default.png`.

#### m-app-menu-button

"Open menu" button. The hamburger that opens the nav sheet.

Page: /. Selector: `header button[aria-label*="menu" i]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 32 x 32 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 600 | = |
| Letter spacing | normal | = |
| Colour | #13161c | = |
| Transition | all 0.15s cubic-bezier(0.16, 1, 0.3, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #13161c | = |
| How | resting state | mouse hover over the element |

Crops: `m-app-menu-button-default.png`, `m-app-menu-button-hover.png`.

#### m-app-drawer

Nav sheet (open). The opened navigation sheet — an overlay panel over the page. The "Open menu" press happens in find().

Page: /. Selector: `[role="dialog"], aside`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 288 x 844 |
| Padding | 0px |
| Gap | 16px |
| Border | T: none; R: 1px solid #e2e4e8; B: none; L: none |
| Radius | 0px |
| Background | #f7f8fa |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Text node | span: Inter 14px/20px 400, #63666d |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.5s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 118.53 x 16, colour #13161c |
| Painted layers | div.data-[state=open]:animate-in.data-[state=closed]:animate-out 288.0x844.0 bg #f7f8fa border R:1px solid shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.06 0px 1px 2px 0px, #13161c @ 0.22 0px 12px 32px -12px; button.peer/menu-button.flex 263.0x36.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px; kbd.inline-flex.h-5 40.8x20.0 bg #f2f3f6 r 6px; kbd.inline-flex.h-5 20.0x20.0 bg #f2f3f6 r 6px; div.flex.min-h-0 287.0x626.0 image linear-gradient(#f7f8fa 30%, #000000 @ 0), linear-gradient(#000000 @ 0, #f7f8fa 70%), radi; a.peer/menu-button.flex 263.0x32.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #e2e4e8 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #13161c @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 1 up body.antialiased.bg-background bg #ffffff |
| How | the "Open menu" button's own press |

Crops: `m-app-drawer-opened.png`.

### Blog chrome (mobile)

#### m-th-header

Mobile blog header. The sticky blog bar at 390px: wordmark, More, search and theme icons.

Page: /. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0.8 |
| Box shadow | none |
| Backdrop filter | blur(12px) |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #13161c |
| Transition | transform, translate, scale, rotate 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 20 x 20, colour #63666d |
| Painted layers | header.sticky.top-0 390.0x64.0 bg #ffffff @ 0.8; span.h-5.w-px 7.8x19.1 bg #ced1d6; ul.flex.h-9 0.0x0.0 bg #f7f8fa border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; button.hidden.h-9 0.0x0.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px; kbd.font-keys.inline-flex 0.0x0.0 bg #f2f3f6 r 3.35544e+07px; a.items-center.justify-center 0.0x0.0 bg #181b20 r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.min-h-screen bg #ffffff |
| How | resting state |

Crops: `m-th-header-default.png`.

## Transitions declared in the readable stylesheets

hashnode.com and townhall.hashnode.com serve their own CSS same-origin (/_next/static/chunks), so this list is the site's own transition declarations the CSSOM could read on each page.

- /: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /@anish78: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /agents: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /archive: none

- /brand: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /changelog: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /feed: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /onboard: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /posts/i-used-to-be-a-magician/6afadee8cd8f659889f399ed: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /pro: `background 0.15s`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /why-diy-qa-doesnt-work-anymore-a-2025-guide-to-e2e-testing-for-modern-web-apps: none
