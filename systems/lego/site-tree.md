# LEGO public site tree

Mapped on 2026-11-21 from [https://www.lego.com/en-us](https://www.lego.com/en-us) in Chromium, signed out, before the screenshot pass. The request stayed on the Official LEGO Shop US. Title: Home | Official LEGO Shop US. HTTP 200. This is a live shop, not a parked domain and not a captcha wall.

The shop paints one light theme. There is no theme switch. The footer button "United States" is the region control. It was not used to pick another country. No email, password, phone, code, or address was typed. No form was submitted. No identity provider was clicked. Add to Bag was not pressed. Checkout was not opened. The bag link was not followed.

Sign In and Join leave the shop for `identity.lego.com`. Those walls were photographed empty and the branch stopped there.

## Utility bar

Sits above the yellow header.

| Control | Opens | Stop? |
|---|---|---|
| Shop now | `/categories/all-sets` | |
| Close (banner) | Dismisses the loyalty banner on the same page | |

## Header

Yellow bar. The wordmark is "Home". Shop, Discover, and Help are buttons that open panels on the same page. Search is a field. Sign Up, Wish List, and the bag sit at the right.

| Control | Opens | Stop? |
|---|---|---|
| Home (logo) | `/en-us` | |
| Shop | Panel on `/en-us`. Does not navigate. | |
| Discover | Panel on `/en-us`. Does not navigate. | |
| Help | Panel on `/en-us`. Does not navigate. | |
| LEGO Insiders Weekend | `/en-us/categories/lego-offers-promotions/member-offer` | |
| Search | Focus opens a Popular searches list on the same page. Nothing typed. | |
| Sign Up (`data-test` account) | Insiders dialog on `/en-us` | yes, account wall from its links |
| Wish List (`data-test` wishlist) | Same Insiders dialog | yes, account wall from its links |
| My Bag, 0 items | `/cart` | not followed |

## Shop panel

Opened from the Shop button. Left column is a list. Themes is the default pane, with round theme tiles.

| Item | Opens |
|---|---|
| Themes (pane) | Theme tiles, then See all themes `/en-us/themes` |
| Age | Age listing links under `/en-us/age/` |
| Price ranges | Price listing links |
| Occasions | Occasion listing links |
| LEGO merchandise | Merchandise listings |
| Interests | `/en-us/categories/interests` and child listings |
| Bricks and pieces | Parts shop |
| SMART Play | `/en-us/smart-play/all-sets` |
| New | `/en-us/categories/new-sets-and-products` |
| Exclusives | `/en-us/categories/exclusives` |
| Bestsellers | `/en-us/categories/bestsellers` |
| Offers & sale | `/en-us/page/lego-offers-promotions` |
| Coming soon | `/en-us/categories/coming-soon` |
| Retiring soon | `/en-us/categories/last-chance-to-buy` |
| Gift cards | `/en-us/gift-cards` |
| City (theme tile) | `/en-us/themes/city` |
| See all themes | `/en-us/themes` |

Theme tiles in the default pane also include Architecture, Art, Batman, Botanicals, BrickHeadz, Disney, Editions, Harry Potter, Icons, Ideas, Marvel, NINJAGO, One Piece, Pokemon, Star Wars, and Technic. Each goes to `/en-us/themes/<slug>`.

## Discover panel

| Item | Opens |
|---|---|
| About the LEGO Group | `/en-us/aboutus` |
| Livestreams | `/live` |
| All LEGO themes | `/en-us/themes` |
| All LEGO interests | `/en-us/categories/interests` |
| Find inspiration | `/en-us/lego-set-inspiration` |
| Adults welcome | `/en-us/categories/adults-welcome` |
| For families | `/en-us/families` |
| Preschool | `/en-us/preschool` |
| LEGO Insiders | `/en-us/insiders/home` |
| About Us | `/en-us/aboutus` |
| LEGO news | `/en-us/aboutus/newsroom` |
| Sustainability | `/en-us/sustainability` |
| LEGO builder | `/en-us/builder-app` |
| LEGO play app | `/en-us/apps/play-app` |
| LEGO Insiders app | `/en-us/insiders/app` |
| LEGO catalogs | `/en-us/themes/brand-catalogue` |
| LEGO Magazine (FREE) | `/en-us/magazine` |
| LEGO Sanrio | `/en-us/themes/sanrio/about` |
| DAFT PUNK | `/en-us/categories/adults-welcome/article/daft-punk` |

## Help panel

| Item | Opens |
|---|---|
| Check order status | `/en-us/page/static/orders` |
| Find a LEGO store | `/en-us/stores` |
| Find building instructions | `/en-us/service/buildinginstructions` |
| Common questions | `/en-us/service/help-topics` |
| Contact us | `/en-us/service` |
| Replacement parts | `/en-us/service/replacementparts` |

## Account dialog

Sign Up and Wish List both open the same dialog on `/en-us`. It is a membership pitch, not a form.

| Control | Opens | Stop? |
|---|---|---|
| Become a member | `/identity/register`, then `https://identity.lego.com/en-US/register` | yes, signup wall |
| Sign In | `/identity/login`, then `https://identity.lego.com/en-US/login` | yes, login wall |
| Check Order Status | `/en-us/guest/orders` | not followed |
| Close | Closes the dialog | |

## Homepage body

| Control | Opens | Stop? |
|---|---|---|
| Become a member (hero) | `/identity/register` | yes, signup wall |
| Learn more (hero) | `/en-us/insiders-weekend-deals` | |
| Trending chips | Public listings: member offer, 4x points, all sets, Insiders Weekend, Adults Welcome, gifts, bestsellers, rewards | |
| Product cards | `/en-us/product/<slug>`, for example Tower Bridge `/en-us/product/tower-bridge-21067` | |
| Add to Bag on a card | Not pressed | |

## Search

Focusing the header field opens Popular searches (star wars, marvel, batman, harry potter, ninjago). Nothing was typed there. A public results page for `city` is `/en-us/search`. A query of `""` is the empty state: "Oops, we couldn't find anything".

## Footer

Columns: About us, Support, Attractions, More from us. The region button reads United States. The email field and Subscribe were not used. Cookie Settings and Do not sell or share were not opened.

| Item | Opens |
|---|---|
| About the LEGO Group | `/en-us/aboutus` |
| Contact us | `/en-us/service` |
| Find building instructions | `/en-us/service/buildinginstructions` |
| Find a LEGO store | `/en-us/stores` |
| Sustainability | `/en-us/sustainability` |
| Privacy policy | `/en-us/legal/legal-notice/privacy-policy` |
| LEGO Education | `http://education.lego.com/` (exit) |
| LEGO Ideas | `https://ideas.lego.com/` (exit) |
| Social (Facebook, Instagram, YouTube, TikTok) | External. Not followed. |

## Phone width (390)

The yellow header collapses to a hamburger (`aria-label` common.open), logo, Sign Up, Wish List, bag, and a full-width search. The hamburger opens a drawer: Shop, Discover, Help, LEGO Insiders Weekend, Sign In, Join LEGO Insiders. Sign In and Join are the same walls as desktop. They were not followed from the phone drawer.

## Login wall

[https://identity.lego.com/en-US/login](https://identity.lego.com/en-US/login). Title: LEGO account. Empty email or username field, Continue, Forgot your username?, and identity providers (Apple, Facebook, Google, Epic). Nothing typed. No provider clicked. Continue not pressed.

## Signup wall

[https://identity.lego.com/en-US/register](https://identity.lego.com/en-US/register). Title: Create your adult LEGO account. Country or region is prefilled by the site (Singapore on this network). Birthdate fields are empty. Identity providers are shown and not clicked. Continue not pressed. No date, email, or address typed.
