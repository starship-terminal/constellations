# Patterns

Public tilda.cc pages, 2026-11-21. Screenshots are 256-colour PNGs.

## Marketing shell

The English homepage is a long block page. A transparent header sits over the first screen. Wordmark, PRICING, #MADEONTILDA, BLOG, and MORE are text links. LOG IN and SIGN UP are small TildaSans buttons. MORE opens a full menu panel (`.tmain-submenu__container`) with Platform, Support, Education, and More columns. The panel shadow is `rgba(0, 0, 0, 0.15) 0px 0px 10px`.

See [home-light-default.png](screenshots/home-light-default.png) and [home-light-menu.png](screenshots/home-light-menu.png).

## Coral call to action

Primary marketing actions are a coral fill `#fa8669` with white 15px TildaSans at weight 600, height 50px, square corners. The pricing page uses a white pill (`60px` radius, 26px type, 80px height) for the same "Create a website for free" action.

See [hero-cta-default.png](components/crops/hero-cta-default.png) and [pricing-light-default.png](screenshots/pricing-light-default.png).

## Pricing

Three plans (Free, Personal, Business) in black TildaSans on a light page. A billing control offers "Billed annually" and "Month to month". The currency `select` was in the DOM with a 0×0 box.

## Templates and FAQ

`/tpls/` is a template gallery with category radios. The selected radio chip reads coral. `/en/answers/` is a search field plus category chips (`#ececec` on `#282828`).

See [templates-light-default.png](screenshots/templates-light-default.png) and [faq-light-default.png](screenshots/faq-light-default.png).

## Auth walls

`/login/` and `/registration/` are separate screens: white type, a 1px `rgba(255,255,255,0.3)` field line, and a cream pill button `#ffe8c7` with black type and a 100px radius. A translucent panel (`.ts-form`, `rgba(255,255,255,0.1)`) holds the form. Neither form was filled or submitted.

See [login-light-default.png](screenshots/login-light-default.png) and [registration-light-default.png](screenshots/registration-light-default.png).

## Phone

At 390×844 the same header links remain. No hamburger was found. Full pages taller than 24000px were truncated and the capture log records the boundary.

See [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).
