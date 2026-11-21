# Components

Public Patreon, read on 2026-11-20. Crops were not cut. The states below were seen in full screenshots or measured on the live page. A value that was not read is Not captured.

## Button

Marketing Get Started is a white pill, 114×47, radius 30px, Oracle 13.5px weight 350, on the pricing header. See [pricing-light-default](screenshots/pricing-light-default.png).

Creator Join for free is a filled pill, 116×40, radius 9999px, fill rgb(175, 2, 16), white text, ABC Oracle Plus Variable 14px weight 550. Membership Join links are the same fill at radius 8px. See [creator-membership-light-default](screenshots/creator-membership-light-default.png).

Hover, focus-visible, pressed, disabled, and loading were not captured. Join was not clicked.

## Icon button

Explore carousel controls are 26×26, radius 9999px. The phone marketing sheet uses Open menu. See [explore-light-default](screenshots/explore-light-default.png) and [mobile-marketing-light-nav-sheet](screenshots/mobile-marketing-light-nav-sheet.png).

## Link

Marketing Log in is an Oracle text link, 13.5px weight 350, transparent fill, in a 30px radius hit area. App text links use `--TextLink-color-*`, declared, not measured on a live link.

## Text field

Explore search placeholder "Search creators or topics" sits in a pill. The input node itself measured transparent, 594×40, 14px weight 337. The painted pill is the parent. Marketing Find a Creator is 148×45, radius 45px. Help Center search was focused. See [explore-light-search-typed](screenshots/explore-light-search-typed.png) and [help-light-search-focused](screenshots/help-light-search-focused.png).

Nothing was submitted.

## Text area, select, checkbox, radio, switch

Not captured. No public page in this capture showed them without a form submit or a login wall.

## Tabs

Creator pages use Home, Posts, Quips, Collections, Shop, Membership, Recommendations, Chats. Explore uses topic chips (All, Pop culture, Comedy, and the rest). Selected All is a black pill in the screenshot. The button node measured transparent, so the fill is painted by an inner element. See [explore-light-default](screenshots/explore-light-default.png) and [creator-light-default](screenshots/creator-light-default.png).

## Menu

Marketing Creators, Features, and Resources are header buttons. Creators hover opens links to podcast, video, music, artist, and game pages. Share on a post opens Copy link, Share on X, Share on Facebook. Those share URLs were not opened. The account menu was mapped on the logged-out app home and is not in a screenshot in this package.

## Tooltip, dialog, toast

Not captured on the pages that stayed public. Chats, Notifications, and Join open a login wall. That wall was not screenshotted.

## Card

Explore topic cards are 243×84, radius 12px, fill rgb(249, 249, 249). Creator cards on Explore are photo tiles with a name and a category line. See [explore-light-default](screenshots/explore-light-default.png).

## List row, table, avatar, badge

Creator cards include avatars. A table was not on the captured public pages. List rows appear in the Help Center and in creator post lists. Badge values were declared as `--Badge-*` and not measured on an element.

## Gaps

- Logged-out app home screenshots, including the account menu and dark appearance, are not in this package. Later loads of `/` served the marketing homepage.
- Login, signup, Apple, and Facebook were not opened past the URL record in [site-tree.md](site-tree.md).
- Hover, focus-visible, pressed, disabled, loading, and error states were not measured on the painted controls.
- Focus ring colour is Not captured.
