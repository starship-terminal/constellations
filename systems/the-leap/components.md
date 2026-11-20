# Components

Public signed-out The Leap, measured on 2026-11-19 at a 1169 by 731 CSS viewport, devicePixelRatio 2. Screenshots were not saved: the preview browser returned "The browser is not producing screenshot frames." Values below are computed styles.

## Button

Marketing buttons use class `button button-yellow`. Auth buttons paint the yellow or white face on an inner span.

| State | Where | Values |
|---|---|---|
| Primary | "Explore features" on https://www.theleap.co/ | background `#ecf956`, text `#482317`, 1px solid `#482317`, radius `100px`, padding `10px 30px 7px`, height 39px, 20px / 400 / 20px, letter-spacing 0.16px, uppercase, Favorit |
| Primary, small | "Learn more" on https://www.theleap.co/features/ | same fill and border, radius `100px`, padding `8px 24px 5.6px`, height 40px, 16px / 400 |
| Pricing | "Sign up" on https://www.theleap.co/pricing/ | same fill, border and type as primary, radius `20px`, width 250px, height 39px |
| Submit | "Let's go" on https://make.theleap.co/accounts/login | inner span background `#ecf956`, text `#4c2116`, 1px solid `#4c2116`, radius `9999px`, padding `6px 48px`, height 46px, 22px / 400, Favorit. Outer button is transparent |
| OAuth | "Sign in with Google" and "Sign in with Thinkific" | inner span background `#ffffff`, text `#4c2116`, 1px solid `#4c2116`, radius `9999px`, padding `6px 24px`, height 44px, 18px / 400 |
| Hover, declared | `.button-yellow:hover` in the theme stylesheet | box-shadow `rgb(236, 249, 86) 0px 4px 24px 10px`. `::before` is a rainbow gradient at opacity 0, set to opacity 1 on hover, transition `opacity 0.15s ease-in`. The hover state was not shown |
| Focus | button class `focus:outline-none` | outline `transparent solid 2px`. A visible focus ring was not shown |
| Disabled | class `disabled:opacity-50 disabled:cursor-not-allowed` on the auth button | the empty form was not disabled when read. Disabled paint was not shown |

Pressed and loading were not shown.

## Link

Nav links ("Features") are Favorit 20px / 350 / 20px, `#482317`, letter-spacing 0.16px, uppercase, no radius. Footer links are Favorit 16px / 400, `#482317`, `text-decoration: none`. "Help is here" on the login page is Favorit 16px / 400, `#4c2116`, 85 by 20.

## Text field

Login email and password on https://make.theleap.co/accounts/login: background `#ffffff`, text `#4c2116`, 1px solid `#4c2116`, radius `0px`, height 44px, width 704px, padding `6px 12px`, Favorit 18px / 400 / 30px. Placeholder colour `#a1a1a1`. Label "Email" is Favorit 16px / 400 / 17.6px, `#4c2116`. The fields already held a previous session's email and a masked password. Those values were not changed, not copied into this package, and the form was not submitted.

## Text area, select, checkbox, radio, switch, tabs

Not present on the public pages opened. Contact at https://www.theleap.co/contact/ has no form. It lists two public email addresses as text. No message was sent.

## Menu

The header submenu is declared as a white panel, padding `0.5rem 1.5rem`, shadow `0 0.25rem 0.375rem -0.0625rem rgba(0,0,0,.1), 0 0.125rem 0.25rem -0.0625rem rgba(0,0,0,.06)`. It was not opened, so the open state is a stylesheet reading, not a shown state.

## Tooltip, dialog, toast

Not shown. A hidden waitlist modal exists in the home DOM (`modal modal--waitlist-signup`, `display` hidden). It was not opened.

## Cookie banner

`.cookie-banner.banner-shown` on home: background `#eeeeee`, radius 8px, height 80px, width 1052px, shadow `rgba(0, 0, 0, 0.2) 0px 0px 2px 1px`, text Favorit 16px / 400 / 24px, `#482317`. Close control "X" is 32px / 700, padding 16px. It was not dismissed.

## Card

Pricing plan (`.pricing-plan`) on https://www.theleap.co/pricing/: background `#fafafa`, padding 40px, radius 20px, width 330px, height 784px. Plan name is ABC Favorit 35px / 400 / 32px, letter-spacing -0.7px, `#4c2116`. Price is ABC Favorit 62px / 700 / 74.4px, `#4c2116`.

Testimonial card on home: 550 by 420, radius 30px, padding 40px, background image `linear-gradient(129deg, #f3e8f3 24.01%, #dff5dd 96.01%)`. Quote is Favorit 16px / 400 / 24px, `#482317`.

Journey step (`.card`) on home: 238 by 212 to 299, transparent background, title ABC Favorit 24.6px / 400, `#4c2116`.

## Avatar

Testimonial image is 50 by 50, radius `100%`.

## Badge

Blog category "Audience growth" is 18px / 400, uppercase, letter-spacing 0.16px, ABC Favorit, colour `#4c2116`, radius 38.5px, height 41px, background transparent. A filled badge was not measured.

## List row, table

Changelog lists dates as links. Individual row chrome was not measured: the first matching node was the page wrapper, not a row. Pricing features are a list inside the plan card. No data table was on the pages opened.

## Gaps

- Hover, focus-visible, pressed, disabled and loading were not shown.
- Signup at https://accounts.theleap.co/signup redirected to the login page. No email-only signup form was found, so AgentMail was not used.
- Google and Thinkific were not followed.
- No card, phone, government ID or KYC step was reached.
- The signed-in app was not entered.
- Phone width 390 and desktop width 1440 were not applied. The live width was 1169.
- No dark theme was found. `color-scheme` was `normal`. Theme-toggle markup exists in the DOM and did not change the page.
