# Patterns

Page-level arrangements on the public signed-out surfaces, 2026-11-19.

## Marketing shell

A 72px top bar sits on `dark.color.topbar` with a 1px line at 15% white. The logo is at the left, Products / Resources / Pricing in the middle, and the two actions at the right. The page behind it is `dark.color.page`. Shot: [home-dark-default.png](screenshots/home-dark-default.png).

On a 390px width the same bar collapses to the logo and a menu button. Shot: [mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png).

The footer repeats the product list on `dark.color.page`. It was not cropped separately.

## Hero

The home hero is a centred 72px headline, a 16px lede at 70% white, and the prompt card. The headline types a second line in ("mobile product" and similar). Both home shots catch that animation mid-cycle. The grid behind the hero is a painted background, not a token.

## Pricing

Three plan columns under a 72px headline. Each column has a wordmark, a tier pill, a 32px title, a price well, a feature list and a white button. The Pro column carries the orange "MOST POPULAR" badge. Shot: [pricing-dark-default.png](screenshots/pricing-dark-default.png).

The FAQ sits below as a two-column block: a 48px heading on the left, the question list on the right. Shot: [pricing-dark-faq-open.png](screenshots/pricing-dark-faq-open.png).

## Product page

`/mwm-ai` uses the same shell and a 72px headline over a full-bleed product screenshot. Shot: [mwm-ai-dark-default.png](screenshots/mwm-ai-dark-default.png). `/mwm-console` and `/company` follow the same headline pattern. Shots: [mwm-console-dark-default.png](screenshots/mwm-console-dark-default.png), [company-dark-default.png](screenshots/company-dark-default.png).

## Directory

`/apps/` is a public index: a 72px headline, a lede, and a "LIVE APP INDEX" card with two figures. Shot: [apps-dark-default.png](screenshots/apps-dark-default.png).

## Sign-in

Console splits the viewport: a form column on `dark.color.page` and an orange panel. The form stacks a title, two provider buttons, an or-rule, email, password and a white submit. Shot: [console-sign-in-dark-email.png](screenshots/console-sign-in-dark-email.png).

Create splits the viewport the other way: a form on `#1c1c1c` and a wall of app icons. Three provider buttons, no email field on the first screen. Shot: [create-sign-in-dark-default.png](screenshots/create-sign-in-dark-default.png).

## Not captured

Signed-in app shells, checkout, and any flow that asks for a card or a phone number. The provider buttons and "Sign In" were not activated.
