# Oku public site tree

Mapped from [https://oku.club/](https://oku.club/) on 2026-11-21 in headless Chromium before any screenshot pass. Signed out. No form was submitted. No email, password, username, or profile field was typed. Google, Facebook, and Apple controls were not clicked.

Oku is a reading-tracker marketing site plus public book, profile, review, and blog pages. The signed-in library, collections editor, and checkout sit behind a signup wall. The product paints light by default and dark when the browser asks for `prefers-color-scheme: dark`. There is no in-page theme switch on the public surface.

## Shell

Desktop header (fixed, 80px, z-index 89): logo, Explore, Blog, Pricing, Twitter, Contact, Sign in, Join.

| Control | Opens |
|---|---|
| Logo | [https://oku.club/](https://oku.club/) |
| Explore | [https://oku.club/explore](https://oku.club/explore) |
| Blog | [https://oku.club/blog](https://oku.club/blog) |
| Pricing | [https://oku.club/pricing](https://oku.club/pricing) |
| Twitter | [https://twitter.com/okuclub](https://twitter.com/okuclub) (left the site; not captured) |
| Contact | `mailto:` (not opened; the address is not written here) |
| Sign in | [https://oku.club/signin](https://oku.club/signin) email and password wall. Branch stopped. |
| Join (header button) | Signup dialog on the current page: white panel, 480px, 20px radius, over an `rgba(0, 0, 0, 0.6)` scrim. Fields ask for email, username, and password. Not filled. Escape closes it. |
| Join for free / Create a free account / Subscribe | [https://oku.club/join](https://oku.club/join) full-page signup wall. Not filled. |

Phone header (390px): logo at the left, an unlabeled menu button at the right (about 22×40 at x=344). The desktop nav links are not in the header.

| Control | Opens |
|---|---|
| Menu button | A vertical list over the page: Join, Sign in, Explore, Blog, Pricing, Twitter, Contact. Join in that list opens the same signup dialog. Sign in opens the sign-in wall. |
| Join for free (hero) | Same signup dialog. Not filled. |

Footer on explore, blog, pricing, book, profile, and legal pages: Create a free account (`/join` wall), Privacy, Terms, Twitter, Facebook. Facebook was not clicked.

## Pages reached from the homepage

| Page | How it opens | What is public |
|---|---|---|
| Home `/` | Logo, or the address itself | Hero, feature sections, a live activity feed of public book and profile links, App Store badge |
| Explore `/explore` | Header Explore | "Explore Oku" heading, then a public grid of recommended books. No search field. |
| Blog `/blog` | Header Blog | A list of dated posts. Each post title is a link. |
| Pricing `/pricing` | Header Pricing | Free / Premium / a third plan. "Pay monthly" and "Pay yearly" are text labels, not controls that change the price (clicking them left `$35 / year` and `$125 / year` on screen). Join for free and Subscribe go to `/join`. |
| Sign in `/signin` | Header Sign in, "Already a member? Sign in.", "Or sign in" | Wall. Email and password fields, Forgot password?, Sign in button, Or sign up. Stopped. |
| Login `/login` | Not linked from the homepage. Known missing wall. | HTTP 200 body is the public 404 ("How did you get here?"). No email or password field. |
| Join `/join` | Create a free account, Subscribe, Join for free links | Wall. Email, username, password. Stopped. |
| Signup `/signup` | Not linked | HTTP 404, the public 404 page. |
| Reset password `/reset-password` | Forgot password? on `/signin` | Recorded as a wall branch. Not opened, not filled. |
| Privacy `/privacy` | Footer Privacy, and the signup dialog's Privacy Policy link | Public policy page. |
| Terms `/terms` | Footer Terms | Public terms page. The HTTP status is 404 while the terms body still renders. |
| About, help, faq | Not linked. Probed. | Public 404. |
| Search | Not linked. `/explore` has no input. | No public search control. |

## Content types the homepage feed opens

The homepage activity feed is a list of public cards. Each card links a book and a profile. One example of each type was opened. The feed itself changes as members read, so the specific titles are a sample from 2026-11-21, not a fixed catalog.

| Control | Opens |
|---|---|
| Book cover or title | `/book/<slug>` public book page: cover, title, author, description, Book Info / Reviews / Highlights tabs, status buttons (Want to read, Reading, Read). |
| Status buttons on a book | Signup dialog (email, username, password). Branch stopped. They do not open a status menu while signed out. |
| Profile name or avatar | `/user/<handle>` public profile: library, collections, reviews, highlights, reading / read / to-read shelves. |
| Profile shelf ("See more", "Collections", "Reviews", "Highlights", "Follows") | `/user/<handle>/collections`, `/reviews`, `/highlights`, `/collection/reading`, `/collection/read`, `/collection/to-read`, `/following`. Public when the profile is public. |
| Review card | `/reviews/<bookId>/<reviewId>` public review. "Read more reviews" opens `/reviews/<book-slug>`. |
| "Review may contain spoilers / Tap to read" | Toggles the spoiler open on the same page. No wall. |
| App Store badge | `https://apps.apple.com/us/app/oku/id1604015977`. Left the site. Not captured. |
| Embedded tweets | `https://twitter.com/...`. Left the site. Not captured. |

Blog posts linked from `/blog` (public articles, same header and footer):

- `/blog/oku-now-available-for-ios`
- `/blog/2021/how-to-install-on-a-mobile-device`
- `/blog/oku-referral-reward-program`
- `/blog/oku-has-rss-feeds`
- `/blog/2021/introducing-oku`
- `/blog/premium-membership-is-here`
- `/blog/say-hello-to-book-reviews`
- `/blog/2021/deep-work-on-the-rise`
- `/blog/2021/importing-your-data-from-goodreads`
- `/blog/2021/a-new-look-and-a-sneak-peek`

## Walls (branch stopped)

| URL | What it asks for |
|---|---|
| [https://oku.club/login](https://oku.club/login) | Missing. The response is the public 404 page, not a login form. |
| [https://oku.club/signin](https://oku.club/signin) | Email address and password. Forgot password? links to `/reset-password`. |
| [https://oku.club/join](https://oku.club/join) | Email, username, password. Same form as the Join dialog. |
| Join dialog (any page) | Same three fields, over a scrim. Not submitted. |
| Book status buttons | Open that same Join dialog. |
| `/reset-password` | Linked only from the sign-in wall. Not opened. |

## Not present on the public surface

No theme toggle, no search field, no checkbox, radio, switch, select, tooltip, toast (toastify CSS is loaded; no toast was shown), table, or destructive confirmation. Dark theme exists only as `prefers-color-scheme: dark`.
