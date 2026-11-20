# Component measurements — forhers.com

Computed styles read on 2026-11-17 by `tools/capture/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

www.forhers.com answers every automated request from this network with a Cloudflare managed challenge (HTTP 403), so the DOM is Wayback Machine SSR snapshots served locally — the real markup painted by the archived styled-components and inline sheets, with every script removed. Elements hydration would own — the slide menu, login menu, accordion expansion, carousels, the quiz/intake flow and "Read more" — cannot open, so those states are absent rather than faked. Some archived sheets and assets never resolved; those gaps are documented per page.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and site chrome

#### header

Header. The top chrome: promo bar over the nav row (wordmark, category links, Log in, hamburger).

Page: mental-health. Selector: `navigation-mast / GlobalNavigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 57 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Icon | 57.59 x 24, colour #000000 @ 0.89, fill #000000 |
| Painted layers | div._exterior_152ff_19 1440.0x57.0 bg #ffffff; button._reset_5zh37_19._base_5zh37_28 304.0x304.0 bg #efefef border T:2px outset #000000 / R:2px outset #000000 / B:2px outset #000000 / L:2px outset #000000 |
| How | at rest |

Crops: `header-default.png`.

#### promo-bar

Promo bar. The lime announcement strip ("Peptides+ is coming soon" / "The GLP-1 pill is here") with a tertiary CTA link.

Page: hair-loss. Selector: `data-navigation-banner`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 44 |
| Padding | 0px 20px 5px 20px |
| Gap | 4px 8px |
| Border | none |
| Radius | 0px |
| Background | #bff8b1 |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | strong.options_marks_bold__by1BQ: CareSans 15.6667px/20.0238px 600, #000000 @ 0.81, ls 0.354276px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | pointer |
| ::before | 16px x 32px, absolute, bg #000000 @ 0, radius 16px 0px 0px, shadow #bff8b1 0px -16px 0px 0px |
| ::after | 16px x 32px, absolute, bg #000000 @ 0, radius 0px 16px 0px 0px, shadow #bff8b1 0px -16px 0px 0px |
| Painted layers | section._navigation-banner_1e874_11._navigation-banner-transition_1e874_26 1440.0x44.0 bg #bff8b1; section::before._navigation-banner_1e874_11._navigation-banner-transition_1e874_26 16pxx32px r 16px 0px 0px shadow #bff8b1 0px -16px 0px 0px; section::after._navigation-banner_1e874_11._navigation-banner-transition_1e874_26 16pxx32px r 0px 16px 0px 0px shadow #bff8b1 0px -16px 0px 0px |
| How | at rest |

Crops: `promo-bar-default.png`.

#### logo

Wordmark. The "hers" serif wordmark linking home; measured, never followed.

Page: mental-health. Selector: `nav logo link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 57.59 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CareSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.89 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 57.59 x 24, colour #000000 @ 0.89, fill #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `logo-default.png`, `logo-hover.png`, `logo-focus-visible.png`, `logo-pressed.png`.

#### nav-link

Nav link. A category link in the nav row; measured, never followed.

Page: skin-care. Selector: `nav link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 36.03 x 18 | = | = | = |
| Padding | 0px 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CareSans 12px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.65 | #000000 @ 0.89 | #000000 @ 0.89 | #000000 @ 0.89 |
| Transition | text-decoration-color, color 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-pressed.png`.

#### login-button

Log in control. The "Log in" button/link; measured, never pressed — its menu and the account are hydration- and auth-gated.

Page: mental-health. Selector: `GlobalNavigationLogin / Log in link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 43.59 x 24 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | CareSans 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #0000ee | = | - | #ff0000 |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `login-button-default.png`, `login-button-hover.png`, `login-button-pressed.png`.

#### menu-toggle

Menu toggle. The hamburger that opens the slide menu; measured, never toggled (the drawer needs hydration).

Page: home. Selector: `GlobalNavigationButton`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 42 x 42 | = | = | = |
| Padding | 0px | = | = | = |
| Border | T: none; R: none; B: 2px solid #000000 @ 0; L: none | = | = | = |
| Radius | 48px | = | = | = |
| Background | transparent | #000000 @ 0.06 | = | #000000 @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CareSans 12px/12px 600 | = | = | = |
| Letter spacing | 1.5px | = | = | = |
| Colour | #000000 @ 0.89 | = | = | = |
| Transition | color, background-color, box-shadow, fill, stroke 0.3s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #000000 @ 0.89, fill #000000 | = | = | = |
| ::before | auto x calc(100% + 2px), absolute, bg #000000 @ 0, radius 48px | = | = | = |
| Painted layers | button.elements-style__ButtonReset-sc-82b26c75-0.link-style__ButtonLink-sc-67ab2a15-1 42.0x42.0 border B:2px solid #000000 @ 0 r 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.link-style__ButtonLink-sc-67ab2a15-1 autoxcalc(100% + 2px) border T:1px solid #000000 @ 0.03 / R:1px solid #000000 @ 0.03 / B:1px solid #000000 @ 0.03 / L:1px solid #000000 @ 0.03 r 48px | button.elements-style__ButtonReset-sc-82b26c75-0.link-style__ButtonLink-sc-67ab2a15-1 42.0x42.0 bg #000000 @ 0.06 border B:2px solid #000000 @ 0 r 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.link-style__ButtonLink-sc-67ab2a15-1 autoxcalc(100% + 2px) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 48px | = | button.elements-style__ButtonReset-sc-82b26c75-0.link-style__ButtonLink-sc-67ab2a15-1 42.0x42.0 bg #000000 @ 0.06 border B:2px solid #000000 @ 0 r 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.link-style__ButtonLink-sc-67ab2a15-1 autoxcalc(100% + 2px) border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 48px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `menu-toggle-default.png`, `menu-toggle-hover.png`, `menu-toggle-focus-visible.png`, `menu-toggle-pressed.png`.

### Home page (marketing stack)

#### hero-heading

Hero headline. "The care you’ve always deserved" — the IvarSoft serif hero.

