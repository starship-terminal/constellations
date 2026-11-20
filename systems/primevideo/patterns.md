# Patterns

How the public signed-out pages combine the components. The map of which control opens which page is [site-tree.md](site-tree.md).

## App shell

A 66px bar on `dark.color.bg.page`. Wordmark, Home, Movies, TV shows, Sports on the left. Search, language, categories, account and Join Prime on the right. The bar does not change colour on scroll in the captures.

At 390x844 the links collapse into a Menu button. Search, EN and the account glyph stay in the bar. Join Prime moves into the menu.

Screenshots: [home-dark-default.png](screenshots/home-dark-default.png), [mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png), [mobile-home-dark-menu.png](screenshots/mobile-home-dark-menu.png). Crop: [nav-default.png](components/crops/nav-default.png).

## Marketing home

Left column on black: a 50px/56px heading, a 14px lede, a white Sign in button, a divider with "or", a white trial button, a 14px footnote. Right column is a poster mosaic. Below the fold, promo blocks repeat the trial button. Footer is Terms and Privacy Notice, Send us feedback, Help.

[home-dark-full.png](screenshots/home-dark-full.png) is the page to 4865px. The phone full page is [mobile-home-dark-full.png](screenshots/mobile-home-dark-full.png).

## Browse

Movies, TV shows and Sports are poster rows under the same shell. Categories is a grid of genre and collection links. A genre page adds a 32px title, pill filters, and rows with See more.

[movies-dark-default.png](screenshots/movies-dark-default.png), [categories-dark-default.png](screenshots/categories-dark-default.png), [genre-action-dark-default.png](screenshots/genre-action-dark-default.png).

## Title

A full-bleed still, a row of icon buttons, a white trial button, synopsis, cast, genre links, then Related and Details. Details is raised cards for advisory, languages and cast.

[detail-dark-default.png](screenshots/detail-dark-default.png), [detail-dark-details.png](screenshots/detail-dark-details.png), [mobile-detail-dark-default.png](screenshots/mobile-detail-dark-default.png).

## Search and filter

Search is a panel over the current page, not a route. Filters on a genre page are the pill chips. Selecting Movies in the capture navigated to `/movie` rather than filtering in place, so that state is not a second genre view.

[home-dark-search.png](screenshots/home-dark-search.png).

## Help and legal

Help is a list of article titles plus account links that wall at Amazon Sign-In. One article opened on the same host. Terms and Privacy Notice is a long help node.

[help-dark-default.png](screenshots/help-dark-default.png), [help-dark-article.png](screenshots/help-dark-article.png), [legal-dark-default.png](screenshots/legal-dark-default.png).

## Feedback

Share is the only feedback dialog that stayed on the site. Trailer playback failed closed with Video Unavailable and OK. No toast appeared.

[detail-dark-share.png](screenshots/detail-dark-share.png), [detail-dark-trailer-unavailable.png](screenshots/detail-dark-trailer-unavailable.png).

## Not on these pages

Signed-in home, playback of a full title, watchlist, profiles, purchases, a validation error, an empty library, a loading skeleton that settled into a measured state, a destructive confirmation, onboarding. Those sit behind Amazon Sign-In or did not appear.
