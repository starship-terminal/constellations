# LinkedIn public site tree

Mapped from https://www.linkedin.com/ on 2026-11-21, signed out, in headless Chromium. A control that opens a login or signup wall is recorded and that branch stops. No form was submitted. No email, password, phone, or address was typed. Google, Apple, and Microsoft were not clicked. Language was left on English.

The homepage paints a guest marketing page, not the signed-in feed. Nav labels and job suggestions are geo-localised (this session saw Singapore job chips). Auth walls use the URL the browser landed on.

## Homepage controls

| Control | Opens | Then |
|---|---|---|
| Skip to main content | In-page `#main-content` | Stay |
| Logo | `/` | Stay |
| Top Content | `/top-content` | Public topic index |
| People | `/pub/dir/+/+` | Public "Search for people" prompt (HTTP 404 shell) with Join now and Sign in. Stop there. Do not search a name |
| Learning | `/learning/search` | Public course search. Search is not submitted |
| Jobs | `/jobs/search` | Public jobs search (this session landed on United States listings). Embedded sign-in is not filled |
| Games | `/games` | Public games lobby |
| Sign in | `/login` | Email or phone, password, Sign in with Apple. Stop |
| Join now | `/signup` | Email or phone, password, Agree & Join, Continue with Google. Stop. Google is not clicked |
| Continue with Google | Identity provider | Not clicked |
| Sign in with email | `/login` | Same login wall. Stop |
| User Agreement, Privacy Policy, Cookie Policy | `/legal/user-agreement`, `/legal/privacy-policy`, `/legal/cookie-policy` | Public legal pages |
| Topic chips (Career, Productivity, Finance, and the rest) | `/top-content/<topic>/` | Public topic page. Member names on those pages are public site content |
| Show all top content | `/top-content/` | Public topic index |
| Job suggestion chips | `/jobs/<role>-jobs-<place>` | Public job listing (this session: `engineering-jobs-singapore`) |
| Show more | Expands the same chip list in place | Stay. No navigation |
| Post a job | `/talent/post-a-job` | "Join LinkedIn to start your job post". Stop |
| Product category chips | `/products/categories/<slug>` | Public category |
| Show all softwares and platforms | `/products/home` | Same public product index as `/products` |
| Game cards (Patches, Zip, Queens, and the rest) | `/games/<slug>/` | Public game shell. Start game is not entered past the public shell |
| Next Slide | In-page carousel | Stay |
| Find people you know / Find a coworker or classmate | `/pub/dir/+/+` | Same people prompt. Stop |
| Find a new job | `/jobs/jobs-in-<place>` | Public jobs list |
| Find a course or training | `/learning/search` | Public course search |
| Choose a topic to learn about | Language menu, not a topic picker. Items are languages | Stay. Do not change language |
| Footer Language | Language menu, same items. English stays selected. The menu opens from the footer and is tall; the captured shot shifts it left so the labels fit the viewport | Stay |
| Get started / Sign Up | `/signup` | Signup wall. Stop |
| Footer General, Browse LinkedIn, Business Solutions, Directories | See footer table | Per row |

## Footer and directory

| Control | Opens | Then |
|---|---|---|
| Help Center | `/help/linkedin` | Public help home. A navigation-update notice is on the page. Search is not submitted |
| About | `https://about.linkedin.com/` | Public About marketing page on the about host. `/about` on www is a language picker, not the About page |
| Press | `press.linkedin.com` | Off the product host. Not captured this pass |
| Blog | `blog.linkedin.com` | Off the product host. Not captured this pass |
| Careers | `/company/linkedin/jobs` | Auth wall (`/authwall`, HTTP 999). Stop. Do not fill the join form |
| Developers | `developer.linkedin.com` | Off the product host. Not captured this pass |
| Learning, Jobs, Games | Same as nav | See homepage |
| Mobile | `https://members.linkedin.com/apps` | Public "Get the LinkedIn app" |
| Services | `/services` | Public services marketing |
| Products | `/products` | Public product index. `/products/home` is the same page |
| Top Companies, Top Startups, Top Colleges | `/hubs/top-companies`, `/hubs/top-startups`, `/hubs/top-colleges` | Public hubs. Top Companies is geo-served (this session: United States, 2026) |
| Talent, Marketing, Sales | `business.linkedin.com/...` | Off the product host. Not captured this pass |
| Learning (business) | `learning.linkedin.com` | Off the product host. Not captured this pass |
| Members | `/directory/people` | Auth wall (`/authwall`, HTTP 999). Stop |
| Jobs, Companies, Featured, Learning, Posts, Articles, Schools, News, Newsletters, Services, Products, People Search | `/directory/<name>` | Directory indexes. People is a wall. The rest were not re-walked this pass |

## Second-level public controls

| Page | Control | Opens |
|---|---|---|
| `/top-content/career/` | Share | In-page share sheet (LinkedIn, Facebook, X). Not followed off-site. Escape closes it |
| `/jobs/search` and `/jobs/engineering-jobs-singapore` | Date posted, Company | In-page filter popovers. Escape closes them. Search is not submitted |
| `/jobs/search` | Where are the filters? | Dismissible notice. Not submitted |
| `/jobs/search` | Sign in, Join now, Easy Apply | Sign-in or signup. Stop |
| `/jobs` | Email or phone, Password, Sign in, Continue | Embedded sign-in module on the jobs marketing page. Not filled |
| `/learning/` | Start free trial, Sign in | Walls. Stop |
| `/learning/` | Subject tabs | In-page. Stay |
| `/learning/search` | Search, filters | On screen. Not submitted |
| `/products` | Category and product cards | `/products/categories/<slug>` or `/products/<slug>` |
| `/services` | Category cards, search | Public. Search is not submitted |
| `/services` | Get started | Services onboarding. Stop |
| `/games` | Game card | `/games/<slug>/` |
| `/games/zip/` | Start game | Public game shell. Not signed in |
| `/legal/user-agreement` | Open navigation | In-page legal nav. Close navigation closes it |
| `/help/linkedin` | Notice, product menu, topic links | Public help. Sign in, email settings, and close account are walls. Stop |
| `/hubs/top-companies` | Show more / Show less | In-page disclosure |

## Walls (recorded, not entered)

- https://www.linkedin.com/login/ asks for email or phone and password, or Sign in with Apple. Photographed empty.
- https://www.linkedin.com/signup asks for email or phone and password, then Agree & Join, or Continue with Google. Photographed empty. Google is not clicked.
- https://www.linkedin.com/authwall (from `/directory/people` and `/company/linkedin/jobs`) asks to join. Stop.
- https://www.linkedin.com/talent/post-a-job asks for a name, email, and password before a job post. Stop. Not photographed with any typed value.
- Embedded email/password modules on `/jobs` are the same wall. They are not filled.
- Continue with Google, Sign in with Apple, and any Microsoft control are identity providers. Not clicked.

## Not a public app state

Feed, messaging, profile, notifications, settings, and the signed-in job application flow are not reachable without an account. Dark theme is declared in the guest CSS (`light-dark()` and `[data-color-scheme]`) and is not a control on these pages. Language menus are present and are left on English. `login-extracted` stays `not-started`.
