# Components

Public controls only. Values are the computed style, named with a token when one matches. A state that was not on the page is listed under Gaps.

## Button

Log in, home nav, 1440. White face, ink label, 30px radius, 44px tall, padding 12px. Eina 03 Bold 16px / 700.

| State | What changed |
|---|---|
| Default | Background `#ffffff`, text `#0c021c`. [components/crops/button-login-default.png](components/crops/button-login-default.png) |
| Hover | Background `#5216eb`, text `#ffffff` |
| Focus | Browser outline `rgb(0, 95, 204) auto 1px`. No product focus ring on this control. |

Sign up, home nav. Lime `#c4ee87`, ink label, 4px radius, padding 10px 12px, 44px tall. Hover background `#c6a5ff`. [components/crops/button-signup-default.png](components/crops/button-signup-default.png)

Generate, home prompt. Violet `#5318eb`, white label, 4px radius, 36px tall, padding 8px 12px 8px 16px. Mark Pro 14px / 400.

Continue with email, login wall, 21 November. `#6b53ff`, white label, 8px radius, 40px tall, padding 12px 0, Lato 14px / 500. On the empty signup arrival the button is painted at full colour with the captcha checkbox still empty. The 19 November crop shows the disabled look. [components/crops/button-continue-disabled.png](components/crops/button-continue-disabled.png) [screenshots/signup-light-default.png](screenshots/signup-light-default.png)

Continue with Google, Continue with Apple, Single sign-on (SSO). White face, `#2b2a35` label, 1px solid `rgba(43, 42, 53, 0.12)`, 8px radius, 40px tall, gap 8px.

Search, templates page. `#6b53ff`, white label, 8px radius, 40px tall, padding 8px 16px. Pitch-Lato-UI 14px / 500.

## Link

Nav links on the home hero are Eina 03 Regular 16px / 400, white, padding 12px, transparent. On the product page the same links are ink `#0c021c`. Footer links are 14px / 400, ink, line-height 22.4px.

Login text links are Lato 12px or 14px, `#6b53ff`, no underline in the computed style of the password link.

## Text field

Work email, login, at rest. White, 300 by 40, radius 8px, padding 0 8px, border `1px solid rgba(43, 42, 53, 0.12)`, no shadow. Placeholder `#939da8`. [components/crops/field-email-rest.png](components/crops/field-email-rest.png)

Focused. Border and shadow become `#6b53ff` (`--focus-box-shadow`). Text colour `#3f4250`.

Templates search. White, 460 by 40, radius 8px, padding 6px 12px 6px 42px, border `1px solid rgba(13, 14, 19, 0.1)`. Focused border and shadow `#6b53ff`. Placeholder `#8f92a3`.

Password field on `#/sign-in/email`. Same 40px field, padding 0 40px 0 8px, rest border `1px solid rgba(43, 42, 53, 0.12)`.

## Card

Login card. 560px wide, white, radius 12px, shadow `0 20px 80px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(0, 0, 0, 0.05)`. [components/crops/card-login.png](components/crops/card-login.png)

Plan card. 287px wide. Header radius 32px 32px 0 0, padding 16px 16px 64px. Body white, radius 32px, border `1px solid #ebe3fe`, padding 16px 16px 32px. [components/crops/card-plan.png](components/crops/card-plan.png)

| Plan | Header |
|---|---|
| Free | `#ebe3fe`, label `#280f62` |
| Plus | `#c6a5ff`, label `#0c021c` |
| Team | `#5318eb`, label `#ffffff` |
| Business | `#280f62`, label `#ffffff` |

Seat picker. White, radius 24px, padding 20px, border `1px solid #c6a5ff`.

## Badge

17% saving. `#5318eb` face, white label, radius 100px, padding 4px 12px, Eina 03 Regular 14px / 700.

New, on a template card. White label, radius 30px, padding 3px 9px, 9px / 700. The computed background was transparent, so the fill is a gap.

## Gaps

- Pressed, loading, and error states of buttons were not on the page.
- Text area, select, checkbox, radio, switch, menu, tooltip, dialog, toast, list row, table and avatar were not on the public pages.
- The nav dropdowns were not opened.
- The New badge fill did not compute to a colour.
- No dark theme was shown.
