# Components

Measured on the live signed-out DOM, 2026-11-19, light, 1440 (phone menu at 390). Nothing was submitted. Login email was filled with `sample@example.com` and cleared. Password, billing, Google and the newsletter were never submitted.

## Navigation

### Wordmark

Selector: `header a[href="/"] in the nav row`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 72×14 | fill transparent, ink #0e0e0e `black`, size 16px, weight 400, font ui-sans-serif | at rest | [crop](components/crops/wordmark-default.png) |

### Pricing link

Selector: `nav a[href="/pricing"]`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 66×32 | fill transparent, ink #fafafa `offwhite`, size 13.6px, weight 400, font easeStandard, radius 6px | at rest | [crop](components/crops/nav-link-default.png) |
| hover | 66×32 | fill #2a2a2a `grayDark2` | mouse hover | [crop](components/crops/nav-link-hover.png) |
| focus-visible | 66×32 | outline 2px, outline colour #f04e23 `orange` | Shift+Tab, Tab | [crop](components/crops/nav-link-focus-visible.png) |
| pressed | 66×32 | fill #2a2a2a `grayDark2` | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/nav-link-pressed.png) |

### Mobile menu button

Selector: `first header button at 390; pressed via CDP`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 0×0 | fill transparent, ink #fafafa `offwhite`, size 13.6px, weight 400, font easeStandard, radius 6px | at rest |  |
| pressed | 0×0 | same | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit |  |

## Button

### Sign In

Selector: `nav a to /login. Yellow fill. Not clicked.`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 66×40 | fill #fff78b `yellow`, ink #0e0e0e `black`, size 12.8px, weight 400, font easeStandard, radius 6px | at rest | [crop](components/crops/nav-signin-default.png) |
| hover | 66×40 | fill lab(96.2008 -7.76836 52.536 / 0.8) | mouse hover | [crop](components/crops/nav-signin-hover.png) |
| focus-visible | 66×40 | outline 2px, outline colour #f04e23 `orange` | Shift+Tab, Tab | [crop](components/crops/nav-signin-focus-visible.png) |
| pressed | 66×40 | fill lab(96.2008 -7.76836 52.536 / 0.8) | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/nav-signin-pressed.png) |

### Start for Free

Selector: `nav a to /signup. Orange fill. Not clicked.`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 103×40 | fill #f04e23 `orange`, ink #fafafa `offwhite`, size 12.8px, weight 400, font easeStandard, radius 6px | at rest | [crop](components/crops/nav-start-default.png) |
| hover | 103×40 | fill lab(57.0275 61.7287 58.5433 / 0.8) | mouse hover | [crop](components/crops/nav-start-hover.png) |
| focus-visible | 103×40 | outline 2px, outline colour #f04e23 `orange` | Shift+Tab, Tab | [crop](components/crops/nav-start-focus-visible.png) |
| pressed | 103×40 | fill lab(57.0275 61.7287 58.5433 / 0.8) | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/nav-start-pressed.png) |

### Get started for free

Selector: `hero a, orange fill. Not clicked.`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 185×48 | fill #f04e23 `orange`, ink #fafafa `offwhite`, size 16px, weight 400, font easeStandard, radius 6px | at rest | [crop](components/crops/hero-cta-default.png) |
| hover | 185×48 | fill lab(57.0275 61.7287 58.5433 / 0.8) | mouse hover | [crop](components/crops/hero-cta-hover.png) |
| focus-visible | 185×48 | outline 2px, outline colour #f04e23 `orange` | Shift+Tab, Tab | [crop](components/crops/hero-cta-focus-visible.png) |
| pressed | 185×48 | fill lab(57.0275 61.7287 58.5433 / 0.8) | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/hero-cta-pressed.png) |

### Start with Creator

Selector: `pricing a to /billing. Not clicked.`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 345×48 | fill #1a1616 `offblack`, ink #fafafa `offwhite`, size 12.8px, weight 400, font easeStandard, radius 6px | at rest | [crop](components/crops/plan-cta-default.png) |
| hover | 345×48 | fill #fff78b `yellow`, ink #0e0e0e `black` | mouse hover | [crop](components/crops/plan-cta-hover.png) |
| focus-visible | 345×48 | outline 2px, outline colour #f04e23 `orange` | Shift+Tab, Tab | [crop](components/crops/plan-cta-focus-visible.png) |
| pressed | 345×48 | fill #fff78b `yellow`, ink #0e0e0e `black` | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/plan-cta-pressed.png) |

### Log in button

