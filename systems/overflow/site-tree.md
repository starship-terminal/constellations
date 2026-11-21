# Overflow public site tree

Mapped from https://overflow.io/ on 2026-11-21 with headless Playwright, before screenshots. Desktop viewport 1440x900. The cookie bar was hidden in the DOM for reading, never accepted or rejected.

Overflow is a marketing site for a desktop user-flow app. The signed-in product is not on these pages. https://overflow.io/login/ returns 404 ("Don't know where you are?"). https://overflow.io/n/signin is the sign-in wall. https://overflow.io/n/signup?buy is the purchase sign-up wall. Both branches stop there.

The site declares one light scheme (`color-scheme: normal`, body background `rgb(255, 255, 255)`). No theme toggle was found.

## Homepage chrome

| Control | Opens |
|---|---|
| Logo | https://overflow.io/ |
| Product (`a[href="#product-collapse"]`) | Mega menu `#product-collapse` (measured open, height 393px, `aria-expanded=true`). Items below. |
| Examples | https://overflow.io/examples/ |
| Blog | https://overflow.io/blog/ |
| Pricing | https://overflow.io/pricing/ |
| Sign In | https://overflow.io/n/signin (wall; stop) |
| Download for free | https://overflow.io/download/ |
| Skip to Content | `#content` |
| Cookie Statement | https://overflow.io/cookie-statement/ |
| Required only / Allow all | Cookie bar buttons. Not clicked. The bar is hidden in captures. |
| Watch product demo | Bootstrap dialog `[role=dialog].modal.fade.show` with a YouTube nocookie iframe (`ClUAaGHvJxY`) and Close. |
| Canvas view / Prototype view / Story presentation | Hash links (`#canvas-view`, `#prototype-view`, `#story-presentation`) that open the same product-demo dialog on a later frame of the video. They are not in-page tab panels. The selected class stayed on Canvas view in the first probe. The named screenshots show the dialog, not a switched page section. |
| Open example | https://overflow.io/s/Q4DI0PH6/ (public shared story) |
| Previous slide / Next slide | Testimonial carousel on the homepage. |
| Subscribe | Footer newsletter form (`input[name=email]`, placeholder "Your email"). Not filled. Not submitted. |
| Footer social icons | External: Twitter, Facebook, YouTube, Instagram, TikTok, LinkedIn. Not captured. |
| Email us | `mailto:` link. Not opened. Address not copied into this package. |
| Careers | https://protoioinc.com/careers/ (external). Not captured. |

## Product menu

| Item | Opens |
|---|---|
| How it Works | https://overflow.io/how-it-works/ |
| Features | https://overflow.io/features/ |
| Design presentation | https://overflow.io/design/presentation/ |
| Product Teams | https://overflow.io/teams/product/ |
| Design Teams | https://overflow.io/teams/design/ |
| Design Agencies | https://overflow.io/organizations/agencies/ |
| Tech Startups | https://overflow.io/organizations/startups/ |
| Agile Teams | https://overflow.io/teams/agile/ |
| Educational Institutions | https://overflow.io/organizations/education/ |
| Figma / Sketch / Adobe XD | External support articles on support.overflow.io. Not captured. |
| Jira | Atlassian Marketplace. External. Not captured. |
| Trello | trello.com power-up. External. Not captured. |
| See All Integrations | https://overflow.io/integrations/ |
| Pro / Compare Plans | https://overflow.io/pricing/ |
| Enterprise | https://overflow.io/enterprise/ |

## Footer (same on marketing pages)

| Item | Opens |
|---|---|
| How it works, Features, Integrations, Pricing | Same URLs as the header and product menu. |
| Overflow Stories | https://overflow.io/stories/ |
| Enterprise | https://overflow.io/enterprise/ |
| Start for free | https://overflow.io/download/ |
| Help Center | https://support.overflow.io/ (external). Not captured. |
| Support | Footer "Support" goes to the external help center. The on-site page https://overflow.io/support/ is in the sitemap and is captured. |
| Events | https://overflow.io/events/ |
| Our Story | https://overflow.io/blog/welcome-overflow-1-0/ |
| Media Kit | https://overflow.io/media-kit/ |
| Terms of Service | https://overflow.io/eula/ |
| Privacy Policy | https://overflow.io/privacy-policy/ |
| Cookie Statement | https://overflow.io/cookie-statement/ |
| PROTOIO Inc. | https://protoioinc.com/ (external). Not captured. |

