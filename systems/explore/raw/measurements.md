# Component measurements

Computed styles read from the archived explore.family build on 2026-11-14 by `tools/capture/public/measure.mjs`, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), and written here by `tools/capture/public/build-measurements.mjs` from [components-computed.json](components-computed.json). explore.family closed on 2023-04-19 and the domain lapsed, so every page was replayed from the local Internet Archive mirror (the 2023-02-23 product build plus archived API JSON and uploads; the `ssr` group is the server-rendered profile HTML the site sent crawlers, replayed with its scripts aborted). One table per component: a column per state, a row per property. A cell that repeats the first state's value reads `=`. Colours are hex, with `@ alpha` when translucent. "Painted layers" lists the first nodes inside the component that paint a fill, border, shadow or outline; "Ancestor paint" the same for its parents.

States: `hover` is a real pointer hover; `focus-visible` a real keyboard focus (Shift+Tab, Tab); `pressed` is forced with DevTools (`CSS.forcePseudoState` :active:hover), so no button was pressed; `focused` is a text field clicked into; `filled` is sample text typed and deleted again, with nothing sent; `opened`, `expanded` and the rest are resting states reached by the page or by a UI toggle.

## Components

### Auth forms

#### mkt-header

Site header. The fixed grey top bar: logo left, "Sign in" link and yellow "Sign up free" pill right.

Page: forgot. Selector: `header.header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 60 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #9d9d9d |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | a: UntitledSans 16px/22px 400, #ffffff |
| Transition | none |
| Icon | 0 x 0, colour #ffffff, fill #000000 |
| Painted layers | header.header 1440.0x60.0 bg #9d9d9d; a.btn.btn--auto 121.0x38.0 bg #ffc60a r 50px |
| How | at rest |

Crops: `mkt-header-default.png`.

#### mkt-logo

Logo. The Explore wordmark (inline svg) in the header, linking home.

Page: forgot. Selector: `.header__logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 27 x 31 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/0px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | color 0.2s ease |
| Transform | matrix(1, 0, 0, 1, -13.5, -15.5) |
| Cursor | pointer |
| Icon | 27 x 31, colour #ffffff, fill #000000 |
| How | at rest |

Crops: `mkt-logo-default.png`.

#### nav-signin

Sign in link. The "Sign in" header link; measured, never followed.

Page: forgot. Selector: `.header__auth-links a "Sign in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 52 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | UntitledSans 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 52.0x22.0 outline 1px auto #101010 offset 1px | = |

Crops: `nav-signin-default.png`, `nav-signin-hover.png`, `nav-signin-focus-visible.png`, `nav-signin-pressed.png`.

#### nav-signup

Sign up pill. The yellow "Sign up free" pill (btn--yellow btn--rounded btn--small); measured, never followed.

Page: forgot. Selector: `.header__auth-links a.btn--yellow`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121 x 38 | = | = | = |
| Padding | 9px 16px 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | #ffc60a | #ffcc24 | #ffcc24 | #ffcc24 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | UntitledSans 16px/19px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn--auto 121.0x38.0 bg #ffc60a r 50px | a.btn.btn--auto 121.0x38.0 bg #ffcc24 r 50px | a.btn.btn--auto 121.0x38.0 bg #ffcc24 r 50px | a.btn.btn--auto 121.0x38.0 bg #ffcc24 r 50px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `nav-signup-default.png`, `nav-signup-hover.png`, `nav-signup-focus-visible.png`, `nav-signup-pressed.png`.

#### auth-panel

Auth layout. The split auth screen: community welcome on the left, the form panel on the right.

Page: login. Selector: `.auth`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 900 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | span: UntitledSans 16px/22px 400, #c1c1c1 |
| Transition | none |
| Icon | 182 x 28, colour #262626, fill #000000 |
| Painted layers | div.auth__left 720.0x900.0 bg #717171; div.row.row--label 424.0x73.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.input 388.0x20.0 bg #ffffff; div.row.row--label 424.0x73.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.input 388.0x20.0 bg #ffffff; button.btn.btn--full 424.0x47.0 bg #262626 r 7px |
| How | at rest |

Crops: `auth-panel-default.png`.

#### auth-quote

Welcome quote. The left welcome panel: "Remember we are a community…" over the looping animation.

Page: login. Selector: `.auth__left`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 900 |
| Padding | 60px |
| Border | none |
| Radius | 0px |
| Background | #717171 |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | span: UntitledSans 16px/22px 400, #c1c1c1 |
| Transition | none |
| Painted layers | div.auth__left 720.0x900.0 bg #717171 |
| How | at rest |

Crops: `auth-quote-default.png`.

#### auth-logo

Auth logo. The Explore logo above the form.

Page: login. Selector: `.auth__logo`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 424 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | color 0.2s ease |
| Cursor | pointer |
| Icon | 182 x 28, colour #262626, fill #000000 |
| How | at rest |

Crops: `auth-logo-default.png`.

#### auth-heading

Auth heading. "Welcome back to Explore! / Log in to your account" — the form intro.

Page: login. Selector: `.auth__text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 330 x 50 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 21px/25px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `auth-heading-default.png`.

