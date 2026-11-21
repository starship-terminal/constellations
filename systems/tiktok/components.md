# Components

Public signed-out chrome. Dark values are the 2026-11-19 readings. Light values are the 2026-11-21 Playwright readings. Crops were not cut. The page shots are in [screenshots/](screenshots/).

## Button

The desktop Log in control in the sidebar.

| State | What was read |
|---|---|
| Default | `component.button.bg` `#fe2c55`, `component.button.text` white, `component.button.radius` 6px, `component.button.height` 40px, padding 1px 16px, type `typography.button` 16px weight 500. Width 200px at innerWidth 1169. |
| Hover | Light pass: background `#ea284e` while the pointer was over the desktop Log in button. Transform none. |
| Pressed | Light pass: background `#e0274b` while the pointer was down. Transform none. Opacity 1. |
| Focus | Declared `button:focus-visible` outline is 2px solid `#ff4c3a`. `:focus` sets outline none. Not painted. |
| Disabled | Not shown. |
| Phone | The visible Log in control is a 40 by 40 icon button, transparent, white, radius 6px, 14px weight 400. The filled primary is not painted at innerWidth 390. |

## Icon button

Close on the login dialog is 32 by 32, radius 50%, background `rgba(255, 255, 255, 0.04)`. The glyph is [icons/close.svg](icons/close.svg). Search at 390 is a 39 by 40 capsule. Follow on a video is 28px tall, transparent, white, 14px, padding 1px 8px.

## Link

Sign up in the login dialog is `typography.signup-link`, 11px weight 600, color `#ff3b5c`. Terms of Service is 10px weight 400, white at 90%, no underline. The region name is 11px weight 600.

## Text field

A search input exists in the DOM with placeholder "Search", 16px, transparent, and a painted size of 0 at both measured widths. The visible search control is the capsule button, not the field. `--tux-colorBGInput` is `rgba(255, 255, 255, 0.12)`. The hidden search form uses that fill and a 92px radius. Neither was painted.

The phone or email field was not opened. That step starts account entry.

## Text area

Not present on these surfaces.

## Select

Not present on these surfaces.

## Checkbox, radio, switch

Not present on these surfaces.

## Tabs

Not present. For You, Explore, Following, and LIVE are nav buttons, not a tab list.

## Menu

More was not opened.

## Tooltip

Not shown. `--tux-v2-color-misc-tooltip-background` is `#fff` and the text token is `#000`. Declared, not painted.

## Dialog

The login sheet. `component.sheet.bg` `#1e1e1e`, radius 24px, no box-shadow. Desktop size 428 by 562, inset from x 371. Phone size 390 by 562, x 0, y 125. Mask is `rgba(0, 0, 0, 0.68)`. Title is `typography.display`, TikTokDisplayFont, 33px weight 700, line-height 49.5px.

## Toast

Not shown. `--tux-colorToastDefault` is `rgba(84, 84, 84, 0.92)`. `--tux-colorToastNegative` is `rgba(255, 76, 58, 0.92)`.

## Card

Not present as a marketing card. The login channel row is the closest surface: 300 by 48, radius 24px, fill `rgba(255, 255, 255, 0.13)`, label 16px weight 600.

## List row

Seven channel rows share that chrome: QR code, phone or email, Facebook, Google, LINE, KakaoTalk, Apple. The option container padding is 8px 32px 0px 40px.

## Table

Not present.

## Avatar

Video chrome shows creator marks. Those are feed content, not a measured account avatar. No signed-in avatar was available.

## Badge

Not present on the measured chrome.

## Gaps

- Signup was not entered. The Sign up link was measured and not followed.
- Phone and email fields were not opened.
- QR code was not opened.
- No account was created. No phone number was entered.
- Hover, pressed, disabled, error, and loading were not painted.
- Focus-visible was read from a stylesheet rule, not from a focused control.
- Light theme was not on the page. `data-theme` and `data-tux-color-scheme` were both dark.
- Screenshots and crops are the labeled placeholder only.
