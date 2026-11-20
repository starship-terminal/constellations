# Discord component measurements

Computed styles read from discord.com on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the marketing pages (/, /download, /nitro) and the app surfaces (/servers discovery, a /servers/<slug> detail page, /login, /register), where the marketing chrome sits inside a .theme-light root and the app content paints .theme-dark.theme-darker — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Marketing chrome

#### mk-nav

Marketing nav. The fixed marketing top bar — Discord wordmark, section links, Log In pill.

Page: home. Selector: `header.nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Ginto Normal 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div: Abcgintodiscord 16px/22px 500, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | a.skip-link.w-inline-block 205.0x48.0 bg #35ed7e r 12px; div.nav_dd_content-wr.isnew 0.0x0.0 bg #5865f2 r 40px; div.nav_dd_content-wr.isnew 0.0x0.0 bg #5865f2 r 40px; div.nav_dd_link-group.is_2025 0.0x0.0 border R:1px solid #ffffff @ 0.1; div.nav_dd_content-wr.isnew 0.0x0.0 bg #5865f2 r 40px; div.nav_dd_content-wr.isnew 0.0x0.0 bg #5865f2 r 40px |
| How | at rest |

Crops: `mk-nav-default.png`.

#### mk-nav-download

Nav link. The Download nav link; measured, never followed.

Page: home. Selector: `header.nav a Download`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110 x 39.2 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | 1px | = |
| Background | transparent | #5865f2 | = | #5865f2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset -2px | = |
| Font | Abcgintodiscord 16px/19.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | font-variation-settings 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.nav_link 110.0x39.2 bg #5865f2 r 12px | a.nav_link 110.0x39.2 r 1px outline 2px solid #ffffff offset -2px | a.nav_link 110.0x39.2 bg #5865f2 r 12px |

Crops: `mk-nav-download-default.png`, `mk-nav-download-hover.png`, `mk-nav-download-focus-visible.png`, `mk-nav-download-pressed.png`.

#### mk-nav-drop

Nav dropdown. The Discover nav dropdown trigger; measured, never opened through.

Page: home. Selector: `nav Discover`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 117 x 39.2 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ABC Ginto Normal 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | span.menu-title: Abcgintodiscord 16px/19.2px 500, #ffffff | = | - | = |
| Transition | none | = | - | = |
| Icon | 16 x 16, colour #ffffff | = | - | = |
| Painted layers | div.nav_dd_content-wr.isnew 0.0x0.0 bg #5865f2 r 40px | div.nav_dd_trigger.w-dropdown-toggle 117.0x39.2 bg #5865f2 r 12px; div.nav_dd_content-wr.isnew 203.0x167.2 bg #5865f2 r 40px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `mk-nav-drop-default.png`, `mk-nav-drop-hover.png`, `mk-nav-drop-pressed.png`.

#### mk-nav-login

Nav Log In. The white Log In pill in the nav; measured, never followed.

Page: home. Selector: `nav Log In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.5 x 39.19 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | 1px | = |
| Background | #ffffff | #c7c8ce | = | #c7c8ce |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #5865f2 offset 4px | = |
| Font | Abcgintodiscord 16px/19.2px 500 | = | = | = |
| Letter spacing | 0.25px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | background-color 0.25s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button-nav.login-button-js 80.5x39.2 bg #ffffff r 16px | a.button-nav.login-button-js 80.5x39.2 bg #c7c8ce r 16px | a.button-nav.login-button-js 80.5x39.2 bg #ffffff r 1px outline 2px solid #5865f2 offset 4px | a.button-nav.login-button-js 80.5x39.2 bg #c7c8ce r 16px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mk-nav-login-default.png`, `mk-nav-login-hover.png`, `mk-nav-login-focus-visible.png`, `mk-nav-login-pressed.png`.

### Marketing hero

#### mk-h1

Hero display. "GROUP CHAT THAT’S ALL FUN & GAMES" — the hero display headline in Ggsans.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 491.19 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Abcgintodiscordnord 56px/48px 700 |
| Letter spacing | -0.56px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `mk-h1-default.png`.

#### mk-lede

Hero lede. The hero supporting paragraph.

