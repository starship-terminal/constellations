# Component measurements

Computed styles read from elevenmusic.io on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the app's default dark paint, with the Cookiebot consent overlay hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### sidebar

Sidebar. The fixed left rail (248px): logo, Search, primary nav, the Publish-your-music promo and the Playlists list.

Page: home. Selector: `the fixed left rail ancestor of the logo anchor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 248 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #a1a1a1 |
| Text node | span.relative.min-w-0: Inter 14px/20px 450, #868686 |
| Transition | none |
| Icon | 7.72 x 13, colour #fafafa |
| Painted layers | button.font-normal.focus-visible:focus-ring 224.0x49.0 bg #222222 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; span.-right-1.-bottom-1 18.0x18.0 bg #000000 r 3.35544e+07px; div.absolute.inset-0 0.0x0.0 bg #171717; div.cover-border.pointer-events-none 0.0x0.0 r 8px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.absolute.inset-0 0.0x0.0 bg #171717; div.cover-border.pointer-events-none 0.0x0.0 r 8px shadow #ffffff @ 0.05 0px 0px 0px 1px inset |
| How | at rest |

Crops: `sidebar-default.png`.

#### sidebar-nav

Sidebar nav item. A primary nav row in the rail (icon + label, 36px); Explore holds the selected state on /.

Page: home. Selector: `sidebar a "Tools"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 36 | = | = | = |
| Padding | 0px 8px 2px 8px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #fafafa offset 2px | = |
| Font | Inter 14px/20px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Text node | span.relative.min-w-0: Inter 14px/20px 450, #868686 | span.relative.min-w-0: Inter 14px/20px 450, #fafafa | = | span.relative.min-w-0: Inter 14px/20px 450, #fafafa |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #868686 | 18 x 18, colour #fafafa | = | 18 x 18, colour #fafafa |
| ::before | 224px x 34px, absolute, bg #000000 @ 0, radius 10px | 224px x 34px, absolute, bg #ffffff @ 0.043, radius 10px | = | 224px x 34px, absolute, bg #ffffff @ 0.043, radius 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a::before.group/row.relative 224pxx34px bg #ffffff @ 0.043 r 10px | a.group/row.relative 224.0x36.0 r 10px outline 1px solid #fafafa offset 2px | a::before.group/row.relative 224pxx34px bg #ffffff @ 0.043 r 10px |

Crops: `sidebar-nav-default.png`, `sidebar-nav-hover.png`, `sidebar-nav-focus-visible.png`, `sidebar-nav-pressed.png`.

#### sidebar-action

Sidebar action. A gated rail action (Composer/Chat) that prompts sign-in; measured, never pressed.

Page: home. Selector: `sidebar button "Composer"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 36 | = | = | = |
| Padding | 0px 8px 2px 8px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #fafafa offset 2px | = |
| Font | Inter 14px/20px 450 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Text node | span.relative.min-w-0: Inter 14px/20px 450, #868686 | span.relative.min-w-0: Inter 14px/20px 450, #fafafa | = | span.relative.min-w-0: Inter 14px/20px 450, #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #868686 | 18 x 18, colour #fafafa | = | 18 x 18, colour #fafafa |
| ::before | 224px x 34px, absolute, bg #000000 @ 0, radius 10px | 224px x 34px, absolute, bg #ffffff @ 0.043, radius 10px | = | 224px x 34px, absolute, bg #ffffff @ 0.043, radius 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button::before.transition-[background-color,color,box-shadow,border-color].focus-visible:focus-ring 224pxx34px bg #ffffff @ 0.043 r 10px | button.transition-[background-color,color,box-shadow,border-color].focus-visible:focus-ring 224.0x36.0 r 10px outline 1px solid #fafafa offset 2px | button::before.transition-[background-color,color,box-shadow,border-color].focus-visible:focus-ring 224pxx34px bg #ffffff @ 0.043 r 10px |

Crops: `sidebar-action-default.png`, `sidebar-action-hover.png`, `sidebar-action-focus-visible.png`, `sidebar-action-pressed.png`.

#### sidebar-promo

Sidebar promo. The Publish-your-music promo card in the rail (surface-1 fill, artwork chip).

Page: home. Selector: `button "Publish your music"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 49 | = | = | = |
| Padding | 6px 14px 6px 6px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #222222 | #2b2b2b | = | #2b2b2b |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px solid #fafafa offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a1a1a1 | = | = | = |
| Text node | span.truncate: Inter 13px/20px 500, #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #a1a1a1 | = | = | = |
| Painted layers | button.font-normal.focus-visible:focus-ring 224.0x49.0 bg #222222 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; span.-right-1.-bottom-1 18.0x18.0 bg #000000 r 3.35544e+07px | button.font-normal.focus-visible:focus-ring 224.0x49.0 bg #2b2b2b r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; span.-right-1.-bottom-1 18.0x18.0 bg #000000 r 3.35544e+07px | button.font-normal.focus-visible:focus-ring 224.0x49.0 bg #222222 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px outline 1px solid #fafafa offset 2px; span.-right-1.-bottom-1 18.0x18.0 bg #000000 r 3.35544e+07px | button.font-normal.focus-visible:focus-ring 224.0x49.0 bg #2b2b2b r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; span.-right-1.-bottom-1 18.0x18.0 bg #000000 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sidebar-promo-default.png`, `sidebar-promo-hover.png`, `sidebar-promo-focus-visible.png`, `sidebar-promo-pressed.png`.

#### playlist-row

Playlist row. A media row in the rail's Playlists list (36px art + name + Featured tag).

