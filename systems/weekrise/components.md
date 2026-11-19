# Weekrise components

Public marketing components, measured on weekrise.com on 2026-11-19. Crops are from headless Chromium screenshots of public pages. Auth controls were measured in the preview browser and have no crops.

## Button

The hero primary button is `button.bt_jhk0t8`. The stylesheet sets `background: var(--vapor-primary)`, `border: solid var(--vapor-primary) 1px`, `color: var(--vapor-primary-text)`. Computed: 46px tall, padding 0 17px, radius 10px, Inter 20px / 400, white on #2481ff.

![Get Started](components/crops/button-primary-default.png)

The secondary button is `button.bt_1ybz7cv`: transparent background, 1px `--vapor-primary` border, `--vapor-primary` text, same 46px height and 10px radius.

![Learn more](components/crops/button-secondary-default.png)

The desktop Signup chip is the same primary fill at nav size: 30px tall, padding 0 11px, radius 10px, white on #2481ff. Login beside it is a #f6f6f6 chip, text #2481ff, radius 6px.

![Signup](components/crops/button-signup-chip-default.png)

![Login](components/crops/button-login-chip-default.png)

Hover and pressed colours were not in the readable stylesheets. The shared button class `.bt_a0pmeg` sets `transition: 0.3s` and `outline: none`. The only `:hover` rule found scales `.bt_vsr5ua` to 1.02.

Auth Continue is a different blue: #417ff7 fill, white text, 36px tall, radius 8px, padding 0 13px, Inter 16px / 400. "Sign in with Google" is white, 1px #e8e8e8 border, text #333333, same size. Neither was cropped.

## Icon button

At 390px the nav collapses to a 30 x 30 button, `aria-label="Open Navigation"`, white fill, 1px #e8e8e8 border, radius 6px, text #333333. The icon is an inline 16 x 16 SVG of three lines, stroke currentColor, stroke-width 2.

![Open navigation](components/crops/icon-button-menu-default.png)

## Link

Marketing links (Academy, footer Privacy, footer Terms) paint `--vapor-primary` (#2481ff), Inter 16px / 400, no underline in the computed style. Auth links ("Sign up instead", Terms of Service) paint #417ff7, Inter 14px / 500.

## Text field

The login email field is an input inside a `main` wrapper. The input is 34px tall, padding 0 12px, Inter 14px / 400, transparent background. The wrapper is 36px tall, radius 7px, border 1px solid #e8e8e8. Placeholder colour is #757575 ("Enter your email"). The label is Inter 13px / 500, #000000.

Focusing the input left the wrapper border and the outline unchanged (`outline: none` 3px). No error state was produced. Signup adds a Name field with the same chrome and placeholder "What's your name". No screenshot of either form was taken.

## Card

Feature cards ("Share it with your team", "Daily Digest") are white or #fafafa, radius 20px, padding 60px. Title Inter 34px / 600, body Inter 24px / 500.

Pricing cards are 340px wide, radius 15px, padding 40px, gap 30px, shadow `rgba(0, 0, 0, 0.12) 0px 0px 25px 0px`. Free is transparent with a 1px #e8e8e8 border. Pro is #2481ff. Team is #a55eea. Amount is Inter 48px / 700. Plan name is Inter 19.2px / 600.

![Pro](components/crops/card-price-pro-default.png)

![Free](components/crops/card-price-free-default.png)

![Team](components/crops/card-price-team-default.png)

The academy next-article card is a white card with a blue icon tile, title in #2481ff, and a grey "Next Article" line. The crop is the part that sat inside the 900px viewport.

![Next article](components/crops/card-article-default.png)

## List row

The academy index is a vertical list of icon plus label. Labels are Inter, black, with a 16px line icon.

![Academy list](components/crops/list-academy-default.png)

## Navigation

Desktop nav is 61px tall, padding 15px 20px, transparent. Wordmark is an h1, Inter 18px / 600. Pricing is a 30px button, Inter 13px / 400, colour #666666, radius 6px. At `max-width: 720px` those links collapse and the menu button appears.

The mobile overlay `.bt_btqge8` is `position: absolute; inset: 0; background: var(--vapor-background); transition: 0.5s 0.5s`. `.hidden` sets opacity 0 and pointer-events none. A click did not remove `hidden`.

## Gaps

- No hover, pressed, disabled or loading crop. The stylesheet did not declare a hover colour for the primary button.
- No focus-visible change on the email field.
- No text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar or badge on the captured surfaces.
- No menu open state.
- No signed-in planner, so no app shell, empty state, or task list.
- No form error. Nothing was submitted.
- Login and signup have no screenshots. The headless pass was limited to public pages.
