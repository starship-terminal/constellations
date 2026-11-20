# GoFundMe component measurements

Computed styles read from gofundme.com on 2026-11-16 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the consumer pages that resolve the :root-declared `--hrt-*` light theme (home, discover, search, a public fundraiser page, the wizard and the pages in screenshots/), the WordPress content stack at /c/* (an older hrt-base-*/wp-* layer, a different public system), the /sign-in auth shell (which hydrates to a card or stays an empty form in headless), and the mobile drawer — with the Transcend 'Privacy Information' consent banner hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). No dark variant or theme toggle exists on the consumer site; the declared [data-theme="pro"] layer never paints here. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-promo

Global promo banner. The dismissal strip above the header ("Introducing the Kind 50…"); its close icon-button was never pressed.

Page: home. Selector: `.hrt-global-promo-banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 16px 40px |
| Border | none |
| Radius | 0px |
| Background | #ccf88e |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #274a34 |
| Text node | span: GoFundMe Sans 16px/24px 100, #274a34 |
| Transition | none |
| Icon | 24 x 24, colour #232323, fill #000000 |
| Painted layers | div.hrt-global-promo-banner 1440.0x64.0 bg #ccf88e |
| How | at rest |

Crops: `mkt-promo-default.png`.

#### mkt-header

Site header. The sticky bar on every consumer page: the GoFundMe mark, Donate/Fundraise/About dropdown triggers, Search, "Sign in" and "Start a GoFundMe".

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | span: GoFundMe Sans 16px/19.2px 100, #232323 |
| Transition | box-shadow, background-color 0.2s cubic-bezier(0.3, 0.01, 0, 1) |
| Icon | 0 x 0, colour #232323, fill #000000 |
| Painted layers | a.hrt-header-skip.hrt-show-on-focus 16.0x34.0 bg #ffffff r 9999px; div.hrt-header-dropdown-caret 8.0x5.0 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0; div.hrt-header-dropdown-content.hrt-header-dropdown-content--left 632.0x236.0 bg #ffffff r 8px shadow #232323 @ 0.1 0px 6px 14px 0px; div.hrt-spot-icon.hrt-spot-icon--neutral-subtle 40.0x40.0 bg #f5f5f5 r 9999px; a.hrt-base-list-item--body-size.hrt-base-list-item 296.0x78.0 bg #ffffff r 12px; a.hrt-base-list-item--body-size.hrt-base-list-item 296.0x78.0 bg #ffffff r 12px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The GoFundMe mark in the header, linking home.

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 105 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Transition | none |
| Cursor | pointer |
| Icon | 105 x 36, colour #232323 |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-search

Nav search button. The "Search" header button (search-field styling) to /s; measured, never followed.

Page: home. Selector: `header Search button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91 x 34 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GoFundMe Sans 16px/19.2px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #232323, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.default-header_search-button.hrt-hide-max-md 91.0x34.0 bg #232323 @ 0.05 r 9999px | a.default-header_search-button.hrt-hide-max-md 91.0x34.0 r 9999px outline 1px auto #101010 offset 1px | a.default-header_search-button.hrt-hide-max-md 91.0x34.0 bg #232323 @ 0.1 r 9999px |

Crops: `nav-search-default.png`, `nav-search-hover.png`, `nav-search-focus-visible.png`, `nav-search-pressed.png`.

#### nav-donate-dd

Nav dropdown trigger. The "Donate" header item whose dropdown opens on hover (panel measured next; links never followed).

Page: home. Selector: `button.hrt-header-dropdown-button Donate`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87 x 34 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/19.2px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span.hrt-header-dropdown-title-wrapper: GoFundMe Sans 16px/19.2px 100, #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.hrt-header-dropdown-caret 8.0x5.0 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0 | button.hrt-ml-1.hrt-header-dropdown-button 87.0x34.0 bg #232323 @ 0.05 r 9999px; div.hrt-header-dropdown-caret.hrt-header-dropdown-caret--open 8.1x5.2 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0 | button.hrt-ml-1.hrt-header-dropdown-button 87.0x34.0 r 9999px outline 1px auto #101010 offset 0px; div.hrt-header-dropdown-caret 8.0x5.0 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0 | button.hrt-ml-1.hrt-header-dropdown-button 87.0x34.0 bg #232323 @ 0.1 r 9999px; div.hrt-header-dropdown-caret 8.0x5.0 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-donate-dd-default.png`, `nav-donate-dd-hover.png`, `nav-donate-dd-focus-visible.png`, `nav-donate-dd-pressed.png`.

#### nav-panel

Header dropdown panel. The mega-dropdown panel under "Donate" (multi-column link groups); opened by hovering the trigger, its links never followed.

Page: home. Selector: `.hrt-header-dropdown-content--open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 632 x 236 |
| Padding | 16px |
| Border | none |
| Radius | 8px |
| Background | #ffffff |
| Box shadow | #232323 @ 0.1 0px 6px 14px 0px |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | p.hrt-text-legend.hrt-mb-0: GoFundMe Sans 20px/22px 100, #232323, ls -0.2px |
| Transition | opacity, top, visibility 0.15s, 0.15s ease-in-out, linear |
| Icon | 24 x 24, colour #424242, fill #000000 |
| ::before | 632px x 8px, absolute, bg #000000 @ 0, radius 0px |
| ::after | 632px x 8px, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | div.hrt-header-dropdown-content.hrt-header-dropdown-content--left 632.0x236.0 bg #ffffff r 8px shadow #232323 @ 0.1 0px 6px 14px 0px; div.hrt-spot-icon.hrt-spot-icon--neutral-subtle 40.0x40.0 bg #f5f5f5 r 9999px; a.hrt-base-list-item--body-size.hrt-base-list-item 296.0x78.0 bg #ffffff r 12px; a.hrt-base-list-item--body-size.hrt-base-list-item 296.0x78.0 bg #ffffff r 12px; a.hrt-base-list-item--body-size.hrt-base-list-item 296.0x78.0 bg #ffffff r 12px; a.hrt-base-list-item--body-size.hrt-base-list-item 296.0x78.0 bg #ffffff r 12px |
| How | at rest |

Crops: `nav-panel-default.png`.

#### nav-about-dd

About dropdown trigger. The "About" header item — the right-aligned dropdown trigger; its panel was never opened beyond the one menu reading.

Page: home. Selector: `button.hrt-header-dropdown-button About`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 75 x 34 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/19.2px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span.hrt-header-dropdown-title-wrapper: GoFundMe Sans 16px/19.2px 100, #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.hrt-header-dropdown-caret 8.0x5.0 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0 | button.hrt-header-dropdown-button.hrt-button 75.0x34.0 bg #232323 @ 0.05 r 9999px; div.hrt-header-dropdown-caret.hrt-header-dropdown-caret--open 8.1x5.2 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0 | button.hrt-header-dropdown-button.hrt-button 75.0x34.0 r 9999px outline 1px auto #101010 offset 0px; div.hrt-header-dropdown-caret 8.0x5.0 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0 | button.hrt-header-dropdown-button.hrt-button 75.0x34.0 bg #232323 @ 0.1 r 9999px; div.hrt-header-dropdown-caret 8.0x5.0 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-about-dd-default.png`, `nav-about-dd-hover.png`, `nav-about-dd-focus-visible.png`, `nav-about-dd-pressed.png`.

