# Components

Crops are 2x slices of the headless screenshots. Values are the computed styles from the T3 preview browser on 19 November 2026.

## Button

Primary marketing button. Fill `#ff891c`, label `#ffffff`, radius 30px, padding 10px 22px, height 47px. Label is DM Sans 18px weight 500.

![Start for Free](components/crops/button-primary-default.png)

Outline variant on the home page. White fill, 3px `#ff891c` border, orange label, radius 30px, height 53px. Text was "View integration".

Hover is declared as `#db7414` on `.buttonprimary:hover`. A live hover was not held. Pressed, disabled and loading were not on the page.

## OAuth button

Signed-out login. White fill, 1px `#dcdcdc` border, radius 4px, height 45.3px, padding 11px 20px, width 320px, ink `#413f39`, Avenir 15px weight 500. Google, Outlook and SSO share that chrome. They were not clicked.

![Log in with Google](components/crops/button-oauth-google.png)

## Email button

`button.onboarding-btn-secondary`. Fill `#d2d2d2`, text `#ffffff`, radius 4px, height 45.3px. It was not disabled. It was not clicked.

![Log in with email](components/crops/button-email-default.png)

## Text field

Email input, focused. Border 1px solid `#8cb4f0`, radius 4px, height 42.5px, padding 11px 14px. Placeholder `jane@company.com` in `#b4b4b4`. That string is the product's example.

![Email field](components/crops/field-email-focus.png)

Password field at rest. Border 1px solid `#dcdcdc`. Placeholder `password`. Nothing was typed.

![Password field](components/crops/field-password-default.png)

Marketing newsletter field computed radius 20px, padding 8px 12px, height 38px, transparent background. It was not focused and was not submitted.

## Tabs

Login and Sign up. Active tab ink `#413f39`, weight 600, 2px bottom border. Inactive `#787878`, weight 500. Bar is 1px `#dcdcdc`. Sign up was not opened.

![Log in and Sign up](components/crops/tabs-login.png)

## Card

Login card. `#ffffff`, radius 16px, padding 40px, 400 by 576 CSS pixels, on page `#f7f8fa`. Shadow `rgba(0, 0, 0, 0.04) 0px 1px 2px 0px, rgba(0, 0, 0, 0.06) 0px 12px 32px 0px`.

![Login card](components/crops/card-login-default.png)

Pricing card. Radius 12px, padding 32px, shadow `rgba(29, 31, 39, 0.1) 0px 16px 30px 0px`. The muted modifier computed `#ffffff` at alpha 0.5.

Feature card on the home page. `#f8f8f8`, radius 24px, padding 32px, border 1px `#0000001f`.

Subfeature card. `#fafafa`, radius 10px, border 1px `#f2f2f2`.

## Link

Recover password. `#2ca7ff`, Avenir 13px weight 500. Not clicked.

Nav links. DM Sans 15px weight 400, colour `#000000`. The Login nav item is a pill with radius 50px and padding 4px 12px.

## Badge

Home `.badge` computed a 1px `#f59549` border and radius 48px. `.badge-label` uses a clipped gradient from `#ff891c` to `#f06351`.

## Gaps

| Component | Status |
|---|---|
| Button hover, pressed, disabled, loading | Hover colour is declared (`#db7414`). Not held live. Pressed, disabled and loading were not on these pages. |
| Icon button | Not present on the captured pages. |
| Text area, select, checkbox, radio, switch | Not present on the captured pages. |
| Menu, tooltip, dialog, toast | Not opened. The cookie banner was dismissed before measurement. |
| Table | Pricing comparison grid is further down the pricing page. Not cropped. |
| Avatar | Marketing portraits are photography. Not a component crop. |
| Validation error | Declared border `#f25a43` on `.text-input-light.alert`. The form was not submitted. |
| Dark theme | Login CSS has `.dark` rules. The signed-out page had no dark class. |
