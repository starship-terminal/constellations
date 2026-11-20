# Designmodo component measurements

Computed styles read from designmodo.com on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the marketing pages and the Postcards app shell behind the Welcome-back modal, and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Header and navigation

#### mkt-header

Site header. The top bar: Designmodo wordmark, Apps/Articles menus, Log In and Sign Up.

Page: home. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 70 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | a.menu-link.dropdownTrigger: InterVariable 15px/70px 500, #ffffff |
| Transition | box-shadow, transform, opacity, background 0.35s, 0.35s, 0.35s, 0.35s ease, cubic-bezier(0.5, 0, 0.35, 1), cubic-bezier(0.5, 0, 0.35, 1), ease delay 0s, 0s, 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 30 x 30, colour #ffffff |
| Painted layers | a.button.round 94.0x38.5 bg #f49a40 r 999px; span::before.menu-icon.sidebarTrigger 24pxx2px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff; span::after.menu-icon.sidebarTrigger 24pxx2px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff |
| How | at rest |

Crops: `mkt-header-default.png`.

#### nav-apps

Apps menu. The "Apps" product menu in the header; measured, never opened beyond hover.

Page: home. Selector: `Apps`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 84 x 70 | = | = | = |
| Padding | 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | InterVariable 15px/70px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #2f80ed | = | #2f80ed |
| Transition | all 0.35s ease | all 0.15s ease | all 0.15s ease | all 0.15s ease |
| Cursor | pointer | = | = | = |
| Icon | 11 x 10, colour #ffffff | 11 x 10, colour #2f80ed, fill #186bff | = | 11 x 10, colour #2f80ed, fill #186bff |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.menu-link.dropdownTrigger 84.0x70.0 outline 2px solid #ffffff offset 2px | = |

Crops: `nav-apps-default.png`, `nav-apps-hover.png`, `nav-apps-focus-visible.png`, `nav-apps-pressed.png`.

#### nav-login

Log In. The header Log-In action; measured, never followed.

Page: home. Selector: `Log In`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69 x 70 | = | = | = |
| Padding | 0px 10px 0px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | InterVariable 15px/70px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | #2f80ed | = | #2f80ed |
| Transition | all 0.35s ease | all 0.15s ease | all 0.15s ease | all 0.15s ease |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.menu-link.middle 69.0x70.0 outline 2px solid #ffffff offset 2px | = |

Crops: `nav-login-default.png`, `nav-login-hover.png`, `nav-login-focus-visible.png`, `nav-login-pressed.png`.

#### nav-signup

Sign Up. The header Sign-Up action; measured, never followed.

Page: home. Selector: `Sign Up`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94 x 38.5 | = | = | = |
| Padding | 8px 18px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #f49a40 | #f18110 | #f18110 | #f18110 |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | InterVariable 15px/22.5px 600 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease | all 0.15s ease | all 0.15s ease | all 0.35s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, 2) |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.round 94.0x38.5 bg #f49a40 r 999px | a.button.round 94.0x38.5 bg #f18110 r 999px | a.button.round 94.0x38.5 bg #f18110 r 999px outline 2px solid #ffffff offset 2px | a.button.round 94.0x38.5 bg #f18110 r 999px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

### Home marketing

#### hero-h1

Hero headline. "Level up email & web designs faster" — the 56px display heading over the dark hero.

Page: home. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 498.33 x 123.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 56px/61.6px 600 |
| Letter spacing | -1.568px |
| Colour | #ffffff |
| Text node | span: InterVariable 56px/61.6px 600, #defaca, ls -1.568px |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### openapp-cta

