# Fiverr component measurements

Computed styles read from fiverr.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's public surfaces — the home page and its categories drawer, the /categories directory, a subcategory hub, /search/gigs results, a gig page and its seller profile (the first live gig card's own links), /join and /login, /logo-maker, /about-us, /start_selling and /cp/how-fiverr-works — with the UserWay widget and any consent layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). fiverr.com's :root carries ~1,290 custom properties all named by content hash — a token-free layer with no semantic names to alias — so every value is a measured computed style; the single light theme is the only theme painted (the hero search form's `dark` class is a component skin). PerimeterX's press&hold was driven automatically, never answered by hand. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

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
| Size (w x h) | 0 x 0 | - | - | = | = |
| Padding | 0px | - | - | = | = |
| Gap | 8px | - | - | = | = |
| Border | 1px solid #000000 @ 0 | - | - | = | = |
| Radius | 8px | - | - | = | = |
| Background | transparent | - | - | #efeff0 | = |
| Box shadow | none | - | - | = | = |
| Outline | none | - | - | = | = |
| Font | Macan 16px/24px 600 | - | - | = | = |
| Letter spacing | normal | - | - | = | = |
| Colour | #222325 | - | - | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | - | - | = | = |
| Cursor | pointer | - | - | = | = |
| Icon | 0 x 0, colour #222325 | - | - | = | = |
| Painted layers | button._arosdn._1xeo152 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | - | - | button._arosdn._1xeo152 0.0x0.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = |
| How | at rest | - | - | CDP forcePseudoState :active:hover | own toggle |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('button[aria-label*="idebar" i], button:has-text("Sidebar menu")').first().first().first()     - locator resolved to <button rol | = | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: none.

#### nav-ai

Connect to your AI button. The header "Connect to your AI" button (the Fiverr AI-assistant entry); measured, never pressed.

Page: home. Selector: `button Connect to your AI`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 242.91 x 42 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | #efeff0 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 16px/24px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222325 | = | - | = |
| Text node | div._ifhvih._xwb3qf: Macan 16px/24px 600, #222325 | = | - | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 20 x 20, colour #222325 | = | - | = |
| Painted layers | button._arosdn._1xeo152 242.9x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | - | button._arosdn._1xeo152 242.9x42.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-ai-default.png`, `nav-ai-hover.png`, `nav-ai-pressed.png`.

#### nav-locale

Locale button. The "EN" header button — a local UI toggle for the language list; measured, never toggled.

Page: home. Selector: `button EN`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 79.91 x 42 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | #f5f5f5 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 16px/24px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222325 | = | - | = |
| Text node | span.label: Macan 16px/24px 600, #222325 | = | - | = |
| Transition | background 0.1s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #222325 | = | - | = |
| Painted layers | button.selection-trigger.language-selection-trigger 79.9x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | - | button.selection-trigger.language-selection-trigger 79.9x42.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-locale-default.png`, `nav-locale-hover.png`, `nav-locale-pressed.png`.

#### nav-seller

Become a Seller link. The header "Become a Seller" link to /start_selling; measured, never followed.

Page: home. Selector: `a Become a Seller`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 159 x 42 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | #efeff0 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 16px/24px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222325 | = | - | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a._arosdn._1xeo152 159.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | - | a._arosdn._1xeo152 159.0x42.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-seller-default.png`, `nav-seller-hover.png`, `nav-seller-pressed.png`.

#### nav-signin

Sign in link. The header "Sign in" link to /login; measured, never followed.

Page: home. Selector: `a Sign in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.02 x 42 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | #efeff0 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 16px/24px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222325 | = | - | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a._arosdn._1xeo152 85.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | - | a._arosdn._1xeo152 85.0x42.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-pressed.png`.

#### nav-join

Join CTA. The green "Join" header pill to /join — the primary header action; measured, never followed.

Page: home. Selector: `a Join`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88 x 42 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | #222325 | = | - | #62646a |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 16px/24px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a._arosdn._1xeo152 88.0x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | - | a._arosdn._1xeo152 88.0x42.0 bg #62646a border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-join-default.png`, `nav-join-hover.png`, `nav-join-pressed.png`.

#### cat-nav

Category nav link. A category-strip link under the header (Trending, Graphics & Design, Programming & Tech, …); measured, never followed.

Page: home. Selector: `a Graphics & Design`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 142.39 x 0 | 142.39 x 40 | - | = |
| Padding | 8px 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #62646a | #74767e | - | #74767e |
| Transition | color 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| ::after | - | 142.391px x 3px, absolute, bg #1dbf73, radius 0px | = | = |
| Painted layers | - | a::after 142.391pxx3px bg #1dbf73 | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `cat-nav-default.png`, `cat-nav-hover.png`, `cat-nav-pressed.png`.

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

Hero search form. The hero search field — the `dark`-skinned pill inside the light page: an input plus its submit button.

