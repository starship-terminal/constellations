# Quizlet components

Public capture of https://quizlet.com/ on 2026-11-21, signed out. Body class `theme-default`. Desktop CSS viewport measured 1440 by 900 at device pixel ratio 2. Phone CSS viewport measured 390 by 844 at device pixel ratio 2. PNG sizes are those viewports at 2x: 2880 by 1800, and 780 by 1688.

Crops are 2x element screenshots in [components/crops/](components/crops). Page shots are in [screenshots/](screenshots). Read colours from [tokens.json](tokens.json), not from the quantized crops.

## Discovery list

| Surface | URL | Screenshot |
|---|---|---|
| Homepage | https://quizlet.com/ | [home-light-default](screenshots/home-light-default.png) |
| Footer | https://quizlet.com/ | [home-light-footer](screenshots/home-light-footer.png) |
| Flashcards marketing | https://quizlet.com/features/flashcards | [flashcards-light-default](screenshots/flashcards-light-default.png) |
| Pricing | https://quizlet.com/upgrade | [pricing-light-default](screenshots/pricing-light-default.png) |
| Login dialog, empty | dialog on https://quizlet.com/ | [login-light-empty](screenshots/login-light-empty.png) |
| Signup dialog, empty | dialog on https://quizlet.com/ | [signup-light-empty](screenshots/signup-light-empty.png) |
| Homepage, phone | https://quizlet.com/ | [home-light-phone](screenshots/home-light-phone.png) |
| Phone drawer | https://quizlet.com/ | [nav-light-phone-menu](screenshots/nav-light-phone-menu.png) |

## Log in pill

Header button. It opens a dialog. It is not an anchor. Background `{color.twilight.500}` (`#4255FF`), white label, 14px weight 600, padding 10px 16px, height 40px, radius `{radius.pill}` (`200px`), border 2px solid transparent. Hover background `{color.twilight.600}` (`#423ED8`).

![Log in](components/crops/button-login-default.png)

## Sign up pill

Hero button, same blue, 16px weight 600, padding 12px 24px, height 48px, radius 200px. It opens the signup dialog.

![Sign up for free](components/crops/button-signup-default.png)

## Search field

`AssemblyTextInput` on the homepage. Background `{color.gray.200}` (`#F6F7FB`), radius `{radius.field}` (`8px`), height 40px, border 2px solid transparent. Placeholder colour matches body text `{color.gray.800}`. The word algebra was typed and not submitted. No suggestion list appeared.

![Search field](components/crops/field-search-default.png)

## Trial button

On https://quizlet.com/upgrade. Background `{color.sunset.400}` (`#FFCD1F`), label `{color.gray.800}` (`#282E3E`), radius 200px, padding 12px 24px, height 48px, 16px weight 600. The page background is `{color.twilight.900}` (`#0A092D`). The trial was not started. A crop was not cut because a yellow-pixel search of the quantized shot found no sunset fill.

## Link

"I'm a teacher" is `{color.twilight.500}`, 16px weight 600. Href https://quizlet.com/teachers. The Teachers control in the header is a signup URL and was not followed.

## Focus

A keyboard focus ring was not observed as a painted outline. Computed outline on the focused Log in control was `rgb(255, 255, 255) none 3px`. The focused search field outline was `rgb(40, 46, 62) none 3px`. `prefers-reduced-motion` was false.

## Gaps

Pressed, disabled, loading, and error states were not captured. A public study set did not load. A phone shot of an inner page hit a captcha and was discarded. SVG icons were not exported.
