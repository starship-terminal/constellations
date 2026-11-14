# Esquire component measurements

Computed styles read from esquire.com on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the light home, section, article, essay, offers, premium-hub, search and about pages — with the OneTrust consent layer hidden (never answered) and third-party ad/tracker requests aborted so ad slots read as blank containers, and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Navigation and site chrome

#### nav

Desktop navigation. The full top chrome: the dark utility strip (edition, Newsletter), the main bar (search field, Esquire wordmark, Sign In, Subscribe) and the .megaMenu category strip.

Page: home. Selector: `nav[data-tracking-id=topNav]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 155.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.translate-y-(--comp-btn-md-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-md-type-decoration-line-mobile)]: Lausanne 13px/18.2px 400, #121212, ls 0.4px |
| Transition | none |
| Icon | 16 x 16, colour #121212, fill #000000 |
| Painted layers | nav.css-1cbuarp.eju4swf4 1440.0x155.5 bg #ffffff; div.css-zbfy27.eju4swf3 1440.0x155.5 bg #ffffff; div.css-1rxqawy.e17hn77m2 1440.0x32.0 bg #ff3a30; button.hds-do-not-use.inline-flex 64.8x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px; div.css-1gvhv7i.e1c0kr9d1 0.0x0.0 bg #ffffff border T:1px solid #ededed / R:1px solid #ededed / B:1px solid #ededed / L:1px solid #ededed; a.hds-do-not-use.inline-flex 0.0x0.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 |
| How | at rest |

Crops: `nav-default.png`.

#### nav-utility

Utility strip. The 32px top utility bar holding the US edition switcher and the Newsletter link.

Page: home. Selector: `div ancestor of the US button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 64.81 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.translate-y-(--comp-btn-md-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-md-type-decoration-line-mobile)]: Lausanne 13px/18.2px 400, #121212, ls 0.4px |
| Transition | none |
| Icon | 16 x 16, colour #121212, fill #000000 |
| Painted layers | button.hds-do-not-use.inline-flex 64.8x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px; div.css-1gvhv7i.e1c0kr9d1 0.0x0.0 bg #ffffff border T:1px solid #ededed / R:1px solid #ededed / B:1px solid #ededed / L:1px solid #ededed; a.hds-do-not-use.inline-flex 0.0x0.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04; a.hds-do-not-use.inline-flex 0.0x0.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04; a.hds-do-not-use.inline-flex 0.0x0.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04; a.hds-do-not-use.inline-flex 0.0x0.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 |
| How | at rest |

Crops: `nav-utility-default.png`.

#### nav-edition

Edition switcher. The "US" edition button in the utility strip; measured, never toggled open beyond a hover.

Page: home. Selector: `nav US button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64.81 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ff3a30 | = | = | = |
| Radius | 1024px | = | = | = |
| Background | #ff3a30 | #ffffff | = | #fff0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Lausanne 13px/18.2px 400 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #121212 | = | = | = |
| Text node | span.translate-y-(--comp-btn-md-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-md-type-decoration-line-mobile)]: Lausanne 13px/18.2px 400, #121212, ls 0.4px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #121212, fill #000000 | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 64.8x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | button.hds-do-not-use.inline-flex 64.8x32.0 bg #ffffff border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | button.hds-do-not-use.inline-flex 64.8x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px outline 1px auto #101010 offset 0px | button.hds-do-not-use.inline-flex 64.8x32.0 bg #fff0f0 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-edition-default.png`, `nav-edition-hover.png`, `nav-edition-focus-visible.png`, `nav-edition-pressed.png`.

#### nav-newsletter

Newsletter link. The "Newsletter" utility link; measured, never followed.

Page: home. Selector: `nav a Newsletter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 125 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ff3a30 | = | = | = |
| Radius | 1024px | = | = | = |
| Background | #ff3a30 | #ffffff | = | #fff0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Lausanne 13px/18.2px 400 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #121212 | = | = | = |
| Text node | span.translate-y-(--comp-btn-md-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-md-type-decoration-line-mobile)]: Lausanne 13px/18.2px 400, #121212, ls 0.4px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #121212, fill #000000 | = | = | = |
| Painted layers | a.hds-do-not-use.inline-flex 125.0x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | a.hds-do-not-use.inline-flex 125.0x32.0 bg #ffffff border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | a.hds-do-not-use.inline-flex 125.0x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px outline 1px auto #101010 offset 1px | a.hds-do-not-use.inline-flex 125.0x32.0 bg #fff0f0 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-newsletter-default.png`, `nav-newsletter-hover.png`, `nav-newsletter-focus-visible.png`, `nav-newsletter-pressed.png`.

#### nav-logo

Wordmark. The Esquire wordmark lockup centred in the main bar (a link home holding the widest inline svg).

Page: home. Selector: `widest svg inside a nav anchor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 296 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -148, 0) |
| Cursor | pointer |
| Icon | 296 x 60, colour #121212, fill #000000 |
| How | at rest |

Crops: `nav-logo-default.png`.

#### nav-signin

Sign In link. The "Sign In" link to account.esquire.com; measured, never followed.

Page: home. Selector: `nav a Sign In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 77.41 x 38.3 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.04 | 1px solid #ff3a30 @ 0.08 | = | 1px solid #ff3a30 @ 0.16 |
| Radius | 1024px | = | = | = |
| Background | #ff382e @ 0 | #ff3a30 @ 0.08 | = | #ff3a30 @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Lausanne 16px/20.3px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #121212 | = | = | = |
| Text node | span.translate-y-(--comp-btn-lg-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-lg-type-decoration-line-mobile)]: Lausanne 16px/20.3px 400, #121212, ls 0.2px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hds-do-not-use.inline-flex 77.4x38.3 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px | a.hds-do-not-use.inline-flex 77.4x38.3 bg #ff3a30 @ 0.08 border T:1px solid #ff3a30 @ 0.08 / R:1px solid #ff3a30 @ 0.08 / B:1px solid #ff3a30 @ 0.08 / L:1px solid #ff3a30 @ 0.08 r 1024px | a.hds-do-not-use.inline-flex 77.4x38.3 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px outline 1px auto #101010 offset 1px | a.hds-do-not-use.inline-flex 77.4x38.3 bg #ff3a30 @ 0.16 border T:1px solid #ff3a30 @ 0.16 / R:1px solid #ff3a30 @ 0.16 / B:1px solid #ff3a30 @ 0.16 / L:1px solid #ff3a30 @ 0.16 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-subscribe

Subscribe button. The red "Subscribe" call-to-action in the main bar; measured, never followed.

Page: home. Selector: `nav Subscribe`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.81 x 38.3 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ff3a30 | = | = | = |
| Radius | 1024px | = | = | = |
| Background | #ff3a30 | #ffffff | = | #fff0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Lausanne 16px/20.3px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #121212 | = | = | = |
| Text node | span.translate-y-(--comp-btn-lg-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-lg-type-decoration-line-mobile)]: Lausanne 16px/20.3px 400, #121212, ls 0.2px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hds-do-not-use.inline-flex 105.8x38.3 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | a.hds-do-not-use.inline-flex 105.8x38.3 bg #ffffff border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | a.hds-do-not-use.inline-flex 105.8x38.3 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px outline 1px auto #101010 offset 1px | a.hds-do-not-use.inline-flex 105.8x38.3 bg #fff0f0 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-subscribe-default.png`, `nav-subscribe-hover.png`, `nav-subscribe-focus-visible.png`, `nav-subscribe-pressed.png`.

