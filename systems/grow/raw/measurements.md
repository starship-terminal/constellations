# Grow with Google component measurements

Computed styles read from grow.google's US edition on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the public surfaces — the light-only glue marketing pages: home, the certificate catalog, a certificate detail page and the AI training page — with any cookie-notification layer hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). grow.google serves a regional /intl/<locale>/ edition to a request announcing a real user agent or explicit locale; every reading here is the US edition, taken in a bare context. One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Site chrome

#### header

Site header. The glue top bar: the "Grow with Google" wordmark, the Career Certificates / AI Training / For Partners / Stories & Resources nav and its dropdown mega-menus.

Page: home. Selector: `.glue-header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 16px/24px 400 |
| Letter spacing | 0.1px |
| Colour | #202124 |
| Text node | p.glue-header__skip-content-text: Google Sans Flex 16px/24px 500, #3c4043 |
| Transition | none |
| Icon | 0 x 0, colour #5f6368 |
| Painted layers | header.nav_v1.custome_nav 1440.0x64.0 bg #ffffff; div.glue-header__bar.glue-header__bar--mobile 0.0x0.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px; div.glue-header__bar.glue-header__bar--desktop 1440.0x64.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px; ul.glue-header__list.header-sub_links 0.0x0.0 r 0px 0px 50px 50px shadow #3c4043 @ 0.2 0px 15px 20px 0px; ul.glue-header__list.header-sub_links 0.0x0.0 r 0px 0px 50px 50px shadow #3c4043 @ 0.2 0px 15px 20px 0px; hr.xl-lg-view-only 0.0x0.0 border T:1px #dadce0 |
| How | at rest |

Crops: `header-default.png`.

#### header-logo

Logo. The "Grow with Google" lockup in the header (a .glue-header__logo-link anchor in the desktop bar — the Google mark plus the "Grow with Google" img wordmark, 210x48; the mobile bar carries a second display:none copy).

Page: home. Selector: `.glue-header__bar--desktop .glue-header__logo-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 210 x 48 | = | = | = |
| Padding | 0px 9px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | #f8f9fa | = |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | #000000 @ 0 0px 0px 0px 1px |
| Outline | none | = | = | = |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | 0.25px | = | = | = |
| Colour | #5f6368 | #202124 | #3186ff | #202124 |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Ancestor paint | - | 1 up div.glue-header__logo bg #f8f9fa | = | = |
| Painted layers | - | = | a.glue-header__logo-link 210.0x48.0 bg #f8f9fa r 4px shadow #1a73e8 0px 0px 0px 2px | a.glue-header__logo-link 210.0x48.0 r 4px shadow #000000 @ 0 0px 0px 0px 1px |

Crops: `header-logo-default.png`, `header-logo-focus-visible.png`, `header-logo-pressed.png`.

#### nav-link

Nav link. A header nav link (AI Training); measured, never followed.

Page: home. Selector: `header nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 107.75 x 48 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | #f8f9fa | = |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | 0.25px | = | = | = |
| Colour | #3c4043 | = | #3186ff | = |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.glue-header__link 107.8x48.0 bg #f8f9fa r 4px shadow #1a73e8 0px 0px 0px 2px | a.glue-header__link 107.8x48.0 r 4px shadow #000000 @ 0 0px 0px 0px 0px |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-drop-trigger

Mega-menu trigger. The "Career Certificates" nav item that opens the three-column mega-menu (Foundational / Advanced / Courses). opened was measured after clicking it — a local UI toggle.

Page: home. Selector: `header dropdown trigger`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 174.75 x 48 | = | = | = | = |
| Padding | 0px 12px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 4px | = | = | = | = |
| Background | transparent | = | #f8f9fa | = | = |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | #000000 @ 0 0px 0px 0px 1px | = |
| Outline | none | = | = | = | = |
| Font | Google Sans Flex 16px/24px 500 | = | = | = | = |
| Letter spacing | 0.25px | = | = | = | = |
| Colour | #3c4043 | = | #3186ff | = | = |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | clicked the "Career Certificates" trigger; the mega-menu is open (aria-expanded=true at save) |
| Painted layers | - | = | a.glue-header__link 174.8x48.0 bg #f8f9fa r 4px shadow #1a73e8 0px 0px 0px 2px | a.glue-header__link 174.8x48.0 r 4px shadow #000000 @ 0 0px 0px 0px 1px | = |

Crops: `nav-drop-trigger-default.png`, `nav-drop-trigger-hover.png`, `nav-drop-trigger-focus-visible.png`, `nav-drop-trigger-pressed.png`, `nav-drop-trigger-opened.png`.

#### mega-panel

Mega-menu panel. The opened mega-menu panel: Foundational, Advanced and Courses columns.

Page: home. Selector: `header dropdown panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 623 |
| Padding | 5px 0px |
| Border | none |
| Radius | 0px 0px 50px 50px |
| Background | #ffffff |
| Box shadow | #3c4043 @ 0.2 0px 15px 20px 0px |
| Outline | 1px solid #000000 @ 0 offset 0px |
| Font | Google Sans Flex 16px/24px 400 |
| Letter spacing | normal |
| Colour | #202124 |
| Text node | span.header-sub_links-title: Google Sans Flex 18px/27px 400, #202124 |
| Transition | opacity 0.15s ease-in |
| Painted layers | ul.glue-header__list.header-sub_links 1440.0x623.0 bg #ffffff r 0px 0px 50px 50px shadow #3c4043 @ 0.2 0px 15px 20px 0px outline 1px solid #000000 @ 0 offset 0px; hr.xl-lg-view-only 394.7x1.0 border T:1px #dadce0; a.glue-header__link 272.0x48.0 border L:2px #000000 @ 0 r 4px 0px 0px 4px; a.glue-header__link 272.0x48.0 border L:2px #000000 @ 0 r 4px 0px 0px 4px; a.glue-header__link 272.0x48.0 border L:2px #000000 @ 0 r 4px 0px 0px 4px; a.glue-header__link 272.0x48.0 border L:2px #000000 @ 0 r 4px 0px 0px 4px |
| How | at rest |