#### nav-signin

Sign in link. The "Sign in" header link (tertiary button styling) to /sign-in; measured, never followed.

Page: home. Selector: `header Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64 x 34 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GoFundMe Sans 16px/19.2px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span: GoFundMe Sans 16px/19.2px 100, #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.hrt-ml-1.hrt-button 64.0x34.0 bg #232323 @ 0.05 r 9999px | a.hrt-ml-1.hrt-button 64.0x34.0 r 9999px outline 1px auto #101010 offset 1px | a.hrt-ml-1.hrt-button 64.0x34.0 bg #232323 @ 0.1 r 9999px |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-start

Header CTA. The pill "Start a GoFundMe" header button (secondary hierarchy); links to the wizard, measured never followed.

Page: home. Selector: `header Start a GoFundMe`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 161 x 32 | = | = | = |
| Padding | 4px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0 | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | #b7b7b6 0px 0px 0px 1px inset | #585858 0px 0px 0px 1px inset | = | #595959 0px 0px 0px 1px inset |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GoFundMe Sans 14px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span: GoFundMe Sans 14px/20px 175, #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.default-header_shared-default-header-sign-up-button.hrt-ml-2 161.0x32.0 bg #ffffff @ 0 r 9999px shadow #b7b7b6 0px 0px 0px 1px inset | a.default-header_shared-default-header-sign-up-button.hrt-ml-2 161.0x32.0 bg #232323 @ 0.05 r 9999px shadow #585858 0px 0px 0px 1px inset | a.default-header_shared-default-header-sign-up-button.hrt-ml-2 161.0x32.0 bg #ffffff @ 0 r 9999px shadow #b7b7b6 0px 0px 0px 1px inset outline 1px auto #101010 offset 1px | a.default-header_shared-default-header-sign-up-button.hrt-ml-2 161.0x32.0 bg #232323 @ 0.1 r 9999px shadow #595959 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-start-default.png`, `nav-start-hover.png`, `nav-start-focus-visible.png`, `nav-start-pressed.png`.

### Home

#### hero-h1

Hero headline. "Where successful fundraisers start" — the home hero display heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 770 x 180.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 82px/90.2px 175 |
| Letter spacing | -1.64px |
| Colour | #232323 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The primary "Start a GoFundMe" button in the hero; links to the wizard, measured never followed.

Page: home. Selector: `hero Start a GoFundMe`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 190 x 56 | = | = | = |
| Padding | 2px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #274a34 | #2d6339 | = | #2d6339 |
| Box shadow | #000000 @ 0 0px 0px 0px 1440px inset | = | = | #357d3a @ 0.25 0px 0px 0px 1440px inset |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GoFundMe Sans 16px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ccf88e | = | = | = |
| Text node | span: GoFundMe Sans 16px/20px 175, #ccf88e | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hrt-button.hrt-button--hierarchy-primary 190.0x56.0 bg #274a34 r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset | a.hrt-button.hrt-button--hierarchy-primary 190.0x56.0 bg #2d6339 r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset | a.hrt-button.hrt-button--hierarchy-primary 190.0x56.0 bg #274a34 r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset outline 1px auto #101010 offset 1px | a.hrt-button.hrt-button--hierarchy-primary 190.0x56.0 bg #2d6339 r 9999px shadow #357d3a @ 0.25 0px 0px 0px 1440px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### section-h2

Section heading. A marketing section heading further down the home page.

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 880 x 140.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 64px/70.4px 175 |
| Letter spacing | -1.28px |
| Colour | #232323 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### collection-btn

Collection selector. A "Happening worldwide"-style collection filter pill; measured at rest, never toggled (toggling would re-filter the rail).

Page: home. Selector: `collection-selector button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 247 x 40 | = | = | = |
| Padding | 2px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #ffffff @ 0 | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | #b7b7b6 0px 0px 0px 1px inset | #585858 0px 0px 0px 1px inset | = | #595959 0px 0px 0px 1px inset |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #232323, fill #000000 | = | = | = |
| Painted layers | button.collection-selector_button.hrt-button 247.0x40.0 bg #ffffff @ 0 r 24px shadow #b7b7b6 0px 0px 0px 1px inset | button.collection-selector_button.hrt-button 247.0x40.0 bg #232323 @ 0.05 r 24px shadow #585858 0px 0px 0px 1px inset | button.collection-selector_button.hrt-button 247.0x40.0 bg #ffffff @ 0 r 24px shadow #b7b7b6 0px 0px 0px 1px inset outline 1px auto #101010 offset 0px | button.collection-selector_button.hrt-button 247.0x40.0 bg #232323 @ 0.1 r 24px shadow #595959 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `collection-btn-hover.png`, `collection-btn-focus-visible.png`, `collection-btn-pressed.png`.

#### card-media-tag

Media tag. A location tag chip overlaid on a fundraiser card image ("Blaine, Minnesota" and neighbours).

Page: home. Selector: `.hrt-media-tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 207 x 24 |
| Padding | 0px 8px |
| Gap | 4px |
| Border | 1px solid #000000 @ 0 |
| Radius | 4px |
| Background | #ccf88e |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 14px/14px 175 |
| Letter spacing | normal |
| Colour | #274a34 |
| Transition | none |
| Painted layers | span.hrt-tag.hrt-tag--brand 207.0x24.0 bg #ccf88e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px |
| How | at rest |

Crops: `card-media-tag-default.png`.

#### pause-motion-btn

Pause-motion icon button. The reduced-motion control on the how-it-works steps; an icon-only button, measured never pressed.

