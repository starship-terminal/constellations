# Stocktwits components

Measured on the public signed-out pages, 2026-11-19, from computed styles in the T3 preview tab. Desktop innerWidth was 1440. Phone innerWidth was 390. Token names point at [tokens.json](tokens.json).

There are no element crops. The preview browser returned no screenshot frames, and headless Playwright hit a Cloudflare challenge on every URL.

## Button

`STButton` is a pill. Radius is `core.radius.full` (9999px). The md size, used by Continue with Apple, Create Account, Log In, and Customize Watchlist, is 40px tall, padding 0 20px, gap 8px, 15px weight 600, line-height 22.5px.

The secondary face is white with a 1px `#e5e5ea` border and black text (`light.button.secondary`, `light.border`). The empty Log In submit is disabled: background `rgb(209, 209, 214)`, which is `light.button.disabled`, white text, cursor default.

Sign up or log in, and Subscribe on the plan card, are a black pill with white text. That fill is not `--primary-button-background`. The declared primary fill stays `#1b66e7` in both themes (`core.color.blue5`).

On `/about`, Sign Up is a transparent pill with a 1px border at `rgba(255, 255, 255, 0.5)` and white text. Get Started is the xl size: 56px tall, padding 0 28px, 20px weight 600, white face, black text. Enter Stocktwits is the lg size: 48px, padding 0 24px, 18px.

Use App at 390px is the xs size: 24px tall, padding 0 12px, 12px weight 600, white face, 1px `#e5e5ea` border.

Hover, pressed, and loading were not measured. The sheets declare `--primary-button-hover` as `#008fff`. No control was hovered.

## Link

Log in to existing account is 14px weight 400, colour `rgb(27, 102, 231)`, which is `light.accent`. Forgot your password? and Sign up on the auth pages use the same blue (`text-blue-ada`).

Site nav links on the shell are 13px weight 400, black. On `/about` the same links are 18px weight 600, white.

## Text field

Sign-in has two fields, Email or Username and Password. Each is 400 by 40px, padding 8px 12px, radius 8px (`core.radius.md`), background `rgb(242, 242, 247)` (`light.field.background`), 16px weight 400. Placeholder colour is `rgb(156, 163, 175)`.

Focus on the email field computed outline none and box-shadow none. `--select-focused` is `#86b7fe` in light and `#000000` in dark. That ring was not painted on this field.

Signup shows one email field and Continue with Apple. The form was not submitted, so later steps are a gap.

Enterprise fields are 480 by 53px, padding 15px 32px 4px 15px, radius 6px, 1px `#e5e5ea` border, white background. Labels are 16px `#8e8e93`. The form was not submitted.

Search on the desktop shell is a 400 by 36px pill, radius 9999px, background `#f2f2f7`, padding-left 16px, gap 12px. At 390px the search input computed 0 by 0.

## Tabs

For You and Following sit in a 41px row. The label is 16px weight 600, line-height 40px, padding 0 20px. The selected label is black. Unselected symbol tabs (News, Sentiment) are `#8e8e93`.

The symbol tab list is 40px tall with a 1px `#f2f2f7` top border. An underline on the selected tab was not isolated.

## Badge

1 Live Calls is a 24px pill, padding 4px 8px, radius 9999px, background `rgb(239, 232, 255)` (`--tag-purple` in light), text `rgb(129, 70, 255)` (`--purple` in light), 12px weight 600.

## Price

The symbol price is 30px weight 600, line-height 34px, black. The ticker is 20px weight 600. The company name is 12px weight 400, `#636366`.

A gain computes `rgb(18, 135, 96)`, which is `light.positive`. A loss on the widgets page computes `rgb(221, 51, 29)`, which is `light.negative`. The class is `text-price-positive` or the negative twin. The ticker percent on the home shell inherited black from a parent, so that strip is not a reliable price-colour reading.

## Card

A subscription card is 289px wide, padding 40px 20px 20px, radius 12px, white, shadow `0 10px 20px rgba(0, 0, 0, 0.05)`. The plan name is 36px weight 700. The price is 24px weight 700. The struck list price is 24px `#aeaeb2` with line-through. Subscribe is the black pill.

An about content card is black, white text, radius 40px, padding 60px 24px 24px, no shadow.

## Avatar

The stream avatar image is 40 by 40px, object-fit cover. Computed border-radius was 0. A circular clip was not measured.

## Select, checkbox, radio, switch, menu, tooltip, dialog, toast, table

Not captured. The signed-out pages that loaded did not show these as Stocktwits controls. OneTrust paints its own checkboxes and buttons. Those were left unclicked and are not Stocktwits tokens, except the measured `#1d68d7` note in the raw file.

## Gaps

- No hover, pressed, loading, or error state.
- No focus ring on the sign-in field.
- Signup stopped at the email field. No password, username, phone, or KYC step was opened, because the form was not submitted.
- Dark theme tokens were read by setting `data-theme="dark"` and restoring it. The live UI was not switched, and there is no dark screenshot.
- No crops.
