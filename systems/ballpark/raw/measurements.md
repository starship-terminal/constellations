# Component measurements

Computed styles read from ballparkhq.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme (no consent overlay mounts on these routes), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The two-row bar under the announcement strip: logo, the nav (Platform, Solutions, Templates, Pricing), Sign in and the black Book a demo pill.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 156 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px 0px 16px 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-1f64xwd: IBM Plex Mono 11px/16.5px 600, #ffffff, ls 1.65px |
| Transition | none |
| Icon | 13 x 13, colour #0000ee, fill #000000 |
| Painted layers | header.framer-rMAWK.framer-nZWxi 1392.0x156.0 bg #ffffff r 0px 0px 16px 16px; a.framer-UBFC0.framer-jrDdx 1280.0x56.0 bg #f9fafb r 0px 0px 16px 16px; div.framer-vpvGg.framer-nZWxi 44.8x26.0 bg #e8704e r 100px; a.framer-S1C7R.framer-vTRZK 84.1x36.0 bg #ffffff r 7px; a.framer-S1C7R.framer-vTRZK 90.0x36.0 bg #ffffff r 7px; a.framer-PSt6z.framer-vTRZK 97.0x36.0 bg #ffffff r 7px |
| How | at rest |

Crops: `header-default.png`.

#### announcement-bar

Announcement bar. The "NEW · Ballpark is now available in Claude" banner over the header: a centred pill link with a coral NEW chip. Measured, never followed.

Page: home. Selector: `a[href*="claude"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1280 x 56 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px 0px 16px 16px | = | = | = |
| Background | #f9fafb | #f3f4f6 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1f64xwd: IBM Plex Mono 11px/16.5px 600, #ffffff, ls 1.65px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13 x 13, colour #0000ee, fill #000000 | = | = | 13 x 13, colour #ff0000, fill #000000 |
| Painted layers | a.framer-UBFC0.framer-jrDdx 1280.0x56.0 bg #f9fafb r 0px 0px 16px 16px; div.framer-vpvGg.framer-nZWxi 44.8x26.0 bg #e8704e r 100px | a.framer-UBFC0.framer-jrDdx 1280.0x56.0 bg #f3f4f6 r 0px 0px 16px 16px; div.framer-vpvGg.framer-nZWxi 44.8x26.0 bg #e8704e r 100px | a.framer-UBFC0.framer-jrDdx 1280.0x56.0 bg #f9fafb r 0px 0px 16px 16px outline 1px auto #005fcc offset 1px; div.framer-vpvGg.framer-nZWxi 44.8x26.0 bg #e8704e r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `announcement-bar-default.png`, `announcement-bar-hover.png`, `announcement-bar-focus-visible.png`, `announcement-bar-pressed.png`.

#### nav-link

Nav link.

Page: home. Selector: `a:has-text("Platform")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84.08 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #ffffff | #f3f4f6 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-121aysi: Inter 14px/20px 600, #111827, ls -0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-S1C7R.framer-vTRZK 84.1x36.0 bg #ffffff r 7px | a.framer-S1C7R.framer-vTRZK 84.1x36.0 bg #f3f4f6 r 7px | a.framer-S1C7R.framer-vTRZK 84.1x36.0 bg #ffffff r 7px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-solutions

Solutions menu link. The nav item that opens the mega menu of solutions pages on hover.

Page: home. Selector: `a:has-text("Solutions")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 90 x 36 | = | - | = |
| Padding | 0px 14px | = | - | = |
| Gap | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 7px | = | - | = |
| Background | #ffffff | #f3f4f6 | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sans-serif 12px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | p.framer-text.framer-styles-preset-121aysi: Inter 14px/20px 600, #111827, ls -0.14px | = | - | = |
| Transition | none | = | - | = |
| Painted layers | a.framer-S1C7R.framer-vTRZK 90.0x36.0 bg #ffffff r 7px | a.framer-S1C7R.framer-vTRZK 90.0x36.0 bg #f3f4f6 r 7px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-solutions-default.png`, `nav-solutions-hover.png`, `nav-solutions-pressed.png`.

#### nav-solutions-open

Solutions menu, open. The link after its own hover opens the menu; the crop holds the opened panel region.

Page: home. Selector: `a:has-text("Solutions")`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 90 x 36 |
| Padding | 0px 14px |
| Gap | 0px |
| Border | none |
| Radius | 7px |
| Background | #f3f4f6 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-121aysi: Inter 14px/20px 600, #111827, ls -0.14px |
| Transition | none |
| Painted layers | a.framer-S1C7R.framer-vTRZK 90.0x36.0 bg #f3f4f6 r 7px |
| How | menu held open by opts.open |

Crops: `nav-solutions-open-opened.png`.

#### nav-signin

Sign in link. The secondary action on the right of the nav. Measured, never followed.

