# Components

Measured on the live signed-out DOM, 2026-11-18, light, 1440 (phone menu at 390). Nothing was submitted. Login email was filled with `sample@example.com` and cleared. The password field was focused and never filled.

## Navigation

### Wordmark

Selector: `header a[href="/"]`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 108×24 | fill transparent, ink #000000 `neutral.900`, size 16px, weight 400, font ui-sans-serif | at rest | [crop](components/crops/wordmark-default.png) |

### Nav link

Selector: `header a[href="/pricing/"] in the nav row`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 91×39 | fill transparent, ink oklch(0.226 0 0), size 14px, weight 400, font Phonic | at rest | [crop](components/crops/nav-link-default.png) |
| hover | 91×39 | same | mouse hover | [crop](components/crops/nav-link-hover.png) |
| focus-visible | 91×39 | outline 1px | Shift+Tab, Tab | [crop](components/crops/nav-link-focus-visible.png) |
| pressed | 91×39 | same | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/nav-link-pressed.png) |

### Open navigation

Selector: `button Open navigation; pressed via CDP, not opened here`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 24×24 | fill transparent, ink #000000 `neutral.900`, size 16px, weight 400, font ui-sans-serif | at rest | [crop](components/crops/m-menu-default.png) |
| pressed | 24×24 | same | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/m-menu-pressed.png) |

## Link

### Log in

Selector: `header a[href*=auth.maze.co/login] in the nav row. The label is text, not a nested button.`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 45×24 | fill transparent, ink oklch(0.226 0 0), size 17px, weight 400, font Phonic | at rest | [crop](components/crops/nav-login-default.png) |
| hover | 45×24 | same | mouse hover | [crop](components/crops/nav-login-hover.png) |
| focus-visible | 45×24 | outline 1px | Shift+Tab, Tab | [crop](components/crops/nav-login-focus-visible.png) |
| pressed | 45×24 | same | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/nav-login-pressed.png) |

### Continue with SSO

Selector: `a Continue with SSO; never clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 440×48 | fill #ffffff `neutral.0`, ink #0568fd `action`, size 16px, weight 600, font Inter, radius 8px, shadow rgba(5, 104, 253, 0.08) 0px 1px 2px 0px, rgba(5, 104, 253, 0.28) 0px 0px 0px ... | at rest | [crop](components/crops/login-sso-default.png) |
| hover | 440×48 | fill #ceeeff, ink #034fd6, shadow rgba(5, 104, 253, 0.08) 0px 1px 2px 0px, rgba(5, 104, 253, 0.28) 0px 0px 0px ... | mouse hover | [crop](components/crops/login-sso-hover.png) |
| focus-visible | 440×48 | outline 2px, outline colour #034fd6, shadow rgba(5, 104, 253, 0.28) 0px 0px 0px 1px inset | Shift+Tab, Tab | [crop](components/crops/login-sso-focus-visible.png) |
| pressed | 440×48 | fill #9ad6ff, ink #0138a9, shadow rgb(5, 104, 253) 0px 0px 0px 1px inset | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/login-sso-pressed.png) |

### Reset password

Selector: `a Reset password; never clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 440×20 | fill transparent, ink #000000 `neutral.900`, size 14px, weight 400, font Inter, radius 4px, outline 2px, outline colour transparent | at rest | [crop](components/crops/login-reset-default.png) |
| hover | 440×20 | same | mouse hover | [crop](components/crops/login-reset-hover.png) |

## Button

### Try Maze for free

Selector: `header signup button (pill, hairline)`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 160×40 | fill oklab(1 0 0 / 0.7), ink oklch(0.226 0 0), size 17px, weight 400, font Phonic, radius 3.35544e+07px | at rest | [crop](components/crops/nav-try-default.png) |
| hover | 160×40 | fill oklch(1 0 0) | mouse hover | [crop](components/crops/nav-try-hover.png) |
| focus-visible | 160×40 | outline 2px | Shift+Tab, Tab | [crop](components/crops/nav-try-focus-visible.png) |
| pressed | 160×40 | fill oklch(1 0 0) | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/nav-try-pressed.png) |

