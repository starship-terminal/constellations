# Component measurements

Computed styles read from www.doctronic.ai on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844; the Dark group on the site's real `data-theme="dark"` theme), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Marketing top bar. The bar over the home page: wordmark, Log in, Sign up and the menu button that opens the site-menu drawer.

Page: home. Selector: `[class*="_marketingHeader"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #1b1b18, ls -0.24px |
| Transition | transform 0.25s ease |
| Icon | 115.89 x 22, colour #1b1b18 |
| Painted layers | div.content.contentShrink 1440.0x72.0 bg #fdfdf7; span.content 59.1x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 65.6x32.8 bg #0b0b0a r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; div.openMenuWrapper 57.0x40.0 border L:1px dashed #1b1b18 @ 0.08 |
| Ancestor paint | 1 up main.layoutContent bg #fdfdf7 |
| How | at rest |

Crops: `header-default.png`.

#### signup-button

Sign up button. The dark pill at the right of the top bar. Measured, never pressed.

Page: home. Selector: `top bar "Sign up"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.64 x 34.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3c83f6 offset 0px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 65.6406px x 43.9844px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content 65.6x32.8 bg #0b0b0a r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 65.6x32.8 bg #272725 r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | button.button.primary 65.6x34.8 r 32px outline 2px solid #3c83f6 offset 0px; span.content 65.6x32.8 bg #0b0b0a r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 64.3x32.1 bg #1b1b18 r 32px; span.shimmer 64.3x32.1 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-button-default.png`, `signup-button-hover.png`, `signup-button-focus-visible.png`, `signup-button-pressed.png`.

#### login-button

Log in button. The quiet secondary button beside Sign up. Measured, never pressed.

Page: home. Selector: `top bar "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 59.11 x 34.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3c83f6 offset 0px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #1b1b18, ls -0.24px | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px | = | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 59.1094px x 43.9844px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content 59.1x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 59.1x34.8 bg #0b0b0a border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | button.button.secondary 59.1x34.8 r 32px outline 2px solid #3c83f6 offset 0px; span.content 59.1x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 57.9x34.1 bg #1b1b18 border T:1px solid #1b1b18 / R:1px solid #1b1b18 / B:1px solid #1b1b18 / L:1px solid #1b1b18 r 32px; span.shimmer 56.0x32.1 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-button-default.png`, `login-button-hover.png`, `login-button-focus-visible.png`, `login-button-pressed.png`.

#### menu-button

Site-menu button. aria-label "open sidebar": opens the site-menu drawer. The drawer was opened and measured below, then dismissed with Escape.

Page: home. Selector: `[class*="_expandHitArea"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #2463eb 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1b1b18 | = | = | = |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | span.surface 40.0x40.0 bg #f5f5f0 r 100px | button.buttonBase.expandHitArea 40.0x40.0 r 100px shadow #2463eb 0px 0px 0px 2px | = |

Crops: `menu-button-default.png`, `menu-button-hover.png`, `menu-button-focus-visible.png`, `menu-button-pressed.png`.

#### logo

Wordmark.

Page: home. Selector: `top bar home link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 620 x 25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Transition | none |
| Icon | 115.89 x 22, colour #1b1b18 |
| Ancestor paint | 1 up div.content.contentShrink bg #fdfdf7 |
| How | at rest |

Crops: `logo-default.png`.

#### menu-drawer

Site-menu drawer. The left drawer the menu button opens: Dashboard links (New chat, Explore, Health record, Health information), then a Company group (About us, Careers, Partnerships, …).