Page: home. Selector: `first h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 114 |
| Padding | 0px 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 57px/57px 410 |
| Letter spacing | -0.57px |
| Colour | #000000 @ 0.88 |
| Transition | none |
| How | at rest |

Crops: `hero-heading-default.png`.

#### bento-card

Bento card. A hero bento tile (category card: headline, image, arrow); measured, never followed.

Page: home. Selector: `BentoContentCard`. States: none.

Selector matched the wrong element (see measure.mjs). Not republished as this component until a recapture with the scoped selector.

#### tile-card

Category tile. A category entry tile ("Grow fuller hair" / "Treat menopause"); measured, never followed.

Page: home. Selector: `category tile link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 337 x 100 | = |
| Padding | 0px 8px 0px 16px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | transparent | = |
| Background image | linear-gradient(167deg, #e4eee6 0%, #f2f9f4 38%, #f2f9f4 84%, #e4eee6 100%) | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | CareSans 16px/22.4px 400 | = |
| Letter spacing | -0.176px | = |
| Colour | #0000ee | = |
| Text node | span.sc-aXZVg.tile-content-style__TileContentTypography-sc-b801c808-2: CareSans 19px/23.6906px 400, #3e4f49, ls 0.409687px | span.sc-aXZVg.tile-content-style__TileContentTypography-sc-b801c808-2: CareSans 19px/23.6906px 400, #fcfcfc @ 0.514, ls 0.409687px |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 6.45 x 12, colour #0000ee | = |
| ::before | 337px x 100px, absolute, bg #000000 @ 0 linear-gradient(167deg, #194737 -3.36%, #3b5b50 33.89%, #3b5b50 79.75%, #194737 95.99%), radius 24px | = |
| Painted layers | a.treatment-tile-style__TreatmentTileLink-sc-618313ed-1.dfWlvi 337.0x100.0 image linear-gradient(167deg, #e4eee6 0%, #f2f9f4 38%, #f2f9f4 84%, #e4eee6 100%) r 24px; a::before.treatment-tile-style__TreatmentTileLink-sc-618313ed-1.dfWlvi 337pxx100px image linear-gradient(167deg, #194737 -3.36%, #3b5b50 33.89%, #3b5b50 79.75%, #194737 95.99%) r 24px | = |
| How | at rest | mouse hover |

Crops: `tile-card-default.png`, `tile-card-hover.png`.

#### quiz-tile

Quiz entry tile. The "Unsure where to begin? Start here" quiz entry tile; measured, never followed (the quiz is a client app).

Page: home. Selector: `tile with Start here`. States: none.

Not found on the page at capture time.

#### product-card

Product card. A GLP-1 product card in the lineup rail (image, name, drug, price, CTA).

Page: home. Selector: `wl-sidekick ProductCard`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 320 x 389 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | CareSans 16px/22.4px 400 | = |
| Letter spacing | -0.176px | = |
| Colour | #ffffff | = |
| Text node | h4.sc-aXZVg.wl-sidekick-style__ProductTitle-sc-6d946ce3-10: CareSans 28px/31.5px 460, #ffffff, ls -0.0466693px | = |
| Transition | opacity 0.2s linear | = |
| Opacity | 0 | = |
| Painted layers | a.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320.0x389.0 image linear-gradient(#9fb089, #7b8967) r 24px; a::after.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320pxx389px image linear-gradient(#7d8f66, #536240); div::after.wl-sidekick-style__ProductImageWrapper-sc-6d946ce3-2.iA-DSMA 64pxx8px image radial-gradient(#000000 @ 0.3, #000000 @ 0 80%) r 50% | a.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 329.6x400.7 image linear-gradient(#9fb089, #7b8967) r 24px; a::after.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320pxx389px image linear-gradient(#7d8f66, #536240); div::after.wl-sidekick-style__ProductImageWrapper-sc-6d946ce3-2.iA-DSMA 64pxx8px image radial-gradient(#000000 @ 0.3, #000000 @ 0 80%) r 50% |
| How | at rest | mouse hover |

Crops: `product-card-hover.png`.

#### fda-badge

FDA badge. The "FDA-approved" badge on a product card.

Page: home. Selector: `FdaBadge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 56 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/22.4px 400 |
| Letter spacing | -0.176px |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `fda-badge-default.png`.

#### testimonial

Testimonial card. A testimonial slide (quote, user photo, name) in the carousel.

Page: home. Selector: `TestimonialCard/SlideItem`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 546 x 745.25 |
| Padding | 0px 36px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/22.4px 400 |
| Letter spacing | -0.176px |
| Colour | #ffffff |
| Text node | p.testimonial-card-style__Quote-sc-179bb82b-9.hPiLra: CareSans 25px/24.85px 400, #b4cdc4, ls -0.176px |
| Transition | none |
| How | at rest |

Crops: `testimonial-default.png`.

#### app-cta

Section CTA. A mid-page secondary CTA ("Meet the app" / "Learn more"); measured, never followed.

Page: home. Selector: `section CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 151.48 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CareSans 16px/22.4px 400 | = | = | = |
| Letter spacing | -0.176px | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.sc-aXZVg.wl-secton-nn-style__ButtonLabel-sc-40ecf109-3: CareSans 16px/19.2px 500, #343c2b, ls 0.04px | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 151.5x48.0 bg #c5ed82 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 155.484pxx52px border T:2px solid #ffffff @ 0 / R:2px solid #ffffff @ 0 / B:2px solid #ffffff @ 0 / L:2px solid #ffffff @ 0 r 48px | button.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 151.5x48.0 bg #9dbd67 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 155.484pxx52px border T:2px solid #ffffff @ 0 / R:2px solid #ffffff @ 0 / B:2px solid #ffffff @ 0 / L:2px solid #ffffff @ 0 r 48px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-cta-hover.png`, `app-cta-focus-visible.png`, `app-cta-pressed.png`.

### Shop pages (weight-loss, hair, skin, mental-health, birth-control, product, labs, benefits)

#### page-heading

Page heading. The serif section heading ("Weight loss that works" / "Lose weight the way you want").

Page: mental-health. Selector: `first h1/section headings`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 781.08 x 52.83 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 52.8333px/52.8333px 410 |
| Letter spacing | -0.528333px |
| Colour | #000000 @ 0.81 |
| Transition | none |
| How | at rest |

Crops: `page-heading-default.png`.

#### page-dek

Section dek. The body copy beside the section heading.

Page: mental-health. Selector: `page-section-remaining p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 557.92 x 46.31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 18.5px/23.1537px 400 |
| Letter spacing | 0.401913px |
| Colour | #000000 @ 0.5 |
| Text node | em.options_marks_with-gradient__yWDlC.options_marks_reset__pynUw: CareSans 18.5px/23.1537px 400, #000000 @ 0.5, ls 0.401913px |
| Transition | none |
| Painted layers | em.options_marks_with-gradient__yWDlC.options_marks_reset__pynUw 516.3x44.2 image linear-gradient(135deg, #5d62c8 -0.03%, #5e91d6 32.99%, #6cc2d6 66.01%, #8fdfc5 100.03%) |
| How | at rest |

Crops: `page-dek-default.png`.

#### cta-primary

Primary CTA. The dark-green pill primary action ("Start losing weight" / "Go to membership"); measured, never followed.

Page: mental-health. Selector: `data-variant=primary / _format-primary-*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 173.41 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | CareSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span: CareSans 16px/24px 400, #0000ee | = | = | span: CareSans 16px/24px 400, #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._reset_5zh37_19._base_5zh37_28 173.4x17.0 outline 1px auto #101010 offset 1px | = |

Crops: `cta-primary-default.png`, `cta-primary-hover.png`, `cta-primary-focus-visible.png`, `cta-primary-pressed.png`.

#### cta-secondary

Secondary CTA. The outlined secondary action ("Get started"); measured, never followed.

Page: skin-care. Selector: `_format-secondary-* inside main/card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 388 x 48 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | 1px solid #000000 @ 0.19 | 1px solid #000000 @ 0 | 1px solid #000000 @ 0 | 1px solid #000000 @ 0 |
| Radius | 9999px | = | = | = |
| Background | #ffffff @ 0.01 | #000000 @ 0.65 | #000000 @ 0.65 | #000000 @ 0.74 |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(10px) | = | = | = |
| Outline | 1px solid #000000 @ 0 offset 0px | = | 1px solid #000000 @ 0 offset 3px | = |
| Font | CareSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.89 | #ffffff | #ffffff | #ffffff |
| Text node | strong.options_marks_bold__by1BQ: CareSans 16px/24px 600, #000000 @ 0.89 | strong.options_marks_bold__by1BQ: CareSans 16px/24px 600, #ffffff | strong.options_marks_bold__by1BQ: CareSans 16px/24px 600, #ffffff | strong.options_marks_bold__by1BQ: CareSans 16px/24px 600, #ffffff |
| Transition | border-color, color, background-color, box-shadow, outline-offset, outline-color, text-decoration-color 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button._reset_5zh37_19._base_5zh37_28 388.0x48.0 bg #ffffff @ 0.01 border T:1px solid #000000 @ 0.19 / R:1px solid #000000 @ 0.19 / B:1px solid #000000 @ 0.19 / L:1px solid #000000 @ 0.19 r 9999px outline 1px solid #000000 @ 0 offset 0px | button._reset_5zh37_19._base_5zh37_28 388.0x48.0 bg #000000 @ 0.65 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #000000 @ 0 offset 0px | button._reset_5zh37_19._base_5zh37_28 388.0x48.0 bg #000000 @ 0.65 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #000000 @ 0 offset 3px | button._reset_5zh37_19._base_5zh37_28 388.0x48.0 bg #000000 @ 0.74 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`.

#### cta-tertiary

Tertiary CTA. The quiet tertiary action ("View details"); measured, never followed.

Page: skin-care. Selector: `_format-tertiary-*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 188.67 x 48 | = | = | = |
| Padding | 8px 24px | = | = | = |
| Border | 1px solid #000000 @ 0 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | #000000 @ 0.06 | #000000 @ 0.65 | #000000 @ 0.65 | #000000 @ 0.74 |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(10px) | = | = | = |
| Outline | 1px solid #000000 @ 0 offset 0px | = | 1px solid #000000 @ 0 offset 3px | = |
| Font | CareSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.89 | #ffffff | #ffffff | #ffffff |
| Text node | span: CareSans 16px/24px 400, #000000 @ 0.89 | span: CareSans 16px/24px 400, #ffffff | span: CareSans 16px/24px 400, #ffffff | span: CareSans 16px/24px 400, #ffffff |
| Transition | border-color, color, background-color, box-shadow, outline-offset, outline-color, text-decoration-color 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a._reset_5zh37_19._base_5zh37_28 188.7x48.0 bg #000000 @ 0.06 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #000000 @ 0 offset 0px | a._reset_5zh37_19._base_5zh37_28 188.7x48.0 bg #000000 @ 0.65 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #000000 @ 0 offset 0px | a._reset_5zh37_19._base_5zh37_28 188.7x48.0 bg #000000 @ 0.65 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #000000 @ 0 offset 3px | a._reset_5zh37_19._base_5zh37_28 188.7x48.0 bg #000000 @ 0.74 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #000000 @ 0 offset 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-tertiary-hover.png`, `cta-tertiary-focus-visible.png`, `cta-tertiary-pressed.png`.

#### cta-underlined

Underlined link. The underlined "Important safety information" action; measured, never followed.

Page: mental-health. Selector: `_format-underlined-*`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 198.31 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | CareSans 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span: CareSans 16px/24px 400, #0000ee | = | = | span: CareSans 16px/24px 400, #ff0000 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a._reset_5zh37_19._base_5zh37_28 198.3x17.0 outline 1px auto #101010 offset 1px | = |

Crops: `cta-underlined-default.png`, `cta-underlined-hover.png`, `cta-underlined-focus-visible.png`, `cta-underlined-pressed.png`.

#### content-card

Content card. A rounded media-first content card in the rails (gradient surface, image, heading, CTA stack).

Page: mental-health. Selector: `data-content=componentngcontentcard`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 438 x 584 | = |
| Padding | 25px | = |
| Gap | 20px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | CareSans 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 | = |
| Text node | h4._text-heading-s-max-medium_ncjzh_245._text-heading-s-min-medium-max-large_ncjzh_663: CareSans 26.6667px/30.2222px 500, #000000 @ 0.81, ls -0.0301333px | = |
| Transition | none | = |
| How | at rest | mouse hover |

Crops: `content-card-default.png`, `content-card-hover.png`.

#### treatment-card

Treatment card. A medication treatment card (name, drug, price "From $149/mo", CTA stack).

Page: home. Selector: `treatment-card / ProductCard`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 320 x 389 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | CareSans 16px/22.4px 400 | = |
| Letter spacing | -0.176px | = |
| Colour | #ffffff | = |
| Text node | h4.sc-aXZVg.wl-sidekick-style__ProductTitle-sc-6d946ce3-10: CareSans 28px/31.5px 460, #ffffff, ls -0.0466693px | = |
| Transition | opacity 0.2s linear | = |
| Opacity | 0 | = |
| Painted layers | a.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320.0x389.0 image linear-gradient(#9fb089, #7b8967) r 24px; a::after.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320pxx389px image linear-gradient(#7d8f66, #536240); div::after.wl-sidekick-style__ProductImageWrapper-sc-6d946ce3-2.iA-DSMA 64pxx8px image radial-gradient(#000000 @ 0.3, #000000 @ 0 80%) r 50% | a.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 329.6x400.7 image linear-gradient(#9fb089, #7b8967) r 24px; a::after.wl-sidekick-style__ProductCard-sc-6d946ce3-4.gFjMRV 320pxx389px image linear-gradient(#7d8f66, #536240); div::after.wl-sidekick-style__ProductImageWrapper-sc-6d946ce3-2.iA-DSMA 64pxx8px image radial-gradient(#000000 @ 0.3, #000000 @ 0 80%) r 50% |
| How | at rest | mouse hover |

Crops: `treatment-card-default.png`, `treatment-card-hover.png`.

#### card-price

Price line. The "From $149/mo †" price line on a treatment/product card.

Page: home. Selector: `price text inside a card`. States: none.

Selector matched the wrong element (see measure.mjs). Not republished as this component until a recapture with the scoped selector.

#### accordion

Accordion. The FAQ accordion block; the first panel ships open in SSR, toggles need hydration.

Page: mental-health. Selector: `accordion_* / AccordionWrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 616 x 325 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | p._text-label-m-max-medium_ncjzh_173._text-label-m-min-medium-max-large_ncjzh_591: CareSans 15.6667px/18.8326px 500, #000000 @ 0.81, ls 0.0407856px |
| Transition | none |
| Painted layers | div::before._accordion-icon_1wnp5_28 10.5pxx2px bg #000000 @ 0.88 r 4px 0px 0px 4px; div::after._accordion-icon_1wnp5_28 10.5pxx2px bg #000000 @ 0.88 r 0px 4px 4px 0px; div._visibility-precluded_1wnp5_147._content_1wnp5_94 616.0x1.0 border B:1px solid #000000 @ 0.12; div::before._accordion-icon_1wnp5_28 10.5pxx2px bg #000000 @ 0.88 r 4px 0px 0px 4px; div::after._accordion-icon_1wnp5_28 10.5pxx2px bg #000000 @ 0.88 r 0px 4px 4px 0px; div._visibility-precluded_1wnp5_147._content_1wnp5_94 616.0x1.0 border B:1px solid #000000 @ 0.12 |
| How | at rest |

Crops: `accordion-default.png`.

#### accordion-toggle

Accordion toggle. An accordion row toggle (title + icon); measured, never toggled.

Page: mental-health. Selector: `accordion heading/title`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 575 x 18.83 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 20px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | CareSans 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | p._text-label-m-max-medium_ncjzh_173._text-label-m-min-medium-max-large_ncjzh_591: CareSans 15.6667px/18.8326px 500, #000000 @ 0.81, ls 0.0407856px | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `accordion-toggle-default.png`, `accordion-toggle-hover.png`, `accordion-toggle-pressed.png`.

#### disclaimer

Disclaimer. The collapsed legal disclaimer block (grey text, expandable).

Page: mental-health. Selector: `disclaimer_frame / DisclaimerWrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 800.86 x 40.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: CareSans 15.6667px/20.0238px 600, #000000 @ 0.81, ls 0.354276px |
| Transition | none |
| How | at rest |

Crops: `disclaimer-default.png`.

#### read-more

Read more toggle. The "Read more" disclaimer toggle; measured, never toggled.

Page: weight-loss. Selector: `DisclaimerToggle / ReadMore_button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66.72 x 15.66 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 0px | = |
| Font | CareSans 12.8333px/15.654px 600 | = | = | = |
| Letter spacing | 0.0448097px | = | = | = |
| Colour | #000000 @ 0.37 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.ReadMore_button__B36Ye 66.7x15.7 outline 1px auto #101010 offset 0px | = |

Crops: `read-more-hover.png`, `read-more-focus-visible.png`, `read-more-pressed.png`.

#### carousel-arrow

Carousel arrow. A carousel next/previous control; measured, never pressed.

Page: home. Selector: `carousel-controls button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 48 x 48 | = | - | = |
| Padding | 1px 6px | = | - | = |
| Border | 2px solid #ffffff @ 0.11 | = | - | = |
| Radius | 100% | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | CareSans 16px/18.4px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff @ 0.11 | = | - | = |
| Transition | color, border-color 0.3s ease-in-out | = | - | = |
| Transform | matrix(1, 0, 0, 1, 0, -24) | = | - | = |
| Cursor | default | = | - | = |
| Icon | 24 x 24, colour #ffffff @ 0.11, fill #000000 | = | - | = |
| Painted layers | button.testimonial-card-style__SlideNavigationButton-sc-179bb82b-4.hLBlZn 48.0x48.0 border T:2px solid #ffffff @ 0.11 / R:2px solid #ffffff @ 0.11 / B:2px solid #ffffff @ 0.11 / L:2px solid #ffffff @ 0.11 r 100% | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `carousel-arrow-default.png`, `carousel-arrow-hover.png`, `carousel-arrow-pressed.png`.

#### slide-dot

Slide indicator. A carousel position dot; measured, never pressed.

Page: home. Selector: `SlideIndicatorDot`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 60 x 12 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 4px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | CareSans 16px/22.4px 400 | = | - | = |
| Letter spacing | -0.176px | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | transform 0.3s ease | = | - | = |
| Painted layers | span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 12.0x12.0 bg #ffffff r 100%; span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 10.0x10.0 bg #ffffff @ 0.1 r 100%; span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 10.0x10.0 bg #ffffff @ 0.1 r 100%; span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 8.0x8.0 bg #ffffff @ 0.1 r 100%; span.testimonial-card-style__SlideIndicatorDot-sc-179bb82b-15.dDiWwq 0.0x0.0 bg #ffffff @ 0.1 r 100% | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `slide-dot-default.png`, `slide-dot-hover.png`, `slide-dot-pressed.png`.

### Footer

#### footer

Footer. The site footer: link columns, social icons, legal fineprint row.

Page: mental-health. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1774.95 |
| Padding | 90px 60px 60px 60px |
| Border | none |
| Radius | 0px |
| Background | #f0f0f0 |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: CareSans 12.8333px/15.654px 490.75, #000000 @ 0.65, ls 0.0448097px |
| Transition | none |
| Icon | 10 x 12, colour #000000 @ 0.65 |
| Painted layers | footer._footer_13xxf_2._set-footer-text-color-default_k2duq_2 1440.0x1775.0 bg #f0f0f0; div::before.breadcrumbs-styles_breadcrumbs__mPB4k 80pxx46px image linear-gradient(to right, #f0f0f0, #ffffff @ 0); div::after.breadcrumbs-styles_breadcrumbs__mPB4k 100pxx46px image linear-gradient(to right, #ffffff @ 0, #f0f0f0); article._frame_1jop7_2 264.4x850.0 bg #000000 @ 0.06 r 24px; div._download-cta-desktop_1jop7_42 178.0x86.0 bg #000000 @ 0.06 r 8px; li._social-link_80bzd_37 48.0x48.0 bg #000000 @ 0.06 r 50% |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A footer column link; measured, never followed.

Page: mental-health. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 113.8 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CareSans 12.8333px/16.7434px 400 | = | = | = |
| Letter spacing | 0.301476px | = | = | = |
| Colour | #000000 @ 0.89 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-fineprint

Fineprint link. A legal fineprint link in the footer's last row; measured, never followed.

Page: mental-health. Selector: `fineprint-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 227.75 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CareSans 12.8333px/16.7434px 400 | = | = | = |
| Letter spacing | 0.301476px | = | = | = |
| Colour | #000000 @ 0.89 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-fineprint-default.png`, `footer-fineprint-hover.png`, `footer-fineprint-focus-visible.png`, `footer-fineprint-pressed.png`.

#### footer-social

Social icon link. A social icon link in the footer; measured, never followed.

Page: mental-health. Selector: `footer a:has(svg)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 20 x 20 | = | = | = |
| Padding | 0px 5px | = | = | = |
| Border | none | = | = | = |
| Radius | 100% | = | = | = |
| Background | transparent | #000000 @ 0.06 | #000000 @ 0.06 | #000000 @ 0.06 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | CareSans 12px/18px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.65 | #000000 @ 0.89 | #000000 @ 0.89 | #000000 @ 0.89 |
| Transition | background-color 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 10 x 12, colour #000000 @ 0.65 | 10 x 12, colour #000000 @ 0.89 | 10 x 12, colour #000000 @ 0.89 | 10 x 12, colour #000000 @ 0.89 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a 20.0x20.0 bg #000000 @ 0.06 r 100% | a 20.0x20.0 bg #000000 @ 0.06 r 100% | a 20.0x20.0 bg #000000 @ 0.06 r 100% |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

### Content pages (blog, article, quality, drugs-info)

#### article-card

Article card. An article card on the blog index; measured, never followed.

Page: blog. Selector: `article/card link`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 691.89 x 389.19 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sofia-pro 16px/22.4px 400 | = |
| Letter spacing | normal | = |
| Colour | #000000 @ 0.89 | = |
| Transition | none | = |
| Cursor | pointer | = |
| Painted layers | div.sc-46d8ac7e-2.emlLAx 691.9x389.2 bg #000000 @ 0.06 | div.sc-46d8ac7e-2.emlLAx 705.7x397.0 bg #000000 @ 0.06 |
| How | at rest | mouse hover |

Crops: `article-card-default.png`, `article-card-hover.png`.

#### blog-topic

Topic link. A blog topic/category link; measured, never followed.

Page: blog. Selector: `topic link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 64 | = | = | 132.05 x 60.8 |
| Padding | 0px 32px | = | = | = |
| Border | none | = | = | = |
| Radius | 100px | = | = | = |
| Background | #000000 @ 0.06 | #000000 @ 0.89 | #000000 @ 0.89 | #000000 @ 0.89 |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(20px) | = | = | = |
| Outline | none | = | = | = |
| Font | sofia-pro 14px/19.6px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.89 | #ffffff | #ffffff | #ffffff |
| Transition | background, color, transform 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.sc-ce0a9025-0.sc-94c05b7-6 139.0x64.0 bg #000000 @ 0.06 r 100px | a.sc-ce0a9025-0.sc-94c05b7-6 139.0x64.0 bg #000000 @ 0.89 r 100px | a.sc-ce0a9025-0.sc-94c05b7-6 139.0x64.0 bg #000000 @ 0.89 r 100px | a.sc-ce0a9025-0.sc-94c05b7-6 132.0x60.8 bg #000000 @ 0.89 r 100px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.95, 0, 0, 0.95, 0, 0) |

Crops: `blog-topic-default.png`, `blog-topic-hover.png`, `blog-topic-focus-visible.png`, `blog-topic-pressed.png`.

#### region-dialog

Regional redirect card. The "It looks like you’re visiting from Canada" redirect card, the one dialog the signed-out SSR paints. Its CTA was measured, never followed; the card was hidden, never answered.

Page: drugs-info. Selector: `RegionalRedirectPopupWrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 388 x 234.39 |
| Padding | 0px |
| Border | 1px solid #000000 @ 0.06 |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.08 0px 20px 40px 0px |
| Outline | none |
| Font | sofia-pro 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.89 |
| Text node | h4.regional-redirect-popupstyle__RegionalRedirectCaption-web-components__sc-o05fs-3.Seote: sofia-pro 24px/32px 400, #000000 @ 0.89 |
| Transition | none |
| Icon | 16 x 16, colour #000000 |
| Painted layers | div.regional-redirect-popupstyle__RegionalRedirectPopupWrapper-web-components__sc-o05fs-0.dVvNUF 388.0x234.4 bg #ffffff border T:1px solid #000000 @ 0.06 / R:1px solid #000000 @ 0.06 / B:1px solid #000000 @ 0.06 / L:1px solid #000000 @ 0.06 r 16px shadow #000000 @ 0.08 0px 20px 40px 0px; button.elementsstyle__ButtonReset-web-components__sc-u730hl-0.regional-redirect-popupstyle__RegionalRedirectCloseButton-web-components__sc-o05fs-6 24.0x24.0 bg #ffffff border T:1px solid #000000 @ 0.03 / R:1px solid #000000 @ 0.03 / B:1px solid #000000 @ 0.03 / L:1px solid #000000 @ 0.03 r 100% shadow #000000 @ 0.08 0px 6px 16px 0px; a.regional-redirect-popupstyle__RegionalRedirectLink-web-components__sc-o05fs-5.jKYbck 338.0x48.4 border T:1px solid #000000 @ 0.89 / R:1px solid #000000 @ 0.89 / B:1px solid #000000 @ 0.89 / L:1px solid #000000 @ 0.89 r 9999px |
| How | at rest |

Crops: `region-dialog-default.png`.

#### region-cta

Redirect CTA. The "Go to forhers.ca" pill button inside the redirect card; measured, never followed.

Page: drugs-info. Selector: `RegionalRedirectLink`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 338 x 48.39 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Gap | 8px | = | = | = |
| Border | 1px solid #000000 @ 0.89 | = | = | = |
| Radius | 9999px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sofia-pro 16px/22.4px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.89 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #000000 @ 0.89 | = | = | = |
| Painted layers | a.regional-redirect-popupstyle__RegionalRedirectLink-web-components__sc-o05fs-5.jKYbck 338.0x48.4 border T:1px solid #000000 @ 0.89 / R:1px solid #000000 @ 0.89 / B:1px solid #000000 @ 0.89 / L:1px solid #000000 @ 0.89 r 9999px | = | a.regional-redirect-popupstyle__RegionalRedirectLink-web-components__sc-o05fs-5.jKYbck 338.0x48.4 border T:1px solid #000000 @ 0.89 / R:1px solid #000000 @ 0.89 / B:1px solid #000000 @ 0.89 / L:1px solid #000000 @ 0.89 r 9999px outline 1px auto #101010 offset 1px | = |
| Ancestor paint | 2 up div.regional-redirect-popupstyle__RegionalRedirectPopupWrapper-web-components__sc-o05fs-0.dVvNUF bg #ffffff shadow #000000 @ 0.08 0px 20px 40px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.85 | 0.85 | 0.85 |

Crops: `region-cta-default.png`, `region-cta-hover.png`, `region-cta-focus-visible.png`, `region-cta-pressed.png`.

#### article-title

Article title. The article H1.

Page: blog-post. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 648.5 x 130.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 62px/65.1px 500 |
| Letter spacing | -4.34px |
| Colour | #000000 @ 0.89 |
| Transition | none |
| How | at rest |

Crops: `article-title-default.png`.

#### prose-p

Body paragraph. A body paragraph in the article prose.

Page: blog-post. Selector: `article p`. States: none.

Selector matched the wrong element (see measure.mjs). Not republished as this component until a recapture with the scoped selector.

#### prose-h2

Section heading. An in-article section heading.

Page: blog-post. Selector: `article h2`. States: none.

Not found on the page at capture time.

#### prose-link

Inline link. An inline link inside the article body; measured, never followed.

Page: blog-post. Selector: `article p a`. States: none.

Not found on the page at capture time.

#### prose-list

List item. A list item in the article body.

Page: blog-post. Selector: `article li`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 0 x 0 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 16px/24.8889px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.89 |
| Transition | none |
| How | at rest |

Crops: none.

#### byline

Byline block. The author/reviewer byline under the title.

Page: blog-post. Selector: `author/byline/caption`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 648.5 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 12px/20px 500 |
| Letter spacing | normal |
| Colour | #000000 @ 0.44 |
| Transition | none |
| How | at rest |

Crops: `byline-default.png`.

#### prose-h

Heading. A heading on the quality/safety page.

Page: quality. Selector: `h1/h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 694 x 69.44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 62px/69.44px 400 |
| Letter spacing | -3.875px |
| Colour | #ffffff |
| Text node | span.cactus-typography-component__TypographyBase-sc-22492af4-0.bgiBTD: sofia-pro 12px/12px 500, #ffffff, ls -0.0494118px |
| Transition | none |
| Painted layers | span.cactus-typography-component__TypographyBase-sc-22492af4-0.bgiBTD 147.8x24.0 bg #338585 r 46px |
| How | at rest |

Crops: `prose-h-default.png`.

#### prose-body

Body text. A body paragraph.

Page: quality. Selector: `main p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 752 x 168 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 20px/28px 400 |
| Letter spacing | -0.317647px |
| Colour | #000000 @ 0.65 |
| Transition | none |
| How | at rest |

Crops: `prose-body-default.png`.

#### az-chip

A-Z chip. A grey circular letter chip in "Browse A-Z"; measured, never followed.

Page: drugs-info. Selector: `A-Z letter link`. States: none.

Not found on the page at capture time.

#### drug-link

Drug link. A medication link in the "Popular Medications" list; measured, never followed.

Page: drugs-info. Selector: `drug name link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 455 x 37.34 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sofia-pro 29px/37.35px 400 | = | = | = |
| Letter spacing | -0.72px | = | = | = |
| Colour | #0077ab | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.sc-7735162f-0.hbdJaM 455.0x37.3 outline 1px auto #101010 offset 1px | = |

Crops: `drug-link-default.png`, `drug-link-hover.png`, `drug-link-focus-visible.png`, `drug-link-pressed.png`.

#### page-lede

Page lede. The page heading/dek block.

Page: drugs-info. Selector: `h1 + description`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 964 x 83.75 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 87px/83.75px 400 |
| Letter spacing | -6.41px |
| Colour | #000000 @ 0.89 |
| Transition | none |
| Painted layers | span 422.5x112.0 image linear-gradient(135deg, #5d62c8 -0.03%, #5e91d6 32.99%, #6cc2d6 66.01%, #8fdfc5 100.03%) |
| How | at rest |

Crops: `page-lede-default.png`.

#### topic-tab

Topic link. A topic link in the drugs index sub-nav (All / Weight Loss / …).

Page: drugs-info. Selector: `sub-nav topic link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | T: none; R: none; B: 2px solid #000000 @ 0; L: none | T: none; R: none; B: 2px solid #000000 @ 0.89; L: none | T: none; R: none; B: 2px solid #000000; L: none | T: none; R: none; B: 2px solid #000000 @ 0.89; L: none |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | sofia-pro 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 @ 0.89 | = | = | = |
| Transition | all 0.1s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.sc-4263aab9-2.dUetuz 85.0x18.0 border B:2px solid #000000 @ 0 | a.sc-4263aab9-2.dUetuz 85.0x18.0 border B:2px solid #000000 @ 0.89 | a.sc-4263aab9-2.dUetuz 85.0x18.0 border B:2px solid #000000 outline 1px auto #101010 offset 1px | a.sc-4263aab9-2.dUetuz 85.0x18.0 border B:2px solid #000000 @ 0.89 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `topic-tab-default.png`, `topic-tab-hover.png`, `topic-tab-focus-visible.png`, `topic-tab-pressed.png`.

### Forms and tools (bmi-calculator, lead capture)

#### bmi-form

BMI form. The calculator form: height feet/inches and weight number fields plus the submit.

Page: bmi-calculator. Selector: `form`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 652.5 x 273.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.89 |
| Text node | div.bmi-formstyle__InputsHeader-web-components__sc-1h7s3up-3.kqMlBX: sofia-pro 14px/19.6px 500, #000000 @ 0.89 |
| Transition | none |
| Painted layers | div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 318.3x56.0 bg #ffffff border T:1px solid #000000 @ 0.19 / R:1px solid #000000 @ 0.19 / B:1px solid #000000 @ 0.19 / L:1px solid #000000 @ 0.19 r 12px; div::before.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 316.25pxx54px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 11px; div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 318.3x56.0 bg #ffffff border T:1px solid #000000 @ 0.19 / R:1px solid #000000 @ 0.19 / B:1px solid #000000 @ 0.19 / L:1px solid #000000 @ 0.19 r 12px; div::before.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 316.25pxx54px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 11px; div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 652.5x56.0 bg #ffffff border T:1px solid #000000 @ 0.19 / R:1px solid #000000 @ 0.19 / B:1px solid #000000 @ 0.19 / L:1px solid #000000 @ 0.19 r 12px; div::before.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 650.5pxx54px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 11px |
| How | at rest |

Crops: `bmi-form-default.png`.

#### text-field

Number field. A labelled number input ("feet"/"inches"/"pounds"); focused and typed into then cleared — never submitted.

Page: bmi-calculator. Selector: `TextInputElement input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 316.25 x 54 | = | = |
| Padding | 18px 15px 0px 15px | = | = |
| Border | none | = | = |
| Radius | 11px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sofia-pro 14px/16.1px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0.89 | = | = |
| Transition | color, background-color 0.2s cubic-bezier(0.33, 0, 0, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.89, opacity 1 | = | = |
| Ancestor paint | 1 up div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "150", then deleted; nothing sent |

Crops: `text-field-default.png`, `text-field-focused.png`, `text-field-filled.png`.

#### email-field

Email field. The lead-capture email input; focused and typed into then cleared — never submitted.

Page: bmi-calculator. Selector: `input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 358 x 62 | = | = |
| Padding | 18px 15px 0px 15px | = | = |
| Border | none | = | = |
| Radius | 11px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sofia-pro 16px/18.4px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 @ 0.89 | = | = |
| Transition | color, background-color 0.2s cubic-bezier(0.33, 0, 0, 1) | = | = |
| Cursor | text | = | = |
| Placeholder | #000000 @ 0.89, opacity 1 | = | = |
| Ancestor paint | 1 up div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `email-field-default.png`, `email-field-focused.png`, `email-field-filled.png`.

#### form-submit

Form submit. The form's dark pill submit; measured, never pressed.

Page: bmi-calculator. Selector: `form button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 652.5 x 48 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | 2px solid #ffffff @ 0 | = | = | = |
| Radius | 48px | = | = | = |
| Background | #b6dd64 | #d5ff5d | #000000 @ 0.54 | #d5ff5d |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sofia-pro 14px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.buttonstyle__ContainerRouterButton-web-components__sc-1dj8m2j-2.eurUky: sofia-pro 14px/normal 500, #000000 | = | = | = |
| Transition | color, background-color, box-shadow, fill, stroke, backdrop-filter, border-color 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 656.5px x 52px, absolute, bg #000000 @ 0, radius 48px | = | = | = |
| Painted layers | button.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 652.5x48.0 bg #b6dd64 border T:2px solid #ffffff @ 0 / R:2px solid #ffffff @ 0 / B:2px solid #ffffff @ 0 / L:2px solid #ffffff @ 0 r 48px; button::before.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 656.5pxx52px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 48px | button.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 652.5x48.0 bg #d5ff5d border T:2px solid #ffffff @ 0 / R:2px solid #ffffff @ 0 / B:2px solid #ffffff @ 0 / L:2px solid #ffffff @ 0 r 48px; button::before.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 656.5pxx52px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 48px | button.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 652.5x48.0 bg #000000 @ 0.54 border T:2px solid #ffffff @ 0 / R:2px solid #ffffff @ 0 / B:2px solid #ffffff @ 0 / L:2px solid #ffffff @ 0 r 48px; button::before.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 656.5pxx52px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 48px | button.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 652.5x48.0 bg #d5ff5d border T:2px solid #ffffff @ 0 / R:2px solid #ffffff @ 0 / B:2px solid #ffffff @ 0 / L:2px solid #ffffff @ 0 r 48px; button::before.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 656.5pxx52px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 48px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `form-submit-default.png`, `form-submit-hover.png`, `form-submit-focus-visible.png`, `form-submit-pressed.png`.

#### disabled-button

Disabled button. A disabled pagination/option button in the tool (resting disabled state, SSR).

Page: bmi-calculator. Selector: `button[disabled]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 1px 6px |
| Border | none |
| Radius | 100% |
| Background | #000000 @ 0.06 |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #101010 @ 0.3 |
| Transition | background, box-shadow, transform 0.2s cubic-bezier(0.28, 0.13, 0.38, 1) |
| Cursor | default |
| Icon | 24 x 24, colour #101010 @ 0.3, fill #000000 |
| Painted layers | button.sc-95bd330a-0.fYCpay 48.0x48.0 bg #000000 @ 0.06 r 100% |
| How | at rest |

Crops: `disabled-button-default.png`.

#### bmi-dial

BMI dial. The result dial gauge beside the form.

Page: bmi-calculator. Selector: `BmiDialWrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 652.5 x 615.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.89 |
| Text node | text: sofia-pro 16px/22.4px 400, #000000 @ 0.89 |
| Transition | none |
| Icon | 480 x 285, colour #000000 @ 0.89 |
| Painted layers | div.bmi-dialstyle__BmiDialWrapper-web-components__sc-19w4ur4-1.exnzvJ 652.5x615.6 bg #313631 border T:4px solid #b0d563 / R:4px solid #b0d563 / B:4px solid #b0d563 / L:4px solid #b0d563 r 32px; div.bmi-tablestyle__RowContainer-web-components__sc-1xbn2ud-3.gFWFul 380.0x55.4 border B:1px solid #ffffff; div.bmi-tablestyle__RowContainer-web-components__sc-1xbn2ud-3.gFWFul 380.0x55.4 border B:1px solid #ffffff; div.bmi-tablestyle__RowContainer-web-components__sc-1xbn2ud-3.gFWFul 380.0x55.4 border B:1px solid #ffffff |
| Ancestor paint | 1 up div.bmi-calculatorstyle__BmiCalculatorWrapper-web-components__sc-1s5qk2f-1.dZpUFx bg #ffffff |
| How | at rest |

Crops: `bmi-dial-default.png`.

#### lead-capture

Lead capture block. The email sign-up block (input + submit + privacy disclosure).

Page: bmi-calculator. Selector: `LeadCaptureBlockWrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 466.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.89 |
| Text node | h2: sofia-pro 62px/65.1px 400, #000000 @ 0.89, ls -4.34px |
| Transition | none |
| Painted layers | div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 360.0x64.0 bg #ffffff border T:1px solid #000000 @ 0.19 / R:1px solid #000000 @ 0.19 / B:1px solid #000000 @ 0.19 / L:1px solid #000000 @ 0.19 r 12px; div::before.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy 358pxx62px border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 11px; button.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 100.0x48.0 bg #000000 border T:2px solid #ffffff @ 0 / R:2px solid #ffffff @ 0 / B:2px solid #ffffff @ 0 / L:2px solid #ffffff @ 0 r 48px; button::before.elementsstyle__ButtonReset-web-components__sc-u730hl-0.buttonstyle__ButtonVariant-web-components__sc-1dj8m2j-6 104pxx52px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 48px; a.linkstyle__BlogLink-web-components__sc-kz1v8b-3.linkstyle__UnderlinedBlogLink-web-components__sc-kz1v8b-4 106.0x17.0 border B:2px solid #000000 @ 0; a.linkstyle__BlogLink-web-components__sc-kz1v8b-3.linkstyle__UnderlinedBlogLink-web-components__sc-kz1v8b-4 74.0x17.0 border B:2px solid #000000 @ 0 |
| How | at rest |

Crops: `lead-capture-default.png`.

#### privacy-note

Privacy disclosure. The fine-print privacy disclosure under the lead capture.

Page: bmi-calculator. Selector: `PrivacyDisclosure`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 31.91 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 12px/15.96px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.65 |
| Transition | none |
| Painted layers | a.linkstyle__BlogLink-web-components__sc-kz1v8b-3.linkstyle__UnderlinedBlogLink-web-components__sc-kz1v8b-4 106.0x17.0 border B:2px solid #000000 @ 0; a.linkstyle__BlogLink-web-components__sc-kz1v8b-3.linkstyle__UnderlinedBlogLink-web-components__sc-kz1v8b-4 74.0x17.0 border B:2px solid #000000 @ 0 |
| How | at rest |

Crops: `privacy-note-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The top chrome at 390: promo bar, wordmark, hamburger (the slide menu needs hydration).

Page: blog-post. Selector: `navigation-mast / GlobalNavigation`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 785 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 16px/22.4px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.89 |
| Text node | a.sc-4263aab9-2.dUetuz: sofia-pro 16px/16px 400, #000000 @ 0.89 |
| Transition | transform 0.3s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 51 x 20, colour #0000ee, fill #000000 |
| Painted layers | div.global-navigation-headerstyle__GlobalNavigationBackground-navigation__sc-o5ejvm-1.dDoiyQ 390.0x98.0 bg #ffffff r 16px 16px 0px 0px; a.sc-4263aab9-2.dUetuz 18.0x18.0 border B:2px solid #000000 @ 0; a.sc-4263aab9-2.dUetuz 85.0x18.0 border B:2px solid #000000 @ 0; a.sc-4263aab9-2.dUetuz 87.0x18.0 border B:2px solid #000000 @ 0; a.sc-4263aab9-2.dUetuz 104.0x18.0 border B:2px solid #000000 @ 0; a.sc-4263aab9-2.dUetuz 31.0x18.0 border B:2px solid #000000 @ 0 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-toggle

Mobile menu toggle. The hamburger at phone width; measured, never toggled.

Page: blog-post. Selector: `menu button`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 48 x 48 |
| Padding | 0px |
| Border | T: none; R: none; B: 2px solid #000000 @ 0; L: none |
| Radius | 48px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 10px/10px 600 |
| Letter spacing | 1.25px |
| Colour | #000000 |
| Transition | color, background-color, box-shadow, fill, stroke 0.3s ease-out |
| Cursor | pointer |
| Icon | 24 x 24, colour #000000 |
| ::before | auto x calc(100% + 2px), absolute, bg #000000 @ 0, radius 48px |
| Painted layers | button.elementsstyle__ButtonReset-web-components__sc-u730hl-0.linkstyle__ButtonLink-web-components__sc-kz1v8b-1 48.0x48.0 border B:2px solid #000000 @ 0 r 48px; button::before.elementsstyle__ButtonReset-web-components__sc-u730hl-0.linkstyle__ButtonLink-web-components__sc-kz1v8b-1 autoxcalc(100% + 2px) border T:1px solid #000000 @ 0.03 / R:1px solid #000000 @ 0.03 / B:1px solid #000000 @ 0.03 / L:1px solid #000000 @ 0.03 r 48px |
| How | at rest |

Crops: `m-menu-toggle-default.png`.

#### m-logo

Mobile wordmark. The "hers" wordmark at phone width.

Page: product. Selector: `logo link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 57.59 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.89 |
| Transition | none |
| Cursor | pointer |
| Icon | 57.59 x 24, colour #000000 @ 0.89, fill #000000 |
| How | at rest |

Crops: `m-logo-default.png`.

#### m-bento-card

Mobile bento card. A bento tile at phone width.

Page: home. Selector: `BentoContentCard`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 374 x 400 |
| Padding | 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/22.4px 400 |
| Letter spacing | -0.176px |
| Colour | #ffffff |
| Text node | span.sc-aXZVg.ehfisG: CareSans 20px/23.5px 480, #ffffff, ls 0.025px |
| Transition | none |
| Painted layers | button.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 128.5x44.0 bg #ffffff @ 0.17 border T:2px solid #ffffff @ 0 / R:2px solid #ffffff @ 0 / B:2px solid #ffffff @ 0 / L:2px solid #ffffff @ 0 r 48px; button::before.elements-style__ButtonReset-sc-82b26c75-0.button-style__ButtonVariant-sc-de21aabe-5 132.484pxx48px border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 48px |
| Ancestor paint | 1 up div.stacked-cta-card-style__Frame-sc-142aa7a5-0.kOucQG bg #000000 @ 0.12 |
| How | at rest |

Crops: `m-bento-card-default.png`.

#### m-cta-primary

Mobile primary CTA. The primary pill action at phone width.

Page: product. Selector: `data-variant=primary`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 346 x 48 |
| Padding | 8px 24px |
| Border | 1px solid #000000 @ 0 |
| Radius | 9999px |
| Background | #000000 |
| Box shadow | none |
| Backdrop filter | blur(10px) |
| Outline | 1px solid #000000 @ 0 offset 0px |
| Font | CareSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span: CareSans 16px/24px 400, #ffffff |
| Transition | border-color, color, background-color, box-shadow, outline-offset, outline-color, text-decoration-color 0.2s ease-in-out |
| Cursor | pointer |
| Painted layers | a._reset_5zh37_19._base_5zh37_28 346.0x48.0 bg #000000 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 9999px outline 1px solid #000000 @ 0 offset 0px |
| How | at rest |

Crops: `m-cta-primary-default.png`.

#### m-content-card

Mobile content card. A content card at phone width.

Page: product. Selector: `content card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 346 x 63.48 |
| Padding | 0px |
| Gap | 16px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | CareSans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h4._text-label-xl-max-medium_ncjzh_221._text-label-xl-min-medium-max-large_ncjzh_639: CareSans 18px/21.375px 500, #000000 @ 0.81, ls 0.03384px |
| Transition | none |
| How | at rest |

Crops: `m-content-card-default.png`.

#### m-text-field

Mobile number field. The number input at phone width.

Page: bmi-calculator. Selector: `TextInputElement input`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 161.5 x 54 |
| Padding | 18px 15px 0px 15px |
| Border | none |
| Radius | 11px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sofia-pro 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #000000 @ 0.89 |
| Transition | color, background-color 0.2s cubic-bezier(0.33, 0, 0, 1) |
| Cursor | text |
| Placeholder | #000000 @ 0.89, opacity 1 |
| Ancestor paint | 1 up div.text-inputstyle__TextInputWrapper-web-components__sc-wod1kx-0.fhZqmy bg #ffffff |
| How | at rest |

Crops: `m-text-field-default.png`.

## Transitions declared in the readable stylesheets

forhers's archived sheets are same-origin on the local mirror (the inline styled-components blocks plus the /shop bundle that resolved), so this list holds every declared transition the CSSOM could read on each page.
