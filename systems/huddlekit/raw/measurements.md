# Component measurements

Computed styles read from huddlekit.com and app.huddlekit.com on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a field clicked into (nothing typed); `dark` is the same element after an emulated prefers-color-scheme repaint — the signal app.huddlekit.com honours (its login has no theme control of its own; the marketing site paints light only, its dark evidence the nested `.dark` panels measured as their own components); `opened`, `selected` and `off` are resting states reached by a component's own UI toggle. Nothing was typed, sent or signed into.

## Components

### Consent

#### consent-banner

Cookie consent banner. The fixed bottom consent banner ("We'd like to use cookies…"): bg-background rounded-2xl border shadow-lg with Decline / Accept.

Page: /. Selector: `section.fixed`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352 x 174 |
| Padding | 8px |
| Border | 1px solid #e4e4e7 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111827 |
| Text node | p.text-muted-foreground.px-2: Inter 14px/20px 400, #747170 |
| Transition | none |
| Painted layers | section.bg-background.fixed 352.0x174.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; button.inline-flex.items-center 163.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; button.inline-flex.items-center 163.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 1 up body.font-sans.antialiased bg #f6f3f2 |
| How | resting state |

Crops: `consent-banner-default.png`.

#### consent-decline

Consent "Decline" button. The decline control in the consent banner (secondary style).

Page: /. Selector: `button (text Decline)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 163 x 36 | = | = |
| Padding | 8px 12px | = | = |
| Gap | 6px | = | = |
| Border | 1px solid #e4e4e7 | = | 1px solid #111827 @ 0.2 |
| Radius | 12px | = | = |
| Background | #ffffff | #f6f3f2 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | #18181b | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.inline-flex.items-center 163.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.inline-flex.items-center 163.0x36.0 bg #f6f3f2 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.inline-flex.items-center 163.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 2 up section.bg-background.fixed bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `consent-decline-default.png`, `consent-decline-hover.png`, `consent-decline-focus-visible.png`.

#### consent-accept

Consent "Accept" button. The accept control in the consent banner (bg-primary).

Page: /. Selector: `button (text Accept)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e4e4e7 | = | 1px solid #111827 @ 0.2 | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | #f6f3f2 | = | #f6f3f2 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111827 | #18181b | = | #18181b |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 163.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.inline-flex.items-center 163.0x36.0 bg #f6f3f2 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.inline-flex.items-center 163.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px | button.inline-flex.items-center 163.0x36.0 bg #f6f3f2 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 2 up section.bg-background.fixed bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `consent-accept-default.png`, `consent-accept-hover.png`, `consent-accept-focus-visible.png`, `consent-accept-pressed.png`.

### Chrome

#### announce-bar

Announcement bar. The top "New: hand feedback to your AI agent over MCP" announcement link — border-b over the header.

Page: /. Selector: `a (announcement)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1440 x 40 | = |
| Padding | 8px 16px | = |
| Gap | 4px | = |
| Border | T: none; R: none; B: 1px solid #e4e4e7; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #111827 | = |
| Painted layers | a.group.text-foreground 1440.0x40.0 border B:1px solid | = |
| How | resting state | mouse hover over the element |

Crops: `announce-bar-default.png`, `announce-bar-hover.png`.

#### nav-header

Site header. The header holding the logo, the Features / Solutions / Resources / Pricing / Sign in nav and the "Get started" button.

Page: /. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 976 x 64 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111827 |
| Text node | a.hover:text-foreground/70.text-foreground: Inter 14px/20px 500, #111827 |
| Transition | none |
| Icon | 104 x 28, colour #111827 |
| Painted layers | a.inline-flex.items-center 104.0x32.0 bg #ede9e7 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px; button.inline-flex.items-center 0.0x0.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | resting state |

Crops: `nav-header-default.png`.

#### nav-link

Nav link. A plain nav link ("Features"), text-foreground with hover:text-foreground/70.

Page: /. Selector: `nav a, header a`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 62 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #ff6900 @ 0.5 offset 1px |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | #111827 @ 0.7 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |
| Painted layers | - | = | a.hover:text-foreground/70.text-foreground 62.0x20.0 outline 1px auto #ff6900 @ 0.5 offset 1px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`.

#### nav-menu-button

Nav menu trigger. The "Solutions" button that opens a nav-surface popover on hover. "opened" is after the real hover that opened it.

