# Patterns

No page screenshots. Each row is what the live DOM showed on 2026-11-19.

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

`data-theme="system"` follows the OS. The capture session was dark, so `/browse` and `/login` were read dark first, then `data-theme` was set to `light` and the same pages were read again. Some controls (explore card border, login fields) did not repaint. Those are called out in [README.md](README.md).
