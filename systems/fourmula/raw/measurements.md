# Fourmula component measurements

Computed styles read from fourmula.ai on 2026-11-15 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844) across the site's painted surfaces — the fourmula.ai Webflow marketing site in both of its themes (the first-visit light paint, `.body.dark`, and the site's own dark paint on a plain `.body`, reached through the same isDarkMode key the header toggle writes), plus the separate dark-only Next.js + Tailwind v4 app at app.fourmula.ai (/start, /auth and the signed-out /project/create-pdp generator, which share no token layer with the marketing site) — with the finsweet consent modal measured then hidden (never answered), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `selected`, `expanded` and the rest are resting states reached by the page or by a local UI toggle.

## Components

### Cookie consent

#### cookie-modal

Cookie consent modal. The @finsweet consent modal shown on first load ("By clicking Accept all…"): the banner plus the cookie-preference manager. Measured, then hidden — never answered.

Page: home. Selector: `.cookies`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 13.3084px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.cookies__modal__title.u-title-3: Sf Pro Display 19.9626px/29.9439px 500, #020108, ls -0.174739px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 10) |
| Opacity | 0 |
| Icon | 19.95 x 19.95, colour #020108 @ 0.3 |
| Painted layers | div.cookies__modal__main 359.3x186.7 bg #d9d9d9 r 39.9252px; a.cookies__modal__close.w-inline-block 33.3x33.3 bg #f7f7f7 r 39.9252px; div.fs-cc_modal-buttons 359.3x66.5 bg #d9d9d9 r 39.9252px; a.btn-primary.u-btn 150.4x39.9 bg #020108 r 1317.53px; a.btn-outline.u-btn 152.4x39.9 bg #d9d9d9 border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 1317.53px; div.fs-cc_modal 0.0x0.0 bg #d9d9d9 r 39.9252px |
| Ancestor paint | 1 up body.body.dark bg #ffffff |
| How | at rest |

Crops: none.

#### cookie-accept

Accept all button. The filled "Accept all" in the consent modal; measured, never pressed.

Page: home. Selector: `.cookies .btn-primary "Accept all"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 150.39 x 39.92 | = |
| Padding | 11.6449px 19.9626px | = |
| Border | none | = |
| Radius | 1317.53px | = |
| Background | #020108 | #146ef5 |
| Box shadow | none | = |
| Outline | none | = |
| Font | Sf Pro Display 14.1402px/16.9682px 400 | = |
| Letter spacing | -0.282804px | = |
| Colour | #ffffff | = |
| Text node | div: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px | = |
| Transition | all 0.2s ease | = |
| Cursor | pointer | = |
| Painted layers | a.btn-primary.u-btn 150.4x39.9 bg #020108 r 1317.53px | a.btn-primary.u-btn 150.4x39.9 bg #146ef5 r 1317.53px |
| Ancestor paint | 1 up div.fs-cc_modal-buttons bg #d9d9d9 | = |
| How | at rest | mouse hover |

Crops: `cookie-accept-default.png`, `cookie-accept-hover.png`.

#### cookie-save

Save changes button. The outline "Save changes" inside the opened preference manager; measured, never pressed.

Page: home. Selector: `.cookies .btn-outline "Save changes"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 198.98 x 39.92 | = |
| Padding | 11.6449px 19.9626px | = |
| Border | 1px solid #020108 @ 0.2 | 1px solid #146ef5 |
| Radius | 1317.53px | = |
| Background | #d9d9d9 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Sf Pro Display 14.1402px/16.9682px 400 | = |
| Letter spacing | -0.282804px | = |
| Colour | #020108 | #146ef5 |
| Text node | div: Sf Pro Display 14.1402px/16.9682px 400, #020108, ls -0.282804px | div: Sf Pro Display 14.1402px/16.9682px 400, #146ef5, ls -0.282804px |
| Transition | all 0.2s ease | = |
| Cursor | pointer | = |
| Painted layers | a.btn-outline.u-btn 199.0x39.9 bg #d9d9d9 border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 1317.53px | a.btn-outline.u-btn 199.0x39.9 bg #d9d9d9 border T:1px solid #146ef5 / R:1px solid #146ef5 / B:1px solid #146ef5 / L:1px solid #146ef5 r 1317.53px |
| Ancestor paint | 1 up div.fs-cc_modal-buttons.is-form bg #d9d9d9 | = |
| How | at rest | mouse hover |

Crops: `cookie-save-default.png`, `cookie-save-hover.png`.

#### cookie-settings

Settings button. The outline "Settings" that opens the cookie-preference manager in place — a local UI toggle accepting nothing; the opened state was measured after clicking it, and the manager was left open to measure its controls.

Page: home. Selector: `.cookies .btn-outline "Settings"`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 152.39 x 39.92 | = | 0 x 0 |
| Padding | 11.6449px 19.9626px | = | = |
| Border | 1px solid #020108 @ 0.2 | 1px solid #146ef5 | = |
| Radius | 1317.53px | = | = |
| Background | #d9d9d9 | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Sf Pro Display 14.1402px/16.9682px 400 | = | = |
| Letter spacing | -0.282804px | = | = |
| Colour | #020108 | #146ef5 | = |
| Text node | div: Sf Pro Display 14.1402px/16.9682px 400, #020108, ls -0.282804px | div: Sf Pro Display 14.1402px/16.9682px 400, #146ef5, ls -0.282804px | - |
| Transition | all 0.2s ease | = | = |
| Cursor | pointer | = | = |
| Painted layers | a.btn-outline.u-btn 152.4x39.9 bg #d9d9d9 border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 1317.53px | a.btn-outline.u-btn 152.4x39.9 bg #d9d9d9 border T:1px solid #146ef5 / R:1px solid #146ef5 / B:1px solid #146ef5 / L:1px solid #146ef5 r 1317.53px | a.btn-outline.u-btn 0.0x0.0 bg #d9d9d9 border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 1317.53px |
| Ancestor paint | 1 up div.fs-cc_modal-buttons bg #d9d9d9 | = | = |
| How | at rest | mouse hover | own toggle |

Crops: `cookie-settings-default.png`, `cookie-settings-hover.png`.

#### cookie-check

Consent checkbox row. A category checkbox row in the opened preference manager (Strictly necessary is forced active); measured, never toggled.

Page: home. Selector: `.cookies .fs-cc_checkbox row`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 399.27 x 73.19 |
| Padding | 13.3084px 19.9626px 19.9626px 46.5794px |
| Gap | 3.3271px |
| Border | 1px solid #f7f7f7 |
| Radius | 19.9626px |
| Background | #d9d9d9 |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #020108 |
| Text node | div.fs-cc_titles.u-title-1: Sf Pro Display 13.3084px/19.9626px 500, #020108, ls -0.199626px |
| Transition | all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) |
| Cursor | not-allowed |
| ::before | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| ::after | 0px x 0px, static, bg #000000 @ 0, radius 0px |
| Painted layers | div.fs-cc_checkbox.is--not-allowed 399.3x73.2 bg #d9d9d9 border T:1px solid #f7f7f7 / R:1px solid #f7f7f7 / B:1px solid #f7f7f7 / L:1px solid #f7f7f7 r 19.9626px; div.fs-cc_checkbox-button._w--redirected-checked 16.6x16.6 bg #146ef5 border T:1px solid #146ef5 / R:1px solid #146ef5 / B:1px solid #146ef5 / L:1px solid #146ef5 r 4.65794px |
| How | at rest |

Crops: `cookie-check-default.png`.

### Site chrome

#### mkt-header

Site header. The 91px header: the logo-and-wordmark, the centre Menu pill with the theme toggle and scroll-percentage counter, the Fourmula-app account icon-link and the Get started pill.