Page: home. Selector: `button[aria-label*="pause" i]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.8 | #ffffff @ 0.7 | = | = |
| Box shadow | #232323 @ 0.1 0px 1px 2px 0px | #232323 @ 0.1 0px 1.99646px 5.98582px 0px | = | #232323 @ 0.1 0px 1.97868px 5.91473px 0px |
| Backdrop filter | blur(20px) | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #232323, fill #000000 | = | = | = |
| Painted layers | button.how-it-works-steps_pauseButton.hrt-icon-button 32.0x32.0 bg #ffffff @ 0.8 r 9999px shadow #232323 @ 0.1 0px 1px 2px 0px | button.how-it-works-steps_pauseButton.hrt-icon-button 32.0x32.0 bg #ffffff @ 0.7 r 9999px shadow #232323 @ 0.1 0px 1.99646px 5.98582px 0px | button.how-it-works-steps_pauseButton.hrt-icon-button 32.0x32.0 bg #ffffff @ 0.8 r 9999px shadow #232323 @ 0.1 0px 1px 2px 0px outline 1px auto #101010 offset 0px | button.how-it-works-steps_pauseButton.hrt-icon-button 32.0x32.0 bg #ffffff @ 0.8 r 9999px shadow #232323 @ 0.1 0px 1.97868px 5.91473px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pause-motion-btn-default.png`, `pause-motion-btn-hover.png`, `pause-motion-btn-focus-visible.png`, `pause-motion-btn-pressed.png`.

#### carousel-btn

Carousel arrow. A forward arrow icon-button on a fundraiser rail; measured never pressed (it would scroll the rail).

Page: home. Selector: `button[aria-label*="forward" i]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #b7b7b6 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0 | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #232323, fill #000000 | = | = | = |
| Painted layers | button.hrt-icon-button.hrt-icon-button--hierarchy-secondary 32.0x32.0 bg #ffffff @ 0 border T:1px #b7b7b6 / R:1px #b7b7b6 / B:1px #b7b7b6 / L:1px #b7b7b6 r 9999px | button.hrt-icon-button.hrt-icon-button--hierarchy-secondary 32.0x32.0 bg #232323 @ 0.05 border T:1px #b7b7b6 / R:1px #b7b7b6 / B:1px #b7b7b6 / L:1px #b7b7b6 r 9999px | button.hrt-icon-button.hrt-icon-button--hierarchy-secondary 32.0x32.0 bg #ffffff @ 0 border T:1px #b7b7b6 / R:1px #b7b7b6 / B:1px #b7b7b6 / L:1px #b7b7b6 r 9999px outline 1px auto #101010 offset 0px | button.hrt-icon-button.hrt-icon-button--hierarchy-secondary 32.0x32.0 bg #232323 @ 0.1 border T:1px #b7b7b6 / R:1px #b7b7b6 / B:1px #b7b7b6 / L:1px #b7b7b6 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-btn-default.png`, `carousel-btn-hover.png`, `carousel-btn-focus-visible.png`, `carousel-btn-pressed.png`.

#### merch-card

Featured merch card. A featured-topic merch card link (large image card); measured at rest and on hover, never followed.

Page: home. Selector: `merch-card link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1104 x 311 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #fafafa | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GoFundMe Sans 16px/24px 100 | = |
| Letter spacing | normal | = |
| Colour | #232323 | = |
| Text node | strong: GoFundMe Sans 14px/14px 175, #642878 | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = |
| Cursor | pointer | = |
| Icon | 12 x 12, colour #232323, fill #000000 | = |
| Painted layers | a.merch-card_merch-unit-link.hrt-action-card 1104.0x311.0 bg #fafafa r 16px; div.merch-card_merch-unit-link.hrt-media-card 1104.0x311.0 bg #fafafa r 16px; span.merch-card_merch-unit-tag.hrt-tag 49.0x24.0 bg #eccff6 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px | a.merch-card_merch-unit-link.hrt-action-card 1104.0x311.0 bg #fafafa r 16px; div.merch-card_merch-unit-link.hrt-media-card 1104.0x311.0 bg #fafafa r 16px; span.merch-card_merch-unit-tag.hrt-tag 49.0x24.0 bg #eccff6 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px; div.merch-card_merch-unit-button.hrt-text-default 130.0x38.3 bg #ffffff r 8px |
| How | at rest | mouse hover |

Crops: `merch-card-default.png`, `merch-card-hover.png`.

### Footer

#### footer

Footer. The page footer: column links, social icons, the locale selector and the Transcend consent link.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 686 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | h3.hrt-footer-list-header.hrt-text: GoFundMe Sans 16px/24px 175, #232323 |
| Transition | none |
| Icon | 16 x 16, colour #232323, fill #000000 |
| Painted layers | div.hrt-mt-0.hrt-mb-0 1440.0x1.0 border T:1px #d8d8d8; a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #ffffff r 12px; a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #ffffff r 12px; a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #ffffff r 12px; a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #ffffff r 12px; a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #ffffff r 12px |
| Ancestor paint | 1 up div.home_footerContainer bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a Careers`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 268 x 40 | = | = | = |
| Padding | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | #fafafa | = | #fafafa |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span.hrt-base-list-item-title: GoFundMe Sans 16px/24px 100, #232323 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #ffffff r 12px | a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #fafafa r 12px | a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #ffffff r 12px outline 1px auto #101010 offset 1px | a.hrt-base-list-item--condensed-size.hrt-base-list-item 268.0x40.0 bg #fafafa r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-more

Footer accordion. A footer accordion button ("More resources"); measured at rest, never toggled.

Page: home. Selector: `footer More resources button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 158 x 40 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/20px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #232323, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | button.hrt-footer-resources-button.hrt-button 158.0x40.0 bg #232323 @ 0.05 r 9999px | button.hrt-footer-resources-button.hrt-button 158.0x40.0 r 9999px outline 1px auto #101010 offset 0px | button.hrt-footer-resources-button.hrt-button 158.0x40.0 bg #232323 @ 0.1 r 9999px |

Crops: `footer-more-default.png`, `footer-more-hover.png`, `footer-more-focus-visible.png`, `footer-more-pressed.png`.

#### locale-btn

Locale selector. The "United States · English" locale control in the footer; measured, never opened (opening would offer a locale switch).

Page: home. Selector: `footer locale button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 187 x 36 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff @ 0 | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | #b7b7b6 0px 0px 0px 1px inset | #585858 0px 0px 0px 1px inset | = | #595959 0px 0px 0px 1px inset |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 14px/20px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #232323, fill #000000 | = | = | = |
| Painted layers | button.locale-picker_localePickerButton.hrt-button 187.0x36.0 bg #ffffff @ 0 r 12px shadow #b7b7b6 0px 0px 0px 1px inset | button.locale-picker_localePickerButton.hrt-button 187.0x36.0 bg #232323 @ 0.05 r 12px shadow #585858 0px 0px 0px 1px inset | button.locale-picker_localePickerButton.hrt-button 187.0x36.0 bg #ffffff @ 0 r 12px shadow #b7b7b6 0px 0px 0px 1px inset outline 1px auto #101010 offset 0px | button.locale-picker_localePickerButton.hrt-button 187.0x36.0 bg #232323 @ 0.1 r 12px shadow #595959 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `locale-btn-default.png`, `locale-btn-hover.png`, `locale-btn-focus-visible.png`, `locale-btn-pressed.png`.

