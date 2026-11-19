# Components

Signed-out chrome only. Crops are from the 1440 desktop captures.

## Button

Marketing primary pill: Capsule Sans Text 13px, colour `#FFFFFF` on `#110E08`, radius 36px, height 44px, padding `0 32px`, border 1px solid `#110E08`. Crop: [signup-pill-default.png](components/crops/signup-pill-default.png) (the dark Sign up under the hero; the lime Get started uses the same size with `#110E08` on `#CCFF00`).

Nav Log in: transparent face, 1px solid `#CCFF00`, text `#CCFF00`, radius 36px, height 44px. Visible in [nav-default.png](components/crops/nav-default.png).

App Log In: face `#FFFFFF`, label `#000000` weight 700, radius 44px, height 44px, padding `0 48px`. Crop: [login-submit-default.png](components/crops/login-submit-default.png).

Help is the same pill with a transparent face and a white hairline. Crop: [help-default.png](components/crops/help-default.png).

Google and Apple are full-width pills, radius 44px, height 44px. Crop: [google-default.png](components/crops/google-default.png). They were not clicked.

Hover, pressed, disabled, and loading were not captured. App hover colours exist as `--rh__primary-hover` and `--rh__neutral-hover-*` and are tokenised. They were not seen painted.

## Text field

Email box: height 36px, radius 4px, padding `0 12px`, border 1px solid `#FFFFFF` while that field was the active one, background `#000000`, text `#FFFFFF`, Capsule Sans Text 13px, letter-spacing -0.1px. Crop: [email-field-default.png](components/crops/email-field-default.png).

Password box at rest used border `#30363A` (`--rh__neutral-bg3`). Focus ring colour is `--rh__focus-inner-color` `#007FF5`. A focused ring was not isolated from the browser's own outline (`rgb(153, 200, 255) auto 1px` after `focus()`).

Error, disabled, and filled states were not shown. Nothing was typed.

## Checkbox

"Keep me logged in for up to 30 days": 16px box, radius 2px, border 1px solid `#919FA6` (`--rh__neutral-fg2`). Not toggled.

## Link

Banner link is Phonic 16/24, letter-spacing -0.25px, colour `#110E08` on `#CCFF00`. Footer links are Capsule Sans Text 16px on the lime footer.

## Gaps

- Signup wall: region search only. No email form, no password rules, no phone, no SSN, no KYC, no funding. Continue was not pressed.
- No account, so no portfolio, chart, order ticket, transfer, or settings.
- Nav dropdowns were not opened.
- Cookie dialog was not accepted. It is not in the tokens.
- No toast, tooltip, tabs, radio, switch, text area, table, avatar, or badge on the pages opened.
- Icon set is the wordmark and the feather. Social marks in the footer were not extracted.
