# Component measurements

Computed styles read from acuityscheduling.com and secure.acuityscheduling.com on 2026-11-10 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The fixed top bar at 80px: the Acuity wordmark left; How It Works plus the Solutions / Product / Resources dropdown triggers, Pricing and Log in; the Get started CTA right. Transparent over the hero, opaque after scroll.

Page: home. Selector: `.menu-container.frontsite-hero-nav`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 80 |
| Padding | 18px 20px 18px 40px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0 |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a: Clarkson 14px/18.76px 400, #000000 |
| Transition | background 0.25s ease-in-out |
| Painted layers | div.menu-container.frontsite-hero-nav 1440.0x80.0 bg #ffffff @ 0; a.navlogo__tryscheduling-btn.try 0.0x0.0 bg #283849 r 12px; div.dropdown__content 0.0x0.0 bg #ffffff r 22px shadow #000000 @ 0.05 0px 4px 4px 2px; a.solutions-grid__item 0.0x0.0 border B:1px solid #f2f2f2; a.solutions-grid__item 0.0x0.0 border B:1px solid #f2f2f2; a.solutions-grid__item 0.0x0.0 border B:1px solid #f2f2f2 |
| How | at rest |

Crops: `header-default.png`.

#### logo

Wordmark. The Acuity logotype in the header, an SVG lockup that links home.

Page: home. Selector: `.navlogo a svg`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 168 x 24 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Ancestor paint | 1 up div.menu-container.frontsite-hero-nav bg #ffffff @ 0 |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. A direct header link (How It Works, Pricing).

Page: home. Selector: `header a "How It Works"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 85.39 x 18.77 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 14px/18.76px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.5 | = | 0.5 |
| Painted layers | - | = | a 85.4x18.8 outline 1px auto #005fcc offset 1px | = |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-trigger

Nav dropdown trigger. A hoverable dropdown trigger (Solutions, Product, Resources): a nav item that opens a mega-menu of industry / feature links.

Page: home. Selector: `button.dropdown__trigger-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 80.86 x 18.77 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Clarkson 14px/18.76px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.5 | = | 0.5 |
| Painted layers | - | = | button.dropdown__trigger-link 80.9x18.8 outline 1px auto #005fcc offset 0px | = |

Crops: `nav-trigger-default.png`, `nav-trigger-hover.png`, `nav-trigger-focus-visible.png`, `nav-trigger-pressed.png`.

#### nav-dropdown

Nav dropdown. The Solutions mega-menu under the header: a padded card grid of industry links (Beauty, Business Services, Wellness, Fitness, Visual and Performing Arts, Education).

Page: home. Selector: `.dropdown__content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 788 x 347 |
| Padding | 44px |
| Gap | 22px |
| Border | none |
| Radius | 22px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.05 0px 4px 4px 2px |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.solutions-grid: Clarkson 14px/22px 400, #000000 |
| Transition | opacity 0.25s ease-in-out |
| Painted layers | div.dropdown__content 788.0x347.0 bg #ffffff r 22px shadow #000000 @ 0.05 0px 4px 4px 2px; a.solutions-grid__item 353.0x65.0 border B:1px solid #f2f2f2; a.solutions-grid__item 353.0x65.0 border B:1px solid #f2f2f2; a.solutions-grid__item 353.0x65.0 border B:1px solid #f2f2f2; a.solutions-grid__item 353.0x65.0 border B:1px solid #f2f2f2; a.solutions-grid__item 353.0x65.0 border B:1px solid #f2f2f2 |
| How | at rest |

Crops: `nav-dropdown-default.png`.

#### dropdown-item

Dropdown item. An industry link inside the mega-menu: a bold name with a grey one-line description.

Page: home. Selector: `.dropdown__content a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 353 x 65 | = | = | = |
| Padding | 11px | = | = | = |
| Gap | 4px | = | = | = |
| Border | T: none; R: none; B: 1px solid #f2f2f2; L: none | = | = | = |
| Radius | 0px | 8px | = | 8px |
| Background | transparent | #f2f2f2 | = | #f2f2f2 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 14px/18.76px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | span.solutions-grid: Clarkson 14px/22px 400, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.solutions-grid__item 353.0x65.0 border B:1px solid #f2f2f2 | a.solutions-grid__item 353.0x65.0 bg #f2f2f2 border B:1px solid #f2f2f2 r 8px | a.solutions-grid__item 353.0x65.0 border B:1px solid #f2f2f2 outline 1px auto #005fcc offset 1px | a.solutions-grid__item 353.0x65.0 bg #f2f2f2 border B:1px solid #f2f2f2 r 8px |
| Ancestor paint | 3 up div.dropdown__content bg #ffffff shadow #000000 @ 0.05 0px 4px 4px 2px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `dropdown-item-default.png`, `dropdown-item-hover.png`, `dropdown-item-focus-visible.png`, `dropdown-item-pressed.png`.

#### login-link

Log in link. The Log in entry in the header, an <a> to the Squarespace sign-in gate. Hovered and focused, never followed.

Page: home. Selector: `header "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40.27 x 18 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 14px/18.76px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.5 | = | 0.5 |
| Painted layers | - | = | a 40.3x18.0 outline 1px auto #005fcc offset 1px | = |

Crops: `login-link-default.png`, `login-link-hover.png`, `login-link-focus-visible.png`, `login-link-pressed.png`.

#### nav-cta

Nav CTA. The Get started button in the header: the signup CTA.

Page: home. Selector: `header "Get started"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121.48 x 42.77 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #283849 | #3e5772 | #3e5772 | #3e5772 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px auto #000000 offset 4px | = |
| Font | Clarkson 14px/18.76px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s ease-in | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.try.amp-external 121.5x42.8 bg #283849 r 12px | a.try.amp-external 121.5x42.8 bg #3e5772 r 12px | a.try.amp-external 121.5x42.8 bg #3e5772 r 12px outline 2px auto #000000 offset 4px | a.try.amp-external 121.5x42.8 bg #3e5772 r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero

