# Melius component measurements

Computed styles read from www.melius.com, app.melius.com and docs.melius.com on 2026-11-19 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Navigation

#### wordmark

Wordmark.

Page: undefined. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 72 x 14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0e0e0e |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `wordmark-default.png`.

#### nav-link

Pricing link.

Page: undefined. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.59 x 32.31 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #2a2a2a | = | #2a2a2a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f04e23 offset 2px | = |
| Font | easeStandard 13.6px/16.32px 400 | = | = | = |
| Letter spacing | -0.408px | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### m-menu

Mobile menu button.

Page: undefined. Selector: ``. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 0 x 0 | = |
| Padding | 8px 12px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | easeStandard 13.6px/16.32px 400 | = |
| Letter spacing | -0.408px | = |
| Colour | #fafafa | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |

Crops: none.

### Button

#### nav-signin

Sign In.

Page: undefined. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.06 x 40 | = | = | = |
| Padding | 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #fff78b | #fff78b @ 0.8 | = | #fff78b @ 0.8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f04e23 offset 2px | = |
| Font | easeStandard 12.8px/15.36px 400 | = | = | = |
| Letter spacing | -0.384px | = | = | = |
| Colour | #0e0e0e | = | = | = |
| Transition | background-color, border-color, color, opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-start

Start for Free.

Page: undefined. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.39 x 40 | = | = | = |
| Padding | 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f04e23 | #f04e23 @ 0.8 | = | #f04e23 @ 0.8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f04e23 offset 2px | = |
| Font | easeStandard 12.8px/15.36px 400 | = | = | = |
| Letter spacing | -0.384px | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, border-color, color, opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |

Crops: `nav-start-default.png`, `nav-start-hover.png`, `nav-start-focus-visible.png`, `nav-start-pressed.png`.

#### hero-cta

Get started for free.

Page: undefined. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184.8 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #f04e23 | #f04e23 @ 0.8 | = | #f04e23 @ 0.8 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f04e23 offset 2px | = |
| Font | easeStandard 16px/22.4px 400 | = | = | = |
| Letter spacing | -0.48px | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, border-color, color, opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### plan-cta

Start with Creator.

Page: undefined. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344.66 x 48 | = | = | = |
| Padding | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #1a1616 | #fff78b | = | #fff78b |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #f04e23 offset 2px | = |
| Font | easeStandard 12.8px/15.36px 400 | = | = | = |
| Letter spacing | -0.384px | = | = | = |
| Colour | #fafafa | #0e0e0e | = | #0e0e0e |
| Transition | background-color, border-color, color, opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### login-submit

Log in button.

Page: undefined. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f04e23 | = | = | #ad3213 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Instrument Sans 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-google

Continue with Google.

Page: undefined. Selector: ``. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 334 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #ffffff @ 0.9 | = | #ffffff @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Instrument Sans 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

### Type

#### hero-title

Hero title.

Page: undefined. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 751.97 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | recklessStandard 56px/56px 400 |
| Letter spacing | -1.12px |
| Colour | #0e0e0e |
| Text node | undefined: recklessStandard 56px/56px 400, #0e0e0e, ls -1.12px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### login-title

Login title.

Page: undefined. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1 x 1 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Instrument Sans 20px/24px 500 |
| Letter spacing | -0.2px |
| Colour | #c0c0c0 |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### signup-title

Signup title.

Page: undefined. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1 x 1 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Instrument Sans 20px/24px 500 |
| Letter spacing | -0.2px |
| Colour | #c0c0c0 |
| Transition | none |
| How | at rest |

Crops: `signup-title-default.png`.

#### docs-title

Docs title.

Page: undefined. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 101.45 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/24px 600 |
| Letter spacing | normal |
| Colour | #161616 |
| Text node | undefined: Inter 14px/24px 600, #161616 |
| Transition | none |
| How | at rest |

Crops: `docs-title-default.png`.

### Menu

#### nav-product

Product menu trigger.

Page: undefined. Selector: ``. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 96.44 x 32.31 | = |
| Padding | 8px 12px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | transparent | #2a2a2a |
| Box shadow | none | = |
| Outline | none | = |
| Font | easeStandard 13.6px/16.32px 400 | = |
| Letter spacing | -0.408px | = |
| Colour | #fafafa | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `nav-product-default.png`, `nav-product-hover.png`.

#### menu-item

Product menu item.

Page: undefined. Selector: ``. States: .

Not found on the page at capture time.

#### m-menu-link

Mobile pricing link.

Page: undefined. Selector: ``. States: .

Not found on the page at capture time.

### Link

#### footer-link

Footer link.

Page: undefined. Selector: ``. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 37.27 x 16.31 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 6px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | easeStandard 13.6px/16.32px 400 | = |
| Letter spacing | -0.408px | = |
| Colour | #676767 | #fafafa |
| Transition | background-color, border-color, color, opacity 0.2s cubic-bezier(0.37, 0, 0.63, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Opacity | - | 0.8 |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

#### docs-link

Docs link.

Page: undefined. Selector: ``. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 53.66 x 20 | = |
| Padding | 0px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #4f4f4f | #161616 |
| Text node | undefined: Inter 14px/20px 500, #4f4f4f | undefined: Inter 14px/20px 500, #161616 |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `docs-link-default.png`, `docs-link-hover.png`.

### Card

#### plan-title

Creator plan title.

Page: undefined. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 328.66 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futurist 32px/32px 400 |
| Letter spacing | -1.28px |
| Colour | #0e0e0e |
| Transition | none |
| How | at rest |

Crops: `plan-title-default.png`.

#### plan-card

Creator plan card.

Page: undefined. Selector: ``. States: default.

| Property | default |
|---|---|
| Size (w x h) | 386.66 x 754.53 |
| Padding | 32px 20px 12px 20px |
| Border | 1px solid #000000 @ 0 |
| Radius | 12px |
| Background | #fafafa |
| Box shadow | #f04e23 @ 0.237807 0px 0px 15.3355px 0px, #f04e23 @ 0.126678 0px 0px 24.4452px 0px |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0e0e0e |
| Transition | all 0.2s ease |
| How | at rest |

Crops: `plan-card-default.png`.

### Field

#### login-email

Email field.

Page: undefined. Selector: ``. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 284 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Instrument Sans 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #c0c0c0 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| How | at rest | clicked into the field; nothing submitted | sample text typed, then the field is cleared; nothing submitted |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### signup-email

Signup email.

Page: undefined. Selector: ``. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 284 x 20 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Instrument Sans 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #c0c0c0 | = |
| Transition | none | = |
| Cursor | text | = |
| How | at rest | clicked into the field; nothing submitted |

Crops: `signup-email-default.png`, `signup-email-focused.png`.

#### contact-field

Contact field.

Page: undefined. Selector: ``. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 250.5 x 44 | = |
| Padding | 4px 12px | = |
| Border | 1px solid #fafafa @ 0.25 | = |
| Radius | 6px | = |
| Background | transparent | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #f04e23 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | ui-sans-serif 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| How | at rest | clicked into the field; nothing submitted |

Crops: `contact-field-default.png`, `contact-field-focused.png`.

## Transitions declared in the readable stylesheets

Cross-origin stylesheets may be missing from this list; the per-state Transition rows above are computed values.