Page: home. Selector: `p.hero-p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 491.19 x 104 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Abcgintodiscord 20px/26px 400 |
| Letter spacing | 0.32px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `mk-lede-default.png`.

#### mk-cta-download

Hero primary CTA. The "Download for …" white button; hover/focus measured, never followed (it would start a download).

Page: home. Selector: `hero Download`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 262.5 x 65 | = | = | = |
| Padding | 15px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | #c7c8ce | = | #c7c8ce |
| Box shadow | none | #000000 @ 0.2 0px 8px 15px 0px | = | #000000 @ 0.2 0px 8px 15px 0px |
| Outline | none | = | = | = |
| Font | Abcgintodiscord 20px/26px 400 | = | = | = |
| Letter spacing | 0.25px | = | = | = |
| Colour | #23272a | = | = | = |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #23272a, fill #000000 | = | = | = |
| Painted layers | button.button-ZGMevK.buttonWhite-1M-wED 262.5x65.0 bg #ffffff r 12px | button.button-ZGMevK.buttonWhite-1M-wED 262.5x65.0 bg #c7c8ce r 12px shadow #000000 @ 0.2 0px 8px 15px 0px | = | button.button-ZGMevK.buttonWhite-1M-wED 262.5x65.0 bg #c7c8ce r 12px shadow #000000 @ 0.2 0px 8px 15px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mk-cta-download-default.png`, `mk-cta-download-hover.png`, `mk-cta-download-focus-visible.png`, `mk-cta-download-pressed.png`.

#### mk-cta-open

Hero secondary CTA. The "Open Discord in your browser" brand-fill button; measured, never followed.

Page: home. Selector: `hero Open Discord`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 324 x 65 | = | = | = |
| Padding | 19.5px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #5865f2 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Abcgintodiscord 20px/26px 400 | = | = | = |
| Letter spacing | 0.25px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 324px x 65px, absolute, bg #000000 @ 0 linear-gradient(#000000 @ 0 0px, #1f1d5d 130%), radius 0px | = | = | = |
| Painted layers | button.button-ZGMevK.buttonBrand-24ECS3 324.0x65.0 bg #5865f2 r 12px; button::after.button-ZGMevK.buttonBrand-24ECS3 324pxx65px image linear-gradient(#000000 @ 0 0px, #1f1d5d 130%) | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mk-cta-open-default.png`, `mk-cta-open-hover.png`, `mk-cta-open-focus-visible.png`, `mk-cta-open-pressed.png`.

### Marketing page

#### dl-h1

Download heading. "Download Discord wherever you hang out" — the download page heading.

Page: download. Selector: `download h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 924 x 194.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Abcgintodiscordnord 72px/64.8px 700 |
| Letter spacing | -2.16px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `dl-h1-default.png`.

#### dl-cta

Download CTA. A platform download button; measured, never followed.

Page: download. Selector: `a.download-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 228.5 x 48 | = | = | = |
| Padding | 15px 24px 14px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px solid #5865f2 offset 1px | = |
| Font | ABC Ginto Normal 16px/20.8px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.btn_text: ABC Ginto Normal 16px/20.8px 500, #ffffff | = | = | = |
| Transition | all, background-color 0.3s, 0.4s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff, fill #000000 | = | = | = |
| Ancestor paint | 1 up div.btn_wr.is_2025 bg #5865f2 @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.btn.download-button 228.5x48.0 r 12px outline 1px solid #5865f2 offset 1px | = |

Crops: `dl-cta-default.png`, `dl-cta-hover.png`, `dl-cta-focus-visible.png`, `dl-cta-pressed.png`.

#### nt-h1

Nitro heading. "UNLOCK A WORLD OF PERKS WITH NITRO" — the Nitro page display heading.

Page: nitro. Selector: `nitro h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 788 x 194.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Abcgintodiscordnord 72px/64.8px 700 |
| Letter spacing | -2.16px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `nt-h1-default.png`.

#### nt-card

Nitro plan card. A Nitro plan/perk card on the marketing page.

Page: nitro. Selector: `nitro plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 590 x 683.38 |
| Padding | 32px 32px 56px 32px |
| Border | none |
| Radius | 96px |
| Background | #1a1a1e |
| Box shadow | #452a7c @ 0.1 0px 2px 32px 0px |
| Outline | none |
| Font | Ggsans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.nitro_heading-banner.is-new: Abcgintodiscordnord 36px/36px 700, #ffffff, ls -0.36px |
| Transition | none |
| Painted layers | div.nitro-card 590.0x683.4 bg #1a1a1e r 96px shadow #452a7c @ 0.1 0px 2px 32px 0px; div.nitro-card-img.w-background-video 526.0x459.4 r 96px shadow #452a7c @ 0.1 0px 2px 32px 0px |
| How | at rest |

Crops: `nt-card-default.png`.

#### nt-cta

Nitro CTA. A Nitro subscribe button; measured, never followed.

