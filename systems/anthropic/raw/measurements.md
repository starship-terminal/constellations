# Component measurements

Computed styles read from www.anthropic.com, claude.com and docs.claude.com on 2026-11-09 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Top navigation bar. The fixed header on every marketing and product page: the Anthropic wordmark, section triggers, Search and the Try Claude pill.

Page: product. Selector: `header.__header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 593.09 x 88 |
| Padding | 24px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | span: anthropicSans 15px/24px 400, #30302e |
| Transition | none |
| Icon | 16 x 16, colour #5e5d59 |
| Painted layers | div.content.panel 200.0x453.0 bg #ffffff r 12px shadow #000000 @ 0.1 0px 4px 16px 0px; div.verticalSeparator 0.0x368.0 bg #e8e6dc; div.verticalSeparator 0.0x368.0 bg #e8e6dc; div.verticalSeparator 0.0x368.0 bg #e8e6dc; div.footer 200.0x53.0 bg #f5f4ed border T:1px solid #e8e6dc; a.button.variant-tertiary 133.2x28.0 bg #faf9f5 r 8px shadow #faf9f5 0px 0px 0px 0px, #d1cfc5 0px 0px 0px 1px |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-search

Nav search button. The square search icon button in the header.

Page: home. Selector: `"Search" icon button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 28 x 28 | = | = | = |
| Padding | 8px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e8e6dc | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f5f4ed | #e8e6dc | = | #e8e6dc |
| Box shadow | none | #e8e6dc 0px 0px 0px 1px | = | #e8e6dc 0px 0px 0px 1px |
| Outline | none | = | 2px solid #154c92 offset 4px | = |
| Font | anthropicSans 13px/20.02px 400 | = | = | = |
| Letter spacing | 0.13px | = | = | = |
| Colour | #3d3d3a | #141413 | #141413 | #141413 |
| Transition | border-color, box-shadow, background-color, color 0.2s, 0.2s, 0.2s, 0.2s ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #3d3d3a | 20 x 20, colour #141413 | 20 x 20, colour #141413 | 20 x 20, colour #141413 |
| Painted layers | a.f9ZZrG_button.f9ZZrG_corner-small 28.0x28.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 8px | a.f9ZZrG_button.f9ZZrG_corner-small 28.0x28.0 bg #e8e6dc border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 8px shadow #e8e6dc 0px 0px 0px 1px | a.f9ZZrG_button.f9ZZrG_corner-small 28.0x28.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 8px outline 2px solid #154c92 offset 4px | a.f9ZZrG_button.f9ZZrG_corner-small 28.0x28.0 bg #e8e6dc border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 8px shadow #e8e6dc 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-search-default.png`, `nav-search-hover.png`, `nav-search-focus-visible.png`, `nav-search-pressed.png`.

#### nav-cta

Nav CTA button. The header's primary action pill ("Try Claude" on the marketing site, "Explore here" on claude.com). Measured and focused, never followed.

Page: home. Selector: `the CTA in the header`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116.73 x 28 | = | = | = |
| Padding | 8px 12px 8px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #e8e6dc | 1px solid #141413 | = | = |
| Radius | 999999px | = | = | = |
| Background | #f5f4ed | #141413 | = | #e8e6dc |
| Box shadow | none | #141413 0px 0px 0px 1px | = | #e8e6dc 0px 0px 0px 1px |
| Outline | none | = | 2px solid #154c92 offset 4px | = |
| Font | anthropicSans 13px/20.02px 400 | = | = | = |
| Letter spacing | 0.13px | = | = | = |
| Colour | #3d3d3a | #faf9f5 | #141413 | #141413 |
| Transition | border-color, box-shadow, background-color, color 0.15s, 0.15s, 0.15s, 0.15s ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #3d3d3a | 16 x 16, colour #faf9f5 | 16 x 16, colour #141413 | 16 x 16, colour #141413 |
| Painted layers | button.f9ZZrG_button.f9ZZrG_corner-full 116.7x28.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px | button.f9ZZrG_button.f9ZZrG_corner-full 116.7x28.0 bg #141413 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 999999px shadow #141413 0px 0px 0px 1px | button.f9ZZrG_button.f9ZZrG_corner-full 116.7x28.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px outline 2px solid #154c92 offset 4px | button.f9ZZrG_button.f9ZZrG_corner-full 116.7x28.0 bg #e8e6dc border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px shadow #e8e6dc 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### footer

Footer. The site footer: link columns, the wordmark, legal row with Privacy choices.

Page: product. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1226.78 |
| Padding | 95.9999px 0px |
| Border | T: 1px solid #30302e; R: none; B: none; L: none |
| Radius | 0px |
| Background | #141413 |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #faf9f5 |
| Text node | p.copyright: anthropicSans 11px/16.5px 400, #87867f |
| Transition | none |
| Icon | 144 x 31.41, colour #faf9f5 |
| Painted layers | footer.footer.theme-dark 1440.0x1226.8 bg #141413 border T:1px solid #30302e; form.form.promptBar 280.0x46.0 bg #141413; div.text-caption.inputWrapper 280.0x46.0 bg #262624 border T:1px solid #3d3d3a / R:1px solid #3d3d3a / B:1px solid #3d3d3a / L:1px solid #3d3d3a r 12px; button.button.variant-brand 28.0x28.0 bg #c6613f r 8px shadow #c6613f 0px 0px 0px 0px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in the footer columns. Privacy choices opens a settings dialog and is never pressed.

Page: product. Selector: `a footer link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 189.34 x 27.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | anthropicSans 15px/22.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #faf9f5 | = | = | = |
| Text node | a.sectionLink.text-caption: anthropicSans 12px/19.2px 400, #faf9f5, ls 0.12px | = | = | = |
| Transition | none | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.sectionLink.text-caption 189.3x27.2 outline 2px solid #c46849 offset 2px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### nav-pill

Nav pill link. A section pill in the header (News, Research, Policy, Commitments, Company). Measured, never followed.

Page: home. Selector: `a header pill link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69.2 x 28 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #e8e6dc | = | = | = |
| Radius | 999999px | = | = | = |
| Background | #f5f4ed | #e8e6dc | = | #e8e6dc |
| Box shadow | none | #e8e6dc 0px 0px 0px 1px | = | #e8e6dc 0px 0px 0px 1px |
| Outline | none | = | 2px solid #154c92 offset 4px | = |
| Font | anthropicSans 13px/20.02px 400 | = | = | = |
| Letter spacing | 0.13px | = | = | = |
| Colour | #3d3d3a | #141413 | #141413 | #141413 |
| Transition | border-color, box-shadow, background-color, color 0.2s, 0.2s, 0.2s, 0.2s ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.f9ZZrG_button.f9ZZrG_corner-full 69.2x28.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px | a.f9ZZrG_button.f9ZZrG_corner-full 69.2x28.0 bg #e8e6dc border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px shadow #e8e6dc 0px 0px 0px 1px | a.f9ZZrG_button.f9ZZrG_corner-full 69.2x28.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px outline 2px solid #154c92 offset 4px | a.f9ZZrG_button.f9ZZrG_corner-full 69.2x28.0 bg #e8e6dc border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px shadow #e8e6dc 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-pill-default.png`, `nav-pill-hover.png`, `nav-pill-focus-visible.png`, `nav-pill-pressed.png`.

