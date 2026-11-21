# Patterns

Signed-out Twitch, 2026-11-21. The map of controls is [site-tree.md](site-tree.md).

## App shell

The home is a 50px top bar, a left rail of live channels, a featured player, and a grid under "Live on Twitch". The top bar paints transparent in both themes. A purple banner sits on the bottom edge: "Join the Twitch community!" with a white Sign Up pill.

![Home, dark](screenshots/home-dark-default.png)

![Home, light](screenshots/home-light-default.png)

At 390 CSS pixels the wordmark drops out, search becomes an icon, and the rail is gone. Log In and Sign Up stay in the top bar.

![Phone](screenshots/home-light-phone.png)

The user menu holds Language, Dark Theme, and Labeled Content. Dark Theme is the theme switch. See [screenshots/home-dark-user-menu.png](screenshots/home-dark-user-menu.png).

## Browse

Browse opens `/directory`: a Browse title, five illustrated chips (Games, IRL, Music & DJs, Creative, Esports), then Categories and Live Channels. Sort by opens Recommended For You and Viewers (High to Low).

![Directory](screenshots/directory-dark-default.png)

![Sort](screenshots/directory-dark-sort.png)

A category card opens a category page with Live Channels, Videos, and Clips, a Language menu, and a labeled-content notice. Manage Settings is a link to a help article, not an in-app settings page.

![Just Chatting](screenshots/category-dark-default.png)

![Language](screenshots/category-dark-language.png)

## Login and signup walls

Log In and Sign Up are dialogs on the home, not separate routes. Log In asks for Email or Username. Sign Up asks for Email and offers a phone link. Both offer Google, Amazon, and Apple. Continue stays disabled. Nothing was typed and no provider was clicked.

![Log in](screenshots/login-dark-default.png)

![Sign up](screenshots/signup-dark-dialog.png)

![Log in, light](screenshots/login-light-default.png)

## Search

The top-bar search is a split control. Focus paints a purple ring. No query was typed.

![Search focus](screenshots/home-dark-search.png)

## Downloads

More Options > Download Apps opens `/downloads`, a public grid of store buttons. No store was opened.

![Downloads](screenshots/downloads-dark-default.png)

## Empty, loading, error

The featured player shows "This video is either unavailable or not supported in this browser. (Error #4000)". That is the headless player. The signup dialog ships an "Email is invalid" sentence before typing. It is not a submitted error. A loading skeleton was not isolated.
