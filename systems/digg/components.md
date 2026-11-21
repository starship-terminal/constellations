# Components

Public signed-out Digg, measured 2026-11-21. Values are token names where a token holds them. Crops were not cut: the screenshots show the control in place.

## Button

Sign up is `data-slot=button` `data-variant=default` `data-size=lg`. Height 40px, padding-left 16px, radius 26px, weight 500, size 14px. Fill `{color.blue.500}`, text `#ffffff`. Hover fill is an oklab mix, not a hex token. [screenshots/home-light-default.png](screenshots/home-light-default.png), hover in [screenshots/home-light-signup-hover.png](screenshots/home-light-signup-hover.png).

Log in and the theme cycle button are `data-variant=secondary`, same size. Light fill `#f0f0f5`. Continue on the login page is 36px tall, fully rounded, same blue. Follow on a profile matches Sign up, and clicking it opens the login wall.

The story **digg it** control is `data-variant=outline`, height 44px, radius 999px.

Pressed: the class includes `active:translate-y-px`. Not measured. Disabled and loading: not present.

## Icon button

Toggle Sidebar is a rail control, `aria-label` Toggle Sidebar. On the phone, Open navigation menu is the header icon button. [screenshots/mobile-home-light-feed.png](screenshots/mobile-home-light-feed.png).

## Link

Sidebar links are `data-slot=sidebar-menu-button`, height 40px, padding 4px 12px, radius fully round, size 14px, weight 600. The current topic uses the secondary fill. Others are transparent until hover, which uses the same fill. Story titles are 16px / 600, no underline. Footer links on About include contact and llms.txt.

## Text field

Login `#identifier-field` (`name=identifier`, placeholder "Enter your email address") and signup email and password fields: height 36px, padding 4px 10px, radius 8px, size 14px, weight 400, transparent fill. Password on signup has a show-password icon button. Nothing was typed. [screenshots/signup-light-default.png](screenshots/signup-light-default.png), focus in [screenshots/login-light-email-focused.png](screenshots/login-light-email-focused.png).

## Select

Feed View and Feed display are `data-slot=select-trigger`, height 36px, padding 8px 12px, radius 26px. Open listbox options: Trending, Best, Hot, Newest, Top, and Comfy, Compact. [screenshots/home-light-feed-view-open.png](screenshots/home-light-feed-view-open.png), [screenshots/home-light-feed-display-open.png](screenshots/home-light-feed-display-open.png).

## Switch

Cookie preferences has Analytics and Audience insights switches. They were not toggled. Essential is "Always on", not a switch. [screenshots/about-light-cookie-preferences.png](screenshots/about-light-cookie-preferences.png).

## Menu

The feed controls open listboxes. The phone navigation control opens a sheet with the topic links, the theme cycle, Log in, and Sign up. [screenshots/mobile-home-light-nav-open.png](screenshots/mobile-home-light-nav-open.png).

## Dialog

Cookie preferences is a dialog: title, two switches, Only necessary, Save preferences, Privacy Policy, Close. Save was not clicked.

## Card, list row, avatar, badge

Feed posts are `data-slot=item`, radius 18px, padding 14px 16px. The right rail holds Top Contributors (avatar plus handle) and Top Posts Today. Source avatars on a post are 24px and fully round. Topic labels are outline pills, height 36px. SPONSORED is a text label on an ad row.

## Gaps

Text area, checkbox, radio, tabs, tooltip, toast, and table are not present on the public pages. Validation, disabled, loading, and pressed states were not captured. Overlay and scrim colours were not read. The cookie dialog's own fill was not sampled as a token.