#### nav-trigger

Nav dropdown trigger. A section trigger in the header; opens the section dropdown on hover. Measured, never followed.

Page: product. Selector: `"Product" trigger`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 96.67 x 40 | = | = | = |
| Padding | 8px 8px 8px 12px | = | = | = |
| Gap | 4px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #c46849 offset 2px | = |
| Font | anthropicSans 15px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #30302e | #141413 | = | #141413 |
| Text node | span: anthropicSans 15px/24px 400, #30302e | span: anthropicSans 15px/24px 400, #141413 | = | span: anthropicSans 15px/24px 400, #141413 |
| Transition | color 0.5s cubic-bezier(0.19, 1, 0.22, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #5e5d59 | 16.68 x 16.68, colour #141413 | 16.37 x 16.37, colour #5e5d59 | 16 x 16, colour #141413 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.trigger.text-body-3 96.7x40.0 outline 2px solid #c46849 offset 2px | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-dropdown

Nav dropdown. The dropdown under a header section (Product: Claude, Claude Code, Claude in Chrome, …). Shown in its hover-open state.

Page: product. Selector: `the open dropdown panel`. States: .

Not found on the page at capture time.

### Home

#### hero-title

Hero title. The home h1, a large serif display line ("AI research and products that put safety at the frontier.").

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 152.95 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 40.7843px/50.9804px 400 |
| Letter spacing | -0.407843px |
| Colour | #141413 |
| Text node | span.LOCOdG_lead: anthropicSans 40.7843px/50.9804px 600, #141413, ls -0.407843px |
| Transition | color 0.3s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The primary pill under the hero title.

Page: home. Selector: `the first primary button on the page`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.94 x 36 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #141413 | = | = | = |
| Radius | 10px | = | = | = |
| Background | #141413 | = | = | = |
| Box shadow | none | #141413 0px 0px 0px 1px | = | #141413 0px 0px 0px 1px |
| Outline | none | = | 2px solid #154c92 offset 4px | = |
| Font | anthropicSans 16.6863px/25.53px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #faf9f5 | = | = | = |
| Transition | border-color, box-shadow, background-color, color 0.2s, 0.2s, 0.2s, 0.2s ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.f9ZZrG_button.f9ZZrG_corner-small 138.9x36.0 bg #141413 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 10px | a.f9ZZrG_button.f9ZZrG_corner-small 138.9x36.0 bg #141413 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 10px shadow #141413 0px 0px 0px 1px | a.f9ZZrG_button.f9ZZrG_corner-small 138.9x36.0 bg #141413 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 10px outline 2px solid #154c92 offset 4px | a.f9ZZrG_button.f9ZZrG_corner-small 138.9x36.0 bg #141413 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 10px shadow #141413 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

### Cards and indexes

#### news-card-title

News page title.

Page: news. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1 x 1 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 16.6863px/25.53px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Transition | none |
| How | at rest |

Crops: `news-card-title-default.png`.

#### news-card

News card. News card: a linked post card in the news index.

Page: news. Selector: `a linked card in the index`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 632 x 104.17 | = |
| Padding | 0px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 16.6863px/25.53px 400 | = |
| Letter spacing | normal | = |
| Colour | #141413 | = |
| Text node | h2.tOQyXa_headline-3.W1FydW_featuredTitle: anthropicSans 32.549px/37.1059px 700, #141413 | h2.tOQyXa_headline-3.W1FydW_featuredTitle: anthropicSans 32.549px/37.1059px 700, #87867f |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `news-card-default.png`, `news-card-hover.png`.

#### research-card-title

Research page title.

Page: research. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 94.88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 42.3529px/47.4353px 600 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | span.kMamaW_heading-block: anthropicSans 42.3529px/47.4353px 600, #141413 |
| Transition | none |
| How | at rest |

Crops: `research-card-title-default.png`.

#### engineering-card-title

Engineering page title.

Page: engineering. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 203.94 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 40.7843px/50.9804px 400 |
| Letter spacing | -0.407843px |
| Colour | #141413 |
| Text node | button.v9lDbq_button: anthropicSans 40.7843px/50.9804px 600, #141413, ls -0.407843px |
| Transition | color 0.3s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | span.v9lDbq_mark 40.8x40.8 bg #141413 r 7.74902px; span._6xvBMG_mark.v9lDbq_markImage 27.3x27.3 bg #141413 |
| How | at rest |

Crops: `engineering-card-title-default.png`.

#### engineering-card

Engineering entry. Engineering entry: a linked post in the engineering index.

Page: engineering. Selector: `a linked card in the index`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 848 x 477 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 16.6863px/25.53px 400 | = |
| Letter spacing | normal | = |
| Colour | #141413 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `engineering-card-default.png`, `engineering-card-hover.png`.

#### feature-card

Feature card. A large card or slide on the home page (the report/announcement feature).

Page: home. Selector: `a card-sized element`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1440 x 810 | = |
| Padding | 224px 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #f5f4ed | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 16.6863px/25.53px 400 | = |
| Letter spacing | normal | = |
| Colour | #141413 | = |
| Text node | h2.tOQyXa_headline-1._8i4M7a_title: anthropicSans 51.902px/56.0541px 600, #141413 | = |
| Transition | none | = |
| Icon | 20 x 20, colour #3d3d3a | = |
| Painted layers | div.rLIPjq_card 1440.0x810.0 bg #f5f4ed; a.f9ZZrG_button.f9ZZrG_corner-small 138.9x36.0 bg #141413 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 10px; button.f9ZZrG_button.f9ZZrG_corner-small 36.0x36.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 10px | = |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### news-card-link

News card title link. The caption/title link of an index entry.

Page: news. Selector: `the carousel info link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 308 x 26.72 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 16.6863px/25.53px 400 | = |
| Letter spacing | normal | = |
| Colour | #30302e | = |
| Text node | h2.tOQyXa_headline-5._5NNTzG_carousel-info-title: anthropicSans 21.3725px/26.7157px 700, #141413 | h2.tOQyXa_headline-5._5NNTzG_carousel-info-title: anthropicSans 21.3725px/26.7157px 700, #87867f |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `news-card-link-default.png`, `news-card-link-hover.png`.

#### research-card

Research entry. Research entry: a linked paper/post in the research index.

Page: research. Selector: `a linked card in the index`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 928 x 522 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 16.6863px/25.53px 400 | = |
| Letter spacing | normal | = |
| Colour | #faf9f5 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `research-card-default.png`, `research-card-hover.png`.

#### research-card-link

Research entry title link. The caption/title link of an index entry.

Page: research. Selector: `the carousel info link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 308 x 53.44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 16.6863px/25.53px 400 | = |
| Letter spacing | normal | = |
| Colour | #b0aea5 | = |
| Text node | h2.tOQyXa_headline-5._5NNTzG_carousel-info-title: anthropicSans 21.3725px/26.7157px 700, #faf9f5 | h2.tOQyXa_headline-5._5NNTzG_carousel-info-title: anthropicSans 21.3725px/26.7157px 700, #5e5d59 |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `research-card-link-default.png`, `research-card-link-hover.png`.

#### engineering-card-link

Engineering entry title link. The caption/title link of an index entry.

Page: engineering. Selector: `the carousel info link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 308 x 53.44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 16.6863px/25.53px 400 | = |
| Letter spacing | normal | = |
| Colour | #30302e | = |
| Text node | h2.tOQyXa_headline-5._5NNTzG_carousel-info-title: anthropicSans 21.3725px/26.7157px 700, #141413 | h2.tOQyXa_headline-5._5NNTzG_carousel-info-title: anthropicSans 21.3725px/26.7157px 700, #87867f |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `engineering-card-link-default.png`, `engineering-card-link-hover.png`.

### Product pages

#### product-title

Product page title. The product page h1 (the Claude product overview).

Page: product. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 606.48 x 79.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 72px/79.2px 500 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | span.hword: anthropicSerif 72px/79.2px 500, #141413 |
| Transition | none |
| How | at rest |

Crops: `product-title-default.png`.

#### product-cta

Product CTA. A primary button on the product page.

Page: product. Selector: `the first CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 100.25 x 36 | = | = | = |
| Padding | 8px 12px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #141413 | = | = | = |
| Box shadow | #141413 0px 0px 0px 0px | #141413 0px 0px 0px 2px | = | #141413 0px 0px 0px 2px |
| Outline | none | = | 2px solid #c46849 offset 4px | = |
| Font | anthropicSans 15px/15px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #faf9f5 | = | = | = |
| Transition | color, background-color, border-color, box-shadow 0.1s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.variant-primary 100.3x36.0 bg #141413 r 8px shadow #141413 0px 0px 0px 0px | a.button.variant-primary 100.3x36.0 bg #141413 r 8px shadow #141413 0px 0px 0px 2px | a.button.variant-primary 100.3x36.0 bg #141413 r 8px shadow #141413 0px 0px 0px 0px outline 2px solid #c46849 offset 4px | a.button.variant-primary 100.3x36.0 bg #141413 r 8px shadow #141413 0px 0px 0px 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `product-cta-default.png`, `product-cta-hover.png`, `product-cta-focus-visible.png`, `product-cta-pressed.png`.

#### product-card

Product card. A card on the product overview page.

Page: product. Selector: `a card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 480 x 270 | = |
| Padding | 0px | = |
| Border | 1px solid #e8e6dc | = |
| Radius | 19px | = |
| Background | #f0eee6 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 20px/32px 400 | = |
| Letter spacing | normal | = |
| Colour | #141413 | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Icon | 32 x 32, colour #faf9f5 | 33.92 x 33.92, colour #faf9f5 |
| Painted layers | div.card.video 480.0x270.0 bg #f0eee6 border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 19px; span.play 72.0x72.0 bg #1a1918 border T:1px solid #3d3d3a / R:1px solid #3d3d3a / B:1px solid #3d3d3a / L:1px solid #3d3d3a r 14px shadow #000000 @ 0.05 0px 3px 10px 0px | div.card.video 480.0x270.0 bg #f0eee6 border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 19px; span.play 76.3x76.3 bg #1a1918 border T:1px solid #3d3d3a / R:1px solid #3d3d3a / B:1px solid #3d3d3a / L:1px solid #3d3d3a r 14px shadow #000000 @ 0.05 0px 3px 10px 0px |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### api-title

Platform page title. The Claude Platform/API page headline.

Page: platform-api. Selector: `the largest heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 752 x 116.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 64px/70.4px 500 |
| Letter spacing | normal |
| Colour | #141413 |
| Transition | opacity, transform 0.75s, 0.75s cubic-bezier(0.25, 1, 0.5, 1), cubic-bezier(0.25, 1, 0.5, 1) delay 0.12s |
| How | at rest |

Crops: `api-title-default.png`.

#### api-cta

Platform CTA. A primary button or link on the platform page.

Page: platform-api. Selector: `the first CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 238.03 x 20 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 8px 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | anthropicSans 15px/22.5px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #5e5d59 | = | - | = |
| Text node | span.linkLabel.text-caption: anthropicSans 12px/19.2px 400, #5e5d59, ls 0.12px | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 20 x 20, colour #5e5d59 | = | - | = |
| Ancestor paint | 1 up a.card.gridCard bg #ffffff | 1 up a.card.gridCard bg #ffffff shadow #000000 @ 0 0px 0.0367769px 0.183884px 0px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Error | - | = | keyboard focus could not reach the element | = |

Crops: `api-cta-default.png`, `api-cta-hover.png`, `api-cta-pressed.png`.

### Pricing

#### pricing-title

Pricing title. The "Pricing" h1 on claude.com/pricing.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1246.05 x 49.28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 64px/70.4px 500 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | span.word: anthropicSerif 64px/70.4px 500, #141413 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-tabs

Plan type tabs. The Individual / Developer / Team plan tabs.

Page: pricing. Selector: `the tab strip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1312 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | button.tab.text-caption: anthropicSans 12px/19.2px 400, #141413, ls 0.12px |
| Transition | none |
| Icon | 0 x 0, colour #5e5d59 |
| Painted layers | div.track 375.7x48.0 bg #f0eee6 r 16px; button.tab.text-caption 88.0x40.0 bg #ffffff r 12px; button.pickerButton.text-caption 0.0x0.0 bg #ffffff border T:1px solid #f0eee6 / R:1px solid #f0eee6 / B:1px solid #f0eee6 / L:1px solid #f0eee6 r 12px |
| How | at rest |

Crops: `plan-tabs-default.png`.

#### plan-tab

Plan tab. One segment of the plan-type tabs.

Page: pricing. Selector: `"Developer" tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 91.33 x 40 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #faf9f5 | = | #faf9f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #c46849 offset 2px | = |
| Font | anthropicSans 12px/19.2px 400 | = | = | = |
| Letter spacing | 0.12px | = | = | = |
| Colour | #5e5d59 | #141413 | = | #141413 |
| Transition | background-color, color 0.2s, 0.1s ease-in-out, ease-in-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | button.tab.text-caption 91.3x40.0 bg #faf9f5 r 12px | button.tab.text-caption 91.3x40.0 r 12px outline 2px solid #c46849 offset 2px | button.tab.text-caption 91.3x40.0 bg #faf9f5 r 12px |

Crops: `plan-tab-default.png`, `plan-tab-hover.png`, `plan-tab-focus-visible.png`, `plan-tab-pressed.png`.

#### plan-tab-active

Plan tab, switched. The same tab strip after a local click: the API segment is the active one, and the API usage table replaces the plan cards.

Page: pricing. Selector: `the "API" tab after clicking it`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 51.81 x 40 |
| Padding | 8px 16px |
| Gap | 8px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 12px/19.2px 400 |
| Letter spacing | 0.12px |
| Colour | #141413 |
| Transition | background-color, color 0.2s, 0.1s ease-in-out, ease-in-out delay 0s, 0s |
| Cursor | pointer |
| Painted layers | button.tab.text-caption 51.8x40.0 bg #ffffff r 12px |
| How | at rest |

Crops: `plan-tab-active-default.png`.

#### plan-card

Plan card. A plan card on the pricing grid.

Page: pricing. Selector: `a plan column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 420 x 375.2 |
| Padding | 40px 32px 48px 32px |
| Border | 1px solid #f0eee6 |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | h3.modelName.text-headline-4-serif: anthropicSerif 32px/35.2px 500, #141413 |
| Transition | none |
| Painted layers | div.modelCard.whiteSurface 420.0x375.2 bg #ffffff border T:1px solid #f0eee6 / R:1px solid #f0eee6 / B:1px solid #f0eee6 / L:1px solid #f0eee6 r 24px; div.priceBlock 354.0x104.3 border T:1px solid #f0eee6; div.priceBlock 354.0x38.1 border T:1px solid #f0eee6; div.priceBlock 354.0x38.1 border T:1px solid #f0eee6 |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. A button inside a plan card ("Try Claude", "Contact sales"). Measured and focused, never followed.

Page: pricing. Selector: `a plan card button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 108.25 x 36 | = | = | = |
| Padding | 8px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #141413 | = | = | = |
| Box shadow | #141413 0px 0px 0px 0px | #141413 0px 0px 0px 2px | = | #141413 0px 0px 0px 2px |
| Outline | none | = | 2px solid #c46849 offset 4px | = |
| Font | anthropicSans 15px/15px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #faf9f5 | = | = | = |
| Transition | color, background-color, border-color, box-shadow 0.1s, 0.2s, 0.2s, 0.2s ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.variant-primary 108.3x36.0 bg #141413 r 8px shadow #141413 0px 0px 0px 0px | a.button.variant-primary 108.3x36.0 bg #141413 r 8px shadow #141413 0px 0px 0px 2px | a.button.variant-primary 108.3x36.0 bg #141413 r 8px shadow #141413 0px 0px 0px 0px outline 2px solid #c46849 offset 4px | a.button.variant-primary 108.3x36.0 bg #141413 r 8px shadow #141413 0px 0px 0px 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### faq-item

FAQ item. An accordion question in the pricing FAQ.

Page: pricing. Selector: `an accordion button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 640 x 88 | = |
| Padding | 32px 0px | = |
| Gap | 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 15px/17.25px 400 | = |
| Letter spacing | normal | = |
| Colour | #141413 | = |
| Text node | span.question.trim: anthropicSerif 19px/22.8px 500, #141413 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.iconLine 14.0x1.0 bg #5e5d59; span.iconLine.iconLineVertical 1.0x14.0 bg #5e5d59 | = |
| How | at rest | mouse hover |

Crops: `faq-item-default.png`, `faq-item-hover.png`.

#### batch-banner

Batch processing banner. The "Save 50% with batch processing" toggle banner on the API pricing tab.

Page: pricing. Selector: `the batch banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 200.8 x 34 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | span.bannerToggleText.text-body-3: anthropicSans 15px/24px 400, #3d3d3a |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.switch 56.0x34.0 bg #dedcd1 border T:1px solid #c2c0b6 / R:1px solid #c2c0b6 / B:1px solid #c2c0b6 / L:1px solid #c2c0b6 r 30px; span::after.switch 23pxx23px bg #ffffff border T:1px solid #9c9a92 / R:1px solid #9c9a92 / B:1px solid #9c9a92 / L:1px solid #9c9a92 r 50% shadow #000000 @ 0.05 0px 4px 24px 0px |
| Ancestor paint | 1 up div.banner bg #f0eee6 |
| How | at rest |

Crops: `batch-banner-default.png`.

#### batch-toggle

Batch toggle. The switch that shows batch-processing prices; a local toggle.

Page: pricing. Selector: `the painted track of the batch switch (input[role=switch])`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 56 x 34 | = | = | = |
| Padding | 4px | = | = | = |
| Border | 1px solid #c2c0b6 | = | = | = |
| Radius | 30px | = | = | = |
| Background | #dedcd1 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #c46849 offset 2px | = |
| Font | anthropicSans 15px/22.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #141413 | = | = | = |
| Transition | background-color, border-color 0.4s, 0.4s cubic-bezier(0.35, 1.5, 0.6, 1), cubic-bezier(0.35, 1.5, 0.6, 1) delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 23px x 23px, static, bg #ffffff, radius 50%, shadow #000000 @ 0.05 0px 4px 24px 0px | = | = | = |
| Painted layers | span.switch 56.0x34.0 bg #dedcd1 border T:1px solid #c2c0b6 / R:1px solid #c2c0b6 / B:1px solid #c2c0b6 / L:1px solid #c2c0b6 r 30px; span::after.switch 23pxx23px bg #ffffff border T:1px solid #9c9a92 / R:1px solid #9c9a92 / B:1px solid #9c9a92 / L:1px solid #9c9a92 r 50% shadow #000000 @ 0.05 0px 4px 24px 0px | = | span.switch 56.0x34.0 bg #dedcd1 border T:1px solid #c2c0b6 / R:1px solid #c2c0b6 / B:1px solid #c2c0b6 / L:1px solid #c2c0b6 r 30px outline 2px solid #c46849 offset 2px; span::after.switch 23pxx23px bg #ffffff border T:1px solid #9c9a92 / R:1px solid #9c9a92 / B:1px solid #9c9a92 / L:1px solid #9c9a92 r 50% shadow #000000 @ 0.05 0px 4px 24px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `batch-toggle-default.png`, `batch-toggle-hover.png`, `batch-toggle-focus-visible.png`, `batch-toggle-pressed.png`.

### Contact sales form

#### contact-title

Contact page title. The heading over the contact-sales form.

Page: contact-sales. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 448.03 x 79.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 72px/79.2px 500 |
| Letter spacing | normal |
| Colour | #141413 |
| Transition | opacity, transform 0.75s, 0.75s cubic-bezier(0.25, 1, 0.5, 1), cubic-bezier(0.25, 1, 0.5, 1) |
| How | at rest |

Crops: `contact-title-default.png`.

#### contact-form

Contact form. The HubSpot contact-sales form: a "What can we help you with?" radio topic group first, then dependent fields. Photographed and focused, never submitted.

Page: contact-sales. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 755.38 x 303.48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | span: anthropicSans 15px/19.5px 500, #141413 |
| Transition | none |
| Painted layers | div::after.input 16pxx16px bg #5e5d59; input 20.0x20.0 bg #faf9f5 border T:1px solid #5e5d59 / R:1px solid #5e5d59 / B:1px solid #5e5d59 / L:1px solid #5e5d59 r 9999px shadow #000000 @ 0.02 0px 0px 0px 1px inset; input::after 8pxx8px bg #faf9f5 r 9999px; input 20.0x20.0 bg #faf9f5 border T:1px solid #5e5d59 / R:1px solid #5e5d59 / B:1px solid #5e5d59 / L:1px solid #5e5d59 r 9999px shadow #000000 @ 0.02 0px 0px 0px 1px inset; input::after 8pxx8px bg #faf9f5 r 9999px; input 20.0x20.0 bg #faf9f5 border T:1px solid #5e5d59 / R:1px solid #5e5d59 / B:1px solid #5e5d59 / L:1px solid #5e5d59 r 9999px shadow #000000 @ 0.02 0px 0px 0px 1px inset |
| Ancestor paint | 1 up div.container.page bg #f5f4ed |
| How | at rest |

Crops: `contact-form-default.png`.

#### text-field

Text field. A text input in the form. Focused and filled with sample text that was deleted; nothing was sent.

Page: contact-sales. Selector: `the first text input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 755.38 x 56 | = | = |
| Padding | 16px 24px | = | = |
| Border | 1px solid #e8e6dc | 1px solid #5e5d59 | 1px solid #5e5d59 |
| Radius | 16px | = | = |
| Background | #faf9f5 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | anthropicSans 15px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #141413 | = | = |
| Transition | border-color, background-color, box-shadow 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | text | = | = |
| Placeholder | #5e5d59, opacity 1 | = | = |
| Painted layers | input.hs-input 755.4x56.0 bg #faf9f5 border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 16px | input.hs-input 755.4x56.0 bg #faf9f5 border T:1px solid #5e5d59 / R:1px solid #5e5d59 / B:1px solid #5e5d59 / L:1px solid #5e5d59 r 16px | input.hs-input 755.4x56.0 bg #faf9f5 border T:1px solid #5e5d59 / R:1px solid #5e5d59 / B:1px solid #5e5d59 / L:1px solid #5e5d59 r 16px |
| How | at rest | clicked into the field | typed "a voice agent for a clinic", then deleted; nothing sent |

Crops: `text-field-default.png`, `text-field-focused.png`, `text-field-filled.png`.

#### text-field-box

Text field box. The same field measured at rest (default only).

Page: contact-sales. Selector: `the first text input`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 755.38 x 56 |
| Padding | 16px 24px |
| Border | 1px solid #e8e6dc |
| Radius | 16px |
| Background | #faf9f5 |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/18px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Transition | border-color, background-color, box-shadow 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | text |
| Placeholder | #5e5d59, opacity 1 |
| Painted layers | input.hs-input.invalid 755.4x56.0 bg #faf9f5 border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 16px |
| How | at rest |

Crops: none.

#### text-area

Text area. The message textarea.

Page: contact-sales. Selector: `textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 755.38 x 120 | = |
| Padding | 16px 24px | = |
| Border | 1px solid #e8e6dc | 1px solid #5e5d59 |
| Radius | 16px | = |
| Background | #faf9f5 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 15px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #141413 | = |
| Transition | border-color, background-color, box-shadow 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #5e5d59, opacity 1 | = |
| Painted layers | textarea.hs-input.hs-fieldtype-textarea 755.4x120.0 bg #faf9f5 border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 16px | textarea.hs-input.hs-fieldtype-textarea 755.4x120.0 bg #faf9f5 border T:1px solid #5e5d59 / R:1px solid #5e5d59 / B:1px solid #5e5d59 / L:1px solid #5e5d59 r 16px |
| How | at rest | clicked into the field |

Crops: `text-area-default.png`, `text-area-focused.png`.

#### select-field

Select field. A select/combobox in the form.

Page: contact-sales. Selector: `select`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 755.38 x 56 |
| Padding | 16px 24px |
| Border | 1px solid #e8e6dc |
| Radius | 16px |
| Background | #faf9f5 |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/18px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Transition | border-color, background-color, box-shadow 0.3s, 0.3s, 0.3s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | default |
| Painted layers | select.hs-input.is-placeholder 755.4x56.0 bg #faf9f5 border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 16px |
| How | at rest |

Crops: `select-field-default.png`.

#### submit-button

Submit button. The form submit. Measured and focused, never pressed.

Page: contact-sales. Selector: `the submit button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 755.38 x 44 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | anthropicSans 15px/22.5px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #141413 | = | = |
| Text node | span: anthropicSans 15px/19.5px 500, #141413 | = | = |
| Transition | none | = | = |
| Painted layers | input 20.0x20.0 bg #141413 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 9999px shadow #000000 @ 0.02 0px 0px 0px 1px inset; input::after 8pxx8px bg #faf9f5 r 9999px | = | input 20.0x20.0 bg #141413 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 9999px outline 2px solid #c46849 offset 2px; input::after 8pxx8px bg #faf9f5 r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `submit-button-default.png`, `submit-button-hover.png`, `submit-button-focus-visible.png`.

#### topic-radio-row

Topic radio row. A radio row in the "What can we help you with?" topic group.

Page: contact-sales. Selector: `a .hs-form-radio row`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 755.38 x 44 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 15px/22.5px 400 | = |
| Letter spacing | normal | = |
| Colour | #141413 | = |
| Text node | span: anthropicSans 15px/19.5px 500, #141413 | = |
| Transition | none | = |
| Painted layers | input 20.0x20.0 bg #faf9f5 border T:1px solid #5e5d59 / R:1px solid #5e5d59 / B:1px solid #5e5d59 / L:1px solid #5e5d59 r 9999px shadow #000000 @ 0.02 0px 0px 0px 1px inset; input::after 8pxx8px bg #faf9f5 r 9999px | input 20.0x20.0 bg #faf9f5 border T:1px solid #141413 / R:1px solid #141413 / B:1px solid #141413 / L:1px solid #141413 r 9999px shadow #000000 @ 0.02 0px 0px 0px 1px inset; input::after 8pxx8px bg #faf9f5 r 9999px |
| How | at rest | mouse hover |

Crops: `topic-radio-row-default.png`, `topic-radio-row-hover.png`.

#### topic-radio

Radio input. The radio input inside a topic row.

Page: contact-sales. Selector: `input[type=radio]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 20 x 20 |
| Padding | 0px |
| Border | 1px solid #5e5d59 |
| Radius | 9999px |
| Background | #faf9f5 |
| Box shadow | #000000 @ 0.02 0px 0px 0px 1px inset |
| Outline | none |
| Font | anthropicSans 15px/17.25px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | border-color, background-color, box-shadow 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s |
| Cursor | pointer |
| Placeholder | #000000, opacity 1 |
| ::after | 8px x 8px, static, bg #faf9f5, radius 9999px |
| Painted layers | input 20.0x20.0 bg #faf9f5 border T:1px solid #5e5d59 / R:1px solid #5e5d59 / B:1px solid #5e5d59 / L:1px solid #5e5d59 r 9999px shadow #000000 @ 0.02 0px 0px 0px 1px inset; input::after 8pxx8px bg #faf9f5 r 9999px |
| How | at rest |

Crops: `topic-radio-default.png`.

#### field-label

Field label. A label over a field in the form.

Page: contact-sales. Selector: `a label`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 73.3 x 19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 15px/19.5px 500 |
| Letter spacing | normal |
| Colour | #141413 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `field-label-default.png`.

### Docs (platform.claude.com)

#### docs-topbar

Docs top bar. The 56px docs header: product tabs, search, language, Console, Log in.

Page: docs-api. Selector: `the fixed docs header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px 16px |
| Gap | 40px |
| Border | T: none; R: none; B: 1px solid #0b0b0b @ 0.1; L: none |
| Radius | 0px |
| Background | #fcfcfb |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 14px/21px 400 |
| Letter spacing | normal |
| Colour | #0b0b0b |
| Text node | span.whitespace-nowrap.font-voice: anthropicSerif 20px/20px 500, #0b0b0b |
| Transition | none |
| Icon | 20 x 20, colour #0b0b0b, fill #d97757 |
| Painted layers | header.fixed.right-0 1440.0x56.0 bg #fcfcfb border B:1px solid #0b0b0b @ 0.1; div.rounded-card.bg-surface-3 0.0x0.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.1 0px 0px 0px 0px inset, #0b0b0b @ 0.1 0px 0px 0px 1px, #000000 @ 0.12 0px 8px 24px 0px, #000000 @ 0.08 0px 2px 6px 0px; a.cds-reset.group/btn 135.3x32.0 bg #0b0b0b @ 0.1 r 8px; div.h-4.w-px 1.0x16.0 bg #0b0b0b @ 0.1; span.absolute.inset-0 98.4x32.0 bg #ffffff @ 0.1 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.1 0px 0px 0px 1px inset, #000000 @ 0.05 0px 1px 2px 0px; span.absolute.inset-0 63.2x31.0 bg #0b0b0b r 8px |
| How | at rest |

Crops: `docs-topbar-default.png`.

#### docs-tab

Docs top tab. A product tab in the docs header.

Page: docs-api. Selector: `"Messages" tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.47 x 32 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | anthropicSans 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0b0b0b | = | - | = |
| Text node | a.flex.h-control: anthropicSans 14px/20px 400, #898781 | = | - | = |
| Transition | none | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.h-control 66.5x32.0 bg #0b0b0b @ 0.05 r 3.35544e+07px | = | = |
| Error | - | = | keyboard focus could not reach the element | = |

Crops: `docs-tab-default.png`, `docs-tab-hover.png`, `docs-tab-pressed.png`.

#### docs-lang

Language picker. The "English" locale picker in the docs header.

Page: docs-api. Selector: `the lang button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 89.33 x 32 | = |
| Padding | 0px 12px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 8px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #0b0b0b | = |
| Text node | span.inline-flex.min-w-0: anthropicSans 14px/20px 400, #0b0b0b | = |
| Transition | box-shadow 0.06s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | span.absolute.inset-0 89.3x32.0 bg #0b0b0b @ 0.05 r 8px |

Crops: `docs-lang-default.png`, `docs-lang-hover.png`.

#### docs-hero-title

Docs home title. The docs home h1 ("Start building with Claude").

Page: docs-home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 317.48 x 114.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 52px/57.2px 300 |
| Letter spacing | normal |
| Colour | #0b0b0b |
| Transition | none |
| How | at rest |

Crops: `docs-hero-title-default.png`.

#### docs-sidebar

Docs sidebar. The left docs navigation: section groups and page links.

Page: docs-api. Selector: `the left nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 264 x 844 |
| Padding | 0px |
| Border | T: none; R: 1px solid #0b0b0b @ 0.1; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 14px/21px 400 |
| Letter spacing | normal |
| Colour | #0b0b0b |
| Text node | span: Anthropicons-Variable 16px/16px 533.25, #898781 |
| Transition | none |
| Painted layers | aside.hidden.w-56 264.0x844.0 border R:1px solid #0b0b0b @ 0.1; button.flex.h-control 239.0x32.0 bg #ffffff @ 0.5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.1 0px 0px 0px 1px inset; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px; label.flex.items-center 263.0x34.0 border B:1px solid #0b0b0b @ 0.1; span.cds-reset.relative 28.8x16.0 bg #2a78d6 r 3.35544e+07px |
| How | at rest |

Crops: `docs-sidebar-default.png`.

#### docs-nav-link

Docs nav link. A link in the docs sidebar.

Page: docs-api. Selector: `a sidebar link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 247 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px | = |
| Outline | none | = | = | = |
| Font | anthropicSans 14px/21px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0b0b0b | = | = | = |
| Text node | div.hit-row.hit-row-main: anthropicSans 14px/20px 500, #0b0b0b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.hit-row.hit-row-main 247.0x32.0 bg #0b0b0b @ 0.05 r 8px | a.block.rounded 247.0x32.0 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px | = |

Crops: `docs-nav-link-default.png`, `docs-nav-link-hover.png`, `docs-nav-link-focus-visible.png`, `docs-nav-link-pressed.png`.

#### docs-nav-active

Docs nav link, current. The current page in the docs sidebar.

Page: docs-start. Selector: `the active sidebar link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 91.09 x 32 |
| Padding | 0px 12px |
| Gap | 6px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #0b0b0b @ 0.1 |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0b0b0b |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.flex.h-control 91.1x32.0 bg #0b0b0b @ 0.1 r 3.35544e+07px |
| How | at rest |

Crops: `docs-nav-active-default.png`.

#### docs-start-title

Docs page title. The h1 at the top of a docs page.

Page: docs-start. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 295.2 x 32.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 26.25px/32.8125px 520 |
| Letter spacing | normal |
| Colour | #0b0b0b |
| Transition | none |
| How | at rest |

Crops: `docs-start-title-default.png`.

#### docs-start-body

Docs body text. A paragraph of docs body copy.

Page: docs-start. Selector: `a prose paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 832 x 25.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 16.875px/25.3125px 400 |
| Letter spacing | normal |
| Colour | #52514e |
| Transition | none |
| How | at rest |

Crops: `docs-start-body-default.png`.

#### docs-start-code-block

Docs code block. A fenced code block in the docs.

Page: docs-start. Selector: `pre`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 754 x 57 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicMono 13px/19px 400 |
| Letter spacing | normal |
| Colour | #1f2328 |
| Text node | span.lj.dt: anthropicMono 13px/19px 400, #953800 |
| Transition | none |
| How | at rest |

Crops: `docs-start-code-block-default.png`.

#### docs-start-inline-code

Docs inline code. Inline `code` in the docs body.

Page: docs-start. Selector: `p code`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 770 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicMono 13px/19px 400 |
| Letter spacing | normal |
| Colour | #1f2328 |
| Text node | span.lj.dt: anthropicMono 13px/19px 400, #953800 |
| Transition | none |
| How | at rest |

Crops: `docs-start-inline-code-default.png`.

#### docs-copy-page

Copy page button. The "Copy page" utility button above the docs body.

Page: docs-start. Selector: `the Copy page button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 111.86 x 28 | = |
| Padding | 0px 10px | = |
| Gap | 6px | = |
| Border | none | = |
| Radius | 7px 0px 0px 7px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | anthropicSans 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #0b0b0b | = |
| Text node | span.-ms-1: Anthropicons-Variable 20px/20px 433.25, #0b0b0b | = |
| Transition | box-shadow 0.06s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | span.absolute.inset-0 111.9x28.0 bg #ffffff @ 0.1 r 7px 0px 0px 7px | span.absolute.inset-0 111.9x28.0 bg #0b0b0b @ 0.05 r 7px 0px 0px 7px |
| Ancestor paint | 3 up div.relative.inline-flex shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = |
| How | at rest | mouse hover |

Crops: `docs-copy-page-default.png`, `docs-copy-page-hover.png`.

#### docs-api-title

Docs page title. The h1 at the top of a docs page.

Page: docs-api. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 130.3 x 35 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 28px/35px 520 |
| Letter spacing | normal |
| Colour | #0b0b0b |
| Transition | none |
| How | at rest |

Crops: `docs-api-title-default.png`.

#### docs-api-body

Docs body text. A paragraph of docs body copy.

Page: docs-api. Selector: `a prose paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 14px/21px 400 |
| Letter spacing | normal |
| Colour | #52514e |
| Transition | none |
| How | at rest |

Crops: `docs-api-body-default.png`.

#### docs-api-inline-code

Docs inline code. Inline `code` in the docs body.

Page: docs-api. Selector: `p code`. States: .

Not found on the page at capture time.

#### docs-method-badge

HTTP method badge. The method badge on an endpoint (POST, GET).

Page: docs-api. Selector: `the method pill`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 31.38 x 15.59 |
| Padding | 0px 0px 0.6px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 12px/15px 500 |
| Letter spacing | normal |
| Colour | #184f95 |
| Transition | none |
| Ancestor paint | 1 up span.inline-flex.items-center bg #76b2fb @ 0.35 |
| How | at rest |

Crops: `docs-method-badge-default.png`.

#### docs-search-field

Search field. The "Search ⌘K" field in the docs chrome (288x32, bg-fill-field). Opens the search dialog.

Page: docs-api. Selector: `the search field button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 239 x 32 | = | = |
| Padding | 0px 5px 0px 8px | = | = |
| Gap | 12px | = | = |
| Border | none | = | = |
| Radius | 8px | = | = |
| Background | #ffffff @ 0.5 | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.1 0px 0px 0px 1px inset | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.2 0px 0px 0px 1px inset | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px |
| Outline | none | = | = |
| Font | anthropicSans 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #898781 | = | = |
| Text node | span: Anthropicons-Variable 16px/16px 533.25, #898781 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.06s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Painted layers | button.flex.h-control 239.0x32.0 bg #ffffff @ 0.5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.1 0px 0px 0px 1px inset; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px | button.flex.h-control 239.0x32.0 bg #ffffff @ 0.5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.2 0px 0px 0px 1px inset; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px | button.flex.h-control 239.0x32.0 bg #ffffff @ 0.5 r 8px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #fcfcfb 0px 0px 0px 1px inset, #2a78d6 0px 0px 0px 1px, #cde2fb 0px 0px 6px 1px; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `docs-search-field-default.png`, `docs-search-field-hover.png`, `docs-search-field-focus-visible.png`.

### Overlays

#### docs-search-dialog

Search dialog. The docs search dialog opened from the header field. Nothing was typed.

Page: docs-home. Selector: `the open search dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672 x 500 |
| Padding | 0px |
| Border | none |
| Radius | 12px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.1 0px 0px 0px 0px inset, #0b0b0b @ 0.1 0px 0px 0px 1px, #0b0b0b @ 0.08 0px 4px 8px 0px, #0b0b0b @ 0.08 0px 12px 28px -2px |
| Outline | none |
| Font | anthropicSans 14px/20px 400 |
| Letter spacing | normal |
| Colour | #0b0b0b |
| Text node | span.shrink-0.text-muted: Anthropicons-Variable 16px/16px 533.25, #898781 |
| Transition | scale 0.12s cubic-bezier(0.165, 0.84, 0.44, 1) |
| ::after | 672px x 500px, absolute, bg #000000 @ 0.4, radius 12px |
| Painted layers | div.cds-dialog-regions.draggable-none 672.0x500.0 bg #ffffff r 12px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0b0b0b @ 0.1 0px 0px 0px 0px inset, #0b0b0b @ 0.1 0px 0px 0px 1px, #0b0b0b @ 0.08 0px 4px 8px 0px, #0b0b0b @ 0.08 0px 12px 28px -2px; div::after.cds-dialog-regions.draggable-none 672pxx500px bg #000000 @ 0.4 r 12px; div.border-b.px-sm 672.0x57.0 border B:1px solid #0b0b0b @ 0.1; div.group.grid 656.0x36.0 bg #0b0b0b @ 0.05 r 8px; div.shrink-0.border-t 672.0x43.0 border T:1px solid #0b0b0b @ 0.1; kbd.inline-flex.shrink-0 18.0x18.0 border T:1px solid #6d6b67 @ 0.18 / R:1px solid #6d6b67 @ 0.18 / B:1px solid #6d6b67 @ 0.18 / L:1px solid #6d6b67 @ 0.18 r 4px |
| How | at rest |

Crops: `docs-search-dialog-default.png`.

#### docs-search-input

Search input. The field inside the search dialog.

Page: docs-home. Selector: `input in the dialog`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 564 x 56 |
| Padding | 16px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #0b0b0b |
| Transition | none |
| Cursor | text |
| Placeholder | #898781, opacity 1 |
| How | at rest |

Crops: `docs-search-input-default.png`.

### Mobile (390 wide)

#### m-nav-bar

Top navigation bar (mobile). The header at 390: wordmark and menu button.

Page: home. Selector: `the mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #faf9f5 |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 16px/24.48px 400 |
| Letter spacing | normal |
| Colour | #141413 |
| Text node | button.f9ZZrG_button.f9ZZrG_corner-full: anthropicSans 13px/20.02px 400, #3d3d3a, ls 0.13px |
| Transition | transform 0.3s ease |
| Icon | 0 x 0, colour #3d3d3a |
| Painted layers | header.UTJ3Tq_root 390.0x84.0 bg #faf9f5; a.f9ZZrG_button.f9ZZrG_corner-full 0.0x0.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px; button.f9ZZrG_button.f9ZZrG_corner-full 0.0x0.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px; button.f9ZZrG_button.f9ZZrG_corner-full 0.0x0.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px; button.f9ZZrG_button.f9ZZrG_corner-full 0.0x0.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px; button.f9ZZrG_button.f9ZZrG_corner-full 0.0x0.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 999999px |
| Ancestor paint | 1 up body bg #faf9f5 |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-nav-menu-btn

Nav menu button (mobile). The menu button in the mobile header. Opened for the screenshot; nothing is followed.

Page: home. Selector: `the menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 28 x 28 |
| Padding | 8px |
| Gap | 8px |
| Border | 1px solid #e8e6dc |
| Radius | 8px |
| Background | #f5f4ed |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 13px/20.02px 400 |
| Letter spacing | 0.13px |
| Colour | #3d3d3a |
| Transition | border-color, box-shadow, background-color, color 0.2s, 0.2s, 0.2s, 0.2s ease-in-out delay 0s, 0s, 0s, 0s |
| Cursor | pointer |
| Icon | 20 x 20, colour #3d3d3a |
| Painted layers | button.f9ZZrG_button.f9ZZrG_corner-small 28.0x28.0 bg #f5f4ed border T:1px solid #e8e6dc / R:1px solid #e8e6dc / B:1px solid #e8e6dc / L:1px solid #e8e6dc r 8px |
| How | at rest |

Crops: `m-nav-menu-btn-default.png`.

#### m-nav-sheet

Mobile nav sheet. The open navigation sheet at 390.

Page: home. Selector: `the open menu`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #141413 |
| Box shadow | none |
| Outline | none |
| Font | anthropicSans 16px/24.48px 400 |
| Letter spacing | normal |
| Colour | #b0aea5 |
| Text node | span.OU0HOa_mainLabel: anthropicSans 30px/38px 600, #faf9f5 |
| Transition | opacity 0.15s ease |
| Icon | 35 x 24, colour #faf9f5 |
| Painted layers | div.A1YAyq_popup.theme-slate 390.0x844.0 bg #141413; button.f9ZZrG_button.f9ZZrG_corner-small 28.0x28.0 bg #262624 border T:1px solid #3d3d3a / R:1px solid #3d3d3a / B:1px solid #3d3d3a / L:1px solid #3d3d3a r 8px; div::before.A1YAyq_viewport.base-ui-disable-scrollbar 390pxx0px image linear-gradient(#141413, #000000 @ 0); div::after.A1YAyq_viewport.base-ui-disable-scrollbar 390pxx40px image linear-gradient(to top, #141413, #000000 @ 0); span.HhA2_a_picture 293.5x165.4 bg #1f1e1d border T:1px solid #848484 @ 0.2 / R:1px solid #848484 @ 0.2 / B:1px solid #848484 @ 0.2 / L:1px solid #848484 @ 0.2 r 4px; span.HhA2_a_picture 293.5x165.4 bg #1f1e1d border T:1px solid #848484 @ 0.2 / R:1px solid #848484 @ 0.2 / B:1px solid #848484 @ 0.2 / L:1px solid #848484 @ 0.2 r 4px |
| How | at rest |

Crops: `m-nav-sheet-default.png`.

#### m-hero-title

Hero title (mobile). The h1 at 390.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 326 x 260 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | anthropicSerif 25px/32.5px 400 |
| Letter spacing | -0.25px |
| Colour | #141413 |
| Text node | span.LOCOdG_lead: anthropicSans 25px/32.5px 600, #141413, ls -0.25px |
| Transition | color 0.3s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `m-hero-title-default.png`.

## Transitions declared in the readable stylesheets

The Anthropic sites serve their stylesheets same-origin but as CSS modules with hashed prefixes, so this list holds the transition rules the CSSOM could read on each page; the per-state Transition rows above are computed values and cover the real rules.

- docs-api: `transform var(--cds-dur-slow) var(--cds-btn-spring)`, `transform var(--cds-dur-fast) ease-out`, `clip-path var(--cds-dur-slow) var(--cds-btn-spring)`, `clip-path var(--cds-dur-fast) ease-out`, `none`, `opacity 0s linear calc((1 - var(--cds-message-actions-opacity)) * ( var(--cds-message-actions-reveal-out-delay) + var(--cds-message-actions-reveal-out-duration) ))`, `opacity 0.2s cubic-bezier(0.215, 0.61, 0.355, 1), transform 0.2s cubic-bezier(0.215, 0.61, 0.355, 1)`, `transform 0.18s cubic-bezier(0.215, 0.61, 0.355, 1), opacity 0.18s cubic-bezier(0.215, 0.61, 0.355, 1)`, `transform 0.15s ease-out`

- docs-start: `transform var(--cds-dur-slow) var(--cds-btn-spring)`, `transform var(--cds-dur-fast) ease-out`, `clip-path var(--cds-dur-slow) var(--cds-btn-spring)`, `clip-path var(--cds-dur-fast) ease-out`, `none`, `opacity 0s linear calc((1 - var(--cds-message-actions-opacity)) * ( var(--cds-message-actions-reveal-out-delay) + var(--cds-message-actions-reveal-out-duration) ))`, `opacity 0.2s cubic-bezier(0.215, 0.61, 0.355, 1), transform 0.2s cubic-bezier(0.215, 0.61, 0.355, 1)`, `transform 0.18s cubic-bezier(0.215, 0.61, 0.355, 1), opacity 0.18s cubic-bezier(0.215, 0.61, 0.355, 1)`

- home: `color 0.2s ease-out`, `background-color 0.25s, border-color 0.25s, color 0.25s`, `background-color 0.2s`, `opacity 0.25s, scale 0.25s`, `color .2s var(--ease-in-quart)`, `translate 0.25s cubic-bezier(0.2, 0.8, 0.2, 1)`, `color 0.1s ease-out`, `rotate 0.15s`, `transform 0.15s, opacity 0.15s`, `border-color 0.2s, background-color 0.2s, box-shadow 0.2s`, `color 0.3s`, `transform 0.3s ease-in-out`
