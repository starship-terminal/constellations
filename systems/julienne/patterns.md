# Patterns

How the public pages combine the components. Screenshots are 256-colour PNGs. Read values from [tokens.json](tokens.json).

## App shell

The product header is fixed, 80px, transparent, with the mark, Discover and Cookbook, a glass search pill, Log in and the theme toggle. It sits on `/`, `/discover`, recipe pages, search, collections and `/privacy-policy`.

![Home](screenshots/home-light-default.png)

The marketing pages (`/team`, `/roadmap`, `/shop`) use a different header: wordmark, social links, Shop, Say hi, and a Menu button.

![Team](screenshots/team-light-default.png)

Phone width keeps the same header and stacks the hero.

![Home, phone](screenshots/mobile-home-light-default.png)

## Search and filtering

Discover opens on "Browse all" and a row of meal and diet chips. Selecting Breakfast is a local toggle. It filters the grid in place. The ingredient browse on the home page links to `/search?ingredients=…`, which is a published result page, not a typed query.

![Discover](screenshots/discover-light-default.png)

![Breakfast selected](screenshots/discover-light-filtered.png)

![Ingredient search](screenshots/search-light-default.png)

## Data display

A collection is a title in EB Garamond and the same recipe cards. A recipe page is a 48px title, a byline, ingredients and steps. Cook and Save sit on the page and were not pressed.

![Collection](screenshots/collection-light-default.png)

![Recipe](screenshots/recipe-light-default.png)

## Form at rest

`/signup` and the Log in dialog are the same card: email, password, agreement, a disabled Create account, and Google and Apple. The form was not filled in and not submitted.

![Signup](screenshots/signup-light-default.png)

## Empty

`/cookbook` signed out is a single line, "Come back soon."

![Cookbook boundary](screenshots/cookbook-light-default.png)

## Dark

The header Toggle theme control sets `html.js.dark`. The page becomes `#131313` and the display type turns white. Glass fills drop to about 7% white.

![Home, dark](screenshots/home-dark-default.png)

## Loading, error, destructive, feedback, onboarding

Not present on the signed-out surfaces. The signup page can show "Security verification failed" when its Turnstile widget does not complete. That widget was not solved, and the message is a boundary, not a captured error pattern.
