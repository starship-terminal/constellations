# Components

Measured on the public pages, signed out, 2026-11-19. Marketing controls are from [https://pop.site/](https://pop.site/). Auth controls are from [https://app.pop.site/?signin](https://app.pop.site/?signin). Nothing was typed into a field except focus. Nothing was submitted.

## Button

The claim control is 40px tall, radius 26px, padding 16px 24px. Its fill is `linear-gradient(110deg, #00a8f5, #3b82f6)`. The label is Satoshi 15px, weight 500, white.

![Claim your site](components/crops/button-primary.png)

Hover did not change the computed gradient. [components/crops/button-primary-hover.png](components/crops/button-primary-hover.png) matches the rest state.

The sign-in control is 36px tall, a pill, white 16px Satoshi at weight 500. The fill is `linear-gradient(90.54deg, #1e293b 6.97%, #0f172a 93.03%)` with a 1px `#475569` border.

![Sign in](components/crops/button-signin.png)

Continue with Google is a 43px pill, fill `rgba(23, 23, 23, 0.05)`, label `oklch(0.373 0.034 259.733)` at weight 500. It was not clicked. Google SSO was not entered.

![Continue with Google](components/crops/button-google.png)

## Link

Nav links are Satoshi 15px, weight 500, `#171717`, letter-spacing -0.45px. Create Account and Log In use the same style.

![Create Account](components/crops/link-nav.png)

Reset Password and Sign up are `#2563eb`, 16px, weight 500.

![Reset Password](components/crops/link-reset.png)

Profile links on the home page (`oliur.pop.site`) are `#3b82f6`.

## Text field

The claim field is 40px tall. The name side is a transparent input, Satoshi 15px weight 500, left radius 999px, padding-left 20px. The suffix is `#fafafc`, padding 16px 20px 16px 12px, right radius 9999px.

![yourname.pop.site](components/crops/field-claim.png)

The auth email field is 38px tall, radius 6px, padding 8px 0 8px 12px, border 1px `#e5e5e5`, text `#1e293b`.

![Email field](components/crops/field-email.png)

Focus adds a 2px ring, `oklch(0.623 0.214 259.815)`. The border colour stays `#e5e5e5`.

![Email field focused](components/crops/field-email-focus.png)

## Card

Section cards on the home page are white, radius 10px, padding 20px.

![Links Section](components/crops/card-section.png)

The auth shell is 420px wide, white, radius 20px, 1px `#e2e8f0`, padding 10px, shadow `rgba(0, 0, 0, 0.04) 0px 8px 32px`. The inner card is 398px, radius 10px, a white to `#f8fafc` gradient, 0.5px `#e2e8f0`, shadow `rgba(30, 58, 138, 0.1) 0px 4px 8px`.

![Sign in card](components/crops/card-auth.png)

## Badge

The home eyebrow is a 39px pill, radius 10px, fill `rgba(255, 255, 255, 0.3)`, padding 4px 12px 4px 6px.

![Join 10K+ People](components/crops/badge-pill.png)

## Gaps

Text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, table, and avatar were not on the captured pages. Disabled, pressed, loading, and error states were not on screen. A validation error was not triggered, because submitting the form would create an account or send a reset.