Page: nitro. Selector: `nitro cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121 x 48 | = | = | = |
| Padding | 14.4px 24px 13.6px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | 1px | = |
| Background | #ffffff | #c7c8ce | #c7c8ce | #c7c8ce |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #5865f2 offset 4px | = |
| Font | Abcgintodiscord 16px/20.8px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.btn_text: Abcgintodiscord 16px/20.8px 500, #000000 | = | = | = |
| Transition | background-color 0.4s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-global.is-primary 121.0x48.0 bg #ffffff r 12px | a.btn-global.is-primary 121.0x48.0 bg #c7c8ce r 12px | a.btn-global.is-primary 121.0x48.0 bg #c7c8ce r 1px outline 2px solid #5865f2 offset 4px | a.btn-global.is-primary 121.0x48.0 bg #c7c8ce r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nt-cta-default.png`, `nt-cta-hover.png`, `nt-cta-focus-visible.png`, `nt-cta-pressed.png`.

### Server discovery

#### ds-h1

Discovery heading. "DISCOVERABLE SERVERS" — the display-lg heading on the app discovery page (painted under .theme-dark.theme-darker).

Page: servers. Selector: `h1.display-lg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Ginto Discord Nord 56px/56px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `ds-h1-default.png`.

#### ds-search

Search box. The "Search servers for games and interests" field wrapper on discovery.

Page: servers. Selector: `.searchBox`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #efeff1 |
| Text node | span.text-muted.size12_meTJex: gg sans 12px/16px 400, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ffffff, fill #000000 |
| Painted layers | div.searchBox__7pJSN.searchBarContainer__J-bNz 640.0x64.0 bg #ffffff @ 0.12 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest |

Crops: `ds-search-default.png`.

#### ds-search-input

Search input. The discovery search input; the filled state types "fortnite" then deletes it — the query runs client-side, nothing is submitted or signed in.

Page: servers. Selector: `input.searchBoxInput`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 570 x 32 | = | 419.61 x 32 |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 3px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | gg sans 16px/16px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | border-color 0.2s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #ffffff @ 0.75, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "fortnite", then deleted; nothing sent |
| Ancestor paint | - | 2 up div.searchBox__7pJSN.searchBarContainer__J-bNz bg #ffffff @ 0.2 outline 2px solid #6aa8f4 | 2 up div.searchBox__7pJSN.searchBarContainer__J-bNz bg #ffffff @ 0.2 outline 2px solid #6aa8f4 |

Crops: `ds-search-input-default.png`, `ds-search-input-focused.png`, `ds-search-input-filled.png`.

#### ds-tab

Category pill. A category filter pill (Gaming) — a real link to /servers/gaming; measured, never followed.

Page: servers. Selector: `a.categoryTab Gaming`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 146.13 x 57.03 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6aa8f4 offset 2px | = |
| Font | gg sans 24px/23.04px 500 | = | = | = |
| Letter spacing | -0.48px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.fullSizeLabel_zXq3Fx.label_zXq3Fx: gg sans 24px/23.04px 500, #ffffff, ls -0.48px | = | = | = |
| Transition | none | = | = | = |
| Opacity | 0.5 | - | - | - |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | a.link_vQTvMr.categoryTab_zXq3Fx 146.1x57.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px | = | a.link_vQTvMr.categoryTab_zXq3Fx 146.1x57.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px outline 2px solid #6aa8f4 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ds-tab-default.png`, `ds-tab-hover.png`, `ds-tab-focus-visible.png`, `ds-tab-pressed.png`.

#### ds-tab-all

Category pill (All). The "All" category pill — the selected state of the filter row.

Page: servers. Selector: `a.categoryTab All`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.56 x 57.03 | = | = | = |
| Padding | 16px 24px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #97979f @ 0.12 | = | = | = |
| Radius | 12px | = | = | = |
| Background | #97979f @ 0.16 | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(120px) | = | = | = |
| Outline | none | = | 2px solid #6aa8f4 offset 2px | = |
| Font | gg sans 24px/23.04px 500 | = | = | = |
| Letter spacing | -0.48px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.fullSizeLabel_zXq3Fx.label_zXq3Fx: gg sans 24px/23.04px 500, #ffffff, ls -0.48px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff, fill #000000 | = | = | = |
| ::before | 94.5625px x 55.0312px, absolute, bg #000000 @ 0 radial-gradient(70% 60% at 50% 0px, #5865f2 @ 0.5 0px, #000000 @ 0 70%), radius 0px | = | = | = |
| Painted layers | a.link_vQTvMr.categoryTab_zXq3Fx 96.6x57.0 bg #97979f @ 0.16 border T:1px solid #97979f @ 0.12 / R:1px solid #97979f @ 0.12 / B:1px solid #97979f @ 0.12 / L:1px solid #97979f @ 0.12 r 12px; a::before.link_vQTvMr.categoryTab_zXq3Fx 94.5625pxx55.0312px image radial-gradient(70% 60% at 50% 0px, #5865f2 @ 0.5 0px, #000000 @ 0 70%) | = | a.link_vQTvMr.categoryTab_zXq3Fx 96.6x57.0 bg #97979f @ 0.16 border T:1px solid #97979f @ 0.12 / R:1px solid #97979f @ 0.12 / B:1px solid #97979f @ 0.12 / L:1px solid #97979f @ 0.12 r 12px outline 2px solid #6aa8f4 offset 2px; a::before.link_vQTvMr.categoryTab_zXq3Fx 94.5625pxx55.0312px image radial-gradient(70% 60% at 50% 0px, #5865f2 @ 0.5 0px, #000000 @ 0 70%) | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ds-tab-all-default.png`, `ds-tab-all-hover.png`, `ds-tab-all-focus-visible.png`, `ds-tab-all-pressed.png`.

