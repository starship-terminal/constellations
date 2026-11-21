# Nomad Goods site tree

Mapped from the public homepage at https://nomadgoods.com/ on 2026-11-21, before screenshots. The root redirects to https://nomadgoods.com/sg/ (Singapore storefront, HTTP 200, title "NOMAD | Premium iPhone Cases, Watch Bands and Chargers"). This file records which control opens which page, menu, dialog, or interaction. Account, login, and signup branches stop at the wall. No form was submitted.

## Entry

| Control | Opens |
|---|---|
| https://nomadgoods.com/ | Redirects to https://nomadgoods.com/sg/ |
| Wordmark "Nomad" (`a[aria-label=home]`) | `/sg/` |
| Announcement "Sitewide Black Friday Savings" | `/sg/pages/black-friday-2026` |
| Promo "Shop Now" (hero and feature tiles) | Collection or product pages linked from the tile |

## Header, desktop

The bar is a rounded surface under the announcement. Text items are links. Icon items are buttons, except Account.

| Control | Kind | Opens |
|---|---|---|
| Best Sellers | link | `/sg/pages/best-sellers`. No submenu (`aria-expanded` absent). |
| Cases | link, hover submenu | Page `/sg/collections/cases`. Hover opens `submenu-gid://shopify/Metaobject/611644407856`. |
| Watch | link, hover submenu | Page `/sg/collections/bands`. Hover opens `submenu-gid://shopify/Metaobject/611642867760`. |
| Charging | link, hover submenu | Page `/sg/collections/power`. Hover opens `submenu-gid://shopify/Metaobject/611643326512`. |
| Tracking & Wallets | link, hover submenu | Page `/sg/collections/wallets`. Hover opens `submenu-gid://shopify/Metaobject/611644538928`. |
| More Gear | link, hover submenu | Page `/sg/collections/lifestyle-gear`. Hover opens `submenu-gid://shopify/Metaobject/611642834992`. |
| Sale | link | `/sg/pages/black-friday-2026`. No submenu. |
| Locale selector | button | Region menu. Not a page. |
| Notification | button | Notification panel. Badge showed 3 on the map pass. Not a page. |
| Account (`a[aria-label="Go to account page"]`) | link | **Wall.** Host `https://account.nomadgoods.com/` (a `_cs` query was present on the href). Branch stopped. Not entered. |
| Search | button | Search field on the storefront. The search page is `/sg/search` (HTTP 200). |
| Cart drawer | button | Cart drawer overlay. `/sg/cart` redirected back to `/sg/` (HTTP 200). |

## Header, phone

| Control | Kind | Opens |
|---|---|---|
| Open menu | button | Burger drawer with the same nav destinations. |
| Search, Cart drawer, Account, Notification | same as desktop | Same destinations. Account remains the account host and is not entered. |

## Menus

Each submenu is in the homepage DOM, controlled by the nav link `aria-controls`. Empty image links that repeat a destination are omitted.

### Cases

Opened by hovering the Cases nav link. The link itself goes to `/sg/collections/cases`.

| Label | Path |
|---|---|
| iPhone Cases | `/sg/collections/phone-cases` |
| iPhone 18 | `/sg/collections/iphone-18-cases` |
| iPhone Duo | `/sg/pages/iphone-duo` |
| iPhone 17 | `/sg/collections/iphone-17-cases` |
| iPhone 16 | `/sg/collections/iphone-16-cases` |
| iPhone 15 | `/sg/collections/iphone-15-cases` |
| Legacy iPhones | `/sg/collections/legacy-iphone-cases` |
| iPhone Extras | `/sg/pages/iphone-18-accessories` |
| Screen Protectors | `/sg/collections/screen-protectors` |
| MagSafe Wallets | `/sg/products/leather-mag-wallet-with-find-my-tracking-black-camino-leather` |
| Wrist Strap | `/sg/products/wrist-strap-carbide` |
| iPad Cases | `/sg/collections/ipad` |
| iPad Pro M4 & M5 | `/sg/products/leather-folio-black-ipad-pro-11-m4` |
| iPad Air M3 & M4 | `/sg/products/leather-folio-plus-brown-ipad-pro-11-inch` |
| Headphone Cases | `/sg/collections/headphone-cases` |
| AirPods Pro 3 | `/sg/products/modern-leather-case-airpods-pro-3-horween-black` |
| Airpods Pro 1 & 2 | `/sg/products/modern-leather-case-airpods-pro-2nd-gen-horween-black` |
| AirPods 4 & 5 | `/sg/products/modern-leather-case-airpods-4th-generation-brown` |
| AirPods 3 | `/sg/products/modern-leather-case-airpod-3rd-generation-black` |
| Pixel Buds Pro | `/sg/products/pixel-buds-pro-case-rustic-brown-horween-leather` |
| Pixel Buds | `/sg/products/pixel-buds-case-rustic-brown-leather` |
| Pixel Buds A Series | `/sg/products/modern-case-pixel-buds-a-rustic-brown-leather` |

