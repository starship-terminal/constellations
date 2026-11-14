# Component measurements

Computed styles read on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). expedia.com returns a 429 "Bot or Not?" wall to automation, so the DOM is a Wayback snapshot of the public home and hotel-search pages served locally, painted with Expedia's live travel-assets CDN CSS; the Search interaction group (calendar, room picker, destination panel) was measured on the same page hydrated with the site's own JavaScript. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and navigation

#### header

Header. The top bar over the whole page: the Expedia logo, the "Shop travel" menu, the USD currency control, "List your property", "Support", "Trips", the notifications bell and "Sign in".

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #0c0e1c @ 0.08 0px 2px 12px 0px |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div: Centra No2 14px/18px 500, #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 18 x 18, colour #191e3b |
| Painted layers | header.global-navigation-site-header 1440.0x72.0 bg #ffffff shadow #0c0e1c @ 0.08 0px 2px 12px 0px; section.global-navigation-row.primary 1440.0x72.0 bg #ffffff; div.uitk-menu-container.animation-disabled 0.0x0.0 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; hr.uitk-spacing.uitk-spacing-margin-block-four 0.0x0.0 border T:1px solid #dfe0e4 / R:1px inset #191e3b / L:1px inset #191e3b; div.uitk-menu-container.animation-disabled 0.0x0.0 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; a::before.uitk-button.uitk-button-medium 100%x100% bg #0e3672 r 40000px |
| Ancestor paint | 1 up div.page-header.with-shadow shadow #0c0e1c @ 0.12 0px 1px 0px 0px |
| How | at rest |

Crops: `header-default.png`.

#### header-logo

Logo link.

Page: home. Selector: `the first link in the header (the Expedia logo)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 138 x 44 |
| Padding | 8px 12px 8px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 16px/0px 400 |
| Letter spacing | normal |
| Colour | #1668e3 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `header-logo-default.png`.

#### header-shop-travel

Shop travel menu button. The nav menu trigger next to the logo: a tertiary uitk-button with a chevron. Pressed is forced; the menu is shot separately on the public page.

Page: home. Selector: `button[data-testid="header-menu-button"] (first)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128 x 36 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #ffffff @ 0 | = | #ffffff @ 0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Centra No2 14px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191e3b | #1668e3 | = | #0d4eaf |
| Text node | div: Centra No2 14px/18px 500, #191e3b | div: Centra No2 14px/18px 500, #1668e3 | = | div: Centra No2 14px/18px 500, #0d4eaf |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #191e3b | 18 x 18, colour #1668e3 | = | 18 x 18, colour #0d4eaf |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.uitk-button.uitk-button-medium 128.0x36.0 bg #ffffff @ 0 | button.uitk-button.uitk-button-medium 128.0x36.0 outline 1px auto #101010 offset 0px | button.uitk-button.uitk-button-medium 128.0x36.0 bg #ffffff @ 0 |

Crops: `header-shop-travel-default.png`, `header-shop-travel-hover.png`, `header-shop-travel-focus-visible.png`, `header-shop-travel-pressed.png`.

#### header-signin

Sign in button. The account menu trigger rightmost in the header. Pressed is forced: a real click only opens the guest card, measured separately.

Page: home. Selector: `header "Sign in" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78 x 36 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #ffffff @ 0 | = | #ffffff @ 0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Centra No2 14px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191e3b | #1668e3 | = | #0d4eaf |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.uitk-button.uitk-button-medium 78.0x36.0 bg #ffffff @ 0 | button.uitk-button.uitk-button-medium 78.0x36.0 outline 1px auto #101010 offset 0px | button.uitk-button.uitk-button-medium 78.0x36.0 bg #ffffff @ 0 |

Crops: `header-signin-default.png`, `header-signin-hover.png`, `header-signin-focus-visible.png`, `header-signin-pressed.png`.

#### header-currency

Currency button. The locale/currency control in the header ("USD" + flag). Hovered and focused only.

Page: home. Selector: `header control reading USD`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 92 x 36 | = | - |
| Padding | 0px | = | - |
| Border | none | = | - |
| Radius | 0px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Centra No2 16px/normal 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #191e3b | = | - |
| Text node | span.uitk-spacing.uitk-spacing-margin-inline-one: Centra No2 14px/18px 500, #191e3b | span.uitk-spacing.uitk-spacing-margin-inline-one: Centra No2 14px/18px 500, #1668e3 | - |
| Transition | none | = | - |
| Cursor | default | = | - |
| How | at rest | mouse hover | - |
| Painted layers | - | button.uitk-button.uitk-button-medium 92.0x36.0 bg #ffffff @ 0 | = |
| Error | - | = | keyboard focus did not reach the element |

Crops: `header-currency-default.png`, `header-currency-hover.png`.

#### header-link

Header link. A plain header link ("Support"; "Trips" and "List your property" share the style): tertiary as-link buttons.

Page: home. Selector: `a[data-stid="support-cs-link"]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 88 x 36 | = | = |
| Padding | 4px 16px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | #ffffff @ 0 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 1px |
| Font | Centra No2 14px/18px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #191e3b | #1668e3 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | a.uitk-button.uitk-button-medium 88.0x36.0 bg #ffffff @ 0 | a.uitk-button.uitk-button-medium 88.0x36.0 outline 1px auto #101010 offset 1px |

Crops: `header-link-default.png`, `header-link-hover.png`, `header-link-focus-visible.png`.

#### signin-card

Sign-in card. The 375px guest menu the Sign in button opens: "Unlock instant savings with Member Prices", the primary Sign in button, "Learn more about One Key" and a Feedback link. Opened through the SSR checkbox mechanism; nothing was submitted.