Hero. The opening band: the 40px "Scheduling software to power exceptional client experiences" headline, the signup pair and a product booking-page mock. Measured at rest.

Page: home. Selector: `section.hero-block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1317.33 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h1: Clarkson-Serif 40px/48px 500, #283849 |
| Transition | none |
| Icon | 22 x 22, colour #283849, fill #000000 |
| Painted layers | div.large-csp-hero__gradient.large-csp-hero__gradient--9 1440.0x1317.3 image linear-gradient(66deg, #f0ece1 0px, #f9f6ea 75%, #f6f3ed 100%); div::after.large-csp-hero__gradient.large-csp-hero__gradient--9 1440pxx395.188px image linear-gradient(#000000 @ 0, #ffffff); a 0.0x0.0 bg #283849 r 12px; a.hero-cta-email 220.1x56.0 border T:1px solid #283849 / R:1px solid #283849 / B:1px solid #283849 / L:1px solid #283849 r 12px; a.hero-cta-google 212.0x56.0 border T:1px solid #283849 / R:1px solid #283849 / B:1px solid #283849 / L:1px solid #283849 r 12px; div.carousel__frame-slide-wrapper 787.1x524.7 r 24px shadow #000000 @ 0.12 0px 2px 8px 0px, #000000 @ 0.08 0px 0px 1px 0px |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `hero-default.png`.

#### hero-title

Hero title. The 40px Clarkson headline.

Page: home. Selector: `hero h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 572 x 96 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson-Serif 40px/48px 500 |
| Letter spacing | normal |
| Colour | #283849 |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero sub. The supporting line under the title ("Book appointments, take payments, and automate the busywork…").

Page: home. Selector: `hero sub`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 572 x 51.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/25.6px 400 |
| Letter spacing | normal |
| Colour | #283849 |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### hero-cta-email

Sign up with email. The hero signup button: a 56px 12px-radius control, followed to the account gate only in captures — never pressed here.

Page: home. Selector: `a.hero-cta-email`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 220.06 x 56 | = | = | = |
| Padding | 16px 33px | = | = | = |
| Gap | 10px | = | = | = |
| Border | 1px solid #283849 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 14px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #283849 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #283849, fill #000000 | = | = | = |
| Painted layers | a.hero-cta-email 220.1x56.0 border T:1px solid #283849 / R:1px solid #283849 / B:1px solid #283849 / L:1px solid #283849 r 12px | = | a.hero-cta-email 220.1x56.0 border T:1px solid #283849 / R:1px solid #283849 / B:1px solid #283849 / L:1px solid #283849 r 12px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `hero-cta-email-default.png`, `hero-cta-email-hover.png`, `hero-cta-email-focus-visible.png`, `hero-cta-email-pressed.png`.

#### hero-cta-google

Sign up with Google. The Google signup button beside the email one, with the G glyph.

Page: home. Selector: `a.hero-cta-google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211.98 x 56 | = | = | = |
| Padding | 16px 25px | = | = | = |
| Gap | 5px | = | = | = |
| Border | 1px solid #283849 | = | = | = |
| Radius | 12px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 14px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #283849 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #283849, fill #000000 | = | = | = |
| Painted layers | a.hero-cta-google 212.0x56.0 border T:1px solid #283849 / R:1px solid #283849 / B:1px solid #283849 / L:1px solid #283849 r 12px | = | a.hero-cta-google 212.0x56.0 border T:1px solid #283849 / R:1px solid #283849 / B:1px solid #283849 / L:1px solid #283849 r 12px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.8 | = | 0.8 |

Crops: `hero-cta-google-default.png`, `hero-cta-google-hover.png`, `hero-cta-google-focus-visible.png`, `hero-cta-google-pressed.png`.

#### hero-terms

Signup legal line. The "By creating an account, you agree to our Terms of Service…" line under the buttons.

Page: home. Selector: `p.hero-cta-terms`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 273 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 10px/16px 400 |
| Letter spacing | normal |
| Colour | #283849 |
| Transition | none |
| How | at rest |

Crops: `hero-terms-default.png`.

#### vertical-card

Industry card. A tile in "Acuity is for anyone in the business of time" (Beauty, Business Services, Wellness, Fitness, Visual and Performing Arts, Education): a named card with an image and a one-line descriptor, linking the industry page.

Page: home. Selector: `a.verticals-section__card`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 458.89 x 150 | = | = | = |
| Padding | 10px | = | = | = |
| Gap | 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | #fdf9f7 | = | = | = |
| Box shadow | #000000 @ 0.08 0px 0px 0.5px 0px, #000000 @ 0.12 0px 16px 32px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Text node | h3.verticals-section__card-title: Clarkson 16px/19.44px 500, #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.verticals-section__card.verticals-section__card--beauty 458.9x150.0 bg #fdf9f7 r 16px shadow #000000 @ 0.08 0px 0px 0.5px 0px, #000000 @ 0.12 0px 16px 32px 0px | = | a.verticals-section__card.verticals-section__card--beauty 458.9x150.0 bg #fdf9f7 r 16px shadow #000000 @ 0.08 0px 0px 0.5px 0px, #000000 @ 0.12 0px 16px 32px 0px outline 1px auto #005fcc offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `vertical-card-default.png`, `vertical-card-hover.png`, `vertical-card-focus-visible.png`, `vertical-card-pressed.png`.

#### vertical-cta

Industries CTA. "Explore all industries" under the grid.

Page: home. Selector: `.verticals-section__cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155.73 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0e0e0e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up section.verticals-section bg #ffffff | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.verticals-section__cta 155.7x22.0 outline 1px auto #005fcc offset 1px | = |

