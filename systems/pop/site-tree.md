# Pop Site public tree

Mapped on 2026-11-21 from https://pop.site/ in headless Chromium before any
screenshot was taken. The marketing site is a Framer publish (generator
`Framer fb64017`, HTML comment "Published Nov 17, 2026 at 7:42 PM UTC").
`robots.txt` points at https://pop.site/sitemap.xml. There is no dark theme
toggle and no hamburger: `prefers-color-scheme: dark` leaves the page white,
and at 390 px the same header links stay in the bar.

Nothing on this tree was submitted. No email was typed. No password was
typed. Claim fields were left empty. The privacy form was not filled.

## How a control was classified

| Kind | What it means |
|---|---|
| Public page | Same host `pop.site` or `www.pop.site`, no password field, loaded signed out |
| Login wall | Host `app.pop.site`, or a page that asks for email and password, or Google. Recorded and not followed |
| External | Another host. Recorded and not captured |
| Published site | A `*.pop.site` subdomain that is someone else's published site. Recorded and not crawled |
| Interaction | Opens or changes something on the same page. No navigation |

## From the home page

https://pop.site/ (https://www.pop.site/ redirects here). Title: "Make a stunning site."

| Control | Opens |
|---|---|
| Logo (`data-framer-name="Black"`) | https://pop.site/ |
| Pricing | https://pop.site/pricing |
| Blog | https://pop.site/blog |
| Create Account | Login wall: https://app.pop.site/ (Sign Up, email, password, Continue with Google). Stopped |
| Log In | Login wall: https://app.pop.site/?signin (Sign in, email, password, Reset Password, Continue with Google). Stopped. Password was not submitted |
| Username field, placeholder `yourname` | Stays on the page. Five copies (hero and later claim bands). Not typed into |
| `.pop.site` suffix button | Stays on the page. No dialog |
| Claim your site / Claim your pop.site, empty field | Login wall: https://app.pop.site/ (Sign Up). Stopped. Not clicked again during capture |
| Theme row links (`https://framer.link/isaacdsign`, six of them) | External designer link. Not followed |
| FAQ question row (six, closed by default) | Same-page accordion. The icon button is the chevron. Opening one reveals its answer and does not navigate |
| oliur.pop.site | Published site. Not crawled |
| django.pop.site | Published site. Not crawled |
| Footer Sign In | Login wall: https://app.pop.site/. Stopped |
| Footer Blog | https://pop.site/blog |
| Footer Support | External: https://popsitesupport.framer.wiki/ |
| Footer Featured | https://pop.site/featured |
| Footer Press & Media | https://pop.site/pressandmedia-logos |
| Footer Terms | https://pop.site/terms |
| Footer Privacy | https://pop.site/privacy |
| Footer My Information | https://pop.site/myinformation |
| Footer GDPR & CPRA | https://pop.site/privacy (same page as Privacy) |
| Footer X (Twitter) | External: https://x.com/popdotsite |
| Footer Instagram | External: https://www.instagram.com/popdotsite |

Phone (390 px) shows the same header links (Pricing, Blog, Create Account,
Log In) with no extra menu control. The FAQ chevrons sit further down the page.

Home FAQ questions, each a same-page expand:

1. What is Pop Site?
2. Can I use Pop Site as my portfolio?
3. Can I build my business website on Pop Site?
4. Can I run my online school on Pop Site?
5. Can I run my membership on Pop Site?
6. Can I sell digital products on Pop Site?

## Pages reached from the home page

Each of these repeats the same header (Pricing, Blog, Create Account, Log In)
and the same footer. Those controls are not listed again. Create Account, Log
In and footer Sign In are the login wall on every page.