Page: home. Selector: `sidebar a[href^="/playlists/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 50 | = | = | = |
| Padding | 0px 7px | = | = | = |
| Gap | 11px | = | = | = |
| Border | none | = | = | = |
| Radius | 15px | = | = | = |
| Background | transparent | #ffffff @ 0.043 | = | #ffffff @ 0.043 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #fafafa offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a1a1a1 | = | = | = |
| Text node | span.truncate.text-foreground/85: Inter 13px/18px 400, #fafafa @ 0.85 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | auto x auto, static, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | div.absolute.inset-0 36.0x36.0 bg #171717; div.cover-border.pointer-events-none 36.0x36.0 r 8px shadow #ffffff @ 0.05 0px 0px 0px 1px inset | a.group/media.[--row:3.125rem] 224.0x50.0 bg #ffffff @ 0.043 r 15px; div.absolute.inset-0 36.0x36.0 bg #171717; div.cover-border.pointer-events-none 36.0x36.0 r 8px shadow #ffffff @ 0.05 0px 0px 0px 1px inset | a.group/media.[--row:3.125rem] 224.0x50.0 r 15px outline 1px solid #fafafa offset 1px; div.absolute.inset-0 36.0x36.0 bg #171717; div.cover-border.pointer-events-none 36.0x36.0 r 8px shadow #ffffff @ 0.05 0px 0px 0px 1px inset | a.group/media.[--row:3.125rem] 224.0x50.0 bg #ffffff @ 0.043 r 15px; div.absolute.inset-0 36.0x36.0 bg #171717; div.cover-border.pointer-events-none 36.0x36.0 r 8px shadow #ffffff @ 0.05 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `playlist-row-default.png`, `playlist-row-hover.png`, `playlist-row-focus-visible.png`, `playlist-row-pressed.png`.

#### icon-button

Icon button. The rail's 30px Search icon button (opens the sign-in dialog).

Page: home. Selector: `button[aria-label="Search"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30 x 30 | = | = | 29.4 x 29.4 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #868686 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.items-center 30.0x30.0 bg #ffffff @ 0.08 r 10px | button.inline-flex.items-center 30.0x30.0 r 10px outline 1px solid #ffffff offset 2px | button.inline-flex.items-center 29.4x29.4 bg #ffffff @ 0.08 r 10px |

Crops: `icon-button-default.png`, `icon-button-hover.png`, `icon-button-focus-visible.png`, `icon-button-pressed.png`.

#### sidebar-collapse

Sidebar collapse. The 32px rail-collapse icon button; measured, never pressed.

Page: home. Selector: `button[aria-label="Close sidebar"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 31.36 x 31.36 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #868686 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| Ancestor paint | 1 up header.h-13.shrink-0 bg #000000 @ 0.95 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.items-center.justify-center 32.0x32.0 bg #ffffff @ 0.08 r 10px | button.items-center.justify-center 32.0x32.0 r 10px outline 1px solid #ffffff offset 2px | button.items-center.justify-center 31.4x31.4 bg #ffffff @ 0.08 r 10px |

Crops: `sidebar-collapse-default.png`, `sidebar-collapse-hover.png`, `sidebar-collapse-focus-visible.png`, `sidebar-collapse-pressed.png`.

#### new-playlist-btn

New-playlist button. The 24px + button on the Playlists heading; measured, never pressed.

Page: home. Selector: `button[aria-label="New playlist"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 12px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff @ 0.4 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff @ 0.4 | 16 x 16, colour #fafafa | = | 16 x 16, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.items-center 24.0x24.0 bg #ffffff @ 0.08 r 6px | button.inline-flex.items-center 24.0x24.0 r 6px outline 1px solid #ffffff offset 2px | button.inline-flex.items-center 24.0x24.0 bg #ffffff @ 0.08 r 6px |

Crops: `new-playlist-btn-default.png`, `new-playlist-btn-hover.png`, `new-playlist-btn-focus-visible.png`, `new-playlist-btn-pressed.png`.

#### header

Header. The app header (52px, translucent lab(0 0 0 / .95)): Main nav, Sign in, Start free.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1186 x 52 |
| Padding | 0px 10px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.95 |
| Box shadow | none |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | a.flex.h-7: Inter 13px/19.5px 500, #868686 |
| Transition | none |
| Icon | 16 x 16, colour #868686 |
| Painted layers | header.h-13.shrink-0 1186.0x52.0 bg #000000 @ 0.95; button.font-normal.outline-hidden 0.0x0.0 bg #151515 r 3.35544e+07px; button.inline-flex.shrink-0 69.8x32.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; button.inline-flex.shrink-0 85.7x32.0 bg #fafafa r 3.35544e+07px; span.absolute.left-0 0.0x0.0 bg #fafafa r 3.35544e+07px; span.absolute.left-0 0.0x0.0 bg #fafafa r 3.35544e+07px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The ElevenMusic wordmark/mark anchor.

Page: home. Selector: `a[aria-label="ElevenMusic"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 124.33 x 32 |
| Padding | 0px 8px |
| Border | none |
| Radius | 10px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| Cursor | pointer |
| Icon | 7.72 x 13, colour #fafafa |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Header nav link. A header nav link (28px pill); measured, never followed.

Page: home. Selector: `header a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62.56 x 28 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #ffffff @ 0.043 | = | #ffffff @ 0.043 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.h-7 62.6x28.0 bg #ffffff @ 0.043 r 3.35544e+07px | a.flex.h-7 62.6x28.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.flex.h-7 62.6x28.0 bg #ffffff @ 0.043 r 3.35544e+07px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-trigger

Resources trigger. The header Resources button that opens the dropdown; toggled for the open state.

Page: home. Selector: `header button "Resources"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.55 x 28 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.043 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | Inter 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.flex.h-7 86.5x28.0 bg #ffffff @ 0.08 r 3.35544e+07px | button.flex.h-7 86.5x28.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | button.flex.h-7 86.5x28.0 bg #ffffff @ 0.043 r 3.35544e+07px |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### signin-btn

Sign-in button. The dark Sign-in pill (surface-2 fill); measured, never pressed.

Page: home. Selector: `header button "Sign in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.84 x 32 | = | = | 68.45 x 31.36 |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #222222 | #2b2b2b | = | #2b2b2b |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.shrink-0 69.8x32.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | button.inline-flex.shrink-0 69.8x32.0 bg #2b2b2b r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | button.inline-flex.shrink-0 69.8x32.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 68.4x31.4 bg #2b2b2b r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-btn-default.png`, `signin-btn-hover.png`, `signin-btn-focus-visible.png`, `signin-btn-pressed.png`.

#### cta-btn

Start-free CTA. The white Start-free pill (primary fill); measured, never pressed.

Page: home. Selector: `header button "Start free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.66 x 32 | = | = | 83.94 x 31.36 |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fafafa | #faf8f7 | = | #faf8f7 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.shrink-0 85.7x32.0 bg #fafafa r 3.35544e+07px | button.inline-flex.shrink-0 85.7x32.0 bg #faf8f7 r 3.35544e+07px | button.inline-flex.shrink-0 85.7x32.0 bg #fafafa r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 83.9x31.4 bg #faf8f7 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-btn-default.png`, `cta-btn-hover.png`, `cta-btn-focus-visible.png`, `cta-btn-pressed.png`.

#### nav-dropdown

Resources dropdown. The Resources menu panel (popover fill, opened by its own trigger).

Page: home. Selector: `painted ancestor of a Resources menu link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 274 x 194 |
| Padding | 0px |
| Border | none |
| Radius | 14px |
| Background | #2e2e2e |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | a.block.text-pretty: Inter 13px/20px 500, #fafafa |
| Transition | width, height 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.relative.h-(--radix-navigation-menu-viewport-height) 274.0x194.0 bg #2e2e2e r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A link inside the opened Resources dropdown.

Page: home. Selector: `resources menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 222 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 13px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | #868686 | #868686 | #868686 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | = | 1 up div.group/link.relative shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | 1 up div.group/link.relative shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home hero

#### hero-title

Hero headline. The "Make music yours." display headline (font-display light).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 349.08 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | waldenburg 40px/44px 300 |
| Letter spacing | -0.8px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-lede

Hero copy. The muted lede under the headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 349.08 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #868686 |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### composer-field

Composer field. The prompt input in the hero composer (556px); sample text was typed and deleted, nothing sent.

Page: home. Selector: `hero composer input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 556 x 36 | = | = |
| Padding | 0px 8px 0px 6px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 15px/22.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #fafafa | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #fafafa, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `composer-field-default.png`, `composer-field-focused.png`, `composer-field-filled.png`.

#### attach-btn

Attach button. The composer's 36px + button (black circle); measured, never pressed.

Page: home. Selector: `button[aria-label="Attach"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.6 0px 0px 0px 2px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #fafafa | = | = | = |
| Painted layers | button.focus-visible:focus-ring.motion-reduce:active:scale-100 36.0x36.0 bg #000000 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; span.absolute.bottom-0 17.1x17.1 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; span.absolute.bottom-0 16.0x16.0 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; span.absolute.bottom-0 17.1x17.1 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | button.focus-visible:focus-ring.motion-reduce:active:scale-100 36.0x36.0 bg #000000 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; span.absolute.bottom-0 19.0x19.0 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; span.absolute.bottom-0 16.0x16.0 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; span.absolute.bottom-0 19.0x19.0 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | button.focus-visible:focus-ring.motion-reduce:active:scale-100 36.0x36.0 bg #000000 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.6 0px 0px 0px 2px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px outline 1px solid #ffffff offset 2px; span.absolute.bottom-0 17.1x17.1 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; span.absolute.bottom-0 16.0x16.0 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px; span.absolute.bottom-0 17.1x17.1 bg #2e2e2e r 5px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px | = |
| Ancestor paint | 1 up div.flex.h-12 bg #ffffff @ 0.08 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `attach-btn-default.png`, `attach-btn-hover.png`, `attach-btn-focus-visible.png`, `attach-btn-pressed.png`.

#### send-button

Send button. The composer's white 36px circular send button (Create); measured, never pressed.

Page: home. Selector: `composer send button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 34.2 x 34.2 |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fafafa | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | opacity, transform 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | 15.2 x 15.2, colour #000000 |
| Painted layers | button.font-normal.outline-hidden 36.0x36.0 bg #fafafa r 3.35544e+07px | = | button.font-normal.outline-hidden 36.0x36.0 bg #fafafa r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.font-normal.outline-hidden 34.2x34.2 bg #fafafa r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.h-12 bg #ffffff @ 0.08 | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `send-button-default.png`, `send-button-hover.png`, `send-button-focus-visible.png`, `send-button-pressed.png`.

#### prompt-chip

Prompt chip. A suggestion chip under the composer (lighten-100 fill, pill).

Page: home. Selector: `button "Trap beat"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.53 x 28 | = | = | 76.18 x 27.16 |
| Padding | 0px 12px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff @ 0.08 | #ffffff @ 0.114 | = | #ffffff @ 0.114 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 12px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | background-color, color, transform 0.15s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.font-normal.focus-visible:focus-ring 78.5x28.0 bg #ffffff @ 0.08 r 3.35544e+07px | button.font-normal.focus-visible:focus-ring 78.5x28.0 bg #ffffff @ 0.114 r 3.35544e+07px | = | button.font-normal.focus-visible:focus-ring 76.2x27.2 bg #ffffff @ 0.114 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `prompt-chip-default.png`, `prompt-chip-hover.png`, `prompt-chip-focus-visible.png`, `prompt-chip-pressed.png`.

#### seg-tab-on

Segmented tab, selected. The selected segment (Songs) of the Songs/Sounds control (lighten-150 fill).

Page: home. Selector: `[role=tab][data-state=active]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74.52 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff @ 0.114 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 74.5156px x 2px, absolute, bg #fafafa, radius 0px | = | = | = |
| Painted layers | button.relative.inline-flex 74.5x40.0 bg #ffffff @ 0.114 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button::after.relative.inline-flex 74.5156pxx2px bg #fafafa | = | button.relative.inline-flex 74.5x40.0 bg #ffffff @ 0.114 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 1px solid #ffffff offset 2px; button::after.relative.inline-flex 74.5156pxx2px bg #fafafa | = |
| Ancestor paint | 1 up div.group/tabs-list.relative bg #ffffff @ 0.08 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `seg-tab-on-default.png`, `seg-tab-on-hover.png`, `seg-tab-on-focus-visible.png`, `seg-tab-on-pressed.png`.

#### seg-tab-off

Segmented tab. An unselected segment (Sounds/Featured rail tabs).

Page: home. Selector: `[role=tab][data-state=inactive]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82.84 x 40 | = | - | = |
| Padding | 0px 16px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | transparent | #ffffff @ 0.08 | - | #ffffff @ 0.08 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #868686 | #fafafa | - | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| ::after | 82.8438px x 2px, absolute, bg #fafafa, radius 0px | = | - | = |
| Painted layers | button::after.relative.inline-flex 82.8438pxx2px bg #fafafa | button.relative.inline-flex 82.8x40.0 bg #ffffff @ 0.08 r 3.35544e+07px; button::after.relative.inline-flex 82.8438pxx2px bg #fafafa | - | button.relative.inline-flex 82.8x40.0 bg #ffffff @ 0.08 r 3.35544e+07px; button::after.relative.inline-flex 82.8438pxx2px bg #fafafa |
| Ancestor paint | 1 up div.group/tabs-list.relative bg #ffffff @ 0.08 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `seg-tab-off-default.png`, `seg-tab-off-hover.png`, `seg-tab-off-pressed.png`.

#### track-row

Track row. A song row in the demo list (art + title + artist); measured, never pressed.

Page: home. Selector: `wide labelled button in the hero demo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 614.66 x 52 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.group/media-row.relative bg #171717 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `track-row-default.png`, `track-row-hover.png`, `track-row-focus-visible.png`, `track-row-pressed.png`.

#### demo-card

Stem card. A stem/description card in the hero demo (surface-1 fill).

Page: home. Selector: `hero stem card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 156 x 68 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #222222 | #2b2b2b | = | #2b2b2b |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span.font-medium.text-sm: Inter 14px/20px 500, #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.font-normal.outline-hidden 156.0x68.0 bg #222222 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; span.absolute.inset-x-3 0.0x2.0 bg #fafafa r 3.35544e+07px | button.font-normal.outline-hidden 156.0x68.0 bg #2b2b2b r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; span.absolute.inset-x-3 0.0x2.0 bg #fafafa r 3.35544e+07px | button.font-normal.outline-hidden 156.0x68.0 bg #222222 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px outline 1px solid #ffffff offset 2px; span.absolute.inset-x-3 0.0x2.0 bg #fafafa r 3.35544e+07px | button.font-normal.outline-hidden 156.0x68.0 bg #2b2b2b r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; span.absolute.inset-x-3 0.0x2.0 bg #fafafa r 3.35544e+07px |
| Ancestor paint | 3 up article.flex.h-[340px] bg #000000 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.08 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `demo-card-default.png`, `demo-card-hover.png`, `demo-card-focus-visible.png`, `demo-card-pressed.png`.

#### carousel-prev

Carousel previous. The 32px frosted carousel arrow.

Page: home. Selector: `button[aria-label="Previous"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 30.4 x 30.4 |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #2e2e2e @ 0.85 | #2e2e2e | = | #2e2e2e |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px | = | = | = |
| Backdrop filter | blur(16px) | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | transform, background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa | = | = | 15.2 x 15.2, colour #fafafa |
| Painted layers | button.font-normal.outline-hidden 32.0x32.0 bg #2e2e2e @ 0.85 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px | button.font-normal.outline-hidden 32.0x32.0 bg #2e2e2e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px | button.font-normal.outline-hidden 32.0x32.0 bg #2e2e2e @ 0.85 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px outline 1px solid #ffffff offset 2px | button.font-normal.outline-hidden 30.4x30.4 bg #2e2e2e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-prev-default.png`, `carousel-prev-hover.png`, `carousel-prev-focus-visible.png`, `carousel-prev-pressed.png`.

#### carousel-next

Carousel next. The 32px frosted carousel arrow.

Page: home. Selector: `button[aria-label="Next"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | - | 30.4 x 30.4 |
| Padding | 0px | = | - | = |
| Gap | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | #2e2e2e @ 0.85 | = | - | #2e2e2e |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px | = | - | = |
| Backdrop filter | blur(16px) | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #fafafa | = | - | = |
| Transition | transform, background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #fafafa | = | - | 15.2 x 15.2, colour #fafafa |
| Painted layers | button.font-normal.outline-hidden 32.0x32.0 bg #2e2e2e @ 0.85 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px | = | - | button.font-normal.outline-hidden 30.4x30.4 bg #2e2e2e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.35 0px 20px 24px 0px, #000000 @ 0.18 0px 5px 8px 0px, #ffffff @ 0.06 0px 0px 0px 0.5px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `carousel-next-default.png`, `carousel-next-hover.png`, `carousel-next-pressed.png`.

#### carousel-dot

Carousel dot. A carousel pagination dot (the active one is a white 32x6 pill).

Page: home. Selector: `button[aria-label^="Go to"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 6 x 6 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fafafa @ 0.3 | #fafafa @ 0.499765 | = | #fafafa @ 0.497926 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | width, background-color 0.5s cubic-bezier(0.2, 0.8, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 6.0x6.0 bg #fafafa @ 0.3 r 3.35544e+07px | button.inline-flex.items-center 6.0x6.0 bg #fafafa @ 0.499765 r 3.35544e+07px | button.inline-flex.items-center 6.0x6.0 bg #fafafa @ 0.3 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.items-center 6.0x6.0 bg #fafafa @ 0.497926 r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.h-9 bg #fafafa @ 0.05 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-dot-default.png`, `carousel-dot-hover.png`, `carousel-dot-focus-visible.png`, `carousel-dot-pressed.png`.

#### play-hero

Round play button. A white circular play button (36-48px); measured, never pressed here.

Page: home. Selector: `button[aria-label^="Play"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | 45.6 x 45.6 |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff @ 0.1 | #ffffff @ 0.15 | = | #ffffff @ 0.15 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset | = | = | = |
| Backdrop filter | blur(24px) | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, transform 0.2s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff, fill #000000 | = | = | 19 x 19, colour #ffffff, fill #000000 |
| Painted layers | button.focus-visible:focus-ring.motion-reduce:active:scale-100 48.0x48.0 bg #ffffff @ 0.1 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset | button.focus-visible:focus-ring.motion-reduce:active:scale-100 48.0x48.0 bg #ffffff @ 0.15 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset | = | button.focus-visible:focus-ring.motion-reduce:active:scale-100 45.6x45.6 bg #ffffff @ 0.15 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.12 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `play-hero-default.png`, `play-hero-hover.png`, `play-hero-focus-visible.png`, `play-hero-pressed.png`.

### Footer

#### footer

Footer. The site footer inside the shell: language selector, link columns, legal and the theme control.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1186 x 708 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | button.group.focus-visible:focus-ring: Inter 14px/20px 500, #fafafa |
| Transition | none |
| Icon | 24.08 x 28, colour #fafafa |
| Painted layers | div.flex.items-center 76.0x28.0 bg #fafafa @ 0.05 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.06 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.absolute.inset-0 24.0x24.0 bg #fafafa @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.08 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer column link (36px row).

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.14 x 36 | = | = | = |
| Padding | 8px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | #868686 | = | #868686 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.focus-visible:focus-ring.-mx-1.5 106.1x36.0 r 6px outline 1px solid #ffffff offset 2px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### lang-btn

Language selector. The English locale button; measured, never opened.

Page: home. Selector: `button "English"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.17 x 28 | = | = | = |
| Padding | 0px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.group.focus-visible:focus-ring 103.2x28.0 r 6px outline 1px solid #ffffff offset 2px | = |

Crops: `lang-btn-default.png`, `lang-btn-hover.png`, `lang-btn-focus-visible.png`, `lang-btn-pressed.png`.

#### cookie-btn

Cookie settings. The Cookie-settings button (opens Cookiebot; measured, never pressed).

Page: home. Selector: `button "Cookie settings"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114.5 x 36 | = | = | = |
| Padding | 8px 6px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | #868686 | = | #868686 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.items-center.outline-hidden 114.5x36.0 r 6px outline 1px solid #ffffff offset 2px | = |

Crops: `cookie-btn-default.png`, `cookie-btn-hover.png`, `cookie-btn-focus-visible.png`, `cookie-btn-pressed.png`.

#### theme-seg

Theme control. The System/Light/Dark segmented control in the footer.

Page: home. Selector: `theme segmented control`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 76 x 28 |
| Padding | 2px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #fafafa @ 0.05 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.06 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| Icon | 14 x 14, colour #868686 |
| Painted layers | div.flex.items-center 76.0x28.0 bg #fafafa @ 0.05 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.06 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; span.absolute.inset-0 24.0x24.0 bg #fafafa @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.08 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px |
| How | at rest |

Crops: `theme-seg-default.png`.

#### theme-dark-btn

Theme dark button. The Dark segment of the theme control (selected when the page paints dark).

Page: home. Selector: `button[aria-label="Dark theme"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #fafafa | = | = | = |
| Painted layers | span.absolute.inset-0 24.0x24.0 bg #fafafa @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.08 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = | button.focus-visible:focus-ring.motion-reduce:active:scale-100 24.0x24.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px; span.absolute.inset-0 24.0x24.0 bg #fafafa @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.08 0px 0px 0px 1px, #000000 @ 0.1 0px 1px 3px 0px, #000000 @ 0.1 0px 1px 2px -1px | = |
| Ancestor paint | 1 up div.flex.items-center bg #fafafa @ 0.05 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.06 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `theme-dark-btn-default.png`, `theme-dark-btn-hover.png`, `theme-dark-btn-focus-visible.png`, `theme-dark-btn-pressed.png`.

#### theme-light-btn

Theme light button. The Light segment of the theme control; measured, never pressed here (the light pass toggles it).

Page: home. Selector: `button[aria-label="Light theme"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #868686 | 14 x 14, colour #fafafa | = | 14 x 14, colour #fafafa |
| Ancestor paint | 1 up div.flex.items-center bg #fafafa @ 0.05 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fafafa @ 0.06 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.focus-visible:focus-ring.motion-reduce:active:scale-100 24.0x24.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px | = |

Crops: `theme-light-btn-default.png`, `theme-light-btn-hover.png`, `theme-light-btn-focus-visible.png`, `theme-light-btn-pressed.png`.

### Explore and browse

#### sidebar-nav-selected

Sidebar nav item, selected. The Explore row held selected on its own page.

Page: explore. Selector: `sidebar a "Explore"`. States: selected.

| Property | selected |
|---|---|
| Size (w x h) | 224 x 36 |
| Padding | 0px 8px 2px 8px |
| Gap | 10px |
| Border | none |
| Radius | 10px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 450 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.relative.min-w-0: Inter 14px/20px 450, #fafafa |
| Transition | none |
| Cursor | pointer |
| Icon | 18 x 18, colour #fafafa |
| ::before | 224px x 34px, absolute, bg #222222, radius 10px, shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px |
| Painted layers | a::before.group/row.relative 224pxx34px bg #222222 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px |
| How | held selected by an earlier toggle |

Crops: `sidebar-nav-selected-selected.png`.

#### explore-title

Explore title. The "Create music" page heading.

Page: explore. Selector: `h1 on /explore`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 444.42 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | waldenburg 40px/44px 300 |
| Letter spacing | -0.8px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `explore-title-default.png`.

#### create-nav

Create nav. The pill nav under the title (Create/Composer/Styles/Sounds/Library — every item gated behind sign-in).

Page: explore. Selector: `nav[aria-label="Create"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 752 x 70 |
| Padding | 0px |
| Gap | 32px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.w-full.truncate: Inter 14px/20px 500, #fafafa |
| Transition | none |
| Icon | 20 x 20, colour #868686 |
| Painted layers | div.composer-hairline.flex 40.0x40.0 bg #151515 r 12px shadow #ffffff @ 0.15 0px 1px 0px 0px inset, #2b2b2b 0px 0px 0px 1px inset, #ffffff @ 0.08 0px -1px 0px 0px inset, #1c1917 @ 0.53 0px 1px 2px -1px, #1c1917 @ 0.53 0px 10px 24px -10px; div.composer-hairline.flex 40.0x40.0 bg #151515 r 12px shadow #ffffff @ 0.15 0px 1px 0px 0px inset, #2b2b2b 0px 0px 0px 1px inset, #ffffff @ 0.08 0px -1px 0px 0px inset, #1c1917 @ 0.53 0px 1px 2px -1px, #1c1917 @ 0.53 0px 10px 24px -10px; div.composer-hairline.flex 40.0x40.0 bg #151515 r 12px shadow #ffffff @ 0.15 0px 1px 0px 0px inset, #2b2b2b 0px 0px 0px 1px inset, #ffffff @ 0.08 0px -1px 0px 0px inset, #1c1917 @ 0.53 0px 1px 2px -1px, #1c1917 @ 0.53 0px 10px 24px -10px; div.composer-hairline.flex 40.0x40.0 bg #151515 r 12px shadow #ffffff @ 0.15 0px 1px 0px 0px inset, #2b2b2b 0px 0px 0px 1px inset, #ffffff @ 0.08 0px -1px 0px 0px inset, #1c1917 @ 0.53 0px 1px 2px -1px, #1c1917 @ 0.53 0px 10px 24px -10px; div.composer-hairline.flex 40.0x40.0 bg #151515 r 12px shadow #ffffff @ 0.15 0px 1px 0px 0px inset, #2b2b2b 0px 0px 0px 1px inset, #ffffff @ 0.08 0px -1px 0px 0px inset, #1c1917 @ 0.53 0px 1px 2px -1px, #1c1917 @ 0.53 0px 10px 24px -10px |
| How | at rest |

Crops: `create-nav-default.png`.

#### explore-input

Prompt input. The "Describe your song" prompt field (556px); sample text typed and deleted, nothing sent.

Page: explore. Selector: `explore prompt input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 556 x 36 | = | = |
| Padding | 0px 8px 0px 6px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 15px/22.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #fafafa | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #fafafa, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `explore-input-default.png`, `explore-input-focused.png`, `explore-input-filled.png`.

#### feature-card

Feature card. The featured track's carousel card (artwork, title, artist, Remix chip).

Page: explore. Selector: `painted ancestor of the feature play button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 328 x 328.5 |
| Padding | 0px |
| Border | none |
| Radius | 6px |
| Background | #171717 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.relative.flex-1 328.0x328.5 bg #171717 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; div.pointer-events-none.absolute 328.0x328.5 image linear-gradient(to right bottom, #ffffff @ 0.1 0%, #000000 @ 0 50%, #000000 @ 0 100%); div.cover-border.pointer-events-none 328.0x328.5 r 6px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; span.flex.h-9 36.0x36.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px |
| Ancestor paint | 1 up div.absolute.inset-0 bg #000000 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px, #000000 @ 0.06 0px 6px 6px -3px, #000000 @ 0.04 0px 12px 12px -6px, #000000 @ 0.04 0px 24px 24px -12px, #000000 @ 0.02 0px 48px 48px -24px, #000000 @ 0.04 0px 10px 20px 1px |
| How | at rest |

Crops: `feature-card-default.png`.

#### play-feature

Card play button. The 36px play control on a feature card; pressed once below to mount the player bar.

Page: explore. Selector: `button[aria-label^="Play "]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | span.flex.h-9 36.0x36.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = | button.items-center.transition-[background-color,color,box-shadow,border-color] 36.0x36.0 outline 1px solid #ffffff offset 2px; span.flex.h-9 36.0x36.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = |
| Ancestor paint | 1 up div.relative.flex-1 bg #171717 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0 0px 0px 0px 0px; 2 up div.absolute.inset-0 bg #000000 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px, #000000 @ 0.06 0px 6px 6px -3px, #000000 @ 0.04 0px 12px 12px -6px, #000000 @ 0.04 0px 24px 24px -12px, #000000 @ 0.02 0px 48px 48px -24px, #000000 @ 0.04 0px 10px 20px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `play-feature-default.png`, `play-feature-hover.png`, `play-feature-focus-visible.png`, `play-feature-pressed.png`.

#### remix-chip

Remix chip. The Remix chip on a feature card; measured, never pressed (gated).

Page: explore. Selector: `feature card "Remix"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.42 x 32 | = | = | 76.85 x 31.36 |
| Padding | 0px 10px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #1c1c1c | #292929 | = | #292929 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa | = | = | 15.68 x 15.68, colour #fafafa |
| Painted layers | button.inline-flex.shrink-0 78.4x32.0 bg #1c1c1c r 3.35544e+07px | button.inline-flex.shrink-0 78.4x32.0 bg #292929 r 3.35544e+07px | button.inline-flex.shrink-0 78.4x32.0 bg #1c1c1c r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 76.9x31.4 bg #292929 r 3.35544e+07px |
| Ancestor paint | 3 up div.absolute.inset-0 bg #000000 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px, #000000 @ 0.06 0px 6px 6px -3px, #000000 @ 0.04 0px 12px 12px -6px, #000000 @ 0.04 0px 24px 24px -12px, #000000 @ 0.02 0px 48px 48px -24px, #000000 @ 0.04 0px 10px 20px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `remix-chip-default.png`, `remix-chip-hover.png`, `remix-chip-focus-visible.png`, `remix-chip-pressed.png`.

#### track-card

Track card. A 208px track card in a shelf (artwork, title, artist, version badge); hover raises the play button.

Page: explore. Selector: `role=group track card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 208 x 237 | = |
| Padding | 0px 0px 0px 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #fafafa | = |
| Text node | h3.truncate.font-medium: Inter 13px/20px 500, #fafafa | = |
| Transition | none | = |
| Icon | 14.4 x 14.4, colour #000000 | 16 x 16, colour #000000 |
| Painted layers | div.absolute.overflow-hidden 192.0x192.0 bg #ffffff @ 0.043 r 14px; div.absolute.inset-0 192.0x192.0 bg #171717; button.transition-[background-color,color,box-shadow,border-color].outline-hidden 32.4x32.4 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; div.cover-border.pointer-events-none 192.0x192.0 r 14px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.pointer-events-none.absolute 192.0x192.0 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px; span.inline-flex.h-4 34.3x16.0 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 3.35544e+07px | div.absolute.overflow-hidden 192.0x192.0 bg #ffffff @ 0.043 r 14px; div.absolute.inset-0 192.0x192.0 bg #171717; button.transition-[background-color,color,box-shadow,border-color].outline-hidden 36.0x36.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; div.cover-border.pointer-events-none 192.0x192.0 r 14px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.pointer-events-none.absolute 192.0x192.0 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px; span.inline-flex.h-4 34.3x16.0 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 3.35544e+07px |
| How | at rest | mouse hover |

Crops: `track-card-default.png`, `track-card-hover.png`.

#### play-track

Track play button. The white 32px circular play button a card raises on hover.

Page: explore. Selector: `button[aria-label="Play track"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32.4 x 32.4 | 36 x 36 | - | = |
| Padding | 0px | = | - | = |
| Gap | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #fafafa | = | - | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | default | = | - | = |
| Icon | 14.4 x 14.4, colour #000000 | 16 x 16, colour #000000 | - | = |
| Painted layers | button.transition-[background-color,color,box-shadow,border-color].outline-hidden 32.4x32.4 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | button.transition-[background-color,color,box-shadow,border-color].outline-hidden 36.0x36.0 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `play-track-default.png`, `play-track-hover.png`, `play-track-pressed.png`.

#### version-badge

Version badge. The "v2.5" badge on track cards.

Page: explore. Selector: `version badge span`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 34.25 x 16 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/16px 400 |
| Letter spacing | normal |
| Colour | #868686 |
| Text node | span.inline-flex.h-4: Inter 10px/10px 500, #868686 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.inline-flex.h-4 34.3x16.0 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 3.35544e+07px |
| How | at rest |

Crops: `version-badge-default.png`.

#### genre-card

Genre card. A genre tile in Genres & Moods (artwork + name + play chip).

Page: explore. Selector: `tile ancestor of a "Play playlist" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 192 x 192 | 192.26 x 188.96 | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 14px | = | = | = |
| Background | #ffffff @ 0.043 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | transform, translate, scale, rotate 0.22s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14.4 x 14.4, colour #000000 | 16.13 x 16.04, colour #000000 | = | = |
| Painted layers | div.absolute.overflow-hidden 192.0x192.0 bg #ffffff @ 0.043 r 14px; div.absolute.inset-0 192.0x192.0 bg #171717; button.transition-[background-color,color,box-shadow,border-color].outline-hidden 25.2x25.2 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; div.cover-border.pointer-events-none 192.0x192.0 r 14px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.pointer-events-none.absolute 192.0x192.0 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | div.absolute.overflow-hidden 192.3x189.0 bg #ffffff @ 0.043 r 14px; div.absolute.inset-0 192.3x189.0 bg #171717; button.transition-[background-color,color,box-shadow,border-color].outline-hidden 28.2x28.1 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px; div.cover-border.pointer-events-none 192.3x189.0 r 14px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.pointer-events-none.absolute 192.3x189.0 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | div.absolute.overflow-hidden 192.0x192.0 bg #ffffff @ 0.043 r 14px; div.absolute.inset-0 192.0x192.0 bg #171717; button.transition-[background-color,color,box-shadow,border-color].outline-hidden 25.2x25.2 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #ffffff offset 2px; div.cover-border.pointer-events-none 192.0x192.0 r 14px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.pointer-events-none.absolute 192.0x192.0 r 14px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 2px inset, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix3d(0.998, 0, 0, 0, 0, 0.996444, 0.0557099, -6.33067e-05, 0, -0.0558215, 0.998441, -0.00113459, 0, 0, 0, 1) | = | = |

Crops: `genre-card-default.png`, `genre-card-hover.png`, `genre-card-focus-visible.png`, `genre-card-pressed.png`.

#### play-genre

Genre play button. The white 25px circular play button on a genre tile.

Page: explore. Selector: `button[aria-label="Play playlist"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 25.2 x 25.2 | 28.22 x 28.07 | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14.4 x 14.4, colour #000000 | 16.13 x 16.04, colour #000000 | = | = |
| Painted layers | button.transition-[background-color,color,box-shadow,border-color].outline-hidden 25.2x25.2 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | button.transition-[background-color,color,box-shadow,border-color].outline-hidden 28.2x28.1 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px | button.transition-[background-color,color,box-shadow,border-color].outline-hidden 25.2x25.2 bg #ffffff r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 10px 15px -3px, #000000 @ 0.1 0px 4px 6px -4px outline 1px solid #ffffff offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `play-genre-default.png`, `play-genre-hover.png`, `play-genre-focus-visible.png`, `play-genre-pressed.png`.

#### artist-link

Artist link. An artist-name link under a track title; measured, never followed.

Page: explore. Selector: `a[href^="/artists/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95.34 x 18.75 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #ffffff @ 0.5 offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span.truncate.font-medium: Inter 15px/18.75px 500, #868686, ls -0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #fafafa | = | = | = |
| Ancestor paint | 3 up div.absolute.inset-0 bg #000000 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 1px inset, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.06 0px 1px 1px -0.5px, #000000 @ 0.06 0px 3px 3px -1.5px, #000000 @ 0.06 0px 6px 6px -3px, #000000 @ 0.04 0px 12px 12px -6px, #000000 @ 0.04 0px 24px 24px -12px, #000000 @ 0.02 0px 48px 48px -24px, #000000 @ 0.04 0px 10px 20px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.inline-flex.min-w-0 95.3x18.8 outline 1px auto #ffffff @ 0.5 offset 1px | = |

Crops: `artist-link-default.png`, `artist-link-hover.png`, `artist-link-focus-visible.png`, `artist-link-pressed.png`.

#### shelf-heading

Shelf heading. A shelf heading ("Featured", "Genres & Moods").

Page: explore. Selector: `h2 shelf heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 85.73 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/28px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `shelf-heading-default.png`.

### Player

#### player-bar

Player bar. The bottom transport bar mounted by pressing a card's Play (art, progress, transport, volume).

Page: explore. Selector: `painted ancestor of the pause button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1186 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #000000 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.16 0px 0px 0px 0.5px, #000000 @ 0.45 0px 1px 2px 0px, #000000 @ 0.4 0px 4px 8px -2px, #000000 @ 0.35 0px 12px 24px -6px |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | a.block.truncate: Inter 14px/20px 500, #fafafa |
| Transition | none |
| Icon | 12 x 12, colour #fafafa |
| Painted layers | div.@container/pb.pointer-events-auto 1186.0x72.0 bg #000000 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.16 0px 0px 0px 0.5px, #000000 @ 0.45 0px 1px 2px 0px, #000000 @ 0.4 0px 4px 8px -2px, #000000 @ 0.35 0px 12px 24px -6px; a.-ml-1.@min-[650px]/pb:-ml-1.5 52.0x52.0 bg #171717 r 14px; div.absolute.inset-0 52.0x52.0 bg #171717; div.cover-border.pointer-events-none 52.0x52.0 r 14px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; button.inline-flex.shrink-0 36.0x36.0 bg #fafafa r 3.35544e+07px; div.relative.w-full 328.0x4.0 bg #fafafa @ 0.15 r 3.35544e+07px |
| How | at rest |

Crops: `player-bar-default.png`.

#### player-play

Player play/pause. The transport's central pause button (a playing track).

Page: explore. Selector: `button[aria-label="Pause"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 34.2 x 34.2 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fafafa | #fafafa @ 0.9 | = | #fafafa @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | transform, translate, scale, rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | 15.2 x 15.2, colour #000000 |
| Painted layers | button.inline-flex.shrink-0 36.0x36.0 bg #fafafa r 3.35544e+07px | button.inline-flex.shrink-0 36.0x36.0 bg #fafafa @ 0.9 r 3.35544e+07px | button.inline-flex.shrink-0 36.0x36.0 bg #fafafa r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 34.2x34.2 bg #fafafa @ 0.9 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `player-play-default.png`, `player-play-hover.png`, `player-play-focus-visible.png`, `player-play-pressed.png`.

#### player-prev

Player previous. The transport previous button (the unlabeled control before Pause).

Page: explore. Selector: `button before transport Pause`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 35.28 x 35.28 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.8 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa @ 0.8 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.items-center 36.0x36.0 bg #ffffff @ 0.08 r 3.35544e+07px | button.inline-flex.items-center 36.0x36.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.items-center 35.3x35.3 bg #ffffff @ 0.08 r 3.35544e+07px |

Crops: `player-prev-default.png`, `player-prev-hover.png`, `player-prev-focus-visible.png`, `player-prev-pressed.png`.

#### player-next

Player next. The transport next button (the unlabeled control after Pause).

Page: explore. Selector: `button after transport Pause`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 35.28 x 35.28 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.8 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa @ 0.8 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.items-center 36.0x36.0 bg #ffffff @ 0.08 r 3.35544e+07px | button.inline-flex.items-center 36.0x36.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.items-center 35.3x35.3 bg #ffffff @ 0.08 r 3.35544e+07px |

Crops: `player-next-default.png`, `player-next-hover.png`, `player-next-focus-visible.png`, `player-next-pressed.png`.

#### player-repeat

Player repeat. The transport repeat toggle.

Page: explore. Selector: `button[aria-label="Repeat"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 35.28 x 35.28 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.8 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #fafafa @ 0.8 | 14 x 14, colour #fafafa | = | 13.72 x 13.72, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.items-center 36.0x36.0 bg #ffffff @ 0.08 r 3.35544e+07px | button.inline-flex.items-center 36.0x36.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.items-center 35.3x35.3 bg #ffffff @ 0.08 r 3.35544e+07px |

Crops: `player-repeat-default.png`, `player-repeat-hover.png`, `player-repeat-focus-visible.png`, `player-repeat-pressed.png`.

#### player-progress

Player progress. The seek rail across the player's top edge.

Page: explore. Selector: `thin wide rail inside the player bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 328 x 4 |
| Padding | 0px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #fafafa @ 0.15 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.relative.w-full 328.0x4.0 bg #fafafa @ 0.15 r 3.35544e+07px; div.absolute.inset-y-0 0.0x4.0 bg #fafafa @ 0.25 r 3.35544e+07px; div.absolute.inset-y-0 54.8x4.0 bg #fafafa r 3.35544e+07px |
| How | at rest |

Crops: `player-progress-default.png`.

#### player-volume

Player volume. The transport volume control.

Page: explore. Selector: `button[aria-label="Volume"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 35.28 x 35.28 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.8 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa @ 0.8 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.items-center 36.0x36.0 bg #ffffff @ 0.08 r 3.35544e+07px | button.inline-flex.items-center 36.0x36.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.items-center 35.3x35.3 bg #ffffff @ 0.08 r 3.35544e+07px |

Crops: `player-volume-default.png`, `player-volume-hover.png`, `player-volume-focus-visible.png`, `player-volume-pressed.png`.

#### player-queue

Player queue. The transport queue button.

Page: explore. Selector: `button[aria-label="Queue"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | 35.28 x 35.28 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.8 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa @ 0.8 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| Ancestor paint | 3 up div.@container/pb.pointer-events-auto bg #000000 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.16 0px 0px 0px 0.5px, #000000 @ 0.45 0px 1px 2px 0px, #000000 @ 0.4 0px 4px 8px -2px, #000000 @ 0.35 0px 12px 24px -6px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.items-center 36.0x36.0 bg #ffffff @ 0.08 r 3.35544e+07px | button.inline-flex.items-center 36.0x36.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.items-center 35.3x35.3 bg #ffffff @ 0.08 r 3.35544e+07px |

Crops: `player-queue-default.png`, `player-queue-hover.png`, `player-queue-focus-visible.png`, `player-queue-pressed.png`.

#### player-remix

Player remix. The transport Remix button; measured, never pressed (gated).

Page: explore. Selector: `transport Remix`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 31.36 x 31.36 | - | - | = |
| Padding | 0px | - | - | = |
| Gap | 0px | - | - | = |
| Border | none | - | - | = |
| Radius | 3.35544e+07px | - | - | = |
| Background | transparent | - | - | = |
| Box shadow | none | - | - | = |
| Outline | none | - | - | = |
| Font | Inter 16px/24px 400 | - | - | = |
| Letter spacing | normal | - | - | = |
| Colour | #ffffff @ 0.7 | - | - | #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | - | - | = |
| Cursor | pointer | - | - | = |
| Icon | 17.64 x 17.64, colour #ffffff @ 0.7 | - | - | 17.64 x 17.64, colour #ffffff |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is outside of the viewport Call log:   - waiting for locator('button[aria-label="Remix"]').visible().last().visible().first().visible().first()     - locator resolved to <button | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `player-remix-default.png`, `player-remix-pressed.png`.

### Charts

#### charts-title

Charts title. The charts page heading.

Page: charts. Selector: `h1 on /charts`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 842 x 83 |
| Padding | 0px 0px 8px 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | waldenburg 60px/60px 300 |
| Letter spacing | -1.5px |
| Colour | #ffffff |
| Text node | span.min-w-0.leading-tight: waldenburg 60px/75px 300, #ffffff, ls -1.5px |
| Transition | none |
| How | at rest |

Crops: `charts-title-default.png`.

#### chart-play

Play-all button. The white 40px Play pill at the top of the chart.

Page: charts. Selector: `button "Play"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.86 x 40 | = | = | 78.26 x 39.2 |
| Padding | 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff | #ffffff @ 0.9 | = | #ffffff @ 0.9 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | 15.68 x 15.68, colour #000000 |
| Painted layers | button.inline-flex.shrink-0 79.9x40.0 bg #ffffff r 3.35544e+07px | button.inline-flex.shrink-0 79.9x40.0 bg #ffffff @ 0.9 r 3.35544e+07px | button.inline-flex.shrink-0 79.9x40.0 bg #ffffff r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 78.3x39.2 bg #ffffff @ 0.9 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `chart-play-default.png`, `chart-play-hover.png`, `chart-play-focus-visible.png`, `chart-play-pressed.png`.

#### shuffle-btn

Shuffle button. The 40px Shuffle pill next to Play.

Page: charts. Selector: `button "Shuffle"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98.92 x 40 | = | = | 96.94 x 39.2 |
| Padding | 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff @ 0.15 | #ffffff @ 0.25 | = | #ffffff @ 0.25 |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(12px) | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | 15.68 x 15.68, colour #ffffff |
| Painted layers | button.inline-flex.shrink-0 98.9x40.0 bg #ffffff @ 0.15 r 3.35544e+07px | button.inline-flex.shrink-0 98.9x40.0 bg #ffffff @ 0.25 r 3.35544e+07px | button.inline-flex.shrink-0 98.9x40.0 bg #ffffff @ 0.15 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 96.9x39.2 bg #ffffff @ 0.25 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `shuffle-btn-default.png`, `shuffle-btn-hover.png`, `shuffle-btn-focus-visible.png`, `shuffle-btn-pressed.png`.

#### share-btn

Share button. The 32px Share pill; measured, never pressed.

Page: charts. Selector: `button "Share"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 82.33 x 32 | = | = | 80.68 x 31.36 |
| Padding | 0px 10px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff @ 0.15 | #ffffff @ 0.25 | = | #ffffff @ 0.25 |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(12px) | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | 15.68 x 15.68, colour #ffffff |
| Painted layers | button.inline-flex.shrink-0 82.3x32.0 bg #ffffff @ 0.15 r 3.35544e+07px | button.inline-flex.shrink-0 82.3x32.0 bg #ffffff @ 0.25 r 3.35544e+07px | button.inline-flex.shrink-0 82.3x32.0 bg #ffffff @ 0.15 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 80.7x31.4 bg #ffffff @ 0.25 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `share-btn-default.png`, `share-btn-hover.png`, `share-btn-focus-visible.png`, `share-btn-pressed.png`.

#### chart-row

Chart row. A ranked chart row (rank, art, title, artist, Like/Remix icons).

Page: charts. Selector: `row-height ancestor of an artist link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 810 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span.block.min-w-0: Inter 14px/17.5px 500, #fafafa | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #868686 | = | = | = |
| Painted layers | span.inline-flex.cursor-default 18.0x18.0 bg #171717 @ 0.6 border T:1px solid #ffffff @ 0.06 / R:1px solid #ffffff @ 0.06 / B:1px solid #ffffff @ 0.06 / L:1px solid #ffffff @ 0.06 r 3.35544e+07px | = | a.pointer-events-auto.min-w-0 55.7x16.3 outline 1px auto #ffffff @ 0.5 offset 1px; span.inline-flex.cursor-default 18.0x18.0 bg #171717 @ 0.6 border T:1px solid #ffffff @ 0.06 / R:1px solid #ffffff @ 0.06 / B:1px solid #ffffff @ 0.06 / L:1px solid #ffffff @ 0.06 r 3.35544e+07px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.group.relative bg #fafafa @ 0.05 | = | = |

Crops: `chart-row-default.png`, `chart-row-hover.png`, `chart-row-focus-visible.png`, `chart-row-pressed.png`.

#### like-btn

Like button. A row's 32px heart icon button; measured, never pressed (gated).

Page: charts. Selector: `button[aria-label="Like"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 31.36 x 31.36 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #ffffff @ 0.08 | = | #ffffff @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #868686 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.shrink-0 32.0x32.0 bg #ffffff @ 0.08 r 3.35544e+07px | button.inline-flex.shrink-0 32.0x32.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 31.4x31.4 bg #ffffff @ 0.08 r 3.35544e+07px |

Crops: `like-btn-default.png`, `like-btn-hover.png`, `like-btn-focus-visible.png`, `like-btn-pressed.png`.

#### remix-btn

Remix button. A row's 32px Remix icon button; measured, never pressed (gated).

Page: charts. Selector: `button[aria-label="Remix"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | 31.36 x 31.36 |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #1e1e1e | = | #1e1e1e |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #868686 | 16 x 16, colour #fafafa | = | 15.68 x 15.68, colour #fafafa |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.inline-flex.shrink-0 32.0x32.0 bg #1e1e1e r 3.35544e+07px | button.inline-flex.shrink-0 32.0x32.0 r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 31.4x31.4 bg #1e1e1e r 3.35544e+07px |

Crops: `remix-btn-default.png`, `remix-btn-hover.png`, `remix-btn-focus-visible.png`, `remix-btn-pressed.png`.

#### chart-artist

Chart artist link. An artist link inside a chart row.

Page: charts. Selector: `chart row a[href^="/artists/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 55.7 x 16.25 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #ffffff @ 0.5 offset 1px | = |
| Font | Inter 13px/16.25px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.pointer-events-auto.min-w-0 55.7x16.3 outline 1px auto #ffffff @ 0.5 offset 1px | = |

Crops: `chart-artist-default.png`, `chart-artist-hover.png`, `chart-artist-focus-visible.png`, `chart-artist-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The "Free to start. Pro when you're ready." heading.

Page: pricing. Selector: `pricing heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.text-balance.font-display: waldenburg 36px/42px 300, #fafafa, ls -0.72px |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-card

Plan card, Free. The Free plan card (dark surface, hairline border).

Page: pricing. Selector: `painted ancestor of the Free plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472 x 909.38 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | p.mb-3.font-medium: Inter 14px/20px 500, #fafafa |
| Transition | none |
| Icon | 16 x 16, colour #fafafa |
| Painted layers | div.relative.@2xl:row-span-5 472.0x909.4 bg #000000 r 24px; div.pointer-events-none.absolute 472.0x909.4 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.1 0px 0px 0px 0.5px inset, #000000 @ 0 0px 0px 0px 0px; div.relative.mr-2 88.0x88.0 bg #0a0a0a r 12px; div.cover-border.pointer-events-none 88.0x88.0 r 12px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.relative.mr-2 88.0x88.0 bg #0a0a0a r 12px; div.cover-border.pointer-events-none 88.0x88.0 r 12px shadow #ffffff @ 0.05 0px 0px 0px 1px inset |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-card-pro

Plan card, Pro. The Pro plan card — an inverted white island on the dark page.

Page: pricing. Selector: `painted ancestor of the Pro plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472 x 909.38 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | #fafafa |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.mb-3.font-medium: Inter 14px/20px 500, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.relative.@2xl:row-span-5 472.0x909.4 bg #fafafa r 24px; div.relative.mr-2 88.0x88.0 bg #0a0a0a r 12px; div.cover-border.pointer-events-none 88.0x88.0 r 12px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.relative.mr-2 88.0x88.0 bg #0a0a0a r 12px; div.cover-border.pointer-events-none 88.0x88.0 r 12px shadow #ffffff @ 0.05 0px 0px 0px 1px inset; div.relative.mr-2 88.0x88.0 bg #0a0a0a r 12px |
| How | at rest |

Crops: `plan-card-pro-default.png`.

#### plan-price

Plan price. The $9.99/month price figure on the Pro card.

Page: pricing. Selector: `Pro price figure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126.69 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | waldenburg 48px/52px 300 |
| Letter spacing | -0.96px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-feature

Plan feature row. A checked feature row inside a plan card.

Page: pricing. Selector: `plan feature li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 408 x 47 |
| Padding | 12px 0px |
| Gap | 12px |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.1; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/22px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| Icon | 16 x 16, colour #fafafa |
| Painted layers | li.flex.items-center 408.0x47.0 border B:1px solid #ffffff @ 0.1 |
| How | at rest |

Crops: `plan-feature-default.png`.

#### plan-cta-free

Plan CTA, Free. The Start-free pill on the Free card (white fill on dark); measured, never followed.

Page: pricing. Selector: `a "Start free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110.91 x 44 | = | = | 108.69 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fafafa | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #fafafa offset 4px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | transform, background-color 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 110.9x44.0 bg #fafafa r 3.35544e+07px | = | a.inline-flex.items-center 110.9x44.0 bg #fafafa r 3.35544e+07px outline 2px solid #fafafa offset 4px | a.inline-flex.items-center 108.7x43.1 bg #fafafa r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.85 | = | 0.85 |

Crops: `plan-cta-free-default.png`, `plan-cta-free-hover.png`, `plan-cta-free-focus-visible.png`, `plan-cta-free-pressed.png`.

#### plan-cta-pro

Plan CTA, Pro. The Get-Pro pill on the Pro card (dark fill on the white island); measured, never followed.

Page: pricing. Selector: `a "Get Pro"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.58 x 44 | = | = | 94.65 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #1e1e1e | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 2px solid #fafafa offset 4px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | transform, background-color 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 96.6x44.0 bg #1e1e1e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | = | a.inline-flex.items-center 96.6x44.0 bg #1e1e1e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px outline 2px solid #fafafa offset 4px | a.inline-flex.items-center 94.6x43.1 bg #1e1e1e r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-pro-default.png`, `plan-cta-pro-hover.png`, `plan-cta-pro-focus-visible.png`, `plan-cta-pro-pressed.png`.

#### faq-item

FAQ accordion. A pricing FAQ row (68px, border-t); the expanded state was opened by its own toggle.

Page: pricing. Selector: `pricing faq button`. States: default, hover, focus-visible, pressed, expanded.

| Property | default | hover | focus-visible | pressed | expanded |
|---|---|---|---|---|---|
| Size (w x h) | 960 x 68 | = | = | = | = |
| Padding | 20px 0px | = | = | = | = |
| Gap | 16px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 4px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = | = |
| Font | Inter 18px/28px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #fafafa | = | = | = | = |
| Text node | span.flex-auto: Inter 18px/28px 400, #fafafa | = | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 5.3 x 5.3, colour #868686, fill #000000 | 5.3 x 5.3, colour #fafafa, fill #000000 | = | 5.3 x 5.3, colour #fafafa, fill #000000 | 5.3 x 5.3, colour #fafafa, fill #000000 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own accordion toggle |
| Painted layers | - | = | button.flex.flex-1 960.0x68.0 r 4px outline 1px solid #ffffff offset 2px | = | = |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-focus-visible.png`, `faq-item-pressed.png`, `faq-item-expanded.png`.

#### faq-answer

FAQ row. The accordion item wrapper (question + answer region).

Page: pricing. Selector: `faq item wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 152 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.flex-auto: Inter 18px/28px 400, #fafafa |
| Transition | none |
| Icon | 5.3 x 5.3, colour #868686, fill #000000 |
| How | at rest |

Crops: `faq-answer-default.png`.

### Log in and sign up

#### auth-card

Auth column. The centred 384px log-in/sign-up column on the bare page; nothing submitted.

Page: login. Selector: `centred ancestor of the Google SSO button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | h2.text-pretty.font-display: waldenburg 30px/36px 300, #fafafa |
| Transition | none |
| Icon | 24.08 x 28, colour #fafafa |
| Painted layers | button.inline-flex.shrink-0 384.0x40.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; button.inline-flex.shrink-0 384.0x40.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; div.flex-1.border-border 173.2x1.0 border T:1px dashed #ffffff @ 0.1; div.flex-1.border-border 173.2x1.0 border T:1px dashed #ffffff @ 0.1; button.inline-flex.shrink-0 384.0x36.0 bg #1e1e1e r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.min-h-svh bg #000000 |
| How | at rest |

Crops: `auth-card-default.png`.

#### auth-title

Auth title. The "Log in or sign up" heading.

Page: login. Selector: `auth heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | waldenburg 30px/36px 300 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `auth-title-default.png`.

#### sso-google

Google SSO button. The Continue-with-Google button (surface-1 fill, 40px); measured, never pressed.

Page: login. Selector: `button "Continue with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 40 | = | = | 376.32 x 39.2 |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #222222 | #2b2b2b | = | #2b2b2b |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span: Inter 14px/20px 400, #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa | = | = | 15.68 x 15.68, colour #fafafa |
| Painted layers | button.inline-flex.shrink-0 384.0x40.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | button.inline-flex.shrink-0 384.0x40.0 bg #2b2b2b r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | button.inline-flex.shrink-0 384.0x40.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 376.3x39.2 bg #2b2b2b r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-google-default.png`, `sso-google-hover.png`, `sso-google-focus-visible.png`, `sso-google-pressed.png`.

#### sso-apple

Apple SSO button. The Continue-with-Apple button; measured, never pressed.

Page: login. Selector: `button "Continue with Apple"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 40 | = | = | 376.32 x 39.2 |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #222222 | #2b2b2b | = | #2b2b2b |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span: Inter 14px/20px 400, #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa | = | = | 15.68 x 15.68, colour #fafafa |
| Painted layers | button.inline-flex.shrink-0 384.0x40.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | button.inline-flex.shrink-0 384.0x40.0 bg #2b2b2b r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px | button.inline-flex.shrink-0 384.0x40.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 376.3x39.2 bg #2b2b2b r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-apple-default.png`, `sso-apple-hover.png`, `sso-apple-focus-visible.png`, `sso-apple-pressed.png`.

#### options-btn

Other-options toggle. The Show-other-options button that expands the email form in place; toggled for the expanded state, never submitted.

Page: login. Selector: `button "Show other options"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | 376.32 x 35.28 |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #1e1e1e | #2b2b2b | = | #2b2b2b |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.shrink-0 384.0x36.0 bg #1e1e1e r 3.35544e+07px | button.inline-flex.shrink-0 384.0x36.0 bg #2b2b2b r 3.35544e+07px | button.inline-flex.shrink-0 384.0x36.0 bg #1e1e1e r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 376.3x35.3 bg #2b2b2b r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `options-btn-default.png`, `options-btn-hover.png`, `options-btn-focus-visible.png`, `options-btn-pressed.png`.

#### email-field

Email field. The Enter-email-address input revealed by the options toggle; sample text was typed and deleted, nothing sent.

Page: login. Selector: `login input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 376 x 36 | = | = |
| Padding | 4px 14px | = | = |
| Border | 1px solid #ffffff @ 0.12 | 1px solid #ffffff @ 0.5 | 1px solid #ffffff @ 0.5 |
| Radius | 12px | = | = |
| Background | #ffffff @ 0.043 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #fafafa | = | = |
| Transition | color, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #868686, opacity 1 | = | = |
| Painted layers | input.bg-gray-alpha-50.file:text-foreground 376.0x36.0 bg #ffffff @ 0.043 border T:1px solid #ffffff @ 0.12 / R:1px solid #ffffff @ 0.12 / B:1px solid #ffffff @ 0.12 / L:1px solid #ffffff @ 0.12 r 12px | input.bg-gray-alpha-50.file:text-foreground 376.0x36.0 bg #ffffff @ 0.043 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 12px | input.bg-gray-alpha-50.file:text-foreground 376.0x36.0 bg #ffffff @ 0.043 border T:1px solid #ffffff @ 0.5 / R:1px solid #ffffff @ 0.5 / B:1px solid #ffffff @ 0.5 / L:1px solid #ffffff @ 0.5 r 12px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### tos-checkbox

Terms checkbox. The agree-to-Terms checkbox; measured, never checked.

Page: login. Selector: `login checkbox`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #ffffff @ 0.2 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.peer.border-outline 16.0x16.0 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px | = | button.peer.border-outline 16.0x16.0 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 4px outline 1px solid #ffffff offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tos-checkbox-default.png`, `tos-checkbox-hover.png`, `tos-checkbox-focus-visible.png`, `tos-checkbox-pressed.png`.

#### continue-btn

Continue button. The Continue-with-Email submit (disabled until the box is checked); measured, never pressed.

Page: login. Selector: `button "Continue with Email"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 376 x 36 | = | - | 368.48 x 35.28 |
| Padding | 0px 14px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | #fafafa | = | - | #faf8f7 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0a0a0a | = | - | = |
| Text node | span: Inter 14px/20px 400, #0a0a0a | = | - | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Opacity | 0.4 | = | - | = |
| Cursor | default | = | - | = |
| Painted layers | button.inline-flex.shrink-0 376.0x36.0 bg #fafafa r 3.35544e+07px | = | - | button.inline-flex.shrink-0 368.5x35.3 bg #faf8f7 r 3.35544e+07px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `continue-btn-default.png`, `continue-btn-hover.png`, `continue-btn-pressed.png`.

#### tos-link

Terms link. An underlined legal link; measured, never followed.

Page: login. Selector: `a "Terms of Service"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.66 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #ffffff @ 0.5 offset 1px | = |
| Font | Inter 12px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.underline.transition-colors 96.7x15.0 outline 1px auto #ffffff @ 0.5 offset 1px | = |

Crops: `tos-link-default.png`, `tos-link-hover.png`, `tos-link-focus-visible.png`, `tos-link-pressed.png`.

#### tryit-link

Try-it link. The muted Try-it-first link under the form.

Page: login. Selector: `a "Try it first"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 63.27 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #ffffff @ 0.5 offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #868686 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-muted-foreground.underline-offset-4 63.3x20.0 outline 1px auto #ffffff @ 0.5 offset 1px | = |

Crops: `tryit-link-default.png`, `tryit-link-hover.png`, `tryit-link-focus-visible.png`, `tryit-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The compact header at 390: mark, Search, Start free, menu.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 52 |
| Padding | 0px 10px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.95 |
| Box shadow | none |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | button.inline-flex.shrink-0: Inter 14px/20px 400, #0a0a0a |
| Transition | none |
| Icon | 0 x 0, colour #868686 |
| Painted layers | header.h-13.shrink-0 390.0x52.0 bg #000000 @ 0.95; button.font-normal.outline-hidden 32.0x32.0 bg #151515 r 3.35544e+07px; button.inline-flex.shrink-0 0.0x0.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; button.inline-flex.shrink-0 85.7x32.0 bg #fafafa r 3.35544e+07px; span.absolute.left-0 18.0x1.5 bg #fafafa r 3.35544e+07px; span.absolute.left-0 18.0x1.5 bg #fafafa r 3.35544e+07px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-logo

Mobile logo. The mark at 390.

Page: mobile. Selector: `mobile logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 29.2 x 32 |
| Padding | 0px 6px |
| Border | none |
| Radius | 10px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| Cursor | pointer |
| Icon | 17.2 x 20, colour #fafafa |
| Ancestor paint | 1 up header.h-13.shrink-0 bg #000000 @ 0.95 |
| How | at rest |

Crops: `m-logo-default.png`.

#### m-search-btn

Mobile search button. The header search icon at 390.

Page: mobile. Selector: `button[aria-label="Open search"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #151515 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18.39 x 18.39, colour #fafafa | = | = | = |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.font-normal.outline-hidden 32.0x32.0 bg #151515 r 3.35544e+07px | = | button.font-normal.outline-hidden 32.0x32.0 bg #151515 r 3.35544e+07px outline 1px solid #ffffff offset 2px | = |
| Ancestor paint | 1 up header.h-13.shrink-0 bg #000000 @ 0.95 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-search-btn-default.png`, `m-search-btn-hover.png`, `m-search-btn-focus-visible.png`, `m-search-btn-pressed.png`.

#### m-cta

Mobile CTA. The Start-free pill at 390.

Page: mobile. Selector: `"Start free" at 390`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.66 x 32 | = | = | 83.94 x 31.36 |
| Padding | 0px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fafafa | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0a0a0a | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 85.6562px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.inline-flex.shrink-0 85.7x32.0 bg #fafafa r 3.35544e+07px | = | button.inline-flex.shrink-0 85.7x32.0 bg #fafafa r 3.35544e+07px outline 1px solid #ffffff offset 2px | button.inline-flex.shrink-0 83.9x31.4 bg #fafafa r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

#### m-hero

Mobile headline. The "Make music yours." headline at 390.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 349.08 x 35.52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | waldenburg 32.292px/35.5212px 300 |
| Letter spacing | -0.64584px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-composer

Mobile composer. The prompt field at 390.

Page: mobile. Selector: `composer input at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 258 x 36 |
| Padding | 0px 8px 0px 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| Cursor | text |
| Placeholder | #fafafa, opacity 1 |
| How | at rest |

Crops: `m-composer-default.png`.

#### m-chip

Mobile prompt chip. A suggestion chip at 390.

Page: mobile. Selector: `prompt chip at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 82.53 x 40 |
| Padding | 0px 14px |
| Gap | 0px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #ffffff @ 0.08 |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/16px 400 |
| Letter spacing | normal |
| Colour | #868686 |
| Transition | background-color, color, transform 0.15s cubic-bezier(0, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | button.font-normal.focus-visible:focus-ring 82.5x40.0 bg #ffffff @ 0.08 r 3.35544e+07px |
| How | at rest |

Crops: `m-chip-default.png`.

#### m-tab-bar

Mobile tab bar. The bottom tab bar pinned to the viewport (Explore / Create / Library).

Page: mobile. Selector: `bottom tab bar at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | T: 1px solid #ffffff @ 0.1; R: none; B: none; L: none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.text-[11px].leading-none: Inter 11px/11px 600, #fafafa |
| Transition | none |
| Icon | 22 x 22, colour #fafafa |
| Painted layers | nav.flex.h-14 390.0x56.0 bg #000000 border T:1px solid #ffffff @ 0.1; button.outline-hidden.focus-visible:focus-ring 109.0x40.0 bg #fafafa r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px |
| Ancestor paint | 1 up div.relative.z-46 bg #000000 |
| How | at rest |

Crops: `m-tab-bar-default.png`.

#### m-tab

Mobile tab. A tab-bar item (the selected Explore tab).

Page: mobile. Selector: `tab bar item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 132.5 x 55 | = | = | 124.55 x 51.7 |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #ffffff @ 0.5 offset 1px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Text node | span.text-[11px].leading-none: Inter 11px/11px 600, #fafafa | = | = | = |
| Transition | transform, translate, scale, rotate 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #fafafa | = | = | 20.68 x 20.68, colour #fafafa |
| Ancestor paint | 1 up nav.flex.h-14 bg #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.flex.h-full 132.5x55.0 outline 1px auto #ffffff @ 0.5 offset 1px | = |

Crops: `m-tab-default.png`, `m-tab-hover.png`, `m-tab-focus-visible.png`, `m-tab-pressed.png`.

#### m-menu-btn

Mobile menu button. The header hamburger.

Page: mobile. Selector: `button[aria-label="Open menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 6px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | 1px solid #ffffff offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | background-color, color, box-shadow, border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.absolute.left-0 18.0x1.5 bg #fafafa r 3.35544e+07px; span.absolute.left-0 18.0x1.5 bg #fafafa r 3.35544e+07px | = | button.inline-flex.items-center 36.0x36.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 1px solid #ffffff offset 2px; span.absolute.left-0 18.0x1.5 bg #fafafa r 3.35544e+07px; span.absolute.left-0 18.0x1.5 bg #fafafa r 3.35544e+07px | = |
| Ancestor paint | 1 up header.h-13.shrink-0 bg #000000 @ 0.95 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`.

#### m-menu-sheet

Mobile menu, open. The fullscreen nav sheet the hamburger opens (measured, then dismissed).

Page: mobile. Selector: `mobile menu dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | button.inline-flex.shrink-0: Inter 14px/20px 400, #0a0a0a |
| Transition | none |
| Icon | 17.2 x 20, colour #fafafa |
| Painted layers | div.flex.h-[3.25rem] 390.0x52.0 bg #000000; button.inline-flex.shrink-0 0.0x0.0 bg #222222 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.07 0px 0px 0px 1px, #000000 @ 0.5 0px 1px 2px 0px; button.inline-flex.shrink-0 85.7x32.0 bg #fafafa r 3.35544e+07px; span.absolute.left-0 13.8x13.8 bg #fafafa r 3.35544e+07px; span.absolute.left-0 13.8x13.8 bg #fafafa r 3.35544e+07px; nav.relative.flex 382.0x776.0 bg #2e2e2e r 20px shadow #ffffff @ 0.08 0px 0px 0px 1px, #000000 @ 0.3 0px 10px 20px 1px, #000000 @ 0.4 0px 48px 48px -24px |
| Ancestor paint | 1 up body bg #000000 |
| How | at rest |

Crops: `m-menu-sheet-default.png`.

#### m-menu-link

Mobile menu link. A link inside the open nav sheet.

Page: mobile. Selector: `sheet link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 366 x 44 | = | = | = |
| Padding | 12px 12px 12px 16px | = | = | = |
| Gap | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | 1px solid #ffffff offset 2px | 1px solid #ffffff offset 2px |
| Font | Inter 12px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #868686 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.focus-visible:focus-ring.motion-reduce:active:scale-100 366.0x44.0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 1px solid #ffffff offset 2px | button.focus-visible:focus-ring.motion-reduce:active:scale-100 366.0x44.0 r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px outline 1px solid #ffffff offset 2px |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

## Transitions declared in the readable stylesheets

elevenmusic.io serves its Next.js CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- charts: `unset`, `opacity 1.1s cubic-bezier(0.45, 0, 0.25, 1), filter 1.1s cubic-bezier(0.45, 0, 0.25, 1)`, `opacity 0.3s ease-out`, `background-color 0.15s`, `background-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`

- explore: `unset`, `opacity 1.1s cubic-bezier(0.45, 0, 0.25, 1), filter 1.1s cubic-bezier(0.45, 0, 0.25, 1)`, `opacity 0.3s ease-out`, `background-color 0.15s`, `background-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`

- home: `unset`, `opacity 1.1s cubic-bezier(0.45, 0, 0.25, 1), filter 1.1s cubic-bezier(0.45, 0, 0.25, 1)`, `opacity 0.3s ease-out`, `background-color 0.15s`, `background-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`

- login: `unset`, `opacity 1.1s cubic-bezier(0.45, 0, 0.25, 1), filter 1.1s cubic-bezier(0.45, 0, 0.25, 1)`, `opacity 0.3s ease-out`, `background-color 0.15s`, `background-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`

- pricing: `unset`, `opacity 1.1s cubic-bezier(0.45, 0, 0.25, 1), filter 1.1s cubic-bezier(0.45, 0, 0.25, 1)`, `opacity 0.3s ease-out`, `background-color 0.15s`, `background-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.15s cubic-bezier(0.23, 1, 0.32, 1), color 0.15s cubic-bezier(0.23, 1, 0.32, 1), transform 0.15s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`
