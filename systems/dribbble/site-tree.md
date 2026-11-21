# Dribbble public site tree

Mapped on 2026-11-21 from the homepage at https://dribbble.com/ before any screenshot of this pass. The page title is "Browse thousands of images for design inspiration | Dribbble". It is a live product site, not a parked or captcha wall. The signed-out body class reads `logged-out`.

The T3 preview tab loaded the homepage and answered DOM reads. Preview screenshots failed twice because the browser was not producing frames. Menu contents below were read after hovering the header controls. Query strings are omitted. Nothing was typed. No identity provider was clicked. No form was submitted.

Opened means the control was used and the destination was loaded or photographed. Linked means the href was read and the page was not opened from that control. Help Center, social profiles, and designer profiles were not followed from the homepage. Log in and Sign up stay on dribbble.com. Those walls are recorded in [login-review.json](login-review.json).

## Header, desktop

The logo (`aria-label` Back to home page) links to `/`. Explore, Hire Talent, Get Hired, and Community are links that open menus on hover. The URL stays `/`. Sign up and Log in sit in the same bar. Start Project Brief is in the DOM at `/instantmatch` and paints 0 x 0 at this width.

| Control | Opens |
|---|---|
| Logo | `/` |
| Explore | `/shots/popular`, and a menu on the same URL. See below. |
| Hire Talent | `/hire`, and a menu on the same URL. See below. |
| Get Hired | `/browse-project-briefs`, and a menu on the same URL. See below. |
| Community | `/stories`, and a menu on the same URL. See below. |
| Start Project Brief | `/instantmatch` (present, not painted at 1440) |
| Sign up | `/signups/new` (signup wall) |
| Log in | `/session/new` (login wall) |

Explore, opened by hovering the header link. URL stays `/`.

| Control | Opens |
|---|---|
| Popular | `/shots/popular` |
| New and Noteworthy | `/shots/recent` |
| Product Design | `/shots/popular/product-design` |
| Web Design | `/shots/popular/web-design` |
| Animation | `/shots/popular/animation` |
| Branding | `/shots/popular/branding` |
| Illustration | `/shots/popular/illustration` |
| Mobile | `/shots/popular/mobile` |
| Typography | `/shots/popular/typography` |
| Print | `/shots/popular/print` |

Hire Talent, opened by hovering the header link. URL stays `/`.

| Control | Opens |
|---|---|
| Start Project Brief | `/instantmatch` |
| Browse Profiles | `/hire` |
| Explore Services | `/services` |
| Managed Creative Services | `/enterprise/managed-creative-services` |
| Browse Design Agencies | `/design-agency` |
| Post a Full-Time Job | `/jobs/new` |
| Learn more about how hiring works | `https://help.dribbble.com/articles/11083661` (linked, not followed) |

Get Hired, opened by hovering the header link. URL stays `/`.

| Control | Opens |
|---|---|
| Browse Project Briefs | `/browse-project-briefs` |
| Add Service | `/session/new` (login wall) |
| Full-Time Jobs | `/jobs` |
| Upgrade to Pro | `/pro` |
| Advertise with Us | `/designer-advertising` |
| Send Outbound Proposal | `/proposals` |
| Learn more about getting hired | `https://help.dribbble.com/articles/11083653` (linked, not followed) |

Community, opened by hovering the header link. URL stays `/`.

| Control | Opens |
|---|---|
| Blog | `/stories` |
| Playoffs | `/shots` |
| Help Center | `https://help.dribbble.com/` (linked, not followed) |
| Instagram | `https://instagram.com/dribbble` (linked, not followed) |
| X | `https://x.com/dribbble` (linked, not followed) |
| Pinterest | `https://www.pinterest.com/dribbble/` (linked, not followed) |
| YouTube | `https://www.youtube.com/dribbble/` (linked, not followed) |
| TikTok | `https://www.tiktok.com/@dribbble.com` (linked, not followed) |
| Threads | `https://threads.com/dribbble` (linked, not followed) |

The header also holds a search form (`role` search). Its type control is a button labelled Shots. The menu options are Shots, Designers, and Services. They switch the search index. They do not navigate. The field placeholder is "What are you looking for?". Submit was not pressed. At 1440 the header search paints 0 x 0. The same control is painted in the hero search strip.

## Header, phone (390)

The logo goes to `/`. The burger (`aria-label` Toggle mobile menu, class `site-nav-burger`) is the only other painted header control before it opens. Sign up is not painted in the bar. Clicking the burger opens a drawer on the same URL. The drawer shows a close control, the logo, and a Log in pill. Explore is expanded. Hire Talent, Get Hired, and Community stay collapsed. Their destinations match the desktop menus and were read from the open drawer, not followed.

