# OpenSea public site tree

Walked signed out on 2026-11-21 from [https://opensea.io/](https://opensea.io/) (HTTP 200, title "OpenSea, exchange everything — token trading and NFT marketplace"). Desktop viewport 1440 x 900. Incognito preview tab. `html` class included `dark`. No cookie banner was on screen. Query strings on the app banner are kept because they are the live href. Token hrefs that embed a contract address are named by the token, not copied.

Opened means the control was used and the result was read on screen. Linked means the href was read and the page was not opened in this pass. A prior package (2026-11-19) already names several of those destinations. This file records this pass.

## Banner

A bar above the nav. Text: "OpenSea Mobile is live: Trade everything, together."

| Control | Opens |
|---|---|
| Get the app | `https://opensea.io/app?utm_source=opensea&utm_medium=web_banner&utm_campaign=mobile_launch&utm_content=click`. Linked. |
| Scan to download | Button, `aria-expanded`. Not opened in this pass. |
| Close | Button. Dismisses the banner. Not used, so the bar stayed for the homepage shot. |

## Header, desktop

| Control | Opens |
|---|---|
| OpenSea home (logo) | `/` |
| Home | `/` |
| Explore | Button, `aria-expanded`. Keeps the URL on `/` and opens a dialog. See Explore. |
| Feed | `/feed`. Linked. |
| Activity | `/activity`. Linked. |
| More | Button, `aria-expanded`. Keeps the URL on `/` and opens a dialog. See More. |
| Search | Button. Opens an in-page search field, `aria-label` "Search OpenSea". See Search. |
| Sign in | Button. Connect wall. Branch stops there. Not opened in this pass. |
| Profile | `/profile/holdings`, `aria-label` "Profile", `aria-expanded`. Account wall. Not opened. |

## Explore

Opened from the header. URL stays `/`. Dialog rows:

| Control | Opens |
|---|---|
| Collections | `/collections` |
| Tokens | `/tokens` |
| Perps | `/perpetuals` |
| Trading Cards | `/trading-cards/all` |

Closed with Escape.

## More

Opened from the header. URL stays `/`.

| Control | Opens |
|---|---|
| Drops | `/drops` |
| Rewards | `/rewards`. Prior capture: this bounced to the connect dialog. Not opened in this pass. |
| Tools | `/tools`. The row also says Beta. |
| Studio | `/studio`. Linked. |
| Profile | Submenu. See Profile. |
| Settings | Submenu. See Settings. |
| Resources | Submenu. See Resources. |

### Profile

Account routes. Not opened. A signed-out visit is a wall.

| Control | Opens |
|---|---|
| Galleries | `/profile/galleries` |
| Items | `/profile/holdings` |
| Tokens | `/profile/tokens` |
| Portfolio | `/profile/portfolio` |
| Listings | `/profile/listings` |
| Offers | `/profile/offers` |
| Created | `/profile/created` |
| Watchlist | `/profile/watchlist` |
| Favorites | `/profile/favorites` |
| Activity | `/profile/activity` |

### Settings

Account routes plus two in-page controls. The routes were not opened.

| Control | Opens |
|---|---|
| Profile | `/settings/profile` |
| Wallets | `/settings/wallet-linking` |
| Agents | `/settings/agents` |
| Notifications | `/settings/notifications` |
| Customize | `/settings/customize` |
| Developer | `/settings/developer` |
| Verification | `/settings/verification` |
| Shortcuts | In-page dialog, same URL. Public keyboard list. Close is a Close button, and Escape closes it. |
| Cookie preferences | Button. Not opened. Consent was not posted. |

Shortcuts text, read and not submitted: Discover `G then D` or `G then H`, Stats `G then S`, Activity `G then A`, Rewards `G then R` or `G then L`, Profile `G then P`, Toggle Collector / Pro Mode `T then M`, Toggle Currency `T then C`, Copy page content for agents `C then A`, Search `/` or `⌘ then K`, Shortcut help `?`, Previous item `J` or left arrow, Next item `K` or right arrow, Exit item page `ESC`.

### Resources

| Control | Opens |
|---|---|
| Learn | `https://opensea.io/learn` |
| Help Center | `https://support.opensea.io/` |
| Blog | `https://opensea.io/blog` |
| Careers | `/careers` |
| About | `/about-opensea` |
| Tax Resources | `https://opensea.io/tax-resources` |
| Discord | `https://discord.gg/opensea` |
| Dev Docs | `https://docs.opensea.io/reference/api-overview` |
| Support | Button. Not opened from this submenu. |

## Search

The Search button opens an input labelled "Search OpenSea" on the same URL. Typing `azuki` (not submitted, Enter not pressed) opened a listbox.

| Control | Result |
|---|---|
| All | Filter chip inside the listbox. Not used. |
| Azuki | `/collection/azuki`. Listed as COLLECTION, 10K ITEMS. Linked, not opened from the listbox. |
| MORE RESULTS (9) | Button. Not used. |
| Trending collections, tokens, perpetuals | Public links in the same listbox. Not opened. |

The listbox also showed "Something went wrong. An error occurred. Try refreshing the page." beside the trending rows. Escape closed the field. The typed query was not submitted as a form.

## Discover bar

URL stays `/` unless noted. These sit under the header.

| Control | Opens |
|---|---|
| All | `/` |
| Memes | `/discover/memes`, plus a switch button with the same label. The link is the navigation. |
| Trading Cards | `/discover/trading-cards`. Also a switch. Clicking the link left `/` and opened the collectibles intro dialog. See that dialog. |
| Art | `/discover/art` |
| PFPs | `/discover/pfps` |
| Photography | `/discover/photography` |
| Gaming | `/discover/gaming` |
| All chains | Menu, same URL. See chains. |
| NFTs | Switch. Stays on the page. Not a navigation. |
| Tokens | Switch. Stays on the page. |
| Perps | Switch. Stays on the page. |
| 1d | Menu, same URL. See time range. |
| Toggle table view | Button. Stays on the page. |
| Collapse Stats | Button. Stays on the page. |

### All chains

A menu. Each row is a link. Opened and closed with Escape. Not followed.

`/` (All chains), `/discover/chain/ethereum`, `/discover/chain/solana`, `/discover/chain/base`, `/discover/chain/arc`, `/discover/chain/arbitrum`, `/discover/chain/hyperevm`, `/discover/chain/optimism`, `/discover/chain/abstract`, `/discover/chain/monad`, `/discover/chain/ink`, `/discover/chain/polygon`, `/discover/chain/ape_chain`, `/discover/chain/megaeth`, `/discover/chain/robinhood`, `/discover/chain/elysium`, `/discover/chain/soneium`, `/discover/chain/somnia`, `/collection/gate-0/overview` (AnimeChain), `/discover/chain/avalanche`, `/discover/chain/bera_chain`, `/discover/chain/flow`, `/collections?chains=gunzilla` (GUNZ), `/discover/chain/ronin`, `/discover/chain/sei`, `/discover/chain/shape`, `/discover/chain/unichain`, `/discover/chain/zora`.

### Time range

A menu of buttons. URL stays. Opened and closed with Escape. Options: All, 30d, 7d, 1d, 1h, 15m, 5m, 1m. 1d was already selected. No other option was chosen.

## Collectibles intro

Clicking Trading Cards navigated to `/discover/trading-cards` and opened a dialog, "An improved collectibles experience is coming to OpenSea". Five steps. Continue, Back, and Go to step 1 through 5 were visible. `@opensea` links to `https://x.com/opensea`. Continue was not clicked. Escape closed the dialog. The page stayed on `/discover/trading-cards`.

## Homepage body

URL stays `/`. Carousel cards are links. Previous, Next, and Go to slide 1 through 6 move the carousel and stay on `/`.

Examples read on this pass, not all opened: `/collection/sections-by-grant-yun`, Kinetiq Governance Token (a `/token/hyperevm/` href; the contract address is not copied here), `/collection/argonauts`, `/collection/azuki`, `/collection/cryptopunks`, `/collection/yield-field-deeds`.

Trending Tokens rows link to `/token/...`. Recent Signals names public handles and token tickers. Those rows were not opened. No account chrome was on the page.

## Footer

Pinned to the bottom of the viewport.

| Control | Opens |
|---|---|
| Platform Terms | `/tos` |
| Wallet & Onramp Terms | `/tosw` |
| Privacy Policy | `/privacy` |
| Discord | `https://discord.gg/opensea` |
| Reddit | `https://reddit.com/r/opensea` |
| Telegram | `https://t.me/officialopensea` |
| X | `https://x.com/opensea` |
| Instagram | `https://instagram.com/opensea` |
| ETH price. Switch native currency | Button. One click switched the label from ETH to SOL and the displayed price. Not a page. |
| Support | Button. A click did not open a menu or leave the page. |
| Light, Dark, System | Buttons. Dark was the live theme. Light and System were not clicked, so the theme was not changed during the walk. |
| Collector, Pro | Buttons. Mode switch. Not clicked. |
| Crypto, USD | Buttons. Currency display. Not clicked. |
| Sound volume: low | Button. Not clicked. |

## Header, phone (390)

The bar collapses. Photographed in [mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png).

| Control | Opens |
|---|---|
| Menu (hamburger, `aria-expanded`) | Full-screen dialog on the same URL. See phone menu. Close is the X. |
| OpenSea home | `/` |
| Search | Button. Same search field as desktop. Not opened at 390 in this pass. |
| Sign in | Button. Filled blue pill. Connect wall. Not opened at 390. |

Category chips scroll sideways: All, Memes, Trading Cards, Art, and the rest of the desktop set.

### Phone menu

Opened from the hamburger. URL stays `/`. Photographed in [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png).

| Control | Opens |
|---|---|
| Discover | `/` |
| Collections | `/collections` |
| Tokens | `/tokens` |
| Perpetuals | `/perpetuals` |
| Swap | `/swap`. Not on the desktop header. Linked, not opened. |
| Drops | `/drops` |
| Activity | `/activity` |
| Rewards | `/rewards`. Wall. Not opened. |
| Profile | `/profile/holdings`. Wall. Not opened. |
| My Offers | `/profile/offers`. Wall. |
| Portfolio | `/profile/portfolio`. Wall. |
| Watchlist | `/profile/watchlist`. Wall. |
| Favorites | `/profile/favorites`. Wall. |
| My Activity | `/profile/activity`. Wall. |
| Profile settings | `/settings/profile`. Wall. |
| Pro mode, Light mode, Show in USD, Volume | Buttons in the drawer. Not clicked. |
| Customize | `/settings/customize`. Wall. |
| Studio | `/studio`. Linked. |
| Learn | `https://opensea.io/learn` |
| Help Center | `https://support.opensea.io/` |
| Blog | `https://opensea.io/blog` |
| Careers | `/careers` |
| Support | Button. Not opened. |
| Privacy Policy | `/privacy` |
| Your Privacy Choices | Button. Not opened. Consent was not posted. |
| Platform Terms of Service | `/tos` |
| Login | Button at the bottom of the drawer. Connect wall. Not opened. |

## Walls

Sign in on desktop was opened. It stays on `/` and shows a dialog titled "Connect with OpenSea". Visible and not used: Continue with email, Continue with Google, Continue with Apple, MetaMask, WalletConnect, Robinhood Wallet, More Wallet Options. Closed with Escape. No email, password, or code was typed. No provider or wallet was clicked. No form was submitted.

Profile, Rewards, Login, and every `/profile/` and `/settings/` href are the same wall. Those routes were not opened.
