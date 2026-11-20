# Component measurements

Computed styles read from joinhandshake.com's public pages (the App access group from app.joinhandshake.com/access) on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is the search field clicked into (nothing typed); `opened` and the rest are resting states reached by a component's own UI toggle. Nothing was typed, sent or signed into.

## Components

### Site chrome

#### hs-nav

Fixed nav bar. The pill-shaped bar fixed under --desktop-nav-top-offset over every marketing page: wordmark, section items, "Sign up" and "Log in".

Page: /. Selector: `nav.fixed`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.rounded-lg.px-4: NoiGrotesk 14px/19.6px 400, #ffffff, ls -0.21px |
| Transition | top, color 0.3s, 0.2s ease-in-out, ease delay 0s, 0s |
| Icon | 0 x 0, colour #d3fb52 |
| Painted layers | div.flex.items-center 1392.0x56.0 bg #ffffff @ 0 r 16px; a.flex.flex-col 73.8x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; a.flex.flex-col 80.5x40.0 bg #d3fb52 r 8px |
| How | resting state |

Crops: `hs-nav-default.png`.

#### hs-nav-link

Nav section item. A top-level nav item ("Employers") — opens the mega menu on hover.

Page: /. Selector: `nav a (text Employers)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 95.13 x 43.59 | = | = |
| Padding | 12px 16px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | #ffffff @ 0.1 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 14px/19.6px 400 | = | = |
| Letter spacing | -0.21px | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.4s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | a.rounded-lg.px-4 95.1x43.6 bg #ffffff @ 0.1 r 8px | a.rounded-lg.px-4 95.1x43.6 r 8px outline 1px auto #101010 offset 1px |

Crops: `hs-nav-link-default.png`, `hs-nav-link-hover.png`, `hs-nav-link-focus-visible.png`.

#### hs-signup-button

"Sign up" button. The solid sign-up control in the nav's right rail.

Page: /. Selector: `nav a,nav button (text Sign up)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.53 x 40 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #d3fb52 | #a1dd3b | #e7ff89 | #a1dd3b |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | NoiGrotesk 14px/15.4px 500 | = | = | = |
| Letter spacing | -0.21px | = | = | = |
| Colour | #14151c | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-col 80.5x40.0 bg #d3fb52 r 8px | a.flex.flex-col 80.5x40.0 bg #a1dd3b r 8px | a.flex.flex-col 80.5x40.0 bg #e7ff89 r 8px outline 1px auto #101010 offset 1px | a.flex.flex-col 80.5x40.0 bg #a1dd3b r 8px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `hs-signup-button-default.png`, `hs-signup-button-hover.png`, `hs-signup-button-focus-visible.png`, `hs-signup-button-pressed.png`.

#### hs-login-link

"Log in" link. The outlined log-in control in the nav's right rail.

Page: /. Selector: `nav a (text Log in)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 73.75 x 40 | = | = |
| Padding | 12px 16px | = | = |
| Gap | normal 4px | = | = |
| Border | 1px solid #ffffff | 1px solid #000000 @ 0 | 1px solid #f3f4fa |
| Radius | 8px | = | = |
| Background | transparent | #ffffff | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 14px/15.4px 500 | = | = |
| Letter spacing | -0.21px | = | = |
| Colour | #ffffff | #14151c | #f3f4fa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.flex.flex-col 73.8x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 73.8x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 73.8x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px outline 1px auto #101010 offset 1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `hs-login-link-default.png`, `hs-login-link-hover.png`, `hs-login-link-focus-visible.png`.

#### hs-nav-menu

Nav mega menu (open). The hover-opened panel under a nav section item. "opened" is the item's own hover: the pointer rests on it until aria-expanded flips.

Page: /. Selector: `div.absolute.top-full.rounded-2xl`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 774 x 249.68 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Outline | none |
| Font | NoiGrotesk 14px/19.6px 400 |
| Letter spacing | -0.21px |
| Colour | #000000 |
| Text node | div.w-fit.rounded-full: NoiGrotesk 10px/11px 500, #d3fb52, ls 0.2px |
| Transition | none |
| Transform | matrix3d(0.9, 0, 0, 0, 0, 0.779423, -0.45, 0, 0, 0.5, 0.866025, 0, 0, 0, 0, 1) |
| Opacity | 0 |
| Icon | 14.4 x 12.47, colour #000000 |
| Painted layers | div.absolute.top-full 774.0x249.7 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; a.relative.flex 248.4x237.2 bg #f3f4fa r 12px; div.relative.h-38 219.6x118.5 image linear-gradient(to right in oklab, #004449 0px, #052326 100%) r 12px; div.absolute.inset-0 219.6x118.5 image radial-gradient(circle at right top, #d3fb52 @ 0.2 0px, #000000 @ 0 34%); div.w-fit.rounded-full 70.9x21.0 bg #d3fb52 @ 0.12 r 9999px |
| How | the nav item's own hover — the panel is measured in the nav region it overlays |

Crops: `hs-nav-menu-opened.png`.

#### hs-footer

Footer. The rounded-top footer (rounded-t-3xl) with link columns.

Page: /. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 766.25 |
| Padding | 24px |
| Border | none |
| Radius | 24px 24px 0px 0px |
| Background | #14151c |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.font-noi-grotesk.text-[36px]/lg: NoiGrotesk 40px/44px 400, #ffffff, ls -1px |
| Transition | none |
| Icon | 140 x 46.09, colour #ffffff, fill #000000 |
| Painted layers | footer.w-full.rounded-t-3xl 1440.0x766.3 bg #14151c r 24px 24px 0px 0px |
| Ancestor paint | 1 up div.relative.z-10 bg #14151c |
| How | resting state |

Crops: `hs-footer-default.png`.

#### hs-footer-link

Footer link. A single link inside the footer columns.

Page: /. Selector: `footer a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 140 x 47.22 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | #d3fb52 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 140 x 46.09, colour #ffffff, fill #000000 | 140 x 46.09, colour #d3fb52, fill #000000 | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a 140.0x47.2 outline 1px auto #101010 offset 1px |

