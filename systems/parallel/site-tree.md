# Parallel site tree

Mapped from the live public site at https://www.useparallel.com/ on 2026-11-21, in headless Chromium, before screenshots. Each row is a control that was opened or followed, and where it went. A login, signup, LinkedIn, Google, or Apple wall stops that branch. No form was submitted. No email, phone, password, or profile field was typed.

The product is Parallel (Parallel Inc.), the hiring and job-matching site at useparallel.com. It is not parallel.ai. The homepage loaded with HTTP 200.

## Header, talent mode (desktop, on `/`)

| Control | Opens |
|---|---|
| Logo button, aria-label "Go to talent" | Stays on `/` (talent home) |
| Explore (button, `aria-haspopup="menu"`) | Menu: Explore Paths, Explore Jobs, AI Training, Take Workform |
| Explore Paths (menuitem) | `/app/candidate/paths` |
| Explore Jobs (menuitem) | `/app/candidate/search` |
| AI Training (menuitem) | `/ai-training` |
| Take Workform (menuitem) | `/work-form` |
| Talent (tab) | Stays on the talent home `/` |
| Employers (tab) | `/employers` |
| Sign in (button) | `/login`. Wall: email, password, or LinkedIn. Branch stopped. |
| Sign up (button) | Dialog on `/`: "Get started with Parallel" with one control, "Continue with LinkedIn". Branch stopped. Not clicked. |

## Header, employer mode (desktop, on `/employers`)

| Control | Opens |
|---|---|
| Logo button, aria-label "Go to talent" | `/` |
| Overview (button, menu) | Menu: Overview, Platform, Recruiting, Studio |
| Overview (menuitem) | `/employers` |
| Platform (menuitem) | `/employers/platform` |
| Recruiting (menuitem) | `/employers/recruiting` |
| Studio (menuitem) | `/employers/studio` |
| Talent (tab) | `/` |
| Employers (tab) | Stays on `/employers` |
| Sign in (button) | `/employers/login`. Wall: work email, password, or LinkedIn. Branch stopped. |
| Start Free (button) | `/employers/signup`. Wall: full name and work email. Branch stopped. Not filled. |

The same employer menu is labelled Platform on `/employers/platform` and Recruiting on `/employers/recruiting`. The items are the same four pages.

## Phone header (390, on `/`)

| Control | Opens |
|---|---|
| Go to talent | `/` |
| Sign Up | Same LinkedIn dialog as desktop Sign up. Branch stopped. |
| Open menu | Full-screen menu. Close menu dismisses it. |
| Talent / Employers tabs | Same destinations as desktop |

Open menu items, top to bottom: Explore Paths, Explore Jobs, AI Training, Explore Companies, Take WorkForm, Overview, Platform, Recruiting, Studio, Post a Job, Start Free, Manifesto, Lifework Blog, Sign Up.

Explore Companies goes to `/all-companies`. Post a Job goes to `/employers`. Start Free goes to `/employers/signup` (wall).

## Talent home (`/`)

| Control | Opens |
|---|---|
| Search roles (input) plus Submit search | Local search field. Submitting would query jobs. Not submitted. The chips beside it are the public filters. |
| Full time | `/app/candidate/search?jobType=Full+Time` |
| Contract | `/app/candidate/search?jobType=Contract` |
| AI training | `/ai-training` |
| Remote | `/app/candidate/search?location=Remote` |
| Sign up to discover your fit | LinkedIn signup dialog. Branch stopped. |
| Sign up to find hidden roles | LinkedIn signup dialog. Branch stopped. |
| Sign up to get guidance | LinkedIn signup dialog. Branch stopped. |
| Read More | `/manifesto` |
| Get Started | LinkedIn signup dialog. Branch stopped. |

## Footer (every marketing page)

| Control | Opens |
|---|---|
| Explore Jobs | `/app/candidate/search` |
| AI Training | `/ai-training` |
| Explore Paths | `/app/candidate/paths` |
| Take WorkForm | `/work-form` |
| Post a job | `/employers` |
| Platform | `/employers/platform` |
| Recruiting | `/employers/recruiting` |
| Studio | `/employers/studio` |
| Start free | `/employers/signup` (wall) |
| Manifesto | `/manifesto` |
| Lifework Blog | `/blog` |
| Parallel Ventures | https://ventures.useparallel.com (other host, not captured) |
| Careers | `/parallel/careers` |
| Contact | A mailto link to the published support address (mail client, not a page). The address is not stored in this package. |
| Terms | `/about/terms` |
| Privacy | `/about/privacy` |
| Instagram | https://instagram.com/useparallel (external, not opened) |
| LinkedIn | https://linkedin.com/company/useparallel (external, not opened) |

## Public pages reached from the tree