#### nav-search

Search field. The header "Search..." input; focused and typed into then cleared — never submitted.

Page: home. Selector: `nav input[placeholder*=Search]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 211.81 x 26.19 | = | = |
| Padding | 4px 2px 4px 12px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Lausanne 14px/18.2px 400 | = | = |
| Letter spacing | 0.4px | = | = |
| Colour | #121212 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Ancestor paint | 1 up div.flex.items-center bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "suits", then deleted; nothing sent |

Crops: `nav-search-default.png`, `nav-search-focused.png`, `nav-search-filled.png`.

#### nav-search-btn

Search icon button. The search-icon submit inside the header search box; measured, never pressed.

Page: home. Selector: `nav button[aria-label=Search]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 26.19 x 26.19 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #121212 @ 0 | 1px solid #121212 @ 0.04 | = | 1px solid #121212 @ 0.08 |
| Radius | 1024px | = | = | = |
| Background | #121212 @ 0 | #121212 @ 0.04 | = | #121212 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Lausanne 13px/18.2px 400 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #121212, fill #000000 | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 26.2x26.2 bg #121212 @ 0 border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px | button.hds-do-not-use.inline-flex 26.2x26.2 bg #121212 @ 0.04 border T:1px solid #121212 @ 0.04 / R:1px solid #121212 @ 0.04 / B:1px solid #121212 @ 0.04 / L:1px solid #121212 @ 0.04 r 1024px | button.hds-do-not-use.inline-flex 26.2x26.2 bg #121212 @ 0 border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px outline 1px auto #101010 offset 0px | button.hds-do-not-use.inline-flex 26.2x26.2 bg #121212 @ 0.08 border T:1px solid #121212 @ 0.08 / R:1px solid #121212 @ 0.08 / B:1px solid #121212 @ 0.08 / L:1px solid #121212 @ 0.08 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-search-btn-default.png`, `nav-search-btn-hover.png`, `nav-search-btn-focus-visible.png`, `nav-search-btn-pressed.png`.

#### megamenu

Category menu. The .megaMenu category strip under the main bar: Entertainment through Food and Drinks plus the "More" overflow toggle.

Page: home. Selector: `.megaMenu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 53.2 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #757575; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.hds-do-not-use.no-underline: Lausanne 16px/23.2px 400, #121212, ls 0.2px |
| Transition | none |
| Icon | 16 x 16, colour #121212, fill #000000 |
| Painted layers | div.megaMenu.css-1uwvko7 1440.0x53.2 border B:1px solid #757575; button.hds-do-not-use.inline-flex 26.0x18.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px; button.hds-do-not-use.inline-flex 26.0x18.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px; button.hds-do-not-use.inline-flex 26.0x18.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px; button.hds-do-not-use.inline-flex 26.0x18.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px; button.hds-do-not-use.inline-flex 26.0x18.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px |
| Ancestor paint | 1 up div.css-zbfy27.eju4swf3 bg #ffffff |
| How | at rest |

Crops: `megamenu-default.png`.

#### nav-link

Category link. A .megaMenu category link ("Entertainment"); measured, never followed.

Page: home. Selector: `.megaMenu a Entertainment`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.61 x 23.2 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Lausanne 16px/23.2px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.hds-do-not-use.no-underline 112.6x23.2 outline 1px auto #101010 offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-subchevron

Submenu chevron. The per-category "Open X submenu" chevron button; measured, never toggled.

Page: home. Selector: `.megaMenu button[aria-label*=submenu]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 26 x 18 | = | = | = |
| Padding | 0px 4px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ffffff @ 0.04 | = | = | 1px solid #ff3a30 @ 0.16 |
| Radius | 1024px | = | = | = |
| Background | #ff382e @ 0 | = | = | #ff3a30 @ 0.16 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Lausanne 13px/18.2px 400 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #121212, fill #000000 | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 26.0x18.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px | = | button.hds-do-not-use.inline-flex 26.0x18.0 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px outline 1px auto #101010 offset 0px | button.hds-do-not-use.inline-flex 26.0x18.0 bg #ff3a30 @ 0.16 border T:1px solid #ff3a30 @ 0.16 / R:1px solid #ff3a30 @ 0.16 / B:1px solid #ff3a30 @ 0.16 / L:1px solid #ff3a30 @ 0.16 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-subchevron-default.png`, `nav-subchevron-hover.png`, `nav-subchevron-focus-visible.png`, `nav-subchevron-pressed.png`.

#### more-btn

More toggle. The "More" overflow toggle — a local UI toggle; the opened state was measured after clicking it, its links never followed.

Page: home. Selector: `.megaMenu button More`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 87.61 x 28.2 | = | = | = | = |
| Padding | 4px 12px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | 1px solid #ffffff @ 0.04 | = | = | 1px solid #ff3a30 @ 0.16 | = |
| Radius | 1024px | = | = | = | = |
| Background | #ff382e @ 0 | = | = | #ff3a30 @ 0.16 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Lausanne 16px/18.2px 400 | = | = | = | = |
| Letter spacing | 0.4px | = | = | = | = |
| Colour | #121212 | = | = | = | = |
| Text node | span.translate-y-(--comp-btn-md-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-md-type-decoration-line-mobile)]: Lausanne 16px/18.2px 400, #121212, ls 0.4px | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #121212, fill #000000 | = | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 87.6x28.2 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px | = | button.hds-do-not-use.inline-flex 87.6x28.2 bg #ff382e @ 0 border T:1px solid #ffffff @ 0.04 / R:1px solid #ffffff @ 0.04 / B:1px solid #ffffff @ 0.04 / L:1px solid #ffffff @ 0.04 r 1024px outline 1px auto #101010 offset 0px | button.hds-do-not-use.inline-flex 87.6x28.2 bg #ff3a30 @ 0.16 border T:1px solid #ff3a30 @ 0.16 / R:1px solid #ff3a30 @ 0.16 / B:1px solid #ff3a30 @ 0.16 / L:1px solid #ff3a30 @ 0.16 r 1024px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `more-btn-default.png`, `more-btn-hover.png`, `more-btn-focus-visible.png`, `more-btn-pressed.png`, `more-btn-opened.png`.

#### more-panel

More panel. The overflow panel opened by "More" — the hidden sections (Sports, Member Exclusives, For You) plus their submenu links.

Page: home. Selector: `.megaMenu overflow panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 302 x 92.89 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | a.hds-do-not-use.no-underline: Lausanne 14px/20.3px 400, #121212, ls 0.4px |
| Transition | none |
| Ancestor paint | 3 up div.css-96zydn.edouk7815 bg #ffffff shadow #000000 @ 0.1 0px 10px 10px 0px |
| How | at rest |

Crops: `more-panel-default.png`.

### Home page

#### ad-disclaimer

Ad disclaimer. The "Advertisement - Continue Reading Below" furniture label that sits above each blank ad slot; the slots themselves stay empty because ad requests are aborted.

Page: home. Selector: `.ad-disclaimer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 14.84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 11px/14.85px 400 |
| Letter spacing | 0.4px |
| Colour | #121212 |
| Transition | none |
| ::before | 507.906px x 1px, relative, bg #ededed, radius 0px |
| ::after | 507.906px x 1px, relative, bg #ededed, radius 0px |
| Painted layers | div::before.ad-disclaimer.no-print 507.906pxx1px bg #ededed; div::after.ad-disclaimer.no-print 507.906pxx1px bg #ededed |
| How | at rest |

