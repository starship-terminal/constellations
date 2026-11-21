# Savee public site tree

Mapped from https://savee.it on 2026-11-21, signed out. The request returned 200 and redirected to https://savee.com/. The page title was "Savee". This is a live marketing site, not a parked domain.

The marketing site and the public browse pages share one app. Light pages ship `html` class `theme-light` and paint `#fdfdfd`. Dark pages ship `theme-dark` and paint `#0e0e0e`. There is no theme switch on the public pages. The marketplace is a separate Shopify host at https://marketplace.savee.com/.

No email was typed. No password was typed. No code was typed. No phone or address was typed. No form was submitted. Continue with Google and Continue with Apple were not clicked. Apply now, Get Pro, Create team and Contact us were not followed into a form submit or a checkout.

## Header (desktop, 1440)

The wordmark and three labels sit in a 64 px bar. They are links, not flyouts. Hovering a label did not open a menu.

| Control | Opens | Stop? |
|---|---|---|
| Savee (wordmark) | `/` | |
| Features | `/features/` | |
| Teams | `/team/`, which redirects to `/team/create/` | |
| Pricing | `/upgrade/?source=nav_bar` | |
| Instagram | `https://instagram.com/letsavee` | Off-site. Not opened |
| X | `https://x.com/letsavee` | Off-site. Not opened |
| Log in | `/login/` | Stop. Empty wall only |
| Join for free | `/join/`, which redirects to `/login/` | Stop. Same empty wall |

On FAQ, search, item, profile, MCP and the other dark pages the bar shortens to Features, Marketplace, MCP, Log in, Join for free, plus a Get started link to `/login/`.

## Phone bar (390)

The labels collapse. An unnamed 20 px button at the right of the bar opens a drawer. Close is a button labelled Close. Escape also closes it.

| Control | Opens | Stop? |
|---|---|---|
| Savee | `/` | |
| Features | `/features/` | |
| Teams | `/team/` | |
| Pricing | `/upgrade/?source=nav_bar` | |
| Join for free | `/join/` | Stop. Empty wall only |
| Log in | `/login/` | Stop. Empty wall only |

A Google "Sign in to Savee with Google" sheet can appear over this drawer in an automated browser. It was not clicked. The committed phone menu shot is the drawer alone.

## Homepage

The page is one long light page. A fixed "Get the app / Scan with your phone" card sits at the bottom right on desktop (`max-md:hidden`). Close hides that card. It is not a page.

| Control | Opens | Stop? |
|---|---|---|
| Show another save (three buttons in the headline) | Swaps the inline save thumbnail on the same page | |
| Join for free | `/join/` | Stop. Empty wall only |
| See plans | `/upgrade/?source=home_pricing` | |
| Save (on the reference strip) | `/join/` | Stop. Not followed |
| Review tabs | Same page. Eight public review quotes | |
| Connect MCP | `/mcp/` | |
| Marketplace card | `/marketplace/`, which redirects to `https://marketplace.savee.com/` | |
| Design Masterclass card | `/workshop/` | |
| Create your site | `/site/create/` | |
| Create a team, Get Pro, Get Portfolio, Compare all plans | `/upgrade/?source=home_pricing` | Stop before checkout. The plan page is public. The buy buttons were not clicked |

## Features

`/features/` is a light marketing page. iOS and Android links leave the site (App Store, Play Store) and were not opened. Start exploring goes to `/join/` and was not followed.

## Pricing

`/upgrade/` is public. Yearly and Monthly are radios on the same page. FAQ questions are buttons on the same page. Get Pro, Get Portfolio and Create team were not clicked. They are the checkout boundary.

## Search and a public item

`/search/?q=typography` loads signed out and paints dark. Item tiles link to `/i/<id>/`. `/i/hcOfvOK/` loaded without an account. Title: "Green by Martin Naumann". More options opens a menu on the same page: Comments, Share, Download, Find original. Those items were not followed. Join and Log in on that page go to the wall and were not followed.

`/explore/` redirected to `/login/?next=%2Fpop%2F` and was not entered.

## Public profile

`/mnaumanndesign/` loads signed out. Follow was not clicked. A missing profile (`/this-profile-does-not-exist-xyz/`, which the app rewrites without hyphens) paints "Not found. This may have been deleted, or it's private." with Back to Home.

## Team, MCP, workshop, site, students, shortcuts, extension

| Page | Lands on | Notes |
|---|---|---|
| `/team/` | `/team/create/` | Dark. Create your team was not clicked |
| `/mcp/` | `/mcp/` | Dark. Client tabs (Claude Code, Cursor, ChatGPT & Codex, Other clients) stay on the page. Copy to clipboard was not used |
| `/workshop/` | `/workshop/` | Dark. English, episode row, Trailer. Start watching and Watch free were not followed into a player session |
| `/site/create/` | `/site/create/` | Light. Create your portfolio was not followed into an editor |
| `/students/` | `/students/` | Dark. Apply now was not clicked |
| `/shortcuts/` | `/shortcuts/` | Dark. A public shortcut list, not a table element |
| `/extension/` | `/extension/` | Dark. Store links were not opened |

## Contact

`/contact/` is a dark form: name, email, message, a reCAPTCHA field, and Contact us. Nothing was typed. Contact us was not clicked. The reCAPTCHA was not solved.

## Legal

`/terms/`, `/privacy/` and `/copyright-policy/` are public dark documents. Terms also links Privacy Policy, Community Guidelines, Copyright Policy, Trademark Policy, Platform Enforcement Policy. Those further policy links were not all opened. Terms and privacy were photographed.

## Marketplace

`/marketplace/` redirects to `https://marketplace.savee.com/`. It is a public product grid (Shopify). Filter opens a panel on the same page (sort radios, format checkboxes, a price range). Search was left empty. Log in there points at Shopify customer authentication and was not followed. Cart was not opened. No product was added.

## Blog

The footer Blog link goes to `https://inspire.savee.com/`. It was not opened on this pass.

## Footer

| Group | Items |
|---|---|
| About us | How it started (`https://inspire.savee.com/the-story-behind-how-we-built-savee/`), Features, Pricing, Keyboard Shortcuts, Students Discount, Blog, FAQ, Contact us |
| Downloads | iOS App, Android App, Figma Plugin, Chrome Extension, Safari Extension, Firefox Extension, Edge Extension |
| Features | Create your site, For Teams, Marketplace, Design Workshop, Savee MCP |
| Social | Instagram, X, Threads, YouTube |
| Legal | Terms, Privacy, Copyright |

Store, social and the Inspire blog links were not opened.

## Login and signup walls

`/login/` and `/join/` are the same wall. `/join/` redirects to `/login/`. `/signup/` and `/register/` do not exist: both paint the public Not found page.

The wall asks for Continue with Google, Continue with Apple, and an empty "Email or username" field. Continue is disabled until that field has a value. The lede is "Log in or sign up, no password needed." There is no password field. The field was left empty. Continue was not clicked. Google and Apple were not clicked.

A headless browser hit "We're making sure you are human" on this URL. Those frames were discarded. The committed wall shots are the empty form.
