# Drafts public site tree

Mapped on 2026-11-22 from [https://getdrafts.com/](https://getdrafts.com/) in an incognito preview tab, signed out. Desktop shots are 1440 × 900 CSS pixels at 2× (PNG 2880 × 1800, or taller when the page was captured full length). Phone shots are 390 × 844 CSS pixels at 2× (PNG 780 × 1688). The homepage returned the title "Drafts | Where Text Starts". The first visible heading is "How Drafts Works". The cover says "Drafts" and "Where Text Starts". This is a live marketing site, not a parked domain.

Nothing was typed. No email, password, code, phone, or address was entered. No form was submitted. No identity provider was clicked. No captcha was solved. `login-extracted` stays `not-started`.

origin/main did not have `systems/drafts/`. This is a first capture. The slug is `drafts`. `systems/drafts-ios/` was not created and was not on origin/main.

The product screens on the homepage (Mac, iPad, iPhone, Apple Watch) are a public illustration. They are not a signed-in account.

## How a control opens something

| Control | Gesture | Opens |
|---|---|---|
| Header Menu | click | White panel: Home, User Guide, Community, Directory, Script Reference, What's New. |
| Header logo | link | [/](https://getdrafts.com/) The image is `brand.svg` at opacity 0. The painted wordmark is in the cover photo. |
| Phone menu button | click | The same six links, in the collapsed nav. Close is the X. |
| App Store badges | link | Apple App Store. Not followed. |
| Cookie or consent card | none seen | No consent dialog was on the page. |
| Sign in or Sign up | none in the painted header or footer | Theme demo modals exist in the page source and stay closed. They were not opened. |

There is no site search on the marketing header. There is no pricing link on the marketing site.

## Header

Photographed: [home-desktop.png](screenshots/home-desktop.png), [home-desktop-menu.png](screenshots/home-desktop-menu.png), [home-phone.png](screenshots/home-phone.png), [home-phone-menu.png](screenshots/home-phone-menu.png).

| Control | Kind | Destination | This pass |
|---|---|---|---|
| Logo | link | [/](https://getdrafts.com/) | home |
| Menu | button, menu | panel below | photographed |

### Menu

Opened by click. Six links. The labels are set in small caps.

| Label | Destination | This pass |
|---|---|---|
| Home | [/](https://getdrafts.com/) | home |
| User Guide | [docs.getdrafts.com](https://docs.getdrafts.com/) | opened, first viewport |
| Community | [forums.getdrafts.com](https://forums.getdrafts.com/) | opened, first viewport |
| Directory | [actions.getdrafts.com](https://actions.getdrafts.com/) | opened, first viewport |
| Script Reference | [scripting.getdrafts.com](https://scripting.getdrafts.com/) | opened, first viewport |
| What's New | [docs.getdrafts.com/changelog](https://docs.getdrafts.com/changelog) | opened, first viewport |

The docs, directory, community, script reference, and changelog hosts are public. Deeper docs pages, directory search, and forum threads were not opened.

## Footer

On the homepage, five columns: brand, Get Drafts, Resources, Support, Legal.

| Column | Label | Destination | This pass |
|---|---|---|---|
| Brand | Where Text Starts | none | photographed |
| Get Drafts | iOS App Store | [App Store, iOS](https://apps.apple.com/app/apple-store/id1236254471?pt=273342&ct=Landing&mt=8) | not followed |
| Get Drafts | Mac App Store | [App Store, Mac](https://apps.apple.com/app/apple-store/id1435957248?pt=273342&ct=Landing&mt=8) | not followed |
| Resources | User Guide | [docs.getdrafts.com](https://docs.getdrafts.com/) | opened |
| Resources | Community | [forums.getdrafts.com](https://forums.getdrafts.com/) | opened |
| Resources | Drafts Directory | [actions.getdrafts.com](https://actions.getdrafts.com/) | opened |
| Resources | Script Reference | [scripting.getdrafts.com](https://scripting.getdrafts.com/) | opened |
| Resources | What's New | [docs.getdrafts.com/changelog](https://docs.getdrafts.com/changelog) | opened |
| Support | Get Help | [/support/](https://getdrafts.com/support/) | opened |
| Support | Mastodon | [indieapps.space/@drafts](https://indieapps.space/@drafts) | not followed |
| Legal | Terms of Service | [/support/terms](https://getdrafts.com/support/terms) | opened |
| Legal | Privacy Policy | [/support/privacy](https://getdrafts.com/support/privacy) | opened |

A hidden `rel="me"` link to the same Mastodon profile sits in the Get Drafts column. It is not painted.

## Pages opened

| URL | Title | Shot |
|---|---|---|
| [/](https://getdrafts.com/) | Drafts \| Where Text Starts | [home-desktop.png](screenshots/home-desktop.png) |
| [/](https://getdrafts.com/) at 390 | same | [home-phone.png](screenshots/home-phone.png) |
| [/support/](https://getdrafts.com/support/) | Drafts \| Where Text Starts | [support.png](screenshots/support.png) |
| [/support/privacy](https://getdrafts.com/support/privacy) | Drafts \| Where Text Starts | [privacy.png](screenshots/privacy.png) |
| [/support/terms](https://getdrafts.com/support/terms) | Drafts \| Where Text Starts | [terms.png](screenshots/terms.png) |
| a missing path, served as [/error](https://getdrafts.com/error) | Drafts \| Where Text Starts | [not-found.png](screenshots/not-found.png) |
| [docs.getdrafts.com](https://docs.getdrafts.com/) | Home \| Drafts User Guide | [docs.png](screenshots/docs.png) |
| [actions.getdrafts.com](https://actions.getdrafts.com/) | Drafts Directory | [directory.png](screenshots/directory.png) |
| [forums.getdrafts.com](https://forums.getdrafts.com/) | Drafts Community | [community.png](screenshots/community.png) |
| [scripting.getdrafts.com](https://scripting.getdrafts.com/) | Drafts Script Reference | [script-reference.png](screenshots/script-reference.png) |
| [docs.getdrafts.com/changelog](https://docs.getdrafts.com/changelog) | Release Notes \| Drafts User Guide | [changelog.png](screenshots/changelog.png) |

The 404 is the page at `/error`. A missing path such as `/pricing`, `/login`, and `/signup` is rewritten there. It says "Oops" and "We ran into an issue, maybe you were looking for..." and offers Drafts Home, User Guide, and Community. That is the empty state photographed this pass.

## Pricing

Not present on the public marketing site. There is no pricing nav item, no pricing footer link, and `/pricing` is the error page. Subscription copy appears inside the privacy policy ("Subscriptions and Accounts") as legal text, not as a price list.

## Download

Public. The homepage and the footer link to the iOS App Store and the Mac App Store. Those store pages were not opened. The badges were not clicked.

## Auth walls

No public login or signup page was found.

| Probe | Result |
|---|---|
| Header and footer | No Sign in and no Sign up control. |
| [/login](https://getdrafts.com/login) | Rewrites to [/error](https://getdrafts.com/error). |
| [/signup](https://getdrafts.com/signup) | Rewrites to [/error](https://getdrafts.com/error). |
| [/account](https://getdrafts.com/account) | Rewrites to [/error](https://getdrafts.com/error). |
| [signin-illustration.html](https://getdrafts.com/signin-illustration.html) | Linked only from closed theme demo modals in the page source. The URL itself rewrites to `/error`. |

The homepage HTML includes closed Bootstrap modals titled "Sign In", "Sign Up", "Schedule a demo with us", and "Add Payment". They are theme leftovers (Landkit-style copy: "Simplify your workflow in minutes", "We can help you solve company communication"). They are not in the painted header or footer. They were not opened, and nothing was typed into them.

The product is an Apple app. Account and purchase flows sit in the App Store and in the app. Those were not opened.

`login-extracted` stays `not-started`.