Page: home. Selector: `hero form.search-form (the header search excluded)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1159.94 x 60 |
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
| Icon | 18 x 18, colour #ffffff |
| Painted layers | input.long-placeholder.vvvkay0 1159.9x60.0 bg #ffffff border T:1px solid #c5c6c9 / R:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 12px; input.short-placeholder.vvvkay0 0.0x0.0 bg #ffffff border T:1px solid #c5c6c9 / R:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 12px; button.ec83942.b520005 48.0x48.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest |

Crops: `hero-search-default.png`.

#### hero-search-input

Hero search field. The "Search for any service" input inside the dark search form; focused and typed into then cleared — never searched.

Page: home. Selector: `hero search-form input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 1159.94 x 60 | = | = |
| Padding | 10px 58px 10px 16px | = | = |
| Border | 1px solid #c5c6c9 | = | = |
| Radius | 12px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Macan 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #62646a | = | = |
| Transition | all 0.15s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #95979d, opacity 0.916729 | #95979d, opacity 1 | #95979d, opacity 1 |
| Painted layers | input.long-placeholder.vvvkay0 1159.9x60.0 bg #ffffff border T:1px solid #c5c6c9 / R:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 12px | = | = |
| How | at rest | clicked into the field | typed "logo design", then deleted; nothing sent |

Crops: `hero-search-input-default.png`, `hero-search-input-focused.png`, `hero-search-input-filled.png`.

#### hero-search-btn

Search submit. The search submit button inside the hero form; its states were measured but it was never clicked — nothing was searched.

Page: home. Selector: `hero search-form submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | #222325 | = | - | #404145 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 14px/14px 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 18 x 18, colour #ffffff | = | - | = |
| Painted layers | button.ec83942.b520005 48.0x48.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | - | button.ec83942.b520005 48.0x48.0 bg #404145 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `hero-search-btn-default.png`, `hero-search-btn-hover.png`, `hero-search-btn-pressed.png`.

#### popular-chip

Popular-service chip. A "Popular services" pill under the hero (Website Development, Logo Design, …); measured, never followed.

Page: home. Selector: `popular service chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 232.72 x 42 | = | - | = |
| Padding | 8px 16px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #ffffff | = | - | = |
| Radius | 8px | = | - | = |
| Background | #ffffff @ 0.1 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 16px/24px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | p._1koqg34k._1oslsch1j: Macan 16px/24px 400, #ffffff | = | - | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 13.91 x 16, colour #ffffff | = | - | = |
| Painted layers | a._1koqg34r._12ky2ni5 232.7x42.0 bg #ffffff @ 0.1 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 8px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `popular-chip-default.png`, `popular-chip-hover.png`, `popular-chip-pressed.png`.

#### cat-card

Category card. A service-category card tile further down the home page; measured, never followed.

Page: home. Selector: `category card tile`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 129 x 129 | = |
| Padding | 16px 12px | = |
| Gap | 0px | = |
| Border | 1px solid #ffffff | = |
| Radius | 16px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0.027 0px 0px 0.880517px 0px, #000000 @ 0.03 0px 0px 2.29197px 0px, #000000 @ 0.055 0px 0px 5.52px 0px, #000000 @ 0.09 0px 0px 11px 0px | = |
| Outline | none | = |
| Font | Macan 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #222325 | = |
| Text node | p._1koqg34k._1oslsch16: Macan 14px/22px 600, #222325 | = |
| Transition | color 0.2s ease | = |
| Cursor | pointer | = |
| ::before | 127px x 127px, absolute, bg #ffffff radial-gradient(63.44% 63.44%, #c2ffe2 0%, #ffffff 100%), none, radius 16px | = |
| Painted layers | a._1j14nt12 129.0x129.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 16px shadow #000000 @ 0.027 0px 0px 0.880517px 0px, #000000 @ 0.03 0px 0px 2.29197px 0px, #000000 @ 0.055 0px 0px 5.52px 0px, #000000 @ 0.09 0px 0px 11px 0px; a::before._1j14nt12 127pxx127px bg #ffffff image radial-gradient(63.44% 63.44%, #c2ffe2 0%, #ffffff 100%), none r 16px | = |
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

Page: home. Selector: `the on-screen page footer (the drawer's off-screen footer excluded)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 751 |
| Padding | 0px |
| Border | 1px solid #dadbdd |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #62646a |
| Text node | p._ifhvih._zbphw9: Macan 16px/24px 600, #222325 |
| Transition | none |
| Icon | 90 x 28, colour #62646a |
| Painted layers | footer._188cbt6._8wb4qe 1425.0x751.0 bg #ffffff border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd; div._188cbt6._r1o28d 1336.0x53.0 border T:1px solid #dadbdd; a._arosdn._1xeo152 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a._arosdn._1xeo152 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a._arosdn._1xeo152 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; a._arosdn._1xeo152 36.0x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer sitemap link; measured, never followed.

Page: home. Selector: `footer a Careers`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53.23 x 14 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 14px/22px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #222325 | = | - | = |
| Transition | color 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-pressed.png`.

#### footer-locale

Footer locale button. The "English" button in the footer — a local UI toggle for the locale list; measured, never toggled.

Page: home. Selector: `footer button English`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97.73 x 36 | = | - | = |
| Padding | 6px 12px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | #f5f5f5 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 14px/22px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #74767e | = | - | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #74767e | = | - | = |
| Painted layers | button._arosdn._1xeo152 97.7x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | - | button._arosdn._1xeo152 97.7x36.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `footer-locale-default.png`, `footer-locale-hover.png`, `footer-locale-pressed.png`.

#### footer-currency

Currency button. The currency button in the footer ("S$ SGD" for this client — prices localize); measured, never toggled.