| Page | What is extra |
|---|---|
| https://pop.site/pricing | One claim field and Claim your pop.site. No plan picker, no toggle, no checkout. Heading: "Free to create and share." |
| https://pop.site/blog | Article cards, listed below. One claim field |
| https://pop.site/sections | Section marketing. Linked from the home copy, not from the header. Two claim fields. In the sitemap as a live page even though sitemap.xml omits it |
| https://pop.site/featured | "See Feature" / "See Award" cards. Each card leaves pop.site. Not followed |
| https://pop.site/pressandmedia-logos | Download SVG and Download PNG. Files on framerusercontent.com. Not downloaded into the package |
| https://pop.site/pressandmedia-product-mocks | Linked from the logos page. Download buttons for product mock PNGs on framerusercontent.com. Not downloaded |
| https://pop.site/terms | Long legal page. No extra controls |
| https://pop.site/privacy | Long legal page. One outbound link to https://www.memberspace.com/privacy |
| https://pop.site/myinformation | Privacy request form: Name, Email, four checkboxes (request a copy, delete, correct, opt out), Message, Submit. Not filled. Not submitted |
| https://pop.site/enterprise | 404. Not in the sitemap. Captured as the error state. The Framer 404 template's canonical is https://pop.site/404. Go home is a link back to https://pop.site/ |

## Blog articles

Every article is linked from https://pop.site/blog and listed in sitemap.xml.
Each ends in the same claim band. Three articles embed a YouTube poster whose
Play button swaps in a youtube.com embed on the same page. Play was pressed
once to confirm that; capture leaves the poster, because the embed is YouTube's
player, not Pop's UI.

| Path | Play button |
|---|---|
| /articles/meet-the-new-pop-site | no |
| /articles/why-pop-site-analytics-are-powerful | no |
| /articles/pop-site-vs.-squarespace-the-best-squarespace-alternative-in-2026 | yes, YouTube embed |
| /articles/introducing-the-pop-site-alerts-app-for-ios | yes, YouTube embed |
| /articles/introducing-the-new-shopify-pop-site-integration | no |
| /articles/pop-site-featured-see-who-s-talking-about-pop-site | no |
| /articles/why-pop-site-subdomains-are-better-for-your-brand-than-traditional-link-in-bio-tools | no |
| /articles/introducing-animated-themes | yes, YouTube embed |
| /articles/pop-site-is-featured-in-landbook | no |
| /articles/pop-site-is-featured-in-product-disrupt-issue-186 | no |
| /articles/launch-your-personal-brand-with-pop-site-a-free-linktree-alternative | no |
| /articles/use-pop-site-instead-of-squarespace-to-make-a-website-thank-us-later-(it-s-free) | no |
| /articles/pop-site-is-the-best-alternative-to-linktree-here-s-why | no |

## Featured cards (external, not followed)

| Label | URL |
|---|---|
| See Feature | https://www.awwwards.com/websites/technology/ |
| See Feature | https://www.lapa.ninja/post/pop-site/ |
| See Feature | https://toolfolio.io/blog/create-a-stunning-personal-site-effortlessly-with-customizable-templates |
| See Award | https://www.awwwards.com/sites/pop-site |
| See Feature | https://www.awwwards.com/websites/header-design/ |
| See Feature | https://land-book.com/websites/77843-pop-site-free-personal-site-builder-and-linktree-alternative |
| See Feature | https://productdisrupt.com/archive/?issue=186 |
| See Feature | https://greatstuff.fyi/ |
| See Feature | https://app.usepanda.com/ |
| See Feature | https://saaspo.com/pages/pop-site-landing-page |
| See Feature | https://dezignheroes.framer.website/web-builders |
| See Feature | https://websitevice.com/ |
| See Feature | https://refero.design/websites/679 |
| See Feature | https://verygoodalternatives.com/ |
| See Feature | https://webcatalog.io/en/apps/pop-site |

## Walls and branches not taken

| Control | URL recorded | Why the branch stops |
|---|---|---|
| Log In | https://app.pop.site/?signin | Email and password, or Google. Password was not submitted |
| Create Account, Claim your site (empty), footer Sign In | https://app.pop.site/ | Sign Up with email and password, or Google |
| Reset Password? | on the sign-in wall | Not clicked |
| Sign up, from the sign-in wall | on the sign-in wall | Not clicked |
| Continue with Google | on both walls | Not clicked |
| My Information form | https://pop.site/myinformation | Name, email, checkboxes, message. Not filled, not submitted |
| Published sites | https://oliur.pop.site/ and https://django.pop.site/ | Other people's sites |
| Support, social, featured cards, press downloads | listed above | Other hosts |

No menu, select, tooltip, toast, dialog, or theme switch exists on the public
pages. The only in-page interaction that changes layout is the home FAQ
accordion. The only video control is the YouTube poster Play button on three
articles.
