# Krisp components

Public marketing components measured on krisp.ai on 2026-11-18, signed out.

30 components.

## Shell and navigation

### Header

The 73px white bar: wordmark, product menus, Sign in, Book a demo, Get Krisp.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 1440×73 | rgba(255, 255, 255, 0.8) | rgb(19, 16, 50) | 0px |

### Wordmark

The krisp wordmark in the header.

Not found on the page during this run.

### Nav link

A top-level destination. Hover and pressed measured; the link was not followed.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 70.36×32 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 8px |
| hover | 70.36×32 | rgb(244, 244, 245) | rgb(26, 26, 34) | 8px |
| focus-visible | 70.36×32 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 8px |
| pressed | 70.36×32 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 8px |

### Nav menu trigger

Opens the product menu. The opened menu is captured separately.

Not found on the page during this run.

### Sign in link

Text link to app.krisp.ai/login. Measured, never followed.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 43.95×20 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 0px |
| hover | 43.95×20 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 0px |
| focus-visible | 43.95×20 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 0px |

### Book a demo button

Near-black pill in the header. The control is a `div.button.btn--dark` wrapping a link to `/contact-sales/`. The crop and the size below are the wrapper. Paint lives on the inner `a`: background `{light.action.inverse}` (`#131032`), text `{light.text.on-accent}`, radius `{core.radius.sm}`, padding `{core.spacing.2}` `{core.spacing.5}`. Hover of the inner face is `{light.action.inverse-hover}` on the hero variant. Measured, never followed. Crop: [book-demo-default](components/crops/book-demo-default.png).

| State | Size | Wrapper fill | Wrapper text | Radius |
|---|---|---|---|---|
| default | 128.88×36 | transparent | `{light.text.primary}` | `{core.radius.sm}` |
| hover | 128.88×36 | transparent | `{light.text.primary}` | `{core.radius.sm}` |
| focus-visible | 128.88×36 | transparent | `{light.text.primary}` | `{core.radius.sm}` |
| pressed | 128.88×36 | transparent | `{light.text.primary}` | `{core.radius.sm}` |

### Get Krisp button

Indigo primary pill. The control is a `div.button.btn--primary` wrapping a link. Paint lives on the inner `a`: background `{light.action.primary}` (`#614efa`), hover `{light.action.primary-hover}` (`#4a3bbe`), text `{light.text.on-accent}`, radius `{core.radius.sm}`, height `{core.size.button-sm}`. The sign-up destination was not followed. Crop: [get-krisp-default](components/crops/get-krisp-default.png).

| State | Size | Wrapper fill | Wrapper text | Radius |
|---|---|---|---|---|
| default | 124.53×36 | transparent | `{light.text.primary}` | `{core.radius.sm}` |
| hover | 124.53×36 | transparent | `{light.text.primary}` | `{core.radius.sm}` |
| focus-visible | 124.53×36 | transparent | `{light.text.primary}` | `{core.radius.sm}` |
| pressed | 124.53×36 | transparent | `{light.text.primary}` | `{core.radius.sm}` |

### Get Krisp menu

The download menu under Get Krisp, if the click revealed one.

Not found on the page during this run.

## Home

### Hero title

Plus Jakarta Sans display heading.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 1280×72 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |

### Hero announcement pill

The "New" chip linking to a product page.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 204.25×40 | rgba(0, 0, 0, 0) | rgb(36, 35, 45) | 32px |
| hover | 208.31×40.4 | rgba(0, 0, 0, 0) | rgb(36, 35, 45) | 36px |

### Hero Get Krisp button

The primary CTA under the headline. Same paint as the header Get Krisp face: `{light.action.primary}` on the inner `a`, text `{light.text.on-accent}`, radius `{core.radius.sm}`, height `{core.size.button}`. Measured, never followed. Crop: [hero-cta-default](components/crops/hero-cta-default.png).

| State | Size | Wrapper fill | Face fill | Radius |
|---|---|---|---|---|
| default | 133.47×44 | transparent | `{light.action.primary}` | `{core.radius.sm}` |
| hover | 133.47×44 | transparent | `{light.action.primary-hover}` | `{core.radius.sm}` |
| focus-visible | 133.47×44 | transparent | `{light.action.primary}` | `{core.radius.sm}` |
| pressed | 133.47×44 | transparent | `{light.action.primary}` | `{core.radius.sm}` |

### Footer