Crops: `hs-footer-link-default.png`, `hs-footer-link-hover.png`, `hs-footer-link-focus-visible.png`.

### Homepage hero

#### hs-hero-h1

Hero headline (h1). "LET'S FIND YOUR NEXT JOB" — the hero title in the brand face. The page ships two hero copies (one per breakpoint); the visible one is picked, never the zero-rect twin.

Page: /. Selector: `main h1, h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 274 |
| Padding | 0px 0px 18px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SansPlomb 160px/128px 600 |
| Letter spacing | -4px |
| Colour | #ffffff |
| Text node | span.block: SansPlomb 160px/128px 600, #ffffff, ls -4px |
| Transition | none |
| How | resting state |

Crops: `hs-hero-h1-default.png`.

#### hs-search-form

Job search form. The hero job-search field row — measured at rest; typing and submitting were never done (the form navigates to the app).

Page: /. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 920 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: NoiGrotesk 20px/22px 400, #14151c @ 0.6, ls -0.3px |
| Transition | none |
| Icon | 32 x 32, colour #252630 |
| Painted layers | input.hidden.size-full 920.0x88.0 bg #ffffff r 24px; textarea.block.size-full 0.0x0.0 bg #ffffff r 24px; button.absolute.right-(--mobile-input-padding) 56.0x56.0 bg #252630 @ 0.1 r 12px |
| How | resting state |

Crops: `hs-search-form-default.png`.

#### hs-search-input

Job search input. The rounded text field inside the hero form.

Page: /. Selector: `form input[type="text"], form input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 920 x 88 | = |
| Padding | 0px 80px 0px 64px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #101010 offset 0px |
| Font | NoiGrotesk 20px/22px 400 | = |
| Letter spacing | -0.3px | = |
| Colour | #252630 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #252630, opacity 1 | = |
| Painted layers | input.hidden.size-full 920.0x88.0 bg #ffffff r 24px | input.hidden.size-full 920.0x88.0 bg #ffffff r 24px outline 1px auto #101010 offset 0px |
| How | resting state | the field clicked into |

Crops: `hs-search-input-default.png`, `hs-search-input-focused.png`.

#### hs-search-button

"Search jobs" button. The submit-styled button inside the hero form — pressed states are CDP-forced, so it never submits.

Page: /. Selector: `form button[aria-label*="search" i] (icon-only "Search jobs" submit)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #252630 @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | NoiGrotesk 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | not-allowed | = | = | = |
| Icon | 13 x 20, colour #7b7b85 | = | = | = |
| Painted layers | button.absolute.right-(--mobile-input-padding) 56.0x56.0 bg #252630 @ 0.1 r 12px | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `hs-search-button-default.png`, `hs-search-button-hover.png`, `hs-search-button-focus-visible.png`, `hs-search-button-pressed.png`.

#### hs-filter-pill

Job-type pill. A selectable type pill under the search field ("Full-time").

Page: /. Selector: `button (text Full-time)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 91.13 x 45.91 | = | = |
| Padding | 16px | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = |
| Radius | 8px | = | = |
| Background | transparent | #ffffff @ 0.1 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.leading-xs.font-noi-grotesk: NoiGrotesk 14px/11.9px 500, #ffffff, ls -0.21px | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.flex.shrink-0 91.1x45.9 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | button.flex.shrink-0 91.1x45.9 bg #ffffff @ 0.1 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | button.flex.shrink-0 91.1x45.9 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px outline 1px auto #101010 offset 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `hs-filter-pill-default.png`, `hs-filter-pill-hover.png`, `hs-filter-pill-focus-visible.png`.

### Employers page

#### hs-banner

Notification banner. The top banner (its height is --notification-banner-height); while it shows, the nav's top offset switches to --desktop-nav-top-offset-with-banner.

Page: /employers/. Selector: `div[class*="notification-banner-height"]:visible`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #d3fb52 |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #252630 |
| Text node | p.font-noi-grotesk.text-[14px]/xl: NoiGrotesk 14px/19.6px 400, #252630, ls -0.21px |
| Transition | none |
| Icon | 16 x 16, colour #252630, fill #000000 |
| Painted layers | div.z-40.h-(--notification-banner-height) 1392.0x40.0 bg #d3fb52 r 8px |
| How | resting state |