#### cookie-btn

Cookie preferences link. The "Manage Cookie Preferences" Transcend footer control; measured, never pressed (it would open the consent manager).

Page: home. Selector: `.transcend-consent-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 0 x 0 | - | - | = |
| Padding | 2px 8px | - | - | = |
| Gap | 8px | - | - | = |
| Border | none | - | - | = |
| Radius | 9999px | - | - | = |
| Background | transparent | - | - | #232323 @ 0.1 |
| Box shadow | none | - | - | = |
| Outline | none | - | - | = |
| Font | GoFundMe Sans 16px/20px 100 | - | - | = |
| Letter spacing | normal | - | - | = |
| Colour | #232323 | - | - | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | - | - | = |
| Cursor | pointer | - | - | = |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('.transcend-consent-link, footer button, footer a').filter({ hasText: /Manage Cookie Preferences/i }).first().first().first()    | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Painted layers | - | = | = | button.hrt-footer-legal-item.hrt-text-left 0.0x0.0 bg #232323 @ 0.1 r 9999px |

Crops: none.

### Discover

#### disc-h1

Discover headline. The /discover masthead ("Fundraisers" and the result count).

Page: discover. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 714.66 x 180.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 82px/90.2px 175 |
| Letter spacing | -1.64px |
| Colour | #232323 |
| Transition | none |
| How | at rest |

Crops: `disc-h1-default.png`.

#### disc-cat-btn

Category expander. The "Show more categories" button under the category chips; measured at rest, never toggled.

Page: discover. Selector: `Show more categories`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 225 x 48 | = | = | = |
| Padding | 2px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0 | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | #b7b7b6 0px 0px 0px 1px inset | #585858 0px 0px 0px 1px inset | = | #595959 0px 0px 0px 1px inset |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span: GoFundMe Sans 16px/20px 175, #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hrt-button.hrt-button--hierarchy-secondary 225.0x48.0 bg #ffffff @ 0 r 9999px shadow #b7b7b6 0px 0px 0px 1px inset | button.hrt-button.hrt-button--hierarchy-secondary 225.0x48.0 bg #232323 @ 0.05 r 9999px shadow #585858 0px 0px 0px 1px inset | button.hrt-button.hrt-button--hierarchy-secondary 225.0x48.0 bg #ffffff @ 0 r 9999px shadow #b7b7b6 0px 0px 0px 1px inset outline 1px auto #101010 offset 0px | button.hrt-button.hrt-button--hierarchy-secondary 225.0x48.0 bg #232323 @ 0.1 r 9999px shadow #595959 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `disc-cat-btn-default.png`, `disc-cat-btn-hover.png`, `disc-cat-btn-focus-visible.png`, `disc-cat-btn-pressed.png`.

#### fundraiser-card

Fundraiser card. A discover-grid fundraiser card (image, location tag, title, raised line, progress bar); measured at rest and on hover, never followed.

Page: discover. Selector: `[class*=fundraiser-card]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 354.66 x 339.78 | = |
| Padding | 8px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | #ffffff | #fafafa |
| Box shadow | none | = |
| Outline | none | = |
| Font | GoFundMe Sans 16px/24px 100 | = |
| Letter spacing | normal | = |
| Colour | #232323 | = |
| Text node | span.hrt-media-tag-text: GoFundMe Sans 14px/24px 175, #ffffff | = |
| Transition | background-color 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = |
| Cursor | pointer | = |
| Painted layers | div.fundraiser-card_container.hrt-media-card 354.7x339.8 bg #ffffff r 12px; div.fundraiser-card_imageContainer 338.7x225.8 bg #f5f5f5 r 12px; span.fundraiser-card_mediaTag.hrt-hide-max-md 145.0x26.0 bg #000000 @ 0.55 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px; progress.fundraiser-card_progressBar.hrt-goal-bar 306.7x8.0 bg #232323 @ 0.05 r 9999px | div.fundraiser-card_container.hrt-media-card 354.7x339.8 bg #fafafa r 12px; div.fundraiser-card_imageContainer 338.7x225.8 bg #f5f5f5 r 12px; span.fundraiser-card_mediaTag.hrt-hide-max-md 145.0x26.0 bg #000000 @ 0.55 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px; progress.fundraiser-card_progressBar.hrt-goal-bar 306.7x8.0 bg #232323 @ 0.05 r 9999px |
| Ancestor paint | 1 up a.hrt-action-card.hrt-base-button bg #ffffff | 1 up a.hrt-action-card.hrt-base-button bg #fafafa |
| How | at rest | mouse hover |

Crops: `fundraiser-card-default.png`, `fundraiser-card-hover.png`.

#### card-title

Card title. The fundraiser title inside a discover card.

Page: discover. Selector: `.fundraiser-card title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 306.66 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/16px 175 |
| Letter spacing | normal |
| Colour | #232323 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `card-title-default.png`.

#### card-goal-bar

Goal bar (card). The progress element inside a discover card.

Page: discover. Selector: `card progress`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 306.66 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | label.hrt-goal-bar-label.hrt-goal-bar-label--default: GoFundMe Sans 14px/20px 175, #232323 |
| Transition | none |
| Cursor | pointer |
| Painted layers | progress.fundraiser-card_progressBar.hrt-goal-bar 306.7x8.0 bg #232323 @ 0.05 r 9999px |
| How | at rest |

Crops: `card-goal-bar-default.png`.

#### card-location

Card location tag. The location tag chip overlaid on a card image.

Page: discover. Selector: `[class*=mediaTag]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 145 x 26 |
| Padding | 0px 8px |
| Gap | 4px |
| Border | 1px solid #000000 @ 0 |
| Radius | 4px |
| Background | #000000 @ 0.55 |
| Box shadow | none |
| Backdrop filter | blur(20px) |
| Outline | none |
| Font | GoFundMe Sans 14px/24px 175 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.hrt-media-tag-text: GoFundMe Sans 14px/24px 175, #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.fundraiser-card_mediaTag.hrt-hide-max-md 145.0x26.0 bg #000000 @ 0.55 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px |
| Ancestor paint | 1 up div.fundraiser-card_imageContainer bg #f5f5f5 |
| How | at rest |

