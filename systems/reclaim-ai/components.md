# Components

Values are computed styles from 2026-11-19. No crops: the preview browser produced no screenshot frames.

## Button

Marketing primary, `a.nav_start_button` and `a.button-5`. Background `rgb(0, 97, 254)`, text white, radius 10px, Atlas Grotesk Web weight 300. Nav size 16px, padding 10px 30px, height 40. Hero size 18px, padding 15px 30px, height 62.

Marketing outline, `a.button-6`. Transparent fill, 1px solid `rgb(0, 97, 254)`, text the same blue, radius 10px, padding 15px 30px.

Nav outline, Book a Demo. Transparent fill, 1px solid black, text black, 14px, padding 10px 30px, height 40, radius 10px.

Pricing CTA, `.pricing_top_cta`. Black fill, white label at 16px weight 500, radius 10px, 190 by 50.

Login providers. Google `rgb(0, 107, 255)`, Microsoft `rgb(47, 47, 47)`, Dropbox `rgb(0, 97, 255)`. Each 370 by 44, radius 26px, padding 4px, white text, Poppins 14px. Shadow `0 2px 4px` at 10% of `rgb(23, 29, 38)`.

SSO. Transparent, 1px solid `rgba(255, 255, 255, 0.15)`, white text, Poppins 16px weight 500, padding 15px 23px, radius 40px, 370 by 44.

Hover, focus-visible, pressed, disabled and loading were not captured.

## Link

Log In in the marketing nav: Poppins 18px, `rgb(51, 51, 51)`, padding 0 10px, no underline.

Login page links: Poppins 13px weight 500, `rgb(238, 154, 178)`. The top "Get started" link is 16px weight 500 in the same colour, underline none.

## Text field

Not on the marketing pages or the login page. The contact form is a HubSpot iframe: label Arial 14px weight 500 `rgb(51, 71, 91)`; input background `rgb(245, 248, 250)`, border `1px solid rgb(203, 214, 226)`, radius 3px, height 40, padding 0 15px, Helvetica Neue 16px. Textarea height 66, padding 10px 15px. Not submitted. Focus and error were not captured.

## Select

HubSpot company-size and personal-or-team selects, same chrome as the text field, placeholder colour `rgb(191, 191, 191)`. Closed. Options were not opened.

## Tabs

Pricing billing, `.pricing_cards_tabs`. Track `#f7f5f2`, radius 10px, shadow `2px 3px 7px rgba(0,0,0,0.1)`, 350 by 46. Selected tab white, text `rgb(0, 97, 254)`, radius 10px, shadow `0 2px 11px rgba(0,0,0,0.05)`. Idle tab matches the track, text `rgb(34, 34, 34)`, radius 0.

## Card

`.pricing_card`: white, radius 10px, shadow `1px 3px 7px -2px rgba(0,0,0,0.15)`, 340 by 950. Popular flag `.popular_flag_cont`: `rgb(0, 97, 254)`, radius 8px 8px 0 0, height 50. Discount cards `.department_card`: `#f7f5f2`, radius 10px, padding 30px 0 20px, 257 by 406.

## FAQ

`.faq-q` buttons on the homepage: Poppins 20px, `rgb(43, 43, 43)`, padding 26px 0, no border. Closed. Expanded answer styles were not read.

## Badge

"Most Popular" label inside the flag: Poppins 14px weight 500, white, padding 15px 0 0.

## Not present on the captured surfaces

Text area in the product UI, checkbox, radio, switch, menu, tooltip, dialog (other than the dismissed Osano cookie box), toast, list row, table, avatar, icon button. The signed-in app may have them. They were not reached.

## Gaps

- No screenshots or crops. Preview frames failed.
- No hover, focus-visible, pressed, disabled, loading or error states.
- No 390px layout.
- Signup and the signed-in app were not entered. Login has no email field.
- Contact form is HubSpot chrome, measured and not submitted.
- Motion was not probed. `core.motion` holds two declared login custom properties only.
