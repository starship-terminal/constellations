# Patterns

How the public pages combine. Screenshots are in [screenshots/](screenshots/). The map of which control opens which page is [site-tree.md](site-tree.md).

## Login wall

`https://www.instagram.com/` and `https://www.instagram.com/accounts/login/` are the same form. Desktop is a split: a phone mock on the left, the form on the right, a footer of legal and product links. Phone width replaces the form with "Open Instagram" and "Log in or sign up", plus a bottom tab bar that does not navigate while signed out.

[login-light-default.png](screenshots/login-light-default.png), [login-dark-default.png](screenshots/login-dark-default.png), [mobile-login-light-default.png](screenshots/mobile-login-light-default.png)

## Directory shell

Locations, a country page, and Popular share one header: wordmark, a blue "Log In" pill, a "Sign Up" text link. Locations is a four-column country list. Popular is a chip row, then topic cards, then profile cards. "Log In" and "Sign Up" leave the page for the login or signup wall.

[locations-light-default.png](screenshots/locations-light-default.png), [popular-light-default.png](screenshots/popular-light-default.png)

## Public profile

`https://www.instagram.com/instagram/` shows the avatar, counts, bio, highlight row, icon tabs, and a post grid. Followers and following open a signup dialog. That dialog was closed with Escape on desktop. On the phone the page opens under an "Open Instagram" sheet.

[profile-light-default.png](screenshots/profile-light-default.png), [mobile-profile-light-default.png](screenshots/mobile-profile-light-default.png)

## Download

Instagram Lite is a centred mark, one sentence, a "Download APK" button, and a Google Play badge. The APK link and the Play badge were not followed.

[lite-light-default.png](screenshots/lite-light-default.png)

## Missing page

`/directory/profiles/` returns the older "Sorry, this page isn't available." layout, with a blue "Log in" text link.

[missing-light-default.png](screenshots/missing-light-default.png)

## Not captured

The signed-in shell (home, search, reels, messages, create, profile menu) sits behind the login wall. Signup, password reset, Facebook login, and Meta Verified stop at a credential form. No form was submitted.