Crops: `mega-panel-default.png`.

#### mega-item

Mega-menu item. A certificate link inside the opened mega-menu; measured while the menu was held open, never followed.

Page: home. Selector: `mega-menu link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 272 x 48 | = | = | = |
| Padding | 8px 0px | = | = | = |
| Border | T: none; R: none; B: none; L: 2px solid #000000 @ 0 | = | = | = |
| Radius | 4px 0px 0px 4px | = | = | = |
| Background | transparent | #f8f9fa | #f8f9fa | #f8f9fa |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | #000000 @ 0 0px 0px 0px 1px |
| Outline | none | = | = | = |
| Font | Google Sans Flex 16px/24px 400 | = | = | = |
| Letter spacing | 0.25px | = | = | = |
| Colour | #202124 | #3186ff | #3186ff | #3186ff |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.glue-header__link 272.0x48.0 border L:2px #000000 @ 0 r 4px 0px 0px 4px | a.glue-header__link 272.0x48.0 bg #f8f9fa border L:2px #000000 @ 0 r 4px 0px 0px 4px | a.glue-header__link 272.0x48.0 bg #f8f9fa border L:2px #000000 @ 0 r 4px 0px 0px 4px shadow #1a73e8 0px 0px 0px 2px | a.glue-header__link 272.0x48.0 bg #f8f9fa border L:2px #000000 @ 0 r 4px 0px 0px 4px shadow #000000 @ 0 0px 0px 0px 1px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `mega-item-default.png`, `mega-item-hover.png`, `mega-item-focus-visible.png`, `mega-item-pressed.png`.

### Home

#### promo-banner

Promo banner. The blue "New! Enroll in the AI Certificate and learn vibe coding…" promotion banner under the header — the whole banner is one anchor.

Page: home. Selector: `promo banner`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 575.83 x 25 | = | - | = |
| Padding | 1px 0px 0px 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Google Sans Flex 16px/24px 400 | = | - | = |
| Letter spacing | 0.1px | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span.anchorText: Google Sans Flex 16px/24px 500, #ffffff, ls 0.1px | = | - | = |
| Transition | none | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `promo-banner-default.png`, `promo-banner-hover.png`, `promo-banner-pressed.png`.

#### promo-link

Promo link. The banner's "Enroll now →" tail; measured, never followed.

Page: home. Selector: `promo Enroll now`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 119 x 26 | = | = | = |
| Padding | 0px 1px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | #1a73e8 @ 0.04 |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 5px auto #101010 offset 0px |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | = | = | #3186ff |
| Text node | u: Google Sans Flex 16px/24px 700, #ffffff, ls 0.5px | = | = | u: Google Sans Flex 16px/24px 700, #3186ff, ls 0.5px |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | none | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | 18 x 18, colour #3186ff |
| Painted layers | a.glue-button.glue-button--link 119.0x26.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px | = | a.glue-button.glue-button--link 119.0x26.0 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px shadow #1a73e8 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a.glue-button.glue-button--link 119.0x26.0 bg #1a73e8 @ 0.04 border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 4px outline 5px auto #101010 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `promo-link-default.png`, `promo-link-hover.png`, `promo-link-focus-visible.png`, `promo-link-pressed.png`.

#### hero-h1

Hero headline. The home display heading.

Page: home. Selector: `home h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 616 x 88 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 36px/44px 400 |
| Letter spacing | -0.25px |
| Colour | #202124 |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-cta

Hero CTA. The hero's blue pill action (glue-button--high-emphasis); measured, never followed.

Page: home. Selector: `.glue-button--high-emphasis`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 142.5 x 50 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ffffff | = |
| Radius | 48px | = | = | = |
| Background | #3186ff | = | #185abc | #185abc |
| Box shadow | none | = | #185abc 0px 0px 0px 2px | #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 2px 6px 2px |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 5px auto #101010 offset 0px |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | none | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.glue-button.glue-button--high-emphasis 142.5x50.0 bg #3186ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px | = | a.glue-button.glue-button--high-emphasis 142.5x50.0 bg #185abc border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 48px shadow #185abc 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a.glue-button.glue-button--high-emphasis 142.5x50.0 bg #185abc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 2px 6px 2px outline 5px auto #101010 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### video-teaser

