# Components

Measured on the public signed-out site, 2026-11-19, at 1440×900. Crops are element screenshots from headless Chromium. The T3 preview browser loaded the page but returned no screenshot frames.

| Component | States captured | Source |
|---|---|---|
| Primary button | default, hover, focus | [button-primary-default.png](components/crops/button-primary-default.png) |
| Login link | default, hover | [link-login-default.png](components/crops/link-login-default.png) |
| Hero heading | default | [heading-hero-default.png](components/crops/heading-hero-default.png) |
| Text field | default, focus (book-demo, not submitted) | [field-text-default.png](components/crops/field-text-default.png) |

## Button

Nav "Get started" (`a.button.is-small`): background `#090b22`, text `#ffffff`, 14px weight 500, padding `8px 16px`, radius `8px`, height 38px, shadow `rgba(16, 24, 40, 0.08) 0px 2px 10px 0px`. Hover and keyboard focus both paint `rgba(13, 15, 44, 0.8)`.

Hero "Get started for free" is the same fill at 16px, padding `12px 18px`, radius `10px`, height 48px.

Secondary "Book demo" is white with an inset `1px` ring `#dadadd`, text `#090b22`, radius `10px`.

## Link

Nav "Log in" is a text link, not a button: 16px, `#68686a`, transparent background. Hover paints `#090b22`.

## Text field

Book-demo fields are 478×48, white, 16px, radius `8px`, required first name, last name, work email, phone, and job title. Focus did not change the computed border colour in this read. The form was not submitted.

## Gaps

Checkbox, radio, switch, select open state, tabs selected state, menu, tooltip, dialog, toast, avatar, badge, and table were not isolated. Pricing uses a tab strip and a four-column table, captured only as the page screenshot. Disabled, loading, error, and pressed states were not on the public pages. The signed-in app was not entered.
