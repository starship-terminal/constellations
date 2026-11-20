# Component measurements

Computed styles read from care.com on 2026-11-12 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public marketing pages, the /child-care category page, the /babysitters provider listing, the signed-out login and join cards and the pricing surface — with the cookie banner and the "Join Care.com" signup-gate modal hidden after their own measurement (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The fixed header: wordmark, the Find care / Find jobs / List your business / Resources mega-menu triggers, Log in and the Join-now pill.

Page: home. Selector: `header.CareHeaderContainer-root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 104 |
| Padding | 24px 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | div.MuiTypography-root.MuiTypography-body2: Oceanic Grotesk 16px/24px 400, #ffffff |
| Transition | background-color 0.3s ease-in-out |
| Icon | 230 x 40, colour #377a69 |
| Painted layers | a::before.MuiTypography-root.MuiTypography-inherit autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; button::before.MuiButtonBase-root.DesktopDropdownButton--root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; button::before.MuiButtonBase-root.DesktopDropdownButton--root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; button::before.MuiButtonBase-root.DesktopDropdownButton--root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; button::before.MuiButtonBase-root.DesktopDropdownButton--root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a::before.MuiTypography-root.MuiTypography-body2 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Care.com wordmark anchor.

Page: home. Selector: `header logo a`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 230 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #377a69 |
| Transition | none |
| Cursor | pointer |
| Icon | 230 x 40, colour #377a69 |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 6px |
| Painted layers | a::before.MuiTypography-root.MuiTypography-inherit autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-trigger

Nav trigger. The "Find care" button that opens the mega menu; toggled, never followed.

Page: home. Selector: `header button Find care`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 92.83 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.MuiTypography-root.MuiTypography-body2: Oceanic Grotesk 16px/24px 400, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #ffffff | = | = | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 6px | = | 108.828px x 32px, absolute, bg #000000 @ 0, radius 6px | = |
| Painted layers | button::before.MuiButtonBase-root.DesktopDropdownButton--root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = | button::before.MuiButtonBase-root.Mui-focusVisible 108.828pxx32px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### login-link

Log-in link. The header Log-in action; measured, never followed.

Page: home. Selector: `header a Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43.44 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 6px | = | 59.4375px x 32px, absolute, bg #000000 @ 0, radius 6px | = |
| Painted layers | a::before.MuiTypography-root.MuiTypography-body2 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = | a::before.MuiTypography-root.MuiTypography-body2 59.4375pxx32px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### join-cta

Join CTA. The green Join-now header action; measured, never followed.

Page: home. Selector: `header Join now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170 x 40 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | 1px solid #d0f5a3 | 1px solid #e4ffb8 | none | 1px solid #8ae718 |
| Radius | 20px | = | = | = |
| Background | #d0f5a3 | #e4ffb8 | = | #8ae718 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 16px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #025747 | = | = | = |
| Transition | background 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.MuiTypography-root.MuiTypography-inherit 170.0x40.0 bg #d0f5a3 border T:1px solid #d0f5a3 / R:1px solid #d0f5a3 / B:1px solid #d0f5a3 / L:1px solid #d0f5a3 r 20px | a.MuiTypography-root.MuiTypography-inherit 170.0x40.0 bg #e4ffb8 border T:1px solid #e4ffb8 / R:1px solid #e4ffb8 / B:1px solid #e4ffb8 / L:1px solid #e4ffb8 r 20px | a.MuiTypography-root.MuiTypography-inherit 170.0x40.0 bg #d0f5a3 r 20px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | a.MuiTypography-root.MuiTypography-inherit 170.0x40.0 bg #8ae718 border T:1px solid #8ae718 / R:1px solid #8ae718 / B:1px solid #8ae718 / L:1px solid #8ae718 r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `join-cta-default.png`, `join-cta-hover.png`, `join-cta-focus-visible.png`, `join-cta-pressed.png`.

#### nav-dropdown

Mega menu. The Find-care mega menu panel, opened by its own trigger.

Page: home. Selector: `nav.MegaMenu--root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 928 x 360 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | h4.MuiTypography-root.MuiTypography-h4: Oceanic Grotesk 16px/20px 500, #1e1e1e |
| Transition | none |
| Icon | 24 x 24, colour #1e1e1e |
| Painted layers | div.MuiBox-root.mui-bm0daf 196.0x360.0 bg #f6f3ee; button.MuiButtonBase-root.MegaMenu--item 164.0x48.0 bg #ffffff r 8px; button::before.MuiButtonBase-root.MegaMenu--item autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 8px; button::before.MuiButtonBase-root.MegaMenu--item autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 8px; button::before.MuiButtonBase-root.MegaMenu--item autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 8px; button::before.MuiButtonBase-root.MegaMenu--item autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 8px |
| Ancestor paint | 2 up div.MuiPaper-root.MuiPaper-elevation bg #ffffff shadow #000000 @ 0.15 0px 4px 16px 0px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-item

Mega-menu tab. A category tab inside the mega menu (Child care active by default).

Page: home. Selector: `button.MegaMenu--item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 164 x 48 | = | = | = |
| Padding | 0px 10px 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | h4.MuiTypography-root.MuiTypography-h4: Oceanic Grotesk 16px/20px 500, #1e1e1e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1e1e1e | = | = | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 8px | = | 164px x 48px, absolute, bg #000000 @ 0, radius 8px | 164px x 48px, absolute, bg #000000 @ 0, radius 8px |
| Painted layers | button.MuiButtonBase-root.MegaMenu--item 164.0x48.0 bg #ffffff r 8px; button::before.MuiButtonBase-root.MegaMenu--item autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 8px | = | button.MuiButtonBase-root.Mui-focusVisible 164.0x48.0 bg #ffffff r 8px; button::before.MuiButtonBase-root.Mui-focusVisible 164pxx48px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 8px | button.MuiButtonBase-root.Mui-focusVisible 164.0x48.0 bg #ffffff r 8px; button::before.MuiButtonBase-root.Mui-focusVisible 164pxx48px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 8px |
| Ancestor paint | 1 up div.MuiBox-root.mui-bm0daf bg #f6f3ee | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-item-default.png`, `menu-item-hover.png`, `menu-item-focus-visible.png`, `menu-item-pressed.png`.

#### menu-link

Menu link. A link inside the opened mega menu.

Page: home. Selector: `mega menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 250 x 44 | = | = | = |
| Padding | 10px 0px 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #377a69 | = | = | = |
| Text node | span.NavLink--content.MuiBox-root: Oceanic Grotesk 16px/24px 400, #377a69 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 6px | = | 250px x 40px, absolute, bg #000000 @ 0, radius 6px | 250px x 40px, absolute, bg #000000 @ 0, radius 6px |
| Painted layers | a::before.MuiTypography-root.MuiTypography-body2 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = | a::before.MuiTypography-root.MuiTypography-body2 250pxx40px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | a::before.MuiTypography-root.MuiTypography-body2 250pxx40px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

### Home

#### hero-title

Hero headline. The hero display headline over the photo ("Connecting families with quality, local caregivers"); the testimonial-name accentHeadline1 h1s are excluded.

Page: home. Selector: `largest display text in the hero fold`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 700 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NaN Druid Sans 64px/72px 550 |
| Letter spacing | -2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### zip-field

ZIP field. The hero ZIP-code search input; focused and given a sample ZIP that was deleted again — never searched.

Page: home. Selector: `input[placeholder=ZIP code]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 270 x 25.88 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Oceanic Grotesk 18px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #1e1e1e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #707070, opacity 1 | = | = |
| Ancestor paint | 1 up div.MuiInputBase-root.MuiInput-root bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `zip-field-default.png`, `zip-field-focused.png`, `zip-field-filled.png`.

#### search-cta

Search CTA. The green Search action under the ZIP field; measured, never pressed.

Page: home. Selector: `button.MuiButton-contained Search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344 x 56 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Border | 1px solid #d0f5a3 | 1px solid #e4ffb8 | none | 1px solid #8ae718 |
| Radius | 28px | = | = | = |
| Background | #d0f5a3 | #e4ffb8 | = | #8ae718 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 20px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #025747 | = | = | = |
| Transition | background 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.MuiButtonBase-root.MuiButton-root 344.0x56.0 bg #d0f5a3 border T:1px solid #d0f5a3 / R:1px solid #d0f5a3 / B:1px solid #d0f5a3 / L:1px solid #d0f5a3 r 28px | button.MuiButtonBase-root.MuiButton-root 344.0x56.0 bg #e4ffb8 border T:1px solid #e4ffb8 / R:1px solid #e4ffb8 / B:1px solid #e4ffb8 / L:1px solid #e4ffb8 r 28px | button.MuiButtonBase-root.MuiButton-root 344.0x56.0 bg #d0f5a3 r 28px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | button.MuiButtonBase-root.MuiButton-root 344.0x56.0 bg #8ae718 border T:1px solid #8ae718 / R:1px solid #8ae718 / B:1px solid #8ae718 / L:1px solid #8ae718 r 28px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-cta-default.png`, `search-cta-hover.png`, `search-cta-focus-visible.png`, `search-cta-pressed.png`.

#### category-card

Category card. A "One membership" category card (Child care, Senior care, Pet care ...); measured, never followed.

Page: home. Selector: `a.MuiLink-root category card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 200 x 252 | = | - | = |
| Padding | 32px 24px | = | - | = |
| Border | none | = | - | = |
| Radius | 24px | = | - | = |
| Background | #ffffff | #f5f5f5 | - | #e8e8e8 |
| Box shadow | none | = | - | = |
| Outline | none | 1px solid #707070 offset 0px | - | 1px solid #707070 offset 0px |
| Font | Oceanic Grotesk 18px/28px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1e1e1e | = | - | = |
| Text node | span.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 18px/24px 500, #1e1e1e | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #1e1e1e | = | - | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 24px | = | - | = |
| Painted layers | a.MuiTypography-root.MuiTypography-inherit 200.0x252.0 bg #ffffff r 24px; a::before.MuiTypography-root.MuiTypography-inherit autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 24px | a.MuiTypography-root.MuiTypography-inherit 200.0x252.0 bg #f5f5f5 r 24px outline 1px solid #707070 offset 0px; a::before.MuiTypography-root.MuiTypography-inherit autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 24px | - | a.MuiTypography-root.MuiTypography-inherit 200.0x252.0 bg #e8e8e8 r 24px outline 1px solid #707070 offset 0px; a::before.MuiTypography-root.MuiTypography-inherit autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 24px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `category-card-default.png`, `category-card-hover.png`, `category-card-pressed.png`.

#### section-h2

Section heading. A section display heading ("One membership for every season of life").

Page: home. Selector: `h2.display2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 657.05 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NaN Druid Sans 40px/40px 550 |
| Letter spacing | -1px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

### Category page

#### cat-h1

Category title. The category page display title ("Find child care on your terms").

Page: childcare. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NaN Druid Sans 64px/72px 550 |
| Letter spacing | -2px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `cat-h1-default.png`.

#### service-card

Service card. A service-card panel (Nannies / Babysitters / Daycares ...) in the services grid.

Page: childcare. Selector: `.MuiPaper-root service card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 608 x 512 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 32px | = | - | = |
| Background | #ffffff | = | - | = |
| Box shadow | none | #000000 @ 0.15 0px 4px 16px 0px | - | #000000 @ 0.15 0px 4px 16px 0px |
| Outline | none | = | - | = |
| Font | Oceanic Grotesk 18px/28px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1e1e1e | = | - | = |
| Text node | a.MuiTypography-root.MuiTypography-h2: Oceanic Grotesk 24px/32px 500, #1e1e1e | = | - | = |
| Transition | box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Painted layers | div.MuiPaper-root.MuiPaper-elevation 608.0x512.0 bg #ffffff r 32px; a::before.MuiTypography-root.MuiTypography-h2 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a.MuiButtonBase-root.MuiButton-root 144.3x40.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px | div.MuiPaper-root.MuiPaper-elevation 608.0x512.0 bg #ffffff r 32px shadow #000000 @ 0.15 0px 4px 16px 0px; a::before.MuiTypography-root.MuiTypography-h2 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a.MuiButtonBase-root.MuiButton-root 144.3x40.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px | - | div.MuiPaper-root.MuiPaper-elevation 608.0x512.0 bg #ffffff r 32px shadow #000000 @ 0.15 0px 4px 16px 0px; a::before.MuiTypography-root.MuiTypography-h2 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a.MuiButtonBase-root.MuiButton-root 144.3x40.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Cursor | - | pointer | = | pointer |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `service-card-default.png`, `service-card-hover.png`, `service-card-pressed.png`.

#### service-cta

Service CTA. A card action ("Find babysitters"); measured, never followed.

Page: childcare. Selector: `service card action`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 144.33 x 40 | = | 142.33 x 40 | = |
| Padding | 8px 24px | = | = | = |
| Border | 1px solid #025747 | 1px solid #377a69 | none | 1px solid #034135 |
| Radius | 20px | = | = | = |
| Background | #025747 | #377a69 | = | #034135 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 16px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e4ffb8 | = | = | = |
| Transition | background 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.MuiButtonBase-root.MuiButton-root 144.3x40.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px | a.MuiButtonBase-root.MuiButton-root 144.3x40.0 bg #377a69 border T:1px solid #377a69 / R:1px solid #377a69 / B:1px solid #377a69 / L:1px solid #377a69 r 20px | a.MuiButtonBase-root.MuiButton-root 142.3x40.0 bg #025747 r 20px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | a.MuiButtonBase-root.MuiButton-root 144.3x40.0 bg #034135 border T:1px solid #034135 / R:1px solid #034135 / B:1px solid #034135 / L:1px solid #034135 r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 3 up div.MuiPaper-root.MuiPaper-elevation bg #ffffff shadow #000000 @ 0.15 0px 4px 16px 0px | = | = |

Crops: `service-cta-default.png`, `service-cta-hover.png`, `service-cta-focus-visible.png`, `service-cta-pressed.png`.

#### review-card

Testimonial card. A member-quote card ("Trusted by families like yours").

Page: childcare. Selector: `testimonial .MuiCard-root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 410.66 x 256 |
| Padding | 8px 0px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | p.MuiTypography-root.MuiTypography-accentDisplay1: Oceanic Text Semibold 96px/80px 450, #025747 |
| Transition | box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.MuiPaper-root.MuiPaper-elevation 410.7x256.0 bg #ffffff r 24px |
| How | at rest |

Crops: `review-card-default.png`.

#### cat-faq

FAQ question. A question row in the category FAQ block; measured closed.

Page: childcare. Selector: `FAQ accordion row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 722.66 x 72 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | #000000 @ 0.12 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 18px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | h4.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 18px/24px 500, #1e1e1e | = | = | = |
| Transition | min-height, background-color 0.15s, 0.15s cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1e1e1e | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | div.MuiButtonBase-root.Mui-focusVisible 722.7x72.0 bg #000000 @ 0.12 | = |

Crops: `cat-faq-default.png`, `cat-faq-hover.png`, `cat-faq-focus-visible.png`, `cat-faq-pressed.png`.

### Provider listing

#### listing-h1

Listing title. The listing display title ("Find Local Babysitters").

Page: listing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NaN Druid Sans 64px/72px 550 |
| Letter spacing | -2px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `listing-h1-default.png`.

#### city-button

Location button. The outlined "City, State" location trigger on the listing toolbar; measured, never opened.

Page: listing. Selector: `button.MuiButton-outlined City State`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 252 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #025747 | = | 1px solid #4d9380 | = |
| Radius | 20px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #e8e8e8 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 14px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #034135 | = | = | = |
| Text node | p.MuiTypography-root.MuiTypography-body3: Oceanic Grotesk 18px/20px 400, #9b9b9b | = | = | = |
| Transition | background 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #034135 | = | = | = |
| Painted layers | button.MuiButtonBase-root.MuiButton-root 252.0x32.0 bg #ffffff border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px | button.MuiButtonBase-root.MuiButton-root 252.0x32.0 bg #f5f5f5 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px | button.MuiButtonBase-root.MuiButton-root 252.0x32.0 bg #ffffff border T:1px solid #4d9380 / R:1px solid #4d9380 / B:1px solid #4d9380 / L:1px solid #4d9380 r 20px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | button.MuiButtonBase-root.MuiButton-root 252.0x32.0 bg #e8e8e8 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `city-button-default.png`, `city-button-hover.png`, `city-button-focus-visible.png`, `city-button-pressed.png`.

#### filter-button

Filter button. The outlined Filter action on the listing toolbar; measured, never opened.

Page: listing. Selector: `button.MuiButton-outlined Filter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120 x 32 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Border | 1px solid #025747 | = | 1px solid #4d9380 | = |
| Radius | 20px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #e8e8e8 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 14px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #034135 | = | = | = |
| Text node | span.MuiTypography-root.MuiTypography-body1: Oceanic Grotesk 18px/28px 400, #034135 | = | = | = |
| Transition | background 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #034135 | = | = | = |
| Painted layers | button.MuiButtonBase-root.MuiButton-root 120.0x32.0 bg #ffffff border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px | button.MuiButtonBase-root.MuiButton-root 120.0x32.0 bg #f5f5f5 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px | button.MuiButtonBase-root.MuiButton-root 120.0x32.0 bg #ffffff border T:1px solid #4d9380 / R:1px solid #4d9380 / B:1px solid #4d9380 / L:1px solid #4d9380 r 20px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | button.MuiButtonBase-root.MuiButton-root 120.0x32.0 bg #e8e8e8 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `filter-button-default.png`, `filter-button-hover.png`, `filter-button-focus-visible.png`, `filter-button-pressed.png`.

#### gate-dialog

Signup-gate dialog. The "Join Care.com" modal the listing mounts over the results once they are scrolled to: measured open, then hidden, never answered or submitted.

Page: listing. Selector: `join gate dialog`. States: .

Not found on the page at capture time.

#### gate-cta

Gate CTA. The gate dialog's primary action; measured, never pressed.

Page: listing. Selector: `gate dialog action`. States: .

Not found on the page at capture time.

#### provider-card

Provider card. A caregiver listing row (first name + initial, photo, rate, tags, review count) — a real person's public profile summary; structure only, measured, never followed.

Page: listing. Selector: `provider grid row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 645.33 x 160 | = | = | = |
| Padding | 0px 0px 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 18px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | h2.MuiTypography-root.MuiTypography-h2: Oceanic Grotesk 24px/32px 500, #1e1e1e | = | = | = |
| Transition | none | = | = | = |
| Icon | 24 x 24, colour #1e1e1e | = | = | = |
| Painted layers | a::before.MuiTypography-root.MuiTypography-h3 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = | a::before.MuiTypography-root.MuiTypography-h3 473.984pxx40px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `provider-card-default.png`, `provider-card-hover.png`, `provider-card-focus-visible.png`, `provider-card-pressed.png`.

#### care-tag

Care tag. A service chip on the provider card (light cleaning, meal prep, travel ...).

Page: listing. Selector: `.CareTag chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.95 x 24 | = | - | = |
| Padding | 2px 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 4px | = | - | = |
| Background | #f5f5f5 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Oceanic Grotesk 18px/28px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1e1e1e | = | - | = |
| Text node | div.MuiTypography-root.MuiTypography-body3: Oceanic Grotesk 14px/20px 400, #1e1e1e | = | - | = |
| Transition | none | = | - | = |
| Painted layers | div.CareTag.CareTag--large 72.0x24.0 bg #f5f5f5 r 4px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `care-tag-default.png`, `care-tag-hover.png`, `care-tag-pressed.png`.

#### read-more

Read-more link. The bio expander on a provider card.

Page: listing. Selector: `button read more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 74 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px auto #4d9380 offset 0px | = |
| Font | Oceanic Grotesk 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #377a69 | #256959 | #4d9380 | #034135 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 6px | = | 82px x 32px, absolute, bg #000000 @ 0, radius 6px | = |
| Painted layers | button::before.MuiTypography-root.MuiTypography-inherit autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = | button.MuiTypography-root.MuiTypography-inherit 74.0x24.0 outline 3px auto #4d9380 offset 0px; button::before.MuiTypography-root.MuiTypography-inherit 82pxx32px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `read-more-default.png`, `read-more-hover.png`, `read-more-focus-visible.png`, `read-more-pressed.png`.

#### pagination

Pagination. The results pager (1 2 3 4 5 ... N).

Page: listing. Selector: `nav.MuiPagination-root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 332.23 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | a.MuiButtonBase-root.MuiPaginationItem-root: Oceanic Grotesk 16px/32px 400, #ffffff |
| Transition | none |
| Icon | 20 x 20, colour #c6c6c6 |
| Painted layers | a.MuiButtonBase-root.MuiPaginationItem-root 24.0x24.0 bg #1e1e1e r 16px |
| How | at rest |

Crops: `pagination-default.png`.

#### page-item

Page item. A page-number item in the pager.

Page: listing. Selector: `.MuiPaginationItem-root 2`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | #f5f5f5 | = | #e8e8e8 |
| Box shadow | none | = | #4d9380 0px 0px 0px 1px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 16px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Transition | color, background-color 0.25s, 0.25s cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.MuiButtonBase-root.MuiPaginationItem-root 24.0x24.0 bg #f5f5f5 r 16px | a.MuiButtonBase-root.Mui-focusVisible 24.0x24.0 r 16px shadow #4d9380 0px 0px 0px 1px | a.MuiButtonBase-root.MuiPaginationItem-root 24.0x24.0 bg #e8e8e8 r 16px |

Crops: `page-item-default.png`, `page-item-hover.png`, `page-item-focus-visible.png`, `page-item-pressed.png`.

#### learn-more

Learn-more link. A text-button link on the listing page.

Page: listing. Selector: `button.MuiButton-text Learn more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.11 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 16px/18px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #377a69 | #8ae718 | #4d9380 | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `learn-more-default.png`, `learn-more-hover.png`, `learn-more-focus-visible.png`, `learn-more-pressed.png`.

#### list-faq

FAQ question. A question row in the "FAQs for finding a babysitter" block; measured closed.

Page: listing. Selector: `listing FAQ row`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 746.66 x 72 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | #000000 @ 0.12 | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 18px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | h4.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 18px/24px 500, #1e1e1e | = | = | = |
| Transition | min-height, background-color 0.15s, 0.15s cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1e1e1e | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | div.MuiButtonBase-root.Mui-focusVisible 746.7x72.0 bg #000000 @ 0.12 | = |

Crops: `list-faq-default.png`, `list-faq-hover.png`, `list-faq-focus-visible.png`, `list-faq-pressed.png`.

### Login page

#### login-card

Login card. The sign-in card on /vis/auth/login (redirects to /vis/lcp/login, a legacy form — not the MUI layer): captured as a boundary surface, never filled or submitted.

Page: login. Selector: `login form card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 311 x 252 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Proxima Nova 14px/20px 400 |
| Letter spacing | normal |
| Colour | #172c42 |
| Text node | label: Proxima Nova 14px/17px 400, #172c42 |
| Transition | none |
| Painted layers | input.form-control 311.0x50.0 bg #ffffff border T:1px solid #b3bac1 / R:1px solid #b3bac1 / B:1px solid #b3bac1 / L:1px solid #b3bac1 r 10px; button.btn.btn-primary-2 311.0x50.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 50px |
| Ancestor paint | 1 up div.login-main bg #f6f3ee |
| How | at rest |

Crops: `login-card-default.png`.

#### login-email

Email field. The login email input (input.form-control); focused only, never typed into. The password step sits behind Continue, never reached.

Page: login. Selector: `input.form-control`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 311 x 50 | = |
| Padding | 6px 12px | = |
| Border | 1px solid #b3bac1 | 1px solid #083093 |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Proxima Nova 16px/22.8571px 400 | = |
| Letter spacing | normal | = |
| Colour | #172c42 | = |
| Transition | border-color, box-shadow 0.15s, 0.15s ease-in-out, ease-in-out delay 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #172c42, opacity 1 | = |
| Painted layers | input.form-control 311.0x50.0 bg #ffffff border T:1px solid #b3bac1 / R:1px solid #b3bac1 / B:1px solid #b3bac1 / L:1px solid #b3bac1 r 10px | input.form-control 311.0x50.0 bg #ffffff border T:1px solid #083093 / R:1px solid #083093 / B:1px solid #083093 / L:1px solid #083093 r 10px |
| How | at rest | clicked into the field |

Crops: `login-email-default.png`, `login-email-focused.png`.

#### login-button

Login button. The Continue action; measured, never pressed — the password step and the account sit behind it.

Page: login. Selector: `button.btn-primary-2 Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 311 x 50 | = | = | = |
| Padding | 7px 30px | = | = | = |
| Border | 1px solid #025747 | 1px solid #377a69 | = | 1px solid #377a69 |
| Radius | 50px | = | = | = |
| Background | #025747 | #377a69 | = | #377a69 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 20px/18px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #d0f5a3 | #e4ffb8 | = | #e4ffb8 |
| Transition | transform, background, -webkit-transform 0.3s, 0.3s, 0.3s ease-out, ease-out, ease-out delay 0s, 0s, 0s | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.btn-primary-2 311.0x50.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 50px | button.btn.btn-primary-2 311.0x50.0 bg #377a69 border T:1px solid #377a69 / R:1px solid #377a69 / B:1px solid #377a69 / L:1px solid #377a69 r 50px | button.btn.btn-primary-2 311.0x50.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 50px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | button.btn.btn-primary-2 311.0x50.0 bg #377a69 border T:1px solid #377a69 / R:1px solid #377a69 / B:1px solid #377a69 / L:1px solid #377a69 r 50px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `login-button-default.png`, `login-button-hover.png`, `login-button-focus-visible.png`, `login-button-pressed.png`.

#### passwordless-link

Passwordless link. The "Log in without a password" link; measured, never followed.

Page: login. Selector: `passwordless link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 311 x 50 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #005fcc offset -2px | = |
| Font | Proxima Nova 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #015ac8 | #014dac | #014dac | #014dac |
| Text node | span: Proxima Nova 18px/25.7143px 700, #025747 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.passwordless-login-btn.cta-login-btn 311.0x50.0 bg #ffffff border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 50px | div.passwordless-login-btn.cta-login-btn 311.0x50.0 bg #fafef5 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 50px | a 311.0x50.0 outline 5px auto #005fcc offset -2px; div.passwordless-login-btn.cta-login-btn 311.0x50.0 bg #ffffff border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 50px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `passwordless-link-default.png`, `passwordless-link-hover.png`, `passwordless-link-focus-visible.png`, `passwordless-link-pressed.png`.

### Join page

#### join-card

Join card. A chooser card on /app/vhp/get-started ("I need a caregiver" / "I want a care job"); captured as a boundary, never followed.

Page: join. Selector: `get-started .MuiPaper-root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 391 x 376 |
| Padding | 48px 24px |
| Border | none |
| Radius | 32px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | h2.MuiTypography-root.MuiTypography-h2: Oceanic Grotesk 24px/32px 500, #1e1e1e |
| Transition | box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 128 x 128, colour #1e1e1e |
| Painted layers | div.MuiPaper-root.MuiPaper-elevation 391.0x376.0 bg #ffffff r 32px; button.MuiButtonBase-root.MuiButton-root 170.0x40.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px |
| How | at rest |

Crops: `join-card-default.png`.

#### join-option

Join option. The Find-care/Find-jobs action inside a chooser card; measured, never pressed.

Page: join. Selector: `chooser card button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170 x 40 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | 1px solid #025747 | 1px solid #377a69 | none | 1px solid #034135 |
| Radius | 20px | = | = | = |
| Background | #025747 | #377a69 | = | #034135 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 16px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e4ffb8 | = | = | = |
| Transition | background 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.MuiButtonBase-root.MuiButton-root 170.0x40.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 20px | button.MuiButtonBase-root.MuiButton-root 170.0x40.0 bg #377a69 border T:1px solid #377a69 / R:1px solid #377a69 / B:1px solid #377a69 / L:1px solid #377a69 r 20px | button.MuiButtonBase-root.MuiButton-root 170.0x40.0 bg #025747 r 20px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | button.MuiButtonBase-root.MuiButton-root 170.0x40.0 bg #034135 border T:1px solid #034135 / R:1px solid #034135 / B:1px solid #034135 / L:1px solid #034135 r 20px |
| Ancestor paint | 1 up div.MuiPaper-root.MuiPaper-elevation bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `join-option-default.png`, `join-option-hover.png`, `join-option-focus-visible.png`, `join-option-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The "Flexible plans that fit your life" title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1183 x 36.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NaN Druid Sans 32px/36.8px 550 |
| Letter spacing | -0.96px |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### plan-card

Plan card. A Premium plan column (monthly/quarterly/annual); measured, never checked out.

Page: pricing. Selector: `premium plan column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 373 x 341 |
| Padding | 24px |
| Border | none |
| Radius | 32px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | h2.MuiTypography-root.MuiTypography-h2: Oceanic Grotesk 24px/32px 500, #1e1e1e |
| Transition | none |
| Icon | 24 x 24, colour #1e1e1e |
| Painted layers | div.MuiBox-root.mui-1k2cf0s 373.0x341.0 bg #ffffff r 32px; div::before.CareDivider.CareDivider--hairline 325pxx1px border T:1px solid #dddddd |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-price

Plan price. A plan price figure ($39.99 monthly / $25.99 quarterly / $13.99 annual).

Page: pricing. Selector: `plan price h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 109.73 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 32px/32px 500 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan Get-started action; measured, never pressed.

Page: pricing. Selector: `button.MuiButton-contained Get started`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171 x 56 | = | = | = |
| Padding | 14px 16px | = | = | = |
| Border | 1px solid #025747 | 1px solid #377a69 | none | 1px solid #034135 |
| Radius | 32px | = | = | = |
| Background | #025747 | #377a69 | = | #034135 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 20px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #e4ffb8 | = | = | = |
| Transition | background 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.MuiButtonBase-root.MuiButton-root 171.0x56.0 bg #025747 border T:1px solid #025747 / R:1px solid #025747 / B:1px solid #025747 / L:1px solid #025747 r 32px | button.MuiButtonBase-root.MuiButton-root 171.0x56.0 bg #377a69 border T:1px solid #377a69 / R:1px solid #377a69 / B:1px solid #377a69 / L:1px solid #377a69 r 32px | button.MuiButtonBase-root.MuiButton-root 171.0x56.0 bg #025747 r 32px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | button.MuiButtonBase-root.MuiButton-root 171.0x56.0 bg #034135 border T:1px solid #034135 / R:1px solid #034135 / B:1px solid #034135 / L:1px solid #034135 r 32px |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-alt

Plan alt. An outlined secondary action (Why join?); measured, never pressed.

Page: pricing. Selector: `button.MuiButton-outlined`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 183.48 x 56 | = | = | = |
| Padding | 14px 28px 14px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 28px | = | = | = |
| Background | #ffffff @ 0.9 | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 20px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #025747 | #034135 | #034135 | #034135 |
| Text node | h3.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 20px/24px 700, #025747 | h3.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 20px/24px 700, #034135 | h3.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 20px/24px 700, #034135 | h3.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 20px/24px 700, #034135 |
| Transition | background 0.3s ease-out | = | = | = |
| Transform | matrix(1, 0, 0, 1, -91.7422, -28) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 48 x 48, colour #034135 | = | = | = |
| Painted layers | button.MuiButtonBase-root.MuiButton-root 183.5x56.0 bg #ffffff @ 0.9 r 28px | button.MuiButtonBase-root.MuiButton-root 183.5x56.0 bg #f5f5f5 r 28px | button.MuiButtonBase-root.MuiButton-root 183.5x56.0 bg #ffffff @ 0.9 r 28px shadow #ffffff 0px 0px 0px 2px, #4d9380 0px 0px 0px 4px | button.MuiButtonBase-root.MuiButton-root 183.5x56.0 bg #f5f5f5 r 28px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-alt-default.png`, `plan-alt-hover.png`, `plan-alt-focus-visible.png`, `plan-alt-pressed.png`.

#### addon-card

Add-on card. An add-on product card (Feature your job post, Social Media Check, Hiring Helper).

Page: pricing. Selector: `.MuiPaper-contrast add-on`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 624 x 188 |
| Padding | 32px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | h2.MuiTypography-root.MuiTypography-h2: Oceanic Grotesk 24px/32px 500, #1e1e1e |
| Transition | box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 40 x 40, colour #1e1e1e |
| Painted layers | div.MuiPaper-root.MuiPaper-contrast 624.0x188.0 bg #ffffff r 24px; div.MuiBox-root.mui-1qpgnfw 64.0x64.0 bg #aaecf3 r 50% |
| How | at rest |

Crops: `addon-card-default.png`.

#### pricing-faq

Pricing FAQ. A billing FAQ row (How do I pay the caregiver once hired?); measured closed.

Page: pricing. Selector: `pricing FAQ accordion`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 737 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 18px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | p.MuiTypography-root.MuiTypography-body2: Oceanic Grotesk 18px/24px 700, #1e1e1e | = | = | = |
| Transition | margin 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Icon | 20 x 20, colour #000000 @ 0.54 | = | = | = |
| ::before | auto x 1px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | div.MuiButtonBase-root.Mui-focusVisible 737.0x24.0 bg #000000 @ 0.12 | = |

Crops: `pricing-faq-default.png`, `pricing-faq-hover.png`, `pricing-faq-focus-visible.png`, `pricing-faq-pressed.png`.

### Footer

#### footer

Footer. The inverse (dark) GlobalFooter: link columns, legal and the social row.

Page: home. Selector: `footer.GlobalFooter`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 886.8 |
| Padding | 40px 0px 8.8px 0px |
| Border | none |
| Radius | 0px |
| Background | #025747 |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | span.MuiTypography-root.MuiTypography-h4: Oceanic Grotesk 16px/20px 500, #d0f5a3 |
| Transition | none |
| Icon | 48 x 48, colour #d0f5a3 |
| Painted layers | footer.MuiBox-root.mui-qsc991 1440.0x886.8 bg #025747; a::before.MuiTypography-root.MuiTypography-link3 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a::before.MuiTypography-root.MuiTypography-link3 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a::before.MuiTypography-root.MuiTypography-link3 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a::before.MuiTypography-root.MuiTypography-link3 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a::before.MuiTypography-root.MuiTypography-link3 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56.58 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Oceanic Grotesk 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #d0f5a3 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 6px | = | 64.5781px x 28px, absolute, bg #000000 @ 0, radius 6px | = |
| Painted layers | a::before.MuiTypography-root.MuiTypography-link3 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = | a::before.MuiTypography-root.MuiTypography-link3 64.5781pxx28px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social link. A social link/icon in the footer.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Oceanic Grotesk 18px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 48 x 48, colour #d0f5a3 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.MuiBox-root.mui-3n26xl 48.0x56.0 outline 1px auto #005fcc offset 1px | = |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 12px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | a.MuiTypography-root.MuiTypography-body1: Oceanic Grotesk 18px/28px 400, #ffffff |
| Transition | background-color 0.3s ease-in-out |
| Icon | 24 x 24, colour #1e1e1e |
| Painted layers | button::before.MuiButtonBase-root.CareTouchMenuButton-root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; span.MuiBadge-badge.MuiBadge-dot 0.0x0.0 bg #d73218 r 4px; a::before.MuiTypography-root.MuiTypography-inherit autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a::before.MuiTypography-root.MuiTypography-body1 autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The "Open menu" touch toggle at phone width.

Page: mobile. Selector: `button[aria-label=Open menu]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 24 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Transition | none |
| Cursor | pointer |
| Icon | 24 x 24, colour #1e1e1e |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 6px |
| Painted layers | button::before.MuiButtonBase-root.CareTouchMenuButton-root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; span.MuiBadge-badge.MuiBadge-dot 0.0x0.0 bg #d73218 r 4px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The CareMobileDrawer panel opened by the header toggle at 390 (full-screen).

Page: mobile. Selector: `div.CareMobileDrawer--root`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.15 0px 4px 16px 0px |
| Outline | none |
| Font | Oceanic Grotesk 18px/28px 400 |
| Letter spacing | normal |
| Colour | #1e1e1e |
| Text node | div.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 18px/24px 500, #1e1e1e |
| Transition | transform, boxShadow 0.2s, 0.2s cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1) delay 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 24 x 24, colour #1e1e1e |
| Painted layers | div.CareMobileDrawer--root.CareMobileDrawer--open 390.0x844.0 bg #ffffff shadow #000000 @ 0.15 0px 4px 16px 0px; div.CareMobileDrawer--header.MuiBox-root 390.0x56.0 border B:1px solid #000000 @ 0; button::before.MuiButtonBase-root.CareFocusOutline autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; a::before.MuiTypography-root.MuiTypography-inherit autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; button::before.MuiButtonBase-root.MobileNavTraverseBtn--root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px; button::before.MuiButtonBase-root.MobileNavTraverseBtn--root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A link inside the opened mobile drawer.

Page: mobile. Selector: `CareMobileDrawer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 390 x 56 | = | = | = |
| Padding | 16px 16px 16px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 13.3333px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1e1e1e | = | = | = |
| Text node | div.MuiTypography-root.MuiTypography-h3: Oceanic Grotesk 18px/24px 500, #1e1e1e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #1e1e1e | = | = | = |
| ::before | auto x auto, absolute, bg #000000 @ 0, radius 6px | = | 390px x 56px, absolute, bg #000000 @ 0, radius 6px | = |
| Painted layers | button::before.MuiButtonBase-root.MobileNavTraverseBtn--root autoxauto border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = | button::before.MuiButtonBase-root.Mui-focusVisible 390pxx56px border T:2px solid #4d9380 / R:2px solid #4d9380 / B:2px solid #4d9380 / L:2px solid #4d9380 r 6px | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `largest display text in the hero fold at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 330 x 224 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NaN Druid Sans 48px/56px 550 |
| Letter spacing | -1px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

care.com serves its _next CSS chunks same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- childcare: `background-color 300ms ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `background 300ms ease-out`, `none`, `box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `margin 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `opacity 150ms cubic-bezier(0.4, 0, 0.2, 1), background-color 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `max-height 150ms cubic-bezier(0, 1, 0, 1)`, `max-height 300ms ease-in-out`, `min-height 150ms cubic-bezier(0.4, 0, 0.2, 1), background-color 150ms cubic-bezier(0.4, 0, 0.2, 1)`

- home: `background-color 300ms ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `background 300ms ease-out`, `none`, `background-color 5000s ease-in-out`, `opacity 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `margin 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `opacity 150ms cubic-bezier(0.4, 0, 0.2, 1), background-color 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `max-height 150ms cubic-bezier(0, 1, 0, 1)`

- join: `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 0.4s linear`, `background 300ms ease-out`, `0.1s`, `300ms ease-in`, `none`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`

- listing: `background-color 300ms ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `background 300ms ease-out`, `none`, `background-color 5000s ease-in-out`, `opacity 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `color 250ms cubic-bezier(0.4, 0, 0.2, 1), background-color 250ms cubic-bezier(0.4, 0, 0.2, 1)`, `box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)`, `background-color 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `margin 150ms cubic-bezier(0.4, 0, 0.2, 1)`

- login: `0.1s`, `300ms ease-in`, `none`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- pricing: `background-color 300ms ease-in-out`, `fill 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 200ms cubic-bezier(0.4, 0, 0.2, 1)`, `background 300ms ease-out`, `none`, `box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1)`, `transform 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `margin 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `opacity 150ms cubic-bezier(0.4, 0, 0.2, 1), background-color 150ms cubic-bezier(0.4, 0, 0.2, 1)`, `max-height 150ms cubic-bezier(0, 1, 0, 1)`, `max-height 300ms ease-in-out`, `min-height 150ms cubic-bezier(0.4, 0, 0.2, 1), background-color 150ms cubic-bezier(0.4, 0, 0.2, 1)`
