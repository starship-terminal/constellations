# Component measurements

Computed styles read from appwrite.io on 2026-11-21 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) with the marketing site's pinned dark theme, and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### banner

Announcement banner. The strip above the header carrying the current announcement and a dismiss button.

Page: home. Selector: `div:has(> button[aria-label*="ismiss" i])`. States: default.

Not found on the page at capture time.

#### banner-dismiss

Banner dismiss button.

Page: home. Selector: `button[aria-label*="ismiss" i]`. States: default, hover, focus-visible, pressed.

Not found on the page at capture time.

#### header

Top bar. The fixed glass bar over every marketing page: logo, Products/Solutions flyout buttons, section links, GitHub stars, Sign in/up.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px 24px 0px 16px |
| Gap | 8px |
| Border | T: none; R: none; B: 1px solid #222224; L: none |
| Radius | 0px |
| Background | #19191c |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | button.inline-flex.h-9: -apple-system 13px/19.5px 500, #9f9fa9 |
| Transition | none |
| Icon | 0 x 0, colour #9f9fa9 |
| Painted layers | header.h-14.min-h-14 1440.0x56.0 bg #19191c border B:1px solid #222224; span.absolute.-end-1.5 6.0x6.0 bg #fd366e r 3.35544e+07px; a.inline-flex.items-center 67.9x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px; a.inline-flex.items-center 72.6x36.0 bg #fd366e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `a[aria-label="Appwrite"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126 x 40 |
| Padding | 0px 8px |
| Border | none |
| Radius | 10px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 110 x 20, colour #fafafa |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A top-level destination in the bar: 13px text in a 36px rounded-md row.

Page: home. Selector: `header a:has-text("Pricing")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 63.11 x 36 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Text node | span.relative: -apple-system 13px/19.5px 500, #9f9fa9 | span.relative: -apple-system 13px/19.5px 500, #fafafa | = | span.relative: -apple-system 13px/19.5px 500, #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.link-unstyled.inline-flex 63.1x36.0 bg #2d2d31 r 8px | a.link-unstyled.inline-flex 63.1x36.0 r 8px outline 1px auto #54545d @ 0.5 offset 1px | a.link-unstyled.inline-flex 63.1x36.0 bg #2d2d31 r 8px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-menu-button

Nav flyout button. Products and Solutions open a flyout; measured at rest, never opened (the flyout is captured in screenshots only when it mounts open).

Page: home. Selector: `header button:has-text("Products")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.88 x 36 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 0px | = |
| Font | -apple-system 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #9f9fa9 | 14 x 14, colour #fafafa | = | 14 x 14, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.h-9 93.9x36.0 bg #2d2d31 r 8px | button.inline-flex.h-9 93.9x36.0 r 8px outline 1px auto #54545d @ 0.5 offset 0px | button.inline-flex.h-9 93.9x36.0 bg #2d2d31 r 8px |

Crops: `nav-menu-button-default.png`, `nav-menu-button-hover.png`, `nav-menu-button-focus-visible.png`, `nav-menu-button-pressed.png`.

#### nav-menu-open

Nav flyout, open. The button after its own flyout toggle: the opened panel underneath (a popover-foreground div the toggle mounts) is what the crop shows.

Page: home. Selector: `header button:has-text("Products")`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 93.88 x 36 |
| Padding | 0px 10px |
| Gap | 4px |
| Border | none |
| Radius | 8px |
| Background | #2d2d31 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 13px/19.5px 500 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 14 x 14, colour #fafafa |
| Painted layers | button.inline-flex.h-9 93.9x36.0 bg #2d2d31 r 8px |
| How | own toggle |

Crops: `nav-menu-open-opened.png`.

#### nav-github

GitHub stars link. The star-count link to the repo.

