# Digg component measurements

Computed styles read from digg.com on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the trending feed, /tech, a story page, /u/wired, /login and /sign-up, with the Dark group read after the sidebar pill cycled to dark — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Left sidebar

#### sb-home

Sidebar item (active). The Home row in the left sidebar — icon + label pill, painted selected on the feed; measured, never followed.

Page: home. Selector: `a.peer/menu-button Home`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 231 x 40 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #f0f0f5 | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 600 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 | = | = | = |
| Text node | span.site-rail-label.whitespace-nowrap: roobert 14px/20px 600, #161617, ls -0.091px | = | = | = |
| Transition | width, height, padding 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.peer/menu-button.group/menu-button 231.0x40.0 bg #f0f0f5 r 3.35544e+07px | = | a.peer/menu-button.group/menu-button 231.0x40.0 bg #f0f0f5 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sb-home-default.png`, `sb-home-hover.png`, `sb-home-focus-visible.png`, `sb-home-pressed.png`.

#### sb-tech

Sidebar item. A category row in the left sidebar (Technology, with its badge icon); measured, never followed.

Page: home. Selector: `a.peer/menu-button Technology`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 231 x 40 | = | = | = |
| Padding | 4px 12px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #f0f0f5 | = | #f0f0f5 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 600 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 | = | = | = |
| Text node | span.site-rail-label.whitespace-nowrap: roobert 14px/20px 600, #161617, ls -0.091px | = | = | = |
| Transition | width, height, padding 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.peer/menu-button.group/menu-button 231.0x40.0 bg #f0f0f5 r 3.35544e+07px | a.peer/menu-button.group/menu-button 231.0x40.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.peer/menu-button.group/menu-button 231.0x40.0 bg #f0f0f5 r 3.35544e+07px |

Crops: `sb-tech-default.png`, `sb-tech-hover.png`, `sb-tech-focus-visible.png`, `sb-tech-pressed.png`.

#### sb-pill

Theme pill. The sidebar theme pill (System / Light / Dark cycle); pressed is CDP-forced — the real cycle is exercised by the dark pass.

Page: home. Selector: `theme pill button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 231 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ababbf | = |
| Radius | 26px | = | = | = |
| Background | #f0f0f5 | #dbe3f6 | = | #dbe3f6 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #161617 | = | = | = |
| Painted layers | button.group/button.inline-flex 231.0x40.0 bg #f0f0f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | button.group/button.inline-flex 231.0x40.0 bg #dbe3f6 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | button.group/button.inline-flex 231.0x40.0 bg #f0f0f5 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.group/button.inline-flex 231.0x40.0 bg #dbe3f6 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sb-pill-default.png`, `sb-pill-hover.png`, `sb-pill-focus-visible.png`, `sb-pill-pressed.png`.

#### sb-login

Log in link. The sidebar Log in link to /login; measured, never followed.

Page: home. Selector: `Log in`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 231 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ababbf | = |
| Radius | 26px | = | = | = |
| Background | #f0f0f5 | #dbe3f6 | = | #dbe3f6 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group/button.inline-flex 231.0x40.0 bg #f0f0f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 231.0x40.0 bg #dbe3f6 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 231.0x40.0 bg #f0f0f5 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 231.0x40.0 bg #dbe3f6 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sb-login-default.png`, `sb-login-hover.png`, `sb-login-focus-visible.png`, `sb-login-pressed.png`.

#### sb-signup

Sign up CTA. The blue Sign up button at the foot of the sidebar; measured, never followed.

Page: home. Selector: `Sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 231 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ababbf | = |
| Radius | 26px | = | = | = |
| Background | #1c66eb | #1c66eb @ 0.8 | = | #1c66eb @ 0.801409 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group/button.inline-flex 231.0x40.0 bg #1c66eb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 231.0x40.0 bg #1c66eb @ 0.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 231.0x40.0 bg #1c66eb border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 231.0x40.0 bg #1c66eb @ 0.801409 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sb-signup-default.png`, `sb-signup-hover.png`, `sb-signup-focus-visible.png`, `sb-signup-pressed.png`.

#### cat-tech-active

Sidebar item (selected). The Technology sidebar row on /tech — the painted selected state of a category item.

Page: tech. Selector: `sidebar Technology (active)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 231 x 40 |
| Padding | 4px 12px |
| Gap | 12px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #f0f0f5 |
| Box shadow | none |
| Outline | none |
| Font | roobert 14px/20px 600 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | span.site-rail-label.whitespace-nowrap: roobert 14px/20px 600, #161617, ls -0.091px |
| Transition | width, height, padding 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Cursor | pointer |
| Painted layers | a.peer/menu-button.group/menu-button 231.0x40.0 bg #f0f0f5 r 3.35544e+07px |
| How | at rest |

Crops: `cat-tech-active-default.png`.

#### st-crumb

Category crumb. The category chip link beside the back button; measured, never followed.

Page: story. Selector: `story crumb`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 170.55 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ababbf | = |
| Radius | 26px | = | = | = |
| Background | #f0f0f5 | #dbe3f6 | = | #dbe3f6 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group/button.inline-flex 170.5x40.0 bg #f0f0f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 170.5x40.0 bg #dbe3f6 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 170.5x40.0 bg #f0f0f5 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 170.5x40.0 bg #dbe3f6 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-crumb-default.png`, `st-crumb-hover.png`, `st-crumb-focus-visible.png`, `st-crumb-pressed.png`.

### Feed controls

#### feed-trending

Sort dropdown. The Trending sort trigger over the feed; its opened state is a local dropdown of sort options.