Video teaser. The hero video preview with the 48px play overlay; clicking it opens a glue-modal carrying a YouTube embed. Measured at rest; the modal was screenshotted in the capture pass and closed.

Page: home. Selector: `.glue-video`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 616 x 346.5 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #185abc 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 0px | = |
| Font | Google Sans Flex 19px/28.5px 400 | = | = | = |
| Letter spacing | 0.1px | = | = | = |
| Colour | #202124 | = | = | = |
| Text node | span.glue-label.glue-video__timestamp-duration: Google Sans Flex 11px/16px 500, #202124, ls 0.5px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 48 x 48, colour #ffffff | = | = | = |
| Painted layers | span.glue-video__timestamp.glue-video__timestamp--light 61.5x20.0 bg #ffffff @ 0.62 r 100px | = | div.glue-video.glue-video__preview-container 616.0x346.5 r 4px shadow #185abc 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 0px; span.glue-video__timestamp.glue-video__timestamp--light 61.5x20.0 bg #ffffff @ 0.62 r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `video-teaser-default.png`, `video-teaser-hover.png`, `video-teaser-focus-visible.png`, `video-teaser-pressed.png`.

#### h2

Section heading. A section heading on the marketing home.

Page: home. Selector: `home h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 575 x 46.28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 28px/36px 400 |
| Letter spacing | normal |
| Colour | #202124 |
| Text node | span.glue-font-weight-regular: Google Sans Flex 36px/46.2857px 400, #202124 |
| Transition | none |
| How | at rest |

Crops: `h2-default.png`.

#### body-p

Body paragraph. A body paragraph on the marketing home.

Page: home. Selector: `home p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 394.66 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 14px/21px 400 |
| Letter spacing | normal |
| Colour | #3c4043 |
| Transition | none |
| How | at rest |

Crops: `body-p-default.png`.

#### card

Content card. A bordered content card on the home (the "New vibe coding course…" announcement cards).

Page: home. Selector: `.glue-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1296 x 285 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Google Sans Flex 16px/24px 400 | = |
| Letter spacing | 0.1px | = |
| Colour | #202124 | = |
| Text node | p.glue-headline.glue-headline--headline-5: Google Sans Flex 20px/28px 400, #202124 | = |
| Transition | none | = |
| Icon | 24 x 24, colour #336ef3 | = |
| Painted layers | a.glue-card 616.0x205.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 0px; div.glue-card__inner 616.0x205.0 border T:1px #202124 / R:1px #202124 / B:1px #202124 / L:1px #202124 r 32px; a.glue-card 616.0x205.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 0px; div.glue-card__inner 616.0x205.0 border T:1px #202124 / R:1px #202124 / B:1px #202124 / L:1px #202124 r 32px | = |
| How | at rest | mouse hover |

Crops: `card-default.png`, `card-hover.png`.

#### card-link

Card link. The "Learn more →" link inside a card; measured, never followed.

Page: home. Selector: `card Learn more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 616 x 205 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px | none | #1a73e8 0px 0px 0px 2px | none |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 2px solid #000000 @ 0 offset 0px |
| Font | Google Sans Flex 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1a73e8 | #174ea6 | #174ea6 | #174ea6 |
| Text node | p.glue-headline.glue-headline--headline-5: Google Sans Flex 20px/28px 400, #202124 | = | = | = |
| Transition | box-shadow 0.25s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #336ef3 | = | = | = |
| Painted layers | a.glue-card 616.0x205.0 bg #ffffff r 8px shadow #000000 @ 0 0px 0px 0px 0px; div.glue-card__inner 616.0x205.0 border T:1px #202124 / R:1px #202124 / B:1px #202124 / L:1px #202124 r 32px | a.glue-card 616.0x205.0 bg #ffffff r 8px; div.glue-card__inner 616.0x205.0 border T:1px #202124 / R:1px #202124 / B:1px #202124 / L:1px #202124 r 32px | a.glue-card 616.0x205.0 bg #ffffff r 8px shadow #1a73e8 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px; div.glue-card__inner 616.0x205.0 border T:1px #202124 / R:1px #202124 / B:1px #202124 / L:1px #202124 r 32px | a.glue-card 616.0x205.0 bg #ffffff r 8px outline 2px solid #000000 @ 0 offset 0px; div.glue-card__inner 616.0x205.0 border T:1px #202124 / R:1px #202124 / B:1px #202124 / L:1px #202124 r 32px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-link-default.png`, `card-link-hover.png`, `card-link-focus-visible.png`, `card-link-pressed.png`.

### Footer

#### footer

Footer. The marketing footer: link columns, social marks, legal links and the locale <select>.

