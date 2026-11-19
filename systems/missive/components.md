# Components

Measured on the live signed-out DOM, 2026-11-19, light, 1440. Nothing was submitted. The password field was never filled. Hover is a real pointer. Focus on the email field is a real focus. Pressed states were not captured: a click on Try for free leaves for signup, and a click on Log in would submit.

## Navigation

### Wordmark

Selector: `a[href="/"] svg.missive-logo`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 144×36 CSS, crop includes padding | fill currentColor, ink #34363a `neutral.900` | at rest | [crop](components/crops/wordmark-default.png) |

### Nav link

Selector: `a.button-base.s-ghost` labelled Pricing. The first ghost link in the nav.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 70×44 | fill transparent, ink #34363a `neutral.900`, size 14px, weight 400, font Inter, radius 8px, padding 12px | at rest | [crop](components/crops/nav-login-default.png) |
| hover | 65×44 on Log in | fill #f5f6f6 `neutral.050` | mouse hover | [crop](components/crops/nav-login-hover.png) |

### Try for free

Selector: nav `a.button-base.w-button` whose label is Try for free.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 99×44 | fill #2266ed `brand`, ink #ffffff, size 14px, weight 500, font Inter, radius 8px, padding 12px | at rest | [crop](components/crops/nav-try-default.png) |
| hover | 99×44 | same fill in this reading | mouse hover | [crop](components/crops/nav-try-hover.png) |
| focus | 99×44 | outline rgb(0, 95, 204) auto 1px | element.focus() | not cropped |

### Book a demo

Selector: nav `a.button-base.s-ghost` labelled Book a demo. The href is a Calendly URL. It was not followed.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 111×44 | fill transparent, ink #34363a `neutral.900`, size 14px, weight 400, font Inter, radius 8px | at rest | [crop](components/crops/nav-demo-default.png) |

### Watch demo

Selector: hero `a` labelled Watch demo.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 157×54 | fill #f5f6f6 `neutral.050`, ink #34363a `neutral.900`, size 17.84px, weight 500, font Inter, radius 8px, padding 16px 24px, border 1px #e4e6e9 `neutral.100` | at rest | [crop](components/crops/watch-demo-default.png) |
| hover | 157×54 | same fill in this reading | mouse hover | [crop](components/crops/watch-demo-hover.png) |

## Type

### Hero title

Selector: `h1`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 768×120 | ink #34363a `neutral.900`, size 56px, weight 400, line-height 60px, font Tiempos Headline | at rest | [crop](components/crops/hero-title-default.png) |

### Hero body

Selector: `p.text-2xl.text-color-b`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 640×56 | ink #646c76 `neutral.500`, size 20px, weight 400, line-height 28px, font Inter | at rest | not cropped |

### Login title

Selector: `div.text-3xl.font-medium` whose text is Log in to Missive.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | crop 380×42 | ink #2e3034 `mail.ink`, size 24px, weight 500, line-height 33.6px, font the system stack | at rest | [crop](components/crops/login-title-default.png) |

## Button

### Continue with Google

Selector: first `button` on `#login`. Not clicked. Google OAuth was not started.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 372×45 | fill transparent, ink #2e3034 `mail.ink`, size 14px, weight 600, radius 8px, padding 12px 24px, shadow rgba(46, 48, 52, 0.14) 0px 0px 0px 1px inset | at rest | [crop](components/crops/login-google-default.png) |
| hover | 372×45 | fill rgba(46, 48, 52, 0.05) | mouse hover | [crop](components/crops/login-google-hover.png) |

### Continue with Apple

Selector: `button` labelled Continue with Apple. Not clicked.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 372×45 | same chrome as Continue with Google | at rest | [crop](components/crops/login-apple-default.png) |

### Single sign-on

Selector: `button` labelled Single sign-on (SSO) on the login card. The SSO screen itself was opened by URL, `#sso`, and not submitted.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 372×45 | same chrome as Continue with Google | at rest | [crop](components/crops/login-sso-default.png) |

### Log in

Selector: `button[type="submit"]` on `#login`. Not clicked.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 372×45 | fill #2266ed `brand`, ink #ffffff, size 14px, weight 600, radius 8px, padding 12px 24px | at rest | [crop](components/crops/login-submit-default.png) |
| hover | 372×45 | fill #1b51da | mouse hover | [crop](components/crops/login-submit-hover.png) |

## Text field

### Work email

Selector: `input[type="email"]`. Placeholder only. Nothing typed.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 372×43 | fill transparent, ink #2e3034, size 14px, weight 400, radius 8px, padding 12px, border 1px rgba(46, 48, 52, 0.14) | at rest | [crop](components/crops/login-email-default.png) |
| focus | 372×43 | border reads as a blue ring in the crop | element.focus() | [crop](components/crops/login-email-focused.png) |

### Password

Selector: `input[type="password"]`. The field shows the browser's placeholder dots. It was never filled.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 372×43 | same chrome as the email field, padding 12px 40px 12px 12px for the visibility control | at rest | [crop](components/crops/login-password-default.png) |

## Link

### Forgot your password

Selector: `a` labelled Forgot your password. The reset screen was not opened. `#forgot`, `#forgot-password` and `#reset` redirect back to login. `/forgot` is a 404.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 151×17 | fill transparent, ink #0677f9 `mail.blue`, size 14px, weight 500, radius 4px | at rest | [crop](components/crops/login-forgot-default.png) |
| hover | 151×17 | underline on hover in the stylesheet; this reading kept the colour | mouse hover | [crop](components/crops/login-forgot-hover.png) |

### Create an account

Selector: `a` labelled Create an account. `#signup` was opened by URL and not submitted.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 129×17 | ink #0677f9 `mail.blue`, size 14px, weight 500 | at rest | [crop](components/crops/login-create-default.png) |

## Card

### Pricing plan

Selector: the Starter column on `/pricing`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 401×422 | fill transparent, radius 16px on the left, border 1px #e4e6e9 `neutral.100` | at rest | [crop](components/crops/plan-card-default.png) |

### Billed yearly

Selector: the label next to the yearly switch.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | crop 121×44 | label text | at rest | [crop](components/crops/billing-label-default.png) |

## Gaps

Not present on these surfaces: text area, select, checkbox (the signup agreement checkbox was on screen and not toggled), radio, tabs, menu (the Product dropdown was not opened; a click opened the privacy sheet), tooltip, dialog (the privacy sheet was hidden, never accepted), toast, table, avatar, badge as a product component.

Not captured: hover on Try for free that changes the fill (this reading stayed #2266ed), focus-visible crops, pressed states, the dark login controls as crops (the dark page shot is [login-dark-default](screenshots/login-dark-default.png)), the signed-in inbox, and any error state. The signup form was left empty, so the disabled Sign up and the validation error were not shown.
