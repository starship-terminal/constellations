# Patterns

Captured signed out. First readings 2026-11-19. Public pages and empty auth walls refreshed 2026-11-21. Desktop viewport 1440 by 900, devicePixelRatio 1. Phone viewport 390 by 844, devicePixelRatio 2.

## Marketing shell

[https://retool.com/](https://retool.com/) and [https://retool.com/pricing](https://retool.com/pricing) share one dark shell. `html` carries `class="scroll-pt-nav-offset dark"`. The page's own payload sets `themeMode` to dark. Body fill is rgb(21, 21, 21). Text is rgb(233, 235, 223).

The header is fixed. `--dvt-nav-height` is 5rem and `--dvt-banner-height` is 2.5rem. On 2026-11-21 the painted 1440 nav is Solution, Resources, Use cases, App gallery, Pricing and Ask AI. Audience is in the DOM and `display: none` at that width. The right side is `Sign in`, a gray-stroke `Book a demo` pill, and a cream `Start for free` pill.

The homepage h1 is saansFont, 66.7885px, weight 300, letter-spacing -1.46935px. Pricing's h1 is the same family at 54.7885px.

## Pricing grid

Four plans sit in a grid with a 12px radius and a 1px rgba(233, 235, 223, 0.2) border. Names are saansFont 21.3942px, weight 380. Visible prices included `$5/month`, `$10/month`, `$50/month` and `Custom`. Those are page copy, not tokens. No plan was started.

## Login

[https://login.retool.com/auth/login](https://login.retool.com/auth/login) is a light page, not the marketing dark theme. Body is white, Inter, 12px, color rgb(34, 34, 34). The title `Welcome back.` is Saans, 36px, weight 380. The form is 450px wide: Google button, an OR divider, email, password, a black `Sign in` button, then `Sign in with login link instead`. Nothing was typed.

## Signup

[https://login.retool.com/auth/signup](https://login.retool.com/auth/signup) asks for a work email and a password, plus Continue with Google. The fields were empty on 2026-11-21. Nothing was typed. Google was not clicked. The form was not submitted. [screenshots/signup-dark-default.png](screenshots/signup-dark-default.png)

## Docs

[https://docs.retool.com/](https://docs.retool.com/) is dark (`data-theme="dark"`). Navbar is rgb(21, 21, 21) and 80px tall. Body type is SaansReg. A banner announces the signup pause. Search was visible as a button and was not opened. The theme toggle was not used.

## Not captured

App shell after sign-in, form validation, destructive confirmation, and onboarding. Book a demo and the agents waitlist were opened only to see empty fields. No database was connected. `login-extracted` stays not-started. Phone width on 2026-11-21 covers the homepage and pricing: [screenshots/mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png), [screenshots/mobile-pricing-dark-default.png](screenshots/mobile-pricing-dark-default.png).