Crops: `ad-disclaimer-default.png`.

#### section-h2

Section heading. A home-page section heading ("The Latest") — 32px Lausanne.

Page: home. Selector: `h2 The Latest`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 302 x 41.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 32px/41.6px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### story-card

Story list card. A story row in "The Latest": thumbnail, 18px Lausanne headline, byline and read-time.

Page: home. Selector: `ancestor of first main h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 302 x 132 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | span: Lausanne 12px/16.8px 400, #3b3b3b, ls 0.4px |
| Transition | none |
| Icon | 16 x 16, colour #3b3b3b, fill #000000 |
| How | at rest |

Crops: `story-card-default.png`.

#### story-title

Story headline. An 18px Lausanne story headline in the Latest list.

Page: home. Selector: `main h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 214 x 69.61 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 18px/23.2px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `story-title-default.png`.

#### story-thumb

Story thumbnail. The thumbnail image inside a story list card.

Page: home. Selector: `story card img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 80 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ededed |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0 |
| Transition | none |
| How | at rest |

Crops: `story-thumb-default.png`.

#### byline

Byline. A "BY <AUTHOR>" byline under a story headline.

Page: home. Selector: `main BY-line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 114.41 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 12px/16.8px 400 |
| Letter spacing | 0.4px |
| Colour | #3b3b3b |
| Transition | none |
| How | at rest |

Crops: `byline-default.png`.

#### readtime

Read time. The "min read" duration label with its clock icon on a story card.

Page: home. Selector: `min read label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 86 x 16.8 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 12px/16.8px 400 |
| Letter spacing | 0.4px |
| Colour | #3b3b3b |
| Transition | none |
| Icon | 16 x 16, colour #3b3b3b, fill #000000 |
| How | at rest |

Crops: `readtime-default.png`.

#### eyebrow

Eyebrow. The small uppercase red eyebrow ("NEWS" / "STYLE") over a headline.

Page: home. Selector: `uppercase eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40.61 x 13 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 13px/18.2px 400 |
| Letter spacing | 0.4px |
| Colour | #121212 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `eyebrow-default.png`.

#### hero-story

Hero story. The cover hero headline painted at display size (56px PlayFair).

Page: home. Selector: `largest h3 by computed font-size`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 628 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PlayFair 56px/56px 400 |
| Letter spacing | -1.5px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `hero-story-default.png`.

#### hero-dek

Hero dek. The standfirst paragraph under the hero headline.

Page: home. Selector: `hero dek p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 628 x 52.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 20px/26.1px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `hero-dek-default.png`.

#### rail-card

Rail card. A right-rail "MAN AT HIS BEST" style card: thumbnail over a 20px headline with a dek.

Page: home. Selector: `rail card ancestor of h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 302 x 342.8 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | a.hds-do-not-use.no-underline: Lausanne 13px/18.2px 400, #121212, ls 0.4px |
| Transition | none |
| Icon | 16 x 16, colour #3b3b3b, fill #000000 |
| Painted layers | hr.css-1n2oy37.ehvmj2s4 302.0x1.0 bg #121212 |
| How | at rest |

Crops: `rail-card-default.png`.

#### newsletter-block

Newsletter block. The mid-page "Real journalism and real style" newsletter band: 28px Lausanne pitch, email field, Sign Up button and terms copy.