Page: /. Selector: `button (text Solutions)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 85 x 20 | = | = |
| Padding | 0px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | #111827 @ 0.7 | #111827 @ 0.7 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | default | = | = |
| Icon | 14 x 14, colour #111827 | 14 x 14, colour #111827 @ 0.7 | 14 x 14, colour #111827 @ 0.7 |
| How | resting state | mouse hover over the element | the trigger's own hover (the nav-surface popover open; the pointer is then moved away) |

Crops: `nav-menu-button-default.png`, `nav-menu-button-hover.png`, `nav-menu-button-opened.png`.

#### nav-menu-surface

Nav popover (open). The open nav-surface popover under the header — the Solutions menu the hover shows.

Page: /. Selector: `.nav-surface`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 194 x 154 |
| Padding | 0px |
| Border | 1px solid #e4e4e7 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #09090b |
| Text node | a.text-foreground.hover:bg-foreground/5: Inter 14px/20px 500, #111827 |
| Transition | translate, width, height 0.2s cubic-bezier(0.22, 1, 0.36, 1) |
| Icon | 16 x 16, colour #747170 |
| Painted layers | div.nav-surface.bg-popover 194.0x154.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px |
| How | the Solutions trigger's own hover; the popover itself is read while open |

Crops: `nav-menu-surface-opened.png`.

#### nav-signin

"Sign in" link. The header sign-in link — measured, never followed (it leads to app.huddlekit.com, which was captured separately).

Page: /. Selector: `a (text Sign in)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 48 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #111827 | #111827 @ 0.7 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`.

#### cta-primary

Primary CTA button. The solid "Get started for free" call-to-action (bg-primary text-primary-foreground, the inner-shadow stack) — links to the app, measured never followed.

Page: /. Selector: `a (text Get started for free)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 169 x 40 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ea580d | #ea580d @ 0.9 | = | #ea580d @ 0.9 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fff7ed | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 169.0x40.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | a.inline-flex.items-center 169.0x40.0 bg #ea580d @ 0.9 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | a.inline-flex.items-center 169.0x40.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | a.inline-flex.items-center 169.0x40.0 bg #ea580d @ 0.9 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `cta-primary-default.png`, `cta-primary-hover.png`, `cta-primary-focus-visible.png`, `cta-primary-pressed.png`.

#### cta-secondary

Secondary button. The header's "Get started" button (bg-secondary with the same inner-shadow stack).

Page: /. Selector: `a (text Get started)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104 x 32 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #111827 @ 0.2 | = |
| Radius | 12px | = | = | = |
| Background | #ede9e7 | #ede9e7 @ 0.8 | = | #ede9e7 @ 0.8 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #18181b | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 104.0x32.0 bg #ede9e7 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | a.inline-flex.items-center 104.0x32.0 bg #ede9e7 @ 0.8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | a.inline-flex.items-center 104.0x32.0 bg #ede9e7 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | a.inline-flex.items-center 104.0x32.0 bg #ede9e7 @ 0.8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`, `cta-secondary-pressed.png`.

#### cta-outline

Outline button. A bordered ghost action in the hero ("5-star reviews"): border + transparent fill, hover:bg-accent.

Page: /. Selector: `a (text 5-star reviews)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 152 x 40 | = | = |
| Padding | 0px 14px | = | = |
| Gap | 6px | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #111827 @ 0.2 |
| Radius | 12px | = | = |
| Background | transparent | #111827 @ 0.05 | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | #18181b | = |
| Text node | span.from-primary.to-foreground: Inter 14px/20px 500, #000000 @ 0 | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 14, colour #ea580d | = | = |
| Painted layers | a.inline-flex.items-center 152.0x40.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px; span.from-primary.to-foreground 102.0x20.0 image linear-gradient(to right, #ea580d 0px, #111827 100%) | a.inline-flex.items-center 152.0x40.0 bg #111827 @ 0.05 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px; span.from-primary.to-foreground 102.0x20.0 image linear-gradient(to right, #ea580d 0px, #111827 100%) | a.inline-flex.items-center 152.0x40.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.from-primary.to-foreground 102.0x20.0 image linear-gradient(to right, #ea580d 0px, #111827 100%) |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `cta-outline-default.png`, `cta-outline-hover.png`, `cta-outline-focus-visible.png`.

#### footer

Site footer (dark). The .dark footer (bg-background text-foreground inside .dark): Product / Solutions / Resources columns, "Cookie settings" button and the social links.

Page: /. Selector: `footer.dark, footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 860.02 |
| Padding | 0px |
| Border | T: 1px solid #ffffff @ 0.08; R: none; B: none; L: none |
| Radius | 0px |
| Background | #0e0b0d |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #e3e0df |
| Text node | h3.mb-3.text-sm: Inter 14px/20px 600, #e3e0df |
| Transition | none |
| Icon | 16 x 16, colour #e3e0df |
| Painted layers | footer.dark.bg-background 1440.0x860.0 bg #0e0b0d border T:1px solid; div.mx-auto.max-w-5xl 1024.0x516.0 border R:1px solid / L:1px solid; div.mx-auto.max-w-5xl 1024.0x343.0 border R:1px solid / L:1px solid; div.border-border.flex 1022.0x85.0 border T:1px solid; a.bg-foreground/5.hover:bg-foreground/10 129.0x28.0 bg #e3e0df @ 0.05 r 3.35544e+07px; span.absolute.inline-flex 16.0x16.0 bg #00bc7d r 3.35544e+07px |
| How | resting state |

