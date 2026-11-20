# Peerlist patterns

Public pages, signed out, 2026-11-21. The map of which control opens which page is [site-tree.md](site-tree.md).

## App shell

Marketing (`/`, `/ads`, `/login`, `/signup`) uses a centered top bar: logo, Scroll, Jobs, Launchpad, Log in (quiet), Create Profile (green). Phone width replaces the links with a hamburger. [screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png), [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

App pages (`/scroll`, `/jobs`, `/launchpad`, `/search`, `/blog`) use a left rail (Scroll, Launchpad, Jobs, Search, Blog, Advertise) plus a top row with Log in and Create Profile. Current rail item has a green edge. [screenshots/scroll-light-default.png](screenshots/scroll-light-default.png), [screenshots/scroll-dark-default.png](screenshots/scroll-dark-default.png).

## Form with validation

The login form is public and was not submitted, so no validation error was shown. Fields are empty. [screenshots/login-wall-light-default.png](screenshots/login-wall-light-default.png). Signup is the same shape at `/signup`.

## Empty, loading, error

`/help` is a 404. [screenshots/not-found-light-default.png](screenshots/not-found-light-default.png). A Scroll video card shows "Unable to load video." No skeleton loader was isolated. Search with an empty query shows filters, not an empty-results state (the field was not typed into).

## Destructive confirmation

Not present while signed out. Not captured.

## Feedback after an action

Post, Launch and Follow open the login dialog instead of completing. [screenshots/scroll-light-login-dialog.png](screenshots/scroll-light-login-dialog.png). No toast fired.

## Search and filtering

`/search` has People / Projects / Jobs / Posts. People is public. The other three tabs open the login dialog. Filters on People: Skills and Tools, Match with all the tags, Location, Roles, Company. [screenshots/search-light-default.png](screenshots/search-light-default.png). Jobs also filter by role at `/jobs/role/{slug}`.

## List or table

Jobs is a list of role rows. Launchpad is a ranked project list. Scroll is a feed. No data table.

## Onboarding

Create Profile and the username claim on the homepage start signup. Both were left alone. The login and signup walls are the only onboarding screens captured.
