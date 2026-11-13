# Component measurements

Computed styles read from endless.app (what endless.io redirects to) on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). The marketing pages, the free-tool pages, the model catalog, the radar trends, /docs and /brand were measured light; a small dark group repeats the home chrome under emulated prefers-color-scheme dark, the same trigger next-themes honours. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The sticky 56px marketing header: logo mark, flat nav links, Sign in and the Sign-up-for-free pill.

Page: home. Selector: `header.home-marketing-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0; L: none |
| Radius | 0px |
| Background | oklch(0.990998 0.0000251858 none / 0.9) |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.col-start-1.row-start-1: TikTok Sans 14px/20px 500, #0a0a0a |
| Transition | background-color, border-bottom-color 0.15s, 0.15s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1) delay 0s, 0s |
| Icon | 24 x 24, colour #0a0a0a |
| Painted layers | header.sticky.top-0 1440.0x56.0 bg oklch(0.990998 0.0000251858 none / 0.9) border B:1px #000000 @ 0; div.pointer-events-none.absolute 0.0x0.0 image linear-gradient(#fcfcfc 0%, #000000 @ 0 100%); button.group/button.inline-flex 80.1x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; button.group/button.inline-flex 138.9x32.0 bg #0a0a0a border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; button.group/button.inline-flex 0.0x0.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| Ancestor paint | 1 up div.flex.flex-col bg #fcfcfc |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Endless mark anchor.

Page: home. Selector: `header a:first`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 109.39 x 32 | = | = | = |
| Padding | 0px 8px 0px 4px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #01bcff offset 2px | = |
| Font | TikTok Sans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #0a0a0a | = | = | = |
| ::after | 113.391px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.relative.flex 109.4x32.0 r 8px outline 2px solid #01bcff offset 2px | = |

Crops: `logo-default.png`, `logo-hover.png`, `logo-focus-visible.png`, `logo-pressed.png`.

#### nav-industries

Nav link — Industries. The Industries header link (a plain link, not a dropdown trigger).

Page: home. Selector: `header a "Industries"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.77 x 32 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | #0a0a0a | = | #0a0a0a |
| Text node | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #6e6e6e | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #0a0a0a | = | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #6e6e6e, fill #000000 | 12 x 12, colour #0a0a0a, fill #000000 | = | 12 x 12, colour #0a0a0a, fill #000000 |
| ::after | 101.766px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.group/navigation-menu-trigger.w-max 101.8x32.0 bg #f5f5f5 r 8px | a.group/navigation-menu-trigger.w-max 101.8x32.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.group/navigation-menu-trigger.w-max 101.8x32.0 bg #f5f5f5 r 8px |

Crops: `nav-industries-default.png`, `nav-industries-hover.png`, `nav-industries-focus-visible.png`, `nav-industries-pressed.png`.

#### nav-link

Nav link. The plain Pricing header link.

Page: home. Selector: `header a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.91 x 32 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f5f5 | #f5f5f5 | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | #0a0a0a | = | #0a0a0a |
| Text node | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #6e6e6e | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #0a0a0a | = | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 65.9062px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.p-2.duration-hover 65.9x32.0 bg #f5f5f5 r 8px | a.p-2.duration-hover 65.9x32.0 bg #f5f5f5 r 8px | a.p-2.duration-hover 65.9x32.0 bg #f5f5f5 r 8px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signin

Sign-in button. The Sign-in control (goes to clerk.endless.app; measured, never followed).

Page: home. Selector: `"Sign in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.06 x 32 | = | = | 76.86 x 30.72 |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | #0a0a0a | = | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| ::before | 78.0625px x 42px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.group/button.inline-flex 80.1x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | = | button.group/button.inline-flex 80.1x32.0 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 76.9x30.7 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Sign-up CTA. The dark Sign-up-for-free pill (goes to s.endless.app; measured, never followed).

