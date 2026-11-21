# Buy Me a Coffee site tree

Mapped from the public homepage `https://buymeacoffee.com/` on 2026-11-21 in
headless Chromium at 1440×900, before screenshots. Each row is a control a
visitor can reach without an account, and what it opens. A branch that lands
on a login or signup wall is recorded and not followed.

The marketing site is a Nuxt app (`#bmc-header`). The blog and help center
are separate shells. The product (creator dashboard, payouts, shop admin)
sits behind `/login` and `/signup`.

## Header, desktop

The bar is `#bmc-header`. Apps and Resources are hover menus (`div.relative`,
panel class starts `hidden` until hover). Search creators is a click that
opens a modal. Nothing in the bar is a `<button>` on the marketing shell.

| Control | Opens |
|---|---|
| FAQ | Page `https://buymeacoffee.com/faq` |
| Wall of love (heart icon) | Page `https://buymeacoffee.com/reviews` |
| Apps (hover) | Menu. iOS opens the App Store (`https://apps.apple.com/in/app/buy-me-a-coffee/id1480229954`). Android opens Google Play (`https://play.google.com/store/apps/details?id=app.buymeacoffee`). Both leave the site. |
| Resources (hover) | Menu, two groups. Creator Tools: QR Code `https://buymeacoffee.com/qr-code`, Stream Alerts `https://buymeacoffee.com/stream-alerts`, Buttons `https://buymeacoffee.com/brand`. Comparisons: Ko-fi `https://buymeacoffee.com/ko-fi-alternative`, Patreon `https://buymeacoffee.com/patreon-alternative`, Kickstarter `https://buymeacoffee.com/kickstarter-alternative`, Ghost `https://buymeacoffee.com/ghost-alternative`, Podia `https://buymeacoffee.com/podia-alternative`, Gumroad `https://buymeacoffee.com/gumroad-alternative`, Memberful `https://buymeacoffee.com/memberful-alternative`, Teachable `https://buymeacoffee.com/teachable-alternative`. Then Request a feature, which opens a Typeform (`https://form.typeform.com/to/oCHpJ8qt`) and leaves the site, and Blog `https://buymeacoffee.com/blog`. |
| Wordmark | Page `https://buymeacoffee.com/` |
| Search creators | Dialog on the same page (`body.modal-open`, `.bmc-modal`). The field placeholder is "Search creators". Typing does not navigate. Close is the modal close icon. Not submitted as a search form. |
| Log in | Page `https://buymeacoffee.com/login`. Auth wall. Stop. |
| Sign up | Page `https://buymeacoffee.com/signup`. Auth wall. Stop. |

## Header, phone (390)

A hamburger (the fixed drawer starts off-screen with `-translate-x-full` and
`hidden md:block`) opens a full-screen white drawer.

| Control | Opens |
|---|---|
| Menu icon | Drawer: FAQ, Wall of love, iOS, Android, Start my page |
| FAQ | `https://buymeacoffee.com/faq` |
| Wall of love | `https://buymeacoffee.com/reviews` |
| iOS | App Store, leaves the site |
| Android | Google Play, leaves the site |
| Start my page | `https://buymeacoffee.com/signup`. Auth wall. Stop. |
| Close | Closes the drawer |

Apps and Resources are not in the phone drawer. Search creators is a desktop
control (`lg:hidden` on the trigger means it is hidden below the `lg` width).

## Homepage body

| Control | Opens |
|---|---|
| Start my page | `https://buymeacoffee.com/signup`. Auth wall. Stop. |
| Creator cards (Cara, Kaleigh Cohen, Double Take Reacts, The Thrill Of The Thrift, Beach Talk Radio, Simple Politics) | Public creator pages, for example `https://buymeacoffee.com/cara.app`. These are published pages, not the dashboard. |
| Footer columns | Same destinations as the Resources menu, plus About, Help Center, legal, and the product's own social accounts |

## Footer

Present on every marketing page. Help Center and the store and social links
leave `buymeacoffee.com`.

