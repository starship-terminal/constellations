# Component measurements

Computed styles read from busuu.com on 2026-11-11 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) in the site's one light theme, with the OneTrust consent stack hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Shell and navigation

#### header

Header. The marketing header: logo, Learn for free, Log in, For Educators/Businesses.

Page: home. Selector: `header.main-header-simplified`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 557 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.header-simplified__title: Nista 40px/52px 800, #ffffff |
| Transition | none |
| ::before | 1440px x 557px, absolute, bg #000000 @ 0 linear-gradient(20.78deg, #6e00f8 3.3%, #563ce9 27.67%, #116eee 93.23%), radius 0px |
| Painted layers | header::before.main-header-simplified 1440pxx557px image linear-gradient(20.78deg, #6e00f8 3.3%, #563ce9 27.67%, #116eee 93.23%); a.header-simplified__cta.btn 290.0x48.0 bg #11ee92 border T:2px solid #11ee92 / R:2px solid #11ee92 / B:2px solid #11ee92 / L:2px solid #11ee92 r 45.04px shadow #000000 @ 0.3 0px 2px 4px 0px |
| How | at rest |

Crops: `header-default.png`.

#### logo

Logo. The wordmark anchor (a.nav-dropdown__logo, a labelled svg), top-left of the nav bar.

Page: home. Selector: `a.nav-dropdown__logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 127 x 40 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Cursor | pointer |
| Icon | 127 x 40, colour #0000ee, fill #000000 |
| How | at rest |

Crops: `logo-default.png`.

#### cta-signup

Signup CTA. The header CTA; links to signup, measured never followed.

Page: home. Selector: `header signup CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 290 x 48 | = | = | = |
| Padding | 12px 40px | = | = | = |
| Border | 2px solid #11ee92 | 2px solid #41f1a8 | 2px solid #41f1a8 | 2px solid #41f1a8 |
| Radius | 45.04px | = | = | = |
| Background | #11ee92 | #41f1a8 | #41f1a8 | #41f1a8 |
| Box shadow | #000000 @ 0.3 0px 2px 4px 0px | = | = | = |
| Outline | none | = | = | = |
| Font | Nista 16px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #252b2f | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.header-simplified__cta.btn 290.0x48.0 bg #11ee92 border T:2px solid #11ee92 / R:2px solid #11ee92 / B:2px solid #11ee92 / L:2px solid #11ee92 r 45.04px shadow #000000 @ 0.3 0px 2px 4px 0px | a.header-simplified__cta.btn 290.0x48.0 bg #41f1a8 border T:2px solid #41f1a8 / R:2px solid #41f1a8 / B:2px solid #41f1a8 / L:2px solid #41f1a8 r 45.04px shadow #000000 @ 0.3 0px 2px 4px 0px | a.header-simplified__cta.btn 290.0x48.0 bg #41f1a8 border T:2px solid #41f1a8 / R:2px solid #41f1a8 / B:2px solid #41f1a8 / L:2px solid #41f1a8 r 45.04px shadow #000000 @ 0.3 0px 2px 4px 0px | a.header-simplified__cta.btn 290.0x48.0 bg #41f1a8 border T:2px solid #41f1a8 / R:2px solid #41f1a8 / B:2px solid #41f1a8 / L:2px solid #41f1a8 r 45.04px shadow #000000 @ 0.3 0px 2px 4px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `cta-signup-default.png`, `cta-signup-hover.png`, `cta-signup-focus-visible.png`, `cta-signup-pressed.png`.

#### nav-dropdown

Nav dropdown. The language/product dropdown in the header.

Page: home. Selector: `.nav-dropdown`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 1400 x 40 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Nista 16px/27.2px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #000000 | = | - | = |
| Text node | a.btn.btn--s: Nista 14px/normal 700, #116eee | = | - | = |
| Transition | none | = | - | = |
| Icon | 127 x 40, colour #0000ee, fill #000000 | = | - | = |
| Painted layers | a.btn.btn--s 155.8x33.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 45.04px; a.btn.btn--s 101.0x33.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 45.04px; span::before.responsive-nav__icon.icon 100%x3px bg #116eee; span::after.responsive-nav__icon.icon 65%x3px bg #116eee; div::before.main-nav-dropdown autoxauto border T:9px solid #000000 @ 0 / R:9px solid #000000 @ 0 / B:9px solid #717a8c / L:9px solid #000000 @ 0; div::after.main-nav-dropdown autoxauto border T:9px solid #000000 @ 0 / R:9px solid #000000 @ 0 / B:9px solid #ffffff / L:9px solid #000000 @ 0 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `nav-dropdown-default.png`, `nav-dropdown-hover.png`, `nav-dropdown-pressed.png`.

#### nav-link

Nav link. The nav's Log-in outline button (a.nav-dropdown__btn.btn--outline-default); measured, never followed.

Page: home. Selector: `.nav-dropdown__btn.btn--outline-default`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101 x 33 | = | = | = |
| Padding | 6px 28px | = | = | = |
| Border | 2px solid #ffffff | = | = | = |
| Radius | 45.04px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Nista 14px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn--s 101.0x33.0 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 45.04px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-link-default.png`, `nav-link-hover.png`, `nav-link-focus-visible.png`, `nav-link-pressed.png`.

### Home

#### hero-title

Hero headline.

Page: home. Selector: `h1.header-simplified__title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 504 x 156 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 40px/52px 800 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-cta

Hero CTA. The hero action; measured never followed.

Page: home. Selector: `hero CTA (main/section scope)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 290 x 48 | = | = | = |
| Padding | 12px 40px | = | = | = |
| Border | 2px solid #11ee92 | 2px solid #41f1a8 | 2px solid #41f1a8 | 2px solid #41f1a8 |
| Radius | 45.04px | = | = | = |
| Background | #11ee92 | #41f1a8 | #41f1a8 | #41f1a8 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Nista 16px/normal 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #252b2f | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn--primary-lighter 290.0x48.0 bg #11ee92 border T:2px solid #11ee92 / R:2px solid #11ee92 / B:2px solid #11ee92 / L:2px solid #11ee92 r 45.04px | a.btn.btn--primary-lighter 290.0x48.0 bg #41f1a8 border T:2px solid #41f1a8 / R:2px solid #41f1a8 / B:2px solid #41f1a8 / L:2px solid #41f1a8 r 45.04px | a.btn.btn--primary-lighter 290.0x48.0 bg #41f1a8 border T:2px solid #41f1a8 / R:2px solid #41f1a8 / B:2px solid #41f1a8 / L:2px solid #41f1a8 r 45.04px | a.btn.btn--primary-lighter 290.0x48.0 bg #41f1a8 border T:2px solid #41f1a8 / R:2px solid #41f1a8 / B:2px solid #41f1a8 / L:2px solid #41f1a8 r 45.04px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-cta-default.png`, `hero-cta-hover.png`, `hero-cta-focus-visible.png`, `hero-cta-pressed.png`.

#### hero-sub

Hero copy. The lede under the headline.

Page: home. Selector: `hero lede paragraph`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 540 x 81.56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #252b2f |
| Transition | none |
| How | at rest |

Crops: `hero-sub-default.png`.

#### flag-card

Language card. A language entry in the flag module.

Page: home. Selector: `flag module item`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152 x 114 | = | = | = |
| Padding | 15px 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 16px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Nista 16px/27.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #666e7e | = | = | = |
| Text node | p.flag-text__text: Nista 16px/24px 800, #666e7e | p.flag-text__text: Nista 16px/24px 800, #116eee | = | p.flag-text__text: Nista 16px/24px 800, #116eee |
| Transition | background-color 0.15s ease-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | span.icon.icon--circle 56.0x56.0 r 100% shadow #000000 @ 0.1 0px 1px 2px 0px | = | a.flag-text.js-flag 152.0x114.0 r 16px outline 1px auto #005fcc offset 1px; span.icon.icon--circle 56.0x56.0 r 100% shadow #000000 @ 0.1 0px 1px 2px 0px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `flag-card-default.png`, `flag-card-hover.png`, `flag-card-focus-visible.png`, `flag-card-pressed.png`.

### Premium

#### premium-title

Premium title.

Page: premium. Selector: `h1/h2 on /en/premium`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 585.42 x 44.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 32px/44.8px 800 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `premium-title-default.png`.

#### period-toggle

Period toggle. A billing-period option (12 months/1 month).

Page: premium. Selector: `period option`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78.48 x 22 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Nista 16px/22px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `period-toggle-default.png`, `period-toggle-hover.png`, `period-toggle-pressed.png`.

#### plan-price

Plan price. A monthly price figure inside a tier card.

Page: premium. Selector: `price text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 67.97 x 27 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 18px/27px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `plan-price-default.png`.

#### plan-cta

Plan CTA. A Get Premium action; measured never followed.

Page: premium. Selector: `Get Premium button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 304 x 48 | = | = | = |
| Padding | 12px 24px | = | = | = |
| Border | 2px solid #ffffff | 2px solid #5438dc | = | 2px solid #432db0 |
| Radius | 26px | = | = | = |
| Background | #ffffff | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 0px | = |
| Font | Nista 16px/24px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #5438dc | = | = | #432db0 |
| Transition | all 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-gEvEer.ljlyRc 304.0x48.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 26px | button.sc-gEvEer.ljlyRc 304.0x48.0 bg #ffffff border T:2px solid #5438dc / R:2px solid #5438dc / B:2px solid #5438dc / L:2px solid #5438dc r 26px | button.sc-gEvEer.ljlyRc 304.0x48.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 26px outline 1px auto #005fcc offset 0px | button.sc-gEvEer.ljlyRc 304.0x48.0 bg #ffffff border T:2px solid #432db0 / R:2px solid #432db0 / B:2px solid #432db0 / L:2px solid #432db0 r 26px |
| Ancestor paint | 1 up div.sc-aXZVg.kBEXOl bg #221658 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-card

Plan card. A Premium plan tier card (the Get Premium column).

Page: premium. Selector: `deepest div containing Get Premium`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 356 x 812 |
| Padding | 24px |
| Border | 2px solid #ffffff |
| Radius | 8px |
| Background | #221658 |
| Box shadow | none |
| Outline | none |
| Font | Nista 16px/22px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.sc-fjvvzt.hTTXrX: Nista 16px/24px 700, #1e2d40 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 24 x 24, colour #ffffff |
| Painted layers | div.sc-aXZVg.kBEXOl 356.0x812.0 bg #221658 border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 8px; div.sc-9bc2c4b2-1.gCMeSA 356.0x28.0 bg #ffffff r 8px 8px 0px 0px; button.sc-gEvEer.ljlyRc 304.0x48.0 bg #ffffff border T:2px solid #ffffff / R:2px solid #ffffff / B:2px solid #ffffff / L:2px solid #ffffff r 26px; div.sc-9bc2c4b2-13.craYPm 33.7x1.0 bg #ffffff; div.sc-9bc2c4b2-13.craYPm 33.7x1.0 bg #ffffff |
| How | at rest |

Crops: `plan-card-default.png`.

#### save-badge

Save badge. A SAVE n% label on the plan cards.

Page: premium. Selector: `p with SAVE n%`. States: .

Not found on the page at capture time.

### Course pages

#### course-cta

Course CTA.

Page: course. Selector: `course page CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 161.44 x 48 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | NistaFonts 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #116eee | = | = | = |
| Text node | button.sc-gEvEer.dUizwn: NistaFonts 16px/24px 700, #1e2d40 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-gEvEer.dUizwn 161.4x48.0 bg #11ee92 border T:2px solid #11ee92 / R:2px solid #11ee92 / B:2px solid #11ee92 / L:2px solid #11ee92 r 100px | button.sc-gEvEer.dUizwn 161.4x48.0 bg #88f7c8 border T:2px solid #88f7c8 / R:2px solid #88f7c8 / B:2px solid #88f7c8 / L:2px solid #88f7c8 r 100px | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `course-cta-default.png`, `course-cta-hover.png`, `course-cta-focus-visible.png`, `course-cta-pressed.png`.

#### course-section

Section heading.

Page: course. Selector: `course page h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 840.53 x 62 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NistaFonts 48px/62px 900 |
| Letter spacing | -0.48px |
| Colour | #252b2f |
| Transition | none |
| How | at rest |

Crops: `course-section-default.png`.

#### course-title

Course page title. The visible display heading (the semantic h1 is clipped for accessibility).

Page: course. Selector: `h2 course display heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 560 x 195 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NistaFonts 48px/65px 900 |
| Letter spacing | -0.96px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `course-title-default.png`.

### Signup and login

#### register-title

Signup heading.

Page: register. Selector: `register heading`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 595.13 x 52 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | NistaFonts 40px/52px 800 |
| Letter spacing | normal |
| Colour | #252b2f |
| Transition | none |
| How | at rest |

Crops: `register-title-default.png`.

#### language-item

Language option. A language choice in the signup flow; measured never chosen.

Page: register. Selector: `language option`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 182 x 147 | = | - | = |
| Padding | 0px | = | - | = |
| Border | 1px solid #dae1ea | 1px solid #116eee | - | 1px solid #116eee |
| Radius | 16px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | NistaFonts 16px/22px 700 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #116eee | = | - | = |
| Text node | p.sc-hCPjZK.ePua-dn: NistaFonts 16px/24px 700, #1e2d40 | p.sc-hCPjZK.ePua-dn: NistaFonts 16px/24px 700, #116eee | - | p.sc-hCPjZK.ePua-dn: NistaFonts 16px/24px 700, #116eee |
| Transition | border-color 0.15s ease-out | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 60 x 60, colour #116eee | = | - | = |
| Painted layers | a.sc-ehixzo.edjEfB 182.0x147.0 border T:1px solid #dae1ea / R:1px solid #dae1ea / B:1px solid #dae1ea / L:1px solid #dae1ea r 16px; p.sc-hCPjZK.iKMCem 180.0x29.0 bg #f3f8fe | a.sc-ehixzo.edjEfB 182.0x147.0 border T:1px solid #116eee / R:1px solid #116eee / B:1px solid #116eee / L:1px solid #116eee r 16px; p.sc-hCPjZK.iKMCem 180.0x29.0 bg #f3f8fe | - | a.sc-ehixzo.edjEfB 182.0x147.0 border T:1px solid #116eee / R:1px solid #116eee / B:1px solid #116eee / L:1px solid #116eee r 16px; p.sc-hCPjZK.iKMCem 180.0x29.0 bg #f3f8fe |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `language-item-default.png`, `language-item-hover.png`, `language-item-pressed.png`.

### Footer

#### footer

Footer. The main-footer: link columns, social, legal.

Page: home. Selector: `.main-footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1280 x 640.91 |
| Padding | 30px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | h2.main-footer__title: Nista 16px/27.2px 800, #252b2f |
| Transition | none |
| Icon | 20 x 20, colour #000000, fill #ffffff |
| Painted layers | div::before.form__select-wrap 8pxx6px border R:4px solid #000000 @ 0 / B:6px solid #666e7e / L:4px solid #000000 @ 0; div::after.form__select-wrap 8pxx6px border T:6px solid #666e7e / R:4px solid #000000 @ 0 / L:4px solid #000000 @ 0; select.form__select.js-interface-switcher 220.0x41.2 border T:1px solid #d6dee6 / R:1px solid #d6dee6 / B:1px solid #d6dee6 / L:1px solid #d6dee6 r 5px; div.main-footer__credits.cf 1240.0x79.2 border T:1px solid #d6dee6; span.icon.icon--light 40.0x40.0 bg #a7b0b7 r 100%; span.icon.icon--light 40.0x40.0 bg #a7b0b7 r 100% |
| Ancestor paint | 1 up div.main-footer bg #f2f7fd |
| How | at rest |

Crops: none.

#### footer-link

Footer link.

Page: home. Selector: `.main-footer a`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 145.61 x 17 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #005fcc offset 1px | = |
| Font | Nista 14px/23.8px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #252b2f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 145.6x17.0 outline 1px auto #005fcc offset 1px | = |

Crops: `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### social-icon

Social icon.

Page: home. Selector: `footer social link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 40 x 48.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Nista 16px/27.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #000000, fill #ffffff | = | = | = |
| Painted layers | span.icon.icon--light 40.0x40.0 bg #a7b0b7 r 100% | span.icon.icon--light 40.0x40.0 bg #c3c9ce r 100% | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `social-icon-default.png`, `social-icon-hover.png`, `social-icon-focus-visible.png`, `social-icon-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header.

Page: mobile. Selector: `header at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 725.64 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h1.header-simplified__title: Nista 30px/36px 800, #ffffff |
| Transition | none |
| ::before | 390px x 725.641px, absolute, bg #000000 @ 0 url(…), linear-gradient(20.78deg, #6e00f8 3.3%, #563ce9 27.67%, #116eee 93.23%), radius 0px |
| Painted layers | a.header-simplified__cta.btn 193.4x43.2 bg #11ee92 border T:2px solid #11ee92 / R:2px solid #11ee92 / B:2px solid #11ee92 / L:2px solid #11ee92 r 45.04px shadow #000000 @ 0.3 0px 2px 4px 0px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-button

Menu button. The kebab toggle: an empty anchor wrapping span.responsive-nav__icon.

Page: mobile. Selector: `span.responsive-nav__icon`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 23 x 23 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #0000ee |
| Transition | none |
| Transform | matrix(0, 1, -1, 0, 0, 0) |
| Cursor | pointer |
| Icon | 23 x 23, colour #0000ee, fill #ffffff |
| ::before | 100% x 3px, absolute, bg #116eee, radius 0px |
| ::after | 65% x 3px, absolute, bg #116eee, radius 0px |
| Painted layers | span::before.responsive-nav__icon.icon 100%x3px bg #116eee; span::after.responsive-nav__icon.icon 65%x3px bg #116eee |
| How | at rest |

Crops: `m-menu-button-default.png`.

#### m-menu-open

Mobile menu, open. The kebab dropdown, opened by its own toggle.

Page: mobile. Selector: `opened responsive nav list`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 250 x 165.56 |
| Padding | 0px |
| Border | none |
| Radius | 16px |
| Background | #ffffff |
| Box shadow | #000000 @ 0.15 1px 0px 10px 1px |
| Outline | none |
| Font | Nista 16px/27.2px 400 |
| Letter spacing | normal |
| Colour | #000000 |
| Text node | span.main-nav-dropdown__link-text: Nista 14px/23.8px 700, #252b2f |
| Transition | none |
| Painted layers | ul.main-nav-dropdown__list 250.0x165.6 bg #ffffff r 16px shadow #000000 @ 0.15 1px 0px 10px 1px |
| How | at rest |

Crops: `m-menu-open-default.png`.

#### m-nav-item

Mobile nav item. A link inside the opened responsive nav dropdown.

Page: mobile. Selector: `.main-nav-dropdown__link`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 250 x 55.19 | = | = | = |
| Padding | 14px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | #f2f7fd | #f2f7fd | #f2f7fd |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Nista 16px/27.2px 700 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #0000ee | = | = | #ff0000 |
| Text node | span.main-nav-dropdown__link-text: Nista 14px/23.8px 700, #252b2f | = | = | = |
| Transition | none | = | = | = |
| Cursor | pointer | = | = | = |
| Ancestor paint | 2 up ul.main-nav-dropdown__list bg #ffffff shadow #000000 @ 0.15 1px 0px 10px 1px | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | a.main-nav-dropdown__link 250.0x55.2 bg #f2f7fd | a.main-nav-dropdown__link 250.0x55.2 bg #f2f7fd | a.main-nav-dropdown__link 250.0x55.2 bg #f2f7fd |

Crops: `m-nav-item-default.png`, `m-nav-item-hover.png`, `m-nav-item-focus-visible.png`, `m-nav-item-pressed.png`.

#### m-hero

Mobile headline.

Page: mobile. Selector: `h1 at 390`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 348 x 108 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Nista 30px/36px 800 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `m-hero-default.png`.

## Transitions declared in the readable stylesheets

This list holds only what the CSSOM could read on each page: inline styles and same-origin sheets, since a cross-origin sheet stays unreadable there. The per-state Transition rows in the tables above are computed values and cover every rule the page paints.

- home: `height 0.2s linear`, `width 0.3s linear`, `background-color 0.218s, border-color 0.218s`, `background-color 0.218s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`

- premium: `0.2s ease-in-out`, `0.3s ease-in-out`, `color 0.3s ease-in-out`, `border 0.2s`, `0.1s`, `300ms ease-in`, `0.2s ease-in`, `0.4s`, `150ms ease-in`, `0.2s`, `0.25s ease-out`, `0.1s ease-in`