Page: home. Selector: `"Sign up for free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.86 x 32 | = | = | 133.3 x 30.72 |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 8px | = | = | = |
| Background | #0a0a0a | #0a0a0a @ 0.9 | = | #0a0a0a @ 0.9 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| ::before | 136.859px x 42px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.group/button.inline-flex 138.9x32.0 bg #0a0a0a border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 138.9x32.0 bg #0a0a0a @ 0.9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 138.9x32.0 bg #0a0a0a border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 133.3x30.7 bg #0a0a0a @ 0.9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Nav dropdown. No dropdown exists on the desktop header — recorded missing.

Page: home. Selector: `header dropdown panel`. States: .

Not found on the page at capture time.

#### menu-link

Menu link. No dropdown menu on the desktop header — recorded missing.

Page: home. Selector: `industries menu a`. States: .

Not found on the page at capture time.

### Home hero

#### hero-title

Hero headline. The home display headline.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 504.11 x 127.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 59.2px/63.936px 500 |
| Letter spacing | -1.8944px |
| Colour | #0a0a0a |
| Transition | none |
| Icon | 35.17 x 35.17, colour #0a0a0a, fill #000000 |
| Painted layers | div.rounded-xl.bg-surface-control 135.2x88.5 bg #f5f5f5 r 16px shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px; div.overflow-hidden.rounded-lg 126.4x79.7 r 12px shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px; div.home-sticker-frame.bg-surface-control 52.7x52.7 bg #f5f5f5 r calc(22.5% + 2.2px) shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px; div.flex.size-10 44.0x44.0 bg #ffffff r 22.5% shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px; div.home-sticker-frame.bg-surface-control 52.7x52.7 bg #f5f5f5 r calc(22.5% + 2.2px) shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px; span.relative.flex 44.0x44.0 bg #ffffff r 22.5% shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero copy. The lede under the headline.

Page: home. Selector: `p.home-intro`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 512 x 58.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 18px/29.25px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a @ 0.75 |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### composer

Prompt composer. The painted Ask-Endless prompt box (the hero's chat composer). Its send control is never pressed.

Page: home. Selector: `painted ancestor of the hero textarea`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 660 x 122 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.truncate.text-sm: TikTok Sans 14px/20px 500, #6e6e6e |
| Transition | none |
| Cursor | text |
| Icon | 16 x 16, colour #6e6e6e, fill #000000 |
| Painted layers | form.relative.overflow-hidden 660.0x122.0 bg #ffffff r 20px shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px; button.group/button.inline-flex 36.0x36.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px; button.group/button.inline-flex 145.6x36.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; button.group/button.inline-flex 36.0x36.0 bg #171717 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| Ancestor paint | 1 up div.rounded-3xl.bg-surface-control bg #f5f5f5 |
| How | at rest |

Crops: `composer-default.png`.

#### composer-input

Composer input. The "Ask Endless…" textarea; sample text was typed and deleted, nothing sent.

Page: home. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 660 x 72 | = | = |
| Padding | 16px 20px 4px 20px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | TikTok Sans 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #6e6e6e, opacity 1 | = | = |
| Ancestor paint | 2 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px | 2 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | 2 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "A launch post for the winter drop", then deleted; nothing sent |

Crops: `composer-input-default.png`, `composer-input-focused.png`, `composer-input-filled.png`.

#### composer-send

Composer send. The send/generate control inside the composer; measured, never pressed.

Page: home. Selector: `composer send button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 12px | = | = | = |
| Background | transparent | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | #0a0a0a | = | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #6e6e6e, fill #000000 | 16 x 16, colour #0a0a0a, fill #000000 | = | 16 x 16, colour #0a0a0a, fill #000000 |
| Painted layers | button.group/button.inline-flex 36.0x36.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | button.group/button.inline-flex 36.0x36.0 bg #f5f5f5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | button.group/button.inline-flex 36.0x36.0 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 36.0x36.0 bg #f5f5f5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| Ancestor paint | 3 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px | = | 3 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `composer-send-default.png`, `composer-send-hover.png`, `composer-send-focus-visible.png`, `composer-send-pressed.png`.

#### mode-pill

Model pill. The model-picker pill on the composer ("GPT-6.1 Terra" on this pass).

Page: home. Selector: `model picker button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145.59 x 36 | = | = | = |
| Padding | 0px 8px 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | #0a0a0a | = | #0a0a0a |
| Text node | span.truncate.text-sm: TikTok Sans 14px/20px 500, #6e6e6e | span.truncate.text-sm: TikTok Sans 14px/20px 500, #0a0a0a | = | span.truncate.text-sm: TikTok Sans 14px/20px 500, #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #6e6e6e | 16 x 16, colour #0a0a0a | = | 16 x 16, colour #0a0a0a |
| ::before | 143.594px x 42px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.group/button.inline-flex 145.6x36.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 145.6x36.0 bg #f5f5f5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 145.6x36.0 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 145.6x36.0 bg #f5f5f5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| Ancestor paint | 3 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px | = | 3 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mode-pill-default.png`, `mode-pill-hover.png`, `mode-pill-focus-visible.png`, `mode-pill-pressed.png`.

#### prompt-chip

Prompt chip. A suggestion chip under the composer; measured, never pressed.

Page: home. Selector: `prompt suggestion chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 156.05 x 36 | = | = | 149.8 x 34.56 |
| Padding | 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #e5e5e5 | = | 1px solid #01bcff | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #6e6e6e, fill #000000 | = | = | 15.36 x 15.36, colour #6e6e6e, fill #000000 |
| Painted layers | button.group/button.inline-flex 156.0x36.0 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px | button.group/button.inline-flex 156.0x36.0 bg #f5f5f5 border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px | button.group/button.inline-flex 156.0x36.0 bg #ffffff border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 149.8x34.6 bg #f5f5f5 border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `prompt-chip-default.png`, `prompt-chip-hover.png`, `prompt-chip-focus-visible.png`, `prompt-chip-pressed.png`.

### Home

#### h2-section

Section heading. A home section heading.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 36px/40px 500 |
| Letter spacing | -0.9px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `h2-section-default.png`.

### Pricing

#### pricing-h1

Pricing title. The pricing page heading.

Page: pricing. Selector: `h1 on /pricing`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 48px/60px 500 |
| Letter spacing | -1.2px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: none.

#### billing-toggle

Billing toggle. The Monthly/Annual billing segment; Annual was toggled for the screenshot state, never checked out.

Page: pricing. Selector: `button "Annual"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfc 0px 0px 0px 2px, #01bcff 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| ::after | 96px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Ancestor paint | 1 up div.relative.inline-flex bg #f5f5f5 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative.after:absolute 96.0x32.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfc 0px 0px 0px 2px, #01bcff 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: none.

#### plan-name

Plan name. A plan card's name.

Page: pricing. Selector: `plan name heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 225 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 18px/28px 600 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Ancestor paint | 2 up li.flex.flex-col bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 @ 0.6 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### plan-price

Plan price. A plan card's price figure.

Page: pricing. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 225 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.text-4xl.font-semibold: TikTok Sans 36px/40px 600, #0a0a0a, ls -0.9px |
| Transition | none |
| Ancestor paint | 1 up li.flex.flex-col bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 @ 0.6 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### plan-cta

Plan CTA. A plan card's action; measured never followed (sign-up goes to s.endless.app).

Page: pricing. Selector: `plan CTA button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 225 x 52 | = | = | 216 x 49.92 |
| Padding | 12px 28px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 12px | = | = | = |
| Background | #fcfcfc | #f5f5f5 | = | #f5f5f5 |
| Box shadow | #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 16px/26px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.group/button.inline-flex 225.0x52.0 bg #fcfcfc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px | button.group/button.inline-flex 225.0x52.0 bg #f5f5f5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px | button.group/button.inline-flex 225.0x52.0 bg #fcfcfc border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 216.0x49.9 bg #f5f5f5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px |
| Ancestor paint | 1 up li.flex.flex-col bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 @ 0.6 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### plan-card