Link columns, social marks, legal links including Cookie settings (not clicked).

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 1440×738 | rgb(244, 244, 245) | rgb(19, 16, 50) | 0px |

### FAQ row

An accordion row on the home page, if one is present.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 1440×943 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |
| opened | 1440×1153 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |

## Pricing

### Billing toggle

Monthly / Annually pill. Annually is the resting state and shows Save 50%.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 1280×44 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |

### Plan card

A pricing column: title, description, price, CTA. Fill `{light.background.surface}`, text `{light.text.primary}`, radius `{core.radius.lg}`, border `{core.borderWidth.hairline}` `{light.border.default}`, padding `{core.spacing.6}`. Crop: [plan-card-default](components/crops/plan-card-default.png).

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 308×740.25 | `{light.background.surface}` | `{light.text.primary}` | `{core.radius.lg}` |

### Highlighted plan card

The Most popular column. Same surface as a plan card, with border `{core.borderWidth.strong}` `{light.border.highlight}`. Crop: [plan-card-highlight-default](components/crops/plan-card-highlight-default.png).

| State | Size | Fill | Border | Radius |
|---|---|---|---|---|
| default | 308×740.25 | `{light.background.surface}` | `{light.border.highlight}` | `{core.radius.lg}` |
| hover | 308×740.25 | `{light.background.surface}` | `{light.border.highlight}` | `{core.radius.lg}` |

### Plan price

The yearly price shown at rest.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 258×50 | rgba(0, 0, 0, 0) | rgb(35, 32, 64) | 0px |

### Plan CTA

Try it Free / Start with Core. Measured, never followed (it links to app.krisp.ai sign-up).

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 258×46 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |
| hover | 258×46 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |
| focus-visible | 258×46 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |

### Most popular badge

The badge on the highlighted plan. Fill `{light.action.primary}`, text near-white, radius `{core.radius.pill}`. Crop: [plan-badge-default](components/crops/plan-badge-default.png).

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 96.61×24 | `{light.action.primary}` | `{light.text.on-accent}` | `{core.radius.pill}` |

## Product pages

### Product page title

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 670×144 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |

### Product page primary button

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 154.78×36 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 8px |
| hover | 154.78×36 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 8px |

### Demo switch

The "With Krisp" demo switch on the noise-cancellation page. Not toggled if doing so starts audio.

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 40×24 | rgb(97, 78, 250) | rgb(26, 26, 34) | 50px |

## Customers, about, security, blog, careers

### customers title

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 760×108 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |

### about title

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 900×128 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 0px |

### security title

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 800×60 | rgba(0, 0, 0, 0) | rgb(255, 255, 255) | 0px |

### blog title

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 1280×80 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 0px |

### careers title

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 642.83×64 | rgba(0, 0, 0, 0) | rgb(26, 26, 34) | 0px |

### 404 page

`/download/` returns the marketing 404. The heading reads "Error 404: Page not found" in `{light.text.primary}`, with a construction illustration and a text link back to krisp.ai in `{light.text.link}`. The measurer's title selector missed the heading; the page itself is in [not-found-light-default](screenshots/not-found-light-default.png).

## Mobile (390 wide)

### Mobile header

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 405×63 | rgba(255, 255, 255, 0.8) | rgb(19, 16, 50) | 0px |

### Mobile menu button

| State | Size | Fill | Text | Radius |
|---|---|---|---|---|
| default | 28×18 | rgba(0, 0, 0, 0) | rgb(19, 16, 50) | 0px |

## Gaps

The signed-in app at https://app.krisp.ai/login (the meeting assistant, notes, recordings and account settings) was not captured.
Get Krisp and Try it Free go to https://app.krisp.ai/sign-up. Account creation was not followed.
Book a demo and Talk to Sales open https://krisp.ai/contact-sales/, a sales form with email, name, select and radios. It was not submitted. Text fields, selects, checkboxes, radios and toasts live on that form or inside the app.
Help centre at https://help.krisp.ai/hc/en-us was not captured.
Cookie settings (OneTrust) was hidden and never clicked.
The wordmark is an image, not a text node, so it has no crop. It is visible in [home-light-default](screenshots/home-light-default.png).
Focus-visible was requested on the public buttons and did not paint a designed ring. `light.border.focus` records the accent as the nearest colour, not a measured outline.
Text fields, selects, checkboxes, radios and toasts live on that form or inside the app.