Crops: `hs-banner-default.png`.

#### hs-banner-dismiss

Banner dismiss button. The icon-only "Dismiss notification" control — measured, never pressed.

Page: /employers/. Selector: `button[aria-label="Dismiss notification"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #252630 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #252630 | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | button.absolute.right-6 16.0x16.0 outline 1px auto #101010 offset 0px |

Crops: `hs-banner-dismiss-default.png`, `hs-banner-dismiss-hover.png`, `hs-banner-dismiss-focus-visible.png`.

#### hs-segment-tab

Segment switcher tab. One of Source / Automate / Brand / Measure — opacity carries the selection. "selected" is the tab's own press: it swaps the feature panel.

Page: /employers/. Selector: `button (text Source/Automate)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 120 x 44 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | NoiGrotesk 40px/44px 400 | = | = |
| Letter spacing | -1px | = | = |
| Colour | #a9aaae | #252630 | #252630 |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | the tab's own press — a local UI toggle that swaps the published panel |

Crops: `hs-segment-tab-default.png`, `hs-segment-tab-hover.png`, `hs-segment-tab-selected.png`.

#### hs-cta

CTA link-button. A solid call-to-action ("Post a job today" / "Get started" / "Contact sales") — the group.inline-flex pill.

Page: /employers/. Selector: `a.group.inline-flex (text Get started/Contact sales/Post a job)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.38 x 40 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | 1px solid #ffffff | 1px solid #000000 @ 0 | 1px solid #f3f4fa | = |
| Radius | 8px | = | = | = |
| Background | transparent | #ffffff | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | NoiGrotesk 16px/17.6px 500 | = | = | = |
| Letter spacing | -0.24px | = | = | = |
| Colour | #ffffff | #14151c | #f3f4fa | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.inline-flex 120.4x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.group.inline-flex 120.4x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.group.inline-flex 120.4x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px outline 1px auto #101010 offset 1px | = |
| Ancestor paint | 1 up div.flex.flex-1 bg #ffffff @ 0.1 | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `hs-cta-default.png`, `hs-cta-hover.png`, `hs-cta-focus-visible.png`, `hs-cta-pressed.png`.

#### hs-carousel-dot

Testimonial dot. A carousel page dot ("Go to testimonial N").

Page: /employers/. Selector: `button[aria-label*="testimonial" i]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 8 x 8 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 9999px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.size-2.rounded-full 8.0x8.0 bg #ffffff r 9999px | = |
| How | resting state | mouse hover over the element |

Crops: `hs-carousel-dot-default.png`, `hs-carousel-dot-hover.png`.

#### hs-faq

FAQ accordion question. A question row in the FAQ. "opened" is the question button's own press: it unfolds the answer.

Page: /employers/. Selector: `button (question)`. States: default, hover, focus-visible, opened.

| Property | default | hover | focus-visible | opened |
|---|---|---|---|---|
| Size (w x h) | 597.33 x 25.2 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | NoiGrotesk 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | p.font-noi-grotesk.text-[18px]/xl: NoiGrotesk 18px/25.2px 400, #ffffff, ls -0.27px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 20, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | div.flex.size-6 24.0x24.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 9999px | = | button 597.3x25.2 outline 1px auto #101010 offset 0px; div.flex.size-6 24.0x24.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 9999px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | the question button's own press — a local UI toggle |

Crops: `hs-faq-default.png`, `hs-faq-hover.png`, `hs-faq-focus-visible.png`, `hs-faq-opened.png`.

### Pricing page

#### pricing-table

Plan comparison table. One of the plan/feature tables on /employers/pricing/ (the page mounts four).

Page: /employers/pricing/. Selector: `table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 856.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | th: NoiGrotesk 16px/24px 700, #000000 |
| Transition | none |
| Icon | 24 x 24, colour #00b1b5 |
| Painted layers | table.w-full.bg-white 1152.0x856.5 bg #ffffff; td.col-span-1.flex 164.6x92.8 bg #252630 @ 0.04; tr.grid.grid-cols-7 1152.0x93.8 border T:1px solid; td.col-span-1.flex 164.6x92.8 bg #252630 @ 0.04; tr.grid.grid-cols-7 1152.0x73.0 border T:1px solid; td.col-span-1.flex 164.6x72.0 bg #252630 @ 0.04 |
| How | resting state |

Crops: `pricing-table-default.png`.

#### pricing-th

Table header cell. A th in the comparison table.

Page: /employers/pricing/. Selector: `th`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 83 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | resting state |

Crops: `pricing-th-default.png`.

#### pricing-td

Table cell. A td in the comparison table.

Page: /employers/pricing/. Selector: `td`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 493.7 x 92.81 |
| Padding | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.font-noi-grotesk.text-[16px]/xl: NoiGrotesk 16px/22.4px 400, #252630 @ 0.8, ls -0.24px |
| Transition | none |
| How | resting state |

Crops: `pricing-td-default.png`.

#### pricing-plan-card

Plan card. A plan column/card on the pricing page.

Page: /employers/pricing/. Selector: `[class*="plan" i], [class*="tier" i], main section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 256 x 125.61 |
| Padding | 0px |
| Gap | 64px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.font-noi-grotesk.text-[32px]/lg: NoiGrotesk 32px/35.2px 400, #000000, ls -0.8px |
| Transition | none |
| Ancestor paint | 1 up div.flex.h-fit bg #f3f4fa |
| How | resting state |