Page: home. Selector: `footer currency button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.91 x 36 | = | - | = |
| Padding | 6px 12px | = | - | = |
| Gap | 8px | = | - | = |
| Border | 1px solid #000000 @ 0 | = | - | = |
| Radius | 8px | = | - | = |
| Background | transparent | = | - | #f5f5f5 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Macan 14px/22px 600 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #74767e | = | - | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | button._arosdn._1xeo152 76.9x36.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | - | button._arosdn._1xeo152 76.9x36.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `footer-currency-default.png`, `footer-currency-hover.png`, `footer-currency-pressed.png`.

### Categories and directory

#### dir-h2

Directory heading. "Fiverr Gigs® Directory" — the /categories services-directory masthead.

Page: categories. Selector: `directory heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 988 x 48.41 |
| Padding | 0px 0px 10px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 32px/38.4px 700 |
| Letter spacing | normal |
| Colour | #404145 |
| Transition | none |
| How | at rest |

Crops: `dir-h2-default.png`.

#### dir-cat-link

Directory category link. A top-category link in the services directory; measured, never followed.

Page: categories. Selector: `directory Graphics & Design`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 124.59 x 14 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Macan 14px/22px 400 | = |
| Letter spacing | normal | = |
| Colour | #222325 | = |
| Transition | none | color 0.2s ease |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `dir-cat-link-default.png`, `dir-cat-link-hover.png`.

#### dir-sub-link

Directory subcategory link. A subcategory link nested under a top category in the directory; measured, never followed.

Page: categories. Selector: `directory subcategory link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.72 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Macan 14px/28px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #555555 | #1dbf73 | = | #1dbf73 |
| Transition | none | color 0.2s ease | = | color 0.2s ease |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dir-sub-link-default.png`, `dir-sub-link-hover.png`, `dir-sub-link-focus-visible.png`, `dir-sub-link-pressed.png`.

#### sub-h1

Subcategory heading. The subcategory masthead on /categories/graphics-design/creative-logo-design.

Page: subcategory. Selector: `subcategory h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1336 x 52 |
| Padding | 8px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 32px/36px 700 |
| Letter spacing | normal |
| Colour | #222325 |
| Transition | none |
| How | at rest |

Crops: `sub-h1-default.png`.

#### breadcrumb

Breadcrumb link. The category breadcrumb link back up the tree; measured, never followed.

Page: subcategory. Selector: `breadcrumb Graphics & Design`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 142.39 x 40 | = |
| Padding | 8px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Macan 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #62646a | #74767e |
| Transition | color 0.2s ease | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| ::after | - | 142.391px x 3px, absolute, bg #1dbf73, radius 0px |
| Painted layers | - | a::after 142.391pxx3px bg #1dbf73 |

Crops: `breadcrumb-default.png`, `breadcrumb-hover.png`.

#### related-chip

Related-search chip. A related-search/style chip row on the subcategory page; measured, never followed.

Page: subcategory. Selector: `subcategory related chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185.23 x 80 | = | = | = |
| Padding | 12px | = | = | = |
| Border | 1px solid #e4e5e7 | 1px solid #222325 | = | 1px solid #222325 |
| Radius | 40px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Text node | span.chip-tile-text.tbody-5: Macan 16px/24px 600, #222325 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.filter-tile.chip-tile 185.2x80.0 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 40px; div.chip-tile-icon-wrapper 56.0x56.0 bg #f5f5f5 r 50% | button.filter-tile.chip-tile 185.2x80.0 border T:1px solid #222325 / R:1px solid #222325 / B:1px solid #222325 / L:1px solid #222325 r 40px; div.chip-tile-icon-wrapper 56.0x56.0 bg #f5f5f5 r 50% | = | button.filter-tile.chip-tile 185.2x80.0 border T:1px solid #222325 / R:1px solid #222325 / B:1px solid #222325 / L:1px solid #222325 r 40px; div.chip-tile-icon-wrapper 56.0x56.0 bg #f5f5f5 r 50% |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `related-chip-default.png`, `related-chip-hover.png`, `related-chip-focus-visible.png`, `related-chip-pressed.png`.

### Search results

#### search-h1

Results headline. "Results for logo design" — the search-results masthead.

Page: search. Selector: `search h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 308.19 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 28px/36px 400 |
| Letter spacing | normal |
| Colour | #222325 |
| Transition | none |
| How | at rest |

Crops: `search-h1-default.png`.

#### filter-btn

Filter button. A results-filter dropdown trigger (Category, Service Options, Seller Details, Budget, Delivery Time) — a local UI toggle; the opened state was measured after its own click, then closed.

Page: search. Selector: `filter dropdown button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 132.86 x 48 | = | = | = | = |
| Padding | 10px 20px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 1px solid #dadbdd | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #f5f5f5 | = | #efeff0 | #f5f5f5 |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = | = |
| Font | Macan 16px/26px 600 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #222325 | = | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 12 x 12, colour #222325 | = | = | = | = |
| Painted layers | button.nxfpcer._17nvinu5 132.9x48.0 border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd r 8px | button.nxfpcer._17nvinu5 132.9x48.0 bg #f5f5f5 border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd r 8px | button.nxfpcer._17nvinu5 132.9x48.0 border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd r 8px outline 2px solid #222325 offset 1px | button.nxfpcer._17nvinu5 132.9x48.0 bg #efeff0 border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd r 8px | button.nxfpcer._17nvinu5 132.9x48.0 bg #f5f5f5 border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `filter-btn-default.png`, `filter-btn-hover.png`, `filter-btn-focus-visible.png`, `filter-btn-pressed.png`, `filter-btn-opened.png`.