#### field-email

Email field. The Email input; focused and typed into then cleared — never submitted.

Page: login. Selector: `input.input (Email)`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 388 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | UntitledSans 16px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #262626 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #262626, opacity 1 | = | = |
| Painted layers | input.input 388.0x20.0 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `field-email-default.png`, `field-email-focused.png`, `field-email-filled.png`.

#### field-password

Password field. The Password input with the visibility eye; typed into and cleared, never submitted.

Page: login. Selector: `input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 388 x 20 | = | = |
| Padding | 0px 34px 0px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | UntitledSans 16px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #262626 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #9d9d9d, opacity 1 | = | = |
| Painted layers | input.input 388.0x20.0 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "hunter2example", then deleted; nothing sent |

Crops: `field-password-default.png`, `field-password-focused.png`, `field-password-filled.png`.

#### password-eye

Password visibility eye. The eye icon that toggles password visibility — a local UI toggle, pressed for nothing else.

Page: login. Selector: `.input-password .svg-eye`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 16 x 16 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #d0d0d0 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, 0, -8) |
| Cursor | pointer |
| Icon | 16 x 16, colour #d0d0d0, fill #000000 |
| How | at rest |

Crops: `password-eye-default.png`.

#### login-submit

Log in button. The full-width "Log in" submit (btn--full); states measured, never clicked — nothing was submitted.

Page: login. Selector: `button.btn "Log in"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 424 x 47 | = | = | = |
| Padding | 14px 25px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #262626 | #333333 | #333333 | #333333 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | UntitledSans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.btn--full 424.0x47.0 bg #262626 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `login-submit-default.png`, `login-submit-hover.png`, `login-submit-focus-visible.png`, `login-submit-pressed.png`.

#### forgot-link

Forgot password link. The "Forgot your password?" link under the submit; measured, never followed.

Page: login. Selector: `a.forgot-password`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 169 x 22 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | UntitledSans 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #9d9d9d | #262626 | #262626 | #262626 |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a.forgot-password 169.0x22.0 outline 1px auto #101010 offset 1px | = |

Crops: `forgot-link-default.png`, `forgot-link-hover.png`, `forgot-link-focus-visible.png`, `forgot-link-pressed.png`.

#### signup-link

Sign up link. The "Sign up free" link under the submit; measured, never followed.

Page: login. Selector: `.text-center a "Sign up free"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 89 x 19 | = | = | = |
| Padding | 0px | = | = | = |
| Border | none | = | = | = |
| Radius | 0px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | UntitledSans 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |
| Painted layers | - | = | a 89.0x19.0 outline 1px auto #101010 offset 1px | = |

Crops: `signup-link-default.png`, `signup-link-hover.png`, `signup-link-focus-visible.png`, `signup-link-pressed.png`.

#### reg-heading

Register heading. The sign-up form intro.

Page: register. Selector: `.auth__right .auth__text`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 900 |
| Padding | 60px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | label: UntitledSans 14px/17px 400, #9d9d9d |
| Transition | none |
| Icon | 182 x 28, colour #262626, fill #000000 |
| Painted layers | div.row.row--label 424.0x73.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.input 388.0x20.0 bg #ffffff; div.row.row--label 424.0x73.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.input 388.0x20.0 bg #ffffff; label::before 17pxx17px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 6px; button.btn.btn--full 424.0x47.0 bg #262626 r 7px |
| How | at rest |

Crops: `reg-heading-default.png`.

#### reg-field-email

Email field (register). The Email input; typed into and cleared, never submitted.

Page: register. Selector: `register input.input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 388 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | UntitledSans 16px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #262626 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #262626, opacity 1 | = | = |
| Painted layers | input.input 388.0x20.0 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `reg-field-email-default.png`, `reg-field-email-focused.png`, `reg-field-email-filled.png`.

