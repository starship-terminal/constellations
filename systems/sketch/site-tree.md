# Sketch public site tree

Mapped from the homepage at https://www.sketch.com/ on 2026-11-20, before screenshots. Desktop viewport 1440×900. Phone viewport 390×844. Headless Chromium. No form was submitted. No email was typed.

The marketing site is one origin, `www.sketch.com`. Header items Product, Explore and Support are disclosure menus (their links live in `.main-nav__subnav`). Pricing is a direct link. Sign In and Get started are direct links. On a 390-wide viewport the same lists sit behind the header Menu button (`aria-controls="main-nav-menu"`).

## Header controls (desktop)

| Control | Opens | Stop? |
|---|---|---|
| Skip Navigation | `#content` on the current page | no |
| Sketch wordmark | [/](https://www.sketch.com/) | no |
| Product (subnav, hover or focus) | Design, Collaboration, Prototyping, Developer Handoff, AI, All Features, plus the latest changelog card | no |
| Explore (subnav) | Changelog, Roadmap, Blog, Design Resources, Plugins & Integrations | no |
| Pricing | [/pricing/](https://www.sketch.com/pricing/) | no |
| Support (subnav) | Help Center, Documentation, Request a Feature, Contact Us, Community Discord | Discord is off-site; Contact Us is a form page, not submitted |
| Sign In | [/signin/](https://www.sketch.com/signin/) | auth wall: email, password, Apple, Google, SSO. Branch stops |
| Get started | [/downloads/mac/](https://www.sketch.com/downloads/mac/) | download page, no account form submitted |
| Menu button | hidden at 1440 (the bar is expanded). On 390 it opens `#main-nav-menu` | no |

Desktop hover probe (subnav parents): `Product` open=true; `Explore` open=true; `Support` open=true.

Menu button at 1440: visible=false, aria="Toggle menu", controls=main-nav-menu, expanded=false.

## Phone menu

The Menu button does not flip `aria-expanded` (it stayed `false`). It opens `.mobile-nav` (panel visible: true). That drawer lists Product, Explore and Support links directly. Close is `.mobile-nav__close`. `#main-nav-menu` stays `display: none` at 390.

## Home interactions that are not navigations

| Control | Opens |
|---|---|
| Promo banner ("New in Sketch") | /changelog/ghent/ |
| In-page section nav (`.page-nav`, `.top-bar`) | hash targets on the homepage (`#design`, `#prototype`, `#collaborate`, `#about`) |
| Newsletter form in the footer | email field plus a marketing-consent checkbox and Sign up. Not filled. Not submitted |
| Grid-layout toggle | an internal layout debug control (`main-nav#toggleGridLayout`). Not a public page |
| Tooltip triggers on Pricing | `.tooltip-trigger` buttons. Hover/focus only; no navigation |
| Billing toggle on Pricing | Yearly / Monthly buttons. In-page state |
| Currency select on Pricing | USD / EUR. In-page state. Not a form submit of account data |

## Auth wall (branch stops)

[/signin/](https://www.sketch.com/signin/) shows "Sign in to Sketch", an email field, a password field, Continue with Apple, Continue with Google, Continue with SSO, Forgot Password, Sign In, and Create an account. Password is not submitted. No email is typed. Create an account, Forgot Password, Apple, Google and SSO are not clicked.

The Mac app, the web app workspace, and the iOS app sit behind that wall or an App Store listing. They are not captured.

## Form pages (opened, not submitted)

Contact Us ([/support/contact/](https://www.sketch.com/support/contact/)) is recorded as a form page. Fields are not filled.

## Public pages reached from the homepage

- / — labels: Home — via footer
- /about-us/ — labels: About Us — via footer
- /ai/ — labels: AIConnect your AI client / AI — via header-subnav, footer, phone-menu
- /beta/ — labels: Beta — via footer
- /blog/ — labels: Blog — via header-subnav, footer, phone-menu
- /careers/ — labels: Careers — via footer
- /changelog/ — labels: Changelog — via header-subnav, footer, phone-menu
- /changelog/ghent/ — labels: New Component variants, sections, and more 17 Nov / New in Sketch promo — via header-subnav, promo-banner
- /collaborate/ — labels: CollaborationWork better, together / Collaboration — via header-subnav, footer, phone-menu
- /design-resources/ — labels: Design Resources — via header-subnav, footer, phone-menu
- /design/ — labels: DesignCreate with precision / Design — via header-subnav, footer, phone-menu
- /docs/ — labels: Documentation — via header-subnav, footer, phone-menu
- /downloads/mac/ — labels: Get started — via header-subnav, home-page-nav
- /education/ — labels: Free for Education — via footer
- /feature-requests/ — labels: Request a Feature — via header-subnav, footer, phone-menu
- /features/ — labels: All FeaturesEverything in one place / All Features — via header-subnav, footer, phone-menu
- /handoff/ — labels: Developer HandoffFrom design to code / Developer Handoff — via header-subnav, footer, phone-menu
- /legal/ — labels: Terms & Policies — via footer
- /license/ — labels: Manage License — via footer
- /partners/ — labels: Partners — via footer
- /plugins/ — labels: Plugins & Integrations — via header-subnav, footer, phone-menu
- /pricing/ — labels: Pricing — via header, footer, phone-menu
- /privacy/ — labels: Privacy Policy — via footer
- /prototype/ — labels: PrototypingBring ideas to life / Prototyping — via header-subnav, footer, phone-menu
- /roadmap/ — labels: Roadmap — via header-subnav, footer, phone-menu
- /security/ — labels: Security — via footer
- /support/ — labels: Help Center — via header-subnav, footer, phone-menu
- /vs/figma/ — labels: Figma to Sketch — via footer

## Off-site (recorded, not walked)

- https://developer.sketch.com/ — Developer Platform — via footer
- https://status.sketch.com/ — Service Status — via footer
- https://mastodon.design/@Sketch — (unlabelled) — via footer
- https://apps.apple.com/app/sketch-view-and-mirror/id1609224699 — View & Mirror on iOS — via footer
- https://discord.gg/ascPpfDSSV — Community Discord — via header-subnav, footer, phone-menu
- https://www.youtube.com/c/SketchDesign/ — (unlabelled) — via footer
- https://www.instagram.com/madewithsketch/ — (unlabelled) — via footer
- https://bsky.app/profile/sketch.com — (unlabelled) — via footer
- https://x.com/sketch — (unlabelled) — via footer

## Sitemap

`/sitemap.xml` lists hundreds of documentation, blog, changelog and support articles. Those are the same public marketing/docs surface, not extra product UI. The capture visits the section indexes linked from the homepage (docs, blog, changelog, support, plugins, design resources) plus one article each where a homepage card links it. It does not crawl all 800 sitemap URLs.

## Walls and skips

| URL | Why the branch stops |
|---|---|
| https://www.sketch.com/signin/ | Email and password, or Apple, Google, or SSO |
| Create an account / Forgot Password (linked from the sign-in page) | Account creation and recovery. Not opened |
| Newsletter Sign up | Form. Not submitted. No email typed |
| https://www.sketch.com/support/contact/ | Contact form. Page may be opened; fields not filled |
| Discord, X, Bluesky, Instagram, YouTube, Mastodon, App Store, developer.sketch.com, status.sketch.com | Off-site. Recorded only |
