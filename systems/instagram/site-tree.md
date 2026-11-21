# Instagram public site tree

Mapped on 2026-11-22 from `https://www.instagram.com/` in a signed-out browser, then photographed in headless Chromium. A control that opens a login or signup wall is recorded and that branch stops. No form was filled or submitted. No password, code, phone, address, or third-party login was used. Facebook was not clicked.

Theme is not a page. `color-scheme: light` sets `html.__fb-light-mode` (body `#ffffff`). `color-scheme: dark` sets `html.__fb-dark-mode` (body `#0c1014`). There is no public theme switch.

## Main page

`https://www.instagram.com/` is the login wall. Status 200. Title "Instagram". Desktop copy: "See everyday moments from your close friends." / "Log into Instagram".

| Control | Opens | Stop? |
|---|---|---|
| Text field, placeholder "Mobile number, username or email" (`input` name `email`) | Stays on the login form. Empty. | No |
| Password field (`input` name `pass`) | Stays on the login form. Empty. | No |
| "Log in" (`role=button`, disabled while both fields are empty) | Would submit the login form. | Yes. Not clicked. |
| "Forgot password?" | `https://www.instagram.com/accounts/password/reset/`. "Find your account". Asks for mobile number, username, or email, then "Continue". | Yes. Wall. Photographed empty. |
| "Log in with Facebook" | Facebook login. | Yes. Not clicked. |
| "Create new account" | `https://www.instagram.com/accounts/emailsignup/`. "Get started on Instagram with a Meta Account". Empty fields for mobile number or email, password, birthday, name, username, then "Submit". | Yes. Wall. Photographed empty. |
| Footer "Meta" | `https://about.meta.com/` | Off product. Not captured. |
| Footer "About" | `https://about.instagram.com/` | Off product. Not captured. |
| Footer "Blog" | `https://about.instagram.com/blog/` | Off product. Not captured. |
| Footer "Jobs" | `https://about.instagram.com/about-us/careers` | Off product. Not captured. |
| Footer "Help" | `https://help.instagram.com/` | Off product. Not captured. |
| Footer "API" | `https://developers.facebook.com/docs/instagram` | Off product. Not captured. |
| Footer "Privacy" | `https://www.instagram.com/legal/privacy/` (redirects toward the privacy center) | Off product. Not captured. |
| Footer "Terms" | `https://www.instagram.com/legal/terms/` | Off product. Not captured. |
| Footer "Locations" | `https://www.instagram.com/explore/locations/` | No. Public. |
| Footer "Popular" | `https://www.instagram.com/popular/` | No. Public. |
| Footer "Instagram Lite" | `https://www.instagram.com/web/lite/` | No. Public. |
| Footer "Meta AI" | `https://www.meta.ai/` | Off product. Not captured. |
| Footer "Muse" | `https://muse.ai/` | Off product. Not captured. |
| Footer "Threads" | `https://www.threads.com/` | Off product. Not captured. |
| Footer "Contact Uploading & Non-Users" | Facebook Help. | Off product. Not captured. |
| Footer "Meta Verified" | `https://www.instagram.com/accounts/meta_verified/?entrypoint=web_footer` redirects to login. | Yes. Login wall. Not entered. |
| "Switch Display Language" (`select`, 53 options) | Reloads the same page in another language. | Not changed. English left as loaded. |

## Login wall, named URL

`https://www.instagram.com/accounts/login/` is the same form as the main page: mobile number, username, or email, plus a password, or Facebook. Branch stops. Photographed empty.

## Signup wall

`https://www.instagram.com/accounts/emailsignup/` is public as a form and is a wall. Desktop shows the Meta Account signup with empty fields. Phone width (`390`) shows "What's your mobile number?" with an empty field, "Next", and "Sign up with email". Neither was filled. "Submit" and "Next" were not clicked.

## Password reset wall

`https://www.instagram.com/accounts/password/reset/` is public as a form and is a wall. "Find your account" / "Continue". The field was left empty. "Continue" was not clicked.

## Locations

`https://www.instagram.com/explore/locations/` is public. Header: logo, "Log In", "Sign Up". Body: a country list (United States, Brazil, India, and the rest of the published list). On a phone the same URL opens under a "Locations" title, and an "Get the full experience" sheet sits on top until it is dismissed. The sheet was dismissed for the country-list shot. "Open Instagram" and "Sign up" on that sheet were not clicked.

