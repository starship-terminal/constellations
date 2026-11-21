# DJI public site tree

Captured 2026-11-21, signed out, in headless Chromium. Start URL `https://www.dji.com/` redirected this client to `https://www.dji.com/sg` (Singapore / English). That region was not chosen. No form was filled, no password typed, no SSO button clicked, no file downloaded.

Two headers share the same labels. The homepage and several older pages use the classic bar (`nav.dui-navbar`). Category and product pages use a newer bar (`header.official-site-header`). A phone user agent is sent to `/sg/mobile`, which uses `nav.dui-navbar-m`.

Login, register, account and store checkout are walls. Those URLs are recorded and the branch stops.

## Desktop bar (1440)

The logo links to `https://www.dji.com/sg`.

| Control | Opens |
|---|---|
| Camera Drones | Page `https://www.dji.com/sg/camera-drones`. Hover does not open a product mega menu on this client. |
| Handheld | Page `https://www.dji.com/sg/handheld`. Hover does not open a product mega menu. |
| Lifestyle Tech (label, not a link) | In-page dropdown. Power Stations goes to `https://www.dji.com/sg/products/power-series`. Robot Vacuums goes to `https://www.romo.tech/` (leaves dji.com). Shot: [home-light-nav-power-stations.png](screenshots/home-light-nav-power-stations.png). |
| Specialized (label, not a link) | In-page dropdown. Enterprise goes to `https://enterprise.dji.com/`. Agriculture goes to `https://ag.dji.com/`. DJI Delivery goes to `https://www.dji.com/sg/delivery`. Shot: [home-light-nav-enterprise.png](screenshots/home-light-nav-enterprise.png). |
| Explore (label, not a link) | In-page dropdown. Who We Are `https://www.dji.com/sg/company`. SkyPixel `https://www.skypixel.com/`. DJI Forum `https://forum.dji.com/`. Media Center `https://www.dji.com/sg/media-center`. DJI Trust Center `https://www.dji.com/sg/trust-center`. DJI Blog `https://viewpoints.dji.com/blog`. Careers `https://we.dji.com/index_en.html`. Shot: [home-light-nav-who-we-are.png](screenshots/home-light-nav-who-we-are.png). |
| Support | Page `https://www.dji.com/sg/support`. |
| Where to Buy | Page `https://www.dji.com/sg/where-to-buy/online-stores`. |
| Search icon | In-page search disclosure. Placeholder "Search dji.com...". Form action `/search`, target `_blank`. Not submitted from the disclosure. Shot: [home-light-search.png](screenshots/home-light-search.png). A direct search URL was loaded separately: `https://www.dji.com/sg/search?q=mavic`. |
| User icon | Account menu. Login goes to `https://www-api.dji.com/sg/redirect/member/login`, which redirects to the login wall. Register goes to the register redirect on the same host. My account points at `https://my.dji.com/`. Logout points at the logout redirect. None of these were followed from the menu. The click that opened the menu also revealed the search recommended list (Checking Device Info, Activating Your Drone, Download Center, Become a Partner, Accessories). Shot: [home-light-account-menu.png](screenshots/home-light-account-menu.png). |
| Singapore | In-page country and region panel. No region was selected. Shot: [home-light-region.png](screenshots/home-light-region.png). |
| Store | Leaves the marketing site for `https://store.dji.com/sg`. Store home was not entered. Checkout and cart were not entered. |

Homepage hero controls, repeated per slide: Learn More opens the product page on `www.dji.com`. Buy Now opens a product URL on `store.dji.com` and that branch stops. Swiper Prev and Swiper Next move the hero. A blue round chat control sits at the lower right. Footer Subscribe is a form and was not filled.

## Phone bar (390)

A phone user agent requesting `https://www.dji.com/` lands on `https://www.dji.com/sg/mobile`. Measured viewport 390 by 844 at device pixel ratio 2.

| Control | Opens |
|---|---|
| Menu (`a.navbar-control`) | Full-screen drawer. Close is the X. Shot: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). |
| Logo | `https://www.dji.com/sg/mobile`. |
| Search | `https://www.dji.com/sg/mobile/search`. Not opened as a typed query. |
| Bag | `https://store.dji.com/sg`. Store branch stops. |
| Camera Drones | `https://www.dji.com/sg/camera-drones`. |
| Handheld | `https://www.dji.com/sg/handheld`. |
| Lifestyle Tech (chevron) | Power Stations and Robot Vacuums, same destinations as desktop. |
| Specialized (chevron) | Enterprise, Agriculture, and `https://www.dji.com/sg/mobile/delivery`. |
| Explore (chevron) | Company, SkyPixel, Forum, media center, trust center, blog, careers. Company, media and trust use `/sg/mobile/...` on this header. |
| Support | `https://www.dji.com/sg/support`. |
| Where to Buy | `https://www.dji.com/sg/mobile/where-to-buy/online-stores`. |
| Singapore / English | `https://www.dji.com/sg/mobile/choose-your-language`. Not followed. |
| Log in to DJI | Login redirect, then the login wall. Not followed from the drawer. |

A Google one-tap sheet ("Sign in to DJI with Google") can mount over the phone homepage. It was removed from the DOM and its script was blocked. Continue was not clicked.

## Pages photographed