#### gs-h1

Category heading. The Gaming category discovery page heading.

Page: gaming. Selector: `gaming h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Ginto Discord Nord 56px/56px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `gs-h1-default.png`.

#### gs-tab-gaming

Category pill (selected). The Gaming pill on /servers/gaming — the painted selected state.

Page: gaming. Selector: `a.categoryTab Gaming (selected)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 146.13 x 57.03 |
| Padding | 16px 24px |
| Gap | 4px |
| Border | 1px solid #97979f @ 0.12 |
| Radius | 12px |
| Background | #97979f @ 0.16 |
| Box shadow | none |
| Backdrop filter | blur(120px) |
| Outline | none |
| Font | gg sans 24px/23.04px 500 |
| Letter spacing | -0.48px |
| Colour | #ffffff |
| Text node | span.fullSizeLabel_zXq3Fx.label_zXq3Fx: gg sans 24px/23.04px 500, #ffffff, ls -0.48px |
| Transition | none |
| Cursor | pointer |
| Icon | 16 x 16, colour #ffffff, fill #000000 |
| ::before | 144.125px x 55.0312px, absolute, bg #000000 @ 0 radial-gradient(70% 60% at 50% 0px, #5865f2 @ 0.5 0px, #000000 @ 0 70%), radius 0px |
| Painted layers | a.link_vQTvMr.categoryTab_zXq3Fx 146.1x57.0 bg #97979f @ 0.16 border T:1px solid #97979f @ 0.12 / R:1px solid #97979f @ 0.12 / B:1px solid #97979f @ 0.12 / L:1px solid #97979f @ 0.12 r 12px; a::before.link_vQTvMr.categoryTab_zXq3Fx 144.125pxx55.0312px image radial-gradient(70% 60% at 50% 0px, #5865f2 @ 0.5 0px, #000000 @ 0 70%) |
| How | at rest |

Crops: `gs-tab-gaming-default.png`.

### Server card

#### sc-card

Server card. A discoverable-server card — banner art, icon, name, verified badge, description, member counts; hover measured, never followed.

Page: servers. Selector: `.searchListItem`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 322 x 362 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | gg sans 16px/18.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #efeff1 | = |
| Text node | a.link_vQTvMr.linkDefault_vQTvMr: gg sans 20px/24px 600, #fbfbfb | = |
| Transition | none | = |
| Icon | 16 x 16, colour #23a559, fill #000000 | = |
| Painted layers | article.guildItemContainer_OnY3sU 322.0x362.0 bg #202024 border T:1px solid #97979f @ 0.12 / R:1px solid #97979f @ 0.12 / B:1px solid #97979f @ 0.12 / L:1px solid #97979f @ 0.12 r 8px; div.listIconContainer_OnY3sU 59.7x59.7 bg #202024 r 12.7893px; div.dotOnline_U3tHuW 8.0x8.0 bg #43b581 r 50%; div.dotOffline_U3tHuW.dotOnline_U3tHuW 8.0x8.0 bg #c4c9ce r 50% | article.guildItemContainer_OnY3sU 322.0x362.0 bg #242429 border T:1px solid #97979f @ 0.44 / R:1px solid #97979f @ 0.44 / B:1px solid #97979f @ 0.44 / L:1px solid #97979f @ 0.44 r 8px shadow #000000 @ 0.14 0px 1px 4px 0px; div.listIconContainer_OnY3sU 59.7x59.7 bg #242429 r 12.7893px; div.dotOnline_U3tHuW 8.0x8.0 bg #43b581 r 50%; div.dotOffline_U3tHuW.dotOnline_U3tHuW 8.0x8.0 bg #c4c9ce r 50% |
| How | at rest | mouse hover |

Crops: `sc-card-default.png`, `sc-card-hover.png`.

#### sc-name

Server name. The server name line inside the card, with its verified check.

