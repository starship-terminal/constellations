# Steel components

Measured with `getComputedStyle` on 2026-11-19. The preview browser returned "The browser is not producing screenshot frames", so this file has no crops.

## Button

Marketing actions use `a.steel-button`.

| State | Where | Values |
|---|---|---|
| Primary | Home "START FOR FREE" | 36px tall, padding `0px 9px 0px 12px`, radius 6px, background `color(display-p3 0.933 0.933 0.926)` painted `#eeeeec`, text `rgb(20, 20, 20)`, schengenAMono 12px, letter-spacing 0.18px |
| Sign in | Header "SIGN IN" | 32px tall, padding `0px 7px 0px 12px`, radius 6px, background `#ffffff`, text `#000000` |
| Quiet | Header "CONTACT SALES" | 32px tall, radius 6px, background `color(display-p3 0.135 0.135 0.129)`, text `color(display-p3 0.933 0.933 0.926)` |
| Plan | Pricing "GET STARTED" | 36px tall, 501px wide, radius 6px, same primary face |
| Scale plan | Pricing "START SCALING" | background `#ffffff`, text `rgb(0, 198, 197)` on the `#00c6c5` card |
| Enterprise | Pricing "CONTACT SALES" | background `rgb(249, 235, 115)`, text `rgb(121, 51, 135)` |
| Auth primary | "Sign in with GitHub" and the email submit | 36px tall, 392px wide, padding `0px 14px`, radius 6px, background `rgb(238, 238, 236)`, text `rgb(17, 17, 16)`, Inter 13px weight 500, letter-spacing -0.13px |
| Auth secondary | "Sign in with Google", "Sign in with email" before the form opens | background `rgb(34, 34, 33)`, text `rgb(238, 238, 236)` |
| Docs | "Sign in" | 28px tall, radius 6px, background `#222221`, Inter 13px weight 500 |
| Focus | "START FOR FREE" after `element.focus()` | outline `rgb(5, 165, 255) solid 1px` |
| Hover | mouseover events on Start for free and Contact sales | computed background did not change |
| Pressed, disabled, loading | not shown | Not captured |

## Link

Nav links are schengenAMono 12px, letter-spacing 0.18px, radius 6px, padding `0px 12px`, height 32px. On the home hero, "PRICING" computed `color(srgb 0.129412 0.12549 0.109804 / 0.7)`. On pricing, the current "PRICING" link computed `rgb(255, 255, 255)`.

The announcement bar is a full-width link, 36px tall, background `rgb(5, 165, 255)`, text `rgb(255, 255, 255)`, schengenAMono 12px, padding `0px 16px`.

## Text field

Auth email input, after "Sign in with email": type email, name email, placeholder "Email address", 392 by 36, radius 6px, padding `0px 12px`, background `rgb(42, 42, 40)`, text `rgb(238, 238, 236)`, Inter 13px weight 500. Filled with an email address, then cleared. Not submitted.

Docs search control: 270 by 27, radius 4px, padding `0px 8px 0px 6px`, Inter 13px weight 500, text `#b4b3ad`.

## Badge

Pricing "POPULAR": 68 by 20, padding `2px 8px`, radius 2px, background `rgb(191, 240, 239)`, text `rgb(0, 128, 127)`, schengenAMono 12px.

## Card

Pricing plan columns are 549px wide. The Scale column's painted face is `rgb(0, 198, 197)` with 24px padding and 6px radius. Launch's painted face is `color(display-p3 0.098 0.098 0.094)`.

## Table

Pricing has six comparison tables. A body cell is 16px schengenA, padding `14px 16px`, line-height 24px. Border colour computed as `--line-subtle`, painted `#2d2c2a` on black.

## Menu

At 390px CSS width, the header shows a 32px "Menu" button. After click, a panel 390 by 844 used background `color(display-p3 0.164 0.163 0.156)` and listed Browser infra, Pricing, Resources, Docs, Contact sales, and Sign in.

## FAQ

Home questions are buttons, 76px tall, schengenA 20px weight 400, transparent background. They were not opened.

## Not present on the pages opened

Text area, select, checkbox, radio as a product control (the theme switcher is three 1px radios), switch, tabs, tooltip, dialog, toast, avatar, list row.

## Gaps

Hover did not change computed colour. Pressed, disabled, and loading were not shown. No screenshot crops. Signed-in app chrome was not entered. Google, GitHub, and SSO were not followed.