Page: home. Selector: `a:has-text("Sign in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 72.88 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #ffffff | #f9fafb | = | = |
| Box shadow | #ffffff @ 0 0px 0px 0px 0px, #4b5563 @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 2px 2px 0px | #ffffff @ 0 0px 0px 0px 0px, #4b5563 @ 0.4 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter 14px/20px 600, #111827, ls -0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 72.875px x 36px, absolute, bg #000000 @ 0, radius 7px | = | = | = |
| Painted layers | a.framer-Z8GqO.framer-yuus7z 72.9x36.0 bg #ffffff r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #4b5563 @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 2px 2px 0px | a.framer-Z8GqO.framer-yuus7z 72.9x36.0 bg #f9fafb r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #4b5563 @ 0.4 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px | a.framer-Z8GqO.framer-yuus7z 72.9x36.0 bg #ffffff r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #4b5563 @ 0.2 0px 0px 0px 1px, #000000 @ 0.06 0px 2px 2px 0px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Book a demo button. The black pill on the right of the nav. Measured, never followed.

Page: home. Selector: `a:has-text("Book a demo")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139.95 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #111827 | #1f2937 | = | = |
| Box shadow | #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter 14px/20px 600, #f9fafb, ls -0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13 x 13, colour #0000ee, fill #000000 | = | = | 13 x 13, colour #ff0000, fill #000000 |
| ::after | 139.953px x 36px, absolute, bg #000000 @ 0, radius 7px | = | = | = |
| Painted layers | a.framer-Z8GqO.framer-yuus7z 140.0x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | a.framer-Z8GqO.framer-yuus7z 140.0x36.0 bg #1f2937 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | a.framer-Z8GqO.framer-yuus7z 140.0x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

#### intercom-launcher

Intercom launcher. The round chat bubble Intercom mounts at the bottom-right of every page (third-party widget).

Page: home. Selector: `div[role="button"][aria-label*="Intercom"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | 52.8 x 52.8 | = | 40.8 x 40.8 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | #0071b2 | = | = | = |
| Box shadow | #000000 @ 0.06 0px 1px 6px 0px, #000000 @ 0.16 0px 2px 32px 0px | = | #38373e 0px 0px 0px 5px inset | = |
| Outline | none | = | = | = |
| Font | system-ui 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | transform 0.167s cubic-bezier(0.33, 0, 0, 1) | transform 0.25s cubic-bezier(0.33, 0, 0, 1) | = | transform 0.134s cubic-bezier(0.45, 0, 0.2, 1) |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 | 26.4 x 26.4, colour #000000 | = | 20.4 x 20.4, colour #000000 |
| Painted layers | div.intercom-lightweight-app-launcher.intercom-launcher 48.0x48.0 bg #0071b2 r 50% shadow #000000 @ 0.06 0px 1px 6px 0px, #000000 @ 0.16 0px 2px 32px 0px | div.intercom-lightweight-app-launcher.intercom-launcher 52.8x52.8 bg #0071b2 r 50% shadow #000000 @ 0.06 0px 1px 6px 0px, #000000 @ 0.16 0px 2px 32px 0px | div.intercom-lightweight-app-launcher.intercom-launcher 48.0x48.0 bg #0071b2 r 50% shadow #38373e 0px 0px 0px 5px inset | div.intercom-lightweight-app-launcher.intercom-launcher 40.8x40.8 bg #0071b2 r 50% shadow #000000 @ 0.06 0px 1px 6px 0px, #000000 @ 0.16 0px 2px 32px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.1, 0, 0, 1.1, 0, 0) | = | matrix(0.85, 0, 0, 0.85, 0, 0) |

Crops: `intercom-launcher-default.png`, `intercom-launcher-hover.png`, `intercom-launcher-focus-visible.png`, `intercom-launcher-pressed.png`.

#### logo

Logo.

Page: home. Selector: `header a:has-text("Ballpark")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 96 x 26 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Text node | p.framer-text.framer-styles-preset-12yaez7: Inter 14px/20px 400, #111827, ls -0.14px |
| Transition | none |
| Cursor | pointer |
| Icon | 96 x 26, colour #0000ee, fill #000000 |
| How | at rest |

Crops: `logo-default.png`.

### Home

#### hero-title

Hero title. "Research without the complexity" in the site's display face (Inter Display).

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 850 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 96px/96px 800 |
| Letter spacing | -3.36px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subcopy.

