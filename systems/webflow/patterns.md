# Webflow patterns

Public site only. The signed-in product was not opened. Screenshots are in [screenshots/](screenshots). The control map is [site-tree.md](site-tree.md).

## App shell and navigation

The marketing shell is a sticky header: logo, Platform, Source, Solutions, Resources, Enterprise, Pricing, Log in, and one blue CTA. On the captured homepage the blue CTA is Start for free and Contact Sales is a text link beside Log in. On pricing the blue CTA is also Start for free. A blue campaign bar sits above the header. Dark mode paints the page `#080808` and keeps the blue bar and the blue CTA. See [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/home-dark-default.png](screenshots/home-dark-default.png).

Phone replaces the links with one menu button. The open sheet lists Platform, Source, Solutions, Resources, Enterprise, and Pricing, with arrows on the menus. See [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Form with a validation error

Not captured. The contact-sales form and the login form were opened and not submitted, so no validation error was shown.

## Empty, loading, and error

Not captured as product states. Signup and some phone auth URLs showed a bot check ("Confirm you're not a bot"). That is a gate, not an app error state. See [screenshots/signup-light-wall.png](screenshots/signup-light-wall.png).

## Destructive confirmation

Not present on the public site.

## Feedback after an action

Not captured. No form was submitted, so no success toast or confirmation was shown.

## Search and filtering

Templates has a search field named `query`. It was focused and not submitted. See [screenshots/templates-light-search-focus.png](screenshots/templates-light-search-focus.png). Blog has a search input that was not submitted. Pricing filters plans with the yearly switch and with selects. The selects were not submitted.

## List or table

Pricing is a card grid: Starter, Basic, Premium, Team, Enterprise. See [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png). Customer stories and the blog are card lists.

## Onboarding

Not captured. Signup stops at a bot wall. No profile, birthday, plan, or survey field was filled.
