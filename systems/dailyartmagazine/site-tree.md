# DailyArt Magazine public site tree

Mapped on 2026-11-21 from https://www.dailyartmagazine.com in headless Chromium at 1440 and 390. WordPress 7.1.5, theme `idvetmp-child`. Public magazine. No account wall on the pages below.

Shop and Courses are external stores. Their links are recorded and were not followed. PayPal donation links were not followed. Newsletter and contact fields were not filled. No form was submitted.

The hamburger menu lists 81 links. Category archives share one template, so two archives were photographed (Art Movements, Painting) and the rest are recorded as the same template.

## Header

The bar is `#top-header`, 65px, ink `#19191c`. It is on every page.

| Control | Opens |
|---|---|
| `#hamburger` | `nav.fixed-nav.navigation` with class `open`. A white panel of category columns. Same control at 390. Click again to close. |
| Logo (`a.logo`) | https://www.dailyartmagazine.com/ |
| Stories | https://www.dailyartmagazine.com/latest/ |
| Shop | http://shop.dailyartmagazine.com/ (external store, not followed) |
| Courses | http://courses.dailyartmagazine.com/ (external store, not followed) |
| Facebook icon | https://www.facebook.com/DailyArtMag/ (external, not followed) |
| Twitter icon | https://twitter.com/dailyartmag (external, not followed) |
| Instagram icon | https://www.instagram.com/dailyartmagazine/ (external, not followed) |
| Search (`button.primary.btn` labelled Search) | https://www.dailyartmagazine.com/?s= (search page, empty query). Does not open an overlay. |

## Menu panel

Opened by `#hamburger`. Column headings are links. Each child is a category archive of the same template as Art Movements, unless noted.

| Column | Heading opens | Children open |
|---|---|---|
| Art Movements | /category/art-movements/ | Prehistoric Art, Ancient Art, Ancient Egypt, Medieval Art, Renaissance, Mannerism, Baroque, Rococo, Neoclassicism, Romanticism, Academic Art, Realism, Symbolism, Impressionism, Art Nouveau, Post-Impressionism, Fauvism, Expressionism, Cubism, Surrealism, Dadaism, Abstract Expressionism, Pop art, Contemporary Art. Each is `/category/art-movements/<slug>/`. |
| Art Forms | /category/art-forms/ | Painting, Sculpture, Architecture, Photography, Design, Fashion, Theater & Cinema, Literature, Music, Dance. Each is `/category/art-forms/<slug>/`. |
| Regions | /category/regions/ | African Art, Art of Australia & Oceania, Asian Art, European Art, North American Art, South American Art. |
| Special | /category/special/ | Art History 101, Women Artists, Artist Stories, Museum Stories, Masterpiece Stories, Art Travels, Animals, Bizarre, Cats, Dine & Wine, Erotica, Love Story, Sport, Surprising Art History. Herstory opens /category/herstory/. History opens /category/history/. |
| Article Types | /category/article/ | Long Read, Review, Interview, News, Video. Quizzes opens /quizzes/ (a page, not a category). |