Page: home. Selector: `newsletter form ancestor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 942 x 235.31 |
| Padding | 32px 48px 20px 48px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | #f5f6f8 |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | h4.css-13k504j.e1wwtey52: Lausanne 13px/18.2px 400, #121212, ls 0.4px |
| Transition | none |
| Icon | 24 x 24, colour #575757, fill #000000 |
| Painted layers | div.css-1near0n.e1wwtey50 942.0x235.3 bg #f5f6f8; div.flex.items-center 512.0x38.3 bg #ffffff border T:1px solid #757575 / R:1px solid #757575 / B:1px solid #757575 / L:1px solid #757575 r 1024px; button.hds-do-not-use.inline-flex 85.4x28.3 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px; div.grecaptcha-badge 256.0x60.0 shadow #808080 0px 0px 5px 0px; textarea.g-recaptcha-response 0.0x0.0 bg #ffffff border T:1px solid #c1c1c1 / R:1px solid #c1c1c1 / B:1px solid #c1c1c1 / L:1px solid #c1c1c1; iframe 0.0x0.0 border T:2px inset #121212 / R:2px inset #121212 / B:2px inset #121212 / L:2px inset #121212 |
| How | at rest |

Crops: `newsletter-block-default.png`.

#### newsletter-input

Newsletter field. The "Enter your email address" field; focused and typed into then cleared — never submitted.

Page: home. Selector: `input[placeholder*=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 368.59 x 36.3 | = | = |
| Padding | 8px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Lausanne 16px/20.3px 400 | = | = |
| Letter spacing | 0.2px | = | = |
| Colour | #121212 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Ancestor paint | 1 up div.flex.items-center bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `newsletter-input-default.png`, `newsletter-input-focused.png`, `newsletter-input-filled.png`.

#### newsletter-signup

Sign Up button. The red "Sign Up" submit inside the newsletter band; measured, never pressed.

Page: home. Selector: `newsletter Sign Up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.41 x 28.3 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #ff3a30 | = | = | = |
| Radius | 1024px | = | = | = |
| Background | #ff3a30 | #ffffff | = | #fff0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Lausanne 16px/20.3px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #121212 | = | = | = |
| Text node | span.translate-y-(--comp-btn-lg-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-lg-type-decoration-line-mobile)]: Lausanne 16px/20.3px 400, #121212, ls 0.2px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 85.4x28.3 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | button.hds-do-not-use.inline-flex 85.4x28.3 bg #ffffff border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | button.hds-do-not-use.inline-flex 85.4x28.3 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px outline 1px auto #101010 offset 0px | button.hds-do-not-use.inline-flex 85.4x28.3 bg #fff0f0 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `newsletter-signup-default.png`, `newsletter-signup-hover.png`, `newsletter-signup-focus-visible.png`, `newsletter-signup-pressed.png`.

#### pagination

Pagination. The "1 | 2 | 3" pagination under the story feed; measured, never followed.

Page: home. Selector: `nav[aria-label=Pagination]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 192 x 56.39 |
| Padding | 12px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | a.hds-do-not-use.inline-flex: Lausanne 14px/20.3px 400, #121212, ls 0.4px |
| Transition | none |
| Icon | 24 x 24, colour #121212, fill #000000 |
| Painted layers | a.hds-do-not-use.inline-flex 32.0x32.0 bg #ff382e @ 0 r 1024px; a.hds-do-not-use.inline-flex 32.0x32.0 bg #d6d6d6 border T:1px solid #ededed / R:1px solid #ededed / B:1px solid #ededed / L:1px solid #ededed r 1024px; a.hds-do-not-use.inline-flex 32.0x32.0 bg #ffffff border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px; a.hds-do-not-use.inline-flex 32.0x32.0 bg #ffffff border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px; a.hds-do-not-use.inline-flex 32.0x32.0 bg #ff382e @ 0 r 1024px |
| Ancestor paint | 2 up section.css-1imhwz1.ege0am41 bg #ffffff shadow #ffffff 0px 0px 0px 1440px |
| How | at rest |

Crops: `pagination-default.png`.

### Footer

#### footer

Footer. The site footer: wordmark, social icons, the Newsletter/About Us link columns and the legal line.

Page: home. Selector: `footer holding nav[footer-menu]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 634.2 |
| Padding | 0px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | a.hds-do-not-use.no-underline: Lausanne 14px/20.3px 400, #121212, ls 0.4px |
| Transition | none |
| Icon | 148 x 48, colour #121212, fill #000000 |
| Painted layers | a.ot-sdk-show-settings.ebnr9ku0 144.8x54.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer nav link ("About Us"); measured, never followed.

Page: home. Selector: `footer-menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 67.2 x 20.3 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | Lausanne 14px/20.3px 400 | = | = | = |
| Letter spacing | 0.4px | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.hds-do-not-use.no-underline 67.2x20.3 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social icon link. A square social icon button in the footer (x, tiktok, youtube…); measured, never followed.

Page: home. Selector: `footer social a`. States: .

Not found on the page at capture time.

### Section front

#### sec-h1

Section title. The section-front title ("Style") — the display word at the top of the front.

Page: section. Selector: `section h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 205 x 85 |
| Padding | 25px 40px 13px 40px |
| Border | none |
| Radius | 80px |
| Background | #000000 @ 0.7 |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 52px/52px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | h1.css-hk395m.e1vkanl82 205.0x85.0 bg #000000 @ 0.7 r 80px |
| How | at rest |

Crops: `sec-h1-default.png`.

#### sec-desc

Section description. The standfirst describing the section under its title.

Page: section. Selector: `section description`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 87.59 |
| Padding | 0px 0px 30px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: Lora 18px/28.8px 700, #000000 |
| Transition | none |
| Painted layers | a 118.0x24.0 border B:1px solid #000000; a 102.0x24.0 border B:1px solid #000000; a 57.0x24.0 border B:1px solid #000000; a 875.5x52.8 border B:1px solid #000000; a 78.0x24.0 border B:1px solid #000000; a 138.0x24.0 border B:1px solid #000000 |
| How | at rest |

Crops: `sec-desc-default.png`.

#### sec-hero

Section lead card. The lead story card on the section front — the first image-carrying story link on the front.

Page: section. Selector: `first main a with img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 813 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.css-ecg1iu.e1otnc5c1: Lausanne 40px/48px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.css-wjntws.e11w5h812 1200.0x213.0 bg #f5f6f8 |
| How | at rest |

Crops: `sec-hero-default.png`.

#### sec-eyebrow

Section eyebrow. The uppercase eyebrow over the lead story.

Page: section. Selector: `section eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 205 x 85 |
| Padding | 25px 40px 13px 40px |
| Border | none |
| Radius | 80px |
| Background | #000000 @ 0.7 |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 52px/52px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | h1.css-hk395m.e1vkanl82 205.0x85.0 bg #000000 @ 0.7 r 80px |
| How | at rest |

Crops: `sec-eyebrow-default.png`.

#### sec-card

Section card. A standard story card lower on the section front.

Page: section. Selector: `section card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1311.58 |
| Padding | 10px 40px 30px 40px |
| Gap | 20px 0px |
| Border | none |
| Radius | 0px |
| Background | #f5f6f8 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Lausanne 44px/52.8px 400, #000000 |
| Transition | none |
| Painted layers | section.css-1l0vm3i.e17377vn1 1440.0x1311.6 bg #f5f6f8 |
| How | at rest |

Crops: `sec-card-default.png`.

#### sec-see-more

See More button. The "See More" pagination ghost button — dark #121212 outline, red text; measured, never pressed.

Page: section. Selector: `See More`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.61 x 38.3 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #121212 | = | = | = |
| Radius | 1024px | = | = | = |
| Background | #ffffff | #121212 @ 0.04 | = | #121212 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Lausanne 16px/20.3px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ff3a30 | = | = | = |
| Text node | span.translate-y-(--comp-btn-lg-dim-offset-y).[text-decoration-line:var(--comp-btn-secondary-lg-type-decoration-line-mobile)]: Lausanne 16px/20.3px 400, #ff3a30, ls 0.2px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 101.6x38.3 bg #ffffff border T:1px solid #121212 / R:1px solid #121212 / B:1px solid #121212 / L:1px solid #121212 r 1024px | button.hds-do-not-use.inline-flex 101.6x38.3 bg #121212 @ 0.04 border T:1px solid #121212 / R:1px solid #121212 / B:1px solid #121212 / L:1px solid #121212 r 1024px | button.hds-do-not-use.inline-flex 101.6x38.3 bg #ffffff border T:1px solid #121212 / R:1px solid #121212 / B:1px solid #121212 / L:1px solid #121212 r 1024px outline 1px auto #101010 offset 0px | button.hds-do-not-use.inline-flex 101.6x38.3 bg #121212 @ 0.08 border T:1px solid #121212 / R:1px solid #121212 / B:1px solid #121212 / L:1px solid #121212 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sec-see-more-default.png`, `sec-see-more-hover.png`, `sec-see-more-focus-visible.png`, `sec-see-more-pressed.png`.

#### about-h1

About heading. The "About Us" page heading.

Page: about. Selector: `about h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1140 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PlayFair 64px/64px 400 |
| Letter spacing | -2.4px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `about-h1-default.png`.

#### about-para

About paragraph. A paragraph on the About Us page.

Page: about. Selector: `about p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 644 x 259.17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `about-para-default.png`.

### Article page

#### related-strip

Related strip. The "RELATED" pill row pinned under the nav linking sibling stories; measured, never followed.

Page: article. Selector: `RELATED strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 40 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.css-eykynl.e1gtgae81: SF Pro 14px/15.4px 700, #000000 |
| Transition | none |
| Painted layers | span.css-6o028r.e1gtgae89 8.0x8.0 bg #000000 r 50%; a.e1gtgae84.css-1ylu0af 220.4x32.0 border T:1px solid #525252 / R:1px solid #525252 / B:1px solid #525252 / L:1px solid #525252 r 24px; a.e1gtgae84.css-1ylu0af 272.6x32.0 border T:1px solid #525252 / R:1px solid #525252 / B:1px solid #525252 / L:1px solid #525252 r 24px; a.e1gtgae84.css-1ylu0af 174.5x32.0 border T:1px solid #525252 / R:1px solid #525252 / B:1px solid #525252 / L:1px solid #525252 r 24px; a.e1gtgae84.css-1ylu0af 247.9x32.0 border T:1px solid #525252 / R:1px solid #525252 / B:1px solid #525252 / L:1px solid #525252 r 24px; a.e1gtgae84.css-1ylu0af 374.4x32.0 border T:1px solid #525252 / R:1px solid #525252 / B:1px solid #525252 / L:1px solid #525252 r 24px |
| Ancestor paint | 1 up div.css-p4n3k4.e1gtgae80 bg #ffffff |
| How | at rest |

Crops: `related-strip-default.png`.

#### art-breadcrumb

Breadcrumb. The section breadcrumb over the headline ("Entertainment › Movies").

Page: article. Selector: `article breadcrumb`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1140 x 34.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Lausanne 11.2045px/14.5658px 400, #525252 |
| Transition | none |
| How | at rest |

Crops: `art-breadcrumb-default.png`.

#### art-h1

Article headline. The cover-story headline — large PlayFair display.

Page: article. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1140 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | PlayFair 64px/64px 400 |
| Letter spacing | -2.4px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `art-h1-default.png`.

#### art-standfirst

Standfirst. The intro standfirst under the headline — lighter, larger Lausanne copy.

Page: article. Selector: `article standfirst p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1140 x 82.89 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 21px/27.3px 400 |
| Letter spacing | normal |
| Colour | #515150 |
| Transition | none |
| How | at rest |

Crops: `art-standfirst-default.png`.

#### art-byline

Byline. The author byline link ("By <name>"); measured, never followed.

Page: article. Selector: `a[href*=author]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 116 x 25.19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Lausanne 14px/25.2px 400 | = |
| Letter spacing | normal | = |
| Colour | #161616 | #525252 |
| Transition | all 0.3s ease-in-out | = |
| Cursor | pointer | = |
| ::before | 116px x 48px, absolute, bg #000000 @ 0, radius 0px | = |
| How | at rest | mouse hover |

Crops: `art-byline-default.png`, `art-byline-hover.png`.

#### art-hero

Hero image. The hero photograph under the article header.

Page: article. Selector: `article hero figure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 17 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `art-hero-default.png`.

#### art-caption

Caption. The photo caption / credit line under the hero.

Page: article. Selector: `figcaption`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1430 x 16.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.css-qt9nna.e1j223mq0: Lausanne 12px/15.6px 400, #525252 |
| Transition | none |
| How | at rest |

Crops: `art-caption-default.png`.

#### art-para

Body paragraph. A body paragraph — Lora 18px on the measure.

Page: article. Selector: `article body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 644 x 86.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `art-para-default.png`.

#### art-dropcap

Drop-cap paragraph. The lede paragraph whose first letter paints a drop cap.

Page: article. Selector: `p.body-dropcap`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 644 x 345.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `art-dropcap-default.png`.

#### art-link

Inline story link. An inline text link inside body copy; measured, never followed. Not every story carries one — this story had only the styled SUBSCRIBE CTA, so the link is a gap rather than a mislabelled button.

Page: article. Selector: `inline body-copy anchor`. States: .

Not found on the page at capture time.

#### art-pullquote

Pull quote. A display pull quote inside the story.

Page: article. Selector: `article blockquote`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 644 x 307.77 |
| Padding | 15px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | blockquote.css-1r62ir5.eb971bu1: Lausanne 38px/45.6px 400, #000000 |
| Transition | none |
| Painted layers | span::before.css-5esr6z.e1ge6zcj1 35pxx35px border T:5px solid #ff3a30 / R:5px solid #ff3a30 / B:5px solid #ff3a30 / L:5px solid #ff3a30 r 100% |
| How | at rest |

Crops: `art-pullquote-default.png`.

#### art-blockhead

Block heading. A mid-story block heading ("readers also read…").

Page: article. Selector: `article h2 block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 52.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 44px/52.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Lausanne 44px/52.8px 400, #000000 |
| Transition | none |
| How | at rest |

Crops: `art-blockhead-default.png`.

#### art-ad

Ad furniture. The "Advertisement - Continue Reading Below" furniture inside the story; the slot below it stays blank because ad requests are aborted.

Page: article. Selector: `.ad-disclaimer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1436.81 x 12.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 11.2045px/12.3249px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| ::before | 588.906px x 1px, relative, bg #e5e5e5, radius 0px |
| ::after | 588.906px x 1px, relative, bg #e5e5e5, radius 0px |
| Painted layers | div::before.ad-disclaimer.no-print 588.906pxx1px bg #e5e5e5; div::after.ad-disclaimer.no-print 588.906pxx1px bg #e5e5e5 |
| How | at rest |

Crops: `art-ad-default.png`.

#### art-related-card

Related card. A related-story card in the tail of the article.

Page: article. Selector: `related card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 982 |
| Padding | 0px |
| Gap | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.css-3zlrm4.e1otnc5c1: Lausanne 20px/24px 400, #161616 |
| Transition | none |
| Ancestor paint | 1 up section.css-5l71pd.e17377vn1 bg #f5f6f8 |
| How | at rest |

Crops: `art-related-card-default.png`.

#### essay-h1

Essay headline. A shorter essay headline — same display treatment as the cover story.

Page: essay. Selector: `essay h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 660 x 171.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 52px/57.2px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `essay-h1-default.png`.

#### essay-para

Essay paragraph. A body paragraph on the shorter essay.

Page: essay. Selector: `essay body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 612 x 230.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `essay-para-default.png`.

### Membership offers

#### offers-h1

Offers heading. "Choose a Plan" — the display heading over the plan grid.

Page: offers. Selector: `h1/h2 Choose a Plan`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1088 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 32px/36px 700 |
| Letter spacing | -0.96px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `offers-h1-default.png`.

#### plan-card

Plan card. A membership plan card: plan name, price line, perk list and its Join action.

Page: offers. Selector: `ancestor of Join button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352 x 250.95 |
| Padding | 16px 16px 20px 16px |
| Border | 1px solid #3b3b3b |
| Radius | 10px |
| Background | #f5f6f8 |
| Box shadow | none |
| Outline | none |
| Font | SF Pro 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | label.css-ywotwd.enfk5g713: SF Pro 12px/15.96px 600, #ffffff, ls 0.48px |
| Transition | none |
| Painted layers | div.css-15330ls.enfk5g70 352.0x251.0 bg #f5f6f8 border T:1px solid #3b3b3b / R:1px solid #3b3b3b / B:1px solid #3b3b3b / L:1px solid #3b3b3b r 10px; div.css-16hzl36.enfk5g712 99.7x24.0 bg #000000 r 20px; span.css-1djccpg.enfk5g72 85.5x26.1 bg #ffffff border T:1px solid #bdbdbd / R:1px solid #bdbdbd / B:1px solid #bdbdbd / L:1px solid #bdbdbd r 1024px; button.e11a0evt0.css-1hamzhx 318.0x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-name

Plan name. The plan name ("Premium") heading on a plan card.

Page: offers. Selector: `plan name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 85.47 x 26.09 |
| Padding | 4px 8px |
| Border | 1px solid #bdbdbd |
| Radius | 1024px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | SF Pro 14px/16.1px 600 |
| Letter spacing | 0.48px |
| Colour | #121212 |
| Transition | none |
| Painted layers | span.css-1djccpg.enfk5g72 85.5x26.1 bg #ffffff border T:1px solid #bdbdbd / R:1px solid #bdbdbd / B:1px solid #bdbdbd / L:1px solid #bdbdbd r 1024px |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. The "$xx/year" price line on a plan card.

Page: offers. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 35.05 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SF Pro 20px/24px 400 |
| Letter spacing | 0.24px |
| Colour | #575757 |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-perk

Plan perk. A perk bullet inside a plan card.

Page: offers. Selector: `plan perk li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 298 x 16.09 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SF Pro 14px/16.1px 400 |
| Letter spacing | 0.36px |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `plan-perk-default.png`.

#### plan-join

Join button. The "Join Premium" primary button on a plan card — links to checkout; measured, never followed.

Page: offers. Selector: `button[data-theme-key=button-primary] Join`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 318 x 32 | = | = | = |
| Padding | 9.6px 18px 5px 18px | = | = | = |
| Border | 1px solid #ff3a30 | = | = | = |
| Radius | 1024px | = | = | = |
| Background | #ff3a30 | #ffffff | = | #ffffff |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dotted #000000 offset 4px | = |
| Font | Lausanne 16px/32px 400 | = | = | = |
| Letter spacing | 0.72px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.e11a0evt0.css-1hamzhx 318.0x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | button.e11a0evt0.css-1hamzhx 318.0x32.0 bg #ffffff border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px | button.e11a0evt0.css-1hamzhx 318.0x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px outline 2px dotted #000000 offset 4px | button.e11a0evt0.css-1hamzhx 318.0x32.0 bg #ffffff border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-join-default.png`, `plan-join-hover.png`, `plan-join-focus-visible.png`, `plan-join-pressed.png`.

#### best-value

Best Value chip. The "Best Value" badge on the featured plan.

Page: offers. Selector: `Best Value`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 99.7 x 23.95 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SF Pro 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | label.css-ywotwd.enfk5g713: SF Pro 12px/15.96px 600, #ffffff, ls 0.48px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -49.8516, 0) |
| Painted layers | div.css-16hzl36.enfk5g712 99.7x24.0 bg #000000 r 20px |
| Ancestor paint | 1 up div.css-15330ls.enfk5g70 bg #f5f6f8 |
| How | at rest |

Crops: `best-value-default.png`.

#### perks-h2

Membership Perks heading. The "Membership Perks" section heading on the offers page.

Page: offers. Selector: `h2 Membership Perks`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1216 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SF Pro 32px/56px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `perks-h2-default.png`.

#### faq-h2

FAQ heading. The "Frequently Asked Questions" section heading.

Page: offers. Selector: `h2 FAQ`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SF Pro 32px/48px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `faq-h2-default.png`.

#### faq-header

FAQ accordion header. An FAQ collapsible header ("When will my magazine be delivered?") — a local UI toggle; the opened state was measured after clicking it.

Page: offers. Selector: `collapsible-header-button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 1200 x 56 | = | = | = | = |
| Padding | 20px 10px 0px 10px | = | = | = | = |
| Gap | normal 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = | = |
| Font | Lausanne 18px/20.7px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #000000 | = | = | = | = |
| Text node | span.css-105s8eq.eiafxuc2: SF Pro 20px/24px 700, #000000 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |
| Opacity | - | 0.8 | = | 0.8 | 0.8 |
| Painted layers | - | = | button.css-6kn1c7.eupr88z2 1200.0x56.0 outline 1px auto #101010 offset 0px | = | = |

Crops: `faq-header-default.png`, `faq-header-hover.png`, `faq-header-focus-visible.png`, `faq-header-pressed.png`, `faq-header-opened.png`.

#### faq-answer

FAQ answer. The answer panel revealed by the FAQ header toggle — the region its aria-controls names, or the sibling of the header heading when the attribute is absent; captured only when visible with text.

Page: offers. Selector: `aria-controls region, else header-heading sibling`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 284 |
| Padding | 0px 0px 4px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.css-lz1flv.eiafxuc3: SF Pro 16px/20px 400, #000000 |
| Transition | height 0.25s ease-in-out |
| How | at rest |

Crops: `faq-answer-default.png`.

#### gift-cta

Gift subscription CTA. The "GIVE A GIFT SUBSCRIPTION" ghost action — red text on white at rest, filling red on hover; measured, never followed.

Page: offers. Selector: `a[data-theme-key=button-primary] gift`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 322.28 x 40.59 | = | = | = |
| Padding | 9.6px 18px 5px 18px | = | = | = |
| Border | 1px solid #000000 @ 0 | 1px solid #ffffff | = | 1px solid #ffffff |
| Radius | 1024px | = | = | = |
| Background | #ffffff | #ff3a30 | = | #ff3a30 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dotted #000000 offset 4px | = |
| Font | Lausanne 20px/24px 400 | = | = | = |
| Letter spacing | 0.72px | = | = | = |
| Colour | #ff3a30 | #ffffff | = | #ffffff |
| Text node | span.css-0.e1h403oy12: Lausanne 20px/24px 400, #ff3a30, ls 0.72px | span.css-0.e1h403oy12: Lausanne 20px/24px 400, #ffffff, ls 0.72px | = | span.css-0.e1h403oy12: Lausanne 20px/24px 400, #ffffff, ls 0.72px |
| Transition | all 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.e1h403oy11.eglk2w90 322.3x40.6 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 1024px | a.e1h403oy11.eglk2w90 322.3x40.6 bg #ff3a30 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 1024px | a.e1h403oy11.eglk2w90 322.3x40.6 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 1024px outline 2px dotted #000000 offset 4px | a.e1h403oy11.eglk2w90 322.3x40.6 bg #ff3a30 border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gift-cta-default.png`, `gift-cta-hover.png`, `gift-cta-focus-visible.png`, `gift-cta-pressed.png`.

#### offers-fine

Renewal fine print. The "Cancel anytime…" fine print under the plan grid.

Page: offers. Selector: `renewal fine print`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1088 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | SF Pro 12px/16px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: SF Pro 12px/16px 700, #000000 |
| Transition | none |
| How | at rest |

Crops: `offers-fine-default.png`.

#### prem-h1

Premium hub heading. The heading on the /esq-premium-exclusive/ hub.

Page: premium. Selector: `premium h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 481 x 90 |
| Padding | 25px 40px 13px 40px |
| Border | none |
| Radius | 80px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 52px/52px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `prem-h1-default.png`.

#### prem-card

Premium story card. A member-exclusive story card on the premium hub.

Page: premium. Selector: `premium card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 72.8 |
| Padding | 20px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Lausanne 44px/52.8px 400, #000000 |
| Transition | none |
| Ancestor paint | 1 up section.css-1l0vm3i.e17377vn1 bg #f5f6f8 |
| How | at rest |

Crops: `prem-card-default.png`.

### Search

#### search-field

Search results field. The big search field on the results page (1115x48); focused and typed into then cleared — never submitted.

Page: search. Selector: `input.search-input-field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 1115 x 48 | = | = |
| Padding | 12px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Lausanne 14px/18.2px 400 | = | = |
| Letter spacing | 0.4px | = | = |
| Colour | #121212 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #757575, opacity 1 | = | = |
| Ancestor paint | 1 up div.css-1h43vkx.e1ow10r31 bg #ffffff | 1 up div.css-1h43vkx.e1ow10r31 bg #ffffff outline 1px solid #1c1c1c | 1 up div.css-1h43vkx.e1ow10r31 bg #ffffff outline 1px solid #1c1c1c |
| How | at rest | clicked into the field | typed "suits", then deleted; nothing sent |

Crops: `search-field-default.png`, `search-field-focused.png`, `search-field-filled.png`.

#### search-btn

Search submit. The round red search submit beside the field; measured, never pressed.

Page: search. Selector: `search submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 45 | = | = | = |
| Padding | 13px 12px 10px 12px | = | = | = |
| Border | 1px solid #ff3a30 | = | = | = |
| Radius | 32px | = | = | = |
| Background | #ff3a30 | #ffffff | = | #ffffff |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px dotted #000000 offset 4px | = |
| Font | Lausanne 14px/18.2px 400 | = | = | = |
| Letter spacing | 0.72px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.css-5asak4.eglk2w90 46.0x45.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 32px | button.css-5asak4.eglk2w90 46.0x45.0 bg #ffffff border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 32px | button.css-5asak4.eglk2w90 46.0x45.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 32px outline 2px dotted #000000 offset 4px | button.css-5asak4.eglk2w90 46.0x45.0 bg #ffffff border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-btn-default.png`, `search-btn-hover.png`, `search-btn-focus-visible.png`, `search-btn-pressed.png`.

#### search-count

Result count. The "N results for keyword <q>" line.

Page: search. Selector: `result count`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 253 x 28.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `search-count-default.png`.

#### search-sort

Sort control. The "Sort By: Relevance" popover trigger; measured, never toggled.

Page: search. Selector: `Sort By`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 238 x 51.19 | = | = | = |
| Padding | 12px | = | = | = |
| Border | 1px solid #d4d4d4 | = | = | = |
| Radius | 3px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Lausanne 14px/25.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 236px x 49.1875px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | button.e1t2wlxr1.css-1oix73v 238.0x51.2 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 3px | = | button.e1t2wlxr1.css-1oix73v 238.0x51.2 bg #ffffff border T:1px solid #d4d4d4 / R:1px solid #d4d4d4 / B:1px solid #d4d4d4 / L:1px solid #d4d4d4 r 3px; button::before.e1t2wlxr1.css-1oix73v 236pxx49.1875px outline 2px dotted #000000 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-sort-default.png`, `search-sort-hover.png`, `search-sort-focus-visible.png`, `search-sort-pressed.png`.

#### search-card

Result card. A search-result card: thumbnail, 40px Lausanne title, muted dek.

Page: search. Selector: `result card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 265 x 212.7 |
| Padding | 4px 5px 15px 5px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.css-1ns2ldj.e1otnc5c1: Lausanne 20px/24px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `search-card-default.png`.

#### search-title

Result title. A 40px Lausanne result title.

Page: search. Selector: `.custom-item-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 255 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 40px/48px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.css-1ns2ldj.e1otnc5c1: Lausanne 20px/24px 400, #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `search-title-default.png`.

#### search-more

See More button. The red-outline "See More" button at the foot of the results; measured, never pressed.

Page: search. Selector: `See More`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.61 x 38.3 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #121212 | = | = | = |
| Radius | 1024px | = | = | = |
| Background | #ffffff | #121212 @ 0.04 | = | #121212 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Lausanne 16px/20.3px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #ff3a30 | = | = | = |
| Text node | span.translate-y-(--comp-btn-lg-dim-offset-y).[text-decoration-line:var(--comp-btn-secondary-lg-type-decoration-line-mobile)]: Lausanne 16px/20.3px 400, #ff3a30, ls 0.2px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 101.6x38.3 bg #ffffff border T:1px solid #121212 / R:1px solid #121212 / B:1px solid #121212 / L:1px solid #121212 r 1024px | button.hds-do-not-use.inline-flex 101.6x38.3 bg #121212 @ 0.04 border T:1px solid #121212 / R:1px solid #121212 / B:1px solid #121212 / L:1px solid #121212 r 1024px | button.hds-do-not-use.inline-flex 101.6x38.3 bg #ffffff border T:1px solid #121212 / R:1px solid #121212 / B:1px solid #121212 / L:1px solid #121212 r 1024px outline 1px auto #101010 offset 0px | button.hds-do-not-use.inline-flex 101.6x38.3 bg #121212 @ 0.08 border T:1px solid #121212 / R:1px solid #121212 / B:1px solid #121212 / L:1px solid #121212 r 1024px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `search-more-default.png`, `search-more-hover.png`, `search-more-focus-visible.png`, `search-more-pressed.png`.

### Mobile (390 wide)

#### m-nav

Mobile navigation. The phone top chrome: red utility strip, hamburger, Esquire wordmark and search icon.

Page: mobile. Selector: `nav[data-tracking-id=topNav]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 154.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.translate-y-(--comp-btn-md-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-md-type-decoration-line-mobile)]: Lausanne 13px/18.2px 400, #121212, ls 0.4px |
| Transition | none |
| Icon | 16 x 16, colour #121212, fill #000000 |
| Painted layers | nav.css-1cbuarp.eju4swf4 390.0x154.2 bg #ffffff; div.css-zbfy27.eju4swf3 390.0x154.2 bg #ffffff; div.css-1rxqawy.e17hn77m2 390.0x32.0 bg #ff3a30; a.hds-do-not-use.inline-flex 125.0x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px; a.hds-do-not-use.inline-flex 96.6x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px; button.hds-do-not-use.inline-flex 42.0x42.0 bg #121212 @ 0 border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px |
| How | at rest |

Crops: `m-nav-default.png`.

#### m-hamburger

Hamburger. The hamburger button that toggles the side panel — a local UI toggle; the opened state was measured after clicking it.

Page: mobile. Selector: `mobile hamburger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 42 x 42 | = | = | = | = |
| Padding | 8px | = | = | = | = |
| Gap | 4px | = | = | = | = |
| Border | 1px solid #121212 @ 0 | = | = | 1px solid #121212 @ 0.08 | = |
| Radius | 1024px | = | = | = | = |
| Background | #121212 @ 0 | = | = | #121212 @ 0.08 | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = | = |
| Font | Lausanne 16px/20.3px 400 | = | = | = | = |
| Letter spacing | 0.2px | = | = | = | = |
| Colour | #121212 | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #121212, fill #000000 | = | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 42.0x42.0 bg #121212 @ 0 border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px | = | button.hds-do-not-use.inline-flex 42.0x42.0 bg #121212 @ 0 border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px outline 1px auto #e59700 offset 0px | button.hds-do-not-use.inline-flex 42.0x42.0 bg #121212 @ 0.08 border T:1px solid #121212 @ 0.08 / R:1px solid #121212 @ 0.08 / B:1px solid #121212 @ 0.08 / L:1px solid #121212 @ 0.08 r 1024px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-focus-visible.png`, `m-hamburger-pressed.png`, `m-hamburger-opened.png`.

#### m-logo

Mobile wordmark. The Esquire wordmark centred in the phone bar.

Page: mobile. Selector: `widest svg inside a nav anchor`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 192 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -96, 0) |
| Cursor | pointer |
| Icon | 192 x 48, colour #121212, fill #000000 |
| How | at rest |