Plan card. A pricing plan card (the painted ancestor of the plan name).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 273 x 612 |
| Padding | 24px |
| Gap | 28px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 @ 0.6 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | h2.text-lg.font-semibold: TikTok Sans 18px/28px 600, #0a0a0a |
| Transition | none |
| Icon | 16 x 16, colour #6e6e6e, fill #000000 |
| Painted layers | li.flex.flex-col 273.0x612.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 @ 0.6 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; button.group/button.inline-flex 225.0x52.0 bg #fcfcfc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px |
| How | at rest |

Crops: none.

#### credits-slider

Credits slider. The shared-credits range input on /pricing; focused only, never dragged.

Page: pricing. Selector: `input[type=range]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 18 x 18 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 1px auto #01bcff @ 0.5 offset 0px |
| Font | TikTok Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | none | = |
| Cursor | default | = |
| Placeholder | #0a0a0a, opacity 1 | = |
| Ancestor paint | 1 up div.relative.block bg #fcfcfc shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | 1 up div.relative.block bg #fcfcfc shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfc 0px 0px 0px 2px, #01bcff 0px 0px 0px 4px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px |
| How | at rest | clicked into the field |
| Painted layers | - | input 18.0x18.0 outline 1px auto #01bcff @ 0.5 offset 0px |

Crops: none.

#### faq-item

FAQ row. A pricing FAQ accordion row; measured closed, never opened.

Page: pricing. Selector: `faq row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1152 x 64 | = | = | = |
| Padding | 20px 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #01bcff offset 2px | = |
| Font | TikTok Sans 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Text node | h3: TikTok Sans 16px/24px 500, #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #6e6e6e, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | summary.flex.w-full 1152.0x64.0 r 8px outline 2px solid #01bcff offset 2px | = |

Crops: none.

### Contact form

#### contact-form

Contact form. The contact/sales form (an unpainted 640px column; the fields paint their own fills); never submitted.

Page: contact. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 436 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | label.text-sm.font-medium: TikTok Sans 14px/20px 500, #0a0a0a |
| Transition | none |
| Painted layers | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; textarea.flex.field-sizing-content 640.0x64.0 bg #e5e5e5 @ 0.5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; button.group/button.inline-flex 640.0x52.0 bg #0a0a0a border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| How | at rest |

Crops: `contact-form-default.png`.

#### field-name

Name field. A text input on the contact form; sample text typed and deleted, nothing sent.

Page: contact. Selector: `input[type=text]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 640 x 40 | = | = |
| Padding | 4px 12px | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #01bcff | 1px solid #01bcff |
| Radius | 8px | = | = |
| Background | #e5e5e5 @ 0.5 | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | TikTok Sans 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #0a0a0a, opacity 1 | = | = |
| Painted layers | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "Ada Lovelace", then deleted; nothing sent |

Crops: `field-name-default.png`, `field-name-focused.png`, `field-name-filled.png`.

#### field-email

Email field. The email input; sample text typed and deleted, nothing sent.

Page: contact. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 640 x 40 | = | = |
| Padding | 4px 12px | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #01bcff | 1px solid #01bcff |
| Radius | 8px | = | = |
| Background | #e5e5e5 @ 0.5 | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | TikTok Sans 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #0a0a0a, opacity 1 | = | = |
| Painted layers | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `field-email-default.png`, `field-email-focused.png`, `field-email-filled.png`.

#### field-company

Company field. The company/domain input ("acme.com" placeholder); focused only.

Page: contact. Selector: `input[placeholder*=acme]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 640 x 40 | = |
| Padding | 4px 12px | = |
| Border | 1px solid #000000 @ 0 | 1px solid #01bcff |
| Radius | 8px | = |
| Background | #e5e5e5 @ 0.5 | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | TikTok Sans 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #6e6e6e, opacity 1 | = |
| Painted layers | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | input.w-full.min-w-0 640.0x40.0 bg #e5e5e5 @ 0.5 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: `field-company-default.png`, `field-company-focused.png`.

#### field-message

Message field. The message textarea; focused only, nothing typed.

Page: contact. Selector: `contact textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 640 x 64 | = |
| Padding | 12px | = |
| Border | 1px solid #000000 @ 0 | 1px solid #01bcff |
| Radius | 8px | = |
| Background | #e5e5e5 @ 0.5 | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = |
| Font | TikTok Sans 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #0a0a0a | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #0a0a0a, opacity 1 | = |
| Painted layers | textarea.flex.field-sizing-content 640.0x64.0 bg #e5e5e5 @ 0.5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | textarea.flex.field-sizing-content 640.0x64.0 bg #e5e5e5 @ 0.5 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: `field-message-default.png`, `field-message-focused.png`.

#### send-btn

Send button. The Send-message submit; measured, never pressed.

Page: contact. Selector: `button "Send message"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 640 x 52 | = | = | 614.4 x 49.92 |
| Padding | 12px 28px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 12px | = | = | = |
| Background | #0a0a0a | #0a0a0a @ 0.9 | = | #0a0a0a @ 0.9 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 16px/26px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.group/button.inline-flex 640.0x52.0 bg #0a0a0a border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | button.group/button.inline-flex 640.0x52.0 bg #0a0a0a @ 0.9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | button.group/button.inline-flex 640.0x52.0 bg #0a0a0a border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 614.4x49.9 bg #0a0a0a @ 0.9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `send-btn-default.png`, `send-btn-hover.png`, `send-btn-focus-visible.png`, `send-btn-pressed.png`.

### AI image generator (free tool)

#### tool-title

Tool title. The free-tool page heading (AI image generator).

Page: toolgen. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 392.23 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 48px/60px 500 |
| Letter spacing | -2.4px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `tool-title-default.png`.

