# Patterns

How the signed-in New York Times account and masthead combine. Light theme, 2026-11-21. Desktop shots are 1440 x 900 CSS at devicePixelRatio 2. The phone shot is 390 x 844 CSS at the same ratio.

## Account shell

![Email and settings](screenshots/account-settings-light.png)

The desktop account page is a white page with a slim wordmark bar, a left nav, and a single column of settings. The selected nav item carries a short ink rule. Sections open with a 2px rule, then a Franklin heading, then rows separated by hairlines.

The phone account page drops the left nav into a drawer and stacks the same rows. [account phone](screenshots/account-phone.png). Opening that drawer covers the page with a grey scrim. [account nav phone](screenshots/account-nav-phone.png).

## Empty list

![Reading list](screenshots/saved-empty-light.png)

Saved articles is a news-site page, not the account shell: masthead, ad slot, a Cheltenham-weight page title, a hairline, then one empty sentence with a bookmark glyph. The footer index sits at the bottom of the viewport. This account had no saved stories.

## Search

![Search empty](screenshots/search-empty-light.png)

![Search typed](screenshots/search-typed-light.png)

The masthead search opens in the header. Empty, the field is white with a hairline and a disabled Go. After text, Go fills with `core.color.go` and Clear appears inside the field. The query was typed and not submitted.

## Section drawer

![Section nav](screenshots/section-nav-light.png)

The hamburger opens a 240px white drawer over a scrim. Rows are Franklin 18/23, weight 600, with a chevron. Home, U.S., World, Business, Arts, Lifestyle, Opinion, Video, Shows, Games, Cooking, Wirecutter and The Athletic were listed. Only the drawer itself was opened. The search field that was already open sits clipped behind the drawer.

## What was not walked

Subscribe, gift, password create, connect, disconnect, profile update, delete account and log out were visible and not used. Games, Cooking, Wirecutter, The Athletic and Help Center were not entered. No article page was opened.
