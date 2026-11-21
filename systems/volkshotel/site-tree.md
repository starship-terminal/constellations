# Volkshotel site tree

Mapped from the public homepage [https://www.volkshotel.nl/](https://www.volkshotel.nl/) on 2026-11-21, in headless Chromium, before the screenshot pass. The English home is [https://www.volkshotel.nl/en/](https://www.volkshotel.nl/en/). The homepage returned HTTP 200. Title: "Volkshotel Amsterdam Oost | Hotel / Bar / Restaurant".

The public sitemap index lists `sitemap-misc.xml` (the homepage), `page-sitemap.xml` (marketing pages), and `post-sitemap.xml` (628 blog posts). `robots.txt` allows `/` and disallows `/wordpress/wp-admin/`. There is no dark theme switch. `main.css` has no custom properties and no `prefers-color-scheme` rule.

Cookiebot covers the first paint. It was removed from the DOM. Consent buttons were not clicked. No form was submitted. No date was chosen. No booking was completed. No email, name, phone, or code was typed.

Phone numbers, street addresses, emails, and map links are not copied into this file. The footer shows a published street line and a published inbox. Those strings stay in the screenshots the way the site paints them, and they are not repeated here.

## Auth walls (stop)

| URL | What it is | What this capture did |
|---|---|---|
| [https://www.volkshotel.nl/en/login](https://www.volkshotel.nl/en/login) | HTTP 302 to [https://www.volkshotel.nl/wordpress/wp-login.php](https://www.volkshotel.nl/wordpress/wp-login.php). That URL redirects to itself. Playwright `domcontentloaded` timed out. | Recorded and stopped. No fields filled. No identity provider. |
| [https://www.volkshotel.nl/login](https://www.volkshotel.nl/login) | Same 302 loop. | Recorded and stopped. |
| [https://www.volkshotel.nl/wp-login.php](https://www.volkshotel.nl/wp-login.php) | HTTP 302 to the same WordPress login. | Recorded and stopped. |
| [https://www.volkshotel.nl/en/account](https://www.volkshotel.nl/en/account) | HTTP 404, title "Not found \| Volkshotel". | Dead end. |

The public header has no Sign in label. There is no product account wall on the marketing pages.

## Shared chrome

These controls appear on the English pages.

| Control | Opens |
|---|---|
| BOOK ROOM | Dialog on the same page. Title: "How long would you like to stay?" Month select, day buttons, Business stay, Promocode, Submit. Photographed and stopped. No date chosen. No submit. |
| MENU | Menu overlay `#main-nav-overlay`, same URL. EN, NL, Home, Hotel, Meetings & Events, Badplaats, Canvas, Werkplaats, Doka, Broedplaats, Blog, Agenda, plus map, phone, and mail icons. |
| Logo (menu) | Page [https://www.volkshotel.nl/en/](https://www.volkshotel.nl/en/) |
| EN / NL | Page [https://www.volkshotel.nl/en](https://www.volkshotel.nl/en) or [https://www.volkshotel.nl/nl](https://www.volkshotel.nl/nl) |
| Bottom nav ROOMS, EAT & DRINK, BLOG / AGENDA, LOCATION | In-page anchors on the home page. |
| Footer social (Facebook, Instagram, Spotify) | External. Not followed. |
| Footer map, phone, mail | External. Not followed. |
| job section | External [https://jobs.volkshotel.nl/](https://jobs.volkshotel.nl/). Not entered. |
| press kit | Page [https://www.volkshotel.nl/en/press-kit/](https://www.volkshotel.nl/en/press-kit/) |
| General Info | Page [https://www.volkshotel.nl/en/general-information-house-rules/](https://www.volkshotel.nl/en/general-information-house-rules/) |
| Privacy & Cookie Statement | Page [https://www.volkshotel.nl/en/privacy-and-cookie-statement/](https://www.volkshotel.nl/en/privacy-and-cookie-statement/) |
| Terms & Conditions | Anchor on the general info page. |
| Sustainability | Page [https://www.volkshotel.nl/en/sustainability/](https://www.volkshotel.nl/en/sustainability/) |
| Giftcard | Page [https://www.volkshotel.nl/en/giftcard/](https://www.volkshotel.nl/en/giftcard/) |
| Business | Page [https://www.volkshotel.nl/en/hotel/business-hotel-rooms/](https://www.volkshotel.nl/en/hotel/business-hotel-rooms/) |
| SIGN UP TO OUR NEWSLETTER | Page [https://www.volkshotel.nl/en/newsletter/](https://www.volkshotel.nl/en/newsletter/) |
| Phone hamburger | Same menu overlay, at 390. |

## Home ([https://www.volkshotel.nl/en/](https://www.volkshotel.nl/en/))

| Control | Opens |
|---|---|
| LEARN MORE (promo) | Page [https://www.volkshotel.nl/christmas](https://www.volkshotel.nl/christmas) (English title, path has no `/en/`) |
| SEE OUR ROOMS | Page [https://www.volkshotel.nl/en/hotel/](https://www.volkshotel.nl/en/hotel/) |
| Canvas card | Page [https://www.volkshotel.nl/en/canvas/](https://www.volkshotel.nl/en/canvas/) |
| Doka card | Page [https://www.volkshotel.nl/en/doka/](https://www.volkshotel.nl/en/doka/) |
| Werkplaats card | Page [https://www.volkshotel.nl/en/werkplaats/](https://www.volkshotel.nl/en/werkplaats/) |
| Badplaats card | Page [https://www.volkshotel.nl/en/badplaats/](https://www.volkshotel.nl/en/badplaats/) |
| START READING | Page [https://www.volkshotel.nl/en/blog/](https://www.volkshotel.nl/en/blog/) |
| READ THE LATEST | Page [https://www.volkshotel.nl/en/agenda/](https://www.volkshotel.nl/en/agenda/) |
| SHOW ME THE WAY | Page [https://www.volkshotel.nl/en/directions/](https://www.volkshotel.nl/en/directions/) |

The Dutch home uses the same controls with Dutch labels (BOEK KAMER, MENU, BEKIJK ONZE KAMERS, LEES MEER).

## Hotel ([https://www.volkshotel.nl/en/hotel/](https://www.volkshotel.nl/en/hotel/))

| Control | Opens |
|---|---|
| STANDARD ROOMS / SPECIAL ROOMS (anchor) | In-page anchor. |
| STANDARD ROOMS / SPECIAL ROOMS (`javascript:;`) | In-page tab. Selected tab is black fill, white type, 3px border. |
| Room card | A room page, for example [https://www.volkshotel.nl/en/hotel/m/](https://www.volkshotel.nl/en/hotel/m/). One room page was opened. The other sizes are the same template. |
| BOOK ROOM on a card | Same date dialog as the header. Not completed. |
| Activities | Page [https://www.volkshotel.nl/en/activities/](https://www.volkshotel.nl/en/activities/) |
| Long stay | Page [https://www.volkshotel.nl/en/hotel/longstay/](https://www.volkshotel.nl/en/hotel/longstay/) |
| CONTACT US | External mail link. Not followed. |

`/en/book/` returns the same hotel document. It is not a separate booking page.

## Eat and drink

| Page | Extra control | Opens |
|---|---|---|
| [https://www.volkshotel.nl/en/canvas/](https://www.volkshotel.nl/en/canvas/) | book a table | In-page control. A Zenchef iframe (`bookings.zenchef.com`) paints "Reserve a table". Not entered. |
| Canvas | dinner & drinks, groups, canvas nights, klein canvas, agenda | In-page anchors or sibling Canvas pages. |
| [https://www.volkshotel.nl/en/doka/](https://www.volkshotel.nl/en/doka/) | menu and event links | Sibling Doka pages. |
| [https://www.volkshotel.nl/en/werkplaats/](https://www.volkshotel.nl/en/werkplaats/) | drinks, food, menu | Sibling Werkplaats pages. |
| [https://www.volkshotel.nl/en/badplaats/](https://www.volkshotel.nl/en/badplaats/) | page prose | Footer and chrome only. |

## Blog and agenda

| Control | Opens |
|---|---|
| PEOPLE, HOTSPOTS, MUSIC, ART & CULT, EXPERIMENTS, HOTEL | In-page category filter on [https://www.volkshotel.nl/en/blog/](https://www.volkshotel.nl/en/blog/). |
| Search icon | In-page search. Not typed into. |
| A post card | One blog post. The sitemap lists 628 posts. One index was photographed. Each post is the same card template. |
| Agenda cards | Event pages under the agenda index. |

## Other public pages opened from the footer or the promo

| Page | What it is |
|---|---|
| [https://www.volkshotel.nl/en/directions/](https://www.volkshotel.nl/en/directions/) | Map and arrival prose. |
| [https://www.volkshotel.nl/en/newsletter/](https://www.volkshotel.nl/en/newsletter/) | Title and lede on the page. The form is an iframe. Not filled. |
| [https://www.volkshotel.nl/en/general-information-house-rules/](https://www.volkshotel.nl/en/general-information-house-rules/) | Prose. |
| [https://www.volkshotel.nl/en/press-kit/](https://www.volkshotel.nl/en/press-kit/) | Press sections. Downloads not taken. |
| [https://www.volkshotel.nl/en/sustainability/](https://www.volkshotel.nl/en/sustainability/) | Prose. |
| [https://www.volkshotel.nl/en/giftcard/](https://www.volkshotel.nl/en/giftcard/) | Gift card copy and a balance field. Not filled. |
| [https://www.volkshotel.nl/en/hotel/business-hotel-rooms/](https://www.volkshotel.nl/en/hotel/business-hotel-rooms/) | Business stays. BOOK NOW points at `/?book_room`. Not followed into a completed booking. |
| [https://www.volkshotel.nl/en/privacy-and-cookie-statement/](https://www.volkshotel.nl/en/privacy-and-cookie-statement/) | Prose. |
| [https://www.volkshotel.nl/christmas](https://www.volkshotel.nl/christmas) | Promo page. BOOK A ROOM points at `/?book_room`. Not completed. |
| [https://www.volkshotel.nl/en/meetings-events/](https://www.volkshotel.nl/en/meetings-events/) | Event types. Contact forms were not submitted. |
| [https://www.volkshotel.nl/en/activities/](https://www.volkshotel.nl/en/activities/) | Activity cards. |
| [https://www.volkshotel.nl/en/broedplaats/](https://www.volkshotel.nl/en/broedplaats/) | Workspace page. |

## Not followed

Booking submit, Mews at `booking.volkshotel.nl`, the Zenchef table widget, the newsletter iframe, the gift card balance field, jobs.volkshotel.nl, WordPress admin, identity providers, and every `mailto:`, `tel:`, and map link.