Page: home. Selector: `.header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 92.48 |
| Padding | 19.9626px 26.6168px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.header__menu-txt.u-btn: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px |
| Transition | all 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 48.56 x 46.58, colour #020108 |
| Painted layers | div.header__main 206.2x39.9 bg #020108 r 1317.53px; div.header__menu-line.is-top 22.0x0.8 bg #ffffff; div.header__menu-line.is-bottom 22.0x0.8 bg #ffffff; div.header__theme 26.6x26.6 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 1317.53px; div.header__prc 47.9x26.6 bg #ffffff @ 0.2 r 1317.53px; a.header_signin.is-header-btn 26.6x26.6 border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 26.6168px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The header's fourmula.ai logo-and-wordmark.

Page: home. Selector: `.header__left`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 143.06 x 52.58 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Transition | none |
| Icon | 48.56 x 46.58, colour #020108 |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### menu-pill

Menu pill. The header's centre "Menu" pill (lines icon + label) — a local UI toggle that opens the fixed .menu overlay; the opened state was measured after clicking it, then closed.

Page: home. Selector: `.header__menu`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 78.48 x 35.23 | = | - | = | = |
| Padding | 6.65421px 0px 6.65421px 6.65421px | = | - | = | = |
| Gap | 9.98131px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Arial 14.4px/20px 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #333333 | = | - | = | = |
| Text node | div.header__menu-txt.u-btn: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px | = | - | = | = |
| Transition | opacity 0.2s ease | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | div.header__menu-line.is-top 22.0x0.8 bg #ffffff; div.header__menu-line.is-bottom 22.0x0.8 bg #ffffff | = | - | = | div.header__menu-line.is-top 16.1x16.1 bg #ffffff; div.header__menu-line.is-bottom 16.1x16.1 bg #ffffff |
| Ancestor paint | 1 up div.header__main bg #020108 | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Opacity | - | 0.64 | = | 0.64 | 0.64 |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `menu-pill-default.png`, `menu-pill-hover.png`, `menu-pill-pressed.png`, `menu-pill-opened.png`.

#### theme-toggle

Theme toggle. The sun/moon half of the header pill — writes localStorage isDarkMode and flips body.dark (note .body.dark paints the LIGHT surface). Never pressed here; both paints are captured as separate pages instead.

Page: home. Selector: `[data-theme-toggle]`. States: default, hover, focus-visible.

| Property | default | hover | focus-visible |
|---|---|---|---|
| Size (w x h) | 26.61 x 26.61 | = | - |
| Padding | 0px | = | - |
| Border | 1px solid #ffffff @ 0.2 | 1px solid #ffffff @ 0.65 | - |
| Radius | 1317.53px | = | - |
| Background | transparent | = | - |
| Box shadow | none | = | - |
| Outline | none | = | - |
| Font | Arial 14.4px/20px 400 | = | - |
| Letter spacing | normal | = | - |
| Colour | #333333 | = | - |
| Transition | all 0.2s ease | = | - |
| Cursor | pointer | = | - |
| Icon | 13.3 x 13.3, colour #ffffff | = | - |
| Painted layers | div.header__theme 26.6x26.6 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 1317.53px | div.header__theme 26.6x26.6 border T:1px solid #ffffff @ 0.65 / R:1px solid #ffffff @ 0.65 / B:1px solid #ffffff @ 0.65 / L:1px solid #ffffff @ 0.65 r 1317.53px | - |
| Ancestor paint | 1 up div.header__main bg #020108 | = | - |
| How | at rest | mouse hover | - |
| Skipped | - | = | focus failed: keyboard focus did not reach the element |

Crops: `theme-toggle-default.png`, `theme-toggle-hover.png`.

#### prc-counter

Scroll-percentage counter. The "0%" readout inside the header pill that counts down scroll progress through the page.

Page: home. Selector: `.header__prc`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 47.89 x 26.61 |
| Padding | 0px 7.31963px |
| Border | none |
| Radius | 1317.53px |
| Background | #ffffff @ 0.2 |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.header__prc-txt.u-btn: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px |
| Transition | none |
| Painted layers | div.header__prc 47.9x26.6 bg #ffffff @ 0.2 r 1317.53px |
| Ancestor paint | 1 up div.header__main bg #020108 |
| How | at rest |

Crops: `prc-counter-default.png`.

#### account-link

App account link. The icon-only "Fourmula app account" link to app.fourmula.ai/auth; measured, never followed.

Page: home. Selector: `a.header_signin.is-header-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 26.61 x 26.61 | = | = | = |
| Padding | 0px | = | = | = |
| Border | 1px solid #020108 @ 0.2 | 1px solid #020108 @ 0.64 | = | 1px solid #020108 @ 0.64 |
| Radius | 26.6168px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 14.4px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020108 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 13.3 x 13.3, colour #020108 | = | = | = |
| Painted layers | a.header_signin.is-header-btn 26.6x26.6 border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 26.6168px | a.header_signin.is-header-btn 26.6x26.6 border T:1px solid #020108 @ 0.64 / R:1px solid #020108 @ 0.64 / B:1px solid #020108 @ 0.64 / L:1px solid #020108 @ 0.64 r 26.6168px | = | a.header_signin.is-header-btn 26.6x26.6 border T:1px solid #020108 @ 0.64 / R:1px solid #020108 @ 0.64 / B:1px solid #020108 @ 0.64 / L:1px solid #020108 @ 0.64 r 26.6168px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `account-link-default.png`, `account-link-hover.png`, `account-link-focus-visible.png`, `account-link-pressed.png`.

#### header-cta

Get started button. The primary "Get started" pill in the header linking to app.fourmula.ai/start; measured, never followed.

Page: home. Selector: `a.btn-primary.is-header-btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.81 x 39.92 | = | = | = |
| Padding | 11.6449px 19.9626px | = | = | = |
| Border | none | = | = | = |
| Radius | 1317.53px | = | = | = |
| Background | #020108 | #ff6b02 | = | #ff6b02 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Sf Pro Display 14.1402px/16.9682px 400 | = | = | = |
| Letter spacing | -0.282804px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.char: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Transform | matrix(1, 0, 0, 1, 0, 0) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-primary.u-btn 101.8x39.9 bg #020108 r 1317.53px | a.btn-primary.u-btn 101.8x39.9 bg #ff6b02 r 1317.53px | = | a.btn-primary.u-btn 101.8x39.9 bg #ff6b02 r 1317.53px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `header-cta-default.png`, `header-cta-hover.png`, `header-cta-focus-visible.png`, `header-cta-pressed.png`.

#### mkt-header-dark

Site header (dark paint). The 91px header under the site's dark paint (plain .body, isDarkMode=false): the Menu pill, the theme toggle, the scroll-percentage counter, the account icon-link and the Get started pill.

Page: home-dark. Selector: `.header @ dark paint`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 92.48 |
| Padding | 19.9626px 26.6168px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.header__menu-txt.u-btn: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px |
| Transition | all 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 48.56 x 46.58, colour #ffffff |
| Painted layers | div.header__main 206.2x39.9 bg #272727 r 1317.53px; div.header__menu-line.is-top 22.0x0.8 bg #ffffff; div.header__menu-line.is-bottom 22.0x0.8 bg #ffffff; div.header__theme 26.6x26.6 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 1317.53px; div.header__prc 47.9x26.6 bg #ffffff @ 0.2 r 1317.53px; a.header_signin.is-header-btn 26.6x26.6 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 26.6168px |
| How | at rest |

Crops: `mkt-header-dark-default.png`.

#### menu-pill-dark

Menu pill (dark paint). The header's centre "Menu" pill under the dark paint.

Page: home-dark. Selector: `.header__menu @ dark paint`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 78.48 x 35.23 |
| Padding | 6.65421px 0px 6.65421px 6.65421px |
| Gap | 9.98131px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.header__menu-txt.u-btn: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px |
| Transition | opacity 0.2s ease |
| Cursor | pointer |
| Painted layers | div.header__menu-line.is-top 22.0x0.8 bg #ffffff; div.header__menu-line.is-bottom 22.0x0.8 bg #ffffff |
| Ancestor paint | 1 up div.header__main bg #272727 |
| How | at rest |

Crops: `menu-pill-dark-default.png`.

#### header-cta-dark

Get started button (dark paint). The header's primary "Get started" pill under the dark paint; measured, never followed.

Page: home-dark. Selector: `a.btn-primary.is-header-btn @ dark paint`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 101.81 x 39.92 |
| Padding | 11.6449px 19.9626px |
| Border | none |
| Radius | 1317.53px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 14.1402px/16.9682px 400 |
| Letter spacing | -0.282804px |
| Colour | #020108 |
| Text node | div.char: Sf Pro Display 14.1402px/16.9682px 400, #020108, ls -0.282804px |
| Transition | all 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Cursor | pointer |
| Painted layers | a.btn-primary.u-btn 101.8x39.9 bg #ffffff r 1317.53px |
| How | at rest |

Crops: `header-cta-dark-default.png`.

### Nav overlay

#### nav-overlay

Nav overlay. The fixed .menu overlay opened by the Menu pill: PDP's / Products / Videos / Our features anchors, Privacy/Terms/Cookie links, Instagram and the app account link. Its links were never followed.

Page: home. Selector: `.menu (opened)`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 1440 x 528.98 |
| Padding | 9.98131px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.menu__label.u-small-text-1: Sf Pro Display 9.98131px/14.972px 400, #020108 @ 0.5, ls -0.0998131px |
| Transition | all 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 13.3 x 13.3, colour #020108 |
| Painted layers | div.menu__wrap 239.5x519.0 bg #d9d9d9 r 26.6168px; div.menu__item.is-lined 206.3x102.2 border T:1px solid #020108 @ 0.2; a.btn-primary.u-btn 0.0x0.0 bg #020108 r 1317.53px; a.header_signin.w-inline-block 26.6x26.6 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 26.6168px |
| How | held open by an earlier toggle |

Crops: `nav-overlay-opened.png`.

#### nav-overlay-link

Nav overlay link. An anchor link inside the opened .menu overlay ("PDP's"); measured, never followed.

Page: home. Selector: `.menu .menu__link "PDP's"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 206.3 x 29.95 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Sf Pro Display 19.9626px/29.9439px 500 | = |
| Letter spacing | -0.174739px | = |
| Colour | #020108 | = |
| Text node | div.char: Sf Pro Display 19.9626px/29.9439px 500, #020108, ls -0.174739px | = |
| Transition | opacity 0.2s ease | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `nav-overlay-link-default.png`, `nav-overlay-link-hover.png`.

### Home

#### hero-h1

Hero headline. "Your catalog, instantly re-shot." — the display h1; the second line paints --fonts-50 (u-fonts-50).