Crops: `footer-default.png`.

#### footer-link

Footer link. A muted footer link (text-muted-foreground) inside the dark footer.

Page: /. Selector: `footer a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 62 x 17 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #a3a09f | #e3e0df |
| Transition | none | = |
| Cursor | pointer | = |
| How | resting state | mouse hover over the element |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

#### cookie-settings

"Cookie settings" button. The footer control that re-shows the consent banner — a local UI toggle.

Page: /. Selector: `button (text Cookie settings)`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 112 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #a3a09f | #e3e0df | #e3e0df |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | resting state | mouse hover over the element | the button's own press (the consent banner returns; Decline dismisses it again) |

Crops: `cookie-settings-default.png`, `cookie-settings-hover.png`, `cookie-settings-opened.png`.

### Home

#### feature-tab

Feature tab (vertical). One row of the vertical feature tabs ("Draw on the page"): role=tab, muted until selected. "selected" is the tab's own activation.

Page: /. Selector: `[role="tab"]`. States: default, hover, selected.

| Property | default | hover | selected |
|---|---|---|---|
| Size (w x h) | 282.67 x 57 | = | 282.67 x 111 |
| Padding | 16px 0px | = | = |
| Border | T: none; R: none; B: 1px solid #e4e4e7; L: none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #747170 | #111827 | #111827 |
| Text node | span.text-base.font-medium: Inter 16px/24px 500, #747170, ls -0.4px | span.text-base.font-medium: Inter 16px/24px 500, #111827, ls -0.4px | span.text-base.font-medium: Inter 16px/24px 500, #111827, ls -0.4px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.group.text-muted-foreground 282.7x57.0 border B:1px solid | = | button.group.text-muted-foreground 282.7x111.0 border B:1px solid |
| How | resting state | mouse hover over the element | the tab's own activation (aria-selected switches the demo panel) |

Crops: `feature-tab-default.png`, `feature-tab-hover.png`, `feature-tab-selected.png`.

#### integration-card

Integration card. An integration card on the home grid ("Linear" — icon, name, one line): bg-background rounded-xl shadow-xs.

Page: /. Selector: `a (text Linear)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 314.66 x 196 | = |
| Padding | 24px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Text node | h3.heading-4: Inter 20px/28px 500, #111827, ls -0.5px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #111827 | = |
| Painted layers | a.bg-background.flex 314.7x196.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.bg-background.ring-background 40.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `integration-card-default.png`, `integration-card-hover.png`.

#### mcp-card-dark

Dark MCP panel. The .dark "Let your AI agent fix comments over MCP" card — the marketing page's painted-dark surface evidence: bg-background/text-foreground inside .dark re-point to the dark palette.

Page: /. Selector: `.dark a, a.dark`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 976 x 88 | = |
| Padding | 24px | = |
| Gap | 24px 16px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #0e0b0d | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #e3e0df | = |
| Text node | h3.heading-4.order-last: Inter 20px/28px 500, #e3e0df, ls -0.5px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #e3e0df | = |
| Painted layers | a.bg-background.flex 976.0x88.0 bg #0e0b0d r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.bg-muted.ring-background 40.0x40.0 bg #2a2625 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0e0b0d 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.bg-muted.ring-background 40.0x40.0 bg #2a2625 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0e0b0d 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; span.bg-muted.ring-background 40.0x40.0 bg #2a2625 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0e0b0d 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `mcp-card-dark-default.png`, `mcp-card-dark-hover.png`.

