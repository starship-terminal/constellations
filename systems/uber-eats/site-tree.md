# Uber Eats public site tree

Mapped on 2026-11-21 from [https://www.ubereats.com/](https://www.ubereats.com/) in headless Chromium, signed out. Desktop shots are 1440 by 900 CSS pixels at 1x. The phone location shot is 390 by 844 CSS pixels at 2x. Query strings are omitted. Visitor ids and device ids are not recorded.

A Cloudflare challenge dialog (`#cf-challenge-overlay`, "Please verify you are human") painted over some loads. It was hidden in the page, not solved. Routes that stayed on "One more step" or "Just a moment" were not photographed as product pages.

The homepage paints one of two heroes. This pass photographed the wood table hero ("Enter delivery address", Deliver now, Search here). An earlier load in the same session painted a green illustrated hero ("Enter your address to find local favorites", Current location). Both are the same URL.

## Header

| Control | Opens | Shot |
|---|---|---|
| Uber Eats wordmark | [https://www.ubereats.com/](https://www.ubereats.com/) | [home-light-default.png](screenshots/home-light-default.png) |
| Main navigation menu | A start drawer, 300 px, white. Items below. | [home-light-nav-open.png](screenshots/home-light-nav-open.png) |
| Get a ride | [https://www.uber.com/ride](https://www.uber.com/ride). Not opened. | header in the home shot |
| Log in | [https://auth.uber.com/v2/](https://auth.uber.com/v2/). Wall. Stopped. | [login-wall-light-default.png](screenshots/login-wall-light-default.png) |
| Sign up | Same auth host. Wall. Stopped. | same login shot |
| Address pill in the scrolled header | The address field. Not filled. | [home-light-footer.png](screenshots/home-light-footer.png) |

Drawer items, from the open panel:

| Item | Destination | Followed |
|---|---|---|
| Sign up | auth.uber.com/v2/ | No. Wall. |
| Log in | auth.uber.com/v2/ | No. Wall. |
| Add your restaurant | merchants.ubereats.com/s/signup/ | No. Signup. |
| Create a business account | www.uber.com/business/eats | No. Account creation. |
| Sign up to deliver | www.uber.com/drive/delivery/ on this load. A footer link used www.uber.com/deliver/. | No. Signup. |
| iPhone | apps.apple.com, Uber Eats listing | No. Store. |
| Android | play.google.com, Uber Eats listing | No. Store. |

## Hero

| Control | Opens | Shot |
|---|---|---|
| Address field, placeholder "Enter delivery address" | Focus. A blue focus ring painted. Nothing typed. | [home-light-address-focused.png](screenshots/home-light-address-focused.png) |
| Deliver now | A menu: Deliver now, Schedule for later. Schedule was not opened. | [home-light-deliver-now.png](screenshots/home-light-deliver-now.png) |
| Search here | Would search. Not pressed. | home default |
| Or Sign in | auth.uber.com/v2/. Wall. Stopped. | login wall |

## Footer

Photographed at the bottom of the home page: [home-light-footer.png](screenshots/home-light-footer.png).

| Control | Destination | Followed |
|---|---|---|
| Get Help | help.uber.com/ubereats | Yes. Landed on the restaurants help hub. [help-light-default.png](screenshots/help-light-default.png) |
| Buy gift cards | uber.com/gift-cards/ | No. |
| Add your restaurant | merchants.ubereats.com/s/signup/ | No. Signup. |
| Sign up to deliver | www.uber.com/deliver/ | No. Signup. |
| Create a business account | www.uber.com/business/eats | No. |
| Promotions | /promo | Opened. The response was a reCAPTCHA interstitial ("One more step"). Not solved. Not kept as a product shot. |
| Restaurants near me | /near-me | Blocked by an automated security check at def.uber.com/en/challenge. Not solved. |
| View all cities | /location | Yes. [location-light-default.png](screenshots/location-light-default.png) |
| View all countries | /location#all-countries | Yes, scrolled to the country list. [location-light-countries.png](screenshots/location-light-countries.png) |
| Pickup near me | /pickup/near-me | Blocked on an earlier pass (403 security verification). |
| About Uber Eats | about.ubereats.com/ | 404, "Page Not Found". Not kept. |
| Shop groceries | /shopping | Redirected to the security check. Not solved. |
| English | Dialog "Select a language": English (checked), Español. No language was chosen. | [home-light-language.png](screenshots/home-light-language.png) |
| App Store badge | apps.apple.com listing | No. |
| Google Play badge | play.google.com listing | No. |
| Facebook, Twitter, Instagram | Public Uber Eats profiles | No. |
| Privacy Policy | www.uber.com/legal/privacy/users/ | No. |
| Terms | www.uber.com/terms | No. |
| Pricing | help.uber.com pricing article | No. |
| Do not sell or share my personal information | privacy.uber.com | No. |
| $0 Delivery Fee with Uber One | /eats-pass, which redirected to /uber-one | Yes. [uber-one-light-default.png](screenshots/uber-one-light-default.png) |

Chain names on the home page (Subway, Dunkin', Pizza Hut, and the rest of the visible grid) go to `/brand/<slug>`. One brand URL was requested and returned a security verification page. No brand page was photographed. "Load more chains" was visible on a footer scroll and was not pressed.

City names go to `/city/<slug>`. Country names go to `/<country-code>`. One city was not opened as its own document: the location index already shows the city list.

## Location page

[https://www.ubereats.com/location](https://www.ubereats.com/location)

| Control | Opens | Shot |
|---|---|---|
| Address field | Focus. Nothing typed. | [location-light-address-focused.png](screenshots/location-light-address-focused.png) |
| Find Food | Would search. Not pressed. | location default |
| Region and city links | `/region/<name>` and `/city/<slug>` | Listed, not each opened |
| Phone width | Same page, address stacked over Find Food | [mobile-location-light-default.png](screenshots/mobile-location-light-default.png) |

## Uber One

[https://www.ubereats.com/uber-one](https://www.ubereats.com/uber-one), reached from the footer membership bar (`/eats-pass` redirected here).

| Control | Destination | Followed |
|---|---|---|
| Sign in | auth.uber.com/v2/ | No. Wall. |
| Sign in to join | auth.uber.com/v2/ | No. Wall. |
| Legal and membership links | www.uber.com documents and help articles | No. |

## Help

[https://help.uber.com/ubereats](https://help.uber.com/ubereats) redirected to the restaurants hub.

| Control | Opens | Followed |
|---|---|---|
| Audience tabs (Riders, Driving & Delivering, Uber Eats, Merchants, Bikes, Business, Freight, Fleet) | Other help hubs | Uber Eats was already selected. Others not opened. |
| Restaurants / Stores | In-page topic filter | Restaurants was selected. Stores not pressed. |
| Log in for personalized support | help.uber.com login | No. Wall. |
| Search | A question field. Not filled. Not submitted. | Visible in the help shot |
| Topic rows (Account, Membership) | Help articles | Not opened. |

## Phone

A 390 px load of the homepage painted an app gate: Continue in app, Continue in browser. Continue in browser was pressed once. The next paint was still the gate, then a Cloudflare verify dialog. The captcha was not solved. Those frames were not kept. The phone location page loaded without the gate and is the phone shot.

## Walls and blocked routes

| URL | What happened |
|---|---|
| auth.uber.com/v2/ | Login and signup wall. Photographed. Stopped. |
| merchants.ubereats.com/s/signup/ | Restaurant signup. Not opened. |
| www.uber.com/business/eats | Business account. Not opened. |
| www.uber.com/deliver/ and www.uber.com/drive/delivery/ | Courier signup. Not opened. |
| /near-me, /near-me/grocery, /pickup/near-me, /shopping | Automated security check. Not solved. |
| /promo | reCAPTCHA interstitial. Not solved. |
| /brand/subway and other brand slugs | Security verification on the one request. Not solved. |
| about.ubereats.com/ | 404. |

Signed-in feed, orders, checkout, and account settings were not entered. The known probe of `/orders` redirected to sign-in. That branch stays stopped.
