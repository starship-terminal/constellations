# LinkedIn public site tree

Mapped from https://www.linkedin.com/ on 2026-11-21, signed out, in headless Chromium, before screenshots. A control that opens a login or signup wall is recorded and that branch stops. No form was submitted. No password, code, or social sign-in was used.

The homepage paints a guest marketing page, not the signed-in feed. Nav labels and job suggestions are geo-localised (this session saw Singapore job chips). Auth walls use the URL the browser landed on.

## Homepage controls

| Control | Opens | Then |
|---|---|---|
| Skip to main content | In-page `#main-content` | Stay |
| Logo | `/` | Stay |
| Top Content | `/top-content` | Public topic index |
| People | `/pub/dir/+/+` | Auth wall (`/authwall`, Join LinkedIn). Stop |
| Learning | `/learning/search` | Public course search |
| Jobs | `/jobs/search` | Redirects to `/jobs` (HTTP 429 on one probe). Marketing jobs page with an embedded email/password sign-in module. Stop that module |
| Games | `/games` | Public games lobby |
| Sign in | `/login` | Email, password, Sign in with Apple. Stop |
| Join now | `/signup` and `/signup/cold-join` | Name, email, password, Agree & Join. Stop |
| Sign in with email | `/login` | Same login wall. Stop |
| User Agreement, Privacy Policy, Cookie Policy | `/legal/user-agreement`, `/legal/privacy-policy`, `/legal/cookie-policy` | Public legal pages |
| Topic chips (Career, Productivity, Finance, and the rest) | `/top-content/<topic>/` | Public topic page |
| Show all (topics) | `/top-content/` | Public topic index |
| Job suggestion chips | `/jobs/<role>-jobs-<place>` | Public job listing |
| Show more jobs | Expands the same chip list in place | Stay. No navigation |
| Post a job | `/talent/post-a-job` | "Join LinkedIn to start your job post". Stop |
| Product category chips | `/products/categories/<slug>` | Public category |
| Show all (products) | `/products` | Public product index |
| Game cards (Zip, Queens, and the rest) | `/games/<slug>/` | Public game shell |
| Find jobs / Find people / Find a course | `/jobs/...`, people directory or auth wall, `/learning/...` | Capture the public one. Stop on auth |
| Get started | Signup wall | Stop |
| Choose a topic | Language menu (`role=menu`), not a topic picker. The button's accessible name is "Choose a topic to learn about"; the menu items are languages | Stay. Do not change language |
| Language | Same language menu | Stay |
| Footer General, Browse LinkedIn, Directories | See footer table | Per row |

## Footer and directory

| Control | Opens | Then |
|---|---|---|
| Help Center | `/help/linkedin` | Public help home. Search box is not submitted |
| About | `about.linkedin.com` | Off the product host. Not captured |
| Press | `press.linkedin.com` | Off the product host. Not captured |
| Blog | `blog.linkedin.com` | Off the product host. Not captured |
| Careers | `/company/linkedin/jobs` | Public company jobs list, with an embedded sign-in module. Stop that module |
| Developers | `developer.linkedin.com` | Off the product host. Not captured |
| Learning, Jobs, Games | Same as nav | See homepage |
| Mobile | `members.linkedin.com/apps` | Public "Get the LinkedIn app" |
| Services | `/services` | Public services marketing |
| Products | `/products` | Public |
| Top Companies, Top Startups, Top Colleges | `/hubs/top-companies`, `/hubs/top-startups`, `/hubs/top-colleges` | Public hubs |
| Talent, Marketing, Sales | `business.linkedin.com/...` | Off the product host. Not captured |
| Learning (business) | `learning.linkedin.com` | Off the product host. Not captured |
| Members, Jobs, Companies, Featured, Learning, Posts, Articles, Schools, News, Newsletters, Services, Products, People Search | `/directory/<name>` | Public directory indexes |
| Accessibility | `/accessibility` | Public |
| Copyright Policy | `/legal/copyright-policy` | Public |
| Brand Policy | `brand.linkedin.com` | Off the product host. Not captured |
| Guest controls | `/psettings/guest-controls` redirects to `/mypreferences/g/guest-controls` | Public preference page. Not submitted |
| Community Guidelines | `/legal/professional-community-policies` | Public |

## Second-level public controls

| Page | Control | Opens |
|---|---|---|
| `/top-content/career/` | Open menu, Share | In-page menu and share sheet (LinkedIn, Facebook, X). Not followed off-site. Dismiss closes it |
| `/jobs/engineering-jobs` | Date posted, Company | In-page filter popovers. Done closes them. Search is not submitted |
| `/jobs/engineering-jobs` | Job title | `/jobs/view/<id>` public job detail, with a sign-in module. Stop that module |
| `/jobs/engineering-jobs` | Company name | `/company/<slug>` public company page |
| `/jobs/engineering-jobs` | Where are the filters? | Dismissible notice. Dismiss closes it |
| `/jobs/engineering-jobs` | Show / Sign in / See more jobs | Sign-in dialog. Stop |
| `/learning/` | Course card | `/learning/<course>` public course page. Start free trial and Sign in are walls |
| `/learning/` | Subject tabs (All courses, Business, Technology, Creative) | In-page tab. Stay |
| `/learning/` | Search skills | Focuses the search field. Not submitted |
| `/products` | Category and product cards | `/products/categories/<slug>` or `/products/<slug>` |
| `/products/categories/e-commerce-platforms` | Checkboxes | Filter the list in place. Not submitted as a form |
| `/services` | Category cards | `/services/l2/<slug>` |
| `/services` | See all services | `/services/browse` |
| `/services` | Get started | `/services/page/onboarding` onboarding. Stop |
| `/services` | Play video | In-page video. Not a form |
| `/games` | Game card | `/games/<slug>/` |
| `/games/zip/` | Back | `/games` |
| `/legal/user-agreement` | Open navigation | In-page nav. Close navigation closes it |
| `/legal/user-agreement` | Expand to show more links | In-page disclosure |
| `/help/linkedin` | Dismiss notice | Hides the notice. Not a consent POST |
| `/help/linkedin` | Product menu | In-page menu of help centres. Close menu closes it |
| `/help/linkedin` | Topic links | `/help/linkedin/topic/<id>` and `/help/linkedin/answer/<id>` |
| `/help/linkedin` | Sign in, email settings, close account | Auth or account settings. Stop |
| `/hubs/top-companies` | Show more / Show less | In-page disclosure |
| `/company/linkedin/jobs` | Show more affiliated / similar / jobs | In-page disclosure |

## Walls (recorded, not entered)

- https://www.linkedin.com/login/ asks for email and password, or Sign in with Apple.
- https://www.linkedin.com/signup and https://www.linkedin.com/signup/cold-join ask for email, password, and name (Agree & Join).
- https://www.linkedin.com/authwall (from People) asks to join.
- https://www.linkedin.com/talent/post-a-job asks to join before a job post.
- https://www.linkedin.com/uas/login and https://www.linkedin.com/checkpoint/lg/login are the same class of sign-in wall, reached from product and help links.
- Embedded `session_key` / `session_password` modules on `/jobs` and company jobs pages are the same wall. They are not filled.

## Not a public app state

Feed, messaging, profile, notifications, settings, and the signed-in job application flow are not reachable without an account. Dark theme is declared in the guest CSS (`light-dark()` and `[data-color-scheme]`) and is not a control on these pages. Language menus are present on every guest page and are left on English.
