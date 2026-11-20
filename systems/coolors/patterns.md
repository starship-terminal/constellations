# Coolors patterns

How the signed-in screens combine the components in [components.md](components.md).

## App header

A 60px white bar. The wordmark sits left. Tools opens a mega-menu of generators and discover links. Go Pro is a pink text button. The avatar replaces Sign in once `body` has `is-logged`.

## Palette generator

The create surface is `/generate`, which redirects to a palette URL such as `/264653-2a9d8f-e9c46a-f4a261-e76f51`. Five full-height columns fill the page under a thin toolbar (View, Export, Save, and icon tools). The hint is "Press the spacebar to generate color palettes!" Spacebar changes the palette in the page. Save, Export, and publish were not used.

At 390px the same palette stacks into five 146px rows, with Generate and an icon nav on a bottom bar.

## Library

`/dashboard` redirects to `/user/palettes`. A left rail lists Palettes, Colors, Gradients, Fonts, Images, Projects, Collections, and Favorites. The palettes view was empty: "You don't have any palette yet." Search and Filters sit above the empty state.

## Account

`/account` redirects to `/account/general`. The nav is General, Profile, Subscription, Affiliation, Settings, and Delete account. General holds username, email, and change password. Those fields were not edited and not submitted. Settings holds a newsletter checkbox, a private-profile Pro control, a landing-page select, and a white-label image control. None of those were changed.

## What was not opened

Delete account, Sign out, Go Pro checkout, Save, Export, affiliation, and the account theme submenu. Opening the theme submenu can write a preference, so dark remains a stylesheet reading.
