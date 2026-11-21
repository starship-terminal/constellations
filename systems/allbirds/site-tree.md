# Allbirds public site tree

Mapped from https://www.allbirds.com/ on 2026-11-21, signed out, before the screenshot pass. The page title was "Allbirds: Comfortable, Sustainable Shoes & Apparel" and the response was 200. This is a live Shopify storefront, not a parked domain.

There is no theme switch. The only region control is the shipping dialog "Where are we shipping to?" with US and SG. That dialog was closed by choosing US so the header could be read. No email was typed. No password was typed. No form was submitted. No identity provider was clicked. Nothing was added to the cart.

Account sign-in is not in the header. `/account/login` redirects to `accounts.allbirds.com` and stops at an email wall. The query string on that redirect carries signing parameters and is not copied here.

## Promo bar

A swiper sits above the floating nav. Previous and next arrows change the slide. They do not navigate.

| Control | Opens |
|---|---|
| Shop Men | `/collections/bfcm-mens` |
| Shop Women | `/collections/bfcm-womens` |
| Previous / next arrows | The other promo slide, same page |

A second slide reads "Free ground shipping on orders over $100". It has no link of its own.

## Header

The wordmark and the four nav items sit in a white rounded bar. Search is an icon link. The cart control is a button labelled "View Cart". It shows the count (0 on this visit).

| Control | Opens | Stop? |
|---|---|---|
| Wordmark | `/` | |
| HOLIDAY SALE | `/collections/bfcm-all` | |
| SHOP ALL | `/collections/shop-all-26` | |
| MEN | Men's mega-menu. Does not navigate. | |
| WOMEN | Women's mega-menu. Does not navigate. | |
| Search | Search overlay, then `/search` if the overlay is a page | |
| View Cart | Empty cart drawer on the same page | |
| Skip to Content | In-page skip link. Keyboard only. | |
| Open main menu (phone, `aria-label`) | `#top-navigation-drawer-mobile` | |

There is no Log in, Account, or Sign in control in the header.

## MEN menu

Hover or click on MEN opens the flyout. Escape closes it.

| Item | Opens |
|---|---|
| MENS HOLIDAY SALE | `/collections/bfcm-mens` |
| NEW ARRIVALS | `/collections/mens-new-arrivals` |
| BESTSELLERS | `/collections/mens-bestsellers` |
| LEATHER ALTERNATIVES | `/collections/mens-terralux-cl` |
| GIFT CARD | `/products/digital-gift-cards` |
| MEN'S SHOES / Shop All | `/collections/mens` |
| All-Weather | `/collections/mens-mizzles` |
| Sneakers | `/collections/mens-sneakers` |
| Slip Ons | `/collections/mens-loungers` |
| Sandals | `/collections/mens-sandals` |
| Active | `/collections/mens-active-shoes` |
| Final Few | `/collections/mens-final-few` |
| Tree Runner NZ | `/products/mens-tree-runner-nz-medium-grey` |
| Runner NZ | `/products/mens-runner-nz-slip-on-mushroom` |
| Cruiser | `/products/mens-cruiser-medium-grey` |
| Socks | `/collections/mens-socks` |

## WOMEN menu

| Item | Opens |
|---|---|
| WOMEN'S HOLIDAY SALE | `/collections/bfcm-womens` |
| NEW ARRIVALS | `/collections/womens-new-arrivals` |
| BESTSELLERS | `/collections/womens-bestsellers` |
| LEATHER ALTERNATIVES | `/collections/womens-terralux-cl` |
| GIFT CARD | `/products/digital-gift-cards` |
| WOMEN'S SHOES / Shop All | `/collections/womens` |
| All-Weather | `/collections/womens-mizzles` |
| Sneakers | `/collections/womens-sneakers` |
| Flats | `/collections/womens-flats` |
| Slip Ons | `/collections/womens-loungers` |
| Sandals | `/collections/womens-sandals` |
| Active | `/collections/womens-active-shoes` |
| Final Few | `/collections/womens-final-few` |
| Tree Breezer | `/products/womens-tree-breezers` |
| Tree Runner NZ | `/products/womens-tree-runner-nz-medium-grey` |
| Canvas Cruiser | `/products/womens-cruiser-canvas-port` |
| Socks | `/collections/womens-socks` |
| Women's Apparel | `/collections/womens-apparel` |

## Search

The header Search control navigates to `/search`. It is not an overlay. The field placeholder is "What are you looking for?". The field was left empty. Search was not submitted. The page lists suggested products (Tree Breezer, Tree Runner NZ, Canvas Cruiser) and a QUICK ADD button on each. Those product links go to `/products/...`.

## Cart drawer

View Cart opens a drawer on the same page. On this visit it was empty.