Page: home. Selector: `.uitk-menu-container of the Sign in uitk-menu`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 375 x 279 |
| Padding | 12px 0px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #0c0e1c @ 0.08 0px 2px 12px 0px |
| Outline | none |
| Font | Centra No2 16px/20px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.uitk-type-center: Centra No2 20px/24px 500, #191e3b |
| Transition | none |
| Cursor | default |
| Painted layers | div.uitk-menu-container.animation-disabled 375.0x279.0 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; a::before.uitk-button.uitk-button-medium 327pxx36px bg #0e3672 r 40000px; a::after.uitk-button.uitk-button-medium 327pxx36px bg #1668e3 r 40000px; a.uitk-button.uitk-button-medium 375.0x36.0 bg #ffffff @ 0 r 40000px; hr.uitk-spacing.uitk-spacing-margin-block-four 375.0x1.0 border T:1px solid #dfe0e4 / R:1px inset #191e3b / L:1px inset #191e3b |
| How | at rest |

Crops: `signin-card-open.png`.

#### signin-card-button

Sign-in card button. The blue primary "Sign in" button inside the guest card. Hovered only, never pressed.

Page: home. Selector: `primary button inside the sign-in card`. States: open, hover.

| Property | open | hover |
|---|---|---|
| Size (w x h) | 327 x 36 | = |
| Padding | 4px 16px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 40000px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Centra No2 16px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::before | 327px x 36px, absolute, bg #0e3672, radius 40000px | = |
| ::after | 327px x 36px, absolute, bg #1668e3, radius 40000px | = |
| Painted layers | a::before.uitk-button.uitk-button-medium 327pxx36px bg #0e3672 r 40000px; a::after.uitk-button.uitk-button-medium 327pxx36px bg #1668e3 r 40000px | = |
| How | at rest | mouse hover |

Crops: `signin-card-button-open.png`, `signin-card-button-hover.png`.

### Search form

#### search-shell

Search form shell. The white rounded card under the hero holding the product tabs and the three search fields with the Search button.

Page: home. Selector: `[data-testid="multi-product-search-form"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 252 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | span.egds-tab-custom-text: Centra No2 14px/18px 500, #1668e3 |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #191e3b |
| Painted layers | div.uitk-card.uitk-card-roundcorner-all 1200.0x252.0 bg #ffffff r 16px; div::before.uitk-card.uitk-card-roundcorner-all 1200pxx252px border T:1px solid #dfe0e4 / R:1px solid #dfe0e4 / B:1px solid #dfe0e4 / L:1px solid #dfe0e4 r 16px; ul.egds-tabs-custom.egds-tabs-custom-natural 1200.0x110.0 bg #ffffff r 16px 16px 0px 0px shadow #dfe0e4 0px 1px 0px 0px; a.egds-tab-custom-anchor.egds-tab-custom-anchor-selected 96.0x110.0 shadow #1668e3 0px -2px 0px 0px inset; li.egds-tab-custom-highlighter 0.0x2.0 bg #1668e3; input.uitk-field-input.empty-placeholder 344.3x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px |
| How | at rest |

Crops: `search-shell-default.png`.

#### search-tabs

Product tabs. The tab rail atop the form: Stays, Flights, Cars, Packages, Things to do, Cruises, each an icon over a label.

Page: home. Selector: `[role=tablist]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 110 |
| Padding | 0px |
| Gap | normal 0px |
| Border | none |
| Radius | 16px 16px 0px 0px |
| Background | #ffffff |
| Box shadow | #dfe0e4 0px 1px 0px 0px |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | span.egds-tab-custom-text: Centra No2 14px/18px 500, #1668e3 |
| Transition | none |
| Cursor | default |
| ::before | 284px x 110px, static, bg #000000 @ 0, radius 0px |
| ::after | 284px x 110px, static, bg #000000 @ 0, radius 0px |
| Painted layers | ul.egds-tabs-custom.egds-tabs-custom-natural 1200.0x110.0 bg #ffffff r 16px 16px 0px 0px shadow #dfe0e4 0px 1px 0px 0px; a.egds-tab-custom-anchor.egds-tab-custom-anchor-selected 96.0x110.0 shadow #1668e3 0px -2px 0px 0px inset; li.egds-tab-custom-highlighter 0.0x2.0 bg #1668e3 |
| How | at rest |

Crops: `search-tabs-default.png`.

#### tab-active

Product tab (active). The current product tab (Stays): label and icon in the primary blue with a 2px underline.

Page: home. Selector: `[role=tab][aria-selected=true]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96 x 110 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #1668e3 0px -2px 0px 0px inset | = | = | none |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Centra No2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1668e3 | = | = | = |
| Text node | span.egds-tab-custom-text: Centra No2 14px/18px 500, #1668e3 | = | = | = |
| Transition | none | = | = | box-shadow 0.275s ease |
| Cursor | pointer | = | = | = |
| Painted layers | a.egds-tab-custom-anchor.egds-tab-custom-anchor-selected 96.0x110.0 shadow #1668e3 0px -2px 0px 0px inset | = | a.egds-tab-custom-anchor.egds-tab-custom-anchor-selected 96.0x110.0 shadow #1668e3 0px -2px 0px 0px inset outline 1px auto #101010 offset 1px | - |
| Ancestor paint | 2 up ul.egds-tabs-custom.egds-tabs-custom-natural bg #ffffff shadow #dfe0e4 0px 1px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tab-active-default.png`, `tab-active-hover.png`, `tab-active-focus-visible.png`, `tab-active-pressed.png`.

#### tab

Product tab. A resting product tab (Flights). Pressed is forced: a real click switches the form, shot separately on the hydrated page.

