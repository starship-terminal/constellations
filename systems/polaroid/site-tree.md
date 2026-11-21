# Polaroid site tree

Mapped 2026-11-21 from the public storefront. `https://polaroid.com` redirects to `https://www.polaroid.com/en_sg`. Title: Polaroid EU | Official Online Store. Locale on the bar: SG · EN. Currency on the announcement bar is €. One light theme. `color-scheme` computed `normal`. No dark-theme control.

The cookie dialog was hidden in the browser, not submitted. No email, password, code, phone, or address was typed. No identity provider was clicked. No form was submitted. Confirm on the region dialog was not clicked. Continue, Add to Bag, and checkout were not used.

## Shell (desktop, 1440)

| Control | Opens |
|---|---|
| Announcement bar (`button`, aria-label "Toggle USPs overlay") | in-page overlay `#usps-overlay`. Copy: Free Standard Shipping over €95, Pay with Klarna, Shop sets. Same page. |
| SG · EN | dialog "Change region" (Country select, Language select, Confirm, close). Not submitted. |
| Wordmark (`a`, aria-label "Homepage link") | page `https://www.polaroid.com/en_sg` |
| Journal | page `https://www.polaroid.com/en_sg/blog/journal` |
| Education | page `https://www.polaroid.com/en_sg/blog/education` |
| Apps | page `https://www.polaroid.com/en_sg/pages/polaroid-apps` |
| Support | external `https://support.polaroid.com` |
| Account icon (`a`, aria-label "My Account") | page `https://www.polaroid.com/en_sg/account/login`. Login wall. Branch stopped. |
| Search (`button`, aria-label "Search") | search panel on the same page. Placeholder "Type to search". Popular searches: For beginners, Best-sellers, Film. A nonsense query shows "No results found". Not a personal query. |
| Bag (`a`, count 0) | page `https://www.polaroid.com/en_sg/cart`. Empty bag. Checkout not entered. |

Primary nav. Each label is a link. Hover opens a flyout on the same page. The link itself opens the category page. Holidays is red when it is the current item.

| Nav control | Page the link opens | Flyout (same page) |
|---|---|---|
| Holidays | `https://www.polaroid.com/en_sg/campaigns/all-sets` | Holiday-Ready Sets, Creative Gift Sets, Camera & Film Sets, Printer Sets, All Sets, Holiday Photo Tips, Gift Finder, Make it Creative |
| Cameras | `https://www.polaroid.com/en_sg/cameras` | All Cameras, Polaroid Mod, Polaroid Flip, Polaroid I-2, Polaroid Now+, Polaroid Now, Polaroid Go, Camera Sets, Camera Finder, Make it their camera |
| Specials | `https://www.polaroid.com/en_sg/collaborations` | All Collaborations, Polaroid x Pokémon, Polaroid x MoMA, Polaroid x Thrasher, Online Exclusive Sets, e-Gift Card, A wild gift appears! |
| Film | `https://www.polaroid.com/en_sg/film` | All Film, Film Pack Savings, i-Type Film, 600 Film, Go Film, SX-70 Film, 8x10 Film, Film Subscription, Gift Polaroid Film |
| Printers | `https://www.polaroid.com/en_sg/printers` | All, Polaroid Lab, Polaroid Hi·Print 3x3, Polaroid Hi·Print 2x3, Polaroid Hi·Print 4x6, Hi·Print paper sizes, Product Finder, Easy Printers. Great Gifts. |
| Accessories | `https://www.polaroid.com/en_sg/accessories` | All, Albums, Straps, Camera Bags, Frames, Go Accessories, Filters, Apparel, Shop Now |

## Phone (390)

The category row collapses. Account, Search, the wordmark, the bag count, and a hamburger stay in the header. The hamburger opens a full-page drawer on the same URL: Holidays, Cameras, Specials, Film, Printers, Accessories (each with a chevron), My Account, Journal, Education, Apps, Support, and SG · EN. Close returns to the same page. My Account in the drawer is the login wall. Branch stopped.

## Home `https://www.polaroid.com/en_sg`

| Control | Opens |
|---|---|
| Shop Bundles | campaign page under `/en_sg/campaigns/` |
| Get Inspired | journal or campaign page on the same site |
| Hero photography | no separate URL; the hero is the page |

## Catalogue and product

| Page | Extra controls | Opens |
|---|---|---|
| `/en_sg/cameras` | camera-type chips (New cameras, Mod, Flip, I-2, Now+, Now, Go, Sets) | filtered listing on the same page |
| `/en_sg/cameras` | Product Finder | page `https://www.polaroid.com/en_sg/gear-guide` |
| `/en_sg/cameras` | Filters · 0, Compare | in-page panels. Not submitted. |
| `/en_sg/film` | film-type chips, Film compatibility, Filters · 0 | in-page filters. Not submitted. |
| product page `/en_sg/products/polaroid-now-moma-edition` | gallery, Product info, Compatibility, member-price note | in-page disclosures. Add to Bag sits below the first viewport. Not clicked. |
| product tile on `/en_sg/cameras` | | product page, including `/en_sg/products/polaroid-mod-instant-camera` |

## Footer (every page)

About: Careers (external, jobs.ashbyhq.com), Affiliate Program, All Policies.

Support: Contact, FAQ's (support.polaroid.com), Cancel your order, Return your order.

Social: Instagram, TikTok, Youtube. External.

Cameras, Film, and Extras columns repeat the category links, plus Download Android app and Download Apple app.

Newsletter: "Join our newsletter." and a Sign up control. Not submitted.

Login and Become a member open the same login wall (`/en_sg/account/login` and `/en_sg/account/register`).

Legal row: Terms of Purchase, Terms of Use, Privacy Policy, Cookie Policy, Accessibility, Sitemap. A second SG · EN control sits in the legal row.

## Login walls (recorded, not entered)

| URL or control | What loaded |
|---|---|
| Account icon, footer Login, `/en_sg/account/login`, `/en_sg/account` | HTTP 200. Heading "Log in or sign up". Empty email field, Continue. No password field. No identity provider. Branch stopped. Nothing typed. |
| `/en_sg/account/register`, footer Become a member | redirects to `/en_sg/account/login`. Same empty wall. Branch stopped. |
| Phone drawer, My Account | same wall. Branch stopped. |

`login-extracted` stays `not-started`.

## Other public pages

| URL | What loaded |
|---|---|
| `/en_sg/cart` | heading Bag. "Your cart is currently empty." Go shopping. Checkout not entered. |
| `/en_sg/contact` | heading Contact Us. Customer Service and Membership cards. Forms not submitted. |
| `/en_sg/this-page-is-not-real` | HTTP 404. Heading "Uh oh!" Copy: this page doesn't exist in this version of reality. Go to homepage. |