### Get a demo

Selector: `header a[href="/demo/"] button (filled)`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 118×40 | fill oklch(0.226 0 0), ink oklch(1 0 0), size 17px, weight 400, font Phonic, radius 8px | at rest | [crop](components/crops/nav-demo-default.png) |
| hover | 118×40 | fill oklch(0.356 0 0) | mouse hover | [crop](components/crops/nav-demo-hover.png) |
| focus-visible | 118×40 | fill oklch(0.356 0 0), outline 2px | Shift+Tab, Tab | [crop](components/crops/nav-demo-focus-visible.png) |
| pressed | 118×40 | fill oklch(0 0 0) | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/nav-demo-pressed.png) |

### Starter sign up

Selector: `pricing Starter CTA; not clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 124×40 | fill oklch(0.226 0 0), ink oklch(1 0 0), size 17px, weight 400, font Phonic, radius 8px | at rest | [crop](components/crops/plan-cta-default.png) |
| hover | 124×40 | fill oklch(0.356 0 0) | mouse hover | [crop](components/crops/plan-cta-hover.png) |
| focus-visible | 124×40 | fill oklch(0.356 0 0), outline 2px | Shift+Tab, Tab | [crop](components/crops/plan-cta-focus-visible.png) |
| pressed | 124×40 | fill oklch(0 0 0) | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/plan-cta-pressed.png) |

### Log in button

Selector: `button[type=submit]; pressed via CDP, never clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 440×48 | fill #0568fd `action`, ink #ffffff `neutral.0`, size 16px, weight 600, font Inter, radius 8px, shadow rgba(5, 104, 253, 0.08) 0px 1px 2px 0px, rgba(5, 104, 253, 0.28) 0px 0px 0px ... | at rest | [crop](components/crops/login-submit-default.png) |
| hover | 440×48 | fill #034fd6, shadow rgba(5, 104, 253, 0.08) 0px 1px 2px 0px, rgba(5, 104, 253, 0.28) 0px 0px 0px ... | mouse hover | [crop](components/crops/login-submit-hover.png) |
| focus-visible | 440×48 | shadow rgba(5, 104, 253, 0.28) 0px 0px 0px 1px inset | Shift+Tab, Tab | [crop](components/crops/login-submit-focus-visible.png) |
| pressed | 440×48 | fill #0138a9, shadow rgb(5, 104, 253) 0px 0px 0px 1px inset | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/login-submit-pressed.png) |

### Continue with Google

Selector: `button Continue with Google; never clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 440×48 | fill #ffffff `neutral.0`, ink #0568fd `action`, size 16px, weight 600, font Inter, radius 8px, shadow rgba(5, 104, 253, 0.08) 0px 1px 2px 0px, rgba(5, 104, 253, 0.28) 0px 0px 0px ... | at rest | [crop](components/crops/login-google-default.png) |
| hover | 440×48 | fill #ceeeff, ink #034fd6, shadow rgba(5, 104, 253, 0.08) 0px 1px 2px 0px, rgba(5, 104, 253, 0.28) 0px 0px 0px ... | mouse hover | [crop](components/crops/login-google-hover.png) |
| focus-visible | 440×48 | shadow rgba(5, 104, 253, 0.28) 0px 0px 0px 1px inset | Shift+Tab, Tab | [crop](components/crops/login-google-focus-visible.png) |
| pressed | 440×48 | fill #9ad6ff, ink #0138a9, shadow rgb(5, 104, 253) 0px 0px 0px 1px inset | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/login-google-pressed.png) |

### Report sign up

Selector: `painted Sign up for free on the public report; never clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 118×32 | fill #0568fd `action`, ink #ffffff `neutral.0`, size 14px, weight 600, font Inter, radius 8px, shadow rgba(5, 104, 253, 0.08) 0px 1px 2px 0px, rgba(5, 104, 253, 0.28) 0px 0px 0px ... | at rest | [crop](components/crops/report-signup-default.png) |
| hover | 118×32 | fill #034fd6, shadow rgba(5, 104, 253, 0.08) 0px 1px 2px 0px, rgba(5, 104, 253, 0.28) 0px 0px 0px ... | mouse hover | [crop](components/crops/report-signup-hover.png) |
| focus-visible | 118×32 | shadow rgba(5, 104, 253, 0.28) 0px 0px 0px 1px inset | Shift+Tab, Tab | [crop](components/crops/report-signup-focus-visible.png) |
| pressed | 118×32 | fill #0138a9, shadow rgb(5, 104, 253) 0px 0px 0px 1px inset | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/report-signup-pressed.png) |

