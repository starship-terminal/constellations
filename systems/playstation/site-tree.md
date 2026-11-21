# PlayStation public site tree

Mapped from the live en-sg homepage on 2026-11-21 before screenshots, with Playwright (headless Chromium). Start URL `https://www.playstation.com/` redirects to `https://www.playstation.com/en-sg/` (HTTP 200). No account was created. The OneTrust cookie overlay was hidden in CSS and never submitted.

Auth boundary: the header Sign In control navigates to `https://my.account.sony.com/sonyacct/signin/` (title "Sign In | PlayStation"), which shows a Sign-In ID field, Next, and Create an Account. That branch stops there. `https://www.playstation.com/en-sg/login/` is HTTP 404. Password reset and email sign-up are recorded as walls and not opened past the URL.

## Header (desktop, every marketing page)

| Control | Opens |
|---|---|
| PlayStation logo | Page: `https://www.playstation.com/en-sg` |
| Store | Menu on the same page (does not navigate) |
| PS5 | Menu on the same page |
| Games | Menu on the same page |
| PS Plus | Menu on the same page |
| Accessories | Menu on the same page |
| News | Menu on the same page |
| Support | Menu on the same page |
| Sign In | Auth wall: `https://my.account.sony.com/sonyacct/signin/` |
| Search | Search field on the same page ("Search PlayStation.com"). Typing a query was not submitted |

### Store menu

| Control | Opens |
|---|---|
| Buy games | Page: `https://store.playstation.com/en-sg` (lands on Latest) |
| Subscribe to PS Plus | Page: `/en-sg/ps-plus/` |
| New releases | Page: `https://store.playstation.com/en-sg/pages/latest` |
| Latest discounts | Page: `https://store.playstation.com/en-sg/pages/deals` |
| Buy gift card | Page: `/en-sg/playstation-gift-cards/` |
| Retail Store | Page: `/en-sg/local/retailers/` |

### PS5 menu

| Control | Opens |
|---|---|
| PS5 | Page: `/en-sg/ps5/` |
| PS5 Pro | Page: `/en-sg/ps5/ps5-pro/` |
| PlayStation Portal Remote Player | Page: `/en-sg/accessories/playstation-portal-remote-player/` |
| Games | Page: `/en-sg/ps5/games/` |
| Controllers | Page: `/en-sg/accessories/#controllers` |
| Audio | Page: `/en-sg/accessories/#headsets` |
| Beta Program at PlayStation | Page: `/en-sg/beta-program-at-playstation/` |
| PlayStation App | Page: `/en-sg/playstation-app/` |
| PlayStation Family App | Page: `/en-sg/ps-family-app/` |
| Entertainment | Page: `/en-sg/ps5/ps5-entertainment/` |

### Games menu

| Control | Opens |
|---|---|
| PS5 | Page: `/en-sg/ps5/games/` |
| PS4 | Page: `/en-sg/ps4/ps4-games/` |
| PS VR2 | Page: `/en-sg/ps-vr2/games/` |
| PC | Page: `/en-sg/games/pc-games/` |
| PS Plus | Page: `/en-sg/ps-plus/games/` |
| Browse by genre | Page: `/en-sg/games/` |
| Indies | Page: `/en-sg/games/indies/` |
| Free to play | Page: `/en-sg/editorial/great-free-to-play-games-on-playstation-4/` |
| Deals | Page: `https://store.playstation.com/en-sg/pages/deals` |

### PS Plus menu

| Control | Opens |
|---|---|
| Subscribe | Page: `/en-sg/ps-plus/` |
| What's New | Page: `/en-sg/ps-plus/whats-new/` |
| All Games | Page: `/en-sg/ps-plus/games/` |

### Accessories menu

| Control | Opens |
|---|---|
| PS5 controllers | Page: `/en-sg/accessories/#controllers` |
| PlayStation Portal Remote Player | Page: `/en-sg/accessories/playstation-portal-remote-player/` |
| PS VR2 | Page: `/en-sg/ps-vr2/` |
| Audio | Page: `/en-sg/accessories/#headsets` |
| All accessories | Page: `/en-sg/accessories/` |
| DualSense wireless controller | Page: `/en-sg/accessories/dualsense-wireless-controller/` |
| DualSense Edge wireless controller | Page: `/en-sg/accessories/dualsense-edge-wireless-controller/` |
| PULSE Elite wireless headset | Page: `/en-sg/accessories/pulse-elite-wireless-headset/` |
| PULSE Explore wireless earbuds | Page: `/en-sg/accessories/pulse-explore-wireless-earbuds/` |

### News menu

| Control | Opens |
|---|---|
| This Month on PlayStation | Page: `/en-sg/editorial/this-month-on-playstation/` |
| Facebook | External: `https://www.facebook.com/PlayStationAsia` (not captured) |
| YouTube | External: `https://www.youtube.com/PlayStationAsia` (not captured) |
| Instagram | External: `https://www.instagram.com/playstationasia/` (not captured) |

