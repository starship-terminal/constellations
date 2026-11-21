# Dona public site tree

Mapped from [https://dona.ai/](https://dona.ai/) on 2026-11-21 with headless Playwright. Signed out. No form was filled. No password, code, captcha, or SSO control was used. Cookie **Accept** was not clicked. The cookie bar was hidden in captures so it would not cover the page.

Gatsby 4.25.2. Page components in the app bundle: `index`, `about`, `terms-of-service`, `privacy-policy`, `discord`, `twitter`, `404`. Unknown marketing paths render the 404 page with HTTP 404.

The product app is a separate host. Opening it signed out redirects to a login wall. That branch stops there.

## Tree

```
https://dona.ai/
├── header (every marketing page and the 404 page)
│   ├── logo link  →  https://dona.ai/
│   ├── About button  →  https://dona.ai/about/   (client route)
│   └── Login button  →  window.open https://app.dona.ai/   (new tab)
│                         which redirects to https://app.dona.ai/login   LOGIN WALL
├── home sections
│   ├── Watch video  →  in-page modal (YouTube iframe), same URL
│   ├── Try for free  →  window.open https://app.dona.ai   LOGIN WALL
│   ├── newsletter email field + Join our newsletter  →  POST https://api.dona.ai/signup
│   │     not submitted
│   ├── Follow us on Twitter  →  window.open https://twitter.com/getdona
│   │     visible only after a successful newsletter post; not reached
│   └── Join our Discord community  →  window.open https://discord.gg/ar9KGYjvAA
│         visible only after a successful newsletter post; not reached
├── footer (every marketing page and the 404 page)
│   ├── Terms of Service  →  https://dona.ai/terms-of-service/
│   ├── Privacy policy  →  https://dona.ai/privacy-policy/
│   └── Twitter icon  →  https://twitter.com/getdona   (new tab)
├── cookie bar (fixed, until Accept)
│   ├── Learn more  →  https://dona.ai/privacy-policy
│   └── Accept  →  writes localStorage cookieAllowed, hides the bar. Not clicked.
├── /about/
│   ├── same header and footer
│   └── team icon links (new tab), not followed:
│         https://twitter.com/jakubantalik
│         https://dribbble.com/antalik
│         https://twitter.com/aaroniker_me
│         https://dribbble.com/ai
│         https://www.instagram.com/aaroniker
│         https://twitter.com/nisargptel
│         https://nisarg.io/
├── /terms-of-service/
├── /privacy-policy/
├── /discord/   →  location replace https://discord.gg/P4Z4ua6sRS
│     (a different invite from the newsletter button)
├── /twitter/   →  location replace https://twitter.com/getdona
└── any other path  →  404 page
      └── Back to Home  →  https://dona.ai/

https://app.dona.ai/          redirects to /login     LOGIN WALL
https://app.dona.ai/login     email + password. Not filled.
    ├── Sign in               submit. Not clicked.
    ├── Forgot your password? →  /forgot-password
    └── Sign up for free      →  /register
https://app.dona.ai/register  name + email + password. Not filled.
    ├── Sign up               submit. Not clicked.
    ├── Forgot your password? →  /forgot-password
    └── Log in                →  /login
https://app.dona.ai/forgot-password   email field. Not filled.
    ├── Send password         submit. Not clicked.
    └── Log in                →  /login
```

No Google, Apple, Facebook, Microsoft, GitHub, or other SSO control was on the login, register, or forgot-password pages.

## Pages

| Page | URL | HTTP | Opens from | Screenshot |
|---|---|---|---|---|
| Home | https://dona.ai/ | 200 | logo, 404 Back to Home | [home-light-default](screenshots/home-light-default.png), [home-light-full](screenshots/home-light-full.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png) |
| About | https://dona.ai/about/ | 200 | header About | [about-light-default](screenshots/about-light-default.png), [about-light-full](screenshots/about-light-full.png), [mobile-about-light-default](screenshots/mobile-about-light-default.png) |
| Terms of Service | https://dona.ai/terms-of-service/ | 200 | footer link | [terms-light-default](screenshots/terms-light-default.png), [terms-light-full](screenshots/terms-light-full.png) |
| Privacy policy | https://dona.ai/privacy-policy/ | 200 | footer link, cookie Learn more | [privacy-light-default](screenshots/privacy-light-default.png), [privacy-light-full](screenshots/privacy-light-full.png) |
| Discord redirect | https://dona.ai/discord/ | 200 then off-site | no in-page control; page component only | not photographed after the redirect |
| Twitter redirect | https://dona.ai/twitter/ | 200 then off-site | no in-page control; page component only | not photographed after the redirect |
| 404 | any other dona.ai path, for example /pricing | 404 | direct | [notfound-light-default](screenshots/notfound-light-default.png), [mobile-notfound-light-default](screenshots/mobile-notfound-light-default.png) |
| Log in | https://app.dona.ai/login | 200 | header Login, Try for free, app root | [login-light-default](screenshots/login-light-default.png), [mobile-login-light-default](screenshots/mobile-login-light-default.png) |
| Sign up | https://app.dona.ai/register | 200 | Sign up for free on the login wall | [register-light-default](screenshots/register-light-default.png) |
| Forgot password | https://app.dona.ai/forgot-password | 200 | Forgot your password? | [forgot-light-default](screenshots/forgot-light-default.png) |

Paths probed and found to be the 404 page: /pricing, /blog, /login, /signup, /app, /download, /features, /changelog, /help, /support, /docs, /careers, /jobs, /press, /contact, /faq, /legal, /cookies, /cookie-policy, /watch, /video, /demo, /sitemap.xml. /robots.txt is a content-signal text file, not a page.

## Controls

### Header

Present on home, about, terms, privacy, and 404. At 390 the same three controls stay in one row. There is no hamburger, drawer, or menu.

| Control | Kind | Result |
|---|---|---|
| Logo (wordmark, link to /) | link | https://dona.ai/. The anchor is in the DOM. On the settled page the painted logo sits in a styled wrapper; a normal click on the anchor timed out because the anchor box was 0×0. Destination is the href. |
| About | button | Client navigation to https://dona.ai/about/. Confirmed from home and from /terms-of-service/. |
| Login | button | `window.open("https://app.dona.ai/", "_blank")`. The new tab lands on https://app.dona.ai/login. Login wall. Stop. |

### Home

| Control | Kind | Result |
|---|---|---|
| Watch video | button | Sets modal state. Does not change the URL. Opens a fixed overlay (`pages__Modal`, z-index 200, scrim `rgba(191, 195, 200, 0.8)`) with an iframe `https://www.youtube.com/embed/0_2xORiONDo` (autoplay query present on the live iframe). Inner panel max-width 1140px, radius 11px. A round close control paints at the top right of the viewport. Escape was pressed after the desktop shot. Phone shot: [mobile-home-light-video](screenshots/mobile-home-light-video.png). Desktop shot: [home-light-video](screenshots/home-light-video.png). |
| Try for free | button | `window.open("https://app.dona.ai", "_blank")`. Login wall. Stop. |
| Email field | input, placeholder "Enter your email" | Not typed. Empty submit was not used as a capture state. |
| Join our newsletter | submit | Would POST `{email}` to https://api.dona.ai/signup. Not submitted. On success the form swaps to "Thank you! You're in." and reveals Follow us on Twitter and Join our Discord community. Those two buttons are in the DOM under the success pane and are covered by the default pane until a successful post, so they were not clicked. |
| Follow us on Twitter | button, success pane | `window.open("https://twitter.com/getdona", "_blank")`. Not reached. |
| Join our Discord community | button, success pane | `window.open("https://discord.gg/ar9KGYjvAA", "_blank")`. Not reached. |

No tabs, accordion, search, filter, select, checkbox, radio, or switch on the home page. The product UI in the hero and feature sections is a recorded demo (video), not a live app.

### Footer

| Control | Kind | Result |
|---|---|---|
| Terms of Service | link | https://dona.ai/terms-of-service |
| Privacy policy | link | https://dona.ai/privacy-policy |
| Twitter icon | link, target blank | https://twitter.com/getdona. Not followed. |

### Cookie bar

Fixed bottom-left at desktop (radius 40px) and full-width along the bottom at phone width. Copy: "This website uses cookies."

| Control | Kind | Result |
|---|---|---|
| Learn more | link | https://dona.ai/privacy-policy |
| Accept | button | Writes `localStorage.cookieAllowed` and animates the bar away. Not clicked. Hidden with CSS for screenshots. |

### About

Same header and footer. Team rows are text plus icon links. No menu.

| Control | Kind | Result |
|---|---|---|
| Twitter / Dribbble / Instagram / personal site icons | links, new tab | The seven URLs in the tree above. Not followed. |

### Terms and privacy

Same header and footer. No in-page tabs, accordions, or search. Long text only.

### 404

| Control | Kind | Result |
|---|---|---|
| Back to Home | button | Client navigation to https://dona.ai/. Confirmed. |
| Header and footer | as above | As above. |

### Redirect pages

| URL | Behaviour |
|---|---|
| https://dona.ai/discord/ | `useEffect` sets `window.location.href` to https://discord.gg/P4Z4ua6sRS. Not followed past the assignment. |
| https://dona.ai/twitter/ | `useEffect` sets `window.location.href` to https://twitter.com/getdona. Not followed past the assignment. |

The newsletter Discord invite (`discord.gg/ar9KGYjvAA`) and the /discord/ invite (`discord.gg/P4Z4ua6sRS`) are different URLs.

### Login wall

No control on these pages was submitted. No field was typed.

| Page | Controls | Result |
|---|---|---|
| https://app.dona.ai/login | Email, Password, Sign in, Forgot your password?, Sign up for free | Sign in not clicked. Forgot goes to /forgot-password. Sign up goes to /register. |
| https://app.dona.ai/register | Name, Email, Password, Sign up, Forgot your password?, Log in | Sign up not clicked. Log in goes to /login. |
| https://app.dona.ai/forgot-password | Email, Send password, Log in | Send password not clicked. Log in goes to /login. |
| https://app.dona.ai/ | Redirects to /login | Stop. |

No theme switch, search, filter, tab, accordion, drawer, or dialog on the login wall.

## Not present on the public marketing site

- Dark or black page theme. The copy says the app has light, dark, and black. The marketing site paints Light only. The theme object read from the page is `id: "light"`.
- Search, filters, tabs, accordions, selects, checkboxes, radios, switches, toasts, tooltips, tables.
- A mobile menu. Header controls stay visible at 390.
- A public pricing, blog, docs, download, or changelog page.
- Signed-in app screens. Stopped at the login wall.
