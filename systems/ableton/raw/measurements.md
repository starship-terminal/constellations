# Component measurements

Computed styles read from ableton.com on 2026-11-08 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### nav-bar

Top navigation bar. The white top bar: the Ableton logo (the grid mark), product links (Live / Push / Move / Note / Link / Shop / Packs / Help), the "More" disclosure, "Try Live 12 for free" in blue and "Log in or register".

Page: home. Selector: `header.main-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 69 |
| Padding | 20px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: futura-pt 20px/30px 700, #000000 |
| Transition | none |
| Icon | 60 x 28, colour #000000 |
| Painted layers | button::after.main-nav__trigger-label.abl-btn--reset 0pxx0px border T:5px solid #000000 / R:5px solid #000000 @ 0 / B:5px solid #000000 @ 0 / L:5px solid #000000 @ 0; span::before.main-nav__icon.main-nav__icon--collapse 12pxx2px bg #000000; span::before.main-nav__icon.main-nav__icon--expand 12pxx2px bg #000000; span::after.main-nav__icon.main-nav__icon--expand 2pxx12px bg #000000 |
| Ancestor paint | 1 up div.main.js-main bg #ffffff |
| How | at rest |

Crops: `nav-bar-default.png`.

#### nav-logo

Logo. The Ableton grid-mark wordmark linking home.

Page: home. Selector: `.main-nav__logo`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60 x 28 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 60 x 28, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.main-nav__logo.focus-visible 60.0x28.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-logo-default.png`, `nav-logo-hover.png`, `nav-logo-focus-visible.png`, `nav-logo-pressed.png`.

#### nav-link

Nav link. A product link in the top bar.

Page: home. Selector: `.main-nav__link-list__link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 30.69 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.focus-visible 30.7x26.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-more

More button. The "More +" disclosure button opening the extended menu.

Page: home. Selector: `.js-main-nav-more-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 63.31 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 20px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span: futura-pt 20px/normal 700, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span::before.main-nav__icon.main-nav__icon--collapse 12pxx2px bg #000000; span::before.main-nav__icon.main-nav__icon--expand 12pxx2px bg #000000; span::after.main-nav__icon.main-nav__icon--expand 2pxx12px bg #000000 | = | button.abl-btn--reset.main-nav__more-button 63.3x26.0 outline 1px auto #005fcc offset 0px; span::before.main-nav__icon.main-nav__icon--collapse 12pxx2px bg #000000; span::before.main-nav__icon.main-nav__icon--expand 12pxx2px bg #000000; span::after.main-nav__icon.main-nav__icon--expand 2pxx12px bg #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-more-default.png`, `nav-more-hover.png`, `nav-more-focus-visible.png`, `nav-more-pressed.png`.

#### nav-more-panel

More menu panel. The expanded "More" menu: "More on Ableton.com" link row plus "More from Ableton" cards (Ableton Learn, Learning Synths, Making Music).

Page: home. Selector: `.main-nav__more`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 1440 x 380.27 |
| Padding | 27px 40px 55px 40px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h3.main-nav__section-heading: futura-pt 30px/42px 700, #000000 |
| Transition | none |
| How | More button pressed; local disclosure, nothing navigated |

Crops: `nav-more-panel-open.png`.

#### nav-more-link

More menu link. A link inside the expanded More menu.

Page: home. Selector: `.main-nav__more a`. States: open, hover.

| Property | open | hover |
|---|---|---|
| Size (w x h) | 35.77 x 26 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | menu open | mouse hover |

Crops: `nav-more-link-open.png`, `nav-more-link-hover.png`.

#### nav-trial-cta

Trial CTA link. The blue "Try Live 12 for free" link at the right end of the top bar; links to /en/trial/. Hovered and focused only.

Page: home. Selector: `nav trial link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 147.95 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.focus-visible 148.0x26.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-trial-cta-default.png`, `nav-trial-cta-hover.png`, `nav-trial-cta-focus-visible.png`, `nav-trial-cta-pressed.png`.

#### nav-login

Log in link. "Log in or register" in the top bar; links to /en/login/. Hovered and focused only.

Page: home. Selector: `nav login link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.78 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 16px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.focus-visible 106.8x21.0 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### footer

Footer. The page footer: link columns, the newsletter form, social buttons, the language and location selectors and the legal row.

Page: home. Selector: `.main-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 783.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.main-footer__h3.abl-block: futura-pt 20px/30px 700, #000000 |
| Transition | none |
| Icon | 32 x 32, colour #000000 |
| Painted layers | footer.main-footer 1440.0x784.0 bg #ffffff; div.main-footer__separator 0.0x0.0 bg #ffffff; div::after.main-footer__separator autox0px border T:2px solid #efefef; input 360.0x42.0 bg #eeeeee; input.main-footer 120.0x42.0 bg #0000ff; a::after.main-footer__has-arrow 6pxx6px border T:1px solid #000000 / R:1px solid #000000 |
| How | at rest |

Crops: `footer-default.png`.

#### footer-heading

Footer column heading.

Page: home. Selector: `.main-footer__h3`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `footer-heading-default.png`.

#### footer-link

Footer link.