Page: home. Selector: `[role=tab] "Flights"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96 x 110 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | #191e3b 0px -4px 0px 0px inset |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Centra No2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1668e3 | = | = | #191e3b |
| Text node | span.egds-tab-custom-text: Centra No2 14px/18px 500, #191e3b | = | = | = |
| Transition | none | = | = | box-shadow 0.275s ease |
| Cursor | pointer | = | = | = |
| Ancestor paint | 2 up ul.egds-tabs-custom.egds-tabs-custom-natural bg #ffffff shadow #dfe0e4 0px 1px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.egds-tab-custom-anchor.egds-tab-custom-anchor-graphic 96.0x110.0 outline 1px auto #101010 offset 1px | a.egds-tab-custom-anchor.egds-tab-custom-anchor-graphic 96.0x110.0 shadow #191e3b 0px -4px 0px 0px inset |

Crops: `tab-default.png`, `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`.

#### field-destination

Destination field. The "Where to?" field: a uitk-field box with floated label, pin icon and empty input; once hydrated its trigger button opens the destination panel. Pressed is forced.

Page: home. Selector: `[data-stid="search-location"] .uitk-field`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344.33 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Centra No2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191e3b | = | = | = |
| Text node | label.uitk-field-label: Centra No2 16px/20px 400, #191e3b | = | label.uitk-field-label: Centra No2 12px/16px 400, #191e3b | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #191e3b | = | = | = |
| Painted layers | input.uitk-field-input.empty-placeholder 344.3x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px | = | input.uitk-field-input.empty-placeholder 344.3x48.0 bg #ffffff border T:1px solid #1668e3 / R:1px solid #1668e3 / B:1px solid #1668e3 / L:1px solid #1668e3 r 8px shadow #1668e3 0px 0px 0px 1px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `field-destination-default.png`, `field-destination-hover.png`, `field-destination-focus-visible.png`, `field-destination-pressed.png`.

#### field-dates

Dates field. The "Dates" field with the range value (Fri, Feb 13 - Tue, Feb 17) and a calendar icon. Pressed is forced: a click opens the calendar.

Page: home. Selector: `.uitk-field containing "Dates"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344.33 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Centra No2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191e3b | = | = | = |
| Text node | label.uitk-field-label: Centra No2 12px/16px 400, #191e3b | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #191e3b | = | = | = |
| Painted layers | input.uitk-field-input 344.3x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px | = | input.uitk-field-input 344.3x48.0 bg #ffffff border T:1px solid #1668e3 / R:1px solid #1668e3 / B:1px solid #1668e3 / L:1px solid #1668e3 r 8px shadow #1668e3 0px 0px 0px 1px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `field-dates-default.png`, `field-dates-hover.png`, `field-dates-focus-visible.png`, `field-dates-pressed.png`.

#### field-travelers

Travelers field. The "Travelers" field ("2 travelers, 1 room") with a person icon. Pressed is forced: a click opens the room picker.

Page: home. Selector: `.uitk-field containing "Travelers"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 344.34 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Centra No2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191e3b | = | = | = |
| Text node | label.uitk-field-label: Centra No2 12px/16px 400, #191e3b | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #191e3b | = | = | = |
| Painted layers | input.uitk-field-input 344.3x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px | = | input.uitk-field-input 344.3x48.0 bg #ffffff border T:1px solid #1668e3 / R:1px solid #1668e3 / B:1px solid #1668e3 / L:1px solid #1668e3 r 8px shadow #1668e3 0px 0px 0px 1px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `field-travelers-default.png`, `field-travelers-hover.png`, `field-travelers-focus-visible.png`, `field-travelers-pressed.png`.

#### search-submit

Search button. The primary Search button at the form's right end (uitk-button-primary-large). Pressed is forced: a real press would run a search.

Page: home. Selector: `the Search button in the search form`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83 x 48 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 40000px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #101010 offset 2px | = |
| Font | Centra No2 16px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 83px x 48px, absolute, bg #0e3672, radius 40000px | = | = | = |
| ::after | 83px x 48px, absolute, bg #1668e3, radius 40000px | = | = | = |
| Painted layers | button::before.uitk-button.uitk-button-large 83pxx48px bg #0e3672 r 40000px; button::after.uitk-button.uitk-button-large 83pxx48px bg #1668e3 r 40000px | = | button.uitk-button.uitk-button-large 83.0x48.0 r 40000px outline 5px auto #101010 offset 2px; button::before.uitk-button.uitk-button-large 83pxx48px bg #0e3672 r 40000px; button::after.uitk-button.uitk-button-large 83pxx48px bg #1668e3 r 40000px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-submit-default.png`, `search-submit-hover.png`, `search-submit-focus-visible.png`, `search-submit-pressed.png`.

#### bundle-checkbox

Bundle & Save checkbox. The "Add a flight to Bundle & Save*" checkbox under the fields: an uitk-checkbox box plus label.

Page: home. Selector: `the Bundle & Save checkbox`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1152 x 34 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | p.uitk-checkbox-label-content: Centra No2 14px/18px 400, #191e3b |
| Transition | none |
| Cursor | default |
| Painted layers | input.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18.0x18.0 bg #ffffff; span.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18.0x18.0 bg #ffffff border T:2px solid #818494 / R:2px solid #818494 / B:2px solid #818494 / L:2px solid #818494 r 4px; span::before.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18pxx18px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest |

Crops: `bundle-checkbox-default.png`.

#### tertiary-button

Tertiary button. The "See all deals" button by the deals heading: outlined tertiary uitk-button. Pressed is forced, never followed.

Page: home. Selector: `"See all deals" uitk-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128 x 36 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #818494 | = | = | = |
| Radius | 40000px | = | = | = |
| Background | #ffffff | #ecf4fd | = | #ecf4fd |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Centra No2 16px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1668e3 | #0d4eaf | = | #0d4eaf |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.uitk-button.uitk-button-medium 128.0x36.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px | a.uitk-button.uitk-button-medium 128.0x36.0 bg #ecf4fd border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px | a.uitk-button.uitk-button-medium 128.0x36.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px outline 1px auto #101010 offset 1px | a.uitk-button.uitk-button-medium 128.0x36.0 bg #ecf4fd border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tertiary-button-default.png`, `tertiary-button-hover.png`, `tertiary-button-focus-visible.png`, `tertiary-button-pressed.png`.

### Home content

#### hero-title

Hero title. "The one place you go to go places" over the hero photo: the display type style in Reckless XPD, inverse colour.

Page: home. Selector: `[data-testid="hero-title-campaign"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 659 x 49 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Reckless XPD 44px/40px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `hero-title-default.png`.

#### marketing-band

Marketing band. The section re-themed data-theme-light="marketing-3": the pale-blue palette applied to the same components (the promo strip under the search form).

Page: home. Selector: `section[data-theme-light="marketing-3"] (first child)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.uitk-type-400: Centra No2 16px/20px 500, #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #191e3b |
| Painted layers | div.uitk-card.uitk-card-roundcorner-all 1200.0x72.0 bg #b7cddc r 16px |
| How | at rest |