Crops: `vertical-cta-default.png`, `vertical-cta-hover.png`, `vertical-cta-focus-visible.png`, `vertical-cta-pressed.png`.

#### feature-card

Feature card. A card in "Everything you need to run your business" (Book beautifully 24/7, Reduce no-shows, Automate your day, Boost your earnings): an image, a 24px header and body text.

Page: home. Selector: `.feature-area-card`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 928 x 333.73 | = |
| Padding | 40px | = |
| Gap | 20px | = |
| Border | none | = |
| Radius | 16px | = |
| Background | #f4f4f4 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Clarkson 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | h2.feature-area-card: Clarkson-Serif 24px/28px 500, #283849 | = |
| Transition | none | = |
| Painted layers | div.feature-area-card.feature-area-card--featured 928.0x333.7 bg #f4f4f4 r 16px; a.feature-area-card__cta-button 293.4x54.0 bg #283849 r 12px; img.feature-area-card__desktop-image 414.0x253.7 r 8px shadow #000000 @ 0.08 0px 0px 0.38px 0px, #000000 @ 0.12 0px 6px 24px 0px; video.feature-area-card.feature-area-card__video--has-desktop-image 0.0x0.0 r 8px shadow #000000 @ 0.08 0px 0px 0.38px 0px, #000000 @ 0.12 0px 6px 24px 0px | = |
| How | at rest | mouse hover |

Crops: `feature-card-default.png`, `feature-card-hover.png`.

#### feature-card-title

Feature card title. A 24px feature card header.

Page: home. Selector: `.feature-area-card__header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 414 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson-Serif 24px/28px 500 |
| Letter spacing | normal |
| Colour | #283849 |
| Transition | none |
| How | at rest |

Crops: `feature-card-title-default.png`.

#### testimonial-card

Testimonial card. A quote card in "Real results from professionals just like you".

Page: home. Selector: `testimonial card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 787.95 x 444.55 |
| Padding | 0px |
| Border | none |
| Radius | 24px |
| Background | transparent |
| Box shadow | #000000 @ 0.12 0px 2px 8px 0px, #000000 @ 0.08 0px 0px 1px 0px |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | p.testimonial-card__name: Clarkson 20px/32px 500, #162427 |
| Transition | none |
| Painted layers | div.carousel__frame-slide-wrapper 788.0x444.6 r 24px shadow #000000 @ 0.12 0px 2px 8px 0px, #000000 @ 0.08 0px 0px 1px 0px; div.carousel__frame-slide 788.0x444.6 bg #fafafa r 22px; div.testimonial-card.testimonial-card--purple 788.0x444.6 bg #d6d0ed; div.testimonial-card__tag 70.4x20.4 bg #ebe7f6 r 15px; span.testimonial-card__tag-icon 13.6x13.6 bg #574f8a; span.testimonial-card__dot.testimonial-card__dot--active 27.2x3.4 bg #574f8a r 2px |
| How | at rest |

Crops: `testimonial-card-default.png`.

#### carousel-nav

Carousel arrow. A prev/next control on the testimonials carousel.

Page: home. Selector: `testimonials arrow button`. States: .

Not found on the page at capture time.

#### integration-logo

Integration logo. A partner mark in "Connect your calendar and so much more" (Google, Outlook, Stripe…).

Page: home. Selector: `.integrations-v2 img`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 60 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | none |
| Ancestor paint | 1 up div.integrations-v2__tile bg #ffffff @ 0.78; 3 up div.integrations-v2 shadow #283849 @ 0.06 0px 12px 40px 0px |
| How | at rest |

Crops: `integration-logo-default.png`.

#### bottom-cta

Bottom CTA. The closing "Get started for free" band before the footer.

Page: home. Selector: `section.bottom-cta`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 599 |
| Padding | 204px 20px 195px 20px |
| Gap | 32px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h2: Clarkson-Serif 40px/48px 500, #283849 |
| Transition | none |
| Painted layers | a.bottom-cta 230.0x72.0 bg #283849 r 12px |
| Ancestor paint | 1 up div.bottom-section bg #e0ebf4 |
| How | at rest |

Crops: `bottom-cta-default.png`.

#### carousel-dots

Carousel dots. The testimonials carousel has no arrows: a .testimonial-card__dots row of thin dash indicators (the active one wider) marks position while slides auto-play.

Page: home. Selector: `.testimonial-card__dots`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 68 x 3.4 |
| Padding | 0px |
| Gap | 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #162427 |
| Transition | none |
| Painted layers | span.testimonial-card__dot.testimonial-card__dot--active 27.2x3.4 bg #574f8a r 2px; span.testimonial-card__dot 3.4x3.4 bg #162427 @ 0.25 r 50%; span.testimonial-card__dot 3.4x3.4 bg #162427 @ 0.25 r 50%; span.testimonial-card__dot 3.4x3.4 bg #162427 @ 0.25 r 50%; span.testimonial-card__dot 3.4x3.4 bg #162427 @ 0.25 r 50% |
| Ancestor paint | 1 up div.testimonial-card.testimonial-card--purple bg #d6d0ed; 3 up div.carousel__frame-slide-wrapper shadow #000000 @ 0.12 0px 2px 8px 0px, #000000 @ 0.08 0px 0px 1px 0px |
| How | at rest |

