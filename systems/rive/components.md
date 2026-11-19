# Components

Measured on 2026-11-19 from signed-out pages. Screenshot frames failed, so this file has no crops. Values are computed styles.

## Button

Marketing GET STARTED on https://rive.app/: white face, black text, 4px radius, padding 5px 9px 6px, height 27px, PragmataPro 12px weight 500, letter-spacing 1.2px, uppercase. Inset ring `rgba(255, 255, 255, 0.1) 0 0 0 1px`. Hover and focus-visible set the background to rgb(223, 224, 227). Transition is background 0.15s ease.

COPY uses the same radius and type, with background rgba(255, 255, 255, 0.9) and a 1px white border.

Auth LOG IN and SIGN UP: background rgb(31, 111, 229), white text, height 44px, radius 2px, Orbitron 12px weight 500, letter-spacing 0.96px. Hover sets the background to the panel `--s-accent-hover`, #1a5bc4.

CONTINUE WITH GOOGLE: transparent face, 1px border rgba(0, 0, 0, 0.2), same height and radius, Orbitron 12px.

Pricing plan buttons: background rgb(29, 29, 29), height 40px, radius 4px, width 225px. The button's own computed color was black. The label color was not isolated.

## Link

Nav link: Inter 12px weight 500, letter-spacing 0.96px, rgba(255, 255, 255, 0.85), uppercase. Transition color 0.15s ease.

Auth text link (Create account, Log in): Inter 13px, black, weight 500 on the action word.

Footer link on the auth page: Inter 14px, rgb(170, 170, 170).

## Text field

Login `#auth-email` and `#auth-password`: white face, black text, Inter 16px, height 44px, width 360px, padding 0 12px, radius 2px, border 1px solid rgba(0, 0, 0, 0.2). Hover border is rgba(0, 0, 0, 0.4). Focusing the email field did not change its computed box-shadow. The panel's `:focus-visible` rule excludes `input`.

Home newsletter email: height 40px, background rgba(255, 255, 255, 0.05), color white, radius 4px, padding 0 14px, inset ring rgba(255, 255, 255, 0.15). Placeholder text is `email@rive.app`. Not submitted.

Signup uses the same field metrics as login, for email and password only.

## Checkbox

Signup "Send me emails with the latest updates from Rive": 16 x 16, `accent-color` rgb(31, 111, 229), checked when the page loaded. Label is Inter 13px.

## Card

Pricing plan card: 257px wide, radius 8px, padding 16px. The card background computed as transparent. The page behind it is black.

## Icon button

SHOW on the password field: JetBrains Mono 11px, letter-spacing 0.88px, color rgb(85, 85, 85), height 36px, padding 0 10px, radius 2px, no border.

## Gaps

Text area, select, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar, badge, and list row were not on the pages that were opened, or were not opened. The docs search button was measured. The search dialog it opens was not. The form error rule was read. The error was not shown, because the form was not submitted. Pressed and disabled states were not held. Loading was not shown.
