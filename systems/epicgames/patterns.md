# Epic Games patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Store chrome (dark, every store page)

Two stacked bars over the `#101014` canvas (`dark.background.default`). The 72px `<egs-navigation>` web component (`core.component.nav-height`) carries the Epic mark, STORE/SUPPORT links, the Distribute dropdown, the globe locale button, a translucent dark Sign-in pill and the `#26bbff` brand-blue Download pill (`dark.action.accent-primary`, `#33bfff` resolved). Under it, the 100px store tab bar holds the 230×40 "Search store" field (a `#202024` elevated-low field, `dark.background.field`, 20px radius) and the Discover/Browse/News tab links — the active tab underlined in the accent blue.

Every store page ends in the `<egs-footer>` web component (~878px): link columns, social icons, ratings and legal, same `#101014` canvas with `#ffffffa6` secondary text (`dark.text.secondary`).

## Discover (store home)

A 488px hero carousel dominates: a full-bleed slide (868px wide at 1440px viewport) with promo art, a headline block and a white "Save Now" pill (111×48, `radius.full`-like 9999px). A rail of 180×79 thumbnail buttons pips the slides; a 30×30 "Next page" chevron sits on the shelf rails. Below, horizontal shelves of 335×100 game cards: cover art left, title and a `#fffffff2`/`#ffffffa6` price line right, plus the 48×48 plus-corner wishlist button. Each shelf ends in a ghost "View More" (117×48).

## Browse (legacy grid)

The oldest store surface: Emotion `css-*` classes rather than EDS tokens. "Popular Genres" display heading over 255×230 genre tiles, then a 126×30 "New Release" sort `menuitem` dropdown over a grid of 194×370 game cards (taller covers, 44×44 wishlist corner). The 240px right rail is a Filters aside: a 206×40 keyword field, then Events/Genre/Features/Types/Platform/Subscriptions accordions (238×62 headers) that expand into 206×24 styled-div checkbox rows. Numbered pagination (27px items) under the grid.

## Product page (Fortnite)

1069px title, an ESRB ratings strip and a 69px sub-nav (Overview/Achievements/Add-Ons) under the chrome. Left: a media stage with 56×56 pager buttons and 89px thumbnails. Right rail: a `#26bbff` "Get" CTA (270×46), a 312px "Add to Cart" ghost button, a 320px wishlist row, price line, share and platform links. Below the fold: genre/tag chips (58×23, `radius.full`), the 46×78 ratings badge, "Why play on Epic" rows, add-on table rows (368×40) and a system-requirements tab bar (62px tabs).

## Free Games / News / Download

Free Games: a 226×50 heading, the 265×40 banner CTA, and 347×301 promo cards carrying a 240×20 "Free Now"/"Coming Soon" badge. News: article cards (530×439) with an 81×21 "Read More" link. Download: a 640×65 display heading over a 176×20 "Download Epic Games Launcher" CTA.

## Sign-in (www.epicgames.com/id)

A MUI dialog (562×972 paper) on a dark scrim: Epic mark, "Sign in" title, a 463×48 outlined email field (focus ring, filled state measured then cleared — never sent), a 464×48 Continue button, a 131px "Create account" link, then two grids of provider buttons: console tiles (PlayStation, Xbox, Nintendo, 149px) and social buttons (Google, Steam, Disney+, Apple, Facebook).

## Support centre (www.epicgames.com/help)

Same dark canvas: a 524px hero heading, a 784×40 "Search support" field (focused and filled states measured, never submitted), then a grid of 276×120 category tiles. A 99px "All Systems Operational" status chip and the 150×48 floating chat launcher.

## Marketing home (www.epicgames.com/site)

The older OpenSans surface (`core.font.family.www`): a dark hero with game tiles (480×868) and an "Explore" CTA (137px). Painted dark even though it is a marketing page — no light theme anywhere on the captured surfaces.

## Mobile (390px)

The same store re-lays at 390×844: `<egs-navigation>` keeps the 72px bar with a 46×32 hamburger (the drawer is captured in `mobile-discover-dark-drawer.png`), and shelves become a swipeable 278px card carousel.
