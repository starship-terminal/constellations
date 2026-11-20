# Patterns

Signed out. Desktop shots are 1440 by 900 CSS pixels at device pixel ratio 2. Phone shots are 390 by 844.

## Marketing home

A 72px header holds the wordmark and Pricing, Blog, Create Account, Log In. The hero is centred in a 1000px column, with 80px of padding above and below. The claim field and the blue pill sit on one row at 1440. At 390 the nav does not collapse, and the claim control drops under the field.

![Home](screenshots/home-light-default.png)

![Home at 390](screenshots/home-light-phone.png)

The page is long (about 10966px in the preview tab). The full shot is [screenshots/home-light-full.png](screenshots/home-light-full.png). Phone mockups in the hero are product demos, not the signed-in app.

## Pricing

Pricing is a short page. The hero sits on a purple image. The only measured type on that hero is the 51px heading "Free to create and share." and the 19px line "For pro-level features, plans start at just $10/mo". There is no plan table. The claim field repeats.

![Pricing](screenshots/pricing-light-default.png)

## Blog

The blog index is a list of posts with a date and, on one row, a "Pro Tips" pill. The title is the 51px display style.

![Blog](screenshots/blog-light-default.png)

## Sign in and sign up

Both screens are the same card on a `#f3f3f3` page with a pale blue radial wash. Sign in asks for email and password, then Google. Sign up asks for email and a password, then Google. Neither form was submitted. Google was not clicked.

![Sign in](screenshots/signin-light-default.png)

![Sign in, email focused](screenshots/signin-light-focus.png)

![Sign up](screenshots/signup-light-default.png)

![Sign in at 390](screenshots/signin-light-phone.png)

`prefers-color-scheme: dark` did not change either surface. The dark-scheme shots match the light ones.