Page: home. Selector: `.main-footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 218.55 x 26 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 6px x 6px, static, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a::after.main-footer__has-arrow 6pxx6px border T:1px solid #000000 / R:1px solid #000000 | = | a.main-footer__has-arrow.focus-visible 218.5x26.0 outline 1px auto #005fcc offset 1px; a::after.main-footer__has-arrow.focus-visible 6pxx6px border T:1px solid #000000 / R:1px solid #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social icon link. One of the social-icon links (Facebook, X, YouTube, Instagram, TikTok, Discord).

Page: home. Selector: `.main-footer__social-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 44 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 0px/0px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 32 x 32, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.main-footer__social-button.focus-visible 44.0x44.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### newsletter-field

Newsletter email field. The email field of the footer newsletter form; clicked into, nothing typed or sent.

Page: home. Selector: `.main-footer__newsletter__form input[type=email]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 360 x 42 | = |
| Padding | 8px 15px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #eeeeee | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 0px |
| Font | futura-pt 20px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #666666, opacity 1 | = |
| Painted layers | input 360.0x42.0 bg #eeeeee | input.focus-visible 360.0x42.0 bg #eeeeee outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field |

Crops: `newsletter-field-default.png`, `newsletter-field-focused.png`.

#### newsletter-submit

Newsletter sign-up button. The "Sign up" button of the footer newsletter form. Measured, never pressed.

Page: home. Selector: `.main-footer__button`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 120 x 42 | = | = |
| Padding | 7px 30px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #0000ff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px |
| Font | futura-pt 20px/normal 700 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | pointer | = | = |
| Placeholder | #ffffff, opacity 1 | = | = |
| Painted layers | input.main-footer 120.0x42.0 bg #0000ff | = | input.main-footer.focus-visible 120.0x42.0 bg #0000ff outline 1px auto #005fcc offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab |

Crops: `newsletter-submit-default.png`, `newsletter-submit-hover.png`, `newsletter-submit-focus-visible.png`.

#### footer-locale

Language selector. The footer language <select>.

Page: home. Selector: `.main-footer__secondary__select`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 116.5 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/21px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Painted layers | div::after.form__element.main-footer__icon-arrow--small 30pxx30px image url(data:…); select.js-language-chooser 116.5x30.0 bg #eeeeee |
| How | at rest |

Crops: `footer-locale-default.png`.

### Home

#### hero-teaser

Hero teaser. The lead tile of the home grid: a photo/video cell with a large white headline and a "See what's new" link.

Page: home. Selector: `.homepage-teaser`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 839.98 x 559.98 |
| Padding | 0px 0px 559.984px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.homepage-teaser__primary-headline: futura-pt 60px/66px 700, #ffffff |
| Transition | none |
| Painted layers | span::after.has-arrow.is-underlined 7.1875pxx7.1875px border T:2px solid #ffffff / R:2px solid #ffffff |
| How | at rest |

Crops: `hero-teaser-default.png`.

#### hero-title

Hero headline. The white display headline over the hero media.

Page: home. Selector: `.homepage-teaser__primary-headline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 719.98 x 198 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 60px/66px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero link. "See what's new" — the arrow link under the hero headline.

Page: home. Selector: `.homepage-teaser__cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 719.98 x 36 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | futura-pt 24px/36px 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span.has-arrow.is-underlined: futura-pt 24px/36px 700, #ffffff | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | span::after.has-arrow.is-underlined 7.1875pxx7.1875px border T:2px solid #ffffff / R:2px solid #ffffff | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-pressed.png`.

#### home-cell

Grid cell. One tile of the loose homepage grid: the layout mixes image cells and text-on-white cells.

Page: home. Selector: `.cell`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 839.98 x 559.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.homepage-teaser__primary-headline: futura-pt 60px/66px 700, #ffffff |
| Transition | none |
| Painted layers | span::after.has-arrow.is-underlined 7.1875pxx7.1875px border T:2px solid #ffffff / R:2px solid #ffffff |
| How | at rest |

Crops: `home-cell-default.png`.

#### home-promo-card

Promo card. A text-on-tint promo cell in the grid (the rent-to-own card on lime stripes).

Page: home. Selector: `promo cell`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 479.98 x 319.98 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.homepage-teaser__primary-headline: futura-pt 30px/42px 700, #000000 |
| Transition | none |
| Painted layers | span::after.has-arrow.is-underlined 6pxx6px border T:1px solid #000000 / R:1px solid #000000 |
| How | at rest |

Crops: `home-promo-card-default.png`.

#### scroll-down

Scroll-down button. The blue chevron button pinned under the first screen; an in-page anchor, measured at rest.

Page: home. Selector: `.homepage-grid__anchor`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 60 x 60 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #0000ff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | bottom 0.15s ease | = |
| Cursor | pointer | = |
| ::after | 26px x 14px, absolute, bg #000000 @ 0 url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+PHN2ZyB3aWR0aD0iM, radius 0px | = |
| Painted layers | a.homepage-grid.icon-scroll-down 60.0x60.0 bg #0000ff; a::after.homepage-grid.icon-scroll-down 26pxx14px image url(data:…) | = |
| How | at rest | mouse hover |

