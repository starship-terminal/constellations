# Patterns

How the public pages are built. Screenshots are in [screenshots/](screenshots/).

## Store shell

Every store page shares one chrome. A 40px announcement strip sits above a black header. The header holds a 36px menu button, the wordmark, a home icon, a search field, an outline CREATE link, and a ghost SIGN IN button. At 390 the search field is not in the header. CREATE stays.

[home-dark-default.png](screenshots/home-dark-default.png) shows the desktop shell. [home-dark-mobile.png](screenshots/home-dark-mobile.png) shows 390.

The menu opens a list of Phonic uppercase links: Careers, Open Letter, Gift cards, Customer reviews, Privacy, Help, Contact, Newsletter. [home-dark-nav-open.png](screenshots/home-dark-nav-open.png).

The footer repeats those links under "Company" and ends with "Shipping worldwide" in the display face. [home-dark-footer.png](screenshots/home-dark-footer.png).

## Home feed

The home page is a black storefront. A welcome line, a personalize sentence in Lateral, and a coral START ONBOARDING button sit over a blurred shoe. Below that, coral section bars name "Today's top shoes", "Selected for you", and "All time favourites". Ranked rows carry a number, a shoe image, a bold title, a muted creator name, colour dots, a price, and sometimes a sold-out badge.

Onboarding was not continued. The button was measured at rest.

## Product

[product-dark-default.png](screenshots/product-dark-default.png) is `/products/pdf-bol-sneaker`. A large shoe image sits beside a 443px panel with a 12px radius. The panel holds the title, creator, price, colour tiles, a reviews outline button, a heart control, and a 56px BUY NOW. BUY NOW was not followed. No size was chosen and no card was entered.

## Content pages

FAQ, the open letter, shipping, how to scan, and careers share the shell and a large Lateral Zeller TM heading. FAQ questions are `details` rows. [faq-dark-open.png](screenshots/faq-dark-open.png) shows one answer open. [why-dark-default.png](screenshots/why-dark-default.png), [shipping-dark-default.png](screenshots/shipping-dark-default.png), and [scan-dark-default.png](screenshots/scan-dark-default.png) are the other content pages.

## Lists

[creators-dark-default.png](screenshots/creators-dark-default.png) ranks creators. [reviews-dark-default.png](screenshots/reviews-dark-default.png) is the public wall of love. Reviewer names are published on that page. No review was written.

## Forms that were not submitted

[newsletter-dark-default.png](screenshots/newsletter-dark-default.png) is an email field and a coral button. Nothing was typed or sent.

[signin-dark-default.png](screenshots/signin-dark-default.png) is a light card on the black page: Google, an email field, Continue, Use phone, and Sign up. None of those were used. The phone control was not opened.

## Missing routes

`/collections/all` paints the same 404 as a made-up page: "Hey, this is 404." [notfound-dark-default.png](screenshots/notfound-dark-default.png).

## Theme

There is one painted theme. The page is black. Semantic tokens live on `.dark`. No light store theme was found.