#### reg-field-password

Password field (register). The Password input; typed into and cleared, never submitted.

Page: register. Selector: `register input[type=password]`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 388 x 20 | = | = |
| Padding | 0px 34px 0px 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | UntitledSans 16px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #262626 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #9d9d9d, opacity 1 | = | = |
| Painted layers | input.input 388.0x20.0 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "hunter2example", then deleted; nothing sent |

Crops: `reg-field-password-default.png`, `reg-field-password-focused.png`, `reg-field-password-filled.png`.

#### newsletter-check

Newsletter checkbox. The "Subscribe to newsletter (no spam…)" checkbox; measured, never toggled.

Page: register. Selector: `.input-checkbox`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 424 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #9d9d9d |
| Text node | label: UntitledSans 16px/28px 400, #9d9d9d |
| Transition | none |
| Painted layers | label::before 17pxx17px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 6px |
| How | at rest |

Crops: `newsletter-check-default.png`.

#### terms-line

Terms agreement line. "By clicking Sign up, I agree to Terms of Service and Privacy Policy."

Page: register. Selector: `register agreement line`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 424 x 92 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #9d9d9d |
| Text node | label: UntitledSans 16px/28px 400, #9d9d9d |
| Transition | none |
| Painted layers | label::before 17pxx17px border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 6px |
| How | at rest |

Crops: `terms-line-default.png`.

#### reg-submit

Sign up button. The "Sign up" submit; states measured, never clicked — nothing was submitted.

Page: register. Selector: `register "Sign up"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 424 x 47 | = | = | = |
| Padding | 14px 25px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #262626 | #333333 | #333333 | #333333 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | UntitledSans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.btn--full 424.0x47.0 bg #262626 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `reg-submit-default.png`, `reg-submit-hover.png`, `reg-submit-focus-visible.png`, `reg-submit-pressed.png`.

#### forgot-intro

Reset intro. "Please enter your email address and you will receive a link…"

Page: forgot. Selector: `forgot intro`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 720 x 900 |
| Padding | 60px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | div.auth__text: UntitledSans 21px/25px 400, #262626 |
| Transition | none |
| Icon | 182 x 28, colour #262626, fill #000000 |
| Painted layers | div.row.row--label 424.0x73.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 8px; input.input 388.0x20.0 bg #ffffff; button.btn.btn--full 424.0x47.0 bg #262626 r 7px |
| How | at rest |

Crops: `forgot-intro-default.png`.

#### forgot-field

Email field (reset). The Email input on the reset form; typed into and cleared, never submitted.

Page: forgot. Selector: `forgot input.input`. States: default, focused, filled.

| Property | default | focused | filled |
|---|---|---|---|
| Size (w x h) | 388 x 20 | = | = |
| Padding | 0px | = | = |
| Border | none | = | = |
| Radius | 0px | = | = |
| Background | #ffffff | = | = |
| Box shadow | none | = | = |
| Outline | none | = | = |
| Font | UntitledSans 16px/20px 400 | = | = |
| Letter spacing | normal | = | = |
| Colour | #262626 | = | = |
| Transition | none | = | = |
| Cursor | text | = | = |
| Placeholder | #262626, opacity 1 | = | = |
| Painted layers | input.input 388.0x20.0 bg #ffffff | = | = |
| How | at rest | clicked into the field | typed "name@example.com", then deleted; nothing sent |

Crops: `forgot-field-default.png`, `forgot-field-focused.png`, `forgot-field-filled.png`.

#### forgot-submit

Reset button. The "Reset Password" submit; states measured, never clicked.

Page: forgot. Selector: `forgot "Reset Password"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 424 x 47 | = | = | = |
| Padding | 14px 25px | = | = | = |
| Border | none | = | = | = |
| Radius | 7px | = | = | = |
| Background | #262626 | #333333 | #333333 | #333333 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | UntitledSans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | button.btn.btn--full 424.0x47.0 bg #262626 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px | button.btn.btn--full 424.0x47.0 bg #333333 r 7px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `forgot-submit-default.png`, `forgot-submit-hover.png`, `forgot-submit-focus-visible.png`, `forgot-submit-pressed.png`.

