# Patterns

Public pages of The Leap, measured on 2026-11-19. The CSS viewport was 1169 by 731 at devicePixelRatio 2. No screenshots were saved.

## Marketing shell

https://www.theleap.co/ uses a fixed header, class `main-navigation navigation-menu-background-solid`. It is 80px tall, background `#f0edee`, bottom border `1px solid #482317`. Links are uppercase Favorit at 20px / 350. The wordmark is an inline SVG filled `#4d2114`, 83 by 60.

The page background is `#f0edee`. `meta theme-color` is `#f0edee`. Body text is `#482317` in Favorit 16px / 400 / 24px, letter-spacing 0.16px. Headlines are Tobias Light (weight 300).

The hero is a green-to-warm wash: computed background image `linear-gradient(323deg, #c6e57d 17.8%, #efedee 70.54%)` over `#ffffff`. The h1 is Tobias 70px / 300, letter-spacing -1.4px, `#482317`, 471 by 164. The subtitle is ABC Favorit 22px / 400, `#4c2116`.

Feature bands alternate colour washes. Measured block fills include `#b1dcfc`, `#c6e57d`, `#f3fb9a`, `#e2f2fe`, `#f6eef7`, `#e7f7c1` and `#faffc4`. Feature blocks use padding `100px 88px`. Image panels use 30px radius on the outer corners.

A brown band, `.container-brown`, is `#4c2116` with 48px padding. Its heading computed as `#4c2116` on that brown, so the heading colour does not separate from the band. The "Start earning" button on that band is the yellow pill.

The footer is transparent over the page colour. Copyright and links are Favorit 16px, `#482317`. Social marks are 35px circle SVGs stroked `#482317`.

## Pricing

https://www.theleap.co/pricing/ repeats the same header. The h1 is Tobias 92px / 300, line-height 97.9px, letter-spacing -1.84px. Three plan cards sit side by side at 330px, radius 20px, padding 40px, fill `#fafafa`. Each "Sign up" button links toward signup and uses radius 20px rather than the home pill. The FAQ band uses `linear-gradient(354deg, #29a7ff 4.04%, #efedee 67.81%)`. Questions are Tobias 40px / 300, letter-spacing -0.8px. The accordion was not opened.

## Features, blog, contact, changelog

https://www.theleap.co/features/ uses the same type scale as pricing for its h1 (Tobias 92px). Feature blocks carry the colour washes above.

https://www.theleap.co/blog/ lists posts under category pills. A post title measured Tobias 54px / 300, line-height 55.35px, letter-spacing -1.08px.

https://www.theleap.co/contact/ is a text page. No form.

https://www.theleap.co/changelog/ lists dated entries. The lede is Favorit 24px, `#482317`.

## Signed-out login

https://accounts.theleap.co/login and https://accounts.theleap.co/signup both redirected to https://make.theleap.co/accounts/login. The page is "Welcome back to The Leap!" in Tobias 40px / 400 / 52.8px, `#4c2116`. The card is 768px wide, background `#fafafa`, radius 16px, padding 32px, class `bg-gray-100 md:rounded-2xl`. Body background is `#fafafa`. The form asks for email and password, then "Let's go", then "Or", then Google and Thinkific. "Help is here" goes to `/accounts/forgot-password`. There is no create-account link on that page. The form was not submitted. Google and Thinkific were not followed.

## Cookie notice

A cookie banner sits over the marketing pages. It was left open. Copy says the site uses cookies for content and advertising. Closing it was not required to read styles.