Page: home. Selector: `first long paragraph under h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 670 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-11rrpbt: Inter 20px/30px 400, #4b5563, ls -0.4px |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### section-title

Section title.

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 590 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 42px/42px 700 |
| Letter spacing | -1.26px |
| Colour | #111827 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### feature-card

Feature card. A tall image card linking a feature page (live interviews, creative testing, …). Measured, never followed.

Page: home. Selector: `a[href*="features/"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 366.67 x 600 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.04 0px 0.597144px 0.597144px -0.9375px, #000000 @ 0.04 0px 1.81088px 1.81088px -1.875px, #000000 @ 0.04 0px 4.78699px 4.78699px -2.8125px, #000000 @ 0.02 0px 15px 15px -3.75px, #4b5563 @ 0.1 0px 0px 0px 1px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1v68qu7: Inter 12px/16px 700, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.framer-10f1fwn.framer-xutp51 366.7x600.0 bg #ffffff r 16px shadow #000000 @ 0.04 0px 0.597144px 0.597144px -0.9375px, #000000 @ 0.04 0px 1.81088px 1.81088px -1.875px, #000000 @ 0.04 0px 4.78699px 4.78699px -2.8125px, #000000 @ 0.02 0px 15px 15px -3.75px, #4b5563 @ 0.1 0px 0px 0px 1px; div.framer-Ht8Si.framer-9eiQp 53.0x24.0 bg #dc2626 r 100px; div::after.framer-Ht8Si.framer-9eiQp 53.0469pxx24px border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 100px; div.framer-x21wra 10.0x10.0 bg #ffffff r 100px shadow #ffffff 0px 0px 0px 1px; div::after.framer-x21wra 10pxx10px border T:2px solid #dc2626 / R:2px solid #dc2626 / B:2px solid #dc2626 / L:2px solid #dc2626 r 100px; div.framer-gbkgzl 100.0x108.0 bg #ffffff r 8px shadow #000000 @ 0.2 0px 3px 10px 0px, #000000 @ 0.1 0px 0px 0px 1px | = | a.framer-10f1fwn.framer-xutp51 366.7x600.0 bg #ffffff r 16px shadow #000000 @ 0.04 0px 0.597144px 0.597144px -0.9375px, #000000 @ 0.04 0px 1.81088px 1.81088px -1.875px, #000000 @ 0.04 0px 4.78699px 4.78699px -2.8125px, #000000 @ 0.02 0px 15px 15px -3.75px, #4b5563 @ 0.1 0px 0px 0px 1px outline 1px auto #005fcc offset 1px; div.framer-Ht8Si.framer-9eiQp 53.0x24.0 bg #dc2626 r 100px; div::after.framer-Ht8Si.framer-9eiQp 53.0469pxx24px border T:1px solid #000000 @ 0.1 / R:1px solid #000000 @ 0.1 / B:1px solid #000000 @ 0.1 / L:1px solid #000000 @ 0.1 r 100px; div.framer-x21wra 10.0x10.0 bg #ffffff r 100px shadow #ffffff 0px 0px 0px 1px; div::after.framer-x21wra 10pxx10px border T:2px solid #dc2626 / R:2px solid #dc2626 / B:2px solid #dc2626 / L:2px solid #dc2626 r 100px; div.framer-gbkgzl 100.0x108.0 bg #ffffff r 8px shadow #000000 @ 0.2 0px 3px 10px 0px, #000000 @ 0.1 0px 0px 0px 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `feature-card-default.png`, `feature-card-hover.png`, `feature-card-focus-visible.png`, `feature-card-pressed.png`.

#### cta-request

Request a demo button. The closing CTA over the footer ("Try Ballpark with your team"). Measured, never followed.

Page: home. Selector: `a:has-text("Request a demo")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160.73 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #111827 | #1f2937 | = | = |
| Box shadow | #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter 14px/20px 600, #f9fafb, ls -0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13 x 13, colour #0000ee, fill #000000 | = | = | 13 x 13, colour #ff0000, fill #000000 |
| ::after | 160.734px x 36px, absolute, bg #000000 @ 0, radius 7px | = | = | = |
| Painted layers | a.framer-Z8GqO.framer-yuus7z 160.7x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | a.framer-Z8GqO.framer-yuus7z 160.7x36.0 bg #1f2937 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | a.framer-Z8GqO.framer-yuus7z 160.7x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `cta-request-default.png`, `cta-request-hover.png`, `cta-request-focus-visible.png`, `cta-request-pressed.png`.

#### carousel-dot

Carousel page dot. The pagination dots of the stories carousel ("Scroll to page 1"…).

Page: home. Selector: `button:has-text("Scroll to page")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 19 x 24 | = | = | = |
| Padding | 8px 3px 8px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | div 8.0x8.0 bg #ffffff r 50% | = | button 19.0x24.0 outline 1px auto #005fcc offset 0px; div 8.0x8.0 bg #ffffff r 50% | = |
| Ancestor paint | 1 up div bg #ffffff @ 0.2 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `carousel-dot-default.png`, `carousel-dot-hover.png`, `carousel-dot-focus-visible.png`, `carousel-dot-pressed.png`.

#### coach-widget

Coach demo widget. The working "Ask Coach" demo box on the home page: the product's chat UI with an "Ask me anything…" field and a round submit.

Page: home. Selector: `Coach box (marked in-page)`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 320 x 560 | = |
| Padding | 0px | = |
| Gap | 0px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | #000000 @ 0.07 0px 0.602187px 0.602187px -1.25px, #000000 @ 0.06 0px 2.28853px 2.28853px -2.5px, #000000 @ 0.03 0px 10px 10px -3.75px, #000000 @ 0.2 0px 20px 40px -15px, #4b5563 @ 0.1 0px 0px 0px 1px, #000000 @ 0.03 0px 0px 0px 5px | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | p.framer-text.framer-styles-preset-121aysi: Inter 14px/20px 600, #111827, ls -0.14px | = |
| Transition | none | = |
| Icon | 30 x 24, colour #000000 | 10 x 10, colour #000000 |
| Painted layers | div.framer-oxdq0j.hidden-f7oyih 320.0x560.0 r 16px shadow #000000 @ 0.07 0px 0.602187px 0.602187px -1.25px, #000000 @ 0.06 0px 2.28853px 2.28853px -2.5px, #000000 @ 0.03 0px 10px 10px -3.75px, #000000 @ 0.2 0px 20px 40px -15px, #4b5563 @ 0.1 0px 0px 0px 1px, #000000 @ 0.03 0px 0px 0px 5px; div.framer-Mw1Zu.framer-vTRZK 320.0x560.0 bg #f9fafb r 0px 12px 0px 0px; div.framer-tap5oe 320.0x50.0 bg #ffffff @ 0.85 shadow #4b5563 @ 0.1 0px 1px 0px 0px; div.framer-1jn6nqz 48.0x48.0 bg #fca5a5 r 100px; div.framer-5tv6xb 280.0x100.0 bg #ffffff r 6px shadow #ffffff 0px 0px 0px 0px, #9ca3af @ 0.25 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px; div::after.framer-5tv6xb 280pxx100px border T:1px solid #111827 / R:1px solid #111827 / B:1px solid #111827 / L:1px solid #111827 r 6px | div.framer-oxdq0j.hidden-f7oyih 320.0x560.0 r 16px shadow #000000 @ 0.07 0px 0.602187px 0.602187px -1.25px, #000000 @ 0.06 0px 2.28853px 2.28853px -2.5px, #000000 @ 0.03 0px 10px 10px -3.75px, #000000 @ 0.2 0px 20px 40px -15px, #4b5563 @ 0.1 0px 0px 0px 1px, #000000 @ 0.03 0px 0px 0px 5px; div.framer-Mw1Zu.framer-vTRZK 320.0x560.0 bg #f9fafb r 0px 12px 0px 0px; div.framer-tap5oe 320.0x50.0 bg #ffffff @ 0.85 shadow #4b5563 @ 0.1 0px 1px 0px 0px; div.framer-j5pe2e 228.0x81.0 bg #e5e7eb @ 0.5 r 12px; div.framer-5tv6xb 280.0x100.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px; div::after.framer-5tv6xb 280pxx100px border T:1px solid #4b5563 @ 0.2 / R:1px solid #4b5563 @ 0.2 / B:1px solid #4b5563 @ 0.2 / L:1px solid #4b5563 @ 0.2 r 6px |
| Ancestor paint | 2 up div.framer-v8hx28 bg #ffffff shadow #000000 @ 0.07 0px 0.602187px 0.602187px -1.25px, #000000 @ 0.06 0px 2.28853px 2.28853px -2.5px, #000000 @ 0.03 0px 10px 10px -3.75px, #000000 @ 0.2 0px 20px 40px -15px, #4b5563 @ 0.1 0px 0px 0px 1px, #000000 @ 0.03 0px 0px 0px 5px | = |
| How | at rest | mouse hover |

Crops: `coach-widget-default.png`, `coach-widget-hover.png`.

#### coach-field

Coach ask field. The demo's ask field. The box paints a fake field (a Framer div, not an input or textarea), so the entry is recorded missing when the sweep finds no real input.

Page: home. Selector: `input inside the Coach box`. States: .

Not found on the page at capture time.

#### coach-submit

Coach send button. The round send button inside the demo. Measured, never pressed.

Page: home. Selector: `button:has-text("Submit")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #e5e7eb | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.framer-text.framer-styles-preset-18la29v: Inter 10px/14px 400, #111827 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 10, colour #000000 | = | = | = |
| Painted layers | button.framer-oSb0X.framer-Ihna6 24.0x24.0 bg #e5e7eb r 6px | = | button.framer-oSb0X.framer-Ihna6 24.0x24.0 bg #e5e7eb r 6px outline 1px auto #005fcc offset 0px | = |
| Ancestor paint | 2 up div.framer-5tv6xb bg #ffffff shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `coach-submit-default.png`, `coach-submit-hover.png`, `coach-submit-focus-visible.png`, `coach-submit-pressed.png`.

### Pricing

#### pricing-title

Pricing title.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 850 x 192 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 96px/96px 800 |
| Letter spacing | -3.36px |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-cta

Plan CTA. The action inside an enterprise plan card. Measured, never followed.

Page: pricing. Selector: `a:has-text("demo/trial") inside a plan card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 320 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #111827 | #1f2937 | = | = |
| Box shadow | #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter 14px/20px 600, #f9fafb, ls -0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13 x 13, colour #0000ee, fill #000000 | = | = | 13 x 13, colour #ff0000, fill #000000 |
| ::after | 320px x 36px, absolute, bg #000000 @ 0, radius 7px | = | = | = |
| Painted layers | a.framer-Z8GqO.framer-yuus7z 320.0x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | a.framer-Z8GqO.framer-yuus7z 320.0x36.0 bg #1f2937 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | a.framer-Z8GqO.framer-yuus7z 320.0x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-card

Plan card.

Page: pricing. Selector: `card ancestor of a plan CTA (marked in-page)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 594.39 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 24px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.01 0px 0.839802px 0.839802px -0.125px, #000000 @ 0.01 0px 1.99048px 1.99048px -0.25px, #000000 @ 0.01 0px 3.63084px 3.63084px -0.375px, #000000 @ 0.01 0px 6.03627px 6.03627px -0.5px, #000000 @ 0.02 0px 9.74808px 9.74808px -0.625px, #000000 @ 0.02 0px 15.9566px 15.9566px -0.75px, #000000 @ 0.03 0px 27.4762px 27.4762px -0.875px, #000000 @ 0.04 0px 50px 50px -1px, #4b5563 @ 0.2 0px 0px 0px 0.5px |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h6.framer-text.framer-styles-preset-7mbi4u: Inter Display 22px/30.8px 600, #111827, ls -0.22px |
| Transition | none |
| Icon | 32 x 32, colour #4b5563 |
| Painted layers | div.framer-pu963d 384.0x594.4 bg #ffffff r 24px shadow #000000 @ 0.01 0px 0.839802px 0.839802px -0.125px, #000000 @ 0.01 0px 1.99048px 1.99048px -0.25px, #000000 @ 0.01 0px 3.63084px 3.63084px -0.375px, #000000 @ 0.01 0px 6.03627px 6.03627px -0.5px, #000000 @ 0.02 0px 9.74808px 9.74808px -0.625px, #000000 @ 0.02 0px 15.9566px 15.9566px -0.75px, #000000 @ 0.03 0px 27.4762px 27.4762px -0.875px, #000000 @ 0.04 0px 50px 50px -1px, #4b5563 @ 0.2 0px 0px 0px 0.5px; div.framer-eaobqe 384.0x256.4 image linear-gradient(#f9fafb 0%, #ffffff 100%) shadow #ffffff 0px 1px 0px 0px inset; div.framer-snkvbt 56.0x56.0 bg #ffffff r 16px shadow #000000 @ 0.18 0px 0.602187px 0.602187px -1.25px, #000000 @ 0.16 0px 2.28853px 2.28853px -2.5px, #000000 @ 0.06 0px 10px 10px -3.75px, #4b5563 @ 0.1 0px 0px 0px 0.5px; a.framer-Z8GqO.framer-yuus7z 320.0x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.framer-GylQJ.framer-9uoaq1 288.0x1.0 bg #4b5563 @ 0.1; div.framer-GylQJ.framer-9uoaq1 288.0x1.0 bg #4b5563 @ 0.1 |
| How | at rest |

Crops: `plan-card-default.png`.

### Contact sales

#### contact-title

Contact title.

Page: contact. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 489.5 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter Display 42px/42px 700 |
| Letter spacing | -1.26px |
| Colour | #111827 |
| Transition | none |
| How | at rest |

Crops: `contact-title-default.png`.

#### contact-field

Contact field. A short text field of the sales form (first/last name pair); sample text was typed and deleted, nothing sent.

Page: contact. Selector: `input[type=text]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 204.75 x 19.59 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Inter 14px/19.6px 400 | = | = |
| Letter spacing | -0.14px | = | = |
| Colour | #111827 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #6b7280, opacity 1 | = | = |
| Ancestor paint | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #ffffff shadow #000000 @ 0.25 0px 0px 0px 0px, #000000 @ 0.25 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #ffffff shadow #ffffff @ 0.25 0px 0px 0px 0px, #d0d5db 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #ffffff shadow #ffffff @ 0.25 0px 0px 0px 0px, #d0d5db 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `contact-field-default.png`, `contact-field-focused.png`, `contact-field-filled.png`.

#### contact-email

Contact email field. The wider field under the name pair (work email); focused only, nothing typed.

Page: contact. Selector: `wide input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 465.5 x 19.59 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/19.6px 400 | = |
| Letter spacing | -0.14px | = |
| Colour | #111827 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #6b7280, opacity 1 | = |
| Ancestor paint | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #ffffff shadow #000000 @ 0.25 0px 0px 0px 0px, #000000 @ 0.25 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #ffffff shadow #ffffff @ 0.25 0px 0px 0px 0px, #d0d5db 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field |

Crops: `contact-email-default.png`, `contact-email-focused.png`.

#### contact-message

Message textarea. The form's message box; focused only, nothing typed.

Page: contact. Selector: `textarea`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 489.5 x 136 | = |
| Padding | 10px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/19.6px 400 | = |
| Letter spacing | -0.14px | = |
| Colour | #111827 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #6b7280, opacity 1 | = |
| Ancestor paint | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #ffffff shadow #000000 @ 0.25 0px 0px 0px 0px, #000000 @ 0.25 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | 1 up div.framer-form-text-input.framer-form-input-wrapper bg #ffffff shadow #ffffff @ 0.25 0px 0px 0px 0px, #d0d5db 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field |

Crops: `contact-message-default.png`, `contact-message-focused.png`.

#### contact-submit

Submit request button. The form's black submit. Measured, never pressed.

Page: contact. Selector: `button:has-text("Submit request")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 489.5 x 40 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #111827 | #1f2937 | = | = |
| Box shadow | #ffffff 0px 0px 0px 0px, #111827 0px 0px 0px 0px, #000000 @ 0.06 0px 2px 3px 0px, #000000 @ 0.06 0px 1px 2px -1px | #ffffff 0px 0px 0px 0px, #1f2937 0px 0px 0px 0px, #000000 @ 0.06 0px 2px 3px 0px, #000000 @ 0.06 0px 1px 2px -1px | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | p.framer-text.framer-styles-preset-121aysi: Inter 14px/20px 600, #ffffff, ls -0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 489.5px x 40px, absolute, bg #000000 @ 0, radius 6px | = | = | = |
| Painted layers | button.framer-Sgwjm.framer-vTRZK 489.5x40.0 bg #111827 r 6px shadow #ffffff 0px 0px 0px 0px, #111827 0px 0px 0px 0px, #000000 @ 0.06 0px 2px 3px 0px, #000000 @ 0.06 0px 1px 2px -1px; button::after.framer-Sgwjm.framer-vTRZK 489.5pxx40px border T:1px solid #e4e6eb @ 0 / R:1px solid #e4e6eb @ 0 / B:1px solid #e4e6eb @ 0 / L:1px solid #e4e6eb @ 0 r 6px | button.framer-Sgwjm.framer-vTRZK 489.5x40.0 bg #1f2937 r 6px shadow #ffffff 0px 0px 0px 0px, #1f2937 0px 0px 0px 0px, #000000 @ 0.06 0px 2px 3px 0px, #000000 @ 0.06 0px 1px 2px -1px; button::after.framer-Sgwjm.framer-vTRZK 489.5pxx40px border T:1px solid #e4e6eb @ 0 / R:1px solid #e4e6eb @ 0 / B:1px solid #e4e6eb @ 0 / L:1px solid #e4e6eb @ 0 r 6px | button.framer-Sgwjm.framer-vTRZK 489.5x40.0 bg #111827 r 6px shadow #ffffff 0px 0px 0px 0px, #111827 0px 0px 0px 0px, #000000 @ 0.06 0px 2px 3px 0px, #000000 @ 0.06 0px 1px 2px -1px outline 1px auto #005fcc offset 0px; button::after.framer-Sgwjm.framer-vTRZK 489.5pxx40px border T:1px solid #e4e6eb @ 0 / R:1px solid #e4e6eb @ 0 / B:1px solid #e4e6eb @ 0 / L:1px solid #e4e6eb @ 0 r 6px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `contact-submit-default.png`, `contact-submit-hover.png`, `contact-submit-focus-visible.png`, `contact-submit-pressed.png`.

### Sign in

#### signin-title

Sign-in title.

Page: signin. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 169.77 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 20px/28px 600 |
| Letter spacing | -0.2px |
| Colour | #101828 |
| Transition | none |
| How | at rest |

Crops: `signin-title-default.png`.

#### signin-google

Continue with Google. The OAuth link. Measured, never followed — no sign-in was attempted.

Page: signin. Selector: `a:has-text("Continue with Google")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | = |
| Padding | 0px 16px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | #f9fafb | = | #f3f4f6 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.4 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.25 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #101828 | = | = | = |
| Transition | background-color, border-color, box-shadow, color, opacity, transform 0.3s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #101828 | = | = | = |
| Painted layers | a.appearance-none.border-0 384.0x36.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px | a.appearance-none.border-0 384.0x36.0 bg #f9fafb r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.4 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | a.appearance-none.border-0 384.0x36.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px | a.appearance-none.border-0 384.0x36.0 bg #f3f4f6 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.25 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-google-default.png`, `signin-google-hover.png`, `signin-google-focus-visible.png`, `signin-google-pressed.png`.

#### signin-sso

Continue with SSO. The SSO link. Measured, never followed.

Page: signin. Selector: `a:has-text("Continue with SSO")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | = |
| Padding | 0px 16px 0px 14px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #ffffff | #f9fafb | = | #f3f4f6 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.4 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.25 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #101828 | = | = | = |
| Transition | background-color, border-color, box-shadow, color, opacity, transform 0.3s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #101828 | = | = | = |
| Painted layers | a.appearance-none.border-0 384.0x36.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.2 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px | a.appearance-none.border-0 384.0x36.0 bg #f9fafb r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.4 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | a.appearance-none.border-0 384.0x36.0 bg #ffffff r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px | a.appearance-none.border-0 384.0x36.0 bg #f3f4f6 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #4a5565 @ 0.25 0px 0px 0px 1px, #000000 @ 0.05 0px 2px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-sso-default.png`, `signin-sso-hover.png`, `signin-sso-focus-visible.png`, `signin-sso-pressed.png`.

#### signin-field

Email field. The sign-in email field; sample text was typed and deleted, nothing sent.

Page: signin. Selector: `input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 384 x 38 | = | = |
| Padding | 0px 12px | = | = |
| Border | 1px solid #4a5565 @ 0.2 | 1px solid #4a5565 | 1px solid #4a5565 |
| Radius | 6px | = | = |
| Background | #ffffff | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d1d5dc 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d1d5dc 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = | = |
| Font | Inter 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #101828 | = | = |
| Transition | background-color, border-color, box-shadow, color, opacity, transform 0.3s cubic-bezier(0.23, 1, 0.32, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #6a7282, opacity 1 | = | = |
| Painted layers | input.appearance-none.block 384.0x38.0 bg #ffffff border T:1px solid #4a5565 @ 0.2 / R:1px solid #4a5565 @ 0.2 / B:1px solid #4a5565 @ 0.2 / L:1px solid #4a5565 @ 0.2 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.appearance-none.block 384.0x38.0 bg #ffffff border T:1px solid #4a5565 / R:1px solid #4a5565 / B:1px solid #4a5565 / L:1px solid #4a5565 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d1d5dc 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px | input.appearance-none.block 384.0x38.0 bg #ffffff border T:1px solid #4a5565 / R:1px solid #4a5565 / B:1px solid #4a5565 / L:1px solid #4a5565 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d1d5dc 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `signin-field-default.png`, `signin-field-focused.png`, `signin-field-filled.png`.

#### signin-password

Password field. The password field; focused only — nothing was typed into it.

Page: signin. Selector: `input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 384 x 38 | = |
| Padding | 0px 12px | = |
| Border | 1px solid #4a5565 @ 0.2 | 1px solid #4a5565 |
| Radius | 6px | = |
| Background | #ffffff | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d1d5dc 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| Outline | none | = |
| Font | Inter 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #101828 | = |
| Transition | background-color, border-color, box-shadow, color, opacity, transform 0.3s cubic-bezier(0.23, 1, 0.32, 1) | = |
| Cursor | text | = |
| Placeholder | #6a7282, opacity 1 | = |
| Painted layers | input.appearance-none.block 384.0x38.0 bg #ffffff border T:1px solid #4a5565 @ 0.2 / R:1px solid #4a5565 @ 0.2 / B:1px solid #4a5565 @ 0.2 / L:1px solid #4a5565 @ 0.2 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0.05 0px 1px 2px 0px | input.appearance-none.block 384.0x38.0 bg #ffffff border T:1px solid #4a5565 / R:1px solid #4a5565 / B:1px solid #4a5565 / L:1px solid #4a5565 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #d1d5dc 0px 0px 0px 3px, #000000 @ 0.05 0px 1px 2px 0px |
| How | at rest | clicked into the field |

Crops: `signin-password-default.png`, `signin-password-focused.png`.

#### signin-submit

Continue with email button. The email sign-in submit. Measured, never pressed.

Page: signin. Selector: `button:has-text("Continue with email")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 384 x 36 | = | = | = |
| Padding | 0px 16px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #0a4481 | #0954a5 | = | #0954a5 |
| Box shadow | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a4481 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0954a5 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = | #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0954a5 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| Outline | none | = | = | = |
| Font | Inter 14px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #f9fafb | = | = | = |
| Transition | background-color, border-color, box-shadow, color, opacity, transform 0.3s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.appearance-none.border-0 384.0x36.0 bg #0a4481 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0a4481 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | button.appearance-none.border-0 384.0x36.0 bg #0954a5 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0954a5 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = | button.appearance-none.border-0 384.0x36.0 bg #0954a5 r 6px shadow #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #000000 @ 0 0px 0px 0px 0px, #0954a5 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-submit-default.png`, `signin-submit-hover.png`, `signin-submit-focus-visible.png`, `signin-submit-pressed.png`.

#### signin-forgot

Forgot password link.

Page: signin. Selector: `a:has-text("Forgot password")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102.7 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | 2px | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101828 @ 0.1 offset 4px | = |
| Font | Inter 12px/16px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6a7282 | #101828 | = | #101828 |
| Transition | all 0.3s cubic-bezier(0.23, 1, 0.32, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.duration-300.ease-smooth 102.7x16.0 r 2px outline 2px solid #101828 @ 0.1 offset 4px | = |

Crops: `signin-forgot-default.png`, `signin-forgot-hover.png`, `signin-forgot-focus-visible.png`, `signin-forgot-pressed.png`.

### Footer

#### footer

Footer.

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 1539 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 16px |
| Background | #f9fafb |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-4hkkfc: Inter Display 60px/60px 800, #111827, ls -1.8px |
| Transition | none |
| Icon | 13 x 13, colour #0000ee, fill #000000 |
| Painted layers | footer.framer-gsucS.framer-Jz1qM 1392.0x1539.0 bg #f9fafb r 16px; a.framer-Z8GqO.framer-yuus7z 160.7x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px; div.framer-GylQJ.framer-9uoaq1 1180.0x1.0 bg #4b5563 @ 0.1; div::after.framer-1v2gxnr 1180pxx948px border B:1px solid #4b5563 @ 0.1; div.framer-GylQJ.framer-9uoaq1 1.0x44.0 bg #4b5563 @ 0.1; div.framer-2delir 44.0x44.0 bg #ff492c r 100px |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 160.73 x 36 | = | = | = |
| Padding | 0px 14px | = | = | = |
| Gap | 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #111827 | #1f2937 | = | = |
| Box shadow | #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text: Inter 14px/20px 600, #f9fafb, ls -0.14px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13 x 13, colour #0000ee, fill #000000 | = | = | 13 x 13, colour #ff0000, fill #000000 |
| ::after | 160.734px x 36px, absolute, bg #000000 @ 0, radius 7px | = | = | = |
| Painted layers | a.framer-Z8GqO.framer-yuus7z 160.7x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px | a.framer-Z8GqO.framer-yuus7z 160.7x36.0 bg #1f2937 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #1f2937 0px 0px 0px 1px, #000000 @ 0.1 0px 4px 6px -1px, #000000 @ 0.1 0px 2px 4px -2px | a.framer-Z8GqO.framer-yuus7z 160.7x36.0 bg #111827 r 7px shadow #ffffff @ 0 0px 0px 0px 0px, #111827 0px 0px 0px 1px, #000000 @ 0 0px 0px 0px 0px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Footer social icon.

Page: home. Selector: `footer social a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #f9fafb | #f3f4f6 | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | p.framer-text.framer-styles-preset-1wj1g05: Inter 12px/16px 500, #111827 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #4b5563 | 22 x 22, colour #111827 | = | = |
| Painted layers | a.framer-lIZC4.framer-FYn2Y 36.0x36.0 bg #f9fafb r 100px | a.framer-lIZC4.framer-FYn2Y 36.0x36.0 bg #f3f4f6 r 100px | a.framer-lIZC4.framer-FYn2Y 36.0x36.0 bg #f9fafb r 100px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-rating

G2 rating badge. The "4.6 Star Rating" badge linking the G2 review page. Measured, never followed.

Page: home. Selector: `footer a[href*="g2.com"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 156.28 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | sans-serif 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span: Inter 14px/20px 500, #111827, ls -0.14px | span: Inter 14px/20px 500, #fc4a2b, ls -0.14px | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 44 x 44, colour #0000ee, fill #000000 | = | = | 44 x 44, colour #ff0000, fill #000000 |
| Painted layers | div.framer-2delir 44.0x44.0 bg #ff492c r 100px | = | a.framer-SznH3.framer-jrDdx 156.3x44.0 outline 1px auto #005fcc offset 1px; div.framer-2delir 44.0x44.0 bg #ff492c r 100px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -1) | = | = |

Crops: `footer-rating-default.png`, `footer-rating-hover.png`, `footer-rating-focus-visible.png`, `footer-rating-pressed.png`.

#### footer-legal

Legal link.

Page: home. Selector: `footer a:has-text("Privacy")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53.91 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Inter 14px/20px 400 | = | = | = |
| Letter spacing | -0.14px | = | = | = |
| Colour | #4b5563 | #111827 | = | #111827 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.framer-text.framer-styles-preset-1tsklxz 53.9x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-legal-default.png`, `footer-legal-hover.png`, `footer-legal-focus-visible.png`, `footer-legal-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p.framer-text.framer-styles-preset-12yaez7: Inter 14px/20px 400, #111827, ls -0.14px |
| Transition | none |
| Icon | 96 x 26, colour #0000ee, fill #000000 |
| Painted layers | div.framer-6fskld 390.0x72.0 bg #ffffff; div.framer-Ry1Ea.framer-1475qpa 36.0x36.0 bg #ffffff r 100px; div.framer-o53dih 20.0x2.0 bg #111827 r 1px; div.framer-1pz2ia8 20.0x2.0 bg #111827 r 1px; div.framer-136aklz 390.0x998.8 bg #ffffff; div.framer-EB8Ss.framer-fhuvU 366.0x46.0 bg #ffffff r 7px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Mobile menu button. The 36px trigger at the right of the mobile bar; its own press opens the menu overlay.

Page: home. Selector: `header div[cursor=pointer] at right`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 36 x 36 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 100px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sans-serif 12px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.framer-Ry1Ea.framer-1475qpa 36.0x36.0 bg #ffffff r 100px; div.framer-o53dih 20.0x2.0 bg #111827 r 1px; div.framer-1pz2ia8 20.0x2.0 bg #111827 r 1px | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-menu-button-default.png`, `m-menu-button-pressed.png`.

#### m-menu-open

Mobile menu, open. The trigger after its own toggle; the open overlay shows in the crop.

Page: home. Selector: `header menu trigger`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 36 x 36 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 100px |
| Background | #f9fafb |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 12px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.framer-Ry1Ea.framer-1475qpa 36.0x36.0 bg #f9fafb r 100px; div.framer-o53dih 15.6x15.6 bg #4b5563 r 1px; div.framer-1pz2ia8 15.6x15.6 bg #4b5563 r 1px |
| How | own toggle |

Crops: `m-menu-open-opened.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `opacity 0.4s ease-out`, `unset`, `transform 167ms cubic-bezier(0.33, 0, 0, 1)`, `transform 250ms cubic-bezier(0.33, 0, 0, 1)`, `transform 134ms cubic-bezier(0.45, 0, 0.2, 1)`, `transform 100ms linear, opacity 80ms linear`, `opacity 80ms linear`