### Watch

Opened by hovering the Watch nav link. The link itself goes to `/sg/collections/bands`.

| Label | Path |
|---|---|
| Apple Watch | `/sg/collections/bands` |
| Sport & Rugged Bands | `/sg/collections/waterproof-bands` |
| Metal Bands | `/sg/collections/metal-bands` |
| Leather Bands | `/sg/collections/bands-leather` |
| Charging | `/sg/collections/power-apple-watch` |
| Garmin Bands | `/sg/collections/garmin-bands` |
| Sport & Rugged Bands | `/sg/pages/garmin` |
| Charging | `/sg/products/garmin-adapter-for-usb-c-cables-black` |
| Pixel Watch | `/sg/products/active-band-pro-pixel-watch-45mm-black-silver-hardware` |
| DesignLab | `/sg/pages/design-lab/apple-watch` |

### Charging

Opened by hovering the Charging nav link. The link itself goes to `/sg/collections/power`.

| Label | Path |
|---|---|
| Cables and Adapters | `/sg/collections/cables` |
| USB-C Cables | `/sg/products/cable-usb-c-kevlar-white-1-5m` |
| USB-C Adapters | `/sg/products/ac-adapter-65w-usb-c` |
| ChargeKey | `/sg/products/chargekey-v2-silver` |
| Apple Watch Charging | `/sg/products/universal-cable-apple-watch-carbide` |
| Wireless Charging | `/sg/collections/magsafe` |
| Single Device Charging | `/sg/products/stand-one-4th-gen-stellar-orange` |
| Multi Device Charging | `/sg/products/stand-one-max-4th-gen-silver` |
| Vehicle Charging | `/sg/products/car-charger-70w-usb-c` |
| Starlink Cable | `/sg/products/starlink-cable-carbide-15m` |
| Charge Mount | `/sg/products/charge-mount-black` |

### Tracking & Wallets

Opened by hovering the Tracking & Wallets nav link. The link itself goes to `/sg/collections/wallets`.

| Label | Path |
|---|---|
| Find My Tracking | `/sg/collections/airtags` |
| Tracking Card Air | `/sg/products/tracking-card-air-v2` |
| Tracking Card Pro | `/sg/products/tracking-card-pro-stellar-orange` |
| Leather Mag Wallet | `/sg/products/leather-mag-wallet-with-find-my-tracking-black-camino-leather` |
| Wallets | `/sg/collections/wallets` |
| Bifold Wallet | `/sg/products/bifold-wallet-olde-dublin` |
| Card Wallet Plus | `/sg/products/card-wallet-plus-black` |
| Passport Wallet | `/sg/products/passport-wallet` |
| Card Wallet | `/sg/products/card-wallet-black` |
| Shell Cordovan Wallet | `/sg/products/shell-cordovan-wallet-color-8-le` |

### More Gear

Opened by hovering the More Gear nav link. The link itself goes to `/sg/collections/lifestyle-gear`.

| Label | Path |
|---|---|
| Lifestyle Gear | `/sg/collections/lifestyle-gear` |
| Rugged Keychain | `/sg/products/rugged-keychain-airtag-driftwood-v2` |
| Key Organizer | `/sg/products/orbitkey-horween-leather-rustic-brown` |
| Pen | `/sg/products/pen-titanium` |
| Pen Refill | `/sg/products/pen-refill-gel-black` |
| Wrist Strap | `/sg/products/wrist-strap-carbide` |
| Pixel | `/sg/products/active-band-pro-pixel-watch-45mm-black-silver-hardware` |
| Pixel Buds Pro | `/sg/products/pixel-buds-pro-case-rustic-brown-horween-leather` |
| Pixel Buds | `/sg/products/pixel-buds-case-rustic-brown-leather` |
| Pixel Buds A Series | `/sg/products/modern-case-pixel-buds-a-rustic-brown-leather` |
| Apparel | `/sg/products/santa-barbara-sunset-shirt-ivory-small` |