Crops: `scroll-down-default.png`, `scroll-down-hover.png`.

#### panel-title

Section headline. A section headline over a blog-teaser row ("From the blog" and friends).

Page: home. Selector: `.panel-blog-teasers__headline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200.03 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 40px/48px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `panel-title-default.png`.

#### blog-teaser

Blog teaser card. An article teaser in the home/blog rows: media cell, category tag and headline.

Page: home. Selector: `.blog-teaser`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 360 x 303.05 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span: futura-pt 14px/21px 700, #000000 | = |
| Transition | none | = |
| Painted layers | div.blog-teaser.js-lazyload-image 360.0x202.5 bg #eeeeee; a.blog-teaser__category 87.0x24.9 bg #ff8389 | = |
| How | at rest | mouse hover |

Crops: `blog-teaser-default.png`, `blog-teaser-hover.png`.

#### blog-teaser-title

Blog teaser headline.

Page: home. Selector: `.blog-teaser__headline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | a: futura-pt 20px/30px 700, #000000 |
| Transition | none |
| How | at rest |

Crops: `blog-teaser-title-default.png`.

#### blog-teaser-tag

Blog teaser category.

Page: home. Selector: `.blog-teaser__category`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 87.03 x 24.91 |
| Padding | 1.96px 11.9px |
| Border | none |
| Radius | 0px |
| Background | #ff8389 |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 14px/21px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: futura-pt 14px/21px 700, #000000 |
| Transition | none |
| Cursor | pointer |
| Painted layers | a.blog-teaser__category 87.0x24.9 bg #ff8389 |
| How | at rest |

Crops: `blog-teaser-tag-default.png`.

#### panel-cat-link

Category link. A blog category filter link under a teasers panel.

Page: home. Selector: `.panel-blog-teasers__link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 141.39 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 24px/36px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 7.1875px x 7.1875px, static, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a::after.panel-blog-teasers__link.text-blue 7.1875pxx7.1875px border T:2px solid #0000ff / R:2px solid #0000ff | = | a.panel-blog-teasers__link.text-blue 141.4x36.0 outline 1px auto #005fcc offset 1px; a::after.panel-blog-teasers__link.text-blue 7.1875pxx7.1875px border T:2px solid #0000ff / R:2px solid #0000ff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `panel-cat-link-default.png`, `panel-cat-link-hover.png`, `panel-cat-link-focus-visible.png`, `panel-cat-link-pressed.png`.

### Consent overlay

#### cookie-bar

Cookie consent card. The black consent card fixed at the bottom left: "Clicking Accept means you consent…" copy with Accept (blue), Close and More info buttons. Re-shown for the measurement, never answered.

Page: home. Selector: `#biscuits-overlay .bg-black`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 453.33 x 414.91 |
| Padding | 20px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.abl-type-12.abl-type-14-ms: futura-pt 16px/24px 400, #ffffff |
| Transition | none |
| Painted layers | div.abl-pa-10.abl-pa-20-ml 453.3x414.9 bg #000000; button.abl-button.abl-button--outline 201.7x47.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff; button.abl-button.abl-button--primary 413.3x47.0 bg #0000ff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; a.abl-button.abl-button--outline 201.7x47.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff |
| How | re-shown after the sweep hid it |

Crops: `cookie-bar-open.png`.

#### cookie-accept

Accept button. The blue "Accept" button of the consent card. Measured in every state — never pressed (it would post consent).

Page: home. Selector: `#biscuits-accept-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 413.33 x 47 | = | = | = |
| Padding | 6.5px 30px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | 2px solid #000000 | = |
| Radius | 0px | = | = | = |
| Background | #0000ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | futura-pt 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.abl-button.abl-button--primary 413.3x47.0 bg #0000ff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 | = | button.abl-button.abl-button--primary 413.3x47.0 bg #0000ff border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cookie-accept-default.png`, `cookie-accept-hover.png`, `cookie-accept-focus-visible.png`, `cookie-accept-pressed.png`.

#### cookie-close

Close button. The outline "Close" button, which denies consent. Measured, never pressed.

Page: home. Selector: `#biscuits-overlay .abl-button--outline`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 201.66 x 47 | = | = | = |
| Padding | 6.5px 30px | = | = | = |
| Border | 2px solid #ffffff | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.abl-button.abl-button--outline 201.7x47.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff | = | button.abl-button.abl-button--outline 201.7x47.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cookie-close-default.png`, `cookie-close-hover.png`, `cookie-close-focus-visible.png`, `cookie-close-pressed.png`.

#### cookie-more-info

More info link. "More info" — the outline link to /en/cookie-settings/. Hovered and focused only.

Page: home. Selector: `#biscuits-overlay a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 201.67 x 47 | = | = | = |
| Padding | 6.5px 30px | = | = | = |
| Border | 2px solid #ffffff | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.abl-button.abl-button--outline 201.7x47.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff | = | a.abl-button.abl-button--outline 201.7x47.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cookie-more-info-default.png`, `cookie-more-info-hover.png`, `cookie-more-info-focus-visible.png`, `cookie-more-info-pressed.png`.

### Live page

#### live-title

