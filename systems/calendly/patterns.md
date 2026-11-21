# Patterns

How the public site combines the components. Screenshots are in [screenshots/](screenshots/).

## Marketing shell

A 68px sticky header on magnolia (`--color-surface-bg-primary`), a wordmark, three hover menus, then Talk to sales, Log In, and a midnight Get started button. The footer repeats product, feature, integration, solution, resource, and company columns, then store badges and a legal row. Desktop: [home-light-default](screenshots/home-light-default.png). Phone: [mobile-home-light-default](screenshots/mobile-home-light-default.png) and the drawer [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Hero signup

The homepage hero is a blue gradient with a serif headline, two identity-provider buttons (not opened), and a quiet "Sign up with email" link. The same pair of provider buttons repeats on the login and signup walls.

## Pricing

Plan cards in a row, a FAQ accordion below. CTAs leave the page for /signup or /contact. No checkout was started. [pricing-light-default](screenshots/pricing-light-default.png).

## Auth wall

A centered white card on the marketing gradient (login, signup) or on a plain gray app canvas (`/app/login`, `/app/signup`). One email field, a midnight continue button, an "or" rule, then Google and Microsoft. See [login-review.json](login-review.json).

## Public booking

A separate, quieter surface: a white card, a "Powered by Calendly" ribbon, an avatar initial, and one event row that opens a date picker. [booking-light-default](screenshots/booking-light-default.png), [booking-event-light-default](screenshots/booking-event-light-default.png).

## Empty, loading, error, confirmation

Not captured. The booking month with no times is the only empty state on screen ("No times in November"). No destructive confirmation, toast, or search-results state was opened. Help search was not submitted.
