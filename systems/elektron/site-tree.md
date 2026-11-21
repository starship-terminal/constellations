# Elektron site tree

Public signed-out map of [https://www.elektron.se/](https://www.elektron.se/), read on 2026-11-21 in headless Chromium. No sitemap is published (`/sitemap.xml`, `/sitemap_index.xml` and `/wp-sitemap.xml` return the site 404 page). The tree is the pages a crawler reached by following on-site links from `/`, plus the controls opened by click.

Nothing was submitted. No email, password or code was typed. Cookie dialogs were hidden or photographed, never accepted. Identity providers were not clicked. The signed-in app is out of scope.

Opened states are in [screenshots/states/](screenshots/states/). Desktop shots are 1440 CSS px. Phone shots are 390 CSS px.

## How a control opens something

| Control | Where | Opens | Stopped |
|---|---|---|---|
| Catalog | Header, and the phone menu | [/explore](https://www.elektron.se/explore) | |
| Shop | Header, phone menu, footer | [/shop](https://www.elektron.se/shop) | |
| Kulture | Header, phone menu | [/kulture](https://www.elektron.se/kulture) | |
| Support | Header, phone menu, footer | [/support-downloads](https://www.elektron.se/support-downloads) | |
| Wordmark | Header center, footer | [/](https://www.elektron.se/) | |
| Search | Header link `#id-1104c661-e6ef-4fcd-9f92-162373951988` | Search bar under the header. Placeholder "Type and press enter to search". Not submitted. | [desktop-home-search](screenshots/states/desktop-home-search.png) |
| Search field | Phone menu, after the menu icon | Same search field, focused, empty. Not submitted. | [phone-search-focused](screenshots/states/phone-search-focused.png) |
| Account | Header link `#id-48ecf5ed-59f0-4e2e-a3a5-1aa752af779f` | Right drawer: Log in, Create New Account | [desktop-home-account](screenshots/states/desktop-home-account.png) |
| Log in row | Inside the Account drawer (accordion) | Empty Email field and SEND ME A CODE. Password fields exist in the DOM (`username`, `password`, `remember[]`) and were not shown in this open. Nothing typed. | [desktop-account-login-form](screenshots/states/desktop-account-login-form.png) |
| Create New Account | Account drawer row | Not expanded. The DOM holds an unfilled form (`first_name`, `last_name`, `email`). Not filled. | |
| Account | Phone menu | Login card: empty Email, empty Password, Remember Me, LOGIN, Forgot your password?, CREATE NEW ACCOUNT. Nothing typed. | [phone-account](screenshots/states/phone-account.png) |
| Cart | Header link to `/cart` | Does not navigate. Opens the empty cart drawer: "Your cart is empty." and CONTINUE SHOPPING (not clicked). | [desktop-cart-opened](screenshots/states/desktop-cart-opened.png) |
| Cart icon | Phone header | Same empty cart drawer, full screen. Close is the X. | [phone-cart](screenshots/states/phone-cart.png) |
| Direct `/cart` | URL | Redirects to `/shop`. | |
| Menu icon | Phone header, `a[href="#menu-trigger"]` | Full-screen menu: Search, Catalog, Shop, Kulture, Support, Account | [phone-home-menu](screenshots/states/phone-home-menu.png) |
| Region | Footer | Select Region list. Not followed. | [desktop-home-region](screenshots/states/desktop-home-region.png) |
| Cookie dialog | On load, `#thedock-cookie-banner` | Accept All, Reject All, Cookie settings, Privacy policy. Hidden, never clicked. | [desktop-home-cookie](screenshots/states/desktop-home-cookie.png), [phone-home-cookie](screenshots/states/phone-home-cookie.png) |
| Cookie settings | Link inside the banner, and footer `#thedock-cookie-preferences` | Right panel: Necessary (always active), Preferences, Statistics, Marketing, each with Off/On. Save Settings, Reject All, Accept All. None clicked. | [desktop-cookie-settings](screenshots/states/desktop-cookie-settings.png) |
| Withdraw Purchase | Footer `#elektron-withdrawal` | In-page withdrawal form (category, name, order, items, comment). Not filled, not submitted. | |
| Skip to content | First focusable link | `#main-content` | |

Region links, present in the footer picker, were not followed:

| Label | Href |
|---|---|
| Canada | `?locale=cad` |
| Europe | `?locale=eur` |
| Norway | `?locale=nok` |
| Switzerland | `?locale=chf` |
| Sweden | `?locale=sek` |
| United Kingdom | `?locale=gbp` |
| United States | `?locale=usd` |
| Japan | `?locale=jpy` |
| Rest of the world | `?locale=usd` |

No language switcher was found. `<html lang>` is `en-US`. Region changes currency, not language.

## Chrome on every page

Header, left to right: Catalog, Shop, Kulture, Search, wordmark, Support, Account, Cart.

Footer resources: Shop, Support, Press, Store Locator, Elektronauts (external). Company: About Us, Work With Us (external), Contact Us, Withdraw Purchase. Legal: Terms & Conditions, Privacy, Cookie settings, Region. Social: YouTube, X, Instagram, Facebook. A newsletter sentence is on the page. The signup form was not filled.

## Sections


### Home

https://www.elektron.se/ — "We Are Elektron | Drum Machines, Samplers & Synths". H1: Introducing Outbox 8.

In-page controls, besides the chrome:

- FIND OUT MORE opens `/explore/outbox-8`.
- WATCH OUTBOX 8 opens a YouTube URL. Not followed.
- News cards: FIND OUT MORE opens an Elektronauts news URL (not followed) or a `/support-downloads/<product>` page. DOWNLOAD opens a `/media/...zip` or a support page. Zips were not downloaded.
- Product cards (Digitone II, Digitakt II, Syntakt, lids, cables, bags, sound packs) open `/product/<slug>`.
- Story cards open YouTube. Not followed.

[desktop-home-default](screenshots/states/desktop-home-default.png), [phone-home-default](screenshots/states/phone-home-default.png)

### Catalog

https://www.elektron.se/explore — instrument index. Each card opens an explore article. Overbridge and Legacy are sibling pages, linked from this index.

| Control | Opens |
|---|---|
| analog-four-mkii | `/explore/analog-four-mkii` |
| analog-heat-fx | `/explore/analog-heat-fx` |
| analog-rytm-mkii | `/explore/analog-rytm-mkii` |
| digitakt-ii | `/explore/digitakt-ii` |
| digitone-ii | `/explore/digitone-ii` |
| modelcycles | `/explore/modelcycles` |
| modelsamples | `/explore/modelsamples` |
| octatrack-mkii | `/explore/octatrack-mkii` |
| outbox-8 | `/explore/outbox-8` |
| syntakt | `/explore/syntakt` |
| tonverk | `/explore/tonverk` |
| Overbridge | `/overbridge` |
| Legacy | `/legacy` |

[desktop-explore](screenshots/states/desktop-explore.png)

### Shop

https://www.elektron.se/shop — category rail, then product cards. A category link filters the same shop template. A product card opens `/product/<slug>`. ADD TO CART and OUT OF STOCK - NOTIFY ME were not clicked.

| Control | Opens |
|---|---|
| Featured | `/shop` |
| Instruments & Tools | `/shop/instruments` |
| Sound Packs | `/shop/soundpacks` |
| Cables | `/shop/cables` |
| Bags & Protection | `/shop/bags-protection` |
| Merch & Music | `/shop/merch` |
| Add-ons | `/shop/add-ons` |

[desktop-shop](screenshots/states/desktop-shop.png), [phone-shop](screenshots/states/phone-shop.png)

### Product pages

Template: gallery, title, price, EXPLORE `<name>` (opens `/explore/<slug>`), ADD TO CART or OUT OF STOCK - NOTIFY ME (not clicked), Key Features accordion, Full specifications accordion.

Key Features was opened on Digitakt II. It expands a list in place. Full specifications is the same accordion pattern and was left closed.

[desktop-pdp-digitakt](screenshots/states/desktop-pdp-digitakt.png), [phone-pdp-digitakt](screenshots/states/phone-pdp-digitakt.png)

Phone Key Features open: [phone-pdp-features](screenshots/states/phone-pdp-features.png). Desktop open: [desktop-pdp-digitakt-toggle](screenshots/states/desktop-pdp-digitakt-toggle.png).

Visited 31 product URLs. Further product cards use the same template and were not all opened.

- `/product/2323`
- `/product/5-pin-midi-cable`
- `/product/amby`
- `/product/button-cap-kit-smooth-surface`
- `/product/cv-patch-cable-6-35mm-to-3-5mm`
- `/product/digitakt-ii`
- `/product/digitone-ii`
- `/product/ecc-7-carry-bag`
- `/product/gutnishy-islands`
- `/product/long-sleeve-shirt-ekta`
- `/product/long-sleeve-shirt-tetsunori`
- `/product/mega-mechs`
- `/product/outbox-8`
- `/product/overhub-ii`
- `/product/pl-2-protective-lid`
- `/product/pl-2s-protective-lid`
- `/product/pl-3-protective-lid`
- `/product/pl-5-protective-lid`
- `/product/revidden`
- `/product/rhizomorphosis`
- `/product/sender-by-jogging-house`
- `/product/shapes-memory`
- `/product/super-glue`
- `/product/syntakt`
- `/product/t-shirt-degrader`
- `/product/tonverk`
- `/product/twin-balanced-audio-cable`
- `/product/twinshot`
- `/product/usb-c-to-usb-b`
- `/product/usb-c-to-usb-c`
- `/product/viscous-circle`

### Kulture

https://www.elektron.se/kulture — story index. Each card opens `/kulture/<slug>`. Story pages link out to YouTube. Those were not followed.

[desktop-kulture](screenshots/states/desktop-kulture.png)

Visited 12 story pages plus the index. Further stories use the same template.

- `/kulture`
- `/kulture/andreas-tilliander`
- `/kulture/baseck`
- `/kulture/drum-lace`
- `/kulture/dungeon-acid`
- `/kulture/ekta`
- `/kulture/in-flames`
- `/kulture/intonal-festival-elektron-super-sekvens-26`
- `/kulture/matt-mcjunkins`
- `/kulture/mythologen`
- `/kulture/roger-odonnell-the-cure`
- `/kulture/the-field`
- `/kulture/thom-yorke`

### Support and downloads

https://www.elektron.se/support-downloads — "Pick subject" is a native `<select>`. Clicking it did not paint an open list in headless Chromium, so the option labels are Not captured. Subject cards and the select navigate to `/support-downloads/<slug>`.

A subject page lists update rows (title, date, release-note link, a download link to `/media/...zip` or a PDF). Rows were not downloaded. Digitakt II OS 1.17 was expanded in place.

[desktop-support](screenshots/states/desktop-support.png)

Subject page: [desktop-support-digitakt](screenshots/states/desktop-support-digitakt.png). Row open: [desktop-support-digitakt-open](screenshots/states/desktop-support-digitakt-open.png).

Contact Support on this index opens `/my-account/contact-support`, which redirects to the login wall. Stopped. Not entered.

Visited subject pages:

- `/support-downloads`
- `/support-downloads/analog-four-mkii`
- `/support-downloads/syntakt`
- `/support-downloads/tonverk`

Linked subject pages with the same template, not each opened:

- `/support-downloads/accessories`
- `/support-downloads/analog-drive`
- `/support-downloads/analog-four-mki`
- `/support-downloads/analog-heat-fx`
- `/support-downloads/analog-heat-mki`
- `/support-downloads/analog-heat-mkii`
- `/support-downloads/analog-keys`
- `/support-downloads/analog-rytm-mki`
- `/support-downloads/analog-rytm-mkii`
- `/support-downloads/digitakt`
- `/support-downloads/digitakt-ii`
- `/support-downloads/digitone`
- `/support-downloads/digitone-ii`
- `/support-downloads/digitone-keys`
- `/support-downloads/machinedrum`
- `/support-downloads/machinedrum-uw`
- `/support-downloads/modelcycles`
- `/support-downloads/modelsamples`
- `/support-downloads/monomachine`
- `/support-downloads/octatrack-mki`
- `/support-downloads/octatrack-mkii`
- `/support-downloads/outbox-8`
- `/support-downloads/overbridge`
- `/support-downloads/sidstation`
- `/support-downloads/sound-packs`
- `/support-downloads/transfer`

Freshworks article links (`/support/solutions/articles/...`) appear on some subject pages. They were not followed. `/customer/tickets` is a login wall and was not entered.

### Press, about, contact, locator

| Page | What the controls do | Shot |
|---|---|---|
| `/press` | Kit download links (`/media/...zip`). Not downloaded. | [desktop-press](screenshots/states/desktop-press.png) |
| `/who-we-are` | Long article. No extra in-page tabs. | [desktop-about](screenshots/states/desktop-about.png) |
| `/contact-us` | CONTACT SUPPORT opens `/my-account/contact-support` (login wall, stopped). Contact info form (category, name, and further fields) was not filled and not submitted. | [desktop-contact](screenshots/states/desktop-contact.png) |
| `/store-locator` | Map. Search was not submitted. | [desktop-locator](screenshots/states/desktop-locator.png) |
| `/overbridge` | Product article linked from Catalog. | [desktop-overbridge](screenshots/states/desktop-overbridge.png) |
| `/legacy` | Older instruments, linked from Catalog. | [desktop-legacy](screenshots/states/desktop-legacy.png) |
| `/terms-conditions` | Legal article. | [desktop-terms](screenshots/states/desktop-terms.png) |
| `/privacy-policy` | Legal article. Footer Privacy link. | |

### Login walls

Stopped at the empty wall. See [login-review.json](login-review.json).

| URL | What happened |
|---|---|
| `/login` | Stays on `/login`. Visible: empty Email, SEND ME A CODE, CREATE NEW ACCOUNT. Code path not used. |
| `/my-account` | Redirects to `/login?redirect_to=https://www.elektron.se/my-account`. Same wall. |
| `/lost-password` | Redirects to `/login`. |
| `/my-account/contact-support` | Linked as Contact Support. Not entered. |
| Forgot your password? | Drawer link to `https://elektron.se/lost-password`, which redirects to `/login`. Not followed past the wall. |

No Google, Apple, Facebook, Microsoft, GitHub or SSO button was on the wall.

[desktop-login-wall](screenshots/states/desktop-login-wall.png), [phone-login-wall](screenshots/states/phone-login-wall.png)

## External links, not followed

| Host | Where it appears |
|---|---|
| youtube.com, youtu.be | Home and Kulture watch cards |
| elektronauts.com | Footer Elektronauts, home news cards |
| careers.elektron.se | Footer Work With Us |
| youtube.com/channel, x.com, instagram.com, facebook.com | Footer social |

## Not opened

- Checkout, add to cart, notify-me, and any POST.
- File downloads (`.zip`, `.pdf`, `.dmg`).
- The support subject `<select>` list (headless click did not paint it). Option labels: Not captured.
- Create New Account expansion in the desktop drawer.
- A submitted search.
- Every remaining `/product/` and `/kulture/` card. The templates above cover them.
- Freshworks `/support/solutions/articles/` pages.
- Region locale query changes.

Crawl: 80 URLs opened, 4559 control edges recorded. Date: 2026-11-21T01:40:06.759Z.
