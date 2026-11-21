# Kickstarter patterns

How the public signed-out surface is put together. Screenshots are in [screenshots/](screenshots).

## App shell

A white header: green wordmark, a search field, "For creators", "Log in", then a category row (Art through Theater, then Discover). Hovering a category opens a three-column panel of subcategories, filters, and a featured project. [home-light-default](screenshots/home-light-default.png), [home-light-category-menu](screenshots/home-light-category-menu.png).

On a 390-wide phone the category row scrolls sideways and a menu glyph sits at the right of the header. [mobile-home-light-default](screenshots/mobile-home-light-default.png).

The 2026-11-21 refresh did not show that yellow status toast. The phone Discover shot showed a site error toast. It is page content, not a consent dialog. [mobile-discover-light-default](screenshots/mobile-discover-light-default.png).

## Home

A centred headline, then a dark green editorial banner with a white "Explore the app" pill, then project rails (Featured, Recommended) of image cards with a green funding rule, a creator line, and a bookmark. [home-light-default](screenshots/home-light-default.png).

## Search and filtering

Discover is a left filter column (project status checkboxes, category, location radios) and a card grid, with sort at the top right. Search from the header lands on `/discover/advanced?term=`. [discover-light-default](screenshots/discover-light-default.png), [search-light-default](screenshots/search-light-default.png).

## Project page

A public campaign: title, video, pledged amount in brand green, backer count, a green "Back this project" button, Remind me, and share glyphs. Tabs run Campaign, Rewards, FAQ, Updates, Comments, Community. [project-light-default](screenshots/project-light-default.png). The full page is long and was truncated at the kit's eight-chunk ceiling.

## Auth boundary

`/login` and `/signup` both paint "Log in or sign up": email, a Cloudflare Turnstile check, a remember checkbox, a disabled Continue, and Sign in with Apple. Nothing was submitted. [login-light-default](screenshots/login-light-default.png).

## Start a project

`/start` is public for the first step: category and subcategory selects, and a Next button that stays inactive until a category is chosen. Next was not pressed. Later steps, the project editor, and launch sit behind an account. [start-light-default](screenshots/start-light-default.png).

## Content pages

About, rules, trust, press, creators, environment, and the blog are public marketing or policy pages on the same white chrome. [about-light-default](screenshots/about-light-default.png), [creators-light-default](screenshots/creators-light-default.png), [rules-light-default](screenshots/rules-light-default.png).

## Signed-in shell

Not captured on this public pass. Log in opens a dialog and the branch stops. Settings, saved projects, messages, and the account menu sit behind that wall. See [site-tree.md](site-tree.md) and [login-review.json](login-review.json).

## Not on the signed-out surface

Empty, loading, and error states of a submitted form, a destructive confirmation, and feedback after a pledge or a save. Those need an account or a checkout, recorded in the catalog gaps.