| Page | How it is reached | Notes |
|---|---|---|
| `/` | Logo, Talent tab | Talent marketing home |
| `/employers` | Employers tab, Post a job | Employer marketing home. FAQ buttons expand in place. Feature chips (Screened Talent, Career Page, Pipeline Management, People Search, Analytics) switch a local panel. |
| `/employers/platform` | Platform menu item, footer | Feature anchors `#feature-panel-0` through `#feature-panel-3`. FAQ expands in place. |
| `/employers/recruiting` | Recruiting menu item | FAQ expands in place. Get Started goes to the signup wall. |
| `/employers/studio` | Studio menu item | FAQ expands in place. Start building goes to the signup wall. |
| `/ai-training` | Explore menu, footer, home chip | FAQ expands in place. Explore Roles and View all roles go to job search. |
| `/work-form` | Explore menu, footer | Public explainer. Take the WorkForm goes to `/app/candidate/work-form`, which asks to connect LinkedIn. Branch stopped there. Archetype chips (Builder, Visionary, and the rest) switch a local panel. |
| `/manifesto` | Read More, footer | Long public essay |
| `/blog` | Footer | Category links filter in place: All, Self, Careers, Work & Life, Future of Work, Founders. Subscribe is an email field. Not filled. |
| `/blog/<slug>` | A post card | One public post captured as the article pattern |
| `/pricing` | Linked from `/templates` and `/whats-next` | Public price page. Sign in and Try free and Start free trial go to the employer signup or login wall. |
| `/app/candidate/search` | Explore Jobs, home chips | Public job list, signed out. Sidebar links Home, Matches, Work, Messages, Profile go to `/app/candidate` and stop at the LinkedIn or login wall. |
| `/app/candidate/search` filters | All Filters, Sort by, Jobs, Companies, Remote Only | In-page panels. Location, Salary, Job Type, Most Recent. |
| `/app/candidate/job/<id>` | A job card | Public job detail. Agent Apply, Save, Follow, and Sign up are walls. Not submitted. |
| `/company/<slug>` | A company name on a job card | Public company page. Follow and Sign up are walls. |
| `/app/candidate/paths` | Explore Paths | Public path catalog. Take the WorkForm is the LinkedIn wall. |
| `/all-companies` | Mobile menu Explore Companies | Public company index |
| `/collections` | Older chrome on manifesto-era pages | Public collection index |
| `/case-studies` | Sitemap, employer stories | Index plus one public story |
| `/resources` | Sitemap | Guide index |
| `/help-center` | Sitemap, release notes | Public help index. Open Hire goes to `/app/hire` (signed-in product). Branch stopped. |
| `/release-notes` | Sitemap | Public notes. Open Hire is the same wall. |
| `/parallel/careers` | Footer Careers | Parallel's own career page. Job rows open `/parallel/careers/<id>`. Filters (location, department, type) open in place. Join Network is a signup wall. |
| `/about/terms` | Footer | Public terms |
| `/about/privacy` | Footer | Public privacy policy (the word "email" in the policy text is not a form) |
| `/about/candidatemanifesto` | Sitemap | Older page chrome with a search field. Not submitted. |
| `/about/employeemanifesto` | Sitemap | Same older chrome |
| `/templates` | Linked from `/whats-next` | Career-page template previews. Start and Try free go to the signup wall. Preview switches a local template. |
| `/whats-next` | Sitemap | Public talent-open page. Try For Free and Log in are walls. |
| `/sync-jobs` | Linked from `/employers` ("Sync your ATS") | Recorded if it loads without a form. |
| `/energy` | Sitemap | HireCore marketing page. Get started fields ask for email and a website. Not filled. Book demo goes to `/energy/get-started` (same kind of form). Branch stopped at the form. |

## Walls (URL recorded, branch stopped)

| URL | What it asks for | How it was reached |
|---|---|---|
| `/login` | Email, password, or LinkedIn | Talent Sign in |
| `/signup` | LinkedIn only | Login page "Create new account" |
| `/employers/login` | Work email, password, or LinkedIn | Employer Sign in |
| `/employers/signup` | Full name and work email | Start Free, book-demo redirect |
| `/company/login` | Work email, password, or LinkedIn | Sitemap |
| `/claim-page` | Work email and company website | Sitemap |
| `/post-job` | Email and company website | Sitemap |
| `/employers/join` | Work email and company website | Sitemap |
| `/auth/linkedin/complete` | LinkedIn return | Sitemap. Not opened. |
| `/app/candidate` and `/app/candidate/matches`, `/saves`, `/inbox`, `/resume` | Signed-in candidate app | Search sidebar |
| `/app/candidate/work-form` | Connect LinkedIn | Take the WorkForm |
| `/app/hire` | Signed-in Hire app | Help center "Open Hire" |

## Not opened

Dev preview routes under `/dev/` are internal previews, not linked from the public home. Job and company URLs in the server sitemap (about 30,000) are the same two templates as the one job and one company captured. Blog posts beyond the index and one article are the same article template. External hosts (Ventures, Instagram, LinkedIn, X) were not opened. Google and Apple sign-in buttons were not present on the walls that loaded. No Google, LinkedIn, or Apple control was clicked.
