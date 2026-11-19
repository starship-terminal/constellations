# Patterns

How the public pages are built. Screenshots are viewport captures at 1440x900
(desktop) and 390x844 at 2x (phone), after the cookie banner was dismissed
with Required only except where a shot still shows it.

## Marketing shell

Sticky header, 96px tall on desktop, transparent over the hero, 77px on the phone. Wordmark left, Product / Examples / Blog / Pricing, then Sign In and a black Download for free button. Product opens a full-bleed white mega-menu. Phone replaces the links with a hamburger that opens a white drawer ending in Sign in and Download for free.

[screenshots/home-light-default.png](screenshots/home-light-default.png)
[screenshots/home-light-nav-open.png](screenshots/home-light-nav-open.png)
[screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png)
[screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png)

## Hero

White type on a blue-violet wash, centred. Display headline, a two-line lede, one black primary button. The wash is painted, not a CSS gradient on the section. A product screenshot sits under the fold. A blue chat bubble is fixed at the bottom right (an iframe; not opened).

## Interior page

Same header. Black display headline on white, often over a faint blue wash at the right edge. Body sections alternate white, `#fafafc` (`.site-section--gray-light`, 156px padding) and `#f2f2f4` (`.site-section--gray-dark`).

[screenshots/features-light-default.png](screenshots/features-light-default.png)
[screenshots/how-it-works-light-default.png](screenshots/how-it-works-light-default.png)
[screenshots/download-light-default.png](screenshots/download-light-default.png)
[screenshots/examples-light-default.png](screenshots/examples-light-default.png)
[screenshots/stories-light-default.png](screenshots/stories-light-default.png)
[screenshots/integrations-light-default.png](screenshots/integrations-light-default.png)
[screenshots/enterprise-light-default.png](screenshots/enterprise-light-default.png)
[screenshots/blog-light-default.png](screenshots/blog-light-default.png)

## Pricing

Two plan cards side by side, white, 24px radius, soft shadow. Pro leads with a blue title and a black price. Enterprise leads with a blue title and a "Everything in Pro plus" row. No billing switch.

[screenshots/pricing-light-default.png](screenshots/pricing-light-default.png)
[screenshots/mobile-pricing-light-default.png](screenshots/mobile-pricing-light-default.png)

## Footer

White, 128px top padding, 14px type. Four link columns, a newsletter field (4% black, 8px radius, 48px) and a Subscribe button. Legal row: Cookie Statement, Terms, Privacy. Subscribe was not pressed.

## Cookie notice

White bar over the lower hero. 14px sentence, a blue Cookie Statement link, Required only (grey) and Allow all (black). Required only was the only press used to dismiss it.

## Signed-out app

Split layout at 1440: a 485px `#d6f3ff` panel with the wordmark, a short line, and an illustration; a white form column. Phone drops the panel and centres the form under the wordmark.

Sign in: email, password, disabled Sign in until the fields validate, an "or" rule, Sign in with Google, Sign in with SSO, then a trial card with a platform menu and a blue Download for free. None of those actions were taken.

Sign up: first name, last name, email, password, two checkboxes, a disabled Sign up, Sign up with Google. Not submitted. The form asks for a name and a password, so it is not an email-only signup.

[screenshots/signin-light-default.png](screenshots/signin-light-default.png)
[screenshots/signup-light-default.png](screenshots/signup-light-default.png)
[screenshots/mobile-signin-light-default.png](screenshots/mobile-signin-light-default.png)

## What these pages do not show

The signed-in product, the desktop app, a payment step, a validation error, an empty dashboard, a loading state, and a destructive confirm. `/n/forgot` is a 404. `support.overflow.io` returned 403.
