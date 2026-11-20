# Bio Sites component measurements

Computed styles read from biosites.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the light theme every captured route paints (the site declares no design-token custom properties at all; a TrustArc consent mount stays empty in this geo), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### navbar

Navbar. The fixed top bar (a #navbar div, not a header): the BIO.SITES mark left, BLOG / LOG IN / SIGN UP FOR FREE pills right.

Page: home. Selector: `#navbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 97 |
| Padding | 40px 40px 0px 40px |
| Border | none |
| Radius | 39px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Clarkson 12px/13.2px 500, #000000 |
| Transition | all 0.3s ease |
| Icon | 49 x 40, colour #000000, fill #ffffff |
| Painted layers | a.index_navbarButtons__button__Y11L3 81.3x40.0 bg #ffffff r 40px; a.index_navbarButtons__button__Y11L3 88.8x40.0 bg #ffffff r 40px; a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 155.2x40.0 bg #ffffff r 40px |
| How | at rest |

Crops: `navbar-default.png`.

#### logo

Logo. The BIO.SITES wordmark and Squarespace tagline (svg inside the first nav anchor).

Page: home. Selector: `#navbar a (first)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 203 x 57 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| Icon | 49 x 40, colour #000000, fill #ffffff |
| How | at rest |

Crops: `logo-default.png`.

#### nav-link

Nav link. The BLOG pill, the only outbound item in the bar (text-transform renders "Blog" caps).

Page: home. Selector: `#navbar a:has-text("Blog")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 81.34 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #ffffff | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 12px/13.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Text node | span: Clarkson 12px/13.2px 500, #000000 | span: Clarkson 12px/13.2px 500, #ffffff | = | span: Clarkson 12px/13.2px 500, #ffffff |
| Transition | background-color, color, border 0.3s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.index_navbarButtons__button__Y11L3 81.3x40.0 bg #ffffff r 40px | a.index_navbarButtons__button__Y11L3 81.3x40.0 bg #000000 r 40px | = | a.index_navbarButtons__button__Y11L3 81.3x40.0 bg #000000 r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

#### nav-login

Log in pill. The inverted pill linking to /editor?loginUser=true. Measured, never followed.

Page: home. Selector: `#navbar a:has-text("Log in")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 88.83 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #ffffff | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 12px/13.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Text node | span: Clarkson 12px/13.2px 500, #000000 | span: Clarkson 12px/13.2px 500, #ffffff | = | span: Clarkson 12px/13.2px 500, #ffffff |
| Transition | background-color, color, border 0.3s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.index_navbarButtons__button__Y11L3 88.8x40.0 bg #ffffff r 40px | a.index_navbarButtons__button__Y11L3 88.8x40.0 bg #000000 r 40px | = | a.index_navbarButtons__button__Y11L3 88.8x40.0 bg #000000 r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

Sign up pill. The black "SIGN UP FOR FREE" pill linking to /editor. Measured, never followed.

Page: home. Selector: `#navbar a:has-text("Sign up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 155.17 x 40 | = | = | = |
| Padding | 0px 24px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #ffffff | #000000 | = | #000000 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 12px/13.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | #ffffff | = | #ffffff |
| Text node | span: Clarkson 12px/13.2px 500, #000000 | span: Clarkson 12px/13.2px 500, #ffffff | = | span: Clarkson 12px/13.2px 500, #ffffff |
| Transition | background-color, color, border 0.3s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 155.2x40.0 bg #ffffff r 40px | a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 155.2x40.0 bg #000000 r 40px | = | a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 155.2x40.0 bg #000000 r 40px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

#### page-ground

Page ground. The body fill: black under the hero collage; the content sections paint their own surfaces.

Page: home. Selector: `body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 7535.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Clarkson 12px/13.2px 500, #000000 |
| Transition | none |
| Icon | 49 x 40, colour #000000, fill #ffffff |
| Painted layers | body 1440.0x7535.8 bg #000000; a.index_navbarButtons__button__Y11L3 81.3x40.0 bg #ffffff r 40px; a.index_navbarButtons__button__Y11L3 88.8x40.0 bg #ffffff r 40px; a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 155.2x40.0 bg #ffffff r 40px; div.index_heroContainer__km_g5 1440.0x900.0 bg #ffffff; div.index_mask__YPvnw 1440.0x720.0 image linear-gradient(#111111 -39.18%, #111111 @ 0 49.17%) r 0px 0px 40px 40px |
| How | at rest |

Crops: none.

### Home

#### hero-title

Hero title. "Your brand, your storefront, one link." under the dark collage band.

Page: home. Selector: `first h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 355 x 70 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 35px/35px 500 |
| Letter spacing | -1px |
| Colour | #000000 |
| Text node | span: Clarkson 35px/35px 500, #000000, ls -1px |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-sub

Hero subcopy.

Page: home. Selector: `first long paragraph under h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 437 x 87 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 21px/29px 400 |
| Letter spacing | -0.5px |
| Colour | #6a6a6a |
| Text node | span: Clarkson 21px/29px 400, #6a6a6a, ls -0.5px |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### cta

CTA button. The black "Create a free Bio Site" pill repeated down the page; a real <button>. Measured, never pressed for real.

Page: home. Selector: `button:has-text("Create a free Bio Site")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 325 x 80 | = | = | = |
| Padding | 10px 32px | = | = | = |
| Border | 1px solid #010101 | 1px solid #e6e6e6 | = | 1px solid #e6e6e6 |
| Radius | 46px | = | = | = |
| Background | #000000 | #ffffff | = | #ffffff |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 21px/23px 400 | = | = | = |
| Letter spacing | -0.5px | = | = | = |
| Colour | #ffffff | #010101 | = | #010101 |
| Text node | span: Clarkson 21px/23px 400, #ffffff, ls -0.5px | span: Clarkson 21px/23px 400, #010101, ls -0.5px | = | span: Clarkson 21px/23px 400, #010101, ls -0.5px |
| Transition | background-color, color, border 0.3s linear | = | = | = |
| Cursor | default | pointer | = | pointer |
| Painted layers | button.index_heroHeaderCTA__uwh02 325.0x80.0 bg #000000 border T:1px solid #010101 / R:1px solid #010101 / B:1px solid #010101 / L:1px solid #010101 r 46px | button.index_heroHeaderCTA__uwh02 325.0x80.0 bg #ffffff border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 46px | = | button.index_heroHeaderCTA__uwh02 325.0x80.0 bg #ffffff border T:1px solid #e6e6e6 / R:1px solid #e6e6e6 / B:1px solid #e6e6e6 / L:1px solid #e6e6e6 r 46px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-default.png`, `cta-hover.png`, `cta-focus-visible.png`, `cta-pressed.png`.

#### section-nav-link

Section link. One of the STAND OUT / SELL / CONNECT / ANALYZE anchor links under the hero.

Page: home. Selector: `a[href="#standout"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380.17 x 70 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 70px/70px 500 | = | = | = |
| Letter spacing | -2px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | opacity 0.5s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| ::before | 10px x 10px, absolute, bg #ffffff, radius 50% | = | = | = |
| Painted layers | a::before.index_blendWithBackground__VcFba 10pxx10px bg #ffffff r 50% | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `section-nav-link-default.png`, `section-nav-link-hover.png`, `section-nav-link-focus-visible.png`, `section-nav-link-pressed.png`.

#### section-title

Section title.

Page: home. Selector: `h2:has-text("Stand out")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 331.19 x 25.2 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 18px/25.2px 400 |
| Letter spacing | -0.5px |
| Colour | #010101 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### eyebrow

Eyebrow label. The "TRUSTED BY MILLIONS OF" small-caps label over the carousel.

Page: home. Selector: `h3:has-text("Trusted by")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 417.59 x 23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 18.72px/normal 500 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Clarkson 18.72px/normal 500, #000000 |
| Transition | none |
| How | at rest |

Crops: `eyebrow-default.png`.

#### persona-card

Persona card. A template card in the sliding carousel ("Health & Wellness", "Musician", …) with a "Get started ↗" link.

Page: home. Selector: `marked ancestor of a Get started link`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 325 x 480 |
| Padding | 20px 60px 0px 60px |
| Border | none |
| Radius | 20px |
| Background | #4f566f |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/normal 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.index_cardHeading__O9mki: sans-serif 14px/17px 400, #ffffff, ls -0.5px |
| Transition | none |
| Painted layers | figure.index_card__KykGK 325.0x480.0 bg #4f566f r 20px; a.index_getStartedBtn__GZirW 305.0x45.6 bg #000000 @ 0.25 r 46px |
| How | at rest |

Crops: `persona-card-default.png`.

#### card-cta

Card CTA. The "Get started ↗" link inside a persona card, straight to /editor (each state reads whichever card the marquee had in view; hover/pressed force :hover on the link and its card, because a pointer can never hold the moving card still). Measured, never followed.

Page: home. Selector: `a:has-text("Get started")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 305 x 45.59 | = | = | = |
| Padding | 14px | = | = | = |
| Border | none | = | = | = |
| Radius | 46px | = | = | = |
| Background | #000000 @ 0.25 | = | = | = |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(50px) | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 16px/17.6px 400 | = | = | = |
| Letter spacing | -0.5px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span: Clarkson 16px/17.6px 400, #ffffff, ls -0.5px | = | = | = |
| Transition | all 0.2s ease-out | all 0.2s ease-in | = | all 0.2s ease-in |
| Opacity | 0 | - | = | - |
| Cursor | pointer | = | = | = |
| Painted layers | a.index_getStartedBtn__GZirW 305.0x45.6 bg #000000 @ 0.25 r 46px | = | = | = |
| How | marked the in-view instance | CDP forcePseudoState :hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `card-cta-default.png`, `card-cta-hover.png`, `card-cta-focus-visible.png`, `card-cta-pressed.png`.

#### faq-item

FAQ item. A question row of the static FAQ <dl>; answers are always painted, nothing to expand.

Page: home. Selector: `h3:has-text("Why should I use")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 316.86 x 29.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 21px/29.4px 400 |
| Letter spacing | -0.5px |
| Colour | #000000 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `faq-item-default.png`.

### Footer

#### footer

Footer. The bottom band: a white outer band holding the "BUILD YOUR FREE LINK IN BIO PAGE" CTA, with near-black (rgb(1,1,1)) inner panels painting the BIO.SITE/YOURNAME marquee and the ABOUT/SUPPORT/CONTACT/LEGAL/SOCIAL link hub.

Page: home. Selector: `marked footer div`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 673.42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | sans-serif 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Clarkson 18px/19.8px 500, #ffffff, ls -0.5px |
| Transition | none |
| Icon | 49 x 40, colour #000000, fill #ffffff |
| Painted layers | div.index_fixedFooter__HyRSl 1440.0x673.4 bg #ffffff; div.index_megaLinkContainer__4dOH4 1440.0x461.8 bg #010101; div.index_linkHubContainer__JDRhO 1440.0x251.6 bg #010101; div.index_divider__AvaJ9 1360.0x1.0 bg #ffffff |
| How | at rest |

Crops: `footer-default.png`.

#### footer-cta

Footer marquee. The giant "BIO.SITE/YOURNAME ↗" call; its ancestor links to /editor. Measured, never followed.

Page: home. Selector: `h2:has-text("BIO.SITE/YOURNAME")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 776.55 x 98 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Clarkson 70px/98px 500 | = | - | = |
| Letter spacing | -0.5px | = | - | = |
| Colour | #ffffff | = | - | = |
| Text node | span: Clarkson 70px/98px 500, #ffffff, ls -0.5px | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `footer-cta-default.png`, `footer-cta-hover.png`, `footer-cta-pressed.png`.

#### footer-link

Footer link. An ABOUT column link (Squarespace).

Page: home. Selector: `a:has-text("Squarespace")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106.81 x 23 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 18px/29.4px 400 | = | = | = |
| Letter spacing | -0.5px | = | = | = |
| Colour | #6a6a6a | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-legal

Legal link.

Page: home. Selector: `a:has-text("Terms of service")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123.16 x 22.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6a6a6a | = | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-legal-default.png`, `footer-legal-hover.png`, `footer-legal-focus-visible.png`, `footer-legal-pressed.png`.

#### footer-social

Social link. A SOCIAL column link (Instagram; TikTok is the same control).

Page: home. Selector: `a:has-text("Instagram")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 76.09 x 22.41 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 16px/22.4px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6a6a6a | = | = | #ffffff |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

### Claim (signed-out editor)

#### claim-title

Claim title. "Claim your free username" on the signed-out /editor screen.

Page: claim. Selector: `text "Claim your free"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 387.27 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 32px/42px 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Transition | none |
| How | at rest |

Crops: `claim-title-default.png`.

#### claim-field-wrap

Username field shell. The 50px-radius bordered pill holding the bio.site/ prefix, the input and the circular submit.

Page: claim. Selector: `bordered ancestor of the username input (marked in-page)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 652 x 102 |
| Padding | 0px |
| Border | 1px solid #000000 @ 0.2 |
| Radius | 50px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 10px/normal 400 |
| Letter spacing | normal |
| Colour | #1b1b1b |
| Text node | span.Editor-pages-CreateSite-_pages-UsernameSearch-UsernameSearch__searchPrefix--_vj7Y: Clarkson 36px/22px 400, #1b1b1b |
| Transition | none |
| Icon | 28 x 28, colour #e6e6e6 |
| Painted layers | div.Editor-pages-CreateSite-_pages-UsernameSearch-UsernameSearch__searchContainer--Y1hLC 652.0x102.0 border T:1px solid #000000 @ 0.2 / R:1px solid #000000 @ 0.2 / B:1px solid #000000 @ 0.2 / L:1px solid #000000 @ 0.2 r 50px; button.Editor-pages-CreateSite-_pages-UsernameSearch-UsernameSearch__submit--L6wVx 53.0x53.0 bg #2a2a2a r 100% |
| How | at rest |

Crops: `claim-field-wrap-default.png`.

#### claim-field

Username field. The "bio.site/username" text input; a throwaway string was typed and deleted, nothing submitted.

Page: claim. Selector: `input[type=text]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 357.94 x 44 | = | = |
| Padding | 0px 10px 0px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Clarkson 36px/22px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #000000 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #9c9c9c, opacity 1 | = | = |
| How | at rest | clicked into the field | typed "capturesample", then deleted; nothing sent |

Crops: `claim-field-default.png`, `claim-field-focused.png`, `claim-field-filled.png`.

#### claim-submit

Claim submit. The circular arrow button inside the field pill. Measured, never pressed for real — nothing was claimed.

Page: claim. Selector: `button.UsernameSearch__submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53 x 53 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 100% | = | - | = |
| Background | #2a2a2a | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Clarkson 10px/normal 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #1b1b1b | = | - | = |
| Transition | none | = | - | = |
| Opacity | 0.2 | = | - | = |
| Icon | 28 x 28, colour #e6e6e6 | = | - | = |
| Painted layers | button.Editor-pages-CreateSite-_pages-UsernameSearch-UsernameSearch__submit--L6wVx 53.0x53.0 bg #2a2a2a r 100% | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `claim-submit-default.png`, `claim-submit-hover.png`, `claim-submit-pressed.png`.

#### claim-login

Log in button. The "Log In" pill top right of the claim screen. Measured, never pressed.

Page: claim. Selector: `button:has-text("Log In")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 112.73 x 40 | = | = | = |
| Padding | 0px 36px | = | = | = |
| Border | none | = | = | = |
| Radius | 20px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #000000 @ 0.24 0px 20px 60px 0px | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Clarkson 14px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1b1b1b | = | = | = |
| Text node | span: Clarkson 14px/normal 400, #1b1b1b | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.Editor-pages-CreateSite-CreateSite__logInButton--OIJGh 112.7x40.0 bg #ffffff r 20px shadow #000000 @ 0.24 0px 20px 60px 0px | = | button.Editor-pages-CreateSite-CreateSite__logInButton--OIJGh 112.7x40.0 bg #ffffff r 20px shadow #000000 @ 0.24 0px 20px 60px 0px outline 1px auto #005fcc offset 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `claim-login-default.png`, `claim-login-hover.png`, `claim-login-focus-visible.png`, `claim-login-pressed.png`.

#### claim-legal

Legal link. The Privacy Policy link in the claim footer (squarespace.com). Measured, never followed.

Page: claim. Selector: `a:has-text("Privacy Policy")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 63.92 x 12 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Clarkson 10px/12px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9c9c9c | = | = | = |
| Text node | span: Clarkson 10px/12px 400, #9c9c9c | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 63.9x12.0 outline 1px auto #005fcc offset 1px | = |

Crops: `claim-legal-default.png`, `claim-legal-hover.png`, `claim-legal-focus-visible.png`, `claim-legal-pressed.png`.

### Mobile (390 wide)

#### m-navbar

Mobile navbar. The fixed bar at 390 wide: the circle-dot mark, BLOG and LOG IN text links, the black SIGN UP pill. No menu trigger exists.

Page: home. Selector: `#navbar`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 64 |
| Padding | 12px 16px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.12 0px 20px 60px 0px |
| Outline | none |
| Font | sans-serif 16px/normal 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span: Clarkson 12px/13.2px 500, #000000 |
| Transition | all 0.3s ease |
| Icon | 43 x 36, colour #000000 |
| Painted layers | div.index_navbar__7al9c.index_scrolled__JL789 390.0x64.0 bg #ffffff shadow #000000 @ 0.12 0px 20px 60px 0px; a.index_navbarButtons__button__Y11L3.index_invert__e1qwV 63.3x40.0 bg #ffffff r 40px; a.index_navbarButtons__button__Y11L3.index_invert__e1qwV 70.8x40.0 bg #ffffff r 40px; a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 78.6x40.0 bg #000000 r 40px |
| How | at rest |

Crops: `m-navbar-default.png`.

#### m-signup

Mobile sign up pill. The black SIGN UP pill, the mobile bar's only button. Measured, never followed.

Page: home. Selector: `#navbar a:has-text("Sign up")`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.61 x 40 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 40px | = | = | = |
| Background | #000000 | #ffffff | = | #ffffff |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Clarkson 12px/13.2px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #000000 | = | #000000 |
| Text node | span: Clarkson 12px/13.2px 500, #ffffff | span: Clarkson 12px/13.2px 500, #000000 | = | span: Clarkson 12px/13.2px 500, #000000 |
| Transition | background-color, color, border 0.3s linear | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 78.6x40.0 bg #000000 r 40px | a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 78.6x40.0 bg #ffffff r 40px | = | a.index_navbarButtons__button__Y11L3.index_navbarButtons__button--signup__rRABN 78.6x40.0 bg #ffffff r 40px |
| Ancestor paint | 3 up div.index_navbar__7al9c.index_scrolled__JL789 bg #ffffff shadow #000000 @ 0.12 0px 20px 60px 0px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-signup-default.png`, `m-signup-hover.png`, `m-signup-focus-visible.png`, `m-signup-pressed.png`.

#### m-cta

Mobile CTA. The "Create a free Bio Site" button at 390 wide.

Page: home. Selector: `button:has-text("Create a free Bio Site")`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 325 x 64 |
| Padding | 10px 32px |
| Border | 1px solid #010101 |
| Radius | 46px |
| Background | #000000 |
| Box shadow | none |
| Outline | none |
| Font | Clarkson 16px/23px 400 |
| Letter spacing | -0.5px |
| Colour | #ffffff |
| Text node | span: Clarkson 16px/23px 400, #ffffff, ls -0.5px |
| Transition | background-color, color, border 0.3s linear |
| Cursor | default |
| Painted layers | button.index_heroHeaderCTA__uwh02 325.0x64.0 bg #000000 border T:1px solid #010101 / R:1px solid #010101 / B:1px solid #010101 / L:1px solid #010101 r 46px |
| How | at rest |

Crops: `m-cta-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: none
