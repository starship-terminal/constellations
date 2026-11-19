# Patterns

Signed-out marketing pages. Screenshots are viewport captures at the measured CSS size, deviceScaleFactor 2, so a 1440 CSS viewport is a 2880-pixel PNG. A cookie overlay (`rgba(0, 0, 0, 0.7)`) was hidden for the shots and never answered.

| Pattern | Where | Shot |
|---|---|---|
| Home with signup card | https://www.skillshare.com/en/ | [home-light-default.png](screenshots/home-light-default.png) |
| Home at 390 | same URL, innerWidth 390 | [home-light-mobile.png](screenshots/home-light-mobile.png) |
| About | /en/about, dark nav, photo hero, gray content | [about-light-default.png](screenshots/about-light-default.png) |
| Teach | /en/teach, 74px white headline, mint Sign Up to Teach, purple band | [teach-light-default.png](screenshots/teach-light-default.png) |
| Teams | /teams, black nav, mint Get Started and See Plans | [teams-light-default.png](screenshots/teams-light-default.png) |
| Press | /en/press, same marketing nav as About | [press-light-default.png](screenshots/press-light-default.png) |
| Terms | legal.skillshare.com, black header, mint Search submit | [terms-light-default.png](screenshots/terms-light-default.png) |

The home nav is an 80px white bar with 16px 20px padding: wordmark, Browse, a 500px search field, Sign In, and a mint Sign Up. The hero sits a signup card on the right: "Get 7 free days of Skillshare" at 22px/700, then Google, Facebook, Apple, and a purple text button. The card was not submitted.

About, Teach, and Press invert the same bar to `{color.ink-soft}` and paint the nav labels white. Teams uses a black bar and a filled Sign In (`{color.ink-soft}` face, white label, 16px, 4px radius).

## Not captured

Class pages, teacher profiles, browse, and the blog hit a Cloudflare challenge in headless Chromium. The signed-in classroom, membership checkout, and the Sign In sheet were not entered.
