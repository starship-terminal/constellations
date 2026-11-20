# MSCHF site tree

Mapped on 2026-11-21 from the public page at https://mschf.com/ in headless Chromium, viewport 1440x900. The sitemap at https://mschf.com/sitemap.xml lists only `/`. `https://www.mschf.com/` timed out (connection reset, matching an earlier probe). No account control exists on this host.

The page is one index. A fixed header holds two controls. The body is a numbered list of drop titles. Each title is an anchor. There is no in-page route, no menu, no search, and no theme switch.

## Header

| Control | Opens |
|---|---|
| SHOP↗ (header and footer) | https://store.mschf.com/ in a new context. On this host, `/shop` also redirects there. Below 500px the header shop link is `display: none`. |
| Gold square button (no accessible name) | Nothing. A click does not open a menu, a search field, or a page. |

## Store pages the header opens

These are the public pages on store.mschf.com that the index, the store header, or the store footer reach. Account login was not opened. A direct request to `/account/login` redirects to a Shopify sign-in page; that URL is recorded in [login-review.json](login-review.json) and was not screenshotted.

| Control | URL | What it is |
|---|---|---|
| SHOP↗ | https://store.mschf.com/ | Product grid. Country, search, and cart sit in the header. |
| Country/region button | same page, disclosure | Opens a country list. No country was chosen. The list paints under the header and is not in the viewport shot. |
| Search summary | same page, disclosure | Opens a search field. On desktop the modal mounts at 1px beside the cart icon, so the field is captured on the search results page instead. |
| Cart icon | https://store.mschf.com/cart | Empty cart. |
| Product tile (example) | https://store.mschf.com/products/super-normal-2 | Product page. Sold out. |
| Get notified | same product page, dialog | Email and phone fields. Nothing was typed. Submit was not clicked. |
| Search results | https://store.mschf.com/search?q=boot | Three results. Availability filter opened. Apply was not clicked. |
| Footer PRIVACY | https://store.mschf.com/policies/privacy-policy | Policy page. |
| Footer CONTACT | https://store.mschf.com/policies/contact-information | Trade name and support address. |
| Footer TERMS | https://store.mschf.com/policies/terms-of-service | Linked, not separately captured. Same shell as privacy. |
| Footer SHIPPING | https://store.mschf.com/policies/shipping-policy | Linked, not separately captured. |
| Footer REFUND | https://store.mschf.com/policies/refund-policy | Linked, not separately captured. |
| Footer MSCHF APP, STORE APP, INSTA, TIKTOK, SNAP | external app and social hosts | Left the store. Not captured. |
| Check out | not clicked | Would start checkout. |

## Index rows

Each row is a title that leaves mschf.com. 137 unique anchors. 28 go to store.mschf.com. 22 go to another host whose name contains mschf. 87 go elsewhere. None of these project sites were captured: they are separate products, not pages of this design system.

