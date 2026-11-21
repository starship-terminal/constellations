# Patterns

Public patterns from 2026-11-21. The earlier signed-in pattern notes are in [patterns.signed-in-2026-10.md](patterns.signed-in-2026-10.md).

## Shell

The homepage uses a floating pill nav: wordmark on the left, Sign in on the right. After scroll, Get started joins Sign in. The hero is oat. The rest of the page is white until the black footer.

Inner pages such as Topics and Pricing use a dark bar: wordmark, a Topics link, Sign in, and a green Sign up pill. See [courses-dark-default](screenshots/public-2026-11/courses-dark-default.png).

## Start

"I'm a learner" is the filled green 3D button. "I'm a parent or teacher" is the quiet white 3D button. Sign in is an outline pill. The learner path opens /welcome/ and stops on a Koji intro with one Continue button. That button was not clicked.

## Catalog

/courses/ is public without an account. A subject strip filters the list. Each row is a title, a short description, and sometimes a green NEW badge. Phone width turns the strip into a scroller and the rows into cards. See [courses-dark-phone](screenshots/public-2026-11/courses-dark-phone.png).

## Pricing

/subscribe/ is public. Monthly and Annual are tabs. Annual carries a MOST POPULAR pill. Two plan cards sit in an iridescent frame. Subscribe now was not clicked. Prices on this capture were in SGD.

## Help

The Help Center is a light page with an empty search field and category cards. The search was not submitted. See [help-light-default](screenshots/public-2026-11/help-light-default.png).

## Empty

The public catalog is not empty. The empty states that were photographed are the login and signup walls: blank email and password fields, no error text. See [login-dark-empty](screenshots/public-2026-11/login-dark-empty.png) and [signup-light-empty](screenshots/public-2026-11/signup-light-empty.png).

## Not this pass

No form was submitted, so there is no validation error, no toast, and no destructive confirmation. Search was not run. No lesson was started. The signed-in app shell was not opened. `login_extracted` stays `not-started`.