#### sort-btn

Sort control. The "Sort by" results control; measured at rest, never toggled.

Page: search. Selector: `sort control`. States: .

Not found on the page at capture time.

#### gig-card

Gig card. A gig listing card (thumbnail, seller name, rating, starting price, collect heart); measured, never followed.

Page: search. Selector: `gig result card`. States: .

Not found on the page at capture time.

#### gig-heart

Collect button. A gig card's heart/collect button; measured, never pressed (a collect would write to an account).

Page: search. Selector: `collect button`. States: .

Not found on the page at capture time.

#### gig-price

Card price. The "From S$xx" starting price on a gig card — localized to this client's currency (SGD).

Page: search. Selector: `gig card price`. States: .

Not found on the page at capture time.

#### seller-badge

Seller badge. A seller-level badge on a gig card (Top Rated, Level 2, …); recorded at rest.

Page: search. Selector: `seller level badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 85.66 x 18 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 14px/18px 600 |
| Letter spacing | normal |
| Colour | #222325 |
| Text node | p._15macpw2: Macan 14px/18px 600, #222325 |
| Transition | none |
| Icon | 10 x 10, colour #222325 |
| How | at rest |

Crops: `seller-badge-default.png`.

### Gig page

#### gig-h1

Gig headline. The gig page's "I will …" title.

Page: gig. Selector: `gig h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 712 x 52 |
| Padding | 0px 0px 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 28px/36px 700 |
| Letter spacing | normal |
| Colour | #222325 |
| Transition | none |
| Ancestor paint | 1 up div.gig-overview bg #ffffff |
| How | at rest |

Crops: `gig-h1-default.png`.

#### gig-breadcrumb

Gig breadcrumb. The category breadcrumb on the gig page; measured, never followed.

Page: gig. Selector: `gig breadcrumb`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 142.39 x 40 | = |
| Padding | 8px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Macan 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #62646a | #74767e |
| Transition | color 0.2s ease | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| ::after | - | 142.391px x 3px, absolute, bg #1dbf73, radius 0px |
| Painted layers | - | a::after 142.391pxx3px bg #1dbf73 |

Crops: `gig-breadcrumb-default.png`, `gig-breadcrumb-hover.png`.

#### pkg-tablist

Package tabs. The Basic/Standard/Premium package tablist on the pricing card.

Page: gig. Selector: `package tablist`. States: .

Not found on the page at capture time.

#### pkg-tab-on

Selected package tab. The selected package tab (Basic) in the pricing card.

Page: gig. Selector: `selected package tab`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 137.84 x 59 |
| Padding | 16px |
| Border | T: none; R: 1px solid #dadbdd; B: 3px solid #222325; L: none |
| Radius | 8px 0px 0px 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 700 |
| Letter spacing | normal |
| Colour | #222325 |
| Transition | none |
| Cursor | pointer |
| Painted layers | label.new-pro-layout 137.8x59.0 bg #ffffff border R:1px solid #dadbdd / B:3px solid #222325 r 8px 0px 0px |
| How | at rest |

Crops: `pkg-tab-on-default.png`.

#### pkg-tab

Package tab. An unselected package tab (Standard/Premium) in the pricing card; measured at rest, never switched (switching re-prices the card).

Page: gig. Selector: `package tab`. States: .

Not found on the page at capture time.

#### pkg-price

Package price. The selected package's price on the pricing card — localized (SGD for this client).

Page: gig. Selector: `package price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 94.47 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 20px/24px 400 |
| Letter spacing | normal |
| Colour | #222325 |
| Transition | none |
| How | at rest |

Crops: `pkg-price-default.png`.

#### gig-continue

Continue button. The pricing card's green "Continue" button; its states were measured but it was never pressed — it leads to checkout.

Page: gig. Selector: `gig Continue`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 364.55 x 42 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #000000 | #404145 | = | #222325 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Macan 16px/16px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button._05cff4._363b2e 364.5x42.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | button._05cff4._363b2e 364.5x42.0 bg #404145 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | = | button._05cff4._363b2e 364.5x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gig-continue-default.png`, `gig-continue-hover.png`, `gig-continue-focus-visible.png`, `gig-continue-pressed.png`.

#### gig-contact

Contact me button. The "Contact me" button beside Continue; measured, never pressed (it fronts a sign-in wall).

Page: gig. Selector: `gig Contact me`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 364.55 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e4e5e7 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #f5f5f5 | = | #efeff0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button._1fe1trbr._1n2vpki5 364.5x42.0 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 4px | button._1fe1trbr._1n2vpki5 364.5x42.0 bg #f5f5f5 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 4px | button._1fe1trbr._1n2vpki5 364.5x42.0 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 4px outline 2px solid #222325 offset 1px | button._1fe1trbr._1n2vpki5 364.5x42.0 bg #efeff0 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gig-contact-default.png`, `gig-contact-hover.png`, `gig-contact-focus-visible.png`, `gig-contact-pressed.png`.

#### seller-card

Seller card. The "Get to know" seller card (avatar, level, rating, location).