#### tool-panel

Tool panel. The prompt panel of the free tool; Generate is never pressed.

Page: toolgen. Selector: `tool panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 504 x 114 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | button.group/button.inline-flex: TikTok Sans 14px/21px 500, #fcfcfc |
| Transition | none |
| Icon | 16 x 16, colour #fcfcfc, fill #000000 |
| Painted layers | form.relative.overflow-hidden 504.0x114.0 bg #ffffff r 20px shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px; button.group/button.inline-flex 177.5x36.0 bg #0a0a0a border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| Ancestor paint | 1 up div.rounded-3xl.bg-surface-control bg #f5f5f5 shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px |
| How | at rest |

Crops: `tool-panel-default.png`.

#### tool-prompt

Prompt field. The tool's prompt input ("e.g. a fox reading a map…" placeholder); sample text typed and deleted, nothing generated.

Page: toolgen. Selector: `tool prompt input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 504 x 64 | = | = |
| Padding | 16px 20px 24px 20px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | TikTok Sans 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #6e6e6e, opacity 1 | = | = |
| Ancestor paint | 1 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px; 2 up div.rounded-3xl.bg-surface-control bg #f5f5f5 shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px | 1 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; 2 up div.rounded-3xl.bg-surface-control bg #f5f5f5 shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px | 1 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; 2 up div.rounded-3xl.bg-surface-control bg #f5f5f5 shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px |
| How | at rest | clicked into the field | typed "a fox reading a map in a snowy forest", then deleted; nothing sent |

Crops: `tool-prompt-default.png`, `tool-prompt-focused.png`, `tool-prompt-filled.png`.

#### tool-generate

Generate button. The Generate-the-image submit; measured, never pressed.

Page: toolgen. Selector: `button "Generate the image"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 177.55 x 36 | = | = | 170.44 x 34.56 |
| Padding | 0px 12px 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 12px | = | = | = |
| Background | #0a0a0a | #0a0a0a @ 0.9 | = | #0a0a0a @ 0.9 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/21px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #fcfcfc, fill #000000 | = | = | 15.36 x 15.36, colour #fcfcfc, fill #000000 |
| Painted layers | button.group/button.inline-flex 177.5x36.0 bg #0a0a0a border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | button.group/button.inline-flex 177.5x36.0 bg #0a0a0a @ 0.9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | button.group/button.inline-flex 177.5x36.0 bg #0a0a0a border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 170.4x34.6 bg #0a0a0a @ 0.9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| Ancestor paint | 2 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px; 3 up div.rounded-3xl.bg-surface-control bg #f5f5f5 shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px | = | 2 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; 3 up div.rounded-3xl.bg-surface-control bg #f5f5f5 shadow #000000 @ 0.05 0px 1px 2px 0px, #000000 @ 0.15 0px 8px 24px -12px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tool-generate-default.png`, `tool-generate-hover.png`, `tool-generate-focus-visible.png`, `tool-generate-pressed.png`.

#### tool-step

How-it-works heading. A how-it-works heading on the tool page.

Page: toolgen. Selector: `tool h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 36px/40px 500 |
| Letter spacing | -0.9px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `tool-step-default.png`.

### Model catalog

#### models-title

Models title. The model catalog heading.

Page: models. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 636.8 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 48px/60px 500 |
| Letter spacing | -2.4px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `models-title-default.png`.

#### models-search

Search field. The catalog search input; sample text typed and deleted.

Page: models. Selector: `input[type=search]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 256 x 32 | = | = |
| Padding | 4px 32px | = | = |
| Border | 1px solid #e5e5e5 | 1px solid #01bcff | 1px solid #01bcff |
| Radius | 12px | = | = |
| Background | #fcfcfc | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | TikTok Sans 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0a0a0a | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #6e6e6e, opacity 1 | = | = |
| Painted layers | input.w-full.min-w-0 256.0x32.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px | input.w-full.min-w-0 256.0x32.0 bg #fcfcfc border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | input.w-full.min-w-0 256.0x32.0 bg #fcfcfc border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field | typed "image", then deleted; nothing sent |

Crops: `models-search-default.png`, `models-search-focused.png`, `models-search-filled.png`.

#### mode-tab

Modality tab. A modality filter pill ("All · 65", "Chat · 21", …); measured, never toggled.

Page: models. Selector: `modality filter pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.23 x 32 | = | = | 71.27 x 30.72 |
| Padding | 6px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #0a0a0a | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 74.2344px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.inline-block.relative 74.2x32.0 bg #0a0a0a r 3.35544e+07px | = | a.inline-block.relative 74.2x32.0 bg #0a0a0a r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-block.relative 71.3x30.7 bg #0a0a0a r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mode-tab-default.png`, `mode-tab-hover.png`, `mode-tab-focus-visible.png`, `mode-tab-pressed.png`.

#### model-card

Model card. A model tile in the catalog grid (the anchor is the card; 354x200, rounded 20px); measured, never followed.

Page: models. Selector: `a[href*=/models/] with a heading`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 354.66 x 200 | = | = | = |
| Padding | 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | #f5f5f5 @ 0.5 | = | #f5f5f5 @ 0.5 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 2px solid #01bcff offset 2px | = |
| Font | TikTok Sans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Text node | h3.text-lg.font-medium: TikTok Sans 18px/28px 500, #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #0a0a0a | = | = | = |
| Painted layers | a.group.flex 354.7x200.0 r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | a.group.flex 354.7x200.0 bg #f5f5f5 @ 0.5 r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | a.group.flex 354.7x200.0 r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #01bcff offset 2px | a.group.flex 354.7x200.0 bg #f5f5f5 @ 0.5 r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `model-card-default.png`, `model-card-hover.png`, `model-card-focus-visible.png`, `model-card-pressed.png`.

#### model-link

Model link. A model name link in the catalog; measured, never followed.

