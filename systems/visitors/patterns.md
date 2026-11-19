# Patterns

Public pages only. The signed-in product was not entered.

## Marketing home

A fixed dark pill holds Features, Pricing, Blog, Docs, Login and Register. The page is white. The h1 is 60px `#181925`. One purple pill and one quiet pill sit under the lede. A product screenshot is painted into the page; that screenshot is marketing art, not the signed-in app. See [screenshots/home-light-default.png](screenshots/home-light-default.png).

At 390px the pill keeps Login, Register and a menu glyph. The trial button becomes full width. See [screenshots/home-light-mobile.png](screenshots/home-light-mobile.png).

## Pricing

Pricing is a section on the home page (`/#pricing`), not a route. `/pricing` is the 404. The section is one card, a monthly/yearly toggle, an events slider, and the same trial pill. The trial was not followed. See [screenshots/home-light-pricing.png](screenshots/home-light-pricing.png).

## Sign-in

`/login` and `/register` are a split: a white form on the left, a map on the right. The form is an email field, a disabled Continue button, and Google and GitHub buttons. A Turnstile response field is in the DOM. Nothing was typed or submitted. See [screenshots/login-light-default.png](screenshots/login-light-default.png) and [screenshots/register-light-default.png](screenshots/register-light-default.png).

## Docs

`/docs` is a three-column docs shell: a 288px nav, a 30px title, and an "On this page" list. The current item is `#181925`. Other items are body ink. See [screenshots/docs-light-default.png](screenshots/docs-light-default.png).

## Blog and contact

`/blog` is a grid of post cards with no card fill. `/contact` points at Docs, Telegram and Email. No form was on the contact page. See [screenshots/blog-light-default.png](screenshots/blog-light-default.png) and [screenshots/contact-light-default.png](screenshots/contact-light-default.png).

## Missing route

A route the site does not have renders a 128px "404" and a quiet "Back to home" pill over the same globe. See [screenshots/notfound-light-default.png](screenshots/notfound-light-default.png).

## Public demo

`/s/godly.website` is a public stats view with a trial pill in the header. It is not an account. See [screenshots/demo-light-default.png](screenshots/demo-light-default.png).