Crops: `pricing-plan-card-default.png`.

#### pricing-feature-tab

Feature group tab. A "Target & Connect" / "Centralize" / "Brand" / "Measure" group button that switches the comparison section.

Page: /employers/pricing/. Selector: `button (text Target & Connect/Centralize)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 1152 x 74.59 | = | = |
| Padding | 24px | = | = |
| Border | T: none; R: none; B: 1px solid #878aae; L: none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | h3.text-left.text-b40: NoiGrotesk 16px/25.6px 600, #000000 | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #bebdbf | = | = |
| Painted layers | button.flex.w-full 1152.0x74.6 border B:1px solid | = | = |
| How | resting state | mouse hover over the element | the tab's own press — a local UI toggle |

Crops: `pricing-feature-tab-default.png`, `pricing-feature-tab-hover.png`, `pricing-feature-tab-selected.png`.

### Marketo forms

#### mkto-form

Demo form shell. The "Request a demo" Marketo form — its fields mount from go.joinhandshake.com vendor script.

Page: /employers/request-more-info/. Selector: `form[class*="marketo" i], form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 502.67 x 466 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | button.inline-flex.min-h-12: NoiGrotesk 18px/18px 400, #14151c, ls -0.18px |
| Transition | none |
| Painted layers | input.mktoField.mktoEmailField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoTextField 243.3x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoTextField 243.3x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoTextField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoTelField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px; input.mktoField.mktoNumberField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px |
| How | resting state |

Crops: `mkto-form-default.png`.

#### mkto-input

Form text field. A text input inside the Marketo form.

Page: /employers/request-more-info/. Selector: `form input[type="text"], form input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 502.67 x 58 | = |
| Padding | 16px | = |
| Border | 1px solid #484851 | 1px solid #ff455b |
| Radius | 4px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #9b53f6 offset 0px |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #252630 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #bebdbf, opacity 1 | = |
| Painted layers | input.mktoField.mktoEmailField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px | input.mktoField.mktoEmailField 502.7x58.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 4px outline 1px auto #9b53f6 offset 0px |
| How | resting state | the field clicked into |

Crops: `mkto-input-default.png`, `mkto-input-focused.png`.

#### mkto-select

Form select. A select inside the Marketo form.

Page: /employers/request-more-info/. Selector: `form select`. States: .

Not found on the page at capture time.

#### mkto-submit

Form submit button. The form's submit control — measured, never pressed (pressed states are CDP-forced).

Page: /employers/request-more-info/. Selector: `form button[type="submit"], form button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 502.67 x 48 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #d3fb52 | #ffffff | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | NoiGrotesk 18px/18px 400 | = | = | = |
| Letter spacing | -0.18px | = | = | = |
| Colour | #14151c | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.min-h-12 502.7x48.0 bg #d3fb52 r 4px | button.inline-flex.min-h-12 502.7x48.0 bg #ffffff r 4px | button.inline-flex.min-h-12 502.7x48.0 bg #d3fb52 r 4px outline 1px auto #101010 offset 0px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `mkto-submit-default.png`, `mkto-submit-hover.png`, `mkto-submit-focus-visible.png`, `mkto-submit-pressed.png`.

#### cc-form

Career-center contact form. The EDU contact form on /career-centers/contact/ — same Marketo stack.

Page: /career-centers/contact/. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 728 x 921.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | label.mktoLabel.mktoHasWidth: NoiGrotesk 16px/25.6px 400, #000000 |
| Transition | none |
| Painted layers | input.mktoField.mktoTextField 728.0x40.0 bg #f3f4fa r 3px; input.mktoField.mktoTextField 728.0x40.0 bg #f3f4fa r 3px; input.mktoField.mktoEmailField 728.0x40.0 bg #f3f4fa r 3px; input.mktoField.mktoTelField 728.0x40.0 bg #f3f4fa r 3px; input.mktoField.mktoTextField 728.0x40.0 bg #f3f4fa r 3px; select.mktoField.mktoHasWidth 728.0x35.0 bg #f3f4fa r 3px |
| How | resting state |

Crops: `cc-form-default.png`.

### Students page

#### stu-email-input

Email capture field. The "Type school or personal email here" field in the hero — measured at rest, nothing typed.

