# Patterns

Page screenshots from 2026-11-21 are in [screenshots/](screenshots/). The rows below are what the live DOM showed on 2026-11-19, checked again against the public pages on 2026-11-21.

## Logged-out shell

Header class `site-header site-header-logged-out`. At 1440px the inner bar is 76px tall, padding `0 28px`, gap 30px. Links: Browse, Community, Search, Show more, Log in, Join for free. At 390px the header is 56px and a 42px hamburger (`toggle-slide-out-navigation`) is displayed. The phone hero heading computes 29.64px.

Footer class `site-footer`, fill `#f5f5f5`, padding `45px 0 22.5px`, 13px type. Directory links cover Releases, Artists, Labels, Genres, Users, Reviews, Lists, About, Help, Blog, Changelog, Supporter, Contact, and the legal pages.

## Marketing home

`/` is a long marketing page. Display heading in GTFAdieu, a GT America lede at 20px in muted ink, a primary "Create free account" and an outline "Get the app". Bento blocks at radius 16px and `#fafafa` hold the primer. A FAQ list sits above the footer. "Join the club today" repeats the primary action.

## Browse and releases

`/browse` is a directory: a 44px display heading, outline cards (radius 9px, 1px `#3f3f3f` border in dark), and a release rail. `/releases` is a filterable grid. Type chips (All, Albums, Singles, EPs) sit above 186px artwork at radius 4px. Filter menus were not opened.

## Release page

`/releases/albums/2hollis-pirouette` is a public release. Artwork 270px at radius 4px, GT America title at 35px / 500, a type label, stat row, section nav, and a track table. Listened, Rotation, Queue, Like and Submit rating are visible and were not pressed.

## Auth

`/login` heading is "Welcome back." `/register` heading is "Join the community." Both stack Continue with Apple, Continue with Google, an "Or continue with email" divider at 13px muted, then email, password, and a disabled Continue until the fields are filled. Legal line points at Terms of Use and Privacy Policy. Neither form was submitted. Apple and Google were not pressed. The form is not email-only, so no address was typed.

## Help and 404

`/help` heading "How can we help?" at 44px GTFAdieu, then topic groups. A missing route renders "Page not found" in the same display style, with the sentence "Oh no! We can't find the page you've requested."

## Supporter

`/supporter` at 390px shows Monthly and Yearly, a free Standard column, and Supporter at $4 per month. Checkout was not opened.

## Theme

`data-theme="system"` follows the OS. The 2026-11-19 session was dark, so `/browse` and `/login` were read dark first, then `data-theme` was set to `light` and the same pages were read again. Some controls (explore card border, login fields) did not repaint. Those are called out in [README.md](README.md).

## 2026-11-21 frames

The refresh left `data-theme` on `system` and did not flip it. Homepage and about painted light. Browse, the album page, lists, search, help, supporter, the 404, and both auth walls painted dark. Frames: [home-light-default](screenshots/home-light-default.png), [home-light-more](screenshots/home-light-more.png), [home-light-footer](screenshots/home-light-footer.png), [home-light-mobile](screenshots/home-light-mobile.png), [home-light-mobile-menu](screenshots/home-light-mobile-menu.png), [browse-dark-default](screenshots/browse-dark-default.png), [album-dark-default](screenshots/album-dark-default.png), [album-dark-mobile](screenshots/album-dark-mobile.png), [lists-dark-default](screenshots/lists-dark-default.png), [search-dark-empty](screenshots/search-dark-empty.png), [about-light-default](screenshots/about-light-default.png), [help-dark-default](screenshots/help-dark-default.png), [supporter-dark-default](screenshots/supporter-dark-default.png), [notfound-dark-default](screenshots/notfound-dark-default.png), [login-dark-default](screenshots/login-dark-default.png), [signup-dark-default](screenshots/signup-dark-default.png). Community and the blog were read and not photographed. Login and signup were photographed empty and not submitted.
