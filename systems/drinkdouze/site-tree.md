# Douze public site tree

Captured 2026-11-21, signed out, from https://drinkdouze.com/. An en-US browser is redirected from `/` to `/en`. A fr-FR browser stays on `/` (French default). English `/en` is the mapped surface. French sitemap URLs exist and were not walked page by page. One French home shot is [screenshots/home-fr-light-default.png](screenshots/home-fr-light-default.png).

HTTP status is 200 unless a row says otherwise. Login, signup, account, and checkout branches stop at the wall. No email, password, newsletter, contact, stockist, referral, or checkout form was filled. No SSO button was clicked. No app was downloaded.

## Header at 1440

The desktop header is `store-header`. Announcement copy reads "FREE DELIVERY IN MAINLAND FRANCE FOR ORDERS OVER €50".

| Control | Opens |
|---|---|
| Skip to content | `/en#main`, same page |
| SHOP `a[aria-controls=desktop-menu-1]` | `/en/collections/all`. The id `desktop-menu-1` is not in the DOM. Hover does not open a panel. Click navigates. |
| OUR STORY | `/en/pages/our-story` |
| WHY DOUZE? | `/en/pages/why-douze` |
| RECIPES | `https://drinkdouze.com/blogs/recipes` (unprefixed). English index is also `/en/blogs/recipes`. |
| Logo "Back to Homepage" | `/en` |
| FIND US | `/en/pages/store-locator` |
| SUBSCRIBE | `/en/pages/subscription` |
| Login icon `a[aria-label=Login]` | `/en/account/login` (login wall, stop) |
| Cart `a[aria-controls=mini-cart]` href `/en/cart` | In-page cart drawer `#mini-cart`. Empty cart copy: "CART Your cart is empty START SHOPPING". URL stays `/en`. START SHOPPING goes to `/en/collections/all`. Shot: [screenshots/home-light-cart.png](screenshots/home-light-cart.png). |
| Newsletter `button[aria-controls=newsletter-popup]` | Not openable. The button is `hidden-phone` with width 0. `#newsletter-popup` is absent from the DOM. |
| Search drawer `#search-drawer` | Present (`predictive-search-drawer`, `reverse-breakpoint` min-width 1200px, form GET `/en/search`, placeholder "What are you looking for?"). No visible `aria-controls` trigger at 1440 or at 1000. Setting the `open` attribute shows the drawer. That shot is evidence of the drawer chrome, not of a visible search button. |

## Header at 390

| Control | Opens |
|---|---|
| Navigation `button[aria-controls=mobile-menu-drawer]` | Mobile menu drawer, `open=true`. Links: SHOP `/en/collections/all`, OUR STORY, WHY DOUZE?, RECIPES `/en/blogs/recipes`, FIND US `/en/pages/store-locator`, SUBSCRIBE `/en/pages/subscription`, ACCOUNT `/en/account/login` (login wall, stop). Shot: [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). |
| Logo | `/en` |
| Login | `/en/account/login` (stop) |
| Cart | Cart drawer, same as desktop |

## Footer

Present on public pages. The footer email field and the `>` submit are a newsletter form. Not filled.

| Control | Opens |
|---|---|
| SHOP | `/en/collections/all` |
| OUR STORY | `/en/pages/our-story` |
| WHY DOUZE? | `/en/pages/why-douze` |
| MY ACCOUNT | `/en/account/login` (stop) |
| SHIPPING | `/en/pages/page-faq`, which redirects to `/en/pages/faqs` |
| FAQS | `/en/pages/page-faq`, same redirect |
| SPONSORSHIP | `/en/pages/parrainage` |
| PRIVACY POLICY | `/en/pages/privacy-policy` |
| TERMS & CONDITIONS | `/en/pages/terms-and-conditions` |
| Footer logo | `/en` |
| ENGLISH `button[aria-controls=footer-locale-selector]` | Popover text "Language Français English". Buttons `locale_code=fr` and `locale_code=en`. Not submitted. The 1440 home shot after the click does not clearly show the popover (hero still fills the frame). The control and its buttons were read from the DOM. French home was captured in a separate fr-FR context. |
| Footer search field `input[name=q]` | Inside `#search-drawer`, action `/en/search`. Not submitted. |
| Instagram `@drinkdouze` | External. Not crawled. |