Crops: `m-logo-default.png`.

#### m-search

Mobile search link. The search icon link in the phone bar; measured, never followed.

Page: mobile. Selector: `mobile search a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | sans-serif 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #121212, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.hds-do-not-use.no-underline 24.0x32.0 outline 1px auto #e59700 offset 1px | = |

Crops: `m-search-default.png`, `m-search-hover.png`, `m-search-focus-visible.png`, `m-search-pressed.png`.

#### m-story

Mobile story headline. A story headline in the phone feed.

Page: mobile. Selector: `mobile h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 36.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 28px/36.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Transition | none |
| How | at rest |

Crops: `m-story-default.png`.

#### m-eyebrow

Mobile eyebrow. The uppercase eyebrow over a phone headline.

Page: mobile. Selector: `mobile eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 40.61 x 13 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 13px/18.2px 400 |
| Letter spacing | 0.4px |
| Colour | #121212 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-eyebrow-default.png`.

#### m-byline

Mobile byline. A "BY <AUTHOR>" byline on the phone feed.

Page: mobile. Selector: `mobile byline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 114.41 x 12 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 12px/16.8px 400 |
| Letter spacing | 0.4px |
| Colour | #3b3b3b |
| Transition | none |
| Cursor | grab |
| How | at rest |

Crops: `m-byline-default.png`.

#### m-newsletter

Mobile newsletter. The newsletter band in the phone feed.

Page: mobile. Selector: `mobile newsletter form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 217.61 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lausanne 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | span.translate-y-(--comp-btn-lg-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-lg-type-decoration-line-mobile)]: Lausanne 16px/20.3px 400, #121212, ls 0.2px |
| Transition | none |
| Icon | 24 x 24, colour #575757, fill #000000 |
| Painted layers | div.flex.items-center 326.0x38.3 bg #ffffff border T:1px solid #757575 / R:1px solid #757575 / B:1px solid #757575 / L:1px solid #757575 r 1024px; button.hds-do-not-use.inline-flex 326.0x38.3 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px |
| How | at rest |