Page: models. Selector: `a[href*=/models/]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.81 x 32 | = | = | 83.34 x 30.72 |
| Padding | 6px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #f5f5f5 | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | #0a0a0a | = | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 86.8125px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a.inline-block.relative 86.8x32.0 bg #f5f5f5 r 3.35544e+07px | = | a.inline-block.relative 86.8x32.0 bg #f5f5f5 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.inline-block.relative 83.3x30.7 bg #f5f5f5 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `model-link-default.png`, `model-link-hover.png`, `model-link-focus-visible.png`, `model-link-pressed.png`.

### Radar trends

#### radar-title

Radar title. The social radar heading.

Page: radar. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 512 x 180 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 48px/60px 500 |
| Letter spacing | -2.4px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `radar-title-default.png`.

#### radar-search

Radar search. No search input exists on /radar — recorded missing.

Page: radar. Selector: `radar search input`. States: .

Not found on the page at capture time.

#### radar-row

Trend row. A trend row in the live radar list (a link to a trend detail page); measured, never followed.

Page: radar. Selector: `main a[href*=/radar/] trend link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 184.81 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #01bcff offset 4px | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #0a0a0a, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.mt-8.inline-flex 184.8x44.0 r 8px outline 2px solid #01bcff offset 4px | = |

Crops: `radar-row-default.png`, `radar-row-hover.png`, `radar-row-focus-visible.png`, `radar-row-pressed.png`.

#### radar-copy

Copy button. A trend Copy button; measured, never pressed.

Page: radar. Selector: `button "Copy"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.06 x 32 | = | = | 70.14 x 30.72 |
| Padding | 0px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 8px | = | = | = |
| Background | #171717 | #171717 @ 0.8 | = | #171717 @ 0.8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #fafafa, fill #000000 | = | = | 15.36 x 15.36, colour #fafafa, fill #000000 |
| ::before | 71.0625px x 42px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.group/button.inline-flex 73.1x32.0 bg #171717 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 73.1x32.0 bg #171717 @ 0.8 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 73.1x32.0 bg #171717 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 70.1x30.7 bg #171717 @ 0.8 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| Ancestor paint | 1 up div.flex.items-center bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `radar-copy-default.png`, `radar-copy-hover.png`, `radar-copy-focus-visible.png`, `radar-copy-pressed.png`.

#### radar-why

Why link. A trend's Find-out-why action; measured, never followed.

Page: radar. Selector: `"Find out why"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87.94 x 32 | = | = | 84.42 x 30.72 |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | #0a0a0a | = | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | button.group/button.inline-flex 87.9x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | = | button.group/button.inline-flex 87.9x32.0 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 84.4x30.7 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `radar-why-default.png`, `radar-why-hover.png`, `radar-why-focus-visible.png`, `radar-why-pressed.png`.

### Brand kit

#### brand-title

Brand title. The brand-kit heading.

Page: brand. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 48px/60px 500 |
| Letter spacing | -1.2px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: none.

#### brand-logo-block

Logo block. A logo asset card on the brand page (a rounded-2xl bg-card tile with On-light/On-dark variants and SVG/PNG download links).

Page: brand. Selector: `main .bg-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 436 x 208 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.truncate.text-xs: TikTok Sans 12px/16px 500, #6e6e6e |
| Transition | none |
| Icon | 44 x 44, colour #0a0a0a |
| Painted layers | div.overflow-hidden.rounded-2xl 436.0x208.0 bg #ffffff r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; div.flex.items-center 436.0x160.0 bg #ffffff border B:1px #e5e5e5; button.group/button.inline-flex 32.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; a.group/button.inline-flex 107.2x24.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; a.group/button.inline-flex 108.2x24.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| How | at rest |

Crops: none.

#### brand-swatch

Colour swatch. A brand colour swatch tile in the Colors section (285x174; the page names #0A0A0A, #FAFAFA, #01BCFF).

Page: brand. Selector: `main .swatch`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 285.33 x 174 |
| Padding | 0px |
| Border | none |
| Radius | 20px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | span.font-medium: TikTok Sans 16px/24px 500, #0a0a0a |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default |
| Icon | 285.33 x 95, colour #0a0a0a, fill #000000 |
| Painted layers | button.group/swatch.block 285.3x174.0 bg #ffffff r 20px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; span.relative.block 285.3x96.0 border B:1px #e5e5e5 |
| How | at rest |

Crops: none.

#### brand-btn

Asset button. An asset Download link; measured, never pressed.

Page: brand. Selector: `brand asset download link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180.45 x 40 | = | = | 173.23 x 38.4 |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 12px | = | = | = |
| Background | #171717 | #171717 @ 0.8 | = | #171717 @ 0.8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa, fill #000000 | = | = | 15.36 x 15.36, colour #fafafa, fill #000000 |
| Painted layers | a.group/button.inline-flex 180.5x40.0 bg #171717 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | a.group/button.inline-flex 180.5x40.0 bg #171717 @ 0.8 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px | a.group/button.inline-flex 180.5x40.0 bg #171717 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 173.2x38.4 bg #171717 @ 0.8 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Blog

#### blog-title

Blog title. The blog index heading.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 48px/60px 500 |
| Letter spacing | -1.2px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: none.

#### blog-pill

Category pill. A blog category filter pill; measured, never toggled.

