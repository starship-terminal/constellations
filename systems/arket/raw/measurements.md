# Component measurements

Computed styles read from arcade.software on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (the Finsweet consent banner, the Intercom launcher and the custom play cursor were hidden, never clicked or answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Consent and location dialogs

#### consent-card

Cookie consent card. "Before you start shopping": the consent card measured as it arrives, never answered.

Page: home. Selector: `.cookie-consent-popup`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 343 x 447.9 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.2 0px 4px 16px 0px |
| Outline | none |
| Font | __arketSansMono_00261e 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.banner-title: Arket Sans 16px/24px 400, #000000 |
| Transition | top, height 0.3s, 0.3s ease-in-out, ease-in-out delay 0s, 0s |
| Painted layers | div.cookie-consent-popup 343.0x447.9 bg #ffffff shadow #000000 @ 0.2 0px 4px 16px 0px; button.accept-button.consent-buttons 295.0x56.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px; button.accept-button.consent-buttons 295.0x56.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px; button.settings-button 172.0x40.0 bg #ffffff |
| How | at rest |

Crops: `consent-card-default.png`.

#### consent-accept

Accept all button. The consent primary. Measured, never pressed.

Page: home. Selector: `.cookie-consent-popup button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 295 x 56 | = | = | = |
| Padding | 4px 32px 6px 32px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 2px | = | = | = |
| Background | #000000 | #080808 | = | #080808 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arket Sans 20px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.accept-button.consent-buttons 295.0x56.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.accept-button.consent-buttons 295.0x56.0 bg #080808 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.accept-button.consent-buttons 295.0x56.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px outline 1px auto #005fcc offset 0px | button.accept-button.consent-buttons 295.0x56.0 bg #080808 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px |
| Ancestor paint | 3 up div.cookie-consent-popup bg #ffffff shadow #000000 @ 0.2 0px 4px 16px 0px | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `consent-accept-default.png`, `consent-accept-hover.png`, `consent-accept-focus-visible.png`, `consent-accept-pressed.png`.

#### consent-required

Only required cookies button. The consent secondary. Measured, never pressed.

Page: home. Selector: `.cookie-consent-popup button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 295 x 56 | = | = | = |
| Padding | 4px 32px 6px 32px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 2px | = | = | = |
| Background | #000000 | #080808 | = | #080808 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arket Sans 20px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.accept-button.consent-buttons 295.0x56.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.accept-button.consent-buttons 295.0x56.0 bg #080808 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.accept-button.consent-buttons 295.0x56.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px outline 1px auto #005fcc offset 0px | button.accept-button.consent-buttons 295.0x56.0 bg #080808 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px |
| Ancestor paint | 3 up div.cookie-consent-popup bg #ffffff shadow #000000 @ 0.2 0px 4px 16px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `consent-required-default.png`, `consent-required-hover.png`, `consent-required-focus-visible.png`, `consent-required-pressed.png`.

#### consent-settings-link

Cookie settings link. The text link to the settings panel. Measured, never pressed.

Page: home. Selector: `consent settings link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171.98 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arket Sans SC 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #080808 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.settings-button 172.0x40.0 bg #ffffff | = | button.settings-button 172.0x40.0 bg #ffffff outline 1px auto #005fcc offset 0px | = |
| Ancestor paint | 2 up div.cookie-consent-popup bg #ffffff shadow #000000 @ 0.2 0px 4px 16px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `consent-settings-link-default.png`, `consent-settings-link-hover.png`, `consent-settings-link-focus-visible.png`, `consent-settings-link-pressed.png`.

#### location-dialog

Location dialog. "Please confirm your location", the auto-mounted <dialog>. Measured, never answered.

Page: home. Selector: `dialog:has-text("confirm your location")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 538 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.font-regular.bg-transparent: arketSansMono 22px/28px 400, #000000 |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 16 x 16, colour #000000 |
| Painted layers | dialog.w-full.rounded-t-4 538.0x900.0 bg #ffffff; hr.mx-16.border-y 490.0x2.0 border T:1px solid #000000 / B:1px solid #000000; input.bg-white.peer 490.0x56.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 r 2px; label.absolute.pointer-events-none 104.2x20.0 bg #ffffff; span.bg-white.text-black 48.0x48.0 bg #ffffff; details.flex.flex-col 490.0x198.0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2px 10px 2px |
| How | at rest |

Crops: `location-dialog-default.png`.

#### location-search

Country search field. The "Search country" input; focused only, nothing typed.

Page: home. Selector: `location dialog input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 490 x 56 | = |
| Padding | 16px 56px 16px 16px | = |
| Border | 1px solid #767676 | 1px solid #000000 |
| Radius | 2px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 0px |
| Font | arketSansMono 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #9ca3af, opacity 1 | = |
| Painted layers | input.bg-white.peer 490.0x56.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 r 2px | input.bg-white.peer 490.0x56.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field |

Crops: `location-search-default.png`, `location-search-focused.png`.

#### location-continue

Continue to country button. The black confirm action. Measured, never pressed.

Page: home. Selector: `Continue to <country>`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 458 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 2px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.bg-black.hover:bg-black 458.0x32.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px | = | button.bg-black.hover:bg-black 458.0x32.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px outline 1px auto #005fcc offset 0px | = |
| Ancestor paint | 2 up details.flex.flex-col shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2px 10px 2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `location-continue-default.png`, `location-continue-hover.png`, `location-continue-focus-visible.png`, `location-continue-pressed.png`.

#### location-stay

Stay in country button. The outlined alternative. Measured, never pressed.

Page: home. Selector: `Stay in <country>`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 458 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #000000 | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #ffffff | = | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.border-black.hover:bg-black 458.0x32.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.border-black.hover:bg-black 458.0x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.border-black.hover:bg-black 458.0x32.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px outline 1px auto #005fcc offset 0px | button.border-black.hover:bg-black 458.0x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px |
| Ancestor paint | 2 up details.flex.flex-col shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2px 10px 2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `location-stay-default.png`, `location-stay-hover.png`, `location-stay-focus-visible.png`, `location-stay-pressed.png`.

#### location-row

Country row. A country/currency row in the list. Measured, never pressed.

Page: home. Selector: `country row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 490 x 38 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | arketSansMono 10px/15px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #000000 | = |
| Transition | none | = |
| Icon | 12 x 8, colour #000000 | = |
| Painted layers | details.flex.flex-col 490.0x38.0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2px 10px 2px; button.bg-black.hover:bg-black 458.0x32.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px | = |
| How | at rest | mouse hover |

Crops: `location-row-default.png`, `location-row-hover.png`.

### Shell and navigation

#### locale-notice

Locale notice bar. The top "Location and language: <country>/<lang>" strip with Change and Close.

Page: home. Selector: `locale notice strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 379.06 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `locale-notice-default.png`.

#### promo-strip

Promo strip. The thin promo line under the notice bar.

Page: home. Selector: `promo strip section`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #f5f5f5; L: none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-16.leading-22: arketSansMono 16px/16px 400, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | section.relative.flex 1440.0x56.0 bg #ffffff border B:1px solid #f5f5f5 |
| How | at rest |

Crops: `promo-strip-default.png`.

#### header

Header. The sticky z-header bar: wordmark, search field, account, wishlist, cart.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-20.uppercase: arketSansMono 16px/30px 400, #000000 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 0 x 0, colour #000000 |
| Painted layers | header.z-header.transition-colors 1440.0x120.0 bg #ffffff; div.grid.grid-cols-[auto_1fr_auto] 1440.0x120.0 border B:2px solid #000000; div.bg-white.transition-all 1376.0x30.0 bg #ffffff; div.desktop:z-header.pointer-events-none 1440.0x900.0 bg #a49b70 @ 0.2; div.desktop:hidden.absolute 0.0x0.0 bg #faf8f3; div.absolute.top-0 376.7x724.0 bg #ffffff |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo.

Page: home. Selector: `a:has-text("ARKET")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 43.31 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.group-hover:underline.group-focus:underline: arketSCSansMono 16px/16px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav item. A top-level shop category button; opens the nav drawer at that section.

Page: home. Selector: `nav button "Women"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.57 x 30 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 64px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Text node | span.text-20.uppercase: arketSansMono 16px/30px 400, #000000 | span.text-20.uppercase: arketSansMono 16px/30px 400, #ffffff | = | span.text-20.uppercase: arketSansMono 16px/30px 400, #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 0 x 0, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.flex.w-full 71.6x30.0 bg #000000 r 2px | button.flex.w-full 71.6x30.0 r 2px outline 1px auto #005fcc offset 0px | button.flex.w-full 71.6x30.0 bg #000000 r 2px |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### account-button

Account button. The account icon button. Measured, never followed.

Page: home. Selector: `button:has-text("My account")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.69 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.group-hover:underline.group-focus:underline: arketSansMono 16px/22px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.inline-flex 85.7x22.0 outline 1px auto #005fcc offset 1px | = |

Crops: `account-button-default.png`, `account-button-hover.png`, `account-button-focus-visible.png`, `account-button-pressed.png`.

#### wishlist-link

Wishlist link. The wishlist icon link. Measured, never followed.

Page: home. Selector: `a:has-text("Wishlist")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 32 x 32, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.relative 32.0x32.0 outline 1px auto #005fcc offset 1px | = |

Crops: `wishlist-link-default.png`, `wishlist-link-hover.png`, `wishlist-link-focus-visible.png`, `wishlist-link-pressed.png`.

#### cart-button

Cart button. The bag icon button; opens the cart drawer.

Page: home. Selector: `button:has-text("Cart")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 32 x 32, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.relative 32.0x32.0 outline 1px auto #005fcc offset 0px | = |

Crops: `cart-button-default.png`, `cart-button-hover.png`, `cart-button-focus-visible.png`, `cart-button-pressed.png`.

#### locale-button

Locale button. The "AR | EN" region/language button. Measured, never pressed.

Page: home. Selector: `locale button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 73.23 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.flex.flex-row 73.2x22.0 outline 1px auto #005fcc offset 0px | = |

Crops: `locale-button-default.png`, `locale-button-hover.png`, `locale-button-focus-visible.png`, `locale-button-pressed.png`.

#### cafe-link

ARKET CAFÉ link. The café utility link. Measured, never followed.

Page: home. Selector: `a:has-text("ARKET CAFÉ")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 115.63 x 30 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-20.leading-26: arketSansMono 16px/30px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.flex.items-center 115.6x30.0 outline 1px auto #005fcc offset 1px | = |

Crops: `cafe-link-default.png`, `cafe-link-hover.png`, `cafe-link-focus-visible.png`, `cafe-link-pressed.png`.

#### search-field

Search field. The header search input; focused only, nothing typed or sent.

Page: home. Selector: `header input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 680 x 40 | = |
| Padding | 0px 48px 0px 44px | = |
| Border | none | = |
| Radius | 4px | = |
| Background | #f9f9f9 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | arketSansMono 16px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.6 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0.6, opacity 1 | = |
| Painted layers | input.block.h-32 680.0x40.0 bg #f9f9f9 r 4px | = |
| How | at rest | clicked into the field |

Crops: `search-field-default.png`, `search-field-focused.png`.

#### cart-drawer

Cart drawer, empty. The bag drawer after its own icon press; the signed-out bag is empty.

Page: home. Selector: `dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 538 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.font-regular.bg-transparent: arketSansMono 22px/28px 400, #000000 |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 24 x 24, colour #000000 |
| Painted layers | dialog.w-full.rounded-t-4 538.0x900.0 bg #ffffff; div.sticky.border-b 538.0x113.0 border B:1px solid #eaeae8; a.flex.h-48 490.0x48.0 bg #000000 r 2px; div.w-full.overflow-y-scroll 538.0x514.0 bg #ffffff @ 0.6 r 6px; button.border-black.hover:bg-transparent 245.0x48.0 border B:2px solid #000000; button.border-grey-dark.hover:border-grey-mid 245.0x48.0 border B:1px solid #767676 |
| How | at rest |

Crops: `cart-drawer-default.png`.

### Customer service

#### service-link

Service link.

Page: service. Selector: `main a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43.31 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.group-hover:underline.group-focus:underline: arketSCSansMono 16px/16px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.inline-flex 43.3x40.0 outline 1px auto #005fcc offset 1px | = |

Crops: `service-link-default.png`, `service-link-hover.png`, `service-link-focus-visible.png`, `service-link-pressed.png`.

#### service-title

Service title.

Page: service. Selector: `main h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 688 x 34 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.font-regular.bg-transparent: arketSansMono 28px/34px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `service-title-default.png`.

#### service-accordion

Service accordion. A help-topic disclosure row.

Page: service. Selector: `main disclosure`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 688 x 50 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 2px | = | = | = |
| Background | #000000 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 22px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 22px/28px 400, #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.bg-black.hover:bg-black 688.0x50.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px | = | button.bg-black.hover:bg-black 688.0x50.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `service-accordion-default.png`, `service-accordion-hover.png`, `service-accordion-focus-visible.png`, `service-accordion-pressed.png`.

#### service-accordion-open

Service accordion, open. The same row after its own toggle.

Page: service. Selector: `main disclosure`. States: opened.

| Property | opened |
|---|---|
| Error | toggle refused: BUTTON "Track order" |

Crops: none.

### Home

#### hero-title

Hero heading.

Page: home. Selector: `first main h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 208.41 x 34 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 28px/34px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### tile-card

Campaign tile. A hero/editorial image tile link (the whole tile is the link).

Page: home. Selector: `main a:has(img)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 720 x 960.05 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | arketSansMono 10px/15px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `tile-card-default.png`, `tile-card-hover.png`.

#### section-title

Section heading.

Page: home. Selector: `h2/h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 208.41 x 34 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 28px/34px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### tile-label

Tile label. The text on a campaign tile.

Page: home. Selector: `inside campaign tile`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 22px/28px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 3 up a.flex.flex-row shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.1 0px 2px 10px 2px |
| How | at rest |

Crops: `tile-label-default.png`.

### Listing page

#### plp-title

Category title. "Women's clothes" h1.

Page: clothing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 624 x 50 |
| Padding | 0px 0px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 28px/34px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `plp-title-default.png`.

#### breadcrumb

Breadcrumb. The ARKET / Women / Clothing trail.

Page: clothing. Selector: `breadcrumb`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 443.53 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-20.uppercase: arketSansMono 16px/30px 400, #000000 |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | div.absolute.top-0 376.7x724.0 bg #ffffff; div.relative.grid 376.7x724.0 border R:1px solid #000000; button.sticky.top-0 0.0x0.0 bg #ffffff; ul.mb-32.grid 375.7x400.0 bg #ffffff; div.bottom-0.w-full 396.9x724.0 bg #ffffff; button.sticky.top-0 0.0x0.0 bg #ffffff |
| How | at rest |

Crops: `breadcrumb-default.png`.

#### read-more

Read more button. The category intro expander; a local toggle, measured closed.

Page: clothing. Selector: `button:has-text("Read more")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.57 x 22 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 99990px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 12px/16px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #000000 | = | = | = |
| Painted layers | button.flex.items-center 93.6x22.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 99990px | = | button.flex.items-center 93.6x22.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 99990px outline 1px auto #005fcc offset 0px | = |
| Ancestor paint | 1 up span.absolute.bottom-0 bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `read-more-default.png`, `read-more-hover.png`, `read-more-focus-visible.png`, `read-more-pressed.png`.

#### filter-button

Filter button. Opens the filter panel. Measured, never applied.

Page: clothing. Selector: `button:has-text("Filter")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.85 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #000000 | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #ffffff | = | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | 16 x 16, colour #ffffff | = | 16 x 16, colour #ffffff |
| Painted layers | button.border-black.hover:bg-black 88.9x32.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.border-black.hover:bg-black 88.9x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.border-black.hover:bg-black 88.9x32.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px outline 1px auto #005fcc offset 0px | button.border-black.hover:bg-black 88.9x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `filter-button-default.png`, `filter-button-hover.png`, `filter-button-focus-visible.png`, `filter-button-pressed.png`.

#### filter-panel

Filter panel, open. The filter sheet after the Filter button's own press; nothing inside was applied.

Page: clothing. Selector: `filter dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 538 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | dialog.w-full.rounded-t-4 538.0x900.0 bg #ffffff |
| How | at rest |

Crops: `filter-panel-default.png`.

#### filter-option

Filter option. A filter facet row inside the open panel; measured, never selected.

Page: clothing. Selector: `filter facet`. States: .

Not found on the page at capture time.

#### sort-button

Sort button. The sort control. Measured, never opened.

Page: clothing. Selector: `button:has-text("Sort by")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102.2 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #000000 | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #ffffff | = | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #ffffff |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | 16 x 16, colour #ffffff | = | 16 x 16, colour #ffffff |
| Painted layers | button.border-black.hover:bg-black 102.2x32.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.border-black.hover:bg-black 102.2x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px | button.border-black.hover:bg-black 102.2x32.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px outline 1px auto #005fcc offset 0px | button.border-black.hover:bg-black 102.2x32.0 bg #000000 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `sort-button-default.png`, `sort-button-hover.png`, `sort-button-focus-visible.png`, `sort-button-pressed.png`.

#### view-button

View button. The grid-density control. Measured, never pressed.

Page: clothing. Selector: `button:has-text("View")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86.34 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 2px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.font-regular.bg-transparent: arketSansMono 16px/22px 400, #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | button.bg-white.hover:bg-white 86.3x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px | = | button.bg-white.hover:bg-white 86.3x32.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 2px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `view-button-default.png`, `view-button-hover.png`, `view-button-focus-visible.png`, `view-button-pressed.png`.

#### product-card

Product card. A listing card: image, name, price, "+N" colours.

Page: clothing. Selector: `a.text-center product card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 357 x 109.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | arketSansMono 10px/15px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.font-regular.bg-transparent: arketSansMono 16px/18px 400, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.block.h-16 14.0x16.0 bg #272a3e border T:1px solid #eaeae8 / R:1px solid #eaeae8 / B:1px solid #eaeae8 / L:1px solid #eaeae8 r 2px; span.block.h-16 14.0x16.0 bg #4c3b3d border T:1px solid #eaeae8 / R:1px solid #eaeae8 / B:1px solid #eaeae8 / L:1px solid #eaeae8 r 2px; span.block.h-16 14.0x16.0 bg #e32b35 border T:1px solid #eaeae8 / R:1px solid #eaeae8 / B:1px solid #eaeae8 / L:1px solid #eaeae8 r 2px | = |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### card-badge

New badge. The "New" tag on a card image.

Page: clothing. Selector: `badge a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 357 x 476 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.flex.items-center: arketSCSansMono 12px/12px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.flex.items-center 35.3x18.0 bg #fff3db r 1px |
| How | at rest |

Crops: `card-badge-default.png`.

#### product-name

Product name. The card text block: name, price, colour count.

Page: clothing. Selector: `card text block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 357 x 109.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.font-regular.bg-transparent: arketSansMono 16px/18px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.block.h-16 14.0x16.0 bg #272a3e border T:1px solid #eaeae8 / R:1px solid #eaeae8 / B:1px solid #eaeae8 / L:1px solid #eaeae8 r 2px; span.block.h-16 14.0x16.0 bg #4c3b3d border T:1px solid #eaeae8 / R:1px solid #eaeae8 / B:1px solid #eaeae8 / L:1px solid #eaeae8 r 2px; span.block.h-16 14.0x16.0 bg #e32b35 border T:1px solid #eaeae8 / R:1px solid #eaeae8 / B:1px solid #eaeae8 / L:1px solid #eaeae8 r 2px |
| How | at rest |

Crops: `product-name-default.png`.

#### price

Price. The "$ 349" price text inside a card.

Page: clothing. Selector: `card price text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 46.32 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 16px/18px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `price-default.png`.

#### more-colors

More colours chip. The "+2" colour count.

Page: clothing. Selector: `"+N" chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 17.05 x 19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSCSansMono 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `more-colors-default.png`.

#### card-add-bag

Quick add-to-bag. The card's quick-add control, shown only while the card image is hovered. Measured, never pressed.

Page: clothing. Selector: `button:has-text("Add to bag")`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 36 x 35 | - |
| Padding | 0px | - |
| Border | none | - |
| Radius | 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | arketSansMono 10px/15px 400 | - |
| Letter spacing | normal | - |
| Colour | #000000 | - |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | - |
| Cursor | pointer | - |
| Icon | 13 x 35, colour #000000 | - |
| Ancestor paint | 1 up div.flex.items-center bg #ffffff | - |
| How | at rest | - |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('button[aria-label*="add to bag" i], button:has-text("Add to bag")').first().filter({ visible: true }).first().filter({ visibl |

Crops: `card-add-bag-default.png`.

#### card-wishlist

Card wishlist button. The heart quick-toggle, shown on card hover. Measured, never pressed.

Page: clothing. Selector: `button:has-text("Add to wishlist")`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 36 x 35 | - |
| Padding | 0px | - |
| Border | none | - |
| Radius | 0px | - |
| Background | transparent | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | arketSansMono 10px/15px 400 | - |
| Letter spacing | normal | - |
| Colour | #000000 | - |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | - |
| Cursor | pointer | - |
| Icon | 17 x 35, colour #000000 | - |
| Ancestor paint | 1 up div.flex.items-center bg #ffffff | - |
| How | at rest | - |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('button[aria-label*="wishlist" i], button:has-text("Add to wishlist")').first().filter({ visible: true }).first().filter({ vis |

Crops: `card-wishlist-default.png`.

#### card-img-prev

Card image previous. The card image carousel arrow, shown on card hover.

Page: clothing. Selector: `button:has-text("Previous image")`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 36 x 36 | - |
| Padding | 0px | - |
| Border | none | - |
| Radius | 2px | - |
| Background | #ffffff | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | arketSansMono 10px/15px 400 | - |
| Letter spacing | normal | - |
| Colour | #000000 | - |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | - |
| Opacity | 0.3 | - |
| Cursor | not-allowed | - |
| Icon | 14 x 36, colour #000000 | - |
| Painted layers | button.min-h-16.min-w-16 36.0x36.0 bg #ffffff r 2px | - |
| How | at rest | - |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('button[aria-label*="previous image" i], button:has-text("Previous image")').first().filter({ visible: true }).first().filter( |

Crops: `card-img-prev-default.png`.

#### card-img-next

Card image next. The card image carousel arrow, shown on card hover.

Page: clothing. Selector: `button:has-text("Next image")`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 36 x 36 | - |
| Padding | 0px | - |
| Border | none | - |
| Radius | 2px | - |
| Background | #ffffff | - |
| Box shadow | none | - |
| Outline | none | - |
| Font | arketSansMono 10px/15px 400 | - |
| Letter spacing | normal | - |
| Colour | #000000 | - |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | - |
| Cursor | pointer | - |
| Icon | 14 x 36, colour #000000 | - |
| Painted layers | button.min-h-16.min-w-16 36.0x36.0 bg #ffffff r 2px | - |
| How | at rest | - |
| Error | - | locator.hover: Timeout 5000ms exceeded. Call log:   - waiting for locator('button[aria-label*="next image" i], button:has-text("Next image")').first().filter({ visible: true }).first().filter({ visibl |

Crops: `card-img-next-default.png`.

### Account gate

#### gate-title

Gate title. The Login/Signup gate heading.

Page: account. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 624 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arket-Sans-Mono 24px/30px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `gate-title-default.png`.

#### gate-field

Email field. The sign-in email input; focused only, nothing typed or sent.

Page: account. Selector: `account input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 624 x 60 | = |
| Padding | 8px 8px 10px 15px | = |
| Border | 1px solid #767676 | = |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arket-Sans-Mono 16px/22.08px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #808080, opacity 1 | = |
| Painted layers | input 624.0x60.0 bg #ffffff border T:1px solid #767676 / R:1px solid #767676 / B:1px solid #767676 / L:1px solid #767676 | = |
| How | at rest | clicked into the field |

Crops: `gate-field-default.png`, `gate-field-focused.png`.

#### gate-continue

Continue button. The gate's primary action. Measured, never pressed — no sign-in was attempted.

Page: account. Selector: `account button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 304 x 48 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Arket-Sans-Mono 16px/22.08px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.social-media-button: Arket-Sans-Mono 16px/22.08px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 20px x 20px, static, bg #000000 @ 0 url(…), radius 0px | = | = | = |
| Painted layers | button.accountButton.firstButton 304.0x48.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 | = | button.accountButton.firstButton 304.0x48.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `gate-continue-default.png`, `gate-continue-hover.png`, `gate-continue-focus-visible.png`, `gate-continue-pressed.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 464 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.group-hover:underline.group-focus:underline: arketSansMono 22px/28px 400, #000000 |
| Transition | none |
| Icon | 1080 x 34, colour #000000 |
| Painted layers | div.border-t-2.border-black 1440.0x418.0 bg #ffffff border T:2px solid #000000; div.flex.flex-col 1440.0x46.0 bg #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-heading

Footer heading.

Page: home. Selector: `footer h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 138.65 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 22px/28px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `footer-heading-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.65 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h2.group-hover:underline.group-focus:underline: arketSansMono 22px/28px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.group.inline-flex 138.6x28.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.inline-block.h-24 24.0x24.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 107 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-20.uppercase: arketSansMono 20px/28px 400, #000000 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 24 x 24, colour #000000 |
| Painted layers | header.z-header.transition-colors 390.0x107.0 bg #ffffff; div.grid.grid-cols-[auto_1fr_auto] 390.0x107.0 border B:1px solid #000000; div.bg-white.transition-all 390.0x431.0 bg #ffffff; div.desktop:hidden.absolute 390.0x844.0 bg #faf8f3; button.flex.w-full 390.0x52.0 border T:1px solid #eaeae8; button.flex.w-full 390.0x52.0 border T:1px solid #eaeae8 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button.

Page: home. Selector: `button[aria-label="menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.min-h-16.min-w-16 24.0x24.0 outline 1px auto #005fcc offset 0px | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-focus-visible.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The bar after its own toggle; the crop is the opened drawer that holds the links and actions.

Page: home. Selector: `button[aria-label="menu"]`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Icon | 24 x 24, colour #000000 |
| How | own toggle |

Crops: none.

#### m-nav-link

Mobile nav link. Read inside the open menu.

Page: home. Selector: `drawer nav item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 52 |
| Padding | 11px 16px 12px 16px |
| Gap | 64px |
| Border | T: 1px solid #eaeae8; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | arketSansMono 10px/15px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-20.uppercase: arketSansMono 20px/28px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 20 x 20, colour #000000 |
| Painted layers | button.flex.w-full 390.0x52.0 border T:1px solid #eaeae8 |
| How | at rest |

Crops: `m-nav-link-default.png`.

#### m-search

Mobile search. The mobile search affordance, header or drawer.

Page: home. Selector: `mobile search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | arketSansMono 10px/15px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.min-h-16.min-w-16 24.0x24.0 outline 1px auto #005fcc offset 0px | = |

Crops: `m-search-default.png`, `m-search-hover.png`, `m-search-focus-visible.png`, `m-search-pressed.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `transform 0.3s`, `opacity 0.1s`, `0.3s`, `transform 0.2s`, `none`, `top 0.3s ease-in-out, height 0.3s ease-in-out`, `right 0.3s ease-in-out`, `opacity 0.3s`, `0.4s`