Page: /students/. Selector: `input[type="email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 448 x 56 | = |
| Padding | 8px 16px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #101010 offset 0px |
| Font | NoiGrotesk 18px/25.2px 400 | = |
| Letter spacing | -0.27px | = |
| Colour | #14151c | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #14151c @ 0.6, opacity 1 | = |
| Painted layers | input.mx-auto.h-14 448.0x56.0 bg #ffffff r 8px | input.mx-auto.h-14 448.0x56.0 bg #ffffff r 8px outline 1px auto #101010 offset 0px |
| How | resting state | the field clicked into |

Crops: `stu-email-input-default.png`, `stu-email-input-focused.png`.

#### stu-signup-button

"Sign up" CTA. The students sign-up button (group.inline-flex).

Page: /students/. Selector: `button.group.inline-flex (text Sign up)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82.53 x 40 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | normal 4px | = | = | = |
| Border | 1px solid #252630 | 1px solid #000000 @ 0 | 1px solid #14151c | 1px solid #000000 @ 0 |
| Radius | 8px | = | = | = |
| Background | transparent | #14151c @ 0.1 | #ffffff | #ffffff |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | NoiGrotesk 14px/15.4px 500 | = | = | = |
| Letter spacing | -0.21px | = | = | = |
| Colour | #252630 | = | = | #14151c |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.flex.flex-col 82.5x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 82.5x40.0 bg #14151c @ 0.1 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | a.flex.flex-col 82.5x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px outline 1px auto #101010 offset 1px | a.flex.flex-col 82.5x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `stu-signup-button-default.png`, `stu-signup-button-hover.png`, `stu-signup-button-focus-visible.png`, `stu-signup-button-pressed.png`.

#### stu-text-link

Arrow text link. "Find jobs and internships →" — an arrow-suffixed text link in the brand face.

Page: /students/. Selector: `a (text Find jobs and internships)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 243.53 x 46.41 | = | = |
| Padding | 12px 20px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 32px | = | = |
| Background | #052326 @ 0.8 | #004449 @ 0.8 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 16px/22.4px 500 | = | = |
| Letter spacing | -0.24px | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.font-noi-grotesk.text-[16px]/xl 243.5x46.4 bg #052326 @ 0.8 r 32px | a.font-noi-grotesk.text-[16px]/xl 243.5x46.4 bg #004449 @ 0.8 r 32px | a.font-noi-grotesk.text-[16px]/xl 243.5x46.4 bg #052326 @ 0.8 r 32px outline 1px auto #101010 offset 1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `stu-text-link-default.png`, `stu-text-link-hover.png`, `stu-text-link-focus-visible.png`.

#### stu-carousel-btn

Card carousel arrow. A "Slide to the next/previous card" arrow button.

Page: /students/. Selector: `button[aria-label*="card" i]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 48 x 48 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | #14151c |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 14, colour #ffffff | 20 x 14, colour #14151c, fill #ffffff |
| Painted layers | div.flex.size-12 48.0x48.0 bg #ffffff r 9999px | div.flex.size-12 48.0x48.0 bg #14151c r 9999px |
| How | resting state | mouse hover over the element |

Crops: `stu-carousel-btn-default.png`, `stu-carousel-btn-hover.png`.

### Blog

#### blog-search-input

Blog search field. The search input on the blog index — measured at rest, nothing typed.

Page: /blog/. Selector: `input[type="search"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 343 x 27 | = |
| Padding | 0px 0px 0px 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f3f4fa | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 22px/22px 400 | = |
| Letter spacing | -0.44px | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input.w-full.bg-neutral-10 343.0x27.0 bg #f3f4fa | = |
| How | resting state | the field clicked into |
| Ancestor paint | - | 2 up div.flex.min-h-12 bg #f3f4fa outline 1px solid #000000 |

Crops: `blog-search-input-default.png`, `blog-search-input-focused.png`.

#### blog-search-button

Search button. The Search button beside the field — CDP-forced states only.

Page: /blog/. Selector: `button (text Search)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.92 x 48 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #052326 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | NoiGrotesk 18px/18px 400 | = | = | = |
| Letter spacing | -0.18px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.min-h-12 88.9x48.0 bg #052326 r 4px | = | button.inline-flex.min-h-12 88.9x48.0 bg #052326 r 4px outline 1px auto #101010 offset 0px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `blog-search-button-default.png`, `blog-search-button-hover.png`, `blog-search-button-focus-visible.png`, `blog-search-button-pressed.png`.

#### blog-category-link

Category link. An uppercase category link ("AI SKILLS STUDIO").

Page: /blog/. Selector: `a.uppercase`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 137 x 17 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 16px/24px 600 | = | = |
| Letter spacing | normal | = | = |
| Colour | #2e6aff | #1552d6 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.uppercase.font-semibold 137.0x17.0 outline 1px auto #101010 offset 1px |

Crops: `blog-category-link-default.png`, `blog-category-link-hover.png`, `blog-category-link-focus-visible.png`.

#### blog-card

Article card. An article card link on the blog index.

