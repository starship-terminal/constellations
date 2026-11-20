# Patterns

How the public LottieFiles site combines the measured controls. Screenshots are in [screenshots/](screenshots).

## App shell

The desktop header is a sticky white bar: logo, five menus (Products, Integrations, Tools, Customers, Learn), a Pricing link, a search button, an English locale menu, Log in, and a teal Sign up. See [home-light-default.png](screenshots/home-light-default.png).

Phone width drops the menus. The top bar is the logo, a search icon, and a menu icon. See [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

## Navigation menus

Products, Tools, and Customers open on click. Integrations and Learn open on hover. Each menu is a white panel of links with a short description. See [home-light-products-menu.png](screenshots/home-light-products-menu.png).

## Search

Search animations opens a dialog with a text field. Typing a query does not submit a form. See [home-light-search.png](screenshots/home-light-search.png).

## Login wall

Log in opens a modal from login.lottiefiles.com: Google, other providers, and enterprise login. The capture stops there. See [home-light-login-wall.png](screenshots/home-light-login-wall.png).

## Hero

A 96px DM Sans headline, a 24px muted supporting line, a 48px teal primary link, and a 48px quiet bordered button. Four feature chips sit under the hero.

## Pricing

Plan names and prices on a long comparison page. No monthly/yearly toggle was found. See [pricing-light-default.png](screenshots/pricing-light-default.png).

## Catalog

Featured animations are a filterable card grid. A card opens a public player page. Download was visible and was not completed. See [animations-light-default.png](screenshots/animations-light-default.png).

## Empty, error, onboarding

The known missing route `/login` is a 404 page. See [not-found-light-default.png](screenshots/not-found-light-default.png). Onboarding, toasts after a save, and destructive confirmations sit behind the login wall and were not captured.