Page: home. Selector: `section[class*="_dialog"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 320 x 852 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.label12.colorDefault: geist 12px/16.8px 500, #1b1b18 @ 0.6, ls -0.24px |
| Transition | none |
| Icon | 115.89 x 22, colour #1b1b18 |
| Painted layers | div.divider 320.0x1.0 border B:1px dashed #1b1b18 @ 0.08; div.container 320.0x51.8 border T:1px dashed #1b1b18 @ 0.08; span.content 154.0x32.8 bg #0b0b0a r 32px; span.shimmer 154.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 154.0x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 152.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| Ancestor paint | 1 up div.sidebar bg #fdfdf7 shadow #000000 @ 0.05 0px 1px 12px 0px |
| How | at rest |

Crops: `menu-drawer-default.png`.

#### menu-item

Menu drawer item. A row in the site-menu drawer. Measured while the drawer was open; links were never followed.

Page: home. Selector: `[class*="_menuItem"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 38.39 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | 4px | 4px |
| Background | transparent | #f5f5f0 | = | #f5f5f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1d4fd7 offset 2px | 2px solid #1d4fd7 offset 2px |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | p.label16.colorDefault: geist 16px/22.4px 500, #1b1b18, ls -0.32px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b18 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.menuItem.menuItemButton 320.0x38.4 bg #f5f5f0 r 8px | button.menuItem.menuItemButton 320.0x38.4 r 4px outline 2px solid #1d4fd7 offset 2px | button.menuItem.menuItemButton 320.0x38.4 bg #f5f5f0 r 4px outline 2px solid #1d4fd7 offset 2px |

Crops: `menu-item-default.png`, `menu-item-hover.png`, `menu-item-focus-visible.png`, `menu-item-pressed.png`.

#### menu-item-expand

Menu drawer expandable. A submenu row (About Chat / Health information) with a chevron. Measured, never expanded.

Page: home. Selector: `[class*="_menuItemButton"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 320 x 38.39 | = |
| Padding | 8px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | transparent | #f5f5f0 |
| Box shadow | none | = |
| Outline | 2px solid #1d4fd7 offset 2px | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b18 | = |
| Text node | p.label16.colorDefault: geist 16px/22.4px 500, #1b1b18, ls -0.32px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #1b1b18 | = |
| Painted layers | button.menuItem.menuItemButton 320.0x38.4 r 4px outline 2px solid #1d4fd7 offset 2px | button.menuItem.menuItemButton 320.0x38.4 bg #f5f5f0 r 4px outline 2px solid #1d4fd7 offset 2px |
| How | at rest | mouse hover |

Crops: `menu-item-expand-default.png`, `menu-item-expand-hover.png`.

### Home: hero and marketing

#### hero

Home hero. The first band: the Fraunces display headline, the "What brings you in?" prompt and the chat input card.

Page: home. Selector: `textarea ancestor holding h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 548 x 421.5 |
| Padding | 0px |
| Gap | 64px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | h1.display32.colorDefault: fraunces 48px/56.16px 400, #1b1b18, ls -0.48px |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | div.content 150.5x36.6 bg #d9ff80 @ 0.5 r 16px 18px 18px 2px; div::before.material 148.453pxx34.5938px image linear-gradient(155deg, #ffffff @ 0.06 0%, #000000 @ 0.06 50%, #ffffff @ 0.06 100%) r 16px 18px 18px 2px; div::after.material 150.453pxx36.5938px bg #808080 @ 0 r 16px 18px 18px 2px; div.edgeReflection 186.5x72.6 border T:18px solid #000000 @ 0 / R:18px solid #000000 @ 0 / B:18px solid #000000 @ 0 / L:18px solid #000000 @ 0 r 34px 36px 36px 20px; div.refraction 150.5x36.6 border T:6px solid #000000 @ 0 / R:6px solid #000000 @ 0 / B:6px solid #000000 @ 0 / L:6px solid #000000 @ 0 r 16px 18px 18px 2px; div.inputContainer 548.0x147.4 bg #ffffff border T:1px solid #1b1b18 @ 0.08 / R:1px solid #1b1b18 @ 0.08 / B:1px solid #1b1b18 @ 0.08 / L:1px solid #1b1b18 @ 0.08 r 16px shadow #000000 @ 0.06 0px 2px 24px 0px |
| Ancestor paint | 1 up section.section bg #fdfdf7 |
| How | at rest |

Crops: `hero-default.png`.

#### hero-title

Hero headline. "Hi, I'm Doctronic" in the Fraunces display face with the dashed underline.

Page: home. Selector: `hero h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 378.56 x 56.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraunces 48px/56.16px 400 |
| Letter spacing | -0.48px |
| Colour | #1b1b18 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### anon-label

Anonymous label. The "Anonymous" session badge inside the chat field.

Page: home. Selector: `"Anonymous" badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 105.56 x 32 |
| Padding | 3px 8px |
| Gap | 4px |
| Border | 1px dashed #1b1b18 @ 0.08 |
| Radius | 34px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.label12.colorDefault: geist 12px/16.8px 500, #2463eb, ls -0.24px |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #000000 |
| Painted layers | button.badgeButton 105.6x32.0 border T:1px dashed #1b1b18 @ 0.08 / R:1px dashed #1b1b18 @ 0.08 / B:1px dashed #1b1b18 @ 0.08 / L:1px dashed #1b1b18 @ 0.08 r 34px |
| Ancestor paint | 3 up div.inputContainer bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px |
| How | at rest |

Crops: `anon-label-default.png`.

#### hero-input-card

Hero chat field. The input card the page is built around: raised white surface, soft border, the textarea and the Start chat button. Measured, never submitted.

Page: home. Selector: `[class*="_inputContainer"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 548 x 147.38 | = |
| Padding | 16px | = |
| Border | 1px solid #1b1b18 @ 0.08 | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0.06 0px 2px 24px 0px | = |
| Outline | none | = |
| Font | -apple-system 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b18 | = |
| Text node | p.label12.colorDefault: geist 12px/16.8px 500, #2463eb, ls -0.24px | = |
| Transition | none | = |
| Icon | 20 x 20, colour #000000 | = |
| Painted layers | div.inputContainer 548.0x147.4 bg #ffffff border T:1px solid #1b1b18 @ 0.08 / R:1px solid #1b1b18 @ 0.08 / B:1px solid #1b1b18 @ 0.08 / L:1px solid #1b1b18 @ 0.08 r 16px shadow #000000 @ 0.06 0px 2px 24px 0px; button.badgeButton 105.6x32.0 border T:1px dashed #1b1b18 @ 0.08 / R:1px dashed #1b1b18 @ 0.08 / B:1px dashed #1b1b18 @ 0.08 / L:1px dashed #1b1b18 @ 0.08 r 34px; span.content.submitButtonContent 136.4x43.6 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 136.4x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | = |
| How | at rest | mouse hover |

Crops: `hero-input-card-default.png`, `hero-input-card-hover.png`.

#### hero-textarea

Hero textarea. "Describe symptom or ask any health questions…" — text was typed and deleted; nothing was sent.

Page: home. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 514 x 58.78 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | geist 14px/19.6px 400 | = | = |
| Letter spacing | -0.28px | = | = |
| Colour | #1b1b18 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #1b1b18 @ 0.73, opacity 1 | = | = |
| Ancestor paint | 2 up div.inputContainer bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px | 2 up div.inputContainer bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px outline 2px solid #3c83f6 | 2 up div.inputContainer bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px outline 2px solid #3c83f6 |
| How | at rest | clicked into the field | typed "I have a headache since this morning", then deleted; nothing sent |

Crops: `hero-textarea-default.png`, `hero-textarea-focused.png`, `hero-textarea-filled.png`.

#### start-chat-button

Start chat button. The accent-blue submit control. Measured, never pressed — pressing would start a chat.

Page: home. Selector: `[class*="_submitButton"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 136.36 x 43.59 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 52px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #2463eb @ 0.39 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | span.heading14.colorInherit: geist 14px/19.6px 600, #ffffff, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | 15.68 x 15.68, colour #ffffff |
| ::before | 136.359px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content.submitButtonContent 136.4x43.6 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 136.4x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | span.content.submitButtonContent 136.4x43.6 bg #1d4fd7 r 52px shadow #2463eb @ 0.5 0px 6px 10px 0px; span.shimmer 136.4x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | button.button.hero 136.4x43.6 r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px; span.content.submitButtonContent 136.4x43.6 bg #2463eb r 52px; span.shimmer 136.4x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | span.content.submitButtonContent 133.6x42.7 bg #1e3fae r 52px; span.shimmer 133.6x42.7 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px |
| Ancestor paint | 2 up div.inputContainer bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px | = | 2 up div.inputContainer bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px outline 2px solid #3c83f6 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `start-chat-button-default.png`, `start-chat-button-hover.png`, `start-chat-button-focus-visible.png`, `start-chat-button-pressed.png`.

#### brings-pill

"What brings you in?" pill.

Page: home. Selector: `[class*="_pill"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126.45 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | geist 14px/19.6px 600 |
| Letter spacing | -0.28px |
| Colour | #1b1b18 |
| Transition | none |
| Ancestor paint | 1 up div.content bg #d9ff80 @ 0.5 |
| How | at rest |

Crops: `brings-pill-default.png`.

#### hipaa-badge

HIPAA badge.

Page: home. Selector: `[class*="_hipaaBadge"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 90.39 x 16 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 @ 0.6 |
| Text node | span.label10.colorSubtle: geist 10px/14px 500, #1b1b18 @ 0.6, ls -0.2px |
| Transition | none |
| Icon | 16 x 16, colour #1b1b18 @ 0.6 |
| How | at rest |

Crops: `hipaa-badge-default.png`.

#### feature-card

Feature card.

Page: home. Selector: `[class*="_featureCardBlock"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1233 x 274 | = |
| Padding | 24px 48px | = |
| Gap | 15px | = |
| Border | 1px solid #1b1b18 @ 0.08 | = |
| Radius | 32px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b18 | = |
| Text node | blockquote.display24.colorDefault: fraunces 24px/28.08px 400, #1b1b18, ls -0.24px | = |
| Transition | none | = |
| Icon | 24 x 24, colour #797972 | = |
| Painted layers | article.card 1233.0x274.0 border T:1px solid #1b1b18 @ 0.08 / R:1px solid #1b1b18 @ 0.08 / B:1px solid #1b1b18 @ 0.08 / L:1px solid #1b1b18 @ 0.08 r 32px; hr.divider 608.0x1.0 border T:1px dashed #e4e4dc; span.dot.dotActive 18.0x8.0 bg #1b1b18 r 4px; span.dot 8.0x8.0 bg #e4e4dc r 50%; span.dot 8.0x8.0 bg #e4e4dc r 50%; span.dot 8.0x8.0 bg #e4e4dc r 50% | = |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### pricing-card

Pricing card. The plan card with the $ price and the highlighted callout.

Page: home. Selector: `[class*="_card"] with $`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 384.34 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | span.monoBold16.colorDefault: geistMono 16px/22.4px 600, #3c3c39, ls -0.32px |
| Transition | none |
| Icon | 115.89 x 22, colour #1b1b18 |
| Painted layers | div.root.card 640.0x384.3 bg #fdfdf7 r 24px shadow #000000 @ 0.15 0px 15px 30px -10px, #ffffff @ 0.8 0px 1px 1px 0px inset, #000000 @ 0.05 0px -1px 1px 0px inset, #ffffff @ 0.8 1px 0px 1px 0px inset, #000000 @ 0.05 -1px 0px 1px 0px inset, #ffffff @ 0.4 0px 0px 20px 0px inset; div::before.root.card 640pxx384.344px image linear-gradient(115deg, #ffffff @ 0 0%, #ffffff @ 0 25%, #ff9ad1 @ 0.3 35%, #80d0ff @ 0.3  r 24px; div.holoLayer 640.0x384.3 image linear-gradient(115deg, #ffffff @ 0 0%, #ffffff @ 0 25%, #ff9ad1 @ 0.3 35%, #80d0ff @ 0.3  r 24px; div.textureLayer 640.0x384.3 image url(data:…)' opacity='0.2'/%3E%3C/svg%3E") r 24px; div.glareLayer 640.0x384.3 image radial-gradient(circle, #ffffff @ 0.9 10%, #ffffff @ 0 50%) r 24px; span.leader 365.1x14.0 image radial-gradient(circle, #a7a7a0 1px, #000000 @ 0 1.5px) |
| How | at rest |

Crops: `pricing-card-default.png`.

#### price

Price figure.

Page: home. Selector: `[class*="_price"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 63.39 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | geist 16px/22.4px 400 |
| Letter spacing | -0.32px |
| Colour | #2463eb |
| Transition | none |
| How | at rest |

Crops: `price-default.png`.

#### testimonial-arrow

Testimonial arrow.

Page: home. Selector: `[class*="_arrow"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 100px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | -apple-system 16px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1b1b18 @ 0.3 | = | - | = |
| Transition | none | = | - | = |
| Cursor | not-allowed | = | - | = |
| Icon | 24 x 24, colour #797972 | = | - | = |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `testimonial-arrow-default.png`, `testimonial-arrow-hover.png`, `testimonial-arrow-pressed.png`.

#### watch-button

Watch testimonial button. Measured, never pressed.

Page: home. Selector: `[class*="_secondary"] "Watch…"`. States: .

Not found on the page at capture time.

#### oath-band

Hippocratic oath band.

Page: home. Selector: `[class*="_oathSection"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 490.94 |
| Padding | 0px 0px 32px 0px |
| Gap | 48px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.heading18.colorDefault: geist 28px/39.2px 600, #1b1b18, ls -0.56px |
| Transition | none |
| Icon | 167 x 167, colour #1b1b18 |
| How | at rest |

Crops: `oath-band-default.png`.

#### quote-card

Testimonial card.

Page: home. Selector: `[class*="_quote"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 608 x 112.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraunces 24px/28.08px 400 |
| Letter spacing | -0.24px |
| Colour | #1b1b18 |
| Transition | none |
| How | at rest |

Crops: `quote-card-default.png`.

#### rating-group

Trustpilot rating block.

Page: home. Selector: `[class*="_ratingGroup"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 153.19 x 14 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | span.label10.colorSubtle: geist 10px/14px 500, #1b1b18 @ 0.6, ls -0.2px |
| Transition | none |
| How | at rest |

Crops: `rating-group-default.png`.

#### condensed-form

Condensed chat form. The slim repeat of the chat field near the footer: one textarea and a Get started button.

Page: home. Selector: `[class*="_condensedForm"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 72 |
| Padding | 12px 12px 12px 24px |
| Gap | 12px |
| Border | none |
| Radius | 48px |
| Background | #fdfdf7 |
| Box shadow | #000000 @ 0.1 0px 5px 32px 0px |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Transition | border-radius 0.2s ease-out |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | form.condensedForm 480.0x72.0 bg #fdfdf7 r 48px shadow #000000 @ 0.1 0px 5px 32px 0px; span.content 48.0x48.0 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 48.0x48.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px |
| How | at rest |

Crops: `condensed-form-default.png`.

#### condensed-button

Get started button. Measured, never pressed.

Page: home. Selector: `[class*="_condensedButton"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | - | - | = |
| Padding | 0px | - | - | = |
| Border | none | - | - | = |
| Radius | 52px | - | - | = |
| Background | transparent | - | - | = |
| Box shadow | none | - | - | = |
| Outline | none | - | - | = |
| Font | -apple-system 16px/normal 400 | - | - | = |
| Letter spacing | normal | - | - | = |
| Colour | #1b1b18 | - | - | = |
| Transition | none | - | - | = |
| Cursor | pointer | - | - | = |
| Icon | 24 x 24, colour #ffffff | - | - | 22.8 x 22.8, colour #ffffff |
| ::before | 48px x 48px, absolute, bg #000000 @ 0, radius 0px | - | - | = |
| Painted layers | span.content 48.0x48.0 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 48.0x48.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | - | - | span.content 45.6x45.6 bg #1e3fae r 52px; span.shimmer 45.6x45.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px |
| Ancestor paint | 1 up form.condensedForm bg #fdfdf7 shadow #000000 @ 0.1 0px 5px 32px 0px | - | - | = |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is outside of the viewport Call log:   - waiting for locator('[class*="_condensedButton"]').first().or(locator('[data-m-mark="__none__"]')).visible().first().visible().first()   | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `condensed-button-default.png`, `condensed-button-pressed.png`.

#### footer

Footer. The deep page footer: link columns, legal row and the "Made in" note.

Page: home. Selector: `last footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1414.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.heading18.colorDefault: geist 18px/25.2px 600, #1b1b18, ls -0.36px |
| Transition | none |
| Icon | 147.5 x 28, colour #1b1b18 |
| Painted layers | div.gradient 1440.0x1414.5 image linear-gradient(#fdfdf7 0%, #e1efe3 100%); span.content 59.1x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 65.6x32.8 bg #0b0b0a r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; div.divider 1240.0x2.0 border T:2px dashed #1b1b18 @ 0.08 |
| Ancestor paint | 1 up main.layoutContent bg #fdfdf7 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-legal

Legal line.

Page: home. Selector: `[class*="_legal"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 296.28 x 33.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.body12.colorDefault: geist 12px/16.8px 400, #a7a7a0, ls -0.24px |
| Transition | none |
| How | at rest |

Crops: `footer-legal-default.png`.

#### pause-control

Animation pause control. The round control pinned bottom-right that pauses the page's motion. Measured, never pressed.

Page: home. Selector: `button[aria-label*="pause"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | 159 x 40 | = | 159 x 40 |
| Padding | 8px 32px 8px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | #f5f5f0 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3c83f6 offset 2px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #797972 | #1b1b18 | #1b1b18 | #1b1b18 |
| Transition | background-color, color 0.15s, 0.15s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #797972 | 24 x 24, colour #1b1b18 | 24 x 24, colour #1b1b18 | 24 x 24, colour #1b1b18 |
| Painted layers | button.button 40.0x40.0 bg #f5f5f0 r 32px | button.button 159.0x40.0 bg #f5f5f0 r 32px | button.button 40.0x40.0 bg #f5f5f0 r 32px outline 2px solid #3c83f6 offset 2px | button.button 159.0x40.0 bg #f5f5f0 r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Text node | - | span.label14.colorInherit: geist 14px/19.6px 500, #1b1b18, ls -0.28px | = | span.label14.colorInherit: geist 14px/19.6px 500, #1b1b18, ls -0.28px |

Crops: `pause-control-default.png`, `pause-control-hover.png`, `pause-control-focus-visible.png`, `pause-control-pressed.png`.

#### footer-social-icon

Footer social icon link. An aria-labelled icon link in the footer's social row (e.g. "Doctronic on Instagram"). Measured, never followed.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | #2463eb | #2463eb | #2463eb |
| Transition | color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b18 | 16 x 16, colour #2463eb | 16 x 16, colour #2463eb | 16 x 16, colour #2463eb |
| ::before | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.link 16.0x16.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-social-icon-default.png`, `footer-social-icon-hover.png`, `footer-social-icon-focus-visible.png`, `footer-social-icon-pressed.png`.

#### footer-legal-link

Footer legal link. Privacy Policy / Terms of Service in the legal row. Measured, never followed.

Page: home. Selector: `footer legal link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.63 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | #2463eb | #2463eb | #2463eb |
| Text node | span.body12.colorInherit: geist 12px/16.8px 400, #1b1b18, ls -0.24px | span.body12.colorInherit: geist 12px/16.8px 400, #2463eb, ls -0.24px | span.body12.colorInherit: geist 12px/16.8px 400, #2463eb, ls -0.24px | span.body12.colorInherit: geist 12px/16.8px 400, #2463eb, ls -0.24px |
| Transition | color 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.link 72.6x24.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-legal-link-default.png`, `footer-legal-link-hover.png`, `footer-legal-link-focus-visible.png`, `footer-legal-link-pressed.png`.

### Chat surface

#### chat-sidebar

Chat sidebar (collapsed). The left rail as a signed-out visitor first sees it: collapsed to the logo and toggle.

Page: chat. Selector: `[class*="_sidebar"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 74 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px |
| Transition | none |
| Icon | 115.89 x 22, colour #1b1b18 |
| Painted layers | aside.sidebar.collapsed 74.0x900.0 bg #fdfdf7 shadow #1b1b18 @ 0.08 -1px 0px 0px 0px inset; a.wrapper.collapsed 40.0x40.0 bg #f0f6ff r 50%; span.content 58.0x32.8 bg #0b0b0a r 32px; span.shimmer 58.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 58.0x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 56.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| Ancestor paint | 1 up div.layout bg #fdfdf7 |
| How | at rest |

Crops: `chat-sidebar-default.png`.

#### sidebar-toggle

Sidebar expand button.

Page: chat. Selector: `button "Expand sidebar"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #2463eb 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 @ 0.2 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #1b1b18 @ 0.2 | = | = | = |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Ancestor paint | 3 up aside.sidebar.collapsed bg #fdfdf7 shadow #1b1b18 @ 0.08 -1px 0px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | span.surface 36.0x36.0 bg #f5f5f0 r 100px | button.buttonBase.expandHitArea 36.0x36.0 r 100px shadow #2463eb 0px 0px 0px 2px | = |

Crops: `sidebar-toggle-default.png`, `sidebar-toggle-hover.png`, `sidebar-toggle-focus-visible.png`, `sidebar-toggle-pressed.png`.

#### chat-sidebar-open

Chat sidebar (expanded). Opened with the sidebar's own Expand button: New chat highlighted at the top, Health record / Appointments / Prescriptions below, then Sign up and Log in pinned at the bottom.

Page: chat. Selector: `[class*="_sidebar"] expanded`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 256 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.label14.colorDefault: geist 14px/19.6px 500, #2463eb, ls -0.28px |
| Transition | none |
| Icon | 115.89 x 22, colour #1b1b18 |
| Painted layers | aside.sidebar 256.0x900.0 bg #fdfdf7 shadow #1b1b18 @ 0.08 -1px 0px 0px 0px inset; a.wrapper.highlighted 224.0x36.0 bg #f0f6ff r 8px; span.content 224.0x32.8 bg #0b0b0a r 32px; span.shimmer 224.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 224.0x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 222.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| Ancestor paint | 1 up div.layout bg #fdfdf7 |
| How | at rest |

Crops: `chat-sidebar-open-default.png`.

#### nav-link-current

Sidebar link, current. New chat: the highlighted row in the expanded rail.

Page: chat. Selector: `[class*="_wrapper"] highlighted`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 224 x 36 |
| Padding | 8px |
| Gap | 8px |
| Border | none |
| Radius | 8px |
| Background | #f0f6ff |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.label14.colorDefault: geist 14px/19.6px 500, #2463eb, ls -0.28px |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #2463eb |
| Painted layers | a.wrapper.highlighted 224.0x36.0 bg #f0f6ff r 8px |
| Ancestor paint | 3 up aside.sidebar bg #fdfdf7 shadow #1b1b18 @ 0.08 -1px 0px 0px 0px inset |
| How | at rest |

Crops: `nav-link-current-default.png`.

#### nav-link

Sidebar link.

Page: chat. Selector: `[class*="_wrapper"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 36 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f0f6ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3c83f6 offset 2px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | p.label14.colorDefault: geist 14px/19.6px 500, #2463eb, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #2463eb | = | = | = |
| Painted layers | a.wrapper.highlighted 224.0x36.0 bg #f0f6ff r 8px | = | a.wrapper.highlighted 224.0x36.0 bg #f0f6ff r 8px outline 2px solid #3c83f6 offset 2px | = |
| Ancestor paint | 3 up aside.sidebar bg #fdfdf7 shadow #1b1b18 @ 0.08 -1px 0px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### signup-free

Sign up for free button. The blue primary button pinned at the bottom of the expanded rail. Measured, never pressed.

Page: chat. Selector: `button "Sign up for free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 32.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3c83f6 offset 0px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 224px x 43.9844px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content 224.0x32.8 bg #0b0b0a r 32px; span.shimmer 224.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 224.0x32.8 bg #272725 r 32px; span.shimmer 224.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | button.button.primary 224.0x32.8 r 32px outline 2px solid #3c83f6 offset 0px; span.content 224.0x32.8 bg #0b0b0a r 32px; span.shimmer 224.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 219.5x32.1 bg #1b1b18 r 32px; span.shimmer 219.5x32.1 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-free-default.png`, `signup-free-hover.png`, `signup-free-focus-visible.png`, `signup-free-pressed.png`.

#### sidebar-login

Sidebar log in button. The secondary button beside Sign up for free. Measured, never pressed.

Page: chat. Selector: `button "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 224 x 34.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3c83f6 offset 0px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #1b1b18, ls -0.24px | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px | = | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 224px x 43.9844px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content 224.0x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 222.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 224.0x34.8 bg #0b0b0a border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 222.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | button.button.secondary 224.0x34.8 r 32px outline 2px solid #3c83f6 offset 0px; span.content 224.0x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 222.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 219.5x34.1 bg #1b1b18 border T:1px solid #1b1b18 / R:1px solid #1b1b18 / B:1px solid #1b1b18 / L:1px solid #1b1b18 r 32px; span.shimmer 217.6x32.1 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| Ancestor paint | 3 up aside.sidebar bg #fdfdf7 shadow #1b1b18 @ 0.08 -1px 0px 0px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sidebar-login-default.png`, `sidebar-login-hover.png`, `sidebar-login-focus-visible.png`, `sidebar-login-pressed.png`.

#### anon-badge

Anonymous badge. The "Anonymous" session chip. Pressing it is a sign-in path, so it was hovered and measured only.

Page: chat. Selector: `[class*="_badgeButton"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 105.56 x 32 | = |
| Padding | 3px 8px | = |
| Gap | 4px | = |
| Border | 1px dashed #1b1b18 @ 0.08 | = |
| Radius | 34px | = |
| Background | transparent | #f5f5f0 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.label12.colorDefault: geist 12px/16.8px 500, #2463eb, ls -0.24px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #000000 | = |
| Painted layers | button.badgeButton 105.6x32.0 border T:1px dashed #1b1b18 @ 0.08 / R:1px dashed #1b1b18 @ 0.08 / B:1px dashed #1b1b18 @ 0.08 / L:1px dashed #1b1b18 @ 0.08 r 34px | button.badgeButton 105.6x32.0 bg #f5f5f0 border T:1px dashed #1b1b18 @ 0.08 / R:1px dashed #1b1b18 @ 0.08 / B:1px dashed #1b1b18 @ 0.08 / L:1px dashed #1b1b18 @ 0.08 r 34px |
| Ancestor paint | 3 up form.inputCard.inputCardExpanded bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px | = |
| How | at rest | mouse hover |

Crops: `anon-badge-default.png`, `anon-badge-hover.png`.

#### support-link

Support mail link.

Page: chat. Selector: `a[href^="mailto:"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 93.52 x 13 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #2463eb offset 1px |
| Font | geist 10px/14px 400 | = | = |
| Letter spacing | -0.2px | = | = |
| Colour | #2463eb | #1d4fd7 | = |
| Transition | color 0.2s ease-in-out | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | = | a.link 93.5x13.0 outline 1px auto #2463eb offset 1px |

Crops: `support-link-default.png`, `support-link-hover.png`, `support-link-focus-visible.png`.

#### legal-link

Legal link. The Terms of Service / Privacy Policy link in the chat footer. The first-capture selector read the footer's first anchor — the support@doctronic.ai mailto, already measured as support-link — so those states were dropped and the fixed selector's re-measure is queued.

Page: chat. Selector: `footer a[href*="privacy"/"terms"]`. States: .

Not found on the page at capture time.

#### recent-chats

View recent chats. Link to the (signed-in) chat list; measured only.

Page: chat. Selector: `"View recent chats"`. States: .

Not found on the page at capture time.

#### chat-hero

Chat hero. The centered empty-state: the Fraunces greeting and the large input card.

Page: chat. Selector: `h1 ancestor holding textarea`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fdfdf7 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.label14.colorDefault: geist 14px/19.6px 500, #2463eb, ls -0.28px |
| Transition | none |
| Icon | 115.89 x 22, colour #1b1b18 |
| Painted layers | main.layoutContent 1440.0x900.0 bg #fdfdf7; div.layout 1440.0x900.0 bg #fdfdf7; aside.sidebar 256.0x900.0 bg #fdfdf7 shadow #1b1b18 @ 0.08 -1px 0px 0px 0px inset; a.wrapper.highlighted 224.0x36.0 bg #f0f6ff r 8px; span.content 224.0x32.8 bg #0b0b0a r 32px; span.shimmer 224.0x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| How | at rest |

Crops: `chat-hero-default.png`.

#### chat-greeting

Chat greeting.

Page: chat. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 232 x 46.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraunces 40px/46.8px 400 |
| Letter spacing | -0.4px |
| Colour | #1b1b18 |
| Transition | none |
| How | at rest |

Crops: `chat-greeting-default.png`.

#### input-card

Chat input card. The large raised card holding the textarea and the round Send button; expands when focused.

Page: chat. Selector: `[class*="_inputCard"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 652 x 148 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1b1b18 | = |
| Text node | p.label12.colorDefault: geist 12px/16.8px 500, #2463eb, ls -0.24px | = |
| Transition | none | = |
| Icon | 20 x 20, colour #000000 | = |
| Painted layers | form.inputCard.inputCardExpanded 652.0x126.0 bg #ffffff border T:1px solid #1b1b18 @ 0.08 / R:1px solid #1b1b18 @ 0.08 / B:1px solid #1b1b18 @ 0.08 / L:1px solid #1b1b18 @ 0.08 r 16px shadow #000000 @ 0.06 0px 2px 24px 0px; button.badgeButton 105.6x32.0 border T:1px dashed #1b1b18 @ 0.08 / R:1px dashed #1b1b18 @ 0.08 / B:1px dashed #1b1b18 @ 0.08 / L:1px dashed #1b1b18 @ 0.08 r 34px; span.content 32.0x32.0 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 32.0x32.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | = |
| Ancestor paint | 1 up div.wrapper bg #fdfdf7 | = |
| How | at rest | mouse hover |

Crops: `input-card-default.png`, `input-card-hover.png`.

#### chat-textarea

Chat textarea. "Ask a question about your health…" — text was typed and deleted, Enter never pressed.

Page: chat. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 618 x 52 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | geist 16px/22.4px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #1b1b18 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #1b1b18 @ 0.6, opacity 1 | = | = |
| Ancestor paint | 2 up form.inputCard.inputCardExpanded bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px | = | = |
| How | at rest | clicked into the field | typed "I have a headache since this morning", then deleted; nothing sent |

Crops: `chat-textarea-default.png`, `chat-textarea-focused.png`, `chat-textarea-filled.png`.

#### send-button

Send message button. The condensed dark submit control inside the card. Measured, never pressed — pressing would send a message.

Page: chat. Selector: `[class*="_submitButton"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 52px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #2463eb @ 0.39 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | 19 x 19, colour #ffffff |
| ::before | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content 32.0x32.0 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 32.0x32.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | span.content 32.0x32.0 bg #1d4fd7 r 52px shadow #2463eb @ 0.5 0px 6px 10px 0px; span.shimmer 32.0x32.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | button.button.hero 32.0x32.0 r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px; span.content 32.0x32.0 bg #2463eb r 52px; span.shimmer 32.0x32.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | span.content 30.4x30.4 bg #1e3fae r 52px; span.shimmer 30.4x30.4 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px |
| Ancestor paint | 1 up form.inputCard.inputCardExpanded bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `send-button-default.png`, `send-button-hover.png`, `send-button-focus-visible.png`, `send-button-pressed.png`.

#### starter

Starter chip. "Check my symptoms" — a conversation starter under the card. Measured, never pressed.

Page: chat. Selector: `[class*="_starter"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 164.11 x 36.59 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f5f5f0 | #e4e4dc | = | #e4e4dc |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #1b1b18 offset 2px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | span.label14.colorDefault: geist 14px/19.6px 500, #1b1b18, ls -0.28px | = | = | = |
| Transition | background-color 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.starter 164.1x36.6 bg #f5f5f0 r 8px | button.starter 164.1x36.6 bg #e4e4dc r 8px | button.starter 164.1x36.6 bg #f5f5f0 r 8px outline 2px solid #1b1b18 offset 2px | button.starter 164.1x36.6 bg #e4e4dc r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `starter-default.png`, `starter-hover.png`, `starter-focus-visible.png`, `starter-pressed.png`.

#### disclaimer

Medical disclaimer.

Page: chat. Selector: `[class*="_disclaimer"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 652 x 14 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | geist 10px/14px 400 |
| Letter spacing | -0.2px |
| Colour | #1b1b18 @ 0.6 |
| Transition | none |
| How | at rest |

Crops: `disclaimer-default.png`.

### Dialogs and overlays

#### signin-dialog

Sign-in dialog. Reached by the public ?modal=signin URL: a centered raised card over a dimmed page. Nothing inside it was pressed.

Page: signin. Selector: `[role="dialog"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 393 x 583.45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | h1.display32.colorDefault: fraunces 32px/37.44px 400, #1b1b18, ls -0.32px |
| Transition | none |
| Icon | 16 x 16, colour #1b1b18 |
| Painted layers | img.doctorImage 78.0x78.0 r 50% shadow #000000 @ 0.1 0px 5px 32px 0px; img.patientImage 45.0x45.0 r 50% shadow #000000 @ 0.1 0px 5px 32px 0px; span.content 329.0x43.6 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 329.0x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px; span.content 329.0x44.0 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 40px; span.shimmer 327.0x42.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 40px |
| Ancestor paint | 1 up div.modal bg #fdfdf7 shadow #000000 @ 0.06 0px 2px 24px 0px |
| How | at rest |

Crops: `signin-dialog-default.png`.

#### signin-title

Sign-in title.

Page: signin. Selector: `dialog heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 256.61 x 74.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraunces 32px/37.44px 400 |
| Letter spacing | -0.32px |
| Colour | #1b1b18 |
| Transition | none |
| How | at rest |

Crops: `signin-title-default.png`.

#### email-login-button

Log in with email button. The primary action inside the dialog. Measured, never pressed.

Page: signin. Selector: `dialog button "Log in with email"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 329 x 43.59 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 52px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #2463eb @ 0.39 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px | #2463eb @ 0.39 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px |
| Outline | none | = | = | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | span.heading14.colorInherit: geist 14px/19.6px 600, #ffffff, ls -0.28px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | 15.68 x 15.68, colour #ffffff |
| ::before | 329px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content 329.0x43.6 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 329.0x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | span.content 329.0x43.6 bg #1d4fd7 r 52px shadow #2463eb @ 0.5 0px 6px 10px 0px; span.shimmer 329.0x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | button.button.hero 329.0x43.6 r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px; span.content 329.0x43.6 bg #2463eb r 52px; span.shimmer 329.0x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px | button.button.hero 329.0x43.6 r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px; span.content 322.4x42.7 bg #1e3fae r 52px; span.shimmer 322.4x42.7 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `email-login-button-default.png`, `email-login-button-hover.png`, `email-login-button-focus-visible.png`, `email-login-button-pressed.png`.

#### oauth-button

OAuth button. A Continue-with provider button. Measured, never pressed.

Page: signin. Selector: `dialog OAuth button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 329 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #3c83f6 offset 0px | 2px solid #3c83f6 offset 0px |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Text node | span.heading14.colorInherit: geist 14px/19.6px 600, #1b1b18, ls -0.28px | span.heading14.colorInherit: geist 14px/19.6px 600, #fdfdf7, ls -0.28px | = | span.heading14.colorInherit: geist 14px/19.6px 600, #fdfdf7, ls -0.28px |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b18 | 16 x 16, colour #fdfdf7 | = | 15.68 x 15.68, colour #fdfdf7 |
| ::before | 329px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content 329.0x44.0 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 40px; span.shimmer 327.0x42.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 40px | span.content 329.0x44.0 bg #0b0b0a border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 40px; span.shimmer 327.0x42.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 40px | button.button.secondary 329.0x44.0 r 40px outline 2px solid #3c83f6 offset 0px; span.content 329.0x44.0 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 40px; span.shimmer 327.0x42.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 40px | button.button.secondary 329.0x44.0 r 40px outline 2px solid #3c83f6 offset 0px; span.content 322.4x43.1 bg #1b1b18 border T:1px solid #1b1b18 / R:1px solid #1b1b18 / B:1px solid #1b1b18 / L:1px solid #1b1b18 r 40px; span.shimmer 320.5x41.2 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-button-default.png`, `oauth-button-hover.png`, `oauth-button-focus-visible.png`, `oauth-button-pressed.png`.

#### create-account-link

Create an account link. Measured, never followed.

Page: signin. Selector: `dialog "Create an account"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128.22 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | 1px auto #005fcc offset 1px |
| Font | geist 16px/22.4px 400 | = | = | = |
| Letter spacing | -0.32px | = | = | = |
| Colour | #2463eb | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.signupLink 128.2x21.0 outline 1px auto #005fcc offset 1px | a.signupLink 128.2x21.0 outline 1px auto #005fcc offset 1px |

Crops: `create-account-link-default.png`, `create-account-link-hover.png`, `create-account-link-focus-visible.png`, `create-account-link-pressed.png`.

#### dialog-close

Dialog close button.

Page: signin. Selector: `dialog close button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #2463eb 0px 0px 0px 2px | = |
| Outline | none | = | = | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1b1b18 | = | = | = |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Ancestor paint | 2 up div.modal bg #fdfdf7 shadow #000000 @ 0.06 0px 2px 24px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | span.surface 32.0x32.0 bg #f5f5f0 r 100px | button.buttonBase.expandHitArea 32.0x32.0 r 100px shadow #2463eb 0px 0px 0px 2px | = |

Crops: `dialog-close-default.png`, `dialog-close-hover.png`, `dialog-close-focus-visible.png`, `dialog-close-pressed.png`.

### Symptom checker

#### symptom-title

Symptom-checker headline. "…your private and personal AI symptom checker" in the Fraunces display face.

Page: symptom. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 211.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fraunces 64px/70.4px 400 |
| Letter spacing | -0.64px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `symptom-title-default.png`.

#### symptom-input-card

Symptom input card. The raised card holding the symptoms textarea and the Check button.

Page: symptom. Selector: `textarea ancestor card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 638 x 171 | = |
| Padding | 16px | = |
| Gap | 12px | = |
| Border | 1px solid #e3e1d6 | = |
| Radius | 24px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1b1b18 @ 0.06 0px 10px 30px 0px | = |
| Outline | none | = |
| Font | Geist 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0c0e12 | = |
| Text node | span.absolute.bottom-full: Geist 15px/22.5px 600, #1b1b18, ls -0.3px | = |
| Transition | none | = |
| Icon | 16 x 16, colour #fdfdf8 | = |
| Painted layers | form.ot-hero-item.w-full 638.0x171.0 bg #ffffff border T:1px solid #e3e1d6 / R:1px solid #e3e1d6 / B:1px solid #e3e1d6 / L:1px solid #e3e1d6 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1b1b18 @ 0.06 0px 10px 30px 0px; span.absolute.bottom-full 167.5x42.5 bg #eaf5c8 r 16px 16px 0px 0px; button.hero-button-primary.order-3 209.0x45.0 bg #2563eb r 52px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0961e4 @ 0.39 0px 4px 7px 0px | = |
| How | at rest | mouse hover |

Crops: `symptom-input-card-default.png`, `symptom-input-card-hover.png`.

#### symptom-textarea

Symptoms textarea. "Describe your symptoms…" — text was typed and deleted, never submitted.

Page: symptom. Selector: `textarea`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 604 x 80 | = | = |
| Padding | 4px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1a1a18 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1a1a18 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | Geist 16px/24px 400 | = | = |
| Letter spacing | -0.32px | = | = |
| Colour | #1a1a18 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #1a1a18 @ 0.6, opacity 1 | = | = |
| Ancestor paint | 1 up form.ot-hero-item.w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1b1b18 @ 0.06 0px 10px 30px 0px | = | = |
| How | at rest | clicked into the field | typed "I have a headache since this morning", then deleted; nothing sent |
| Painted layers | - | textarea.order-1.w-full 604.0x80.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1a1a18 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | textarea.order-1.w-full 604.0x80.0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1a1a18 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |

Crops: `symptom-textarea-default.png`, `symptom-textarea-focused.png`, `symptom-textarea-filled.png`.

#### check-button

Check My Symptoms button. Measured, never pressed — pressing would submit symptoms.

Page: symptom. Selector: `"Check My Symptoms"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 208.95 x 45 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 52px | = | = | = |
| Background | #2563eb | oklch(0.488 0.243 264.376) | = | oklch(0.488 0.243 264.376) |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0961e4 @ 0.39 0px 4px 7px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Geist 14px/21px 600 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #fdfdf8 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #fdfdf8 | = | = | = |
| Painted layers | button.hero-button-primary.order-3 209.0x45.0 bg #2563eb r 52px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0961e4 @ 0.39 0px 4px 7px 0px | button.hero-button-primary.order-3 209.0x45.0 bg oklch(0.488 0.243 264.376) r 52px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0961e4 @ 0.39 0px 4px 7px 0px | button.hero-button-primary.order-3 209.0x45.0 bg #2563eb r 52px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0961e4 @ 0.39 0px 4px 7px 0px outline 1px auto #005fcc offset 0px | button.hero-button-primary.order-3 209.0x45.0 bg oklch(0.488 0.243 264.376) r 52px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0961e4 @ 0.39 0px 4px 7px 0px |
| Ancestor paint | 1 up form.ot-hero-item.w-full bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1b1b18 @ 0.06 0px 10px 30px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `check-button-default.png`, `check-button-hover.png`, `check-button-focus-visible.png`, `check-button-pressed.png`.

### Marketing and content pages

#### mkt-header

Marketing top bar. The pill-link bar shared by the content pages: wordmark, About/FAQ/Blog/Online Treatment/Wall of Love, "Try Doctronic For Free" and Sign up.

Page: blog. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #e2f0e4 |
| Box shadow | none |
| Backdrop filter | blur(12px) |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0c0e12 |
| Text node | a.rounded-full.px-[10px]: Geist 14px/21px 600, #1a1a18, ls -0.28px |
| Transition | background-color 0.3s ease |
| Icon | 18 x 18, colour #ffffff |
| Painted layers | header.sticky.top-0 1440.0x56.0 bg #e2f0e4; a.flex.items-center 214.8x40.0 bg #0c0e12 r 3.35544e+07px; a.flex.items-center 0.0x0.0 bg #0a0a09 r 40px; span.block.w-px 0.0x0.0 border L:1px dashed #e5e5dd |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-nav-pill

Marketing pill link.

Page: blog. Selector: `header a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46.39 x 29 | = | = | = |
| Padding | 4px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #000000 @ 0.05 | = | #000000 @ 0.05 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Geist 14px/21px 600 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #1a1a18 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.rounded-full.px-[10px] 46.4x29.0 bg #000000 @ 0.05 r 3.35544e+07px | a.rounded-full.px-[10px] 46.4x29.0 r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.rounded-full.px-[10px] 46.4x29.0 bg #000000 @ 0.05 r 3.35544e+07px |

Crops: `mkt-nav-pill-default.png`, `mkt-nav-pill-hover.png`, `mkt-nav-pill-focus-visible.png`, `mkt-nav-pill-pressed.png`.

#### try-button

Try Doctronic button. The dark rounded-full CTA link in the top bar. Measured, never followed.

Page: blog. Selector: `header a "Try Doctronic For Free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 214.77 x 40 | = | = | = |
| Padding | 10px 22px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #0c0e12 | oklch(0.269 0 0) | = | oklch(0.269 0 0) |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Geist 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | = |
| Painted layers | a.flex.items-center 214.8x40.0 bg #0c0e12 r 3.35544e+07px | a.flex.items-center 214.8x40.0 bg oklch(0.269 0 0) r 3.35544e+07px | a.flex.items-center 214.8x40.0 bg #0c0e12 r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.flex.items-center 214.8x40.0 bg oklch(0.269 0 0) r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `try-button-default.png`, `try-button-hover.png`, `try-button-focus-visible.png`, `try-button-pressed.png`.

#### mkt-signup

Marketing sign up. Measured, never pressed.

Page: blog. Selector: `header "Sign up"`. States: .

Not found on the page at capture time.

#### mkt-footer

Marketing footer. The link-column footer shared by the content pages.

Page: blog. Selector: `last footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1414.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/24px 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.text-[18px].font-semibold: Geist 18px/25.2px 600, #1b1b18, ls -0.36px |
| Transition | none |
| Icon | 120 x 40, colour #1b1b18 |
| Painted layers | div 1440.0x96.0 image linear-gradient(#ffffff, #000000 @ 0); div.absolute.inset-0 1440.0x1414.5 image linear-gradient(#fdfdf8 0%, #e2f0e4 100%); a.flex.items-center 59.1x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; a.flex.items-center 65.6x32.8 bg #1b1b18 r 32px; div.w-full.border-t-2 1240.0x2.0 border T:2px dashed #1a1a18 @ 0.08 |
| Ancestor paint | 1 up body.min-h-dvh.flex bg #fdfdf8 |
| How | at rest |

Crops: `mkt-footer-default.png`.

#### mkt-footer-link

Marketing footer link.

Page: blog. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 16 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Geist 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b18 | #0f64e9 | = | #0f64e9 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.relative.inline-flex 16.0x16.0 outline 1px auto #005fcc offset 1px | = |

Crops: `mkt-footer-link-default.png`, `mkt-footer-link-hover.png`, `mkt-footer-link-focus-visible.png`, `mkt-footer-link-pressed.png`.

#### blog-title

Blog title.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 319.86 x 56.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fraunces 48px/56.16px 400 |
| Letter spacing | -0.48px |
| Colour | #242424 |
| Transition | none |
| How | at rest |

Crops: `blog-title-default.png`.

#### blog-search

Blog search field. Text was typed and deleted; search was never submitted.

Page: blog. Selector: `input[type="search"]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 730 x 39 | = | 706 x 39 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geist 14px/21px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #242424 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #666666, opacity 1 | = | = |
| Ancestor paint | 1 up form.relative.flex bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "prescription", then deleted; nothing sent |

Crops: `blog-search-default.png`, `blog-search-focused.png`, `blog-search-filled.png`.

#### article-card

Article card. A post card: gradient thumbnail with a centred glyph, category/date line and title; the whole card is one link.

Page: blog. Selector: `main [class*="rounded-[14px]"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 370.66 x 480.28 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #e5e7eb | = | = |
| Radius | 14px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Geist 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0c0e12 | = | = |
| Text node | a.block.max-w-[200px]: Geist 12px/18px 600, #000000 | = | = |
| Transition | none | = | = |
| Icon | 64 x 64, colour #0f172a @ 0.6 | = | = |
| Painted layers | article.flex.flex-col 370.7x480.3 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px; div.flex.h-[150px] 368.7x150.0 image linear-gradient(in oklab, #fdfdf8 0%, #e2f0e4 100%); a.block.max-w-[200px] 123.3x26.0 bg #dfff95 @ 0.8 r 12px; a.block.max-w-[200px] 121.1x26.0 bg #dfff95 @ 0.8 r 12px; a.block.max-w-[200px] 118.9x26.0 bg #dce3ec r 12px; a.block.max-w-[200px] 145.3x26.0 bg #dce3ec r 12px | = | article.flex.flex-col 370.7x480.3 bg #ffffff border T:1px solid #e5e7eb / R:1px solid #e5e7eb / B:1px solid #e5e7eb / L:1px solid #e5e7eb r 14px; div.flex.h-[150px] 368.7x150.0 image linear-gradient(in oklab, #fdfdf8 0%, #e2f0e4 100%); a.block.max-w-[200px] 123.3x26.0 bg #dfff95 @ 0.8 r 12px outline 1px auto #005fcc offset 1px; a.block.max-w-[200px] 121.1x26.0 bg #dfff95 @ 0.8 r 12px; a.block.max-w-[200px] 118.9x26.0 bg #dce3ec r 12px; a.block.max-w-[200px] 145.3x26.0 bg #dce3ec r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `article-card-default.png`, `article-card-hover.png`, `article-card-focus-visible.png`.

#### article-card-title

Article card title.

Page: blog. Selector: `card title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 324.66 x 105 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 25px/26.25px 500 |
| Letter spacing | -0.5px |
| Colour | #1a1a18 |
| Text node | a.hover:underline: Geist 25px/26.25px 500, #1a1a18, ls -0.5px |
| Transition | none |
| How | at rest |

Crops: none.

#### body-h2

Content h2.

Page: blog. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 386.77 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 20px/28px 700 |
| Letter spacing | -0.4px |
| Colour | #242424 |
| Transition | none |
| How | at rest |

Crops: `body-h2-default.png`.

#### telehealth-title

Telehealth headline.

Page: telehealth. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 281.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fraunces 64px/70.4px 400 |
| Letter spacing | -0.64px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `telehealth-title-default.png`.

#### telehealth-lede

Telehealth lede.

Page: telehealth. Selector: `first p after h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 57 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 15px/28.5px 400 |
| Letter spacing | -0.3px |
| Colour | #5a5a54 |
| Text node | p: Geist 15px/28.5px 400, #5a5a54, ls -0.3px |
| Transition | none |
| How | at rest |

Crops: none.

#### telehealth-cta

Telehealth CTA. The page's primary call to action — the dark "Try Doctronic For Free" pill shared with the top bar. Measured, never pressed.

Page: telehealth. Selector: `first CTA in main`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 214.77 x 40 | = | = | = |
| Padding | 10px 22px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #0c0e12 | oklch(0.269 0 0) | = | oklch(0.269 0 0) |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Geist 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | = |
| Painted layers | a.flex.items-center 214.8x40.0 bg #0c0e12 r 3.35544e+07px | a.flex.items-center 214.8x40.0 bg oklch(0.269 0 0) r 3.35544e+07px | a.flex.items-center 214.8x40.0 bg #0c0e12 r 3.35544e+07px outline 1px auto #005fcc offset 1px | a.flex.items-center 214.8x40.0 bg oklch(0.269 0 0) r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `telehealth-cta-default.png`, `telehealth-cta-hover.png`, `telehealth-cta-focus-visible.png`, `telehealth-cta-pressed.png`.

#### step-block

Telehealth section heading.

Page: telehealth. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 689.52 x 28.08 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fraunces 24px/28.08px 500 |
| Letter spacing | -0.24px |
| Colour | #1b1b18 |
| Transition | none |
| How | at rest |

Crops: `step-block-default.png`.

#### authors-title

Authors headline.

Page: authors. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 114.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fraunces 52px/57.2px 400 |
| Letter spacing | -0.52px |
| Colour | #0c0e12 |
| Transition | none |
| How | at rest |

Crops: `authors-title-default.png`.

#### author-card

Author card. A reviewer card: portrait, name and medical credential line, with a "View profile" link.

Page: authors. Selector: `main li`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 380 x 280.5 | = |
| Padding | 0px | = |
| Border | T: 1px solid #e7e4de; R: none; B: none; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0c0e12 | = |
| Text node | span.block.text-[20px]: Fraunces 20px/24px 400, #0c0e12, ls -0.6px | span.block.text-[20px]: Fraunces 20px/24px 400, #0961e4, ls -0.6px |
| Transition | none | = |
| Icon | 16 x 16, colour #0961e4 | 16 x 16, colour oklch(0.424 0.199 265.638) |
| Painted layers | li.border-t.border-[#E7E4DE] 380.0x280.5 border T:1px solid #e7e4de | = |
| How | at rest | mouse hover |

Crops: `author-card-default.png`, `author-card-hover.png`.

#### resource-title

Resource center headline.

Page: resource. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 625.52 x 39.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fraunces 36px/40px 800 |
| Letter spacing | normal |
| Colour | oklch(0.208 0.042 265.755) |
| Transition | none |
| Ancestor paint | 1 up article.bg-white.dark:bg-gray-900 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| How | at rest |

Crops: `resource-title-default.png`.

#### body-copy

Body copy.

Page: resource. Selector: `main p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 625.52 x 168 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Geist 16px/28px 400 |
| Letter spacing | normal |
| Colour | oklch(0.372 0.044 257.287) |
| Transition | none |
| Ancestor paint | 1 up article.bg-white.dark:bg-gray-900 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| How | at rest |

Crops: none.

#### wall-title

Wall of Love headline.

Page: wall. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 664.11 x 86.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fraunces 72px/86.4px 400 |
| Letter spacing | -1.8px |
| Colour | #0c0e12 |
| Transition | none |
| How | at rest |

Crops: `wall-title-default.png`.

#### love-card

Testimonial card. A review card on the Wall of Love: avatar, first name, quote and the Love/Reply footer row.

Page: wall. Selector: `main [class*="break-inside-avoid"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 405.33 x 109.38 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Geist 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #0c0e12 | = |
| Transition | none | = |
| Painted layers | div.group.relative 405.3x109.4 bg #fdfdf8 border T:1px solid #1a1a18 @ 0.08 / R:1px solid #1a1a18 @ 0.08 / B:1px solid #1a1a18 @ 0.08 / L:1px solid #1a1a18 @ 0.08 r 24px; div.pointer-events-none.absolute 0.0x0.0 bg #f0ede9 r 18px | div.group.relative 405.3x109.4 bg #fdfdf8 border T:1px solid #1a1a18 @ 0.08 / R:1px solid #1a1a18 @ 0.08 / B:1px solid #1a1a18 @ 0.08 / L:1px solid #1a1a18 @ 0.08 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 8px 24px 0px; div.pointer-events-none.absolute 0.0x0.0 bg #f0ede9 r 18px |
| How | at rest | mouse hover |

Crops: `love-card-default.png`, `love-card-hover.png`.

#### category-chip

Category chip. A tinted pill filtering the article grid ("Allergies", "Mental Health", …). Measured, never followed.

Page: blog. Selector: `main a.rounded-full`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.08 x 28 | = | = | = |
| Padding | 6px 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #e6dbe6 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Geist 14px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #242424 | = | = | = |
| Transition | opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.block.max-w-[260px] 77.1x28.0 bg #e6dbe6 r 3.35544e+07px | = | a.block.max-w-[260px] 77.1x28.0 bg #e6dbe6 r 3.35544e+07px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.7 | = | 0.7 |

Crops: `category-chip-default.png`, `category-chip-hover.png`, `category-chip-focus-visible.png`, `category-chip-pressed.png`.

#### resource-sheet

Resource article sheet. The long-form white card the Resource Center is typeset into.

Page: resource. Selector: `main [class*="prose"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 689.52 x 10568.97 |
| Padding | 32px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px |
| Outline | none |
| Font | Geist 16px/28px 400 |
| Letter spacing | normal |
| Colour | oklch(0.372 0.044 257.287) |
| Text node | h1: Fraunces 36px/40px 800, oklch(0.208 0.042 265.755) |
| Transition | none |
| Painted layers | article.bg-white.dark:bg-gray-900 689.5x10569.0 bg #ffffff r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 20px 25px -5px, #000000 @ 0.1 0px 8px 10px -6px; hr 625.5x1.0 border T:1px solid oklch(0.929 0.013 255.508) |
| How | at rest |

Crops: `resource-sheet-default.png`.

### Dark theme (data-theme="dark")

#### d-header

Top bar, dark. The same bar under data-theme="dark": sunken dark ground, light text.

Page: dark. Selector: `[class*="_marketingHeader"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfdf7 |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px |
| Transition | transform 0.25s ease |
| Icon | 0 x 0, colour #fdfdf7 |
| Painted layers | div.content.contentShrink 1440.0x72.0 bg #0d0e0b; span.content 59.1x34.8 border T:1px solid #fdfdf7 @ 0.2 / R:1px solid #fdfdf7 @ 0.2 / B:1px solid #fdfdf7 @ 0.2 / L:1px solid #fdfdf7 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 65.6x32.8 bg #fdfdf7 r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 32px; div.openMenuWrapper 57.0x40.0 border L:1px dashed #fdfdf7 @ 0.08 |
| Ancestor paint | 1 up main.layoutContent bg #0d0e0b |
| How | at rest |

Crops: `d-header-default.png`.

#### d-signup-button

Sign up button, dark.

Page: dark. Selector: `top bar "Sign up"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 65.64 x 34.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 32px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #61a6fa offset 0px | = |
| Font | -apple-system 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fdfdf7 | = | = | = |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #0b0b0a, ls -0.24px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 65.6406px x 43.9844px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | span.content 65.6x32.8 bg #fdfdf7 r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 65.6x32.8 bg #e4e4dc r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 32px | button.button.primary 65.6x34.8 r 32px outline 2px solid #61a6fa offset 0px; span.content 65.6x32.8 bg #fdfdf7 r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 32px | span.content 64.3x32.1 bg #f5f5f0 r 32px; span.shimmer 64.3x32.1 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-signup-button-default.png`, `d-signup-button-hover.png`, `d-signup-button-focus-visible.png`, `d-signup-button-pressed.png`.

#### d-hero

Hero, dark.

Page: dark. Selector: `textarea ancestor holding h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 548 x 421.5 |
| Padding | 0px |
| Gap | 64px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfdf7 |
| Text node | h1.display32.colorDefault: fraunces 48px/56.16px 400, #fdfdf7, ls -0.48px |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | div.content 150.5x36.6 bg #d9ff80 @ 0.5 r 16px 18px 18px 2px; div::before.material 148.453pxx34.5938px image linear-gradient(155deg, #ffffff @ 0.06 0%, #000000 @ 0.06 50%, #ffffff @ 0.06 100%) r 16px 18px 18px 2px; div::after.material 150.453pxx36.5938px bg #808080 @ 0 r 16px 18px 18px 2px; div.edgeReflection 186.5x72.6 border T:18px solid #000000 @ 0 / R:18px solid #000000 @ 0 / B:18px solid #000000 @ 0 / L:18px solid #000000 @ 0 r 34px 36px 36px 20px; div.refraction 150.5x36.6 border T:6px solid #000000 @ 0 / R:6px solid #000000 @ 0 / B:6px solid #000000 @ 0 / L:6px solid #000000 @ 0 r 16px 18px 18px 2px; div.inputContainer 548.0x147.4 bg #1b1b18 border T:1px solid #fdfdf7 @ 0.08 / R:1px solid #fdfdf7 @ 0.08 / B:1px solid #fdfdf7 @ 0.08 / L:1px solid #fdfdf7 @ 0.08 r 16px shadow #000000 @ 0.06 0px 2px 24px 0px |
| Ancestor paint | 1 up section.section bg #0d0e0b |
| How | at rest |

Crops: `d-hero-default.png`.

#### d-hero-title

Hero headline, dark.

Page: dark. Selector: `hero h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 378.56 x 56.16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraunces 48px/56.16px 400 |
| Letter spacing | -0.48px |
| Colour | #fdfdf7 |
| Transition | none |
| How | at rest |

Crops: `d-hero-title-default.png`.

#### d-input-card

Chat field, dark.

Page: dark. Selector: `[class*="_inputContainer"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 548 x 147.38 |
| Padding | 16px |
| Border | 1px solid #fdfdf7 @ 0.08 |
| Radius | 16px |
| Background | #1b1b18 |
| Box shadow | #000000 @ 0.06 0px 2px 24px 0px |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfdf7 |
| Text node | p.label12.colorDefault: geist 12px/16.8px 500, #61a6fa, ls -0.24px |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | div.inputContainer 548.0x147.4 bg #1b1b18 border T:1px solid #fdfdf7 @ 0.08 / R:1px solid #fdfdf7 @ 0.08 / B:1px solid #fdfdf7 @ 0.08 / L:1px solid #fdfdf7 @ 0.08 r 16px shadow #000000 @ 0.06 0px 2px 24px 0px; button.badgeButton 105.6x32.0 border T:1px dashed #fdfdf7 @ 0.08 / R:1px dashed #fdfdf7 @ 0.08 / B:1px dashed #fdfdf7 @ 0.08 / L:1px dashed #fdfdf7 @ 0.08 r 34px; span.content.submitButtonContent 136.4x43.6 bg #61a6fa r 52px shadow #61a6fa @ 0.39 0px 4px 7px 0px; span.shimmer 136.4x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 52px |
| How | at rest |

Crops: `d-input-card-default.png`.

#### d-start-button

Start chat button, dark.

Page: dark. Selector: `[class*="_submitButton"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 136.36 x 43.59 |
| Padding | 0px |
| Border | none |
| Radius | 52px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfdf7 |
| Text node | span.heading14.colorInherit: geist 14px/19.6px 600, #172554, ls -0.28px |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #172554 |
| ::before | 136.359px x 44px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | span.content.submitButtonContent 136.4x43.6 bg #61a6fa r 52px shadow #61a6fa @ 0.39 0px 4px 7px 0px; span.shimmer 136.4x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 52px |
| Ancestor paint | 2 up div.inputContainer bg #1b1b18 shadow #000000 @ 0.06 0px 2px 24px 0px |
| How | at rest |

Crops: `d-start-button-default.png`.

#### d-pill

Prompt pill, dark.

Page: dark. Selector: `[class*="_pill"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126.45 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | geist 14px/19.6px 600 |
| Letter spacing | -0.28px |
| Colour | #fdfdf7 |
| Transition | none |
| Ancestor paint | 1 up div.content bg #d9ff80 @ 0.5 |
| How | at rest |

Crops: `d-pill-default.png`.

#### d-footer

Footer, dark.

Page: dark. Selector: `last footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1414.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #fdfdf7 |
| Text node | p.heading18.colorDefault: geist 18px/25.2px 600, #fdfdf7, ls -0.36px |
| Transition | none |
| Icon | 0 x 0, colour #fdfdf7 |
| Painted layers | div.gradient 1440.0x1414.5 image linear-gradient(#fdfdf7 0%, #e1efe3 100%); span.content 59.1x34.8 border T:1px solid #fdfdf7 @ 0.2 / R:1px solid #fdfdf7 @ 0.2 / B:1px solid #fdfdf7 @ 0.2 / L:1px solid #fdfdf7 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 65.6x32.8 bg #fdfdf7 r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #0b0b0a @ 0.18 50%, #000000 @ 0 80%) r 32px; div.divider 1240.0x2.0 border T:2px dashed #fdfdf7 @ 0.08 |
| Ancestor paint | 1 up main.layoutContent bg #0d0e0b |
| How | at rest |

Crops: `d-footer-default.png`.

### Mobile (390 wide)

#### m-header

Top bar (mobile). The 390px header: wordmark, Sign up and the menu button (Log in is dropped at this width).

Page: home. Selector: `[class*="_marketingHeader"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #fdfdf7, ls -0.24px |
| Transition | transform 0.25s ease |
| Icon | 115.89 x 22, colour #1b1b18 |
| Painted layers | div.content.contentShrink 390.0x72.0 bg #fdfdf7; span.content 0.0x0.0 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 0.0x0.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 65.6x32.8 bg #0b0b0a r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; div.openMenuWrapper 57.0x40.0 border L:1px dashed #1b1b18 @ 0.08 |
| Ancestor paint | 1 up main.layoutContent bg #fdfdf7 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 100px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #1b1b18 |
| ::after | 44px x 44px, absolute, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-hero

Hero (mobile).

Page: home. Selector: `textarea ancestor holding h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 535.94 |
| Padding | 0px |
| Gap | 56px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | h1.display32.colorDefault: fraunces 32px/37.44px 400, #1b1b18, ls -0.32px |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | div.content 150.5x36.6 bg #d9ff80 @ 0.5 r 16px 18px 18px 2px; div::before.material 148.453pxx34.5938px image linear-gradient(155deg, #ffffff @ 0.06 0%, #000000 @ 0.06 50%, #ffffff @ 0.06 100%) r 16px 18px 18px 2px; div::after.material 150.453pxx36.5938px bg #808080 @ 0 r 16px 18px 18px 2px; div.edgeReflection 186.5x72.6 border T:18px solid #000000 @ 0 / R:18px solid #000000 @ 0 / B:18px solid #000000 @ 0 / L:18px solid #000000 @ 0 r 34px 36px 36px 20px; div.refraction 150.5x36.6 border T:6px solid #000000 @ 0 / R:6px solid #000000 @ 0 / B:6px solid #000000 @ 0 / L:6px solid #000000 @ 0 r 16px 18px 18px 2px; div.inputContainer 342.0x155.8 bg #ffffff border T:1px solid #1b1b18 @ 0.08 / R:1px solid #1b1b18 @ 0.08 / B:1px solid #1b1b18 @ 0.08 / L:1px solid #1b1b18 @ 0.08 r 16px shadow #000000 @ 0.06 0px 2px 24px 0px |
| Ancestor paint | 1 up section.section bg #fdfdf7 |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-hero-title

Hero headline (mobile).

Page: home. Selector: `hero h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 252.39 x 37.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | fraunces 32px/37.44px 400 |
| Letter spacing | -0.32px |
| Colour | #1b1b18 |
| Transition | none |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-input-card

Chat field (mobile).

Page: home. Selector: `[class*="_inputContainer"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 155.77 |
| Padding | 16px |
| Border | 1px solid #1b1b18 @ 0.08 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.06 0px 2px 24px 0px |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.label12.colorDefault: geist 12px/16.8px 500, #2463eb, ls -0.24px |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | div.inputContainer 342.0x155.8 bg #ffffff border T:1px solid #1b1b18 @ 0.08 / R:1px solid #1b1b18 @ 0.08 / B:1px solid #1b1b18 @ 0.08 / L:1px solid #1b1b18 @ 0.08 r 16px shadow #000000 @ 0.06 0px 2px 24px 0px; button.badgeButton 105.6x32.0 border T:1px dashed #1b1b18 @ 0.08 / R:1px dashed #1b1b18 @ 0.08 / B:1px dashed #1b1b18 @ 0.08 / L:1px dashed #1b1b18 @ 0.08 r 34px; span.content.submitButtonContent 136.4x43.6 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 136.4x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px |
| How | at rest |

Crops: `m-input-card-default.png`.

#### m-start-button

Start chat button (mobile).

Page: home. Selector: `[class*="_submitButton"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 136.36 x 43.59 |
| Padding | 0px |
| Border | none |
| Radius | 52px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | span.heading14.colorInherit: geist 14px/19.6px 600, #ffffff, ls -0.28px |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #ffffff |
| ::before | 136.359px x 44px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | span.content.submitButtonContent 136.4x43.6 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 136.4x43.6 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px |
| Ancestor paint | 2 up div.inputContainer bg #ffffff shadow #000000 @ 0.06 0px 2px 24px 0px |
| How | at rest |

Crops: `m-start-button-default.png`.

#### m-footer

Footer (mobile).

Page: home. Selector: `last footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 1643.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.heading18.colorDefault: geist 18px/25.2px 600, #1b1b18, ls -0.36px |
| Transition | none |
| Icon | 147.5 x 28, colour #1b1b18 |
| Painted layers | div.gradient 390.0x1643.3 image linear-gradient(#fdfdf7 0%, #e1efe3 100%); span.content 59.1x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; span.content 65.6x32.8 bg #0b0b0a r 32px; span.shimmer 65.6x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px; div.divider 342.0x2.0 border T:2px dashed #1b1b18 @ 0.08 |
| Ancestor paint | 1 up main.layoutContent bg #fdfdf7 |
| How | at rest |

Crops: `m-footer-default.png`.

#### m-chat-header

Chat top bar (mobile).

Page: chat. Selector: `[class*="_mobileHeader"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 66.8 |
| Padding | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Backdrop filter | blur(6px) |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | span.heading12.colorInherit: geist 12px/16.8px 600, #1b1b18, ls -0.24px |
| Transition | none |
| Icon | 24 x 24, colour #1b1b18 |
| Painted layers | span.content 59.1x34.8 border T:1px solid #1b1b18 @ 0.2 / R:1px solid #1b1b18 @ 0.2 / B:1px solid #1b1b18 @ 0.2 / L:1px solid #1b1b18 @ 0.2 r 32px; span.shimmer 57.1x32.8 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 32px |
| How | at rest |

Crops: `m-chat-header-default.png`.

#### m-input-card-chat

Chat input card (mobile).

Page: chat. Selector: `[class*="_inputCard"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 148 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | p.label12.colorDefault: geist 12px/16.8px 500, #2463eb, ls -0.24px |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | form.inputCard.inputCardExpanded 342.0x126.0 bg #ffffff border T:1px solid #1b1b18 @ 0.08 / R:1px solid #1b1b18 @ 0.08 / B:1px solid #1b1b18 @ 0.08 / L:1px solid #1b1b18 @ 0.08 r 16px shadow #000000 @ 0.06 0px 2px 24px 0px; button.badgeButton 105.6x32.0 border T:1px dashed #1b1b18 @ 0.08 / R:1px dashed #1b1b18 @ 0.08 / B:1px dashed #1b1b18 @ 0.08 / L:1px dashed #1b1b18 @ 0.08 r 34px; span.content 32.0x32.0 bg #2463eb r 52px shadow #2463eb @ 0.39 0px 4px 7px 0px; span.shimmer 32.0x32.0 image linear-gradient(105deg, #000000 @ 0 20%, #fdfdf7 @ 0.18 50%, #000000 @ 0 80%) r 52px |
| Ancestor paint | 1 up div.wrapper bg #fdfdf7 |
| How | at rest |

Crops: `m-input-card-chat-default.png`.

#### m-starter

Starter chip (mobile).

Page: chat. Selector: `[class*="_starter"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 164.11 x 36.59 |
| Padding | 8px 16px |
| Border | none |
| Radius | 8px |
| Background | #f5f5f0 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b18 |
| Text node | span.label14.colorDefault: geist 14px/19.6px 500, #1b1b18, ls -0.28px |
| Transition | background-color 0.15s ease-in |
| Cursor | pointer |
| Painted layers | button.starter 164.1x36.6 bg #f5f5f0 r 8px |
| How | at rest |

Crops: `m-starter-default.png`.

## Dialog backdrop

The layers behind the sign-in dialog that paint a fill or a backdrop-filter, from the dialog outwards. The first is the overlay that dims the page.

- `YT4P-W_modal`:#fdfdf7
- `YT4P-W_modalOverlay`:#fdfdf7 @ 0.4, backdrop-filter blur(4.5px)

## Transitions declared in the readable stylesheets

doctronic.ai's stylesheets are same-origin, so this list holds every transition rule the CSSOM could read on each measured page — CSS-module rules on the app surfaces (home, /chat/) and Tailwind-generated rules on the content pages; the per-state Transition rows above are computed values.

- chat: `border-color 0.15s ease-in-out`, `none`, `border-color 0.18s ease-out, transform 0.18s ease-out`, `background-color 0.15s`, `transform 0.28s cubic-bezier(0.4, 0, 0.2, 1)`, `width 0.7s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.2s`, `scale 0.44s cubic-bezier(0.2, 0, 0, 1) 0.12s`, `opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1)`, `opacity 0.42s cubic-bezier(0.2, 0, 0, 1), --chat-sheet-mobile-sink 0.42s cubic-bezier(0.2, 0, 0, 1)`, `padding 0.44s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s, scale 0.15s`

- home: `border-color 0.15s ease-in-out`, `none`, `border-color 0.18s ease-out, transform 0.18s ease-out`, `background-color 0.15s`, `transform 0.28s cubic-bezier(0.4, 0, 0.2, 1)`, `width 0.7s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.2s`, `scale 0.44s cubic-bezier(0.2, 0, 0, 1) 0.12s`, `opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1)`, `opacity 0.42s cubic-bezier(0.2, 0, 0, 1), --chat-sheet-mobile-sink 0.42s cubic-bezier(0.2, 0, 0, 1)`, `padding 0.44s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s, scale 0.15s`
