# Zara Home site tree

Mapped 2026-11-21 from the public International store at https://www.zarahome.com/, signed out, in the T3 preview browser. Desktop frames are 1440×900 CSS (devicePixelRatio 2). Phone frames are 390×844 CSS (devicePixelRatio 2). Front version `2.11.19` from `window.inditex.iFrontVersion`. One light theme. No dark-theme control.

This package is Zara Home, slug `zara-home`. It is not the Zara fashion store.

A market gate covers the bare host. After Worldwide English is chosen, a dialog titled HELLO asks whether to continue in International. Close dismisses it. YES, CONTINUE IN INTERNATIONAL was used once to enter the store. NO, GO TO THE WEBSITE was not used. The dialog reopens on a fresh load of `/ww/` paths.

No email, password, code, phone, or address was typed. No identity provider was clicked. No form was submitted. No captcha was solved. Checkout was not entered. No signed-in account was opened. The newsletter field was not filled.

## Market gate https://www.zarahome.com/

The bare host redirects into the market selector (`/inditex-sel` during submit). Direct loads of `/ww/` without the selection cookie bounce back here.

| Control | Opens |
|---|---|
| Market combobox | searchable listbox of markets on the same page. Worldwide is the last option. Filtering the field to Worldwide and choosing that option sets the store. |
| Language combobox | listbox on the same page. After Worldwide: Português, Español, Français, English. |
| GO (aria-label "Enter to the store") | page https://www.zarahome.com/ww/ for Worldwide English. A script click does not submit. A pointer click does. |
| Cookie banner close | dismisses the OneTrust banner on the same page. Accept All was not clicked. |
| Cookies policy | PDF at `https://static.zarahome.net/8/staticContent4/PDF/PC/V_en.pdf` |

## International dialog (same page, after `/ww/`)

| Control | Opens |
|---|---|
| Close | dismisses the dialog. The page stays on the current `/ww/` URL. |
| YES, CONTINUE IN INTERNATIONAL | keeps the International store on the same page. |
| NO, GO TO THE WEBSITE | not used. It would leave International. |
| Select yours here | market switch. Not opened after the store was chosen. |

## Shell (desktop, 1440)

Header on https://www.zarahome.com/ww/ and inner shop pages. On the homepage the header sits on the photo and its labels read light. On category, product, search, basket, and error pages the header is a white bar with ink labels.

| Control | Opens |
|---|---|
| Skip to main content | in-page skip link |
| Menu (hamburger) | drawer on the same page, 315px, class `main-menu-side-nav`. See Menu drawer. |
| Logo ("Go to the home page") | page https://www.zarahome.com/ww/ |
| SEARCH | page https://www.zarahome.com/ww/search.html |
| LOG IN (role link, no href, aria-label "Log In") | page on `account.zarahome.com` (login or register wall). A script click does not leave the shop. A pointer click does. Branch stopped. See Login wall. |
| HELP | page https://www.zarahome.com/ww/shop-guide.html |
| BASKET | page https://www.zarahome.com/ww/shop-cart.html |

## Menu drawer (same page)

Opened from Menu. The label is a link for most rows. A chevron marks a submenu. Clicking the BEDDING label both navigates and opens the bedding submenu.

| Control | Opens |
|---|---|
| GIFT IDEAS NEW | page https://www.zarahome.com/ww/gift-ideas-n1472 |
| BEDDING › | page https://www.zarahome.com/ww/bedroom-duvet-covers-n946, and a left submenu on the way |
| HOME DECOR › | page https://www.zarahome.com/ww/home-decor-throws-living-room-couch-n995 |
| KITCHEN AND DINING › | button, no href. Submenu not opened. |
| BATHROOM › | page https://www.zarahome.com/ww/bathroom-bath-towels-n1051 |
| KIDS AND BABY › | page https://www.zarahome.com/ww/kids-n1094 |
| CULINARY STORIES › | page https://www.zarahome.com/ww/culinary-stories-n5364 |
| WITHDRAWAL OF ITEMS | page https://www.zarahome.com/ww/withdrawn-from-sale-n5187 |
| +INFO | link, no href. Not opened. |

Bedding submenu, seen on the category page:

