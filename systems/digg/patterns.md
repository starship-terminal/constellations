# Patterns

## App shell

Desktop: a 255px sidebar (logo, topic links, theme cycle, Log in, Sign up) and a main column that starts at x 256. The feed has a sort control and a density control, then posts, with a right rail of Top Contributors and Top Posts Today. [screenshots/home-light-default.png](screenshots/home-light-default.png). Folding the sidebar is [screenshots/home-light-sidebar-folded.png](screenshots/home-light-sidebar-folded.png).

Phone: a header with the menu button and wordmark, a horizontal topic scroller, then the same sort and density controls. The menu opens a sheet. [screenshots/mobile-home-light-feed.png](screenshots/mobile-home-light-feed.png), [screenshots/mobile-home-light-nav-open.png](screenshots/mobile-home-light-nav-open.png).

Dark uses the same structure with `#161617` page and `#1c1c1f` cards. [screenshots/home-dark-default.png](screenshots/home-dark-default.png), [screenshots/mobile-home-dark-feed.png](screenshots/mobile-home-dark-feed.png).

## Feed

One post pattern repeats: topic chip, title, summary, digg count, comment count, source avatars, source count, thumbnail. Compact is the default density. Comfy shows a larger media block. [screenshots/home-light-comfy.png](screenshots/home-light-comfy.png). Topic feeds (`/tech`, `/gaming`, `/entertainment`, `/world-business`, `/science`, `/sports`, `/ai`) use the same shell with that topic selected.

## Story

A story page keeps the sidebar, adds back and topic chips, a headline, a digg control, sources, and a related column. [screenshots/story-light-default.png](screenshots/story-light-default.png), dark in [screenshots/story-dark-default.png](screenshots/story-dark-default.png), phone in [screenshots/mobile-story-light-default.png](screenshots/mobile-story-light-default.png).

## Profile

A public profile shows a handle, a follow button, and counts. Follow opens the login wall. [screenshots/profile-light-default.png](screenshots/profile-light-default.png).

## Walls

Login and signup are full pages, not dialogs. They offer Google, X, or email. Those identity buttons were not used. [screenshots/login-light-default.png](screenshots/login-light-default.png), [screenshots/signup-light-default.png](screenshots/signup-light-default.png), phone login in [screenshots/mobile-login-light-default.png](screenshots/mobile-login-light-default.png).

## Static pages

About, Contact, Privacy, Terms, and Community Guidelines sit in the same shell. [screenshots/about-light-default.png](screenshots/about-light-default.png). A missing URL renders a 404 in that shell. [screenshots/not-found-light-default.png](screenshots/not-found-light-default.png).

## Cookie notice

The notice offers Accept all, Only necessary, and Manage preferences. It was hidden for the other shots. Cookie preferences, opened from the footer, is the dialog pattern. [screenshots/about-light-cookie-preferences.png](screenshots/about-light-cookie-preferences.png).