Page: blog. Selector: `category pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.98 x 32 | = | = | 43.18 x 30.72 |
| Padding | 6px 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #0a0a0a | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fcfcfc | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| ::after | 44.9844px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.relative.after:absolute 45.0x32.0 bg #0a0a0a r 3.35544e+07px | = | button.relative.after:absolute 45.0x32.0 bg #0a0a0a r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.relative.after:absolute 43.2x30.7 bg #0a0a0a r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### blog-card

Post card. A post card in the blog index; measured, never followed.

Page: blog. Selector: `post card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 269.33 x 347.88 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #e5e5e5 @ 0.6 | 1px solid #e5e5e5 | 1px solid #e5e5e5 | 1px solid #e5e5e5 |
| Radius | 16px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Text node | span.text-2xs.font-medium: TikTok Sans 11px/16px 500, #6e6e6e, ls 0.275px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.flex 269.3x347.9 bg #ffffff border T:1px #e5e5e5 @ 0.6 / R:1px #e5e5e5 @ 0.6 / B:1px #e5e5e5 @ 0.6 / L:1px #e5e5e5 @ 0.6 r 16px; div.relative.aspect-video 267.3x150.4 bg #f5f5f5 outline 1px solid #000000 @ 0.1 offset -1px | a.group.flex 269.3x347.9 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 16px; div.relative.aspect-video 267.3x150.4 bg #f5f5f5 outline 1px solid #000000 @ 0.1 offset -1px | a.group.flex 269.3x347.9 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; div.relative.aspect-video 267.3x150.4 bg #f5f5f5 outline 1px solid #000000 @ 0.1 offset -1px | a.group.flex 269.3x347.9 bg #ffffff border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 16px; div.relative.aspect-video 267.3x150.4 bg #f5f5f5 outline 1px solid #000000 @ 0.1 offset -1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Docs shell

#### docs-sidebar

Docs sidebar. The docs navigation sidebar — a separate shell from the marketing pages.

Page: docs. Selector: `docs aside`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 268 x 900 |
| Padding | 0px |
| Border | T: none; R: 1px solid #e5e5e5; B: none; L: none |
| Radius | 0px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | button.inline-flex.items-center: TikTok Sans 14px/20px 400, #555555 |
| Transition | all 0.25s ease |
| Icon | 24 x 24, colour #0a0a0a |
| Painted layers | aside.absolute.flex 268.0x900.0 bg #fcfcfc border R:1px #e5e5e5; button.inline-flex.items-center 236.0x36.0 bg #f0f0f0 @ 0.5 border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px; a.flex.items-center 236.0x36.0 bg #f0f0f0 r 12px; hr.mt-2.border-t 236.0x1.0 border T:1px #e7e7e7 |
| How | at rest |

Crops: none.

#### docs-nav-item

Docs nav item. A sidebar section button in the docs shell; measured, never toggled.

Page: docs. Selector: `docs nav item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 236 x 36 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #f0f0f0 @ 0.5 | = | #f0f0f0 @ 0.5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #01bcff @ 0.5 offset 0px | = |
| Font | TikTok Sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #181818 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #181818 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.relative.flex 236.0x36.0 bg #f0f0f0 @ 0.5 r 12px | button.relative.flex 236.0x36.0 r 12px outline 1px auto #01bcff @ 0.5 offset 0px | button.relative.flex 236.0x36.0 bg #f0f0f0 @ 0.5 r 12px |

Crops: none.

#### docs-search

Search button. The docs Search (⌘K) button; measured, never opened.

Page: docs. Selector: `docs search button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 236 x 36 | = | = | = |
| Padding | 6px 6px 6px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e5e5e5 | = | = | = |
| Radius | 12px | = | = | = |
| Background | #f0f0f0 @ 0.5 | #f0f0f0 | = | #f0f0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #01bcff @ 0.5 offset 0px | = |
| Font | TikTok Sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #555555 | #181818 | = | #181818 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #555555 | 16 x 16, colour #181818 | = | 16 x 16, colour #181818 |
| Painted layers | button.inline-flex.items-center 236.0x36.0 bg #f0f0f0 @ 0.5 border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px | button.inline-flex.items-center 236.0x36.0 bg #f0f0f0 border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px | button.inline-flex.items-center 236.0x36.0 bg #f0f0f0 @ 0.5 border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px outline 1px auto #01bcff @ 0.5 offset 0px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px | button.inline-flex.items-center 236.0x36.0 bg #f0f0f0 border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 12px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px; kbd.rounded-md.border 22.4x22.0 bg #fcfcfc border T:1px #e5e5e5 / R:1px #e5e5e5 / B:1px #e5e5e5 / L:1px #e5e5e5 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### docs-h1

Docs heading. The docs page heading in the docs typeset.

Page: docs. Selector: `docs h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 836 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 28px/42px 600 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: none.

### MCP page

#### mcp-title

MCP title. The MCP page heading.

Page: mcp. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 768 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 48px/60px 500 |
| Letter spacing | -1.2px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: none.

#### mcp-code

Code block. An install/config code block (monospace surface).

Page: mcp. Selector: `pre code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 470.94 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist Mono 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Ancestor paint | 1 up div.flex.items-center bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: none.

#### mcp-copy

Copy button. A code Copy button; measured, never pressed.