#### testimonial-card-dark

Dark testimonial card. A large .dark testimonial card (quote + attribution) in the testimonials grid.

Page: /. Selector: `a.dark`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 645.33 x 384 | = | = |
| Padding | 24px | = | = |
| Gap | 48px | = | = |
| Border | none | = | = |
| Radius | 16px | = | = |
| Background | #0e0b0d | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f54900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #e3e0df | = | = |
| Text node | blockquote.heading-3.-indent-[0.4em]: Inter 26px/31.2px 500, #e3e0df, ls -1.3px | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.dark.focus-visible:ring-ring/50 645.3x384.0 bg #0e0b0d r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div.from-background/95.via-background/35 645.3x384.0 image radial-gradient(at 0% 100%, #0e0b0d @ 0.95 0px, #0e0b0d @ 0.35 50%, #000000 @ 0 100%) | = | a.dark.focus-visible:ring-ring/50 645.3x384.0 bg #0e0b0d r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f54900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px; div.from-background/95.via-background/35 645.3x384.0 image radial-gradient(at 0% 100%, #0e0b0d @ 0.95 0px, #0e0b0d @ 0.35 50%, #000000 @ 0 100%) |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `testimonial-card-dark-default.png`, `testimonial-card-dark-hover.png`, `testimonial-card-dark-focus-visible.png`.

#### show-more

"Show more testimonials" button. The ghost expander under the testimonial grid. "opened" is its own press (the grid grows).

Page: /. Selector: `button (text Show more testimonials)`. States: default, hover, focus-visible, opened.

| Property | default | hover | focus-visible | opened |
|---|---|---|---|---|
| Size (w x h) | 218 x 36 | = | = | 120 x 36 |
| Padding | 8px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #111827 @ 0.2 | = |
| Radius | 12px | = | = | = |
| Background | transparent | #111827 @ 0.05 | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111827 | #18181b | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #111827 | 16 x 16, colour #18181b | = | = |
| Painted layers | button.inline-flex.items-center 218.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | button.inline-flex.items-center 218.0x36.0 bg #111827 @ 0.05 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | button.inline-flex.items-center 218.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 120.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | the button's own press (testimonial grid expanded) |

Crops: `show-more-default.png`, `show-more-hover.png`, `show-more-focus-visible.png`, `show-more-opened.png`.

#### faq-question

FAQ accordion question. A question row in the page FAQ accordion. "opened" is its own press revealing the answer.

Page: /. Selector: `button[aria-expanded]`. States: .

The saved states read the header Solutions trigger (85x20), not a question row. Selectors are scoped to main button[aria-expanded] whose label contains "?". Not remeasured: no live recapture.

### Pricing

#### plan-card

Plan card. A pricing plan card on /pricing (name, price, feature list, CTA).

Page: /pricing. Selector: `main box (priced plan)`. States: .

The saved state reads the "Free forever" label (274.66x16), not a plan card. The picker now requires a price, a call to action, several lines and height of at least 160. Not remeasured: no live recapture.

#### billing-switch

Billing switch. A monthly/annual switch on the plan cards (role=switch, data-state=checked, bg-primary on). "off" is its own press — then pressed back.

Page: /pricing. Selector: `button[role="switch"]`. States: default, hover, focus-visible, off.

| Property | default | hover | focus-visible | off |
|---|---|---|---|---|
| Size (w x h) | 32 x 18.39 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ff6900 | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ea580d | = | = | #e4e4e7 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111827 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.peer.data-[state=checked]:bg-primary 32.0x18.4 bg #ea580d border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.bg-background.dark:data-[state=unchecked]:bg-foreground 16.0x16.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | button.peer.data-[state=checked]:bg-primary 32.0x18.4 bg #ea580d border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px; span.bg-background.dark:data-[state=unchecked]:bg-foreground 16.0x16.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | button.peer.data-[state=checked]:bg-primary 32.0x18.4 bg #e4e4e7 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.bg-background.dark:data-[state=unchecked]:bg-foreground 16.0x16.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | the switch's own press (aria-checked flips; pressed again to restore) |