Page: home. Selector: `.glue-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 837 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #eff2f7 |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 16px/24px 400 |
| Letter spacing | 0.1px |
| Colour | #202124 |
| Text node | span.glue-footer__site-links-header-text: Google Sans Flex 16px/24px 500, #202124 |
| Transition | none |
| Icon | 0 x 0, colour #202124 |
| Painted layers | footer.glue-footer.glue-spacer-5-top 1440.0x837.0 bg #eff2f7; nav.glue-footer__site-links 1296.0x718.0 border B:1px #dadce0; a.glue-footer__link 194.0x24.0 bg #eff2f7 r 4px; a.glue-footer__link 195.0x24.0 bg #eff2f7 r 4px; a.glue-footer__link 227.2x48.0 bg #eff2f7 r 4px; a.glue-footer__link 98.0x24.0 bg #eff2f7 r 4px |
| Ancestor paint | 1 up body.glue-body bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer link; measured, never followed.

Page: home. Selector: `footer link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 107 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | #eff2f7 | = | = | = |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 5px auto #101010 offset 0px |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3c4043 | = | = | = |
| Transition | background-color, color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.glue-footer__link 107.0x24.0 bg #eff2f7 r 4px | = | a.glue-footer__link 107.0x24.0 bg #eff2f7 r 4px shadow #1a73e8 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a.glue-footer__link 107.0x24.0 bg #eff2f7 r 4px outline 5px auto #101010 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-lang

Locale select. The footer region/language <select>; measured, never changed — its form posts to services.google.com.

Page: home. Selector: `footer select`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 233 x 24 | = | = | = |
| Padding | 0px 24px 0px 2px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #eff2f7 | = | = | = |
| Background image | url(data:…) | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3c4043 | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Painted layers | select.glue-form__dropdown.glue-footer__lang-dropdown 233.0x24.0 bg #eff2f7 image url(data:…) | = | select.glue-form__dropdown.glue-footer__lang-dropdown 233.0x24.0 bg #eff2f7 image url(data:…) outline 1px auto #101010 offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-lang-default.png`, `footer-lang-hover.png`, `footer-lang-focus-visible.png`, `footer-lang-pressed.png`.

### Certificates

#### breadcrumb

Breadcrumb link. The "Grow with Google" link opening the breadcrumb trail above the catalog heading.

Page: certificates. Selector: `breadcrumb link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111.2 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #1a73e8 @ 0.04 | #1a73e8 @ 0.12 | #1a73e8 @ 0.1 |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 5px auto #101010 offset 0px |
| Font | Google Sans Flex 12px/20px 400 | = | = | = |
| Letter spacing | 0.2px | = | = | = |
| Colour | #3186ff | = | = | = |
| Text node | span.anchorText: Google Sans Flex 12px/20px 400, #3186ff, ls 0.2px | = | = | = |
| Transition | background-color, color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | a 111.2x15.0 bg #1a73e8 @ 0.04 r 4px | a 111.2x15.0 bg #1a73e8 @ 0.12 r 4px shadow #1a73e8 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a 111.2x15.0 bg #1a73e8 @ 0.1 r 4px outline 5px auto #101010 offset 0px |

Crops: `breadcrumb-default.png`, `breadcrumb-hover.png`, `breadcrumb-focus-visible.png`, `breadcrumb-pressed.png`.

#### eyebrow

Eyebrow. The "GOOGLE CAREER CERTIFICATES" eyebrow over the page heading.

Page: certificates. Selector: `.glue-eyebrow`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 502.66 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 14px/24px 500 |
| Letter spacing | 0.5px |
| Colour | #202124 |
| Text node | span: Google Sans Flex 14px/24px 500, #202124, ls 0.5px |
| Transition | none |
| How | at rest |

Crops: `eyebrow-default.png`.

#### certs-h1

Certificates headline. "Job-ready skills you can put to work" — the catalog display heading with a coloured first phrase.

Page: certificates. Selector: `certificates h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 502.66 x 112 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 48px/56px 400 |
| Letter spacing | -0.5px |
| Colour | #202124 |
| Text node | span.glue-font-weight-regular: Google Sans Flex 48px/56px 400, #336ef3, ls -0.5px |
| Transition | none |
| How | at rest |

Crops: `certs-h1-default.png`.

#### stat-chip

Stat number. A coloured stat figure in the certificates statistics band (3-6 mos / 70%+ / $102,000+ / 1.7M+ — red, blue, yellow and green numbers over captions).

Page: certificates. Selector: `.bsp-statistics__number`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 276 x 57.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 48px/57.6px 700 |
| Letter spacing | -0.5px |
| Colour | #202124 |
| Text node | span.glue-font-weight-regular: Google Sans Flex 48px/57.6px 400, #c5221f, ls -0.5px |
| Transition | none |
| How | at rest |

Crops: `stat-chip-default.png`.

#### learn-more-btn

Learn more button. The blue pill "Learn more ↓" anchor that scrolls to the catalog; measured, never followed.

