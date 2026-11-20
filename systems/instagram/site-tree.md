# Instagram public site tree

Mapped on 2026-11-21 from `https://www.instagram.com/` in headless Chromium, signed out, before screenshots. A control that opens a login or signup wall is recorded and that branch stops. No form was submitted. No password, code, or third-party login was used.

Theme is not a page. `color-scheme: light` sets `html.__fb-light-mode` (body `#ffffff`). `color-scheme: dark` sets `html.__fb-dark-mode` (body `#0c1014`). There is no public theme switch.

## Main page

`https://www.instagram.com/` is the login wall. Status 200. Title "Instagram". Copy: "See everyday moments from your close friends." / "Log into Instagram".

| Control | Opens | Stop? |
|---|---|---|
| Text field, placeholder "Mobile number, username or email" (`input` name `email`) | Stays on the login form. Typing is not a submit. | No |
| Password field (`input` name `pass`) | Stays on the login form. Not filled. | No |
| "Log In" (`role=button`) | Would submit the login form. | Yes. Not clicked. |
| "Forgot password?" | `https://www.instagram.com/accounts/password/reset/` (HTTP 403). Asks for mobile number, username, or email, then "Continue". | Yes. Wall. |
| "Log in with Facebook" | Facebook login. | Yes. Not clicked. |
| "Create new account" | `https://www.instagram.com/accounts/emailsignup/`. Asks for mobile number or email, then password. | Yes. Wall. |
| Footer "Meta" | `https://about.meta.com/` | Off product. Not captured. |
| Footer "About" | `https://about.instagram.com/` | Off product. Not captured. |
| Footer "Blog" | `https://about.instagram.com/blog/` | Off product. Not captured. |
| Footer "Jobs" | `https://about.instagram.com/about-us/careers` | Off product. Not captured. |
| Footer "Help" | `https://help.instagram.com/` | Off product. Not captured. |
| Footer "API" | `https://developers.facebook.com/docs/instagram` | Off product. Not captured. |
| Footer "Privacy" | Redirects to `https://privacycenter.instagram.com/policy/` | Off product. Not captured. |
| Footer "Terms" | Redirects to `https://help.instagram.com/581066165581870/` | Off product. Not captured. |
| Footer "Locations" | `https://www.instagram.com/explore/locations/` | No. Public. |
| Footer "Popular" | `https://www.instagram.com/popular/` | No. Public. |
| Footer "Instagram Lite" | `https://www.instagram.com/web/lite/` | No. Public. |
| Footer "Meta AI" | `https://www.meta.ai/` | Off product. Not captured. |
| Footer "Muse" | `https://muse.ai/` | Off product. Not captured. |
| Footer "Threads" | `https://www.threads.com/` | Off product. Not captured. |
| Footer "Contact Uploading & Non-Users" | Facebook Help. | Off product. Not captured. |
| Footer "Meta Verified" | Redirects to `https://www.instagram.com/accounts/login/?next=.../accounts/meta_verified/` | Yes. Login wall. |
| "Switch Display Language" (`select`, 53 options) | Reloads the same page in another language. | Not changed. English left as loaded. |

## Login wall, named URL

`https://www.instagram.com/accounts/login/` is the same form as the main page: mobile number, username, or email, plus a password, or Facebook. Branch stops.

## Locations

`https://www.instagram.com/explore/locations/` is public. Header: logo, "Log In", "Sign Up". Body: a country list (United States, Brazil, India, and the rest of the published list).

| Control | Opens | Stop? |
|---|---|---|
| Logo | `https://www.instagram.com/` | Yes. Login wall. |
| "Log In" | `https://www.instagram.com/accounts/login/?next=%2Fexplore%2Flocations%2F&source=desktop_nav` | Yes. Login wall. |
| "Sign Up" | `https://www.instagram.com/accounts/emailsignup/` | Yes. Signup wall. |
| A country, for example "United States" | `https://www.instagram.com/explore/locations/US/united-states/` | No. Public city list. |
| A city, for example "LosAngeles" | `https://www.instagram.com/explore/locations/c2420379/losangeles-united-states/` | Same pattern as the country page. One country page is the sample. The rest of the city list is the same control. |

