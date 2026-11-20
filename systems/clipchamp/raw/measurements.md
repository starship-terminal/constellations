# Component measurements

Computed styles read from clipchamp.com on 2026-11-17 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) on the site's light surface (the cookie banner is hidden, never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Nav bar. The sticky 1440 top nav (position:sticky): logo, four dropdown menus, Sign-in and Try-for-free actions.

Page: home. Selector: `header[class*=_Header]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 62 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | a: segoeVariableFont 18px/20px 400, #545472 |
| Transition | none |
| Icon | 146.81 x 32, colour #5a4cdb |
| ::after | 1440px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | header.Wg1Dzq_Header.sticky 1440.0x62.0 bg #ffffff; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 111.0x42.0 border T:1px solid #433ac7 / R:1px solid #433ac7 / B:1px solid #433ac7 / L:1px solid #433ac7 r 10px; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 139.0x42.0 bg #6453e4 border T:1px solid #6453e4 / R:1px solid #6453e4 / B:1px solid #6453e4 / L:1px solid #6453e4 r 10px; div.PrxzyG_SideBarBackDrop 1440.0x900.0 bg #211e4f @ 0; div.PrxzyG_SideBarDrawer 500.0x900.0 bg #ffffff; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 420.0x42.0 border T:1px solid #433ac7 / R:1px solid #433ac7 / B:1px solid #433ac7 / L:1px solid #433ac7 r 10px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The Clipchamp wordmark anchor (purple mark + logotype; the mark paints #5a4cdb).

Page: home. Selector: `a[class*=_LogoParent]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 146.81 x 32 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #6453e4 |
| Transition | none |
| Cursor | pointer |
| Icon | 146.81 x 32, colour #5a4cdb |
| How | at rest |

Crops: `logo-default.png`.

#### nav-item

Nav menu trigger. The "Features" dropdown trigger — an anchor with role=button/aria-haspopup that opens its submenu locally, never navigates.

Page: home. Selector: `a[aria-haspopup=true]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 108 x 44 | = | = | = |
| Padding | 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | segoeVariableFont 18px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #545472 | #6453e4 | = | #6453e4 |
| Transition | color 0.1s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #1c1c1c @ 0.5 | 16 x 16, colour #6453e4 | = | 16 x 16, colour #6453e4 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 108.0x44.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-focus-visible.png`, `nav-item-pressed.png`.

#### nav-submenu

Nav submenu. The Features dropdown panel, held open by hovering its trigger (DesktopNavSubMenuContainer).

Page: home. Selector: `[class*=_DesktopNavSubMenuContainer]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 248 x 810 |
| Padding | 8px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | a: segoeVariableFont 18px/18px 400, #313242 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 810) |
| Cursor | pointer |
| How | at rest |

Crops: `nav-submenu-default.png`.

#### nav-submenu-link

Submenu link. A link inside the open Features submenu.

Page: home. Selector: `[class*=_SubMenuItem] a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 232 x 38 | = |
| Padding | 10px 16px | = |
| Border | none | = |
| Radius | 12px | = |
| Background | transparent | #6453e4 |
| Box shadow | none | = |
| Outline | none | = |
| Font | segoeVariableFont 18px/18px 400 | = |
| Letter spacing | normal | = |
| Colour | #313242 | #ffffff |
| Transition | all 0.2s ease | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |
| Painted layers | - | a 232.0x38.0 bg #6453e4 r 12px |

Crops: `nav-submenu-link-default.png`, `nav-submenu-link-hover.png`.

#### nav-signin

Sign-in button. The outline "Sign in" button (AccentOutlineButton) linking to app.clipchamp.com/login; measured never followed.

