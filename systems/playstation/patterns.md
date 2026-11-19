# Patterns

Signed-out pages only. Screenshots were not produced: `preview_snapshot` returned "The browser is not producing screenshot frames. For a desktop tab, show or restore the T3 Code window and try again." Layout numbers below are computed rectangles at innerWidth 1169, devicePixelRatio 2.

## Marketing home

`https://www.playstation.com/` redirected to `https://www.playstation.com/en-sg/`. Title: PlayStation® Official Site: Consoles, Games, Accessories & More. Locale `en-SG`.

The header section is white. The shared nav is 64px tall and 492px wide, holding Store, PS5, Games, PS Plus, Accessories, News, and Support. A blue Sign In pill sits in the web toolbar at 22 by 70 px. Search is an icon button.

The first hero (`.hp-hero__banner.theme--dark`) fills `rgb(9, 35, 145)` with white type. A later hardware block is `.theme--light` on white. Primary CTAs are transparent 28px-radius links, white on the dark hero and `rgb(0, 104, 189)` on light plates. Large titles are SST at 34px, weight 300.

The site footer (`.site-footer-v2.theme--dark`) fills `rgb(0, 67, 156)` with white type.

A OneTrust banner ("Sony Interactive Entertainment use cookies...") was showing. Decline was clicked. Accept was not clicked. No account control was used.

## Signed-out store

`https://store.playstation.com/en-sg/pages/latest`. Title: Latest | Official PlayStation™Store Singapore. Not a Cloudflare challenge.

Body is white with text `rgb(54, 54, 54)`. The same shared nav and Sign In pill sit above a row of store tabs. Latest is the active tab, fill `rgb(235, 238, 240)`, radius 24px. Product tiles are 313 by 261 px with a price line (sample text SGD136.00) and a black `-50%` badge on a deal. No item was added to a bag. No checkout was opened.

## Signup wall

Sign In on the store opened `https://my.account.sony.com/sonyacct/signin/` with hash `/signin/input/id`. Title: Sign In | PlayStation. Heading: Sign in to PlayStation, white, 22px, weight 300.

The step shows an email field labelled Sign-In ID (Email Address), a grey Next button, links for About Sony Account and Trouble Signing In?, and a Create an Account button. The email field was left empty. Next was not clicked. Create an Account was not clicked. No password, phone, card, or identity value was entered.

Html and body backgrounds both computed transparent. The heading and field text are white, so the plate reads dark, but no ancestor with a solid page fill was isolated. That page colour is a gap.

## Not captured

App shell after login, bag, checkout, payment, form validation, empty and loading states, destructive confirmation, search results, tables, onboarding, a site-wide dark theme, and a 390px layout. The viewport was the preview pane at 1169 by 731.