Page title. "Find … in Ableton Live" — the product page title in the largest abl-type step.

Page: live. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 115.2 x 77 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 60px/78px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `live-title-default.png`.

#### live-section-title

Section title. A big section heading ("Play freely with ideas").

Page: live. Selector: `h1.abl-type-*`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 396.31 x 155 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 60px/78px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `live-section-title-default.png`.

#### btn-try

Try-for-free button. The boxed "Try Live 12 for free" button on the product page; links to /en/trial/. Hovered and focused only.

Page: live. Selector: `a.boxed-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185.95 x 50 | = | = | = |
| Padding | 10px 0px 10px 38px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px |
| Outline | none | = | 2px solid #ff764d offset 2px | = |
| Font | Futura PT 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ff | #000000 | #000000 | #000000 |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.boxed-btn 186.0x50.0 shadow #000000 @ 0 0px 0px 0px 0px | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px outline 2px solid #ff764d offset 2px; span 186.0x50.0 bg #ffffff | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-try-default.png`, `btn-try-hover.png`, `btn-try-focus-visible.png`, `btn-try-pressed.png`.

#### btn-buy

Buy now button. The boxed "Buy now" button; links to the shop. Hovered and focused only.

Page: live. Selector: `a.boxed-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 130.33 x 48 | = | = | = |
| Padding | 8px 30px | = | = | = |
| Border | 1px solid #0032e6 | 1px solid #042b9f | 1px solid #042b9f | 1px solid #042b9f |
| Radius | 0px | = | = | = |
| Background | #0032e6 | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px | #042b9f @ 0 0px 0px 0px 0px | #042b9f @ 0 0px 0px 0px 0px | #042b9f @ 0 0px 0px 0px 0px |
| Outline | none | = | 2px solid #0000ff offset 2px | = |
| Font | Futura PT 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.boxed-btn 130.3x48.0 bg #0032e6 border T:1px solid #0032e6 / R:1px solid #0032e6 / B:1px solid #0032e6 / L:1px solid #0032e6 shadow #000000 @ 0 0px 0px 0px 0px | a.btn.boxed-btn 130.3x48.0 bg #0032e6 border T:1px solid #042b9f / R:1px solid #042b9f / B:1px solid #042b9f / L:1px solid #042b9f shadow #042b9f @ 0 0px 0px 0px 0px; span 128.3x46.0 bg #042b9f | a.btn.boxed-btn 130.3x48.0 bg #0032e6 border T:1px solid #042b9f / R:1px solid #042b9f / B:1px solid #042b9f / L:1px solid #042b9f shadow #042b9f @ 0 0px 0px 0px 0px outline 2px solid #0000ff offset 2px; span 128.3x46.0 bg #042b9f | a.btn.boxed-btn 130.3x48.0 bg #0032e6 border T:1px solid #042b9f / R:1px solid #042b9f / B:1px solid #042b9f / L:1px solid #042b9f shadow #042b9f @ 0 0px 0px 0px 0px; span 128.3x46.0 bg #042b9f |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `btn-buy-default.png`, `btn-buy-hover.png`, `btn-buy-focus-visible.png`, `btn-buy-pressed.png`.

#### btn-video

Video play button. The "Play: VIDEO" overlay button on a demo clip. Hovered only — pressing plays the video.

Page: live. Selector: `.abl-bg-overlay-button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 60 x 60 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #000000 @ 0.5 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Futura PT 20px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 60 x 60, colour #ffffff, fill #000000 | = |
| Painted layers | button.abl-button.abl-pa-0 60.0x60.0 bg #000000 @ 0.5 | = |
| How | at rest | mouse hover |

Crops: `btn-video-default.png`, `btn-video-hover.png`.

#### btn-audio

Audio play button. A "Play: <sound>" button on an audio example. Hovered only — pressing plays audio.

Page: live. Selector: `.js-simple-audio-play-button`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 32 x 32.84 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #0000ff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Futura PT 20px/28px 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 32 x 32, colour #ffffff, fill #000000 | = |
| Painted layers | button.abl-button.abl-button--primary 32.0x32.8 bg #0000ff | = |
| How | at rest | mouse hover |

Crops: `btn-audio-default.png`, `btn-audio-hover.png`.

#### anchor-link

Anchor link. An in-page anchor link in the feature navigation row.