## Sitemap pages not linked from the homepage

https://overflow.io/sitemap.xml lists 30 URLs. Extra marketing pages:

| URL | What it is |
|---|---|
| https://overflow.io/download/windows/ | Same download page, Windows build button. |
| https://overflow.io/landing/overflow-2.0/ | Overflow 2.0 landing page. |
| https://overflow.io/diagrams/user-flows/ | Article. Links to flowcharts, one case study, and public `/s/` examples. |
| https://overflow.io/diagrams/flowcharts/ | Article. Links back to user-flows and one case study. |
| https://overflow.io/dc/ | Design Critique Guide. Preview opens https://overflow.io/s/ZV0E9F. Zip download is a file, not a page. |
| https://overflow.io/support/ | On-site support page (the footer Support link is the external help center). |
| https://overflow.io/n/signup?buy | Sign-up wall (name, email, password, Google). Stop. |
| https://overflow.io/n/signin | Sign-in wall. Stop. |

## Page-local controls

| Page | Control | Opens |
|---|---|---|
| /features/ | Feature anchors | `#feature_sync`, `#feature_design`, `#feature_present`, `#feature_share`, `#feature_organize`, `#feature_feedback` |
| /pricing/ | FAQ accordion `.accordion__opener` | Expands `.accordion__item` in place. First item: "How does the free trial work?". No monthly/annual toggle was present. |
| /pricing/ | Plan CTAs ("Start free trial") | Not followed. The opened FAQ says a trial starts by signing up. The destination was not confirmed by navigation, so the branch stops. |
| /examples/ | Category anchors | `#high-fidelity-user-flows`, `#early-stage-ideation`, `#wireframe-user-flows`, `#capture-existing-flows`, `#hybrid-flow`, `#cross-device-flows`, `#side-by-side-comparison`, `#version-history`, `#moodboard`, `#flowchart`, `#user-story-mapping`, `#sitemap-and-ia`, `#mind-map`, `#timeline` |
| /examples/ | Example card | Public shared player `/s/<id>/`. `.overflow` file links are downloads, not pages. |
| /blog/ | Post card | One post template: https://overflow.io/blog/how-infinite-red-uses-overflow-to-improve-asynchronous-communication-with-their-clients plus Our Story. The blog index is paginated; further posts are the same template. |
| /download/ | Download for Mac / Download for Windows | File download. Not followed as a page. |
| /s/Q4DI0PH6/ | Player chrome | Same document can open `?node=…&prototype` and `/story/<id>`. Story view has an "Ok, got it" coach mark. |
| Phone 390 | `button.navbar-toggler` ("Toggle navigation") | Collapsed header menu. First probe click did not expand the nav links into view; recapture records the live result. Sign in inside that menu is the wall. |

## Walls and stops

| URL | Why the branch stops |
|---|---|
| https://overflow.io/n/signin | Email, password, Forgot password, Sign in, Sign in with Google, Sign in with SSO. No field filled. No button pressed. |
| https://overflow.io/n/signup?buy | First name, last name, email, password, Terms checkbox, Sign up, Sign up with Google. No field filled. No button pressed. |
| https://overflow.io/login and https://overflow.io/login/ | 404 product-page miss. Not a sign-in form. |
| External hosts | support.overflow.io, marketplace.atlassian.com, trello.com, protoioinc.com, social networks. Not part of the public overflow.io tree. |

## Shared player, not a second product

`/s/<id>/` is a public shared Overflow document (canvas, prototype query, story route). One example from the homepage and one from /examples/ stand in for the family. The rest of the example ids are the same player.