Crops: `carousel-dots-default.png`.

### Footer

#### footer

Footer. The page foot: a Squarespace logo mark, link columns under collapsible headings (Get Started, Features, Solutions, Resources), social icons and legal links.

Page: home. Selector: `footer.frontsite-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 641.19 |
| Padding | 40px 0px 20px 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h3: Clarkson 12px/19.2px 600, #0e0e0e |
| Transition | none |
| Icon | 0 x 0, colour #000000 |
| Painted layers | footer.frontsite-footer 1440.0x641.2 bg #ffffff; div::before.frontsite-footer 1350pxx1px bg #e0e0e0; span.language-selector-chevron 16.0x16.0 image url(data:…); span.language-selector-chevron 0.0x0.0 image url(data:…) |
| How | at rest |

Crops: `footer-default.png`.

#### footer-col-title

Footer column title. A footer column heading (Get Started, Features, Solutions, Resources): a button that expands the column on narrow screens.

Page: home. Selector: `button.footer-link-title`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 203.59 x 41.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Clarkson 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | h3: Clarkson 12px/19.2px 600, #0e0e0e | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 0 x 0, colour #000000 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.footer-link-title 203.6x41.2 outline 1px auto #005fcc offset 0px | = |

Crops: `footer-col-title-default.png`, `footer-col-title-hover.png`, `footer-col-title-focus-visible.png`, `footer-col-title-pressed.png`.

#### footer-link

Footer link. A footer column link (Home, About Us, Pricing, Online Booking).

Page: home. Selector: `footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 203.59 x 37 | = | = | = |
| Padding | 11px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0e0e0e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 203.6x37.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-link

Social link. A social icon link in the footer (Instagram, Pinterest, Facebook, LinkedIn, YouTube): the mark is painted as a background image, not an inline SVG.

Page: home. Selector: `footer a[href*=instagram.com]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 50% | = | = | = |
| Background | transparent | #f0f0f0 | = | #f0f0f0 |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Transition | background-color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a 32.0x32.0 bg #f0f0f0 r 50% | a 32.0x32.0 r 50% outline 1px auto #005fcc offset 1px | a 32.0x32.0 bg #f0f0f0 r 50% |

Crops: `social-link-default.png`, `social-link-hover.png`, `social-link-focus-visible.png`, `social-link-pressed.png`.

#### footer-legal

Legal link. A legal foot link (Terms of Service, Privacy Policy).

Page: home. Selector: `footer legal a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40.52 x 15 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 12px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0e0e0e | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 40.5x15.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-legal-default.png`, `footer-legal-hover.png`, `footer-legal-focus-visible.png`, `footer-legal-pressed.png`.

### Pricing

#### pricing-hero

Pricing plans block. The plan cards row: three or four tiers each with a name, blurb, monthly price, feature list and a CTA.

Page: pricing. Selector: `.pricing-hero-plans-wrapper`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1395 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Background image | url(…) |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h1: Clarkson-Serif 48px/48px 500, #ffffff |
| Transition | none |
| Painted layers | div.segmented-control 300.4x52.0 bg #f2f2f2 @ 0.2 r 100px; div.segmented-control-pill 146.0x48.0 bg #ffffff r 100px; div.plan-wrapper.phase2-plan-wrapper 448.7x438.0 bg #ffffff border T:1px solid #e4e4e4 / R:1px solid #e4e4e4 / B:1px solid #e4e4e4 / L:1px solid #e4e4e4 r 12px; a.signupPage__btn.phase2-cta 0.0x0.0 bg #283849 r 12px; a.signupPage__btn.phase2-cta 138.7x46.0 bg #283849 r 12px; div.phase2-plan-divider 402.7x1.0 bg #e7e7e7 |
| Ancestor paint | 1 up div.content-module-full bg #ffffff |
| How | at rest |

Crops: `pricing-hero-default.png`.

#### plan-card

Plan card. A pricing tier card (~447x436): name, price, feature list with tooltip markers, Start free trial CTA.

Page: pricing. Selector: `.plan.phase2-plan`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 446.67 x 436 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Clarkson 16px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #222222 | = |
| Text node | div.phase2-plan-title: Clarkson Serif 32px/40px 500, #0e0e0e | = |
| Transition | none | = |
| Painted layers | a.signupPage__btn.phase2-cta 0.0x0.0 bg #283849 r 12px; a.signupPage__btn.phase2-cta 138.7x46.0 bg #283849 r 12px; div.phase2-plan-divider 402.7x1.0 bg #e7e7e7; span.feature-tooltip-trigger 67.6x20.0 image linear-gradient(90deg, #b7b7b7 1px, #000000 @ 0 0px); div.feature-tooltip 250.0x88.0 bg #0e0e0e r 4px shadow #000000 @ 0.08 0px 0px 1px 0px, #000000 @ 0.12 0px 8px 32px 0px; span.feature-tooltip-trigger 285.5x20.0 image linear-gradient(90deg, #b7b7b7 1px, #000000 @ 0 0px) | = |
| Ancestor paint | 1 up div.plan-wrapper.phase2-plan-wrapper bg #ffffff | = |
| How | at rest | mouse hover |

Crops: `plan-card-default.png`, `plan-card-hover.png`.

#### plan-name

Plan name. The tier name on a plan card (Starter, Emerging, Growing, Powerhouse), a .phase2-plan-title div.

Page: pricing. Selector: `.phase2-plan-title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 85.3 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson Serif 32px/40px 500 |
| Letter spacing | normal |
| Colour | #0e0e0e |
| Transition | none |
| How | at rest |