## Dialogs and overlays on the homepage

| Control | Opens | Capture rule |
|---|---|---|
| Page load | Klaviyo dialog "Sign Up to Save Even More" (`button.klaviyo-close-form`, aria-label "Close dialog") | Close with the X. Do not type an email. Do not press Sign Up. |
| Page load | Cookie banner (`.pd-cookie-banner-window` / `.cc-window`): Preferences, Accept, Decline, Learn more | Hide with CSS. Do not click Accept, Decline, or Preferences (consent POST). Learn more is `/pages/privacy`. |
| Search button | Search input, placeholder "Search our store", form action `/sg/search` | Open and type a query without submitting if the field is public. Do not submit the form. |
| Cart drawer button | Cart drawer, close control "Close cart drawer" | Open the empty drawer. Do not start checkout. |
| Locale selector | Region list | Open and record. Do not switch region if that rewrites the storefront mid-capture. |
| Notification | Notification list | Open. |
| Chat with us | Chat widget | Recorded as a control. Not opened if it asks for contact details. |
| Manage Cookies | Cookie preferences | Not clicked. Consent control. |

## Footer

| Label | Opens |
|---|---|
| Support | `/sg/pages/support` |
| Help Center | `/sg/pages/support` |
| Shipping | `/sg/pages/support` |
| Returns | `/sg/pages/returns` |
| Report Fraud | `/to/zLMBg0g5` External form. Not submitted. |
| Contact Us | `/sg/pages/support` |
| Withdraw from Contract Here | `/sg/pages/support` |
| About Us | `/sg/pages/about` |
| Sustainability | `/sg/pages/sustainability` |
| Horween Leather | `/sg/pages/horween-leather` |
| Leather Comparison | `/sg/pages/leather` |
| Press & Affiliates | `/sg/pages/press-and-affiliates` |
| Where We're Sold | `/sg/pages/where-we-are-sold` |
| Wholesale | `/sg/pages/wholesale-landing` |
| Discounted Gear | `/sg/collections/overstock-sale` |
| Become an Ambassador | `/sg/pages/ambassador` |
| The Nomadic Blog | `/sg/the-nomadic` |
| Wallpapers | `/sg/pages/wallpapers` |
| Limited Edition | `/sg/pages/limited-edition` |
| Nomad | `/sg/` |
| Nomad on Instagram | `https://www.instagram.com/nomad/` External. Not entered. |
| Nomad on Facebook | `https://www.facebook.com/nomad` External. Not entered. |
| Nomad on Twitter | `https://twitter.com/nomadgoods` External. Not entered. |
| Privacy | `/sg/pages/privacy` |
| Terms | `/sg/pages/terms` |
| Payment | `/sg/pages/payment-options` |
| Accessibility | `/sg/pages/accessibility` |

Footer also has column buttons labelled Support, About, Sales, Explore (they expand link groups) and a newsletter Submit. The newsletter field is not filled and Submit is not pressed.

## Known walls

| URL | Result |
|---|---|
| https://nomadgoods.com/sg/login | Page not found (HTTP 404). Title "Page not found \| NOMAD". Heading "Whoops! Looks like you're lost." |
| https://nomadgoods.com/account/login | Redirects to `/sg/login`, page not found. |
| https://nomadgoods.com/sg/account/login | Page not found (HTTP 404). |
| Account control on `/sg/` | Opens `https://account.nomadgoods.com/`. Host not entered. |

## Pages this capture will open

Public store and marketing pages only. One product page stands in for the product template. Collection pages stand in for the grid template. Account, checkout, newsletter, survey, and Typeform branches stop here.

- `/sg/` home, overlays listed above
- `/sg/pages/best-sellers`
- `/sg/collections/cases` and `/sg/collections/phone-cases`
- `/sg/collections/bands`
- `/sg/collections/power`
- `/sg/collections/wallets`
- one product from the Cases menu (Modern Leather Case, AirPods Pro 3, Horween black)
- `/sg/search`
- `/sg/pages/support`, `/sg/pages/about`, `/sg/pages/privacy`, `/sg/pages/black-friday-2026`
- `/sg/login` as the known 404, so the error page is evidence

Phone width uses the same pages plus the Open menu drawer.