| Control | Opens |
|---|---|
| ‹ BEDDING | back to the main drawer |
| BED LINEN | page https://www.zarahome.com/ww/bedroom-duvet-covers-n946 |
| See all | page https://www.zarahome.com/ww/bedroom-bedding-n945 |
| Duvet covers | page https://www.zarahome.com/ww/bedroom-duvet-covers-n946 |
| Basics | page https://www.zarahome.com/ww/bedroom-basic-sheets-n1799 |
| Fitted sheets | page https://www.zarahome.com/ww/bedroom-fitted-sheets-n948 |
| Flat sheets | page https://www.zarahome.com/ww/bedroom-flat-sheets-n947 |
| Valances | page https://www.zarahome.com/ww/bedroom-valances-n952 |
| QUILTS | page https://www.zarahome.com/ww/bedroom-quilts-n950 |
| BEDSPREADS | page https://www.zarahome.com/ww/bedroom-quilted-bedspreads-n951 |
| CUSHIONS | page https://www.zarahome.com/ww/bedroom-cushions-n964 |
| BLANKETS AND THROWS | page https://www.zarahome.com/ww/bedroom-throws-blankets-n963 |
| DRESSING ROOM | page https://www.zarahome.com/ww/dressing-room-n2463 |

Also linked from the header chrome, not opened in this pass: CONTACT US https://www.zarahome.com/ww/contact-shopping-online.html, GUEST PURCHASE https://www.zarahome.com/ww/guest-orders.html, CAREERS https://www.zarahome.com/ww/careers-n5110.

## Home https://www.zarahome.com/ww/

The homepage is a vertical photo scroller (swiper), not a static document. Scroll position often lands on a later slide or on the footer. Category tiles cover the slide.

| Control | Opens |
|---|---|
| Photo tile "Navigate to category 1023" | page https://www.zarahome.com/ww/kids-n1094 |
| Photo tile "Navigate to category ZARA HOME" | in-page category target |
| Slide labels 1023 / ZARA HOME | same-page slide change |
| App card "STILL DON'T HAVE OUR APP?" Close | dismisses the card (`.qrBanner` becomes `display: none`). Not a navigation. The QR was not followed. |

## Footer (desktop)

Present on the homepage (after the photo scroller) and on inner pages.

| Control | Opens |
|---|---|
| SUBSCRIBE ME | page https://www.zarahome.com/ww/newsletter.html. Not opened for submit. No email typed. |
| Facebook, Instagram, Pinterest, YouTube, X, Spotify, TikTok | external social sites. Not followed. |
| App Store / Google Play / QR | external app stores. Not followed. |
| HELP CENTRE, CONTACT, GUEST PURCHASE, STORES | buttons. Destinations not opened. |
| WORK WITH US | external https://www.inditexpeople.com/ww/en/joinus |
| PRESS | external https://press.zarahome.com/ECOMPressSite/login.html. Not entered. |
| SITEMAP | button. Not opened. |
| TERMS AND CONDITIONS, PRIVACY POLICY, COOKIES POLICY, COOKIES SETTINGS, LEGAL MENTIONS | buttons. Not opened. Cookies Settings was not submitted. |
| USE OF AI | PDF on static.zarahome.net. Not opened. |
| COLLECTIONS | page https://www.zarahome.com/ww/bedroom-n944 |
| DUVET COVERS | page https://www.zarahome.com/ww/bedroom-duvet-covers-n946 |
| DECORATIVE ACCESSORIES | page https://www.zarahome.com/ww/home-decor-n989 |
| TOWELS | page https://www.zarahome.com/ww/bathroom-bath-towels-n1051 |
| KIDS AND BABY | page https://www.zarahome.com/ww/kids-n1094 |
| CUSHIONS | page https://www.zarahome.com/ww/home-decor-sofa-cushions-n994 |
| SINGAPORE / ENGLISH | market switch. The label is the geo guess even on the International store. Not used to change market. |

## Phone (390×844)

The header shrinks to 50px. Menu, logo, and icon buttons for Log In, Help, and Basket stay. Search drops out of the header on the homepage and appears as a full-width row once the photo slide is the active view. On a category page the logo is replaced by the category name, a home icon returns to `/ww`, and Search plus a Filters icon sit under the header.

