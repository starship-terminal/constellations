# Aesop site tree

Mapped 2026-11-21 from the US storefront at https://www.aesop.com/ in headed Chrome (Playwright, `channel: chrome`), desktop 1440×900. Headless Chromium is stopped by Cloudflare ("Just a moment...") on every document, so the map and the captures use headed Chrome. www.aesop.com serves `Sites-aesop-us-Site`. One light theme (`color-scheme: normal`). No dark-theme control.

A region dialog ("It Seems Like You are in …") can cover the page. It was hidden, not submitted. No country, newsletter, login, or enquiry form was submitted. No password, code, or profile field was typed.

## Shell (desktop)

| Control | Opens |
|---|---|
| Skip to content | in-page anchor `#site-content` |
| Skip to footer navigation | in-page anchor `#footer-nav` |
| Logo ("Aesop - Go to the homepage") | page https://www.aesop.com/ |
| Stores | page https://www.aesop.com/stores |
| Customer service (`button.l-header__top-nav-link`) | page https://www.aesop.com/customer-service/contact-us.html |
| Email sign up (`button.c-signup-link`) | dialog on the same page (newsletter). Not submitted. |
| Account (`button.c-user__link`) | dialog "Sign in" on the same page (email, password, stay signed in, forgotten password). Login wall. Branch stopped. Not typed, not submitted. |
| My cart (`button.c-minicart-icon__link`) | drawer (405px, role dialog) "My cart". Empty bag. "Go to cart" opens page https://www.aesop.com/cart. "Continue browsing" closes the drawer. |
| Search (`button.l-header__search-button`, visible copy in the nav row) | search disclosure on the same page (`input[name=q]`, form action `/search`). Not submitted. |
| Promo carousel previous / next / slide bullets | in-page carousel, same page |
| Hero video pause / unmute / play | in-page video controls, same page |
| Change region or country (footer) | region dialog. Not submitted. |

Primary nav. Each category is an `a.c-navigation__link.m-level-1` plus a `button.c-navigation__button.m-level-1` of the same label. Hovering the link or the button opens a flyout (`.c-navigation__flyout-element`) on the same page. The link itself opens the category page. Shop all has no flyout.

| Nav control | Page the link opens | Flyout (same page) |
|---|---|---|
| Gifts | https://www.aesop.com/gifts.html | Discover Gifts, category index, Shop all Gifts, Seasonal Gift Kits, Signature Formulations, Fragrant gifts, Gifts for home, Gifts for travel, Kits & Sets, The Aesop Valise, Gift Finder |
| Shop all | https://www.aesop.com/shop-all/ | none |
| New & Notable | https://www.aesop.com/new-notable.html | New additions, notable formulations, product links, Uniquely Aesop |
| Skin Care | https://www.aesop.com/skin-care.html | Category (Cleansers, Toners, Exfoliants & Masks, Concentrates & Serums, Moisturisers, Eye & Lip Care, Shaving, Sun Care), Skin concern, Skin type, Ingredients, Seasonal Skin Care, Find your skin type |
| Hand & Body | https://www.aesop.com/hand-and-body.html | Hand Washes & Balms, Bar Soaps, Body Cleansers & Scrubs, Body Balms & Oils, Oral Care & Deodorants, kits, Hand & Body Finder |
| Fragrance | https://www.aesop.com/fragrance.html | Floral, Fresh, Woody, Ambery, Sets & Discovery, notable formulations, Fragrance Finder |
| Home | https://www.aesop.com/home-fragrance.html | Room Sprays, Incense, Candles, Oil Burner Blends, Design Objects, Bathroom Deodorisers & Pets |
| Hair | https://www.aesop.com/hair.html | Shampoo & Conditioner, Treatments, Grooming, daily essentials |
| Travel | https://www.aesop.com/travel.html | In-flight essentials, For the commute, Travel Kits, notable formulations |
| Library | https://www.aesop.com/library.html | Literature and culture, Products and guides, Architecture and design, Sound and vision, city guides, About (Our story, Design approach, Product philosophy) |
| Experience | https://www.aesop.com/experience.html | Corporate gifts, Online services, Amenity partners |

## Phone (390)

