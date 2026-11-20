# Relume components

Public marketing chrome and the signed-out login form, measured 19 November 2026. Crops are 2x PNGs, quantised to 256 colours.

## Button

Primary action is `.p-button.is-ai`. Background `#ff00f4`, label white, radius 6px, padding 6px 12px, height 32px, label 14px / 20px, gap 6px. Used for "Start for free", "Generate Website", and the login "Continue" button.

| State | Evidence |
|---|---|
| Default | [button-primary-default.png](components/crops/button-primary-default.png) |
| Hover | Computed background stayed `#ff00f4`. Transform became scale(1.03). Declared hover is `#ff29f6` and did not win. [button-primary-hover.png](components/crops/button-primary-hover.png) |
| Focus-visible | Not captured. Keyboard focus on "Log in" left `outline: none`. |
| Pressed | Not held. Declared press overlay is `#1616161f`. |
| Disabled | Not on the captured pages. Declared disabled is `#b9b9b9`. |
| Loading | Not on the captured pages. |

Secondary is `.p-button.is-secondary`. Transparent fill, 1px border `rgba(27, 25, 25, 0.1)`, text `#101010`, radius 6px, height 34px. Hover fill measured `rgba(22, 22, 22, 0.08)` plus scale(1.03).

| State | Evidence |
|---|---|
| Default | [button-secondary-default.png](components/crops/button-secondary-default.png) |
| Hover | [button-secondary-hover.png](components/crops/button-secondary-hover.png) |

Icon button `.p-button.is-icon-only` is 34px square, padding 9.2px, radius 6px. The theme control uses muted text `#5c5c5c`.

## Link

Nav links are `a.p-navbar_link`. 14px, weight 400, colour `#101010`, padding 4px 8px, radius 6px. Hover fill measured `rgba(22, 22, 22, 0.06)` and scale(1.03). Transition is transform 0.2s ease-out.

[link-nav-default.png](components/crops/link-nav-default.png)

Text links such as "Try an example" are 14px weight 500, colour `#343434`, no underline at rest. Transition is colour and text-decoration-colour 0.2s ease-out.

## Text field

The homepage composer is a textarea inside `form.p-composer_form`. The form is 640px wide, fill `rgba(255, 255, 255, 0.8)`, 1px border `rgba(27, 25, 25, 0.1)`, radius 16px, backdrop blur 10px. The textarea has no border or radius of its own, padding 20px, type 16px / 24px.

[card-composer-default.png](components/crops/card-composer-default.png)

[field-composer-default.png](components/crops/field-composer-default.png)

The login email input is 14px, placeholder colour `#343434`, radius 6px, padding 0 4px, height 20px. Its surrounding field chrome was not separated from the input in the crop.

[field-email-default.png](components/crops/field-email-default.png)

## Text area

The composer textarea is the only text area on the captured pages. See the field above.

## Other controls

| Component | Status |
|---|---|
| Select | Not on the captured pages. A select trigger class exists in the stylesheet and was not painted. |
| Checkbox, radio, switch | Not on the captured pages. Pricing has a 999px pill that was not opened. |
| Tabs | Composer switch tabs exist in the DOM class list. Their resting and selected styles were not measured as a separate state. |
| Menu | Products dropdown links are in the DOM at 0px height until opened. Not captured open. |
| Tooltip | Not captured. |
| Dialog | Not captured. Cookie banner markup is in the page and did not cover the viewport screenshot. |
| Toast | Declared toast background `#101010cc` was not painted. |
| Card | Composer card above. Pricing hosting container is 1280 by 732, radius 12px, no shadow. |
| List row | Not captured. |
| Table | Not on the captured pages. |
| Avatar | Not on the captured pages. |
| Badge | Not measured as its own control. |

## Gaps

- No dark theme painted. `prefers-color-scheme: dark` left `html` on `data-theme` light and the page background `#f1f0ee`.
- Focus ring was `outline: none` on the secondary button. No focus-visible ring was measured.
- Primary hover colour `#ff29f6` is declared and did not apply under a real hover. Recorded as a gap between the stylesheet and the computed style.
- Pressed, disabled, loading, and error states were not on the pages.
- Login was not submitted. The form asks for a password and offers Google and SSO.
