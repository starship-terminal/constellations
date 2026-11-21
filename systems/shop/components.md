# Shop components

Public signed-out chrome measured on 2026-11-19 from a T3 preview tab at 1169 by 731 CSS pixels, devicePixelRatio 2. Page frames from 2026-11-22 are in [screenshots/](screenshots/). No new crops were cut this pass.

## Button

Sign in on https://shop.com/ is a 56 by 56 icon button in the left rail, radius 9999px, transparent background. The visible Sign in label colour is `oklch(0.55161 0.02649 290.54)`. Idle rail icons are `oklch(0.71209 0.01747 291.676)`. The selected Home icon is `oklch(0.11853 0.05087 289.487)`. Colour transitions over 150ms with `cubic-bezier(0.4, 0, 0.2, 1)`.

Continue on https://shop.app/accounts/login is the primary action. It is 344 by 52, padding 16px, radius 999px, background `rgb(84, 51, 235)`, text `rgb(255, 255, 255)`, 16px/22px, letter-spacing -0.5px, weight 500. The computed border is 0.5px `rgb(255, 255, 255)`. The shadow is two white inset highlights at 0.32 alpha plus `rgba(84, 51, 235, 0.24) 0px 4px 24px 0px`. It was enabled, opacity 1, cursor pointer. It was not submitted.

Use a passkey is a text button, 344 by 42, padding 12px, radius 999px, transparent background, black text, 14px/18px, letter-spacing -0.2px, weight 600.

Hover, focus-visible, pressed, loading and disabled were not shown. The login stylesheet declares `--buttons--primary-background-hover` as `rgb(127, 104, 233)` and `--buttons--disabled-background` as `rgba(0, 0, 0, 0.42)`. Those states were not painted.

## Link

Footer links on https://shop.com/ (What is Shop?, Why trust Shop?, Why use Shop Pay?, Help center) are 16px/22px, letter-spacing -0.5px, `rgb(0, 0, 0)`, no underline in the computed style. Login Terms and Privacy Policy are 12px/16px, letter-spacing -0.2px, weight 450, `rgba(0, 0, 0, 0.56)`. The English language control is `rgb(84, 51, 235)` at 14px, weight 450.

## Text field

Home search is a textarea with role searchbox. Placeholder: "What are you shopping for today?". Accessible name: "Search products and stores". The field is 488 by 40, padding 8px 50px 8px 46px, 16px/22px, letter-spacing -0.5px, colour `rgb(0, 0, 0)`, transparent background. Its shell is 32px radius, `rgba(255, 255, 255, 0.75)`, height 64, shadow `rgba(0, 0, 0, 0.12) 0px 0px 1px 0px, rgba(0, 0, 0, 0.2) 0px 12px 64px 0px`.

Login email is `#IdentityEmailForm-email`, type email, autocomplete `email webauthn`, required, placeholder "Enter your email". It was left empty. The input is 310 by 50. The shell is 344 by 52, padding 0 16px, radius 999px, background `rgba(0, 0, 0, 0.04)`, border 1px `rgb(0, 0, 0)`, shadow `rgba(0, 0, 0, 0.02) 0px 2px 4px 0px, rgba(0, 0, 0, 0.04) 0px 6px 16px 0px`.

## Text area

The home search control is a textarea. A multi-line compose field was not present.

## Select, checkbox, radio, switch

Not present on the home page or the login wall that was opened. The login stylesheet declares `--radiobutton--background` as `rgb(255, 255, 255)`. No radio was painted.

## Tabs, menu, tooltip, dialog, toast

Not shown. No `[role=dialog]` was in the DOM on home before Sign in, and the login page is a full document, not a dialog. A toast stylesheet (`Toast-Cs8sOWxc.css`) loads on home. No toast was visible.

## Card

Product tiles on home are 150 by 150 links, radius 20px, fill `rgb(255, 255, 255)`, shadow `rgba(0, 0, 0, 0.06) 0px 2px 8px 0px`. A 0.5px border of `rgba(5, 41, 77, 0.1)` sits on the image. The price chip is padding 2px 6px, pill radius, background `rgba(0, 0, 0, 0.3)`, text `rgb(255, 255, 255)` at 10px/13px, weight 600, letter-spacing -0.2px.

The download prompt is an aside, 380 by 120, background `rgb(0, 0, 0)`, radius 24px, padding 16px 48px 16px 16px, shadow `rgba(0, 0, 0, 0.12) 0px 4px 24px 0px`. The lede is 14px/18px, `rgb(201, 203, 204)`.

## List row, table, avatar, badge

Store rows and category chips are links, not a table. Category chips are 36px tall, radius 9999px, transparent background, 16px black text. Avatar and badge components were not isolated. Review counts sit in store links as plain text.

## Icon button

Rail items are 56 by 56, radius 9999px. The wordmark link is 56 by 56 at x 20 y 20, radius 28.8px. The dismiss control on the download prompt is 44 by 44, radius `10000000px`.

## Gaps

- Hover, focus-visible, pressed, loading and disabled were not shown.
- No account was created. The email field was not filled. Continue was not submitted. Passkey was not used.
- No card, phone, checkout or Shop Pay payment step was opened.
- Dark theme tokens were not painted. `prefers-color-scheme: dark` matched, and both pages still computed light backgrounds.
- Phone width 390 and desktop width 1440 were not applied. The live viewport was 1169 by 731.
- Screenshots and crops are absent because preview frames failed.