Open App CTA. The green "Open App →" product CTA (164x53, #27ae60); measured, never followed.

Page: home. Selector: `Open App`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 164 x 53 | = | = | = |
| Padding | 13px 28px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #27ae60 | #1e8449 | #1e8449 | #1e8449 |
| Box shadow | #27ae60 @ 0.15 0px 4px 9px 0px | #27ae60 @ 0.2 0px 6px 12px 0px | = | #27ae60 @ 0.2 0px 6px 12px 0px |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | InterVariable 18px/27px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease | all 0.15s ease | all 0.15s ease | all 0.35s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, 2) |
| Cursor | pointer | = | = | = |
| Painted layers | a.p.button 164.0x53.0 bg #27ae60 r 999px shadow #27ae60 @ 0.15 0px 4px 9px 0px | a.p.button 164.0x53.0 bg #1e8449 r 999px shadow #27ae60 @ 0.2 0px 6px 12px 0px | a.p.button 164.0x53.0 bg #1e8449 r 999px shadow #27ae60 @ 0.15 0px 4px 9px 0px outline 2px solid #ffffff offset 2px | a.p.button 164.0x53.0 bg #1e8449 r 999px shadow #27ae60 @ 0.2 0px 6px 12px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `openapp-cta-default.png`, `openapp-cta-hover.png`, `openapp-cta-focus-visible.png`, `openapp-cta-pressed.png`.

#### seemore-link

See more link. A "See more →" link on a product strip.

Page: home. Selector: `a.see_more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 102.48 x 27 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #c3cecb offset 2px | = |
| Font | InterVariable 18px/27px 600 | = | = | = |
| Letter spacing | -0.252px | = | = | = |
| Colour | #c3cecb | #ffffff | = | #ffffff |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.p.weight-6 102.5x27.0 outline 2px solid #c3cecb offset 2px | = |

Crops: `seemore-link-default.png`, `seemore-link-hover.png`, `seemore-link-focus-visible.png`, `seemore-link-pressed.png`.

#### article-card

Article card. A "Read more →" article card in the home articles strip.

Page: home. Selector: `Read more`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 340 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | InterVariable 16px/24px 600 | = | = | = |
| Letter spacing | -0.176px | = | = | = |
| Colour | #ffffff | #27ae60 | = | #27ae60 |
| Transition | all 0.3s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.margin-top-2.read_more 340.0x24.0 outline 2px solid #ffffff offset 2px | = |

Crops: `article-card-default.png`, `article-card-hover.png`, `article-card-focus-visible.png`, `article-card-pressed.png`.

#### pc-h1

Product headline. The Postcards product page heading.

Page: postcards. Selector: `postcards h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 880 x 204.97 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 91.5px/102.48px 900 |
| Letter spacing | -4.575px |
| Colour | #101d24 |
| Transition | none |
| Cursor | default |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | span.word-animation.nobr 387.8x111.0 bg #101d24 image url(data:…); span.type-caret 7.3x75.2 bg #fb754b r 1px shadow #fb754b @ 0.35 0px 0px 6px 0px |
| How | at rest |

Crops: `pc-h1-default.png`.

#### pc-cta

Product CTA. The product page primary CTA; measured, never followed.

Page: postcards. Selector: `product CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 227.69 x 62 | = | = | = |
| Padding | 16px 26px | = | = | = |
| Border | none | = | = | = |
| Radius | 12px | = | = | = |
| Background | #0d1d24 | #fb754b | = | #fb754b |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101d24 offset 2px | = |
| Font | InterVariable 20px/30px 750 | = | = | = |
| Letter spacing | -0.28px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease | all 0.35s ease | = | all 0.35s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, 2) |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.big 227.7x62.0 bg #0d1d24 r 12px | a.button.big 227.7x62.0 bg #fb754b r 12px | a.button.big 227.7x62.0 bg #0d1d24 r 12px outline 2px solid #101d24 offset 2px | a.button.big 227.7x62.0 bg #fb754b r 12px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pc-cta-default.png`, `pc-cta-hover.png`, `pc-cta-focus-visible.png`, `pc-cta-pressed.png`.

### Footer

#### site-footer

Site footer. The sitemap footer (products, resources, legal links).

Page: home. Selector: `footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 844.8 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #313942 |
| Text node | div.questions: InterVariable 14px/23.8px 400, #313942, ls -0.2px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 36 x 36, colour #313942 |
| Painted layers | section.slide.whiteSlide 1440.0x844.8 bg #ffffff; div.questions 123.2x32.8 bg #f1f8fe border B:1px solid #e5eef5 r 16px 16px 16px 0px shadow #000000 @ 0.03 0px 5px 13px 0px; div.badge-body 68.1x20.4 bg #27ae60 r 6px |
| How | at rest |

Crops: `site-footer-default.png`.

### Welcome-back auth modal

#### welcome-modal

Welcome modal. The "Welcome back!" auth modal over the app shell (418x615, white card on a dimmed gallery).

Page: app. Selector: `.dialog-container`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 423 x 621.2 |
| Padding | 0px |
| Border | none |
| Radius | 10px |
| Background | #ffffff |
| Box shadow | #a9b3bb @ 0.5 0px 0px 2px 0px, #a9b3bb @ 0.25 0px 10px 12px 0px |
| Outline | none |
| Font | Fira Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d3a41 |
| Text node | div.sc-rPWID.hLPhED: Fira Sans 36px/43.2px 800, #071c26 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 16 x 16, colour #2d3a41 |
| Painted layers | div.sc-BQMaI.ceAPWO 423.0x621.2 bg #ffffff r 10px shadow #a9b3bb @ 0.5 0px 0px 2px 0px, #a9b3bb @ 0.25 0px 10px 12px 0px; button.sc-fscmHZ.fKpett 343.0x48.0 bg #ffffff border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px; a.sc-kpKSZj.bZXRug 343.0x48.0 bg #071c26 border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px; div.sc-dBFDNq.bbwQzS 150.3x1.0 bg #e8ecf0; div.sc-dBFDNq.bbwQzS 150.3x1.0 bg #e8ecf0; input.sc-cXPBUD.fXxuWq 343.0x50.0 bg #ffffff border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px outline 2px solid #000000 @ 0 offset 0px |
| Ancestor paint | 1 up div.sc-leSDtu.tqRJk bg #071c26 @ 0.8 |
| How | at rest |

Crops: `welcome-modal-default.png`.

#### modal-google

Google button. "Continue with Google" in the welcome modal; measured, never pressed.

Page: app. Selector: `Continue with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 343 x 48 | = | = | = |
| Padding | 12px 35px 12px 14px | = | = | = |
| Border | 1px solid #e8ecf0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #ffffff | #e8ecf0 @ 0.5 | #e8ecf0 @ 0.5 | #e8ecf0 @ 0.5 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Fira Sans 15px/22.05px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d3a41 | = | = | = |
| Text node | span.sc-bWJUgm.cMEATG: Fira Sans 15px/22.05px 500, #2d3a41 | = | = | = |
| Transition | all 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #2d3a41 | = | = | = |
| Painted layers | button.sc-fscmHZ.fKpett 343.0x48.0 bg #ffffff border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px | button.sc-fscmHZ.fKpett 343.0x48.0 bg #e8ecf0 @ 0.5 border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px | button.sc-fscmHZ.fKpett 343.0x48.0 bg #e8ecf0 @ 0.5 border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px | button.sc-fscmHZ.fKpett 343.0x48.0 bg #e8ecf0 @ 0.5 border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `modal-google-default.png`, `modal-google-hover.png`, `modal-google-focus-visible.png`, `modal-google-pressed.png`.

#### modal-sso

SSO button. The dark "Sign-in with SSO" button; measured, never pressed.

Page: app. Selector: `Sign-in with SSO`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 343 x 48 | = | = | = |
| Padding | 12px 35px 12px 14px | = | = | = |
| Border | 1px solid #e8ecf0 | = | = | = |
| Radius | 8px | = | = | = |
| Background | #071c26 | #2a3539 | #2a3539 | #2a3539 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Fira Sans 15px/22.05px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.sc-lfYzqA.kocrlX: Fira Sans 15px/22.05px 500, #ffffff | = | = | = |
| Transition | all 0.3s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #ffffff | = | = | = |
| Painted layers | a.sc-kpKSZj.bZXRug 343.0x48.0 bg #071c26 border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px | a.sc-kpKSZj.bZXRug 343.0x48.0 bg #2a3539 border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px | a.sc-kpKSZj.bZXRug 343.0x48.0 bg #2a3539 border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px | a.sc-kpKSZj.bZXRug 343.0x48.0 bg #2a3539 border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `modal-sso-default.png`, `modal-sso-hover.png`, `modal-sso-focus-visible.png`, `modal-sso-pressed.png`.

#### modal-email

Email field. The your@email.com field in the welcome modal; focused and typed then cleared, never submitted.

Page: app. Selector: `modal email field`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 343 x 50 | = | = |
| Padding | 10px 15px 10px 45px | = | = |
| Border | 1px solid #e8ecf0 | 1px solid #000000 @ 0 | 1px solid #000000 @ 0 |
| Radius | 8px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | 2px solid #000000 @ 0 offset 0px | 2px solid #2198ed offset 0px | 2px solid #2198ed offset 0px |
| Font | Fira Sans 15px/18px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #071c26 | = | = |
| Transition | all 0.1s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #2d3a41, opacity 0.5 | = | = |
| Painted layers | input.sc-cXPBUD.fXxuWq 343.0x50.0 bg #ffffff border T:1px solid #e8ecf0 / R:1px solid #e8ecf0 / B:1px solid #e8ecf0 / L:1px solid #e8ecf0 r 8px outline 2px solid #000000 @ 0 offset 0px | input.sc-cXPBUD.fXxuWq 343.0x50.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #2198ed offset 0px | input.sc-cXPBUD.fXxuWq 343.0x50.0 bg #ffffff border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 8px outline 2px solid #2198ed offset 0px |
| How | at rest | clicked into the field | typed "probe@example.com", then deleted; nothing sent |

Crops: `modal-email-default.png`, `modal-email-focused.png`, `modal-email-filled.png`.

#### modal-login

Modal Login. The green modal Login button; measured, never pressed.

Page: app. Selector: `modal Login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 166.5 x 52 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #27ae60 | #239b58 | #239b58 | #239b58 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Fira Sans 15px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-dUYLmH.eeCOfT 166.5x52.0 bg #27ae60 r 8px | button.sc-dUYLmH.eeCOfT 166.5x52.0 bg #239b58 r 8px | button.sc-dUYLmH.eeCOfT 166.5x52.0 bg #239b58 r 8px | button.sc-dUYLmH.eeCOfT 166.5x52.0 bg #239b58 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `modal-login-default.png`, `modal-login-hover.png`, `modal-login-focus-visible.png`, `modal-login-pressed.png`.

#### modal-create

Create Account. The secondary "Create Account" button; measured, never pressed.

Page: app. Selector: `Create Account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 166.5 x 52 | = | = | = |
| Padding | 1px 6px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | #e8ecf0 | #d9dfe6 | #d9dfe6 | #d9dfe6 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Fira Sans 15px/normal 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #2d3a41 | = | = | = |
| Transition | all 0.2s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-iowXnY.etxPfy 166.5x52.0 bg #e8ecf0 r 8px | button.sc-iowXnY.etxPfy 166.5x52.0 bg #d9dfe6 r 8px | button.sc-iowXnY.etxPfy 166.5x52.0 bg #d9dfe6 r 8px | button.sc-iowXnY.etxPfy 166.5x52.0 bg #d9dfe6 r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `modal-create-default.png`, `modal-create-hover.png`, `modal-create-focus-visible.png`, `modal-create-pressed.png`.

### Postcards app (signed out)

#### app-header

App header. The dark navy app header: postcards mark, Login/Signup, the "+ Create" split button.

Page: app. Selector: `app header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px |
| Gap | 0px |
| Border | none |
| Radius | 0px |
| Background | #071c26 |
| Box shadow | none |
| Outline | none |
| Font | Fira Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d3a41 |
| Text node | span.sc-eaoxfQ.svGVp: Fira Sans 15px/22.05px 500, #ffffff |
| Transition | none |
| Icon | 17 x 18, colour #0000ee |
| Painted layers | header.sc-dQEtJz.sc-jpchaS 1440.0x60.0 bg #071c26; button.sc-kYKKLo.beQZtf 94.0x40.0 bg #2198ed r 6px; button.sc-kYKKLo.guYrH 78.0x40.0 bg #485f6b r 6px |
| How | at rest |

Crops: `app-header-default.png`.

#### app-login

App Login. The blue Login pill in the app header; measured, never pressed.

Page: app. Selector: `app Login`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 94 x 40.05 | = | = | = |
| Padding | 9px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #2198ed | #344a56 | = | #344a56 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Fira Sans 15px/22.05px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.sc-eaoxfQ.svGVp: Fira Sans 15px/22.05px 500, #ffffff | = | = | = |
| Transition | all 0.15s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ffffff | = | = | = |
| Painted layers | button.sc-kYKKLo.beQZtf 94.0x40.0 bg #2198ed r 6px | button.sc-kYKKLo.beQZtf 94.0x40.0 bg #344a56 r 6px | = | button.sc-kYKKLo.beQZtf 94.0x40.0 bg #344a56 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-login-default.png`, `app-login-hover.png`, `app-login-focus-visible.png`, `app-login-pressed.png`.

#### app-signup

App Signup. The dark Signup pill in the app header; measured, never pressed.

Page: app. Selector: `app Signup`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 78 x 40.05 | = | = | = |
| Padding | 9px 15px | = | = | = |
| Border | none | = | = | = |
| Radius | 6px | = | = | = |
| Background | #485f6b | #344a56 | = | #344a56 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Fira Sans 15px/22.05px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.sc-eaoxfQ.svGVp: Fira Sans 15px/22.05px 500, #ffffff | = | = | = |
| Transition | all 0.15s ease-in-out | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.sc-kYKKLo.guYrH 78.0x40.0 bg #485f6b r 6px | button.sc-kYKKLo.guYrH 78.0x40.0 bg #344a56 r 6px | = | button.sc-kYKKLo.guYrH 78.0x40.0 bg #344a56 r 6px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-signup-default.png`, `app-signup-hover.png`, `app-signup-focus-visible.png`, `app-signup-pressed.png`.

#### create-split

Create split button. The green "+ Create" split button top-right of the gallery; measured, never pressed.

Page: app. Selector: `+ Create`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 122 x 40 | = | - | = |
| Padding | 0px 13px | = | - | = |
| Gap | 13px | = | - | = |
| Border | none | = | - | = |
| Radius | 6px | = | - | = |
| Background | #27ae60 | #239b58 | - | #239b58 |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Fira Sans 14px/normal 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ffffff | = | - | = |
| Transition | all 0.15s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 16 x 16, colour #ffffff | = | - | = |
| Painted layers | div.sc-hUVTwQ.bzWBtu 122.0x40.0 bg #27ae60 r 6px | div.sc-hUVTwQ.bzWBtu 122.0x40.0 bg #239b58 r 6px | - | div.sc-hUVTwQ.bzWBtu 122.0x40.0 bg #239b58 r 6px |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `create-split-default.png`, `create-split-hover.png`, `create-split-pressed.png`.

#### sidebar

App sidebar. The 240px workspace sidebar: Drafts, Templates (+233 NEW), Workspace Settings, Chat with Us.

Page: app. Selector: `aside`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 241 x 840 |
| Padding | 0px |
| Border | T: none; R: 1px solid #e8ecf0; B: none; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fira Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d3a41 |
| Text node | div.sc-eDknUU.gzbzF: Fira Sans 13px/19.5px 500, #2d3a41 |
| Transition | none |
| Icon | 20 x 20, colour #aab2bb |
| Painted layers | div.sc-iUVXli.gXFlZm 241.0x840.0 border R:1px solid #e8ecf0; div.sc-eDknUU.gzbzF 240.0x60.0 border B:1px solid #e8ecf0; div.sc-tDzRk.dTSGyz 220.0x40.0 r 10px outline 2px solid #2198ed @ 0 offset 0px; div.sc-EtVYz.QEotB 240.0x1.0 border T:1px solid #e8ecf0; div.sc-tDzRk.dsBttE 220.0x40.0 bg #d9efff r 10px outline 2px solid #2198ed @ 0 offset 0px; span.sc-jmLfgi.hfvJKt 54.0x14.0 bg #27ae60 r 3px shadow #000000 @ 0.06 0px -1px 0px 0px inset |
| Ancestor paint | 1 up div.sc-dhHMav.hhTwuQ bg #ffffff |
| How | at rest |

Crops: none.

#### side-templates

Templates nav. The "Templates" sidebar item with the +233 NEW badge.

Page: app. Selector: `Templates nav`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 69 x 21 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Fira Sans 14px/21px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #2198ed | = | - | = |
| Transition | none | = | - | = |
| Ancestor paint | 1 up div.sc-tDzRk.dsBttE bg #d9efff outline 2px solid #2198ed @ 0 | 1 up div.sc-tDzRk.dsBttE bg #d9efff | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `side-templates-default.png`, `side-templates-hover.png`, `side-templates-pressed.png`.

#### new-badge

NEW badge. The green "+233 NEW" counter badge on the Templates item.

Page: app. Selector: `NEW badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 54 x 14 |
| Padding | 0px 4px |
| Border | none |
| Radius | 3px |
| Background | #27ae60 |
| Box shadow | #000000 @ 0.06 0px -1px 0px 0px inset |
| Outline | none |
| Font | Fira Sans 9px/13.5px 600 |
| Letter spacing | 0.5px |
| Colour | #ffffff |
| Text node | span: Fira Sans 9px/9px 600, #ffffff, ls 0.5px |
| Transition | none |
| Painted layers | span.sc-jmLfgi.hfvJKt 54.0x14.0 bg #27ae60 r 3px shadow #000000 @ 0.06 0px -1px 0px 0px inset |
| Ancestor paint | 1 up div.sc-tDzRk.dsBttE bg #d9efff outline 2px solid #2198ed @ 0 |
| How | at rest |

Crops: `new-badge-default.png`.

#### filter-industry

Industry filter. The "Industry" gallery filter dropdown; measured, never opened.

Page: app. Selector: `Industry filter`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61.97 x 15 | = | - | = |
| Padding | 0px | = | - | = |
| Gap | 7px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Fira Sans 13px/normal 400 | = | - | = |
| Letter spacing | -0.13px | = | - | = |
| Colour | #585d63 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 8 x 5, colour #585d63 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `filter-industry-default.png`, `filter-industry-hover.png`, `filter-industry-pressed.png`.

#### create-blank

Create Blank card. The dashed "Create Blank Template" gallery card (266x532); measured, never pressed.

Page: app. Selector: `Create Blank Template`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 266 x 592 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Fira Sans 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #2d3a41 | = | - | = |
| Text node | div.sc-fRUzah.dIrkte: Fira Sans 13px/19.5px 500, #788994 | = | - | = |
| Transition | all 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 24 x 24, colour #788994 | = | - | = |
| Painted layers | div.sc-hBxvHn.emdIll 266.0x532.0 bg #f4f6f7 border T:1px solid #1b1b1b @ 0.1 / R:1px solid #1b1b1b @ 0.1 / B:1px solid #1b1b1b @ 0.1 / L:1px solid #1b1b1b @ 0.1 r 10px outline 2px solid #000000 @ 0 offset 0px | div.sc-hBxvHn.emdIll 266.0x532.0 bg #f4f6f7 border T:1px solid #1b1b1b @ 0.1 / R:1px solid #1b1b1b @ 0.1 / B:1px solid #1b1b1b @ 0.1 / L:1px solid #1b1b1b @ 0.1 r 10px outline 2px solid #2198ed offset 0px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `create-blank-hover.png`, `create-blank-pressed.png`.

#### genai-card

Generate AI card. The lavender "Generate with AI" gallery card; measured, never pressed.

Page: app. Selector: `Generate with AI`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 266 x 592 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | Fira Sans 16px/24px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #2d3a41 | = | - | = |
| Text node | div.sc-jiPWxV.koeunR: Fira Sans 13px/19.5px 500, #405eff | = | - | = |
| Transition | all 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Icon | 20 x 20, colour #405eff | = | - | = |
| Painted layers | div.sc-kjGiqv.kEmqZX 266.0x532.0 image linear-gradient(135deg, #f0f4ff 0%, #e6ebff 100%) border T:1px solid #1b1b1b @ 0.1 / R:1px solid #1b1b1b @ 0.1 / B:1px solid #1b1b1b @ 0.1 / L:1px solid #1b1b1b @ 0.1 r 10px outline 2px solid #000000 @ 0 offset 0px | div.sc-kjGiqv.kEmqZX 266.0x532.0 image linear-gradient(135deg, #f0f4ff 0%, #e6ebff 100%) border T:1px solid #1b1b1b @ 0.1 / R:1px solid #1b1b1b @ 0.1 / B:1px solid #1b1b1b @ 0.1 / L:1px solid #1b1b1b @ 0.1 r 10px outline 2px solid #405eff offset 0px | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `genai-card-default.png`, `genai-card-hover.png`, `genai-card-pressed.png`.

#### tpl-card

Template card. A named template card (Kindred, Nortflow...) with the FREE badge and category tags.

Page: app. Selector: `template card`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 266 x 592 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Fira Sans 16px/24px 400 |
| Letter spacing | normal |
| Colour | #2d3a41 |
| Text node | span.sc-fMjwjh.sc-kbXUY: Fira Sans 9px/9px 600, #ffffff, ls 0.5px |
| Transition | none |
| Cursor | pointer |
| Icon | 10 x 10, colour #ffffff |
| Painted layers | div.sc-dvTebe.hIbSre 266.0x532.0 bg #215c43 r 10px shadow #000000 @ 0 0px 0px 0px 2px outline 1px solid #1b1b1b @ 0.1 offset 0px; span.sc-fMjwjh.sc-kbXUY 43.0x16.0 bg #2198ed r 4px shadow #000000 @ 0.06 0px -1px 0px 0px inset; span.sc-bkSjNy.bqBVzQ 28.5x14.0 bg #27ae60 r 3px shadow #000000 @ 0.06 0px -1px 0px 0px inset |
| How | at rest |

Crops: `tpl-card-default.png`.

#### free-badge

FREE badge. The blue FREE corner badge on template cards.

Page: app. Selector: `FREE badge`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 43 x 16 |
| Padding | 2.5px 4px 3.5px 4px |
| Gap | 3px |
| Border | none |
| Radius | 4px |
| Background | #2198ed |
| Box shadow | #000000 @ 0.06 0px -1px 0px 0px inset |
| Outline | none |
| Font | Fira Sans 9px/9px 600 |
| Letter spacing | 0.5px |
| Colour | #ffffff |
| Transition | none |
| Cursor | pointer |
| Icon | 10 x 10, colour #ffffff |
| Painted layers | span.sc-fMjwjh.sc-kbXUY 43.0x16.0 bg #2198ed r 4px shadow #000000 @ 0.06 0px -1px 0px 0px inset |
| Ancestor paint | 1 up div.sc-dvTebe.hIbSre bg #215c43 shadow #000000 @ 0 0px 0px 0px 2px outline 1px solid #1b1b1b @ 0.1 |
| How | at rest |

Crops: `free-badge-default.png`.

### Pricing

#### pricing-h1

Pricing headline. The 91.5px "Pricing" display heading.

Page: pricing. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1180 x 102.48 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 91.5px/102.48px 900 |
| Letter spacing | -4.575px |
| Colour | #101d24 |
| Text node | span.text-black: InterVariable 91.5px/102.48px 900, #101d24, ls -4.575px |
| Transition | none |
| Cursor | default |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| How | at rest |

Crops: `pricing-h1-default.png`.

#### billing-toggle

Billing toggle. The Yearly/Monthly billing switch; measured, never toggled.

Page: pricing. Selector: `Yearly Monthly`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 193 x 30 | = | - | = |
| Padding | 0px | = | - | = |
| Border | none | = | - | = |
| Radius | 0px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | InterVariable 16px/30px 500 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #101d24 | = | - | = |
| Transition | none | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | span::before.qmark.description 260pxx93px bg #111111 r 8px; span::after.qmark.description 26pxx7px image url(data:…)'%3E%3Cpath d='M0 0L-8.74228e-08 1C2.97731 1 5.81883 2.27754 7.8 4.5C10.4659 7.; span.element 30.0x16.0 bg #101d24 r 10px; span::after.element 10pxx10px bg #ffffff r 50% | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `billing-toggle-default.png`, `billing-toggle-hover.png`, `billing-toggle-pressed.png`.

#### plan-card

Plan card. A pricing plan card (Start FREE FOREVER / Plus / Pro) — white-box 313px wide.

Page: pricing. Selector: `.PriceBlock`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 313.33 x 299.89 |
| Padding | 40px 40px 30px 40px |
| Border | none |
| Radius | 16px |
| Background | #f7f9fc @ 0.9 |
| Box shadow | #3a4c66 @ 0.07 0px 4px 57px 0px, #bfc5ca @ 0.65 0px -1.5px 4.5px 0px inset |
| Outline | none |
| Font | InterVariable 18px/27px 400 |
| Letter spacing | normal |
| Colour | #101d24 |
| Text node | h2.font-size-22.padding-bottom-3: InterVariable 22px/26.4px 700, #101d24, ls -0.396px |
| Transition | none |
| Cursor | default |
| Painted layers | div.margin-bottom-2.equalElement 313.3x299.9 bg #f7f9fc @ 0.9 r 16px shadow #3a4c66 @ 0.07 0px 4px 57px 0px, #bfc5ca @ 0.65 0px -1.5px 4.5px 0px inset; div.float-right.round 94.0x18.0 bg #2ac45e r 999px; a.button.wideForPhone 233.3x52.0 bg #101d24 r 10px |
| How | at rest |

Crops: `plan-card-default.png`.

#### plan-cta

Plan CTA. A plan action (Get Started / $19/month) — it adds to the cart; measured, never pressed.

Page: pricing. Selector: `plan CTA`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 233.33 x 52 | = | = | = |
| Padding | 14px 22px | = | = | = |
| Border | none | = | = | = |
| Radius | 10px | = | = | = |
| Background | #101d24 | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 2px solid #101d24 offset 2px | = |
| Font | InterVariable 16px/24px 800 | = | = | = |
| Letter spacing | -0.176px | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease | all 0.35s ease | = | all 0.35s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, 2) |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.wideForPhone 233.3x52.0 bg #101d24 r 10px | = | a.button.wideForPhone 233.3x52.0 bg #101d24 r 10px outline 2px solid #101d24 offset 2px | = |
| Ancestor paint | 1 up div.margin-bottom-2.equalElement bg #f7f9fc @ 0.9 shadow #3a4c66 @ 0.07 0px 4px 57px 0px, #bfc5ca @ 0.65 0px -1.5px 4.5px 0px inset | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `plan-cta-default.png`, `plan-cta-hover.png`, `plan-cta-focus-visible.png`, `plan-cta-pressed.png`.

#### plan-feature

Plan feature. A plan feature row ("10 template projects") with the ? hint icon.

Page: pricing. Selector: `planFeatures row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 293.33 x 308 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 18px/27px 400 |
| Letter spacing | -0.252px |
| Colour | #101d24 |
| Text node | li.feature.lowercase: InterVariable 16px/28px 700, #101d24, ls -0.192px |
| Transition | none |
| Cursor | default |
| Painted layers | span.qmark.description 14.0x14.0 bg #747491 r 25px; span::before.qmark.description 260pxx72px bg #111111 r 8px; span::after.qmark.description 26pxx7px image url(data:…)'%3E%3Cpath d='M0 0L-8.74228e-08 1C2.97731 1 5.81883 2.27754 7.8 4.5C10.4659 7.; span.qmark.description 14.0x14.0 bg #747491 r 25px; span::before.qmark.description 260pxx72px bg #111111 r 8px; span::after.qmark.description 26pxx7px image url(data:…)'%3E%3Cpath d='M0 0L-8.74228e-08 1C2.97731 1 5.81883 2.27754 7.8 4.5C10.4659 7. |
| How | at rest |

Crops: `plan-feature-default.png`.

### Email-template gallery

#### tpl-h1

Gallery headline. The email-templates gallery heading.

Page: templates. Selector: `h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 780 x 151.19 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 63px/75.6px 900 |
| Letter spacing | -1.386px |
| Colour | #101d24 |
| Transition | none |
| Cursor | default |
| How | at rest |

Crops: `tpl-h1-default.png`.

#### tpl-filter

Gallery filter. The Industry / Usage / Season / Brand / Free-only filter bar over the email-template grid (714x43); measured, never activated.

Page: templates. Selector: `li.fill`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 714 x 43.19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | InterVariable 18px/43.2px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.inlineBlock.dropdownTrigger: InterVariable 16px/38.4px 400, #ffffff, ls -0.176px | = | = | = |
| Transition | none | = | = | = |
| Cursor | default | = | = | = |
| Icon | 11 x 11, colour #ffffff | = | = | = |
| Painted layers | span.white.text-deepPurple 0.0x20.0 bg #ffffff; span.white.text-deepPurple 0.0x20.0 bg #ffffff; span.white.text-deepPurple 0.0x20.0 bg #ffffff; span.white.text-deepPurple 0.0x20.0 bg #ffffff; span.free-filter-box 14.0x14.0 border T:1px solid #ffffff @ 0.55 / R:1px solid #ffffff @ 0.55 / B:1px solid #ffffff @ 0.55 / L:1px solid #ffffff @ 0.55 r 3px; span::after.free-filter-box 4pxx8px border R:1px solid #ffffff / B:1px solid #ffffff | = | span.white.text-deepPurple 0.0x20.0 bg #ffffff; span.white.text-deepPurple 0.0x20.0 bg #ffffff; span.white.text-deepPurple 0.0x20.0 bg #ffffff; span.white.text-deepPurple 0.0x20.0 bg #ffffff; input.free-filter-checkbox 1.0x1.0 outline 1px auto #101010 offset 2px; span.free-filter-box 14.0x14.0 border T:1px solid #ffffff @ 0.55 / R:1px solid #ffffff @ 0.55 / B:1px solid #ffffff @ 0.55 / L:1px solid #ffffff @ 0.55 r 3px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `tpl-filter-default.png`, `tpl-filter-hover.png`, `tpl-filter-focus-visible.png`, `tpl-filter-pressed.png`.

#### tpl-card-m

Template tile. An email-template tile in the marketing gallery grid (210x420, thumbnail + name + tags); measured, never followed.

Page: templates. Selector: `.template-box`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 210 x 420 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 8px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | #0a2141 @ 0.05 0px 10px 20px 0px, #000000 @ 0.13 0px 0px 2px 0px | #0a2141 @ 0.05 0px 18.296px 36.592px 0px, #000000 @ 0.13 0px 0px 2px 0px | = | #0a2141 @ 0.05 0px 16.2721px 32.5442px 0px, #000000 @ 0.13 0px 0px 2px 0px |
| Outline | none | = | = | = |
| Font | InterVariable 18px/27px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #101d24 | #26ab55 | = | #1f7d45 |
| Text node | span.template-license-label.is-free: InterVariable 9px/9px 600, #ffffff, ls 0.5px | = | = | = |
| Transition | transform, box-shadow, color 0.28s, 0.28s, 0.15s cubic-bezier(0.22, 1, 0.36, 1), cubic-bezier(0.22, 1, 0.36, 1), ease delay 0s, 0s, 0s | = | = | = |
| Cursor | default | = | = | = |
| Icon | 10 x 10, colour #ffffff | = | = | = |
| Painted layers | div.template-box.margin-bottom-2 210.0x420.0 r 8px shadow #0a2141 @ 0.05 0px 10px 20px 0px, #000000 @ 0.13 0px 0px 2px 0px; span.template-license-label.is-free 46.0x16.0 bg #2198ed r 4px shadow #000000 @ 0.06 0px -1px 0px 0px inset; div.template-hover-overlay 210.0x420.0 bg #ffffff @ 0.96; a.button.crop 178.0x42.5 bg #101d24 r 8px; a.button.crop 178.0x42.5 bg #fb754b r 8px | div.template-box.margin-bottom-2 210.0x420.0 r 8px shadow #0a2141 @ 0.05 0px 18.296px 36.592px 0px, #000000 @ 0.13 0px 0px 2px 0px; span.template-license-label.is-free 46.0x16.0 bg #2198ed r 4px shadow #000000 @ 0.06 0px -1px 0px 0px inset; div.template-hover-overlay 210.0x420.0 bg #ffffff @ 0.96; a.button.crop 178.0x42.5 bg #101d24 r 8px; a.button.crop 178.0x42.5 bg #fb754b r 8px | div.template-box.margin-bottom-2 210.0x420.0 r 8px shadow #0a2141 @ 0.05 0px 10px 20px 0px, #000000 @ 0.13 0px 0px 2px 0px; span.template-license-label.is-free 46.0x16.0 bg #2198ed r 4px shadow #000000 @ 0.06 0px -1px 0px 0px inset; div.template-hover-overlay 210.0x420.0 bg #ffffff @ 0.96; a 148.5x125.8 outline 1px auto #101010 offset 1px; a.button.crop 178.0x42.5 bg #101d24 r 8px; a.button.crop 178.0x42.5 bg #fb754b r 8px | div.template-box.margin-bottom-2 210.0x420.0 r 8px shadow #0a2141 @ 0.05 0px 16.2721px 32.5442px 0px, #000000 @ 0.13 0px 0px 2px 0px; span.template-license-label.is-free 46.0x16.0 bg #2198ed r 4px shadow #000000 @ 0.06 0px -1px 0px 0px inset; div.template-hover-overlay 210.0x420.0 bg #ffffff @ 0.96; a.button.crop 178.0x42.5 bg #101d24 r 8px; a.button.crop 178.0x42.5 bg #fb754b r 8px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(1, 0, 0, 1, 0, -3.31841) | = | matrix(1, 0, 0, 1, 0, -2.50884) |

Crops: `tpl-card-m-hover.png`, `tpl-card-m-focus-visible.png`, `tpl-card-m-pressed.png`.

### Sign-in form

#### login-form

Sign-in form. The my-account sign-in card (380px, Google/SSO buttons over email+password).

Page: login. Selector: `form.woocommerce-form-login`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 380 x 562.5 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #313942 |
| Text node | a.button.white: InterVariable 16px/24px 500, #313942 |
| Transition | none |
| Icon | 20 x 20, colour #313942, fill #ffffff |
| Painted layers | a.button.white 380.0x50.0 bg #ffffff r 5px shadow #e0e5eb 0px 0px 0px 1px inset; a.button.flat 380.0x50.0 bg #313942 r 5px; div::before.hr.p 170pxx1px bg #e0e5eb; div::after.hr.p 170pxx1px bg #e0e5eb; input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 bg #ffffff border T:1px solid #e0e5eb / R:1px solid #e0e5eb / B:1px solid #e0e5eb / L:1px solid #e0e5eb r 5px; input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 bg #ffffff border T:1px solid #e0e5eb / R:1px solid #e0e5eb / B:1px solid #e0e5eb / L:1px solid #e0e5eb r 5px |
| Ancestor paint | 3 up div.white-box.rounded bg #ffffff shadow #0a2141 @ 0.05 0px 20px 40px 0px, #000000 @ 0.13 0px 0px 2px 0px |
| How | at rest |

Crops: `login-form-default.png`.

#### login-h1

Sign-in heading. "Login to Designmodo" — the 24px form heading.

Page: login. Selector: `login h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 440 x 32.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 24px/32.4px 700 |
| Letter spacing | -0.48px |
| Colour | #313942 |
| Transition | none |
| Ancestor paint | 1 up div.white-box.rounded bg #ffffff shadow #0a2141 @ 0.05 0px 20px 40px 0px, #000000 @ 0.13 0px 0px 2px 0px |
| How | at rest |

Crops: `login-h1-default.png`.

#### login-google

Google login. "Login with Google" — measured, never pressed.

Page: login. Selector: `Login with Google`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 380 x 50 | = | = | = |
| Padding | 13px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 5px | = | = | = |
| Background | #ffffff | #e6e6e6 | #e6e6e6 | #e6e6e6 |
| Box shadow | #e0e5eb 0px 0px 0px 1px inset | = | = | = |
| Outline | none | = | 2px solid #313942 offset 2px | = |
| Font | InterVariable 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #313942 | = | = | = |
| Transition | all 0.3s ease | all 0.15s ease | all 0.15s ease | all 0.35s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, 2) |
| Cursor | pointer | = | = | = |
| Icon | 20 x 20, colour #313942, fill #ffffff | = | = | = |
| Painted layers | a.button.white 380.0x50.0 bg #ffffff r 5px shadow #e0e5eb 0px 0px 0px 1px inset | a.button.white 380.0x50.0 bg #e6e6e6 r 5px shadow #e0e5eb 0px 0px 0px 1px inset | a.button.white 380.0x50.0 bg #e6e6e6 r 5px shadow #e0e5eb 0px 0px 0px 1px inset outline 2px solid #313942 offset 2px | a.button.white 380.0x50.0 bg #e6e6e6 r 5px shadow #e0e5eb 0px 0px 0px 1px inset |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-google-default.png`, `login-google-hover.png`, `login-google-focus-visible.png`, `login-google-pressed.png`.