### Home (marketing + feed)

#### hero

Hero section. The home hero: "Welcome" greeting, the positioning sentence and the feature tags, over the testimonial imagery.

Page: home. Selector: `section.section--hero .hero`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 680 |
| Padding | 0px |
| Border | T: 1px solid #b7b7b7; R: none; B: none; L: none |
| Radius | 0px |
| Background | #9d9d9d |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.hero__welcome: UntitledSans 16px/22px 400, #e0e0e0 |
| Transition | none |
| Painted layers | section.section.section--hero 1440.0x680.0 bg #9d9d9d border T:1px solid; div.testimonial 446.7x230.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.testimonial 446.7x230.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.testimonial 446.7x230.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.hero__tag.hide-mobile 82.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.hero__tag.hide-mobile 96.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px |
| How | at rest |

Crops: `hero-default.png`.

#### hero-welcome

Hero greeting. The "Welcome" greeting at the top of the hero.

Page: home. Selector: `.hero__welcome`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1400 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #e0e0e0 |
| Transition | none |
| How | at rest |

Crops: `hero-welcome-default.png`.

#### hero-title

Hero headline. "Explore is an emotionally intelligent ad-free social media platform…" — the display sentence.

Page: home. Selector: `.hero__title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1082 x 123 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | LabilGrotesk-Medium 40px/41px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| How | at rest |

Crops: `hero-title-default.png`.

#### hero-tag

Hero tag. A feature tag in the hero tag list (Free / For creatives / No ads…).

Page: home. Selector: `.hero__tag`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 82 x 46 |
| Padding | 11px 23px |
| Border | 1px solid #b7b7b7 |
| Radius | 7px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSansMedium 16px/22px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Transition | none |
| Painted layers | div.hero__tag.hide-mobile 82.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px |
| How | at rest |

Crops: `hero-tag-default.png`.

#### hero-tag-cta

Hero tag CTA. The "All features" tag link; measured, never followed.

Page: home. Selector: `a.hero__tag`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 137 x 46 | = | = | = |
| Padding | 11px 23px | = | = | = |
| Border | 1px solid #b7b7b7 | = | = | = |
| Radius | 7px | = | = | = |
| Background | transparent | = | = | = |
| Box shadow | none | = | = | = |
| Outline | none | = | 1px auto #101010 offset 1px | = |
| Font | UntitledSansMedium 16px/22px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #ffffff | = | = | = |
| Transition | color 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.hero__tag 137.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px | = | a.hero__tag 137.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px outline 1px auto #101010 offset 1px | = |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `hero-tag-cta-default.png`, `hero-tag-cta-hover.png`, `hero-tag-cta-focus-visible.png`, `hero-tag-cta-pressed.png`.

#### feed-section

Feed section. The post feed below the hero (the same card grid as /discover).

Page: home. Selector: `home .content--posts`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1440 x 679 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #ffffff |
| Text node | div.hero__welcome: UntitledSans 16px/22px 400, #e0e0e0 |
| Transition | none |
| Painted layers | div.testimonial 446.7x230.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.testimonial 446.7x230.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.testimonial 446.7x230.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.hero__tag.hide-mobile 82.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.hero__tag.hide-mobile 96.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px; div.hero__tag.hide-mobile 149.0x46.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 7px |
| Ancestor paint | 1 up section.section.section--hero bg #9d9d9d |
| How | at rest |

Crops: `feed-section-default.png`.

### Discover feed

#### discover-title

Discover heading. "Browse inspiring work on Explore curated by our team" — the page heading above the feed.

Page: discover. Selector: `.discover__title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 300 x 44 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #9d9d9d |
| Transition | none |
| How | at rest |

Crops: `discover-title-default.png`.

#### pill-row