Crops: `billing-switch-default.png`, `billing-switch-hover.png`, `billing-switch-focus-visible.png`, `billing-switch-off.png`.

#### plan-cta

"Sign up free" button. A plan call-to-action — links to the app sign-up, measured never followed.

Page: /pricing. Selector: `a (text Sign up free)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 306.66 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ea580d | #ea580d @ 0.9 | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fff7ed | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 306.7x36.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | a.inline-flex.items-center 306.7x36.0 bg #ea580d @ 0.9 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | a.inline-flex.items-center 306.7x36.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = |
| Ancestor paint | 3 up div.bg-background.rounded-xl bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### compare-link-card

Alternative-comparison card. A "… alternative" card under the pricing grid, same card grammar as the integration cards.

Page: /pricing. Selector: `a (text alternative)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 314.66 x 56 | = |
| Padding | 16px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Text node | span.text-base.font-medium: Inter 16px/24px 500, #111827 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #747170 | 16 x 16, colour #111827 |
| Painted layers | a.group.bg-background 314.7x56.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `compare-link-card-default.png`, `compare-link-card-hover.png`.

### Support

#### support-search

Support search input. The "Search…" field at the top of /support. "focused" is the field clicked into — nothing is typed.

Page: /support. Selector: `input`. States: default, focused, focus-visible.

| Property | default | focused | focus-visible |
|---|---|---|---|
| Size (w x h) | 976 x 48 | = | = |
| Padding | 4px 12px 4px 40px | = | = |
| Border | 1px solid #e4e4e7 | 1px solid #ff6900 | 1px solid #ff6900 |
| Radius | 3.35544e+07px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | = | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #747170, opacity 1 | = | = |
| Painted layers | input.file:text-foreground.placeholder:text-muted-foreground 976.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.file:text-foreground.placeholder:text-muted-foreground 976.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | input.file:text-foreground.placeholder:text-muted-foreground 976.0x48.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | resting state | the field clicked into | keyboard focus (Shift+Tab, Tab) |

Crops: `support-search-default.png`, `support-search-focused.png`, `support-search-focus-visible.png`.

#### support-category

Support category card. A category card on the support index ("Getting started" — heading + one line).

Page: /support. Selector: `a (text Getting started)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 480 x 172 | = |
| Padding | 24px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Text node | h3.heading-4: Inter 20px/28px 500, #111827, ls -0.5px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #111827 | = |
| Painted layers | a.bg-background.flex 480.0x172.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.flex.size-10 40.0x40.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | = |
| How | resting state | mouse hover over the element |

Crops: `support-category-default.png`, `support-category-hover.png`.

### Tools

#### tool-color-input

Colour input. The native colour swatch input on the contrast checker (input[type=color]) — measured at rest.

Page: /tools/color-contrast-checker. Selector: `input[type="color"]`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 36 x 36 | = |
| Padding | 0px | = |
| Border | 1px solid #e4e4e7 | = |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #ff6900 @ 0.5 offset 0px |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Placeholder | #111827, opacity 1 | = |
| Painted layers | input.border-input.bg-background 36.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px | input.border-input.bg-background 36.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px outline 1px auto #ff6900 @ 0.5 offset 0px |
| How | resting state | keyboard focus (Shift+Tab, Tab) |

Crops: `tool-color-input-default.png`, `tool-color-input-focus-visible.png`.

#### tool-text-input

Hex text input. The hex value text field beside the colour input (#000000) — measured at rest; nothing is typed.

Page: /tools/color-contrast-checker. Selector: `input (no type attr; .type reads text)`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 282 x 36 | = |
| Padding | 4px 12px | = |
| Border | 1px solid #e4e4e7 | 1px solid #ff6900 |
| Radius | 10px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = |
| Font | ui-monospace 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #747170, opacity 1 | = |
| Painted layers | input.file:text-foreground.placeholder:text-muted-foreground 282.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.file:text-foreground.placeholder:text-muted-foreground 282.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | resting state | keyboard focus (Shift+Tab, Tab) |

Crops: `tool-text-input-default.png`, `tool-text-input-focus-visible.png`.

### Contact

#### contact-copy

"Copy" icon button. The copy button beside a published contact email — measured, never pressed (it writes to the clipboard).

Page: /contact. Selector: `button (text Copy)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e4e4e7 | = | 1px solid #111827 @ 0.2 | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | #f6f3f2 | = | #f6f3f2 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #111827 | #18181b | = | #18181b |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #111827 | 16 x 16, colour #18181b | = | 16 x 16, colour #18181b |
| Painted layers | button.inline-flex.items-center 84.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.inline-flex.items-center 84.0x36.0 bg #f6f3f2 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.inline-flex.items-center 84.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px | button.inline-flex.items-center 84.0x36.0 bg #f6f3f2 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| Ancestor paint | 2 up div.bg-card.border-border/50 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press |