Page: mcp. Selector: `button "Copy"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.06 x 32 | = | = | 70.14 x 30.72 |
| Padding | 0px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 8px | = | = | = |
| Background | #171717 | #171717 @ 0.8 | = | #171717 @ 0.8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #fafafa, fill #000000 | = | = | 15.36 x 15.36, colour #fafafa, fill #000000 |
| ::before | 71.0625px x 42px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.group/button.inline-flex 73.1x32.0 bg #171717 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 73.1x32.0 bg #171717 @ 0.8 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 73.1x32.0 bg #171717 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 70.1x30.7 bg #171717 @ 0.8 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| Ancestor paint | 1 up div.flex.items-center bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #e5e5e5 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

### Footer

#### footer

Footer. The marketing footer: link columns, legal, the Cookie-settings and Theme controls.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1452.36 |
| Padding | 0px |
| Border | T: 1px solid #e5e5e5 @ 0.6; R: none; B: none; L: none |
| Radius | 0px |
| Background | #fcfcfc |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | p.text-sm.text-muted-foreground: TikTok Sans 14px/20px 400, #6e6e6e |
| Transition | none |
| Icon | 16 x 16, colour #6e6e6e |
| Painted layers | footer.w-full.border-t 1440.0x1452.4 bg #fcfcfc border T:1px #e5e5e5 @ 0.6; div.flex.flex-wrap 1088.0x69.0 border B:1px #e5e5e5 @ 0.6; a.relative.flex 36.0x36.0 border T:1px #e5e5e5 @ 0.7 / R:1px #e5e5e5 @ 0.7 / B:1px #e5e5e5 @ 0.7 / L:1px #e5e5e5 @ 0.7 r 12px; a.relative.flex 36.0x36.0 border T:1px #e5e5e5 @ 0.7 / R:1px #e5e5e5 @ 0.7 / B:1px #e5e5e5 @ 0.7 / L:1px #e5e5e5 @ 0.7 r 12px; a.relative.flex 36.0x36.0 border T:1px #e5e5e5 @ 0.7 / R:1px #e5e5e5 @ 0.7 / B:1px #e5e5e5 @ 0.7 / L:1px #e5e5e5 @ 0.7 r 12px; a.relative.flex 36.0x36.0 border T:1px #e5e5e5 @ 0.7 / R:1px #e5e5e5 @ 0.7 / B:1px #e5e5e5 @ 0.7 / L:1px #e5e5e5 @ 0.7 r 12px |
| Ancestor paint | 1 up div.flex.flex-col bg #fcfcfc |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44.55 x 24 | = | = | = |
| Padding | 2px 0px | = | = | = |
| Gap | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #01bcff offset 2px | = |
| Font | TikTok Sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a @ 0.8 | #0a0a0a | #0a0a0a | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.inline-flex.items-center 44.5x24.0 r 4px outline 2px solid #01bcff offset 2px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### theme-toggle

Theme toggle. The footer Theme icon control ("Theme: system. Switch to light"; writes the .dark class the system scheme also drives); measured, never pressed.

Page: home. Selector: `footer theme icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 30.72 x 30.72 |
| Padding | 0px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e6e6e | #0a0a0a | = | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #6e6e6e, fill #000000 | 16 x 16, colour #0a0a0a, fill #000000 | = | 15.36 x 15.36, colour #0a0a0a, fill #000000 |
| ::before | 38px x 38px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.group/button.inline-flex 32.0x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 32.0x32.0 bg #f5f5f5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 32.0x32.0 border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 30.7x30.7 bg #f5f5f5 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `theme-toggle-default.png`, `theme-toggle-hover.png`, `theme-toggle-focus-visible.png`, `theme-toggle-pressed.png`.

#### cookie-btn

Cookie settings button. The footer Cookie-settings button; measured, never pressed (a consent surface).

Page: home. Selector: `"Cookie settings"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102.64 x 24 | = | = | = |
| Padding | 2px 0px | = | = | = |
| Gap | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a @ 0.8 | #0a0a0a | #0a0a0a | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.inline-flex.items-center 102.6x24.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `cookie-btn-default.png`, `cookie-btn-hover.png`, `cookie-btn-focus-visible.png`, `cookie-btn-pressed.png`.

### Dark theme (system dark)

#### d-header

Header (dark). The sticky header painted by the dark token scope.

Page: home. Selector: `header under .dark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0; L: none |
| Radius | 0px |
| Background | oklch(0 0 none / 0.9) |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.col-start-1.row-start-1: TikTok Sans 14px/20px 500, #fafafa |
| Transition | background-color, border-bottom-color 0.15s, 0.15s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1) delay 0s, 0s |
| Icon | 24 x 24, colour #fafafa |
| Painted layers | header.sticky.top-0 1440.0x56.0 bg oklch(0 0 none / 0.9) border B:1px #000000 @ 0; div.pointer-events-none.absolute 0.0x0.0 image linear-gradient(#000000 0%, #000000 @ 0 100%); button.group/button.inline-flex 80.1x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; button.group/button.inline-flex 138.9x32.0 bg #fafafa border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; button.group/button.inline-flex 0.0x0.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| Ancestor paint | 1 up div.flex.flex-col bg #000000 |
| How | at rest |

Crops: none.

#### d-nav-cta

Sign-up CTA (dark). The sign-up pill under .dark.