Crops: `m-newsletter-default.png`.

#### m-footer

Mobile footer. The site footer on the phone.

Page: mobile. Selector: `mobile footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 1272.7 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #121212 |
| Text node | a.hds-do-not-use.no-underline: Lausanne 14px/20.3px 400, #121212, ls 0.4px |
| Transition | none |
| Icon | 148 x 48, colour #121212, fill #000000 |
| Painted layers | a.ot-sdk-show-settings.ebnr9ku0 140.8x54.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest |

Crops: `m-footer-default.png`.

### Side panel and overlays

#### m-drawer

Side panel. The slide-in side panel the hamburger opens — section links with accordion chevrons; its links were never followed.

Page: mobile. Selector: `nav#sidepanel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f5f5f5 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.translate-y-(--comp-btn-md-dim-offset-y).[text-decoration-line:var(--comp-btn-primary-md-type-decoration-line-mobile)]: Lausanne 13px/18.2px 400, #121212, ls 0.4px |
| Transition | transform 0.2s linear |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #121212, fill #000000 |
| Painted layers | nav.new-sidepanel-menu.visible 390.0x844.0 bg #f5f5f5; div.css-1rxqawy.e17hn77m2 390.0x32.0 bg #ff3a30; a.hds-do-not-use.inline-flex 125.0x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px; a.hds-do-not-use.inline-flex 96.6x32.0 bg #ff3a30 border T:1px solid #ff3a30 / R:1px solid #ff3a30 / B:1px solid #ff3a30 / L:1px solid #ff3a30 r 1024px; button.hds-do-not-use.inline-flex 42.0x42.0 bg #121212 @ 0 border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px; div.flex.items-center 358.0x28.2 bg #ffffff border T:1px solid #757575 / R:1px solid #757575 / B:1px solid #757575 / L:1px solid #757575 r 1024px |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-drawer-close

