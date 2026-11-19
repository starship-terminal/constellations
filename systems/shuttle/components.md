# Components

Public signed-out Shuttle, measured on 2026-11-19 at a 1169 by 731 CSS viewport, devicePixelRatio 2. Screenshots were not saved: the preview browser returned "The browser is not producing screenshot frames." Values below are computed styles.

## Button

App chrome uses 8px radius, 32px height, 12px / 600 / 16px, padding 0 12px, gap 8px, shadow `rgba(0, 0, 0, 0.25) 0px 0px 1px 0px`. Transition is `color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1)`.

| State | Where | Values |
|---|---|---|
| Primary, app | Share on https://shuttle.zip/new/s/space/ and on the about demo | background `#0077ff`, text `#ffffff`, 76 by 32 on the space page |
| Secondary, app | Log In and Download on the space page | background `#2c2c2e`, text `#ffffff`, Log In 77 by 32, Download 100 by 32 |
| Primary, marketing pill | Sign up on https://shuttle.zip/about | background `#0077ff`, text `#ffffff`, radius 9999px, padding 8px 16px, 14px / 500 / 20px, 102 by 36 |
| Upload pill | Upload File on about | background `#0077ff`, text `#ffffff`, radius 9999px, padding 8px 16px, 15px / 500 / 22.5px, 128 by 39 |
| Inverse pill | Contact us on https://shuttle.zip/pricing | background `#ffffff`, text `#000000`, radius 9999px, padding 8px 20px, 16px / 700 / 24px, 144 by 40. Class names `hover:bg-neutral-800` and `dark:hover:bg-neutral-200`. Hover was not shown |
| Submit | Next on https://shuttle.zip/signup and https://shuttle.zip/login | background `#0077ff`, text `#ffffff`, radius 8px, padding 0 16px, 14px / 500 / 20px, 320 by 32, disabled |
| Link styled as button | Create Account on the space page | wrapper background `#0077ff`, 118 by 32, radius 8px, text 12px / 600 |

Hover, focus-visible, pressed and loading were not forced. Disabled Next was the only disabled state shown.

## Link

Nav links Updates and Pricing are 14px / 500 / 20px, colour `#ffffff`, opacity 0.70, padding 8px 16px, height 36px. The wordmark link is 16px / 600. Terms and Privacy Policy on signup are 12px / 500, `#ffffff`, class `hover:underline`. The underline was not shown. "Already have an account? Log in" is 14px / 400, `rgba(235, 235, 245, 0.6)`.

## Text field

Signup and login fields sit in a wrapper: background `#2c2c2e` (`bg-group`), height 40px, radius 12px, padding 0 16px, gap 8px, width 320px. The input itself is transparent, 16px / 400 / 24px, 288 by 24, placeholder class `placeholder:text-placeholder`. Placeholders are "Your email" and "Your name". The computed placeholder colour token is `#ebebf54d`. A filled state was not created. Focus was not shown. The outline computed as `rgba(0, 0, 0, 0) solid 2px` with style none on the input.

The about demo "Ask Shuttle a question..." field is transparent, height 44px, radius 6px, padding 12px 0, 14px / 400. It is a marketing demo, not a signed-in composer.

## Switch

Signup has two switches, Updates and Legal. The track is 44 by 24, background `#2c2c2e`, radius 9999px, 2px transparent border. The thumb is 20 by 20, background `#3c3c3e`, radius 9999px, `aria-checked` false, transform none. Transition is 0.15s `cubic-bezier(0.4, 0, 0.2, 1)` on color, background and border. The checked state was not opened. A native checkbox input is also in the control, transparent, same 44 by 24 box.

## Card

Pricing cards on https://shuttle.zip/pricing are 284px wide, padding 16px, radius 24px, background `#000000`, 14px body. Free has a 1px border `rgba(255, 255, 255, 0.2)` and height 406. Pro has a 1px border `#007aff` and height 490. Prices are euro 0 and euro 6. Checkout was not opened.

## Menu and panel

The about page embeds static demos. A suggestions menu is 540 by 342, background `#1c1c1e`, radius 12px, shadow `rgba(0, 0, 0, 0.7) 0px 25px 50px -12px`. Preview, Share and Storage panels are `dark:bg-neutral-800/90`, painted `#262626` at 0.9, radius 16px, 14px type, backdrop-blur. Those panels contain other people's names and email addresses as published marketing copy. Those addresses are not stored in this package.

## Avatar, badge, table, tabs, tooltip, dialog, toast, select, radio, text area

Not measured as live components. Demo file rows and avatars are on the marketing page. A table, tab list, tooltip, dialog, toast, select, radio and text area were not found on the pages that were opened.

## Icon button

Log In, Download and Share contain 14px Lucide strokes (`user-round`, `arrow-down-to-line`, `send`). They were not exported as separate icons.