The utility row collapses. A control labelled Main menu (`button.c-hamburger__button`) opens an in-page drawer (`.c-hamburger__content`), not a new URL. The drawer lists Sign in or create an account (login wall, branch stopped), the same category buttons, Customer service, Stores, and My cart. Each category button expands an in-drawer list. Close returns to the same page. Search is an icon button in the header. Stores and My cart stay in the header.

## Home https://www.aesop.com/

| Control | Opens |
|---|---|
| Promo "The Aesop Gift Gathering" | page https://www.aesop.com/the-aesop-gift-gathering/ |
| Exclusions apply | page https://www.aesop.com/customer-service/the-aesop-gift-gathering-2026-terms-and-conditions.html |
| Browse the range | page https://www.aesop.com/the-aesop-gift-gathering/ |
| Discover | page https://www.aesop.com/a-time-to-embrace.html |
| Explore Gift Kits | page https://www.aesop.com/gifts-for-a-season-shared.html |
| Product tiles (Valise, Trusted Companions, and the other seasonal kits) | product page `…/<SKU>.html` |
| Consult The Gift Finder | page https://www.aesop.com/gift-finder/ |
| Kit tiles (Bathroom Dignities, Geranium Leaf Trio, and others) | product or kit page |
| Find a nearby store | page https://www.aesop.com/stores |
| Read more (library features) | library article pages under `/library/` |
| Follow on Instagram, LinkedIn, Pinterest, Facebook | external social sites |

## Catalogue and product

| Page | Extra controls | Opens |
|---|---|---|
| /shop-all/ | All filters (`button.c-refinements-toggler`) | filter rail on the same page (sort, category, concern). Not submitted as a search. |
| /shop-all/ | product tile | product page |
| /skin-care.html and the other category landings | category tiles and article tiles | category index or library article |
| product page (`/<path>/<SKU>.html`) | size or variant boxes | in-page selection, same page |
| product page | accordion titles (phone widths) | in-page disclosure |
| product page | Add to cart | local cart drawer. Not checked out. |

## Stores, cart, help

| Control or page | Opens |
|---|---|
| https://www.aesop.com/stores | store locator. Search field, Filters, Geolocate me, Map/Satellite. A no-match query opens a no-result dialog. Geolocate was not granted. No address typed into the package. |
| https://www.aesop.com/stores/all | all-locations list |
| https://www.aesop.com/cart | empty cart page. Checkout not entered. |
| https://www.aesop.com/customer-service/contact-us.html | help tiles: Start conversation, Submit an enquiry (page `/customer-service/customer-service-contact-us.html`, form not submitted), Find a store, Explore help centre |
| https://www.aesop.com/customer-service/orders-and-delivery.html | FAQs, shipping, returns |
| https://www.aesop.com/customer-service/track-your-order.html | order track form. Not submitted. |
| https://www.aesop.com/gift-finder/ | gift finder. Not submitted. |
| https://www.aesop.com/fragrance-fables-finder/ | fragrance finder |
| https://www.aesop.com/skin-finder/ | skin finder |
| https://www.aesop.com/body-care-finder/ | body-care finder |

## Footer (every page)

Orders and support: Contact us, FAQs, Shipping, Returns, Track your order, Replenishment subscriptions, Product recalls, Terms of use, User Content Permission Terms, SMS Terms & Conditions, E-gift Cards Terms of Use.

About: Our story, Foundation, Careers, Corporate Gifts, Privacy policy, Accessibility Statement, Your Privacy Choices, Notice At Collection, Consumer Health Data Notice, Sustainability.

Online Preferences is `javascript:;` (a preferences dialog). Not submitted. Notice of Financial Incentives and Marketing Disclosure leave the site for Salesforce Marketing Cloud pages. AdChoices leaves for youradchoices.com. Site Map opens https://www.aesop.com/customer-service/customer-service-sitemap.html.

## Login walls (recorded, not entered)

| URL or control | What loaded |
|---|---|
| Account button | Sign-in dialog on the current page. Email and password fields. Branch stopped. |
| Main menu, Sign in or create an account | same sign-in wall. Branch stopped. |
| https://www.aesop.com/account/login | HTTP 404, title "Page Not Found". Styled error page, not a form. |
| https://www.aesop.com/on/demandware.store/Sites-aesop-us-Site/en_US/Login-Show | HTTP 200, heading "My Account Sign In", form `#dwfrm_login` (email, password, remember me, Login) and an order-track form. Login wall. Branch stopped. Nothing typed. |

No theme switch exists on the public storefront.