Page: home. Selector: `"Sign up for free" under .dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.86 x 32 | = | = | 133.3 x 30.72 |
| Padding | 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #01bcff | = |
| Radius | 8px | = | = | = |
| Background | #fafafa | #fafafa @ 0.9 | = | #fafafa @ 0.9 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| ::before | 136.859px x 42px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.group/button.inline-flex 138.9x32.0 bg #fafafa border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 138.9x32.0 bg #fafafa @ 0.9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px | button.group/button.inline-flex 138.9x32.0 bg #fafafa border T:1px #01bcff / R:1px #01bcff / B:1px #01bcff / L:1px #01bcff r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.3 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 133.3x30.7 bg #fafafa @ 0.9 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: none.

#### d-hero-title

Hero headline (dark). The display headline under .dark.

Page: home. Selector: `h1 under .dark`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 504.11 x 127.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 59.2px/63.936px 500 |
| Letter spacing | -1.8944px |
| Colour | #fafafa |
| Transition | none |
| Icon | 35.17 x 35.17, colour #fafafa, fill #000000 |
| Painted layers | div.home-sticker-frame.bg-surface-control 52.8x52.8 bg #171717 r calc(22.5% + 2.2px) shadow #ffffff @ 0.08 0px 0px 0px 1px, #000000 @ 0.6 0px 8px 24px -12px; div.flex.size-10 44.0x44.0 bg #ffffff r 22.5% shadow #ffffff @ 0.08 0px 0px 0px 1px; div.rounded-xl.bg-surface-control 93.5x112.5 bg #171717 r 16px shadow #ffffff @ 0.08 0px 0px 0px 1px, #000000 @ 0.6 0px 8px 24px -12px; div.overflow-hidden.rounded-lg 85.1x104.0 r 12px shadow #ffffff @ 0.08 0px 0px 0px 1px; div.home-sticker-frame.bg-surface-control 56.9x56.9 bg #171717 r calc(22.5% + 2.2px) shadow #ffffff @ 0.08 0px 0px 0px 1px, #000000 @ 0.6 0px 8px 24px -12px; span.relative.flex 47.4x47.4 r 22.5% shadow #ffffff @ 0.08 0px 0px 0px 1px |
| How | at rest |

Crops: none.

#### d-composer-input

Composer input (dark). The Ask-Endless textarea under .dark; focused, nothing typed or sent.

Page: home. Selector: `textarea under .dark`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 660 x 72 | = |
| Padding | 16px 20px 4px 20px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | TikTok Sans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #a1a1a1, opacity 1 | = |
| Ancestor paint | 2 up form.relative.overflow-hidden bg #000000 shadow #ffffff @ 0.08 0px 0px 0px 1px | 2 up form.relative.overflow-hidden bg #000000 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #01bcff @ 0.4 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | clicked into the field |

Crops: none.

#### d-nav-link

Nav link (dark). A header link under .dark.

Page: home. Selector: `header a "Pricing" under .dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.91 x 32 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #262626 @ 0.5 | #262626 | #262626 @ 0.5 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | TikTok Sans 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a1a1a1 | #fafafa | = | #fafafa |
| Text node | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #a1a1a1 | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #fafafa | = | span.col-start-1.row-start-1: TikTok Sans 14px/20px 400, #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 65.9062px x 40px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.p-2.duration-hover 65.9x32.0 bg #262626 @ 0.5 r 8px | a.p-2.duration-hover 65.9x32.0 bg #262626 r 8px | a.p-2.duration-hover 65.9x32.0 bg #262626 @ 0.5 r 8px |

Crops: none.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0; L: none |
| Radius | 0px |
| Background | oklch(0.990998 0.0000251858 none / 0.9) |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | button.group/button.inline-flex: TikTok Sans 14px/20px 600, #6e6e6e |
| Transition | background-color, border-bottom-color 0.15s, 0.15s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1) delay 0s, 0s |
| Icon | 24 x 24, colour #0a0a0a |
| Painted layers | header.sticky.top-0 390.0x56.0 bg oklch(0.990998 0.0000251858 none / 0.9) border B:1px #000000 @ 0; div.pointer-events-none.absolute 0.0x0.0 image linear-gradient(#fcfcfc 0%, #000000 @ 0 100%); button.group/button.inline-flex 64.1x32.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; button.group/button.inline-flex 122.9x32.0 bg #0a0a0a border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 8px; button.group/button.inline-flex 36.0x36.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| Ancestor paint | 1 up div.flex.flex-col bg #fcfcfc |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The header menu toggle.

Page: mobile. Selector: `header menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 0px |
| Border | 1px solid #000000 @ 0 |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 14px/20px 500 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | default |
| Icon | 20 x 20, colour #0a0a0a, fill #000000 |
| ::before | 42px x 42px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | button.group/button.inline-flex 36.0x36.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 12px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The header menu panel opened by its own toggle.

Page: mobile. Selector: `mobile menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 904 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Text node | a.flex.min-h-11: TikTok Sans 16px/24px 500, #0a0a0a |
| Transition | none |
| Icon | 16 x 16, colour #6e6e6e, fill #000000 |
| Painted layers | div.bg-overlay/30.supports-backdrop-filter:backdrop-blur-sm 390.0x904.0 bg #000000 @ 0.3; div.mx-auto.box-border 390.0x436.0 bg #ffffff r 20px 20px 0px 0px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; div.rounded-t-2xl.bg-inherit 390.0x736.0 bg #ffffff r 20px 20px 0px 0px; div.relative.mx-auto 40.0x4.0 bg #6e6e6e @ 0.3 r 3.35544e+07px |
| Ancestor paint | 1 up body.font-sans bg #fcfcfc |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened header menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 374 x 44 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #01bcff offset -2px | = |
| Font | TikTok Sans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.flex.min-h-11 374.0x44.0 r 8px outline 2px solid #01bcff offset -2px | = |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 81.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 37.6px/40.608px 500 |
| Letter spacing | -1.2032px |
| Colour | #0a0a0a |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-composer

Mobile composer.

Page: mobile. Selector: `textarea at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 346 x 72 |
| Padding | 16px 20px 4px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | TikTok Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0a0a0a |
| Transition | none |
| Cursor | text |
| Placeholder | #6e6e6e, opacity 1 |
| Ancestor paint | 2 up form.relative.overflow-hidden bg #ffffff shadow #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 2px -1px, #000000 @ 0.04 0px 2px 4px 0px |
| How | at rest |

Crops: `m-composer-default.png`.

## Transitions declared in the readable stylesheets

endless.app serves its Next.js chunks same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- blog: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`

- brand: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`

- contact: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`

- docs: `background-color 0.3s`, `transform 0.3s`, `opacity 0.2s`, `--fd-sidebar-col 0.15s, --fd-ai-chat-col 0.3s ease-in-out`, `filter 0.2s`, `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`

- home: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`, `opacity 0.2s ease-out`, `background-color 0.15s ease-out, transform 0.15s ease-out`, `opacity 0.25s ease-out`

- mcp: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`

- models: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`

- pricing: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`

- radar: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`, `opacity 0.2s ease-out`, `background-color 0.15s ease-out, transform 0.15s ease-out`, `opacity 0.25s ease-out`

- toolgen: `transform .22s var(--ease-pop), opacity .22s var(--ease-pop), height .22s var(--ease-pop), box-shadow .15s ease-out`, `none`, `background-color var(--transition-duration-hover) var(--ease-standard), border-bottom-color var(--transition-duration-hover) var(--ease-standard)`, `opacity 0.3s ease-out, filter 0.3s ease-out`
