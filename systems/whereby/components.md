# Components

Measured on the public marketing site and the signed-out login on 19 November 2026. Crops are from the 2x screenshots.

| Component | State | Values | Crop |
|---|---|---|---|
| Button, primary | Default | Fill `#2B189B`, label `#FFFFFF`, Inter 16 / 500, height 48px, radius 12px | [button-primary.png](components/crops/button-primary.png) |
| Button, primary | Hover | Fill `#221479` on Sign up. Label stays white. | Not cropped. Reading is in [raw/deep.json](raw/deep.json). |
| Button, secondary | Default | 1px stroke `#2B189B`, label `#2B189B`, height 48px, radius 12px. Computed `border` was `none`; the stroke was sampled from the screenshot. | [button-secondary.png](components/crops/button-secondary.png) |
| Link | Default | Login "Sign up for free" is `#2B189B`, 18px, underlined. | Not cropped. |
| Text field | Rest | White fill, `1px solid rgba(0, 0, 0, 0.12)`, radius 12px, padding 15px 16px, height 58px, input 18px Inter var. Placeholder `name@email.com`. | Not cropped. Login was not screenshotted. |
| Text field | Focus | Border and inset shadow `rgb(43, 24, 155)`. Email was focused and not submitted. | Not cropped. |
| OAuth button | Default | Transparent fill, `1px solid rgb(0, 0, 0)`, radius 12px, height 56px, padding 5px 40px, 18px. Google and Apple were not clicked. | Not cropped. |
| Billing switch | Monthly selected | Track white, radius 80px, shadow `rgba(0, 0, 0, 0.08) 0px 1px 4px`. Active label `#2B189B` 16 / 500. Inactive `rgba(0, 0, 0, 0.56)`. | Visible in [screenshots/meetings-pricing-light-default.png](screenshots/meetings-pricing-light-default.png). |
| Card, plan | Default | 384 by 644, white, radius 12px, shadow `rgba(0, 0, 0, 0.16) 0px 1px 4px, rgba(0, 0, 0, 0.16) 0px 8px 16px`. | [card-plan.png](components/crops/card-plan.png) |
| Accordion | Closed and open | Question Inter 18 / 27, row padding 16px 0, row height 72px. One answer was opened on the pricing index. | [raw/faq-open.json](raw/faq-open.json) |
| Nav | Desktop | Height 96px, padding 0 24px, labels Inter 18 / 400. | [logo.png](components/crops/logo.png) |
| Nav | Phone | Hamburger opens a white sheet. Login and Try for free sit at the bottom. | [screenshots/home-light-phone-menu.png](screenshots/home-light-phone-menu.png) |

## Gaps

- Checkbox, radio, switch (on/off), select, tabs (beyond the billing pill), menu (desktop dropdown was not isolated), tooltip, dialog, toast, table, avatar, badge (the Save 17% mark was not isolated as a painted box), icon button, text area, loading, disabled, pressed, and error states were not on the signed-out pages that were measured.
- The desktop Products menu click did not isolate a dropdown panel in the reading.
- Marketing button focus-visible was the browser outline `rgb(0, 95, 204) auto 1px` on the logo link after Tab. A designed focus ring was measured only on the login field.