Crops: `card-location-default.png`.

### Search

#### s-h1

Search headline. The /s results masthead.

Page: search. Selector: `h1`. States: .

Not found on the page at capture time.

#### s-card

Search result card. A fundraiser card in the /s?q=medical results grid; measured, never followed.

Page: search. Selector: `[class*=fundraiser-card]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 270 x 335 |
| Padding | 16px |
| Gap | 16px |
| Border | 1px solid #d8d8d8 |
| Radius | 20px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 14px/20px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | h3.charity-card_title.hrt-fundraiser-card-title: GoFundMe Sans 20px/22px 175, #232323, ls -0.2px |
| Transition | background-color, border-color, box-shadow 0.5s cubic-bezier(0.3, 0.01, 0, 1) |
| Cursor | pointer |
| Painted layers | a.charity-card_card.hrt-fundraiser-card 270.0x335.0 border T:1px #d8d8d8 / R:1px #d8d8d8 / B:1px #d8d8d8 / L:1px #d8d8d8 r 20px; div.charity-card_cardContent 236.0x109.0 border T:1px #d8d8d8 |
| How | at rest |

Crops: `s-card-default.png`.

#### s-avatar

Avatar. An hrt-avatar on a search result (the organiser image).

Page: search. Selector: `.hrt-avatar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 24px/36px 175 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | span.hrt-avatar-initial.notranslate: GoFundMe Sans 24px/36px 175, #232323 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.hrt-default-avatar.hrt-avatar 96.0x96.0 bg #f5f5f5 r 9999px |
| How | at rest |

Crops: `s-avatar-default.png`.

### Fundraiser page

#### f-title

Fundraiser title. The campaign title h1 on a public /f/<slug> page.

Page: fundraiser. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1104 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 40px/48px 175 |
| Letter spacing | -0.8px |
| Colour | #232323 |
| Transition | none |
| How | at rest |

Crops: `f-title-default.png`.

#### f-raised

Raised amount. The "$X raised of $Y goal" line.

Page: fundraiser. Selector: `raised amount line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 228.16 x 57.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 24px/28.8px 175 |
| Letter spacing | -0.24px |
| Colour | #232323 |
| Text node | span: GoFundMe Sans 24px/28.8px 175, #232323, ls -0.24px |
| Transition | none |
| How | at rest |

Crops: `f-raised-default.png`.

#### f-goal-bar

Goal bar (fundraiser). The progress element beside the raised line (a progress-meter on the campaign pages).

Page: fundraiser. Selector: `progress-meter`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.16 x 77.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | div: GoFundMe Sans 14px/21px 175, #232323 |
| Transition | none |
| Icon | 64 x 64, colour #232323, fill #000000 |
| How | at rest |

Crops: `f-goal-bar-default.png`.

#### f-donate

Donate button. The primary "Donate now" button; all four states measured, the button never pressed — no donation was ever started.

Page: fundraiser. Selector: `a.donate-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 308.16 x 48 | = | = | = |
| Padding | 2px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ccf88e | #e9fcce | = | #e9fccd |
| Box shadow | #000000 @ 0 0px 0px 0px 1440px inset | = | = | #357d3a @ 0.247 0px 0px 0px 1440px inset |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GoFundMe Sans 16px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #274a34 | = | = | = |
| Text node | span.donate-button_buttonLabel: GoFundMe Sans 16px/20px 175, #274a34 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.donate-button_donateButton.hrt-button 308.2x48.0 bg #ccf88e r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset | a.donate-button_donateButton.hrt-button 308.2x48.0 bg #e9fcce r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset | a.donate-button_donateButton.hrt-button 308.2x48.0 bg #ccf88e r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset outline 1px auto #101010 offset 1px | a.donate-button_donateButton.hrt-button 308.2x48.0 bg #e9fccd r 9999px shadow #357d3a @ 0.247 0px 0px 0px 1440px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `f-donate-default.png`, `f-donate-hover.png`, `f-donate-focus-visible.png`, `f-donate-pressed.png`.

#### f-share

Share button. The secondary "Share" button; states measured, never pressed.

Page: fundraiser. Selector: `Share`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 308.16 x 48 | = | = | = |
| Padding | 2px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #274a34 | #2d6339 | = | #2d6339 |
| Box shadow | #000000 @ 0 0px 0px 0px 1440px inset | = | = | #357d3a @ 0.247 0px 0px 0px 1440px inset |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ccf88e | = | = | = |
| Text node | span: GoFundMe Sans 16px/20px 175, #ccf88e | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hrt-button.hrt-button--hierarchy-primary 308.2x48.0 bg #274a34 r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset | button.hrt-button.hrt-button--hierarchy-primary 308.2x48.0 bg #2d6339 r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset | button.hrt-button.hrt-button--hierarchy-primary 308.2x48.0 bg #274a34 r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset outline 1px auto #101010 offset 0px | button.hrt-button.hrt-button--hierarchy-primary 308.2x48.0 bg #2d6339 r 9999px shadow #357d3a @ 0.247 0px 0px 0px 1440px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `f-share-default.png`, `f-share-hover.png`, `f-share-focus-visible.png`, `f-share-pressed.png`.

#### f-message

Message button. The "Message" button beside Share; states measured, never pressed.

Page: fundraiser. Selector: `Message`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117 x 40 | = | = | = |
| Padding | 2px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0 | #232323 @ 0.05 | = | #232323 @ 0.1 |
| Box shadow | #b7b7b6 0px 0px 0px 1px inset | #585858 0px 0px 0px 1px inset | = | #595959 0px 0px 0px 1px inset |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span: GoFundMe Sans 16px/20px 175, #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hrt-button.hrt-button--hierarchy-secondary 117.0x40.0 bg #ffffff @ 0 r 9999px shadow #b7b7b6 0px 0px 0px 1px inset | button.hrt-button.hrt-button--hierarchy-secondary 117.0x40.0 bg #232323 @ 0.05 r 9999px shadow #585858 0px 0px 0px 1px inset | button.hrt-button.hrt-button--hierarchy-secondary 117.0x40.0 bg #ffffff @ 0 r 9999px shadow #b7b7b6 0px 0px 0px 1px inset outline 1px auto #101010 offset 0px | button.hrt-button.hrt-button--hierarchy-secondary 117.0x40.0 bg #232323 @ 0.1 r 9999px shadow #595959 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `f-message-default.png`, `f-message-hover.png`, `f-message-focus-visible.png`, `f-message-pressed.png`.

