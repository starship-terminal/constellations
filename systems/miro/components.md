# Components

Measured on public Miro pages in the T3 preview browser on 2026-11-18. The pane produced no screenshot frames, so there are no crops. Values are computed styles from [raw/components-computed.json](raw/components-computed.json).

## Button

Two primary blues, plus a near-black marketing button.

| State | Where | Background | Text | Border | Radius | Size |
|---|---|---|---|---|---|---|
| Primary | Pricing, Try for free | `#3859ff` | `#ffffff` | 1px `#7a90fe` | 8px | 18px / 600, 48px tall, padding 11px 15px |
| Hover token | `--button-primary-bg-btn-primary-hover` | `#314cd9` | | | | Declared, not hovered |
| Pressed token | `--button-primary-bg-btn-primary-down` | `#2a41b6` | | | | Declared, not pressed |
| Outline | Pricing, Start for free | transparent | `#1c1c1e` | 1px `#c7cad5` | 8px | 18px / 600, 48px tall |
| Auth submit | Login, Continue with email | `#2e4de6` | `#ffffff` | 1px `#2e4de6` | 8px | 18px, 50px tall, padding 12px 16px |
| Provider | Login, Google | `#ffffff` | `#1c1c1e` | 1px `#444749` | 8px | 18px / 400, 50px tall |
| Marketing | Homepage nav, Get started free | `#1c1c1e` | `#ffffff` | none | 8px | 14px / 600, 36px tall, Noto Sans |
| Ghost | Homepage nav, Login | transparent | `#1c1c1e` | none | 8px | 14px / 500, 36px tall |
| Header link | Login, Sign up | `#ffffff` | `#1c1c1e` | 1px `#1c1c1e` | 8px | 18px, 42px tall |
| Focus-visible | Pricing feature trigger | | | outline 2px solid `#3859ff` | | From the stylesheet rule |

Disabled and loading were not on these pages. The disabled colour token is `#c7cad5`.

## Link

Pricing "buy now" is `#3859ff`, 18px, weight 400, line-height 24.3px, Noto Sans. The visited token is `#7a90fe`.

## Text field

| Page | Placeholder | Border | Padding | Height | Radius |
|---|---|---|---|---|---|
| Homepage hero | Enter your work email | 1px `#e9eaef` | 16px | 48px | 8px |
| Login | Enter your email address | 1px `#86b7fe` before and at focus | 6px 16px 6px 48px | 48px | 8px |
| Signup, invalid | Enter your work email | 2px `#dc3545` | | | |
| Templates search | Search for a template | 1px `#d8dae2` | 20px 64px 20px 24px | 66px | 8px |

The login label "Email" is 16px, weight 700, `#1c1c1e`, Roobert PRO. Focus on the login field kept `outline: none` and `box-shadow: none`.

Signup error copy, class `invalid-feedback`: "This email can not be registered, please try another domain", `#cc4856`, 18px, weight 400, Roobert PRO.

## Checkbox

Login "Remember me" is a 24px box, 4px radius, accent `#0d6dfd`. The label is 16px `#1c1c1e`. The checked and disabled states were not opened.

## Switch, radio, select, text area

Not on the public pages that loaded. Cookie-preference switches were in the OneTrust dialog and were not opened.

## Tabs

The pricing billing control is a pill track, not a tab list. Track `#e0e2e8`, radius 40px, padding 4px. The selected "Yearly (save 20%)" pill is `#ffffff` text `#1c1c1e`, padding 6px 12px. "Monthly" is transparent with text `#555a6a`.

## Menu, tooltip, dialog, toast

The Product menu was not opened. No tooltip, dialog or toast was shown. The OneTrust cookie banner was visible on the homepage and was left closed.

## Card

Pricing plan cards are `#ffffff`, 20px radius, 24px padding, 277px wide, `box-shadow: none`. Free, Starter and Enterprise have a 2px white border. Business has a 1.5px `#3859ff` border and padding `35.2px 24px 24px`.

The login and signup card is `#ffffff`, 1px `#444749` border, 12px radius, 48px padding, 565px wide, no shadow. The page behind it is `#fbf7ef`.

## Badge

No "most popular" badge was painted. "Yearly (save 20%)" is the selected billing pill, not a separate badge.

## List row, table, avatar

Not on these public pages. FAQ questions are 24px / 500, line-height 28.8px, Noto Sans, `#1c1c1e`.

## Icon button

The header logo link is 109px by 40px on pricing and 109px by 40px on login. The logo SVG was not exported.

## Gaps

- No crops. The preview browser returned "The browser is not producing screenshot frames."
- Hover, pressed, disabled and loading were not forced. Hover and pressed colours are the declared `--button-primary-bg-btn-primary-*` tokens.
- Dark theme was not on any public page.
- The signed-in board, menus, dialogs and toasts were not reached. `https://miro.com/app/` redirected to signup. Signup rejected `kaichen@agentmail.to` with "please try another domain" and sent no mail.
- Phone width (390) and a 1440 viewport were not measured. Readings are from 1169x731 CSS pixels at devicePixelRatio 2.
