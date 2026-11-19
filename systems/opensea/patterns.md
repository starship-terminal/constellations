# Patterns

Signed-out opensea.io, dark, measured 2026-11-19. The screenshots named here are reconstructions.

## Home

A 48px banner (`#0c0c0c`, padding `6px 12px`) sits above a 64px nav. The wordmark is a 30px circle in `#0086ff`. Nav items are 32px pills. The selected one is `#161616`. At 1440, Sign in is a transparent pill. At 390, the same control is a `#0086ff` pill and the nav is 68px with a menu icon instead of the wordmark.

Below the nav, category links (All, Memes, Trading Cards, Art, PFPs, Photography, Gaming) are 16px text, not pills, in a row that starts 24px from the left. Collection titles are 32px / 48px, weight 500. Stat labels (FLOOR PRICE, TOTAL VOLUME, LISTED) are 12px gtAmericaMono. Percent changes use the same mono at 14px: `#47bb64` up, `#e24756` down.

The footer is a 32px bar, `#080808`, 1px `#202020`, with Platform Terms, Wallet & Onramp Terms, and Privacy Policy.

[screenshots/home-dark-default.png](screenshots/home-dark-default.png) and [screenshots/home-dark-phone.png](screenshots/home-dark-phone.png).

## Collection

`/collection/cryptopunks` keeps the same banner and nav. The visible title is a 32px / 500 span (the `h1` itself computed at 16px). A chain label (ETHEREUM) sits beside a 63px avatar at radius 4px. Tabs are 56px text items. Status filters are 28px pills. Search is a 32px pill. Item media is a 257px square on `#161616`. Buy Now is a 49px `#0086ff` bar with square corners. It was not pressed.

## Activity and discover

`/activity` and `/discover/art` use the same shell. Activity filters (All, Sale, Mint, Transfer) are the 28px pill pair, selected `#161616` / `#2c2c2c`. Events are links to `/item/...` and `/collection/...`, not a table. Discover repeats the home category row.

## Drops and tools

`/drops` titles the page at 24px / 500 / 30px and uses Live & Upcoming / Past as 32px pills. Mint labels are 12px mono. `/tools` is a marketing hero: 60px / 63px, weight 500, letter-spacing `-1.5px`, "Equip your AI agents", with a BETA label in 16px text. Category counts sit under it. Neither page asked for a wallet.

## Connect dialog

Sign in opens a 480px dialog, radius 12px, on a 60% black overlay. The title is 24px / 500. Email is a 56px field. Google and Apple are 48px, radius 12px, side by side. Wallet rows stack in a 12px list. The legal line is 12px `#acacac`. Escape closes it. No row was chosen.

[screenshots/signin-dark-dialog.png](screenshots/signin-dark-dialog.png).

## What sits behind the dialog

`/rewards` and `/settings/customize` both redirected to the same connect dialog. The More menu lists Drops, Rewards, Tools, Studio, Profile, Settings, and Resources. The settings submenu lists Profile, Wallets, Agents, Notifications, Customize, Developer, Verification, Shortcuts, and Cookie preferences. Those settings URLs were not entered past the dialog.
