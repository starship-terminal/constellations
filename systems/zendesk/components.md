# Components

Public Zendesk controls measured on 2026-11-19. Colours are computed styles. Token names that hold the same values are in [tokens.json](tokens.json).

Nothing was typed into a field except a focus click, and no form was submitted. The register email field was already `aria-invalid` when the page loaded.

Not present on the captured public surfaces: text area was on the contact form and measured as a style only (its box was off-screen in the first pass). Radio buttons are on the demo step and were not measured. Switch, tabs (the pricing suite switch was visible and the tab locator missed it), tooltip, toast, table, avatar and a designed menu were not measured. The signed-in agent workspace was not opened.

## Buttons

### Nav primary

Lime pill in the header. Text is "Try it for free". Text is ink, not white.

Page: https://www.zendesk.com/sg/

| State | Size | Fill | Text | Radius | Crop |
|---|---|---|---|---|---|
| default | 127×43 | rgb(209, 244, 112) | rgb(17, 17, 13) | 16px | [crop](components/crops/button-primary-default.png) |
| hover | 127×43 | rgb(209, 244, 112) | rgba(17, 17, 13, 1) | 16px | [crop](components/crops/button-primary-hover.png) |

Forced `:active` drops the text to about 0.85 opacity. The fill does not change.

### Hero submit

Same lime fill, white text, 48px tall, 18px type. Label "Try it for free". It sits in a form and was not pressed.

Page: https://www.zendesk.com/sg/

| State | Size | Fill | Text | Radius | Crop |
|---|---|---|---|---|---|
| default | 164×48 | rgb(209, 244, 112) | rgb(255, 255, 255) | 16px | [crop](components/crops/button-primary-on-hero-default.png) |

### Secondary

"View demo" in the header. Transparent fill, 16px radius, 16px/600 type.

| State | Size | Fill | Text | Radius | Crop |
|---|---|---|---|---|---|
| default | 115×43 | transparent | rgb(17, 17, 13) | 16px | [crop](components/crops/button-secondary-default.png) |
| hover | 115×43 | transparent | text opacity moves | 16px | [crop](components/crops/button-secondary-hover.png) |

### Login sign in

Full-width lime button on the subdomain page. Not pressed.

Page: https://www.zendesk.com/sg/login/

| State | Size | Fill | Text | Radius | Crop |
|---|---|---|---|---|---|
| default | 445×48 | rgb(209, 244, 112) | rgb(17, 17, 13) | 16px | [crop](components/crops/button-signin-default.png) |

### Login secondary

"New here? Start free trial". Transparent, 16px radius, 18px/600. Not followed.

| State | Size | Fill | Text | Radius | Crop |
|---|---|---|---|---|---|
| default | 445×48 | transparent | rgb(17, 17, 13) | 16px | [crop](components/crops/button-secondary-login-default.png) |

### Help centre pill

"Free trial" is a 100px-radius pill, 16px/700, lime fill.

Page: https://support.zendesk.com/hc/en-us

| State | Size | Fill | Text | Radius | Crop |
|---|---|---|---|---|---|
| default | 112×48 | rgb(209, 244, 112) | rgb(17, 17, 13) | 100px | [crop](components/crops/button-pill-default.png) |

Hover adds a 2px border at rgba(17, 17, 13, 0.7). The fill stays lime.

## Fields

### Hero email

White field, 12px radius, 15px type, 48px tall. Placeholder "Enter work email". Not typed, not submitted.

| State | Fill | Ring | Crop |
|---|---|---|---|
| default | rgb(255, 255, 255) | inset 1px rgb(213, 213, 210) | [crop](components/crops/field-email-default.png) |
| focus | rgb(255, 255, 255) | inset 2px rgb(17, 17, 13), plus a 2px rgb(213, 213, 210) outline offset 3px | [crop](components/crops/field-email-focus.png) |

### Subdomain

Raised field on the login page. Suffix ".zendesk.com" sits inside the right padding (120px).

| State | Fill | Ring | Crop |
|---|---|---|---|
| default | rgba(17, 17, 13, 0.05) | inset 1px rgba(17, 17, 13, 0.47) | [crop](components/crops/field-subdomain-default.png) |
| focus | rgba(17, 17, 13, 0.09) | inset 2px rgb(17, 17, 13), plus a 2px rgba(17, 17, 13, 0.47) outline offset 3px | [crop](components/crops/field-subdomain-focus.png) |

### Register email, already invalid

The page painted the error before any typing. `aria-invalid` was true. The ring is inset 2px rgb(184, 66, 66). The form was not submitted.

| State | Fill | Ring | Crop |
|---|---|---|---|
| error | rgba(17, 17, 13, 0.05) at rest; the later focus read was rgba(17, 17, 13, 0.11) | inset 2px rgb(184, 66, 66) | [crop](components/crops/field-email-error.png) |

### Help search

Pill search, 100px radius, white fill, inset 1px rgba(17, 17, 13, 0.47). Not queried.

| State | Size | Radius | Crop |
|---|---|---|---|
| default | 508×48 | 100px | [crop](components/crops/field-search-default.png) |

## Badge

"MOST POPULAR" on the Suite Professional card. Fill rgb(17, 17, 13), text white, 14px/700, letter-spacing 0.75px, uppercase, radius 40px, about 144×32.

[crop](components/crops/badge-popular-default.png)

## Dialog

The trial dialog on /register/ is white, 16px radius, shadow `rgba(0, 0, 0, 0.15) 0px 10px 50px 20px`, 692px wide. The cookie dialog is OneTrust, not Zendesk chrome.

[cookie crop](components/crops/dialog-cookie-default.png)

## Type

Display on the hero: 68px / 500 / 71.4px line height, colour rgb(245, 245, 242), family Vanilla Sans.

[crop](components/crops/type-display-default.png)

## Gaps

- The Platform menu opened on 2026-11-21 as a site-tree shot, not a measured crop. See [site-tree.md](site-tree.md).
- Pricing suite tabs were visible and not measured. The tab locator missed them.
- Contact textarea and select styles were read while the nodes were at 0×0 in one pass. The contact screenshot shows them. Their resting fill and radius match the raised field.
- Pressed states were forced with CSS `forcePseudoState`. A script-applied mousedown style is missing.
- Disabled, loading, toast, tooltip, table, avatar, switch and radio were not measured.
- Garden (garden.zendesk.com) is a separate design system. It is screenshotted and not tokenised here.