#### f-readmore

Read more. The text-button expanding the campaign story; measured at rest, never toggled.

Page: fundraiser. Selector: `Read more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span: GoFundMe Sans 16px/24px 100, #232323 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.hrt-text-button.hrt-text-button--underlined 83.0x24.0 outline 1px auto #101010 offset 0px | = |

Crops: `f-readmore-default.png`, `f-readmore-hover.png`, `f-readmore-focus-visible.png`, `f-readmore-pressed.png`.

#### f-avatar

Organiser avatar. The organiser avatar in the campaign meta row.

Page: fundraiser. Selector: `.hrt-avatar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 9999px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 175 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | span.hrt-avatar-initial.notranslate: GoFundMe Sans 16px/24px 175, #232323 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.hrt-default-avatar.hrt-avatar 40.0x40.0 bg #f5f5f5 r 9999px |
| How | at rest |

Crops: `f-avatar-default.png`.

#### f-media-nav

Media viewer arrow. An arrow icon-button on the fundraiser media viewer; measured never pressed.

Page: fundraiser. Selector: `media next button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | 1px solid #ffffff | = | 1px solid #ffffff |
| Radius | 9999px | = | = | = |
| Background | #000000 @ 0.55 | #000000 @ 0.25 | = | #000000 @ 0.255 |
| Box shadow | #232323 @ 0.1 0px 1px 2px 0px | #232323 @ 0.1 0px 1.99645px 5.98582px 0px | = | #232323 @ 0.1 0px 1.98476px 5.93903px 0px |
| Backdrop filter | blur(20px) | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button.hero-media-viewer_rightButton.hrt-icon-on-overlay 32.0x32.0 bg #000000 @ 0.55 r 9999px shadow #232323 @ 0.1 0px 1px 2px 0px | button.hero-media-viewer_rightButton.hrt-icon-on-overlay 32.0x32.0 bg #000000 @ 0.25 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 9999px shadow #232323 @ 0.1 0px 1.99645px 5.98582px 0px | button.hero-media-viewer_rightButton.hrt-icon-on-overlay 32.0x32.0 bg #000000 @ 0.55 r 9999px shadow #232323 @ 0.1 0px 1px 2px 0px outline 1px auto #101010 offset 0px | button.hero-media-viewer_rightButton.hrt-icon-on-overlay 32.0x32.0 bg #000000 @ 0.255 border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 9999px shadow #232323 @ 0.1 0px 1.98476px 5.93903px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `f-media-nav-default.png`, `f-media-nav-hover.png`, `f-media-nav-focus-visible.png`, `f-media-nav-pressed.png`.

#### f-report

Report link. The "Report fundraiser" text-button; measured, never pressed.

Page: fundraiser. Selector: `Report fundraiser`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 171 x 40 | = | = | = |
| Padding | 2px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #232323 @ 0.05 | = | #232323 @ 0.098 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GoFundMe Sans 16px/20px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #232323, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.hrt-px-1.hrt-gap-half 171.0x40.0 bg #232323 @ 0.05 r 9999px | a.hrt-px-1.hrt-gap-half 171.0x40.0 r 9999px outline 1px auto #101010 offset 1px | a.hrt-px-1.hrt-gap-half 171.0x40.0 bg #232323 @ 0.098 r 9999px |

Crops: `f-report-default.png`, `f-report-hover.png`, `f-report-focus-visible.png`, `f-report-pressed.png`.

#### f-collection

Collection pill (page). The "Nearby"-style collection filter pill on the related-fundraisers rail; measured at rest, never toggled.

Page: fundraiser. Selector: `collection-selector button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 247 x 40 | = | = | = |
| Padding | 2px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 24px | = | = | = |
| Background | #000000 @ 0.1 | #fefefe @ 0.1 | = | #fdfdfd @ 0.2 |
| Box shadow | #ffffff 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMe Sans 16px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button.collection-selector_button.hrt-button 247.0x40.0 bg #000000 @ 0.1 r 24px shadow #ffffff 0px 0px 0px 1px inset | button.collection-selector_button.hrt-button 247.0x40.0 bg #fefefe @ 0.1 r 24px shadow #ffffff 0px 0px 0px 1px inset | button.collection-selector_button.hrt-button 247.0x40.0 bg #000000 @ 0.1 r 24px shadow #ffffff 0px 0px 0px 1px inset outline 1px auto #101010 offset 0px | button.collection-selector_button.hrt-button 247.0x40.0 bg #fdfdfd @ 0.2 r 24px shadow #ffffff 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `f-collection-default.png`, `f-collection-hover.png`, `f-collection-focus-visible.png`, `f-collection-pressed.png`.

#### f-donations-h2

Donations heading. The "Donations (N)" section heading above the supporter list.

Page: fundraiser. Selector: `h2 Donations`. States: .

Not found on the page at capture time.

### Pricing (content stack)

#### price-h1

Pricing headline. "Simple pricing, powerful fundraising" — the /c/pricing masthead on the WordPress content stack.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 890 x 180.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMeSans 82px/90.2px 700 |
| Letter spacing | -1.64px |
| Colour | #232323 |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### price-toggle

Audience toggle. An "Individual or business / Certified nonprofit" segment toggle on the fee section; measured at rest, never switched (switching would re-tab the fees).

Page: pricing. Selector: `input.toggle wrapper`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 772 x 65 | = | = | = |
| Padding | 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #d8d8d8; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | GoFundMeSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Text node | span: GoFundMeSans 24px/30px 700, #333333 | = | = | = |
| Transition | none | = | = | = |
| Icon | 32 x 32, colour #333333 | = | = | = |
| Painted layers | div.group 772.0x65.0 border B:1px #d8d8d8 | = | div.group 772.0x65.0 border B:1px #d8d8d8; input.toggle 13.0x13.0 outline 1px auto #101010 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `price-toggle-default.png`, `price-toggle-hover.png`, `price-toggle-focus-visible.png`, `price-toggle-pressed.png`.

#### price-faq

FAQ row. A CSS-disclosure FAQ row (checkbox + label) in the pricing FAQ; measured at rest, never opened.

