# Component measurements

Computed styles read from cofounder.co on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) on the site's light surface (no consent overlay mounted on the captured routes), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Nav bar. The fixed site header (position:fixed, transparent at top, border+shadow on scroll): logo, flat nav links, Run-a-company CTA.

Page: home. Selector: `header.site-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 91 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #e8e7e6 @ 0; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #ffffff @ 0 0px 1px 0px 0px |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span.nav-link.relative: neoris 15px/22.5px 410, #fbfbf8, ls 0.15px |
| Transition | border-color, box-shadow, background-color 0.02s, 0.02s, 0.12s ease-in-out, ease-in-out, ease-out delay 0s, 0s, 0.03s |
| Icon | 126 x 26, colour #171717 |
| Painted layers | header.site-header.fixed 1440.0x91.0 border B:1px solid #e8e7e6 @ 0 shadow #ffffff @ 0 0px 1px 0px 0px; span.pointer-events-none.absolute 369.8x41.0 image linear-gradient(#ffffff @ 0.16 0%, #ffffff @ 0.08 100%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.24 0px 1px 1px 0px inset; span.pointer-events-none.absolute 56.8x26.5 bg #fbfbf8 @ 0.12 r 4px; span.pointer-events-none.absolute 55.8x26.5 bg #fbfbf8 @ 0.12 r 4px; span.pointer-events-none.absolute 45.6x26.5 bg #fbfbf8 @ 0.12 r 4px; span.pointer-events-none.absolute 58.8x26.5 bg #fbfbf8 @ 0.12 r 4px |
| Ancestor paint | 1 up body.min-h-full.flex bg #f5f5f2 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Cofounder mark+wordmark home anchor in the header.

Page: home. Selector: `header a[aria-label=Home]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 126 x 26 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Cursor | pointer |
| Icon | 126 x 26, colour #171717 |
| Ancestor paint | 2 up header.site-header.fixed shadow #ffffff @ 0 0px 1px 0px 0px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav link. A flat nav link (nav-link, 15px/410 weight, text-surface-raised): Start/Build/Sell/Scale/Resources/Pricing.