Page: /blog/. Selector: `main a[href*="/blog/"] (the card-sized anchor, not a category link)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 536 x 159.22 | = |
| Padding | 0px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h3.font-noi-grotesk.text-[36px]/lg: NoiGrotesk 40px/44px 600, #000000, ls -1px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Ancestor paint | 1 up div.flex.flex-col bg #ffffff | = |
| How | resting state | mouse hover over the element |

Crops: `blog-card-default.png`, `blog-card-hover.png`.

#### blog-readmore

"Read More" link. The Read More affordance on an article card.

Page: /blog/. Selector: `a (text Read More)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 536 x 25.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.font-noi-grotesk.text-[18px]/xl: NoiGrotesk 22px/24.2px 700, #000000, ls -0.33px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 14.11 x 24, colour #000000 | = |
| Ancestor paint | 1 up div.flex.flex-col bg #ffffff | = |
| How | resting state | mouse hover over the element |

Crops: `blog-readmore-default.png`, `blog-readmore-hover.png`.

### Careers page

#### car-benefit-tab

Benefits tab. A benefits category button ("Health & wellness") — the tab's own press swaps the panel.

Page: /careers/. Selector: `button (text Health & wellness)`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 568 x 35.2 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | h2.font-noi-grotesk.text-[32px]/lg: NoiGrotesk 32px/35.2px 400, #000000, ls -0.8px | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 20, colour #000000 | = | = |
| Painted layers | div.flex.size-6 24.0x24.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 9999px | = | = |
| How | resting state | mouse hover over the element | the tab's own press — a local UI toggle |

Crops: `car-benefit-tab-default.png`, `car-benefit-tab-hover.png`, `car-benefit-tab-selected.png`.

#### car-search-input

Roles search field. The open-roles search input — measured at rest, nothing typed.

Page: /careers/. Selector: `input[placeholder*="earch" i], input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 688 x 56 | = |
| Padding | 16px 12px | = |
| Border | 1px solid #252630 @ 0.1 | 1px solid #252630 |
| Radius | 12px | = |
| Background | #ffffff | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #252630 0px 0px 0px 1px |
| Outline | none | = |
| Font | NoiGrotesk 16px/22.4px 400 | = |
| Letter spacing | -0.24px | = |
| Colour | #14151c | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #bebdbf, opacity 1 | #bebdbf, opacity 0 |
| Painted layers | input.border.transition-all 688.0x56.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | input.border.transition-all 688.0x56.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #252630 0px 0px 0px 1px |
| How | resting state | the field clicked into |

Crops: `car-search-input-default.png`, `car-search-input-focused.png`.

#### car-dept-button

Department filter button. The "All departments" filter dropdown in the roles list — "opened" is its own press.

Page: /careers/. Selector: `button.group.flex`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 218.67 x 56 | = | = |
| Padding | 16px 12px | = | = |
| Border | 1px solid #252630 @ 0.1 | 1px solid #bebdbf | 1px solid #252630 |
| Radius | 12px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #252630 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | NoiGrotesk 14px/19.6px 400 | = | = |
| Letter spacing | -0.21px | = | = |
| Colour | #14151c | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #14151c, fill #000000 | = | = |
| Painted layers | button.group.flex 218.7x56.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | = | button.group.flex 218.7x56.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #252630 0px 0px 0px 1px |
| How | resting state | mouse hover over the element | the header's own press — a local UI toggle |

Crops: `car-dept-button-default.png`, `car-dept-button-hover.png`, `car-dept-button-opened.png`.

#### car-job-link

Job row link. An open-role link in the list.

Page: /careers/. Selector: `a (job title)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1392 x 122 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.font-noi-grotesk.text-[24px]/lg: NoiGrotesk 24px/26.4px 400, #000000, ls -0.36px | p.font-noi-grotesk.text-[24px]/lg: NoiGrotesk 24px/26.4px 400, #ffffff, ls -0.36px |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.group.flex 1392.0x122.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px; div.group.inline-flex 73.8x40.0 bg #252630 r 8px | div.group.flex 1392.0x122.0 bg #252630 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px; div.group.inline-flex 73.8x40.0 bg #d3fb52 r 8px |
| How | resting state | mouse hover over the element |

Crops: `car-job-link-default.png`, `car-job-link-hover.png`.

#### car-page-button

Pagination button. A page number in the roles pagination.