Selector: `button[type=submit]; pressed via CDP, never clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 334×40 | fill #f04e23 `orange`, ink #ffffff `white`, size 12px, weight 500, font Instrument Sans, radius 8px | at rest | [crop](components/crops/login-submit-default.png) |
| hover | 334×40 | same | mouse hover | [crop](components/crops/login-submit-hover.png) |
| focus-visible | 334×40 | same | Shift+Tab, Tab | [crop](components/crops/login-submit-focus-visible.png) |
| pressed | 334×40 | fill #ad3213 | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/login-submit-pressed.png) |

### Continue with Google

Selector: `button whose name includes Google; never clicked`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 334×40 | fill #ffffff `white`, ink #000000, size 12px, weight 500, font Instrument Sans, radius 8px | at rest | [crop](components/crops/login-google-default.png) |
| hover | 334×40 | fill oklab(0.999994 0.0000455678 0.0000200868 / 0.9) | mouse hover | [crop](components/crops/login-google-hover.png) |
| focus-visible | 334×40 | same | Shift+Tab, Tab | [crop](components/crops/login-google-focus-visible.png) |
| pressed | 334×40 | fill oklab(0.999994 0.0000455678 0.0000200868 / 0.9) | CDP forcePseudoState :active:hover; no click, so the control does not navigate or submit | [crop](components/crops/login-google-pressed.png) |

## Type

### Hero title

Selector: `h1`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 752×56 | fill transparent, ink #0e0e0e `black`, size 56px, weight 400, font recklessStandard | at rest | [crop](components/crops/hero-title-default.png) |

### Login title

Selector: `first heading on app.melius.com/login`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 1×1 | fill transparent, ink #c0c0c0, size 20px, weight 500, font Instrument Sans | at rest | [crop](components/crops/login-title-default.png) |

### Signup title

Selector: `first heading on app.melius.com/signup`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 1×1 | fill transparent, ink #c0c0c0, size 20px, weight 500, font Instrument Sans | at rest | [crop](components/crops/signup-title-default.png) |

### Docs title

Selector: `first heading on docs.melius.com`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 101×24 | fill transparent, ink #161616, size 14px, weight 600, font Inter | at rest | [crop](components/crops/docs-title-default.png) |

## Menu

### Product menu trigger

Selector: `nav control labelled Product`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 96×32 | fill transparent, ink #fafafa `offwhite`, size 13.6px, weight 400, font easeStandard, radius 6px | at rest | [crop](components/crops/nav-product-default.png) |
| hover | 96×32 | fill #2a2a2a `grayDark2` | mouse hover | [crop](components/crops/nav-product-hover.png) |

### Product menu item

Selector: `a[href="/product/ai-image-generator"] while the menu is open. Not clicked.`.

Not found on the page at measure time.

### Mobile pricing link

Selector: `a[href="/pricing"] after the menu toggle`.

Not found on the page at measure time.

## Link

### Footer link

Selector: `footer a[href="/about"]`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 37×16 | fill transparent, ink #676767 `gray`, size 13.6px, weight 400, font easeStandard, radius 6px | at rest | [crop](components/crops/footer-link-default.png) |
| hover | 37×16 | ink #fafafa `offwhite` | mouse hover | [crop](components/crops/footer-link-hover.png) |

### Docs link

Selector: `fourth link on the docs home; not followed`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 54×20 | fill transparent, ink #4f4f4f, size 14px, weight 500, font Inter | at rest | [crop](components/crops/docs-link-default.png) |
| hover | 54×20 | ink #161616 | mouse hover | [crop](components/crops/docs-link-hover.png) |

## Card

### Creator plan title

Selector: `heading whose text includes Creator`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 329×32 | fill transparent, ink #0e0e0e `black`, size 32px, weight 400, font futurist | at rest | [crop](components/crops/plan-title-default.png) |

### Creator plan card

Selector: `ancestor of Start with Creator, 220-480px wide`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 387×755 | fill #fafafa `offwhite`, ink #0e0e0e `black`, size 16px, weight 400, font ui-sans-serif, radius 12px, shadow oklab(0.645234 0.16807 0.118123 / 0.237807) 0px 0px 15.3355px 0px, oklab(0.64... | at rest | [crop](components/crops/plan-card-default.png) |

## Field

### Email field

Selector: `first email input on /login. Sample text cleared. Nothing submitted.`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 284×20 | fill transparent, ink #c0c0c0, size 14px, weight 500, font Instrument Sans | at rest | [crop](components/crops/login-email-default.png) |
| focused | 284×20 | same | clicked into the field; nothing submitted | [crop](components/crops/login-email-focused.png) |
| filled | 284×20 | same | sample text typed, then the field is cleared; nothing submitted | [crop](components/crops/login-email-filled.png) |

### Signup email

Selector: `first email input on /signup; focused only, nothing typed or submitted`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 284×20 | fill transparent, ink #c0c0c0, size 14px, weight 500, font Instrument Sans | at rest | [crop](components/crops/signup-email-default.png) |
| focused | 284×20 | same | clicked into the field; nothing submitted | [crop](components/crops/signup-email-focused.png) |

### Contact field

Selector: `first field on /contact; focused only, nothing typed or submitted`.

| State | Size | What changed | How | Crop |
|---|---|---|---|---|
| default | 250×44 | fill transparent, ink #fafafa `offwhite`, size 14px, weight 400, font ui-sans-serif, radius 6px | at rest | [crop](components/crops/contact-field-default.png) |
| focused | 250×44 | shadow rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0... | clicked into the field; nothing submitted | [crop](components/crops/contact-field-focused.png) |

## Gaps

| Checklist item | Status |
|---|---|
| Button, link, text field, card, menu | Captured. Nav focus-visible is a 2px orange outline. |
| Icon button | The phone hamburger measured 0×0. The click did not open a drawer. |
| Text area, select, checkbox, radio | Not on the captured routes. |
| Switch | The pricing Monthly/Annual control is in [pricing-light-default](screenshots/pricing-light-default.png). It was not flipped, so its states are not in the tables. |
| Tabs | Docs tabs are in [docs-light-default](screenshots/docs-light-default.png). Not toggled. |
| Tooltip, toast | Not opened. |
| Dialog | The login card is a dialog over the product. [login-light-default](screenshots/login-light-default.png). |
| Table, avatar, list row | Not on these routes. |
| Badge | The Ditto New chip is in the product menu shot. Not cropped on its own. |
| Empty, loading, error, destructive confirmation | Login was not submitted, so no error. Not on the public routes. |
| Disabled, loading, selected | Not shown. |

