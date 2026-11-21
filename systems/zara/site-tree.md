# Zara site tree

Mapped 2026-11-21 from the public shop at https://www.zara.com/, then the United States English storefront at https://www.zara.com/us/. Desktop viewport measured 1440 by 900 CSS pixels at devicePixelRatio 2. Phone shots used a 390 by 844 CSS viewport at devicePixelRatio 2, with a desktop user agent, so the phone chrome is the narrow layout, not a device-class page. One light theme (`color-scheme: normal`). No dark-theme control.

The homepage first paints a location page (Singapore was preselected). United States and English were chosen, Remember selection was cleared, and Continue opened the US shop. That is a market choice, not an account. A cookie dialog was closed. No newsletter, login, filter, or search form was submitted. No email, password, code, phone, or address was typed. Identity providers were not clicked. Checkout was not entered. Nothing was added to the bag.

Zara Home is a separate package. The ZARA HOME row in this menu is recorded as a link only. It was not captured here.

## Shell (desktop, 1440)

The header is `display: contents`. Utility links sit on the right. The wordmark is an inline SVG.

| Control | Opens |
|---|---|
| Skip to main content | in-page anchor `#main` |
| Open Menu (`button`, hamburger) | menu drawer on the same page (role dialog). Close menu returns to the same page |
| Logo ("Go to homepage") | page https://www.zara.com/us/ |
| Search (`a.layout-desktop-search-assist`) | page https://www.zara.com/us/en/search/home |
| Bag ("Cart empty") | page https://www.zara.com/us/en/shop/cart |
| LOG IN | page https://www.zara.com/us/en/logon, which redirects to the account host. Login wall. Branch stopped |
| Help | page https://www.zara.com/us/en/help-center |

## Menu drawer (same page)

Open Menu opens a full-height drawer. The left column is category tabs. The panel to the right lists that category's links. ZARA HOME, BEAUTY, MASSIMO DUTTI, and ZARA SRPLS are sibling tabs, not this package's pages.

| Tab | Link the tab opens | Panel (same drawer) |
|---|---|---|
| WOMAN | https://www.zara.com/us/en/woman-mkt1000.html | NEW ARRIVALS (THE NEW, SKI COLLECTION, BACK IN STOCK), FEATURED EDITS (PARTYWEAR, 100% WOOL \| CASHMERE), SELECTED FOR YOU, COLLECTION (BEST SELLERS, JACKETS \| TRENCHES, COATS, PUFFERS \| TECHNICAL, BLAZERS, KNITWEAR, DRESSES, PANTS, JEANS, SKIRTS, and further rows below the fold) |
| MAN | https://www.zara.com/us/en/man-l534.html | THE NEW, SKI COLLECTION, PARTY, ZARA ORIGINS, ZARA ATHLETICZ, COLLECTION (SHOP ALL, JACKETS, LEATHER, PUFFERS, COATS \| TRENCHES, and further rows) |
| KIDS | https://www.zara.com/us/en/kids-mkt1.html | GIRL 6–14, BOY 6–14, TODDLER GIRL, TODDLER BOY, BABY 0–18 MONTHS |
| ZARA HOME | https://www.zara.com/us/en/home-mkt2085.html | home-store links. Not captured in this package |
| BEAUTY | https://www.zara.com/us/en/woman-beauty-mkt1414.html | WOMAN (PERFUMES, GIFT EDITION, MAKEUP, ZARA HAIR), MAN, KIDS, TRAVEL MODE, DOWNLOAD APP, SUSTAINABILITY, + INFO |
| MASSIMO DUTTI | https://www.zara.com/us/en/massimo-dutti-mkt5753.html | WOMAN, THE NEW, THE SELECTION. Not this package |
| ZARA SRPLS | https://www.zara.com/us/en/srpls-mkt1875.html | not opened past the tab label |
| DISCOVER | button, no href | CAMPAIGN, COLLECTION, LOOKBOOK, TRI-CHIC, RE{FORM}ZARA, THE FILM, INSTALLATION |

Woman collection links that were read from the open drawer:

| Link | Page |
|---|---|
| THE NEW | https://www.zara.com/us/en/woman-new-in-l1180.html |
| SKI COLLECTION | https://www.zara.com/us/en/woman-ski-l6305.html |
| PARTYWEAR | https://www.zara.com/us/en/woman-party-l4824.html |
| BEST SELLERS | https://www.zara.com/us/en/woman-best-sellers-l5912.html |
| JACKETS \| TRENCHES | https://www.zara.com/us/en/woman-jackets-l1114.html |
| COATS | https://www.zara.com/us/en/woman-outerwear-l1184.html |
| PUFFERS \| TECHNICAL | https://www.zara.com/us/en/woman-outerwear-padded-l1195.html |
| BLAZERS | https://www.zara.com/us/en/woman-blazers-l1055.html |
| KNITWEAR | https://www.zara.com/us/en/woman-knitwear-l1152.html |
| DRESSES | https://www.zara.com/us/en/woman-dresses-l1066.html |
| PANTS | https://www.zara.com/us/en/woman-trousers-l1335.html |
| JEANS | https://www.zara.com/us/en/woman-jeans-l1119.html |
| SKIRTS | https://www.zara.com/us/en/woman-skirts-l1299.html |

## Home https://www.zara.com/us/

