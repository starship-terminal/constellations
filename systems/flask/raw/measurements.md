# Flask component measurements

Computed styles read from flask.do on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted dark surfaces — the marketing pages (home, pricing, video-collaboration, frame-io-alternative), the /mcp documentation, /about, /security, the sign-in edge at /login and the 390px mobile pass — and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). Every public page paints the dark `default` theme, the only --ds-* layer the bundle declares; no light variant or theme toggle exists. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### mkt-header

Site header. The sticky top bar on every page (a div, not <header>): the Flask mark, the Pricing/Features nav links and the "Sign Up" CTA (which links to /home — the login boundary).

Page: home. Selector: `div.top-0.z-50`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | a.flex.items-center: ui-sans-serif 13px/19.5px 400, #a0a0a0 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Icon | 48 x 16, colour #fafafa, fill #000000 |
| Painted layers | button.md:hidden.flex 0.0x0.0 outline 2px solid #000000 @ 0 offset 2px; a.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; a::before.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5156pxx32px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px |
| Ancestor paint | 1 up div.min-h-screen.text-fg-1 bg #0c0c0c |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Flask mark (aria-label="Flask") in the top bar, linking home.

Page: home. Selector: `a[aria-label=Flask]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 64 x 32 |
| Padding | 0px 8px |
| Border | none |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | transform 0.15s cubic-bezier(0.23, 1, 0.32, 1) |
| Cursor | pointer |
| Icon | 48 x 16, colour #fafafa, fill #000000 |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-pricing

Nav link. The "Pricing" header link; measured, never followed.

Page: home. Selector: `header a Pricing`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.22 x 32 | = | = | 56.47 x 31.04 |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #fafafa @ 0.035 | = | #fafafa @ 0.035 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a0a0a0 | #fafafa | = | #fafafa |
| Transition | transform 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.items-center 58.2x32.0 bg #fafafa @ 0.035 r 12px | = | a.flex.items-center 56.5x31.0 bg #fafafa @ 0.035 r 12px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `nav-pricing-default.png`, `nav-pricing-hover.png`, `nav-pricing-focus-visible.png`, `nav-pricing-pressed.png`.

#### nav-features

Features nav link. The "Features" header link; measured, never followed. The header offers no Log in link — /login is reached through Sign Up.

Page: home. Selector: `header a Features`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.78 x 32 | = | = | 66.72 x 31.04 |
| Padding | 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | #fafafa @ 0.035 | = | #fafafa @ 0.035 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 13px/19.5px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a0a0a0 | #fafafa | = | #fafafa |
| Transition | transform 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.flex.items-center 68.8x32.0 bg #fafafa @ 0.035 r 12px | = | a.flex.items-center 66.7x31.0 bg #fafafa @ 0.035 r 12px |
| Transform | - | = | = | matrix(0.97, 0, 0, 0.97, 0, 0) |

Crops: `nav-features-default.png`, `nav-features-hover.png`, `nav-features-focus-visible.png`, `nav-features-pressed.png`.

#### nav-cta

Header CTA. The "Sign Up" CTA in the top bar — it links to /home, which redirects to /login; measured, never followed.

Page: home. Selector: `nav "Sign Up" link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.52 x 32 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #a0a0a0 @ 0.063 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.7 | #fafafa @ 0.95 | = | #fafafa @ 0.95 |
| Text node | span.[grid-area:1/1]: ui-sans-serif 13px/19.5px 500, #fafafa @ 0.7 | span.[grid-area:1/1]: ui-sans-serif 13px/19.5px 500, #fafafa @ 0.95 | = | span.[grid-area:1/1]: ui-sans-serif 13px/19.5px 500, #fafafa @ 0.95 |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #fafafa @ 0.7 | 14 x 14, colour #fafafa @ 0.95 | = | 14 x 14, colour #fafafa @ 0.95 |
| ::before | 81.5156px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 81.5156px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 49.9973% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 81.5156px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 49.9973% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 81.5156px x 32px, absolute, bg #000000 @ 0 radial-gradient(220px at 49.9973% 50%, #fafafa @ 0.1, #000000 @ 0 100%), radius 9999px |
| Painted layers | a.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; a::before.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5156pxx32px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | a.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; a::before.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5156pxx32px image radial-gradient(90px at 49.9973% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | a.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; a::before.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5156pxx32px image radial-gradient(90px at 49.9973% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | a.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; a::before.ds-focus:ring-2.ds-focus:ring-focus-ring 81.5156pxx32px image radial-gradient(220px at 49.9973% 50%, #fafafa @ 0.1, #000000 @ 0 100%) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home and landing pages

#### hero-h1

Hero headline. "The world's fastest way to review video." — the flask.do hero display heading.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 138.22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 64px/69.12px 500 |
| Letter spacing | -1.6px |
| Colour | #fafafa |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The hero's "Open Flask" pill — the primary call to action; measured, never followed.

Page: home. Selector: `hero "Open Flask" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.84 x 40 | = | = | = |
| Padding | 0px 12px 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to top, #adadad 20%, #cacaca 80%) | = | = | = |
| Box shadow | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px | #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 15px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #090909 | #242424 | = | #242424 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #090909 | 16 x 16, colour #242424 | = | 16 x 16, colour #242424 |
| ::before | 125.844px x 38px, absolute, bg #000000 @ 0 radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% 40% at 72% 108%, #f78264 @ 0., radius 9999px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset | = | = | = |
| ::after | 125.844px x 38px, absolute, bg #000000 @ 0 linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4), radius 9999px | = | = | = |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 127.8x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 127.8x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 127.8x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 127.8x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-copy-prompt

Hero "Copy Prompt" button. The hero's secondary "Copy Prompt" pill; measured, never pressed.

Page: home. Selector: `hero "Copy Prompt" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145.75 x 40 | = | = | = |
| Padding | 0px 14px 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #121212 | = | = | = |
| Background image | linear-gradient(#a0a0a0 @ 0.063, #a0a0a0 @ 0.063), none | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 15px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.7 | #fafafa @ 0.95 | = | #fafafa @ 0.95 |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #fafafa @ 0.7 | 16 x 16, colour #fafafa @ 0.95 | = | 16 x 16, colour #fafafa @ 0.95 |
| ::before | 145.75px x 40px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 145.75px x 40px, absolute, bg #000000 @ 0 radial-gradient(90px at 49.9987% 49.9766%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 145.75px x 40px, absolute, bg #000000 @ 0 radial-gradient(90px at 49.9987% 49.9766%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 145.75px x 40px, absolute, bg #000000 @ 0 radial-gradient(220px at 49.9987% 49.9766%, #fafafa @ 0.1, #000000 @ 0 100%), radius 9999px |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 145.8x40.0 bg #121212 image linear-gradient(#a0a0a0 @ 0.063, #a0a0a0 @ 0.063), none r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 145.75pxx40px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 145.8x40.0 bg #121212 image linear-gradient(#a0a0a0 @ 0.063, #a0a0a0 @ 0.063), none r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 145.75pxx40px image radial-gradient(90px at 49.9987% 49.9766%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 145.8x40.0 bg #121212 image linear-gradient(#a0a0a0 @ 0.063, #a0a0a0 @ 0.063), none r 9999px shadow #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 145.75pxx40px image radial-gradient(90px at 49.9987% 49.9766%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 145.8x40.0 bg #121212 image linear-gradient(#a0a0a0 @ 0.063, #a0a0a0 @ 0.063), none r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 145.75pxx40px image radial-gradient(220px at 49.9987% 49.9766%, #fafafa @ 0.1, #000000 @ 0 100%) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `hero-copy-prompt-default.png`, `hero-copy-prompt-hover.png`, `hero-copy-prompt-focus-visible.png`, `hero-copy-prompt-pressed.png`.

#### section-h2

Section heading. A marketing section heading further down the home page ("Talk, Draw, Show", "Share, Organize and Compare", …).

Page: home. Selector: `main h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 900 x 48.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 44px/48.4px 500 |
| Letter spacing | -1.1px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### cta-book-demo

Book a Demo CTA. A "Book a Demo" CTA in the marketing page body; measured, never followed.

Page: home. Selector: `main "Book a Demo" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 110.03 x 32 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #a0a0a0 @ 0.063 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px | #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 13px/19.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.7 | #fafafa @ 0.95 | = | #fafafa @ 0.95 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 110.031px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset | 110.031px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 49.996% 49.9961%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset | 110.031px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 49.996% 49.9961%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset | 110.031px x 32px, absolute, bg #000000 @ 0 radial-gradient(190.547px at 49.996% 49.9961%, #fafafa @ 0.094, #000000 @ 0 100%), radius 9999px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset |
| ::after | 110.031px x 32px, absolute, bg #000000 @ 0 linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4), radius 9999px | = | = | = |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 110.0x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 110.031pxx32px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 110.031pxx32px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 110.0x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 110.031pxx32px image radial-gradient(90px at 49.996% 49.9961%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 110.031pxx32px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 110.0x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 110.031pxx32px image radial-gradient(90px at 49.996% 49.9961%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 110.031pxx32px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 110.0x32.0 bg #a0a0a0 @ 0.063 r 9999px shadow #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 110.031pxx32px image radial-gradient(190.547px at 49.996% 49.9961%, #fafafa @ 0.094, #000000 @ 0 100%) r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 110.031pxx32px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `cta-book-demo-default.png`, `cta-book-demo-hover.png`, `cta-book-demo-focus-visible.png`, `cta-book-demo-pressed.png`.

#### seo-h1

SEO page headline. The /video-collaboration landing-page masthead — one of the SEO/landing surfaces sharing the marketing shell.

Page: video-collaboration. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 105.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 48px/52.8px 500 |
| Letter spacing | -1.2px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `seo-h1-default.png`.

#### seo-cta

SEO page CTA. The landing page's CTA; measured, never followed.

Page: video-collaboration. Selector: `seo page CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.77 x 46 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to top, #adadad 20%, #cacaca 80%) | = | = | = |
| Box shadow | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px | = | #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #090909 | #242424 | = | #242424 |
| Transition | color, box-shadow, transform 0.28s, 0.28s, 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 136.766px x 44px, absolute, bg #000000 @ 0 radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% 40% at 72% 108%, #f78264 @ 0., radius 12px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset | = | = | = |
| ::after | 136.766px x 44px, absolute, bg #000000 @ 0 linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4), radius 12px | = | = | = |
| Painted layers | a.button-primary.inline-flex 138.8x46.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px; a::before.button-primary.inline-flex 136.766pxx44px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 12px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; a::after.button-primary.inline-flex 136.766pxx44px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 12px | a.button-primary.inline-flex 138.8x46.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px; a::before.button-primary.inline-flex 136.766pxx44px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 12px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; a::after.button-primary.inline-flex 136.766pxx44px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 12px | = | a.button-primary.inline-flex 138.8x46.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 12px shadow #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px; a::before.button-primary.inline-flex 136.766pxx44px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 12px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; a::after.button-primary.inline-flex 136.766pxx44px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `seo-cta-default.png`, `seo-cta-hover.png`, `seo-cta-focus-visible.png`, `seo-cta-pressed.png`.

#### seo2-h1

Alternative page headline. The /frame-io-alternative landing-page masthead.

Page: frame-io-alternative. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 960 x 105.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 48px/52.8px 500 |
| Letter spacing | -1.2px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `seo2-h1-default.png`.

### Marketing demo (pre-rendered product UI)

#### demo-breadcrumb

Demo breadcrumb chip. The demo mock's "ACME Studios" breadcrumb chip in the workspace bar; measured as painted.

Page: home. Selector: `demo "ACME Studios" breadcrumb`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.87 x 16.61 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | ui-sans-serif 14px/17.5px 400 | = | - | = |
| Letter spacing | -0.35px | = | - | = |
| Colour | #a0a0a0 | = | - | = |
| Transition | none | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `demo-breadcrumb-default.png`, `demo-breadcrumb-hover.png`, `demo-breadcrumb-pressed.png`.

#### demo-tab-context

Demo context tab. The demo's "v2 / Context" tab, painted as the active tab; measured as painted.

Page: home. Selector: `demo "v2 Context" tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.97 x 30.38 | = | - | 71.31 x 30.38 |
| Padding | 0px 12px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | #a0a0a0 @ 0.063 | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | = | - | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | = | - | = |
| Font | ui-sans-serif 14px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #868686 | = | - | #fafafa @ 0.95 |
| Text node | span.flex.items-baseline: ui-monospace 12px/12px 500, #a0a0a0 | = | - | - |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | - | = |
| Opacity | 0.5 | = | - | - |
| Cursor | default | = | - | = |
| ::before | 109.516px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | = | - | 75.1094px x 32px, absolute, bg #000000 @ 0 radial-gradient(212.295px at 50% 50%, #fafafa @ 0.098, #000000 @ 0 100%), radius 9999px |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 104.0x30.4 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 109.516pxx32px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px; span.flex.items-center 27.0x19.0 border T:1px solid #333333 / R:1px solid #333333 / B:1px solid #333333 / L:1px solid #333333 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.55 0px 1px 3px 0px | = | - | button.ds-focus:ring-2.ds-focus:ring-focus-ring 71.3x30.4 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 75.1094pxx32px image radial-gradient(212.295px at 50% 50%, #fafafa @ 0.098, #000000 @ 0 100%) r 9999px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `demo-tab-context-default.png`, `demo-tab-context-hover.png`, `demo-tab-context-pressed.png`.

#### demo-tab-feedback

Demo feedback tab. The demo's "Feedback / 0" tab, painted as inactive; measured as painted.

Page: home. Selector: `demo "Feedback 0" tab`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.96 x 30.38 | = | - | = |
| Padding | 0px 12px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | #a0a0a0 @ 0.063 | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | = | - | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | = | - | = |
| Font | ui-sans-serif 14px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #868686 | = | - | #fafafa @ 0.95 |
| Text node | span.inline-flex.items-center: ui-sans-serif 14px/20px 500, #868686 | = | - | span.inline-flex.items-center: ui-sans-serif 14px/20px 500, #fafafa @ 0.95 |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | - | = |
| Cursor | default | = | - | = |
| ::before | 86.3281px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | = | - | 86.3281px x 32px, absolute, bg #000000 @ 0 radial-gradient(219.862px at 50% 50%, #fafafa @ 0.1, #000000 @ 0 100%), radius 9999px |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 82.0x30.4 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 86.3281pxx32px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | = | - | button.ds-focus:ring-2.ds-focus:ring-focus-ring 82.0x30.4 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 86.3281pxx32px image radial-gradient(219.862px at 50% 50%, #fafafa @ 0.1, #000000 @ 0 100%) r 9999px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `demo-tab-feedback-default.png`, `demo-tab-feedback-hover.png`, `demo-tab-feedback-pressed.png`.

#### demo-feedback-field

Demo feedback composer. The demo's "00:00 / Leave Feedback.." composer field, painted with a timestamp chip; measured as painted.

Page: home. Selector: `demo "Leave Feedback" composer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 154.5 x 44.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 14px/20px 400 |
| Letter spacing | normal |
| Colour | #6f6f6f |
| Transition | opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| Ancestor paint | 2 up div.relative.h-full bg #121212 shadow #000000 @ 0.3 0px -1px 0px 0px inset, #000000 @ 0.55 0px 1px 2px 0px, #000000 @ 0.55 0px 14px 32px -10px, #000000 @ 0.85 0px 56px 110px -30px |
| How | at rest |

Crops: `demo-feedback-field-default.png`.

#### demo-version-chip

Demo version chip. The demo's "Version 3" chip — the mock asset switcher; measured as painted, toggled once during screenshot capture.

Page: home. Selector: `demo "Version 3" chip`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.9 x 30.38 | - | - | = |
| Padding | 0px 6px 0px 12px | - | - | = |
| Gap | 4px | - | - | = |
| Border | none | - | - | = |
| Radius | 9999px | - | - | = |
| Background | #a0a0a0 @ 0.063 | - | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | - | - | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | - | - | = |
| Font | ui-sans-serif 14px/20px 500 | - | - | = |
| Letter spacing | normal | - | - | = |
| Colour | #fafafa @ 0.7 | - | - | #fafafa @ 0.95 |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | - | - | = |
| Cursor | default | - | - | = |
| Icon | 15.19 x 15.19, colour #a0a0a0 | - | - | = |
| ::before | 98.9062px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | - | - | 98.9062px x 32px, absolute, bg #000000 @ 0 radial-gradient(220px at 50% 50%, #fafafa @ 0.1, #000000 @ 0 100%), radius 9999px |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 93.9x30.4 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 98.9062pxx32px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | - | - | button.ds-focus:ring-2.ds-focus:ring-focus-ring 93.9x30.4 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 98.9062pxx32px image radial-gradient(220px at 50% 50%, #fafafa @ 0.1, #000000 @ 0 100%) r 9999px |
| How | at rest | - | - | CDP forcePseudoState :active:hover |
| Error | - | locator.hover: Element is outside of the viewport Call log:   - waiting for locator('[data-m-mark="dvc"]').first().first()     - locator resolved to <button tabindex="-1" data-size="md" data-m-mark="d | = | = |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `demo-version-chip-default.png`, `demo-version-chip-pressed.png`.

#### demo-copy-link

Demo "Copy Link" button. The demo's "Copy Link to Folder" / "Copy Link" control; measured, never pressed.

Page: home. Selector: `demo "Copy Link" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 103.97 x 30.38 | = | - | = |
| Padding | 0px 12px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 20px 4px 4px 20px | = | - | = |
| Background | #a0a0a0 @ 0.063 | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | = | - | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | = | - | = |
| Font | ui-sans-serif 14px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #fafafa @ 0.7 | = | - | #fafafa @ 0.95 |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 15.19 x 15.19, colour #fafafa @ 0.7 | = | - | 15.19 x 15.19, colour #fafafa @ 0.95 |
| ::before | 109.516px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 20px 4px 4px 20px | = | - | 109.516px x 32px, absolute, bg #000000 @ 0 radial-gradient(212.295px at 50% 50%, #fafafa @ 0.098, #000000 @ 0 100%), radius 20px 4px 4px 20px |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 104.0x30.4 bg #a0a0a0 @ 0.063 r 20px 4px 4px 20px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 109.516pxx32px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 20px 4px 4px 20px | = | - | button.ds-focus:ring-2.ds-focus:ring-focus-ring 104.0x30.4 bg #a0a0a0 @ 0.063 r 20px 4px 4px 20px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 109.516pxx32px image radial-gradient(212.295px at 50% 50%, #fafafa @ 0.098, #000000 @ 0 100%) r 20px 4px 4px 20px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `demo-copy-link-default.png`, `demo-copy-link-hover.png`, `demo-copy-link-pressed.png`.

#### demo-th

Demo table header. The demo file list's "Latest Activity" column header; measured as painted.

Page: home. Selector: `demo "Latest Activity" header`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 137.95 x 38.45 | - |
| Padding | 0px 12px | - |
| Gap | 6px | - |
| Border | none | - |
| Radius | 9999px | - |
| Background | #a0a0a0 @ 0.063 | - |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | - |
| Outline | none | - |
| Font | ui-sans-serif 14px/20px 500 | - |
| Letter spacing | normal | - |
| Colour | #fafafa @ 0.7 | - |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | - |
| Cursor | default | - |
| ::before | 114.797px x 32px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | - |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 137.9x38.5 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 114.797pxx32px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | - |
| How | at rest | - |
| Error | - | locator.hover: Element is outside of the viewport Call log:   - waiting for locator('[data-m-mark="dth"]').first().first()     - locator resolved to <button tabindex="-1" data-size="md" data-m-mark="d |

Crops: `demo-th-default.png`.

#### demo-acme-btn

Demo "ACME Studios" share button. The "ACME Studios" button in the demo's rendered share popover ("Who can edit"); measured, never pressed.

Page: home. Selector: `demo share "ACME Studios" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 166.99 x 33.65 | = | - | = |
| Padding | 0px 10px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | #a0a0a0 @ 0.063 | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | = | - | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | = | - | = |
| Font | ui-sans-serif 13px/19.5px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #fafafa @ 0.7 | = | - | #fafafa @ 0.95 |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 8.41 x 8.41, colour #a0a0a0, fill #000000 | = | - | = |
| ::before | 138.969px x 28px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | = | - | 138.969px x 28px, absolute, bg #000000 @ 0 radial-gradient(182.096px at 50% 50%, #fafafa @ 0.13, #000000 @ 0 100%), radius 9999px |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 167.0x33.6 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 138.969pxx28px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | = | - | button.ds-focus:ring-2.ds-focus:ring-focus-ring 167.0x33.6 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 138.969pxx28px image radial-gradient(182.096px at 50% 50%, #fafafa @ 0.13, #000000 @ 0 100%) r 9999px |
| Ancestor paint | 2 up div.rounded-2xl.element-border bg #1f1f1f shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 2px 8px -2px, #000000 @ 0.5 0px 16px 40px -8px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `demo-acme-btn-default.png`, `demo-acme-btn-hover.png`, `demo-acme-btn-pressed.png`.

#### demo-share-scope

Demo share-scope control. The demo's "Anyone with Link" share-scope control; measured as painted, never opened (an earlier pointer attempt was intercepted by the mock overlay).

Page: home. Selector: `demo "Anyone with Link" control`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 191.55 x 33.65 | = | - |
| Padding | 0px 10px | = | - |
| Gap | 6px | = | - |
| Border | none | = | - |
| Radius | 9999px | = | - |
| Background | #a0a0a0 @ 0.063 | = | - |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | = | - |
| Outline | none | = | - |
| Font | ui-sans-serif 13px/19.5px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #fafafa @ 0.7 | = | - |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | - |
| Cursor | pointer | = | - |
| Icon | 19.23 x 19.23, colour #a0a0a0 | = | - |
| ::before | 159.406px x 28px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | = | - |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 191.5x33.6 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 159.406pxx28px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | = | - |
| Ancestor paint | 2 up div.rounded-2xl.element-border bg #1f1f1f shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 2px 8px -2px, #000000 @ 0.5 0px 16px 40px -8px | = | - |
| How | at rest | mouse hover | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element |

Crops: `demo-share-scope-default.png`, `demo-share-scope-hover.png`.

#### demo-share-popover

Demo share popover. The demo mock's painted share popover (bg-surface-3, element-border, shadow-popover): "Who can view / Anyone with Link / Who can edit" — a painted mock state, measured as painted.

Page: home. Selector: `demo share popover`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 406.16 x 57.68 |
| Padding | 10px 10px 10px 20px |
| Gap | 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | span.text-[13px].leading-5: ui-sans-serif 13px/20px 400, #fafafa |
| Transition | none |
| Icon | 19.23 x 19.23, colour #a0a0a0 |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 191.5x33.6 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 159.406pxx28px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px |
| Ancestor paint | 1 up div.rounded-2xl.element-border bg #1f1f1f shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 2px 8px -2px, #000000 @ 0.5 0px 16px 40px -8px |
| How | at rest |

Crops: `demo-share-popover-default.png`.

#### demo-close

Demo "Close" button. A "Close" button in the demo mock's dialog surface; measured, never pressed.

Page: home. Selector: `demo "Close" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 62.09 x 22.71 | = | - | = |
| Padding | 0px 10px | = | - | = |
| Gap | 6px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | #121212 | = | - | = |
| Background image | linear-gradient(#a0a0a0 @ 0.063, #a0a0a0 @ 0.063), none | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | = | - | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | = | - | = |
| Font | ui-sans-serif 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #fafafa @ 0.7 | = | - | #fafafa @ 0.95 |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 12.17 x 12.17, colour #fafafa @ 0.7 | = | - | 12.17 x 12.17, colour #fafafa @ 0.95 |
| ::before | 76.5469px x 28px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | = | - | 76.5469px x 28px, absolute, bg #000000 @ 0 radial-gradient(182.088px at 50% 50%, #fafafa @ 0.13, #000000 @ 0 100%), radius 9999px |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 62.1x22.7 bg #121212 image linear-gradient(#a0a0a0 @ 0.063, #a0a0a0 @ 0.063), none r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 76.5469pxx28px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | = | - | button.ds-focus:ring-2.ds-focus:ring-focus-ring 62.1x22.7 bg #121212 image linear-gradient(#a0a0a0 @ 0.063, #a0a0a0 @ 0.063), none r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 76.5469pxx28px image radial-gradient(182.088px at 50% 50%, #fafafa @ 0.13, #000000 @ 0 100%) r 9999px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `demo-close-default.png`, `demo-close-hover.png`, `demo-close-pressed.png`.

### Pricing

#### price-h1

Pricing headline. "Pricing" — the /pricing masthead.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 896 x 46 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 40px/46px 500 |
| Letter spacing | -1px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `price-h1-default.png`.

#### billing-switch

Billing switch. The plan billing switch beside the plan cards — labelled "Billed yearly" when on ($15/member/mo) and "Billed quarterly" when off ($35/member/mo); the off state was measured after toggling it — a local UI toggle — then toggled back.

Page: pricing. Selector: `[role=switch] billing`. States: default, hover, focus-visible, pressed, off.

| Property | default | hover | focus-visible | pressed | off |
|---|---|---|---|---|---|
| Size (w x h) | 36 x 20 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = | = |
| Radius | 9999px | = | = | = | = |
| Background | #fafafa | = | = | = | #fafafa @ 0.086 |
| Box shadow | none | = | #0c0c0c 0px 0px 0px 2px, #adadad 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | none | = | = | = | = |
| Font | ui-sans-serif 14px/20px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #a0a0a0 | = | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Painted layers | button.peer.inline-flex 36.0x20.0 bg #fafafa border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px; span.pointer-events-none.block 16.0x16.0 bg #0c0c0c r 9999px shadow #ffffff 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 1px 2px 0px | = | button.peer.inline-flex 36.0x20.0 bg #fafafa border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px shadow #0c0c0c 0px 0px 0px 2px, #adadad 0px 0px 0px 4px, #000000 @ 0 0px 0px 0px 0px; span.pointer-events-none.block 16.0x16.0 bg #0c0c0c r 9999px shadow #ffffff 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 1px 2px 0px | = | button.peer.inline-flex 36.0x20.0 bg #fafafa @ 0.086 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 9999px; span.pointer-events-none.block 16.0x16.0 bg #a0a0a0 r 9999px shadow #ffffff 0px 0px 0px 0px, #3b82f6 @ 0.5 0px 0px 0px 0px, #000000 @ 0 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle (aria-checked true→false) |

Crops: `billing-switch-default.png`, `billing-switch-hover.png`, `billing-switch-focus-visible.png`, `billing-switch-pressed.png`, `billing-switch-off.png`.

#### plan-cta

Get Started button. A plan card's "Get Started" button; measured, never followed (it would start a sign-up flow).

Page: pricing. Selector: `"Get Started" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 248 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to top, #adadad 20%, #cacaca 80%) | = | = | = |
| Box shadow | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px | = | #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #090909 | #242424 | = | #242424 |
| Transition | color, box-shadow, transform 0.28s, 0.28s, 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 246px x 38px, absolute, bg #000000 @ 0 radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% 40% at 72% 108%, #f78264 @ 0., radius 9999px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset | = | = | = |
| ::after | 246px x 38px, absolute, bg #000000 @ 0 linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4), radius 9999px | = | = | = |
| Painted layers | button.h-10.w-full 248.0x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px; button::before.h-10.w-full 246pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.h-10.w-full 246pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.h-10.w-full 248.0x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px; button::before.h-10.w-full 246pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.h-10.w-full 246pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | = | button.h-10.w-full 248.0x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px; button::before.h-10.w-full 246pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.h-10.w-full 246pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### book-call

Book Call button. A plan card's "Book Call" button; measured, never followed (external scheduler).

Page: pricing. Selector: `"Book Call" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 248 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #a0a0a0 @ 0.063 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | = | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa @ 0.7 | #fafafa @ 0.95 | = | #fafafa @ 0.95 |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 248px x 40px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 248px x 40px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 49.9828%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 248px x 40px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 49.9828%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | 248px x 40px, absolute, bg #000000 @ 0 radial-gradient(217.53px at 50% 49.9828%, #fafafa @ 0.1, #000000 @ 0 100%), radius 9999px |
| Painted layers | button.h-10.w-full 248.0x40.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.h-10.w-full 248pxx40px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | button.h-10.w-full 248.0x40.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.h-10.w-full 248pxx40px image radial-gradient(90px at 50% 49.9828%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | button.h-10.w-full 248.0x40.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.h-10.w-full 248pxx40px image radial-gradient(90px at 50% 49.9828%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | button.h-10.w-full 248.0x40.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.16 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 1px 0px; button::before.h-10.w-full 248pxx40px image radial-gradient(217.53px at 50% 49.9828%, #fafafa @ 0.1, #000000 @ 0 100%) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `book-call-default.png`, `book-call-hover.png`, `book-call-focus-visible.png`, `book-call-pressed.png`.

#### faq-acc

FAQ accordion. A question row in the /pricing FAQs accordion ("What is the storage limit and what are download windows?"); the opened state was measured after its own toggle — aria-expanded had to stay true.

Page: pricing. Selector: `pricing FAQ button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 896 x 62.5 | = | = | = | = |
| Padding | 20px 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | ui-sans-serif 15px/22.5px 500 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #fafafa | = | = | = | = |
| Transition | all 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 16 x 16, colour #fafafa | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `faq-acc-default.png`, `faq-acc-hover.png`, `faq-acc-focus-visible.png`, `faq-acc-pressed.png`, `faq-acc-opened.png`.

### Docs and about

#### docs-h1

Docs headline. "Flask MCP Server" — the /mcp documentation masthead.

Page: mcp. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 848 x 36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 30px/36px 700 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-code

Code block. A command/code block in the MCP docs (install and tool snippets); measured as painted, never run.

Page: mcp. Selector: `docs code block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 172.83 x 18 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-monospace 16px/24px 400 |
| Letter spacing | normal |
| Colour | #a0a0a0 |
| Transition | none |
| How | at rest |

Crops: `docs-code-default.png`.

#### docs-cursor

Add to Cursor link. The "Add to Cursor" MCP-install link; an external install URL, measured, never followed.

Page: mcp. Selector: `"Add to Cursor" link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 104.25 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-cursor-default.png`, `docs-cursor-hover.png`, `docs-cursor-focus-visible.png`, `docs-cursor-pressed.png`.

#### docs-anchor

Docs anchor link. An in-page anchor link in the MCP docs; measured, never followed.

Page: mcp. Selector: `docs anchor link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 71.48 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #a0a0a0 | #fafafa | = | #fafafa |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-anchor-default.png`, `docs-anchor-hover.png`, `docs-anchor-focus-visible.png`, `docs-anchor-pressed.png`.

#### about-h1

About headline. "About" — the /about masthead.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 688 x 46 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 40px/46px 500 |
| Letter spacing | -1px |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `about-h1-default.png`.

#### about-link

About link. An external/social link on /about (YouTube show, DMs, hello@flask.do); measured, never followed.

Page: about. Selector: `about link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 118 x 33 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Caveat 26px/39px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #fafafa | #a0a0a0 | = | #a0a0a0 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `about-link-default.png`, `about-link-hover.png`, `about-link-focus-visible.png`, `about-link-pressed.png`.

### Security and legal

#### sec-h1

Security headline. "Security" — the /security masthead ("Security: How Flask Protects Your Data").

Page: security. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 848 x 45 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 36px/45px 700 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | none |
| How | at rest |

Crops: `sec-h1-default.png`.

### Login (signed-out)

#### login-panel

Login panel. The sign-in card on /login: "Sign in to Flask" with Continue with Google and Continue with Email plus the e-mail field. Nothing was submitted.

Page: login. Selector: `login panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 288 x 318 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | p.text-sm.text-fg-2: ui-sans-serif 14px/20px 400, #a0a0a0 |
| Transition | none |
| Icon | 72 x 24, colour #fafafa, fill #000000 |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 288.0x44.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px; span.h-px.flex-1 111.6x1.0 bg #282828; span.h-px.flex-1 111.6x1.0 bg #282828; input.w-full.rounded-full 288.0x44.0 bg #fafafa @ 0.047 border T:1px solid #282828 / R:1px solid #282828 / B:1px solid #282828 / L:1px solid #282828 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `login-panel-default.png`.

#### login-google

Google SSO button. The "Continue with Google" button; measured, never pressed (it would leave for Google SSO).

Page: login. Selector: `login "Continue with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 288 x 44 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to top, #adadad 20%, #cacaca 80%) | = | = | = |
| Box shadow | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px | #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #090909 | #242424 | = | #242424 |
| Transition | color, box-shadow, transform 0.28s, 0.28s, 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #090909 | 16 x 16, colour #242424 | = | 16 x 16, colour #242424 |
| ::before | 286px x 42px, absolute, bg #000000 @ 0 radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% 40% at 72% 108%, #f78264 @ 0., radius 9999px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset | = | = | = |
| ::after | 286px x 42px, absolute, bg #000000 @ 0 linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4), radius 9999px | = | = | = |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 288.0x44.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 288.0x44.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 288.0x44.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 288.0x44.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 286pxx42px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-email-btn

Continue with Email button. The "Continue with Email" submit button; its states were measured but the button was never clicked — nothing was submitted.

Page: login. Selector: `login "Continue with Email"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 288 x 44 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 8px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | #a0a0a0 @ 0.063 | = | - | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px | = | - | = |
| Outline | none | = | - | = |
| Font | ui-sans-serif 14px/20px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #fafafa @ 0.7 | = | - | = |
| Transition | color, transform, opacity, box-shadow 0.15s cubic-bezier(0.23, 1, 0.32, 1) | = | - | = |
| Opacity | 0.5 | = | - | = |
| Cursor | default | = | - | = |
| Icon | 16 x 16, colour #fafafa @ 0.7 | = | - | = |
| ::before | 288px x 44px, absolute, bg #000000 @ 0 radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%), radius 9999px | = | - | = |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 288.0x44.0 bg #a0a0a0 @ 0.063 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #adadad @ 0.07 0px 0.5px 0px 0px inset, #6f6f6f @ 0.255 0px 0px 0px 0.5px inset, #000000 @ 0.18 0px 1px 2px 0px, #000000 @ 0.18 0px 2px 6px -2px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 288pxx44px image radial-gradient(90px at 50% 50%, #fafafa @ 0.06, #000000 @ 0 100%) r 9999px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `login-email-btn-default.png`, `login-email-btn-hover.png`, `login-email-btn-pressed.png`.

#### login-email

Email field (login). The e-mail input on the sign-in card (placeholder "han@solo.com"); focused and typed into then cleared — never submitted.

Page: login. Selector: `login email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 288 x 44 | = | = |
| Padding | 0px 16px | = | = |
| Border | 1px solid #282828 | 1px solid #505050 | 1px solid #505050 |
| Radius | 9999px | = | = |
| Background | #fafafa @ 0.047 | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | none | none |
| Font | ui-sans-serif 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #fafafa | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #505050, opacity 1 | = | = |
| Painted layers | input.w-full.rounded-full 288.0x44.0 bg #fafafa @ 0.047 border T:1px solid #282828 / R:1px solid #282828 / B:1px solid #282828 / L:1px solid #282828 r 9999px outline 2px solid #000000 @ 0 offset 2px | input.w-full.rounded-full 288.0x44.0 bg #fafafa @ 0.047 border T:1px solid #505050 / R:1px solid #505050 / B:1px solid #505050 / L:1px solid #505050 r 9999px | input.w-full.rounded-full 288.0x44.0 bg #fafafa @ 0.047 border T:1px solid #505050 / R:1px solid #505050 / B:1px solid #505050 / L:1px solid #505050 r 9999px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

### Mobile (390 wide)

#### m-topbar

Mobile top chrome. The phone top chrome at 390 wide: the Flask logo link plus the hamburger — the page mounts no <header> element at this width.

Page: mobile. Selector: `mobile logo link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 64 x 32 |
| Padding | 0px 8px |
| Border | none |
| Radius | 12px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Transition | transform 0.15s cubic-bezier(0.23, 1, 0.32, 1) |
| Cursor | pointer |
| Icon | 48 x 16, colour #fafafa, fill #000000 |
| How | at rest |

Crops: `m-topbar-default.png`.

#### m-menu-btn

Mobile menu button. The icon-only "Open menu" hamburger (md:hidden — mobile only) — a local UI toggle; the opened state was measured after activating it.

Page: mobile. Selector: `button[aria-label=Open menu]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 38 x 38 | = | = | = | = |
| Padding | 8px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | none | = | = |
| Font | ui-sans-serif 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #a0a0a0 | = | = | = | = |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 22 x 22, colour #a0a0a0 | = | = | = | = |
| Painted layers | button.md:hidden.flex 38.0x38.0 outline 2px solid #000000 @ 0 offset 2px | = | - | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `m-menu-btn-default.png`, `m-menu-btn-hover.png`, `m-menu-btn-focus-visible.png`, `m-menu-btn-pressed.png`, `m-menu-btn-opened.png`.

#### m-drawer

Mobile nav overlay. The nav layer opened by the "Open menu" button; its links were never followed.

Page: mobile. Selector: `mobile nav overlay`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366 x 126 |
| Padding | 4px 6px 8px 6px |
| Border | T: 1px solid #2b2b2b; R: 1px solid #282828; B: 1px solid #282828; L: 1px solid #282828 |
| Radius | 16px |
| Background | #1f1f1f |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 2px 8px -2px, #000000 @ 0.5 0px 16px 40px -8px |
| Backdrop filter | blur(16px) |
| Outline | none |
| Font | ui-sans-serif 16px/24px 400 |
| Letter spacing | normal |
| Colour | #fafafa |
| Text node | a.relative.flex: ui-sans-serif 15px/22.5px 400, #fafafa |
| Transition | none |
| Painted layers | div.z-50.overflow-y-auto 366.0x126.0 bg #1f1f1f border T:1px solid #2b2b2b / R:1px solid #282828 / B:1px solid #282828 / L:1px solid #282828 r 16px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 2px 8px -2px, #000000 @ 0.5 0px 16px 40px -8px; div.mx-auto.mt-1 36.0x4.0 bg #fafafa @ 0.086 r 9999px; a.relative.flex 352.0x44.0 r 10px outline 2px solid #000000 @ 0 offset 2px; a.relative.flex 352.0x44.0 r 10px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `m-drawer-default.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 342 x 142.55 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | ui-sans-serif 44px/47.52px 500 |
| Letter spacing | -1.1px |
| Colour | #fafafa |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero CTA at 390 wide; measured, never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 127.84 x 40 | = | = | = |
| Padding | 0px 12px 0px 16px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Background image | linear-gradient(to top, #adadad 20%, #cacaca 80%) | = | = | = |
| Box shadow | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px | #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px | #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px |
| Outline | none | = | = | = |
| Font | ui-sans-serif 15px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #090909 | #242424 | = | #242424 |
| Transition | color, background-color, border-color, text-decoration-color, fill, stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #090909 | 16 x 16, colour #242424 | = | 16 x 16, colour #242424 |
| ::before | 125.844px x 38px, absolute, bg #000000 @ 0 radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% 40% at 72% 108%, #f78264 @ 0., radius 9999px, shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset | = | = | = |
| ::after | 125.844px x 38px, absolute, bg #000000 @ 0 linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4), radius 9999px | = | = | = |
| Painted layers | button.ds-focus:ring-2.ds-focus:ring-focus-ring 127.8x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 1px 2px 0px, #000000 @ 0.22 0px 4px 12px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 127.8x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.35 0px 2px 4px 0px, #000000 @ 0.28 0px 6px 16px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 127.8x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff 0px 0px 0px 0px, #adadad @ 0.5 0px 0px 0px 2px, #000000 @ 0 0px 0px 0px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px | button.ds-focus:ring-2.ds-focus:ring-focus-ring 127.8x40.0 image linear-gradient(to top, #adadad 20%, #cacaca 80%) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px shadow #ffffff @ 0.6 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset, #000000 @ 0.55 0px 0px 0px 0.5px, #000000 @ 0.3 0px 1px 1px 0px; button::before.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image radial-gradient(55% 40% at 28% 108%, #d15dff @ 0.3, #000000 @ 0 100%), radial-gradient(55% r 9999px shadow #ffffff @ 0.85 0px 1px 0px 0px inset, #000000 @ 0.06 0px -1px 0px 0px inset; button::after.ds-focus:ring-2.ds-focus:ring-focus-ring 125.844pxx38px image linear-gradient(90deg, #d15dff, #f78264 55%, #efd7a4) r 9999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(1, 0, 0, 1, 0, 1) |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

## Transitions declared in the readable stylesheets

flask.do serves its CSS as the inline `<style id="ds-theme">` block plus a linked root-*.css bundle, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- about: `color 0.1s ease-out, text-decoration-color 0.1s ease-out`, `color 50ms ease-out, background-color 50ms ease-out`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), clip-path 0.28s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 80ms ease-out`, `opacity 0.15s ease-out 0.15s`, `none`, `box-shadow 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.9s cubic-bezier(0.2, 0, 0, 1)`, `transform 0.2s`, `opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1), --button-light 0.26s cubic-bezier(0.23, 1, 0.32, 1)`

- home: `color 0.1s ease-out, text-decoration-color 0.1s ease-out`, `color 50ms ease-out, background-color 50ms ease-out`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), clip-path 0.28s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 80ms ease-out`, `opacity 0.15s ease-out 0.15s`, `none`, `box-shadow 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.9s cubic-bezier(0.2, 0, 0, 1)`, `transform 0.2s`, `opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1), --button-light 0.26s cubic-bezier(0.23, 1, 0.32, 1)`

- login: `color 0.1s ease-out, text-decoration-color 0.1s ease-out`, `color 50ms ease-out, background-color 50ms ease-out`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), clip-path 0.28s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 80ms ease-out`, `opacity 0.15s ease-out 0.15s`, `none`, `box-shadow 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.9s cubic-bezier(0.2, 0, 0, 1)`, `transform 0.2s`, `opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1), --button-light 0.26s cubic-bezier(0.23, 1, 0.32, 1)`

- mcp: `color 0.1s ease-out, text-decoration-color 0.1s ease-out`, `color 50ms ease-out, background-color 50ms ease-out`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), clip-path 0.28s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 80ms ease-out`, `opacity 0.15s ease-out 0.15s`, `none`, `box-shadow 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.9s cubic-bezier(0.2, 0, 0, 1)`, `transform 0.2s`, `opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1), --button-light 0.26s cubic-bezier(0.23, 1, 0.32, 1)`

- pricing: `color 0.1s ease-out, text-decoration-color 0.1s ease-out`, `color 50ms ease-out, background-color 50ms ease-out`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), clip-path 0.28s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 80ms ease-out`, `opacity 0.15s ease-out 0.15s`, `none`, `box-shadow 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.9s cubic-bezier(0.2, 0, 0, 1)`, `transform 0.2s`, `opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1), --button-light 0.26s cubic-bezier(0.23, 1, 0.32, 1)`

- security: `color 0.1s ease-out, text-decoration-color 0.1s ease-out`, `color 50ms ease-out, background-color 50ms ease-out`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), clip-path 0.28s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 80ms ease-out`, `opacity 0.15s ease-out 0.15s`, `none`, `box-shadow 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.9s cubic-bezier(0.2, 0, 0, 1)`, `transform 0.2s`, `opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1), --button-light 0.26s cubic-bezier(0.23, 1, 0.32, 1)`

- video-collaboration: `color 0.1s ease-out, text-decoration-color 0.1s ease-out`, `color 50ms ease-out, background-color 50ms ease-out`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), clip-path 0.28s cubic-bezier(0.23, 1, 0.32, 1)`, `opacity 80ms ease-out`, `opacity 0.15s ease-out 0.15s`, `none`, `box-shadow 0.15s cubic-bezier(0.2, 0, 0, 1), color 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.15s cubic-bezier(0.2, 0, 0, 1)`, `opacity 0.28s cubic-bezier(0.23, 1, 0.32, 1), background-size 0.28s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.9s cubic-bezier(0.2, 0, 0, 1)`, `transform 0.2s`, `opacity 0.15s cubic-bezier(0.23, 1, 0.32, 1), --button-light-r 0.26s cubic-bezier(0.23, 1, 0.32, 1), --button-light 0.26s cubic-bezier(0.23, 1, 0.32, 1)`

## Reduced motion

- home (`header a` under prefers-reduced-motion): Error: browser.newContext: Target page, context or browser has been closed