Page: certificates. Selector: `Learn more button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 20 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | #1a73e8 @ 0.04 | #1a73e8 @ 0.12 | #1a73e8 @ 0.1 |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 5px auto #101010 offset 0px |
| Font | Google Sans Flex 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #3186ff | = | = | = |
| Text node | span.anchorText: Google Sans Flex 16px/24px 400, #3186ff | = | = | = |
| Transition | background-color, color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a 84.0x20.0 bg #1a73e8 @ 0.04 r 4px | a 84.0x20.0 bg #1a73e8 @ 0.12 r 4px shadow #1a73e8 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a 84.0x20.0 bg #1a73e8 @ 0.1 r 4px outline 5px auto #101010 offset 0px |

Crops: `learn-more-btn-default.png`, `learn-more-btn-hover.png`, `learn-more-btn-focus-visible.png`, `learn-more-btn-pressed.png`.

#### tab-bar

Section tabs. The pill tab bar (Overview / Professional Certificates / Path to jobs / AI training / FAQs) — glue-jumplinks in-page anchors.

Page: certificates. Selector: `.glue-jumplinks__list`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 721 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 120px |
| Background | #ffffff |
| Box shadow | #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px |
| Outline | none |
| Font | Google Sans Flex 16px/24px 400 |
| Letter spacing | 0.1px |
| Colour | #202124 |
| Text node | a.glue-jumplinks__link: Google Sans Flex 16px/20px 500, #3c4043, ls 0.5px |
| Transition | top 0.3s ease |
| Icon | 18 x 18, colour #5f6368 |
| ::before | 20px x 30px, absolute, bg #000000 @ 0 linear-gradient(269deg, #ffffff @ 0, #ffffff 100%), radius 0px |
| ::after | 20px x 30px, absolute, bg #000000 @ 0 linear-gradient(269deg, #ffffff, #ffffff @ 0), radius 0px |
| Painted layers | div.glue-jumplinks.glue-jumplinks--rewind 721.0x48.0 bg #ffffff r 120px shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px; div::before.glue-jumplinks.glue-jumplinks--rewind 20pxx30px image linear-gradient(269deg, #ffffff @ 0, #ffffff 100%); div::after.glue-jumplinks.glue-jumplinks--rewind 20pxx30px image linear-gradient(269deg, #ffffff, #ffffff @ 0); button.glue-jumplinks__button.glue-jumplinks__button--prev 48.0x48.0 bg #ffffff border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 r 50%; button::before.glue-jumplinks__button.glue-jumplinks__button--prev 20pxx48px image linear-gradient(269deg, #ffffff @ 0, #ffffff 100%); a.glue-jumplinks__link 97.0x38.0 border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 |
| How | at rest |

Crops: `tab-bar-default.png`.

#### tab

Tab item. One pill tab in the jumplinks bar; measured, never followed.

Page: certificates. Selector: `.glue-jumplinks__link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 97 x 38 | = | = | = |
| Padding | 7px 8px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | = | = |
| Radius | 0px | = | 4px | = |
| Background | transparent | #f8f9fa | #ffffff | #f1f3f4 |
| Box shadow | none | = | #4285f4 0px 0px 0px 2px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | = |
| Font | Google Sans Flex 16px/20px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #3c4043 | #202124 | #202124 | #202124 |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.glue-jumplinks__link 97.0x38.0 border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 | a.glue-jumplinks__link 97.0x38.0 bg #f8f9fa border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 | a.glue-jumplinks__link 97.0x38.0 bg #ffffff border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 r 4px shadow #4285f4 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a.glue-jumplinks__link 97.0x38.0 bg #f1f3f4 border T:2px #000000 @ 0 / R:2px #000000 @ 0 / B:2px #000000 @ 0 / L:2px #000000 @ 0 |
| Ancestor paint | 3 up div.glue-jumplinks.glue-jumplinks--rewind bg #ffffff shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tab-default.png`, `tab-hover.png`, `tab-focus-visible.png`, `tab-pressed.png`.

#### cert-card

Certificate card. A certificate card in the "Foundational certificates" grid — a glue-grid__col cell painted as a white rounded card on the light-blue band: icon, title, rating, blurb, "If you like:" line and a "Get started on Coursera" pill.

Page: certificates. Selector: `certificate card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 369.75 x 386 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Google Sans Flex 16px/24px 400 | = |
| Letter spacing | 0.1px | = |
| Colour | #202124 | = |
| Text node | h4.glue-headline.glue-headline--headline-4: Google Sans Flex 28px/36px 400, #202124 | = |
| Transition | none | = |
| Painted layers | a.glue-button.glue-button--high-emphasis 248.5x50.0 bg #3186ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px | a 84.0x20.0 bg #1a73e8 @ 0.04 r 4px; a.glue-button.glue-button--high-emphasis 248.5x50.0 bg #3186ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px |
| Ancestor paint | 2 up div.two-column-container-2-10.glue-page bg #ffffff shadow #000000 7px 10px 0px 0px | = |
| How | at rest | mouse hover |

Crops: `cert-card-default.png`, `cert-card-hover.png`.

### Certificate detail

#### cert-hero

Dark hero. The certificate page's dark hero band — an editorial dark section on a light-only site.

Page: cert-ux. Selector: `cert hero`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 720 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #18191d |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 16px/24px 400 |
| Letter spacing | 0.1px |
| Colour | #202124 |
| Text node | span.glue-font-weight-regular: Google Sans Flex 60px/72px 400, #ffffff, ls -0.5px |
| Transition | none |
| Icon | 25.36 x 25.36, colour #ffffff |
| Painted layers | div.page-hero-c.page-hero 1440.0x720.0 bg #18191d; a.glue-button.glue-button--high-emphasis 254.5x50.0 bg #3186ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px |
| How | at rest |

Crops: `cert-hero-default.png`.

#### cert-h1

Certificate headline. "Google UX Design Certificate" — white display type on the dark hero.

Page: cert-ux. Selector: `cert h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 616 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 60px/72px 400 |
| Letter spacing | -0.5px |
| Colour | #ffffff |
| Text node | span.glue-font-weight-regular: Google Sans Flex 60px/72px 400, #ffffff, ls -0.5px |
| Transition | none |
| How | at rest |