Page: pricing. Selector: `faq checkbox row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 772 x 65 | = |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #d8d8d8; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | GoFundMeSans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #232323 | = |
| Text node | span: GoFundMeSans 24px/30px 700, #333333 | = |
| Transition | none | = |
| Icon | 32 x 32, colour #333333 | = |
| Painted layers | div.group 772.0x65.0 border B:1px #d8d8d8 | = |
| How | at rest | mouse hover |

Crops: `price-faq-default.png`, `price-faq-hover.png`.

#### wp-locale

Locale select (content stack). The WordPress language switcher in the content-stack footer; measured, never changed.

Page: pricing. Selector: `select.wp-language-switcher`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 238 x 35 | = | = | = |
| Padding | 0px 32px 0px 16px | = | = | = |
| Border | 1px solid #c0bdb8 | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Background image | url(data:…) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | GoFundMeSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | border-color 0.25s ease-in-out | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | select.wp-language-switcher.js-locale-select 238.0x35.0 bg #ffffff image url(data:…) border T:1px #c0bdb8 / R:1px #c0bdb8 / B:1px #c0bdb8 / L:1px #c0bdb8 r 12px | = | select.wp-language-switcher.js-locale-select 238.0x35.0 bg #ffffff image url(data:…) border T:1px #c0bdb8 / R:1px #c0bdb8 / B:1px #c0bdb8 / L:1px #c0bdb8 r 12px outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `wp-locale-default.png`, `wp-locale-hover.png`, `wp-locale-focus-visible.png`, `wp-locale-pressed.png`.

#### wp-button

Content CTA. A wp-block button on the content stack; measured, never followed.

Page: pricing. Selector: `wp-block-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 191 x 48 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ccf88e | #e9fcce | = | #e8fccd |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | GoFundMeSans 16px/20px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #274a34 | = | #026c3b | = |
| Transition | background-color, box-shadow, color, border-color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hrt-primary-button.hrt-primary-button--inline 191.0x48.0 bg #ccf88e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 9999px | a.hrt-primary-button.hrt-primary-button--inline 191.0x48.0 bg #e9fcce border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 9999px | a.hrt-primary-button.hrt-primary-button--inline 191.0x48.0 bg #ccf88e border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 9999px outline 1px auto #101010 offset 1px | a.hrt-primary-button.hrt-primary-button--inline 191.0x48.0 bg #e8fccd border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `wp-button-default.png`, `wp-button-hover.png`, `wp-button-focus-visible.png`, `wp-button-pressed.png`.

### Sign-in boundary

#### signin-shell

Sign-in card. The /sign-in document: the Welcome card a signed-out visitor gets — Google/Apple buttons, an email field and Continue. Never submitted.

Page: signin. Selector: `sign-in form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Transition | none |
| Icon | 1440 x 900, colour #232323, fill #000000 |
| Painted layers | body 1440.0x900.0 bg #ffffff; main.descope-layout_content 453.0x523.7 bg #ffffff r 50px shadow #232323 @ 0.1 0px 6px 14px 0px; div.grecaptcha-badge 0.0x0.0 shadow #808080 0px 0px 5px 0px; textarea.g-recaptcha-response 0.0x0.0 bg #ffffff border T:1px #c1c1c1 / R:1px #c1c1c1 / B:1px #c1c1c1 / L:1px #c1c1c1 |
| How | at rest |

Crops: `signin-shell-default.png`.

#### signin-email

Email field. The "Email Address" field on the sign-in card; focused, typed into and cleared — never submitted.

Page: signin. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 385 x 25.11 | = | = |
| Padding | 0px 7px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GoFundMeSans-Regular 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #333333 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #333333, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-email-default.png`, `signin-email-focused.png`, `signin-email-filled.png`.

#### signin-continue

Continue button. The sign-in card's primary "Continue" button; all four states measured with hover/focus/forced-active only — it was never clicked.

Page: signin. Selector: `Continue`. States: .

Not found on the page at capture time.

#### signin-google

Google button. The "Sign in with Google" button; measured at rest and on hover/focus, never pressed (a press would start OAuth).

Page: signin. Selector: `Sign in with Google`. States: .

Not found on the page at capture time.

### Start-a-fundraiser wizard

#### create-h1

Wizard headline. "Let's begin your fundraising journey" — the /create/fundraiser/category masthead, captured at rest before any step was submitted.

Page: create. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 377.59 x 246 |
| Padding | 158px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 40px/44px 100 |
| Letter spacing | -0.8px |
| Colour | #232323 |
| Transition | none |
| How | at rest |

Crops: `create-h1-default.png`.

#### create-country

Country select. The "Select your country" select; measured at rest, never changed (changing would re-price the currency).

Page: create. Selector: `select.hrt-select-field-select`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 245.19 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `create-country-default.png`, `create-country-hover.png`, `create-country-focus-visible.png`, `create-country-pressed.png`.

#### create-zip

Postcode field. The postcode text field; focused and typed into then cleared — the step was never submitted.

Page: create. Selector: `input.hrt-text-field-input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 269.2 x 24 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = |
| Letter spacing | normal | = | = |
| Colour | #232323 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #6f6f6f, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "94107", then deleted; nothing sent |

Crops: `create-zip-default.png`, `create-zip-focused.png`, `create-zip-filled.png`.

#### create-pill

Category pill. A category radio pill (Animals, Business, Community…); measured at rest, never selected — selecting would be a wizard choice.

Page: create. Selector: `select-pills label`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #b7b7b6 | = | = | = |
| Radius | 20px | = | = | = |
| Background | transparent | #274a34 @ 0.1 | = | #274a34 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232323 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | label.select-pills_selectPillsPill 90.0x42.0 border T:1px #b7b7b6 / R:1px #b7b7b6 / B:1px #b7b7b6 / L:1px #b7b7b6 r 20px | label.select-pills_selectPillsPill 90.0x42.0 bg #274a34 @ 0.1 border T:1px #b7b7b6 / R:1px #b7b7b6 / B:1px #b7b7b6 / L:1px #b7b7b6 r 20px | label.select-pills_selectPillsPill 90.0x42.0 border T:1px #b7b7b6 / R:1px #b7b7b6 / B:1px #b7b7b6 / L:1px #b7b7b6 r 20px; input.select-pills_selectPillsInputHidden 1.0x1.0 outline 1px auto #101010 offset 2px; div.select-pills_selectPillsPillOutline 88.0x40.0 r 20px outline 1px auto #101010 offset 0px | label.select-pills_selectPillsPill 90.0x42.0 bg #274a34 @ 0.1 border T:1px #b7b7b6 / R:1px #b7b7b6 / B:1px #b7b7b6 / L:1px #b7b7b6 r 20px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `create-pill-default.png`, `create-pill-hover.png`, `create-pill-focus-visible.png`, `create-pill-pressed.png`.

#### create-continue

Continue button. The wizard "Continue" button; states measured, never clicked — no wizard step was ever submitted.

Page: create. Selector: `Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150 x 56 | = | - | = |
| Padding | 2px 24px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | #274a34 | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 1440px inset | = | - | = |
| Outline | none | = | - | = |
| Font | GoFundMe Sans 16px/20px 175 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ccf88e | = | - | = |
| Text node | span: GoFundMe Sans 16px/20px 175, #ccf88e | = | - | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | - | = |
| Opacity | 0.4 | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.nav-footer_navFooterPrimaryButton.hrt-button 150.0x56.0 bg #274a34 r 9999px shadow #000000 @ 0 0px 0px 0px 1440px inset | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `create-continue-default.png`, `create-continue-hover.png`, `create-continue-pressed.png`.