Drawer close. The "Close Sidepanel" icon button; measured, never pressed.

Page: mobile. Selector: `sidepanel close`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42 x 42 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #121212 @ 0 | = | = | 1px solid #121212 @ 0.08 |
| Radius | 1024px | = | = | = |
| Background | #121212 @ 0 | = | = | #121212 @ 0.08 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | 1px auto #e59700 offset 0px |
| Font | Lausanne 16px/20.3px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #121212 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #121212, fill #000000 | = | = | = |
| Painted layers | button.hds-do-not-use.inline-flex 42.0x42.0 bg #121212 @ 0 border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px | = | button.hds-do-not-use.inline-flex 42.0x42.0 bg #121212 @ 0 border T:1px solid #121212 @ 0 / R:1px solid #121212 @ 0 / B:1px solid #121212 @ 0 / L:1px solid #121212 @ 0 r 1024px outline 1px auto #e59700 offset 0px | button.hds-do-not-use.inline-flex 42.0x42.0 bg #121212 @ 0.08 border T:1px solid #121212 @ 0.08 / R:1px solid #121212 @ 0.08 / B:1px solid #121212 @ 0.08 / L:1px solid #121212 @ 0.08 r 1024px outline 1px auto #e59700 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-drawer-close-default.png`, `m-drawer-close-hover.png`, `m-drawer-close-focus-visible.png`, `m-drawer-close-pressed.png`.

