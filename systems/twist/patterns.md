# Patterns

## Shell

A top bar with the wordmark on the left and Features, Benefits, Why async?, Pricing, and Log in on the right. At 390 the links collapse to Log in and a menu button. The menu was not opened.

Under the bar, a cream banner says Twist is being replaced by Todoist Comms and will close on March 1, 2027. The two links go to a help article and a Typeform waitlist. Neither was followed.

Screenshots: [screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/home-light-phone.png](screenshots/home-light-phone.png).

## Hero

Tiempos Headline at 86px, weight 300, on `#FAFAFA`. The lede is Inter 21px. Below it, a product illustration with a Play control. The illustration is a public demo, not the signed-in app.

## Pricing

Two columns, Free plan and Unlimited, with no card fill and no shadow. A teal Log in button sits to the left. Yearly is selected. Monthly was clicked and Unlimited moved from US$6 to US$8 per user. The button links to `/login`. It was not used as a checkout.

Screenshot: [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).

## Why async

A long-form page. The h1 is Tiempos Headline 74px. No primary button was in the first viewport.

Screenshot: [screenshots/async-light-default.png](screenshots/async-light-default.png).

## Sign up or log in

`/login` is one form for both. Continue with Google and Continue with Apple sit above an email field. Continue with email stays `#99D0DB` until an address is typed, then `#008AA6`. Submitting the AgentMail address opened a gate ("If you're looking for a messaging app that…") and then a profile form asking for a full name and a password. The profile form was not filled. Google and Apple were not clicked.

No login screenshot. The preview browser could not produce frames, and Playwright was not pointed at the login page.