Category pill row. The scrollable category pills row (All / 3D Design / Animation / Art…).

Page: discover. Selector: `.discover__categories .pills`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1000 x 90 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | a.pill.selected: UntitledSans 16px/21px 400, #262626 |
| Transition | none |
| Painted layers | a.pill.selected 47.0x36.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 20px; a.pill 106.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px; a.pill 106.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px; a.pill 51.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px; a.pill 123.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px; a.pill 98.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px |
| How | at rest |

Crops: `pill-row-default.png`.

#### pill

Category pill (active). The selected "All" category pill; measured, never followed.

Page: discover. Selector: `a.pill "All"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 47 x 36 | = | - | = |
| Padding | 5px 12px 6px 12px | = | - | = |
| Border | 2px solid #262626 | = | - | = |
| Radius | 20px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | UntitledSans 16px/21px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #262626 | = | - | = |
| Transition | color 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.pill.selected 47.0x36.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 20px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `pill-default.png`, `pill-hover.png`, `pill-pressed.png`.

#### pill-idle

Category pill. An unselected category pill; measured, never followed.

Page: discover. Selector: `a.pill "Animation"`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 106 x 36 | = | - | = |
| Padding | 6px 13px 7px 13px | = | - | = |
| Border | 1px solid #efefef | = | - | = |
| Radius | 20px | = | - | = |
| Background | transparent | = | - | = |
| Box shadow | none | = | - | = |
| Outline | none | = | - | = |
| Font | UntitledSans 16px/21px 400 | = | - | = |
| Letter spacing | normal | = | - | = |
| Colour | #262626 | = | - | = |
| Transition | color 0.2s ease | = | - | = |
| Cursor | pointer | = | - | = |
| Painted layers | a.pill 106.0x36.0 border T:1px solid / R:1px solid / B:1px solid / L:1px solid r 20px | = | - | = |
| How | at rest | mouse hover | - | CDP forcePseudoState :active:hover |
| Skipped | - | = | focus failed: keyboard focus did not reach the element | = |

Crops: `pill-idle-default.png`, `pill-idle-hover.png`, `pill-idle-pressed.png`.

#### post-card

Post card. A feed post card: gallery tile on top, author row and title below.

Page: discover. Selector: `.post`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 476 x 488.5 |
| Padding | 0px 15px 50px 15px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | a: UntitledSansMedium 16px/22px 400, #262626 |
| Transition | opacity 0.2s ease |
| Icon | 22 x 8, colour #ffffff, fill #000000 |
| Painted layers | div.media.media--image 446.0x334.5 bg #5a5958; div::after 446pxx334.5px bg #000000 @ 0.02; div.pro-badge 37.0x20.0 bg #262626 r 30px |
| How | at rest |

Crops: `post-card-default.png`.

#### post-gallery

Post gallery. The media tile of a feed card (post__gallery--rounded); images or a video poster.

Page: discover. Selector: `.post__gallery`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 446 x 334.5 |
| Padding | 0px |
| Border | none |
| Radius | 7px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| Cursor | pointer |
| Painted layers | div.media.media--image 446.0x334.5 bg #5a5958; div::after 446pxx334.5px bg #000000 @ 0.02 |
| How | at rest |

Crops: `post-gallery-default.png`.

#### post-author

Post author row. The author line under a card: avatar, name, age ("4yr").

Page: discover. Selector: `.post__author`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 446 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | a: UntitledSansMedium 16px/22px 400, #262626 |
| Transition | none |
| Icon | 22 x 8, colour #ffffff, fill #000000 |
| Painted layers | div.pro-badge 37.0x20.0 bg #262626 r 30px |
| How | at rest |

Crops: `post-author-default.png`.

#### post-avatar

Author avatar. The round author avatar on a feed card (post__author-image--blank when empty).

Page: discover. Selector: `.post__author-image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 28 x 28 |
| Padding | 0px |
| Border | none |
| Radius | 34px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSansMedium 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| Cursor | pointer |
| How | at rest |

Crops: `post-avatar-default.png`.

#### post-title

Post title. The work title under a card.

Page: discover. Selector: `.post__content`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 446 x 22 |
| Padding | 0px 30px 0px 41px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `post-title-default.png`.

#### post-actions

