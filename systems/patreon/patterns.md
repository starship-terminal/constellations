# Patreon patterns

How the public pages combine. Values are tokens from [tokens.json](tokens.json). Component sizes are in [components.md](components.md). The control map is [site-tree.md](site-tree.md).

## Marketing hero

The pricing and homepage hero is a full-bleed photograph with a white PATREON wordmark, a large white headline, and a header of text links plus pills. Creators, Features, Pricing, and Resources are text. Updates is an outlined pill. Find a Creator is a search pill. Log in is an outlined pill. Get Started is a white pill, about 114×47, radius 30px, Oracle 13.5px weight 350. The page ground behind the photo is photography, not `light.page`. See [pricing-light-default](screenshots/pricing-light-default.png) and [marketing-light-full](screenshots/marketing-light-full.png).

## Explore

A narrow left rail (logo, search, chats, notifications, create, more) sits on `light.page` (#f9f9f9). The main column is a white card. Search is a long pill with placeholder "Search creators or topics". Topic chips are pills; selected All is black with white text. Creator cards are photo tiles with a name and a category line. Topic tiles below are coloured photography cards, about 243×84, radius 12px. See [explore-light-default](screenshots/explore-light-default.png).

## Creator membership

The creator header keeps the app rail and adds the creator avatar, name, tabs, a search icon, Join for free, and Log in. Tabs are text with an underline on the current tab. Join for free is a filled pill, 116×40, radius 9999px, fill rgb(175, 2, 16), recorded as `light.accent`. Tier cards use the same fill at radius 8px for Join. The annual switch was visible and not toggled. See [creator-membership-light-default](screenshots/creator-membership-light-default.png).

## Help Center

`support.patreon.com` is a separate Zendesk page, not the app rail. Its search was focused. The word "payout" was typed and not submitted. Log in on that host goes to the Patreon login wall and was not followed. See [help-light-search-focused](screenshots/help-light-search-focused.png).

## Phone sheet

At 390 the marketing header collapses to the wordmark and Open menu. The sheet is a black panel: Creators, Features, Pricing, Resources, an outlined Updates pill, a full-width white Get Started pill, and store badges. Store badges were not clicked. See [mobile-marketing-light-nav-sheet](screenshots/mobile-marketing-light-nav-sheet.png).

The logged-out app's phone navigation sheet was mapped in [site-tree.md](site-tree.md) and is not in this screenshot set. Later loads of `/` served marketing.

## Coverage

| Pattern | Screens | Missing |
|---|---|---|
| Marketing hero | [pricing-light-default](screenshots/pricing-light-default.png), [marketing-light-full](screenshots/marketing-light-full.png) | Creators hover menu screenshot |
| Explore | [explore-light-default](screenshots/explore-light-default.png), [explore-light-search-typed](screenshots/explore-light-search-typed.png) | Confirmed topic filter |
| Creator membership | [creator-membership-light-default](screenshots/creator-membership-light-default.png) | Checkout after Join |
| Help Center | [help-light-default](screenshots/help-light-default.png), [help-light-search-focused](screenshots/help-light-search-focused.png) | Submitted search, contact form |
| Phone marketing sheet | [mobile-marketing-light-nav-sheet](screenshots/mobile-marketing-light-nav-sheet.png) | App phone sheet, dark appearance |
| Walls | [site-tree.md](site-tree.md) | Login and signup screenshots, by design |
