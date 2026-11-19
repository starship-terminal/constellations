# Components

Public controls only. Values are the computed style, named with a token when one matches. A state that was not on the page is listed under Gaps.

## Button

Schedule a demo, home nav. Ink face `#1a1a1a`, paper label `#fafafa`, radius 10px, padding 8px 16px 10px, 42px tall. Stabil Grotesk 15px / 600, letter-spacing -0.32px. [components/crops/button-schedule-demo-default.png](components/crops/button-schedule-demo-default.png)

Get started, home nav. Paper face `#fafafa`, label `#434140`, border `0.5px solid #dadbdf`, radius 10px, padding 8px 16px 10px, 42px tall. [components/crops/button-get-started-default.png](components/crops/button-get-started-default.png)

Plan CTA, pricing. Paper face, heading label `#222222`, border `0.5px solid #dadbdf`, radius 10px, padding 10px 16px 12px, 42px tall, 14px / 600. The label is Sign up or Start for free. [components/crops/button-plan-signup.png](components/crops/button-plan-signup.png)

Request a trial, Enterprise plan. Ink face `#1a1a1a`, paper label, radius 10px, padding 10px 16px 12px, 42px tall. [components/crops/button-plan-solid.png](components/crops/button-plan-solid.png)

Continue with Google and Continue with Apple, sign-in. White face, label `#262626`, border `1px solid #ebecef`, radius 14px, padding 12px 20px, 48px tall. Akkurat 16px / 600, letter-spacing -0.16px. [components/crops/button-google-default.png](components/crops/button-google-default.png)

Continue with email, sign-in, disabled. Face `#f5f6f7`, label `#c4c8d1`, border `1px solid transparent`, radius 14px, 48px tall, cursor `not-allowed`. [components/crops/button-continue-disabled.png](components/crops/button-continue-disabled.png)

| State | What changed |
|---|---|
| Default | As above |
| Hover | Not measured. The marketing sheet declares `--pb-hover-dur: .15s` and hover fills of `rgb(255 255 255 / .1)` and `rgb(0 0 0 / .1)`. |
| Focus | Not measured on a button. |
| Disabled | Continue with email, above. |
| Pressed, loading | Not on the page. |

## Link

Home nav links are Stabil Grotesk 16.366px / 600, letter-spacing -0.32px, colour `rgba(255, 255, 255, 0.85)`.

Read the docs and Book a demo, under the hero, are 14px / 400, colour `rgba(255, 255, 255, 0.85)`.

Sign-in Terms, Privacy and Community Guidelines are Akkurat 12px / 400, colour `#a1a5b0`, underlined.

## Text field

Hero prompt, home. The textarea is transparent, 18px / 400, white text, line-height 27px, placeholder "e.g. Tag new product photos and publish the approved ones". The wrapper is `rgba(10, 11, 13, 0.55)`, radius 18px, padding 14px 10px 10px 18px, inset shadow `rgba(255, 255, 255, 0.35) 0px 0.5px 0px 0px, rgba(255, 255, 255, 0.14) 0px 0px 0px 0.5px`. [components/crops/field-prompt-rest.png](components/crops/field-prompt-rest.png)

Work email, sign-in, focused. The input is 342 by 48, transparent, padding 0 4px 0 10px, 17px / 400, placeholder `name@email.com`. The wrapper is white, 350 by 50, radius 10px, border `1px solid #262626`, padding 0 6px 0 0. No box-shadow. [components/crops/field-email-focused.png](components/crops/field-email-focused.png)

The Work email label is 12px / 700, colour `#888c97`.

## Tabs

Billing period, pricing. The track is `#fafafa`, border `0.5px solid #dadbdf`, radius 12px, padding 4px, 42px tall. Yearly is the selected label, `#222222`, 14px / 600, radius 8px. Monthly is `#979797`. [components/crops/tabs-billing.png](components/crops/tabs-billing.png)

## Card

Plan card. White, border `0.5px solid #dadbdf`, radius 17.535px, padding 6px. The top is `#f9f9f9`, radius 11.535px, padding 20px. The name is 24px / 600, letter-spacing -0.72px, colour `#222222`. The amount is 40px / 600, letter-spacing -1.2px. The blurb is 12px / 500, colour `#979797`. A feature row has a dashed `#eeeeee` bottom border and 14px / 500 text. [components/crops/card-plan.png](components/crops/card-plan.png)

| Plan | Price on the yearly view | CTA |
|---|---|---|
| Free | $0 always | Sign up, paper |
| Pro | $10 /month/member | Start for free, paper |
| Team | $20 /month/member | Start for free, paper |
| Enterprise | Custom | Request a trial, ink |

Preview card. Radius 16px, shadow `rgba(60, 60, 60, 0.05) 0px 10px 24px 0px`. The title is 15px / 600 white. The description is 13px / 500, `rgba(255, 255, 255, 0.85)`.

Solutions bento. The large card is `#1a1a1a`, radius 14px, padding 16px, white text. The small cards are `#f9f9f9`, border `0.5px solid #ebecef`, radius 14px, padding 14px, text `#434140`.

## Badge

New, beside MCP. Transparent face, text `rgba(255, 255, 255, 0.85)` on the home nav and `#434140` on the pricing nav, border `1px solid #434140` on pricing, radius 4.41882px, padding about 1px 4px, 9.8196px / 600. [components/crops/badge-new.png](components/crops/badge-new.png)

## Chip

Prompt examples under the hero. Face `rgba(24, 25, 29, 0.94)`, text `#d9dbe1`, radius 999px, padding 6px 11px 8px, 14px / 400, 32px tall. [components/crops/chip-prompt-default.png](components/crops/chip-prompt-default.png)

## Gaps

- Hover, pressed and loading were not on the page. The marketing sheet names a 150ms hover and 10% white or black hover fills. Those were not confirmed on a control.
- The email field was already focused when the page was read. The rest border was not measured.
- Continue with email stays disabled until an address is present. Nothing was typed, so the enabled colour was not painted. `--primaryColor` is `#ff5d64`.
- Google and Apple were not followed. No password step, no error, no toast.
- No checkbox, radio, switch, select, text area outside the hero prompt, menu (the nav menus were not opened), tooltip, dialog, table, avatar or list row was on these pages.
- The sign-in page declares toast colours (`--toastify-color-error` `#dc3636`, `--toastify-color-success` `#7bd067`, `--toastify-color-warning` `#e8f247`). No toast was shown.