### Support menu

| Control | Opens |
|---|---|
| Support | Page: `/en-sg/support/` |
| Service Status | Page: `https://status.playstation.com/en-sg` |
| Account | Page: `/en-sg/support/account/` |
| Store | Page: `/en-sg/support/store/` |
| Subscriptions | Page: `/en-sg/support/subscriptions/` |
| Games | Page: `/en-sg/support/games/` |
| Hardware | Page: `/en-sg/support/hardware/` |
| Online Safety | Page: `/en-sg/support/safety/` |

## Homepage body

| Control | Opens |
|---|---|
| Shop Black Friday / banner | Page: `/en-sg/deals/black-friday/` |
| Find out more (PS5) | Page: `/en-sg/ps5/` |
| Accessory tiles (PS5 Console, PS5 Pro, DualSense, Portal, PULSE, DualSense Edge, Access controller, covers, Media Remote, HD Camera) | Product or accessories pages under `/en-sg/` |
| New releases / Coming soon tabs | Tabs on the same page (game carousels) |
| Game cards | Page: `/en-sg/games/<slug>/` |
| PS Plus editorial links | Page: `/en-sg/ps-plus/` and `/en-sg/editorial/` |
| Blog cards | External: `https://blog.playstation.com/` (not captured as a package surface) |
| See all deals | Page: `https://store.playstation.com/pages/deals` |
| Load More | Expands the news list on the same page |
| Social icons (Twitter, Facebook, Instagram, YouTube) | External profiles (not captured) |

## Footer

| Control | Opens |
|---|---|
| About / About us | Page: `/en-sg/corporate/about-us/` |
| Careers | Page: `/en-sg/corporate/playstation-careers/` |
| PlayStation Studios | Page: `/en-sg/corporate/playstation-studios/` |
| PlayStation Productions | Page: `/en-sg/playstation-productions/` |
| Corporate | External: `https://www.sie.com/` |
| History of PlayStation | Page: `/playstation-history/1994-ps-one/` |
| PS5, PS4, PS VR2, PS Plus, Accessories, Games | Same pages as the header menus |
| Accessibility | Page: `/en-sg/accessibility/` |
| Online safety | Page: `/en-sg/privacy-security-safety/` |
| Diversity, equity and inclusion | External: `https://www.sie.com/en/csr/diversity.html` |
| Support hub and topic links | Support pages listed in the Support menu, plus `/en-sg/support/connectivity/` and `/en-sg/support/important-notice/` |
| Status | `https://status.playstation.com` |
| PlayStation Repairs | `https://www.playstation.com/repairs` |
| Password reset | Auth-adjacent wall: `/en-sg/support/account/password-reset/` (not filled) |
| Refund Request | Page: `/en-sg/support/store/ps-store-refund-request/` (form not submitted) |
| Terms of service, cancellation policy, age ratings, health warning | Legal / support pages under `/en-sg/legal/` and `/en-sg/support/account/` |
| Developers | External: `https://partners.playstation.net/` |
| Official licensing programme | `/official-licensing-program/` |
| PlayStation App store badges | App Store and Google Play (not captured) |
| Beta Program | `/en-sg/beta-program-at-playstation/` |
| Legal, privacy, terms, cookies | `/en-sg/legal/` and children |
| Site map | `/en-sg/site-map/` (93 links) |
| Country (Singapore) | Region picker (dialog). Not changed |
| Settings | Cookie preference dialog (OneTrust). Not submitted |

## Store (store.playstation.com, en-sg)

Public merchandising pages load signed out. Sign In on the store uses the same Sony account wall and stops.

| Control | Opens |
|---|---|
| Latest | Page: `/en-sg/pages/latest` |
| Collections | Page: `/en-sg/pages/collections` (or equivalent browse) |
| Deals | Page: `/en-sg/pages/deals` |
| Subscriptions | PS Plus marketing or store subscriptions page |
| Browse | Category menu or page |
| Product card | Product detail page on the store |
| Search | Search field. Not submitted |
| Sign In | Auth wall: Sony account sign-in |

## Sitemap pages not in the header

These are public pages linked from `/en-sg/site-map/` and the footer. Capture visits the ones that load without an auth wall: PS4, PS4 Pro, PS VR, PS VR2, PlayStation Network, about the store, game franchise landings (God of War, Gran Turismo, Horizon, Uncharted), manuals, environment, accessibility.

| Control | Opens |
|---|---|
| Get email updates | `/en-sg/email-sign-up/` newsletter wall. Not filled. Branch stops |
| 2-Step verification | `/en-sg/playstation-network/two-step-verification/` marketing page if public; account setup stops |
