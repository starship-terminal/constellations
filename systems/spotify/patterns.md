# Spotify patterns

How the components in [components.md](components.md) combine into Spotify's screens on iOS. Token paths are in
[tokens.json](tokens.json); the captures named here are in [screenshots/](screenshots). Spotify for iOS is dark only.

## App shell and navigation

Four tabs sit at the bottom: Home, Search, Your Library and Create. Above them, on every tab, floats the mini player:
a rounded bar inset 8 pt from the screen edges, tinted from the playing track's artwork, with a thin progress line
along its bottom ([02-home](screenshots/dark/02-home.png), [10-library](screenshots/dark/10-library.png)). Each tab
page opens with the account avatar at the top left (a blue dot when there is news); tapping it slides the profile
drawer in from the left ([19-profile-drawer](screenshots/dark/19-profile-drawer.png)). Pushed pages (Settings,
Playback, an artist) replace the header with a round glass back button and, on settings pages, a centred bold
title ([20-settings](screenshots/dark/20-settings.png)).

| Layer | What sits there | Tokens |
|---|---|---|
| Page | Every tab page, pushed pages, lists; tiles and cards are flat fills on it, with no shadow | `color.bg.page`, with `color.surface.tile`, `color.surface.card`, `color.surface.panel` |
| Floating bar | The mini player | `color.surface.miniPlayer` (from the artwork), `radius.md` |
| Drawer | Profile drawer, the page dimmed beside it | `color.bg.elevated`, `size.drawerWidth` |
| Glass | Chips, the focused search field, Cancel, back buttons | `color.surface.glass`, `color.surface.chip`, `color.surface.fieldFocused` |
| Sheet | Sort, context and share sheets, inset 8 pt, over a scrim | `color.surface.sheet`, `radius.sheet`, `color.bg.scrim`, `color.bg.scrimContext`, `color.bg.scrimStrong` |

## Home

Home stacks, top to bottom: filter chips beside the avatar (All, Music, Podcasts), a two-column grid of eight
shortcut tiles (artwork at the left, a bold title), then sections with a bold title and a horizontally scrolling
row of artwork cards (New Music Friday, Recents with 'Show all', Jump back in), with promo cards between them
([02-home](screenshots/dark/02-home.png), [03-home-scrolled](screenshots/dark/03-home-scrolled.png)). The header
chips stay pinned while the page scrolls under them. Choosing Music swaps the page for a music-only feed and adds
sub-chips (Following); there the selected chip took the coral of the New Music Friday banner
([04-home-music-chip](screenshots/dark/04-home-music-chip.png)).

## Search and filtering

Search opens with a bold title, a camera button and a white search field, then rows of tall video and episode
cards and the 'Browse all' grid of flat-colour category tiles ([05-search](screenshots/dark/05-search.png),
[06-search-grid](screenshots/dark/06-search-grid.png)). The field pins to the top as the page scrolls. Tapping it
turns it into a glass capsule with a green caret and a Cancel button, and the page becomes recent searches, each
with + and x ([07-search-focused-recents](screenshots/dark/07-search-focused-recents.png)). Typing shows completion
rows (magnifier, the query in bold, an arrow to fill it in) above result rows, and a clear button in the field
([08-search-typed-suggestions](screenshots/dark/08-search-typed-suggestions.png),
[16-search-typed-clear-cancel](screenshots/dark/16-search-typed-clear-cancel.png)). Even a random string returns
results, so no empty state appeared ([09-search-results-rows](screenshots/dark/09-search-results-rows.png)).

Your Library filters with chips (Playlists, Podcasts, Albums, Artists and more off screen); choosing one turns it green,
adds an x chip to clear it and shows sub-chips (By you, By Spotify)
([10-library](screenshots/dark/10-library.png), [11-library-chip-selected](screenshots/dark/11-library-chip-selected.png)).
A sort row (Recents, with a grid toggle) opens the sort sheet ([12-sort-sheet](screenshots/dark/12-sort-sheet.png)).

## Data display

Lists are rows of artwork, a title and a subtitle line, 64 pt apart in search and 80 pt in Your Library, where the
artwork grows to 64 pt. Subtitles carry the type and owner ('Playlist • Spotify') and lead with small green pin
and download icons. Artists are round, everything else square. Trailing actions are + (add), x (remove) or a green
saved tick ([10-library](screenshots/dark/10-library.png), [07-search-focused-recents](screenshots/dark/07-search-focused-recents.png),
[08-search-typed-suggestions](screenshots/dark/08-search-typed-suggestions.png)).

