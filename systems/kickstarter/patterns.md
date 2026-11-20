# Kickstarter patterns

How the public signed-out surface is put together. Screenshots are in [screenshots/](screenshots).

## App shell

A white header: green wordmark, a search field, "For creators", "Log in", then a category row (Art through Theater, then Discover). Hovering a category opens a three-column panel of subcategories, filters, and a featured project. [home-light-default](screenshots/home-light-default.png), [home-light-category-menu](screenshots/home-light-category-menu.png).

On a 390-wide phone the category row scrolls sideways and a menu glyph sits at the right of the header. [mobile-home-light-default](screenshots/mobile-home-light-default.png).

A yellow status toast ("Abnormal System Error Rate on Sign in with Apple") was on the live site during this capture. It is page content, not a consent dialog.

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

Walked on 2026-11-20. The header swaps Log in for an avatar. The account menu lists Profile, Saved projects, Recommended for you, Following, Settings, Messages, Activity, and Log out. [recommendations-light-signed-in](screenshots/recommendations-light-signed-in.png), [menu-account-open](components/crops/menu-account-open.png).

On a 390-wide phone the same menu opens as a centred card over a dimmed page, with a close button. [account-menu-light-phone](screenshots/account-menu-light-phone.png).

Settings is a title, a tab row (Account, Edit profile, Notifications, Saved searches, Payment methods, Shipping address, Following), then the account card and a right-hand list of privacy, security, and delete links. [settings-account-light-default](screenshots/settings-account-light-default.png). Notifications is a list of rows with Email and App switches, left off. [settings-notifications-light-default](screenshots/settings-notifications-light-default.png).

Empty states are a sentence and one button: Discover projects on saved projects, Get started on Following. Messages is a search field, an Inbox select, and a yellow spam note. Activity is a short paragraph and a link. The profile says the page is only visible to the owner and shows a backed count of zero.

`/start` while signed in is step 1 of 3, with the same category selects and a disabled Next. Next was not clicked. [start-project-light-step1](screenshots/start-project-light-step1.png).

## Not on the signed-out surface

Empty, loading, and error states of a submitted form, a destructive confirmation, and feedback after a pledge or a save. Those need an account or a checkout, recorded in the catalog gaps.