Page: home. Selector: `.hero__title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 485.36 x 137.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 73.1963px/68.8045px 400 |
| Letter spacing | -2.19589px |
| Colour | #020108 |
| Text node | span.hero-flash-word: Sf Pro Display 73.1963px/68.8045px 400, #020108, ls -2.19589px |
| Transition | none |
| How | at rest |

Crops: `hero-h1-default.png`.

#### hero-word

Hero keyword chip. A chip in the hero's right-edge rotating word column (PDPs / UGC / Lifestyle shots / Ads / Stories / Street style).

Page: home. Selector: `.hero__slider__item`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 58.91 x 31.94 |
| Padding | 4.65794px 13.3084px 5.32336px 13.3084px |
| Border | 1px solid #020108 @ 0.2 |
| Radius | 6.65421px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.hero__slider__item-txt.u-title-2: Sf Pro Display 13.3084px/19.9626px 500, #020108, ls -0.174739px |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Painted layers | div.hero__slider__item 58.9x31.9 bg #ffffff border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 6.65421px |
| How | at rest |

Crops: `hero-word-default.png`.

#### hero-scroll

Scroll-down cue. The "SCROLL DOWN" micro-label at the hero's bottom right, an in-page anchor to #what-is-fourmula; measured, never followed.

Page: home. Selector: `.hero__scroll`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 56.2 x 8.31 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Sf Pro Display 8.31776px/8.31776px 500 | = |
| Letter spacing | -0.166355px | = |
| Colour | #020108 | = |
| Text node | span.hero-flash-word: Sf Pro Display 8.31776px/8.31776px 500, #020108, ls -0.166355px | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `hero-scroll-default.png`, `hero-scroll-hover.png`.

#### section-h2

Section heading. "On-brand visuals. Made by AI." — the u-h2 section heading style.

Page: home. Selector: `.what__title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 686.11 x 199.63 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 99.8131px/99.8131px 400 |
| Letter spacing | -2.99439px |
| Colour | #020108 |
| Text node | span.flash-word: Sf Pro Display 99.8131px/99.8131px 400, #020108, ls -2.99439px |
| Transition | none |
| How | at rest |

Crops: `section-h2-default.png`.

#### ai-btn

Round app link. The 53px round icon-link ("fourmula.ai") into app.fourmula.ai/start, repeated beside the AI feature copy; measured, never followed.

Page: home. Selector: `a.ai__btn`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 53.22 x 53.22 | 47.9 x 47.9 | = | 47.9 x 47.9 |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 1317.53px | = | = | = |
| Background | #ffffff | #ff6b02 | = | #ff6b02 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Arial 14.4px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #000000 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 26.61 x 26.61, colour #000000 | 23.95 x 23.95, colour #000000 | = | 23.95 x 23.95, colour #000000 |
| Painted layers | a.ai__btn.w-inline-block 53.2x53.2 bg #ffffff r 1317.53px | a.ai__btn.w-inline-block 47.9x47.9 bg #ff6b02 r 1317.53px | = | a.ai__btn.w-inline-block 47.9x47.9 bg #ff6b02 r 1317.53px |
| Ancestor paint | 1 up div.ai__top bg #f7f7f7 | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Transform | - | matrix(0.9, 0, 0, 0.9, 0, 0) | = | matrix(0.9, 0, 0, 0.9, 0, 0) |

Crops: `ai-btn-default.png`, `ai-btn-hover.png`, `ai-btn-focus-visible.png`, `ai-btn-pressed.png`.

#### how-cta

How-it-works CTA. The "Get started" pill in the How It Works section; measured, never followed.

Page: home. Selector: `a.btn-primary.is-how`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.81 x 39.92 | = | = | = |
| Padding | 11.6449px 19.9626px | = | = | = |
| Border | none | = | = | = |
| Radius | 1317.53px | = | = | = |
| Background | #020108 | #ec6302 | = | #ff6b02 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Sf Pro Display 14.1402px/16.9682px 400 | = | = | = |
| Letter spacing | -0.282804px | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | div.char: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-primary.u-btn 101.8x39.9 bg #020108 r 1317.53px | a.btn-primary.u-btn 101.8x39.9 bg #ec6302 r 1317.53px | = | a.btn-primary.u-btn 101.8x39.9 bg #ff6b02 r 1317.53px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `how-cta-default.png`, `how-cta-hover.png`, `how-cta-focus-visible.png`, `how-cta-pressed.png`.

#### step-h3

Step heading. A u-h2-5 step heading in the "From idea to assets in four steps" section.

Page: home. Selector: `.list__main__h2`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 693.39 x 106.47 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 53.2336px/53.2336px 400 |
| Letter spacing | -1.59701px |
| Colour | #ffffff |
| Text node | span.flash-word: Sf Pro Display 53.2336px/53.2336px 400, #ffffff, ls -1.59701px |
| Transition | none |
| How | at rest |

Crops: `step-h3-default.png`.

#### step-cta

Step CTA. The "Get started" button repeated beside each of the four steps, linking to app.fourmula.ai/start; measured, never followed.

Page: home. Selector: `a.btn-primary-stb`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 101.81 x 39.92 | = | = | = |
| Padding | 11.6449px 19.9626px | = | = | = |
| Border | none | = | = | = |
| Radius | 1317.53px | = | = | = |
| Background | #ffffff | #06050c | = | #020108 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Sf Pro Display 14.1402px/16.9682px 400 | = | = | = |
| Letter spacing | -0.282804px | = | = | = |
| Colour | #020108 | #fbfbfb | = | #ffffff |
| Text node | div.char: Sf Pro Display 14.1402px/16.9682px 400, #020108, ls -0.282804px | div.char: Sf Pro Display 14.1402px/16.9682px 400, #fbfbfb, ls -0.282804px | = | div.char: Sf Pro Display 14.1402px/16.9682px 400, #ffffff, ls -0.282804px |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn-primary-stb.u-btn 101.8x39.9 bg #ffffff r 1317.53px | a.btn-primary-stb.u-btn 101.8x39.9 bg #06050c r 1317.53px | = | a.btn-primary-stb.u-btn 101.8x39.9 bg #020108 r 1317.53px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `step-cta-default.png`, `step-cta-hover.png`, `step-cta-focus-visible.png`, `step-cta-pressed.png`.

#### hero-h1-dark

Hero headline (dark paint). "Your catalog, instantly re-shot." under the dark paint — the second line picks up --fonts-50.

Page: home-dark. Selector: `.hero__title @ dark paint`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 485.36 x 137.59 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 73.1963px/68.8045px 400 |
| Letter spacing | -2.19589px |
| Colour | #ffffff |
| Text node | span.hero-flash-word: Sf Pro Display 73.1963px/68.8045px 400, #ffffff, ls -2.19589px |
| Transition | none |
| How | at rest |

Crops: `hero-h1-dark-default.png`.

#### step-cta-dark

Step CTA (dark paint). A "Get started" button in the four-steps section under the dark paint; measured, never followed.

Page: home-dark. Selector: `a.btn-primary-stb @ dark paint`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 101.81 x 39.92 |
| Padding | 11.6449px 19.9626px |
| Border | none |
| Radius | 1317.53px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 14.1402px/16.9682px 400 |
| Letter spacing | -0.282804px |
| Colour | #020108 |
| Text node | div.char: Sf Pro Display 14.1402px/16.9682px 400, #020108, ls -0.282804px |
| Transition | all 0.2s ease |
| Cursor | pointer |
| Painted layers | a.btn-primary-stb.u-btn 101.8x39.9 bg #ffffff r 1317.53px |
| How | at rest |

Crops: `step-cta-dark-default.png`.

### FAQ accordion

#### faq-item

FAQ row. A FAQ accordion row ("What can AI FOURMULA create for my brand?") — a local UI toggle whose + icon flips and the answer expands; the opened state was measured after clicking, then re-closed by toggling again.

Page: home. Selector: `.faq__item`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 1060.72 x 75.02 | = | 1060.72 x 118.02 |
| Padding | 26.6168px | = | = |
| Border | T: none; R: none; B: 1px solid #d7d7d6; L: none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | Arial 14.4px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #333333 | = | = |
| Text node | div.faq__label.u-body-3: Sf Pro Display 16.6355px/20.7944px 500, #020108 | = | = |
| Transition | none | = | = |
| Painted layers | div.faq__item 1060.7x75.0 border B:1px solid #d7d7d6 | = | div.faq__item.active 1060.7x118.0 border B:1px solid #d7d7d6 |
| How | at rest | mouse hover | own toggle |

Crops: `faq-item-default.png`, `faq-item-hover.png`, `faq-item-opened.png`.

#### faq-item-dark

FAQ row (dark paint). A closed FAQ accordion row under the dark paint.

Page: home-dark. Selector: `.faq__item @ dark paint`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1060.72 x 75.02 |
| Padding | 26.6168px |
| Border | T: none; R: none; B: 1px solid #2a2a30; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.faq__label.u-body-3: Sf Pro Display 16.6355px/20.7944px 500, #ffffff |
| Transition | none |
| Painted layers | div.faq__item 1060.7x75.0 border B:1px solid #2a2a30 |
| How | at rest |

Crops: `faq-item-dark-default.png`.

### Footer

#### footer

