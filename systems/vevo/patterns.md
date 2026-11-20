# Patterns

Signed-out marketing pages on `https://www.hq.vevo.com/`. `https://www.vevo.com/` redirects there. Screenshots are viewport captures at the measured CSS size, 2x, then quantized to 256 colours.

## Home

A transparent header sits on a full-bleed black-and-white artist still. The wordmark is left, six links are right. The hero is four stacked display lines in white, with a white pill under them. Sections then run crimson (statistics), slate (artists), black (originals), sand (advertisers), and black (newsroom), then a black footer.

[home-light-default.png](screenshots/home-light-default.png) at 1440 by 900. [home-light-phone.png](screenshots/home-light-phone.png) at 390 by 844. The phone header replaces the links with a menu button. [home-light-menu.png](screenshots/home-light-menu.png) is that menu open: black panel, current item in violet, close mark at the top right. A blue cookie bar covers the bottom until dismissed. [home-light-cookie.png](screenshots/home-light-cookie.png) is the page scrolled to the statistics; the bar itself is [banner-default.png](components/crops/banner-default.png).

## About and originals

Same header. About opens on a display headline. Originals is a list of performance stills and titles, not a player. `/watch` and a video path both land on `/originals`.

[about-light-default.png](screenshots/about-light-default.png). [originals-light-default.png](screenshots/originals-light-default.png).

## Contact

A black page, a display title, then a stack of blue rows. Each row is a department name and a published address. No form.

[contact-light-default.png](screenshots/contact-light-default.png).

## Not on these pages

No app shell beyond the marketing header. No search. No empty, loading, or error state. No destructive confirmation. No onboarding. No signed-out video chrome: the network does not serve a player at the public URLs tried.