Page: home. Selector: `a[data-testid=nav-login-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 111 x 42 | 116.55 x 44.1 | = | 116.55 x 44.1 |
| Padding | 8px 30px | = | = | = |
| Border | 1px solid #433ac7 | 1px solid #6453e4 | 1px solid #000000 | 1px solid #6453e4 |
| Radius | 10px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | segoeVariableFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #433ac7 | #6453e4 | #000000 | #6453e4 |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 111.0x42.0 border T:1px solid #433ac7 / R:1px solid #433ac7 / B:1px solid #433ac7 / L:1px solid #433ac7 r 10px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 116.6x44.1 border T:1px solid #6453e4 / R:1px solid #6453e4 / B:1px solid #6453e4 / L:1px solid #6453e4 r 10px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 111.0x42.0 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 10px outline 2px solid #000000 offset 2px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 116.6x44.1 border T:1px solid #6453e4 / R:1px solid #6453e4 / B:1px solid #6453e4 / L:1px solid #6453e4 r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.05, 0, 0, 1.05, 0, 0) | = | matrix(1.05, 0, 0, 1.05, 0, 0) |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-cta

Nav CTA. The "Try for free" button (GradientButton class; paints solid #6453e4 over a 1px same-colour border) linking to app.clipchamp.com/signup; measured never followed.

Page: home. Selector: `a[data-testid=nav-signup-button]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 42 | 145.95 x 44.1 | = | 145.95 x 44.1 |
| Padding | 8px 30px | = | = | = |
| Border | 1px solid #6453e4 | 1px solid #4d43de | 1px solid #000000 | 1px solid #4d43de |
| Radius | 10px | = | = | = |
| Background | #6453e4 | #4d43de | = | #4d43de |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | segoeVariableFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 139.0x42.0 bg #6453e4 border T:1px solid #6453e4 / R:1px solid #6453e4 / B:1px solid #6453e4 / L:1px solid #6453e4 r 10px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 145.9x44.1 bg #4d43de border T:1px solid #4d43de / R:1px solid #4d43de / B:1px solid #4d43de / L:1px solid #4d43de r 10px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 139.0x42.0 bg #6453e4 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 10px outline 2px solid #000000 offset 2px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 145.9x44.1 bg #4d43de border T:1px solid #4d43de / R:1px solid #4d43de / B:1px solid #4d43de / L:1px solid #4d43de r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.05, 0, 0, 1.05, 0, 0) | = | matrix(1.05, 0, 0, 1.05, 0, 0) |

Crops: `nav-cta-default.png`, `nav-cta-hover.png`, `nav-cta-focus-visible.png`, `nav-cta-pressed.png`.

### Home

#### hero-title

Hero title. "Online video editor" — the hero display headline.

Page: home. Selector: `h1[class*=_HeroTitle]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 359 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 40px/48px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-subtitle

Hero subtitle. The hero subline under the headline.

Page: home. Selector: `[class*=_HeroSubtitle]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 20px/30px 700 |
| Letter spacing | normal |
| Colour | #ffffff @ 0.867 |
| Transition | none |
| How | at rest |

Crops: `hero-subtitle-default.png`.

#### hero-cta

Hero CTA. The "Create a video" WhiteButton under the hero copy — a light pill on the purple hero band; links to signup, never followed.