Crops: `contact-copy-default.png`, `contact-copy-hover.png`, `contact-copy-focus-visible.png`, `contact-copy-pressed.png`.

#### contact-row

Contact channel row. A contact row on /contact ("Sales, inquiries & partnerships" + the published hello@huddlekit.com).

Page: /contact. Selector: `main box (contact row)`. States: .

The saved state reads only hello@huddlekit.com (179x28), not the channel row. The picker now requires the channel name and the address together. Not remeasured: no live recapture.

### Prose

#### prose-h1

Article title (h1). The post title on a blog article.

Page: /blog/introducing-huddlekit. Selector: `main h1, h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 634.66 x 48.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 44px/48.4px 500 |
| Letter spacing | -2.2px |
| Colour | #111827 |
| Transition | none |
| How | resting state |

Crops: `prose-h1-default.png`.

#### prose-meta

Article meta line. The date / updated / read-time / author line under the title.

Page: /blog/introducing-huddlekit. Selector: `main p, main time`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 274.66 x 20 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 500 |
| Letter spacing | normal |
| Colour | #747170 |
| Text node | span: Inter 14px/20px 500, #747170 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 3 up article.bg-background.flex bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | resting state |

Crops: `prose-meta-default.png`.

#### prose-p

Body paragraph. A paragraph of article prose.

Page: /blog/introducing-huddlekit. Selector: `main p (sentence)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 634.66 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #747170 |
| Text node | em: Inter 16px/24px 400, #747170 |
| Transition | none |
| How | resting state |

Crops: `prose-p-default.png`.

#### prose-link

Prose link. A body-text link inside the article.

Page: /blog/introducing-huddlekit. Selector: `main :is(p,li) a`. States: .

The saved states read the breadcrumb "Home" (40x20), not a link in the article. The selector is now article :is(p, li) a. Not remeasured: no live recapture.

#### breadcrumb

Breadcrumb. The Home / Blog / … breadcrumb above the article.

Page: /blog/introducing-huddlekit. Selector: `nav[aria-label*="breadcrumb" i], nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 634.66 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111827 |
| Text node | a.hover:text-foreground.transition-colors: Inter 14px/20px 500, #747170 |
| Transition | none |
| Icon | 14 x 14, colour #747170 |
| How | resting state |

Crops: `breadcrumb-default.png`.

### Integrations

#### integration-grid-card

Integration page card. A card on the /integrations index (Slack — icon, name, description).

Page: /integrations. Selector: `a (text Slack)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 314.66 x 196 | = |
| Padding | 24px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | = |
| Text node | h3.heading-4: Inter 20px/28px 500, #111827, ls -0.5px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #111827 | = |
| Painted layers | a.bg-background.flex 314.7x196.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.bg-background.ring-background 40.0x40.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| How | resting state | mouse hover over the element |

Crops: `integration-grid-card-default.png`, `integration-grid-card-hover.png`.

### Compare

#### compare-toc

"Contents" rail. The Contents navigation on a comparison page.

Page: /compare/pastel-alternative. Selector: `nav, aside`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 293.33 x 12086.48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111827 |
| Text node | h2.text-foreground.mb-3: Inter 16px/24px 500, #111827 |
| Transition | none |
| Icon | 16 x 16, colour #fff7ed |
| Painted layers | div.bg-card.rounded-md 293.3x304.0 bg #ffffff r 10px; div.bg-card.rounded-lg 293.3x156.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; button.inline-flex.items-center 261.3x36.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px |
| How | resting state |

Crops: `compare-toc-default.png`.

#### compare-check-item

Feature-check list row. A checklist row in the comparison (a lucide check / badge icon + capability line).

Page: /compare/pastel-alternative. Selector: `li`. States: .

The saved state reads the breadcrumb "Home", not a checklist row. The selector now requires a list item that holds an svg and a longer label. Not remeasured: no live recapture.

### App login

#### app-login-card

