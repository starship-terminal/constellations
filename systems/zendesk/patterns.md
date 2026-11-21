# Patterns

How the public signed-out pages are put together. Screenshots are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## Site tree

Which control opens which page is in [site-tree.md](site-tree.md). Opened menus, the cookie dialog, the phone drawer, and the footer are in [screenshots/site-tree/](screenshots/site-tree/).

## Marketing home

A promo strip (fill not sampled; the cookie dialog covered it), a white header, then a dark hero (rgb(17, 17, 13)) with a photograph, a cream display line, a white email field and a lime submit. Below that the page returns to white, with one forest-green band (rgb(32, 53, 36)) for a report.

[home-light-default.png](screenshots/home-light-default.png)

At 390 the nav collapses to a menu icon and the hero type sits on white above the photograph.

[mobile-home-light-default.png](screenshots/mobile-home-light-default.png)

## Cookie dialog

OneTrust covers the first paint. Accept all, Reject all, and Cookie settings. Accepting it is a preference, not an account action.

[home-light-cookie.png](screenshots/home-light-cookie.png)

## Login

Subdomain first. The field ends in `.zendesk.com`. Sign in is lime and full width. Start free trial is a quiet button. Product links (Chat, Sell, Sunshine Conversations) sit below a rule. The form was not submitted.

[login-light-default.png](screenshots/login-light-default.png)

[mobile-login-light-default.png](screenshots/mobile-login-light-default.png)

## Pricing

Four plan cards on a raised fill, radius 40px. The popular plan carries a black pill badge. Buy now is the same lime as the nav primary. The headline paints the second clause in green (rgb(112, 163, 42)).

[pricing-light-default.png](screenshots/pricing-light-default.png)

## Register

A white dialog over a dimmed product screenshot. The email field arrived already invalid. Get started was not pressed. No card field was shown on this step.

[register-light-default.png](screenshots/register-light-default.png)

## Contact

A two-column sales form: name, email, message, country, and a lime Send message. The public sales phone line was covered in the screenshot before commit. The form was not submitted.

[contact-light-default.png](screenshots/contact-light-default.png)

## Help centre

A dark welcome band, a pill search, and a pill Free trial in the header. Search was not run. Sign in was not followed.

[help-light-default.png](screenshots/help-light-default.png)

## Not found

The unknown path falls through to an older Zendesk page (teal links, square fields, a different header). It is not the current marketing system.

[notfound-light-default.png](screenshots/notfound-light-default.png)

## Garden

garden.zendesk.com is Zendesk's product design system site. It uses system-ui, a mint page, and no custom properties on the homepage. It is not the marketing system captured here.

[garden-light-default.png](screenshots/garden-light-default.png)