| Control | Opens | Stop? |
|---|---|---|
| Logo | `https://www.instagram.com/` | Yes. Login wall. |
| "Log In" | `https://www.instagram.com/accounts/login/?next=%2Fexplore%2Flocations%2F&source=desktop_nav` | Yes. Login wall. |
| "Sign Up" | `https://www.instagram.com/accounts/emailsignup/` | Yes. Signup wall. |
| A country, for example "United States" | `https://www.instagram.com/explore/locations/US/united-states/` | No. Public city list. |
| A city on that country page | A city page under `/explore/locations/`. | Same pattern as the country page. One country page is the sample. |

## Popular

`https://www.instagram.com/popular/` is public. Same header as Locations. Body: topic cards ("See what's popular on Instagram"), a "Next" control on the topic row, and public profile cards. `https://www.instagram.com/explore/` redirects here.

| Control | Opens | Stop? |
|---|---|---|
| Logo, "Log In", "Sign Up" | Same walls as Locations. | Yes. |
| A topic card | `/popular/<topic>/?utm_source=popular_home` | No. Public topic page. One topic is the sample class; the index is the captured page. |
| "Next" on the topic row | Stays on the page. Scrolls the card row. | No. Photographed. |
| "Dismiss" on a topic card | Removes that card from the row. | Not clicked. |
| A suggested profile | `/<handle>/` | Same public profile pattern. The official account is the sample. Follow buttons stop at login. |

## Instagram Lite

`https://www.instagram.com/web/lite/` is public. "Download Instagram Lite". "Download APK" is a CDN file URL (not opened). "Get it on Google Play" is a store link (not clicked). Footer matches the main page.

## Official profile

`https://www.instagram.com/instagram/` is public. Title "Instagram (@instagram) • Instagram photos and videos".

| Control | Opens | Stop? |
|---|---|---|
| Logo, "Log In", "Sign Up" | Login or signup wall. | Yes. |
| Signup dialog on load ("See photos, videos and more from instagram" / "Sign up" / "Log in") | Signup or login. Escape closes it. | Dialog recorded. Sign up and Log in not clicked. |
| "View profile story" | A story viewer, then a login prompt if the viewer requires an account. | Not entered. |
| "686M followers" (`href="#"`) | Dialog: "See their followers" / Sign up / Log in. | Yes. Wall. |
| "178 following" (`href="#"`) | Same follower-style signup dialog. | Yes. Wall. |
| Bio "more" (`help.instagram.com and 2 more`) | Expands a dialog that has held private handles. | Not clicked. |
| A highlight, for example "what's new" | `https://www.instagram.com/stories/highlights/<id>/` | Public viewer. Login and reply are walls. Not entered. |
| Tab "Posts" (grid icon, href `/instagram/`) | Post grid. | No. |
| Tab "Reels" (play icon) | Reels grid on the same profile. The icon shows a focus ring after a click. The grid itself did not swap in this pass. | Photographed as the focus state. |
| Tab "Tagged" (camera icon) | Tagged grid on the same profile. | Same control class as Reels. Not a separate page. |
| A post tile | `https://www.instagram.com/instagram/p/<id>/` | Public post page, with a signup prompt. Like, comment, and follow are not used. One post is the sample class; the grid is the captured page. |
| A reel tile | `https://www.instagram.com/instagram/reel/<id>/` | Same class of page as a post. |
| "See all" related profiles | `https://www.instagram.com/instagram/related_profiles/` | Public list. Follow buttons stop at login. |
| A suggested account | `/<handle>/` | Same public profile pattern. The official account is the sample. |

On a phone the profile loads under a "See full profile in the app" sheet. Hiding that sheet leaves a blank document, so the sheet is the phone profile state. "Open Instagram" and "Sign up" on it were not clicked.

## Direct URLs that are walls or missing

| URL | Result |
|---|---|
| `https://www.instagram.com/accounts/login/` | Login wall. Stop. |
| `https://www.instagram.com/accounts/emailsignup/` | Signup wall. Stop. |
| `https://www.instagram.com/accounts/password/reset/` | Account-recovery wall. Stop. |
| `https://www.instagram.com/accounts/meta_verified/` | Redirects to login. Stop. |
| `https://www.instagram.com/explore/tags/photography/` | Redirects to login. Stop. |
| `https://www.instagram.com/about/` | A missing profile, not a product about page. The about site is `https://about.instagram.com/`. |
| `https://www.instagram.com/directory/profiles/` | 404, "Sorry, this page isn't available." |
| `https://www.instagram.com/directory/hashtags/` | Same 404 class. |

## Phone width

At 390x844 the same URLs load, with a mobile user agent. The homepage is an app interstitial ("Open Instagram", "Log in or sign up") plus a cookie bar, not the desktop split form. The named login URL, signup, and password reset stay empty walls. Locations is a country list. Popular keeps the topic row and public profile cards. The official profile is the install sheet over the public header.
