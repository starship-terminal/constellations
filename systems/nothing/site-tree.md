# Nothing site tree

Mapped from the public homepage at https://nothing.tech/ on 2026-11-21, in headless Chromium at 1440x900, before screenshots. The storefront is the UK store (`Nothing | UK`). Two overlays greet a fresh visit. Neither was answered as a preference: the Didomi cookie wall was removed from the DOM (Agree, Disagree and Learn More were never clicked), and the region suggestion was dismissed with Stay on United Kingdom so the page underneath could be mapped. That click does not submit a form and does not leave the UK store.

Login and signup walls stop the branch. Nothing was typed into a field. No form was submitted.

## Homepage chrome

| Control | Opens |
|---|---|
| Yellow promo bar, "The Black Friday deals you've waited for are here" | https://nothing.tech/collections/sale |
| Students promo, "Students save up to 10% with Unidays" | https://www.myunidays.com/GB/gb-GB/partners/nothing/micro/online (external partner, not followed) |
| Wordmark, Nothing (R), aria-label Home | https://nothing.tech/ |
| AUDIO (aria-expanded) | Mega menu. Also a link to /collections/audio if followed. |
| PHONES (aria-expanded) | Mega menu. Also a link to /collections/phones if followed. |
| WATCHES | https://nothing.tech/collections/watches (no aria-expanded menu; the page itself lists the watch) |
| CMF | https://nothing.tech/collections/cmf (no aria-expanded menu; the page itself lists CMF products) |
| COMMUNITY | https://nothing.tech/community (no menu; navigates) |
| Cart button, aria-label Cart (0) | Dialog on the same page: empty cart, Continue shopping, and links All products, Audio, Headphones, Phones, Earbuds, Speakers |
| Account icon, aria-label Account | https://nothing.tech/account/login?return_to=%2F which redirects to https://account.nothing.tech/v2/login/ (email and password). Stop. |
| Menu button (desktop, width 0) | Present in the header, not visible at 1440. Visible at 390. |
| Shop now | https://nothing.tech/collections/sale |

## AUDIO menu

Opened by clicking AUDIO. Links inside the panel:

| Label | Href |
|---|---|
| Headphone (1) Pro | /products/headphone-1-pro |
| Ear (3a) | /products/ear-3a |
| Headphone (a) | /products/headphone-a |
| All audio | /collections/audio |
| Headphones | /collections/headphones |
| Earbuds | /collections/earbuds |
| Speakers | /collections/speakers |
| Accessories | /collections/accessories |
| Offers | /offers |

## PHONES menu

| Label | Href |
|---|---|
| Phone (4a) Pro | /products/phone-4a-pro |
| Phone (4a) | /products/phone-4a |
| Phone (3) | /products/phone-3 |
| All phones | /collections/phones |
| Accessories | /collections/accessories |
| Offers | /offers |

## Homepage body

| Control | Opens |
|---|---|
| Shop by category: Earbuds | /collections/earbuds |
| Shop by category: Headphones | /collections/headphones |
| Shop by category: Phones | /collections/phones |
| Shop by category: CMF | /collections/cmf |
| Discover, Headphone (1) Pro | /products/headphone-1-pro |
| Read the interview, NYC | /headphone-1-pro-nyc-launch-event |
| Discover the campaign, V | /v-global-brand-ambassador |
| Going pink, Headphone (a) | /products/headphone-a |
| Going pink, Phone (4a) Pro | /products/phone-4a-pro |
| Going pink, Ear (3a) | /products/ear-3a |
| Discover, CMF Speaker M | /products/cmf-speaker-m |
| Discover, CMF Speaker S | /products/cmf-speaker-s |
| Discover Headphone (a), Charli xcx | /products/headphone-a |
| Join our mailing list, email field and Sign up | Newsletter form. Not filled. Not submitted. |
| Privacy policy (in the signup line) | /pages/privacy-policy |
| Terms (in the signup line) | /pages/terms-of-sales |

## Footer

| Control | Opens |
|---|---|
| About | /about |
| Nothing OS 5.0 | /nothing-os |
| Community | /community |
| Playground | https://playground.nothing.tech/ (external subdomain, not captured as this store) |
| Offers | /offers |
| Support (link) | /pages/support-centre |
| Support (button) | Navigates to /pages/support-centre |
| Newsletter (button) | Scrolls to or focuses the mailing-list field on the same page. Not filled. |
| Business sales enquiries (link) | /support/business-enquiry |
| Business sales enquiries (button) | Same destination as the link |
| Store: United Kingdom | Store picker. Not used to leave the UK store. |
| Language: EN | Language picker. Left on EN. |
| Consent preferences | Reopens Didomi. Not opened. |
| Account | /account, which redirects to the account login wall. Stop. |
| Contact | /pages/contact-support |
| Careers | https://join.nothing.tech/careers/ (external jobs host, not captured) |
| Legal | /pages/privacy-policy |
| Instagram, YouTube, X, TikTok | External social profiles. Not followed. |

## Phone width (390)

The header shows a Menu button (`aria-label` Menu) in place of the desktop nav labels. It opens the same destinations (Audio, Phones, Watches, CMF, Community) as a drawer. Account and cart stay in the header. Account still hits the login wall.

## Stopped branches

| URL | What happened |
|---|---|
| https://nothing.tech/login | 404. Known probe confirmed. |
| https://nothing.tech/account/login | Redirects to https://account.nothing.tech/v2/login/ (email and password). Stop. |
| https://nothing.tech/account | Same login redirect. Stop. |
| https://account.nothing.tech/login/ | Email and password. Stop. Not typed. |

## Public pages captured from this tree

Home, sale, audio, phones, watches, cmf, headphones, earbuds, speakers, accessories, shop-all, one product (Headphone 1 Pro), community, about, Nothing OS, offers, support centre, contact, privacy policy, business enquiry, NYC event, ambassador, accessibility statement, and the 404 at /login as the error state. Checkout, account, and signup were not entered.