Page: servers. Selector: `card name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 99 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 20px/24px 600 |
| Letter spacing | normal |
| Colour | #fbfbfb |
| Text node | a.link_vQTvMr.linkDefault_vQTvMr: gg sans 20px/24px 600, #fbfbfb |
| Transition | none |
| How | at rest |

Crops: `sc-name-default.png`.

#### sc-members

Member counts. The "N Online · N Members" line — the green presence dot plus counts.

Page: servers. Selector: `card members`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 115 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 14px/18px 400 |
| Letter spacing | normal |
| Colour | #efeff1 |
| Transition | none |
| How | at rest |

Crops: `sc-members-default.png`.

#### sc-icon

Server icon. The squircle server icon overlapping the card banner.

Page: servers. Selector: `card img.listIconImage`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 51.19 x 51.19 |
| Padding | 0px |
| Border | none |
| Radius | 8.53333px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #efeff1 |
| Transition | none |
| How | at rest |

Crops: `sc-icon-default.png`.

### Server detail

#### sv-banner

Server banner. The server detail page banner art.

Page: server. Selector: `server banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 600 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #efeff1 |
| Transition | none |
| How | at rest |

Crops: `sv-banner-default.png`.

#### sv-name

Server name. The server title with the verified badge — display type.

Page: server. Selector: `server h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 264 x 32.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Ginto Discord Nord 28px/32.2px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.name_MZwbsN: ABC Ginto Discord Nord 28px/32.2px 700, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #23a559, fill #000000 |
| How | at rest |

Crops: `sv-name-default.png`.

#### sv-members

Member counts. The "N Online · N Members" line under the name.

Page: server. Selector: `server members`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 89 x 18.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 14px/18.2px 500 |
| Letter spacing | normal |
| Colour | #96979e |
| Transition | none |
| How | at rest |

Crops: `sv-members-default.png`.

#### sv-join

Join CTA. The brand-fill "Join the Conversation" button; hover/focus measured, never followed — joining needs an account.

Page: server. Selector: `Join button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 320 x 48 | = | = |
| Padding | 0px 24px | = | = |
| Gap | 8px | = | = |
| Border | none | = | = |
| Radius | 12px | = | = |
| Background | #5865f2 | #4752c4 | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | gg sans 16px/20.8px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | background-color, color, box-shadow 0.2s ease-in-out | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.button_vOYBES.overlayFocusRing_vOYBES 320.0x48.0 bg #5865f2 r 12px | a.button_vOYBES.overlayFocusRing_vOYBES 320.0x48.0 bg #4752c4 r 12px | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `sv-join-default.png`, `sv-join-hover.png`, `sv-join-focus-visible.png`.

#### sv-share

Share button. The Share button under the member counts; measured, never pressed.

Page: server. Selector: `Share button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6aa8f4 offset 2px | = |
| Font | gg sans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #efeff1 | = | = | = |
| Text node | span.body-md/medium_vADpuW.triggerLabel__sNXK6: gg sans 16px/20px 500, #efeff1 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #efeff1 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.trigger__sNXK6 320.0x44.0 r 12px outline 2px solid #6aa8f4 offset 2px | = |

Crops: `sv-share-default.png`, `sv-share-hover.png`, `sv-share-focus-visible.png`, `sv-share-pressed.png`.

#### sv-chip

Category chip. A category chip in the detail sidebar; measured, never followed.

Page: server. Selector: `category chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 122 x 38 | = | = | = |
| Padding | 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #97979f @ 0.12 | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(12px) | = | = | = |
| Outline | none | = | = | = |
| Font | gg sans 14px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #efeff1 | = | = | = |
| Text node | div.colorHeaderSecondary_O8xN8T.size14_meTJex: gg sans 14px/18px 500, #efeff1 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.link_vQTvMr.aboutFlexRow_8dohDi 122.0x38.0 bg #97979f @ 0.12 r 10px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sv-chip-default.png`, `sv-chip-hover.png`, `sv-chip-focus-visible.png`, `sv-chip-pressed.png`.

#### sv-about

About heading. The tracked ABOUT section label.

Page: server. Selector: `about h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800 x 28.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Ginto Discord Nord 24px/28.8px 700 |
| Letter spacing | normal |
| Colour | #fbfbfb |
| Transition | none |
| How | at rest |

Crops: `sv-about-default.png`.

### Mobile (390 wide)

#### m-bar

Mobile nav. The phone marketing bar over discovery.

Page: mobile. Selector: `mobile nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Ginto Discord 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Icon | 146 x 24, colour #ffffff, fill #000000 |
| Painted layers | a.button_vOYBES.overlayFocusRing_vOYBES 0.0x0.0 bg #ffffff r 12px; button.menuIcon__mQgbA 40.0x40.0 bg #ffffff @ 0.1 r 14px |
| How | at rest |

Crops: `m-bar-default.png`.

#### m-h1

