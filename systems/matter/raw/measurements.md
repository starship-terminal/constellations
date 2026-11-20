# Component measurements

Computed styles read from getmatter.com on 2026-11-18 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844). The marketing site paints one near-black theme. A published article on words.getmatter.com loads signed out. The publication home is a subscribe gate (Subscribe was never pressed). The web reader sign-in card was measured and never submitted. Consent overlays were hidden, never answered. Written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The 62px near-black top bar: wordmark, Overview, Developer, Words That Matter, X, Sign In and the blurple Get Matter pill.

Page: home. Selector: `[class*="Nav_header__"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 62 |
| Padding | 15px |
| Border | none |
| Radius | 0px |
| Background | #0d0d0d |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 14px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.Nav_logoText__9oX8Z: MR-Camphor 17px/normal 600, #ffffff |
| Transition | none |
| Painted layers | header.Nav_header__vWuTK 1440.0x62.0 bg #0d0d0d; span.Nav_logoLockup__8R5pW 118.8x32.0 border R:1px solid #ffffff @ 0.1; a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_s__mSxsm 95.0x32.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Wordmark. The Matter lockup in the header.

Page: home. Selector: `[class*="Nav_logoLockup__"]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 118.8 x 32 |
| Padding | 0px 25px 0px 0px |
| Gap | 8px |
| Border | T: none; R: 1px solid #ffffff @ 0.1; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 14px/normal 400 |
| Letter spacing | normal |
| Colour | #969698 |
| Text node | span.Nav_logoText__9oX8Z: MR-Camphor 17px/normal 600, #ffffff |
| Transition | none |
| Cursor | pointer |
| Painted layers | span.Nav_logoLockup__8R5pW 118.8x32.0 border R:1px solid #ffffff @ 0.1 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A header text link. Overview is the current item.

Page: home. Selector: `a "Overview"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 58.22 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | MR-Camphor 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | filter 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.Nav_active__NSFUZ 58.2x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-signin

Sign-in link. The header Sign In link to web.getmatter.com. Measured, never followed.

Page: home. Selector: `a "Sign In"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42.2 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | MR-Camphor 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #969698 | = | = | = |
| Transition | filter 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 42.2x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Get Matter pill. The small blurple App Store pill in the header. Measured, never followed.