Post actions. The action icon row on a card (appreciate/save/comment affordances).

Page: discover. Selector: `.post__actions`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 458 x 30 |
| Padding | 0px 0px 0px 41px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| Icon | 16 x 16, colour #9d9d9d, fill #000000 |
| How | at rest |

Crops: `post-actions-default.png`.

#### carousel-next

Carousel next arrow. The next-arrow on a multi-image post carousel.

Page: discover. Selector: `button.VueCarousel-navigation-next`. States: default, hover.

| Property | default | hover |
|---|---|---|
| Size (w x h) | 24 x 24 | = |
| Padding | 8px | = |
| Border | none | = |
| Radius | 24px | = |
| Background | #717171 @ 0.3 | = |
| Box shadow | none | = |
| Outline | none | = |
| Font | system 13.3333px/normal 400 | = |
| Letter spacing | normal | = |
| Colour | #ffffff | = |
| Transition | none | = |
| Cursor | pointer | = |
| Icon | 8 x 11, colour #ffffff, fill #000000 | = |
| Painted layers | button.VueCarousel-navigation-button.VueCarousel-navigation-next 24.0x24.0 bg #717171 @ 0.3 r 24px | = |
| How | at rest | mouse hover |

Crops: `carousel-next-default.png`, `carousel-next-hover.png`.

### About / legal

#### about-title

About headline. The about page masthead sentence.

Page: about. Selector: `.title`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 1082 x 161 |
| Padding | 35px 0px 0px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | LabilGrotesk-Medium 41px/42px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `about-title-default.png`.

#### feature

Feature card. A feature block ("Perfectly simple", "Community not numbers"…).

Page: about. Selector: `.feature`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 511 x 371 |
| Padding | 24px 40px 38px 40px |
| Border | none |
| Radius | 7px |
| Background | #f4f4f4 |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 18px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | div: LabilGrotesk-Medium 41px/42px 400, #262626 |
| Transition | none |
| Painted layers | div.feature 511.0x371.0 bg #f4f4f4 r 7px |
| How | at rest |

Crops: `feature-default.png`.

#### about-copy

About statement. "We are building Explore as it should be built…" — the statement copy.

Page: about. Selector: `.about`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 484 x 588 |
| Padding | 140px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | span: UntitledSans 16px/22px 400, #262626 |
| Transition | none |
| How | at rest |

Crops: `about-copy-default.png`.

#### about-cta

About CTA. "Sign up — No bank card required" in the closing section; measured, never followed.

Page: about. Selector: `.section--cta a.btn-submit`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 294 x 47 | = | = | = |
| Padding | 14px 25px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | #ffc60a | #ffcc24 | #ffcc24 | #ffcc24 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | UntitledSans 16px/normal 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn-submit 294.0x47.0 bg #ffc60a r 50px | a.btn.btn-submit 294.0x47.0 bg #ffcc24 r 50px | a.btn.btn-submit 294.0x47.0 bg #ffcc24 r 50px | a.btn.btn-submit 294.0x47.0 bg #ffcc24 r 50px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `about-cta-default.png`, `about-cta-hover.png`, `about-cta-focus-visible.png`, `about-cta-pressed.png`.

#### footer

Footer. The grey closing footer: typeface credits and site links.

Page: about. Selector: `.footer`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 990 x 585 |
| Padding | 130px 0px 175px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | div.footer__column: UntitledSans 18px/28px 400, #262626 |
| Transition | none |
| How | at rest |

Crops: `footer-default.png`.

#### footer-column

Footer column. One footer column (Typefaces credits: Labil Grotesk / Untitled Sans…).

Page: about. Selector: `.footer__column`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 155 x 280 |
| Padding | 0px 20px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 18px/28px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `footer-column-default.png`.

#### legal-title

Legal heading. The page heading on the code of conduct.

Page: legal. Selector: `legal h1`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 21px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `legal-title-default.png`.

#### legal-body

Legal body. Body copy on a legal page (the same type treatment as /terms and /privacy).

Page: legal. Selector: `legal body`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 760 x 42 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/21px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `legal-body-default.png`.

### Server-rendered profile

#### ssr-profile

SSR profile. The server-rendered profile page (Malika Favre): name, avatar placeholder and the post grid the crawler received.

