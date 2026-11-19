# Rarible patterns

Public signed-out pages only. Measured 2026-11-19 at 1440x900 and 390x844, both at devicePixelRatio 2. The start URL `https://rarible.com/` redirected to `https://rarible.com/all`.

## App shell

A sticky bar holds an OG Rarible notice, then the wordmark, Explore / Mint / Gacha / Collectibles, search, and Login. The notice link is brand yellow. The bar background on the combined header was `rgba(10, 10, 10, 0.95)` with a 10px backdrop blur class. Footer is `#0a0a0a` with a `rgba(255,255,255,0.1)` top border, padding `12px 16px`, and links for Terms, Privacy, FAQ, and API.

At 390 the wordmark, search icon, Login, and a menu button remain. Explore, Mint, and Gacha move into a bottom sheet.

## Explore

`/all` is a chain tab row (All, Ethereum, Solana, Robinhood Chain, Polygon, More) over a horizontal hero of collections. Each hero title is Tomorrow. The action is a white "Trade Collection" button. Chain tabs use opacity, not a filled pill, to show selection.

## Collection

`/robinhood/collections/yoodles-ovens` shows the name, a truncated contract, Share, and stats (Floor Price, Top Offer, 24h Vol, All Vol, Listed / Supply, Owners). Tabs are Items, My Items, Offers, Activity. Items is a grid of 188px cards with a yellow Buy Now. Filters is a quiet pill. Sort is a field-shaped button. Buy Now was not pressed. My Items and Offers were not opened.

## Drops

`/all/drops` redirected to `/ethereum/drops`. Chain tabs repeat. "Live & Upcoming" was selected. The empty heading was "Nothing here yet..." in Tomorrow 28px. A featured VeeFriends block used the same white action button as Trade Collection.

## Search

Typing `zzzznotacollection` into the header field, without submitting a form, opened a panel. It showed Collections (0), Items (0), and "No results. NGMI." in Geist Mono 14px weight 500 at `rgba(255,255,255,0.6)`.

## Login

Login opens Privy's "Log in to Rarible" dialog. It is a vendor surface: system-ui, `#020713` panel, 24px radius. Marketplace chrome stays Geist Mono and Tomorrow. The dialog was closed. No wallet was connected and no email was submitted.

## Legal

`/terms` and `/faq` are a single column, max-width 820px. The title is Tomorrow 40px / 48px. Body is Geist Mono 14px at `rgba(255,255,255,0.8)`. FAQ questions are Tomorrow 14px weight 500 under Tomorrow 18px section labels.

## Not entered

Wallet connect, email submit, Buy Now, checkout, listing, `og.rarible.com`, and `rwa.rarible.com` were not entered.