Page: gig. Selector: `seller card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 712 x 7475.45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #62646a |
| Text node | li._1fe1trbk.m2d0eb0: Macan 16px/24px 400, #c5c6c9 |
| Transition | none |
| Icon | 16 x 16, colour #222325 |
| Painted layers | a._1fe1trbr._1n2vpki5 24.0x24.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px; div.gig-overview 712.0x116.0 bg #ffffff; figure._1dxiuao1j._1dxiuao14 0.0x0.0 bg #912626 border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd r 9999px; figure._1dxiuao1j._1dxiuao14 64.0x64.0 bg #912626 border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd r 9999px; a.nav-prev 48.0x48.0 bg #ffffff r 30px shadow #000000 @ 0.15 0px 2px 5px 0px; a::after.nav-prev 16pxx16px image url(data:…) |
| Ancestor paint | 1 up div.gig-page bg #ffffff |
| How | at rest |

Crops: `seller-card-default.png`.

#### faq-acc

FAQ accordion. A question row in the gig page's FAQ section; the opened state was measured after clicking it — a local UI toggle.

Page: gig. Selector: `gig FAQ row`. States: .

Not found on the page at capture time.

#### review-card

Review card. A review block in the gig's reviews list (reviewer name, star rating, review text).

Page: gig. Selector: `gig review card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #62646a |
| Transition | none |
| Painted layers | div._12d3e3 0.0x0.0 bg #e4e5e7 r 999px; span._154693.star-progress-shape 0.0x0.0 bg #222325 r 999px; div._12d3e3 0.0x0.0 bg #e4e5e7 r 999px; span._154693.star-progress-shape 0.0x0.0 bg #222325 r 999px; div._12d3e3 0.0x0.0 bg #e4e5e7 r 999px; span._154693.star-progress-shape 0.0x0.0 bg #222325 r 999px |
| How | at rest |

Crops: none.

#### tag-chip

Related tag. A related-tag chip under the gig (Related tags); measured, never followed.

Page: gig. Selector: `gig related tag`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.72 x 14 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 4px | = |
| Font | Macan 14px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._1fe1trbk._1fe1trbl 81.7x14.0 outline 2px solid #222325 offset 4px | = |

Crops: `tag-chip-default.png`, `tag-chip-hover.png`, `tag-chip-focus-visible.png`, `tag-chip-pressed.png`.

### Seller profile

#### seller-h1

Seller headline. The seller profile's name/headline.

Page: seller. Selector: `seller h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 103.19 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 24px/32px 700 |
| Letter spacing | normal |
| Colour | #222325 |
| Transition | none |
| How | at rest |

Crops: `seller-h1-default.png`.

#### seller-contact

Profile Contact me. The "Contact me" button on the seller profile; measured, never pressed.

Page: seller. Selector: `seller Contact me`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 0 x 0 | - | 149.56 x 42 | 149.56 x 42 |
| Padding | 8px 16px | - | = | = |
| Gap | 8px | - | = | = |
| Border | 1px solid #000000 @ 0 | - | = | = |
| Radius | 8px | - | = | = |
| Background | #222325 | - | = | #62646a |
| Box shadow | none | - | = | = |
| Outline | none | - | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | - | = | = |
| Letter spacing | normal | - | = | = |
| Colour | #ffffff | - | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | - | = | = |
| Cursor | pointer | - | = | = |
| Icon | 0 x 0, colour #ffffff | - | 16 x 16, colour #ffffff | 16 x 16, colour #ffffff |
| Painted layers | button._1b71pl6w._1b71pl6r 0.0x0.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | - | button._1b71pl6w._1b71pl6r 149.6x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #222325 offset 1px | button._1b71pl6w._1b71pl6r 149.6x42.0 bg #62646a border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px |
| How | at rest | - | keydown then focus() | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is not visible Call log:   - waiting for locator('button').filter({ hasText: /^Contact me$/ }).first().first().first()     - locator resolved to <button role="button" data-track | = | = |
| Text node | - | = | span.p-l-8: Macan 16px/24px 600, #ffffff | span.p-l-8: Macan 16px/24px 600, #ffffff |

Crops: `seller-contact-focus-visible.png`, `seller-contact-pressed.png`.

#### seller-gig-card

Profile gig card. A gig card on the seller profile's listings grid; measured, never followed.

Page: seller. Selector: `seller gig card`. States: .

Not found on the page at capture time.

### Join and sign-in edge

#### join-panel

Join panel. The /join sign-up card — "Create a new account" with the Continue-with-* SSO buttons and the email join path.

Page: join. Selector: `join panel`. States: .

Not found on the page at capture time.

#### join-google

Google SSO (join). The "Continue with Google" button on /join; measured, never pressed.

Page: join. Selector: `join Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 370 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e4e5e7 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #efeff0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Text node | p._34ccirk.dcg2eq1j: Macan 16px/24px 600, #222325 | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222325, fill #000000 | = | = | = |
| Painted layers | button._34ccirw._34ccirr 370.0x42.0 bg #ffffff border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px | button._34ccirw._34ccirr 370.0x42.0 bg #f5f5f5 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px | button._34ccirw._34ccirr 370.0x42.0 bg #ffffff border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px outline 2px solid #222325 offset 1px | button._34ccirw._34ccirr 370.0x42.0 bg #efeff0 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `join-google-default.png`, `join-google-hover.png`, `join-google-focus-visible.png`, `join-google-pressed.png`.

#### join-apple

Apple SSO (join). The "Continue with Apple" button on /join; measured, never pressed.

