# YouTube patterns

How the components in [components.md](components.md) combine into YouTube's screens. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots).

## App shell and navigation

Four top-level destinations sit in a five-item tab bar at the bottom: Home, Shorts, a round Create (+) in the
middle, Subscriptions and You (the owner's avatar). The bar is a translucent material (`color.surface.tabBar`)
with a hairline on top (`color.border.tabBar`) and is `size.tabBar` tall above the home-indicator inset. The
selected tab fills its outline icon; labels stay `color.text.tab`. A red dot (`color.brand.red`) on
Subscriptions marks new videos. See [02-home-ad-shorts-shelf-tabbar](screenshots/dark/02-home-ad-shorts-shelf-tabbar.png)
and [08-you-tab-profile-history-library-chips light](screenshots/light/08-you-tab-profile-history-library-chips.png).

Home and Subscriptions open with a header: the logo at the left, then Cast or Inbox, Notifications and Search as
bare outline icons at the right. The You tab swaps the logo for an outlined Accounts pill and adds Settings.

| Layer | What sits there | Tokens |
|---|---|---|
| Page | Feeds, the You tab, search, Settings | `color.bg.page` |
| Pushed page | General, Appearance (back chevron and bold title) | `color.bg.page`, `typography.navTitle` |
| Bottom sheet | Library sort, My Ad Centre | `color.bg.sheet`, `radius.sheet`, `color.bg.scrim` behind |
| Menu | Video overflow | `color.surface.menu`, `radius.menu` |
| Overlay on media | Duration badge, Shorts rail, Subscribe pill, mini player | `color.overlay.duration`, `color.button.subscribe.bg` |
| Tab bar | Always on top of the feeds | `color.surface.tabBar` |

Settings opens full screen with a close (x) at the top left ([10-settings-icon-list](screenshots/dark/10-settings-icon-list.png));
its rows push pages with a back chevron ([11-general-switches-on-off](screenshots/dark/11-general-switches-on-off.png)).

## The feed

Home and Subscriptions are one vertical feed on `color.bg.page`. Subscriptions starts with a row of
`size.avatarSubscription` channel avatars with blue new-content dots and an 'All' link, then the filter chips
([13-subscriptions-avatars-chips](screenshots/dark/13-subscriptions-avatars-chips.png)). Selecting a chip inverts it
and refilters the feed in place ([14-chip-selected-video-cards-preview](screenshots/dark/14-chip-selected-video-cards-preview.png)).

A video card is a full-width 16:9 thumbnail with no radius and a duration badge, then a row of the channel
avatar (`size.avatarChannel`), a two-line title (`typography.videoTitle`), a meta line (`typography.meta`,
`color.text.secondary`) and an overflow button. The card in view plays a muted preview with captions
([14-chip-selected-video-cards-preview](screenshots/dark/14-chip-selected-video-cards-preview.png)). Ads take the same shape with a
'Sponsored' line and a tonal and a filled button side by side, on a block that takes the ad's tint in dark
([02-home-ad-shorts-shelf-tabbar](screenshots/dark/02-home-ad-shorts-shelf-tabbar.png)).

Shelves break the feed: Shorts as a two-column grid of portrait cards with rounded corners
(`radius.thumbnail`) ([06-home-scrolled-ad-buttons-shorts-grid](screenshots/dark/06-home-scrolled-ad-buttons-shorts-grid.png)),
History on the You tab as a horizontal row of small rounded thumbnails with a red progress bar, then the
Library chips and rows ([08-you-tab-profile-history-library-chips](screenshots/dark/08-you-tab-profile-history-library-chips.png)).

## Watching

The watch page puts the player at the top, then the title, the channel handle with likes, views and age, a row
of the channel avatar, a notification pill and outline action icons (like, dislike, share, a sparkle, more), then a
comments teaser card (`color.surface.card`, `radius.card`) with a comment field, then related videos as feed
cards ([16-watch-page-actions-comments-teaser](screenshots/dark/16-watch-page-actions-comments-teaser.png)). In dark
the title block takes a tint from the video. Closing it shrinks the video to a floating mini player above the
tab bar ([18-floating-mini-player](screenshots/dark/18-floating-mini-player.png)). The player's own controls and
scrubber were not captured.

A Short fills the screen: back, search and more at the top, an action rail of icons with counts at the right,
and a search pill, the channel with a white Subscribe pill and the title at the bottom
([07-shorts-player-action-rail-subscribe](screenshots/dark/07-shorts-player-action-rail-subscribe.png)).

## Search and filtering

Tapping Search replaces the header with a back chevron, the grey capsule field (`size.searchField`) and a
microphone. History rows (clock icon, query, a thumbnail, a fill-in arrow) fill the page on a `size.rowSearch`
pitch ([04-search-focused-history-rows](screenshots/dark/04-search-focused-history-rows.png)). Typing swaps the
microphone for a clear x and the rows for suggestions with a magnifier; a suggestion can carry a second line in
`color.text.secondary` ([05-search-typed-suggestions](screenshots/dark/05-search-typed-suggestions.png)). Filtering
is the chip row; sorting the library is a bottom sheet with a tick on the current choice
([09-sort-bottom-sheet-checked](screenshots/dark/09-sort-bottom-sheet-checked.png)). Search results and the
no-results state were not captured.

## Settings and forms

Settings is a plain list on the page colour with no cards and no dividers: an outline icon and a label per row,
`size.row` apart, under bold section headers ([10-settings-icon-list](screenshots/dark/10-settings-icon-list.png)).
General mixes rows with a value at the right, rows with helper text under the label, and Material-style
switches ([11-general-switches-on-off](screenshots/dark/11-general-switches-on-off.png)). Appearance is a choice list
with a tick ([12-appearance-choice-list-not-changed](screenshots/dark/12-appearance-choice-list-not-changed.png)). No
form with validation or an error message was captured.

## Sheets and menus

Bottom sheets sit inset from the screen edges with a grabber and `radius.sheet` corners over a 50% scrim
([09-sort-bottom-sheet-checked](screenshots/dark/09-sort-bottom-sheet-checked.png)). My Ad Centre is a taller sheet
with a title and close, plain rows, outlined accordions and an outlined Send feedback capsule; its body stays
dark in the light theme ([03-ad-centre-sheet-accordions](screenshots/dark/03-ad-centre-sheet-accordions.png),
[03 light](screenshots/light/03-ad-centre-sheet-accordions.png)). The video overflow menu is a floating card of nine
icon-and-label rows ([15-video-overflow-menu](screenshots/dark/15-video-overflow-menu.png)).

## Upsell

The Premium interstitial fills the screen with its own light gradient in either theme: the Premium wordmark, a
two-line bold headline (`typography.display`), a subtitle, a large dark button and a text-only decline
([01-premium-upsell-interstitial](screenshots/dark/01-premium-upsell-interstitial.png)).

## Feedback, empty, loading and error states

Not captured. The capture took no action that raises a toast (like, subscribe, save), submitted no search, and
caught no loading or error state; cutting the network also ends iPhone Mirroring.


## Public web shell, 2026-11-21

Signed out, the desktop shell is a 56px masthead and a 72px mini guide. Guide opens a 240px drawer. The home feed is an empty card, not a video grid, until a search or an Explore destination. See [home-dark-empty](screenshots/public/home-dark-empty.png) and [home-dark-guide](screenshots/public/home-dark-guide.png).

Search results are a chip row (All selected by inversion) over video rows, with a Filters dialog. See [search-dark-results](screenshots/public/search-dark-results.png) and [search-dark-filters](screenshots/public/search-dark-filters.png).

A public watch page keeps the player, title, Subscribe pill, like and share, and a related column. Save opens a sign-in prompt and stops. See [watch-dark-default](screenshots/public/watch-dark-default.png) and [watch-dark-save-signin](screenshots/public/watch-dark-save-signin.png).

Subscriptions, Library and History are empty states with a Sign in pill. See [subscriptions-dark-empty](screenshots/public/subscriptions-dark-empty.png), [library-dark-empty](screenshots/public/library-dark-empty.png) and [history-dark-empty](screenshots/public/history-dark-empty.png).

Premium is a marketing page. The trial button leaves for accounts.google.com and was not followed into checkout. See [premium-dark-default](screenshots/public/premium-dark-default.png). About lives on about.youtube and is a light marketing page. See [about-dark-default](screenshots/public/about-dark-default.png).

Phone width collapses the shell to a bottom bar (Home, Shorts, You) and a search field. See [mobile-home-dark-empty](screenshots/public/mobile-home-dark-empty.png) and [mobile-watch-dark-default](screenshots/public/mobile-watch-dark-default.png).

Login and signup are Google account walls, photographed empty. See [login-light-empty](screenshots/public/login-light-empty.png) and [signup-light-empty](screenshots/public/signup-light-empty.png).
