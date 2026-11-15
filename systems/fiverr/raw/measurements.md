# Fiverr component measurements

Computed styles read from fiverr.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's public surfaces — the home page and its categories drawer, the /categories directory, a subcategory hub, /search/gigs results, a gig page and its seller profile (the first live gig card's own links), /join and /login, /logo-maker, /about-us, /start_selling and /cp/how-fiverr-works — with the UserWay widget and any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). fiverr.com declares no :root custom properties, so every value is a measured computed style; the single light theme is the only theme painted (the hero search form's `dark` class is a component skin). PerimeterX's press&hold was driven automatically, never answered by hand. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The sticky top bar on every public page: the Fiverr wordmark, the Sidebar-menu hamburger, "Connect to your AI", the EN locale button, Become a Seller, Sign in and the green Join pill.

Page: home. Selector: `.main-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 86 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #62646a |
| Text node | div._ifhvih._xwb3qf: Macan 16px/24px 600, #222325 |
| Transition | none |
| Icon | 0 x 0, colour #222325 |
| Painted layers | div.search-bar-dim-background 1425.0x0.0 bg #000000; header._188cbt6._bbx8bt 1425.0x86.0 bg #ffffff border B:1px solid #dadbdd; button._arosdn._1xeo152 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; input.long-placeholder 436.2x42.0 bg #ffffff border T:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 4px 0px 0px 4px; input.short-placeholder 0.0x0.0 bg #ffffff border T:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 4px 0px 0px 4px; button._arosdn._1xeo152 50.0x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 0px 4px 4px 0px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Fiverr wordmark in the header, linking home.

Page: home. Selector: `main-header home link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 90 x 35 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #222325 |
| Transition | color 0.2s ease |
| Cursor | pointer |
| Icon | 90 x 28, colour #222325 |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### sidebar-btn

Sidebar menu button. The header hamburger that opens the Browse-categories drawer — a local UI toggle; the opened state was measured after its own click.

Page: home. Selector: `button Sidebar menu`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 0 x 0 | - | = | = | = |
| Padding | 0px | - | = | = | = |
| Gap | 8px | - | = | = | = |
| Border | 1px solid #000000 @ 0 | - | = | = | = |
| Radius | 8px | - | = | = | = |
| Background | transparent | - | = | #efeff0 | = |
| Box shadow | none | - | = | = | = |
| Outline | none | - | = | = | = |
| Font | Macan 16px/24px 600 | - | = | = | = |
| Letter spacing | normal | - | = | = | = |
| Colour | #222325 | - | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | - | = | = | = |
| Cursor | pointer | - | = | = | = |
| Icon | 0 x 0, colour #222325 | - | = | = | = |
| Painted layers | button._arosdn._1xeo152 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | - | = | button._arosdn._1xeo152 0.0x0.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = |
| How | at rest | - | focus failed | CDP forcePseudoState :active:hover | own toggle |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('button[aria-label*="idebar" i], button:has-text("Sidebar menu")').first().first().first()     - locator resolved to <button rol | = | = | = |

Crops: none.

#### nav-ai

Connect to your AI button. The header "Connect to your AI" button (the Fiverr AI-assistant entry); measured, never pressed.

Page: home. Selector: `button Connect to your AI`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 242.91 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f5f5 | = | #efeff0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Text node | div._ifhvih._xwb3qf: Macan 16px/24px 600, #222325 | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222325 | = | = | = |
| Painted layers | button._arosdn._1xeo152 242.9x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button._arosdn._1xeo152 242.9x42.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button._arosdn._1xeo152 242.9x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #222325 offset 1px | button._arosdn._1xeo152 242.9x42.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-ai-default.png`, `nav-ai-hover.png`, `nav-ai-focus-visible.png`, `nav-ai-pressed.png`.

#### nav-locale

Locale button. The "EN" header button — a local UI toggle for the language list; measured, never toggled.

Page: home. Selector: `button EN`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.91 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f5f5 | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Text node | span.label: Macan 16px/24px 600, #222325 | = | = | = |
| Transition | background 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #222325 | = | = | = |
| Painted layers | button.selection-trigger.language-selection-trigger 79.9x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.selection-trigger.language-selection-trigger 79.9x42.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | button.selection-trigger.language-selection-trigger 79.9x42.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-locale-default.png`, `nav-locale-hover.png`, `nav-locale-focus-visible.png`, `nav-locale-pressed.png`.

#### nav-seller

Become a Seller link. The header "Become a Seller" link to /start_selling; measured, never followed.

Page: home. Selector: `a Become a Seller`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 159 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f5f5 | = | #efeff0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a._arosdn._1xeo152 159.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a._arosdn._1xeo152 159.0x42.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a._arosdn._1xeo152 159.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #222325 offset 1px | a._arosdn._1xeo152 159.0x42.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-seller-default.png`, `nav-seller-hover.png`, `nav-seller-focus-visible.png`, `nav-seller-pressed.png`.

#### nav-signin

Sign in link. The header "Sign in" link to /login; measured, never followed.

Page: home. Selector: `a Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.02 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #f5f5f5 | = | #efeff0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a._arosdn._1xeo152 85.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a._arosdn._1xeo152 85.0x42.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a._arosdn._1xeo152 85.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #222325 offset 1px | a._arosdn._1xeo152 85.0x42.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-join

Join CTA. The green "Join" header pill to /join — the primary header action; measured, never followed.

Page: home. Selector: `a Join`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #222325 | #404145 | = | #62646a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a._arosdn._1xeo152 88.0x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a._arosdn._1xeo152 88.0x42.0 bg #404145 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | a._arosdn._1xeo152 88.0x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #222325 offset 1px | a._arosdn._1xeo152 88.0x42.0 bg #62646a border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-join-default.png`, `nav-join-hover.png`, `nav-join-focus-visible.png`, `nav-join-pressed.png`.

#### cat-nav

Category nav link. A category-strip link under the header (Trending, Graphics & Design, Programming & Tech, …); measured, never followed.

Page: home. Selector: `a Graphics & Design`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 142.39 x 40 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Macan 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #62646a | #74767e | = | #74767e |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | 142.391px x 3px, absolute, bg #1dbf73, radius 0px | = | = |
| Painted layers | - | a::after 142.391pxx3px bg #1dbf73 | = | = |

Crops: `cat-nav-default.png`, `cat-nav-hover.png`, `cat-nav-focus-visible.png`, `cat-nav-pressed.png`.

#### drawer

Categories drawer. The "Browse categories" drawer the Sidebar-menu hamburger slides in from the left: category tree links, English/currency buttons, Join Fiverr and Sign in. Its links were never followed.

Page: home. Selector: `article Browse categories`. States: .

Not found on the page at capture time.

#### drawer-item

Drawer category link. A category link inside the open drawer; measured, never followed.

Page: home. Selector: `drawer category link`. States: .

Not found on the page at capture time.

#### drawer-join

Drawer Join button. The "Join Fiverr" button at the drawer's foot; measured, never pressed.

Page: home. Selector: `drawer Join Fiverr`. States: .

Not found on the page at capture time.

### Home

#### hero-h1

Hero headline. "Our freelancers will take it from here" — the home hero display heading over the dark hero band.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 612.58 x 172.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 72px/86.4px 280 |
| Letter spacing | -4.32px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-search

Hero search form. The hero search field — the `dark`-skinned pill inside the light page: an input plus its green submit button.

Page: home. Selector: `form.search-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 486.17 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #62646a |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | input.long-placeholder 436.2x42.0 bg #ffffff border T:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 4px 0px 0px 4px; input.short-placeholder 0.0x0.0 bg #ffffff border T:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 4px 0px 0px 4px; button._arosdn._1xeo152 50.0x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 0px 4px 4px 0px |
| How | at rest |

Crops: `hero-search-default.png`.

#### hero-search-input

Hero search field. The "Search for any service" input inside the dark search form; focused and typed into then cleared — never searched.

Page: home. Selector: `search-form input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 436.17 x 42 | = | = |
| Padding | 10px 2px 10px 16px | = | = |
| Border | T: 1px solid #c5c6c9; R: none; B: 1px solid #c5c6c9; L: 1px solid #c5c6c9 | = | = |
| Radius | 4px 0px 0px 4px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Macan 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #62646a | = | = |
| Transition | all 0.15s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #95979d, opacity 1 | = | = |
| Painted layers | input.long-placeholder 436.2x42.0 bg #ffffff border T:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 4px 0px 0px 4px | = | = |
| How | at rest | clicked into the field | typed "logo design", then deleted; nothing sent |

Crops: `hero-search-input-default.png`, `hero-search-input-focused.png`, `hero-search-input-filled.png`.

#### hero-search-btn

Search submit. The green search submit button inside the hero form; its states were measured but it was never clicked — nothing was searched.

Page: home. Selector: `search-form submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #222325 | #404145 | = | #404145 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Macan 14px/14px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | = |
| Painted layers | button.ec83942.b520005 48.0x48.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button.ec83942.b520005 48.0x48.0 bg #404145 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | button.ec83942.b520005 48.0x48.0 bg #404145 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-search-btn-default.png`, `hero-search-btn-hover.png`, `hero-search-btn-focus-visible.png`, `hero-search-btn-pressed.png`.

#### popular-chip

Popular-service chip. A "Popular services" pill under the hero (Website Development, Logo Design, …); measured, never followed.

Page: home. Selector: `popular service chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 232.72 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #ffffff | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff @ 0.1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | p._1koqg34k._1oslsch1j: Macan 16px/24px 400, #ffffff | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.91 x 16, colour #ffffff | = | = | = |
| Painted layers | a._1koqg34r._12ky2ni5 232.7x42.0 bg #ffffff @ 0.1 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 8px | = | a._1koqg34r._12ky2ni5 232.7x42.0 bg #ffffff @ 0.1 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 8px outline 2px solid #ffffff offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `popular-chip-default.png`, `popular-chip-hover.png`, `popular-chip-focus-visible.png`, `popular-chip-pressed.png`.

#### cat-card

Category card. A service-category card tile further down the home page; measured, never followed.

Page: home. Selector: `category card link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 138.3 x 14 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Macan 14px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #222325 | = |
| Transition | color 0.2s ease | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `cat-card-default.png`, `cat-card-hover.png`.

#### section-h2

Section heading. A marketing section heading ("Make it all happen with freelancers", …).

Page: home. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 50.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 48px/50.4px 400 |
| Letter spacing | -1.44px |
| Colour | #404145 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### trust-badge

Rating badge. A star-rating badge on the page (seller ratings, reviews strip); recorded missing when none renders.

Page: home. Selector: `rating badge`. States: .

Not found on the page at capture time.

### Footer

#### footer

Footer. The page footer: category sitemap columns, company links, social icons and the language/currency buttons.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 91 |
| Padding | 24px |
| Border | T: 1px solid #dadbdd; R: none; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #62646a |
| Text node | button._arosdn._1xeo152: Macan 16px/24px 600, #ffffff |
| Transition | none |
| Painted layers | footer._188cbt6._16b5yd0 480.0x91.0 border T:1px solid #dadbdd; button._arosdn._1xeo152 210.0x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button._arosdn._1xeo152 210.0x42.0 border T:1px solid #222325 / R:1px solid #222325 / B:1px solid #222325 / L:1px solid #222325 r 8px |
| Ancestor paint | 1 up article._8wb4qe._bbx8bt bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a Careers`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53.23 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 14px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._ifhvih._tgicbx 53.2x14.0 outline 2px solid #222325 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-locale

Footer locale button. The "English" button in the footer — a local UI toggle for the locale list; measured, never toggled.

Page: home. Selector: `footer button English`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.73 x 36 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #fafafa | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #74767e offset 1px | = |
| Font | Macan 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #74767e | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #74767e | = | = | = |
| Painted layers | button._arosdn._1xeo152 97.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button._arosdn._1xeo152 97.7x36.0 bg #fafafa border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button._arosdn._1xeo152 97.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #74767e offset 1px | button._arosdn._1xeo152 97.7x36.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-locale-default.png`, `footer-locale-hover.png`, `footer-locale-focus-visible.png`, `footer-locale-pressed.png`.

#### footer-currency

Currency button. The currency button in the footer ("S$ SGD" for this client — prices localize); measured, never toggled.

Page: home. Selector: `footer currency button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.91 x 36 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | #fafafa | = | #f5f5f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #74767e offset 1px | = |
| Font | Macan 14px/22px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #74767e | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button._arosdn._1xeo152 76.9x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button._arosdn._1xeo152 76.9x36.0 bg #fafafa border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button._arosdn._1xeo152 76.9x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #74767e offset 1px | button._arosdn._1xeo152 76.9x36.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-currency-default.png`, `footer-currency-hover.png`, `footer-currency-focus-visible.png`, `footer-currency-pressed.png`.

## Transitions declared in the readable stylesheets

fiverr.com serves its CSS as linked atomic-class bundles plus inline `<style>` blocks; this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- home: `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`
