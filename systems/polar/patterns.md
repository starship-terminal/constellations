# Patterns

Public signed-out Polar, refreshed 2026-11-21. Desktop shots are 1440 by 900. Phone shots are 390 by 844. Marketing pages paint dark. Docs paint light.

## Marketing shell

https://polar.sh/ uses a dark bar. Links: Features, Docs, Blog, Company. Actions: Sign in and Get Started (white pill). `html` class is `antialiased dark`. [screenshots/home-dark-default.png](screenshots/home-dark-default.png) shows the shell. Features and Docs open hover panels on the same page: [screenshots/home-dark-features-menu.png](screenshots/home-dark-features-menu.png) and [screenshots/home-dark-docs-menu.png](screenshots/home-dark-docs-menu.png).

On a 390-wide viewport the labels collapse. "Toggle Sidebar" opens a drawer: Overview, Integrate, Documentation, Pricing, Blog, Company, Open Source, Polar on X, Login. [screenshots/mobile-home-dark-menu-open.png](screenshots/mobile-home-dark-menu-open.png) shows it.

The hero dashboard is a painted demo. Acme Inc, joe@acme.com and the Visa line are the site's own copy.

## Auth wall

https://polar.sh/signup redirects to https://polar.sh/auth. The card says "Welcome to Polar". Buttons: Sign in with Google, Sign in with Apple, Sign in with GitHub, an "or" divider, an empty email field, and Sign in with email. The header Sign in button opens the same wall as a dialog on the marketing page. Nothing was typed. Identity providers were not clicked. [screenshots/auth-light-default.png](screenshots/auth-light-default.png), [screenshots/signup-light-default.png](screenshots/signup-light-default.png), [screenshots/home-dark-signin-dialog.png](screenshots/home-dark-signin-dialog.png), [screenshots/mobile-auth-light-default.png](screenshots/mobile-auth-light-default.png).

## Pricing

https://polar.sh/resources/pricing is a long public document. `/pricing` is a 404. [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png) and [screenshots/mobile-pricing-dark-default.png](screenshots/mobile-pricing-dark-default.png). No checkout was opened.

## Docs

https://polar.sh/docs/introduction is a Mintlify shell. Page background is white in light and near-black in dark. The sidebar lists Products & Pricing, Checkout and the rest. Theme controls sit in the top bar. Dark was opened, then light was restored. [screenshots/docs-light-default.png](screenshots/docs-light-default.png) and [screenshots/docs-light-dark.png](screenshots/docs-light-dark.png).

## Blog, company, integrate, feature

https://polar.sh/blog lists post cards. https://polar.sh/company is the team page. https://polar.sh/integrate and https://polar.sh/features/usage-billing repeat the marketing shell. [screenshots/blog-dark-default.png](screenshots/blog-dark-default.png), [screenshots/company-dark-default.png](screenshots/company-dark-default.png), [screenshots/integrate-dark-default.png](screenshots/integrate-dark-default.png), [screenshots/feature-dark-default.png](screenshots/feature-dark-default.png).

## 404

https://polar.sh/login and https://polar.sh/pricing render "We can't find the page you're looking for." with a Go to homepage pill. [screenshots/notfound-light-default.png](screenshots/notfound-light-default.png).

## Not captured

Signed-in dashboard, checkout, payout, bank, and KYC. Button hover, focus, pressed and disabled. Element crops. `login-extracted` is not-started.
