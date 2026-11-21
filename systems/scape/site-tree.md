# Scape site tree

Mapped from the public homepage of [https://www.scape.com/](https://www.scape.com/) on 2026-11-21, before screenshots. The official product is Scape UK student housing (London, Leeds, Guildford). Scape Australia is a different site ([https://www.scape.com.au/](https://www.scape.com.au/)) and is out of scope.

The homepage returned HTTP 200. `robots.txt` allows `/` and disallows `/*my-account` and `/*my-portal`. The public sitemap at [https://www.scape.com/sitemap.xml](https://www.scape.com/sitemap.xml) lists 215 URLs. There is no dark theme switch on the public pages.

CookieYes (`cky-consent-container`) covers the first paint. It was hidden in CSS and removed from the DOM. Consent buttons were not clicked (they can POST). The promo strip "RATES FOR 27/28 NOW LIVE" is site chrome, not a cookie banner. Its close control dismisses that strip only.

No form was submitted. No room was booked. No account was created. Phone numbers, street addresses, emails and map links are not copied into this file.

## Auth walls (stop)

| URL | What it is | What this capture did |
|---|---|---|
| [https://www.scape.com/my-account/](https://www.scape.com/my-account/) | Login wall. Title: "Login into your account". `robots.txt` disallows `/*my-account`. | Recorded and stopped. No fields filled. |
| [https://www.scape.com/my-portal/](https://www.scape.com/my-portal/) | Disallowed by `robots.txt`. HTTP 404 in this probe. | Not entered. |
| [https://www.scape.com/login/](https://www.scape.com/login/) | HTTP 404. | Dead end. |
| [https://www.scape.com/account/](https://www.scape.com/account/) | HTTP 404. | Dead end. |
| [https://www.scape.com/sign-in/](https://www.scape.com/sign-in/) | HTTP 404. | Dead end. |
| [https://www.scape.com/signin/](https://www.scape.com/signin/) | HTTP 404. | Dead end. |

The desktop header has no Sign in label. The booking icon goes to a public cart shell, not to login. The phone menu has a Profile row. It was not opened. It is the same account wall as `/my-account/`.

## Shared chrome

These controls appear on every captured page.

| Control | Opens |
|---|---|
| Promo "RATES FOR 27/28 NOW LIVE" | Page [https://www.scape.com/about/offers/](https://www.scape.com/about/offers/) |
| Promo close | Dismisses the promo strip. Not a page. |
| Logo | Page [https://www.scape.com/](https://www.scape.com/) |
| Our locations | Menu (mega menu). London buildings, Explore London, All cities, Visit Scape Australia (external, not followed). |
| Life at Scape | Page [https://www.scape.com/life-at-scape/](https://www.scape.com/life-at-scape/) |
| Blog | Page [https://www.scape.com/blog/](https://www.scape.com/blog/) |
| Company | Page [https://www.scape.com/company/](https://www.scape.com/company/) |
| FAQs | Page [https://www.scape.com/about/faq/](https://www.scape.com/about/faq/) |
| Contact us | Page [https://www.scape.com/contact-us/](https://www.scape.com/contact-us/) |
| FIND A ROOM | Page [https://www.scape.com/rooms/](https://www.scape.com/rooms/) |
| Favourites icon | Page [https://www.scape.com/favourites/](https://www.scape.com/favourites/) |
| Booking icon | Page [https://www.scape.com/booking/](https://www.scape.com/booking/) (public empty cart, title "Welcome", body "Loading...") |
| Mobile menu trigger | Menu (same destinations as the desktop nav, at 390). |
| Profile (phone menu only) | Auth wall. Not opened. Same stop as `/my-account/`. |
| Footer columns | Pages listed under Footer. |
| Footer social (TikTok, Instagram, Facebook) | External. Not followed. |
| tel: and Google Maps links on contact and city pages | External. Not followed. Phone numbers and precise locations are not recorded. |

## Home ([https://www.scape.com/](https://www.scape.com/))

| Control | Opens |
|---|---|
| Hero slides 1–4 | In-page carousel. Not a new page. |
| London / Guildford / Leeds city cards | City pages (see Buildings). |
| LIFE AT SCAPE | Page [https://www.scape.com/life-at-scape/](https://www.scape.com/life-at-scape/) |
| COMPARE NOW | Page [https://www.scape.com/university-halls-vs-private-student-accommodation/](https://www.scape.com/university-halls-vs-private-student-accommodation/) |
| Guide cards and VIEW BLOG | Blog index or one post. |
| VISIT FAQ | Page [https://www.scape.com/about/faq/](https://www.scape.com/about/faq/) |
| FAQ accordions (Who is Scape?, offers, room type, and the rest) | In-page disclosure. Not a new page. |
| Footer tabs London / Other Cities / Neighbourhoods / Universities | In-page tab. Each item is a page link. |

## Find a room ([https://www.scape.com/rooms/](https://www.scape.com/rooms/))

| Control | Opens |
|---|---|
| Full academic year / Semester stay / Flexible stay / Summer stay | In-page filter. Reloads the public room list. Not a booking. |
| SORT BY, LOCATION, BOOKING PERIOD, PRICE, ROOM TYPE, ROOM SIZE | Menu (filter dropdown). Options stay on `/rooms/`. |
| Accessible only | In-page toggle. |
| Find out more (PLUS rooms) | In-page disclosure. |
| Room card | Page under a building, for example [https://www.scape.com/student-accommodation-wembley/en-suite/standard/](https://www.scape.com/student-accommodation-wembley/en-suite/standard/). Representative type captured. Every size variant is the same template. |
| Room card image carousel Previous / Next | In-card carousel. |
| Favourite | Local favourites list at [https://www.scape.com/favourites/](https://www.scape.com/favourites/). Not an account. |
| Book / enquire that would submit a booking | Not pressed. Booking a room is out of scope. |

## Favourites ([https://www.scape.com/favourites/](https://www.scape.com/favourites/))

Empty public state: "NO FAVOURITES ADDED YET" and FIND A ROOM, which returns to [https://www.scape.com/rooms/](https://www.scape.com/rooms/).

## Booking ([https://www.scape.com/booking/](https://www.scape.com/booking/))

Public cart shell. Title "Welcome". Body stayed on "Loading..." in this probe. No checkout was started. No payment fields were filled.

## Contact ([https://www.scape.com/contact-us/](https://www.scape.com/contact-us/))

| Control | Opens |
|---|---|
| OPEN FORM | Dialog (enquiry form). Opened and closed. Not filled. Not submitted. |
| BOOK CALL | Dialog (location select plus scheduling). Not filled. Not submitted. |
| WHATSAPP | External chat. Not followed. |
| Location select | Menu of building names. Not submitted. |
| Phone and Google Maps | External. Not followed. Numbers and pins are not recorded. |
| VISIT FAQ | Page [https://www.scape.com/about/faq/](https://www.scape.com/about/faq/) |

## Blog ([https://www.scape.com/blog/](https://www.scape.com/blog/))

| Control | Opens |
|---|---|
| All / Guides / University Life / Wellbeing | In-page category filter. |
| Tag chips (All, Apartment, Beach, building names, SHOW ALL) | In-page filter. |
| A post card | One blog post. One post captured as the template. |
| Pagination 1–9 | Pages [https://www.scape.com/blog/page/1/](https://www.scape.com/blog/page/1/) through [https://www.scape.com/blog/page/9/](https://www.scape.com/blog/page/9/). Page 2 captured as the template. |

The sitemap lists 86 posts. They share one article template. Capturing every post would repeat the same chrome.

## FAQs ([https://www.scape.com/about/faq/](https://www.scape.com/about/faq/))

Category chips (ALL, CONTRACTS AND PRICING, BOOKINGS, LIVING WITH US, CHECK IN AND CHECK OUT, CANCELLATION AND FEES) filter the list in place. Each question is an accordion. CONTACT US goes to [https://www.scape.com/contact-us/](https://www.scape.com/contact-us/).

## Buildings

Mega menu and footer open these city and building pages:

| Control | Opens |
|---|---|
| London / Explore London | [https://www.scape.com/student-accommodation-london/](https://www.scape.com/student-accommodation-london/) |
| Bloomsbury | [https://www.scape.com/student-accommodation-bloomsbury/](https://www.scape.com/student-accommodation-bloomsbury/) |
| Canada Water | [https://www.scape.com/student-accommodation-canada-water/](https://www.scape.com/student-accommodation-canada-water/) |
| Hammersmith | [https://www.scape.com/student-accommodation-hammersmith/](https://www.scape.com/student-accommodation-hammersmith/) |
| Kings Cross | [https://www.scape.com/student-accommodation-kings-cross/](https://www.scape.com/student-accommodation-kings-cross/) |
| Mile End | [https://www.scape.com/student-accommodation-mile-end/](https://www.scape.com/student-accommodation-mile-end/) |
| Shoreditch | [https://www.scape.com/student-accommodation-shoreditch/](https://www.scape.com/student-accommodation-shoreditch/) |
| Wembley | [https://www.scape.com/student-accommodation-wembley/](https://www.scape.com/student-accommodation-wembley/) |
| Guildford | [https://www.scape.com/student-accommodation-guildford/](https://www.scape.com/student-accommodation-guildford/) |
| Leeds | [https://www.scape.com/student-accommodation-leeds/](https://www.scape.com/student-accommodation-leeds/) |
| Central London | [https://www.scape.com/student-accommodation-central-london/](https://www.scape.com/student-accommodation-central-london/) |
| East London | [https://www.scape.com/student-accommodation-east-london/](https://www.scape.com/student-accommodation-east-london/) |
| Semester stays | [https://www.scape.com/semester-stays/london/](https://www.scape.com/semester-stays/london/) |
| Summer stays | [https://www.scape.com/summer-stays/london/](https://www.scape.com/summer-stays/london/) and [https://www.scape.com/summer-stays/leeds/](https://www.scape.com/summer-stays/leeds/) |
| Visit Scape Australia | External [https://www.scape.com.au/](https://www.scape.com.au/). Not followed. |
| USA - launching soon | [https://www.scape.com/scape-student-accommodation-usa/](https://www.scape.com/scape-student-accommodation-usa/) |

On a building page the local nav is THE BUILDING, ROOMS, NEIGHBOURHOOD, SOCIAL (pages under that building). Amenity chips (THE ESSENTIALS, SHARED SPACES, LIFESTYLE, LOUNGE, and the rest) are in-page tabs. VIEW 360 opens an external Matterport tour and was not followed. FIND A ROOM on a building goes to that building's rooms list.

A room type page (example: Wembley standard en suite) has a gallery, a "Looking for a summer stay?" link, and Read more (in-page disclosure). Book was not pressed.

## Company and editorial pages

| Control | Opens |
|---|---|
| About Scape | [https://www.scape.com/about-scape/](https://www.scape.com/about-scape/) |
| All-inclusive living | [https://www.scape.com/all-inclusive-student-living/](https://www.scape.com/all-inclusive-student-living/) |
| Our awards | [https://www.scape.com/student-accommodation-awards/](https://www.scape.com/student-accommodation-awards/) |
| Uni vs private halls | [https://www.scape.com/university-halls-vs-private-student-accommodation/](https://www.scape.com/university-halls-vs-private-student-accommodation/) |
| London Reviews | [https://www.scape.com/london-reviews/](https://www.scape.com/london-reviews/) |
| Offers | [https://www.scape.com/about/offers/](https://www.scape.com/about/offers/) |
| Flexible Policies | [https://www.scape.com/about/flexible-policies/](https://www.scape.com/about/flexible-policies/) |
| Careers | [https://www.scape.com/company/careers/](https://www.scape.com/company/careers/) |
| ESG | [https://www.scape.com/company/esg/](https://www.scape.com/company/esg/) |
| ESG environment / social / governance | [https://www.scape.com/company/esg-environment/](https://www.scape.com/company/esg-environment/), [https://www.scape.com/company/esg-social/](https://www.scape.com/company/esg-social/), [https://www.scape.com/company/esg-governance/](https://www.scape.com/company/esg-governance/) |
| Meanwhile / Morro / press READ ARTICLE | External. Not followed. |
| London postgraduate / Leeds postgraduate | [https://www.scape.com/london-postgraduate-accommodation/](https://www.scape.com/london-postgraduate-accommodation/), [https://www.scape.com/leeds-postgraduate-accommodation/](https://www.scape.com/leeds-postgraduate-accommodation/) |

University landing pages in the footer (same template, one captured): ACM, Birkbeck, Brunel, City, UEL, Goldsmiths, GSA, Imperial, KCL, Leeds Arts, Leeds Beckett, Leeds University, LSE, Middlesex, Queen Mary, Roehampton, SOAS, Southbank, Surrey, UAL, UCA, UCL, University of Law, UWL, Westminster. UWL's card on the London page points at the university's own site (external, not followed).

## Legal and policy pages

Footer and sitemap. Same long-form template. One captured as the template. The rest are the same chrome:

- [https://www.scape.com/about/privacy-policy/](https://www.scape.com/about/privacy-policy/)
- [https://www.scape.com/about/cookie-policy/](https://www.scape.com/about/cookie-policy/)
- [https://www.scape.com/about/terms-and-conditions/](https://www.scape.com/about/terms-and-conditions/)
- [https://www.scape.com/about/booking-terms/](https://www.scape.com/about/booking-terms/)
- [https://www.scape.com/about/booking-terms-and-conditions/](https://www.scape.com/about/booking-terms-and-conditions/)
- [https://www.scape.com/about/code-of-conduct/](https://www.scape.com/about/code-of-conduct/)
- [https://www.scape.com/about/complaints-process/](https://www.scape.com/about/complaints-process/)
- [https://www.scape.com/about/equal-opportunities/](https://www.scape.com/about/equal-opportunities/)
- [https://www.scape.com/about/esg-policy/](https://www.scape.com/about/esg-policy/)
- [https://www.scape.com/about/health-safety-policy/](https://www.scape.com/about/health-safety-policy/)
- [https://www.scape.com/about/modern-slavery-act/](https://www.scape.com/about/modern-slavery-act/)
- [https://www.scape.com/about/refund-policy/](https://www.scape.com/about/refund-policy/)
- [https://www.scape.com/about/whistleblower-policy/](https://www.scape.com/about/whistleblower-policy/)

## What was not opened

- CookieYes Accept, Reject, Customize, Save preferences.
- Any enquiry, call-booking, newsletter or booking submit.
- Google, Apple, or any other identity provider.
- WhatsApp, Matterport, press sites, Scape Australia, social profiles.
- Account, portal, checkout, payment.