Page: live. Selector: `.nav-anchor-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 151.42 x 34 | = | = | = |
| Padding | 5px 0px 2px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #0000ff offset 2px | = |
| Font | Futura PT 18px/27px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0032e6 | #0000ff | = | #0000ff |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color, transform 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 0px x 1px, absolute, bg #000000 @ 0, radius 0px | 100% x 1px, absolute, bg #0000ff, radius 0px | = | 100% x 1px, absolute, bg #0000ff, radius 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a::after.nav-link.nav-anchor-link 100%x1px bg #0000ff | a.nav-link.nav-anchor-link 151.4x34.0 outline 2px solid #0000ff offset 2px | a::after.nav-link.nav-anchor-link 100%x1px bg #0000ff |

Crops: `anchor-link-default.png`, `anchor-link-hover.png`, `anchor-link-focus-visible.png`, `anchor-link-pressed.png`.

#### collapse-toggle

Discover-more collapse. A "Discover more … sounds" collapsed-content toggle.

Page: live. Selector: `.nav-button-link.collapsed`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1210 x 72 | = |
| Padding | 16px | = |
| Gap | 8px | = |
| Border | 2px solid #0000ff | = |
| Radius | 0px | = |
| Background | #ffffff | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Futura PT 24px/36px 700 | = |
| Letter spacing | normal | = |
| Colour | #0000ff | = |
| Text node | span.a-text: Futura PT 24px/36px 700, #0000ff | = |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color, transform 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = |
| Cursor | pointer | = |
| Icon | 20 x 20, colour #0000ff, fill #000000 | = |
| ::before | 0px x 1px, absolute, bg #000000 @ 0, radius 0px | calc(100% - 40px) x 1px, absolute, bg #0000ff, radius 0px |
| ::after | 40px x auto, absolute, bg #000000 @ 0, radius 0px | = |
| Painted layers | a.nav-link.nav-button-link 1210.0x72.0 bg #ffffff border T:2px solid #0000ff / R:2px solid #0000ff / B:2px solid #0000ff / L:2px solid #0000ff | a.nav-link.nav-button-link 1210.0x72.0 bg #ffffff border T:2px solid #0000ff / R:2px solid #0000ff / B:2px solid #0000ff / L:2px solid #0000ff; a::before.nav-link.nav-button-link calc(100% - 40px)x1px bg #0000ff |
| How | at rest | mouse hover |

Crops: `collapse-toggle-default.png`, `collapse-toggle-hover.png`.

#### collapse-toggle-open

Discover-more collapse (open). The same toggle after being pressed once; client-side expand, nothing sent.

Page: live. Selector: `.nav-button-link`. States: open.

| Property | open |
|---|---|
| Size (w x h) | 1210 x 72 |
| Padding | 16px |
| Gap | 8px |
| Border | 2px solid #0000ff |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 24px/36px 700 |
| Letter spacing | normal |
| Colour | #0000ff |
| Text node | span.a-text: Futura PT 24px/36px 700, #0000ff |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color, transform 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s |
| Cursor | pointer |
| Icon | 20 x 20, colour #0000ff, fill #000000 |
| ::before | 0px x 1px, absolute, bg #000000 @ 0, radius 0px |
| ::after | 40px x auto, absolute, bg #000000 @ 0, radius 0px |
| Painted layers | a.nav-link.nav-button-link 1210.0x72.0 bg #ffffff border T:2px solid #0000ff / R:2px solid #0000ff / B:2px solid #0000ff / L:2px solid #0000ff |
| How | pressed once to expand |

Crops: `collapse-toggle-open-open.png`.

### Content pages

#### push-title

Push page title.

Page: push. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 156.67 x 78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 60px/78px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `push-title-default.png`.

#### push-cta

push primary CTA.

Page: push. Selector: `a.boxed-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185.95 x 50 | = | = | = |
| Padding | 10px 0px 10px 38px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px |
| Outline | none | = | 2px solid #ff764d offset 2px | = |
| Font | Futura PT 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ff | #000000 | #000000 | #000000 |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.boxed-btn 186.0x50.0 shadow #000000 @ 0 0px 0px 0px 0px | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px outline 2px solid #ff764d offset 2px; span 186.0x50.0 bg #ffffff | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `push-cta-default.png`, `push-cta-hover.png`, `push-cta-focus-visible.png`, `push-cta-pressed.png`.

#### move-title

Move page title.

Page: move. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 175.03 |
| Padding | 20px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 60px/78px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Icon | 256 x 77.03, colour #ffffff |
| How | at rest |

Crops: `move-title-default.png`.

#### move-cta

move primary CTA.

Page: move. Selector: `a.boxed-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185.95 x 50 | = | = | = |
| Padding | 10px 0px 10px 38px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px |
| Outline | none | = | 2px solid #ff764d offset 2px | = |
| Font | Futura PT 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ff | #000000 | #000000 | #000000 |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.boxed-btn 186.0x50.0 shadow #000000 @ 0 0px 0px 0px 0px | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px outline 2px solid #ff764d offset 2px; span 186.0x50.0 bg #ffffff | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `move-cta-default.png`, `move-cta-hover.png`, `move-cta-focus-visible.png`, `move-cta-pressed.png`.

#### note-title

Note page title.

Page: note. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1207 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 60px/78px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.abl-type-90-xs.abl-type-120-md: Futura PT 120px/144px 700, #d6ff00 |
| Transition | none |
| How | at rest |

Crops: `note-title-default.png`.

#### note-cta

note primary CTA.

Page: note. Selector: `a.boxed-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 185.95 x 50 | = | = | = |
| Padding | 10px 0px 10px 38px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #000000 @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px | #ffffff @ 0 0px 0px 0px 0px |
| Outline | none | = | 2px solid #ff764d offset 2px | = |
| Font | Futura PT 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ff | #000000 | #000000 | #000000 |
| Transition | opacity, color, background-color, text-decoration, top, right, bottom, left, width, max-width, height, max-height, padding-top, padding-right, padding-bottom, padding-left, box-shadow, border-color 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s, 0.3s ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out, ease-in-out delay 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.boxed-btn 186.0x50.0 shadow #000000 @ 0 0px 0px 0px 0px | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px outline 2px solid #ff764d offset 2px; span 186.0x50.0 bg #ffffff | a.btn.boxed-btn 186.0x50.0 shadow #ffffff @ 0 0px 0px 0px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `note-cta-default.png`, `note-cta-hover.png`, `note-cta-focus-visible.png`, `note-cta-pressed.png`.