Footer columns (Help, Company, Policies, You might be interested) collapse to accordion rows with a plus. Follow us on and Download our app stay expanded. App Store and Google Play are icon links. The QR moves off this width.

| Control | Opens |
|---|---|
| Menu | same drawer as desktop, on the same page |
| Log In icon | same login wall as desktop. Not re-entered on this width. |
| Basket icon | same empty basket page |
| Footer plus rows | in-page accordion. Not expanded in the capture. |

## Category https://www.zarahome.com/ww/bedroom-duvet-covers-n946

Title "Duvet covers | Zara Home Worldwide". Breadcrumb: BEDDING > BED LINEN > DUVET COVERS.

| Control | Opens |
|---|---|
| SEE ALL, DUVET COVERS, BASICS, FITTED SHEETS, FLAT SHEETS, VALANCES | the bedding pages listed in the submenu |
| VIEW 1 2 3 | grid density on the same page |
| FILTERS, SORT, SHARE | same-page controls. Not submitted. |
| Product card | product page, for example https://www.zarahome.com/ww/sateen-duvet-cover-300-thread-count-l40136088 |
| Colour dots | same-page colour change |
| ADD | size list on the same page. A size was not chosen and nothing was added. |
| Newsletter overlay | auto-opens on some loads. Close dismisses it. Not submitted. |

## Product https://www.zarahome.com/ww/sateen-duvet-cover-300-thread-count-l40136088

Title "SATEEN DUVET COVER (300 THREAD COUNT) | Zara Home Worldwide". Price range 45.99 € – 79.99 €.

| Control | Opens |
|---|---|
| Gallery thumbnails and arrows | same-page gallery |
| Colour buttons (MINT GREEN, SAND, PINK, RASPBERRY, BROWN) | same-page colour change |
| ADD | inline size list on the same page (Single, Double, King, Super king, Emperor). Some rows say Coming Soon or View similar products. No size was selected. Nothing was added. Checkout was not entered. |
| PRODUCT DETAILS, SIZE GUIDE, SHIPPING AND RETURNS, IN-STORE AVAILABILITY | in-page disclosures or links. Not used to start checkout. |
| COMPLETE THE LOOK, YOU MAY ALSO LIKE | product links on the same page |

## Search https://www.zarahome.com/ww/search.html

| Control | Opens |
|---|---|
| Field placeholder "What are you searching for?" | same page. Empty state shows YOU MIGHT BE INTERESTED product tiles. |
| Search by image | file input. No file was uploaded. |
| Close (X) | leaves the search field |
| Enter on a product term ("linen") | page https://www.zarahome.com/ww/search.html?term=linen with FILTERS, SORT, and results. This is product search, not an account form. |
| Suggestion chips (BED LINEN, LINEN SHEET, LINEN COTTON) | search refinements on the same page |

## Basket https://www.zarahome.com/ww/shop-cart.html

Empty public basket. Tabs: SHOPPING BASKET (0), BUY LATER (0). Copy: "YOUR BASKET IS EMPTY" and "The items you add will be displayed here". Checkout was not entered. No item was added.

## Error https://www.zarahome.com/ww/error.html

Public empty state. Copy: "PAGE UNAVAILABLE" and "Sorry, this page is no longer available on our website." RETURN TO HOME PAGE returns to `/ww/`. Guessed paths `/ww/logon` and `/ww/logon.html` land here. They are not the login wall.

## Login wall (branch stopped)

LOG IN in the shop header opens a separate host, `account.zarahome.com`, on a combined page titled "Log in or register - Zara Home International". There is no separate signup page until an email is submitted, so signup was not opened.

Visible, empty, not used: ZARA HOME logo, heading LOG IN OR REGISTER, empty Email field, CONTINUE, ACCESS WITH, CONTINUE WITH QR, CONTINUE WITH FACEBOOK, CONTINUE WITH GOOGLE, CONTINUE WITH APPLE, Privacy Policy, Help.

CONTINUE was not clicked. No identity provider was clicked. No email, password, code, or phone was typed. The form was not submitted. The shop tokens stay ZH-Sans. This wall uses Zara APP Sans, a 2px button radius, and weight 500 on CONTINUE. Those values are recorded here and are not written over the shop tokens.

`login-extracted` stays not-started. `webapps-manifest.json` was not edited.