Mobile heading. The DISCOVERABLE SERVERS display at 390px.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 62.41 |
| Padding | 0px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ABC Ginto Discord Nord 31.2px/31.2px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-h1-default.png`.

#### m-search

Mobile search. The discovery search field at 390px.

Page: mobile. Selector: `mobile search`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 64 |
| Padding | 12px 16px |
| Gap | 12px |
| Border | 1px solid #000000 @ 0 |
| Radius | 12px |
| Background | #ffffff @ 0.12 |
| Box shadow | none |
| Outline | none |
| Font | gg sans 14px/16.1px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.text-muted.size12_meTJex: gg sans 12px/16px 400, #ffffff |
| Transition | none |
| Icon | 24 x 24, colour #ffffff, fill #000000 |
| Painted layers | div.searchBox__7pJSN.searchBarContainer__J-bNz 358.0x64.0 bg #ffffff @ 0.12 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px |
| How | at rest |

Crops: `m-search-default.png`.

#### m-card

Mobile server card. A server card at 390px.

Page: mobile. Selector: `mobile card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 358 x 380 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #efeff1 |
| Text node | a.link_vQTvMr.linkDefault_vQTvMr: gg sans 20px/24px 600, #fbfbfb |
| Transition | none |
| Icon | 16 x 16, colour #23a559, fill #000000 |
| Painted layers | article.guildItemContainer_OnY3sU 358.0x380.0 bg #202024 border T:1px solid #97979f @ 0.12 / R:1px solid #97979f @ 0.12 / B:1px solid #97979f @ 0.12 / L:1px solid #97979f @ 0.12 r 8px; div.listIconContainer_OnY3sU 66.4x66.4 bg #202024 r 14.2281px; div.dotOnline_U3tHuW 8.0x8.0 bg #43b581 r 50%; div.dotOffline_U3tHuW.dotOnline_U3tHuW 8.0x8.0 bg #c4c9ce r 50% |
| How | at rest |

Crops: `m-card-default.png`.

### Sign-in / register

#### lg-card

Auth card. The sign-in card on the animated brand backdrop — form fields left, QR panel right.

Page: login. Selector: `login form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 784 x 414 |
| Padding | 32px |
| Border | none |
| Radius | 8px |
| Background | #242429 |
| Box shadow | #000000 @ 0.2 0px 2px 10px 0px |
| Outline | none |
| Font | gg sans 18px/18px 400 |
| Letter spacing | normal |
| Colour | #96979e |
| Text node | h1.heading-xl/semibold_RAOoio.defaultColor_HtJY5C: gg sans 24px/32px 600, #fbfbfb |
| Transition | none |
| Icon | 16 x 16, colour #fbfbfb |
| Painted layers | form.authBoxExpanded_rN1Ls3.authBox_rN1Ls3 784.0x414.0 bg #242429 r 8px shadow #000000 @ 0.2 0px 2px 10px 0px; div.input_b-mzk1.input_ZFr6bW 416.0x44.0 bg #000000 @ 0.121569 border T:1px solid #97979f @ 0.2 / R:1px solid #97979f @ 0.2 / B:1px solid #97979f @ 0.2 / L:1px solid #97979f @ 0.2 r 8px; div.separator_NZ34f3 0.0x0.0 bg #97979f @ 0.121569; div.wrapper_UcGqzv.container_0PLWhS 416.0x40.0 bg #000000 @ 0.121569 border T:1px solid #97979f @ 0.2 / R:1px solid #97979f @ 0.2 / B:1px solid #97979f @ 0.2 / L:1px solid #97979f @ 0.2 r 8px; button.button_F7qvhY.sm_F7qvhY 32.0x32.0 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; button.button_F7qvhY.md_F7qvhY 416.0x40.0 bg #5865f2 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px |
| How | at rest |

Crops: `lg-card-default.png`.

#### lg-h1

Sign-in heading. "Welcome back!" — the auth card heading.

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 156 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 24px/32px 600 |
| Letter spacing | normal |
| Colour | #fbfbfb |
| Transition | none |
| How | at rest |

Crops: `lg-h1-default.png`.

#### lg-email

Email field. The "Email or Phone Number" field; the filled state types an address then deletes it — nothing is submitted.

Page: login. Selector: `input email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 414 x 44 | = | = |
| Padding | 12px 10px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | gg sans 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #efeff1 | = | = |
| Transition | border-color 0.2s ease-in-out | = | = |
| Cursor | text | = | = |
| Placeholder | #8f9097, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `lg-email-default.png`, `lg-email-focused.png`, `lg-email-filled.png`.

#### lg-pass

Password field. The password field with the reveal-button affordance; focused via a click-in, never filled.

Page: login. Selector: `input password`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 374 x 38 | = |
| Padding | 1px 0px 1px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | gg sans 16px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #efeff1 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #8f9097, opacity 1 | = |
| Ancestor paint | 1 up div.wrapper_UcGqzv.container_0PLWhS bg #000000 @ 0.121569 | 1 up div.wrapper_UcGqzv.container_0PLWhS bg #000000 @ 0.121569 outline 2px solid #5865f2 |
| How | at rest | clicked into the field |