Crops: `marketing-band-default.png`.

#### deal-card

Deal card. One card in the deals carousels: a uitk-card with rounded corners, the gallery photo, a heart save button, the property name and the price.

Page: home. Selector: `a deals .uitk-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 270 x 409.06 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Centra No2 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #191e3b | = |
| Text node | h3.uitk-heading.uitk-heading-6: Centra No2 16px/20px 500, #191e3b | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 18 x 18, colour #191e3b | = |
| ::before | 270px x 409.062px, absolute, bg #000000 @ 0, radius 16px | = |
| Painted layers | div.uitk-card.uitk-card-roundcorner-all 270.0x409.1 bg #ffffff r 16px; div::before.uitk-card.uitk-card-roundcorner-all 270pxx409.062px border T:1px solid #dfe0e4 / R:1px solid #dfe0e4 / B:1px solid #dfe0e4 / L:1px solid #dfe0e4 r 16px; div.uitk-image-placeholder.uitk-image-placeholder-image 270.0x151.9 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 270.0x151.9 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 270.0x151.9 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 0.0x0.0 bg #c8dff9 image url(data:…) | = |
| How | at rest | mouse hover |

Crops: `deal-card-default.png`, `deal-card-hover.png`.

#### card-heart

Save (heart) button. The heart save control over a card photo: a round white button, pressed state forced so nothing is saved.

Page: home. Selector: `[data-stid="outlined-save-button"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Centra No2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191e3b | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #000000, fill #000000 @ 0 | = | = | = |
| Painted layers | button.favorite-button.favorite-button-button-no-label 32.0x32.0 bg #ffffff r 40000px | = | button.favorite-button.favorite-button-button-no-label 32.0x32.0 bg #ffffff r 40000px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-heart-default.png`, `card-heart-hover.png`, `card-heart-focus-visible.png`, `card-heart-pressed.png`.

#### footer-link

Footer link. A link in the page footer.

Page: home. Selector: `footer a (first)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 150 x 21 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Centra No2 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #1668e3 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`.

### Menus and dialogs

#### calendar-dialog

Calendar dialog. The date picker the Dates field opens: Calendar/Flexible dates tabs, the range line, two months, weekday headings, the selected range endpoints as filled blue days, the ±day flexibility chips and the Done button. Opened by clicking the field trigger; Escape closed it, nothing was searched.

Page: home-i. Selector: `[role=dialog] containing "Calendar"`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 652 x 558.69 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #0c0e1c @ 0.08 0px 2px 12px 0px |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | span.uitk-tab-text: Centra No2 14px/18px 500, #1668e3 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Icon | 18 x 18, colour #191e3b |
| Painted layers | section.uitk-popover-sheet.uitk-date-selector-popover 652.0x558.7 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; ul.uitk-tabs.uitk-tabs-equal-width 652.0x44.0 bg #eff3f7 shadow #dfe0e4 0px 1px 0px 0px; li.uitk-tab-highlighter 326.0x2.0 bg #1668e3; div.uitk-toolbar.uitk-toolbar-has-placeholder 652.0x56.0 bg #ffffff shadow #0c0e1c @ 0 0px 0px 0px 0px; span.uitk-date-display-value 148.0x48.0 shadow #1668e3 0px -2px 0px 0px inset; button.uitk-button.uitk-button-medium 32.0x32.0 bg #ffffff r 40000px shadow #0c0e1c @ 0.08 0px 2px 12px 0px |
| How | at rest |

Crops: `calendar-dialog-open.png`.

#### calendar-day-selected

Calendar day (selected). A range endpoint in the calendar: the filled primary circle.

Page: home-i. Selector: `the selected day button in the calendar`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 40.84 x 40.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-date-number.uitk-date-number-muted: Centra No2 14px/18px 700, #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | div.uitk-calendar-day-selection.uitk-calendar-day-selection-range-start 40.8x40.9 image linear-gradient(to right, #000000 @ 0 50%, #ecf4fd 50%); div.uitk-calendar-day-selection-edge-start 40.8x40.9 bg #1668e3 r 40000px |
| How | at rest |

Crops: `calendar-day-selected-open.png`.

#### calendar-chip

Flexibility chip. The "Exact dates" / "± N days" chips under the calendar: outlined pills, the active one filled.

Page: home-i. Selector: `a ±days chip in the calendar dialog`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 69 x 32 |
| Padding | 0px 12px |
| Border | none |
| Radius | 40000px |
| Background | #ffffff |
| Box shadow | #818494 0px 0px 0px 1px inset |
| Outline | none |
| Font | Centra No2 12px/16px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | span.single-select-pill-text: Centra No2 12px/16px 400, #191e3b |
| Transition | none |
| Cursor | pointer |
| Painted layers | label.single-select-pill-content 69.0x32.0 bg #ffffff r 40000px shadow #818494 0px 0px 0px 1px inset |
| How | at rest |

Crops: `calendar-chip-open.png`.

#### dialog-done

Dialog Done button. The primary Done button at the foot of the calendar. Hovered only, never pressed.

Page: home-i. Selector: `the Done button in the calendar dialog`. States: open, hover.

| Property | open | hover |
|---|---|---|
| Size (w x h) | 72 x 36 | = |
| Padding | 4px 16px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 40000px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Centra No2 16px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| ::before | 72px x 36px, absolute, bg #0e3672, radius 40000px | = |
| ::after | 72px x 36px, absolute, bg #1668e3, radius 40000px | = |
| Painted layers | button::before.uitk-button.uitk-button-medium 72pxx36px bg #0e3672 r 40000px; button::after.uitk-button.uitk-button-medium 72pxx36px bg #1668e3 r 40000px | = |
| Ancestor paint | 2 up footer.uitk-spacing.uitk-sheet-footer bg #ffffff shadow #0c0e1c @ 0.08 0px 2px 12px 0px; 3 up section.uitk-popover-sheet.uitk-date-selector-popover bg #ffffff shadow #0c0e1c @ 0.08 0px 2px 12px 0px | = |
| How | at rest | mouse hover |

Crops: `dialog-done-open.png`, `dialog-done-hover.png`.

#### travelers-menu

Travelers menu. The room picker the Travelers field opens: "Room 1", the Adults and Children steppers (−/+), "Add another room", the group-booking line and Done. Opened by clicking the field trigger; Escape closed it.

Page: home-i. Selector: `the travelers panel ([role=dialog] or uitk-menu)`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 375 x 318 |
| Padding | 12px 0px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #0c0e1c @ 0.08 0px 2px 12px 0px |
| Outline | none |
| Font | Centra No2 16px/20px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | h2.uitk-heading.uitk-heading-7: Centra No2 14px/18px 500, #191e3b |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Icon | 24 x 16, colour #000000, fill #191e3b |
| Painted layers | div.uitk-menu-container.uitk-menu-open 375.0x318.0 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; span.uitk-step-input-button 32.0x32.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px; span.uitk-step-input-button 32.0x32.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px; span.uitk-step-input-button 32.0x32.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px; span.uitk-step-input-button 32.0x32.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px; button.uitk-button.uitk-button-medium 155.0x36.0 bg #ffffff @ 0 r 40000px |
| How | at rest |

Crops: `travelers-menu-open.png`.

#### whereto-panel

Destination panel. The panel the Where to? field opens: the prompt, the magnifier and the "Search by destination, accommodations, or landmark" input. Opened by clicking the field trigger.

Page: home-i. Selector: `the destination panel`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 376 x 510 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #0c0e1c @ 0.08 0px 2px 12px 0px |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.uitk-type-300: Centra No2 14px/18px 400, #191e3b |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | default |
| Icon | 48 x 48, colour #191e3b |
| Painted layers | section.uitk-popover-sheet.uitk-sheet 376.0x510.0 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; input.uitk-field-input.typeahead-custom-text-input 376.0x72.0 border B:1px solid #dfe0e4 |
| How | at rest |

Crops: `whereto-panel-open.png`.

#### whereto-input

Destination input. The free-text destination field inside the panel; text was typed and deleted, nothing searched.

Page: home-i. Selector: `the input inside the destination panel`. States: filled.

| Property | filled |
|---|---|
| Size (w x h) | 376 x 72 |
| Padding | 16px 48px 0px 24px |
| Border | T: none; R: none; B: 1px solid #dfe0e4; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 28px/32px 700 |
| Letter spacing | normal |
| Colour | #191e3b |
| Transition | none |
| Cursor | text |
| Placeholder | #676a7d, opacity 1 |
| Painted layers | input.uitk-field-input.has-typeahead-custom-text-input-cta 376.0x72.0 border B:1px solid #dfe0e4 |
| How | typed "Las Vegas", then deleted; nothing sent |

Crops: `whereto-input-filled.png`.

### Hotel results

#### search-form-sticky

Sticky search form. The compact search bar pinned under the header on the results page: the same three fields plus the round search button.

Page: search. Selector: `form#lodging_search_form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1016 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | label.uitk-field-label: Centra No2 12px/16px 400, #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #191e3b |
| Painted layers | input.uitk-field-input 310.7x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px; input.uitk-field-input 310.7x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px; input.uitk-field-input 310.7x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px; div.uitk-menu-container.animation-disabled 0.0x0.0 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; span.uitk-step-input-button 0.0x0.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px; span.uitk-step-input-button 0.0x0.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 40000px |
| How | at rest |

Crops: `search-form-sticky-default.png`.

#### header-signin-search

Sign in button (results).

Page: search. Selector: `header "Sign in" button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 78 x 36 | = | = |
| Padding | 4px 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | #ffffff @ 0 | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | Centra No2 14px/18px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #191e3b | #1668e3 | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab |
| Painted layers | - | button.uitk-button.uitk-button-medium 78.0x36.0 bg #ffffff @ 0 | button.uitk-button.uitk-button-medium 78.0x36.0 outline 1px auto #101010 offset 0px |

Crops: `header-signin-search-default.png`, `header-signin-search-hover.png`, `header-signin-search-focus-visible.png`.

#### stay-type-tabs

Stay type tabs. The segmented "All stays / Hotels / Homes" control above the results.

Page: search. Selector: `the All stays segmented control`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 756 x 44 |
| Padding | 4px |
| Border | none |
| Radius | 40000px |
| Background | #eff3f7 |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.truncate: Centra No2 14px/18px 500, #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 18 x 18, colour #191e3b |
| Painted layers | div.lodging-segmented-controls.with-v2-styling 756.0x44.0 bg #eff3f7 r 40000px; label.lodging-segmented-control-item.lodging-segmented-control-item--selected 246.7x36.0 bg #ffffff border T:1px solid #dfe0e4 / R:1px solid #dfe0e4 / B:1px solid #dfe0e4 / L:1px solid #dfe0e4 r 40000px; label.lodging-segmented-control-item 246.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40000px; label.lodging-segmented-control-item 246.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 40000px; div.lodging-segmented-controls__selection-background 756.0x0.0 bg #ffffff r 40000px |
| How | at rest |

Crops: `stay-type-tabs-default.png`.

#### sort-control

Sort control. The "Sort by recommended for you" uitk-pill over the results list. Hovered and focused only, never opened.

Page: search. Selector: `#sort-filter-sort-pill-sort`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 222 x 32 | = | = |
| Padding | 0px 12px | = | = |
| Border | none | = | = |
| Radius | 40000px | = | = |
| Background | #ffffff | #ecf4fd | = |
| Box shadow | #818494 0px 0px 0px 1px inset | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | Centra No2 12px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #191e3b | = | = |
| Text node | span.uitk-pill-text: Centra No2 12px/16px 400, #191e3b | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 16, colour #191e3b | = | = |
| Painted layers | button.uitk-pill.uitk-pill-content 222.0x32.0 bg #ffffff r 40000px shadow #818494 0px 0px 0px 1px inset | button.uitk-pill.uitk-pill-content 222.0x32.0 bg #ecf4fd r 40000px shadow #818494 0px 0px 0px 1px inset | button.uitk-pill.uitk-pill-content 222.0x32.0 bg #ffffff r 40000px shadow #818494 0px 0px 0px 1px inset outline 1px auto #101010 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `sort-control-default.png`, `sort-control-hover.png`, `sort-control-focus-visible.png`.

#### results-summary

Results count. The "N properties" line over the results list.

Page: search. Selector: `the "N properties" text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 81 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.uitk-type-start: Centra No2 12px/16px 400, #191e3b |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `results-summary-default.png`.

#### property-card

Property card. One result card (uitk-card): the 21:9 photo gallery with carousel arrows and the heart, VIP badge, name, amenity icons, refund line, rating pill, nightly and total prices, and the "Sign in for extra savings" pill.

Page: search. Selector: `[data-stid="lodging-card-responsive"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 756 x 232 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Centra No2 14px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #191e3b | = |
| Text node | span.uitk-badge-text: Centra No2 12px/18px 500, #ffffff | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 24 x 24, colour #ffffff | = |
| ::before | 756px x 232px, absolute, bg #000000 @ 0, radius 16px | = |
| Painted layers | div.uitk-card.uitk-card-roundcorner-all 756.0x232.0 bg #ffffff r 16px; div::before.uitk-card.uitk-card-roundcorner-all 756pxx232px border T:1px solid #dfe0e4 / R:1px solid #dfe0e4 / B:1px solid #dfe0e4 / L:1px solid #dfe0e4 r 16px; div.uitk-image-placeholder.uitk-image-placeholder-image 252.0x232.0 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 252.0x232.0 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 252.0x232.0 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 0.0x0.0 bg #c8dff9 image url(data:…) | = |
| How | at rest | mouse hover |

Crops: `property-card-default.png`, `property-card-hover.png`.

#### card-gallery

Card gallery. The 21:9 image carousel in a result card with prev/next circle buttons.

Page: search. Selector: `.uitk-gallery-carousel in a property card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 252 x 232 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.uitk-image-placeholder.uitk-image-placeholder-image 252.0x232.0 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 252.0x232.0 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 252.0x232.0 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 0.0x0.0 bg #c8dff9 image url(data:…); button.uitk-button.uitk-button-medium 32.0x32.0 r 40000px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; button::before.uitk-button.uitk-button-medium 32pxx32px bg #191e3b r 40000px |
| How | at rest |

Crops: `card-gallery-default.png`.

#### price-block

Price block. The right-aligned price area of a result card: the struck list price, the nightly rate in the headline size, and the total with taxes in muted text.

Page: search. Selector: `the price area of a property card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 183 x 62 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.uitk-type-end: Centra No2 16px/20px 400, #191e3b |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `price-block-default.png`.

#### rating-pill

Rating pill. The guest rating on a card: the score chip (9.4) in positive green beside the word and the review count.

Page: search. Selector: `the rating area of a property card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 244.19 x 34 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | span.uitk-text.uitk-type-300: Centra No2 14px/18px 500, #191e3b |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `rating-pill-default.png`.

#### savings-pill

"Sign in for extra savings" pill. The filled primary-blue pill button with white text on each card pointing signed-out guests at member prices (the fill paints on its ::after layer). Hovered and focused only, never followed.

Page: search. Selector: `the "Sign in for extra savings" button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 183 x 32 | = | = |
| Padding | 4px 12px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 40000px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 5px auto #101010 offset 2px |
| Font | Centra No2 12px/16px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #ffffff | = | = |
| ::before | 183px x 32px, absolute, bg #0e3672, radius 40000px | = | = |
| ::after | 183px x 32px, absolute, bg #1668e3, radius 40000px | = | = |
| Painted layers | a::before.uitk-button.uitk-button-small 183pxx32px bg #0e3672 r 40000px; a::after.uitk-button.uitk-button-small 183pxx32px bg #1668e3 r 40000px | = | a.uitk-button.uitk-button-small 183.0x32.0 r 40000px outline 5px auto #101010 offset 2px; a::before.uitk-button.uitk-button-small 183pxx32px bg #0e3672 r 40000px; a::after.uitk-button.uitk-button-small 183pxx32px bg #1668e3 r 40000px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `savings-pill-default.png`, `savings-pill-hover.png`, `savings-pill-focus-visible.png`.

#### vip-badge

VIP Access badge. The dark "VIP Access" chip pinned over the card photo.

Page: search. Selector: `the VIP Access badge on a property card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 77 x 24 |
| Padding | 0px 8px |
| Gap | 4px |
| Border | none |
| Radius | 4px |
| Background | #191e3b |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 12px/18px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.uitk-badge-text: Centra No2 12px/18px 500, #ffffff |
| Transition | none |
| Cursor | default |
| Painted layers | span.uitk-badge.uitk-badge-large 77.0x24.0 bg #191e3b r 4px |
| How | at rest |

Crops: `vip-badge-default.png`.

#### card-heart-search

Save (heart) button. The heart over the card photo. Pressed is forced; nothing was saved.

Page: search. Selector: `[data-stid="outlined-save-button"] on a property card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Centra No2 14px/18px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191e3b | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #000000, fill #000000 @ 0 | = | = | = |
| Painted layers | button.favorite-button.favorite-button-button-no-label 32.0x32.0 bg #ffffff r 40000px | = | button.favorite-button.favorite-button-button-no-label 32.0x32.0 bg #ffffff r 40000px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-heart-search-default.png`, `card-heart-search-hover.png`, `card-heart-search-focus-visible.png`, `card-heart-search-pressed.png`.

#### carousel-nav

Carousel arrow. A round prev/next button in the card gallery (uitk-button-paging). Hovered and focused only.

Page: search. Selector: `an uitk-button-paging in a property card`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 40000px | = | = |
| Background | transparent | = | = |
| Box shadow | #0c0e1c @ 0.08 0px 2px 12px 0px | = | = |
| Outline | none | = | 1px auto #101010 offset 0px |
| Font | Centra No2 16px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | opacity 0.2s ease | = | = |
| Cursor | pointer | = | = |
| Icon | 24 x 24, colour #ffffff | = | = |
| ::before | 32px x 32px, absolute, bg #191e3b, radius 40000px | = | = |
| Painted layers | button.uitk-button.uitk-button-medium 32.0x32.0 r 40000px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; button::before.uitk-button.uitk-button-medium 32pxx32px bg #191e3b r 40000px | = | button.uitk-button.uitk-button-medium 32.0x32.0 r 40000px shadow #0c0e1c @ 0.08 0px 2px 12px 0px outline 1px auto #101010 offset 0px; button::before.uitk-button.uitk-button-medium 32pxx32px bg #191e3b r 40000px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `carousel-nav-default.png`, `carousel-nav-hover.png`, `carousel-nav-focus-visible.png`.

#### amenity-item

Amenity line. One amenity row on a card: a small icon and a muted label.

Page: search. Selector: `an amenity line in a property card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 91 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.uitk-type-200: Centra No2 12px/16px 400, #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 18 x 18, colour #191e3b |
| How | at rest |

Crops: `amenity-item-default.png`.

#### filters

Filter column. The left filter rail: "Search by property name", "Filter by" groups (Property class checkboxes, Guest rating radios), See more links.

Page: search. Selector: `the Filter by sidebar form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 236 x 4108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | span.uitk-switch-label-content: Centra No2 14px/18px 400, #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 16 x 16, colour #191e3b |
| Painted layers | div.uitk-layout-flex.uitk-card 236.0x78.0 bg #ffffff r 16px; div::before.uitk-layout-flex.uitk-card 236pxx78px border T:1px solid #dfe0e4 / R:1px solid #dfe0e4 / B:1px solid #dfe0e4 / L:1px solid #dfe0e4 r 16px; div.uitk-switch-control 48.0x24.0 bg #676a7d border T:2px solid #676a7d / R:2px solid #676a7d / B:2px solid #676a7d / L:2px solid #676a7d r 12px; div::before.uitk-switch-control 20pxx20px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 50%; div.uitk-switch-control-handle 20.0x20.0 bg #ffffff r 50%; div.uitk-spacing.uitk-spacing-margin-blockstart-six 236.0x130.0 border T:1px solid #dfe0e4 / B:1px solid #dfe0e4 |
| How | at rest |

Crops: none.

#### name-field

Property name field. The "e.g. Marriott" text input in the filter rail. Clicked into only.

Page: search. Selector: `the Search by property name field`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 236 x 48 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Centra No2 14px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #191e3b | = |
| Text node | label.uitk-field-label: Centra No2 16px/20px 400, #191e3b | label.uitk-field-label: Centra No2 12px/16px 400, #191e3b |
| Transition | none | = |
| Cursor | default | = |
| Icon | 24 x 24, colour #191e3b | = |
| Painted layers | input.uitk-field-input.empty-placeholder 236.0x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px | input.uitk-field-input.empty-placeholder 236.0x48.0 bg #ffffff border T:1px solid #1668e3 / R:1px solid #1668e3 / B:1px solid #1668e3 / L:1px solid #1668e3 r 8px shadow #1668e3 0px 0px 0px 1px inset |
| How | at rest | clicked into the field |

Crops: `name-field-focused.png`.

#### filter-checkbox

Filter checkbox. A "Property class" checkbox in the filter rail: an uitk-checkbox box with its count-bearing label. Hovered only, never toggled.

Page: search. Selector: `an uitk-checkbox in the filter rail`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 240 x 34 | = |
| Padding | 8px 4px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Centra No2 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #191e3b | = |
| Text node | p.uitk-checkbox-label-content: Centra No2 14px/18px 400, #191e3b | = |
| Transition | none | = |
| Cursor | default | = |
| Painted layers | input.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18.0x18.0 bg #ffffff; span.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18.0x18.0 bg #ffffff border T:2px solid #818494 / R:2px solid #818494 / B:2px solid #818494 / L:2px solid #818494 r 4px; span::before.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18pxx18px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | input.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18.0x18.0 bg #ffffff; span.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18.0x18.0 bg #ffffff border T:2px solid #1668e3 / R:2px solid #1668e3 / B:2px solid #1668e3 / L:2px solid #1668e3 r 4px shadow #1668e3 0px 0px 0px 0px; span::before.uitk-layout-flex-item.uitk-layout-flex-item-flex-shrink-0 18pxx18px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover |

Crops: `filter-checkbox-default.png`, `filter-checkbox-hover.png`.

#### compare-switch

Compare switch. The "Compare properties" toggle over the filter rail. Hovered only, never switched.

Page: search. Selector: `the compare uitk-switch`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 212 x 54 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Centra No2 14px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #191e3b | = |
| Text node | span.uitk-switch-label-content: Centra No2 14px/18px 400, #191e3b | = |
| Transition | none | = |
| Cursor | default | = |
| Icon | 16 x 16, colour #191e3b | = |
| Painted layers | div.uitk-switch-control 48.0x24.0 bg #676a7d border T:2px solid #676a7d / R:2px solid #676a7d / B:2px solid #676a7d / L:2px solid #676a7d r 12px; div::before.uitk-switch-control 20pxx20px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 50%; div.uitk-switch-control-handle 20.0x20.0 bg #ffffff r 50% | = |
| Ancestor paint | 1 up div.uitk-layout-flex.uitk-card bg #ffffff | = |
| How | at rest | mouse hover |

Crops: `compare-switch-default.png`, `compare-switch-hover.png`.

#### urgency-note

Urgency note. "We have 1 left at this price" under a price: the critical-coloured nudge line.

Page: search. Selector: `the "We have N left" text on a card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 183 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.uitk-type-end: Centra No2 12px/16px 400, #a7183c |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `urgency-note-default.png`.

#### refund-note

Refund note. "Fully refundable" / "Reserve now, pay later" in positive green.

Page: search. Selector: `the Fully refundable text on a card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 287.19 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div.uitk-text.uitk-type-300: Centra No2 14px/18px 400, #227950 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `refund-note-default.png`.

#### map-card

Map card. The static map tile card at the top of the filter rail ("View in a map").

Page: search. Selector: `the .uitk-card holding the static map`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 236 x 143.14 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 14px/18px 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | button.uitk-link.uitk-link-align-center: Centra No2 14px/18px 400, #1668e3 |
| Transition | none |
| Cursor | default |
| ::before | 236px x 143.141px, absolute, bg #000000 @ 0, radius 16px |
| Painted layers | div.uitk-card.uitk-card-roundcorner-all 236.0x143.1 bg #ffffff r 16px; div::before.uitk-card.uitk-card-roundcorner-all 236pxx143.141px border T:1px solid #dfe0e4 / R:1px solid #dfe0e4 / B:1px solid #dfe0e4 / L:1px solid #dfe0e4 r 16px |
| How | at rest |

Crops: `map-card-default.png`.

### Mobile (390 wide)

#### m-header

Header. The mobile top bar.

Page: mobile. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #0c0e1c @ 0.08 0px 2px 12px 0px |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | div: Centra No2 14px/18px 500, #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 18 x 18, colour #191e3b |
| Painted layers | header.global-navigation-site-header 390.0x56.0 bg #ffffff shadow #0c0e1c @ 0.08 0px 2px 12px 0px; section.global-navigation-row.primary 390.0x56.0 bg #ffffff; div.uitk-menu-container.animation-disabled 0.0x0.0 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; hr.uitk-spacing.uitk-spacing-margin-block-four 0.0x0.0 border T:1px solid #dfe0e4 / R:1px inset #191e3b / L:1px inset #191e3b; div.uitk-menu-container.animation-disabled 0.0x0.0 bg #ffffff r 8px shadow #0c0e1c @ 0.08 0px 2px 12px 0px; a::before.uitk-button.uitk-button-medium 100%x100% bg #0e3672 r 40000px |
| Ancestor paint | 1 up div.page-header.with-shadow shadow #0c0e1c @ 0.12 0px 1px 0px 0px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hero-title

Hero title.

Page: mobile. Selector: `[data-testid="hero-title-campaign"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 277 x 135 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Reckless XPD 44px/40px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-search-shell

Search form.

Page: mobile. Selector: `[data-testid="multi-product-search-form"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 252 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | span.egds-tab-custom-text: Centra No2 14px/18px 500, #1668e3 |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #191e3b |
| Painted layers | div.uitk-card.uitk-card-roundcorner-all 342.0x252.0 bg #ffffff r 16px; div::before.uitk-card.uitk-card-roundcorner-all 342pxx252px border T:1px solid #dfe0e4 / R:1px solid #dfe0e4 / B:1px solid #dfe0e4 / L:1px solid #dfe0e4 r 16px; ul.egds-tabs-custom.egds-tabs-custom-natural 342.0x110.0 bg #ffffff r 16px 16px 0px 0px shadow #dfe0e4 0px 1px 0px 0px; a.egds-tab-custom-anchor.egds-tab-custom-anchor-selected 96.0x110.0 shadow #1668e3 0px -2px 0px 0px inset; li.egds-tab-custom-highlighter 0.0x2.0 bg #1668e3; input.uitk-field-input.empty-placeholder 58.3x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px |
| How | at rest |

Crops: `m-search-shell-default.png`.

#### m-field

Search field. The first search field at 390 wide.

Page: mobile. Selector: `.uitk-field`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.33 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Centra No2 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #191e3b | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 24 x 24, colour #191e3b | = | = | = |
| Painted layers | input.uitk-field-input.empty-placeholder 58.3x48.0 bg #ffffff border T:1px solid #818494 / R:1px solid #818494 / B:1px solid #818494 / L:1px solid #818494 r 8px | = | input.uitk-field-input.empty-placeholder 58.3x48.0 bg #ffffff border T:1px solid #1668e3 / R:1px solid #1668e3 / B:1px solid #1668e3 / L:1px solid #1668e3 r 8px shadow #1668e3 0px 0px 0px 1px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-field-default.png`, `m-field-hover.png`, `m-field-focus-visible.png`, `m-field-pressed.png`.

#### m-search-button

Search button.

Page: mobile. Selector: `the Search button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83 x 48 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 40000px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #e59700 offset 2px | = |
| Font | Centra No2 16px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 83px x 48px, absolute, bg #0e3672, radius 40000px | = | = | = |
| ::after | 83px x 48px, absolute, bg #1668e3, radius 40000px | = | = | = |
| Painted layers | button::before.uitk-button.uitk-button-large 83pxx48px bg #0e3672 r 40000px; button::after.uitk-button.uitk-button-large 83pxx48px bg #1668e3 r 40000px | = | button.uitk-button.uitk-button-large 83.0x48.0 r 40000px outline 5px auto #e59700 offset 2px; button::before.uitk-button.uitk-button-large 83pxx48px bg #0e3672 r 40000px; button::after.uitk-button.uitk-button-large 83pxx48px bg #1668e3 r 40000px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-search-button-default.png`, `m-search-button-hover.png`, `m-search-button-focus-visible.png`, `m-search-button-pressed.png`.

#### m-card

Deal card.

Page: mobile. Selector: `a deals .uitk-card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 483.58 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Centra No2 16px/normal 400 |
| Letter spacing | normal |
| Colour | #191e3b |
| Text node | h6.uitk-heading.uitk-heading-6: Centra No2 16px/20px 500, #191e3b |
| Transition | none |
| Cursor | default |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.uitk-layout-flex.uitk-layout-flex-block-size-full-size 342.0x483.6 bg #ffffff r 16px; div.uitk-layout-flex.uitk-layout-flex-block-size-full-size 342.0x256.5 bg #ffffff r 16px; div.uitk-image-placeholder.uitk-image-placeholder-image 342.0x256.5 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 342.0x256.5 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 342.0x256.5 bg #c8dff9 image url(data:…); div.uitk-image-placeholder.uitk-image-placeholder-image 0.0x0.0 bg #c8dff9 image url(data:…) |
| How | at rest |

Crops: `m-card-default.png`.

## Transitions declared in the readable stylesheets

Expedia's stylesheets are linked from its travel-assets.com CDN, which permits the CSSOM read, so this list holds every transition rule each page exposes; the per-state Transition rows above are the computed values that apply them.
