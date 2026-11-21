# X public site tree

Mapped from https://x.com/ on 2026-11-21, signed out, in a T3 preview incognito tab. A control that opens a login or signup wall is recorded and that branch stops. No form was submitted. No email, password, code, phone, or address was typed. Phone, Google, and Apple were not clicked. Language was left on English.

The desktop homepage is the login wall, not a separate marketing page. Auth walls use the URL the browser landed on.

## Homepage controls

| Control | Opens | Then |
|---|---|---|
| Continue with phone | Identity provider | Not clicked |
| Continue with Google | Identity provider (Google Identity Services) | Not clicked |
| Continue with Apple | Identity provider | Not clicked |
| Email or username, Continue | Same page until text is entered. Continue stays a stone pill while the field is empty | Not typed. Not submitted |
| Terms of Service | https://x.com/tos | Lands on https://x.com/en/tos. Public |
| Privacy Policy | https://x.com/privacy | Lands on https://x.com/en/privacy. Public |
| Cookie Use | https://help.x.com/rules-and-policies/twitter-cookies | Help host. Headless Chromium hit Cloudflare. Not captured |
| Hidden Sign in | https://x.com/i/jf/onboarding/web?mode=login&redirect_after_login=%2F | Same empty login dialog as /login. Photographed empty. Stop |
| Scan to get the app | QR card on the page | Stay. The public download page is /download |
| About | https://about.x.com | Public marketing page |
| Get App | https://help.x.com/using-x/download-the-x-app | Help host. Not captured |
| Grok | https://grok.com/ | Off the product host. Not captured |
| Help | https://help.x.com | Help host. Headless Chromium hit Cloudflare. Not captured |
| Terms, Privacy | /tos, /privacy | Public legal pages |
| Cookies | https://support.x.com/articles/20170514 | Support host. Not captured |
| Careers | https://careers.x.com | Off the product host. Not captured |
| Ads & Business | https://business.x.com/advertising | Off the product host. Not captured |
| Developers | https://developer.x.com | Off the product host. Not captured |
| News | https://x.com/i/jf/stories/home | Public News, signed out |
| Accessibility | https://help.x.com/resources/accessibility | Help host. Not captured |
| More | Footer disclosure | Not opened this pass |

Phone width (390) replaces the pill stack with "See what's happening" and a Sign in link to the same onboarding login URL. Sign in was not followed.

## Second-level public controls

| Page | Control | Opens |
|---|---|---|
| /i/jf/stories/home | Category chips (Top Stories and the rest) | Same page with `?category=` |
| /i/jf/stories/home | Story card | /i/jf/stories/article/id/<id>. Public article. Not opened this pass |
| /i/jf/stories/home | Log in, Sign up | Onboarding walls. Photographed empty. Stop |
| /i/jf/stories/home | Back | Toward the homepage |
| /this-page-does-not-exist-capture | Search | /search, which redirects to the login wall. Not submitted |
| Missing route | Show more | /explore, which redirects to the login wall. Not followed |
| Missing route | Continue with phone | Signup wall with a redirect. Not clicked |
| Missing route | Log in with username or email | Login wall. Stop |
| /download | QR image | No links and no form. Stay |
| about.x.com/en | Who we are, Our priorities, Resources | In-page nav. Careers points at careers.twitter.com. Brand toolkit is /en/who-we-are/brand-toolkit. Those inner pages were not opened |
| about.x.com/en | Sign In | https://x.com/login?redirect_after_login=https://about.x.com/en. Public return URL, not a session URL. Not followed |
| about.x.com/en | System, Light, Dark | In-page theme. Light was pressed so the light page could be photographed |
| about.x.com/en | Download the X app | https://x.com/download |
| about.x.com/en | Language | Left on English |

## Walls (recorded, not entered)

- https://x.com/ is the desktop login wall. Photographed empty.
- https://x.com/login lands on https://x.com/i/jf/onboarding/web?mode=login. Dialog title "Log in to X". Email and password inputs were empty. Photographed empty. Stop.
- https://x.com/i/jf/onboarding/web?mode=signup is the signup dialog "Sign up for X". Photographed empty. Stop.
- https://x.com/explore redirects to the login dialog with `redirect_after_login=%2Fexplore`. Stop.
- https://x.com/search redirects to the login dialog with `redirect_after_login=%2Fsearch`. Stop. No query was typed.
- Continue with phone, Continue with Google, and Continue with Apple are identity providers. Not clicked.
- about.x.com Sign In was not followed.

## Not a public app state

The signed-in timeline, post composer, likes, follows, inbox, and settings are not reachable without an account. `login-extracted` stays `not-started`.