#### link-title

Link page title.

Page: link. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 220 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 110px/110px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.text-white: futura-pt 110px/110px 700, #ffffff |
| Transition | none |
| How | at rest |

Crops: `link-title-default.png`.

#### link-cta

link primary CTA. The page's main call-to-action (a boxed button, or an arrow link on Link).

Page: link. Selector: `a.boxed-btn / a.has-arrow`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 410.13 x 31 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 24px/36px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| ::after | 7.1875px x 7.1875px, static, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | a::after.text-blue.has-arrow 7.1875pxx7.1875px border T:2px solid #0000ff / R:2px solid #0000ff | = | a.text-blue.has-arrow 410.1x31.0 outline 1px auto #005fcc offset 1px; a::after.text-blue.has-arrow 7.1875pxx7.1875px border T:2px solid #0000ff / R:2px solid #0000ff | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `link-cta-default.png`, `link-cta-hover.png`, `link-cta-focus-visible.png`, `link-cta-pressed.png`.

#### about-title

About title.

Page: about. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 666.69 x 84 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 30px/42px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `about-title-default.png`.

#### about-body

about body text.

Page: about. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 377.64 x 156 |
| Padding | 0px 0px 12px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 120px/144px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | strong: Futura PT 120px/144px 700, #ffffff |
| Transition | none |
| How | at rest |

Crops: `about-body-default.png`.

#### help-title

Help title.

Page: help. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 144 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 120px/144px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `help-title-default.png`.

#### help-body

help body text.

Page: help. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 317.78 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Futura PT 20px/28px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `help-body-default.png`.

#### jobs-title

Jobs title.

Page: jobs. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200.03 x 799.73 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 110px/110px 700 |
| Letter spacing | normal |
| Colour | #00ffff |
| Transition | none |
| Ancestor paint | 1 up header.page-jobs.bg-dolphin bg #eeeeee |
| How | at rest |

Crops: `jobs-title-default.png`.

#### jobs-body

jobs body text.

Page: jobs. Selector: `body p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 180 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `jobs-body-default.png`.

### Trial page

#### trial-title

Trial page title. "Start your free trial of Ableton Live" in the heading_l style.

Page: trial. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 216 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 90px/108px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `trial-title-default.png`.

#### trial-download

Download button. A "Download" button for a trial edition. Measured, never pressed — the download would start.

Page: trial. Selector: `.test-download-lite-button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 147.14 x 47 | = | = | = |
| Padding | 6.5px 30px | = | = | = |
| Border | 2px solid #000000 @ 0 | = | 2px solid #000000 | = |
| Radius | 0px | = | = | = |
| Background | #0000ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | futura-pt 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.abl-button.abl-button--primary 147.1x47.0 bg #0000ff border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 | = | button.abl-button.abl-button--primary 147.1x47.0 bg #0000ff border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `trial-download-default.png`, `trial-download-hover.png`, `trial-download-focus-visible.png`, `trial-download-pressed.png`.

#### trial-edition-card

Trial edition panel. A panel choosing between the Live editions for the trial.

Page: trial. Selector: `edition panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 654.97 |
| Padding | 120px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h1.abl-c-type-heading_l.abl-mb-20: futura-pt 90px/108px 700, #000000 |
| Transition | none |
| Icon | 0 x 0, colour #0000ff, fill #000000 |
| Painted layers | div.js-trial-mobile-screen1.abl-pa-20 0.0x0.0 bg #fbffa7; button.js-trial-mobile-trigger.abl-button 0.0x0.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; button::after.js-trial-mobile-trigger.abl-button 6pxx6px border T:1px solid #0000ff / R:1px solid #0000ff; div.abl-pa-20.abl-bg-lemonade 0.0x0.0 bg #fbffa7; input.abl-form-input.abl-w-100p 0.0x0.0 bg #ffffff border T:2px solid #000000 / R:2px solid #000000 / B:2px solid #000000 / L:2px solid #000000; ul 0.0x0.0 bg #ffc2ca |
| Ancestor paint | 1 up section.abl-grid.abl-grid-cols-12 bg #ffc3a5 |
| How | at rest |

Crops: `trial-edition-card-default.png`.

### Shop

#### shop-title

Shop page title.

Page: shop. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 360 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 60px/66px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `shop-title-default.png`.

#### product-card

Product teaser card. A product tile in the shop grid (Live editions, Push, merchandise).

Page: shop. Selector: `.product-teaser`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 720 x 720 | = |
| Padding | 120px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ffc3a5 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h1: futura-pt 60px/66px 700, #000000 | = |
| Transition | none | = |
| Painted layers | div.product-teaser.product-teaser--live 720.0x720.0 bg #ffc3a5; strong::after.text-black.abl-mr-20 6pxx6px border T:1px solid #000000 / R:1px solid #000000 | = |
| How | at rest | mouse hover |

Crops: `product-card-default.png`, `product-card-hover.png`.

#### product-price

Price. A product price in the shop.

Page: shop. Selector: `.price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 72.27 x 30 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `product-price-default.png`.

