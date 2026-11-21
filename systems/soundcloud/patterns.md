# SoundCloud patterns

Public pages, 2026-11-21. The map of which control opens which page is [site-tree.md](site-tree.md).

## App shell

Desktop player: a 46px logo, Home, Feed, Library, a search field, Sign in, Create account, Upload, and a more menu. A promo banner sits under the header. A play bar sits on the bottom edge. See [discover-dark-default.png](screenshots/discover-dark-default.png).

Phone: `soundcloud.com` at 390px redirects to `m.soundcloud.com`. A top bar has the mark, Sign in, and Listen in app. A five-item tab bar sits at the bottom: Home, Feed, Search, Library, Download. See [mobile-discover-light-default.png](screenshots/mobile-discover-light-default.png).

Company pages use a different header: Company, Services, Newsroom, Careers, Available Plans, and a search field. See [company-dark-default.png](screenshots/company-dark-default.png). On a phone that header collapses to a menu. See [mobile-company-dark-menu.png](screenshots/mobile-company-dark-menu.png).

## Navigation

Home goes to Discover. Feed and Library stop at a sign-in wall: [wall-feed-dark-default.png](screenshots/wall-feed-dark-default.png). Settings and more opens a menu, not a page: [discover-menu-dark-open.png](screenshots/discover-menu-dark-open.png).

## Search and filtering

A query lands on search results with Everything, Tracks, People, Albums, and Playlists. Tracks adds time and tag filters. See [search-results-dark-default.png](screenshots/search-results-dark-default.png) and [search-tracks-dark-default.png](screenshots/search-tracks-dark-default.png). The phone equivalent is [mobile-search-light-results.png](screenshots/mobile-search-light-results.png).

## List

Search and profile rows share artwork, a title, a waveform, and counts. A more menu offers Add to Next up, Add to Playlist, and Station. See [track-more-menu-dark-open.png](screenshots/track-more-menu-dark-open.png).

## Form

The only public form is the sign-in wall. It was not submitted. See [discover-signin-wall-dark-open.png](screenshots/discover-signin-wall-dark-open.png). A known probe of email Continue on `secure.soundcloud.com` said something unexpected happened and did not advance. That error state was not repeated and is Not captured.

## Empty, loading, error

The phone home showed a spinner before tracks arrived, in [mobile-home-light-default.png](screenshots/mobile-home-light-default.png). No empty state and no error state were captured. Charts at `/charts/top` returns HTTP 404 and still paints rows.

## Feedback

No toast was shown. Play starts audio in the bottom bar. The bar did not change enough to crop as its own state. See [search-tracks-dark-playing.png](screenshots/search-tracks-dark-playing.png).

## Destructive confirmation

Not present on public pages.

## Onboarding

Signed-out home is a marketing carousel: [home-dark-default.png](screenshots/home-dark-default.png). Get started opens the sign-in wall and was not followed. The phone discover page offers a sign-in sheet that dismisses with No thanks: [mobile-discover-light-sheet.png](screenshots/mobile-discover-light-sheet.png).