#### m-drawer-link

Drawer section link. A section link inside the side panel; measured, never followed.

Page: mobile. Selector: `sidepanel a`. States: .

Not found on the page at capture time.

## Transitions declared in the readable stylesheets

esquire.com serves its /api/styles.css bundle same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- article: `opacity var(--video-transition)`, `var(--video-transition-overlay-fade)`, `transform var(--video-transition)`, `opacity var(--video-transition),transform var(--video-transition)`, `opacity var(--video-transition),visibility var(--video-transition)`, `width var(--video-transition)`, `0.2s`, `color 0.2s`, `opacity 0.3s linear`, `transform 0.2s linear`, `background 0.3s ease-in-out, color 0.3s ease-in-out`, `background-color 0.2s linear`

- essay: `opacity var(--video-transition)`, `var(--video-transition-overlay-fade)`, `transform var(--video-transition)`, `opacity var(--video-transition),transform var(--video-transition)`, `opacity var(--video-transition),visibility var(--video-transition)`, `width var(--video-transition)`, `0.2s`, `color 0.2s`, `opacity 0.3s linear`, `transform 0.2s linear`, `background 0.3s ease-in-out, color 0.3s ease-in-out`, `background-color 0.2s linear`

- home: `opacity 0.3s linear`, `transform 0.2s linear`, `background 0.3s ease-in-out, color 0.3s ease-in-out`, `background-color 0.2s linear`, `padding 0.3s linear, background-color 0.2s linear`, `color 0.2s linear`, `transform 0.25s ease-in-out`, `opacity 0.2s linear`, `none`, `transform 0.3s ease-in-out`, `max-height 650ms ease-out`, `top var(--rr-ad-transition-duration, 0s) ease-in`

- offers: `opacity 0.3s linear`, `transform 0.2s linear`, `background 0.3s ease-in-out, color 0.3s ease-in-out`, `background-color 0.2s linear`, `padding 0.3s linear, background-color 0.2s linear`, `color 0.2s linear`, `transform 0.25s ease-in-out`, `opacity 0.2s linear`, `transform 0.3s ease-in-out`, `max-height 650ms ease-out`, `0.3s ease-in-out`, `transform 250ms ease-in-out`

- premium: `opacity 0.3s linear`, `transform 0.2s linear`, `background 0.3s ease-in-out, color 0.3s ease-in-out`, `background-color 0.2s linear`, `padding 0.3s linear, background-color 0.2s linear`, `color 0.2s linear`, `transform 0.25s ease-in-out`, `opacity 0.2s linear`, `transform 0.3s ease-in-out`, `max-height 650ms ease-out`, `none`, `color 0.3s ease-in-out`

- search: `opacity 0.3s linear`, `transform 0.2s linear`, `background 0.3s ease-in-out, color 0.3s ease-in-out`, `background-color 0.2s linear`, `padding 0.3s linear, background-color 0.2s linear`, `color 0.2s linear`, `transform 0.25s ease-in-out`, `opacity 0.2s linear`, `transform 0.3s ease-in-out`, `max-height 650ms ease-out`, `0.3s ease-in-out`, `transform 150ms ease-in-out`

- section: `opacity 0.3s linear`, `transform 0.2s linear`, `background 0.3s ease-in-out, color 0.3s ease-in-out`, `background-color 0.2s linear`, `padding 0.3s linear, background-color 0.2s linear`, `color 0.2s linear`, `transform 0.25s ease-in-out`, `opacity 0.2s linear`, `transform 0.3s ease-in-out`, `max-height 650ms ease-out`, `0.3s ease-in-out`, `none`