Crops: `cert-h1-default.png`.

#### cert-cta

Coursera CTA. The "Get started on Coursera →" button — an outbound enrolment link; its states were measured but it was never followed (no enrolment, no external navigation).

Page: cert-ux. Selector: `cert Coursera CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 254.5 x 50 | = | = | = |
| Padding | 12px 12px 12px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ffffff | = |
| Radius | 48px | = | = | = |
| Background | #3186ff | #185abc | #185abc | #185abc |
| Box shadow | none | #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px | #185abc 0px 0px 0px 2px | #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 2px 6px 2px |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 5px auto #101010 offset 0px |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | none | = |
| Cursor | pointer | = | = | = |
| Icon | 25.36 x 25.36, colour #ffffff | = | = | = |
| Painted layers | a.glue-button.glue-button--high-emphasis 254.5x50.0 bg #3186ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px | a.glue-button.glue-button--high-emphasis 254.5x50.0 bg #185abc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px | a.glue-button.glue-button--high-emphasis 254.5x50.0 bg #185abc border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 48px shadow #185abc 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a.glue-button.glue-button--high-emphasis 254.5x50.0 bg #185abc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 2px 6px 2px outline 5px auto #101010 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cert-cta-default.png`, `cert-cta-hover.png`, `cert-cta-focus-visible.png`, `cert-cta-pressed.png`.

#### badge-card

Graduate badge card. The "GABE — GOOGLE UX DESIGN GRADUATE" overlay card on the hero photo.

Page: cert-ux. Selector: `badge card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 377.91 x 68 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 16px/24px 400 |
| Letter spacing | 0.1px |
| Colour | #3c4043 |
| Transition | none |
| How | at rest |

Crops: `badge-card-default.png`.

#### expansion-panel

Expansion panel. One glue-expansion-panel FAQ row; opened was measured after clicking its header — a local UI toggle.

Page: cert-ux. Selector: `.glue-expansion-panel`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 1296 x 93 | 1296 x 213 |
| Padding | 0px | = |
| Border | T: 1px solid #dadce0; R: none; B: none; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Google Sans Flex 16px/24px 400 | = |
| Letter spacing | 0.1px | = |
| Colour | #202124 | = |
| Text node | span.glue-expansion-panel__header-text: Google Sans Flex 20px/30px 400, #202124 | span.glue-expansion-panel__header-text: Google Sans Flex 20px/30px 400, #000000 |
| Transition | none | = |
| Icon | 36 x 36, colour #202124, fill #1a73e8 | 36 x 36, colour #000000 |
| Painted layers | div.glue-expansion-panel.glue-is-collapsed 1296.0x93.0 border T:1px #dadce0; span.glue-expansion-panel__button.glue-expansion-panel__identifier 1296.0x92.0 border B:1px #000000 @ 0 | div.glue-expansion-panel.glue-is-expanded 1296.0x213.0 border T:1px #dadce0; span.glue-expansion-panel__button.glue-expansion-panel__identifier 1296.0x92.0 border B:2px #174ea6 outline 2px solid #000000 @ 0 offset 0px |
| How | at rest | clicked the expansion-panel header (aria-expanded=true at save) |

Crops: `expansion-panel-default.png`, `expansion-panel-opened.png`.

#### expansion-content

Expansion content. An expanded panel's answer block (1296x120, the .glue-expansion-panel__content of the glue-is-expanded row); measured while the row above was held open.

Page: cert-ux. Selector: `.glue-is-expanded .glue-expansion-panel__content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1296 x 120 |
| Padding | 0px 0px 0px 2px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 16px/24px 400 |
| Letter spacing | 0.1px |
| Colour | #202124 |
| Text node | p: Google Sans Flex 16px/24px 400, #3c4043, ls 0.1px |
| Transition | height 0.2s ease-in |
| How | at rest |

Crops: `expansion-content-default.png`.

### AI training

#### ai-h1

AI page headline. "Essential AI skills for everyone" — the AI training page heading.