Page: join. Selector: `join Continue with Apple`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 370 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e4e5e7 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #efeff0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Text node | p._34ccirk.dcg2eq1j: Macan 16px/24px 600, #222325 | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222325 | = | = | = |
| Painted layers | button._34ccirw._34ccirr 370.0x42.0 bg #ffffff border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px | button._34ccirw._34ccirr 370.0x42.0 bg #f5f5f5 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px | button._34ccirw._34ccirr 370.0x42.0 bg #ffffff border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px outline 2px solid #222325 offset 1px | button._34ccirw._34ccirr 370.0x42.0 bg #efeff0 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `join-apple-default.png`, `join-apple-hover.png`, `join-apple-focus-visible.png`, `join-apple-pressed.png`.

#### join-email-btn

Email join button. The e-mail join button on /join; measured, never pressed.

Page: join. Selector: `join email button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 370 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e4e5e7 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #efeff0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 3px solid #222325 offset 0px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Text node | p._34ccirk.dcg2eq1j: Macan 16px/24px 600, #222325 | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222325 | = | = | = |
| Painted layers | button._34ccirw._34ccirr 370.0x42.0 bg #ffffff border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px | button._34ccirw._34ccirr 370.0x42.0 bg #f5f5f5 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px | button._34ccirw._34ccirr 370.0x42.0 bg #ffffff border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px outline 3px solid #222325 offset 0px | button._34ccirw._34ccirr 370.0x42.0 bg #efeff0 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `join-email-btn-default.png`, `join-email-btn-hover.png`, `join-email-btn-focus-visible.png`, `join-email-btn-pressed.png`.

#### join-field

Join field. A join form field (e-mail/username); focused and typed into then cleared — never submitted. Recorded missing when /join renders SSO-only.

Page: join. Selector: `join input`. States: .

Not found on the page at capture time.

#### login-panel

Login panel. The /login card — "Sign in to your account" with the Continue-with-* SSO buttons and the username/password form.

Page: login. Selector: `login panel`. States: .

Not found on the page at capture time.

#### login-google

Google SSO (login). The "Continue with Google" button on /login; measured, never pressed.

Page: login. Selector: `login Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 370 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e4e5e7 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #f5f5f5 | = | #efeff0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | = | = | = |
| Text node | p._34ccirk.dcg2eq1j: Macan 16px/24px 600, #222325 | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #222325, fill #000000 | = | = | = |
| Painted layers | button._34ccirw._34ccirr 370.0x42.0 bg #ffffff border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px | button._34ccirw._34ccirr 370.0x42.0 bg #f5f5f5 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px | button._34ccirw._34ccirr 370.0x42.0 bg #ffffff border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px outline 2px solid #222325 offset 1px | button._34ccirw._34ccirr 370.0x42.0 bg #efeff0 border T:1px solid #e4e5e7 / R:1px solid #e4e5e7 / B:1px solid #e4e5e7 / L:1px solid #e4e5e7 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-email

Email/username field. The username-or-e-mail input on the sign-in form; focused and typed into then cleared — never submitted.

Page: login. Selector: `login username input`. States: .

Not found on the page at capture time.

#### login-password

Password field. The password input on the sign-in form; focused and typed into then cleared — never submitted.

Page: login. Selector: `login password input`. States: .

Not found on the page at capture time.

#### login-submit

Sign-in submit. The sign-in form's submit button; its states were measured but it was never clicked — nothing was submitted.

Page: login. Selector: `login submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 210 x 42 | - | = | = |
| Padding | 8px 16px | - | = | = |
| Gap | 8px | - | = | = |
| Border | 1px solid #222325 | - | = | = |
| Radius | 8px | - | = | = |
| Background | transparent | - | = | #efeff0 |
| Box shadow | none | - | = | = |
| Outline | none | - | 2px solid #222325 offset 1px | = |
| Font | Macan 16px/24px 600 | - | = | = |
| Letter spacing | normal | - | = | = |
| Colour | #222325 | - | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | - | = | = |
| Cursor | pointer | - | = | = |
| Painted layers | button._arosdn._1xeo152 210.0x42.0 border T:1px solid #222325 / R:1px solid #222325 / B:1px solid #222325 / L:1px solid #222325 r 8px | - | button._arosdn._1xeo152 210.0x42.0 border T:1px solid #222325 / R:1px solid #222325 / B:1px solid #222325 / L:1px solid #222325 r 8px outline 2px solid #222325 offset 1px | button._arosdn._1xeo152 210.0x42.0 bg #efeff0 border T:1px solid #222325 / R:1px solid #222325 / B:1px solid #222325 / L:1px solid #222325 r 8px |
| How | at rest | - | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is outside of the viewport Call log:   - waiting for locator('button[type="submit"], button').filter({ hasText: /^(Sign in/Log in/Continue)$/ }).first().first().first()     - lo | = | = |

Crops: `login-submit-default.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

### Logo maker, about and selling

#### lm-h1

Logo maker headline. The /logo-maker masthead.

Page: logo-maker. Selector: `logo-maker h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 499 x 52 |
| Padding | 0px 0px 20px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 24px/32px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `lm-h1-default.png`.

#### lm-cta

Logo maker CTA. The logo maker's primary CTA; measured, never followed.

Page: logo-maker. Selector: `logo-maker CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 128.34 x 48 | = | = | = |
| Padding | 15px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Macan 16px/16px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222325 | #404145 | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.ec83942._666340 128.3x48.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `lm-cta-default.png`, `lm-cta-hover.png`, `lm-cta-focus-visible.png`, `lm-cta-pressed.png`.