### Report login

Selector: `Login on the public report; never clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 64×32 | fill transparent, ink #535a74, size 14px, weight 600, font Inter | at rest | [crop](components/crops/report-login-default.png) |
| hover | 64×32 | ink #034fd6 | mouse hover | [crop](components/crops/report-login-hover.png) |

## Type

### Hero title

Selector: `h1`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 800×136 | fill transparent, ink oklch(0.226 0 0), size 130px, weight 300, font Phonic | at rest | [crop](components/crops/hero-title-default.png) |

### Login title

Selector: `h1 Log in to Maze`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 440×32 | fill transparent, ink #000000 `neutral.900`, size 23px, weight 600, font Inter | at rest | [crop](components/crops/login-title-default.png) |

### Report title

Selector: `first heading on the public sample report`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 419×32 | fill transparent, ink #000000 `neutral.900`, size 23px, weight 600, font Inter | at rest | [crop](components/crops/report-title-default.png) |

### Demo page title

Selector: `first heading on /demo/`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 624×128 | fill transparent, ink oklch(0.226 0 0), size 58px, weight 300, font Phonic | at rest | [crop](components/crops/demo-title-default.png) |

## Card

### Plan title

Selector: `heading Starter`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 295×64 | fill transparent, ink oklch(0.226 0 0), size 58px, weight 300, font Phonic | at rest | [crop](components/crops/plan-title-default.png) |

### Starter plan card

Selector: `ancestor of the Starter heading, 280-560px wide`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 295×468 | fill transparent, ink #000000 `neutral.900`, size 16px, weight 400, font ui-sans-serif | at rest | [crop](components/crops/plan-card-default.png) |

## Field

### Email field

Selector: `input[name=email]`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 440×48 | fill transparent, ink #000000 `neutral.900`, size 16px, weight 400, font Inter, radius 8px | at rest | [crop](components/crops/login-email-default.png) |
| focused | 440×48 | same | clicked into the field; nothing submitted | [crop](components/crops/login-email-focused.png) |
| filled | 440×48 | same | sample text typed, then the field is cleared; nothing submitted | [crop](components/crops/login-email-filled.png) |

### Password field

Selector: `input[name=password]; never filled`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 440×48 | fill transparent, ink #000000 `neutral.900`, size 16px, weight 400, font Inter, radius 8px | at rest | [crop](components/crops/login-password-default.png) |
| focused | 440×48 | same | clicked into the field; nothing submitted | [crop](components/crops/login-password-focused.png) |

### Demo form field

Selector: `first input on /demo/; focused only, nothing typed or submitted`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 576×40 | fill oklch(1 0 0), ink oklch(0.226 0 0), size 15px, weight 400, font Phonic, radius 8px | at rest | [crop](components/crops/demo-field-default.png) |
| focused | 576×40 | ink oklch(0.547 0.218 16.6) | clicked into the field; nothing submitted | [crop](components/crops/demo-field-focused.png) |

## Menu

### Mobile menu

Selector: `opened mobile navigation; local toggle only`.

Not found on the page at measure time.

### Platform menu trigger

Selector: `header a[href=/platform/] in the nav row`.

Not found on the page at measure time.

### Platform menu item

Selector: `open platform panel`.

Not found on the page at measure time.

