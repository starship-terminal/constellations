# Patterns

Signed-out public pages. The dashboard mock in the home hero is a marketing demo, not the signed-in app.

| Pattern | Where | Screenshot |
|---|---|---|
| Marketing home | Black nav, chartreuse marquee, serif hero, two pills, product demo frame | [home-light-default.png](screenshots/home-light-default.png) |
| Home, phone | Same page at 390 CSS px. Nav collapses to a menu button. h1 computes to `39px`. | [home-light-phone.png](screenshots/home-light-phone.png) |
| Pricing | Serif title, Monthly/Yearly pills, four plan columns. Yearly is selected on load. | [pricing-light-default.png](screenshots/pricing-light-default.png) |
| Blog index | Same nav. Article cards. | [blog-light-default.png](screenshots/blog-light-default.png) |
| Example schools | Same nav. Filter chips and school cards that link off-site. | [examples-light-default.png](screenshots/examples-light-default.png) |
| Legal | Privacy policy. h1 is the marketing `5rem` serif. | [privacy-light-default.png](screenshots/privacy-light-default.png) |
| Not found | HTTP 404, "Page Not Found", yellow "Go to Homepage" pill. | [not-found-light-default.png](screenshots/not-found-light-default.png) |
| Sign-in chrome | White page, Reckless heading, email and password fields, yellow Log In button, Forgot Password and Sign Up links. Measured, not screenshotted. | gap |

The accounts form sits in a `420px` column, centred, with `40px` horizontal padding on its wrapper. There is no card shadow around the form.

## Not captured

- Signed-in school admin, course builder, and student view.
- Sign-up, password reset, and checkout. The marketing "Start for free" links go to `sso.teachable.com` with a plan id. That form asks for a password, so it was not submitted.
- Cookie banner: a Hotmart cookie panel is in the DOM and visible on the pricing screenshot. Its OK button was not pressed.
- Search, empty, loading, and destructive confirmation. None of those states appeared on the public pages.