## Popular

`https://www.instagram.com/popular/` is public. Same header as Locations. Body: topic cards ("See what's popular on Instagram"). A "Next" control pages the topic row. Dismiss controls sit on the topic cards.

| Control | Opens | Stop? |
|---|---|---|
| Logo, "Log In", "Sign Up" | Same walls as Locations. | Yes. |
| A topic card, for example the first published topic | `/popular/<topic>/?utm_source=popular_home` | No. Public topic page. |
| "Next" on the topic row | Stays on the page. Scrolls the card row. | No. |
| A pill on a topic page | `/popular/<related>/?utm_source=topic_pill` | Same pattern as the topic page. One topic is the sample. |

`https://www.instagram.com/explore/` redirects to the same popular page.

## Instagram Lite

`https://www.instagram.com/web/lite/` is public. "Download Instagram Lite". "Download APK" is a CDN file URL (not opened). "Get it on Google Play" is a store link (not clicked). Footer matches the main page.

## Official profile

`https://www.instagram.com/instagram/` is public. Title "Instagram (@instagram) • Instagram photos and videos".

| Control | Opens | Stop? |
|---|---|---|
| Logo, "Log In", "Sign Up" | Login or signup wall. | Yes. |
| Signup dialog on load ("See photos, videos and more from instagram" / "Sign up" / "Log in") | Signup or login. Escape closes it. | Dialog recorded. Sign up and Log in not clicked. |
| "View profile story" | A story viewer, then a login prompt if the viewer requires an account. | Recorded as a wall when it asks to log in. |
| "686M followers" (`href="#"`) | Dialog: "See their followers" / Sign up / Log in. | Yes. Wall. |
| "178 following" (`href="#"`) | Same follower-style signup dialog. | Yes. Wall. |
| Bio "more" (`help.instagram.com and 2 more`) | Expands the published bio. | No. |
| A highlight, for example "what's new" | `https://www.instagram.com/stories/highlights/<id>/` | Public viewer. Login and reply are walls. |
| Tab "Posts" (`aria-label` Posts, `aria-selected=true`, href `/instagram/`) | Post grid. | No. |
| Tab "Reels" (`aria-label` Reels, href `#`) | Reels grid on the same profile. | No. |
| Tab "Tagged" (`aria-label` Tagged, href `#`) | Tagged grid on the same profile. | No. |
| A post tile | `https://www.instagram.com/instagram/p/<id>/` | Public post page, with a "Sign up for Instagram to stay in the loop" prompt. Like, comment, and follow are not used. |
| A reel tile | `https://www.instagram.com/instagram/reel/<id>/` | Same class of page as a post. One post is the sample. |
| "See all" related profiles | `https://www.instagram.com/instagram/related_profiles/` | Public list. Follow buttons stop at login. |
| A suggested account | `/<handle>/` | Same public profile pattern. The official account is the sample. |

## Direct URLs that are walls or missing

| URL | Result |
|---|---|
| `https://www.instagram.com/accounts/login/` | Login wall. Stop. |
| `https://www.instagram.com/accounts/emailsignup/` | Signup wall. Stop. |
| `https://www.instagram.com/accounts/password/reset/` | Account-recovery wall. Stop. |
| `https://www.instagram.com/accounts/meta_verified/` | Redirects to login. Stop. |
| `https://www.instagram.com/explore/tags/photography/` | Redirects to `https://www.instagram.com/accounts/login/`. Stop. |
| `https://www.instagram.com/about/` | "Profile isn't available" plus "Sign up for Instagram". Not a product page. |
| `https://www.instagram.com/legal/` | A user profile named legal, not the terms. |
| `https://www.instagram.com/directory/profiles/` | 404, "Sorry, this page isn't available." |
| `https://www.instagram.com/directory/hashtags/` | 404, same error page. |

## Phone width

At 390x844 the same URLs load. The profile header stacks. The login form is the same wall. "Log In" on the missing-profile page uses `source=mobile_nav`.
