# Patterns

One public page. [https://tome.app/](https://tome.app/) and [https://tome.app/login](https://tome.app/login) both render it.

## 404, centered

A full-viewport grid centers a column. The column is at least `--content-width` (283px) and at most `--content-max-width` (360px), shifted up 4px. Main padding is 32px at desktop and 24px at 390px.

| Theme | Desktop | Phone |
|---|---|---|
| dark | [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png) | [screenshots/home-dark-phone.png](screenshots/home-dark-phone.png) |
| light | [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png) | [screenshots/home-light-phone.png](screenshots/home-light-phone.png) |

Desktop shots are 1440×900 CSS, phone shots are 390×844 CSS, both at device pixel ratio 2. The focused desktop shots are [screenshots/home-dark-desktop-focus.png](screenshots/home-dark-desktop-focus.png) and [screenshots/home-light-desktop-focus.png](screenshots/home-light-desktop-focus.png).

## Footer actions

Fixed to the bottom, centered, 283px wide, 12px gap. Bottom offset is 34px at desktop and 24px at the 390px viewport, plus the safe-area inset. Two uppercase actions and a divider.

## Not on this page

No navigation, no form, no empty state of the product, no loading state, no search, no list, no onboarding, no destructive confirm. Signed-in screens were not entered: there is no email field, and the login path is this same page.