#### login-email

Email field. The 380x50 email input; focused and typed then cleared, never submitted.

Page: login. Selector: `email input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 380 x 50 | = | = |
| Padding | 14px 18px | = | = |
| Border | 1px solid #e0e5eb | 1px solid #2f80ed @ 0.8 | 1px solid #2f80ed @ 0.8 |
| Radius | 5px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #638ed8 @ 0.3 0px 0px 10px 0px | #638ed8 @ 0.3 0px 0px 10px 0px |
| Outline | none | 2px solid #242424 offset 2px | 2px solid #242424 offset 2px |
| Font | InterVariable 17px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #242424 | = | = |
| Transition | all 0.15s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #242424, opacity 0.5 | = | = |
| Painted layers | input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 bg #ffffff border T:1px solid #e0e5eb / R:1px solid #e0e5eb / B:1px solid #e0e5eb / L:1px solid #e0e5eb r 5px | input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 bg #ffffff border T:1px solid #2f80ed @ 0.8 / R:1px solid #2f80ed @ 0.8 / B:1px solid #2f80ed @ 0.8 / L:1px solid #2f80ed @ 0.8 r 5px shadow #638ed8 @ 0.3 0px 0px 10px 0px outline 2px solid #242424 offset 2px | input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 bg #ffffff border T:1px solid #2f80ed @ 0.8 / R:1px solid #2f80ed @ 0.8 / B:1px solid #2f80ed @ 0.8 / L:1px solid #2f80ed @ 0.8 r 5px shadow #638ed8 @ 0.3 0px 0px 10px 0px outline 2px solid #242424 offset 2px |
| How | at rest | clicked into the field | typed "probe@example.com", then deleted; nothing sent |

Crops: `login-email-default.png`, `login-email-focused.png`, `login-email-filled.png`.

#### login-pass

Password field. The password input; focused and typed then cleared, never submitted.

Page: login. Selector: `password input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 380 x 50 | = | = |
| Padding | 14px 18px | = | = |
| Border | 1px solid #e0e5eb | 1px solid #2f80ed @ 0.8 | 1px solid #2f80ed @ 0.8 |
| Radius | 5px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | #638ed8 @ 0.3 0px 0px 10px 0px | #638ed8 @ 0.3 0px 0px 10px 0px |
| Outline | none | 2px solid #242424 offset 2px | 2px solid #242424 offset 2px |
| Font | InterVariable 17px/normal 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #242424 | = | = |
| Transition | all 0.15s ease | = | = |
| Cursor | text | = | = |
| Placeholder | #242424, opacity 0.5 | = | = |
| Painted layers | input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 bg #ffffff border T:1px solid #e0e5eb / R:1px solid #e0e5eb / B:1px solid #e0e5eb / L:1px solid #e0e5eb r 5px | input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 bg #ffffff border T:1px solid #2f80ed @ 0.8 / R:1px solid #2f80ed @ 0.8 / B:1px solid #2f80ed @ 0.8 / L:1px solid #2f80ed @ 0.8 r 5px shadow #638ed8 @ 0.3 0px 0px 10px 0px outline 2px solid #242424 offset 2px | input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 bg #ffffff border T:1px solid #2f80ed @ 0.8 / R:1px solid #2f80ed @ 0.8 / B:1px solid #2f80ed @ 0.8 / L:1px solid #2f80ed @ 0.8 r 5px shadow #638ed8 @ 0.3 0px 0px 10px 0px outline 2px solid #242424 offset 2px |
| How | at rest | clicked into the field | typed "probe-not-real", then deleted; nothing sent |

