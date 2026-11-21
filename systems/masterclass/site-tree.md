# MasterClass public site tree

Mapped from the live homepage `https://www.masterclass.com/` on 2026-11-21 in the T3 preview browser (incognito), before screenshots. Signed out. No form was submitted. No Google, Apple, or other identity provider was clicked. A control that opens a login, signup, subscribe, or identity-provider wall is recorded and that branch stops.

Official product: MasterClass (`www.masterclass.com`). Related public hosts linked from the homepage: `oncall.masterclass.com`, `learn.masterclass.com`, `careers.masterclass.com`, `privacy.masterclass.com`. Those hosts are recorded as leaves, not crawled.

## Shell (desktop 1440 and phone 390)

The same header is on marketing pages. Desktop shows Certificates, On Call, Executive, At Work, Browse, Search, Gifts, View Plans, Log In and Get MasterClass. Phone width collapses the product links into a Menu button.

| Control | Opens |
|---|---|
| MasterClass logo | `/` |
| Skip To Main Content | `#mc-main` (in-page) |
| Certificates | `/certificates` |
| On Call | `https://oncall.masterclass.com/` (other host, stop) |
| Executive | `/executive` (redirects to `/executive/program-details`) |
| At Work | `/for-business` |
| Browse | Dialog "Dropdown menu" on the same page. Close button dismisses it. |
| Search field "What do you want to learn today?" (`#searchInput`) | Dialog "Dropdown menu" of popular searches. Typing shows class result links. Enter is not pressed. |
| Gifts | `/gift` |
| View Plans | `/checkout` (plan picker, account step is a login wall) |
| Log In | `/auth/login` (login wall, stop) |
| Get MasterClass | `/promotion` |
| Hamburger (phone, unlabeled icon at the right of the header) | Dialog "Dropdown menu" on the same page. See Menu dialog. A button labelled Menu exists in the desktop DOM at 0 by 0 and does not paint. |
| Close banner | Dismisses the promo strip on the same page. Not a consent POST. |

## Menu dialog (phone)

Opened by the unlabeled hamburger at the right of the phone header. Close dismisses it. Search in this dialog is the same search field, not a submitted query. The 390 by 844 shot clips Executive and At Work below the fold.

| Control | Opens |
|---|---|
| Close | Closes the dialog |
| MasterClass | Stays in the dialog (product label) |
| View Plans / Get 50% off | `/checkout` |
| Gifts | `/gift` |
| Support | `/help-center` |
| Log In | `/auth/login` (login wall, stop) |
| Get MasterClass | `/promotion` |
| Certificates | `/certificates` |
| On Call | `https://oncall.masterclass.com/` (other host, stop) |
| Executive | `/executive` |
| At Work | `/for-business` |

## Browse dialog

Buttons, not links. Clicking a category opens a nested list of subtopics in the same dialog and stays on `/`. The nested items are also buttons. View All Categories is the only link.

| Control | Opens |
|---|---|
| Acting & Performing Arts, Art & Design, Business & Entrepreneurship, Community & Government, Film & TV, Food & Drink, Games & Digital Media, Health & Wellness, Music, Outdoor Adventures & Events, Science & Technology, Sports & Athletics, Writing | Nested subtopic list in the same dialog. Food & Drink opened: Bake Delicious Bread & Pastries, Cook Hearty Pasta & Rice Dishes, Craft Nutritious Flavorful Meals, Create Healthy & Tasty Vegetarian Meals, Elevate Everyday Cuisine, Elevate Your Cooking Skills & Techniques, Explore Global Cuisines & Food Culture, Make Everyday Meals Gourmet, Make The Most Of Your Ingredients, Pair Wines, Mix Cocktails, & Brew Coffee, Prepare Fresh Seafood Recipes, Refine Your Beef, Chicken, & Meat Dishes, Spice Up Your Food With Sauces & Herbs. Those buttons stay in the dialog. |
| View All Categories | `/categories` |
| Close | Closes the dialog |

## Homepage interactions

| Control | Opens |
|---|---|
| Intent buttons (career, AI, acting, lifestyle, science, chef, style, something else) | Selects an option on the same page. Continue is present. Not submitted: it starts the class-finder quiz, which asks for goals and ends at signup. |
| Pause carousel / Previous / Next / Go to slide N / Page N of 3 | Moves the hero or a card row on the same page |
| Watch Trailer | Dialog with a sample video player (Play, Mute, speed, fullscreen). Escape closes it. |
| Category chips (Trending, Acting & Performing Arts, and the same list as Browse) | Filters the card row on `/`. "See all" under Trending is a link to `/categories/trending`, which redirected to `/categories` on 2026-11-21. |
| Class cards | `/classes/<slug>` |
| Explore Classes | `/find-my-classes` (quiz) or `/promotion`, depending on the block |
| Try Certificates | `/certificates` |
| Contact Sales | `/for-business/purchase` |
| Learn More (At Work block) | `/for-business` |
| FAQ buttons (What is MasterClass?, membership, where to watch, which classes, cost, taxes, guarantee) | Accordion on the same page |
| Footer email + consent checkbox | Newsletter form. Not filled. Not submitted. |
| Hero email + terms checkbox (some pages) | Signup field. Not filled. Not submitted. |

## Search dialog