#### about-h1

About headline. The /about-us masthead ("ABOUT US" eyebrow, "Making way for breakthroughs").

Page: about. Selector: `about h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 70.69 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 14px/20px 600 |
| Letter spacing | -0.14px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `about-h1-default.png`.

#### about-cta

About link. A marketing link on /about-us; measured, never followed.

Page: about. Selector: `about link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120.55 x 42 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #222325 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #74767e offset 1px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | -0.16px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | p._1gwpigik.qzwehm1gt: Macan 16px/24px 600, #ffffff, ls -0.16px | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a._1gwpigir._1wkuego5 120.5x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = | a._1gwpigir._1wkuego5 120.5x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #74767e offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `about-cta-default.png`, `about-cta-hover.png`, `about-cta-focus-visible.png`, `about-cta-pressed.png`.

#### sell-h1

Selling headline. The /start_selling masthead ("Turn your expertise into a global business").

Page: selling. Selector: `selling h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 572.48 x 160.81 |
| Padding | 20px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 64px/70.4px 400 |
| Letter spacing | -4px |
| Colour | #222325 |
| Text node | p: Macan 64px/70.4px 400, #222325, ls -4px |
| Transition | none |
| How | at rest |

Crops: `sell-h1-default.png`.

#### sell-cta

Seller CTA. The "Create your profile" / "Get started" CTA on /start_selling; measured, never followed.

Page: selling. Selector: `selling CTA`. States: default, hover, focus-visible, pressed.

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

Crops: `sell-cta-default.png`, `sell-cta-hover.png`, `sell-cta-focus-visible.png`, `sell-cta-pressed.png`.

#### sell-cat

Selling category chip. A category chip on the seller landing page; measured, never toggled.

Page: selling. Selector: `selling category chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 206.22 x 41 | = | = | = |
| Padding | 8px 32px | = | = | = |
| Border | T: none; R: none; B: 1px solid #dadbdd; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset -2px | = |
| Font | Macan 16px/24px 600 | = | = | = |
| Letter spacing | -1px | = | = | = |
| Colour | #222325 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button._1gwpigiw._1gwpigik 206.2x41.0 border B:1px solid #dadbdd | = | button._1gwpigiw._1gwpigik 206.2x41.0 border B:1px solid #dadbdd outline 2px solid #000000 offset -2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sell-cat-default.png`, `sell-cat-hover.png`, `sell-cat-focus-visible.png`, `sell-cat-pressed.png`.

#### hiw-h1

How-it-works headline. The /cp/how-fiverr-works masthead.

Page: how-it-works. Selector: `how-fiverr-works h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 770 x 64 |
| Padding | 0px 86px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 18px/32px 400 |
| Letter spacing | -0.18px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hiw-h1-default.png`.

#### hiw-step

Steps section. A step block on the how-it-works explainer.

Page: how-it-works. Selector: `how-fiverr-works steps`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 5583.2 |
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
| Painted layers | header._188cbt6._bbx8bt 1425.0x86.0 bg #ffffff border B:1px solid #dadbdd; button._arosdn._1xeo152 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; input.long-placeholder 436.2x42.0 bg #ffffff border T:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 4px 0px 0px 4px; input.short-placeholder 0.0x0.0 bg #ffffff border T:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 4px 0px 0px 4px; button._arosdn._1xeo152 50.0x42.0 bg #222325 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 0px 4px 4px 0px; input.long-placeholder 0.0x0.0 bg #ffffff border T:1px solid #c5c6c9 / B:1px solid #c5c6c9 / L:1px solid #c5c6c9 r 4px 0px 0px 4px |
| Ancestor paint | 1 up body.layout-service.layout_service bg #ffffff |
| How | at rest |

Crops: `hiw-step-default.png`.

#### hiw-faq

HIW FAQ accordion. A question row in the page's FAQ section; the opened state was measured after clicking it — a local UI toggle.

Page: how-it-works. Selector: `how-fiverr-works FAQ row`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 1044 x 64 | = |
| Padding | 20px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Macan 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #74767e | = |
| Text node | p: Macan 16px/24px 400, #404145, ls -0.16px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #74767e | = |
| How | at rest | own toggle |