#### add-to-cart

Add-to-cart button. The buy control on a shop tile. Measured, never pressed — pressing carts a product.

Page: shop. Selector: `.add_to_cart`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 360 x 44 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | futura-pt 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Painted layers | input.btn.js_add_to_cart_btn 128.3x44.0 bg #0000ff | = | input.btn.js_add_to_cart_btn 128.3x44.0 bg #0000ff outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `add-to-cart-default.png`, `add-to-cart-hover.png`, `add-to-cart-focus-visible.png`, `add-to-cart-pressed.png`.

### Packs

#### packs-title

Packs page title.

Page: packs. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200.03 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 60px/66px 700 |
| Letter spacing | normal |
| Colour | #00ffaf |
| Transition | none |
| Ancestor paint | 1 up div.packs-banner.abl-relative bg #000000 |
| How | at rest |

Crops: `packs-title-default.png`.

#### pack-card

Pack card. A Pack tile in the catalogue grid.

Page: packs. Selector: `pack teaser`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 1440 x 348 | = |
| Padding | 90px 120px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #000000 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h1.packs-banner__headline.text-malachite: futura-pt 60px/66px 700, #00ffaf | = |
| Transition | none | = |
| Painted layers | div.packs-banner.abl-relative 1440.0x348.0 bg #000000 | = |
| How | at rest | mouse hover |

Crops: `pack-card-default.png`, `pack-card-hover.png`.

#### pack-download

Pack download button. A "Download" button on a Pack row; links to /en/login/ (the download needs an account). Measured, never followed.

Page: packs. Selector: `.test-pack-download`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 143.14 x 44 | = | = | = |
| Padding | 7px 30px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #0000ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | futura-pt 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.test-pack-download 143.1x44.0 bg #0000ff | = | a.button.test-pack-download 143.1x44.0 bg #0000ff outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pack-download-default.png`, `pack-download-hover.png`, `pack-download-focus-visible.png`, `pack-download-pressed.png`.

### Blog

#### blog-title

Blog page title.

Page: blog. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200.03 x 78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 60px/78px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `blog-title-default.png`.

#### blog-row

Article teaser. An article row in the blog index.

Page: blog. Selector: `.blog-teaser`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 360 x 521.5 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span: futura-pt 14px/21px 700, #000000 | = |
| Transition | none | = |
| Painted layers | abl-click-remote.abl-mb-8.abl-mb-16-ml 360.0x202.5 bg #bfbfbf; a.abl-entry-category-badge.abl-bg-blog-category-downloads 87.3x25.0 bg #ff8389; li::before.abl-inline-block 2.8pxx2.8px bg #000000; li::before.abl-inline-block 2.8pxx2.8px bg #000000; li::before.abl-inline-block 2.8pxx2.8px bg #000000; li::before.abl-inline-block 2.8pxx2.8px bg #000000 | = |
| How | at rest | mouse hover |

Crops: `blog-row-default.png`, `blog-row-hover.png`.

#### blog-category-badge

Entry category badge. The coloured category badge on a blog index row (Artists / Downloads / Tutorials).

Page: blog. Selector: `.abl-entry-category-badge`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 87.25 x 25 | = |
| Padding | 2px 12px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #ff8389 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 14px/21px 700 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | span: futura-pt 14px/21px 700, #000000 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | a.abl-entry-category-badge.abl-bg-blog-category-downloads 87.3x25.0 bg #ff8389 | = |
| How | at rest | mouse hover |

Crops: `blog-category-badge-default.png`, `blog-category-badge-hover.png`.

### Log in / register (resting only)

#### login-title

Log in title.

Page: login. Selector: `h1.section__headline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 540 x 66 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 60px/66px 700 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| How | at rest |

Crops: `login-title-default.png`.

#### login-form

Log in form. The Log in card: username and password fields plus the submit. Measured at rest — nothing typed, nothing submitted.

Page: login. Selector: `form.test-login-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 540 x 246.38 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | label: futura-pt 14px/21px 700, #000000 |
| Transition | none |
| Painted layers | input 380.0x46.0 bg #eeeeee; input 380.0x46.0 bg #eeeeee; input.button 107.9x44.0 bg #0000ff |
| How | at rest |

Crops: `login-form-default.png`.

#### login-field

Username field. The username text field. Clicked into for the focus style; nothing typed.

Page: login. Selector: `input[name=username]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 380 x 46 | = |
| Padding | 8px 15px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #eeeeee | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 0px |
| Font | futura-pt 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input 380.0x46.0 bg #eeeeee | input.focus-visible 380.0x46.0 bg #eeeeee outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field |

Crops: `login-field-default.png`, `login-field-focused.png`.

#### login-submit

Log in button. The form's submit. Measured in every state — never pressed.

Page: login. Selector: `login submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 107.89 x 44 | = | = | = |
| Padding | 7px 30px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | #0000ff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | futura-pt 20px/30px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Placeholder | #ffffff, opacity 1 | = | = | = |
| Painted layers | input.button 107.9x44.0 bg #0000ff | = | input.button.focus-visible 107.9x44.0 bg #0000ff outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### register-form