The same panel continues with site pages: About Us, Our Team, Contribute, Advertise, Contact Us, Cookie Policy, Privacy Policy, Newsletter Terms and Conditions, Website Terms and Conditions. Then Courses (https://shop.dailyartmagazine.com/product-category/digital-courses/, external, not followed) and Shop (http://shop.dailyartmagazine.com/, external, not followed), then the same three social icons.

## Footer

On every page. Labelled DAILYART.

| Control | Opens |
|---|---|
| About Us | /about-dailyart-magazine/ |
| Our Team | /dailyart-team/ |
| Contribute | /send-an-article/ |
| Advertise | /advertisement/ |
| Contact Us | /contact/ |
| Cookie Policy | /cookie-policy/ |
| Privacy Policy | /privacy-policy/ |
| Newsletter Terms and Conditions | /newsletter-terms-and-conditions/ |
| Website Terms and Conditions | /terms-of-service/ |
| Courses | https://shop.dailyartmagazine.com/product-category/digital-courses/ (external, not followed) |
| Shop | http://shop.dailyartmagazine.com/ (external, not followed) |
| Newsletter email field | Does not navigate. Not filled. |
| Newsletter checkbox | Does not navigate. Not checked. |
| Subscribe | Would submit `#newsletter-footer`. Not clicked. |
| Social icons | Same Facebook, Twitter, Instagram URLs as the header. Not followed. |

## Overlays

| Control | Opens |
|---|---|
| Donate (`button.donate.open-modal`) | `div.modal-r.modal-r--show` over a 90% black scrim. Copy plus five amount links. Close is `.modal-close-r`. |
| $5, $10, $25, $50, Monthly | PayPal donation URLs. Recorded as external checkout. Not followed. The URLs contain a business email, so they are not copied into this package. |
| Newsletter modal (`#newsletter-modal`) | Present in the DOM, not opened. Email field and Subscribe were not used. |
| Privacy Manager (`#pmLink`) | A button in the page. Not clicked. It is a consent control. |
| Close Ad | Hides a Freestar ad unit. Ads were hidden in captures, not accepted. |

## Home page

https://www.dailyartmagazine.com/

| Control | Opens |
|---|---|
| Featured story title and image | The featured article. On this capture, a story under / (slug changes). |
| Category badge on a card | That category archive. |
| Author name | /author/<slug>/ |
| Card title | That article. |
| Browse More | /trending/ in one band, /long-reads/ in another. |
| Load more (`button.load-more-arts`) | More cards on the same page. The click did not register in this run (the button was off-screen when clicked). Recorded, not treated as a new route. |
| In-page newsletter | Same as the footer form. Not filled. |

## Pages photographed

| Page | URL | What the page is |
|---|---|---|
| Home | / | Featured band and story cards |
| Latest | /latest/ | Story index |
| Art Movements | /category/art-movements/ | Category archive template |
| Painting | /category/art-forms/painting/ | Same archive template |
| Article | /siena-art-of-bronze-frick/ | Article template |
| Author | /author/zstanska/ | Author index. Public byline, not an account. |
| About | /about-dailyart-magazine/ | Static page |
| Team | /dailyart-team/ | Static page |
| Contribute | /send-an-article/ | Static page. Pitch form not filled. |
| Advertise | /advertisement/ | Static page |
| Contact | /contact/ | Contact Form 7. Fields not filled. |
| Quizzes | /quizzes/ | Quiz index |
| Search results | /?s=monet | Results for a public query loaded by URL, not by submitting the form |
| Search empty | /?s= | The page the Search button opens |
| Search focused | /?s= | Same page, field focused with the keyboard. No ring paints. |
| Login | /login | HTTP 404. Heading "Oooops! Page not Found". No password field. |
| Cookie, privacy, terms, newsletter terms | the four policy URLs | Static pages |
| Trending, long reads | /trending/ and /long-reads/ | Story indexes |
| Phone | home, menu, article, login, contact at 390 | Same chrome, stacked |

## Article controls

On /siena-art-of-bronze-frick/ and the same template elsewhere.

| Control | Opens |
|---|---|
| Category label (EUROPEAN ART and similar) | That category archive |
| Author name | /author/<slug>/ |
| Share row (Tweet This Post, Pin This Post) | A hash on the same URL in the contact page's copy. Not followed off-site. |
| Inline links in the body | Other magazine articles or category archives |
| Related cards | Other articles |

## Contact and contribute

| Control | Opens |
|---|---|
| Your name, Your email, Your message | Fields on the contact page. Not filled. |
| Terms of Use | /terms-of-service/ |
| Privacy Policy | /privacy-policy/ |
| Submit | Would post the contact form. Not clicked. |
| Contribute "here" | /send-an-article/ |

## Not on this site

| URL | Result |
|---|---|
| /login | 404 article page. No sign-in form. See login-review.json. |
| shop.dailyartmagazine.com | External store. Not entered. |
| courses.dailyartmagazine.com | External store. Not entered. |
| PayPal donate links | Checkout. Not entered. |