| Control | Opens |
|---|---|
| Popular Searches: Improve my writing, Photography tips, Business lessons, Filmmaking and music, How to be a better chef | Class or category result links. A click leaves the homepage. |
| Typed query results | `/classes/<slug>` links in the dialog. Enter is not pressed, so no search-results URL is submitted. |

## Category and catalogue

`/categories` lists every public category as a link:

| Link | Path |
|---|---|
| All classes | `/categories/all-classes` |
| Acting & Performing Arts | `/categories/acting-performing-arts` |
| Art & Design | `/categories/design-creative-arts` |
| Business & Entrepreneurship | `/categories/business-entrepreneurship` |
| Community & Government | `/categories/community-gov-3` |
| Film & TV | `/categories/film-television-production` |
| Food & Drink | `/categories/culinary` |
| Games & Digital Media | `/categories/digital-content-gaming` |
| Health & Wellness | `/categories/health-wellness-3` |
| Music | `/categories/music-3` |
| Outdoor Adventures & Events | `/categories/outdoor-adventures-events` |
| Science & Technology | `/categories/science-tech-3` |
| Sports & Athletics | `/categories/sports-athletics` |
| Writing | `/categories/writing-3` |

Session teasers on that page link to `/sessions/classes/<slug>`. One category page (`/categories/culinary`) and one session page stand in for the pattern. The other category slugs are the same template.

## Class page (`/classes/<slug>`)

Sample: `/classes/gordon-ramsay-teaches-cooking` (Gordon Ramsay Teaches Cooking I).

| Control | Opens |
|---|---|
| Watch Trailer / Trailer | Trailer dialog or player on the page |
| Sample | Sample lesson player on the page (public sample, not the signed-in lesson) |
| View lesson plan | Expands the lesson list on the page. Lesson playback past the sample is a member wall. |
| Play, Mute, 1x, Enter Fullscreen | Player controls |
| Get MasterClass / View Plans | `/promotion` or `/checkout` |
| Related class cards | Other `/classes/<slug>` |

## Plans, gifts, quiz

| Page | What it is | Stop |
|---|---|---|
| `/promotion` | Public offer page. Category chips and class cards. Promo terms link `/terms/newmember-PBF-40`. | Email fields not filled |
| `/gift` | Gift landing. Audience chips (For Dad, For Mom, and so on) filter cards on the page. Gift checkout link is `/checkout?gift=true`. | Checkout account step is a wall |
| `/checkout` | Plan picker. Steps: Membership, Account, Payment. "Log in" is on the page. | Account and payment not entered |
| `/find-my-classes` | Quiz. Steps: Interests (checkboxes), Goals, Classes For You. Back and Next. | Not completed. It leads into signup. |

## Certificates, Executive, At Work

| Page | Public controls | Stop |
|---|---|---|
| `/certificates` | Explore Certificates, certificate cards (`/certificates/<slug>`), annual pass `/certificates/annualpass`, video Play. Sign Up and Log In (`/auth/login?next_page=%2Fcertificates`). Email field not filled. | Signup, login, `/certificates/annualpass/checkout` |
| `/executive` then `/executive/program-details` | PROGRAM, INSTRUCTORS, CURRICULUM, LOG IN, APPLY FOR FREE (`/executive/enrollment/application`). Subject links `/executive/subjects/<slug>`. | Application form not filled. Login not clicked. |
| `/for-business` | How It Works `/for-business/how-it-works`, Skills Library `/for-business/skills`, Purchase Now, cart `/for-business/cart`, enterprise gift checkout. Contact form (name, email, company, job, phone, seats). | Form not filled. Cart and purchase not submitted. |
| `/for-business/purchase` | Contact Sales destination from the homepage. | Form not submitted |

## Help, legal, editorial

| Page | Notes |
|---|---|
| `/help-center` | Product hubs: `/help-center/masterclass`, `/help-center/certificates`, `/help-center/executive`, `/help-center/oncall`, `/help-center/masterclass-at-work`. Search field is the site search, not submitted. |
| `/help-center/masterclass` | Article list. One article captured: refund answer linked from the footer. |
| `/articles` | Article index with category chips and pagination (page 2 is a link). One article captured. |
| `/sitemap` | Index of categories, classes and articles. Used as the map, not crawled in full. |
| `/newsroom` | Company Information `/newsroom/about`, Press `/newsroom/press`, Contact. |
| `/terms` | Terms. Related: `/ai-terms`, `/policies`, `/gift-terms`. |
| `/privacy` | Footer also links `https://privacy.masterclass.com/` (other host). |

## Footer leaves (not crawled)

App Store, Google Play, Amazon app store, Roku, Twitter, Instagram, Facebook, YouTube, LinkedIn, `learn.masterclass.com` (member wins, DEI, security, grants), `careers.masterclass.com`.

## Login and signup walls (branch stops)

| URL | What happened on 2026-11-21 |
|---|---|
| `https://www.masterclass.com/auth/login` | Stays on MasterClass. Dialog offers Log In With Google, Log In With Facebook, Log In With Apple, Log In With Email, Sign Up, Reset Password, and Log in with your organization (`/auth/discovery`). None of those were clicked. No email was typed. |
| Checkout Account step, certificate Sign Up, Executive LOG IN, quiz completion, lesson playback past the sample | Recorded as walls. Not entered. |

## Not present on the public site

Dark theme toggle. Signed-in library, lesson player, notes, downloads, account settings, toasts after an account action, destructive confirmation.