| Control | Opens |
|---|---|
| About | `https://buymeacoffee.com/about` |
| Help Center | `https://help.buymeacoffee.com/en/` (loaded, public knowledge base, different shell) |
| Apps: iOS, Android | Store listings, leave the site |
| Creator Tools: QR Code, Stream Alerts, Buttons | Same pages as the Resources menu |
| Comparisons | Same eight comparison pages as the Resources menu |
| Request a feature | Typeform, leaves the site. Not filled. |
| Blog | `https://buymeacoffee.com/blog` |
| Terms of Use | `https://buymeacoffee.com/terms` |
| Privacy Policy | `https://buymeacoffee.com/privacy-policy` |
| Community Guidelines | `https://buymeacoffee.com/community-guidelines` |
| Cookie Policy | `https://buymeacoffee.com/cookie-policy` |
| Security Policy | `https://buymeacoffee.com/security` |
| California Privacy Notice | `https://buymeacoffee.com/ccpa` |
| Accessibility Statement | `https://buymeacoffee.com/accessibility-statement` |
| Twitter, YouTube, Instagram | The product's own accounts. Not clicked (Twitter is in the do-not-click list). |
| Privacy, Terms (cookie bar area) | The same privacy and terms pages |

## Marketing pages reached from the homepage

All returned 200 and stayed on the path. Each repeats the header and footer.

| Page | What it adds |
|---|---|
| `/faq` | Question list (Who uses Buy Me a Coffee?, How do I get paid?, How can my audience pay?, fees, safety, ownership, difference from other platforms, building a business, who the team is, contact). "Contact support" and "Visit help center" point at the help center. |
| `/reviews` | Wall of love. Slide back and slide next move a carousel of public social mentions. |
| `/qr-code`, `/stream-alerts`, `/brand` | Feature pages. Brand kit shows logo, button and widget specimens. |
| `/*-alternative` (eight) | Comparison pages. Same shell as the homepage. |
| `/about` | Story page. |
| `/terms`, `/privacy-policy`, `/community-guidelines`, `/cookie-policy`, `/security`, `/ccpa`, `/accessibility-statement` | Legal prose. |

## Blog

`https://buymeacoffee.com/blog/` is a separate shell (WordPress). It has its
own Apps and Resources buttons, a search field (not submitted), and article
links such as `/blog/substack-writers-earn-beyond-subscriptions/`. One article
is captured as the article pattern. Search is not submitted.

## Public creator page

`https://buymeacoffee.com/cara.app` is a published page linked from the
homepage. It is the supporter-facing page, not the creator's dashboard.

| Control | Opens |
|---|---|
| Home | `https://buymeacoffee.com/cara.app` |
| Membership | `https://buymeacoffee.com/cara.app/membership` |
| Wishlist | `https://buymeacoffee.com/cara.app/wishlist` |
| Login (on the page) | `https://buymeacoffee.com/login`. Auth wall. Stop. |
| Coffee quantity radios (1, 3, 5, 10) and the quantity field | Local state on the support form. Not submitted. |
| Name, message, private and monthly checkboxes | Local form state. Not submitted. |
| Support | Would start a payment. Not clicked. |
| Join (membership tiers) | Would start a membership checkout. Not clicked. |
| Extras checkout links | `https://buymeacoffee.com/cara.app/extras/checkout/0` is a payment path. Not opened. |
| Report | `https://buymeacoffee.com/report`. Not opened (report form). |

## Auth walls (recorded, not followed)

| Control | URL | What it asks | Stop |
|---|---|---|---|
| Log in | `https://buymeacoffee.com/login` | Email field and "Continue with email". Also Continue with Google, Facebook, Apple, Twitter. | Yes. No email typed, no social button clicked. |
| Sign up, Start my page | `https://buymeacoffee.com/signup` | "Create your account", a name field (`yourname`), Sign up, and slide dots for a promo carousel. | Yes. No name typed, no form submitted. |

## Not on the public tree

The creator dashboard, payouts, shop admin, messages, and settings are not
linked from the homepage except through Log in and Sign up. Dark theme is
not offered on the public site (`color-scheme: normal`, no theme toggle).
Cookie consent did not mount a banner in this session (CookieYes scripts are
present, no dialog).