Settings opens with three quick tiles (Data Saver, Offline mode, Private session; the active one in green), then
rows of a line icon, a title, a two-part subtitle and a chevron ([20-settings](screenshots/dark/20-settings.png)).
A settings page such as Playback groups title, description and switch rows under bold section titles split by a
divider, with a slider for Crossfade ([21-settings-playback-switches-slider](screenshots/dark/21-settings-playback-switches-slider.png),
[22-settings-switch-off](screenshots/dark/22-settings-switch-off.png)).

## Artist page

An artist page puts a full-bleed photo under the status bar with the name in very large bold type and a 'Verified
by Spotify' line at its bottom. Below: monthly listeners, an action row (a small artwork stack, the outlined
Following pill, more, shuffle, and the round green play button), text tabs with a green underline (Music, Video,
Events, Merch), a 'You liked' row, and the Popular list with numbered rows
([23-artist-tabs-following](screenshots/dark/23-artist-tabs-following.png)).

## Sheets and menus

Every '...' opens a glass context sheet from the bottom: the item's artwork and name, a divider, then rows of a line
icon and a label (Share, Add to playlist, Add to Liked Songs, Add to Queue, Start a Jam, Go to album, Go to artist
concerts; a green 'Beta' tag where a feature is new) ([24-artist-context-sheet](screenshots/dark/24-artist-context-sheet.png),
[25-track-context-sheet](screenshots/dark/25-track-context-sheet.png)). The page behind dims to `color.bg.scrimContext`.
The sort sheet is the same material with a small header, the options, a green tick on the current one, and Cancel
([12-sort-sheet](screenshots/dark/12-sort-sheet.png)).

The share sheet is taller: a preview card in the shared item's colours, swatches to recolour it, a Song or Lyrics
segmented control for a track, then a row of contacts and groups and a row of apps, each a 56 pt circle
([14-share-sheet](screenshots/dark/14-share-sheet.png), [18-share-song-segmented](screenshots/dark/18-share-song-segmented.png)).

## Profile drawer

The drawer holds an account card (avatar, name, 'View profile', Add account), menu rows with line icons (Your
Premium with a lavender plan badge, Listening stats, Recents, Your Updates with a blue dot, Settings and privacy),
friends' activity circles, and Messages with a dismissible card asking to turn on notifications
([19-profile-drawer](screenshots/dark/19-profile-drawer.png)).

## Feedback

Saving shows as a green tick in a filled circle, in the mini player and on saved rows
([02-home](screenshots/dark/02-home.png), [08-search-typed-suggestions](screenshots/dark/08-search-typed-suggestions.png)).
News is a blue dot on the account avatar and on Your Updates; the drawer's notification card is the only banner
seen ([19-profile-drawer](screenshots/dark/19-profile-drawer.png)). No toast appeared.

## Destructive actions

Removal is quiet: an x at the end of a recent-search row, and 'Stop following' as an ordinary row with an x icon in
the artist's context sheet ([07-search-focused-recents](screenshots/dark/07-search-focused-recents.png),
[24-artist-context-sheet](screenshots/dark/24-artist-context-sheet.png)). No red text or fill appeared. Neither was
tapped, and Log out was not tried, so whether Spotify confirms a destructive action is not known.

## Not captured: Now Playing, playlist page, loading, empty, error, onboarding

Spotify opened its share sheet the instant Now Playing or a playlist page was captured, every time
([15-share-sheet-playlist-auto](screenshots/dark/15-share-sheet-playlist-auto.png) is the sheet that opened over a
playlist). Low-resolution references of both screens stay outside the repo and give layout only: Now Playing fills
the screen with the artwork's colour, a down chevron and a centred context title at the top, a large square
artwork, the title and artist with a saved tick, a progress line with times, previous, a large white round play
and next, then devices and share, and a Lyrics card at the bottom. A playlist page uses the artist page's
full-bleed header and large title, then a description, the owner, saves and length, an action row ending in the
green play button, and track rows. No value in this package comes from either reference.

No loading skeleton was caught (the Home capture taken at launch was already loaded), search never came back empty,
cutting the network would end the mirroring session, and the account was already signed in, so loading, empty,
error and onboarding are not covered.
