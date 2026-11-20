# Rarible components

Inventory of controls measured on public signed-out pages on 2026-11-19. Values are computed styles. Crops in [components/crops/](components/crops) are reconstructions drawn from those boxes, because `preview_snapshot` returned "The browser is not producing screenshot frames."

## Button

Login and Buy Now are the same control.

| State | Reading |
|---|---|
| Default | Background `#faff00`, text `#18181b`, border `1px solid #18181b`, radius `9999px`, padding `8px 12px`, height 36px, Geist Mono 14px weight 500. Shadow `rgba(0,0,0,0.1) 0px 1px 3px, rgba(0,0,0,0.1) 0px 1px 2px -1px`. |
| Hover | Class `transition-all duration-200`. Hover colour was not held. Sheet rule `.hover:bg-brand/90:hover` exists and was not the Login class. |
| Focus | Class `focus-visible:ring-1 focus-visible:ring-ring`. A live focus ring on Login was not read. Phone sheet Close, while focused, showed `box-shadow: #0a0a0a 0 0 0 2px, #d4d4d8 0 0 0 4px`. |
| Pressed, disabled, loading | Not on the public pages. Buy Now was not pressed. |

Trade Collection is a white button on the explore hero: background `#ffffff`, text `#000000`, radius 8px, padding `8px 20px`, height 36px, weight 500. Class includes `hover:opacity-90`. Hover was not held.

## Icon button

Phone search is 24 by 24, labelled "Open search". Phone sheet Close is 24 by 24, radius 4px. Privy close is 24 by 24, background `#1a2230`, radius 9999px. That close is the login vendor, not the marketplace chrome.

## Link

Explore, Mint, and Gacha in the desktop header are Geist Mono 14px weight 400, white, no underline. The OG banner link is `#faff00`, 12px / 16px. Privy Terms and Privacy Policy links are `#fbff00`, 13px. Those two yellows differ by one channel. Both readings are kept.

## Text field

Search wrap: height 36px, width 400px, border `1px solid #27272a`, radius 6px, padding `0 8px`. Input is transparent, 14px, placeholder "Search collections and items". On focus the wrap's ring colour was `hsl(61.18 100% 50%)` (`#faff00`). The border colour stayed `#27272a`.

The Privy email field (placeholder `your@email.com`) is a separate control: background `#020713`, border `1px solid #1f2937`, radius 12px, height 56px, system-ui. Nothing was typed into it.

## Text area

Not present on the public pages.

## Select

Sort on the collection page ("Price: Low to High") is a button styled as a field: background `rgba(255,255,255,0.02)`, border `1px solid rgba(255,255,255,0.1)`, radius 6px, height 36px. It was not opened.

## Checkbox, radio, switch

Not present on the public pages. The collection page has Status and Rarity groups. Their selected state was not opened.

## Tabs

Chain tabs on `/all`: selected "All" is white at opacity 1, weight 500, padding `0 12px 16px`, height 37px. Idle "Ethereum" is the same colour at opacity 0.6. No `::after` underline was painted.

Collection tabs: "Items" has `data-state=active` and color `#ffffff`. Idle tabs are `rgba(255,255,255,0.6)`. Padding `0 0 14px`.

Drops has "Live & Upcoming" at 24px white and "Past" at 24px `rgba(255,255,255,0.6)`.

## Menu

Phone nav is a bottom sheet, not a desktop menu. Background `#0a0a0a`, width 390px, height 455px, padding 24px, radius `12px 12px 0 0`. Overlay `rgba(0,0,0,0.8)`. Links are Tomorrow 24px. Closed with Escape.

The desktop "More" chain control was not opened.

## Tooltip

Not present.

## Dialog

Login opens a Privy dialog: panel 360 by 465, background `#020713`, radius 24px, shadow `rgba(55, 65, 81, 0.15) 0px 8px 36px`. Title "Log in to Rarible". Methods shown: MetaMask, Phantom, VeeFriends Wallet, an email field with Submit, and More options. None of those were pressed. Closed with the close control.

## Toast

Sonner keyframes (`sonner-fade-in`, `sonner-fade-out`, `sonner-spin`) and one `prefers-reduced-motion` rule on `[data-sonner-toast]` are in the sheets. No toast was on screen.

## Card

Item card on the collection page: background `#09090b`, 1px border `#27272a`, radius 12px, padding 8px, 188 by 281. Title link is Geist Mono 14px. Buy Now sits on the card and was not pressed.

Explore heroes use a white Trade Collection button over artwork. The artwork is collection media, not a token.

## List row

Item title block under the card image: padding 4px, gap 4px. Not a separate list component.

## Table

Not present. Activity was a tab and was not opened.

## Avatar

Collection contract control "0x7e...d26b" is Geist Mono 14px. No avatar crop was measured.

## Badge

NEW next to Collectibles: background `#faff00`, text `#000000`, 11px weight 700, padding `2px 6px`, radius 2px, height 15px.

## Gaps

- Light theme was declared on `:root` and not shown live. There is no public theme switch.
- Button hover, pressed, disabled, and loading were not on the public pages.
- Checkbox, radio, switch, tooltip, toast, text area, and table were not on the public pages.
- Buy Now, wallet methods, email submit, and More options were not used.
- `preview_snapshot` produced no frames, so crops are reconstructions.