Sign-in panel. The centred "Sign in to Huddlekit" panel: wordmark, heading, the Google and email buttons, and the privacy/terms line.

Page: /login. Selector: `main, main [class*="card"], div[class*="bg-"]`. States: default, dark.

| Property | default | dark |
|---|---|---|
| Size (w x h) | 320 x 168 | = |
| Padding | 0px | = |
| Gap | 24px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #111827 | #e3e0df |
| Text node | h1.text-lg.font-semibold: inter 18px/28px 600, #111827 | h1.text-lg.font-semibold: inter 18px/28px 600, #e3e0df |
| Transition | none | = |
| Icon | 16 x 16, colour #fff7ed, fill #000000 | = |
| Painted layers | button.inline-flex.items-center 320.0x40.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px; button.inline-flex.items-center 320.0x40.0 bg #ede9e7 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | button.inline-flex.items-center 320.0x40.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px; button.inline-flex.items-center 320.0x40.0 bg #2a2625 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px |
| How | resting state | same element after prefers-color-scheme repaints html.dark (the signal the app honours; the login has no theme control of its own) |

Crops: `app-login-card-default.png`, `app-login-card-dark.png`.

#### app-google-button

"Continue with Google" button. The primary OAuth button (bg-primary). Never pressed — it would leave for Google sign-in.

Page: /login. Selector: `button (text Continue with Google)`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 320 x 40 | = | = | = | = |
| Padding | 0px 16px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 12px | = | = | = | = |
| Background | #ea580d | #ea580d @ 0.9 | = | #ea580d @ 0.9 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | = |
| Outline | none | = | = | = | = |
| Font | inter 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #fff7ed | = | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #fff7ed, fill #000000 | = | = | = | = |
| Painted layers | button.inline-flex.items-center 320.0x40.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | button.inline-flex.items-center 320.0x40.0 bg #ea580d @ 0.9 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | button.inline-flex.items-center 320.0x40.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | button.inline-flex.items-center 320.0x40.0 bg #ea580d @ 0.9 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press | same element after prefers-color-scheme repaints html.dark (the signal the app honours; the login has no theme control of its own) |

Crops: `app-google-button-default.png`, `app-google-button-hover.png`, `app-google-button-focus-visible.png`, `app-google-button-pressed.png`, `app-google-button-dark.png`.

#### app-email-button

"Continue with email" button. The secondary sign-in button (bg-secondary). "pressed" is the CDP-forced pseudo-state only; the real press is the email-reveal spec below.

Page: /login. Selector: `button (text Continue with email)`. States: default, hover, focus-visible, pressed, dark.

| Property | default | hover | focus-visible | pressed | dark |
|---|---|---|---|---|---|
| Size (w x h) | 320 x 40 | = | = | = | = |
| Padding | 0px 16px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #111827 @ 0.2 | = | = |
| Radius | 12px | = | = | = | = |
| Background | #ede9e7 | #ede9e7 @ 0.8 | = | #ede9e7 @ 0.8 | #2a2625 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | = |
| Outline | none | = | = | = | = |
| Font | inter 14px/20px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #18181b | = | = | = | #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #18181b | = | = | = | 16 x 16, colour #fafafa |
| Painted layers | button.inline-flex.items-center 320.0x40.0 bg #ede9e7 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | button.inline-flex.items-center 320.0x40.0 bg #ede9e7 @ 0.8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | button.inline-flex.items-center 320.0x40.0 bg #ede9e7 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | button.inline-flex.items-center 320.0x40.0 bg #ede9e7 @ 0.8 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | button.inline-flex.items-center 320.0x40.0 bg #2a2625 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) | CDP CSS.forcePseudoState(:active:hover) — no real press | same element after prefers-color-scheme repaints html.dark (the signal the app honours; the login has no theme control of its own) |

Crops: `app-email-button-default.png`, `app-email-button-hover.png`, `app-email-button-focus-visible.png`, `app-email-button-pressed.png`, `app-email-button-dark.png`.

#### app-email-input

Email input. The "Enter your email" field the Continue-with-email press reveals — a local state change; nothing is typed and Continue is never pressed.

Page: /login. Selector: `input[type="email"]`. States: default, focused, dark.