Page: ai. Selector: `ai h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 502.67 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 60px/72px 400 |
| Letter spacing | -0.5px |
| Colour | #ffffff |
| Text node | span.glue-font-weight-regular: Google Sans Flex 48px/57.6px 400, #ffffff, ls -0.5px |
| Transition | none |
| Painted layers | span.glue-font-weight-regular 197.5x57.6 image linear-gradient(to right, #3186ff, #7f9cff) r 50px |
| How | at rest |

Crops: `ai-h1-default.png`.

#### ai-card

AI card. A training/course card on the AI page.

Page: ai. Selector: `ai card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1069.33 x 702.25 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Google Sans Flex 16px/24px 400 | = |
| Letter spacing | 0.1px | = |
| Colour | #202124 | = |
| Text node | span.glue-headline--headline-5.glue-headline: Google Sans Flex 20px/28px 400, #202124 | = |
| Transition | none | = |
| Icon | 0 x 0, colour #000000 | = |
| Painted layers | button.glue-carousel__button.glue-carousel__button--prev 0.0x0.0 bg #ffffff r 34px; div.glue-card.glue-carousel__item 340.3x632.3 r 8px shadow #000000 @ 0 0px 0px 0px 0px; div.glue-card.glue-carousel__item 340.3x632.3 r 8px shadow #000000 @ 0 0px 0px 0px 0px; div.glue-card.glue-carousel__item 340.3x632.3 r 8px shadow #000000 @ 0 0px 0px 0px 0px; button.glue-carousel__button.glue-carousel__button--next 0.0x0.0 bg #ffffff r 34px; button::before.glue-carousel__dot.glue-is-active 10pxx10px bg #000000 border T:5px #000000 @ 0 / R:5px #000000 @ 0 / B:5px #000000 @ 0 / L:5px #000000 @ 0 r 50% | button.glue-carousel__button.glue-carousel__button--prev 0.0x0.0 bg #ffffff r 34px; div.glue-card.glue-carousel__item 340.3x632.3 r 8px shadow #000000 @ 0 0px 0px 0px 0px; div.glue-card.glue-carousel__item 340.3x632.3 r 8px shadow #000000 @ 0 0px 0px 0px 0px; button.glue-carousel__button.glue-carousel__button--next 0.0x0.0 bg #ffffff r 34px; button::before.glue-carousel__dot.glue-is-active 10pxx10px bg #000000 border T:5px #000000 @ 0 / R:5px #000000 @ 0 / B:5px #000000 @ 0 / L:5px #000000 @ 0 r 50% |
| How | at rest | mouse hover |

Crops: `ai-card-default.png`, `ai-card-hover.png`.

#### ai-link

AI page CTA. An action on the AI training page; measured, never followed.

Page: ai. Selector: `ai CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 150 x 50 | = | = | = |
| Padding | 12px 12px 12px 16px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ffffff | = |
| Radius | 48px | = | = | = |
| Background | #3186ff | #185abc | #185abc | #185abc |
| Box shadow | none | #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px | #185abc 0px 0px 0px 2px | #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 2px 6px 2px |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 5px auto #101010 offset 0px |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | none | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #ffffff | = | = | = |
| Painted layers | a.glue-button.glue-button--high-emphasis 150.0x50.0 bg #3186ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px | a.glue-button.glue-button--high-emphasis 150.0x50.0 bg #185abc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px | a.glue-button.glue-button--high-emphasis 150.0x50.0 bg #185abc border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 48px shadow #185abc 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a.glue-button.glue-button--high-emphasis 150.0x50.0 bg #185abc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 2px 6px 2px outline 5px auto #101010 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `ai-link-default.png`, `ai-link-hover.png`, `ai-link-focus-visible.png`, `ai-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile top bar. The phone header at 390 wide: wordmark and the drawer toggle.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 362 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 16px/24px 400 |
| Letter spacing | 0.1px |
| Colour | #202124 |
| Text node | p.glue-header__skip-content-text: Google Sans Flex 16px/24px 500, #3c4043, ls 0.25px |
| Transition | none |
| Icon | 24 x 24, colour #5f6368 |
| Painted layers | header.nav_v1.custome_nav 362.0x64.0 bg #ffffff; div.glue-header__bar.glue-header__bar--mobile 390.0x64.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px; div.glue-header__bar.glue-header__bar--desktop 390.0x844.0 bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px; hr.xl-lg-view-only 0.0x0.0 border T:1px #dadce0; hr.xl-lg-view-only 0.0x0.0 border T:1px #dadce0; hr.xl-lg-view-only 0.0x0.0 border T:1px #dadce0 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hero-h1

Mobile hero headline. The home display heading at 390 wide.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 334 x 64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Google Sans Flex 24px/32px 400 |
| Letter spacing | normal |
| Colour | #202124 |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-hero-cta

Mobile hero CTA. The hero action at 390 wide; measured, never followed.