| Control | Opens | Stop? |
|---|---|---|
| Close cart | Closes the drawer | |
| SHOP WOMENS | Women's collection | |
| SHOP MENS | Men's collection | |
| SHOP SOCKS | Socks collection | |
| SHOP WOMEN'S SALE | Women's sale collection | |
| SHOP MEN'S SALE | Men's sale collection | |
| Checkout | Not present while the cart is empty. Not followed. | yes |

## Home page

https://www.allbirds.com/

| Control | Opens |
|---|---|
| SHOP MEN (hero) | `/collections/bfcm-mens` |
| SHOP WOMEN (hero) | `/collections/bfcm-womens` |
| SHOP MEN / SHOP WOMEN under NEW ARRIVALS | `/collections/mens-new-arrivals`, `/collections/womens-new-arrivals` |
| SHOP MEN / SHOP WOMEN under the category tiles | `/collections/mens`, `/collections/womens` |
| SHOP MEN / SHOP WOMEN under BEST SELLERS | `/collections/mens-bestsellers`, `/collections/womens-bestsellers` |
| BEST SELLERS tab | Switches the product rail on `/`. Does not navigate. |
| Previous Product / Next Product | Moves the product rail |
| Product card | `/products/<handle>`, for example `/products/womens-tree-runner-nz-medium-grey` |
| QUICK ADD | Size panel on `/` (`ab-qa__panel`): colour, women's sizes, SELECT A SIZE, View full details. Not submitted. No size was chosen. |
| Terralux SHOP MEN / SHOP WOMEN | `/collections/mens-terralux-cl`, `/collections/womens-terralux-cl` |
| All-Weather SHOP MEN / SHOP WOMEN | `/collections/mens-mizzles`, `/collections/womens-mizzles` |

## Phone drawer

Open main menu opens `#top-navigation-drawer-mobile`. Close navigation menu closes it.

| Item | Opens |
|---|---|
| HOLIDAY SALE | `/collections/bfcm-all` |
| SHOP ALL | `/collections/shop-all-26` |
| MEN (`aria-label` Select Men Menu) | Nested list, same destinations as the desktop MEN menu |
| WOMEN (`aria-label` Select Women Menu) | Nested list, same destinations as the desktop WOMEN menu |
| Back (`aria-label` Back to main menu) | Returns to HOLIDAY SALE, SHOP ALL, MEN, WOMEN |
| Search | `/search` |
| View Cart | Cart drawer |

## Footer

Help, Shop, and Company are accordions (`+`). SIGN UP opens an email field labelled "Email Address" (`contact[email]`). The field was left empty. SIGN UP was not submitted.

| Item | Opens | Stop? |
|---|---|---|
| SIGN UP | Email field on the same page | not submitted |
| help@allbirds.com | `mailto:help@allbirds.com` | not sent |
| FAQ/Contact Us | `/pages/help` | |
| Returns/Exchanges | `/pages/returns-exchanges`, a returns login card | yes, identity wall |
| Men's Shoes | `/collections/mens` | |
| Women's Shoes | `/collections/womens` | |
| Men's Apparel | `/collections/mens-apparel` | |
| Women's Apparel | `/collections/womens-apparel` | |
| Our Story | `/pages/our-story` | |
| Our Materials | `/pages/materials` | |
| Materials & Making | `/pages/materials-making` | |
| Shoe Care | `/pages/shoe-care` | |
| Press | `/blogs/news` | |
| Community Offers | `/pages/community-offers` | |
| Our Blog | `/blogs/the-perch` | |
| Patents | `/pages/patents` | |
| Responsible Disclosure Program | Shopify CDN PDF | file, not photographed |
| California Transparency Act | Shopify CDN PDF | file, not photographed |
| Instagram, Pinterest, Facebook, X, TikTok, YouTube | Off-site social profiles | not entered |
| Refund policy, Privacy policy, Terms of service, Shipping policy | In-page policy panels (`role=button`, no href) | |
| Do Not Sell My Personal Information | Consent panel. Not submitted. | |

## Login and returns walls

`/account/login` is not linked from the homepage. It was opened by URL, then stopped. The redirect lands on `accounts.allbirds.com`. The query string carries signing parameters and is not copied here.

| URL | What it shows | Stop? |
|---|---|---|
| `/account/login` | Title "Sign in - Allbirds". Copy: "Sign in or create an account". Continue with shop, then an empty Email field, a news-and-offers checkbox, and a continue arrow. | yes |
| `/pages/returns-exchanges` | A "Returns & Exchanges" card: empty Email or Zip code, empty Order # or Tracking #, Search, Sign in with Google, Sign in with email. | yes |

Continue with shop was not pressed. Sign in with Google was not pressed. Sign in with email was not pressed. Search was not pressed. No email, zip, order number, or password was typed. Checkout was not opened.