Crops: `lg-pass-default.png`, `lg-pass-focused.png`.

#### lg-submit

Log In button. The brand-fill Log In submit; hover/focus measured, never pressed — it would submit the sign-in.

Page: login. Selector: `Log In button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 416 x 40 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #ffffff @ 0.08 | = | = |
| Radius | 8px | = | = |
| Background | #5865f2 | #4452bb | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | gg sans 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.lineClamp1_MMUIw6.body-md/medium_RAOoio: gg sans 16px/20px 500, #ffffff | = | = |
| Transition | background-color, color, border-color, opacity 0.05s, 0.05s, 0.05s, 0.05s ease-in, ease-in, ease-in, ease-in delay 0s, 0s, 0s, 0s | background-color, color, border-color, opacity 0.15s, 0.15s, 0.15s, 0.15s ease-out, ease-out, ease-out, ease-out delay 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = | = |
| Painted layers | button.button_F7qvhY.md_F7qvhY 416.0x40.0 bg #5865f2 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px | button.button_F7qvhY.md_F7qvhY 416.0x40.0 bg #4452bb border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `lg-submit-default.png`, `lg-submit-hover.png`, `lg-submit-focus-visible.png`.

#### lg-forgot

Forgot link. The "Forgot your password?" link; measured, never followed.

Page: login. Selector: `forgot link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 135 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | gg sans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #798df9 | = | = | = |
| Text node | span.lineClamp1_MMUIw6.body-sm/normal_RAOoio: gg sans 14px/18px 400, #798df9 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `lg-forgot-default.png`, `lg-forgot-hover.png`, `lg-forgot-focus-visible.png`, `lg-forgot-pressed.png`.

#### lg-register

Register link. The "Need an account? Register" link; measured, never followed.

Page: login. Selector: `register link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 49 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | gg sans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #798df9 | = | = | = |
| Text node | span.lineClamp1_MMUIw6.body-sm/normal_RAOoio: gg sans 14px/18px 400, #798df9 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `lg-register-default.png`, `lg-register-hover.png`, `lg-register-focus-visible.png`, `lg-register-pressed.png`.

#### lg-qr

QR panel. The "Log in with QR Code" panel on the card’s right.

Page: login. Selector: `qrLogin panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 240 x 322 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 18px/18px 400 |
| Letter spacing | normal |
| Colour | #96979e |
| Text node | h2.heading-xl/semibold_RAOoio.defaultColor_HtJY5C: gg sans 24px/32px 600, #fbfbfb |
| Transition | none |
| Icon | 160 x 160, colour #96979e, fill #000000 |
| Painted layers | div.qrCodeContainer_d4-PpI.qrCode_FDXpbQ 176.0x176.0 bg #ffffff r 4px |
| Ancestor paint | 3 up form.authBoxExpanded_rN1Ls3.authBox_rN1Ls3 bg #242429 shadow #000000 @ 0.2 0px 2px 10px 0px |
| How | at rest |

Crops: `lg-qr-default.png`.

#### rg-h1

Register heading. "Create an account" — the register card heading.

Page: register. Selector: `register h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 416 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | gg sans 24px/32px 600 |
| Letter spacing | normal |
| Colour | #fbfbfb |
| Transition | none |
| Ancestor paint | 2 up section.authBox_rN1Ls3.theme-dark bg #242429 shadow #000000 @ 0.2 0px 2px 10px 0px |
| How | at rest |

Crops: `rg-h1-default.png`.

#### rg-email

Register email. The register email field; the filled state types an address then deletes it — nothing is submitted.

Page: register. Selector: `register email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 414 x 38 | = | = |
| Padding | 1px 12px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | gg sans 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #efeff1 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #8f9097, opacity 1 | = | = |
| Ancestor paint | 1 up div.wrapper_UcGqzv.container_0PLWhS bg #000000 @ 0.121569 | 1 up div.wrapper_UcGqzv.container_0PLWhS bg #000000 @ 0.121569 outline 2px solid #5865f2 | 1 up div.wrapper_UcGqzv.container_0PLWhS bg #000000 @ 0.121569 outline 2px solid #5865f2 |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `rg-email-default.png`, `rg-email-focused.png`, `rg-email-filled.png`.

#### rg-submit

Create Account. The Create Account submit; hover/focus measured, never pressed.