| Title | Host |
|---|---|
| THE PERSISTENCE OF CHAOS | thepersistenceofchaos.com |
| MAN EATING FOOD | www.reddit.com |
| TIMES NEWER ROMAN | timesnewerroman.com |
| NETFLIX HANGOUTS | netflixhangouts.com |
| JESUS SHOES | jesus.shoes |
| BULL & MOON | bullandmoon.com |
| PUFF THE SQUEAKY CHICKEN | www.designboom.com |
| THIS FOOT DOES NOT EXIST | thisfootdoesnotexist.com |
| ZUCKWATCH | zuckwatch.com |
| CUSS COLLAR | cusscollar.com |
| MSCHF BOX | mschfbox.com |
| ALL THE STREAMS | allthestreams.fm |
| NBA FM | nba.fm |
| BOOMER EMAIL | boomer.email |
| SEVERED SPOTS | severedspots.com |
| THE OFFICE (SLACK) | theofficeslack.com |
| MSCHF MAG VOL 1 | bread.mschfmag.com |
| SCREAM CLUB | screamclub.club |
| FINGER ON THE APP | fingeronthe.app |
| MSCHF X | mschfx.com |
| ALEXAGATE | alexagate.com |
| MSCHF MAG VOL 2 | store.mschf.com |
| MASTERWIKI | masterwiki.how |
| SPOTTING PLUTES | spottingplutes.com |
| DINO SWORDS | dinoswords.gg |
| MSCHF LATE NIGHT | mschflatenight.tv |
| CARD V CARD | cardvcard.com |
| MEDICAL BILL ART | medicalbill.art |
| WHITE WHALE | whitewhale.is |
| ANTI AD AD CLUB | antiadvertisingadvertising.club |
| MSCHF WHOLESALE | mschfwholesale.com |
| MSCHF MAG VOL 3 | store.mschf.com |
| PUSH PARTY | pushparty.app |
| BLUR USD $20 | store.mschf.com |
| DATA LOTTO | datalotto.biz |
| 1800 JINGLES | 1800jingles.com |
| WALTS KITCHEN | walts.kitchen |
| KING OF THE CLICKS | kingoftheclicks.com |
| WINGS UNLIMITED | wingsunlimited.co |
| IN THE YEAR 2024 | intheyear2024.com |
| BIRKINSTOCK | birkinstock.shoes |
| SPOTS RAMPAGE | spotsrampage.com |
| MSCHF MAG VOL 4 | store.mschf.com |
| AXE NO 5 | axenumbercensored.com |
| DEATH OF THE INFLUENCER | deathoftheinfluencer.com |
| SATAN SHOES | satan.shoes |
| EMAIL CAPSULE COLLECTION | emailcapsulecollection.com |
| COOOOOOKIES | cooooookies.com |
| FAUXMEGLE | fauxmegle.com |
| CHAIR SIMULATOR | chairsimulator.com |
| AT ALL COSTS | atallcosts.co |
| BOOSTED PACKS | one.boostedpacks.com |
| DEAD STARTUP TOYS | deadstartuptoys.com |
| MSCHF MAIL ORDER CATALOG | mschfmailorder.com |
| KILL PILL | killpill.health |
| STOLEN STORIES | stolenstories.com |
| MSCHF FAMOUS MOUSE | mschfxfamousmouse.com |
| GUNS 2 SWORDS | guns2swords.com |
| SUNDAY SERVICE | mschfsundayservice.com |
| BOOSTED PACKS V2 | two.boostedpacks.com |
| 8TWELVE | findmschf.com |
| MSCHF MAG VOL 5 | bam.mschfmag.com |
| MUSEUM OF FORGERIES | moforgeries.org |
| DUNK DOT BIZ | dunk.biz |
| ILLEGAL CHIPS | illegalchips.com |
| BOOSTED PACKS V3 | three.boostedpacks.com |
| FELLOWSHIP PROGRAM | apply.mschffellowship.com |
| TONTINE | tontine.cash |
| ONLYBAGS | onlybags.biz |
| BLUR WON | store.mschf.com |
| C&D GRAND PRIX | cdgrandprix.com |
| HEART 2 ELECTRIC BOOGALOO | heart2electricboogaloo.com |
| M-SAT | mschfboard.org |
| BLUR UAE | store.mschf.com |
| CHILDRENS CRUSADE | childrenscrusade.com |
| VINYL BLADE | vinylblade.com |
| MSCHF MAG VOL 6 | store.mschf.com |
| BOOSTED PACKS V4 | four.boostedpacks.com |
| MSCHF X TIFFANY | ultimateparticipationtrophy.com |
| SACRED SELTZER | sacredseltzer.com |
| BLUR AUD | store.mschf.com |
| MSCHF WHOLESALE | hats.mschfwholesale.com |
| SCRATCH & SNIFF LOTTO | scratchandsnifflotto.com |
| EAT THE RICH POPSICLES | eattherichpopsicles.com |
| BLUR MONOPOLY | store.mschf.com |
| GOBSTOMPER | store.mschf.com |
| KETCHUP OR MAKEUP | ketchupormakeup.com |
| KEY4ALL | key4all.com |
| AC.1 | store.mschf.com |
| NO MORE TEARS I'M LOVIN IT | leaflet.perrotin.com |
| MADE IN ITALY | store.mschf.com |
| BLUR USD $100 | store.mschf.com |
| MSCHF BIG FRUIT LOOP | bigfruitloop.com |
| SMELLS LIKE WD-40 | store.mschf.com |
| SUPER NORMAL 2 | store.mschf.com |
| BIG RED BOOT | store.mschf.com |
| MSCHF MAG 360 | store.mschf.com |
| TAX HEAVEN 3000 | taxheaven3000.com |
| HOT CHAT 3000 | hotchat3000.com |
| ANTI ROBO CALL | antirobocall.com |
| PYRAMID CHAT | pyramid.chat |
| THE FREE MOVIE | thefreemovie.buzz |
| REEBOK PUMP | store.mschf.com |
| MSCHF X DAELIM | www.perrotin.com |
| SUPER BABY | store.mschf.com |
| SMELLS LIKE FABULOSO | store.mschf.com |
| ASCII THEATER | ascii.theater |
| RAT CHAT | ratchat.chat |
| GLOBAL SUPPLY CHAIN TELEPHONE HANDBAG GLOBAL SUPPLY CHAIN TELEPHONE HANDBAG GLOBAL SUPPLY CHAIN TELEPHONE HANDBAG GLOBAL SUPPLY CHAIN TELEPH | globalsupplychaintelephone.com |
| MSCHF GRIFT CARD | store.mschf.com |
| 2×4 | store.mschf.com |
| ART 2 | art2.mschf.com |
| CANDY AIRPODS | store.mschf.com |
| MUSEUM OF FORGERIES: PICASSO | museumofforgeriespicasso.com |
| KEY BOX KEY: KEY | keyboxkey.com |
| KEY BOX KEY: BOX | keyboxkey.com |
| WAVY COLLECTION | store.mschf.com |
| MSCHF PLAYS VENMO | mschfplaysvenmo.com |
| MSCHF SCOUT COOKIES | mschfscoutcookies.com |
| MSCHF HOTELS | mschfhotels.com |
| OUR COW ANGUS | ourcowangus.com |
| NOT WHEELS | mschfnotwheels.com |
| GUFRAM X MSCHF | mschfindustryplants.com |
| UPBLOB | upblob.com |
| BWD HIGH | store.mschf.com |
| REDACT A CHAT | redact-a-chat.com |
| CLOUD TEE | cloud-tee.com |
| MSCHF MATERIAL VALUES | mschfmaterialvalues.com |
| ROCK CANDY | licktherock.com |
| 2×4 LOAFER | store.mschf.com |
| AMG X MSCHF | amgxmschf.com |
| KING SOLOMON'S BABY↗ | kingsolomonsbaby.com |
| APPLIED MSCHF | appliedmschf.com |
| GSCT | globalsupplychaintelephone.com |
| MADE BY MSCHF | www.phaidon.com |

## Not on this host

- No sign-in, account, or settings control on https://mschf.com/.
- No light theme. `color-scheme` on the index is `normal` and the page paints black.
- https://www.mschf.com/ did not load (timeout).
- The Nuxt 404 at https://mschf.com/missing-page is already in [screenshots/not-found-dark-default.png](screenshots/not-found-dark-default.png).