Page: home. Selector: `a[data-testid=heroBannerButton-0]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163 x 42 | 171.15 x 44.1 | = | 171.15 x 44.1 |
| Padding | 8px 30px | = | = | = |
| Border | 1px solid #ffffff | = | 1px solid #000000 | = |
| Radius | 10px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #1c1c28 @ 0.204 0px 16px 24px -8px | #1c1c28 @ 0.4 0px 16px 24px -8px | none | #1c1c28 @ 0.4 0px 16px 24px -8px |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | segoeVariableFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #6e006c | #b50ac1 | #b50ac1 | #b50ac1 |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.DL38bq_Accent1Palette._8v3Nwa_DefaultButton 163.0x42.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 10px shadow #1c1c28 @ 0.204 0px 16px 24px -8px | a.DL38bq_Accent1Palette._8v3Nwa_DefaultButton 171.2x44.1 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 10px shadow #1c1c28 @ 0.4 0px 16px 24px -8px | a.DL38bq_Accent1Palette._8v3Nwa_DefaultButton 163.0x42.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 10px outline 2px solid #ffffff offset 2px | a.DL38bq_Accent1Palette._8v3Nwa_DefaultButton 171.2x44.1 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 10px shadow #1c1c28 @ 0.4 0px 16px 24px -8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.05, 0, 0, 1.05, 0, 0) | = | matrix(1.05, 0, 0, 1.05, 0, 0) |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### cta-secondary

Section CTA. A mid-page GradientButton inside a ButtonContainer — the section-level signup CTA, the same solid-purple style as the nav CTA in content context.

Page: home. Selector: `main a[class*=_GradientButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 208 x 42 | 218.4 x 44.1 | = | 218.4 x 44.1 |
| Padding | 8px 30px | = | = | = |
| Border | 1px solid #6453e4 | 1px solid #4d43de | 1px solid #000000 | 1px solid #4d43de |
| Radius | 10px | = | = | = |
| Background | #6453e4 | #4d43de | = | #4d43de |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #000000 offset 2px | = |
| Font | segoeVariableFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 208.0x42.0 bg #6453e4 border T:1px solid #6453e4 / R:1px solid #6453e4 / B:1px solid #6453e4 / L:1px solid #6453e4 r 10px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 218.4x44.1 bg #4d43de border T:1px solid #4d43de / R:1px solid #4d43de / B:1px solid #4d43de / L:1px solid #4d43de r 10px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 208.0x42.0 bg #6453e4 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 10px outline 2px solid #000000 offset 2px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 218.4x44.1 bg #4d43de border T:1px solid #4d43de / R:1px solid #4d43de / B:1px solid #4d43de / L:1px solid #4d43de r 10px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.05, 0, 0, 1.05, 0, 0) | = | matrix(1.05, 0, 0, 1.05, 0, 0) |

Crops: `cta-secondary-default.png`, `cta-secondary-hover.png`, `cta-secondary-focus-visible.png`, `cta-secondary-pressed.png`.

#### cta-white

White CTA on dark band. The "Create a video" WhiteButton in the dark AlignedContentWrapper promo block — the light-on-dark signup style (the hero's WhiteButton is hero-cta).

Page: home. Selector: `[class*=_AlignedContentWrapper] a[class*=_WhiteButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 163 x 42 | 171.15 x 44.1 | = | 171.15 x 44.1 |
| Padding | 8px 30px | = | = | = |
| Border | 1px solid #ffffff | = | 1px solid #000000 | = |
| Radius | 10px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #1c1c28 @ 0.204 0px 16px 24px -8px | #1c1c28 @ 0.4 0px 16px 24px -8px | none | #1c1c28 @ 0.4 0px 16px 24px -8px |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | segoeVariableFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #433ac7 | #6453e4 | #6453e4 | #6453e4 |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 163.0x42.0 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 10px shadow #1c1c28 @ 0.204 0px 16px 24px -8px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 171.2x44.1 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 10px shadow #1c1c28 @ 0.4 0px 16px 24px -8px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 163.0x42.0 bg #ffffff border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 10px outline 2px solid #ffffff offset 2px | a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 171.2x44.1 bg #ffffff border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff r 10px shadow #1c1c28 @ 0.4 0px 16px 24px -8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.05, 0, 0, 1.05, 0, 0) | = | matrix(1.05, 0, 0, 1.05, 0, 0) |

Crops: `cta-white-default.png`, `cta-white-hover.png`, `cta-white-focus-visible.png`, `cta-white-pressed.png`.

#### feature-card

Feature link card. A feature link card (LinkCardStyle): a GradientButton-labelled card into a feature page, never followed.

Page: home. Selector: `[class*=_LinkCardStyle]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 402.61 x 221.38 | 414.69 x 228.02 | = | 414.69 x 228.02 |
| Padding | 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #1c1c28 @ 0.1 0px 4px 8px 0px, #1c1c28 @ 0.1 0px 0px 2px 0px | #1c1c28 @ 0.25 0px 8px 16px 0px, #1c1c28 @ 0.2 0px 0px 2px 0px | = | #1c1c28 @ 0.25 0px 8px 16px 0px, #1c1c28 @ 0.2 0px 0px 2px 0px |
| Outline | none | = | = | = |
| Font | segoeVariableFont 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232330 | = | = | = |
| Text node | h3.PG5dYG_Title: segoeVariableFont 18px/21.6px 500, #313242 | h3.PG5dYG_Title: segoeVariableFont 18px/21.6px 500, #6453e4 | = | h3.PG5dYG_Title: segoeVariableFont 18px/21.6px 500, #6453e4 |
| Transition | all 0.2s ease | = | = | = |
| Icon | 16 x 16, colour #433ac7 | 16.48 x 16.48, colour #433ac7 | = | 16.48 x 16.48, colour #433ac7 |
| Painted layers | div.PG5dYG_LinkCardStyle 402.6x221.4 bg #ffffff r 12px shadow #1c1c28 @ 0.1 0px 4px 8px 0px, #1c1c28 @ 0.1 0px 0px 2px 0px | div.PG5dYG_LinkCardStyle 414.7x228.0 bg #ffffff r 12px shadow #1c1c28 @ 0.25 0px 8px 16px 0px, #1c1c28 @ 0.2 0px 0px 2px 0px | div.PG5dYG_LinkCardStyle 402.6x221.4 bg #ffffff r 12px shadow #1c1c28 @ 0.1 0px 4px 8px 0px, #1c1c28 @ 0.1 0px 0px 2px 0px; a 124.0x21.6 outline 1px auto #101010 offset 1px | div.PG5dYG_LinkCardStyle 414.7x228.0 bg #ffffff r 12px shadow #1c1c28 @ 0.25 0px 8px 16px 0px, #1c1c28 @ 0.2 0px 0px 2px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1.03, 0, 0, 1.03, 0, 0) | = | matrix(1.03, 0, 0, 1.03, 0, 0) |

Crops: `feature-card-default.png`, `feature-card-hover.png`, `feature-card-focus-visible.png`, `feature-card-pressed.png`.

#### content-block

Content block. A content slice (ContentBlock) — copy column beside media.

Page: home. Selector: `[class*=_ContentBlock]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 508 x 120 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | p: segoeVariableFont 20px/30px 400, #313242 |
| Transition | none |
| How | at rest |

Crops: `content-block-default.png`.

#### content-block-dark

Dark band. A dark-background content section — the site's dark band inside the single light theme.

Page: home. Selector: `[class*=_DarkBackground]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 79.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 36px/39.6px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `content-block-dark-default.png`.

#### quote

Testimonial. A customer quote block (QuoteWrapper) with the author line.

Page: home. Selector: `[class*=_QuoteWrapper]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 178 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | div.XJz8xW_AuthorName: segoeVariableFont 17.6px/17.6px 500, #4a4a56 |
| Transition | none |
| Painted layers | div.XJz8xW_Quote 616.0x112.0 bg #eaeafa r 2px 16px 16px; div.XJz8xW_Quote 616.0x112.0 bg #eaeafa r 2px 16px 16px |
| How | at rest |

Crops: `quote-default.png`.

#### rating

Rating badge. The store-rating badge row (RatingContainer: stars + score).

Page: home. Selector: `[class*=_RatingContainer]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 352 x 91.19 |
| Padding | 16px |
| Border | 1px solid #e4e4eb |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #4d43de |
| Text node | div.og7zYq_RatingText: segoeVariableFont 14.4px/20px 500, #64647c |
| Transition | box-shadow, transform 0.2s, 0.2s ease, ease delay 0s, 0s |
| Cursor | pointer |
| Icon | 148 x 32, colour #4d43de |
| Painted layers | a.og7zYq_RatingContainer 352.0x91.2 bg #ffffff border T:1px solid #e4e4eb / R:1px solid #e4e4eb / B:1px solid #e4e4eb / L:1px solid #e4e4eb r 16px |
| How | at rest |

Crops: `rating-default.png`.

#### section-title

Section title. The first section heading under the hero.

Page: home. Selector: `first h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 508 x 79.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 36px/39.6px 700 |
| Letter spacing | normal |
| Colour | #313242 |
| Transition | none |
| How | at rest |

Crops: `section-title-default.png`.

#### page-ground

Page ground. The body element's painted fill — the page ground.

Page: home. Selector: `document.body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 5716.92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Times New Roman 16px/24px 400 |
| Letter spacing | normal |
| Colour | #151435 |
| Text node | a: segoeVariableFont 18px/20px 400, #545472 |
| Transition | none |
| Icon | 146.81 x 32, colour #5a4cdb |
| Painted layers | body.WtdJta_variable.q8sKha_variable 1440.0x5716.9 bg #ffffff; div.fui-FluentProvider.fui-FluentProvider_R_db_ 1440.0x5716.9 bg #ffffff; header.Wg1Dzq_Header.sticky 1440.0x62.0 bg #ffffff; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 111.0x42.0 border T:1px solid #433ac7 / R:1px solid #433ac7 / B:1px solid #433ac7 / L:1px solid #433ac7 r 10px; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 139.0x42.0 bg #6453e4 border T:1px solid #6453e4 / R:1px solid #6453e4 / B:1px solid #6453e4 / L:1px solid #6453e4 r 10px; div.PrxzyG_SideBarBackDrop 1440.0x900.0 bg #211e4f @ 0 |
| How | at rest |

Crops: none.

### Pricing

#### pricing-title

Pricing title. The pricing page headline over the plan comparison table.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 608 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 40px/48px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `pricing-title-default.png`.

#### plan-table

Plan table. The Free/Premium comparison table (TableWrapper): header plan cells + feature rows.

Page: pricing. Selector: `[class*=_TableWrapper]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 625 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | p: segoeVariableFont 16px/20px 500, #232330 |
| Transition | none |
| Icon | 18 x 18, colour #64647c |
| Painted layers | table.YLPCUG_Table 1280.0x625.0 border T:1px solid #eaeafa / R:1px solid #eaeafa / B:1px solid #eaeafa / L:1px solid #eaeafa shadow #3c3c48 @ 0.1 0px 4px 24px 0px; th.YLPCUG_HeaderHeadCell 672.2x48.0 bg #eaeafa; th.YLPCUG_HeaderCell.YLPCUG_HeaderHeadCell 311.4x48.0 bg #eaeafa; th.YLPCUG_HeaderCell.YLPCUG_HeaderHeadCell 295.4x48.0 bg #eaeafa; td.YLPCUG_RowHeadCell 672.2x48.0 border T:1px solid #eaeafa / R:1px solid #eaeafa / B:1px solid #eaeafa / L:1px solid #eaeafa; td.YLPCUG_Cell.YLPCUG_CellStyle 311.4x48.0 border T:1px solid #f2f2f8 / R:1px solid #f2f2f8 / B:1px solid #f2f2f8 / L:1px solid #f2f2f8 |
| How | at rest |

Crops: `plan-table-default.png`.

#### plan-head

Plan header cell. A plan header cell (HeaderCell/HeadIcon) carrying the plan name and price.

Page: pricing. Selector: `[class*=_HeaderCell]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 52 x 24 |
| Padding | 0px 20px 0px 8px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 500 |
| Letter spacing | normal |
| Colour | #232330 |
| Transition | none |
| Ancestor paint | 1 up th.YLPCUG_HeaderHeadCell bg #eaeafa |
| How | at rest |

Crops: `plan-head-default.png`.

#### feature-row-head

Feature row head. A feature name cell down the left of the comparison table (RowHeadCell).

Page: pricing. Selector: `[class*=_RowHeadCell]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 672.23 x 48 |
| Padding | 8px 12px |
| Border | 1px solid #eaeafa |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 500 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | p: segoeVariableFont 16px/20px 500, #232330 |
| Transition | none |
| Painted layers | td.YLPCUG_RowHeadCell 672.2x48.0 border T:1px solid #eaeafa / R:1px solid #eaeafa / B:1px solid #eaeafa / L:1px solid #eaeafa |
| Ancestor paint | 3 up table.YLPCUG_Table shadow #3c3c48 @ 0.1 0px 4px 24px 0px |
| How | at rest |

Crops: `feature-row-head-default.png`.

#### feature-cell

Feature cell. A plan value cell in the table (Cell/CellStyle): check, value or dash.

Page: pricing. Selector: `td[class*=_Cell]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 311.41 x 48 |
| Padding | 8px 12px |
| Border | 1px solid #f2f2f8 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #64647c |
| Text node | p: segoeVariableFont 16px/20px 400, #64647c |
| Transition | background 0.1s ease |
| Painted layers | td.YLPCUG_Cell.YLPCUG_CellStyle 311.4x48.0 border T:1px solid #f2f2f8 / R:1px solid #f2f2f8 / B:1px solid #f2f2f8 / L:1px solid #f2f2f8 |
| Ancestor paint | 3 up table.YLPCUG_Table shadow #3c3c48 @ 0.1 0px 4px 24px 0px |
| How | at rest |

Crops: `feature-cell-default.png`.

#### feature-tooltip

Tooltip cell. A feature cell carrying a tooltip affordance (CellTooltip).

Page: pricing. Selector: `[class*=_CellTooltip]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 311.41 x 48 |
| Padding | 8px 12px |
| Border | 1px solid #f2f2f8 |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #64647c |
| Text node | b: segoeVariableFont 16px/20px 500, #64647c |
| Transition | background 0.1s ease |
| Cursor | help |
| Icon | 18 x 18, colour #64647c |
| Painted layers | td.YLPCUG_Cell.YLPCUG_CellStyle 311.4x48.0 border T:1px solid #f2f2f8 / R:1px solid #f2f2f8 / B:1px solid #f2f2f8 / L:1px solid #f2f2f8; div.fui-Tooltip__content.___r8zdtl0 0.0x0.0 bg #302690 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 4px; div.___k5deke0.f1ewtqcl 0.0x0.0 bg #302690 r 0px 0px 0px 2px; div::before.___k5deke0.f1ewtqcl 100%x100% bg #302690 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 0px 0px 0px 2px |
| Ancestor paint | 3 up table.YLPCUG_Table shadow #3c3c48 @ 0.1 0px 4px 24px 0px |
| How | at rest |

Crops: `feature-tooltip-default.png`.

#### faq-item

FAQ item. A pricing FAQ accordion item (details/ItemHeaderContainer); opened with its own summary toggle.

Page: pricing. Selector: `details[class*=_Details]`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 696 x 56 | 696 x 208 |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | segoeVariableFont 16px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #232330 | = |
| Text node | span: segoeVariableFont 20px/24px 400, #5d6276 | span: segoeVariableFont 20px/24px 400, #6453e4 |
| Transition | none | = |
| Icon | 24 x 24, colour #6453e4 | = |
| How | at rest | own toggle |

Crops: `faq-item-default.png`, `faq-item-opened.png`.

#### inline-link

Inline link. An inline entry link in the page copy (InlineEntryLink).

Page: pricing. Selector: `a[class*=_InlineEntryLink]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 207 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | segoeVariableFont 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4d43de | #433ac7 | = | #433ac7 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.hQWgwW_InlineEntryLink 207.0x30.0 outline 1px auto #101010 offset 1px | = |

Crops: `inline-link-default.png`, `inline-link-hover.png`, `inline-link-focus-visible.png`, `inline-link-pressed.png`.

#### pricing-hero

Pricing dark hero. The dark hero band over the plan table (DarkHeroTitle + WhiteButton).

Page: pricing. Selector: `ancestor band of [class*=_DarkHeroTitle]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 640 x 352 |
| Padding | 0px 32px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | h1.d4ZYma_HeroTitle.d4ZYma_DarkHeroTitle: segoeVariableFont 40px/48px 700, #ffffff |
| Transition | none |
| Painted layers | a.brand._8v3Nwa_DefaultButton 211.0x40.0 bg #ffffff r 10px shadow #1c1c28 @ 0.204 0px 16px 24px -8px |
| How | at rest |

Crops: `pricing-hero-default.png`.

#### pricing-cta

Pricing hero CTA. The "Create videos for free" WhiteButton in the dark pricing hero; links to signup, never followed.

Page: pricing. Selector: `dark-hero a[class*=_WhiteButton]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 211 x 40 | = | = | 221.55 x 42 |
| Padding | 8px 30px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | #1c1c28 @ 0.204 0px 16px 24px -8px | = | none | #1c1c28 @ 0.4 0px 16px 24px -8px |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | segoeVariableFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232330 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.brand._8v3Nwa_DefaultButton 211.0x40.0 bg #ffffff r 10px shadow #1c1c28 @ 0.204 0px 16px 24px -8px | = | a.brand._8v3Nwa_DefaultButton 211.0x40.0 bg #ffffff r 10px outline 2px solid #ffffff offset 2px | a.brand._8v3Nwa_DefaultButton 221.5x42.0 bg #ffffff r 10px shadow #1c1c28 @ 0.4 0px 16px 24px -8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, 0) | = | matrix(1.05, 0, 0, 1.05, 0, 0) |

Crops: `pricing-cta-default.png`, `pricing-cta-hover.png`, `pricing-cta-focus-visible.png`, `pricing-cta-pressed.png`.

### Features

#### features-title

Features title. The features index headline.

Page: features. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 608 x 48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 40px/48px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `features-title-default.png`.

#### feature-section

Feature section. An aligned content block on the features index: title, body list of entry links, side media (AlignedContentContainer).

Page: features. Selector: `[class*=_AlignedContentContainer]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1200 x 539.06 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | h2.A55hlG_ContentTitle.dAcj1q_StyledHeading: segoeVariableFont 36px/39.6px 700, #313242 |
| Transition | none |
| How | at rest |

Crops: `feature-section-default.png`.

#### feature-link

Feature entry link. An inline feature link inside a content list (InlineEntryLink); measured never followed.

Page: features. Selector: `a[class*=_InlineEntryLink]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 30 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | segoeVariableFont 20px/30px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #4d43de | #433ac7 | = | #433ac7 |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.hQWgwW_InlineEntryLink 139.0x30.0 outline 1px auto #101010 offset 1px | = |

Crops: `feature-link-default.png`, `feature-link-hover.png`, `feature-link-focus-visible.png`, `feature-link-pressed.png`.

#### feature-heading

Feature section heading. A feature section title inside an aligned content block (ContentTitle/StyledHeading with anchor).

Page: features. Selector: `[class*=_ContentTitle]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 508 x 79.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 36px/39.6px 700 |
| Letter spacing | normal |
| Colour | #313242 |
| Transition | none |
| How | at rest |

Crops: `feature-heading-default.png`.

### App sign-in (boundary)

#### signin-card

Sign-in card. The app.clipchamp.com login surface: the sign-in card the SPA paints. Measured at rest, never submitted.

Page: signin. Selector: `main/first visible login container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 792 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Segoe UI 14px/14px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | h1.sc-fAGzit.jmcQxd: Segoe UI 32px/38.4px 600, #232330 |
| Transition | none |
| Icon | 24 x 24, colour #232330 |
| Painted layers | main.sc-eifrsQ.hOonHL 792.0x900.0 bg #ffffff; button.fui-Button.r1f29ykk 648.0x60.0 bg #13131b @ 0.05 border T:2px solid #dfdfe8 / R:2px solid #dfdfe8 / B:2px solid #dfdfe8 / L:2px solid #dfdfe8 r 4px; div.sc-jOnpCo.duetKj 580.0x1.0 border T:1px solid #e5e5ed; button.fui-Button.r1f29ykk 648.0x60.0 bg #13131b @ 0.05 border T:2px solid #dfdfe8 / R:2px solid #dfdfe8 / B:2px solid #dfdfe8 / L:2px solid #dfdfe8 r 4px; button.fui-Button.r1f29ykk 648.0x60.0 bg #13131b @ 0.05 border T:2px solid #dfdfe8 / R:2px solid #dfdfe8 / B:2px solid #dfdfe8 / L:2px solid #dfdfe8 r 4px; button.fui-Button.r1f29ykk 648.0x60.0 bg #13131b @ 0.05 border T:2px solid #dfdfe8 / R:2px solid #dfdfe8 / B:2px solid #dfdfe8 / L:2px solid #dfdfe8 r 4px |
| How | at rest |

Crops: `signin-card-default.png`.

#### signin-field

Account field. The account/email field on the sign-in card; focused locally, never submitted.

Page: signin. Selector: `first visible input`. States: .

Not found on the page at capture time.

#### signin-button

Continue button. A sign-in/continue control on the card; measured never pressed.

Page: signin. Selector: `first visible button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 648 x 60 | = | 648 x 58 | = |
| Padding | 16px | = | = | = |
| Gap | 16px | = | = | = |
| Border | 2px solid #dfdfe8 | 2px solid #d0d0dd | 1px solid #000000 | 2px solid #000000 @ 0 |
| Radius | 4px | = | = | = |
| Background | #13131b @ 0.05 | #13131b @ 0.1 | = | #13131b @ 0.2 |
| Box shadow | none | = | #000000 0px 0px 0px 1px inset | = |
| Outline | none | = | 2px solid #000000 @ 0 offset 0px | = |
| Font | Segoe UI 18px/20px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #232330 | = | = | = |
| Transition | all 0.1s ease-in-out | = | = | = |
| Cursor | default | pointer | = | pointer |
| Icon | 24 x 24, colour #232330 | = | = | = |
| Painted layers | button.fui-Button.r1f29ykk 648.0x60.0 bg #13131b @ 0.05 border T:2px solid #dfdfe8 / R:2px solid #dfdfe8 / B:2px solid #dfdfe8 / L:2px solid #dfdfe8 r 4px | button.fui-Button.r1f29ykk 648.0x60.0 bg #13131b @ 0.1 border T:2px solid #d0d0dd / R:2px solid #d0d0dd / B:2px solid #d0d0dd / L:2px solid #d0d0dd r 4px | button.fui-Button.r1f29ykk 648.0x58.0 bg #13131b @ 0.05 border T:1px solid #000000 / R:1px solid #000000 / B:1px solid #000000 / L:1px solid #000000 r 4px shadow #000000 0px 0px 0px 1px inset outline 2px solid #000000 @ 0 offset 0px | button.fui-Button.r1f29ykk 648.0x60.0 bg #13131b @ 0.2 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0 r 4px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `signin-button-default.png`, `signin-button-hover.png`, `signin-button-focus-visible.png`, `signin-button-pressed.png`.

### Footer

#### footer

Footer. The footer band: link columns, language selector, social icons and the legal subfooter.

Page: home. Selector: `footer/[class*=_FooterWrapper]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 1062.41 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | p: segoeVariableFont 14px/22.4px 700, #2e248f |
| Transition | none |
| Icon | 0 x 0, colour #2e248f |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. A link in a footer link column. The footer renders duplicate tabindex="-1" clones for the collapsed/mobile variant; only tabindex=0 copies are measured.

Page: home. Selector: `footer [class*=_LinksWrapper] a[tabindex=0]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 120 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | segoeVariableFont 16px/32px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #313242 | #6453e4 | = | #6453e4 |
| Transition | font-variation-settings, color 0.2s, 0.2s ease, ease delay 0s, 0s | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 124 x 4, colour #313242 | 124 x 4, colour #6453e4 | = | 124 x 4, colour #6453e4 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 120.0x21.0 outline 1px auto #101010 offset 1px | = |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-social

Social link. A footer social icon link.

Page: home. Selector: `[class*=_FooterSocial] a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 24 x 21 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 4px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #6453e4 offset 2px | = |
| Font | segoeVariableFont 16px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #313242 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 24 x 24, colour #313242 | 26.4 x 26.4, colour #ff0000 | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 24.0x21.0 r 4px outline 2px solid #6453e4 offset 2px | = |

Crops: `footer-social-default.png`, `footer-social-hover.png`, `footer-social-focus-visible.png`, `footer-social-pressed.png`.

#### footer-lang

Language selector. The footer language selector (LanguageSelectorWrapper).

Page: home. Selector: `[class*=_LanguageSelectorWrapper]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 240 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #2e248f |
| Text node | undefined: segoeVariableFont 16px/normal 400, #2e248f |
| Transition | color, transform 0.2s, 0.2s ease, ease delay 0s, 0s |
| Icon | 20 x 20, colour #2e248f |
| Painted layers | select._aeLXG_LanguageSelectorInput 240.0x42.0 bg #ffffff border T:1px solid #2e248f / R:1px solid #2e248f / B:1px solid #2e248f / L:1px solid #2e248f r 10px |
| How | at rest |

Crops: `footer-lang-default.png`.

### Mobile (390 wide)

#### m-header

Mobile bar. The 390 mobile nav bar: logo + menu toggle.

Page: home. Selector: `header[class*=_Header] at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | #1c1c28 @ 0.15 0px 0px 16px 4px, #1c1c28 @ 0.15 0px 0px 2px 0px |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | p: segoeVariableFont 16px/24px 500, #1c1c1c @ 0.7 |
| Transition | none |
| Icon | 146.81 x 32, colour #5a4cdb |
| ::after | 390px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | header.Wg1Dzq_Header.sticky 390.0x72.0 bg #ffffff shadow #1c1c28 @ 0.15 0px 0px 16px 4px, #1c1c28 @ 0.15 0px 0px 2px 0px; div._96AHPW_Container.Wg1Dzq_HeaderContainer 390.0x72.0 bg #ffffff; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 0.0x0.0 border T:1px solid #433ac7 / R:1px solid #433ac7 / B:1px solid #433ac7 / L:1px solid #433ac7 r 10px; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 0.0x0.0 bg #6453e4 border T:1px solid #6453e4 / R:1px solid #6453e4 / B:1px solid #6453e4 / L:1px solid #6453e4 r 10px; div.PrxzyG_SideBarBackDrop 390.0x844.0 bg #211e4f @ 0; div.PrxzyG_SideBarDrawer 390.0x844.0 bg #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The hamburger (side-bar-nav-button); its own press opens the drawer.

Page: home. Selector: `[data-testid=side-bar-nav-button]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 60 x 60 |
| Padding | 1px 6px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 13.3333px/60px 400 |
| Letter spacing | normal |
| Colour | #313242 |
| Transition | box-shadow 0.2s ease |
| Cursor | pointer |
| Icon | 32 x 32, colour #313242 |
| Ancestor paint | 1 up div._96AHPW_Container.Wg1Dzq_HeaderContainer bg #ffffff; 2 up header.Wg1Dzq_Header.sticky bg #ffffff shadow #1c1c28 @ 0.15 0px 0px 16px 4px, #1c1c28 @ 0.15 0px 0px 2px 0px |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The side-bar drawer after the hamburger press.

Page: home. Selector: `[class*=_SideBarDrawer] after toggle press`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 844 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 16px/20px 400 |
| Letter spacing | normal |
| Colour | #232330 |
| Text node | p: segoeVariableFont 16px/24px 500, #1c1c1c @ 0.7 |
| Transition | none |
| Icon | 32 x 32, colour #313242 |
| Painted layers | div.PrxzyG_SideBarBackDrop 390.0x844.0 bg #211e4f @ 0.9; div.PrxzyG_SideBarDrawer 390.0x844.0 bg #ffffff; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 310.0x42.0 border T:1px solid #433ac7 / R:1px solid #433ac7 / B:1px solid #433ac7 / L:1px solid #433ac7 r 10px; a.DL38bq_BrandPalette._8v3Nwa_DefaultButton 310.0x42.0 bg #6453e4 border T:1px solid #6453e4 / R:1px solid #6453e4 / B:1px solid #6453e4 / L:1px solid #6453e4 r 10px |
| Ancestor paint | 1 up div._96AHPW_Container.Wg1Dzq_HeaderContainer bg #ffffff; 2 up header.Wg1Dzq_Header.sticky bg #ffffff shadow #1c1c28 @ 0.15 0px 0px 16px 4px, #1c1c28 @ 0.15 0px 0px 2px 0px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-menu-link

Menu link. A link row inside the open drawer.

Page: home. Selector: `first link inside the open side bar`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 50 x 48 | = | = | = |
| Padding | 12px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 5px auto #e59700 offset 2px | = |
| Font | segoeVariableFont 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #1c1c1c @ 0.7 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 50.0x48.0 outline 5px auto #e59700 offset 2px | = |

Crops: `m-menu-link-default.png`, `m-menu-link-hover.png`, `m-menu-link-focus-visible.png`, `m-menu-link-pressed.png`.

#### m-hero

Mobile headline. The hero headline at 390.

Page: home. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 251 x 35 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | segoeVariableFont 28px/35px 700 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page (inline styles and same-origin sheets; cross-origin bundles are unreadable); the per-state Transition rows above are computed values and cover the rest.

- home: `color 0.15s, background-color 0.15s, border-color 0.15s, box-shadow 0.15s, opacity 0.15s, background-position 0.15s`, `0.2s`, `opacity 0.2s ease-in-out`, `color var(--hover-duration)`, `box-shadow var(--hover-duration), transform var(--hover-duration)`, `background 0.2s`, `color 0.15s ease-in-out`, `color 0.2s, transform 0.2s`, `color 0.5s`, `box-shadow 0.2s`, `opacity 0.2s`, `0.15s linear`