Crops: `hiw-faq-default.png`, `hiw-faq-opened.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top bar. The phone header at 390 wide: the hamburger, the Fiverr wordmark and the Join/sign-in controls.

Page: mobile. Selector: `mobile main-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 136 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #62646a |
| Text node | h6: Macan 14px/19.6px 700, #404145 |
| Transition | none |
| Icon | 50 x 50, colour #62646a |
| Painted layers | div.app-upper-banner.flex 390.0x71.0 bg #ffffff border B:1px solid #e4e5e7; button._581729._9de274 104.4x36.0 bg #1dbf73 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; header._188cbt6._bbx8bt 390.0x65.0 bg #ffffff border B:1px solid #dadbdd; button._arosdn._1xeo152 42.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; button.selection-trigger.language-selection-trigger 0.0x0.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px; div._188cbt6._bbx8bt 0.0x0.0 border L:1px solid #dadbdd |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Mobile menu button. The hamburger that opens the categories drawer — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `mobile Sidebar menu`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 42 x 42 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Gap | 8px | = | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = | = |
| Radius | 8px | = | = | = | = |
| Background | transparent | #f5f5f5 | = | #efeff0 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 2px solid #222325 offset 1px | = | = |
| Font | Macan 16px/24px 600 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #222325 | = | = | = | = |
| Transition | all 0.07s cubic-bezier(0.75, 0, 0.25, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 20 x 20, colour #222325 | = | = | = | = |
| Painted layers | button._arosdn._1xeo152 42.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button._arosdn._1xeo152 42.0x42.0 bg #f5f5f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | button._arosdn._1xeo152 42.0x42.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #222325 offset 1px | button._arosdn._1xeo152 42.0x42.0 bg #efeff0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile drawer. The categories drawer open at 390 wide (Browse categories tree plus locale/currency and Join/Sign-in at its foot); its links were never followed.

Page: mobile. Selector: `mobile categories drawer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 5147.25 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Macan 16px/24px 400 |
| Letter spacing | normal |
| Colour | #62646a |
| Text node | h6: Macan 14px/19.6px 700, #404145 |
| Transition | none |
| Icon | 50 x 50, colour #62646a |
| Painted layers | body.layout-service.layout_service 390.0x5147.3 bg #ffffff; div.ulsti.hidden 0.0x0.0 bg #3dd6f2 r 50%; div.uai.hidden 0.0x0.0 bg #3dd6f2 r 50%; div.uw-s10-reading-guide 0.0x0.0 bg #000000 border T:3px solid #fff300 / R:3px solid #fff300 / B:3px solid #fff300 / L:3px solid #fff300 r 5px; div::before.uw-s10-reading-guide__arrow 0pxx0px border T:17px solid #000000 @ 0 / R:17px solid #000000 @ 0 / B:17px solid #fff300 / L:17px solid #000000 @ 0; div::after.uw-s10-reading-guide__arrow 0pxx0px border T:14px solid #000000 @ 0 / R:14px solid #000000 @ 0 / B:14px solid #000000 / L:14px solid #000000 @ 0 |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 286.34 x 70.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Macan 32px/35.2px 280 |
| Letter spacing | -1.28px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-search-input

Mobile search field. The hero search input at 390 wide (the header search excluded); focused, never searched.

Page: mobile. Selector: `mobile hero search input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 293 x 52 | = |
| Padding | 10px 48px 10px 16px | = |
| Border | 1px solid #dadbdd | 1px solid #95979d |
| Radius | 12px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Macan 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #404145 | = |
| Transition | all 0.15s ease-in-out | = |
| Cursor | text | = |
| Placeholder | #95979d, opacity 1 | = |
| Painted layers | input 293.0x52.0 bg #ffffff border T:1px solid #dadbdd / R:1px solid #dadbdd / B:1px solid #dadbdd / L:1px solid #dadbdd r 12px | input 293.0x52.0 bg #ffffff border T:1px solid #95979d / R:1px solid #95979d / B:1px solid #95979d / L:1px solid #95979d r 12px |
| How | at rest | clicked into the field |

Crops: `m-search-input-default.png`, `m-search-input-focused.png`.

## Transitions declared in the readable stylesheets

fiverr.com serves its CSS as linked atomic-class bundles plus inline `<style>` blocks; this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- about: `opacity 0.2s ease-in-out`, `0.2s ease-in-out`, `0.5s cubic-bezier(0.37, 0.01, 0, 0.98)`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- categories: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- gig: `opacity 0.1s cubic-bezier(0, 0, 1, 1)`, `stroke-dashoffset 0.35s`, `opacity 0.5s`, `padding 70ms`, `0.15s ease-in-out`, `background-color 0.3s ease-in-out`, `opacity 0.3s`, `0.2s`, `opacity 0.2s`, `width 0.3s`, `0.3s`, `transform 0.2s`

- home: `transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- how-it-works: `opacity 0.2s ease-in-out`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- join: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- login: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- logo-maker: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- search: `opacity 0.3s ease-in-out`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- seller: `opacity 0.1s cubic-bezier(0, 0, 1, 1)`, `stroke-dashoffset 0.35s`, `opacity 0.5s`, `padding 70ms`, `transform 0.5s ease-in-out`, `0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`

- selling: `opacity 0.2s ease-in-out`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

- subcategory: `opacity 0.3s ease-in-out`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `none`, `transform 0.75s linear(0 0%, 0.006 1.1%, 0.023 2.2%, 0.096 4.8%, 0.532 15.4%, 0.72 21%, 0.793 23.85%, 0.853 26.7%, 0.902 29.8667%, 0.941 33.0333%, 0.968 36.2%, 0.987 39.7%, 1 43.7%, 1.007 48.3%, 1.009 55.3%, 1.002 78.2%, 1 100%)`, `opacity 0.3s ease-in`, `max-height 1s ease-in`, `transform 1s linear(0 0%, 0.006 1.15%, 0.022 2.3%, 0.091 5.1%, 0.18 7.6%, 0.508 16.3%, 0.607 19.325%, 0.691 22.35%, 0.762 25.375%, 0.822 28.4%, 0.872 31.75%, 0.912 35.1%, 0.944 38.9%, 0.968 43%, 0.985 47.6%, 0.996 53.1%, 1.001 58.4%, 1.003 65.1%, 1 100%)`

## Reduced motion

- home (`.main-header a[href^="/join"]` under prefers-reduced-motion): Error: page.waitForTimeout: Target page, context or browser has been closed
