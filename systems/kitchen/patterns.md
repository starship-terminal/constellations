# Kitchen.co patterns

How the public pages are put together. Screenshots are the evidence. Values live in [tokens.json](tokens.json).

## Marketing chrome

A black promo bar sits above a white header. The wordmark is a chef-hat mark plus "Kitchen.co". Desktop nav is Features, Solutions (a hover menu), Pricing, Tutorials, Affiliate Program, then an outline Log in and a filled ink Try it FREE. Phone width replaces the nav with a Menu control that opens a full-width list and stacks the two actions.

See [home-light-default](screenshots/home-light-default.png) and [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png).

## Hero

Centered Graphik. A small bold kicker, a 72px headline, an 18px paragraph, then one coral button. The home page follows with a before/after illustration, not a product screenshot of the signed-in app.

See [home-light-default](screenshots/home-light-default.png).

## Pricing

Three plan columns on white: Free (ink button), Agency White-label on a sand field (coral button), Lifetime (ink button, with a coral text link for the one-time price). FAQ rows sit below as an accordion. Pay Now links leave the site for Stripe and were not followed.

See [pricing-light-default](screenshots/pricing-light-default.png) and [pricing-light-faq-open](screenshots/pricing-light-faq-open.png).

## Login boundary

`/login` redirects to `/login/workspace`. The page asks for a workspace slug, shows `.kitchen.co` beside the field, and offers Continue. Continue was not pressed. The workspace app itself was not captured.

See [login-light-default](screenshots/login-light-default.png).

## Get started and demo

`/get-started` is an email field and a submit button. `/get-demo` is a request form. Neither was filled or submitted. Those are the signup and demo boundaries.

See [get-started-light-default](screenshots/get-started-light-default.png) and [get-demo-light-default](screenshots/get-demo-light-default.png).
