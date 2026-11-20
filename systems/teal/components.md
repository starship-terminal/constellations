# Teal components

Measured on the public pages and the signed-out app on 2026-11-19. Values are token names where a token exists. Raw numbers are in [raw/readings.json](raw/readings.json). No crops: the preview browser did not produce screenshot frames.

## Button

Marketing primary, `a.btn--yellow` "Build My Resume": height `core.size.cta` (53px), padding 16px 32px, radius `core.radius.pill` (100px), fill `light.color.yellow`, text `light.color.onYellow`, Roobert 20px weight 600, tracking -0.4px.

Header "Sign up": height `core.size.headerSignup` (41px), padding 10px 24px, same yellow, text `light.color.onYellowHeader` (`#2D2D2D`), 15px weight 500. Class declares `hover:brightness-95`.

Header "Log in": height `core.size.headerLogin` (43px), padding 10px 24px, white fill, 1px `light.color.loginBorder`.

App "Sign in" and "Get Started": height `core.size.authButton` (40px), padding 8px 32px, radius `core.radius.authButton` (24px), fill `app.color.accent` (`#f4b301`), text `app.color.onAccent`, Inter 14px weight 600. Class includes `active:scale-95` and `duration-75`. Pressed was not captured.

"Continue with LinkedIn": 40px, radius 24px, fill `app.color.linkedin`, text `app.color.onLinkedin`, weight 500. Not followed.

Pressed, loading and disabled were not captured.

## Icon button

The phone menu button is in the header with class `lg:hidden` and measured 0 by 0 at 1169px. Not captured as a visible control.

## Link

Footer link: Roobert 13px / 19.2px, colour `light.color.onDark`, on the pheasant footer.

App "Forgot Password?" and "Create an account": Inter 14px, underlined, colour `app.color.brand`.

Nav links declare hover colour `light.color.navHover`. Rest colour is `light.color.ink`.

## Text field

Sign-in email and password, and the sign-up email: height `core.size.field` (36px), width `core.size.authForm` (384px), padding 8px 12px (password adds 40px on the right for the show control), radius `core.radius.xs` (3px), border `core.borderWidth.hairline` solid `app.color.border`, Inter 14px. Placeholder is the label text. Not filled. Not submitted.

Focus on the email field: outline none, box-shadow `core.shadow.fieldFocus`.

## Text area, select, checkbox, radio, switch

Not present on the captured pages.

## Tabs

Hero tabs ("AI Resumes", "Job Tracker", "Matching Mode"): 47px tall, padding 0 12px 0 0, no radius, colour `rgb(34, 34, 34)`, Roobert 16px. The current tab has class `w--current`. A distinct selected colour was not computed.

How it Works tabs are the same family (`n-tab-home`), gap 8px, padding 0 0 10px.

The resume-checker page has text tabs ("Resumes" current, white with a 2px bottom border; "Cover Letters" at 35% white). Those sit on a dark hero that was not given its own surface token, because the hero background colour was not isolated from the page.

## Menu

Tools and Resources rows are in the DOM: padding 12px, gap 16px, radius 8px, declared hover background `light.color.menuHover`. The open panel was not measured.

## Tooltip, dialog, toast

Not present.

## Card

Feature cards: background `light.color.tealSoft`, radius `core.radius.card` (16px), padding 24px.

Home pricing columns: 460px wide, 566px tall, bottom radius `core.radius.pricingCard` (24px). One is `light.color.chickadee`. One is `light.color.teal` with white text.

Pricing testimonials: background `rgb(85, 87, 191)` (`--colors--purple-600` is `#5557bf`), radius `core.radius.testimonial` (13px).

## List row, table, avatar, badge

Not captured as those components. The pricing page compares Free Forever and `$13 per week` in 16px weight 600 columns. The `$13` figure is 84px.

## Gaps

- No component crops. Preview frames failed. Headless Chromium saved only the privacy page. Home, pricing, the resume checker, sign-in and sign-up have no PNG.
- Hover, pressed, loading, error, disabled, checkbox, radio, switch, select, textarea, toast, dialog, tooltip and avatar were not on the pages, or were not opened.
- The signed-in app was not entered. Sign-up asks for email or LinkedIn. It was not submitted.
- Phone width was not measured.