Page: ssr. Selector: `SSR .profile`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 842 x 3092.78 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | div.profile__name: UntitledSans 21px/22px 400, #262626 |
| Transition | none |
| Painted layers | div.profile__left 396.0x396.0 bg #f8f8f8 r 5px; div.profile__cover 396.0x396.0 bg #eaeaea; div.profile__image 142.0x142.0 bg #3a3a3a r 150px; div::after 28.1562pxx14.0781px bg #000000 @ 0.02; div.post__author-image 17.7x28.0 bg #9d9d9d r 34px; div::after 28.1562pxx14.0781px bg #000000 @ 0.02 |
| How | at rest |

Crops: `ssr-profile-default.png`.

#### ssr-avatar

SSR profile avatar. The profile image slot; the avatar file itself was never archived, so it reads as its placeholder.

Page: ssr. Selector: `SSR .profile__image`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 142 x 142 |
| Padding | 0px |
| Border | none |
| Radius | 150px |
| Background | #3a3a3a |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| Transform | matrix(1, 0, 0, 1, -71, -71) |
| Painted layers | div.profile__image 142.0x142.0 bg #3a3a3a r 150px |
| Ancestor paint | 1 up div.profile__left bg #f8f8f8 |
| How | at rest |

Crops: `ssr-avatar-default.png`.

#### ssr-name

SSR profile name. The display name on the server-rendered profile.

Page: ssr. Selector: `SSR .profile__name`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 396 x 22 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 21px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| How | at rest |

Crops: `ssr-name-default.png`.

#### ssr-post

SSR post tile. A post tile in the server-rendered feed; its video/poster media was never archived, so it paints the empty placeholder.

Page: ssr. Selector: `SSR .post`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 58.16 x 264.08 |
| Padding | 0px 15px 50px 15px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | a: UntitledSansMedium 16px/22px 400, #262626 |
| Transition | none |
| Painted layers | div::after 28.1562pxx14.0781px bg #000000 @ 0.02; div.post__author-image 17.7x28.0 bg #9d9d9d r 34px |
| How | at rest |

Crops: `ssr-post-default.png`.

#### ssr-gallery

SSR post gallery. The media tile of a server-rendered post.

Page: ssr. Selector: `SSR .post__gallery`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 28.16 x 14.08 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | none |
| Painted layers | div::after 28.1562pxx14.0781px bg #000000 @ 0.02 |
| How | at rest |

Crops: `ssr-gallery-default.png`.

### Mobile (390 wide)

#### m-header

Mobile header. The fixed top bar at 390 wide.

Page: mobile. Selector: `mobile .header`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 56 |
| Padding | 0px |
| Border | none |
| Radius | 0px |
| Background | #9d9d9d |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | a.btn.btn--auto: UntitledSans 16px/19px 400, #262626 |
| Transition | none |
| Icon | 0 x 0, colour #ffffff, fill #000000 |
| Painted layers | header.header 390.0x56.0 bg #9d9d9d; a.btn.btn--auto 121.0x38.0 bg #ffc60a r 50px |
| How | at rest |

Crops: `m-header-default.png`.

#### m-signup

Mobile sign up pill. The header "Sign up free" pill at 390 wide.

Page: mobile. Selector: `mobile .btn--yellow`. States: default, hover, focus-visible, pressed.

| Property | default | hover | focus-visible | pressed |
|---|---|---|---|---|
| Size (w x h) | 121 x 38 | = | = | = |
| Padding | 9px 16px 10px 16px | = | = | = |
| Border | none | = | = | = |
| Radius | 50px | = | = | = |
| Background | #ffc60a | #ffcc24 | #ffcc24 | #ffcc24 |
| Box shadow | none | = | = | = |
| Outline | none | = | = | = |
| Font | UntitledSans 16px/19px 400 | = | = | = |
| Letter spacing | normal | = | = | = |
| Colour | #262626 | = | = | = |
| Transition | all 0.2s ease | = | = | = |
| Cursor | pointer | = | = | = |
| Painted layers | a.btn.btn--auto 121.0x38.0 bg #ffc60a r 50px | a.btn.btn--auto 121.0x38.0 bg #ffcc24 r 50px | a.btn.btn--auto 121.0x38.0 bg #ffcc24 r 50px | a.btn.btn--auto 121.0x38.0 bg #ffcc24 r 50px |
| How | at rest | mouse hover | Shift+Tab, Tab | CDP forcePseudoState :active:hover |