Page: /careers/. Selector: `button.group.inline-flex (text 1/2/3)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #14151c | = | = |
| Radius | 12px | = | = |
| Background | #14151c | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.group.inline-flex 48.0x48.0 bg #14151c border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | = | button.group.inline-flex 48.0x48.0 bg #14151c border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px outline 1px auto #101010 offset 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `car-page-button-default.png`, `car-page-button-hover.png`, `car-page-button-focus-visible.png`.

### Legal pages

#### legal-nav-active

Legal nav link (active). The current section link in the legal left rail (opacity-100).

Page: /legal/tos/. Selector: `main a.font-medium`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 305.5 x 22.41 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 500 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.font-noi-grotesk.text-[16px]/xl: NoiGrotesk 16px/22.4px 500, #000000, ls -0.24px | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `legal-nav-active-default.png`, `legal-nav-active-hover.png`.

#### legal-nav-link

Legal nav link. An inactive section link in the legal left rail (opacity-60).

Page: /legal/tos/. Selector: `a.opacity-60`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 305.5 x 22.41 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | NoiGrotesk 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Text node | p.font-noi-grotesk.text-[16px]/xl: NoiGrotesk 16px/22.4px 400, #000000, ls -0.24px | = | = |
| Transition | none | = | = |
| Opacity | 0.6 | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.opacity-60 305.5x22.4 outline 1px auto #101010 offset 1px |

Crops: `legal-nav-link-default.png`, `legal-nav-link-hover.png`, `legal-nav-link-focus-visible.png`.

### App access

#### app-shell

Login page shell. The /access page body — the consumer app's signed-out entry.

Page: https://app.joinhandshake.com/access. Selector: `main, #maincontent, body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 72px 0px 76px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Noi Grotesk 15px/18px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | output.rosetta-select__option-ellipsis.rosetta-select__output: Noi Grotesk 15px/18px 400, #121212 |
| Transition | none |
| Icon | 20 x 20, colour #121212 @ 0.7, fill #000000 |
| Painted layers | div.rosetta-field__base.sc-ezOQGI 137.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; div.sc-bYMpWt.jDuFBQ 0.0x0.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0.08 0px 6px 30px 0px, #000000 @ 0.08 0px 1px 3px 0px; div.rosetta-select__option.rosetta-body-medium 0.0x0.0 bg #e7e7e7 r 8px; select.rosetta-select__hidden 1.0x1.0 bg #efefef; svg.rosetta-logo-app-icon.rosetta-entity-avatar 48.0x48.0 bg #ffffff r 8px outline 1px solid #121212 @ 0.12 offset -1px; hr.sc-fNAUDI.fQrJOK 157.0x2.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid |
| How | resting state |

Crops: `app-shell-default.png`.

#### app-locale-select

Locale select. The "English (US)" rosetta-select in the page chrome.

Page: https://app.joinhandshake.com/access. Selector: `select.rosetta-select__hidden, select`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 137 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Noi Grotesk 15px/18px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | output.rosetta-select__option-ellipsis.rosetta-select__output: Noi Grotesk 15px/18px 400, #121212 |
| Transition | none |
| Icon | 20 x 20, colour #121212 @ 0.7, fill #000000 |
| Painted layers | div.rosetta-field__base.sc-ezOQGI 137.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; div.sc-bYMpWt.jDuFBQ 0.0x0.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #000000 @ 0.08 0px 6px 30px 0px, #000000 @ 0.08 0px 1px 3px 0px; div.rosetta-select__option.rosetta-body-medium 0.0x0.0 bg #e7e7e7 r 8px; select.rosetta-select__hidden 1.0x1.0 bg #efefef |
| How | resting state |

Crops: `app-locale-select-default.png`.

#### app-email-field

Email field. The "Enter your email" rosetta-field — measured at rest, nothing typed.

Page: https://app.joinhandshake.com/access. Selector: `input[name="email"], input[type="text"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 344 x 48 | = |
| Padding | 0px 16px | = |
| Border | 1px solid #121212 @ 0.12 | 1px solid #04191b |
| Radius | 8px | = |
| Background | #ffffff | = |
| Box shadow | none | #04191b 0px 0px 0px 1px inset |
| Outline | none | 1px solid #000000 @ 0 offset 0px |
| Font | Noi Grotesk 17px/23.8px 400 | = |
| Letter spacing | -0.34px | = |
| Colour | #121212 | = |
| Transition | transform 0.3s ease-in | = |
| Cursor | text | = |
| Placeholder | #121212 @ 0.7, opacity 1 | = |
| Painted layers | input.rosetta-field__base.sc-ezOQGI 344.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px | input.rosetta-field__base.sc-ezOQGI 344.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px shadow #04191b 0px 0px 0px 1px inset outline 1px solid #000000 @ 0 offset 0px |
| How | resting state | the field clicked into |

Crops: `app-email-field-default.png`, `app-email-field-focused.png`.

#### app-continue-button

"Continue with email" button. The rosetta-button submit — pressed states are CDP-forced, so the form never submits.