A full-viewport campaign carousel. Arrow controls move the slide on the same page. One slide carries an Activate audio button. A later slide is a "THE NEW / SCROLL DOWN" prompt. The last slide of a section carries the footer.

| Control | Opens |
|---|---|
| Carousel slide | campaign or category page for that slide (not followed on every slide) |
| Previous / next arrows | next or previous slide, same page |
| Activate audio | in-page audio, same page |
| THE NEW | category page for the current campaign |
| Sign up for our newsletter | page https://www.zara.com/us/en/z-newsletter-nl1400.html. Not submitted |
| TikTok, Instagram, Facebook, Pinterest, YouTube, Spotify | external sites. Not followed |
| Cookies settings | cookie preference dialog on the same page. Closed, not submitted |
| Use of AI | PDF on static.zara.net |
| Cookie and Ad Preferences | cookie preference dialog. Not submitted |
| Privacy and Cookies Policy | PDF on static.zara.net |
| Terms of use | PDF on static.zara.net |

## Category page

https://www.zara.com/us/en/woman-dresses-l1066.html is the dresses grid. The left rail is a numbered subnav. FILTERS opens a right drawer. VIEW 1 2 3 changes the grid density on the same page. A product tile opens the product page. The plus control on a tile is "Open size selector" (not used to add).

| Control | Opens |
|---|---|
| VIEW ALL | https://www.zara.com/us/en/woman-dresses-l1066.html |
| GOING OUT | https://www.zara.com/us/en/woman-dresses-party-l1581.html |
| MIDI \| MAXI | https://www.zara.com/us/en/woman-dresses-midi-l1081.html |
| MINI | https://www.zara.com/us/en/woman-dresses-mini-l1083.html |
| JUMPSUITS | https://www.zara.com/us/en/woman-jumpsuits-l1150.html |
| SATIN EFFECT | https://www.zara.com/us/en/woman-dresses-camisole-l2184.html |
| VELVET | https://www.zara.com/us/en/woman-dresses-velvet-l2183.html |
| SECONDHAND | in-page, no href on the row that was read |
| FILTERS | right drawer (role dialog): sort, color, size, price, collection. VIEW RESULTS would apply. Not submitted. Close returns to the grid |
| VIEW 1 / 2 / 3 | grid density on the same page |
| Product image or name | product page `…/<name>-p<id>.html` |
| Open size selector | size list on the tile. Not used |

## Product page

https://www.zara.com/us/en/animal-print-tulle-dress-p05039846.html (ANIMAL PRINT TULLE DRESS, $ 45.90).

| Control | Opens |
|---|---|
| Colour swatch | in-page colour, same product family |
| ADD | size step, then bag. Not clicked. Checkout not entered |
| Apple Pay | payment sheet. Not clicked |
| Wishlist bookmark | favorites. Not clicked. Favorites itself redirects toward logon |
| Product measurements, Composition and care, Check in-store availability, Shipping, exchanges and returns | in-page accordions |
| Complete your look tiles | other product pages |
| CHAT | chat widget. Not opened |

## Search, bag, help, error

| Page | What it shows | Stopped at |
|---|---|---|
| https://www.zara.com/us/en/search/home | empty field "What are you looking for?", section tabs WOMAN MAN KIDS, a recommendation row | no query typed or submitted |
| https://www.zara.com/us/en/shop/cart | "YOUR BAG IS EMPTY". Right rail adds FAVORITES and PRE-OWNED | nothing added. Checkout not present |
| FAVORITES | https://www.zara.com/us/en/user/wishlist | not opened. Account-shaped URL |
| PRE-OWNED bag | https://www.zara.com/us/en/shop/cart-preowned | not opened |
| https://www.zara.com/us/en/help-center | search field "How can we help you?", FAQ tiles, topic columns (MY ZARA ACCOUNT, ITEMS AND SIZES, and others) | search not submitted. Account topics not opened |
| https://www.zara.com/us/en/this-page-does-not-exist-capture-9f3a | "PAGE NOT FOUND", "This page is no longer available.", GO TO HOMEPAGE | styled error page |

Product-page footer columns, read from the DOM, not all followed: HELP, MY ZARA ACCOUNT, ITEMS AND SIZES, GIFT OPTIONS, DELIVERIES, PAYMENTS AND INVOICES, MY PURCHASES, EXCHANGES RETURNS AND REFUND, ZARA PRE-OWNED, ZARA EXPERIENCES, NEWSLETTER, social links, ABOUT US, SUSTAINABILITY, OFFICES, STORES, WORK WITH US, and legal PDFs (privacy, use of AI, terms, gift card conditions).

## Phone (390)

The utility row collapses. OPEN APP is a banner (not followed). The header keeps Open Menu, LOG IN, a search icon, and the bag count. The dresses page keeps FILTERS and the numbered subnav above a single-column grid. The menu button is the same drawer as desktop, at this width.

## Login wall (recorded, not entered)

| Control or URL | What loaded |
|---|---|
| LOG IN | https://www.zara.com/us/en/logon redirects to https://account.zara.com/login/two-step. The query string is omitted from this file. Heading "Log in or register". Empty email field, CONTINUE, then Continue with QR, Continue with Google, Continue with Apple. Branch stopped. Nothing typed. Identity providers not clicked. CONTINUE not clicked |
| Help on the login page | help link on the account host. Not followed |

No theme switch exists on the public storefront.
