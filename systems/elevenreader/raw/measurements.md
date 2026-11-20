# Component measurements

Computed styles read from elevenreader.io on 2026-11-13 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's light public surface — the marketing pages, a public audiobook page, and the /reader/sign-in and sign-up cards — with the Cookiebot consent banner hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). The stylesheet declares a .dark token scope but no public page paints it; the email sign-in/sign-up forms were revealed by their own "…with email" toggles (local UI, nothing sent) and the fields were focused, never submitted. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### promo-banner

Promo banner. The announcement strip above the header (a #F5F3F1 band, here the Black-Friday offer).

Page: home. Selector: `div.bg-[#F5F3F1]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 49 |
| Padding | 8px 16px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.1; L: none |
| Radius | 0px |
| Background | #f5f3f1 |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: Inter 14px/18px 500, #000000, ls 0.14px |
| Transition | none |
| Painted layers | div.text-default.flex 1440.0x49.0 bg #f5f3f1 border B:1px solid #000000 @ 0.1; a.inline-flex.items-center 106.8x32.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up body.has-[.payload-admin-bar]:mb-10 bg #fdfcfc |
| How | at rest |

Crops: `promo-banner-default.png`.

#### promo-cta

Promo CTA. The Get-this-offer pill inside the banner; measured never followed (it opens the subscribe flow).

Page: home. Selector: `a "Get this offer"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.78 x 32 | = | = | 104.65 x 31.36 |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #fdfcfc | = | #fdfcfc |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 13px/18px 400 | = | = | = |
| Letter spacing | 0.13px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 106.8x32.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 106.8x32.0 bg #fdfcfc r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 106.8x32.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 offset 2px | a.inline-flex.items-center 104.6x31.4 bg #fdfcfc r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up div.text-default.flex bg #f5f3f1 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `promo-cta-default.png`, `promo-cta-hover.png`, `promo-cta-focus-visible.png`, `promo-cta-pressed.png`.

#### header

Header. The top bar: wordmark, the Main nav (Explore, Discover, Pricing, For Authors, Upload & Listen), Sign in and the dark Start-listening pill.

Page: home. Selector: `div:has(> nav[aria-label="Main"])`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1304 x 64 |
| Padding | 0px 64px |
| Gap | normal 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.inline-flex.items-center: Inter 16px/24px 400, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | a.inline-flex.items-center 158.8x44.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 0px; a.inline-flex.justify-center 164.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.justify-center 74.3x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; button.inline-flex.items-center 40.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.justify-center 70.3x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.justify-center 102.7x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up body.has-[.payload-admin-bar]:mb-10 bg #fdfcfc |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The ElevenReader wordmark anchor (a 140x15 webp).

Page: home. Selector: `header a[href="/"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 164 x 36 |
| Padding | 0px 12px |
| Border | none |
| Radius | 9999px |
| Background | transparent |
| Box shadow | none |
| Outline | 2px solid #000000 @ 0 offset 2px |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.inline-flex.justify-center 164.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A plain header nav link (rounded-full, hover bg-surface).

Page: home. Selector: `nav a "Pricing"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70.27 x 36 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #f6f6f6 | = | #f6f6f6 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.justify-center 70.3x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.justify-center 70.3x36.0 bg #f6f6f6 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.justify-center 70.3x36.0 r 9999px outline 2px solid #000000 offset 2px | a.inline-flex.justify-center 70.3x36.0 bg #f6f6f6 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-discover

Discover trigger. The chevron button that opens the Discover mega-menu; toggled for the panel readings, then closed.

Page: home. Selector: `button[aria-label="Discover"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 36 | = | = | = |
| Padding | 2px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | #f6f6f6 | = | #f6f6f6 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | 0.14px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | = | = | = |
| Painted layers | button.inline-flex.items-center 40.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.inline-flex.items-center 40.0x36.0 bg #f6f6f6 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.inline-flex.items-center 40.0x36.0 r 9999px outline 2px solid #000000 offset 2px | button.inline-flex.items-center 40.0x36.0 bg #f6f6f6 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-discover-default.png`, `nav-discover-hover.png`, `nav-discover-focus-visible.png`, `nav-discover-pressed.png`.

#### nav-signin

Sign-in button. The outlined Sign-in pill (bg-default + border, hover bg-surface); measured never followed.

Page: home. Selector: `a "Sign in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.44 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #e5e5e5 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f6f6f6 | = | #f6f6f6 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.05 0px 1px 2px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.items-center.justify-center 78.4x36.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.05 0px 1px 2px 0px outline 2px solid #000000 @ 0 offset 2px | a.items-center.justify-center 78.4x36.0 bg #f6f6f6 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.05 0px 1px 2px 0px outline 2px solid #000000 @ 0 offset 2px | a.items-center.justify-center 78.4x36.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.05 0px 1px 2px 0px outline 2px solid #000000 offset 2px | a.items-center.justify-center 78.4x36.0 bg #f6f6f6 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.05 0px 1px 2px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Nav CTA. The dark Start-listening-free pill (bg-inverse text-inverse, hover bg-darkest); measured never followed.

Page: home. Selector: `a "Start listening free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 154.27 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #6e6e6e | = | #6e6e6e |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #000000 offset 0px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.hidden.md:inline: Inter 14px/20px 400, #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 154.3x36.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 0px | a.inline-flex.items-center 154.3x36.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 0px | a.inline-flex.items-center 154.3x36.0 bg #000000 r 9999px outline 2px solid #000000 offset 0px | a.inline-flex.items-center 154.3x36.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### nav-dropdown

Discover mega-menu. The Discover dropdown panel (Popular Genres, Trending Collections, Free Audiobooks cover grid), opened by its own trigger.

Page: home. Selector: `discover panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 846 x 470 |
| Padding | 0px |
| Border | 1px solid #f2f2f2 |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.f-ui-02.text-light: Inter 14px/19.6px 500, #6e6e6e |
| Transition | width, height 0.3s cubic-bezier(0.4, 0, 0.2, 1) |
| Painted layers | div.bg-default.border-lightest 846.0x470.0 bg #ffffff border T:1px solid #f2f2f2 / R:1px solid #f2f2f2 / B:1px solid #f2f2f2 / L:1px solid #f2f2f2 r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px; a.inline-flex.cursor-pointer 260.0x40.0 r 6px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.cursor-pointer 260.0x40.0 r 6px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.cursor-pointer 260.0x40.0 r 6px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.cursor-pointer 260.0x40.0 r 6px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.cursor-pointer 260.0x40.0 r 6px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### menu-link

Menu link. A genre link inside the opened mega-menu.

Page: home. Selector: `mega-menu a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 260 x 40 | = | = | = |
| Padding | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | transparent | #f2f2f2 | #f2f2f2 | #f2f2f2 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | 2px solid #000000 offset 2px |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.line-clamp-2.font-medium: Inter 14px/20px 500, #000000 | = | = | = |
| Transition | all 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.cursor-pointer 260.0x40.0 r 6px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.cursor-pointer 260.0x40.0 bg #f2f2f2 r 6px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.cursor-pointer 260.0x40.0 bg #f2f2f2 r 6px outline 2px solid #000000 offset 2px | a.inline-flex.cursor-pointer 260.0x40.0 bg #f2f2f2 r 6px outline 2px solid #000000 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-link-default.png`, `menu-link-hover.png`, `menu-link-focus-visible.png`, `menu-link-pressed.png`.

#### menu-heading

Menu column heading. A column heading inside the mega-menu.

Page: home. Selector: `mega-menu heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 260 x 29.59 |
| Padding | 10px 10px 0px 10px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/19.6px 500 |
| Letter spacing | normal |
| Colour | #6e6e6e |
| Transition | none |
| How | at rest |

Crops: `menu-heading-default.png`.

### Home hero

#### hero-h1

Hero headline. The 60px Waldenburg display headline (40px under lg).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 507.77 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 60px/60px 400 |
| Letter spacing | -1.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-lede

Hero lede. The 18px opacity-60 lede under the headline.

Page: home. Selector: `hero lede (opacity-60)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 472.5 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/26px 400 |
| Letter spacing | 0.16px |
| Colour | #000000 |
| Transition | none |
| Opacity | 0.6 |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-cta

Hero CTA. The dark Start-listening-free pill under the lede; measured never followed.

Page: home. Selector: `main a "Start listening free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 190.94 x 52 | = | = | 187.12 x 50.96 |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #6e6e6e | = | #6e6e6e |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/22.4px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 190.9x52.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 190.9x52.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 190.9x52.0 bg #000000 r 9999px outline 2px solid #000000 offset 2px | a.inline-flex.items-center 187.1x51.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-cta-2

Hero secondary CTA. The white shadowed pill beside the dark CTA (bg-default, layered ring shadow, active scale-98).

Page: home. Selector: `hero secondary pill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163.91 x 52 | = | = | 160.63 x 50.96 |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f2f2f2 | = | #f2f2f2 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/22.4px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 163.9x52.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 163.9x52.0 bg #f2f2f2 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 163.9x52.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 offset 2px | a.inline-flex.items-center 160.6x51.0 bg #f2f2f2 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-2-default.png`, `hero-cta-2-hover.png`, `hero-cta-2-focus-visible.png`, `hero-cta-2-pressed.png`.

#### book-cover

Book cover card. A cover card in the hero orbit carousel (rounded-md, cover img on a gray-300 backing); the front-most (widest) card is read.

Page: home. Selector: `[data-card-index]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 211.11 x 316.66 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 18px/28.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, -12) | = |
| Cursor | grab | = |
| How | at rest | mouse hover |

Crops: `book-cover-default.png`, `book-cover-hover.png`.

### Home sections

#### eyebrow

Section eyebrow. The small medium-weight section eyebrow (opacity-60).

Page: home. Selector: `h2 eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 548 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 24px/32px 375 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `eyebrow-default.png`.

#### section-h3

Section heading. A 36px Waldenburg section heading (30px under lg).

Page: home. Selector: `h3.font-waldenburg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 362 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 36px/42px 375 |
| Letter spacing | -0.36px |
| Colour | #000000 |
| Text node | span: Waldenburg 36px/42px 375, #000000, ls -0.36px |
| Transition | none |
| How | at rest |

Crops: `section-h3-default.png`.

#### book-link

Book link. A title link in a book row (text-inherit, underline on hover/focus).

Page: home. Selector: `a.underline-offset-2`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 257.56 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 15px/22px 500 | = | = | = |
| Letter spacing | 0.15px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Text decoration | - | underline offset 2px | underline offset 2px | underline offset 2px |

Crops: `book-link-default.png`, `book-link-hover.png`, `book-link-focus-visible.png`, `book-link-pressed.png`.

#### genre-chip

Genre chip. A genre filter chip in Trending genres (rounded-full); measured, never pressed (a press navigates).

Page: home. Selector: `genre chip button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.02 x 44 | = | = | 99 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/22.4px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 101.0x44.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | = | button.inline-flex.items-center 101.0x44.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 offset 2px | button.inline-flex.items-center 99.0x43.1 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `genre-chip-default.png`, `genre-chip-hover.png`, `genre-chip-focus-visible.png`, `genre-chip-pressed.png`.

#### view-all

View-all link. The ghost View-all link on a section rail.

Page: home. Selector: `a "View all"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 99.33 x 44 | = | = | 97.34 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 0px 0px 1px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/22.4px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #000000 @ 0.6 | = | = | = |
| Transition | color, background-color, border-color, transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 99.3x44.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px | = | a.inline-flex.items-center 99.3x44.0 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 0px 0px 1px outline 2px solid #000000 offset 2px | a.inline-flex.items-center 97.3x43.1 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.04 0px 0px 0px 1px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `view-all-default.png`, `view-all-hover.png`, `view-all-focus-visible.png`, `view-all-pressed.png`.

#### try-cta

Try-free CTA. A mid-page Try-it-free white pill (bg-default shadow, active scale-98); measured never followed.

Page: home. Selector: `a "Try it free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 114.97 x 44 | = | = | 112.67 x 43.12 |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f2f2f2 | = | #f2f2f2 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/22.4px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, border-color, transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 115.0x44.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 115.0x44.0 bg #f2f2f2 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 115.0x44.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 offset 2px | a.inline-flex.items-center 112.7x43.1 bg #f2f2f2 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `try-cta-default.png`, `try-cta-hover.png`, `try-cta-focus-visible.png`, `try-cta-pressed.png`.

#### faq-item

FAQ item. A homepage FAQ <details>; the open state is the item after its own summary was clicked.

Page: home. Selector: `details[name=homepage-faq]`. States: default, open.

| Property | default | open |
|---|---|---|
| Size (w x h) | 780 x 67 | 796 x 159 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 20px | 24px |
| Background | #faf8f8 | #ffffff |
| Box shadow | none | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 0px 1px 0px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px |
| Outline | none | = |
| Font | Inter 18px/28.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.flex-1: Waldenburg 20px/27px 400, #000000 | = |
| Transition | box-shadow, background-color, margin, border-radius 0.65s cubic-bezier(0.22, 1, 0.36, 1) | = |
| Painted layers | details.faq-accordion-item.group 780.0x67.0 bg #faf8f8 r 20px; summary::before.effect-focus-before.font-waldenburg 788pxx75px border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px; div.absolute.h-0.5 14.0x2.0 bg #646363 r 9999px; div.absolute.h-3.5 2.0x14.0 bg #646363 r 9999px | details.faq-accordion-item.group 796.0x159.0 bg #ffffff r 24px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 0px 1px 0px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px; summary::before.effect-focus-before.font-waldenburg 804pxx75px border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px; div.absolute.h-0.5 14.0x2.0 bg #646363 r 9999px; div.absolute.h-3.5 14.0x2.0 bg #646363 r 9999px |
| How | at rest | opened by its own summary |

Crops: `faq-item-default.png`, `faq-item-open.png`.

#### faq-summary

FAQ summary. The clickable FAQ question row (with the +/- indicator); a press toggles its details.

Page: home. Selector: `details summary`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 796 x 67 | = | = | = |
| Padding | 20px 24px | = | = | = |
| Gap | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Waldenburg 20px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.flex-1: Waldenburg 20px/27px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 804px x 75px, absolute, bg #000000 @ 0, radius 24px | = | = | = |
| Painted layers | summary::before.effect-focus-before.font-waldenburg 804pxx75px border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px; div.absolute.h-0.5 14.0x2.0 bg #646363 r 9999px; div.absolute.h-3.5 14.0x2.0 bg #646363 r 9999px | = | = | = |
| Ancestor paint | 1 up details.faq-accordion-item.group bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.4 0px 0px 1px 0px, #000000 @ 0.04 0px 1px 1px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `faq-summary-default.png`, `faq-summary-hover.png`, `faq-summary-focus-visible.png`, `faq-summary-pressed.png`.

### Footer

#### footer

Footer. The footer: the big Footer heading, the <details> link columns, legal and app badges.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 967.31 |
| Padding | 120px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.text-lighter.text-[13px]: Inter 13px/18.2px 500, #767676 |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | summary::before.effect-color.effect-focus-before autoxauto border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px; summary::before.effect-color.effect-focus-before autoxauto border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px; summary::before.effect-color.effect-focus-before autoxauto border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px; summary::before.effect-color.effect-focus-before autoxauto border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px; summary::before.effect-color.effect-focus-before autoxauto border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px; summary::before.effect-color.effect-focus-before autoxauto border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px |
| Ancestor paint | 1 up body.has-[.payload-admin-bar]:mb-10 bg #fdfcfc |
| How | at rest |

Crops: `footer-default.png`.

#### footer-col

Footer column heading. A muted column heading (text-lighter 13px) over a footer link list.

Page: home. Selector: `footer column p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 279 x 18.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 13px/18.2px 500 |
| Letter spacing | normal |
| Colour | #767676 |
| Transition | none |
| How | at rest |

Crops: `footer-col-default.png`.

#### footer-link

Footer link. A footer link (effect-focus-underline).

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 131.94 x 19.59 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #6e6e6e | = | #6e6e6e |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Text decoration | - | underline offset 2px | underline offset 2px | underline offset 2px |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### cookie-btn

Cookie-settings button. The Cookie Settings text-button in the legal column; measured, never pressed (a press opens the consent preferences).

Page: home. Selector: `footer button "Cookie Settings"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.02 x 28.8 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/28.8px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Text decoration | - | underline offset 2px | underline offset 2px | underline offset 2px |

Crops: `cookie-btn-default.png`, `cookie-btn-hover.png`, `cookie-btn-focus-visible.png`, `cookie-btn-pressed.png`.

### Explore catalog

#### explore-h1

Explore headline. The "Find your next audiobook" Waldenburg heading (text-4xl lg).

Page: explore. Selector: `h1 on /explore`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 399.83 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 36px/40px 400 |
| Letter spacing | -1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `explore-h1-default.png`.

#### rail-h2

Rail heading. A carousel rail heading (Top picks, What's trending).

Page: explore. Selector: `rail h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 73.31 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 16px/24px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `rail-h2-default.png`.

#### coverflow-card

Coverflow card. A cover card in an explore rail (2:3 cover on bg-hovered, rounded-md shadow-lg, group-hover scale-105).

Page: explore. Selector: `[data-coverflow-card]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 300.16 x 564.23 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 18px/28.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span.text-base.text-text: Inter 16px/24px 500, #000000 | = |
| Transition | none | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = |
| Cursor | pointer | = |
| Painted layers | div.transition-transform.[transition-duration:300ms] 300.2x450.2 bg #f0f0f0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px | div.transition-transform.[transition-duration:300ms] 315.2x472.7 bg #f0f0f0 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px |
| How | at rest | mouse hover |

Crops: `coverflow-card-default.png`, `coverflow-card-hover.png`.

#### book-title

Book title link. The title link under a cover (text-base font-medium, group-hover underline).

Page: explore. Selector: `coverflow title a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 300.16 x 114 | = | = | = |
| Padding | 24px 0px 0px 0px | = | = | = |
| Gap | 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-base.text-text: Inter 16px/24px 500, #000000 | = | = | = |
| Transition | opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `book-title-default.png`, `book-title-hover.png`, `book-title-focus-visible.png`, `book-title-pressed.png`.

#### book-meta

Book meta. An author/length label under a cover (variant=subtle, text-label).

Page: explore. Selector: `coverflow span[variant=subtle]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 85.23 x 20 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 400 |
| Letter spacing | normal |
| Colour | #767676 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `book-meta-default.png`.

#### genre-link

Genre link. A genre link in the catalog; measured never followed.

Page: explore. Selector: `a[href*="/genres/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.42 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h2.font-medium.lg:text-base: Inter 16px/24px 500, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #767676 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Text decoration | - | underline | underline | underline |

Crops: `genre-link-default.png`, `genre-link-hover.png`, `genre-link-focus-visible.png`, `genre-link-pressed.png`.

### Pricing

#### pricing-h1

Pricing title. The 60px Waldenburg pricing display heading.

Page: pricing. Selector: `pricing display h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 620 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 60px/60px 375 |
| Letter spacing | -1.8px |
| Colour | #000000 |
| Text node | span: Waldenburg 60px/60px 375, #000000, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### billing-off

Billing option (idle). The unselected Monthly segment (#57534F text, hover black); the state was toggled for a screenshot, never checked out.

Page: pricing. Selector: `button "Monthly"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.3 x 48 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #57534f | #000000 | = | #000000 |
| Transition | color, background-color, box-shadow 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ease-out-slow.effect-focus 101.3x48.0 r 9999px outline 2px solid #000000 @ 0 offset 2px | = | button.ease-out-slow.effect-focus 101.3x48.0 r 9999px outline 2px solid #000000 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-off-default.png`, `billing-off-hover.png`, `billing-off-focus-visible.png`, `billing-off-pressed.png`.

#### billing-on

Billing option (selected). The selected Annual segment (white pill, ring shadow, the green Save-25% chip).

Page: pricing. Selector: `button "Annual"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 188.83 x 48 | = | = | = |
| Padding | 10px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | color, background-color, box-shadow 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.ease-out-slow.effect-focus 188.8x48.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px; span.inline-flex.items-center 89.2x28.0 bg #e1f5e0 r 9999px | = | button.ease-out-slow.effect-focus 188.8x48.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 offset 2px; span.inline-flex.items-center 89.2x28.0 bg #e1f5e0 r 9999px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `billing-on-default.png`, `billing-on-hover.png`, `billing-on-focus-visible.png`, `billing-on-pressed.png`.

#### save-badge

Save badge. The green Save-25% chip inside the Annual segment (#E1F5E0 bg, #307D18 text).

Page: pricing. Selector: `span "Save 25%"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 89.16 x 28 |
| Padding | 4px 12px |
| Gap | 4px |
| Border | none |
| Radius | 9999px |
| Background | #e1f5e0 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/20px 500 |
| Letter spacing | normal |
| Colour | #307d18 |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.inline-flex.items-center 89.2x28.0 bg #e1f5e0 r 9999px |
| Ancestor paint | 1 up button.ease-out-slow.effect-focus bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 |
| How | at rest |

Crops: `save-badge-default.png`.

#### plan-card

Plan card. A pricing plan card (the painted ancestor of the plan name).

Page: pricing. Selector: `plan card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 584 x 721.94 |
| Padding | 56px |
| Border | 1px solid #eae9e9 |
| Radius | 40px |
| Background | #fdfcfc |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.font-waldenburg.text-[22px]: Waldenburg 22px/28px 375, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.flex.flex-col 584.0x721.9 bg #fdfcfc border T:1px solid #eae9e9 / R:1px solid #eae9e9 / B:1px solid #eae9e9 / L:1px solid #eae9e9 r 40px; div.my-7.h-px 470.0x1.0 bg #eae9e9; div.mb-7.h-px 470.0x1.0 bg #eae9e9; a.inline-flex.items-center 470.0x52.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-name

Plan name. A plan card's name.

Page: pricing. Selector: `plan name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 470 x 28 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.font-waldenburg.text-[22px]: Waldenburg 22px/28px 375, #000000 |
| Transition | none |
| Ancestor paint | 1 up div.flex.flex-col bg #fdfcfc |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. A plan card's price figure.

Page: pricing. Selector: `plan price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 470 x 36 |
| Padding | 0px |
| Gap | 12px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.font-waldenburg.-mb-1: Waldenburg 36px/36px 375, #000000, ls -0.36px |
| Transition | none |
| Ancestor paint | 1 up div.flex.flex-col bg #fdfcfc |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A plan card's action (Start-3-day-free-trial pill); measured never followed.

Page: pricing. Selector: `plan CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 472 x 52 | = | = | 462.56 x 50.96 |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #6e6e6e | = | #6e6e6e |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 16px/22.4px 400 | = | = | = |
| Letter spacing | 0.16px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, transform 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.inline-flex.items-center 472.0x52.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 472.0x52.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 2px | a.inline-flex.items-center 472.0x52.0 bg #000000 r 9999px outline 2px solid #000000 offset 2px | a.inline-flex.items-center 462.6x51.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### feature-li

Feature row. A feature row inside a plan card or the "Everything you unlock" list.

Page: pricing. Selector: `main section li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 470 x 44.98 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.font-waldenburg.text-[18px]: Waldenburg 18px/23.4px 375, #000000 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| How | at rest |

Crops: `feature-li-default.png`.

### Audiobook page

#### ab-h1

Title. The audiobook title heading.

Page: audiobook. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 568 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 36px/40px 400 |
| Letter spacing | -1.2px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `ab-h1-default.png`.

#### ab-cover

Cover. The square audiobook cover (8px radius, blurred-thumb placeholder).

Page: audiobook. Selector: `audiobook cover img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 262 x 262 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(data:…);' href='data:image/webp;base64,UklGRiwAAABXRUJQVlA4ICAAAAAwAQCdASoIAAgABUB8JYwAA3AA/vDKRTnSq0tsOsgAAA=='/%3E%3C/svg%3E") |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0 |
| Transition | all 0.7s cubic-bezier(0.31, 0.325, 0, 0.92) |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Ancestor paint | 1 up div.rounded-sm.transition-transform bg #f0f0f0 shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest |

Crops: `ab-cover-default.png`.

#### ab-preview

Preview button. The audio Preview button (speaker icon); measured, never pressed (a press plays audio).

Page: audiobook. Selector: `button "Preview"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264 x 48 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #767676 | = | #767676 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 | 16 x 16, colour #767676 | = | 16 x 16, colour #767676 |
| Painted layers | button.items-center.justify-center 264.0x48.0 r 9999px outline 2px solid #000000 @ 0 offset 2px | = | button.items-center.justify-center 264.0x48.0 r 9999px outline 2px solid #000000 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ab-preview-default.png`, `ab-preview-hover.png`, `ab-preview-focus-visible.png`, `ab-preview-pressed.png`.

#### ab-chip

Format chip. The "Audio only" format chip.

Page: audiobook. Selector: `"Audio only" chip`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 568 x 30 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.flex-none.justify-center: Inter 14px/20px 400, #000000 |
| Transition | none |
| Painted layers | div.flex-none.justify-center 87.6x30.0 bg #f2f2f2 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px |
| How | at rest |

Crops: `ab-chip-default.png`.

#### ab-crumb

Breadcrumb link. A breadcrumb link (Explore / genre) above the title.

Page: audiobook. Selector: `main breadcrumb a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.05 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 12px/13.2px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #767676 | #6e6e6e | = | #6e6e6e |
| Text node | span.whitespace-nowrap.text-inherit: Inter 14px/20px 500, #767676 | span.whitespace-nowrap.text-inherit: Inter 14px/20px 500, #6e6e6e | = | span.whitespace-nowrap.text-inherit: Inter 14px/20px 500, #6e6e6e |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Text decoration | - | underline offset 2px | underline offset 2px | underline offset 2px |

Crops: `ab-crumb-default.png`, `ab-crumb-hover.png`, `ab-crumb-focus-visible.png`, `ab-crumb-pressed.png`.

#### ab-author

Author link. The By-author link under the title.

Page: audiobook. Selector: `a[href*="/authors/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61.64 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #767676 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Text decoration | - | underline offset 2px | underline offset 2px | underline offset 2px |

Crops: `ab-author-default.png`, `ab-author-hover.png`, `ab-author-focus-visible.png`, `ab-author-pressed.png`.

#### ab-row

Related title link. A related-audiobook link in "More from" / "You may also like".

Page: audiobook. Selector: `related a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 264 x 152 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 18px/28.8px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.text-base.text-text: Inter 16px/24px 500, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 14 x 14, colour #949494 | = | = | = |
| Painted layers | div.rounded-sm.shadow-lg 120.0x120.0 bg #f0f0f0 r 2px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px | div.rounded-sm.shadow-lg 126.0x126.0 bg #f0f0f0 r 2px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px | div.rounded-sm.shadow-lg 126.0x126.0 bg #f0f0f0 r 2px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px | div.rounded-sm.shadow-lg 126.0x126.0 bg #f0f0f0 r 2px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ab-row-default.png`, `ab-row-hover.png`, `ab-row-focus-visible.png`, `ab-row-pressed.png`.

### Compare

#### cmp-h1

Compare title. The "ElevenReader vs. other text to speech apps" heading.

Page: compare. Selector: `h1 on /compare`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 95.03 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 44px/47.52px 375 |
| Letter spacing | -1.5px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `cmp-h1-default.png`.

#### cmp-table

Comparison table. The apps comparison table (header row + feature rows).

Page: compare. Selector: `table`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 932 x 538.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | th.text-[11px].leading-4: Inter 11px/16px 500, #000000 @ 0.55, ls 1.1px |
| Transition | none |
| Painted layers | th.align-top.font-medium 177.1x91.0 bg #f5f3f1 r 12px 0px 0px 12px; td.flex.flex-col 251.6x91.0 bg #f5f3f1; td.flex.flex-col 205.0x91.0 bg #f5f3f1; td.flex.flex-col 298.3x91.0 bg #f5f3f1 r 0px 12px 12px 0px; th.align-top.font-medium 177.1x71.0 border T:1px solid #e8e6e5; a.inline-flex.justify-center 67.1x21.0 r 2px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `cmp-table-default.png`.

#### cmp-th

Table head cell. A header cell in the comparison table.

Page: compare. Selector: `table th`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 177.08 x 29.5 |
| Padding | 0px 16px 10px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 11px/16px 500 |
| Letter spacing | 1.1px |
| Colour | #000000 @ 0.55 |
| Transition | none |
| How | at rest |

Crops: `cmp-th-default.png`.

#### cmp-td

Table cell. A body cell in the comparison table (a check/cross or text).

Page: compare. Selector: `table td`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 251.63 x 91 |
| Padding | 14px 16px |
| Gap | 2px |
| Border | none |
| Radius | 0px |
| Background | #f5f3f1 |
| Box shadow | none |
| Outline | none |
| Font | Inter 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | td.flex.flex-col 251.6x91.0 bg #f5f3f1 |
| How | at rest |

Crops: `cmp-td-default.png`.

#### cmp-link

Comparison link. A link to an in-depth comparison page.

Page: compare. Selector: `compare a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 191 x 48.44 | = | = | = |
| Padding | 6px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | transparent | #faf8f8 | = | #faf8f8 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 13.5px/18.225px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.6 | #000000 | = | #000000 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.items-center.cursor-pointer 191.0x48.4 r 10px outline 2px solid #000000 @ 0 offset 2px | a.items-center.cursor-pointer 191.0x48.4 bg #faf8f8 r 10px outline 2px solid #000000 @ 0 offset 2px | a.items-center.cursor-pointer 191.0x48.4 r 10px outline 2px solid #000000 offset 2px | a.items-center.cursor-pointer 191.0x48.4 bg #faf8f8 r 10px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cmp-link-default.png`, `cmp-link-hover.png`, `cmp-link-focus-visible.png`, `cmp-link-pressed.png`.

### Sign in and sign up

#### signin-card

Sign-in card. The centred sign-in card column (max-w-90: logo, OAuth buttons, the revealed email form, the Create-account footer); never filled or submitted.

Page: signin. Selector: `div.max-w-90`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 900 |
| Padding | 96px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.block.text-base: Inter 16px/24px 500, #000000 |
| Transition | none |
| Icon | 20 x 20, colour #000000 |
| Painted layers | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f2f2f2 r 9999px outline 2px solid #000000 @ 0 offset 0px; button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 0px; div.w-full.border-b 0.0x1.0 border B:1px solid #e5e5e5; div.w-full.border-b 0.0x1.0 border B:1px solid #e5e5e5; input.border-gray-alpha-200.placeholder:text-subtle 26.0x40.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px; button.inline-flex.items-center 122.5x32.0 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest |

Crops: `signin-card-default.png`.

#### sso-google

Google button. The Sign-in-with-Google pill (bg-dark, hover bg-overlay-darker); measured never pressed.

Page: signin. Selector: `button "Sign in with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #f2f2f2 | #000000 @ 0.1 | = | #000000 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #000000 offset 0px | = |
| Font | Inter 14px/15.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Inter 14px/15.4px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| Painted layers | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f2f2f2 r 9999px outline 2px solid #000000 @ 0 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 @ 0.1 r 9999px outline 2px solid #000000 @ 0 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f2f2f2 r 9999px outline 2px solid #000000 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 @ 0.1 r 9999px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `sso-google-default.png`, `sso-google-hover.png`, `sso-google-focus-visible.png`, `sso-google-pressed.png`.

#### sso-apple

Apple button. The Sign-in-with-Apple pill (bg-inverse, hover opacity-80); measured never pressed.

Page: signin. Selector: `button "Sign in with Apple"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #6e6e6e | = | #6e6e6e |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #000000 offset 0px | = |
| Font | Inter 14px/15.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | = |
| Painted layers | button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 r 9999px outline 2px solid #000000 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `sso-apple-default.png`, `sso-apple-hover.png`, `sso-apple-focus-visible.png`, `sso-apple-pressed.png`.

#### email-field

Email field. The email input (rounded-full, border-gray-alpha-200, focus-ring) after the email toggle was pressed; sample text was typed and deleted, nothing sent.

Page: signin. Selector: `input#email`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 360 x 40 | = | = |
| Padding | 8px 12px | = | = |
| Border | 1px solid #e5e5e5 | = | = |
| Radius | 9999px | = | = |
| Background | transparent | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | = |
| Font | Inter 16px/24px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.5, opacity 1 | = | = |
| Painted layers | input.border-gray-alpha-200.placeholder:text-subtle 360.0x40.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### password-field

Password field. The password input after the email toggle; focused only, never filled or submitted.

Page: signin. Selector: `input#password`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 360 x 40 | = |
| Padding | 8px 12px | = |
| Border | 1px solid #e5e5e5 | = |
| Radius | 9999px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0.5, opacity 1 | = |
| Painted layers | input.border-gray-alpha-200.placeholder:text-subtle 360.0x40.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | clicked into the field |

Crops: `password-field-default.png`, `password-field-focused.png`.

#### forgot-btn

Forgot-password button. The Forgot-password link-button beside the Password label (opens a dialog; measured, never pressed).

Page: signin. Selector: `button "Forgot password"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 122.48 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 12px/13.2px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #767676 | = | #767676 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.inline-flex.items-center 122.5x32.0 r 9999px outline 2px solid #000000 @ 0 offset 2px | = | button.inline-flex.items-center 122.5x32.0 r 9999px outline 2px solid #000000 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `forgot-btn-default.png`, `forgot-btn-hover.png`, `forgot-btn-focus-visible.png`, `forgot-btn-pressed.png`.

#### signin-submit

Sign-in submit. The form's Sign-in submit (bg-inverse pill) after the email toggle; measured, never pressed (a press would submit).

Page: signin. Selector: `button[type=submit]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 | #6e6e6e | = | #6e6e6e |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #000000 offset 0px | = |
| Font | Inter 14px/15.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 r 9999px outline 2px solid #000000 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #6e6e6e r 9999px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-submit-default.png`, `signin-submit-hover.png`, `signin-submit-focus-visible.png`, `signin-submit-pressed.png`.

#### signin-secondary

Email-signin button. The outlined Sign-in-with-email pill under the OAuth buttons; it toggles the credential form (pressed after its own readings).

Page: signin. Selector: `button "Sign in with email"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #e5e5e5 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f6f6f6 | = | #f6f6f6 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/15.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Inter 14px/15.4px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.justify-center.whitespace-nowrap 360.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f6f6f6 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px outline 2px solid #000000 offset 2px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f6f6f6 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-secondary-default.png`, `signin-secondary-hover.png`, `signin-secondary-focus-visible.png`, `signin-secondary-pressed.png`.

#### create-link

Create-account link. The card footer's Create-account link; measured never followed.

Page: signin. Selector: `a "Create account"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102.86 x 19.59 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 2px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Inter 14px/19.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #6e6e6e | = | #6e6e6e |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Text decoration | - | underline offset 2px | underline offset 2px | underline offset 2px |

Crops: `create-link-default.png`, `create-link-hover.png`, `create-link-focus-visible.png`, `create-link-pressed.png`.

#### signup-card

Sign-up card. The centred create-account card column (max-w-90: logo, heading, OAuth buttons, legal copy); never filled or submitted.

Page: signup. Selector: `div.max-w-90`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 900 |
| Padding | 96px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 18px/28.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4.block.text-base: Inter 16px/24px 500, #000000 |
| Transition | none |
| Icon | 14 x 14, colour #767676 |
| Painted layers | span.border-dark.text-light 60.5x22.0 border T:1px solid #949494 / R:1px solid #949494 / B:1px solid #949494 / L:1px solid #949494 r 9999px; span.border-dark.text-light 47.8x22.0 border T:1px solid #949494 / R:1px solid #949494 / B:1px solid #949494 / L:1px solid #949494 r 9999px; span.border-dark.text-light 70.9x22.0 border T:1px solid #949494 / R:1px solid #949494 / B:1px solid #949494 / L:1px solid #949494 r 9999px; span.border-dark.text-light 54.1x22.0 border T:1px solid #949494 / R:1px solid #949494 / B:1px solid #949494 / L:1px solid #949494 r 9999px; button.justify-center.whitespace-nowrap 360.0x40.0 bg #f2f2f2 r 9999px outline 2px solid #000000 @ 0 offset 0px; button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest |

Crops: `signup-card-default.png`.

#### signup-field

Signup email field. The signup email input after the email toggle; focused only, never filled or submitted.

Page: signup. Selector: `signup input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 360 x 40 | = |
| Padding | 8px 12px | = |
| Border | 1px solid #e5e5e5 | = |
| Radius | 9999px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = |
| Font | Inter 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0.5, opacity 1 | = |
| Painted layers | input.border-gray-alpha-200.placeholder:text-subtle 360.0x40.0 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px outline 2px solid #000000 @ 0 offset 2px | = |
| How | at rest | clicked into the field |

Crops: `signup-field-default.png`, `signup-field-focused.png`.

#### signup-google

Google sign-up button. The Sign-up-with-Google pill; measured never pressed.

Page: signup. Selector: `button "Sign up with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 10px | = | = | = |
| Border | none | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #f2f2f2 | #000000 @ 0.1 | = | #000000 @ 0.1 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | = | 2px solid #000000 offset 0px | = |
| Font | Inter 14px/15.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Inter 14px/15.4px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000 | = | = | = |
| Painted layers | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f2f2f2 r 9999px outline 2px solid #000000 @ 0 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 @ 0.1 r 9999px outline 2px solid #000000 @ 0 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f2f2f2 r 9999px outline 2px solid #000000 offset 0px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #000000 @ 0.1 r 9999px outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-google-default.png`, `signup-google-hover.png`, `signup-google-focus-visible.png`, `signup-google-pressed.png`.

#### signup-legal

Legal copy. The small legal consent paragraph on the sign-up card.

Page: signup. Selector: `signup legal p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 50.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 12px/16.8px 500 |
| Letter spacing | normal |
| Colour | #6e6e6e |
| Transition | none |
| How | at rest |

Crops: `signup-legal-default.png`.

#### signup-email-btn

Email-signup button. The outlined Sign-up-with-email pill; it toggles the credential form (pressed after its own readings).

Page: signup. Selector: `button[data-signup-email-toggle]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 40 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Border | 1px solid #e5e5e5 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #ffffff | #f6f6f6 | = | #f6f6f6 |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/15.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Inter 14px/15.4px 500, #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.justify-center.whitespace-nowrap 360.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f6f6f6 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px outline 2px solid #000000 @ 0 offset 2px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #ffffff border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px outline 2px solid #000000 offset 2px | button.justify-center.whitespace-nowrap 360.0x40.0 bg #f6f6f6 border T:1px solid #e5e5e5 / R:1px solid #e5e5e5 / B:1px solid #e5e5e5 / L:1px solid #e5e5e5 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signup-email-btn-default.png`, `signup-email-btn-hover.png`, `signup-email-btn-focus-visible.png`, `signup-email-btn-pressed.png`.

### Mobile (390 wide)

#### m-promo

Mobile promo banner.

Page: mobile. Selector: `banner at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 53 |
| Padding | 8px 16px |
| Border | T: none; R: none; B: 1px solid #000000 @ 0.1; L: none |
| Radius | 0px |
| Background | #f5f3f1 |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/23.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong: Inter 14px/18px 500, #000000, ls 0.14px |
| Transition | none |
| Painted layers | div.text-default.flex 390.0x53.0 bg #f5f3f1 border B:1px solid #000000 @ 0.1; a.inline-flex.items-center 106.8x32.0 bg #ffffff r 9999px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.06 0px 0px 0px 1px, #000000 @ 0.04 0px 1px 2px 0px, #000000 @ 0.04 0px 2px 4px 0px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up body.has-[.payload-admin-bar]:mb-10 bg #fdfcfc |
| How | at rest |

Crops: `m-promo-default.png`.

#### m-header

Mobile header. The 390px top bar: wordmark and the Open-menu button.

Page: mobile. Selector: `header bar at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 0px 20px |
| Gap | normal 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 17px/23.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.inline-flex.items-center: Inter 16px/24px 400, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | a.inline-flex.items-center 158.8x44.0 bg #000000 r 9999px outline 2px solid #000000 @ 0 offset 0px; a.inline-flex.justify-center 164.0x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.justify-center 0.0x0.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; button.inline-flex.items-center 0.0x0.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.justify-center 0.0x0.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.justify-center 0.0x0.0 r 9999px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up body.has-[.payload-admin-bar]:mb-10 bg #fdfcfc |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger button in the mobile header.

Page: mobile. Selector: `button[aria-label="Open menu"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 40 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 9999px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | - | = |
| Font | Inter 14px/15.4px 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #000000 | = | - | = |
| Painted layers | button.inline-flex.items-center 40.0x40.0 r 9999px outline 2px solid #000000 @ 0 offset 2px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `m-menu-button-default.png`, `m-menu-button-hover.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The full-screen menu the hamburger opens (nav items plus Sign-in/Start-listening pills).

Page: mobile. Selector: `mobile menu panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px |
| Outline | none |
| Font | Inter 17px/23.8px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a.inline-flex.justify-center: Inter 14px/20px 400, #000000 |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.5s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 24 x 24, colour #000000 |
| Painted layers | div.fixed.z-[999] 390.0x844.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #101828 @ 0.03 0px 4px 6px -2px, #101828 @ 0.08 0px 12px 16px -4px; a.inline-flex.justify-center 140.0x11.9 r 2px outline 2px solid #000000 @ 0 offset 2px; a.inline-flex.justify-center 73.3x36.0 r 9999px outline 2px solid #000000 @ 0 offset 2px; button.effect-focus.effect-color 362.0x24.0 outline 2px solid #000000 @ 0.02 offset 2px; div.px-outer-gutter.-mx-outer-gutter 390.0x700.0 bg #ffffff; a.inline-flex.cursor-pointer 350.0x40.0 r 6px outline 2px solid #000000 @ 0 offset 2px |
| Ancestor paint | 1 up body.has-[.payload-admin-bar]:mb-10 bg #fdfcfc |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. An item inside the opened mobile menu.

Page: mobile. Selector: `mobile menu item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 362 x 24 | = | = | = |
| Padding | 0px 0px 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | 2px solid #000000 @ 0 offset 2px | = | 2px solid #000000 offset 2px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: Inter 14px/20px 400, #000000 | = | = | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | = | = | = |
| Painted layers | button.effect-focus.effect-color 362.0x24.0 outline 2px solid #000000 @ 0 offset 2px | = | button.effect-focus.effect-color 362.0x24.0 outline 2px solid #000000 offset 2px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 338.52 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Waldenburg 40px/40px 400 |
| Letter spacing | -1.8px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-footer-col

Mobile footer column. A footer <details> link column (lg:hidden — the mobile-only accordion); the open state is the column after its own summary was tapped.

Page: mobile. Selector: `footer details at 390`. States: default, open.

| Property | default | open |
|---|---|---|
| Size (w x h) | 350 x 24 | 350 x 266.17 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 17px/23.8px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | summary.effect-color.effect-focus-before: Inter 12px/13.2px 700, #000000 | = |
| Transition | none | = |
| Icon | 24 x 24, colour #000000 | 0 x 0, colour #000000 |
| Painted layers | summary::before.effect-color.effect-focus-before 358pxx32px border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px | = |
| How | at rest | opened by its own summary |

Crops: `m-footer-col-default.png`, `m-footer-col-open.png`.

#### m-footer-summary

Mobile footer summary. The tappable footer column row (f-ui-04 with the chevron pair).

Page: mobile. Selector: `footer summary at 390`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 24 | = | - | = |
| Padding | 4px 0px | = | - | = |
| Gap | 12px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Inter 12px/13.2px 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Transition | color, background-color, border-color, outline-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.3s cubic-bezier(0.31, 0.325, 0, 0.92) | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 0 x 0, colour #000000 | = | - | = |
| ::before | 358px x 32px, absolute, bg #000000 @ 0, radius 24px | = | - | = |
| Painted layers | summary::before.effect-color.effect-focus-before 358pxx32px border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 r 24px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `m-footer-summary-default.png`, `m-footer-summary-hover.png`, `m-footer-summary-pressed.png`.

## Transitions declared in the readable stylesheets

elevenreader.io serves its Next.js CSS bundles same-origin, so this list holds the transitions the readable document.styleSheets rules declare on each page (cross-origin sheets are skipped); the per-state Transition rows above are computed values and cover every rule the page paints.

- audiobook: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- compare: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`

- explore: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- home: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- pricing: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`, `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`

- signin: `transform 0.4s`, `transform 0.4s, opacity 0.4s, height 0.4s, box-shadow 0.2s`, `opacity 0.4s, box-shadow 0.2s`, `opacity 0.1s, background 0.2s, border-color 0.2s`, `opacity 0.4s`, `transform 0.5s, opacity 0.2s`, `none`, `opacity 0.2s, transform 0.2s`, `opacity 0.25s linear`