Desktop shots are 1440 by 900 at 1x. Phone shots are 390 by 844 at 2x. `-full` is the scrolled page, capped when the page is taller than the capture ceiling.

| Page | URL this client landed on | Shot |
|---|---|---|
| Home | `https://www.dji.com/sg` | [home-light-default.png](screenshots/home-light-default.png) |
| Camera drones | `https://www.dji.com/sg/camera-drones` | [camera-drones-light-default.png](screenshots/camera-drones-light-default.png) |
| Handheld | `https://www.dji.com/sg/handheld` | [handheld-light-default.png](screenshots/handheld-light-default.png) |
| Power stations | `https://www.dji.com/sg/products/power-series` | [power-light-default.png](screenshots/power-light-default.png) |
| Delivery | `https://www.dji.com/sg/delivery` | [delivery-light-default.png](screenshots/delivery-light-default.png) |
| Who we are | `https://www.dji.com/sg/company` | [company-light-default.png](screenshots/company-light-default.png) |
| Media center | `https://www.dji.com/sg/media-center` | [media-light-default.png](screenshots/media-light-default.png) |
| Trust center | `https://www.dji.com/sg/trust-center` | [trust-light-default.png](screenshots/trust-light-default.png) |
| Support | `https://www.dji.com/sg/support` | [support-light-default.png](screenshots/support-light-default.png) |
| Where to buy | `https://www.dji.com/sg/where-to-buy/online-stores` | [where-to-buy-light-default.png](screenshots/where-to-buy-light-default.png) |
| Mavic 4 Pro | `https://www.dji.com/sg/mavic-4-pro` | [mavic-light-default.png](screenshots/mavic-light-default.png) |
| Comparison | `https://www.dji.com/sg/products/comparison-consumer-drones` | [compare-light-default.png](screenshots/compare-light-default.png) |
| Help me choose | `https://www.dji.com/sg/help-me-choose/camera-drones` | [choose-light-default.png](screenshots/choose-light-default.png) |
| Search results | `https://www.dji.com/sg/search?q=mavic` | [search-light-default.png](screenshots/search-light-default.png) |
| Accessibility | `https://www.dji.com/sg/accessibility/web-accessibility` | [a11y-light-default.png](screenshots/a11y-light-default.png) |
| Missing page | `https://www.dji.com/sg/404` (404) | [notfound-light-default.png](screenshots/notfound-light-default.png) |
| Phone home | `https://www.dji.com/sg/mobile` | [mobile-home-light-default.png](screenshots/mobile-home-light-default.png) |
| Phone category | `https://www.dji.com/sg/mobile/camera-drones` | [mobile-camera-drones-light-default.png](screenshots/mobile-camera-drones-light-default.png) |
| Phone product | `https://www.dji.com/sg/mobile/mavic-4-pro` | [mobile-mavic-light-default.png](screenshots/mobile-mavic-light-default.png) |
| Phone support | `https://www.dji.com/sg/mobile/support` | [mobile-support-light-default.png](screenshots/mobile-support-light-default.png) |
| Phone where to buy | `https://www.dji.com/sg/mobile/where-to-buy/online-stores` | [mobile-where-to-buy-light-default.png](screenshots/mobile-where-to-buy-light-default.png) |

On the camera-drones page, series links are in-page anchors on `https://www.dji.com/sg/products/camera-drones` (Mavic, Air, Mini, Lito, Flip, Neo, Avata, Inspire, RC). Take a quiz opens `https://www.dji.com/sg/help-me-choose/camera-drones`. Consumer Drones Comparison opens `https://www.dji.com/sg/products/comparison-consumer-drones`. Accessories and Shop Now open `store.dji.com` and those branches stop. Product cards use Learn More (stays on www.dji.com) and Buy Now (store, stop).

Support has a search field ("Search for Support") and a Search button. The query was not submitted. Service Request and Inquiry, Download Center, GEO Zone Map and Repair Service are further support links and were not each opened. The Mavic 4 Pro page has Buy Now (store, stop), Watch Video (in-page) and Learn More sections. Its full capture is truncated at 32000px.

## Walls

| Control | URL | What it asked for | What this capture did |
|---|---|---|---|
| Login, and the phone Log in to DJI | `https://account.dji.com/login` after `https://www-api.dji.com/sg/redirect/member/login` | Email and password, or Continue With Apple, Continue With Google, Continue With Facebook. Also a verification-code path and a password path. | Recorded the URL and photographed the wall. Did not type, did not click Apple, Google or Facebook. Shot: [login-wall-light-default.png](screenshots/login-wall-light-default.png). |
| Register, Create Your DJI Account | `https://www-api.dji.com/sg/redirect/member/register` | Account creation. | Not followed. |
| My account | `https://my.dji.com/` | Signed-in account. | Not followed. |
| Store, bag, Buy Now, checkout, cart | `https://store.dji.com/sg` and product URLs under it | Store and checkout. | Not entered. |

The login wall also shows a marketing checkbox and Forgot password. Neither was used. A signed query on the login URL is not copied here.

## Not walked

SkyPixel, DJI Forum, the blog, careers, enterprise.dji.com, ag.dji.com and romo.tech are linked from the menus and were not photographed. Firmware, app download and the footer subscribe form were not used. The product mega menu that a signed-in or other-region visitor might see did not fill on this client: Camera Drones and Handheld go straight to their category pages.
