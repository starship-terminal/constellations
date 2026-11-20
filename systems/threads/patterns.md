# Patterns

Public Threads, signed out, 2026-11-21. The map of which control opens which page is [site-tree.md](site-tree.md).

## App shell

Desktop is three columns. A left rail (logo, Home, New thread, Search, Messages, Activity, Profile, Insights, Log in, More). A centre feed titled Home. A right card, "Log in or sign up for Threads", with Continue with Instagram. The page ground is `light.page` (`rgb(255, 255, 255)`). The rail item for the current page is a light grey pill. [home-light-default.png](screenshots/home-light-default.png).

Dark follows `prefers-color-scheme` and paints `__fb-dark-mode`. The page is `rgb(16, 16, 16)`. Log in inverts to a white pill. [home-dark-default.png](screenshots/home-dark-default.png).

Phone drops the rail. A centred mark, Log in and Open app (or Get app), then the feed, then a five-icon tab bar (Home, Search, Create, Notifications, Profile). [mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png).

## Feed

A post is an avatar, a bold handle, a topic chip, a relative time, body text, optional media, and a row of like, comment, repost, and share with counts. Like, comment, repost, and share were not pressed.

## Login wall

New thread, Messages, Activity, Profile, Insights, Follow, and the follower count open a dialog or `/login`. The branch stops there. The login page itself is a centred form over a black Threads-word pattern, with a QR labelled "Scan to get the app". Nothing was typed. [login-light-default.png](screenshots/login-light-default.png).

## Search

An empty search field in a rounded column, with the same right-hand login card. [search-light-default.png](screenshots/search-light-default.png). No query was typed.

## Profile

The official @threads profile is public: name, handle, bio, topic chips, follower count, Follow, Mention, and four tabs. [profile-light-default.png](screenshots/profile-light-default.png). Follow opens the sign-up dialog. [profile-light-follow-wall.png](screenshots/profile-light-follow-wall.png).

## Menu

More opens Appearance, Sounds, and Report a problem. Appearance shows sun, moon, and Auto, with Auto selected. Sounds shows two off switches. Neither switch was toggled. Report a problem did not open a form in this pass.
