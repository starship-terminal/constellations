# Jasper patterns

How the public pages combine the measured pieces. Captured 2026-11-18, signed out.

## Marketing shell

The header is a white bar, 80px tall, with the red wordmark, five text items (Platform, Solutions, Resources, Company, Pricing), Log In, Free Trial, and a navy Get a Demo button. Hovering Platform opens a mega-menu: three illustrated columns (Strategy, Context, Agents) plus a flame promo card. The footer is a dark island, background near `#262627`, with the wordmark in flame and quiet legal links.

See [home-light-default.png](screenshots/home-light-default.png), [home-light-menu.png](screenshots/home-light-menu.png), [footer-default.png](components/crops/footer-default.png).

## Hero

A light-blue band holds a red New chip, a Feature display headline, and two actions: a navy Get a Demo and an outlined Start Free Trial. Both leave the marketing site. Neither was followed.

See [hero-title-default.png](components/crops/hero-title-default.png), [hero-cta-default.png](components/crops/hero-cta-default.png).

## Pricing chart

`/pricing` is a comparison chart, not plan cards. Category columns sit side by side with a Start Free Trial button under the Pro column. There is no FAQ accordion on the captured page.

See [pricing-light-default.png](screenshots/pricing-light-default.png), [price-card-default.png](components/crops/price-card-default.png).

## Demo form boundary

`/demo` mounts a HubSpot form (email, first name, last name, company) beside marketing copy. The field and the submit button were measured at rest. The form was not submitted.

See [demo-light-default.png](screenshots/demo-light-default.png), [demo-field-default.png](components/crops/demo-field-default.png).

## Login boundary

`https://app.jasper.ai/` redirects to `https://app.jasper.ai/auth/login`. The card is white, with the red wordmark, Continue with Google, an email field, and a blue Continue with email. That blue is product auth chrome, not the marketing flame or navy. There is no password field. Continue with email was submitted on 2026-11-18 on both `/auth/login` and `/auth/signup`; `continueWithEmail` returned HTTP 401 and the page toasted "Failed to send login link. Please contact support for further assistance." Google was not followed. Canvas, agents, Brand IQ and campaigns were not reached.

See [signin-light-default.png](screenshots/signin-light-default.png).

## Phone

At 390 the header keeps the wordmark and Log In. The desktop menu list is `display: none`. No hamburger was mounted, so the phone menu was not captured.

See [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).