Page: home. Selector: `Trending button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 105.28 x 36 | = | = | = | = |
| Padding | 8px 12px | = | = | = | = |
| Gap | 6px | = | = | = | = |
| Border | 1px solid #e5e5e5 | = | 1px solid #ababbf | = | = |
| Radius | 26px | = | = | = | = |
| Background | #e5e5e5 @ 0.3 | = | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | roobert 14px/20px 400 | = | = | = | = |
| Letter spacing | -0.091px | = | = | = | = |
| Colour | #161617 | = | = | = | = |
| Text node | span: roobert 14px/20px 400, #161617, ls -0.091px | = | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #161617 @ 0.7 | = | = | = | = |
| Painted layers | button.flex.w-fit 105.3x36.0 bg #e5e5e5 @ 0.3 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 26px | = | button.flex.w-fit 105.3x36.0 bg #e5e5e5 @ 0.3 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `feed-trending-default.png`, `feed-trending-hover.png`, `feed-trending-focus-visible.png`, `feed-trending-pressed.png`, `feed-trending-opened.png`.

#### feed-compact

Density toggle. The Compact density control beside the sort dropdown; measured, never toggled.

Page: home. Selector: `Compact button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 64 x 36 | = | - | = |
| Padding | 8px 12px | = | - | = |
| Gap | 6px | = | - | = |
| Border | 1px solid #e5e5e5 | = | - | = |
| Radius | 26px | = | - | = |
| Background | #e5e5e5 @ 0.3 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | roobert 14px/20px 400 | = | - | = |
| Letter spacing | -0.091px | = | - | = |
| Colour | #161617 | = | - | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #161617 | = | - | = |
| Painted layers | button.flex.w-fit 64.0x36.0 bg #e5e5e5 @ 0.3 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 26px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `feed-compact-default.png`, `feed-compact-hover.png`, `feed-compact-pressed.png`.

#### cat-title

Category heading. The Technology feed heading.

Page: tech. Selector: `category h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 656 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 30px/36px 700 |
| Letter spacing | -0.39px |
| Colour | #161617 |
| Transition | none |
| How | at rest |

Crops: `cat-title-default.png`.

### Story card

#### post-card

Story card. A feed story card: category chip, headline, summary, vote pill, comment link and source cluster, thumbnail at right.

Page: home. Selector: `post item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 183 |
| Padding | 14px 16px |
| Gap | 14px |
| Border | 1px solid #000000 @ 0 |
| Radius | 18px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | span.inline-flex.items-center: roobert 12px/16px 600, #161617, ls -0.06px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 12 x 12, colour #161617 @ 0.7 |
| Painted layers | div.group/item.flex 704.0x183.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div.group/button-group.flex 77.9x32.0 bg #fdfdff border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; a.group/button.inline-flex 32.0x32.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px; span.group/avatar.flex 24.0x24.0 r 3.35544e+07px shadow #fdfdff 0px 0px 0px 1.5px |
| How | at rest |

Crops: `post-card-default.png`.

#### post-headline

Card headline. The card’s stretched headline link (data-post-headline); measured, never followed.

Page: home. Selector: `data-post-headline`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 536 x 48 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | roobert 16px/24px 600 | = | - | = |
| Letter spacing | -0.12px | = | - | = |
| Colour | #161617 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `post-headline-default.png`, `post-headline-hover.png`, `post-headline-pressed.png`.

#### post-summary

Card summary. The one-two line summary under the headline.

Page: home. Selector: `card p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 536 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `post-summary-default.png`.

#### post-vote

Vote pill. The digg-it vote pill on the card (icon + odometer count); pressed is CDP-forced — a real press would cast a vote.

Page: home. Selector: `vote button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 24 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px 26px 26px 3.35544e+07px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | - | = |
| Outline | none | = | - | = |
| Font | roobert 14px/20px 500 | = | - | = |
| Letter spacing | -0.091px | = | - | = |
| Colour | #161617 @ 0.7 | #161617 | - | #161617 |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 12 x 12, colour #161617 @ 0.7 | 12 x 12, colour #161617 | - | 12 x 12, colour #161617 |
| ::after | 77.8594px x 42px, absolute, bg #000000 @ 0, radius 0px | = | - | = |
| Painted layers | button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px | = | - | = |
| Ancestor paint | 1 up div.group/button-group.flex bg #fdfdff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `post-vote-default.png`, `post-vote-hover.png`, `post-vote-pressed.png`.

#### post-comment

Comment link. The comment-count link on the card; measured, never followed.

Page: home. Selector: `comment link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | - | = |
| Padding | 0px | = | - | = |
| Border | 1px solid #000000 @ 0.08 | = | - | = |
| Radius | 26px | = | - | = |
| Background | transparent | #e5e5e5 @ 0.5 | - | #e5e5e5 @ 0.5 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | roobert 14px/20px 500 | = | - | = |
| Letter spacing | -0.091px | = | - | = |
| Colour | #161617 | = | - | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #161617 @ 0.7 | = | - | = |
| Painted layers | a.group/button.inline-flex 32.0x32.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px | a.group/button.inline-flex 32.0x32.0 bg #e5e5e5 @ 0.5 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px | - | a.group/button.inline-flex 32.0x32.0 bg #e5e5e5 @ 0.5 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `post-comment-default.png`, `post-comment-hover.png`, `post-comment-pressed.png`.

#### post-avatars

Source avatar. A source avatar in the card’s cluster (popover anchor, initials); measured, never followed.

Page: home. Selector: `source avatar`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | roobert 14px/14px 400 | = | - | = |
| Letter spacing | -0.091px | = | - | = |
| Colour | #161617 | = | - | = |
| Text node | span.flex.size-full: roobert 12px/16px 400, #161617 @ 0.7, ls -0.06px | = | - | = |
| Transition | color, text-decoration-color, opacity 0.15s ease-out | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | span.group/avatar.flex 24.0x24.0 r 3.35544e+07px shadow #fdfdff 0px 0px 0px 1.5px; span.flex.size-full 24.0x24.0 bg #f0f0f5 r 3.35544e+07px; span.pointer-events-none.absolute 24.0x24.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.08 0px 0px 0px 1px inset, #000000 @ 0.12 0px 2px 4px 0px inset | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `post-avatars-default.png`, `post-avatars-hover.png`, `post-avatars-pressed.png`.

#### post-sources

Sources link. The "N Sources, updated Xm ago" meta link; measured, never followed.

Page: home. Selector: `sources meta link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 87 x 16 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 2px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | roobert 14px/20px 600 | = | - | = |
| Letter spacing | -0.091px | = | - | = |
| Colour | #161617 @ 0.7 | = | - | = |
| Transition | color, text-decoration-color, opacity 0.15s ease-out | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `post-sources-default.png`, `post-sources-hover.png`, `post-sources-pressed.png`.