Page: home. Selector: `[class*="GetMatterCTAButton_button__"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 95 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #6d7eec | = | = | = |
| Background image | linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | MR-Camphor 14px/36px 500 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | filter 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_s__mSxsm 95.0x32.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px | = | a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_s__mSxsm 95.0x32.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home hero

#### hero-h1

Hero headline. The Camphor display headline on the near-black hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 850 x 80 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 32px/normal 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.typography_h1__yAD9z.Lead_h1__892Zo: MR-Camphor 80px/80px 700, #ffffff, ls -2.4px |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-lede

Hero lede. The sentence under the headline.

Page: home. Selector: `hero lede`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 850 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 20px/28px 400 |
| Letter spacing | normal |
| Colour | #969698 |
| Text node | span.Lead_textDesktop___QEcK: MR-Camphor 20px/28px 400, #969698 |
| Transition | none |
| How | at rest |

Crops: `hero-lede-default.png`.

#### hero-cta

Hero CTA. The large blurple Get Matter pill. Measured, never followed (it opens the App Store).

Page: home. Selector: `[class*="GetMatterCTAButton_l__"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #6d7eec | = | = | = |
| Background image | linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | MR-Camphor 18px/36px 500 | = | = | = |
| Letter spacing | -0.36px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | filter 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_l__Jhb0d 134.0x48.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px | = | a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_l__Jhb0d 134.0x48.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### secondary-link

Secondary link. The "Get the browser extension" text link under the hero CTA. Measured, never followed in this reading.

Page: home. Selector: `[class*="SecondaryLink_a__"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 216.73 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | MR-Camphor 16px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6d7eec | = | = | = |
| Transition | filter 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 14, colour #6d7eec | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.SecondaryLink_a__cZLT2 216.7x19.0 outline 1px auto #005fcc offset 1px | = |

Crops: `secondary-link-default.png`, `secondary-link-hover.png`, `secondary-link-focus-visible.png`, `secondary-link-pressed.png`.

### Home sections

#### section-h2

Section heading. A Camphor section heading.

Page: home. Selector: `h2 "One place"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 650 x 140 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 24px/normal 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.typography_h2__9_w_f: MR-Camphor 60px/70px 700, #ffffff, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### quote

Footer quote. The Ursula K. Le Guin line above the footer CTA.

Page: home. Selector: `quote`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 555.31 x 70 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 60px/70px 700 |
| Letter spacing | -1.8px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `quote-default.png`.

### Browser extension

#### ext-h2

Extension heading. The web-extension page heading.

Page: extension. Selector: `h2 on /web-extension`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 650 x 140 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 24px/normal 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.typography_h2__9_w_f: MR-Camphor 60px/70px 700, #ffffff, ls -1.8px |
| Transition | none |
| How | at rest |

Crops: `ext-h2-default.png`.

#### install-button

Install button. An Install-on-Chrome/Safari/Firefox button. Measured, never followed.

Page: extension. Selector: `[class*="BigButton_bigButton__"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 600 x 104 | = | = | = |
| Padding | 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 30px | = | = | = |
| Background | #1e1f22 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | MR-Camphor 18px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div: MR-Camphor 18px/normal 700, #ffffff | = | = | = |
| Transition | filter 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 16, colour #ffffff | = | = | = |
| Painted layers | a.BigButton_bigButton__PIQ7R 600.0x104.0 bg #1e1f22 r 30px; div.BigButton_positionChevron__HaFAW 48.0x48.0 bg #2f3034 r 50% | = | a.BigButton_bigButton__PIQ7R 600.0x104.0 bg #1e1f22 r 30px outline 1px auto #005fcc offset 1px; div.BigButton_positionChevron__HaFAW 48.0x48.0 bg #2f3034 r 50% | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `install-button-default.png`, `install-button-hover.png`, `install-button-focus-visible.png`, `install-button-pressed.png`.

### Legal pages

#### legal-h1

Legal heading. A privacy-policy section heading.

Page: privacy. Selector: `h1 on /privacy`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1035 x 38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 32px/normal 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `legal-h1-default.png`.

#### legal-body

Legal body. A body paragraph on the privacy page.

Page: privacy. Selector: `privacy p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1035 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 17px/24px 400 |
| Letter spacing | -0.17px |
| Colour | #969698 |
| Transition | none |
| How | at rest |

Crops: `legal-body-default.png`.

### Words That Matter

#### words-h1

Publication title. The Words That Matter title on the public Substack subscribe gate. Subscribe was never pressed.

Page: words. Selector: `h1 on words.getmatter.com`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 219 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 24px/24px 700 |
| Letter spacing | normal |
| Colour | #363737 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `words-h1-default.png`.

#### words-subscribe

Subscribe button. The publication Subscribe button on the gate. Measured at rest, never pressed (a press opens a sign-up).

Page: words. Selector: `button "Subscribe"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 108.52 x 40 |
| Padding | 0px 20px |
| Border | 1px solid #020617 |
| Radius | 0px 8px 8px 0px |
| Background | #020617 |
| Box shadow | none |
| Outline | none |
| Font | system-ui 14px/normal 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.button-text: system-ui 14px/normal 500, #ffffff |
| Transition | color, background-color, box-shadow, border, border-radius, opacity, filter, stroke, transform, scale, outline 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1) delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s |
| Opacity | 0.75 |
| Cursor | default |
| Painted layers | button.pencraft.pc-reset 108.5x40.0 bg #020617 border T:1px solid #020617 / R:1px solid #020617 / B:1px solid #020617 / L:1px solid #020617 r 0px 8px 8px 0px |
| How | at rest |

Crops: `words-subscribe-default.png`.

#### words-nav

Subscribe dismiss. The No thanks control on the subscribe gate. Measured at rest, never pressed.

Page: words. Selector: `No thanks`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 132.17 x 40 |
| Padding | 0px 16px |
| Gap | 8px |
| Border | none |
| Radius | 8px |
| Background | #ffffff @ 0 |
| Box shadow | none |
| Outline | none |
| Font | system-ui 15px/20px 600 |
| Letter spacing | normal |
| Colour | #757575 |
| Transition | color, background-color, box-shadow, border, border-radius, opacity, filter, stroke, transform, scale, outline 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s, 0.25s cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1), cubic-bezier(0.19, 1, 0.22, 1) delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s |
| Cursor | pointer |
| Icon | 20 x 20, colour #757575 |
| Painted layers | button.pencraft.pc-reset 132.2x40.0 bg #ffffff @ 0 r 8px |
| How | at rest |

Crops: `words-nav-default.png`.

### Public article

#### article-h1

Article title. The published article headline, loaded signed out.

Page: article. Selector: `article h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 728 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 32px/36px 600 |
| Letter spacing | normal |
| Colour | #5d4c37 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `article-h1-default.png`.

#### article-byline

Byline link. The author byline link. Measured, never followed.

Page: article. Selector: `byline a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 108.5 x 13 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | SF Compact 11px/20px 500 | = |
| Letter spacing | 0.2px | = |
| Colour | #5d4c37 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Text decoration | - | underline |

Crops: `article-byline-default.png`, `article-byline-hover.png`.

#### article-body

Article paragraph. A body paragraph on the public article.

Page: article. Selector: `article p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 728 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Lora 20px/32px 400 |
| Letter spacing | normal |
| Colour | #5d4c37 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `article-body-default.png`.

### Docs

#### docs-h1

Docs heading. The Matter Documentation heading on docs.getmatter.com.

Page: docs. Selector: `h1 on docs`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 366.48 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Inter 36px/40px 500 |
| Letter spacing | -0.9px |
| Colour | #19191e |
| Transition | none |
| How | at rest |

Crops: `docs-h1-default.png`.

#### docs-tab

Docs tab. A top tab (API). Measured, never followed in this reading.

Page: docs. Selector: `a "API"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 22.73 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Gap | 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #6366f1 offset 1px | = |
| Font | Inter 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #535357 | #28282c | = | #28282c |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | div.absolute.bottom-0 22.7x1.5 bg #e1e1e5 | a.link.nav-tabs-item 22.7x48.0 outline 1px auto #6366f1 offset 1px | div.absolute.bottom-0 22.7x1.5 bg #e1e1e5 |

Crops: `docs-tab-default.png`, `docs-tab-hover.png`, `docs-tab-focus-visible.png`, `docs-tab-pressed.png`.

#### docs-search

Docs search. The Search button. Measured, never opened into a query.

Page: docs. Selector: `button Search`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 256 x 32 | = | = | = |
| Padding | 0px 8px | = | = | = |
| Gap | 4px | = | = | = |
| Border | 1px solid #f1f1f5 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #f5f5fa | #f1f1f5 | = | #f1f1f5 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #6366f1 offset 0px | = |
| Font | Inter 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #737377 | = | = | = |
| Text node | span.flex-1.text-left: Inter 14px/20px 400, #737377 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #737377, fill #000000 | = | = | = |
| Painted layers | button.flex.items-center 256.0x32.0 bg #f5f5fa border T:1px solid #f1f1f5 / R:1px solid #f1f1f5 / B:1px solid #f1f1f5 / L:1px solid #f1f1f5 r 8px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #737377; span.px-1.5.py-0.5 31.4x20.0 bg #ffffff r 4px | button.flex.items-center 256.0x32.0 bg #f1f1f5 border T:1px solid #f1f1f5 / R:1px solid #f1f1f5 / B:1px solid #f1f1f5 / L:1px solid #f1f1f5 r 8px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #737377; span.px-1.5.py-0.5 31.4x20.0 bg #ffffff r 4px | button.flex.items-center 256.0x32.0 bg #f5f5fa border T:1px solid #f1f1f5 / R:1px solid #f1f1f5 / B:1px solid #f1f1f5 / L:1px solid #f1f1f5 r 8px outline 1px auto #6366f1 offset 0px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #737377; span.px-1.5.py-0.5 31.4x20.0 bg #ffffff r 4px | button.flex.items-center 256.0x32.0 bg #f1f1f5 border T:1px solid #f1f1f5 / R:1px solid #f1f1f5 / B:1px solid #f1f1f5 / L:1px solid #f1f1f5 r 8px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 bg #737377; span.px-1.5.py-0.5 31.4x20.0 bg #ffffff r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `docs-search-default.png`, `docs-search-hover.png`, `docs-search-focus-visible.png`, `docs-search-pressed.png`.

#### docs-card

Docs API link. The API card or tab link. Measured, never followed in this reading.

Page: docs. Selector: `a[href*="/api"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 22.73 x 48 | = |
| Padding | 0px | = |
| Gap | 8px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Inter 14px/20px 500 | = |
| Letter spacing | normal | = |
| Colour | #535357 | #28282c |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | div.absolute.bottom-0 22.7x1.5 bg #e1e1e5 |

Crops: `docs-card-default.png`, `docs-card-hover.png`.

### Sign-in card

#### signin-h1

Sign-in heading. The Welcome to Matter heading on the web reader sign-in card. Nothing was submitted.

Page: signin. Selector: `h1 on web.getmatter.com`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 199.56 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 24px/30px 600 |
| Letter spacing | -0.36px |
| Colour | #000000 @ 0.95 |
| Transition | none |
| How | at rest |

Crops: `signin-h1-default.png`.

#### google-button

Google button. Continue with Google (a Google identity widget). Measured, never pressed.

Page: signin. Selector: `.g_id_signin`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 340 x 48.4 |
| Padding | 0px |
| Border | none |
| Radius | 4px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.95 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1.1, 0, 0) |
| How | at rest |

Crops: `google-button-default.png`.

#### apple-button

Apple button. Continue with Apple. Measured, never pressed.

Page: signin. Selector: `button "Continue with Apple"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 44 | = | = | 334.9 x 43.34 |
| Padding | 0px 44px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #ffffff | #f5f5f5 @ 0.997961 | = | #f5f5f5 @ 0.997961 |
| Box shadow | #000000 @ 0.2 0px 0px 0px 1px inset, #000000 @ 0.04 0px 1px 2px 0px | = | = | = |
| Outline | none | = | 2px solid #009efa offset 2px | = |
| Font | -apple-system 14px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.95 | = | = | = |
| Transition | background-color, opacity, transform 0.15s, 0.15s, 0.15s ease-out, ease-out, ease-out delay 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 @ 0.95 | = | = | 15.76 x 15.76, colour #000000 @ 0.95 |
| Painted layers | button.pzzg3fc 340.0x44.0 bg #ffffff r 10px shadow #000000 @ 0.2 0px 0px 0px 1px inset, #000000 @ 0.04 0px 1px 2px 0px | button.pzzg3fc 340.0x44.0 bg #f5f5f5 @ 0.997961 r 10px shadow #000000 @ 0.2 0px 0px 0px 1px inset, #000000 @ 0.04 0px 1px 2px 0px | button.pzzg3fc 340.0x44.0 bg #ffffff r 10px shadow #000000 @ 0.2 0px 0px 0px 1px inset, #000000 @ 0.04 0px 1px 2px 0px outline 2px solid #009efa offset 2px | button.pzzg3fc 334.9x43.3 bg #f5f5f5 @ 0.997961 r 10px shadow #000000 @ 0.2 0px 0px 0px 1px inset, #000000 @ 0.04 0px 1px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.985, 0, 0, 0.985, 0, 0) |

Crops: `apple-button-default.png`, `apple-button-hover.png`, `apple-button-focus-visible.png`, `apple-button-pressed.png`.

#### email-field

Email field. The email field on the sign-in card. Focused only, never filled, never submitted.

Page: signin. Selector: `email input`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 340 x 44 | = |
| Padding | 0px 50px 0px 14px | = |
| Border | 1px solid #000000 @ 0.2 | 1px solid #000000 @ 0.53 |
| Radius | 10px | = |
| Background | #ffffff | = |
| Box shadow | none | #000000 @ 0.04 0px 0px 0px 3px |
| Outline | none | = |
| Font | -apple-system 14px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.95 | = |
| Transition | border-color, box-shadow, opacity 0.15s, 0.15s, 0.15s ease-out, ease-out, ease-out delay 0s, 0s, 0s | = |
| Cursor | text | = |
| Placeholder | #000000 @ 0.53, opacity 1 | = |
| Painted layers | input.pzzg3fj 340.0x44.0 bg #ffffff border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 10px | input.pzzg3fj 340.0x44.0 bg #ffffff border T:1px solid #000000 @ 0.53 / R:1px solid #000000 @ 0.53 / B:1px solid #000000 @ 0.53 / L:1px solid #000000 @ 0.53 r 10px shadow #000000 @ 0.04 0px 0px 0px 3px |
| How | at rest | clicked into the field |

Crops: `email-field-default.png`, `email-field-focused.png`.

#### email-continue

Email continue arrow. The arrow button beside the email field. Measured at rest, never pressed (a press would submit).

Page: signin. Selector: `email arrow button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 32 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 8px |
| Background | #000000 @ 0.04 |
| Box shadow | none |
| Outline | none |
| Font | -apple-system 13.3333px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.53 |
| Transition | background-color, color, opacity, transform 0.15s, 0.15s, 0.15s, 0.15s ease-out, ease-out, ease-out, ease-out delay 0s, 0s, 0s, 0s |
| Cursor | default |
| Icon | 16 x 16, colour #000000 @ 0.53 |
| Painted layers | button.pzzg3fk 32.0x32.0 bg #000000 @ 0.04 r 8px |
| How | at rest |

Crops: `email-continue-default.png`.

#### legal-link

Legal link. The Terms of Service link under the sign-in card.

Page: signin. Selector: `a "Terms of Service"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 98.44 x 15 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 3px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | -apple-system 12.5px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.75 | #000000 @ 0.95 |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Text decoration | - | underline offset 2px |

Crops: `legal-link-default.png`, `legal-link-hover.png`.

### Footer

#### footer

Footer. The marketing footer: quote, Get Matter, Terms, Privacy, X, Say hello.

Page: home. Selector: `Footer_footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #0d0d0d |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.typography_h2__9_w_f: MR-Camphor 60px/70px 700, #ffffff, ls -1.8px |
| Transition | none |
| Painted layers | footer.Footer_footer__OQpsI 1440.0x900.0 bg #0d0d0d; a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_l__Jhb0d 134.0x48.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px; div.Footer_gradient__TNe4a 1440.0x410.0 image linear-gradient(#0d0d0d @ 0, #0d0d0d 90.22%) |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer text link.

Page: home. Selector: `footer a "Privacy"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50.88 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | MR-Camphor 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #969698 | = | = | = |
| Transition | filter 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 50.9x19.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-cta

Footer CTA. The footer Get Matter pill. Measured, never followed.

Page: home. Selector: `footer Get Matter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #6d7eec | = | = | = |
| Background image | linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | MR-Camphor 18px/36px 500 | = | = | = |
| Letter spacing | -0.36px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | filter 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_l__Jhb0d 134.0x48.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px | = | a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_l__Jhb0d 134.0x48.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-cta-default.png`, `footer-cta-hover.png`, `footer-cta-focus-visible.png`, `footer-cta-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The header at 390px.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 66 |
| Padding | 15px 25px |
| Border | none |
| Radius | 0px |
| Background | #0d0d0d |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 16px/normal 400 |
| Letter spacing | normal |
| Colour | #0d0d0d |
| Text node | a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_s__mSxsm: MR-Camphor 14px/36px 500, #ffffff, ls -0.28px |
| Transition | none |
| Icon | 91.83 x 32, colour #ffffff |
| Painted layers | header.Mobile_header__pW_07 390.0x66.0 bg #0d0d0d; a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_s__mSxsm 95.0x32.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hero

Mobile headline. The hero headline at 390px.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 340 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | MR-Camphor 32px/normal 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.typography_h1__yAD9z.Lead_h1__892Zo: MR-Camphor 40px/50px 700, #ffffff, ls -1.2px |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

#### m-cta

Mobile CTA. The large Get Matter pill at 390px. Measured, never followed.

Page: mobile. Selector: `[class*="GetMatterCTAButton_l__"] at 390`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 134 x 48 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 100px | = |
| Background | #6d7eec | = |
| Background image | linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | MR-Camphor 18px/36px 500 | = |
| Letter spacing | -0.36px | = |
| Colour | #ffffff | = |
| Transition | filter 0.3s ease | = |
| Cursor | pointer | = |
| Painted layers | a.GetMatterCTAButton_button__Tnitl.GetMatterCTAButton_l__Jhb0d 134.0x48.0 bg #6d7eec image linear-gradient(210.25deg, #3e467c @ 0.2 18.42%, #ffffff @ 0 75.82%), none r 100px | = |
| How | at rest | mouse hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`.

## Transitions declared in the readable stylesheets

getmatter.com serves its Next.js CSS bundles same-origin, so this list holds the transitions the readable document.styleSheets rules declare on each page (cross-origin sheets are skipped); the per-state Transition rows above are computed values and cover every rule the page paints.

- home: `filter 0.3s`, `opacity 0.3s`, `background 0.2s`, `transform 0.2s`, `opacity 0.2s`