#### create-signin

Wizard sign-in link. The "Sign in" link above the wizard; measured, never followed.

Page: create. Selector: `create Sign in`. States: .

Not found on the page at capture time.

### Mobile (390 wide)

#### m-header

Mobile header. The phone header at 390 wide: the mark, the menu toggle and the start CTA.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | span: GoFundMe Sans 16px/19.2px 100, #232323 |
| Transition | box-shadow, background-color 0.2s cubic-bezier(0.3, 0.01, 0, 1) |
| Icon | 24 x 24, colour #232323, fill #000000 |
| Painted layers | a.hrt-header-skip.hrt-show-on-focus 16.0x34.0 bg #ffffff r 9999px; div.hrt-header-dropdown-caret 0.0x0.0 border T:5px #232323 / R:4px #000000 @ 0 / L:4px #000000 @ 0; div.hrt-header-dropdown-content.hrt-header-dropdown-content--left 0.0x0.0 bg #ffffff r 8px shadow #232323 @ 0.1 0px 6px 14px 0px; div.hrt-spot-icon.hrt-spot-icon--neutral-subtle 0.0x0.0 bg #f5f5f5 r 9999px; a.hrt-base-list-item--body-size.hrt-base-list-item 0.0x0.0 bg #ffffff r 12px; a.hrt-base-list-item--body-size.hrt-base-list-item 0.0x0.0 bg #ffffff r 12px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-btn

Mobile menu button. The header nav toggle at 390 wide — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `mobile nav toggle`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | transparent | = | = | #232323 @ 0.1 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | GoFundMe Sans 16px/24px 100 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #232323 | = | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #232323, fill #000000 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Painted layers | - | = | button.hrt-icon-button.hrt-icon-button--hierarchy-tertiary 40.0x40.0 r 9999px outline 1px auto #e59700 offset 0px | button.hrt-icon-button.hrt-icon-button--hierarchy-tertiary 40.0x40.0 bg #232323 @ 0.1 r 9999px | = |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The nav overlay opened by the menu button; its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 16px/24px 100 |
| Letter spacing | normal |
| Colour | #232323 |
| Text node | span.hrt-base-list-item-title: GoFundMe Sans 20px/22px 100, #232323, ls -0.2px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 24 x 24, colour #232323, fill #000000 |
| Painted layers | div.hrt-rounded-0.hrt-side-modal 330.0x844.0 bg #ffffff shadow #232323 @ 0.1 0px 6px 14px 0px; div.hrt-modal-header 330.0x56.0 bg #ffffff; div.hrt-modal-body 330.0x594.0 border T:1px #000000 @ 0 / B:1px #000000 @ 0; a.hrt-base-list-item--heading-size.hrt-base-list-item 282.0x96.0 bg #ffffff r 12px; button.hrt-base-list-item--heading-size.hrt-base-list-item 282.0x96.0 bg #ffffff r 12px; button.hrt-base-list-item--heading-size.hrt-base-list-item 282.0x96.0 bg #ffffff r 12px |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 330 x 88.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | GoFundMe Sans 40.338px/44.3718px 175 |
| Letter spacing | -0.806761px |
| Colour | #232323 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero "Start a GoFundMe" button at 390 wide; measured never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 190 x 56 | = | = | = |
| Padding | 2px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #274a34 | = | = | #2d6339 |
| Box shadow | #000000 @ 0 0px 0px 0px 844px inset | = | = | #357d3a @ 0.247 0px 0px 0px 844px inset |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | GoFundMe Sans 16px/20px 175 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ccf88e | = | = | = |
| Text node | span: GoFundMe Sans 16px/20px 175, #ccf88e | = | = | = |
| Transition | background-color, box-shadow, color, opacity, transform 0.5s cubic-bezier(0.3, 0.01, 0, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hrt-button.hrt-button--hierarchy-primary 190.0x56.0 bg #274a34 r 9999px shadow #000000 @ 0 0px 0px 0px 844px inset | = | a.hrt-button.hrt-button--hierarchy-primary 190.0x56.0 bg #274a34 r 9999px shadow #000000 @ 0 0px 0px 0px 844px inset outline 1px auto #e59700 offset 1px | a.hrt-button.hrt-button--hierarchy-primary 190.0x56.0 bg #2d6339 r 9999px shadow #357d3a @ 0.247 0px 0px 0px 844px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

www.gofundme.com is a Next.js app: its CSS arrives as linked /ssr/_next/static/css/*.css bundles plus inline <style> blocks, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- home: `grid-template-rows var(--hrt-time-transition-fast) var(--hrt-ease-default)`, `none`, `transform var(--hrt-time-transition-fast) var(--hrt-ease-default)`, `height var(--hrt-time-transition) var(--hrt-ease-default)`, `color var(--hrt-time-transition) var(--hrt-ease-default)`, `transform .25s var(--hrt-ease-default)`, `opacity 0.15s`, `transform 0.2s ease-in-out`, `0.1s ease-in-out`, `all var(--hrt-time-transition) var(--hrt-ease-default)`, `width 0.66s`, `box-shadow var(--hrt-time-transition) var(--hrt-ease-default)`

## Reduced motion

- home (`header a, .hrt-header a` under prefers-reduced-motion): transition `background-color 0.001s cubic-bezier(0.3, 0.01, 0, 1), box-shadow 0.001s cubic-bezier(0.3, 0.01, 0, 1), color 0.001s cubic-bezier(0.3, 0.01, 0, 1), opacity 0.001s cubic-bezier(0.3, 0.01, 0, 1), transform 0.001s cubic-bezier(0.3, 0.01, 0, 1)`, animation `0.001s ease 0s 1 normal none running none`, html scroll-behavior `auto`
