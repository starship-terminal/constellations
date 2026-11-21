# Bear public site tree

Mapped on 2026-11-22 from the public homepage, signed out. Headless Chromium at 1440×900 and 390×844. The T3 preview confirmed the same homepage, help index, contact page, merch, wallpapers, privacy, the Chinese homepage, the blog, the community, and the empty walls. No email, name, password, or code was typed. No identity provider was clicked. No form was submitted. No captcha was solved. Checkout was not entered. The notes app was not entered.

`https://bear.app/` returns 200. The page is the live Bear marketing site (last modified 2026-11-17), not a parked page. The product is the Markdown notes app from Shiny Frog. There is no login or signup control on bear.app itself. Download goes to the App Store.

## Homepage controls

| Control | Opens |
|---|---|
| Logo (Bear) | https://bear.app/ |
| Features | https://bear.app/#features |
| Pricing | https://bear.app/#price |
| Blog | https://blog.bear.app/ |
| Community | https://community.bear.app/ |
| Merch | https://bear.app/merch/ |
| Support | https://bear.app/faq/ |
| Download | https://apps.apple.com/app/bear-markdown-notes/id1016366447 |
| Mac | Same page, Mac App Store badge: https://apps.apple.com/app/bear-markdown-notes/id1091189122?mt=12 |
| iPhone | Same page, iOS App Store badge |
| iPad | Same page, iOS App Store badge |

Features and Pricing are anchors on the homepage. They do not open a menu.

## Pricing

Public, on the homepage at https://bear.app/#price.

- Free: local notes, document scanning, export to TXT, Markdown, TextBundle, RTF, PDF, JPG, HTML, DOCX, ePub, 3 themes, 1 app icon, search inside PDFs and images, iCloud sync.
- Bear Pro: the same, plus 28+ themes and 15 app icons. A 7 day free trial, then $2.99/month or $29.99/year (15% off the yearly plan; the page says the saving can vary by currency and taxes).

No checkout button sits on the price block. Pro is sold in the apps. The blog post of 2026-11-10 says Bear Web is coming and that Bear Pro pricing changes on 2026-11-24. That post was not treated as a checkout.

## Footer

Groups: Bear, Support, Community, More.

- Bear: Features, Pricing, Bear for Mac, Bear for iOS
- Support: Help docs (https://bear.app/faq/), Contact us (https://bear.app/contact/), School Discount (https://bear.app/faq/educational-discount-program/), Api Docs (https://bear.app/faq/x-callback-url-scheme-documentation/)
- Community: Community (https://community.bear.app/), Twitter (https://twitter.com/bearnotesapp), Reddit (https://www.reddit.com/r/bearapp/), Facebook (https://www.facebook.com/BearNotes), Instagram (https://www.instagram.com/bearnotesapp/)
- More: Blog, Wallpapers (https://bear.app/wallpapers/), About us (https://www.shinyfrog.net/), Privacy (https://bear.app/privacy/), 中文版 (https://bear.app/zh/)
- Credit: Shiny Frog © 2025, linking to https://www.shinyfrog.net/

A newsletter line, "The Bear newsletter", sits above the footer on the homepage. Subscribe opens a Brevo form at `sibforms.com`. It was not opened and not submitted.

## Phone width

At 390 the header is the logo and a hamburger (`.navigation-mobile-menu`). Opening it shows Features, Pricing, Blog, Community, Merch, Support, and Download, plus a close control. Download was not followed. The homepage was photographed at 390 with the menu closed and open.

## Pages photographed

| Page | URL | Width |
|---|---|---|
| Home | https://bear.app/ | 1440 and 390 |
| Home, phone menu | https://bear.app/ | 390 |
| Pricing | https://bear.app/#price | 1440 |
| Help | https://bear.app/faq/ | 1440 |
| Merch | https://bear.app/merch/ | 1440 |
| Contact | https://bear.app/contact/ | 1440 |
| Wallpapers | https://bear.app/wallpapers/ | 1440 |
| Privacy | https://bear.app/privacy/ | 1440 |
| School discount | https://bear.app/faq/educational-discount-program/ | 1440 |
| API docs | https://bear.app/faq/x-callback-url-scheme-documentation/ | 1440 |
| Chinese home | https://bear.app/zh/ | 1440 |
| Not found | https://bear.app/this-page-does-not-exist-capture | 1440 |
| Blog | https://blog.bear.app/ | 1440 |
| Blog search, empty field | https://blog.bear.app/ | 1440 |
| Community | https://community.bear.app/ | 1440 |
| Community login wall | https://community.bear.app/login | 1440 |
| Community signup wall | https://community.bear.app/signup | 1440 |
| Bear Web sign-in wall | https://web.bear.app/ | 1440 |

## Help index

https://bear.app/faq/ is public. Heading: "Lost in space? Bear is here to help." An empty search field reads "Search the docs". It was not typed in. The index groups Get Started, Edit and format, Web clip and links, images and sketches, tags, navigation, Apple Watch and widgets, sync and privacy, migration, themes, shortcuts, export, and troubleshooting. Each article lives at `https://bear.app/faq/<slug>/`. Two footer articles were photographed: the school discount and the x-callback-url docs. The rest of the library was mapped from the index and not opened one by one.

`https://beta.bear.app/` redirects to the community. `https://bear.app/login`, `/signin`, `/signup`, `/account`, and `/download` return 404 and the same "This page wandered off" page.

## Stopped branches

Login and signup are recorded in [login-review.json](login-review.json). `login-extracted` stays not-started.

- Community Log In opens https://community.bear.app/login. Heading "Welcome back". Email / Username and Password were empty. "Log in with a passkey" was visible and was not clicked. "Email me a one-time login code" and "I forgot my password" were not clicked. Log In was not submitted.
- Community Sign Up opens https://community.bear.app/signup. Heading "Create your account". The email field was empty. Continue was not clicked.
- Bear Web at https://web.bear.app/ is a sign-in wall: "Sign in to access your notes in Bear." The only identity control is "Sign in with Apple". It was not clicked. A red banner says Bear Web will launch as part of Bear Pro and that new pricing takes effect on 2026-11-24. The grey shapes behind the card are a placeholder, not a signed-in session.
- Merch "Buy on Redbubble" leaves the site for a store. It was not followed. No checkout.
- App Store Download links were not followed.
- The support chat bubble was not opened. The contact page has no form. It points at that bubble and at bear-support@shinyfrog.net.
- The newsletter Subscribe link was not opened.
