# VSCO components

Public marketing site and the login wall, measured 2026-11-21. Values are token names. Crops are the live elements.

| Component | States | Crop | Notes |
|---|---|---|---|
| accordion | default, selected | [components/crops/accordion-default.png](components/crops/accordion-default.png) | Plans FAQ row. Selected opens the answer on the same page. No dialog. |
| badge | default | [components/crops/badge-default.png](components/crops/badge-default.png) | 4px radius. The NEW chip in the promo bar. |
| button-banner | default, hover | [components/crops/button-banner-default.png](components/crops/button-banner-default.png) | Fill `light.accent.pink`. Hover fill `light.accent.pinkHover` and the label went grey. |
| button-gold | default, hover, pressed | [components/crops/button-gold-default.png](components/crops/button-gold-default.png) | Fill `light.accent.gold`, text `light.text.onGold`, height `core.size.button`, radius `core.radius.pill`. Hover fill `light.accent.goldHover`. |
| button-gold-focus-visible | default | [components/crops/button-gold-focus-visible-default.png](components/crops/button-gold-focus-visible-default.png) |  |
| button-primary | default, hover | [components/crops/button-primary-default.png](components/crops/button-primary-default.png) | Fill `light.action.primary`, text `light.text.onAccent`, height `core.size.buttonSmall`. Hover computed style did not change. |
| button-primary-focus-visible | default | [components/crops/button-primary-focus-visible-default.png](components/crops/button-primary-focus-visible-default.png) |  |
| card | default | [components/crops/card-default.png](components/crops/card-default.png) | What's new card on the dark band. |
| drawer-link | default | [components/crops/drawer-link-default.png](components/crops/drawer-link-default.png) | PRICING in the phone drawer. |
| hero-heading | default | [components/crops/hero-heading-default.png](components/crops/hero-heading-default.png) | 100px / 500, black, two lines at 90px line height. |
| icon-button | default, pressed | [components/crops/icon-button-default.png](components/crops/icon-button-default.png) | Phone menu control, 24px. |
| menu-link | default, hover | [components/crops/menu-link-default.png](components/crops/menu-link-default.png) | Opens from PRODUCTS. 16px / 400. Transition 450ms. |
| nav-menu | default, hover, pressed | [components/crops/nav-menu-default.png](components/crops/nav-menu-default.png) | 15px / 500, transparent, 8px vertical padding. Focus-visible paints a 1px auto outline. |
| nav-menu-focus-visible | default | [components/crops/nav-menu-focus-visible-default.png](components/crops/nav-menu-focus-visible-default.png) |  |
| plan-cta | default | [components/crops/plan-cta-default.png](components/crops/plan-cta-default.png) | SELECT VSCO ONE. Not clicked. Purchase path. |
| tab | default, selected | [components/crops/tab-default.png](components/crops/tab-default.png) | 11px / 600, white on the dark band. Selected is a local pane, not a route. |
| text-field | default, focus | [components/crops/text-field-default.png](components/crops/text-field-default.png) | Login email input when the password form loaded. The later visit to the same URL showed an email-only step instead. |
| text-field-password | default | [components/crops/text-field-password-default.png](components/crops/text-field-password-default.png) |  |

## Gaps

- Text area, select, checkbox, radio, switch, tooltip, toast, table, avatar: not present on the captured public pages.
- Dialog: the OneTrust preference center exists and was not opened. No product dialog was opened.
- Disabled, error, and loading on marketing buttons: not present. The login CONTINUE button is disabled until an email is typed. Email was not typed.
- Hover on the ink button did not change computed color. Gold and pink did.
- Focus ring colour is the browser auto outline, not a custom colour.
