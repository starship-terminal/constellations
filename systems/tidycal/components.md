# Components

Public marketing controls measured on tidycal.com, plus the signed-out login and register forms. Crops are 2x screenshots from headless Chrome. Values come from computed styles.

| Component | State | Evidence |
|---|---|---|
| Button, primary | Default | [button-primary-default.png](components/crops/button-primary-default.png). Fill `#1569ef`, label `#ffffff`, radius 8px, height 41px, padding 8px 12px, 15px weight 500. Nav size is 30px, padding 4px 16px, 13px. [button-nav-default.png](components/crops/button-nav-default.png) |
| Button, primary | Hover | [button-primary-hover.png](components/crops/button-primary-hover.png). The register submit did not change fill on hover. The sheet sets `.hp-2026 .btn-primary:hover` to `#0e58cd`. [button-nav-hover.png](components/crops/button-nav-hover.png) |
| Button, OAuth outline | Default | [button-oauth-default.png](components/crops/button-oauth-default.png). Transparent fill, label `#212529`, 1px border `#212529`, radius 8px, height 41px, padding 8px 12px. |
| Button, OAuth outline | Hover | [button-oauth-hover.png](components/crops/button-oauth-hover.png). Computed fill stayed transparent. |
| Button, Google SSO | Default | [button-sso-default.png](components/crops/button-sso-default.png). Fill `#1a73e8`, label `#ffffff`, 1px border `#e5e7eb`, radius 8px, height 60px, padding 14px 20px, 19px weight 500. |
| Button, Google SSO | Hover | [button-sso-hover.png](components/crops/button-sso-hover.png). The sheet sets hover fill `#f9fafb`. The live button stayed blue. |
| Button, deal | Default | [button-deal-default.png](components/crops/button-deal-default.png). Fill `#ffbc00`, sampled from the home PNG. Pricing AppSumo button uses the same `#ffbc00`, label `#1f2937`. Hover computed `#d69e00`. [button-appsumo-default.png](components/crops/button-appsumo-default.png) [button-appsumo-hover.png](components/crops/button-appsumo-hover.png) |
| Link, nav | Default | [link-nav-default.png](components/crops/link-nav-default.png). 13.125px weight 500, `#212529`, no underline. |
| Link, inline | Default | [link-inline-default.png](components/crops/link-inline-default.png). Color `#0053ee`, no underline. [link-inline-hover.png](components/crops/link-inline-hover.png) |
| Text field | Default | [field-email-default.png](components/crops/field-email-default.png). Fill `rgba(100, 109, 118, 0.09)`, transparent border, radius 8px, height 41px, padding 8px 12px, inset shadow. |
| Text field | Focus | [field-email-focus.png](components/crops/field-email-focus.png). Same fill, plus `0 0 0 3px rgba(0, 83, 238, 0.2)`. |
| Checkbox | Unchecked | [checkbox-default.png](components/crops/checkbox-default.png). 22px, radius 6px, fill `#ffffff`, 2px border `#ced4da`. The checked rule in the sheet sets fill `#0053ee`. It was not clicked. |
| Badge | Plan | [badge-plan-default.png](components/crops/badge-plan-default.png). Fill `#ffffff`, text `#1569ef`, 1px border `rgba(21, 105, 239, 0.2)`, radius 20px, padding 8px 16px, 12.8px weight 500. |
| Badge | Upsell | [badge-upsell-default.png](components/crops/badge-upsell-default.png). Fill `#1569ef`, text `#ffffff`, radius 20px. |
| Card | Plan | [card-plan-default.png](components/crops/card-plan-default.png). Fill `#ffffff`, radius 16px, shadow `0 6px 24px rgba(0, 0, 0, 0.08)`. Auth card uses the same radius and `0 8px 32px rgba(0, 0, 0, 0.08)`. |
| Eyebrow | Default | [label-eyebrow-default.png](components/crops/label-eyebrow-default.png). 12px weight 700, letter-spacing 0.96px, uppercase, `#1569ef`. |

## Gaps

- Icon button, text area, select, radio, switch, tabs, menu, tooltip, dialog, toast, avatar, and table were not measured as product controls. Pricing has a Monthly/Yearly control. Its computed styles were not recorded as a crop.
- The FAQ accordion did not match `.accordion-button` on the pricing page, so it was not opened.
- Disabled, pressed, loading, and error states were not on these pages.
- Signup, login, password reset, Google, LinkedIn, and checkout were not submitted.
- Dark theme rules exist under `html[data-bs-theme=dark]` and were not on the public pages.