| Property | default | focused | dark |
|---|---|---|---|
| Size (w x h) | 320 x 36 | = | = |
| Padding | 4px 12px | = | = |
| Border | 1px solid #e4e4e7 | 1px solid #ff6900 | 1px solid #ffffff @ 0.16 |
| Radius | 12px | = | = |
| Background | #ffffff | = | #ffffff @ 0.048 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = | = |
| Font | inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | = | #e3e0df |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #747170, opacity 1 | = | #a3a09f, opacity 1 |
| Painted layers | input.file:text-foreground.placeholder:text-muted-foreground 320.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.file:text-foreground.placeholder:text-muted-foreground 320.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ff6900 @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | input.file:text-foreground.placeholder:text-muted-foreground 320.0x36.0 bg #ffffff @ 0.048 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | resting state | the field clicked into | same element after prefers-color-scheme repaints html.dark (the signal the app honours; the login has no theme control of its own) |

Crops: `app-email-input-default.png`, `app-email-input-focused.png`, `app-email-input-dark.png`.

#### app-continue-button

Email "Continue" submit. The primary submit under the email field — measured, never pressed (it would send a sign-in code).

Page: /login. Selector: `button (text Continue with email)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 320 x 40 | = | = |
| Padding | 0px 24px | = | = |
| Gap | 6px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | #ea580d | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | = |
| Outline | none | = | = |
| Font | inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #fff7ed | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Opacity | 0.5 | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.inline-flex.items-center 320.0x40.0 bg #ea580d r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px | = | = |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `app-continue-button-default.png`, `app-continue-button-hover.png`, `app-continue-button-focus-visible.png`.

#### app-back-button

"Back to login" button. The ghost return control under the email form.

Page: /login. Selector: `button (text Back to login)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 320 x 40 | = |
| Padding | 0px 16px | = |
| Gap | 6px | = |
| Border | 1px solid #000000 @ 0 | = |
| Radius | 12px | = |
| Background | transparent | #f6f3f2 |
| Box shadow | none | = |
| Outline | none | = |
| Font | inter 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #111827 | #18181b |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #111827 | 16 x 16, colour #18181b |
| Painted layers | button.inline-flex.items-center 320.0x40.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px | button.inline-flex.items-center 320.0x40.0 bg #f6f3f2 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px |
| How | resting state | mouse hover over the element |

Crops: `app-back-button-default.png`, `app-back-button-hover.png`.

### Chrome (mobile)

#### m-header

Mobile header. The header at 390px: logo, the "Toggle menu" button and the "Get started" link.

Page: /. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 64 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #111827 |
| Transition | none |
| Icon | 104 x 28, colour #111827 |
| Painted layers | a.inline-flex.items-center 0.0x0.0 bg #ede9e7 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.25 0px 1px 0px 0px inset, #ffffff @ 0.19 0px 6px 9px -7px inset, #000000 @ 0.12 0px 1px 2px 0px, #000000 @ 0.09 0px 2px 5px -1px; button.inline-flex.items-center 36.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | resting state |

Crops: `m-header-default.png`.

#### m-menu-button

"Toggle menu" button. The hamburger that opens the phone nav.

Page: /. Selector: `button (aria-label Toggle menu)`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = |
| Padding | 0px | = | = |
| Gap | 6px | = | = |
| Border | 1px solid #e4e4e7 | = | 1px solid #111827 @ 0.2 |
| Radius | 12px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #111827 | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #111827 | = | = |
| Painted layers | button.inline-flex.items-center 36.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | button.inline-flex.items-center 36.0x36.0 bg #ffffff border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #111827 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 1px 2px 0px |
| How | resting state | mouse hover over the element | keyboard focus (Shift+Tab, Tab) |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`.

#### m-nav-drawer

Nav sheet (open). The opened navigation panel — the "Toggle menu" press drops an absolute rounded-md sheet under the sticky header; the press happens in find().

Page: /. Selector: `header div[class*="absolute"]`. States: .

The saved state reads the Features link (62x17). domFind no longer falls back to that link when the drawer ancestor is absent. Not remeasured: no live recapture. 62px is not the drawer width.

## Transitions declared in the readable stylesheets

huddlekit.com and app.huddlekit.com serve their own CSS same-origin (/_next/static/css), so this list is the site's own transition declarations the CSSOM could read on each page.

- /: none

- /blog/introducing-huddlekit: none

- /compare/pastel-alternative: none

- /contact: none

- /integrations: none

- /login: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- /pricing: none

- /support: none

- /tools/color-contrast-checker: none