Register form. The Register card beside Log in: email, password, names, country select and a newsletter checkbox. Measured at rest.

Page: login. Selector: `form.test-registration-form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 540 x 768.95 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | label: futura-pt 14px/21px 700, #000000 |
| Transition | none |
| Painted layers | input 380.0x46.0 bg #eeeeee; ul 0.0x0.0 bg #ffc2ca; ul::after autoxauto border T:8px solid #000000 @ 0 / R:8px solid #000000 @ 0 / B:8px solid #ffc2ca / L:8px solid #000000 @ 0; input 380.0x46.0 bg #eeeeee; input 380.0x46.0 bg #eeeeee; input 380.0x46.0 bg #eeeeee |
| How | at rest |

Crops: `register-form-default.png`.

#### register-field

Register email field. The email field of the register form. Clicked into only.

Page: login. Selector: `register email`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 380 x 46 | = |
| Padding | 8px 15px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | #eeeeee | = |
| Box shadow | none | = |
| Outline | none | 1px auto #005fcc offset 0px |
| Font | futura-pt 20px/30px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #000000, opacity 1 | = |
| Painted layers | input 380.0x46.0 bg #eeeeee | input.focus-visible 380.0x46.0 bg #eeeeee outline 1px auto #005fcc offset 0px |
| How | at rest | clicked into the field |

Crops: `register-field-default.png`, `register-field-focused.png`.

#### register-select

Country select.

Page: login. Selector: `select[name=country]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 44 |
| Padding | 7px 50px 7px 15px |
| Border | none |
| Radius | 0px |
| Background | #eeeeee |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| Painted layers | select 380.0x44.0 bg #eeeeee |
| How | at rest |

Crops: `register-select-default.png`.

#### register-checkbox

Newsletter checkbox.

Page: login. Selector: `register checkbox`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 13 x 13 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | default |
| Placeholder | #000000, opacity 1 |
| How | at rest |

Crops: `register-checkbox-default.png`.

### Mobile (390 wide)

#### m-nav-bar

Mobile top bar. The mobile header: logo left, menu trigger right.

Page: home. Selector: `header.main-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 69 |
| Padding | 20px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | button.main-nav__trigger-label.abl-btn--reset: futura-pt 20px/30px 700, #000000 |
| Transition | none |
| Icon | 60 x 28, colour #000000 |
| Painted layers | button::after.main-nav__trigger-label.abl-btn--reset 0pxx0px border T:5px solid #000000 / R:5px solid #000000 @ 0 / B:5px solid #000000 @ 0 / L:5px solid #000000 @ 0; div.main-nav__primary-wrapper.main-nav__primary-wrapper--collapses 390.0x1004.0 bg #0000ff; span::before.main-nav__icon.main-nav__icon--collapse 12pxx2px bg #ffffff; span::before.main-nav__icon.main-nav__icon--expand 12pxx2px bg #ffffff; span::after.main-nav__icon.main-nav__icon--expand 2pxx12px bg #ffffff; div::after.main-nav__slideable-wrapper 40pxx84px image linear-gradient(90deg, #0000ff @ 0, #0000ff) |
| Ancestor paint | 1 up div.main.js-main bg #ffffff |
| How | at rest |

Crops: `m-nav-bar-default.png`.

#### m-menu-trigger

Mobile menu trigger. The mobile menu button. Measured, not opened.

Page: home. Selector: `menu trigger`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 64.06 x 30 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 20px/30px 700 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Transition | color 0.35s ease | = |
| Cursor | pointer | = |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px | = |
| Painted layers | button::after.main-nav__trigger-label.abl-btn--reset 0pxx0px border T:5px solid #000000 / R:5px solid #000000 @ 0 / B:5px solid #000000 @ 0 / L:5px solid #000000 @ 0 | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-menu-trigger-default.png`, `m-menu-trigger-pressed.png`.

#### m-hero-title

Mobile hero headline.

Page: home. Selector: `.homepage-teaser__primary-headline`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 325.03 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | futura-pt 20px/30px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `m-hero-title-default.png`.

#### m-trial-cta

Mobile trial CTA.

Page: home. Selector: `mobile trial cta`. States: default, pressed.

| Property | default | pressed |
|---|---|---|
| Size (w x h) | 147.95 x 26 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | futura-pt 20px/30px 700 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | CDP forcePseudoState :active:hover |

Crops: `m-trial-cta-default.png`, `m-trial-cta-pressed.png`.

## Transitions declared in the readable stylesheets

ableton.com's stylesheets are SASS-built and same-origin readable, but they declare almost no custom properties — the design values live in its compiled BEM classes, read as computed styles above; the per-state Transition rows are computed values.

- about: none

- blog: none

- help: none

- home: none

- jobs: none

- link: none

- live: none

- login: none

- move: none

- note: none

- packs: none

- push: none

- shop: none

- trial: none
