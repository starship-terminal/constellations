# Weekrise patterns

Public pages only. The signed-in planner was not entered.

## Marketing shell

A 61px transparent nav sits on the page. The wordmark is left. Pricing, Academy, a grey Login chip and a blue Signup chip are right. At 390px the links hide and a 30px menu button replaces them. The footer is #fcfcfc, padding 60px 15px, with blue links for Privacy, Terms, Payment Policy and Imprint.

See [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/home-light-phone.png](screenshots/home-light-phone.png).

## Hero

The first band is a header whose background colour is #ffaaaa and whose image is `linear-gradient(19deg, #ddddff 20%, #ffcccc 100%)`. The headline is Inter 73.6px / 700 at 1440 and 32px / 700 at 390. The subhead is Inter 36.8px / 500. Two buttons sit under it: filled Get Started and outlined Learn more. A product demo frame starts below the fold. That frame is a marketing illustration, not the signed-in app.

## Section bands

Later bands switch fill: #1a1a1a with white type for the command-palette section, #efefef for collaboration, #2481ff for boards, #fafafa cards for the feature grid. One headline word switches to Playfair Display. Content columns measure 1200px, and the hero copy column measures 684px.

## Pricing

Pricing is a section on the homepage, reached by the Pricing nav button, which scrolls the page. Three cards: Free $0, Pro $4, Team $12. The middle card is the brand blue. The right card is purple. Copy under the cards says taxes are added at checkout. Checkout was not opened.

See [screenshots/home-light-pricing.png](screenshots/home-light-pricing.png).

## Academy

`/academy` reuses the marketing nav and the same gradient hero, then a two-column article: a list of topics on the left and the essay on the right, with a next-article card at the end of the viewport.

See [screenshots/academy-light-default.png](screenshots/academy-light-default.png).

## Legal

`/privacy` and `/terms` drop the gradient. A 40px / 600 title sits on white, body 16px / 400, section headings 24px / 700. Links inside the prose paint the brand blue.

See [screenshots/privacy-light-default.png](screenshots/privacy-light-default.png).

## Auth

`/auth/login` and `/auth/signup` are a split page at 1440. The left half is white, padding 100px 60px, with a 480px form. The right half is a panel with `background-image: url(https://weekrise.com/auth/bg.svg)` and white type: "Welcome to Weekrise" at 60px / 800. At 390px the right panel is `display: none` and the form is 360px wide.

Login asks for email, then Continue, then Sign in with Google. Signup asks for name and email, then the same two buttons. Neither form was submitted. Google was not used.

## Not on these pages

No empty state, no error toast, no destructive confirm, no search, no onboarding, no signed-in shell. The mobile menu did not open.