#### post-thumb

Card thumbnail. The story’s right-side thumbnail inside the card.

Page: home. Selector: `card img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 120 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #000000 @ 0 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `post-thumb-default.png`.

#### cat-card

Category card. A story card on the Technology feed — same anatomy as the trending card.

Page: tech. Selector: `category post item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 160 |
| Padding | 14px 16px |
| Gap | 14px |
| Border | 1px solid #000000 @ 0 |
| Radius | 18px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | h3: roobert 16px/24px 600, #161617, ls -0.12px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 12 x 12, colour #161617 @ 0.7 |
| Painted layers | div.group/item.flex 704.0x160.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div.group/button-group.flex 77.9x32.0 bg #fdfdff border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; a.group/button.inline-flex 32.0x32.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px; span.group/avatar.flex 24.0x24.0 r 3.35544e+07px shadow #fdfdff 0px 0px 0px 1.5px |
| How | at rest |

Crops: `cat-card-default.png`.

### Right rail

#### rail-contribs

Top Contributors. The right-rail "Top Contributors" ranked panel.

Page: home. Selector: `contributors panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376 x 352 |
| Padding | 24px 0px |
| Gap | 16px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 18px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | h2: roobert 16px/24px 600, #161617, ls -0.12px |
| Transition | none |
| Painted layers | div.group/card.flex 376.0x352.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.group/item.flex 326.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; span.group/badge.inline-flex 36.0x20.0 bg #f0f0f5 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px; span::after.group/avatar.relative 24pxx24px border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px; span.flex.size-full 24.0x24.0 bg #f0f0f5 r 3.35544e+07px; a.group/item.flex 326.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px |
| How | at rest |

Crops: `rail-contribs-default.png`.

#### rail-posts

Top Posts panel. The right-rail "Top Posts Yesterday" list with thumbnails.

Page: home. Selector: `top posts panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376 x 556 |
| Padding | 24px 0px |
| Gap | 16px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 18px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | h2: roobert 16px/24px 600, #161617, ls -0.12px |
| Transition | none |
| Icon | 12 x 12, colour #161617 @ 0.7 |
| Painted layers | div.group/card.flex 376.0x556.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.group/item.flex 356.0x106.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; a.relative.isolate 80.0x60.0 bg #f0f0f5 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.group/item.flex 356.0x86.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; a.relative.isolate 80.0x60.0 bg #f0f0f5 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.group/item.flex 356.0x106.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px |
| How | at rest |

Crops: `rail-posts-default.png`.

### Footer

#### site-footer

Site footer. The mono sitemap footer (About / Contact / Privacy Policy / Terms / Community Guidelines / © digg).

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376 x 56 |
| Padding | 8px 0px 16px 0px |
| Gap | normal 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 12px/16px 400 |
| Letter spacing | -0.06px |
| Colour | #161617 @ 0.7 |
| Text node | a.underline-offset-4.hover:text-foreground: roobert 12px/16px 400, #161617 @ 0.7, ls -0.06px |
| Transition | none |
| How | at rest |

Crops: `site-footer-default.png`.

### Dark theme

#### d-card

Card (dark). A feed story card measured with the dark theme painted via the sidebar pill.