Page: home. Selector: `header a[aria-label*="GitHub" i]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.05 x 36 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | #2d2d31 | #2d2d31 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | #fafafa | #fafafa |
| Text node | span: -apple-system 13px/19.5px 500, #9f9fa9 | span: -apple-system 13px/19.5px 500, #fafafa | span: -apple-system 13px/19.5px 500, #fafafa | span: -apple-system 13px/19.5px 500, #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9f9fa9 | 16 x 16, colour #fafafa | 16 x 16, colour #fafafa | 16 x 16, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.inline-flex.h-9 79.0x36.0 bg #2d2d31 r 8px | a.inline-flex.h-9 79.0x36.0 bg #2d2d31 r 8px outline 1px auto #54545d @ 0.5 offset 1px | a.inline-flex.h-9 79.0x36.0 bg #2d2d31 r 8px |

Crops: `nav-github-default.png`, `nav-github-hover.png`, `nav-github-focus-visible.png`, `nav-github-pressed.png`.

#### signin-button

Sign in button. Ghost-style header action. Measured, never followed.

Page: home. Selector: `header a:has-text("Sign in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.88 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 67.9x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | a.inline-flex.items-center 67.9x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | a.inline-flex.items-center 67.9x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 67.9x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-button-default.png`, `signin-button-hover.png`, `signin-button-focus-visible.png`, `signin-button-pressed.png`.

#### signup-button

Sign up button. The filled header action. Measured, never followed.

Page: home. Selector: `header a:has-text("Sign up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.59 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #54545d | = |
| Radius | 8px | = | = | = |
| Background | #fd366e | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 72.6x36.0 bg #fd366e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | a.inline-flex.items-center 72.6x36.0 bg #fd366e border T:1px solid #54545d / R:1px solid #54545d / B:1px solid #54545d / L:1px solid #54545d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `signup-button-default.png`, `signup-button-hover.png`, `signup-button-focus-visible.png`, `signup-button-pressed.png`.

#### skip-link

Skip link. The off-screen accessibility link, revealed by keyboard focus.

Page: home. Selector: `a:has-text("Skip to content")`. States: focus-visible.

| Property | focus-visible |
|---|---|
| Size (w x h) | 127.98 x 41.5 |
| Padding | 10px 16px |
| Border | 1px solid #222224 |
| Radius | 14px |
| Background | #19191c |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #19191c 0px 0px 0px 2px, #54545d 0px 0px 0px 4px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Outline | none |
| Font | -apple-system 13px/19.5px 500 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | opacity, transform 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | a.fixed.start-4 128.0x41.5 bg #19191c border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #19191c 0px 0px 0px 2px, #54545d 0px 0px 0px 4px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Ancestor paint | 1 up div.flex.h-full bg #19191c |
| How | Shift+Tab, Tab |

Crops: `skip-link-focus-visible.png`.

### Home

#### announcement-pill

Announcement pill. The "Breaking" link pill under the hero.

Page: home. Selector: `a:has-text("thrilled to announce")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 347.88 x 28 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Backdrop filter | blur(8px) | = | = | = |
| Outline | none | = | = | = |
| Font | -apple-system 12px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Text node | span.text-[var(--brand-cta)]: -apple-system 12px/18px 500, #fd366e | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #9f9fa9 | 14 x 14, colour #fafafa | = | 14 x 14, colour #fafafa |
| Painted layers | a.inline-flex.items-center 347.9x28.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 3.35544e+07px | a.inline-flex.items-center 347.9x28.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 3.35544e+07px | a.inline-flex.items-center 347.9x28.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 347.9x28.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `announcement-pill-default.png`, `announcement-pill-hover.png`, `announcement-pill-focus-visible.png`, `announcement-pill-pressed.png`.

#### hero-title

Hero title. The 48px Aeonik headline with the brand gradient text.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 870.05 x 164.14 |
| Padding | 0px 5.7px 6.08px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(145deg, oklch(0.804466 0.127483 10.8203) 0%, oklch(0.696146 0.203958 10.8203) 28%, #fafafa 62%) |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Pro 76px/79.04px 400 |
| Letter spacing | -1.672px |
| Colour | #000000 @ 0 |
| Transition | none |
| Painted layers | h1.font-aeonik-pro.text-gradient-brand 870.0x164.1 image linear-gradient(145deg, oklch(0.804466 0.127483 10.8203) 0%, oklch(0.696146 0.203958 10.82 |
| How | at rest |

Crops: `hero-title-default.png`.

#### cta-primary

Primary CTA. "Start project": the main action, brand pink. Measured, never followed.

Page: home. Selector: `a:has-text("Start project")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132.94 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #54545d | = |
| Radius | 8px | = | = | = |
| Background | #fd366e | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 132.9x40.0 bg #fd366e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | a.inline-flex.items-center 132.9x40.0 bg #fd366e border T:1px solid #54545d / R:1px solid #54545d / B:1px solid #54545d / L:1px solid #54545d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `cta-primary-default.png`, `cta-primary-hover.png`, `cta-primary-focus-visible.png`, `cta-primary-pressed.png`.

#### cta-secondary

Secondary CTA. "View docs": the quiet sibling. Measured, never followed.

Page: home. Selector: `a:has-text("View docs")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117.72 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 117.7x40.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | a.inline-flex.items-center 117.7x40.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | a.inline-flex.items-center 117.7x40.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 117.7x40.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`, `cta-secondary-pressed.png`.

#### framework-icon

Framework icon button. One of the 36px round framework icons under the hero strip.

Page: home. Selector: `[aria-label="React"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | 39.6 x 39.6 | = | 39.6 x 39.6 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | transform, translate, scale, rotate 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.home-tool-link.group 36.0x36.0 outline 1px auto #54545d @ 0.5 offset 1px | = |

Crops: `framework-icon-default.png`, `framework-icon-hover.png`, `framework-icon-focus-visible.png`, `framework-icon-pressed.png`.

#### product-card

Product card. A services-grid card (Auth/Databases/...): the overlay link covers the whole card, so the card edges are what the crop shows; painted fills come from the ancestors row.

Page: home. Selector: `a[aria-label^="Learn more about"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 430.33 x 379 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #19191c 0px 0px 0px 2px, #54545d 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | -apple-system 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #fafafa | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Ancestor paint | 2 up div.product-bento-grid.mt-10 bg #19191c shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.06 0px 1px 0px 0px inset | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.link-unstyled.product-bento-link 430.3x379.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #19191c 0px 0px 0px 2px, #54545d 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px |

Crops: `product-card-default.png`, `product-card-hover.png`, `product-card-focus-visible.png`.

#### section-title

Section headline. The 40px Aeonik section title.

Page: home. Selector: `h2:has-text("All the services")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Pro 48px/48px 400 |
| Letter spacing | -1.2px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h2:has-text("Everything your app needs")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 132 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Pro 44px/66px 400 |
| Letter spacing | -1.1px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-card

Plan card. One pricing column: name, price, feature list and its own CTA; an <article> with the muted-tint fill and hairline border.

Page: pricing. Selector: `article:has(h2 "Free")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358.97 x 923.5 |
| Padding | 28px |
| Border | 1px solid #2d2d31 @ 0.3 |
| Radius | 14px |
| Background | #2d2d31 @ 0.08 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| Backdrop filter | blur(8px) |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | h2.font-semibold.text-foreground: -apple-system 14px/21px 600, #fafafa |
| Transition | none |
| Icon | 16 x 16, colour #fd366e |
| Painted layers | article.relative.isolate 359.0x923.5 bg #2d2d31 @ 0.08 border T:1px solid #2d2d31 @ 0.3 / R:1px solid #2d2d31 @ 0.3 / B:1px solid #2d2d31 @ 0.3 / L:1px solid #2d2d31 @ 0.3 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px; a.inline-flex.items-center 301.0x40.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px; div.relative.z-[1] 301.0x590.5 border T:1px solid #2d2d31 @ 0.2 |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price.

Page: pricing. Selector: `text "$0"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 37.58 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Pro 32px/48px 400 |
| Letter spacing | -0.8px |
| Colour | #fafafa |
| Transition | none |
| Ancestor paint | 2 up article.relative.isolate bg #2d2d31 @ 0.08 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The per-card action. Measured, never followed.

Page: pricing. Selector: `article a:has-text("Start project")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300.97 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 301.0x40.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | a.inline-flex.items-center 301.0x40.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | a.inline-flex.items-center 301.0x40.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 301.0x40.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px |
| Ancestor paint | 2 up article.relative.isolate bg #2d2d31 @ 0.08 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-cta-contact

Enterprise CTA. "Contact us" on the Enterprise card. Measured, never followed.

Page: pricing. Selector: `a:has-text("Contact us")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300.98 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 301.0x40.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | a.inline-flex.items-center 301.0x40.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | a.inline-flex.items-center 301.0x40.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-flex.items-center 301.0x40.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px |
| Ancestor paint | 2 up article.relative.isolate bg #2d2d31 @ 0.08 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-contact-default.png`, `plan-cta-contact-hover.png`, `plan-cta-contact-focus-visible.png`, `plan-cta-contact-pressed.png`.

#### faq-question

FAQ accordion button.

Page: pricing. Selector: `button[aria-expanded]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 0px | = |
| Font | -apple-system 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.h-4.w-4 16.0x16.0 bg #9f9fa9 | button.flex.h-8 32.0x32.0 bg #2d2d31 r 8px; span.h-4.w-4 16.0x16.0 bg #fafafa | button.flex.h-8 32.0x32.0 r 8px outline 1px auto #54545d @ 0.5 offset 0px; span.h-4.w-4 16.0x16.0 bg #9f9fa9 | button.flex.h-8 32.0x32.0 bg #2d2d31 r 8px; span.h-4.w-4 16.0x16.0 bg #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-question-default.png`, `faq-question-hover.png`, `faq-question-focus-visible.png`, `faq-question-pressed.png`.

#### faq-open

FAQ accordion, open. The same item after its own toggle; the answer region shows in the crop.

Page: pricing. Selector: `button[aria-expanded]`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #2d2d31 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | button.flex.h-8 32.0x32.0 bg #2d2d31 r 8px; span.h-4.w-4 16.0x16.0 bg #fafafa |
| How | own toggle |

Crops: `faq-open-opened.png`.

#### compare-link

Compare plans link. link-neutral text link.

Page: pricing. Selector: `a:has-text("Compare plans")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.03 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 13px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.984998 0.000024917 none / 0.85) | #fafafa | = | #fafafa |
| Transition | text-decoration-color, color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.link-neutral 93.0x16.0 outline 1px auto #54545d @ 0.5 offset 1px | = |

Crops: `compare-link-default.png`, `compare-link-hover.png`, `compare-link-focus-visible.png`, `compare-link-pressed.png`.

### Docs

#### docs-search

Docs search button. The command-K search trigger in the docs header. Measured, never opened.

Page: docs. Selector: `button:has-text("Search documentation")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 368 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #222224 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #2d2d31 @ 0.5 | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 0px | = |
| Font | -apple-system 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | = | = | = |
| Text node | span.min-w-0.flex-1: -apple-system 13px/19.5px 400, #9f9fa9 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #9f9fa9 | = | = | = |
| Painted layers | button.pointer-events-auto.flex 368.0x36.0 bg #2d2d31 @ 0.5 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px | button.pointer-events-auto.flex 368.0x36.0 bg #2d2d31 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px | button.pointer-events-auto.flex 368.0x36.0 bg #2d2d31 @ 0.5 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px outline 1px auto #54545d @ 0.5 offset 0px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px | button.pointer-events-auto.flex 368.0x36.0 bg #2d2d31 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-nav-link

Docs sidebar link.

Page: docs. Selector: `aside a:has-text("Tutorials")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 195 x 31.5 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Gap | normal 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 @ 0.5 | = | #2d2d31 @ 0.5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #19191c 0px 0px 0px 1px, #54545d 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Text node | span.min-w-0.flex-1: -apple-system 13px/19.5px 500, #9f9fa9 | span.min-w-0.flex-1: -apple-system 13px/19.5px 500, #fafafa | = | span.min-w-0.flex-1: -apple-system 13px/19.5px 500, #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9f9fa9 | 16 x 16, colour #fafafa | = | 16 x 16, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.group.rounded-md 195.0x31.5 bg #2d2d31 @ 0.5 r 8px | a.group.rounded-md 195.0x31.5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #19191c 0px 0px 0px 1px, #54545d 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group.rounded-md 195.0x31.5 bg #2d2d31 @ 0.5 r 8px |

Crops: `docs-nav-link-default.png`, `docs-nav-link-hover.png`, `docs-nav-link-focus-visible.png`, `docs-nav-link-pressed.png`.

#### docs-nav-active

Docs sidebar item, current. The item the page marks current, if any.

Page: docs. Selector: `[aria-current]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 195 x 31.5 |
| Padding | 6px 10px |
| Gap | normal 10px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 13px/19.5px 500 |
| Letter spacing | normal |
| Colour | #9f9fa9 |
| Text node | span.min-w-0.flex-1: -apple-system 13px/19.5px 500, #9f9fa9 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #9f9fa9 |
| How | at rest |

Crops: `docs-nav-active-default.png`.

#### code-block

Code block. The framed snippet on a quick-start page, with --code-* syntax colours.

Page: docs. Selector: `pre`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 621 x 74.88 |
| Padding | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-monospace 12px/19.8px 400 |
| Letter spacing | -0.0765px |
| Colour | #9cdcfe |
| Text node | span.token.function: source-code-pro 13px/21.45px 400, #67a3fe, ls -0.0765px |
| Transition | none |
| Ancestor paint | 1 up div.relative.flex shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `code-block-default.png`.

#### code-inline

Inline code.

Page: docs. Selector: `article code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 83.77 x 21 |
| Padding | 2px 6px |
| Border | 1px solid #222224 |
| Radius | 8px |
| Background | #2d2d31 @ 0.5 |
| Box shadow | none |
| Outline | none |
| Font | source-code-pro 13px/21.45px 400 |
| Letter spacing | -0.0765px |
| Colour | #fafafa @ 0.85 |
| Transition | none |
| Painted layers | code 83.8x21.0 bg #2d2d31 @ 0.5 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px |
| How | at rest |

Crops: `code-inline-default.png`.

#### docs-prose-link

Prose link.

Page: docs. Selector: `article a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.53 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 12px/18px 600 | = | = | = |
| Letter spacing | 1.44px | = | = | = |
| Colour | #9f9fa9 | #fafafa @ 0.85 | = | #fafafa @ 0.85 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-muted-foreground.transition-colors 97.5x15.0 outline 1px auto #54545d @ 0.5 offset 1px | = |

Crops: `docs-prose-link-default.png`, `docs-prose-link-hover.png`, `docs-prose-link-focus-visible.png`, `docs-prose-link-pressed.png`.

#### docs-h1

Docs page title.

Page: docs. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 599 x 45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Pro 36px/45px 400 |
| Letter spacing | -0.9px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-h2

Docs section heading.

Page: docs. Selector: `article h2/h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 623 x 24.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Pro 18px/24.75px 600 |
| Letter spacing | -0.0765px |
| Colour | #fafafa @ 0.95 |
| Text node | a.text-inherit.hover:text-inherit: Aeonik Pro 18px/24.75px 500, #fafafa @ 0.95, ls -0.0765px |
| Transition | none |
| Icon | 22.63 x 22.63, colour #9f9fa9 |
| How | at rest |

Crops: `docs-h2-default.png`.

### Blog

#### blog-title

Blog title.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Pro 48px/72px 400 |
| Letter spacing | -1.2px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `blog-title-default.png`.

#### post-card

Post card. A story tile: image, headline, author row.

Page: blog. Selector: `article:has(h2)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1232 x 333 | = |
| Padding | 0px | = |
| Gap | 48px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Text node | h2.line-clamp-2.min-h-[2lh]: Aeonik Pro 28px/36.4px 400, #fafafa | h2.line-clamp-2.min-h-[2lh]: Aeonik Pro 28px/36.4px 400, #fafafa @ 0.8 |
| Transition | none | = |
| Painted layers | div.relative.w-full 592.0x333.0 bg #2d2d31 @ 0.4; img.size-10.shrink-0 40.0x40.0 bg #2d2d31 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 3.35544e+07px | div.relative.w-full 603.8x339.7 bg #2d2d31 @ 0.4; img.size-10.shrink-0 40.0x40.0 bg #2d2d31 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 3.35544e+07px |
| How | at rest | mouse hover |

Crops: `post-card-default.png`, `post-card-hover.png`.

#### post-headline

Post headline.

Page: blog. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 592 x 72.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Aeonik Pro 28px/36.4px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| How | at rest |

Crops: `post-headline-default.png`.

#### author-link

Author link.

Page: blog. Selector: `author name link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.09 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span.text-[12px].text-muted-foreground: -apple-system 12px/18px 400, #9f9fa9 | span.text-[12px].text-muted-foreground: -apple-system 12px/18px 400, #fafafa | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | img.size-10.shrink-0 40.0x40.0 bg #2d2d31 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 3.35544e+07px | = | a.inline-flex.w-fit 103.1x40.0 outline 1px auto #54545d @ 0.5 offset 1px; img.size-10.shrink-0 40.0x40.0 bg #2d2d31 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 3.35544e+07px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `author-link-default.png`, `author-link-hover.png`, `author-link-focus-visible.png`, `author-link-pressed.png`.

#### blog-search

Blog search button. Measured, never opened.

Page: blog. Selector: `button:has-text("Search articles")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 400 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #222224 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #2d2d31 @ 0.5 | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 0px | = |
| Font | -apple-system 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | = | = | = |
| Text node | span.min-w-0.flex-1: -apple-system 13px/19.5px 400, #9f9fa9 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9f9fa9 | = | = | = |
| Painted layers | button.flex.h-11 400.0x44.0 bg #2d2d31 @ 0.5 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px | button.flex.h-11 400.0x44.0 bg #2d2d31 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px | button.flex.h-11 400.0x44.0 bg #2d2d31 @ 0.5 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px outline 1px auto #54545d @ 0.5 offset 0px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px | button.flex.h-11 400.0x44.0 bg #2d2d31 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 8px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px; kbd.rounded.bg-muted 18.0x19.0 bg #2d2d31 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `blog-search-default.png`, `blog-search-hover.png`, `blog-search-focus-visible.png`, `blog-search-pressed.png`.

#### category-chip

Category link.

Page: blog. Selector: `a:has-text("Tutorials")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.11 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | p.text-[16px].font-semibold: -apple-system 16px/22px 600, #fafafa | p.text-[16px].font-semibold: -apple-system 16px/22px 600, #fafafa @ 0.8 | = | p.text-[16px].font-semibold: -apple-system 16px/22px 600, #fafafa @ 0.8 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.inline-block 66.1x22.0 outline 1px auto #54545d @ 0.5 offset 1px | = |

Crops: `category-chip-default.png`, `category-chip-hover.png`, `category-chip-focus-visible.png`, `category-chip-pressed.png`.

### Sign-in gate

#### signin-card

Sign-in card. The centred auth panel.

Page: signin. Selector: `form/card container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 896 x 687.5 |
| Padding | 0px |
| Gap | 24px |
| Border | 1px solid #222224 |
| Radius | 14px |
| Background | #1d1d21 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | h1.text-2xl.font-semibold: -apple-system 24px/32px 600, #fafafa, ls -0.6px |
| Transition | none |
| Icon | 16 x 16, colour #9f9fa9 |
| Painted layers | div.bg-card.text-card-foreground 896.0x687.5 bg #1d1d21 border T:1px solid #222224 / R:1px solid #222224 / B:1px solid #222224 / L:1px solid #222224 r 14px; button.inline-flex.items-center 279.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px; button.inline-flex.items-center 36.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px; button.inline-flex.items-center 36.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px; button.inline-flex.items-center 367.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px; span.w-full.border-t 367.0x1.0 border T:1px solid #222224 |
| How | at rest |

Crops: `signin-card-default.png`.

#### signin-title

Sign-in title.

Page: signin. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 367 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 24px/32px 600 |
| Letter spacing | -0.6px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `signin-title-default.png`.

#### oauth-button

OAuth button. "Login with GitHub": the wide identity-provider row. Measured, never pressed.

Page: signin. Selector: `button:has-text("Login with GitHub")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 279 x 36 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Text node | span.oauth-login-label-full: -apple-system 14px/20px 500, #9f9fa9 | span.oauth-login-label-full: -apple-system 14px/20px 500, #fafafa | = | span.oauth-login-label-full: -apple-system 14px/20px 500, #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9f9fa9 | 16 x 16, colour #fafafa | = | 16 x 16, colour #fafafa |
| Painted layers | button.inline-flex.items-center 279.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | button.inline-flex.items-center 279.0x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | button.inline-flex.items-center 279.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 279.0x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-button-default.png`, `oauth-button-hover.png`, `oauth-button-focus-visible.png`, `oauth-button-pressed.png`.

#### oauth-icon-button

OAuth icon button. The square GitLab/Bitbucket identity buttons. Measured, never pressed.

Page: signin. Selector: `button[aria-label="Login with GitLab"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | 278.97 x 36 | 279 x 36 | 279 x 36 |
| Padding | 8px 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Text node | span.oauth-login-label-full: -apple-system 14px/20px 500, #9f9fa9 | span.oauth-login-label-full: -apple-system 14px/20px 500, #fafafa | = | span.oauth-login-label-full: -apple-system 14px/20px 500, #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9f9fa9 | 16 x 16, colour #fafafa | = | 16 x 16, colour #fafafa |
| Painted layers | button.inline-flex.items-center 36.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | button.inline-flex.items-center 279.0x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | button.inline-flex.items-center 279.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 279.0x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-icon-button-default.png`, `oauth-icon-button-hover.png`, `oauth-icon-button-focus-visible.png`, `oauth-icon-button-pressed.png`.

#### google-button

Google button. Measured, never pressed.

Page: signin. Selector: `button:has-text("Sign in with Google")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 367 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9f9fa9, fill #000000 | 16 x 16, colour #fafafa, fill #000000 | = | 16 x 16, colour #fafafa, fill #000000 |
| Painted layers | button.inline-flex.items-center 367.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | button.inline-flex.items-center 367.0x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | button.inline-flex.items-center 367.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 367.0x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `google-button-default.png`, `google-button-hover.png`, `google-button-focus-visible.png`, `google-button-pressed.png`.

#### passkey-button

Passkey button. Measured, never pressed.

Page: signin. Selector: `button:has-text("passkey")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 367 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #2d2d31 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #2d2d31 | = | #2d2d31 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9f9fa9 | 16 x 16, colour #fafafa | = | 16 x 16, colour #fafafa |
| Painted layers | button.inline-flex.items-center 367.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | button.inline-flex.items-center 367.0x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | button.inline-flex.items-center 367.0x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.inline-flex.items-center 367.0x36.0 bg #2d2d31 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `passkey-button-default.png`, `passkey-button-hover.png`, `passkey-button-focus-visible.png`, `passkey-button-pressed.png`.

#### email-input

Email field. Focused with element.focus(). Nothing was typed and the form was never submitted.

Page: signin. Selector: `input[placeholder="Your email"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 367 x 36 | = |
| Padding | 4px 12px | = |
| Border | 1px solid #2d2d31 | 1px solid #54545d |
| Radius | 8px | = |
| Background | #2d2d31 @ 0.3 | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | -apple-system 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #9f9fa9, opacity 1 | = |
| Painted layers | input.file:text-foreground.placeholder:text-muted-foreground 367.0x36.0 bg #2d2d31 @ 0.3 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | input.file:text-foreground.placeholder:text-muted-foreground 367.0x36.0 bg #2d2d31 @ 0.3 border T:1px solid #54545d / R:1px solid #54545d / B:1px solid #54545d / L:1px solid #54545d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | element.focus(), nothing typed |

Crops: `email-input-default.png`, `email-input-focused.png`.

#### password-input

Password field. Focused only; nothing was typed.

Page: signin. Selector: `input[type="password"]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 367 x 36 | = |
| Padding | 4px 40px 4px 12px | = |
| Border | 1px solid #2d2d31 | 1px solid #54545d |
| Radius | 8px | = |
| Background | #2d2d31 @ 0.3 | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | -apple-system 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #9f9fa9, opacity 1 | = |
| Painted layers | input.file:text-foreground.placeholder:text-muted-foreground 367.0x36.0 bg #2d2d31 @ 0.3 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px | input.file:text-foreground.placeholder:text-muted-foreground 367.0x36.0 bg #2d2d31 @ 0.3 border T:1px solid #54545d / R:1px solid #54545d / B:1px solid #54545d / L:1px solid #54545d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | element.focus(), nothing typed |

Crops: `password-input-default.png`, `password-input-focused.png`.

#### show-password

Show-password toggle. The eye inside the password field.

Page: signin. Selector: `button[aria-label*="password" i]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #9f9fa9 | 16 x 16, colour #fafafa | = | 16 x 16, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.absolute.end-2 16.0x16.0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `show-password-default.png`, `show-password-hover.png`, `show-password-focus-visible.png`, `show-password-pressed.png`.

#### forgot-link

Forgot-password link.

Page: signin. Selector: `a:has-text("Forgot")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 367 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.984998 0.000024917 none / 0.85) | #fafafa | = | #fafafa |
| Transition | text-decoration-color, color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.link-neutral.text-sm 367.0x20.0 outline 1px auto #54545d @ 0.5 offset 1px | = |

Crops: `forgot-link-default.png`, `forgot-link-hover.png`, `forgot-link-focus-visible.png`, `forgot-link-pressed.png`.

#### login-button

Login button. The submit button; measured in every state except a real press — the form was never submitted.

Page: signin. Selector: `button:has-text("Login")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 367 x 36 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #54545d | = |
| Radius | 8px | = | = | = |
| Background | #fd366e | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 367.0x36.0 bg #fd366e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | button.inline-flex.items-center 367.0x36.0 bg #fd366e border T:1px solid #54545d / R:1px solid #54545d / B:1px solid #54545d / L:1px solid #54545d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `login-button-default.png`, `login-button-hover.png`, `login-button-focus-visible.png`, `login-button-pressed.png`.

#### tos-link

Legal link.

Page: signin. Selector: `a:has-text("Terms of Service")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.09 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | oklch(0.984998 0.000024917 none / 0.85) | #fafafa | = | #fafafa |
| Transition | text-decoration-color, color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.link-neutral 97.1x15.0 outline 1px auto #54545d @ 0.5 offset 1px | = |

Crops: `tos-link-default.png`, `tos-link-hover.png`, `tos-link-focus-visible.png`, `tos-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile top bar.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px 12px |
| Gap | 4px |
| Border | T: none; R: none; B: 1px solid #222224; L: none |
| Radius | 0px |
| Background | #19191c |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | a.inline-flex.items-center: -apple-system 13px/19.5px 500, #9f9fa9 |
| Transition | none |
| Icon | 16 x 16, colour #9f9fa9 |
| Painted layers | header.h-14.min-h-14 390.0x56.0 bg #19191c border B:1px solid #222224; span.absolute.-end-1.5 0.0x0.0 bg #fd366e r 3.35544e+07px; a.inline-flex.items-center 67.9x36.0 border T:1px solid #2d2d31 / R:1px solid #2d2d31 / B:1px solid #2d2d31 / L:1px solid #2d2d31 r 8px; a.inline-flex.items-center 72.6x36.0 bg #fd366e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `header button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 0px | = |
| Font | -apple-system 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #9f9fa9 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.h-9 36.0x36.0 r 8px outline 1px auto #54545d @ 0.5 offset 0px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The button after its own toggle; the open sheet (the data-state=open panel holding the nav links) shows in the crop.

Page: home. Selector: `header button`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #9f9fa9 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 16 x 16, colour #9f9fa9 |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

#### m-nav-link

Mobile nav link. A destination row inside the opened menu sheet.

Page: home. Selector: `open menu a:has-text("Pricing")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 283 x 40 |
| Padding | 0px 12px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 13px/19.5px 500 |
| Letter spacing | normal |
| Colour | #9f9fa9 |
| Text node | span.relative: -apple-system 13px/19.5px 500, #9f9fa9 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Ancestor paint | 2 up div.bg-background.data-[state=open]:animate-in bg #19191c shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| How | at rest |

Crops: `m-nav-link-default.png`.

#### m-cta-primary

Mobile primary CTA.

Page: home. Selector: `a:has-text("Start project")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132.94 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #54545d | = |
| Radius | 8px | = | = | = |
| Background | #fd366e | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | -apple-system 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 132.9x40.0 bg #fd366e border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | a.inline-flex.items-center 132.9x40.0 bg #fd366e border T:1px solid #54545d / R:1px solid #54545d / B:1px solid #54545d / L:1px solid #54545d r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #54545d @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-primary-default.png`, `m-cta-primary-hover.png`, `m-cta-primary-focus-visible.png`, `m-cta-primary-pressed.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 718.5 |
| Padding | 0px |
| Border | T: 1px solid #222224; R: none; B: none; L: none |
| Radius | 0px |
| Background | #19191c |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | h2.mb-4.text-[11px]: -apple-system 11px/16.5px 600, #9f9fa9, ls 0.55px |
| Transition | none |
| Icon | 0 x 0, colour #9f9fa9 |
| Painted layers | footer.@container/footer.w-full 1440.0x718.5 bg #19191c border T:1px solid #222224; div.border-b.last:border-b-0 0.0x0.0 border B:1px solid #222224; div.border-b.last:border-b-0 0.0x0.0 border B:1px solid #222224; div.border-b.last:border-b-0 0.0x0.0 border B:1px solid #222224; div.border-b.last:border-b-0 0.0x0.0 border B:1px solid #222224; div.border-b.last:border-b-0 0.0x0.0 border B:1px solid #222224 |
| Ancestor paint | 1 up main.@container.flex bg #19191c |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 27.14 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 13px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.link-unstyled.inline-flex 27.1x20.0 outline 1px auto #54545d @ 0.5 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `footer a[aria-label]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.03 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #54545d @ 0.5 offset 1px | = |
| Font | -apple-system 13px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9f9fa9 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.link-unstyled.inline-flex 57.0x20.0 outline 1px auto #54545d @ 0.5 offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

## Transitions declared in the readable stylesheets

appwrite.io's bundle is served cross-origin from cdn.appwrite.io, so this list holds only what the CSSOM could read on each page (inline styles and same-origin sheets); the per-state Transition rows above are computed values and cover the bundle's rules.

- home: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`