| Control | Opens |
|---|---|
| Close | closes the drawer on `/` |
| Logo | `/` |
| Log in | `/session/new` (login wall) |
| Explore | `/shots/popular`, expanded in the drawer |
| Popular | `/shots/popular` |
| New and Noteworthy | `/shots/recent` |
| Product Design | `/shots/popular/product-design` |
| Web Design | `/shots/popular/web-design` |
| Animation | `/shots/popular/animation` |
| Branding | `/shots/popular/branding` |
| Illustration | `/shots/popular/illustration` |
| Mobile | `/shots/popular/mobile` |
| Typography | `/shots/popular/typography` |
| Print | `/shots/popular/print` |
| Hire Talent | `/hire`, collapsed accordion |
| Get Hired | `/browse-project-briefs`, collapsed accordion |
| Community | `/stories`, collapsed accordion |
| Start Project Brief | `/instantmatch` |

## Homepage body

URL stays `/` unless noted. Hero heading: "Work with the world's best in web design". The accent words (web design, mobile design, motion design, product design, brand design, UX/UI design) rotate in place. They are not routes.

A promo reads "Get 20% off your first payment for design and development services on Dribbble. Use code WELCOME20". Its Get Started link goes to `/instantmatch`. A close button (`aria-label` close) dismisses the promo. It was not clicked during the map.

| Control | Opens |
|---|---|
| Get Started, promo | `/instantmatch` |
| Start Your Project Brief | `/instantmatch` |
| Share Your Work | `/uploads/new` (upload wall, not followed) |
| Browse Project Briefs | `/browse-project-briefs` |
| Designer names in the hire row | public profile paths such as `/Moonsight` (one public profile was photographed; the row was not walked) |
| Popular sort, feed | menu on the same URL. See below. |

The hero search strip repeats the header search. The type button reads Shots. Options are Shots, Designers, and Services. The placeholder is "What type of design are you interested in?". Submit was not pressed. The pink Search circle is the submit control.

Pills under the strip, linked, not each opened:

| Control | Opens |
|---|---|
| dashboard, landing page, mobile app, portfolio, ecommerce, animation, illustration, onboarding | `/search/<slug>` |
| graphic designers, app designers, web designers, 3D designers, logo designers, UI/UX designers, product designers, brand designers | `/hire/<slug>` |
| landing page, mobile app, website redesign, dashboard, ecommerce, web development, logo design, brand identity | `/services/search/<slug>` |

Shot cards in the feed open `/shots/<id>-<slug>`. Designer names on those cards open public profiles. Promoted cards link out to `https://framer.link/mcp-26` (linked, not followed). Hide ads and PRO go to `/pro`. Advertise goes to `/advertise`.

Popular, opened as a sort control on the feed. URL stays `/`.

| Control | Opens |
|---|---|
| Popular | `/shots/popular` |
| New & Noteworthy | `/shots/recent` |

A floating project-brief card (`brief-floating-promo`) has a dismiss control (`aria-label` Dismiss banner). It was not clicked during the map. The capture hides that card rather than answering it.

The second heading offers Share your work, Offer your services, Send proposals, Create your profile, and Browse client briefs. Those actions lead to upload, signup, or login walls and were not submitted.

## Footer

The category marquee repeats Animation, Product Design, Illustration, Mobile, Web Design, Typography, Print, and Branding. Each goes to `/shots/popular/<slug>`.

| Control | Opens |
|---|---|
| Logo | `/` |
| For designers | `/for-designers` |
| Hire talent | `/hiring` |
| Inspiration | `/shots/popular` |
| Advertising | `/advertise` |
| Blog | `/stories` |
| About | `/about` |
| Support | `/contact` |
| X | `http://x.com/dribbble` (linked, not followed) |
| Facebook | `http://facebook.com/dribbble` (linked, not followed) |
| Instagram | `http://instagram.com/dribbble` (linked, not followed) |
| Pinterest | `http://www.pinterest.com/dribbble/` (linked, not followed) |
| Terms | `/terms` |
| Privacy | `/privacy` |
| Cookies | `/cookie-policy` |
| Jobs | `/directories/jobs` |
| Tags | `/tags` |
| Places | `/places` |
| Resources | `/resources` |

## Login and signup walls

Log in goes to `/session/new`. Sign up goes to `/signups/new`. Add Service in the Get Hired menu also goes to `/session/new`. Share Your Work goes to `/uploads/new`. Those walls were not used as a signed-in path. The empty login and signup cards were opened separately and photographed. No email, password, or code was typed. Google and every other identity provider were not clicked. Continue was not pressed.