Crops: `m-signup-default.png`, `m-signup-hover.png`, `m-signup-focus-visible.png`, `m-signup-pressed.png`.

#### m-pill

Mobile category pill. A category pill in the horizontally scrolling row at 390 wide.

Page: mobile. Selector: `mobile a.pill`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 47 x 36 |
| Padding | 5px 12px 6px 12px |
| Border | 2px solid #262626 |
| Radius | 20px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/21px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Transition | color 0.2s ease |
| Cursor | pointer |
| Painted layers | a.pill.selected 47.0x36.0 border T:2px solid / R:2px solid / B:2px solid / L:2px solid r 20px |
| How | at rest |

Crops: `m-pill-default.png`.

#### m-post

Mobile post card. A feed card at 390 wide.

Page: mobile. Selector: `mobile .post`. States: default.

| Property | default |
|---|---|
| Size (w x h) | 390 x 448.5 |
| Padding | 0px 0px 40px 0px |
| Border | none |
| Radius | 0px |
| Background | transparent |
| Box shadow | none |
| Outline | none |
| Font | UntitledSans 16px/22px 400 |
| Letter spacing | normal |
| Colour | #262626 |
| Text node | a: UntitledSansMedium 16px/22px 400, #262626 |
| Transition | opacity 0.2s ease |
| Icon | 22 x 8, colour #ffffff, fill #000000 |
| Painted layers | div.media.media--image 390.0x292.5 bg #5a5958; div::after 390pxx292.5px bg #000000 @ 0.02; div.pro-badge 37.0x20.0 bg #262626 r 30px |
| How | at rest |

Crops: `m-post-default.png`.

## Transitions declared in the readable stylesheets

Explore ships one compiled stylesheet (app.4ef09b07.css) and one Vue app bundle; this list holds every transition/animation declaration the CSSOM could read on each replayed page. The per-state Transition rows above are the computed values.

- about: `0.35s`, `0.2s`, `color 0.2s`, `opacity 0.5s`, `0.25s`, `transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), opacity 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), -webkit-transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93)`, `all var(--dnd-transition-duration)`, `all`, `var(--dnd-transition-duration)`, `opacity 0.2s`, `width 0.2s linear`, `0.15s`

- discover: `0.35s`, `0.2s`, `color 0.2s`, `opacity 0.5s`, `0.25s`, `transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), opacity 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), -webkit-transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93)`, `all var(--dnd-transition-duration)`, `all`, `var(--dnd-transition-duration)`, `opacity 0.2s`, `width 0.2s linear`, `0.15s`

- forgot: `0.35s`, `0.2s`, `color 0.2s`, `opacity 0.5s`, `0.25s`, `transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), opacity 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), -webkit-transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93)`, `all var(--dnd-transition-duration)`, `all`, `var(--dnd-transition-duration)`, `opacity 0.2s`, `width 0.2s linear`, `0.15s`

- home: `0.35s`, `0.2s`, `color 0.2s`, `opacity 0.5s`, `0.25s`, `transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), opacity 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), -webkit-transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93)`, `all var(--dnd-transition-duration)`, `all`, `var(--dnd-transition-duration)`, `opacity 0.2s`, `width 0.2s linear`, `0.15s`

- login: `0.35s`, `0.2s`, `color 0.2s`, `opacity 0.5s`, `0.25s`, `transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), opacity 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), -webkit-transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93)`, `all var(--dnd-transition-duration)`, `all`, `var(--dnd-transition-duration)`, `opacity 0.2s`, `width 0.2s linear`, `0.15s`

- register: `0.35s`, `0.2s`, `color 0.2s`, `opacity 0.5s`, `0.25s`, `transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), opacity 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93), -webkit-transform 0.5s cubic-bezier(0.3, 0.84, 0.46, 0.93)`, `all var(--dnd-transition-duration)`, `all`, `var(--dnd-transition-duration)`, `opacity 0.2s`, `width 0.2s linear`, `0.15s`