Page: home. Selector: `a.nav-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46.75 x 22.5 | = | = | = |
| Padding | 0px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 15px/22.5px 410 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #fbfbf8 | = | = | = |
| Transition | color, font-weight 0.06s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 34.75px x 0px, static, bg #000000 @ 0, radius 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.nav-link.relative 46.8x22.5 outline 1px auto #101010 offset 1px | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-cta

Nav CTA. The header "Run a company" pill linking to app.cofounder.co/os; measured never followed.

Page: home. Selector: `a[data-analytics-location=site_nav/site_header]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130 x 41 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span.font-[460].text-[15px]: neoris 15px/22.5px 460, #1a1a1a, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.pointer-events-none.absolute 130.0x41.0 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px; span.pointer-events-none.absolute 130.0x41.0 bg #f1f1ee border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.5 0px 1px 1px 0px, #ffffff @ 0.23 0px 0px 0px 1px; span.pointer-events-none.absolute 130.0x41.0 bg #e7e7e1 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #ffffff @ 0.35 0px 0px 0.357px 1.5px inset | = | a.group.relative 130.0x41.0 r 8px outline 1px auto #101010 offset 1px; span.pointer-events-none.absolute 130.0x41.0 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px; span.pointer-events-none.absolute 130.0x41.0 bg #f1f1ee border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.5 0px 1px 1px 0px, #ffffff @ 0.23 0px 0px 0px 1px; span.pointer-events-none.absolute 130.0x41.0 bg #e7e7e1 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #ffffff @ 0.35 0px 0px 0.357px 1.5px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. "Cofounder lets you run an entire company with AI" — the hero headline (hero-gradient-text, 46px/108%).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 580 x 99.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#ffffff 0%, #ffffff @ 0.9 100%) |
| Box shadow | none |
| Outline | none |
| Font | neoris 46px/49.68px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | h1.m-0.font-normal 580.0x99.4 image linear-gradient(#ffffff 0%, #ffffff @ 0.9 100%) |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The hero "Run a company" anchor linking to app.cofounder.co/os; measured never followed.

Page: home. Selector: `a[data-analytics-location=hero]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.95 x 41 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #202020 @ 0.1 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f5f5f2 | #ededea | = | #ededea |
| Box shadow | #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span.text-[15px].font-[460]: neoris 15px/22.5px 460, #171717, ls 0.15px | = | = | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 128.0x41.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | a.group.relative 128.0x41.0 bg #ededea border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | a.group.relative 128.0x41.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset outline 1px auto #101010 offset 1px | a.group.relative 128.0x41.0 bg #ededea border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-prompt-btn

Prompt button. The glass "copy the setup prompt" hero button (glass-hero-btn, backdrop-blur 24px); never pressed — it writes the clipboard. Hover/focus/forced states only.

Page: home. Selector: `button[data-analytics-cta=copy_setup_prompt]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 179.56 x 41 | = | = | = |
| Padding | 0px 10px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(24px) | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 4px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.min-w-[132px].text-[15px]: neoris 15px/22.5px 460, #ffffff, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | span.pointer-events-none.absolute 179.6x41.0 bg #ffffff @ 0.05 r 8px; span.pointer-events-none.absolute 179.6x41.0 image linear-gradient(#000000 @ 0.12, #000000 @ 0.2) r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.24 0px 1px 1px 0px inset; span.pointer-events-none.absolute 179.6x41.0 image linear-gradient(#000000 @ 0.08, #000000 @ 0.15) r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.6 0px 2px 1px 0px inset | = | button.group.relative 179.6x41.0 r 8px outline 2px solid #ffffff offset 4px; span.pointer-events-none.absolute 179.6x41.0 bg #ffffff @ 0.05 r 8px; span.pointer-events-none.absolute 179.6x41.0 image linear-gradient(#000000 @ 0.12, #000000 @ 0.2) r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.24 0px 1px 1px 0px inset; span.pointer-events-none.absolute 179.6x41.0 image linear-gradient(#000000 @ 0.08, #000000 @ 0.15) r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.6 0px 2px 1px 0px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-prompt-btn-default.png`, `hero-prompt-btn-hover.png`, `hero-prompt-btn-focus-visible.png`, `hero-prompt-btn-pressed.png`.

#### cta-dark

Dark CTA. A cta-btn-dark control — the dark button style used for mid-page actions.

Page: home. Selector: `.cta-btn-dark`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 183.7 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #383838 | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 @ 0.85 100%) | = | = | = |
| Box shadow | #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px | = | = | = |
| Outline | none | = | 2px solid #262323 @ 0.8 offset 4px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span.text-[15px].font-[460]: neoris 15px/22.5px 460, #ffffff @ 0.9, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff @ 0.9 | = | = | = |
| Painted layers | a.group.relative 183.7x44.0 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px; span.pointer-events-none.absolute 181.7x42.0 image linear-gradient(#202020 @ 0.8 0%, #202020 @ 0.8 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.4 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset | = | a.group.relative 183.7x44.0 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px outline 2px solid #262323 @ 0.8 offset 4px; span.pointer-events-none.absolute 181.7x42.0 image linear-gradient(#202020 @ 0.8 0%, #202020 @ 0.8 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.4 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-dark-default.png`, `cta-dark-hover.png`, `cta-dark-focus-visible.png`, `cta-dark-pressed.png`.

#### cta-light

Light CTA. A btn-light-surface control — the light pill button style.

Page: home. Selector: `.btn-light-surface`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.95 x 41 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #202020 @ 0.1 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f5f5f2 | #ededea | = | #ededea |
| Box shadow | #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span.text-[15px].font-[460]: neoris 15px/22.5px 460, #171717, ls 0.15px | = | = | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 128.0x41.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | a.group.relative 128.0x41.0 bg #ededea border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | a.group.relative 128.0x41.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset outline 1px auto #101010 offset 1px | a.group.relative 128.0x41.0 bg #ededea border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-light-default.png`, `cta-light-hover.png`, `cta-light-focus-visible.png`, `cta-light-pressed.png`.

#### blue-section

Tools band. The #1a6fd1 "All the tools and systems" band with the tools diagram and tab toggles.

Page: home. Selector: `section.bg-[#1a6fd1]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 1221.81 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #1a6fd1 |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.m-0.mx-auto: neoris 40px/46px 400, #ffffff |
| Transition | none |
| Icon | 110 x 6, colour #ffffff |
| Painted layers | section.relative.w-full 1425.0x1221.8 bg #1a6fd1; span 354.0x50.0 image linear-gradient(#ffffff @ 0.8 -0.93%, #ffffff @ 0.64 104.17%); span.shrink-0.loader-bar-after 1.0x44.0 bg #ffffff @ 0.35; span::after.shrink-0.loader-bar-after 1pxx44px bg #2688dd; span.absolute.left-0 1.0x0.0 bg #ffffff; span.shrink-0.loader-bar-after 1.0x44.0 bg #ffffff @ 0.35 |
| Ancestor paint | 1 up body.min-h-full.flex bg #f5f5f2 |
| How | at rest |

Crops: `blue-section-default.png`.

#### tool-tab

Tools tab (selected). The selected aria-pressed tab in the tools band (text-white selected).

Page: home. Selector: `button[aria-pressed=true] in tools band`. States: default, focus-visible.

| Property | default | focus-visible |
|---|---|---|
| Size (w x h) | 234.66 x 44.81 | 234.67 x 44.81 |
| Padding | 0px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | 1px solid #ffffff @ 0.8 offset 2px |
| Font | neoris 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Text node | span.text-[15px].md:text-[16px]: neoris 16px/22.4px 460, #ffffff, ls 0.16px | = |
| Transition | none | = |
| Cursor | default | = |
| Painted layers | span.shrink-0.loader-bar-after 1.0x44.0 bg #ffffff @ 0.35; span::after.shrink-0.loader-bar-after 1pxx44px bg #2688dd; span.absolute.left-0 1.0x11.0 bg #ffffff | button.group.min-w-0 234.7x44.8 outline 1px solid #ffffff @ 0.8 offset 2px; span.shrink-0.loader-bar-after 1.0x44.0 bg #ffffff @ 0.35; span::after.shrink-0.loader-bar-after 1pxx44px bg #2688dd; span.absolute.left-0 1.0x7.8 bg #ffffff |
| How | at rest | keydown then focus() |

Crops: `tool-tab-default.png`, `tool-tab-focus-visible.png`.

#### tool-tab-off

Tools tab (unselected). An unselected aria-pressed tab (text-white/40, hover white/60); never pressed — it swaps the diagram.

Page: home. Selector: `button[aria-pressed=false] in tools band`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 234.66 x 44.81 | = | = |
| Padding | 0px | = | = |
| Gap | 16px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px solid #ffffff @ 0.8 offset 2px |
| Font | neoris 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff @ 0.4 | #ffffff @ 0.6 | = |
| Text node | span.text-[15px].md:text-[16px]: neoris 16px/22.4px 460, #ffffff @ 0.4, ls 0.16px | span.text-[15px].md:text-[16px]: neoris 16px/22.4px 460, #ffffff @ 0.6, ls 0.16px | = |
| Transition | none | = | = |
| Cursor | default | = | = |
| Painted layers | span.shrink-0.loader-bar-after 1.0x44.0 bg #ffffff @ 0.35; span::after.shrink-0.loader-bar-after 1pxx44px bg #2688dd | = | button.group.min-w-0 234.7x44.8 outline 1px solid #ffffff @ 0.8 offset 2px; span.shrink-0.loader-bar-after 1.0x44.0 bg #ffffff @ 0.35; span::after.shrink-0.loader-bar-after 1pxx44px bg #2688dd |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `tool-tab-off-default.png`, `tool-tab-off-hover.png`, `tool-tab-off-focus-visible.png`.

#### tool-button

Tool button. A tool/agent picker button (border-black/10 bg-white/60 rounded-[10px], hover white-fill swap).

Page: home. Selector: `button.border-black/10`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 47 | = | = | = |
| Padding | 12px 16px | = | = | = |
| Gap | 12px | = | = | = |
| Border | 1px solid #000000 @ 0.1 | 1px solid #000000 @ 0.2 | = | 1px solid #000000 @ 0.2 |
| Radius | 10px | = | = | = |
| Background | #ffffff @ 0.6 | #ffffff | = | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 1px 0px 0px inset | = | = | = |
| Outline | none | = | 2px solid #262323 @ 0.8 offset 2px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span.font-mono.text-[10px]: IBM Plex Mono 10px/15px 400, #262323 @ 0.5 | = | = | = |
| Transition | background-color, border-color, transform 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 16 x 16, colour #262323 @ 0.5 | = | = | = |
| Painted layers | button.group.flex 340.0x47.0 bg #ffffff @ 0.6 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 1px 0px 0px inset | button.group.flex 340.0x47.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 1px 0px 0px inset | button.group.flex 340.0x47.0 bg #ffffff @ 0.6 border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 1px 0px 0px inset outline 2px solid #262323 @ 0.8 offset 2px | button.group.flex 340.0x47.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 10px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #ffffff @ 0.8 0px 1px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tool-button-default.png`, `tool-button-hover.png`, `tool-button-focus-visible.png`, `tool-button-pressed.png`.

#### case-study

Case study card. A case-study card anchor.

Page: home. Selector: `a[aria-label="View Cofounder case studies"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 182 x 96 | = | = | = |
| Padding | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div.logo-tile.flex 170.0x84.0 bg #f3f3f0 r 10px shadow #ffffff 0px 0px 0px 1px inset, #000000 @ 0.12 1px 1px 4px 0px inset, #ffffff @ 0.7 -2px -2px 3px 0px inset | = | a.flex.items-center 182.0x96.0 outline 1px auto #101010 offset 1px; div.logo-tile.flex 170.0x84.0 bg #f3f3f0 r 10px shadow #ffffff 0px 0px 0px 1px inset, #000000 @ 0.12 1px 1px 4px 0px inset, #ffffff @ 0.7 -2px -2px 3px 0px inset | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `case-study-default.png`, `case-study-hover.png`, `case-study-focus-visible.png`, `case-study-pressed.png`.

#### carousel-prev

Carousel arrow. A campaign-carousel arrow button.

Page: home. Selector: `button[aria-label="Previous campaign"]`. States: .

Not found on the page at capture time.

#### logo-tile

Logo tile. A customer logo tile (170x84) in the social-proof row.

Page: home. Selector: `.logo-tile`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 170 x 84 |
| Padding | 28px |
| Border | none |
| Radius | 10px |
| Background | #f3f3f0 |
| Box shadow | #ffffff 0px 0px 0px 1px inset, #000000 @ 0.12 1px 1px 4px 0px inset, #ffffff @ 0.7 -2px -2px 3px 0px inset |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.logo-tile.flex 170.0x84.0 bg #f3f3f0 r 10px shadow #ffffff 0px 0px 0px 1px inset, #000000 @ 0.12 1px 1px 4px 0px inset, #ffffff @ 0.7 -2px -2px 3px 0px inset |
| How | at rest |

Crops: `logo-tile-default.png`.

#### logo-pill

Tool logo pill. An agent-tool logo pill (ChatGPT/Claude/Cursor/Codex icons in /agent-icons/).

Page: home. Selector: `.logo-pill`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 92.45 x 24.16 |
| Padding | 5px 10px |
| Gap | 4px |
| Border | 1px solid #383838 |
| Radius | 20px |
| Background | transparent |
| Background image | linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 @ 0.85 100%) |
| Box shadow | #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span.m-0.text-[13px]: neoris 13px/18.2px 460, #ffffff @ 0.9, ls 0.13px |
| Transition | none |
| Icon | 9.6 x 9.6, colour #171717 |
| Painted layers | span.logo-pill.inline-flex 92.5x24.2 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 20px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px |
| How | at rest |

Crops: `logo-pill-default.png`.

#### section-title

Section title. A section heading under the hero (Neoris, 28-40px responsive).

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1052 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 40px/46px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span.text-ink: neoris 40px/46px 400, #262323 @ 0.8 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### page-ground

Page ground. The body element painted fill — the page ground (--background #f5f5f2).

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 9446.42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f5f5f2 |
| Box shadow | none |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span.nav-link.relative: neoris 15px/22.5px 460, #202020 @ 0.4, ls 0.15px |
| Transition | none |
| Icon | 0 x 0, colour #171717, fill #000000 |
| Painted layers | body.min-h-full.flex 1425.0x9446.4 bg #f5f5f2; header.site-header.fixed 1440.0x91.0 bg #f5f5f2 border B:1px solid #e8e7e6 shadow #ffffff 0px 1px 0px 0px; span.pointer-events-none.absolute 369.8x41.0 image linear-gradient(#ffffff @ 0.16 0%, #ffffff @ 0.08 100%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.24 0px 1px 1px 0px inset; span.pointer-events-none.absolute 56.8x26.5 bg #e7e7e3 @ 0.8 r 4px; span.pointer-events-none.absolute 55.8x26.5 bg #e7e7e3 @ 0.8 r 4px; span.pointer-events-none.absolute 45.6x26.5 bg #e7e7e3 @ 0.8 r 4px |
| Ancestor paint | 1 up html.h-full.antialiased bg #f5f5f2 |
| How | at rest |

Crops: none.

### Footer

#### footer

Footer. The footer band (footer-bg): the Run-a-company CTA card, link columns, social icons and legal row.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1425 x 749.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span.text-ink-navy.md:text-ink: neoris 40px/46px 400, #262323 @ 0.8 |
| Transition | none |
| Icon | 15 x 15, colour #262323 @ 0.5 |
| Painted layers | div.absolute.inset-0 1052.0x610.3 image radial-gradient(circle, #ffffff @ 0 30%, #f5f5f2 80%); div.block.p-[12px] 0.0x0.0 bg #fbfbf8 @ 0.8 r 16px shadow #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset, #000000 @ 0.25 0px 0px 2px 0px, #e8e7e6 @ 0.32 0px 0px 0px 4px; div.-mt-[232px].md:-mt-[200px] 0.0x0.0 image linear-gradient(#ffffff @ 0.06 0%, #ffffff @ 0.03 100%) r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.24 0px 1px 1px 0px inset; span 0.0x0.0 image linear-gradient(#ffffff @ 0.8 -0.93%, #ffffff @ 0.64 104.17%); a.group.relative 0.0x0.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset; a::before.footer-link.text-ink 94.8125pxx23px bg #e7e7e3 @ 0.8 r 4px |
| Ancestor paint | 1 up body.min-h-full.flex bg #f5f5f2 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in a footer link column (footer-link) — the md:hidden mobile CTA copy is skipped.

Page: home. Selector: `footer a.footer-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 46.06 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 15px/21px 460 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #262323 @ 0.8 | = | = | = |
| Transition | color 0.2s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 58.0625px x 23px, absolute, bg #e7e7e3 @ 0.8, radius 4px | = | = | = |
| Painted layers | a::before.footer-link.text-ink 58.0625pxx23px bg #e7e7e3 @ 0.8 r 4px | = | a.footer-link.text-ink 46.1x19.0 outline 1px auto #101010 offset 1px; a::before.footer-link.text-ink 58.0625pxx23px bg #e7e7e3 @ 0.8 r 4px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A footer social icon link (X/LinkedIn).

Page: home. Selector: `footer a[aria-label=X/LinkedIn]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #202020 @ 0.1 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f5f5f2 | #ededea | = | #ededea |
| Box shadow | #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262323 @ 0.5 | #e1e8e7 | = | #e1e8e7 |
| Transition | background-color, box-shadow 0.14s, 0.14s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 15 x 15, colour #262323 @ 0.5 | 15 x 15, colour #e1e8e7 | = | 15 x 15, colour #e1e8e7 |
| Painted layers | a.group.relative 36.0x36.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | a.group.relative 36.0x36.0 bg #ededea border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | a.group.relative 36.0x36.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset outline 1px auto #101010 offset 1px | a.group.relative 36.0x36.0 bg #ededea border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-cta

Footer CTA. The footer CTA card "Run a company" button (btn-light-surface) linking to app.cofounder.co/os; measured never followed.

Page: home. Selector: `footer a[data-analytics-location=footer_card]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.96 x 41 | 129.04 x 41.83 | 128.28 x 41.25 | = |
| Padding | 0px 12px | = | = | = |
| Border | 1px solid #202020 @ 0.1 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f5f5f2 | #f2f2ef | = | #ededea |
| Box shadow | #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span.text-[15px].font-[460]: neoris 15px/22.5px 460, #171717, ls 0.15px | = | = | = |
| Transition | background-color, box-shadow 0.14s, 0.14s ease-out, ease-out delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.group.relative 128.0x41.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | a.group.relative 129.0x41.8 bg #f2f2ef border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset | a.group.relative 128.3x41.3 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset outline 1px auto #101010 offset 1px | a.group.relative 128.0x41.0 bg #ededea border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset |
| Ancestor paint | 1 up div.-mt-[232px].md:-mt-[200px] shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.24 0px 1px 1px 0px inset; 2 up div.block.p-[12px] bg #fbfbf8 @ 0.8 shadow #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset, #000000 @ 0.25 0px 0px 2px 0px, #e8e7e6 @ 0.32 0px 0px 0px 4px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-cta-default.png`, `footer-cta-hover.png`, `footer-cta-focus-visible.png`, `footer-cta-pressed.png`.

### Pricing

#### pricing-title

Pricing title. The visible pricing headline (the h1 is sr-only).

Page: pricing. Selector: `first visible h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1032 x 69 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 46px/69px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span.text-ink: neoris 46px/69px 400, #262323 @ 0.8 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-card

Plan card. A whole-card plan anchor (pricing-card-group -> pricing-card): border-border-card bg-surface-raised rounded-2xl, hover reveals the hidden CTA chip (no lift transition - the anchor computes 0s). Links to app.cofounder.co; never followed.

Page: pricing. Selector: `a.pricing-card-group`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 640 x 594 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | neoris 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #171717 | = | = | = |
| Text node | span.m-0.text-[15px]: neoris 15px/21px 460, #262323 @ 0.7, ls 0.15px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 21 x 21, colour #171717 | = | = | = |
| Painted layers | div.pricing-card.relative 640.0x594.0 bg #fbfbf8 border T:1px solid #dee2de / R:1px solid #dee2de / B:1px solid #dee2de / L:1px solid #dee2de r 16px shadow #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset, #000000 @ 0.25 0px 0px 2px 0px, #e8e7e6 @ 0.32 0px 0px 0px 4px; span.cta-btn-dark.relative 89.3x30.8 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px; div.relative.w-full 614.0x220.0 bg #f5f5f2 border T:1px solid #dee2de / R:1px solid #dee2de / B:1px solid #dee2de / L:1px solid #dee2de r 8px; span.cta-btn-dark.relative 0.0x0.0 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px | = | a.pricing-card-group.group 640.0x594.0 outline 1px auto #101010 offset 1px; div.pricing-card.relative 640.0x594.0 bg #fbfbf8 border T:1px solid #dee2de / R:1px solid #dee2de / B:1px solid #dee2de / L:1px solid #dee2de r 16px shadow #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset, #000000 @ 0.25 0px 0px 2px 0px, #e8e7e6 @ 0.32 0px 0px 0px 4px; span.cta-btn-dark.relative 89.3x30.8 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px; div.relative.w-full 614.0x220.0 bg #f5f5f2 border T:1px solid #dee2de / R:1px solid #dee2de / B:1px solid #dee2de / L:1px solid #dee2de r 8px; span.cta-btn-dark.relative 0.0x0.0 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-card-default.png`, `plan-card-hover.png`, `plan-card-focus-visible.png`, `plan-card-pressed.png`.

#### plan-name

Plan name. The plan label row inside a pricing card (15px ink-muted).

Page: pricing. Selector: `.pricing-card-group .text-ink-muted`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 71.36 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 15px/21px 460 |
| Letter spacing | 0.15px |
| Colour | #262323 @ 0.7 |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 3 up div.pricing-card.relative bg #fbfbf8 shadow #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset, #000000 @ 0.25 0px 0px 2px 0px, #e8e7e6 @ 0.32 0px 0px 0px 4px |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-cta

Revealed CTA chip. The "Get started" cta-btn-dark chip a plan card reveals on hover; exists only while the card is hovered — held open by the card's own hover, never followed.

Page: pricing. Selector: `.pricing-card-group .cta-btn-dark`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 89.33 x 30.8 | = |
| Padding | 6px 12px | = |
| Gap | 6px | = |
| Border | 1px solid #383838 | = |
| Radius | 8px | = |
| Background | transparent | = |
| Background image | linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 @ 0.85 100%) | = |
| Box shadow | #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px | = |
| Outline | none | = |
| Font | neoris 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #171717 | = |
| Text node | span.relative.z-10: neoris 12px/16.8px 460, #ffffff @ 0.9, ls 0.12px | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | span.cta-btn-dark.relative 89.3x30.8 image linear-gradient(#202020 @ 0.1 0%, #202020 @ 0.1 100%), linear-gradient(#4f4f4f 0%, #202020 border T:1px solid #383838 / R:1px solid #383838 / B:1px solid #383838 / L:1px solid #383838 r 8px shadow #404040 @ 0.12 0px 0px 0px 1px, #ffffff @ 0.24 0px 2px 0px 0px inset, #000000 @ 0.25 0px -0.5px 2px 0px inset, #000000 @ 0.03 0px 2px 8px 0px, #000000 @ 0.16 0px 3px 4px 0px | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-pressed.png`.

### How-to guides

#### howto-title

Guide title. The how-to guide headline (40px Neoris at 1440).

Page: howto. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 620 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 40px/46px 400 |
| Letter spacing | normal |
| Colour | #262323 @ 0.8 |
| Text node | span.text-ink: neoris 40px/46px 400, #262323 @ 0.8 |
| Transition | none |
| How | at rest |

Crops: `howto-title-default.png`.

#### howto-section

Guide section. The how-to guide content column.

Page: howto. Selector: `main`. States: .

Not found on the page at capture time.

#### howto-heading

Guide heading. A section heading inside the guide (24px/530).

Page: howto. Selector: `h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 620 x 33.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 24px/33.6px 530 |
| Letter spacing | 0.24px |
| Colour | #262323 @ 0.8 |
| Transition | none |
| How | at rest |

Crops: `howto-heading-default.png`.

#### howto-card-title

Card title. A step/card title inside the guide (15px/530).

Page: howto. Selector: `h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 620 x 21 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 15px/21px 530 |
| Letter spacing | 0.15px |
| Colour | #262323 @ 0.8 |
| Transition | none |
| How | at rest |

Crops: `howto-card-title-default.png`.

### App sign-in (boundary)

#### signin-card

Sign-in card. The app.cofounder.co/os login surface: the sign-in card the app paints. Measured at rest, never submitted.

Page: signin. Selector: `main/first visible login container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1430 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #fcfcf9 |
| Box shadow | none |
| Outline | none |
| Font | anotherSans 14px/19.6px 400 |
| Letter spacing | -0.21px |
| Colour | #202020 |
| Text node | h1.font-mark.text-28: mondwest 32px/38px 400, #202020, ls -0.21px |
| Transition | none |
| Icon | 16 x 16, colour #202020 @ 0.72 |
| Painted layers | main.login-page-theme-light.relative 1430.0x900.0 bg #fcfcf9; button.shrink-0.items-center 384.0x52.0 image linear-gradient(to top, #0f0f0f, #262626) border T:2px solid #4f4f4f / R:2px solid #4f4f4f / B:2px solid #4f4f4f / L:2px solid #4f4f4f r 3.35544e+07px shadow #000000 @ 0.03 0px 13px 5px 0px, #000000 @ 0.07 0px 7px 4px 0px, #000000 @ 0.14 0px 3px 3px 0px, #000000 @ 0.19 0px 1px 2px 0px, #ffffff @ 0.2 0px 0px 0.357px 1.071px inset, #ffffff @ 0.15 0px 0px 0.357px 1.071px inset; button.shrink-0.items-center 384.0x48.0 bg #fefefb r 3.35544e+07px shadow #ffffff @ 0.53 0px 1px 0px 0px inset, #ffffff 0px 0px 1px 1px inset, #000000 @ 0.07 0px 0.5px 1px 0px, #000000 @ 0.13 0px 0px 1px 0px, #000000 @ 0.13 0px 0px 4px -1px |
| How | at rest |

Crops: `signin-card-default.png`.

#### signin-button

Continue button. A "Continue with" OAuth button on the sign-in card; measured never pressed.

Page: signin. Selector: `first visible button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 52 | = | = | = |
| Padding | 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 2px solid #4f4f4f | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to top, #0f0f0f, #262626) | = | = | = |
| Box shadow | #000000 @ 0.03 0px 13px 5px 0px, #000000 @ 0.07 0px 7px 4px 0px, #000000 @ 0.14 0px 3px 3px 0px, #000000 @ 0.19 0px 1px 2px 0px, #ffffff @ 0.2 0px 0px 0.357px 1.071px inset, #ffffff @ 0.15 0px 0px 0.357px 1.071px inset | none | = | none |
| Outline | none | = | = | = |
| Font | ttNeoris 14px/19.6px 500 | = | = | = |
| Letter spacing | -0.21px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.inline-flex.items-center: ttNeoris 14px/19.6px 500, #ffffff, ls -0.21px | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | default | = | = | = |
| Icon | 20 x 20, colour #ffffff, fill #000000 | = | = | = |
| Painted layers | button.shrink-0.items-center 384.0x52.0 image linear-gradient(to top, #0f0f0f, #262626) border T:2px solid #4f4f4f / R:2px solid #4f4f4f / B:2px solid #4f4f4f / L:2px solid #4f4f4f r 3.35544e+07px shadow #000000 @ 0.03 0px 13px 5px 0px, #000000 @ 0.07 0px 7px 4px 0px, #000000 @ 0.14 0px 3px 3px 0px, #000000 @ 0.19 0px 1px 2px 0px, #ffffff @ 0.2 0px 0px 0.357px 1.071px inset, #ffffff @ 0.15 0px 0px 0.357px 1.071px inset | button.shrink-0.items-center 384.0x52.0 image linear-gradient(to top, #0f0f0f, #262626) border T:2px solid #4f4f4f / R:2px solid #4f4f4f / B:2px solid #4f4f4f / L:2px solid #4f4f4f r 3.35544e+07px | = | button.shrink-0.items-center 384.0x52.0 image linear-gradient(to top, #0f0f0f, #262626) border T:2px solid #4f4f4f / R:2px solid #4f4f4f / B:2px solid #4f4f4f / L:2px solid #4f4f4f r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.9 | = | 0.9 |

Crops: `signin-button-default.png`, `signin-button-hover.png`, `signin-button-focus-visible.png`, `signin-button-pressed.png`.

#### signin-back

Back link. The "Back to Cofounder" link returning to the marketing site.

Page: signin. Selector: `a[aria-label="Back to Cofounder"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | transparent | #202020 @ 0.05 | = | #202020 @ 0.05 |
| Box shadow | none | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #202020 @ 0.1 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | none | = | = | = |
| Font | anotherSans 14px/19.6px 400 | = | = | = |
| Letter spacing | -0.21px | = | = | = |
| Colour | #202020 @ 0.72 | #202020 | = | #202020 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #202020 @ 0.72 | 16 x 16, colour #202020 | = | 16 x 16, colour #202020 |
| Ancestor paint | 1 up main.login-page-theme-light.relative bg #fcfcf9 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.absolute.left-4 40.0x40.0 bg #202020 @ 0.05 r 3.35544e+07px | a.absolute.left-4 40.0x40.0 r 3.35544e+07px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #202020 @ 0.1 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | a.absolute.left-4 40.0x40.0 bg #202020 @ 0.05 r 3.35544e+07px |

Crops: `signin-back-default.png`, `signin-back-hover.png`, `signin-back-focus-visible.png`, `signin-back-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile bar. The 390 mobile header bar: logo + menu toggle.

Page: home. Selector: `header.site-header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 78 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #e8e7e6 @ 0; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | #ffffff @ 0 0px 1px 0px 0px |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span.font-[460].text-[15px]: neoris 15px/22.5px 460, #1a1a1a, ls 0.15px |
| Transition | border-color, box-shadow, background-color 0.02s, 0.02s, 0.12s ease-in-out, ease-in-out, ease-out delay 0s, 0s, 0.03s |
| Icon | 87.22 x 18, colour #171717 |
| Painted layers | header.site-header.fixed 390.0x78.0 border B:1px solid #e8e7e6 @ 0 shadow #ffffff @ 0 0px 1px 0px 0px; span.pointer-events-none.absolute 0.0x0.0 image linear-gradient(#ffffff @ 0.16 0%, #ffffff @ 0.08 100%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.24 0px 1px 1px 0px inset; span.pointer-events-none.absolute 0.0x0.0 bg #fbfbf8 @ 0.12 r 4px; span.pointer-events-none.absolute 0.0x0.0 bg #fbfbf8 @ 0.12 r 4px; span.pointer-events-none.absolute 0.0x0.0 bg #fbfbf8 @ 0.12 r 4px; span.pointer-events-none.absolute 0.0x0.0 bg #fbfbf8 @ 0.12 r 4px |
| Ancestor paint | 1 up body.min-h-full.flex bg #f5f5f2 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger (aria-label="Open menu", 41x41 rounded-8); its own press opens the menu.

Page: home. Selector: `button[aria-label="Open menu"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 41 x 41 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Transition | none |
| Cursor | default |
| Painted layers | span.pointer-events-none.absolute 41.0x41.0 image linear-gradient(#ffffff @ 0.16 0%, #ffffff @ 0.08 100%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px shadow #000000 @ 0.12 0px -1px 0px 0px inset, #000000 @ 0.1 0px -1px 2px 0px inset, #ffffff @ 0.24 0px 1px 1px 0px inset; span.pointer-events-none.absolute 41.0x41.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset; span.absolute.block 18.0x1.5 bg #fbfbf8 r 3.35544e+07px; span.absolute.block 18.0x1.5 bg #fbfbf8 r 3.35544e+07px; span.absolute.block 18.0x1.5 bg #fbfbf8 r 3.35544e+07px |
| Ancestor paint | 3 up header.site-header.fixed shadow #ffffff @ 0 0px 1px 0px 0px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The full-screen menu overlay after the hamburger press.

Page: home. Selector: `opened mobile menu overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #f5f5f2 |
| Box shadow | none |
| Outline | none |
| Font | neoris 16px/24px 400 |
| Letter spacing | normal |
| Colour | #171717 |
| Text node | span.text-[24px].[@media(max-height:600px)]:text-[15px]: neoris 24px/36px 410, #bfbfbf, ls -0.3px |
| Transition | none |
| Icon | 15 x 15, colour #171717 |
| Painted layers | div.fixed.inset-0 390.0x844.0 bg #f5f5f2; div.w-25.h-px 100.0x1.0 bg #ffffff border T:1px solid #e8e7e6; a.group.relative 36.0x36.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset; a.group.relative 36.0x36.0 bg #f5f5f2 border T:1px solid #202020 @ 0.1 / R:1px solid #202020 @ 0.1 / B:1px solid #202020 @ 0.1 / L:1px solid #202020 @ 0.1 r 8px shadow #000000 @ 0.06 0px 2px 3px 0px, #ffffff @ 0.35 0px 0px 0.357px 1.5px inset, #ffffff 0px 2px 0px 0px inset |
| Ancestor paint | 1 up body.min-h-full.flex bg #f5f5f2 |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link row inside the open mobile menu.

Page: home. Selector: `first link inside the open menu`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 83.52 x 64 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | neoris 40px/64px 400 | = | = | = |
| Letter spacing | -0.3px | = | = | = |
| Colour | #262323 @ 0.8 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.text-[40px].[@media(max-height:600px)]:text-[24px] 83.5x64.0 outline 1px auto #e59700 offset 1px | = |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline. The hero headline at 390.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 350 x 112.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | linear-gradient(#ffffff 0%, #ffffff @ 0.9 100%) |
| Box shadow | none |
| Outline | none |
| Font | neoris 34px/37.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | h1.m-0.font-normal 350.0x112.2 image linear-gradient(#ffffff 0%, #ffffff @ 0.9 100%) |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `color 0.2s, font-weight 0.2s`, `background-color 0.14s ease-out, box-shadow 0.14s ease-out`, `background-color 0.2s ease-out`, `color 0.2s ease-out`, `opacity 0.2s ease-out`, `background-color 0.2s ease-out, box-shadow 0.2s ease-out`, `background 0.14s ease-out, box-shadow 0.14s ease-out`, `none`, `opacity 0.3s`, `opacity 0.25s`, `opacity 0.2s`, `transform 0.24s cubic-bezier(0.215, 0.61, 0.355, 1)`
