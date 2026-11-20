# Components

Public signed-out Tango, measured on 2026-11-19 at a 1169 by 731 CSS viewport. Screenshots were not saved: `preview_snapshot` returned "The browser is not producing screenshot frames." Values below are computed styles.

## Button

Marketing buttons are pills. The radius token is `100vh`. At this viewport the computed radius is `731px`.

| State | Where | Values |
|---|---|---|
| Primary, header | "Get started for free" on https://www.tango.ai/ | background `#6f26d0`, white text, 16px / 400 Apercu Pro, padding 13.5px 19px, height 52.4px, radius 731px, 1.5px transparent border |
| Primary, hero | Same label under the home h1 | same face, padding 16px 21px, height 60.2px |
| Secondary | "See a demo" | transparent background, `#6f26d0` text, 1.5px solid `#6f26d0`, height 52.4px, radius 731px |
| Text | Header "Login" | black text, transparent background, height 24px, radius 731px, no visible border |
| Sales | "Talk to sales" on https://www.tango.ai/enterprise | background `rgb(255, 140, 73)`, black text, radius 731px, padding 16px 21px, height 60px |
| Selected toggle | "Annual pricing" on https://www.tango.ai/pricing | background `#f9650f`, white text, padding 8px 16px, height 38.8px, radius 731px |
| Unselected toggle | "Monthly pricing" | transparent background, `#383838` text, same size |
| App primary, enabled | "Continue" on https://app.tango.us/sign-up after a valid email | background `#6f26d0`, white text, 13px / 500, letter-spacing 0.1px, height 40px, radius 10px, padding 8px 16px, width 408px |
| App primary, disabled | "Continue" before the email is valid, and on https://app.tango.us/sign-up/email while name and password are empty | background `#e8e6ea`, text `#9b98a0`, cursor not-allowed |
| App tertiary | "Continue with Google" | transparent background, text `#5d1b98`, 1px border `#dec4f3`, radius 10px, height 40px, shadow `0 1px 2px rgba(0,0,0,0.05)`. Not followed |
| App text | "Create an account" and "Reset password" | transparent, text `#524d59`, height 40px, radius 10px, 13px / 500 |
| Help | "?" on the sign-in page | 48 by 48, radius 9999px, background `#e8e6ea`, text `#524d59` |

Hover, pressed and loading were not forced. The marketing stylesheet sets `.button:hover` to a transparent background with purple text and border. That state was not shown. App buttons transition `background, color, border, border-color, opacity, box-shadow` over `0.2s ease-in-out`.

## Link

Nav links ("Pricing", "Enterprise") are Apercu Pro 16px / 400, `#383838`, height 22px, no padding, no radius. Footer links are the same face at 16px, black. App legal links ("privacy policy") are 13px / 400, `#5d1b98`.

## Text field

https://app.tango.us/sign-in email: wrap is white, 1px border `#96949a`, radius 10px, height 36px, width 408px. The input itself is transparent, 13px / 400 Apercu, colour `#251f2d`, padding 8px 12px. Placeholder "Email" is `#c2c0c6`. Label "Work Email*" is 12px / 500, `#524d59`, letter-spacing 0.1px.

After a valid email was set, a password field appeared on the same page. Same wrap. The password input is 366px wide beside a 32 by 32 show button, radius 6px, icon colour `#75717b`. Nothing was submitted. The password was not typed.

Focus, measured on https://app.tango.us/sign-up after clicking the email field: wrap border `#6f26d0`, outline `3px solid #dec4f3`.

https://app.tango.us/sign-up/email repeats the email field (prefilled, not submitted) and adds first name and last name at 182px each, plus a password field. "At least 8 characters" is 12px, `#9b98a0`. Continue stayed disabled. The form was not submitted.

## Switch

Pricing "See Team plan" is `role=switch`, `aria-checked=false`. Track 32.1 by 18.5, white, 1px border `#6f26d0`, radius 11px, padding 2px. Knob 12.5px, `#6f26d0`, radius 731px. The checked state was not toggled.

## Tabs

"Annual pricing" and "Monthly pricing" are two buttons inside a white pill, padding 8px, radius 731px, shadow `0 1px 8px rgba(0,0,0,0.06)`. Annual is selected. Monthly was not clicked, so the price change was not measured.

## Card

Pricing cards on https://www.tango.ai/pricing: 340 by 567, padding 24px, radius 16px, background `#fafafa`. Free and Enterprise use a 1px `#989595` border. Pro uses a 1px `#f9650f` border. Prices are Gelica 35px / 400, black.

The sign-in page shows a public demo card labelled AnyApp, 314 by 224, 1px border `#e8e6ea`, radius 24px. It is a marketing illustration, not a signed-in dashboard.

## Table

The compare table on https://www.tango.ai/pricing is 952px wide, `border-collapse: collapse`, Apercu Pro 16px. Header cells are weight 700. Body cells measured with 0 padding. Row borders were not read individually.

## Icon button

The password visibility control is 32 by 32, radius 6px, colour `#75717b`. The Intercom "?" launcher is 48 by 48, radius 9999px. Neither was activated.

## Text area, select, radio, checkbox, menu, tooltip, dialog, toast, avatar, badge

Not present on the public pages that were opened. A purple "NEW" banner on https://www.tango.ai/enterprise is a 52px strip, background `#6f26d0`, text `#cbd5e1`. It is a banner, not a badge component. No validation error was shown: setting an invalid email and blurring did not change the field border or add an error message.

## App shell

Marketing header is fixed, 80px, transparent. App sign-in is a 404px panel, background `#faf9fa`, radius 32px, inside a 468px column. The rest of the viewport is the AnyApp demo.