Crops: `plan-name-default.png`.

#### plan-price

Plan price. The monthly price figure on a tier card.

Page: pricing. Selector: `.phase2-plan-price`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 100.09 x 27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | span.phase2-price-amount.notranslate: Clarkson 18px/27px 500, #0e0e0e |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. The "Start free trial" button on a tier card: measured and state-forced, never followed.

Page: pricing. Selector: `a.phase2-cta`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 138.66 x 46 | = | = | 124.79 x 41.4 |
| Padding | 12px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #283849 | #1e2d3a | #1e2d3a | #1e2d3a |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #283849 offset 2px | = |
| Font | Clarkson 14px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.15s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.signupPage__btn.phase2-cta 138.7x46.0 bg #283849 r 12px | a.signupPage__btn.phase2-cta 138.7x46.0 bg #1e2d3a r 12px | a.signupPage__btn.phase2-cta 138.7x46.0 bg #1e2d3a r 12px outline 2px solid #283849 offset 2px | a.signupPage__btn.phase2-cta 124.8x41.4 bg #1e2d3a r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | = | = | matrix(0.9, 0, 0, 0.9, 0, 0) |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-feature

Plan feature row. A feature line in a plan card; the marker holds a tooltip on hover.

Page: pricing. Selector: `.phase2-plan .feature`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 402.67 x 22 | = |
| Padding | 0px | = |
| Gap | 16px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Clarkson 14px/22px 500 | = |
| Letter spacing | normal | = |
| Colour | #0e0e0e | = |
| Text node | span.feature-tooltip-trigger: Clarkson 14px/22px 500, #0e0e0e | = |
| Transition | none | = |
| Painted layers | span.feature-tooltip-trigger 67.6x20.0 image linear-gradient(90deg, #b7b7b7 1px, #000000 @ 0 0px); div.feature-tooltip 250.0x88.0 bg #0e0e0e r 4px shadow #000000 @ 0.08 0px 0px 1px 0px, #000000 @ 0.12 0px 8px 32px 0px | = |
| How | at rest | mouse hover |

Crops: `plan-feature-default.png`, `plan-feature-hover.png`.

#### faq-accordion

FAQ accordion. The pricing FAQ: button.accordion-title questions expanding .accordion-panel answers.

Page: pricing. Selector: `.faq-accordion-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 1007.72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h3.accordion-title-text: Clarkson-Serif 24px/27.6px 500, #ffffff |
| Transition | none |
| Icon | 22 x 22, colour #ffffff |
| Painted layers | button.accordion-title 640.0x92.6 border B:1px solid #ffffff @ 0.1; button.accordion-title 640.0x92.6 border B:1px solid #ffffff @ 0.1; button.accordion-title 640.0x92.6 border B:1px solid #ffffff @ 0.1; button.accordion-title 640.0x120.2 border B:1px solid #ffffff @ 0.1; button.accordion-title 640.0x92.6 border B:1px solid #ffffff @ 0.1; button.accordion-title 640.0x92.6 border B:1px solid #ffffff @ 0.1 |
| How | at rest |

Crops: `faq-accordion-default.png`.

#### accordion-title

FAQ question. An accordion question row; pressing it is a local toggle that reveals the answer.

Page: pricing. Selector: `button.accordion-title`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 640 x 92.59 | = | = | = |
| Padding | 32px 0px | = | = | = |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.1; L: none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Clarkson 16px/18.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | h3.accordion-title-text: Clarkson-Serif 24px/27.6px 500, #ffffff | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #ffffff | = | = | = |
| Painted layers | button.accordion-title 640.0x92.6 border B:1px solid #ffffff @ 0.1 | = | button.accordion-title 640.0x92.6 border B:1px solid #ffffff @ 0.1 outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `accordion-title-default.png`, `accordion-title-hover.png`, `accordion-title-focus-visible.png`, `accordion-title-pressed.png`.

#### accordion-panel

FAQ answer. An expanded accordion answer, opened through its own question toggle.

Page: pricing. Selector: `.accordion-panel open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 145 |
| Padding | 0px |
| Border | T: none; R: none; B: 1px solid #ffffff @ 0.1; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/26px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p: Clarkson 16px/26px 400, #ffffff |
| Transition | max-height 0.2s ease-out |
| Painted layers | div.accordion-panel.panel-active 640.0x145.0 border B:1px solid #ffffff @ 0.1 |
| How | at rest |

Crops: `accordion-panel-default.png`.

#### accordion-title-open

FAQ question, open. The question in its expanded state (accordion-active / aria-expanded).

Page: pricing. Selector: `button.accordion-title.open`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 91.59 |
| Padding | 32px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/18.4px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h3.accordion-title-text: Clarkson-Serif 24px/27.6px 500, #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 22 x 22, colour #ffffff |
| How | at rest |

Crops: `accordion-title-open-default.png`.

### Auth gate (Squarespace)

#### gate-card

Create-account card. The Squarespace account gate "Create your account": a centred ~540px card with provider buttons and legal links — the start of the signup flow, never submitted.

Page: getstarted. Selector: `dialog card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 540 x 572 |
| Padding | 0px |
| Border | none |
| Radius | 6px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.12 0px 16px 64px 0px, #000000 @ 0.08 0px 0px 1px 0px |
| Outline | none |
| Font | Times 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Clarkson 20px/28px 600, #0e0e0e |
| Transition | none |
| Icon | 18 x 18, colour #000000 |
| Painted layers | div.Dialog-container-zSER9.css-11nhbx2 540.0x572.0 bg #ffffff r 6px shadow #000000 @ 0.12 0px 16px 64px 0px, #000000 @ 0.08 0px 0px 1px 0px; button.css-ds0862 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-ds0862 450pxx53px bg #e7e7e7; button.css-ds0862 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-ds0862 450pxx53px bg #e7e7e7; button.css-1osw29z 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 |
| How | at rest |

Crops: `gate-card-default.png`.

#### gate-google

Continue with Google. The Google OAuth row on the create-account card. Measured, never pressed.

Page: getstarted. Selector: `"Continue with Google" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 452 x 55 | = | = | = |
| Padding | 0px 22px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Clarkson 14px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.css-40sddq: Clarkson 14px/22px 500, #000000 | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #000000 | = | = | = |
| ::before | 450px x 53px, absolute, bg #e7e7e7, radius 0px | = | = | = |
| Painted layers | button.css-ds0862 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-ds0862 450pxx53px bg #e7e7e7 | = | button.css-ds0862.focus-visible 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px outline 2px solid #000000 @ 0 offset 2px; button::before.css-ds0862.focus-visible 450pxx53px bg #e7e7e7 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gate-google-default.png`, `gate-google-hover.png`, `gate-google-focus-visible.png`, `gate-google-pressed.png`.

#### gate-apple

Continue with Apple. The Apple OAuth row. Measured, never pressed.

Page: getstarted. Selector: `"Continue with Apple" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 452 x 55 | = | = | = |
| Padding | 0px 22px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Clarkson 14px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.css-40sddq: Clarkson 14px/22px 500, #000000 | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 20, colour #000000 | = | = | = |
| ::before | 450px x 53px, absolute, bg #e7e7e7, radius 0px | = | = | = |
| Painted layers | button.css-ds0862 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-ds0862 450pxx53px bg #e7e7e7 | = | button.css-ds0862.focus-visible 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px outline 2px solid #000000 @ 0 offset 2px; button::before.css-ds0862.focus-visible 450pxx53px bg #e7e7e7 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gate-apple-default.png`, `gate-apple-hover.png`, `gate-apple-focus-visible.png`, `gate-apple-pressed.png`.

#### gate-email

Continue with Email. The email signup row — leads to an email field on the next step, which is not reached.

Page: getstarted. Selector: `"Continue with Email" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 452 x 55 | = | = | = |
| Padding | 0px 22px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Clarkson 14px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.css-40sddq: Clarkson 14px/22px 500, #000000 | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #000000 | = | = | = |
| ::before | 450px x 53px, absolute, bg #e7e7e7, radius 0px | = | = | = |
| Painted layers | button.css-1osw29z 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-1osw29z 450pxx53px bg #e7e7e7 | = | button.css-1osw29z.focus-visible 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px outline 2px solid #000000 @ 0 offset 2px; button::before.css-1osw29z.focus-visible 450pxx53px bg #e7e7e7 | = |
| Ancestor paint | 2 up div.Dialog-container-zSER9.css-11nhbx2 bg #ffffff shadow #000000 @ 0.12 0px 16px 64px 0px, #000000 @ 0.08 0px 0px 1px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `gate-email-default.png`, `gate-email-hover.png`, `gate-email-focus-visible.png`, `gate-email-pressed.png`.

#### more-options

More options expander. The "MORE OPTIONS" text expander revealing further providers — a local toggle.

Page: getstarted. Selector: `"MORE OPTIONS" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 98.59 x 55 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 12px/22px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #0e0e0e | = | = | = |
| Text node | span: Clarkson 12px/22px 500, #0e0e0e, ls 0.5px | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 98.5938px x 55px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | div.css-mzw0dv 0.0x2.0 border T:2px solid #0e0e0e | div.css-mzw0dv 98.4x2.0 border T:2px solid #0e0e0e | button::after.css-1qsym0a.focus-visible 110.594pxx47px border T:2px solid #0e0e0e / R:2px solid #0e0e0e / B:2px solid #0e0e0e / L:2px solid #0e0e0e; div.css-mzw0dv 0.0x2.0 border T:2px solid #0e0e0e | = |
| Ancestor paint | 3 up div.Dialog-container-zSER9.css-11nhbx2 bg #ffffff shadow #000000 @ 0.12 0px 16px 64px 0px, #000000 @ 0.08 0px 0px 1px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 110.594px x 47px, absolute, bg #000000 @ 0, radius 0px | = |

Crops: `more-options-default.png`, `more-options-hover.png`, `more-options-focus-visible.png`, `more-options-pressed.png`.

#### more-options-open

Extra provider, revealed. A provider row revealed by MORE OPTIONS.

Page: getstarted. Selector: `extra provider`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 452 x 55 |
| Padding | 0px 22px |
| Border | 1px solid #000000 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 14px/22px 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | div.css-40sddq: Clarkson 14px/22px 500, #000000 |
| Transition | transform 0.05s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | pointer |
| Icon | 22 x 22, colour #000000 |
| ::before | 450px x 53px, absolute, bg #e7e7e7, radius 0px |
| Painted layers | button.css-ds0862 452.0x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-ds0862 450pxx53px bg #e7e7e7 |
| How | at rest |

Crops: `more-options-open-default.png`.

#### login-card

Sign-in card. The Squarespace "Log into Acuity Scheduling with your Squarespace account" card (styled-components css-* classes): email and password fields, LOG IN, OR divider, OAuth rows — the gate for the app, never submitted.

Page: login. Selector: `login card`. States: .

Not found on the page at capture time.

#### login-email

Email field. The EMAIL ADDRESS field; typed and deleted, never submitted.

Page: login. Selector: `input[name=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 326.63 x 22 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Clarkson 14px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #0e0e0e | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #949494, opacity 1 | = | = |
| How | at rest | clicked into the field | focused empty; nothing typed or sent |

Crops: `login-email-focus.png` (empty; earlier typed crops removed).

#### login-password

Password field. The PASSWORD field; focused only, never typed.

Page: login. Selector: `input[type=password]`. States: default, focused.

| Property | default | focused |
|---|---|---|
| Size (w x h) | 326.63 x 22 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Clarkson 14px/22px 500 | = |
| Letter spacing | normal | = |
| Colour | #0e0e0e | = |
| Transition | none | = |
| Cursor | text | = |
| Placeholder | #949494, opacity 1 | = |
| How | at rest | clicked into the field |

Crops: `login-password-default.png`, `login-password-focused.png`.

#### login-submit

Log in button. The LOG IN submit. Measured, never pressed.

Page: login. Selector: `LOG IN button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 326.63 x 44 | = | - | = |
| Padding | 0px 16px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | #f2f2f2 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Clarkson 12px/22px 500 | = | - | = |
| Letter spacing | 0.5px | = | - | = |
| Colour | #b7b7b7 | = | - | = |
| Text node | span: Clarkson 12px/22px 500, #b7b7b7, ls 0.5px | = | - | = |
| Transition | transform 0.05s ease | = | - | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | - | = |
| Cursor | not-allowed | = | - | = |
| Painted layers | button.css-14vi2qu 326.6x44.0 bg #f2f2f2 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Error | - | = | keyboard focus could not reach the element | = |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-pressed.png`.

#### oauth-google

OAuth Google. The Google OAuth row on the sign-in card. Measured, never pressed.

Page: login. Selector: `"Continue with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 326.63 x 55 | = | = | = |
| Padding | 0px 22px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Clarkson 14px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.css-40sddq: Clarkson 14px/22px 500, #000000 | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 18 x 18, colour #000000 | = | = | = |
| ::before | 324.625px x 53px, absolute, bg #e7e7e7, radius 0px | = | = | = |
| Painted layers | button.css-ds0862 326.6x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-ds0862 324.625pxx53px bg #e7e7e7 | = | button.css-ds0862.focus-visible 326.6x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px outline 2px solid #000000 @ 0 offset 2px; button::before.css-ds0862.focus-visible 324.625pxx53px bg #e7e7e7 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-google-default.png`, `oauth-google-hover.png`, `oauth-google-focus-visible.png`, `oauth-google-pressed.png`.

#### oauth-apple

OAuth Apple. The Apple OAuth row.

Page: login. Selector: `"Continue with Apple"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 326.63 x 55 | = | = | = |
| Padding | 0px 22px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Clarkson 14px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.css-40sddq: Clarkson 14px/22px 500, #000000 | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 20, colour #000000 | = | = | = |
| ::before | 324.625px x 53px, absolute, bg #e7e7e7, radius 0px | = | = | = |
| Painted layers | button.css-ds0862 326.6x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-ds0862 324.625pxx53px bg #e7e7e7 | = | button.css-ds0862.focus-visible 326.6x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px outline 2px solid #000000 @ 0 offset 2px; button::before.css-ds0862.focus-visible 324.625pxx53px bg #e7e7e7 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-apple-default.png`, `oauth-apple-hover.png`, `oauth-apple-focus-visible.png`, `oauth-apple-pressed.png`.

#### oauth-facebook

OAuth Facebook. The Facebook OAuth row.

Page: login. Selector: `"Continue with Facebook"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 326.63 x 55 | = | = | = |
| Padding | 0px 22px | = | = | = |
| Border | 1px solid #000000 | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 2px | = |
| Font | Clarkson 14px/22px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Text node | div.css-40sddq: Clarkson 14px/22px 500, #000000 | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 22 x 22, colour #000000 | = | = | = |
| ::before | 324.625px x 53px, absolute, bg #e7e7e7, radius 0px | = | = | = |
| Painted layers | button.css-ds0862 326.6x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000; button::before.css-ds0862 324.625pxx53px bg #e7e7e7 | = | button.css-ds0862.focus-visible 326.6x55.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 shadow #ffffff 0px 0px 0px 2px, #000000 0px 0px 0px 4px outline 2px solid #000000 @ 0 offset 2px; button::before.css-ds0862.focus-visible 324.625pxx53px bg #e7e7e7 | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `oauth-facebook-default.png`, `oauth-facebook-hover.png`, `oauth-facebook-focus-visible.png`, `oauth-facebook-pressed.png`.

#### cant-login

Can't log in link. The recovery link under the OAuth rows.

Page: login. Selector: `"CAN'T LOG IN?"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 93.05 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 12px/22px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #0e0e0e | = | = | = |
| Text node | span: Clarkson 12px/22px 500, #0e0e0e, ls 0.5px | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 93.0469px x 36px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | div.css-mzw0dv 0.0x2.0 border T:2px solid #0e0e0e | div.css-mzw0dv 93.0x2.0 border T:2px solid #0e0e0e | a::after.css-1jn8g6k.focus-visible 105.047pxx28px border T:2px solid #0e0e0e / R:2px solid #0e0e0e / B:2px solid #0e0e0e / L:2px solid #0e0e0e; div.css-mzw0dv 0.0x2.0 border T:2px solid #0e0e0e | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 105.047px x 28px, absolute, bg #000000 @ 0, radius 0px | = |

Crops: `cant-login-default.png`, `cant-login-hover.png`, `cant-login-focus-visible.png`, `cant-login-pressed.png`.

#### create-account-link

Create account link. The CREATE ACCOUNT tab beside LOG IN on the gate.

Page: login. Selector: `"CREATE ACCOUNT" link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 116.27 x 36 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 12px/22px 500 | = | = | = |
| Letter spacing | 0.5px | = | = | = |
| Colour | #0e0e0e | = | = | = |
| Text node | span: Clarkson 12px/22px 500, #0e0e0e, ls 0.5px | = | = | = |
| Transition | transform 0.05s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 116.266px x 36px, absolute, bg #000000 @ 0, radius 0px | = | = | = |
| Painted layers | div.css-mzw0dv 0.0x2.0 border T:2px solid #0e0e0e | div.css-mzw0dv 116.3x2.0 border T:2px solid #0e0e0e | a::after.css-1uj0sxn.focus-visible 128.266pxx28px border T:2px solid #0e0e0e / R:2px solid #0e0e0e / B:2px solid #0e0e0e / L:2px solid #0e0e0e; div.css-mzw0dv 0.0x2.0 border T:2px solid #0e0e0e | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| ::after | - | = | 128.266px x 28px, absolute, bg #000000 @ 0, radius 0px | = |

Crops: `create-account-link-default.png`, `create-account-link-hover.png`, `create-account-link-focus-visible.png`, `create-account-link-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The bar at 390: 55px, wordmark and a hamburger.

Page: mobile. Selector: `.menu-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 55 |
| Padding | 16px 20px |
| Border | none |
| Radius | 0px |
| Background | #ffffff @ 0 |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Transition | background 0.25s ease-in-out |
| Painted layers | div.menu-container.frontsite-hero-nav 390.0x55.0 bg #ffffff @ 0; a.navlogo__tryscheduling-btn.try 121.5x38.0 bg #283849 r 12px; div.dropdown__content 0.0x0.0 bg #ffffff r 22px shadow #000000 @ 0.05 0px 4px 4px 2px; a.solutions-grid__item 0.0x0.0 border B:1px solid #f2f2f2; a.solutions-grid__item 0.0x0.0 border B:1px solid #f2f2f2; a.solutions-grid__item 0.0x0.0 border B:1px solid #f2f2f2 |
| How | at rest |

Crops: `m-header-default.png`.

#### m-hamburger

Hamburger button. The menu trigger; opens the full-screen menu.

Page: mobile. Selector: `button.hamburger-icon`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 25 x 16 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 0px | = |
| Font | Clarkson 16px/16px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #222222 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 1 up div.menu-container.frontsite-hero-nav bg #ffffff @ 0 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | button.reset-button.hamburger-icon 25.0x16.0 outline 1px auto #e59700 offset 0px | = |

Crops: `m-hamburger-default.png`, `m-hamburger-hover.png`, `m-hamburger-focus-visible.png`, `m-hamburger-pressed.png`.

#### m-menu

Mobile menu. The full-height menu the hamburger opens (.mobile-menu-container): primary links stacked.

Page: mobile. Selector: `.mobile-menu-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 @ 0.5 |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | a.mobile-link: Clarkson 28px/37.52px 400, #2d2d2d |
| Transition | background 0.3s ease-in delay 0.15s |
| Painted layers | div.mobile-menu-container.enter 390.0x844.0 bg #000000 @ 0.5; div.mobile-menu-content.mobile-menu-content--full-height 390.0x844.0 bg #ffffff; div.mobile-menu-header 390.0x104.0 bg #ffffff; li 350.0x58.5 border B:1px solid #f2f2f2; li 350.0x58.5 border B:1px solid #f2f2f2; div.mobile-menu-solutions__item 0.0x0.0 border B:1px solid #f2f2f2 |
| How | at rest |

Crops: `m-menu-default.png`.

#### m-menu-link

Mobile menu link. A primary link in the mobile menu.

Page: mobile. Selector: `.mobile-menu-primary a.mobile-link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 350 x 37.52 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #e59700 offset 1px | = |
| Font | Clarkson 28px/37.52px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d2d2d | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.mobile-link 350.0x37.5 outline 1px auto #e59700 offset 1px | = |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile hero. The hero at 390.

Page: mobile. Selector: `section.hero-block`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 1192.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/16px 400 |
| Letter spacing | normal |
| Colour | #222222 |
| Text node | h1: Clarkson-Serif 32px/38.4px 500, #283849 |
| Transition | none |
| Icon | 22 x 22, colour #283849, fill #000000 |
| Painted layers | div.large-csp-hero__gradient.large-csp-hero__gradient--5 390.0x1192.8 image linear-gradient(66deg, #ebddda 0px, #ebdadb 75%, #f5eff6 100%); div::after.large-csp-hero__gradient.large-csp-hero__gradient--5 390pxx357.828px image linear-gradient(#000000 @ 0, #ffffff); a 0.0x0.0 bg #283849 r 12px; a.hero-cta-email 240.0x56.0 border T:1px solid #283849 / R:1px solid #283849 / B:1px solid #283849 / L:1px solid #283849 r 12px; a.hero-cta-google 240.0x56.0 border T:1px solid #283849 / R:1px solid #283849 / B:1px solid #283849 / L:1px solid #283849 r 12px; div.carousel__frame-slide-wrapper 239.7x447.4 r 24px shadow #000000 @ 0.12 0px 2px 8px 0px, #000000 @ 0.08 0px 0px 1px 0px |
| Ancestor paint | 1 up body bg #ffffff |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

Acuity's frontsite CSS is readable in the CSSOM on each page; the per-state Transition rows above are computed values measured on the components themselves, this list is what the stylesheets declare.

- home: none

- pricing: none
