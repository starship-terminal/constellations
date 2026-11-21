# Awwwards public site tree

Mapped 2026-11-21 from [https://www.awwwards.com/](https://www.awwwards.com/) in headless Chrome (Playwright), before the screenshot pass. Desktop viewport measured 1440x900 at dpr 1. Phone viewport measured 390x844 at dpr 2. Signed out. No form was submitted, no password typed, no social login clicked.

A control that opens a login or signup wall is listed under Walls. That branch stops.

## Header (desktop)

The header is `header.header-main`. Explore is a span, not a link. Its click handler (`search#toggleDropdown`) opens `.nav-header-main__dropdown`.

| Control | Kind | Opens |
|---|---|---|
| Awwwards wordmark (`header-main__logo`) | link | `/` |
| Explore (`nav-header-main__item.has-dropdown`) | menu toggle | in-page dropdown `.nav-header-main__dropdown` (Awards, Trending, Categories, Technology, Collections, Library) |
| Directory | link | `/directory/` |
| Academy | link | `/academy/` |
| Jobs | link | `/jobs/` |
| Market | link | `/market/` |
| Search (`search-form__button`, placeholder "Search by Inspiration") | form control | focuses the header search field. Not submitted. |
| Be Pro | link | `/pro` |
| Submit Website | link | `/submit/` (public gate; form not submitted) |

Log in and Sign Up are in the homepage text but were not a visible header control on this load. The known login URL is under Walls.

## Explore dropdown

Opened from the Explore control. Section labels are spans that toggle lists in place. Each item is a link.

| Section | Item | Opens |
|---|---|---|
| Awards | Honor Mentions | `/websites/` |
| Awards | Nominees | `/websites/nominees/` |
| Awards | Sites of the Day | `/websites/sites_of_the_day/` |
| Awards | Sites of the Month | `/websites/sites_of_the_month/` |
| Awards | Sites of the Year | `/websites/sites_of_the_year/` |
| Awards | Honors | `/honors/winners` |
| Awards | Most Awarded Profiles | `/winner-list/` |
| Awards | Jury 2026 | `/jury/2026/` |
| Awards | Annual Awards | `/annual-awards/` |
| Trending | Portfolio, Free fonts, Animated websites, Scrolling, One page, UI, E-commerce, Architecture, Photography | `/websites/<tag>/` or a collection. Same card grid as `/websites/`. |
| Categories | E-commerce, Architecture, Restaurant & Hotel, Design Agencies, Business, Fashion, Mobile & Apps, Interaction Design, Illustration, Header Design | `/websites/<category>/` |
| Technology | CSS animations, Wordpress, Shopify, WebGL, React, 3D, Figma, Gsap, Framer, Webflow | `/websites/<tech>/` or a collection |
| Collections | Collections | `/collections/` |
| Library | Library | `/library/` |

Category and technology items are the same winners-grid pattern as `/websites/`. One filter-open state on `/websites/` covers that interaction. Each tag page is not a separate component surface.

## Home page interactions

| Control | Kind | Opens |
|---|---|---|
| Site of the Day card | link | `/sites/<slug>` (one sample detail; the directory is unbounded) |
| Author name | link | `/<profile>/` (public profile; one sample) |
| View Nominees | link | `/websites/nominees/` |
| View Winners | link | `/websites/sites_of_the_day/` |
| View Course | link | `/academy/course/<slug>` (course sales page; checkout not followed) |
| Floating menu (`.menu-float`) | in-page links | Nominees `#nominees`, Courses `#courses`, Collections `#collections`, Directory `#directory`, Market `#market`, and Visit Sotd (external site, not followed) |
| Vote | button on a site detail | not clicked. A vote records a score. |

## Footer

| Control | Opens |
|---|---|
| Websites | `/websites/` |
| Collections | `/collections/search/` |
| Elements | `/elements/` |
| Academy | `/academy/` |
| Jobs | `/jobs/search/` |
| Market | `/market/` |
| Directory | `/directory/search/` |
| Conferences | `/conferences/` |
| Blog | `/blog/` |
| FAQs | `/faqs/` |
| About Us | `/about-us/` |
| Contact Us | `/contact-us/` (form not submitted) |
| Cookies Policy | `/cookies-policy/` |
| Cookie Settings | `#` in-page. Not clicked (consent is hidden, never answered). |
| Legal Terms | `/terms/` |
| Privacy Policy | `/privacy-policy/` |
| Instagram, LinkedIn, Twitter, Facebook, YouTube, TikTok, Pinterest | external. Not followed. Facebook here is the product's social profile, not a login button. |

## Pages reached (desktop 1440x900)

Every row returned HTTP 200 and stayed on the requested path. None redirected to a login wall.

| Control | Path | Title |
|---|---|---|
| Home | `/` | Awwwards - Website Awards - Best Web Design Trends |
| Websites / Honor Mentions | `/websites/` | Winning websites. Web Design Inspiration |
| Nominees | `/websites/nominees/` | Nominees |
| Sites of the Day | `/websites/sites_of_the_day/` | Sites Of The Day |
| Sites of the Month | `/websites/sites_of_the_month/` | Sites Of The Month |
| Sites of the Year | `/websites/sites_of_the_year/` | Sites Of The Year |
| Honors | `/honors/winners` | Honors |
| Most Awarded Profiles | `/winner-list/` | Most Awarded Profiles |
| Jury 2026 | `/jury/2026/` | Jury Awwwards 2026 |
| Annual Awards | `/annual-awards/` | Annual Awards |
| Collections | `/collections/` | Collections |
| Library | `/library/` | Library |
| Directory | `/directory/` | Awwwards Directory |
| Directory search | `/directory/search/` | Awwwards Directory |
| Academy | `/academy/` | Awwwards Academy |
| Jobs | `/jobs/` | Jobs for Web Designers and Developers |
| Jobs search | `/jobs/search/` | Jobs for Web Designers and Developers |
| Market | `/market/` | Market |
| Be Pro | `/pro` | Awwwards |
| Submit Website | `/submit/` | Submit your website |
| Elements | `/elements/` | Elements |
| Conferences | `/conferences/` | Conferences |
| Blog | `/blog/` | Awwwards Blog |
| FAQs | `/faqs/` | Awwwards |
| About Us | `/about-us/` | Welcome to Awwwards |
| Contact Us | `/contact-us/` | Awwwards |
| Cookies Policy | `/cookies-policy/` | Cookies Policy |
| Legal Terms | `/terms/` | Awwwards |
| Privacy Policy | `/privacy-policy/` | Awwwards |
| User Plans | `/plans/user-plans` | User Plans |

Filter bars on the winners grids (Awards, Category, Tag, Technology) open an in-page dropdown. Search fields on directory, jobs, collections and websites are present and were not submitted.

## Phone (390x844)

The header collapses to the wordmark, a search button, and `header-main__hamburger` (54x54). Tapping the hamburger opens an in-page menu. It does not navigate.

| Control | Opens |
|---|---|
| Hamburger | in-page menu: Collections `/collections/`, Library `/library/`, Directory `/directory/`, Academy `/academy/`, Jobs `/jobs/`, Market `/market/` |
| Search | header search field. Not submitted. |
| Wordmark | `/` |
| Footer links | the same paths as desktop |

The same section indexes load at 390x844. They are the same pages, recomposed.

## Walls (branch stopped)

| Control | Opens | Why stopped |
|---|---|---|
| Known probe `/login` | `https://www.awwwards.com/login` (HTTP 200, title "Log in to Awwwards") | Asks for email or username (`_username`) and a password (`_password`). Not entered. |
| Google on the login page | `/login/google` | Social login. Not clicked. |
| Twitter on the login page | `/login/twitter` | Social login. Not clicked. |
| Facebook on the login page | `/login/facebook` | Social login. Not clicked. |
| Register now | `/register` | Signup wall. Not opened. |
| Forgot your password? | `/forgot-password` | Account recovery. Not opened. |
| LOG IN NOW | submits the login form | Not clicked. |

## Not in this tree

- Individual `/sites/<slug>` winner pages beyond one sample. The directory is unbounded.
- Individual `/<profile>/` pages, course checkout, market product purchase, and job application forms.
- Search result queries. The empty search pages were opened. No query was submitted.
- Votes, submissions, newsletter signup, cookie choices, and account creation.
- Any page that required a password, a code, or a captcha.