Crops: `login-pass-default.png`, `login-pass-focused.png`, `login-pass-filled.png`.

#### login-submit

Login button. The blue Login submit (186x38.5, #2f80ed); measured, never pressed.

Page: login. Selector: `Login button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 186 x 38.5 | = | = | = |
| Padding | 8px 17px | = | = | = |
| Border | none | = | = | = |
| Radius | 5px | = | = | = |
| Background | #2f80ed | #1366d6 | #1366d6 | #1366d6 |
| Box shadow | #2f80ed @ 0.15 0px 4px 9px 0px | #2f80ed @ 0.2 0px 6px 12px 0px | = | #2f80ed @ 0.2 0px 6px 12px 0px |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | InterVariable 15px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease | = | = | all 0.35s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, 2) |
| Cursor | pointer | = | = | = |
| Painted layers | button.button.small 186.0x38.5 bg #2f80ed r 5px shadow #2f80ed @ 0.15 0px 4px 9px 0px | button.button.small 186.0x38.5 bg #1366d6 r 5px shadow #2f80ed @ 0.2 0px 6px 12px 0px | button.button.small 186.0x38.5 bg #1366d6 r 5px shadow #2f80ed @ 0.15 0px 4px 9px 0px outline 2px solid #ffffff offset 2px | button.button.small 186.0x38.5 bg #1366d6 r 5px shadow #2f80ed @ 0.2 0px 6px 12px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### login-create

Create Account. The green "Create Account" pair button; measured, never followed.

Page: login. Selector: `Create Account`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 186 x 38.5 | = | = | = |
| Padding | 8px 17px | = | = | = |
| Border | none | = | = | = |
| Radius | 5px | = | = | = |
| Background | #27ae60 | #1e8449 | #1e8449 | #1e8449 |
| Box shadow | #27ae60 @ 0.15 0px 4px 9px 0px | #27ae60 @ 0.2 0px 6px 12px 0px | = | #27ae60 @ 0.2 0px 6px 12px 0px |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | InterVariable 15px/22.5px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease | all 0.15s ease | all 0.15s ease | all 0.35s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, 2) |
| Cursor | pointer | = | = | = |
| Painted layers | a.button.small 186.0x38.5 bg #27ae60 r 5px shadow #27ae60 @ 0.15 0px 4px 9px 0px | a.button.small 186.0x38.5 bg #1e8449 r 5px shadow #27ae60 @ 0.2 0px 6px 12px 0px | a.button.small 186.0x38.5 bg #1e8449 r 5px shadow #27ae60 @ 0.15 0px 4px 9px 0px outline 2px solid #ffffff offset 2px | a.button.small 186.0x38.5 bg #1e8449 r 5px shadow #27ae60 @ 0.2 0px 6px 12px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-create-default.png`, `login-create-hover.png`, `login-create-focus-visible.png`, `login-create-pressed.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone top bar with the wordmark and menu.

Page: mobile. Selector: `mobile header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 70 |
| Padding | 0px 24px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 15px/22.5px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | box-shadow, transform, opacity, background 0.35s, 0.35s, 0.35s, 0.35s ease, cubic-bezier(0.5, 0, 0.35, 1), cubic-bezier(0.5, 0, 0.35, 1), ease delay 0s, 0s, 0s, 0s |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 0 x 0, colour #ffffff |
| Painted layers | a.button.round 0.0x0.0 bg #f49a40 r 999px; span::before.menu-icon.sidebarTrigger 24pxx2px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff; span::after.menu-icon.sidebarTrigger 24pxx2px border T:1px solid #ffffff / R:1px solid #ffffff / B:1px solid #ffffff / L:1px solid #ffffff |
| How | at rest |

Crops: `m-header-default.png`.

#### m-h1

Mobile headline. The phone hero heading.

Page: mobile. Selector: `mobile h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 343.22 x 158.39 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 44px/52.8px 600 |
| Letter spacing | -1.232px |
| Colour | #ffffff |
| Text node | span: InterVariable 44px/52.8px 600, #defaca, ls -1.232px |
| Transition | none |
| How | at rest |

Crops: `m-h1-default.png`.

#### m-cta

Mobile CTA. The green Open App CTA on the phone; measured, never followed.

Page: mobile. Selector: `mobile Open App`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 134 x 50 | = | = | = |
| Padding | 13px 28px | = | = | = |
| Border | none | = | = | = |
| Radius | 999px | = | = | = |
| Background | #27ae60 | #1e8449 | #1e8449 | #1e8449 |
| Box shadow | #27ae60 @ 0.15 0px 4px 9px 0px | #27ae60 @ 0.2 0px 6px 12px 0px | = | #27ae60 @ 0.2 0px 6px 12px 0px |
| Outline | none | = | 2px solid #ffffff offset 2px | = |
| Font | InterVariable 16px/24px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.3s ease | all 0.15s ease | all 0.15s ease | all 0.35s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | matrix(1, 0, 0, 1, 0, 2) |
| Cursor | pointer | = | = | = |
| Painted layers | a.p.button 134.0x50.0 bg #27ae60 r 999px shadow #27ae60 @ 0.15 0px 4px 9px 0px | a.p.button 134.0x50.0 bg #1e8449 r 999px shadow #27ae60 @ 0.2 0px 6px 12px 0px | a.p.button 134.0x50.0 bg #1e8449 r 999px shadow #27ae60 @ 0.15 0px 4px 9px 0px outline 2px solid #ffffff offset 2px | a.p.button 134.0x50.0 bg #1e8449 r 999px shadow #27ae60 @ 0.2 0px 6px 12px 0px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-cta-default.png`, `m-cta-hover.png`, `m-cta-focus-visible.png`, `m-cta-pressed.png`.

#### m-footer

Mobile footer. The phone footer.

Page: mobile. Selector: `mobile footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 1386.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | InterVariable 16px/24px 400 |
| Letter spacing | normal |
| Colour | #313942 |
| Text node | div.questions: InterVariable 14px/23.8px 400, #313942, ls -0.2px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 36 x 36, colour #313942 |
| Painted layers | section.slide.whiteSlide 390.0x1386.8 bg #ffffff; div.questions 123.2x32.8 bg #f1f8fe border B:1px solid #e5eef5 r 16px 16px 16px 0px shadow #000000 @ 0.03 0px 5px 13px 0px; div.badge-body 68.1x20.4 bg #27ae60 r 6px |
| How | at rest |

Crops: `m-footer-default.png`.

## Transitions declared in the readable stylesheets

designmodo.com serves its CSS bundles same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- app: `opacity 0.2s linear 0.5s`, `visibility, opacity 0.3s ease-in-out`, `0.2s ease-in-out`, `0.3s`, `stroke 0.3s, fill 0.3s`, `0.4s`, `0.2s ease-out 0.2s`, `0.15s ease-in-out`, `0.1s`, `0.3s ease-in-out`, `padding-left 0.4s, padding-right 0.4s`, `transform 0.4s`

- home: `0.35s`, `0.15s`, `0.3s`, `box-shadow 0.35s, transform 0.35s cubic-bezier(0.5, 0, 0.35, 1), opacity 0.35s cubic-bezier(0.5, 0, 0.35, 1), background 0.35s`, `0.35s cubic-bezier(0.35, 1.35, 0.5, 1)`, `0.25s`, `transform 0.5s`, `transform 0.35s, opacity 0.35s, box-shadow 0.35s`, `0.8s`, `opacity 0.35s`, `transform 0.5s, opacity 0.5s`, `opacity 0.5s`

- login: `0.35s`, `0.15s`, `0.3s`, `box-shadow 0.35s, transform 0.35s cubic-bezier(0.5, 0, 0.35, 1), opacity 0.35s cubic-bezier(0.5, 0, 0.35, 1), background 0.35s`, `0.35s cubic-bezier(0.35, 1.35, 0.5, 1)`, `0.25s`, `transform 0.5s`, `transform 0.35s, opacity 0.35s, box-shadow 0.35s`, `0.8s`, `opacity 0.35s`, `transform 0.5s, opacity 0.5s`, `opacity 0.5s`

- postcards: `background-color 0.15s, border-color 0.15s, color 0.15s`, `background-color 0.2s`, `transform 0.2s`, `none`, `transform 0.2s, background-color 0.2s`, `transform 0.35s cubic-bezier(0.22, 0.2, 0.03, 1), box-shadow 0.35s`, `transform 0.25s cubic-bezier(0.22, 0.2, 0.03, 1), opacity 0.25s`, `0.2s`, `0.35s`, `0.15s`, `0.3s`, `color 0.2s, text-decoration-color 0.2s`

- pricing: `background-color 0.15s, border-color 0.15s, color 0.15s`, `background-color 0.2s`, `transform 0.2s`, `none`, `transform 0.2s, background-color 0.2s`, `transform 0.35s cubic-bezier(0.22, 0.2, 0.03, 1), box-shadow 0.35s`, `transform 0.25s cubic-bezier(0.22, 0.2, 0.03, 1), opacity 0.25s`, `0.2s`, `0.35s`, `0.15s`, `0.3s`, `color 0.2s, text-decoration-color 0.2s`

- templates: `background-color 0.15s, border-color 0.15s, color 0.15s`, `background-color 0.2s`, `transform 0.2s`, `none`, `transform 0.2s, background-color 0.2s`, `top 0.35s`, `0.15s`, `background-color 0.15s, color 0.15s`, `border-color 0.15s`, `opacity 0.15s`, `all`, `transform 0.28s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.28s cubic-bezier(0.22, 1, 0.36, 1), color 0.15s`