Page: dark. Selector: `post item (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 183 |
| Padding | 14px 16px |
| Gap | 14px |
| Border | 1px solid #000000 @ 0 |
| Radius | 18px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #fdfdff |
| Text node | span.inline-flex.items-center: roobert 12px/16px 600, #fdfdff, ls -0.06px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 12 x 12, colour #fdfdff @ 0.7 |
| Painted layers | div.group/item.flex 704.0x183.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div.group/button-group.flex 77.9x32.0 bg #161617 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; a.group/button.inline-flex 32.0x32.0 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 26px; span.group/avatar.flex 24.0x24.0 r 3.35544e+07px shadow #161617 0px 0px 0px 1.5px |
| How | at rest |

Crops: `d-card-default.png`.

#### d-headline

Headline (dark). The card headline under the dark theme.

Page: dark. Selector: `data-post-headline (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 536 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 16px/24px 600 |
| Letter spacing | -0.12px |
| Colour | #fdfdff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `d-headline-default.png`.

#### d-vote

Vote pill (dark). The digg-it vote pill under the dark theme.

Page: dark. Selector: `vote button (dark)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px 26px 26px 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1c66eb @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #fdfdff @ 0.7 | #fdfdff | #fdfdff | #fdfdff |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #fdfdff @ 0.7 | 12 x 12, colour #fdfdff | 12 x 12, colour #fdfdff | 12 x 12, colour #fdfdff |
| ::after | 77.8594px x 42px, absolute, bg #000000 @ 0, radius 0px | = | 34px x 36px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px | = | button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1c66eb @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px | = |
| Ancestor paint | 1 up div.group/button-group.flex bg #161617 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-vote-default.png`, `d-vote-hover.png`, `d-vote-focus-visible.png`, `d-vote-pressed.png`.

#### d-signup

Sign up (dark). The blue Sign up CTA under the dark theme.

Page: dark. Selector: `Sign up (dark)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 231 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #1c66eb | = |
| Radius | 26px | = | = | = |
| Background | #1c66eb | #1c66eb @ 0.8 | = | #1c66eb @ 0.8 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1c66eb @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group/button.inline-flex 231.0x40.0 bg #1c66eb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 231.0x40.0 bg #1c66eb @ 0.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px | a.group/button.inline-flex 231.0x40.0 bg #1c66eb border T:1px solid #1c66eb / R:1px solid #1c66eb / B:1px solid #1c66eb / L:1px solid #1c66eb r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1c66eb @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | a.group/button.inline-flex 231.0x40.0 bg #1c66eb @ 0.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-signup-default.png`, `d-signup-hover.png`, `d-signup-focus-visible.png`, `d-signup-pressed.png`.

#### d-trending

Sort dropdown (dark). The Trending sort trigger under the dark theme.

Page: dark. Selector: `Trending (dark)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 105.28 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | 1px solid #ffffff @ 0.15 | = | 1px solid #1c66eb | = |
| Radius | 26px | = | = | = |
| Background | #ffffff @ 0.045 | #ffffff @ 0.075 | = | #ffffff @ 0.075 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1c66eb @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 400 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #fdfdff | = | = | = |
| Text node | span: roobert 14px/20px 400, #fdfdff, ls -0.091px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fdfdff @ 0.7 | = | = | = |
| Painted layers | button.flex.w-fit 105.3x36.0 bg #ffffff @ 0.045 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 26px | button.flex.w-fit 105.3x36.0 bg #ffffff @ 0.075 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 26px | button.flex.w-fit 105.3x36.0 bg #ffffff @ 0.045 border T:1px solid #1c66eb / R:1px solid #1c66eb / B:1px solid #1c66eb / L:1px solid #1c66eb r 26px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #1c66eb @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | button.flex.w-fit 105.3x36.0 bg #ffffff @ 0.075 border T:1px solid #ffffff @ 0.15 / R:1px solid #ffffff @ 0.15 / B:1px solid #ffffff @ 0.15 / L:1px solid #ffffff @ 0.15 r 26px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `d-trending-default.png`, `d-trending-hover.png`, `d-trending-focus-visible.png`, `d-trending-pressed.png`.

#### d-rail

Rail panel (dark). The Top Contributors panel under the dark theme.

Page: dark. Selector: `rail panel (dark)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376 x 352 |
| Padding | 24px 0px |
| Gap | 16px |
| Border | 1px solid #ffffff @ 0.08 |
| Radius | 18px |
| Background | #1c1c1f |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fdfdff @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #fdfdff |
| Text node | h2: roobert 16px/24px 600, #fdfdff, ls -0.12px |
| Transition | none |
| Painted layers | div.group/card.flex 376.0x352.0 bg #1c1c1f border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fdfdff @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; a.group/item.flex 326.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; span.group/badge.inline-flex 36.0x20.0 bg #242424 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px; span::after.group/avatar.relative 24pxx24px border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 3.35544e+07px; span.flex.size-full 24.0x24.0 bg #242424 r 3.35544e+07px; a.group/item.flex 326.0x46.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px |
| How | at rest |

Crops: `d-rail-default.png`.

### Story page

#### st-kicker

REPORT kicker. The tracked-out REPORT label over the story headline.

Page: story. Selector: `REPORT label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 16px/24px 400 |
| Letter spacing | normal |
| Colour | #161617 |
| Text node | span: roobert 12px/16px 600, #161617 @ 0.7, ls 1.2px |
| Transition | none |
| How | at rest |

Crops: `st-kicker-default.png`.

#### st-h1

Story headline. The serif story headline.

Page: story. Selector: `story h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 36px/40px 700 |
| Letter spacing | -0.36px |
| Colour | #161617 |
| Transition | none |
| How | at rest |

Crops: `st-h1-default.png`.

#### st-summary

Story summary. The one-two line summary under the headline.

Page: story. Selector: `story summary`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 20px/28px 400 |
| Letter spacing | -0.15px |
| Colour | #161617 @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `st-summary-default.png`.

#### st-vote

digg it button. The "digg it" vote pill under the headline (icon + count); pressed is CDP-forced — a real press would cast a vote.

Page: story. Selector: `digg it button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.33 x 44 | = | = | 134.18 x 42.68 |
| Padding | 3px 11px 3px 3px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #1c66eb @ 0.2 | 1px solid #1c66eb @ 0.3 | = | 1px solid #1c66eb @ 0.3 |
| Radius | 999px | = | = | = |
| Background | #fdfdff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 | = | = | = |
| Text node | span.aYZIsW_capsule.flex: roobert 12px/16px 600, #1c66eb, ls -0.06px | = | = | = |
| Transition | background-color, border-color, color, scale 0.28s, 0.28s, 0.28s, 0.16s cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.77, 0, 0.175, 1), cubic-bezier(0.23, 1, 0.32, 1) delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #1c66eb | = | = | 11.64 x 11.64, colour #1c66eb |
| Painted layers | button.group/button.inline-flex 138.3x44.0 bg #fdfdff border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 999px; span.aYZIsW_capsule.flex 86.0x36.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px | button.group/button.inline-flex 138.3x44.0 bg #fdfdff border T:1px solid #1c66eb @ 0.3 / R:1px solid #1c66eb @ 0.3 / B:1px solid #1c66eb @ 0.3 / L:1px solid #1c66eb @ 0.3 r 999px; span.aYZIsW_capsule.flex 86.0x36.0 bg #1c66eb @ 0.1 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px | = | button.group/button.inline-flex 134.2x42.7 bg #fdfdff border T:1px solid #1c66eb @ 0.3 / R:1px solid #1c66eb @ 0.3 / B:1px solid #1c66eb @ 0.3 / L:1px solid #1c66eb @ 0.3 r 999px; span.aYZIsW_capsule.flex 83.4x34.9 bg #1c66eb @ 0.1 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `st-vote-default.png`, `st-vote-hover.png`, `st-vote-focus-visible.png`, `st-vote-pressed.png`.

#### st-sources

Sources meta. The "N Sources, first seen Xh ago" meta cluster; measured, never followed.

Page: story. Selector: `sources meta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 86 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fdfdff 0px 0px 0px 2px, #ababbf 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 600 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 @ 0.7 | = | = | = |
| Transition | color, text-decoration-color, opacity 0.15s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.rounded-xs.font-semibold 86.0x16.0 r 2px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fdfdff 0px 0px 0px 2px, #ababbf 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = |

Crops: `st-sources-default.png`, `st-sources-hover.png`, `st-sources-focus-visible.png`, `st-sources-pressed.png`.

#### st-stat

Stat card. The right-rail stat card — TODAY'S RANK over COMBINED VIEWS and the like/comment/save counts.

Page: story. Selector: `stat card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376 x 384 |
| Padding | 24px 0px |
| Gap | 0px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 18px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | span: roobert 12px/16px 600, #161617 @ 0.7, ls 1.2px |
| Transition | none |
| Icon | 12 x 12, colour #161617 @ 0.7 |
| Painted layers | div.group/card.flex 376.0x384.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; div.px-(--card-spacing).border-t 374.0x210.0 border T:1px solid #000000 @ 0.08; div.mt-5.border-t 326.0x69.0 border T:1px solid #000000 @ 0.08 |
| How | at rest |

Crops: `st-stat-default.png`.

#### st-srclist

Sources list. The right-rail "N Sources" list of source posts.

Page: story. Selector: `sources list`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 376 x 246 |
| Padding | 24px 0px |
| Gap | 16px |
| Border | 1px solid #000000 @ 0.08 |
| Radius | 18px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | span: roobert 12px/16px 600, #161617 @ 0.7, ls 1.2px |
| Transition | none |
| Icon | 12 x 12, colour #161617 @ 0.7 |
| Painted layers | div.group/card.flex 376.0x246.0 bg #ffffff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 18px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #161617 @ 0.1 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span::after.group/avatar.relative 24pxx24px border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px; span.flex.size-full 24.0x24.0 bg #f0f0f5 r 3.35544e+07px; span::after.group/avatar.relative 24pxx24px border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px; span.flex.size-full 24.0x24.0 bg #f0f0f5 r 3.35544e+07px; span::after.group/avatar.relative 24pxx24px border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px |
| How | at rest |

Crops: `st-srclist-default.png`.

#### st-tldr

TLDR label. The tracked TLDR section label over the summary prose.

Page: story. Selector: `TLDR label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 605 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 10px/16px 600 |
| Letter spacing | 1px |
| Colour | #161617 @ 0.7 |
| Transition | none |
| How | at rest |

Crops: `st-tldr-default.png`.

#### st-para

TLDR paragraph. A body paragraph in the TLDR section.

Page: story. Selector: `story p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 605 x 189 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 18px/31.5px 500 |
| Letter spacing | normal |
| Colour | #161617 |
| Transition | none |
| How | at rest |

Crops: `st-para-default.png`.

### Source profile

#### pf-name

Profile name. The source profile heading (@wired).

Page: profile. Selector: `profile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 61.06 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 20px/28px 600 |
| Letter spacing | -0.19px |
| Colour | #161617 |
| Transition | none |
| How | at rest |

Crops: `pf-name-default.png`.

#### pf-card

Profile story card. A story card in the source’s profile feed.

Page: profile. Selector: `profile post item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 704 x 183 |
| Padding | 14px 16px |
| Gap | 14px |
| Border | 1px solid #000000 @ 0 |
| Radius | 18px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | span.inline-flex.items-center: roobert 12px/16px 600, #161617, ls -0.06px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 12 x 12, colour #161617 @ 0.7 |
| Painted layers | div.group/item.flex 704.0x183.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div.group/button-group.flex 77.9x32.0 bg #fdfdff border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; a.group/button.inline-flex 32.0x32.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px; span.group/avatar.flex 24.0x24.0 r 3.35544e+07px shadow #fdfdff 0px 0px 0px 1.5px |
| How | at rest |

Crops: `pf-card-default.png`.

### Sign-in / sign-up

#### lg-h1

Sign-in heading. "Welcome back!" — the Clerk sign-in card heading.

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 353 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 24px/32px 600 |
| Letter spacing | -0.264px |
| Colour | #161617 |
| Transition | none |
| Ancestor paint | 3 up div.cl-card.rounded-lg shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `lg-h1-default.png`.

#### lg-google

Google OAuth. The "Continue with Google" outline button; measured, never followed.

Page: login. Selector: `oauth google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 353 x 36 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 16px | = | = | = |
| Border | 1px solid #000000 @ 0.08 | = | 1px solid #ababbf | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fdfdff | #f0f0f5 | = | #f0f0f5 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 @ 0.62 | = | = | = |
| Text node | span.cl-socialButtonsBlockButtonText.cl-socialButtonsBlockButtonText__google: roobert 13px/18px 500, #161617 @ 0.62 | = | = | = |
| Transition | background-color, background, border-color, color, fill, stroke, opacity, box-shadow, transform 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | background-color, background, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cl-socialButtonsBlockButton.cl-button 353.0x36.0 bg #fdfdff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.cl-socialButtonsBlockButton.cl-button 353.0x36.0 bg #f0f0f5 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | button.cl-socialButtonsBlockButton.cl-button 353.0x36.0 bg #fdfdff border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | button.cl-socialButtonsBlockButton.cl-button 353.0x36.0 bg #f0f0f5 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `lg-google-default.png`, `lg-google-hover.png`, `lg-google-focus-visible.png`, `lg-google-pressed.png`.

#### lg-x

X OAuth. The "Continue with X / Twitter" outline button; measured, never followed.

Page: login. Selector: `oauth x`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 353 x 36 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 16px | = | = | = |
| Border | 1px solid #000000 @ 0.08 | = | 1px solid #ababbf | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #fdfdff | #f0f0f5 | = | #f0f0f5 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 @ 0.62 | = | = | = |
| Text node | span.cl-socialButtonsBlockButtonText.cl-socialButtonsBlockButtonText__x: roobert 13px/18px 500, #161617 @ 0.62 | = | = | = |
| Transition | background-color, background, border-color, color, fill, stroke, opacity, box-shadow, transform 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | background-color, background, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cl-socialButtonsBlockButton.cl-button 353.0x36.0 bg #fdfdff border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.cl-socialButtonsProviderIcon.cl-providerIcon 16.0x16.0 bg #161617 | button.cl-socialButtonsBlockButton.cl-button 353.0x36.0 bg #f0f0f5 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.cl-socialButtonsProviderIcon.cl-providerIcon 16.0x16.0 bg #161617 | button.cl-socialButtonsBlockButton.cl-button 353.0x36.0 bg #fdfdff border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px; span.cl-socialButtonsProviderIcon.cl-providerIcon 16.0x16.0 bg #161617 | button.cl-socialButtonsBlockButton.cl-button 353.0x36.0 bg #f0f0f5 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; span.cl-socialButtonsProviderIcon.cl-providerIcon 16.0x16.0 bg #161617 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `lg-x-default.png`, `lg-x-hover.png`, `lg-x-focus-visible.png`, `lg-x-pressed.png`.

#### lg-email

Email field. The "Enter your email address" identifier field; the filled state types an address then deletes it — nothing is submitted.

Page: login. Selector: `#identifier-field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 353 x 36 | = | = |
| Padding | 4px 10px | = | = |
| Border | 1px solid #e5e5e5 | 1px solid #ababbf | 1px solid #ababbf |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | roobert 14px/20px 400 | = | = |
| Letter spacing | -0.091px | = | = |
| Colour | #161617 | = | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #161617 @ 0.7, opacity 1 | = | = |
| Painted layers | input.cl-formFieldInput.cl-input 353.0x36.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.cl-formFieldInput.cl-input 353.0x36.0 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | input.cl-formFieldInput.cl-input 353.0x36.0 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `lg-email-default.png`, `lg-email-focused.png`, `lg-email-filled.png`.

#### lg-pass

Password field. The password field; focused via a click-in, never filled.

Page: login. Selector: `#password-field`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 197 x 36 | = |
| Padding | 4px 10px | = |
| Border | 1px solid #e5e5e5 | 1px solid #ababbf |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = |
| Font | roobert 14px/20px 400 | = |
| Letter spacing | -0.091px | = |
| Colour | #161617 | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #161617 @ 0.7, opacity 1 | = |
| Painted layers | input.cl-formFieldInput.cl-input 197.0x36.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.cl-formFieldInput.cl-input 197.0x36.0 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field |

Crops: `lg-pass-default.png`, `lg-pass-focused.png`.

#### lg-continue

Continue button. The blue Continue submit; hover/focus measured, never pressed — it would submit the sign-in.

Page: login. Selector: `Continue button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 353 x 36 | = | = |
| Padding | 0px 10px | = | = |
| Gap | 6px | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ababbf |
| Radius | 3.35544e+07px | = | = |
| Background | #1c66eb | #1c66eb @ 0.8 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | roobert 14px/20px 500 | = | = |
| Letter spacing | -0.091px | = | = |
| Colour | #ffffff | = | = |
| Text node | span.cl-internal-2iusy0: roobert 14px/20px 500, #ffffff, ls -0.091px | = | = |
| Transition | background-color, background, border-color, color, fill, stroke, opacity, box-shadow, transform 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | background-color, background, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease |
| Cursor | pointer | = | = |
| Icon | 0 x 0, colour #ffffff | = | = |
| ::after | auto x auto, absolute, bg #000000 @ 0 linear-gradient(#ffffff @ 0.11 0%, #000000 @ 0 100%), radius 3.35544e+07px | = | = |
| Painted layers | button.cl-formButtonPrimary.cl-button 353.0x36.0 bg #1c66eb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button::after.cl-formButtonPrimary.cl-button autoxauto image linear-gradient(#ffffff @ 0.11 0%, #000000 @ 0 100%) r 3.35544e+07px | button.cl-formButtonPrimary.cl-button 353.0x36.0 bg #1c66eb @ 0.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button::after.cl-formButtonPrimary.cl-button autoxauto image linear-gradient(#ffffff @ 0.11 0%, #000000 @ 0 100%) r 3.35544e+07px | button.cl-formButtonPrimary.cl-button 353.0x36.0 bg #1c66eb border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; button::after.cl-formButtonPrimary.cl-button autoxauto image linear-gradient(#ffffff @ 0.11 0%, #000000 @ 0 100%) r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `lg-continue-default.png`, `lg-continue-hover.png`, `lg-continue-focus-visible.png`.

#### lg-signup

Sign up link. The "Don’t have an account? Sign up" link under the form; measured, never followed.

Page: login. Selector: `login sign up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46 x 17.98 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #ababbf @ 0.5 offset 1px | = |
| Font | roobert 13px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c66eb | #3a7bee | = | #1359d7 |
| Transition | color, text-decoration-color, opacity 0.15s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 3 up div.cl-cardBox.shadow-sm shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.cl-footerActionLink.🔒️ 46.0x18.0 outline 1px auto #ababbf @ 0.5 offset 1px | = |

Crops: `lg-signup-default.png`, `lg-signup-hover.png`, `lg-signup-focus-visible.png`, `lg-signup-pressed.png`.

#### su-h1

Sign-up heading. The Clerk sign-up card heading.

Page: signup. Selector: `signup h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 353 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 24px/32px 600 |
| Letter spacing | -0.264px |
| Colour | #161617 |
| Transition | none |
| Ancestor paint | 3 up div.cl-card.rounded-lg shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `su-h1-default.png`.

#### su-email

Sign-up email. The sign-up identifier field; the filled state types an address then deletes it — nothing is submitted.

Page: signup. Selector: `signup field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 353 x 36 | = | = |
| Padding | 4px 10px | = | = |
| Border | 1px solid #e5e5e5 | 1px solid #ababbf | 1px solid #ababbf |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | roobert 14px/20px 400 | = | = |
| Letter spacing | -0.091px | = | = |
| Colour | #161617 | = | = |
| Transition | color, box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #161617 @ 0.7, opacity 1 | = | = |
| Painted layers | input.cl-formFieldInput.cl-input 353.0x36.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.cl-formFieldInput.cl-input 353.0x36.0 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | input.cl-formFieldInput.cl-input 353.0x36.0 border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `su-email-default.png`, `su-email-focused.png`, `su-email-filled.png`.

#### su-continue

Sign-up Continue. The sign-up Continue submit; hover/focus measured, never pressed.

Page: signup. Selector: `signup continue`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 353 x 36 | = | = |
| Padding | 0px 10px | = | = |
| Gap | 6px | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ababbf |
| Radius | 3.35544e+07px | = | = |
| Background | #1c66eb | #1c66eb @ 0.8 | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = |
| Font | roobert 14px/20px 500 | = | = |
| Letter spacing | -0.091px | = | = |
| Colour | #ffffff | = | = |
| Text node | span.cl-internal-2iusy0: roobert 14px/20px 500, #ffffff, ls -0.091px | = | = |
| Transition | background-color, background, border-color, color, fill, stroke, opacity, box-shadow, transform 0.1s cubic-bezier(0.4, 0, 0.2, 1) | = | background-color, background, border-color, color, fill, stroke, opacity, box-shadow, transform 0.2s ease |
| Cursor | pointer | = | = |
| Icon | 0 x 0, colour #ffffff | = | = |
| ::after | auto x auto, absolute, bg #000000 @ 0 linear-gradient(#ffffff @ 0.11 0%, #000000 @ 0 100%), radius 3.35544e+07px | = | = |
| Painted layers | button.cl-formButtonPrimary.cl-button 353.0x36.0 bg #1c66eb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button::after.cl-formButtonPrimary.cl-button autoxauto image linear-gradient(#ffffff @ 0.11 0%, #000000 @ 0 100%) r 3.35544e+07px | button.cl-formButtonPrimary.cl-button 353.0x36.0 bg #1c66eb @ 0.8 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; button::after.cl-formButtonPrimary.cl-button autoxauto image linear-gradient(#ffffff @ 0.11 0%, #000000 @ 0 100%) r 3.35544e+07px | button.cl-formButtonPrimary.cl-button 353.0x36.0 bg #1c66eb border T:1px solid #ababbf / R:1px solid #ababbf / B:1px solid #ababbf / L:1px solid #ababbf r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; button::after.cl-formButtonPrimary.cl-button autoxauto image linear-gradient(#ffffff @ 0.11 0%, #000000 @ 0 100%) r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `su-continue-default.png`, `su-continue-hover.png`, `su-continue-focus-visible.png`.

### Mobile (390 wide)

#### m-bar

Mobile top bar. The phone top bar (digg wordmark + menu trigger).

Page: mobile. Selector: `mobile bar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 107 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f8f8fb |
| Box shadow | none |
| Outline | none |
| Font | roobert 16px/24px 400 |
| Letter spacing | normal |
| Colour | #161617 |
| Text node | a.group/button.inline-flex: roobert 14px/20px 500, #ffffff, ls -0.091px |
| Transition | none |
| Icon | 21 x 21, colour #161617 @ 0.7 |
| Painted layers | header.sticky.top-0 390.0x107.0 bg #f8f8fb; button.group/button.inline-flex 40.0x40.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px; nav.border-b.border-sidebar-border 390.0x51.0 bg #f8f8fb border B:1px solid #000000 @ 0.08; a.group/button.inline-flex 92.6x36.0 bg #1c66eb border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 26px; a.group/button.inline-flex 131.1x36.0 bg #e5e5e5 @ 0.3 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px; a.group/button.inline-flex 105.5x36.0 bg #e5e5e5 @ 0.3 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px |
| Ancestor paint | 1 up main.relative.flex bg #fdfdff |
| How | at rest |

Crops: `m-bar-default.png`.

#### m-card

Mobile card. A story card at 390px.

Page: mobile. Selector: `mobile post item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 207 |
| Padding | 14px 16px |
| Gap | 14px |
| Border | 1px solid #000000 @ 0 |
| Radius | 18px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 14px/20px 400 |
| Letter spacing | -0.091px |
| Colour | #161617 |
| Text node | span.inline-flex.items-center: roobert 12px/16px 600, #161617, ls -0.06px |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.1s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 12 x 12, colour #161617 @ 0.7 |
| Painted layers | div.group/item.flex 390.0x207.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 18px; div.group/button-group.flex 77.9x32.0 bg #fdfdff border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px; a.group/button.inline-flex 32.0x32.0 border T:1px solid #000000 @ 0.08 / R:1px solid #000000 @ 0.08 / B:1px solid #000000 @ 0.08 / L:1px solid #000000 @ 0.08 r 26px; span.group/avatar.flex 24.0x24.0 r 3.35544e+07px shadow #fdfdff 0px 0px 0px 1.5px |
| How | at rest |

Crops: `m-card-default.png`.

#### m-vote

Mobile vote pill. The digg-it vote pill at 390px.

Page: mobile. Selector: `mobile vote`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px 26px 26px 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | roobert 14px/20px 500 | = | = | = |
| Letter spacing | -0.091px | = | = | = |
| Colour | #161617 @ 0.7 | = | #161617 | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 12 x 12, colour #161617 @ 0.7 | = | 12 x 12, colour #161617 | = |
| ::after | 77.8594px x 42px, absolute, bg #000000 @ 0, radius 0px | = | 34px x 36px, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px | = | button.group/button.inline-flex 32.0x24.0 r 3.35544e+07px 26px 26px 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ababbf @ 0.5 0px 0px 0px 3px, #000000 @ 0 0px 0px 0px 0px; span.relative.flex 32.0x24.0 bg #1c66eb @ 0.05 border T:1px solid #1c66eb @ 0.2 / R:1px solid #1c66eb @ 0.2 / B:1px solid #1c66eb @ 0.2 / L:1px solid #1c66eb @ 0.2 r 3.35544e+07px | = |
| Ancestor paint | 1 up div.group/button-group.flex bg #fdfdff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-vote-default.png`, `m-vote-hover.png`, `m-vote-focus-visible.png`, `m-vote-pressed.png`.

#### m-footer

Mobile footer. The phone footer.

Page: mobile. Selector: `mobile footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 48 |
| Padding | 0px |
| Gap | normal 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | roobert 12px/16px 400 |
| Letter spacing | -0.06px |
| Colour | #161617 @ 0.7 |
| Text node | a.underline-offset-4.hover:text-foreground: roobert 12px/16px 400, #161617 @ 0.7, ls -0.06px |
| Transition | none |
| How | at rest |

Crops: `m-footer-default.png`.

## Transitions declared in the readable stylesheets

digg.com serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- dark: `transform 0.34s cubic-bezier(0.3, 1.35, 0.6, 1), background-color 0.26s ease-out, border-color 0.26s ease-out, box-shadow 0.26s ease-out`, `background-color 0.15s ease-out, color 0.15s ease-out`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1), translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms, translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `grid-template-columns 0.2s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1)`

- home: `transform 0.34s cubic-bezier(0.3, 1.35, 0.6, 1), background-color 0.26s ease-out, border-color 0.26s ease-out, box-shadow 0.26s ease-out`, `background-color 0.15s ease-out, color 0.15s ease-out`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1), translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms, translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `grid-template-columns 0.2s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1)`

- login: `transform 0.34s cubic-bezier(0.3, 1.35, 0.6, 1), background-color 0.26s ease-out, border-color 0.26s ease-out, box-shadow 0.26s ease-out`, `background-color 0.15s ease-out, color 0.15s ease-out`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1), translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms, translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `grid-template-columns 0.2s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1)`

- profile: `transform 0.34s cubic-bezier(0.3, 1.35, 0.6, 1), background-color 0.26s ease-out, border-color 0.26s ease-out, box-shadow 0.26s ease-out`, `background-color 0.15s ease-out, color 0.15s ease-out`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1), translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms, translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `grid-template-columns 0.2s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1)`

- signup: `transform 0.34s cubic-bezier(0.3, 1.35, 0.6, 1), background-color 0.26s ease-out, border-color 0.26s ease-out, box-shadow 0.26s ease-out`, `background-color 0.15s ease-out, color 0.15s ease-out`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1), translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms, translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `grid-template-columns 0.2s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1)`

- story: `transform 0.34s cubic-bezier(0.3, 1.35, 0.6, 1), background-color 0.26s ease-out, border-color 0.26s ease-out, box-shadow 0.26s ease-out`, `background-color 0.15s ease-out, color 0.15s ease-out`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1), translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms, translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `grid-template-columns 0.2s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1)`

- tech: `transform 0.34s cubic-bezier(0.3, 1.35, 0.6, 1), background-color 0.26s ease-out, border-color 0.26s ease-out, box-shadow 0.26s ease-out`, `background-color 0.15s ease-out, color 0.15s ease-out`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), border-color 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1), translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms, translate 0.2s cubic-bezier(0.23, 1, 0.32, 1)`, `transform 0.28s cubic-bezier(0.77, 0, 0.175, 1)`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1)`, `none`, `background-color 0.28s cubic-bezier(0.77, 0, 0.175, 1), color 0.28s cubic-bezier(0.77, 0, 0.175, 1), scale 0.16s cubic-bezier(0.23, 1, 0.32, 1)`, `grid-template-columns 0.2s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.18s cubic-bezier(0.23, 1, 0.32, 1) 40ms, transform 0.24s cubic-bezier(0.32, 0.72, 0, 1) 40ms`, `opacity 0.12s cubic-bezier(0.23, 1, 0.32, 1), transform 0.18s cubic-bezier(0.32, 0.72, 0, 1)`