Press marks in the footer (Vogue, Vanity Fair, and similar) are external. Not crawled.

## Home `/en`

Shot: [screenshots/home-light-default.png](screenshots/home-light-default.png), full page [screenshots/home-light-full.png](screenshots/home-light-full.png). Mobile: [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

| Control | Opens |
|---|---|
| STORE (hero product) | `/en/products/orange-sanguine-piment-3` |
| Our spritzes | `/en/collections/all` |
| Product cards in the spritz rail | PDP for that product (blood orange can, trio, and the hero product were linked) |
| LEARN MORE (ingredients) | `/en/pages/why-douze` |
| SEE ALL (shop) | `/en/collections/all` |
| Next (carousel) | In-page. No URL change. |
| OUR COMMITMENTS | `/en` (same page anchor or home; href is `/en`) |
| Témoignage précédent / suivant | In-page testimonial carousel. No URL change. |
| FIND US (mid page) | href `/en` on the home capture (not the store-locator URL used by the header) |
| LEARN MORE (subscribe) | `/en/pages/subscription` |
| Sirocco card | `/en/blogs/recipes/sirocco` |
| Toddy card | `/en/blogs/recipes/cold-toddy` |
| SEE ALL (recipes) | `/en/blogs/recipes` |
| previous post / next post | In-page recipe rail. No URL change. |

## Shop

| Page | How it opens | Notes |
|---|---|---|
| `/en/collections/all` | Header SHOP, footer SHOP, hero "Our spritzes" | Tabs are buttons, URL unchanged: ALL (expanded, dusk pill), Cans, Bottles, Gift sets. Each `aria-controls` a featured-collections block. Cans click left the URL at `/en/collections/all` and set Cans `aria-expanded=true`. Shots: [screenshots/shop-light-default.png](screenshots/shop-light-default.png), [screenshots/shop-light-cans.png](screenshots/shop-light-cans.png), [screenshots/shop-light-full.png](screenshots/shop-light-full.png), [screenshots/mobile-shop-light-default.png](screenshots/mobile-shop-light-default.png). |
| `/en/collections` | Direct | Collection index. [screenshots/collections-index-light-default.png](screenshots/collections-index-light-default.png). |
| `/en/collections/the-bubbly` | Collection index / product type | Bottles. [screenshots/bubbly-light-default.png](screenshots/bubbly-light-default.png). |
| `/en/collections/the-tonic` | Same | Cans. [screenshots/tonic-light-default.png](screenshots/tonic-light-default.png). |
| `/en/collections/coffrets` | Same | Gift sets. [screenshots/coffrets-light-default.png](screenshots/coffrets-light-default.png). |
| `/en/collections/accessoires` | Same | Accessories. [screenshots/accessoires-light-default.png](screenshots/accessoires-light-default.png). |

Product cards on those collections open the matching PDP. Not every PDP was photographed. The photographed PDP is the blood orange can.

## Product page `/en/products/blood-orange-chilli`

Shots: [screenshots/pdp-light-default.png](screenshots/pdp-light-default.png), pack [screenshots/pdp-light-pack.png](screenshots/pdp-light-pack.png), subscription option [screenshots/pdp-light-subscribe.png](screenshots/pdp-light-subscribe.png), full [screenshots/pdp-light-full.png](screenshots/pdp-light-full.png), mobile [screenshots/mobile-pdp-light-default.png](screenshots/mobile-pdp-light-default.png).

| Control | Opens |
|---|---|
| Thumbnail buttons | In-page gallery. No URL change. |
| Pack radios `option1` | 6 cans (checked), 12 cans, 24 cans. In-page. Not submitted. |
| ONE-TIME PURCHASE | In-page purchase option. Active on the default shot. |
| SUBSCRIPTION −10% | In-page purchase option. Shot with that option selected. Not submitted. |
| ADD TO CART | Posts to `/cart/add`. Not clicked. |
| Complementary ADD TO CART | Same cart add. Not clicked. |
| BUY WITH 1-CLICK | Shop Pay-style checkout. Not clicked. Stop if it leaves the storefront. |
| PDP accordions | "DO THESE PRODUCTS CONTAIN CBD?", taste, caffeine, when to drink, vegan, mix with alcohol. In-page. Not all opened. |
| ENGLISH locale | Same footer popover as home. Not submitted. |

Other English product URLs from the sitemap, not each photographed:

- `/en/products/apricot-zaatar-25cl-can`
- `/en/products/poire-anis`
- `/en/products/duo-douze`
- `/en/products/plein-soleil`
- `/en/products/kit-dete-plein-soleil`
- `/en/products/kit-complet-plein-soleil`
- `/en/products/apricot-zaatar-75cl-bottle`
- `/en/products/pear-anis-75cl-bottle`
- `/en/products/duo-bubbly`
- `/en/products/attrape-bulles`
- `/en/products/trio-douze`
- `/en/products/carte-cadeau` (shot [screenshots/gift-light-default.png](screenshots/gift-light-default.png))
- `/en/products/coffret-dry-january`
- `/en/products/blood-orange-chilli-75cl`
- `/en/products/orange-sanguine-piment-3`

## Recipes and news

| Page | How it opens | Shot |
|---|---|---|
| `/en/blogs/recipes` | Header RECIPES (unprefixed twin), footer is not a recipes link, home SEE ALL | [screenshots/recipes-light-default.png](screenshots/recipes-light-default.png), [screenshots/mobile-recipes-light-default.png](screenshots/mobile-recipes-light-default.png) |
| `/en/blogs/recipes/sirocco` | Recipe card | [screenshots/recipe-light-default.png](screenshots/recipe-light-default.png) |
| `/en/blogs/general` | Not in the desktop header. Sitemap. | [screenshots/general-light-default.png](screenshots/general-light-default.png) |
| `/en/blogs/general/nice-ses-alentours` | Article card on the general blog. Not photographed separately. | |

Other recipe articles, same template as Sirocco, not each photographed: abricotete, le-sud, cold-toddy, murmure, douze-calling, quartier-libre, coco-douze, le-pierre, lune-de-miel, douzy-mary, garidouzy, rouge-carmin, solstice. All under `/en/blogs/recipes/`.

## Editorial and utility pages

| Page | How it opens | In-page controls | Shot |
|---|---|---|---|
| `/en/pages/our-story` | Header OUR STORY | None that navigate away beyond the shared chrome | [screenshots/story-light-default.png](screenshots/story-light-default.png) |
| `/en/pages/why-douze` | Header WHY DOUZE? | Ingredient filters, URL unchanged: ALL, APRICOT & ZAATAR, BLOOD ORANGE & CHILI, PEAR & ANISE, APRICOT, STAR ANISE, FENNEL, LEMON JUICE, LEMON BALM. Submit buttons. Not a form we filled. | [screenshots/why-light-default.png](screenshots/why-light-default.png) |
| `/en/pages/faqs` | Footer FAQS via `/en/pages/page-faq` redirect | Accordion `button.collapsible-toggle`. First item "HOW DO I CREATE MY CUSTOMER ACCOUNT?" opened (`aria-expanded=true`). Other items stayed closed. | [screenshots/faqs-light-default.png](screenshots/faqs-light-default.png), [screenshots/faqs-light-open.png](screenshots/faqs-light-open.png), [screenshots/mobile-faqs-light-default.png](screenshots/mobile-faqs-light-default.png) |
| `/en/pages/store-locator` | Header FIND US | Testimonial carousel. No obvious search field in the first inputs. | [screenshots/locator-light-default.png](screenshots/locator-light-default.png), [screenshots/mobile-locator-light-default.png](screenshots/mobile-locator-light-default.png) |
| `/en/pages/find-us` | Sitemap, not the header | Thin page. Footer chrome only. | [screenshots/findus-light-default.png](screenshots/findus-light-default.png) |
| `/en/pages/subscription` | Header SUBSCRIBE | Product picker, pack sizes, "+ ADD A PRODUCT", SUBSCRIBE. Not submitted. | [screenshots/subscription-light-default.png](screenshots/subscription-light-default.png), [screenshots/mobile-subscription-light-default.png](screenshots/mobile-subscription-light-default.png) |
| `/en/pages/contact` | Sitemap | Fields `contact[name]`, `contact[email]`, `contact[body]`, SUBMIT. Not filled. | [screenshots/contact-light-default.png](screenshots/contact-light-default.png) |
| `/en/pages/become-a-stockist` | Sitemap | Contact fields plus company, phone, mailing address, city, postal code, country, place type. Not filled. | [screenshots/stockist-light-default.png](screenshots/stockist-light-default.png) |
| `/en/pages/submit-a-stockist` | Sitemap | Place name and a person-in-charge form. Not filled. | [screenshots/suggest-light-default.png](screenshots/suggest-light-default.png) |
| `/en/pages/parrainage` | Footer SPONSORSHIP | Refer-a-friend radios and submit. Not filled. | [screenshots/referral-light-default.png](screenshots/referral-light-default.png) |
| `/en/pages/terms-and-conditions` | Footer | Long text. | [screenshots/terms-light-default.png](screenshots/terms-light-default.png) |
| `/en/pages/privacy-policy` | Footer | Long text. | [screenshots/privacy-light-default.png](screenshots/privacy-light-default.png) |
| `/en/pages/bumble-x-douze-the-walk-of-fame` | Sitemap | Campaign page. | [screenshots/bumble-light-default.png](screenshots/bumble-light-default.png) |
| `/en/search` | Footer search form, not submitted from the capture | Empty search. | [screenshots/search-light-default.png](screenshots/search-light-default.png), [screenshots/mobile-search-light-default.png](screenshots/mobile-search-light-default.png) |
| `/search` | Unprefixed | Title "Recherche" (French). Not used as the English capture. | |
| `/en/cart` | Cart icon href, also direct | Empty. START SHOPPING to `/en/collections/all`. No checkout control while empty. Not filled. | [screenshots/cart-light-default.png](screenshots/cart-light-default.png), [screenshots/mobile-cart-light-default.png](screenshots/mobile-cart-light-default.png) |
| `/en/pages/this-page-does-not-exist` | Probe | 404. | [screenshots/notfound-light-default.png](screenshots/notfound-light-default.png) |

## Walls (stop)

| URL | What rendered | Branch |
|---|---|---|
| `/en/account/login` | E-mail, Password, FORGOT PASSWORD?, SIGN IN, SIGN UP, MANAGE MY SUBSCRIPTION. No code was sent. | Stop. Shots: [screenshots/login-light-default.png](screenshots/login-light-default.png), [screenshots/mobile-login-light-default.png](screenshots/mobile-login-light-default.png). |
| `/en/account/register` | Create account. First name, last name, email, country calling-code select. Not filled. | Stop. [screenshots/register-light-default.png](screenshots/register-light-default.png). |
| `/en/account` | Redirects to `/en/account/login?return_url=%2Fen%2Faccount`. | Stop. |
| `/en/pages/mon-abonnement` | Signed-out shell titled "My subscription", copy starts "Welcome,". | Account wall. Stop. |
| `/en/pages/mes-commandes` | Signed-out shell titled "My orders". | Account wall. Stop. |
| `/en/pages/credit-douze` | Signed-out shell titled "Credit Twelve". | Account wall. Stop. |
| `/en/pages/moyen-de-paiement` | Signed-out shell titled "Method of payment". | Account wall. Stop. |
| `/en/pages/just-post-purchase` | Title "Post purchase". Public-looking, post-purchase. Not filled. | Stop. |
| Checkout | Empty cart has no checkout control. ADD TO CART and BUY WITH 1-CLICK were not used. | Stop. |

Forgot-password, SSO (Google, Apple, Facebook, Microsoft, GitHub, X), and "MANAGE MY SUBSCRIPTION" were not clicked.

## French tree (not walked)

Unprefixed sitemap mirrors the English one: products, `/pages/notre-histoire`, `/pages/engagements`, `/pages/page-faq`, `/pages/conditions-generales`, `/pages/politique-de-confidentialite`, `/pages/page-dabonnement`, `/pages/trouvez-nous`, `/pages/stockists`, collections `bouteilles` and `canettes`, and the same recipe slugs. Locale buttons can switch language. They were not submitted.

## Not present

No dark theme. No cookie banner (no OneTrust nodes). No visible header search button at 1440 or 1000. No desktop mega-menu panel for SHOP.