Page: register. Selector: `Create Account`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 416 x 40 | = | = |
| Padding | 0px | = | = |
| Border | 1px solid #ffffff @ 0.08 | = | = |
| Radius | 8px | = | = |
| Background | #5865f2 | #4452bb | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | gg sans 16px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Text node | span.lineClamp1_MMUIw6.body-md/medium_RAOoio: gg sans 16px/20px 500, #ffffff | = | = |
| Transition | background-color, color, border-color, opacity 0.05s, 0.05s, 0.05s, 0.05s ease-in, ease-in, ease-in, ease-in delay 0s, 0s, 0s, 0s | background-color, color, border-color, opacity 0.15s, 0.15s, 0.15s, 0.15s ease-out, ease-out, ease-out, ease-out delay 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = | = |
| Painted layers | button.button_F7qvhY.md_F7qvhY 416.0x40.0 bg #5865f2 border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px | button.button_F7qvhY.md_F7qvhY 416.0x40.0 bg #4452bb border T:1px solid #ffffff @ 0.08 / R:1px solid #ffffff @ 0.08 / B:1px solid #ffffff @ 0.08 / L:1px solid #ffffff @ 0.08 r 8px | = |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `rg-submit-default.png`, `rg-submit-hover.png`, `rg-submit-focus-visible.png`.

## Transitions declared in the readable stylesheets

discord.com serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- download: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `color 0.3s, background-color 0.3s`, `0.555s`, `opacity 0.2s`, `box-shadow 0.3s, transform 0.3s`, `transform 0.3s`, `color 0.2s`, `box-shadow 0.3s, transform 0.3s, background-color 0.3s`, `0.25s`

- gaming: `max-height 0.3s ease-in-out`, `transform 0.3s`, `opacity 0.35s`, `none`, `background-color 0.4s`, `transform 0.25s`, `background-color 0.16s, color 0.16s`, `transform 0.16s`, `color 0.1s ease-in-out`, `color 0.1s linear`, `border-color 0.2s ease-in-out`, `background 0.1s`

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `color 0.3s, background-color 0.3s`, `0.555s`, `opacity 0.2s`, `box-shadow 0.3s, transform 0.3s`, `transform 0.3s`, `color 0.2s`, `box-shadow 0.3s, transform 0.3s, background-color 0.3s`, `0.25s`

- login: `background-color var(--custom-button-transition-duration) ease,color var(--custom-button-transition-duration) ease`, `color var(--custom-button-transition-duration) ease,background-color var(--custom-button-transition-duration) ease,border-color var(--custom-button-transition-duration) ease`, `none`, `box-shadow 0.1s ease-out`, `opacity 0.2s ease-in-out`, `opacity 0.2s ease-out`, `opacity 0.2s ease-out, visibility ease-out 0.2s`, `opacity 0.2s ease-out, visibility ease-out`, `color 1ms step-start`, `background-color 50ms ease-in, color 50ms ease-in, border-color 50ms ease-in, opacity 50ms ease-in`, `background-color 0.15s ease-out, color 0.15s ease-out, border-color 0.15s ease-out, opacity 0.15s ease-out`, `opacity 0.2s ease-out, transform 0.2s ease-out`

- nitro: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `color 0.3s, background-color 0.3s`, `0.555s`, `opacity 0.2s`, `box-shadow 0.3s, transform 0.3s`, `transform 0.3s`, `color 0.2s`, `box-shadow 0.3s, transform 0.3s, background-color 0.3s`, `0.25s`

- register: `background-color var(--custom-button-transition-duration) ease,color var(--custom-button-transition-duration) ease`, `color var(--custom-button-transition-duration) ease,background-color var(--custom-button-transition-duration) ease,border-color var(--custom-button-transition-duration) ease`, `none`, `box-shadow 0.1s ease-out`, `opacity 0.2s ease-in-out`, `opacity 0.2s ease-out`, `opacity 0.2s ease-out, visibility ease-out 0.2s`, `opacity 0.2s ease-out, visibility ease-out`, `color 1ms step-start`, `background-color 50ms ease-in, color 50ms ease-in, border-color 50ms ease-in, opacity 50ms ease-in`, `background-color 0.15s ease-out, color 0.15s ease-out, border-color 0.15s ease-out, opacity 0.15s ease-out`, `opacity 0.2s ease-out, transform 0.2s ease-out`

- server: `max-height 0.3s ease-in-out`, `transform 0.3s`, `opacity 0.35s`, `none`, `background-color 0.4s`, `transform 0.25s`, `background-color 0.16s, color 0.16s`, `transform 0.16s`, `color 0.1s ease-in-out`, `color 0.1s linear`, `border-color 0.2s ease-in-out`, `background 0.1s`

- servers: `max-height 0.3s ease-in-out`, `transform 0.3s`, `opacity 0.35s`, `none`, `background-color 0.4s`, `transform 0.25s`, `background-color 0.16s, color 0.16s`, `transform 0.16s`, `color 0.1s ease-in-out`, `color 0.1s linear`, `border-color 0.2s ease-in-out`, `background 0.1s`