Page: https://app.joinhandshake.com/access. Selector: `button.rosetta-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #04191b | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #003bcc offset 2px | = |
| Font | Noi Grotesk 15px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.rosetta-button.sc-ftTHYK 344.0x40.0 bg #04191b r 8px | button.rosetta-button.sc-ftTHYK 344.0x40.0 bg #04191b image linear-gradient(#ffffff @ 0.06, #ffffff @ 0.06) r 8px | button.rosetta-button.sc-ftTHYK 344.0x40.0 bg #04191b r 8px outline 2px solid #003bcc offset 2px | button.rosetta-button.sc-ftTHYK 344.0x40.0 bg #04191b image linear-gradient(#ffffff @ 0.12, #ffffff @ 0.12) r 8px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |
| Background image | - | linear-gradient(#ffffff @ 0.06, #ffffff @ 0.06) | = | linear-gradient(#ffffff @ 0.12, #ffffff @ 0.12) |

Crops: `app-continue-button-default.png`, `app-continue-button-hover.png`, `app-continue-button-focus-visible.png`, `app-continue-button-pressed.png`.

#### app-google-button

Google SSO button. The "Continue with Google" button — Google's own rendered widget (GSI), recorded as vendor.

Page: https://app.joinhandshake.com/access. Selector: `[class*="LgbsSe"], [id*="gsi" i], iframe[title*="Google" i], iframe[src*="accounts.google.com"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 364 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Noi Grotesk 15px/18px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | resting state |

Crops: `app-google-button-default.png`.

#### app-employer-link

"Sign up as an employer" link. The employer sign-up link under the login card.

Page: https://app.joinhandshake.com/access. Selector: `a (text employer)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 61 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Noi Grotesk 15px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #1569e0 | #0e489a |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `app-employer-link-default.png`, `app-employer-link-hover.png`.

#### app-tos-link

Terms link. The Terms of Service link in the fine print.

Page: https://app.joinhandshake.com/access. Selector: `a (text Terms of Service)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 106.09 x 14 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Noi Grotesk 13px/15.6px 400 | = |
| Letter spacing | 0.13px | = |
| Colour | #1569e0 | #0e489a |
| Transition | none | = |
| Cursor | pointer | = |
| Ancestor paint | 1 up div bg #ffffff @ 0.6 | = |
| How | resting state | mouse hover over the element |

Crops: `app-tos-link-default.png`, `app-tos-link-hover.png`.

### Site chrome (mobile)

#### m-hs-topbar

Mobile header pill. The floating pill at 390px: the mobile nav wrapper is a 0-height relative container; the painted bar is its fixed child (wordmark, links, the "Open menu" button).

Page: /. Selector: `nav[class*="xl:hidden"] > div:first-child (fixed pill)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 48 |
| Padding | 8px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.group.items-center: NoiGrotesk 16px/14.4px 500, #252630, ls -0.24px |
| Transition | none |
| Icon | 32 x 32, colour #000000 |
| Painted layers | div.fixed.top-(--mobile-top-offset) 358.0x48.0 bg #ffffff r 12px; a.group.items-center 88.3x40.0 bg #000000 @ 0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; a.group.items-center 76.6x40.0 bg #252630 r 8px; a.group.items-center 0.0x0.0 bg #252630 r 8px |
| How | resting state |

Crops: `m-hs-topbar-default.png`.

#### m-hs-hamburger

"Open menu" button. The icon-only button (aria-label "Open menu", no text content) that opens the mobile nav sheet.

Page: /. Selector: `button[aria-label="Open menu"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | NoiGrotesk 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #000000 | = |
| How | resting state | mouse hover over the element |

Crops: `m-hs-hamburger-default.png`, `m-hs-hamburger-hover.png`.

#### m-hs-drawer

Nav sheet (open). The opened mobile navigation sheet. The "Open menu" press happens in find(): the sheet is only reachable once open, so the state itself is a no-op.

Page: /. Selector: `div[class*="mobile-nav-height"][class*="100dvh"] (the fixed sheet under the bar; Ketch's dialog is excluded)`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 390 x 772 |
| Padding | 8px 16px 24px 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | NoiGrotesk 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.flex.w-full: NoiGrotesk 28px/30.8px 400, #000000, ls -0.7px |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.fixed.top-[calc(var(--mobile-top-offset)+var(--mobile-nav-height))] 390.0x772.0 bg #ffffff; div.fixed.inset-0 390.0x772.0 bg #ffffff; div.h-px.w-screen 390.0x1.0 bg #252630 @ 0.1; div.h-px.bg-neutral-90/10 358.0x1.0 bg #252630 @ 0.1; div.h-px.bg-neutral-90/10 358.0x1.0 bg #252630 @ 0.1; div.h-px.bg-neutral-90/10 358.0x1.0 bg #252630 @ 0.1 |
| How | the "Open menu" button's own press |

Crops: `m-hs-drawer-opened.png`.

## Transitions declared in the readable stylesheets

joinhandshake.com serves its own CSS same-origin (/_next/static/css) and app.joinhandshake.com from handshake-production-cdn.joinhandshake.com, so this list is the sites' own transition declarations the CSSOM could read on each page.

- /: `opacity 0.25s linear`

- /blog/: `transform 0.1s ease-in-out`, `transform 0.1s ease-out`, `opacity 0.25s linear`

- /career-centers/contact/: `transform 0.1s ease-in-out`, `transform 0.1s ease-out`, `opacity 0.25s linear`

- /careers/: `opacity 0.25s linear`

- /employers/: `opacity 0.25s linear`

- /employers/pricing/: `opacity 0.25s linear`

- /employers/request-more-info/: `transform 0.1s ease-in-out`, `transform 0.1s ease-out`, `opacity 0.25s linear`

- /legal/tos/: `transform 0.1s ease-in-out`, `transform 0.1s ease-out`, `opacity 0.25s linear`

- /students/: `opacity 0.25s linear`

- https://app.joinhandshake.com/access: `transform 300ms ease-in`, `opacity 150ms ease-in`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`