Footer. The 811px page footer: the fourmula.ai mark, section anchors (PDP's / Videos / Products / Our features), legal links, Instagram.

Page: home. Selector: `.footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 811.78 |
| Padding | 6.65421px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.char: Sf Pro Display 13.3084px/19.9626px 500, #020108, ls -0.199626px |
| Transition | none |
| Icon | 292.78 x 53.22, colour #020108 |
| Painted layers | div.footer__wrap 1426.7x798.5 bg #f7f7f7 r 39.9252px; div.dot 13.3x13.3 bg #020108 r 50%; div.dot 13.3x13.3 bg #020108 r 50%; div.dot 13.3x13.3 bg #020108 r 50%; div.dot 13.3x13.3 bg #020108 r 50%; div.dot 13.3x13.3 bg #020108 r 50% |
| How | at rest |

Crops: `footer-default.png`.

#### footer-link

Footer link. The "Privacy Policy" footer link; measured, never followed.

Page: home. Selector: `.footer__main__link-small "Privacy Policy"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 68.59 x 17.45 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | Sf Pro Display 11.6449px/17.4673px 500 | = | = | = |
| Letter spacing | -0.174739px | = | = | = |
| Colour | #020108 | = | = | = |
| Text node | div.char: Sf Pro Display 11.6449px/17.4673px 500, #020108, ls -0.174739px | = | = | = |
| Transition | opacity 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Opacity | - | 0.65 | = | 0.65 |

Crops: `footer-link-default.png`, `footer-link-hover.png`, `footer-link-focus-visible.png`, `footer-link-pressed.png`.

#### footer-dark

Footer (dark paint). The page footer under the dark paint.

Page: home-dark. Selector: `.footer @ dark paint`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 811.78 |
| Padding | 6.65421px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.char: Sf Pro Display 13.3084px/19.9626px 500, #ffffff, ls -0.199626px |
| Transition | none |
| Icon | 292.78 x 53.22, colour #ffffff |
| Painted layers | div.footer__wrap 1426.7x798.5 bg #111111 r 39.9252px; div.dot 13.3x13.3 bg #ffffff r 50%; div.dot 13.3x13.3 bg #ffffff r 50%; div.dot 13.3x13.3 bg #ffffff r 50%; div.dot 13.3x13.3 bg #ffffff r 50%; div.dot 13.3x13.3 bg #ffffff r 50% |
| How | at rest |

Crops: `footer-dark-default.png`.

### Legal pages

#### legal-title

Legal page title. "PRIVACY & COOKIES POLICY" — the legal page heading.

Page: privacy. Selector: `.tech h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1386.78 x 153.72 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 73.1963px/76.8561px 500 |
| Letter spacing | -1.33084px |
| Colour | #020108 |
| Transition | none |
| How | at rest |

Crops: `legal-title-default.png`.

#### legal-body

Legal body copy. A body paragraph in the privacy policy — the legal prose text style.

Page: privacy. Selector: `.tech p`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1386.78 x 67.36 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.972px/22.4579px 400 |
| Letter spacing | normal |
| Colour | #020108 |
| Transition | none |
| How | at rest |

Crops: `legal-body-default.png`.

#### legal-link

Legal inline link. A link inside the privacy-policy prose; measured, never followed.

Page: privacy. Selector: `.tech a`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 78.23 x 17 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 14.972px/17.9664px 400 | = |
| Letter spacing | normal | = |
| Colour | #020108 | = |
| Transition | none | = |
| Cursor | pointer | = |
| How | at rest | mouse hover |

Crops: `legal-link-default.png`, `legal-link-hover.png`.

#### legal-section

Legal section. The .tech section the legal pages paint their prose in.

Page: privacy. Selector: `.tech`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 6033.16 |
| Padding | 106.467px 26.6168px 0px 26.6168px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 14.4px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | h1.tech__title.u-h3: Sf Pro Display 73.1963px/76.8561px 500, #020108, ls -1.33084px |
| Transition | none |
| Painted layers | th.tech__rich-cell.is-head 159.5x36.5 bg #000000 @ 0.04 border B:2px solid #000000 @ 0.25; th.tech__rich-cell.is-head 455.8x36.5 bg #000000 @ 0.04 border B:2px solid #000000 @ 0.25; th.tech__rich-cell.is-head 411.2x36.5 bg #000000 @ 0.04 border B:2px solid #000000 @ 0.25; th.tech__rich-cell.is-head 360.3x36.5 bg #000000 @ 0.04 border B:2px solid #000000 @ 0.25; td.tech__rich-cell 159.5x68.2 border B:1px solid #000000 @ 0.15; td.tech__rich-cell 455.8x68.2 border B:1px solid #000000 @ 0.15 |
| How | at rest |

Crops: `legal-section-default.png`.

### App chrome

#### app-menu-btn

App menu button. The 32px icon button (aria "Open main menu") in the app header — a local UI toggle that opens the nav drawer; the opened state was measured after clicking it, then the drawer was closed with Escape.

Page: auth. Selector: `button[aria-label="Open main menu"]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | sfProFont 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | #f94a00 | = | #f94a00 | #f94a00 |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 32 x 32, colour #ffffff | 32 x 32, colour #f94a00 | = | 32 x 32, colour #f94a00 | 32 x 32, colour #f94a00 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `app-menu-btn-default.png`, `app-menu-btn-hover.png`, `app-menu-btn-focus-visible.png`, `app-menu-btn-pressed.png`, `app-menu-btn-opened.png`.

#### app-create-btn

Create asset button. The header's "Create asset" submit — its states were measured but it was never pressed (it would start an authenticated action).

Page: auth. Selector: `header "Create asset" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123 x 32 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 | #f94a00 | = | #f94a00 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020108 | = | = | = |
| Text node | span.flex.items-center: sfProFont 14px/20px 400, #020108 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #020108 | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 123.0x32.0 bg #ff6b02 r 3.35544e+07px | button.cursor-pointer.transition-colors 123.0x32.0 bg #f94a00 r 3.35544e+07px | = | button.cursor-pointer.transition-colors 123.0x32.0 bg #f94a00 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-create-btn-default.png`, `app-create-btn-hover.png`, `app-create-btn-focus-visible.png`, `app-create-btn-pressed.png`.

#### app-signin-btn

Sign in button. The header's "Sign in" button (aria "Sign in to your account"); measured, never pressed.

Page: auth. Selector: `button[aria-label="Sign in to your account"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 66 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 @ 0.2 | #ff6b02 @ 0.35 | = | #ff6b02 @ 0.35 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff6b02 | = | = | = |
| Text node | span.flex.items-center: sfProFont 14px/20px 400, #ff6b02 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 66.0x32.0 bg #ff6b02 @ 0.2 r 3.35544e+07px | button.cursor-pointer.transition-colors 66.0x32.0 bg #ff6b02 @ 0.35 r 3.35544e+07px | = | button.cursor-pointer.transition-colors 66.0x32.0 bg #ff6b02 @ 0.35 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `app-signin-btn-default.png`, `app-signin-btn-hover.png`, `app-signin-btn-focus-visible.png`, `app-signin-btn-pressed.png`.

#### app-menu-btn-pdp

App menu button. The 32px icon button (aria "Open main menu") in the app header — a local UI toggle that opens the nav drawer; the opened state was measured after clicking it, then the drawer was closed with Escape.

Page: create-pdp. Selector: `button[aria-label="Open main menu"]`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 32 x 32 | = | = | = | = |
| Padding | 0px | = | = | = | = |
| Border | none | = | = | = | = |
| Radius | 0px | = | = | = | = |
| Background | transparent | = | = | = | = |
| Box shadow | none | = | = | = | = |
| Outline | none | = | = | = | = |
| Font | sfProFont 16px/24px 400 | = | = | = | = |
| Letter spacing | normal | = | = | = | = |
| Colour | #ffffff | #f94a00 | = | #f94a00 | #f94a00 |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = | = |
| Cursor | pointer | = | = | = | = |
| Icon | 32 x 32, colour #ffffff | 32 x 32, colour #f94a00 | = | 32 x 32, colour #f94a00 | 32 x 32, colour #f94a00 |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover | own toggle |

Crops: `app-menu-btn-pdp-default.png`, `app-menu-btn-pdp-hover.png`, `app-menu-btn-pdp-focus-visible.png`, `app-menu-btn-pdp-pressed.png`, `app-menu-btn-pdp-opened.png`.

#### app-header

App header. The app's floating header — a fixed rounded-full bar (1392x56 at 24,24) holding the menu button, the Create asset submit and the Sign in button.

Page: auth. Selector: `header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1392 x 56 |
| Padding | 0px 16px |
| Border | none |
| Radius | 3.35544e+07px |
| Background | #020108 |
| Box shadow | none |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | sfProFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.flex.items-center: sfProFont 14px/20px 400, #020108 |
| Transition | none |
| Icon | 32 x 32, colour #ffffff |
| Painted layers | header.fixed.top-4 1392.0x56.0 bg #020108 r 3.35544e+07px; button.cursor-pointer.transition-colors 123.0x32.0 bg #ff6b02 r 3.35544e+07px; button.cursor-pointer.transition-colors 66.0x32.0 bg #ff6b02 @ 0.2 r 3.35544e+07px |
| How | at rest |

Crops: `app-header-default.png`.

### App start

#### start-h1

Start headline. "Create studio-quality product photos" — the signed-out start-page masthead (the page titles itself "Formula AI | Start").

Page: start. Selector: `start h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 432.33 x 104 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sfProFont 52px/52px 500 |
| Letter spacing | -2.08px |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `start-h1-default.png`.

#### start-cta

Start CTA. The large "Create asset" button in the start-page body; its states were measured but it was never pressed.

Page: start. Selector: `start "Create asset" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 139 x 40 | = | = | = |
| Padding | 0px 24px 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 | #f94a00 | = | #f94a00 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020108 | = | = | = |
| Text node | span.flex.items-center: sfProFont 14px/20px 400, #020108 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #020108 | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 139.0x40.0 bg #ff6b02 r 3.35544e+07px | button.cursor-pointer.transition-colors 139.0x40.0 bg #f94a00 r 3.35544e+07px | = | button.cursor-pointer.transition-colors 139.0x40.0 bg #f94a00 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `start-cta-default.png`, `start-cta-hover.png`, `start-cta-focus-visible.png`, `start-cta-pressed.png`.

### App sign-in

#### auth-card

Sign-in card. The sign-in card over the dark field: "Sign in" heading, Continue with Google, Email + Password fields, Sign in submit, the Forgot password? and Sign up switchers.

Page: auth. Selector: `auth card (painted ancestor of email input)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 384 x 468.8 |
| Padding | 24px 32px |
| Gap | 24px |
| Border | 1px solid #1a1a1a |
| Radius | 28px |
| Background | #111111 |
| Box shadow | none |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | sfProFont 12px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.font-medium.w-full: sfProFont 32px/44.8px 500, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #ff6b02 |
| Painted layers | div.p-6.sm:p-8 384.0x468.8 bg #111111 border T:1px solid #1a1a1a / R:1px solid #1a1a1a / B:1px solid #1a1a1a / L:1px solid #1a1a1a r 28px; button.cursor-pointer.transition-colors 318.0x40.0 bg #ff6b02 @ 0.2 r 3.35544e+07px; div.flex-1.h-px 141.5x1.0 bg #ffffff @ 0.1; div.flex-1.h-px 141.5x1.0 bg #ffffff @ 0.1; div.relative.w-full 318.0x48.0 bg #020108 r 3.35544e+07px; div.relative.w-full 318.0x48.0 bg #020108 r 3.35544e+07px |
| How | at rest |

Crops: `auth-card-default.png`.

#### auth-back

Back button. The "Back" button over the auth card; measured, never pressed (it navigates to the start page).

Page: auth. Selector: `auth "Back" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 70 x 32 | = | = | = |
| Padding | 0px 12px 0px 8px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ffffff @ 0.05 | #ffffff @ 0.15 | = | #ffffff @ 0.15 |
| Box shadow | none | = | = | = |
| Backdrop filter | blur(24px) | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #b0b4ba | = | = | = |
| Text node | span.flex.items-center: sfProFont 14px/20px 500, #b0b4ba | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #b0b4ba | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 70.0x32.0 bg #ffffff @ 0.05 r 3.35544e+07px | button.cursor-pointer.transition-colors 70.0x32.0 bg #ffffff @ 0.15 r 3.35544e+07px | = | button.cursor-pointer.transition-colors 70.0x32.0 bg #ffffff @ 0.15 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-back-default.png`, `auth-back-hover.png`, `auth-back-focus-visible.png`, `auth-back-pressed.png`.

#### auth-google

Google sign-in. The "Continue with Google" button; measured, never pressed — it would start the OAuth flow.

Page: auth. Selector: `auth "Continue with Google"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 318 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 @ 0.2 | #ff6b02 @ 0.35 | = | #ff6b02 @ 0.35 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 500 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff6b02 | = | = | = |
| Text node | span.flex.items-center: sfProFont 14px/20px 500, #ff6b02 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ff6b02 | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 318.0x40.0 bg #ff6b02 @ 0.2 r 3.35544e+07px | button.cursor-pointer.transition-colors 318.0x40.0 bg #ff6b02 @ 0.35 r 3.35544e+07px | = | button.cursor-pointer.transition-colors 318.0x40.0 bg #ff6b02 @ 0.35 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-google-default.png`, `auth-google-hover.png`, `auth-google-focus-visible.png`, `auth-google-pressed.png`.

#### auth-field-email

Email field. The "Email address" field on the sign-in card; focused and typed into then cleared — never submitted.

Page: auth. Selector: `auth input[type=email]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 286 x 48 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sfProFont 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #686a6e, opacity 1 | = | = |
| Ancestor paint | 1 up div.relative.w-full bg #020108 | 1 up div.relative.w-full bg #1a1a1a | 1 up div.relative.w-full bg #1a1a1a |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `auth-field-email-default.png`, `auth-field-email-focused.png`, `auth-field-email-filled.png`.

#### auth-field-pass

Password field. The "Password" field on the sign-in card; focused and typed into then cleared — never submitted.

Page: auth. Selector: `auth input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 262 x 48 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sfProFont 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #686a6e, opacity 1 | = | = |
| Ancestor paint | 1 up div.relative.w-full bg #020108 | 1 up div.relative.w-full bg #1a1a1a | 1 up div.relative.w-full bg #1a1a1a |
| How | at rest | clicked into the field | typed "not-a-real-password", then deleted; nothing sent |

Crops: `auth-field-pass-default.png`, `auth-field-pass-focused.png`, `auth-field-pass-filled.png`.

#### auth-eye

Password visibility eye. The eye button inside the password field — a local UI toggle; measured at rest, never needed to reveal anything.

Page: auth. Selector: `button[aria-label="Toggle password visibility"]`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 16 x 16 | = |
| Padding | 0px | = |
| Border | none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sfProFont 14px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #686a6e | #ffffff |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Icon | 16 x 16, colour #686a6e | 16 x 16, colour #ffffff |
| Ancestor paint | 1 up div.relative.w-full bg #020108 | 1 up div.relative.w-full bg #1a1a1a |
| How | at rest | mouse hover |

Crops: `auth-eye-default.png`, `auth-eye-hover.png`.

#### auth-submit

Sign-in submit. The card's "Sign in" submit; its states were measured but the button was never pressed — nothing was submitted.

Page: auth. Selector: `auth card "Sign in" submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 318 x 40 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 | #f94a00 | = | #f94a00 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020108 | = | = | = |
| Text node | span.flex.items-center: sfProFont 14px/20px 400, #020108 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 318.0x40.0 bg #ff6b02 r 3.35544e+07px | button.cursor-pointer.transition-colors 318.0x40.0 bg #f94a00 r 3.35544e+07px | = | button.cursor-pointer.transition-colors 318.0x40.0 bg #f94a00 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `auth-submit-default.png`, `auth-submit-hover.png`, `auth-submit-focus-visible.png`, `auth-submit-pressed.png`.

#### auth-forgot

Forgot password submit. The "Forgot password?" button on the sign-in card — a form action, not a view switch: pressing it validates the email field in place (the card shows "Please enter a valid email address" and stays on sign-in), and completing it submits. Measured at rest, never pressed.

Page: auth. Selector: `auth "Forgot password?"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 98 x 17 | = |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #686a6e; L: none | T: none; R: none; B: 1px solid #f94a00; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sfProFont 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #686a6e | #f94a00 |
| Text node | span.flex.items-center: sfProFont 12px/16px 400, #686a6e | span.flex.items-center: sfProFont 12px/16px 400, #f94a00 |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.cursor-pointer.transition-colors 98.0x17.0 border B:1px solid #686a6e | button.cursor-pointer.transition-colors 98.0x17.0 border B:1px solid #f94a00 |
| How | at rest | mouse hover |

Crops: `auth-forgot-default.png`, `auth-forgot-hover.png`.

#### auth-switch

Sign-up switcher. The "Sign up" text button at the card's foot that switches it to the create-account view — a local UI switch; measured at rest.

Page: auth. Selector: `auth card "Sign up" switcher`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 41 x 17 | = |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #ff6b02; L: none | T: none; R: none; B: 1px solid #f94a00; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sfProFont 12px/16px 400 | = |
| Letter spacing | normal | = |
| Colour | #ff6b02 | #f94a00 |
| Text node | span.flex.items-center: sfProFont 12px/16px 400, #ff6b02 | span.flex.items-center: sfProFont 12px/16px 400, #f94a00 |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.cursor-pointer.transition-colors 41.0x17.0 border B:1px solid #ff6b02 | button.cursor-pointer.transition-colors 41.0x17.0 border B:1px solid #f94a00 |
| How | at rest | mouse hover |

Crops: `auth-switch-default.png`, `auth-switch-hover.png`.

#### auth-forgot-card

Forgot-password view (uncaptured). The auth card's reset view. "Forgot password?" is a form action, not a local UI switch: pressing it validates the email field in place and the card stays on sign-in, while a valid email would submit — so the reset view is uncaptured.

Page: auth. Selector: `auth card @ forgot view`. States: opened.

| Property | opened |
|---|---|
| Note | never pressed — the control submits |

Crops: none.

#### auth-signup-card

Create-account view. The auth card switched to its create-account view by pressing the "Sign up" switcher; fields were measured, the create submit was never pressed. Returned to the sign-in view afterwards.

Page: auth. Selector: `auth card @ signup view`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 384 x 435.8 |
| Padding | 24px 32px |
| Gap | 24px |
| Border | 1px solid #1a1a1a |
| Radius | 28px |
| Background | #111111 |
| Box shadow | none |
| Backdrop filter | blur(24px) |
| Outline | none |
| Font | sfProFont 12px/16px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.font-medium.w-full: sfProFont 32px/44.8px 500, #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #ff6b02 |
| Painted layers | div.p-6.sm:p-8 384.0x435.8 bg #111111 border T:1px solid #1a1a1a / R:1px solid #1a1a1a / B:1px solid #1a1a1a / L:1px solid #1a1a1a r 28px; button.cursor-pointer.transition-colors 318.0x40.0 bg #ff6b02 @ 0.2 r 3.35544e+07px; div.flex-1.h-px 141.5x1.0 bg #ffffff @ 0.1; div.flex-1.h-px 141.5x1.0 bg #ffffff @ 0.1; div.relative.w-full 318.0x48.0 bg #020108 r 3.35544e+07px; div.relative.w-full 318.0x48.0 bg #020108 r 3.35544e+07px |
| How | held open by an earlier toggle |

Crops: `auth-signup-card-opened.png`.

### Create-PDP generator

#### pdp-cancel

Cancel button. The header's "Cancel and close" (aria "Cancel and close PDP creation"); measured, never pressed — it would leave the generator.

Page: create-pdp. Selector: `button[aria-label="Cancel and close PDP creation"]`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 131 x 32 | = | = | = |
| Padding | 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 @ 0.2 | #ff6b02 @ 0.35 | = | #ff6b02 @ 0.35 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff6b02 | = | = | = |
| Text node | span.hidden.sm:block: sfProFont 14px/20px 400, #ff6b02 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 131.0x32.0 bg #ff6b02 @ 0.2 r 3.35544e+07px | button.cursor-pointer.transition-colors 131.0x32.0 bg #ff6b02 @ 0.35 r 3.35544e+07px | = | button.cursor-pointer.transition-colors 131.0x32.0 bg #ff6b02 @ 0.35 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-cancel-default.png`, `pdp-cancel-hover.png`, `pdp-cancel-focus-visible.png`, `pdp-cancel-pressed.png`.

#### pdp-start-header

Start generation (header). The header's compact "Start generation" submit; measured, never pressed — it would queue a generation.

Page: create-pdp. Selector: `header "Start generation" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 123 x 32 | = | - | = |
| Padding | 0px 12px | = | - | = |
| Border | none | = | - | = |
| Radius | 3.35544e+07px | = | - | = |
| Background | #ff6b02 @ 0.15 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sfProFont 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ff6b02 @ 0.15 | = | - | = |
| Text node | span.hidden.xs:inline: sfProFont 14px/20px 400, #ff6b02 @ 0.15 | = | - | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Painted layers | button.transition-colors.duration-200 123.0x32.0 bg #ff6b02 @ 0.15 r 3.35544e+07px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `pdp-start-header-default.png`, `pdp-start-header-hover.png`, `pdp-start-header-pressed.png`.

#### pdp-dash-link

Dashboard link. The faded "Dashboard" nav link beside the menu button; measured, never followed (the dashboard needs an account).

Page: create-pdp. Selector: `a[href="/"] "Dashboard"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 61 x 24 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 16px/24px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Text node | span.text-xs.whitespace-nowrap: sfProFont 12px/16px 400, #ffffff | = | = | = |
| Transition | opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Opacity | 0.3 | = | = | - |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-dash-link-default.png`, `pdp-dash-link-hover.png`, `pdp-dash-link-focus-visible.png`, `pdp-dash-link-pressed.png`.

#### pdp-visuals-h

Your visuals heading. The left rail's "Your visuals" section heading.

Page: create-pdp. Selector: `create-pdp h2 "Your visuals"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 432 x 70 |
| Padding | 0px 24px |
| Border | T: none; R: none; B: 1px solid #020108; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sfProFont 22px/34.2222px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | h2.text-m.md:text-lg 432.0x70.0 border B:1px solid #020108 |
| Ancestor paint | 1 up div.rounded-[20px].flex bg #111111 |
| How | at rest |

Crops: `pdp-visuals-h-default.png`.

#### pdp-reco

Recommendations button. The small "Recommendations" trigger under Your visuals — a local UI toggle that opens the recommendations dialog; the opened state was measured after clicking it, then the dialog was closed with Escape.

Page: create-pdp. Selector: `"Recommendations" button`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 134 x 20 | = | = |
| Padding | 0px | = | = |
| Gap | 4px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | transparent | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sfProFont 14px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #686a6e | #ffffff | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 14 x 14, colour #686a6e | 14 x 14, colour #ffffff | = |
| How | at rest | mouse hover | own toggle |

Crops: `pdp-reco-default.png`, `pdp-reco-hover.png`, `pdp-reco-opened.png`.

#### pdp-reco-dialog

Recommendations dialog. The "What can I upload?" dialog opened by the Recommendations trigger — a rounded-4xl bg-base-750 panel over a blurred backdrop; measured, never submitted.

Page: create-pdp. Selector: `recommendations dialog panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 480 x 655.86 |
| Padding | 32px 48px |
| Border | none |
| Radius | 28px |
| Background | #1e1e1e |
| Box shadow | none |
| Outline | none |
| Font | sfProFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | h2.text-center.text-lg: sfProFont 32px/44.8px 400, #ffffff, ls -0.4px |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 18 x 18, colour #ffffff |
| Painted layers | div.relative.w-full 480.0x655.9 bg #1e1e1e r 28px; div.mt-4.rounded-2xl 384.0x218.1 bg #31cb4b @ 0.05 border T:1px solid #31cb4b @ 0.2 / R:1px solid #31cb4b @ 0.2 / B:1px solid #31cb4b @ 0.2 / L:1px solid #31cb4b @ 0.2 r 16px; div.relative.aspect-43/50 115.3x134.1 bg #202020 r 8px; div.relative.aspect-43/50 115.3x134.1 bg #202020 r 8px; div.relative.aspect-43/50 115.3x134.1 bg #202020 r 8px; div.mt-2.rounded-2xl 384.0x218.1 bg #f63c34 @ 0.05 border T:1px solid #f63c34 @ 0.2 / R:1px solid #f63c34 @ 0.2 / B:1px solid #f63c34 @ 0.2 / L:1px solid #f63c34 @ 0.2 r 16px |
| How | at rest |

Crops: `pdp-reco-dialog-default.png`.

#### pdp-upload

Upload button. The "Upload Main Image" button in the Your visuals rail; measured, never pressed (it would open the file picker).

Page: create-pdp. Selector: `"Upload Main Image" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 180 x 40 | = | = | = |
| Padding | 0px 24px 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 | #f94a00 | = | #f94a00 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #020108 | = | = | = |
| Text node | span.flex.items-center: sfProFont 14px/20px 400, #020108 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #020108 | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 180.0x40.0 bg #ff6b02 r 3.35544e+07px | button.cursor-pointer.transition-colors 180.0x40.0 bg #f94a00 r 3.35544e+07px | = | button.cursor-pointer.transition-colors 180.0x40.0 bg #f94a00 r 3.35544e+07px |
| Ancestor paint | 1 up div.bg-base-700.rounded-2xl bg #1a1a1a | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-upload-default.png`, `pdp-upload-hover.png`, `pdp-upload-focus-visible.png`, `pdp-upload-pressed.png`.

#### pdp-add-product

Add product button. The "Add your product" button under the upload slot; measured, never pressed.

Page: create-pdp. Selector: `"Add your product" button`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 165 x 40 | = | = | = |
| Padding | 0px 24px 0px 12px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 @ 0.2 | = | = | #ff6b02 @ 0.35 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff6b02 | = | = | = |
| Text node | span.flex.items-center: sfProFont 14px/20px 400, #ff6b02 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Icon | 16 x 16, colour #ff6b02 | = | = | = |
| Painted layers | button.cursor-pointer.transition-colors 165.0x40.0 bg #ff6b02 @ 0.2 r 3.35544e+07px | = | = | button.cursor-pointer.transition-colors 165.0x40.0 bg #ff6b02 @ 0.35 r 3.35544e+07px |
| Ancestor paint | 1 up div.bg-base-700.rounded-2xl bg #1a1a1a | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-add-product-default.png`, `pdp-add-product-hover.png`, `pdp-add-product-focus-visible.png`, `pdp-add-product-pressed.png`.

#### pdp-shopify-h

Shopify banner heading. The "Connect your Shopify store" banner heading.

Page: create-pdp. Selector: `create-pdp h2 "Connect your Shopify store" (painted copy)`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 591 x 22.84 |
| Padding | 0px 112px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sfProFont 16px/22.8571px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `pdp-shopify-h-default.png`.

#### pdp-shopify-cta

Check connection pill. The accent "Check connection" pill linking to /shopify-integration — the only painted accent surface on the signed-out page; measured, never followed.

Page: create-pdp. Selector: `a[href="/shopify-integration"] "Check connection" (painted copy)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 152 x 40 | = | = | = |
| Padding | 0px 20px | = | = | = |
| Border | none | = | = | = |
| Radius | 3.35544e+07px | = | = | = |
| Background | #ff6b02 @ 0.2 | #ff6b02 @ 0.35 | = | #ff6b02 @ 0.35 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | sfProFont 14px/20px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ff6b02 | = | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.shrink-0.self-start 152.0x40.0 bg #ff6b02 @ 0.2 r 3.35544e+07px | a.shrink-0.self-start 152.0x40.0 bg #ff6b02 @ 0.35 r 3.35544e+07px | = | a.shrink-0.self-start 152.0x40.0 bg #ff6b02 @ 0.35 r 3.35544e+07px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `pdp-shopify-cta-default.png`, `pdp-shopify-cta-hover.png`, `pdp-shopify-cta-focus-visible.png`, `pdp-shopify-cta-pressed.png`.

#### pdp-adjust-h

Adjust-look heading. The "Adjust look" section heading that carries the "What's a PDP" trigger.

Page: create-pdp. Selector: `create-pdp h2 "Adjust look"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 639 x 70 |
| Padding | 0px 24px |
| Border | T: none; R: none; B: 1px solid #020108; L: none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sfProFont 22px/34.2222px 500 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Icon | 16 x 16, colour #ffffff |
| Painted layers | h2.text-m.md:text-lg 639.0x70.0 border B:1px solid #020108; button.cursor-pointer.transition-colors 132.0x32.0 bg #1a1a1a r 3.35544e+07px |
| Ancestor paint | 1 up div.flex.h-auto bg #111111 |
| How | at rest |

Crops: `pdp-adjust-h-default.png`.

#### pdp-what

What's-a-PDP button. The pill-shaped "What's a PDP" explainer trigger — a local UI toggle that opens the PDP explainer dialog; the opened state was measured after clicking it, then the dialog was closed with Escape.

Page: create-pdp. Selector: `"What's a PDP" button`. States: default, hover, opened.

| Property | default | hover | opened |
|---|---|---|---|
| Size (w x h) | 132 x 32 | = | = |
| Padding | 0px 12px | = | = |
| Border | none | = | = |
| Radius | 3.35544e+07px | = | = |
| Background | #1a1a1a | #ffffff @ 0.15 | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | sfProFont 14px/20px 500 | = | = |
| Letter spacing | normal | = | = |
| Colour | #ffffff @ 0.65 | = | = |
| Text node | span: sfProFont 14px/20px 500, #ffffff @ 0.65 | = | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | = |
| Cursor | pointer | = | = |
| Icon | 16 x 16, colour #ffffff | = | = |
| Painted layers | button.cursor-pointer.transition-colors 132.0x32.0 bg #1a1a1a r 3.35544e+07px | button.cursor-pointer.transition-colors 132.0x32.0 bg #ffffff @ 0.15 r 3.35544e+07px | = |
| How | at rest | mouse hover | own toggle |

Crops: `pdp-what-default.png`, `pdp-what-hover.png`, `pdp-what-opened.png`.

#### pdp-what-dialog

PDP explainer dialog. The dialog opened by the "What's a PDP" trigger; measured, never submitted.

Page: create-pdp. Selector: `PDP explainer dialog panel`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 880 x 448.38 |
| Padding | 24px |
| Border | none |
| Radius | 28px |
| Background | #1e1e1e |
| Box shadow | none |
| Outline | none |
| Font | sfProFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | span.inline-flex.h-6: sfProFont 14px/14px 500, #ff6b02 |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.2s cubic-bezier(0, 0, 0.2, 1) |
| Icon | 18 x 18, colour #ffffff |
| Painted layers | div.relative.w-full 880.0x448.4 bg #1e1e1e r 28px; span.inline-flex.h-6 52.0x24.0 bg #ff6b02 @ 0.2 r 3.35544e+07px |
| How | at rest |

Crops: `pdp-what-dialog-default.png`.

#### pdp-signedin-chip

Requirement chip. A small "Signed in" status chip in the requirements area; measured, never pressed.

Page: create-pdp. Selector: `"Signed in" chip`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 62 x 25 | = |
| Padding | 0px | = |
| Border | T: none; R: none; B: 1px solid #f94a00 @ 0.65; L: none | T: none; R: none; B: 1px solid #f94a00; L: none |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sfProFont 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #f94a00 @ 0.65 | #f94a00 |
| Text node | span.flex.items-center: sfProFont 16px/24px 400, #f94a00 @ 0.65 | span.flex.items-center: sfProFont 16px/24px 400, #f94a00 |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Cursor | pointer | = |
| Painted layers | button.cursor-pointer.transition-colors 62.0x25.0 border B:1px solid #f94a00 @ 0.65 | button.cursor-pointer.transition-colors 62.0x25.0 border B:1px solid #f94a00 |
| How | at rest | mouse hover |

Crops: `pdp-signedin-chip-default.png`, `pdp-signedin-chip-hover.png`.

#### pdp-start-bottom

Start generation (footer). The full-width "Start generation" submit at the foot of the form; measured, never pressed — it would queue a generation.

Page: create-pdp. Selector: `footer "Start generation" button (painted copy)`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 591 x 40 | = | - | = |
| Padding | 0px 12px | = | - | = |
| Border | none | = | - | = |
| Radius | 12px | = | - | = |
| Background | #ff6b02 @ 0.15 | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | sfProFont 14px/20px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #ff6b02 @ 0.15 | = | - | = |
| Text node | span.hidden.xs:inline: sfProFont 14px/20px 400, #ff6b02 @ 0.15 | = | - | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) | = | - | = |
| Painted layers | button.transition-colors.duration-200 591.0x40.0 bg #ff6b02 @ 0.15 r 12px | = | - | = |
| Ancestor paint | 1 up div.flex.h-auto bg #111111 | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `pdp-start-bottom-default.png`, `pdp-start-bottom-hover.png`, `pdp-start-bottom-pressed.png`.

#### pdp-format-group

Format radiogroup. The "Static content / Video content" radio pair under Adjust look — a local UI toggle; Video paints disabled signed out.

Page: create-pdp. Selector: `[role=radiogroup]`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 564 x 60 |
| Padding | 0px |
| Gap | 4px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | sfProFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | p.text-sm.leading-tight: sfProFont 14px/17.5px 400, #ff6b02 |
| Transition | none |
| Icon | 16 x 16, colour #ff6b02 |
| Painted layers | span.group.relative 280.0x60.0 bg #1a1a1a border T:2px solid #1a1a1a / R:2px solid #1a1a1a / B:2px solid #1a1a1a / L:2px solid #1a1a1a r 16px; div.flex.w-full 260.0x56.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; div.h-full.aspect-square 52.0x52.0 bg #020108 @ 0.3 r 12px; div.size-4.rounded-full 16.0x16.0 bg #ff6b02 @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px; div::after.size-4.rounded-full 6pxx6px bg #ff6b02 r 3.35544e+07px; span.group.relative 280.0x60.0 bg #1a1a1a border T:2px solid #1a1a1a / R:2px solid #1a1a1a / B:2px solid #1a1a1a / L:2px solid #1a1a1a r 16px |
| How | at rest |

Crops: `pdp-format-group-default.png`.

#### pdp-format-static

Format radio (Static). The "Static content" radio — the checked default; measured, never changed.

Page: create-pdp. Selector: `[role=radio] "Static content"`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 280 x 60 | = |
| Padding | 0px 16px 0px 0px | = |
| Border | 2px solid #1a1a1a | = |
| Radius | 16px | = |
| Background | #1a1a1a | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | sfProFont 16px/24px 400 | = |
| Letter spacing | normal | = |
| Colour | #ff6b02 | = |
| Text node | p.text-sm.leading-tight: sfProFont 14px/17.5px 400, #ff6b02 | = |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) | = |
| Icon | 16 x 16, colour #ff6b02 | = |
| Painted layers | span.group.relative 280.0x60.0 bg #1a1a1a border T:2px solid #1a1a1a / R:2px solid #1a1a1a / B:2px solid #1a1a1a / L:2px solid #1a1a1a r 16px; div.flex.w-full 260.0x56.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; div.h-full.aspect-square 52.0x52.0 bg #020108 @ 0.3 r 12px; div.size-4.rounded-full 16.0x16.0 bg #ff6b02 @ 0.2 border T:1px solid #000000 @ 0 / R:1px solid #000000 @ 0 / B:1px solid #000000 @ 0 / L:1px solid #000000 @ 0 r 3.35544e+07px; div::after.size-4.rounded-full 6pxx6px bg #ff6b02 r 3.35544e+07px | = |
| How | at rest | mouse hover |

Crops: `pdp-format-static-default.png`, `pdp-format-static-hover.png`.

#### pdp-format-video

Format radio (Video, disabled). The "Video content" radio — painted disabled (data-disabled, 0.5 opacity) for signed-out visitors; measured, never pressed.

Page: create-pdp. Selector: `[role=radio] "Video content"`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 280 x 60 |
| Padding | 0px 16px 0px 0px |
| Border | 2px solid #1a1a1a |
| Radius | 16px |
| Background | #1a1a1a |
| Box shadow | none |
| Outline | none |
| Font | sfProFont 16px/24px 400 |
| Letter spacing | normal |
| Colour | #b0b4ba |
| Text node | p.text-sm.leading-tight: sfProFont 14px/17.5px 400, #b0b4ba |
| Transition | color, background-color, border-color, outline-color, -webkit-text-decoration-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter, display, content-visibility, overlay, pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| Opacity | 0.5 |
| Icon | 16 x 16, colour #b0b4ba |
| Painted layers | span.group.relative 280.0x60.0 bg #1a1a1a border T:2px solid #1a1a1a / R:2px solid #1a1a1a / B:2px solid #1a1a1a / L:2px solid #1a1a1a r 16px; div.flex.w-full 260.0x56.0 border T:2px solid #000000 @ 0 / R:2px solid #000000 @ 0 / B:2px solid #000000 @ 0 / L:2px solid #000000 @ 0; div.h-full.aspect-square 52.0x52.0 bg #020108 @ 0.3 r 12px; div.size-4.rounded-full 16.0x16.0 bg #ffffff @ 0.1 border T:1px solid #ffffff @ 0.1 / R:1px solid #ffffff @ 0.1 / B:1px solid #ffffff @ 0.1 / L:1px solid #ffffff @ 0.1 r 3.35544e+07px |
| How | at rest |

Crops: `pdp-format-video-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The phone header at 390 wide: logo, the Menu pill with the theme toggle and the Get started pill.

Page: mobile. Selector: `mobile .header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 104.11 |
| Padding | 19.3484px 16.1237px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 3.9px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.header__menu-txt.u-btn: Sf Pro Display 17.1314px/20.5577px 400, #ffffff, ls -0.342629px |
| Transition | all 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 58.84 x 56.42, colour #020108 |
| Painted layers | div.header__main 249.8x48.4 bg #020108 r 1596.25px; div.header__menu-line.is-top 26.6x1.0 bg #ffffff; div.header__menu-line.is-bottom 26.6x1.0 bg #ffffff; div.header__theme 32.2x32.2 border T:1px solid #ffffff @ 0.2 / R:1px solid #ffffff @ 0.2 / B:1px solid #ffffff @ 0.2 / L:1px solid #ffffff @ 0.2 r 1596.25px; div.header__prc 58.0x32.2 bg #ffffff @ 0.2 r 1596.25px; a.header_signin.is-header-btn 0.0x0.0 bg #d9d9d9 border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 32.2474px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-menu-pill

Mobile menu pill. The "Menu" pill at 390 wide — a local UI toggle that opens the nav overlay; the opened state was measured after clicking it, then closed.

Page: mobile. Selector: `mobile .header__menu`. States: default, hover, focus-visible, pressed, opened.

| Property | default | hover | focus-visible | pressed | opened |
|---|---|---|---|---|---|
| Size (w x h) | 95.08 x 42.69 | = | - | = | = |
| Padding | 8.06185px 0px 8.06185px 8.06185px | = | - | = | = |
| Gap | 12.0928px | = | - | = | = |
| Border | none | = | - | = | = |
| Radius | 0px | = | - | = | = |
| Background | transparent | = | - | = | = |
| Box shadow | none | = | - | = | = |
| Outline | none | = | - | = | = |
| Font | Arial 3.9px/20px 400 | = | - | = | = |
| Letter spacing | normal | = | - | = | = |
| Colour | #333333 | = | - | = | = |
| Text node | div.header__menu-txt.u-btn: Sf Pro Display 17.1314px/20.5577px 400, #ffffff, ls -0.342629px | = | - | = | = |
| Transition | opacity 0.2s ease | = | - | = | = |
| Cursor | pointer | = | - | = | = |
| Painted layers | div.header__menu-line.is-top 26.6x1.0 bg #ffffff; div.header__menu-line.is-bottom 26.6x1.0 bg #ffffff | = | - | = | div.header__menu-line.is-top 19.5x19.5 bg #ffffff; div.header__menu-line.is-bottom 19.5x19.5 bg #ffffff |
| Ancestor paint | 1 up div.header__main bg #020108 | = | - | = | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover | own toggle |
| Opacity | - | 0.64 | = | 0.64 | 0.64 |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = | = |

Crops: `m-menu-pill-default.png`, `m-menu-pill-hover.png`, `m-menu-pill-pressed.png`, `m-menu-pill-opened.png`.

#### m-nav-overlay

Mobile nav overlay. The nav overlay opened by the menu pill at 390 wide; its links were never followed.

Page: mobile. Selector: `mobile .menu (opened)`. States: opened.

| Property | opened |
|---|---|
| Size (w x h) | 390 x 499.7 |
| Padding | 12.0928px 10.4804px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Arial 3.9px/20px 400 |
| Letter spacing | normal |
| Colour | #333333 |
| Text node | div.menu__label.u-small-text-1: Sf Pro Display 12.0928px/18.1392px 400, #020108 @ 0.5, ls -0.120928px |
| Transition | all 0.2s ease |
| Transform | matrix(1, 0, 0, 1, 0, 0) |
| Icon | 24.17 x 24.17, colour #020108 |
| Painted layers | div.menu__wrap 258.5x487.6 bg #d9d9d9 r 32.2474px; div.menu__item.is-lined 234.0x117.3 border T:1px solid #020108 @ 0.2; a.btn-primary.u-btn 181.6x48.4 bg #020108 r 1596.25px; a.header_signin.w-inline-block 48.4x48.4 bg #d9d9d9 border T:1px solid #020108 @ 0.2 / R:1px solid #020108 @ 0.2 / B:1px solid #020108 @ 0.2 / L:1px solid #020108 @ 0.2 r 32.2474px |
| How | held open by an earlier toggle |

Crops: `m-nav-overlay-opened.png`.

#### m-hero-h1

Mobile hero headline. The masthead at 390 wide (u-h1 resolves to the mobile size).

Page: mobile. Selector: `mobile .hero__title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 286.22 x 75.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 40.3092px/37.8907px 400 |
| Letter spacing | -1.20928px |
| Colour | #020108 |
| Text node | span.hero-flash-word: Sf Pro Display 40.3092px/37.8907px 400, #020108, ls -1.20928px |
| Transition | none |
| How | at rest |

Crops: `m-hero-h1-default.png`.

#### m-step-cta

Mobile step CTA. A "Get started" button in the steps section at 390 wide; measured, never followed.

Page: mobile. Selector: `mobile a.btn-primary-stb`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 124.73 x 48.36 |
| Padding | 14.1082px 24.1855px |
| Border | none |
| Radius | 1596.25px |
| Background | #ffffff |
| Box shadow | none |
| Outline | none |
| Font | Sf Pro Display 17.1314px/20.5577px 400 |
| Letter spacing | -0.342629px |
| Colour | #020108 |
| Text node | div.char: Sf Pro Display 17.1314px/20.5577px 400, #020108, ls -0.342629px |
| Transition | all 0.2s ease |
| Cursor | pointer |
| Painted layers | a.btn-primary-stb.u-btn 124.7x48.4 bg #ffffff r 1596.25px |
| How | at rest |

Crops: `m-step-cta-default.png`.

#### m-faq-item

Mobile FAQ row. A FAQ accordion row at 390 wide; the opened state was measured after clicking, then re-closed.

Page: mobile. Selector: `mobile .faq__item`. States: default, opened.

| Property | default | opened |
|---|---|---|
| Size (w x h) | 357.78 x 94.69 | 357.78 x 125.53 |
| Padding | 20.1546px 0px 32.2474px 0px | = |
| Border | T: 1px solid #d7d7d6; R: none; B: 1px solid #d7d7d6; L: none | = |
| Radius | 0px | = |
| Background | transparent | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | Arial 3.9px/20px 400 | = |
| Letter spacing | normal | = |
| Colour | #333333 | = |
| Text node | div.faq__label.u-body-3: Sf Pro Display 16.1237px/20.1546px 500, #020108 | = |
| Transition | none | = |
| Painted layers | div.faq__item 357.8x94.7 border T:1px solid #d7d7d6 / B:1px solid #d7d7d6 | div.faq__item.active 357.8x125.5 border T:1px solid #d7d7d6 / B:1px solid #d7d7d6 |
| How | at rest | own toggle |

Crops: `m-faq-item-default.png`, `m-faq-item-opened.png`.

## Transitions declared in the readable stylesheets

fourmula.ai serves its CSS cross-origin from cdn.prod.website-files.com but readable to the page, and app.fourmula.ai serves _next/static chunks same-origin, so this list holds the transitions the readable sheets declare on each page; the per-state Transition rows above are computed values and cover every rule the page paints.

- auth: `background-color 5000s ease-in-out, box-shadow 5000s ease-in-out`

- create-pdp: `background-color 5000s ease-in-out, box-shadow 5000s ease-in-out`

- home: `unset`, `background-color 0.1s, color 0.1s`, `0.3s`, `0.2s`, `opacity 0.2s`, `background-color 0.1s`, `background-color 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`, `opacity 0.25s`

- start: `background-color 5000s ease-in-out, box-shadow 5000s ease-in-out`

## Reduced motion

- home (`a.btn-primary.is-header-btn` under prefers-reduced-motion): transition `0.2s`, animation `none 0s ease 0s 1 normal none running`, html scroll-behavior `auto`
