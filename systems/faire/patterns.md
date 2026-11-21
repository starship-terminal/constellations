# Faire patterns

How the public signed-out pages combine the components. Screenshots are in [screenshots/](screenshots). The control map is [site-tree.md](site-tree.md).

## App shell

A white header, 108px tall at 1440, holds the logo, All categories, a language list, Blog, Sign up to sell, Sign in, and Sign up to buy. A second row lists category links. The page wash behind the marketing content is #fbf8f6. The footer is a white band with company, product, and legal links.

Screenshot: [home-light-default.png](screenshots/home-light-default.png).

## Hero

The home hero is a photograph with a white Nantes display line, "Find your next bestseller", at 52px. The primary button sits in the header, not in the hero. Sign up to buy is repeated down the page and opens the same signup modal.

## Catalog

Category pages keep the shell and add a white title over a photo, then filter pills and a grid of brand cards. All filters is a pill. Opening a card goes to `/brand/<id>`. Unlock wholesale pricing and Add to cart stop at sign-in.

Screenshot: [category-light-default.png](screenshots/category-light-default.png), [brand-light-default.png](screenshots/brand-light-default.png).

## Search and filtering

The help center has a search field. It was not submitted. Category filters were visible and not applied.

## Empty, loading, error

Not captured as designed states. Two support articles returned a Cloudflare 429 page. That is a block, not a Faire error component.

## Form with a validation error

Not captured. The sign-in form was opened and not submitted.

## Destructive confirmation

Not present on the public surface.

## Feedback after an action

Not captured. No action was submitted.

## Onboarding

Not captured. Signup and apply were not entered.

## Phone

At 390 the header collapses and a menu control opens a drawer.

Screenshot: [mobile-home-light-default.png](screenshots/mobile-home-light-default.png), [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).
