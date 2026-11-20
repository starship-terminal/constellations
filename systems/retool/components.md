# Components

Values come from `getComputedStyle` in the T3 preview tab on 2026-11-19. Viewport was 1169 by 731, devicePixelRatio 2. The preview browser did not produce screenshot frames, so there are no crops. Token names point at [tokens.json](tokens.json).

## Button

Marketing primary. `Start for free` on [https://retool.com/](https://retool.com/) and `Get started for free` on [https://retool.com/pricing](https://retool.com/pricing).

| Property | Value | Token |
|---|---|---|
| Background | rgb(233, 235, 223) | `dark.button` |
| Text | rgb(21, 21, 21) | `dark.button-text` |
| Font | pxGroteskFont, 12.6971px, weight 400, line-height 15.2365px | `core.typography.caption` |
| Padding | 0 20px | `core.spacing.5` |
| Height | 40px | `core.spacing.button` |
| Radius | full pill | `core.radius.pill` |
| Border | 0 | |
| Shadow | none | |
| Focus | outline rgb(21, 21, 21) auto 1px, offset 1px | `dark.focus` |

Hover was declared as `#ffffff` (`dark.button-hover`) and was not held.

Marketing secondary. `Book a demo`. Transparent fill, text rgb(233, 235, 223), 1px solid rgb(139, 134, 127), same height and pill radius. Token `dark.border-strong`.

Login primary. `Sign in` on [https://login.retool.com/auth/login](https://login.retool.com/auth/login).

| Property | Value | Token |
|---|---|---|
| Background | rgb(21, 21, 21) | `core.color.login.button` |
| Text | rgb(247, 248, 244) | `core.color.login.button-text` |
| Font | Inter, 15px, weight 600 | `core.typography.button` |
| Padding | 12px 6px | |
| Height | 44px | `core.spacing.login-button` |
| Radius | 6px | `core.radius.login-button` |
| Shadow | none | |

Google button. White fill, 1px solid rgb(235, 235, 235), height 36px, radius 8px, shadow rgba(0, 0, 0, 0.04) 0 1px 2px. Token `core.shadow.login-google`. Google was not clicked.

Prompt submit. 40 by 40 circle, fill rgb(81, 141, 210), icon rgb(233, 235, 223). Token `dark.accent`. It was not clicked.

## Icon button

The pause-video control is 30 by 30, padding 2px, full pill, 1px solid rgba(233, 235, 223, 0.12). No separate crop.

## Link

`Sign in` in the marketing nav is a text button: transparent, pxGroteskFont 12.6971px, padding 0 12px, height 40px, color rgb(233, 235, 223).

`Sign up` on the login page is Inter 13px, weight 400, color rgb(21, 21, 21).

## Text field

Login email. Placeholder `name@company.com`. Fill rgb(247, 248, 244), text rgb(21, 21, 21), Inter 16px, weight 400, line-height 18.4px, height 40px, padding 16px, radius 8px, no border. Focus outline rgb(81, 141, 210) solid 2px, offset 2px. Tokens `core.color.login.field` and `core.color.login.focus`. The field was focused and then blurred. Nothing was typed.

Password uses the same fill, height and radius. It was not typed in.

Signup shows `Work email` and `Password`. Those were not measured as a second set and were not filled.

Marketing prompt field was not a native input in the reading. The starter-prompts chip is 26px tall, radius 8px, fill rgba(21, 21, 21, 0.063), border 1px solid rgba(21, 21, 21, 0.12).

## Text area

Not present on the pages that loaded.

## Select

Not present on the signed-out pages that loaded.

## Checkbox

Not present.

## Radio

Not present.

## Switch

Not present on Retool's own pages. The docs theme control exists and was not used.

## Tabs

Docs top nav labels `Build`, `Automate`, `Code`, `Manage`, `Host` were visible. Their selected state was not measured as a separate crop.

## Menu

Marketing `Solution`, `Audience` and `Resources` are buttons. They were not opened.

## Tooltip

Not present.

## Dialog

Not opened. Book a demo was not followed. Ask AI was not opened.

## Toast

Not present.

## Card

Pricing plan card. Border 1px rgba(233, 235, 223, 0.2), radius 12px, header padding 24px. Plan name saansFont 21.3942px, weight 380. Muted line rgb(203, 204, 196) at 14px, weight 300. Token `core.radius.card`.

Docs banner. `New Cloud signups are temporarily paused`. Radius 10px, padding 10px 16px, border 1px rgb(158, 129, 89), text rgb(233, 235, 223), 14px, weight 500. Its fill was `color(srgb 0.179451 0.170353 0.157804)`, left as a gap rather than converted.

## List row

Not captured as a component. Footer link lists were not measured row by row.

## Table

Pricing comparison table. `border-collapse: collapse`. Header cell background rgb(21, 21, 21), padding 16px 24px. Body cell color rgb(233, 235, 223), padding 16px 32.4722px, size 16px.

## Avatar

Not present.

## Badge

`NEW` chip on the homepage: pxGroteskFont 12px, weight 400, line-height 14.4px, letter-spacing 0.12px, color rgb(21, 21, 21). Its parent fill was not isolated.

## Gaps

- No screenshots and no crops. `preview_snapshot` returned `The browser is not producing screenshot frames`.
- Hover, pressed, disabled, loading and error states were not on screen. Login was not submitted, so no validation error was read.
- Light marketing is a class probe. The live homepage, pricing and docs were dark.
- Text area, select, checkbox, radio, switch, tooltip, toast, avatar and dialog were not captured.
- Docs `--ifm-color-primary` and `--ifm-link-color` computed empty. They are a gap.
- Saans, PX Grotesk and the wordmark were not saved as files.