Page: mobile. Selector: `mobile hero CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 142.5 x 50 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | 1px solid #ffffff | = |
| Radius | 48px | = | = | = |
| Background | #3186ff | #185abc | #185abc | #185abc |
| Box shadow | none | #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px | #185abc 0px 0px 0px 2px | #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 2px 6px 2px |
| Outline | none | = | 2px solid #000000 @ 0 offset 1px | 5px auto #e59700 offset 0px |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | none | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.glue-button.glue-button--high-emphasis 142.5x50.0 bg #3186ff border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px | a.glue-button.glue-button--high-emphasis 142.5x50.0 bg #185abc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 1px 3px 1px | a.glue-button.glue-button--high-emphasis 142.5x50.0 bg #185abc border T:1px #ffffff / R:1px #ffffff / B:1px #ffffff / L:1px #ffffff r 48px shadow #185abc 0px 0px 0px 2px outline 2px solid #000000 @ 0 offset 1px | a.glue-button.glue-button--high-emphasis 142.5x50.0 bg #185abc border T:1px #000000 @ 0 / R:1px #000000 @ 0 / B:1px #000000 @ 0 / L:1px #000000 @ 0 r 48px shadow #3c4043 @ 0.3 0px 1px 2px 0px, #3c4043 @ 0.15 0px 2px 6px 2px outline 5px auto #e59700 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-hero-cta-default.png`, `m-hero-cta-hover.png`, `m-hero-cta-focus-visible.png`, `m-hero-cta-pressed.png`.

#### m-drawer-btn

Drawer toggle. The header button that opens the navigation drawer at 390 wide; opened was measured after tapping it — a local UI toggle.

Page: mobile. Selector: `mobile drawer button`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 4px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | Google Sans Flex 16px/normal 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #5f6368 | = | = | = | = |
| Transition | none | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 24 x 24, colour #5f6368 | = | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | tapped the drawer button to open the navigation drawer (aria-expanded=true at save) |

Crops: `m-drawer-btn-default.png`, `m-drawer-btn-hover.png`, `m-drawer-btn-focus-visible.png`, `m-drawer-btn-pressed.png`, `m-drawer-btn-opened.png`.

#### m-drawer-link

Drawer link. A link inside the opened navigation drawer (Career Certificates, 326x50); measured while the drawer was held open, never followed.

Page: mobile. Selector: `.glue-header__drawer--is-open a.glue-header__link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 326 x 50 | = | = | = |
| Padding | 13px 16px 13px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px 100px 100px 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #1a73e8 0px 0px 0px 2px | #000000 @ 0 0px 0px 0px 1px |
| Outline | none | = | = | = |
| Font | Google Sans Flex 16px/24px 500 | = | = | = |
| Letter spacing | 0.25px | = | = | = |
| Colour | #3c4043 | = | #3186ff | #3186ff |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #3c4043 | = | 18 x 18, colour #3186ff | 18 x 18, colour #3186ff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.glue-header__link 326.0x50.0 r 4px 100px 100px 4px shadow #1a73e8 0px 0px 0px 2px | a.glue-header__link 326.0x50.0 r 4px 100px 100px 4px shadow #000000 @ 0 0px 0px 0px 1px |

Crops: `m-drawer-link-default.png`, `m-drawer-link-hover.png`, `m-drawer-link-focus-visible.png`, `m-drawer-link-pressed.png`.

#### m-skip-link

Skip link. The "Jump to Content" skip link — parked off-canvas at y -999, revealed at 39,8 (160x48) by keyboard focus; hover does not apply to a hidden element.

Page: mobile. Selector: `.glue-header__skip-content`. States: default, focus-visible, pressed.

| Property | default | focus-visible | pressed |
|---|---|---|---|
| Size (w x h) | 134.75 x 48 | 160 x 48 | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 4px 100px 100px 4px | 4px | = |
| Background | transparent | #f8f9fa | = |
| Box shadow | none | #1a73e8 0px 0px 0px 2px | #000000 @ 0 0px 0px 0px 1px |
| Outline | none | = | = |
| Font | Google Sans Flex 16px/24px 500 | = | = |
| Letter spacing | 0.25px | = | = |
| Colour | #3c4043 | #3186ff | = |
| Text node | p.glue-header__skip-content-text: Google Sans Flex 16px/24px 500, #3c4043, ls 0.25px | p.glue-header__skip-content-text: Google Sans Flex 16px/24px 500, #3186ff, ls 0.25px | = |
| Transition | background-color, box-shadow, color 0.2s, 0.2s, 0.2s ease, ease, ease delay 0s, 0s, 0s | = | = |
| Cursor | pointer | = | = |
| How | at rest | keydown then focus() | CDP forcePseudoState :active:hover |
| Painted layers | - | a.glue-header__link.glue-header__skip-content 160.0x48.0 bg #f8f9fa r 4px shadow #1a73e8 0px 0px 0px 2px | a.glue-header__link.glue-header__skip-content 134.8x48.0 r 4px 100px 100px 4px shadow #000000 @ 0 0px 0px 0px 1px |

Crops: `m-skip-link-default.png`, `m-skip-link-focus-visible.png`, `m-skip-link-pressed.png`.

## Transitions declared in the readable stylesheets

grow.google's gstatic marketing-cms bundle is cross-origin to the CSSOM, so this list holds only what the same-origin-readable sheets (inline blocks) declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints, including the bundle's.

- ai: none

- cert-ux: none

- certificates: none

- home: none

## Reduced motion

- home (`.glue-header a, .glue-btn` under prefers-reduced-motion): transition `background-color 0.2s, box-shadow 0.2s, color 0.2s`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
