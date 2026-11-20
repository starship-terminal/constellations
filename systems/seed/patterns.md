# Patterns

Patterns are what the opened pages showed. Screenshots are 256-colour PNGs from 2026-11-21.

## Home

A transparent header over a seed-green hero. The hero heading is snow, 48px at 1169 and 32px at 390. Two snow pills sit under it: Take the Quiz and Shop DS-01. Later sections switch to snow or foam backgrounds with seed-green type. The footer is seed green with 14px snow captions. See [home-light-default.png](screenshots/home-light-default.png) and [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

At 390 the header collapses to a logo and a two-bar menu. Open menu shows Shop, Science, Learn, and Sign in, then the Shop panel. See [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Shop index

`/products` opens on a seed-green hero (html background #1c3a13) with a snow heading at 48px. Product prices are 20px. A struck compare-at price uses the disabled text colour, rgba(28, 58, 19, 0.5). Filled Learn More pills are seed green. See [products-light-default.png](screenshots/products-light-default.png).

## Product

`/daily-synbiotic` is a snow page. A 24px title, a 14px reviews link, a 16px blurb, a 24px price, a bright-green Bestseller badge, and a full-width Start Now pill (304px at the 1169 reading, 432px in the 1440 crop). Benefit and ingredient rows are buttons in the buy column. See [synbiotic-light-default.png](screenshots/synbiotic-light-default.png).

## Shop menu

Opening Shop drops a 375px glass panel, radius 32px, under the header. Desktop menus open on hover, not click. Each product row is 75px. Shop All Products is a 14px / 500 snow link with a pill radius. See [home-light-shop-menu.png](screenshots/home-light-shop-menu.png). Science and Learn use the same glass. See [home-light-science-menu.png](screenshots/home-light-science-menu.png) and [home-light-learn-menu.png](screenshots/home-light-learn-menu.png).

## Sign in

The Sign in button opens the same glass panel. Copy says "Welcome back" and "Enter your email to access your account." One email field and a Continue pill. Nothing was typed or submitted. See [home-light-signin-email.png](screenshots/home-light-signin-email.png). `/login` is a separate snow page, "Hi, sign in.", with an empty email field and Continue. See [login-light-default.png](screenshots/login-light-default.png). Password, Google, and Facebook were not reached.

## Quiz

On 2026-11-19 `/is-ds01-right-for-you` redirected to `/lp/ds01-quiz-baseline` and showed step 1 of 13. On 2026-11-21 Playwright stayed on `/is-ds01-right-for-you` and showed step 1 of 11, "How often do you poop?", with four 72px options. No option was selected. The page says health information is handled under their consumer health policy. That is why the quiz stops at the first screen. See [quiz-light-default.png](screenshots/quiz-light-default.png). `/find-your-routine` is a second quiz. It was opened and not answered. See [routine-light-default.png](screenshots/routine-light-default.png).

## Science

`/approach` has a bright-green promo bar (40px) and 64px / 300 display headings. No dark theme switch was on the page. See [approach-light-default.png](screenshots/approach-light-default.png).

## Cart

Cart is a dialog on the current page, not `/cart`. Empty state: "Your cart is empty", total $0.00, Checkout not pressed. See [products-light-cart.png](screenshots/products-light-cart.png).

## Locale

The footer country control is a listbox: CAD / Canada, USD / United States. It was opened on `/login` and not changed. See [login-light-locale.png](screenshots/login-light-locale.png). The same control on the homepage was covered by a promo lightbox and that shot was not kept.
