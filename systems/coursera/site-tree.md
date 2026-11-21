# Coursera public site tree

Mapped 2026-11-22 from [https://www.coursera.org/](https://www.coursera.org/) while signed out, in an incognito preview tab. The page title is "Coursera | Online Courses, Certificates, & Degrees". Desktop shots are 1440×900 CSS at 2x (2880×1800 PNG). Phone shots are 390×844 CSS at 2x (780×1688 PNG).

A control that opens login, signup, an identity provider, a checkout, or an enroll action stops that branch. Nothing was typed. No form was submitted. No identity provider was clicked. Enroll for free was not clicked. The signed-in classroom was not opened. Cookie preference center was present in the DOM and not opened. Accept and Reject were not pressed.

Opened states live in [screenshots/site-tree/](screenshots/site-tree/). Page shots from this pass use the `public-2026-11-22-` prefix so they sit beside the 2026-10-17 set.

## Audience bar

Present on the homepage at 1440. Hidden at 390 until the drawer opens.

| Control | Kind | Opens | Shot |
|---|---|---|---|
| For Individuals | Link | https://www.coursera.org/ | |
| For Businesses | Link | https://www.coursera.org/business (header campaign query stripped here) | |
| For Universities | Link | https://www.coursera.org/campus | |
| For Governments | Link | https://www.coursera.org/government | |

## Primary bar

| Control | Kind | Opens | Shot |
|---|---|---|---|
| Wordmark | Link | https://www.coursera.org/ | |
| Explore our catalog | Button, `aria-expanded` | Mega menu "Main Menu", listed below | [desktop](screenshots/site-tree/desktop-explore-menu.png) |
| Degrees | Link (`role=button`) | https://www.coursera.org/degrees | [desktop](screenshots/public-2026-11-22-degrees-desktop.png) |
| Search catalog | Combobox | Placeholder "What do you want to learn?". Not typed. | |
| Search | Button | Submits the combobox. Not clicked. | |
| Ask Coursera | Button | Coach panel on the same page. Privacy notice, "Is this right for me?", prompt chips, "Ask anything..." field. Not typed. | [course, open then closed](screenshots/site-tree/desktop-course-promo.png) |
| Log In | Link | `?authMode=login` or `#authMode=login`. Same empty dialog as signup. Stopped. | [desktop](screenshots/public-2026-11-22-login-desktop.png) |
| Join for Free | Link | `?authMode=signup`. Same dialog. Stopped. | [desktop](screenshots/public-2026-11-22-login-desktop.png) |

Phone: the header collapses to the wordmark, Ask Coursera, Search, and a menu button. The drawer is full screen. Shot: [phone-nav-drawer.png](screenshots/site-tree/phone-nav-drawer.png). Homepage at 390: [public-2026-11-22-home-mobile.png](screenshots/public-2026-11-22-home-mobile.png).

## Explore menu

Opened from "Explore our catalog". Groups and the links measured in the menu:

### Explore roles

View all goes to https://www.coursera.org/career-academy.

| Label | Opens |
|---|---|
| AI Series (New) | /explore/ai-series |
| Data Analyst | /career-academy/roles/data-analyst |
| Project Manager | /career-academy/roles/project-manager |
| Cyber Security Analyst | /career-academy/roles/cyber-security-analyst |
| Data Scientist | /career-academy/roles/data-scientist |
| Business Intelligence Analyst | /career-academy/roles/business-intelligence-analyst |
| Digital Marketing Specialist | /career-academy/roles/digital-marketing-specialist |
| UI / UX Designer | /career-academy/roles/user-interface-user-experience-ui-ux-designer |
| Machine Learning Engineer | /career-academy/roles/machine-learning-engineer |
| Social Media Specialist | /career-academy/roles/social-media-strategist-specialist |
| Computer Support Specialist | /career-academy/roles/computer-support-specialist |

### Explore categories

View all goes to https://www.coursera.org/browse. Photographed signed out: [public-2026-11-22-browse-desktop.png](screenshots/public-2026-11-22-browse-desktop.png). Heading "Explore Categories".

| Label | Opens |
|---|---|
| Artificial Intelligence | /explore/generative-ai |
| Business | /browse/business |
| Data Science | /browse/data-science |
| Information Technology | /browse/information-technology |
| Computer Science | /browse/computer-science |
| Healthcare | /browse/health |
| Physical Science and Engineering | /browse/physical-science-and-engineering |
| Personal Development | /browse/personal-development |
| Social Sciences | /browse/social-sciences |
| Language Learning | /browse/language-learning |
| Arts and Humanities | /browse/arts-and-humanities |

Browse chips on the page itself also include Math and Logic. Most popular tabs on /browse: All, Business, Data Science, Information Technology, Computer Science.

### Earn a Professional Certificate

View all goes to `/search?productTypeDescription=Professional%20Certificates&sortBy=BEST_MATCH`. Topic links add `topic=` for Business, Computer Science, Data Science, and Information Technology.

### Earn an online degree

View all goes to https://www.coursera.org/degrees.

| Label | Opens |
|---|---|
| Bachelor's | /degrees/bachelors |
| Master's | /degrees/masters |
| University Certificates | /certificates/learn |

The degrees page itself also links Bachelor's, Master's, Postgraduate Programs, and subject hubs (Business and MBA, Computer Science, Data Science, Data Analytics, Top European, Maestrías en línea, Top Indian). Individual degree cards such as `/degrees/imba` are public marketing pages. RSVP links leave for Zoom webinar registration and were not followed.

### Explore trending skills

| Label | Opens |
|---|---|
| Python | /courses?query=python |
| Artificial Intelligence | /courses?query=artificial%20intelligence |
| Excel | /courses?query=microsoft%20excel |
| Machine Learning | /courses?query=machine%20learning&skills=Machine%20Learning |
| SQL | /courses?query=sql |
| Project Management | /courses?query=project%20management |
| Power BI | /courses?query=power%20bi |
| Marketing | /courses?query=marketing&skills=Marketing |

### Menu footer

| Label | Opens |
|---|---|
| Prepare for a certification exam | /explore/certification-preparation-courses |
| Browse free courses | /courses?query=free |
| Learn more about Coursera Plus | /courseraplus |

## Phone drawer

Opened from the menu button on the homepage at 390. Accordion labels were not expanded; the desktop mega menu already lists their children.

| Control | Kind | Opens |
|---|---|---|
| Wordmark | Link | / |
| Close | Button | Dismisses the drawer |
| Explore roles | Button | Accordion. Not expanded on phone. |
| Explore categories | Button | Accordion. Not expanded on phone. |
| Trending skills | Button | Accordion. Not expanded on phone. |
| Earn a professional certificate | Button | Accordion. Not expanded on phone. |
| Earn an online degree | Button | Accordion. Not expanded on phone. |
| Prepare for a certification exam | Link | /explore/certification-preparation-courses |
| Browse free courses | Link | /courses (drawer href; desktop menu uses `/courses?query=free`) |
| For Businesses | Link | /business |
| For Universities | Link | /campus |
| For Governments | Link | /government |
| Join for Free | Button | Same empty auth dialog. Not clicked on phone. |
| Log In | Button | Same empty auth dialog. Not clicked on phone. |

## Homepage body

Shot: [public-2026-11-22-home-desktop.png](screenshots/public-2026-11-22-home-desktop.png).

| Control | Opens |
|---|---|
| Save now | Coursera Plus annual special. Not a checkout submit. |
| Find your AI Series | /explore/ai-series |
| Save 40% on Teams | https://discover.coursera.org/teams-gifting-pm. Leaves the marketing host. Not followed. |
| Most popular | /explore/most-popular-courses |
| Course cards | Public course and certificate pages. One followed, below. |

## Public course

https://www.coursera.org/learn/foundations-data loaded without an account. Title "Foundations: Data, Data, Everywhere" by Google Career Certificates. Breadcrumbs: Home, Categories `/browse`, Data Science `/browse/data-science`, Data Analysis `/browse/data-science/data-analysis`. Tabs: About, Outcomes, Modules, Recommendations, Testimonials, Reviews. Enroll for free was not clicked.

A Coursera Plus promo dialog auto-opened and later closed itself. It was photographed, not submitted. Ask Coursera was open in that same shot and then closed. Shot with both open: [desktop-course-promo.png](screenshots/site-tree/desktop-course-promo.png). Course with the coach closed: [public-2026-11-22-course-desktop.png](screenshots/public-2026-11-22-course-desktop.png). Phone: [public-2026-11-22-course-mobile.png](screenshots/public-2026-11-22-course-mobile.png).

The promo banner "Claim now" goes to `/courseraplus/special/cplus-annual-november-2026-apac`. Not followed.

## Pricing

There is no `/pricing` item in the public nav. Coursera Plus is the public price page: https://www.coursera.org/courseraplus. Heading "Unwrap a full year of skills at 40% off". Visible prices on 2026-11-22: $399 struck, $239.40/year, or $59/month after a 7-day free trial; a $49/$79 monthly comparison. "Get started" goes to `/purchase/account`. "Start 7-day free trial!" is a button. Neither was clicked. Shot: [public-2026-11-22-plus-desktop.png](screenshots/public-2026-11-22-plus-desktop.png).

## Empty state

https://www.coursera.org/this-page-does-not-exist-capture-2026 returns the public missing-page message: "We were not able to find the page you're looking for." Links offered: Online Degrees, Coursera for Business, Coursera Blog. Not an account wall. Shot: [public-2026-11-22-notfound-desktop.png](screenshots/public-2026-11-22-notfound-desktop.png). The 2026-10-17 package already has `notfound-light-default.png`.

## Footer

Shot: [desktop-footer.png](screenshots/site-tree/desktop-footer.png). Columns measured from the homepage. Off-site links (careers, partners, Udemy, community, blog, podcast, help, investors, Airtable, social, app stores) were not followed.

| Column | Labels |
|---|---|
| Skills | Accounting, AI, Cybersecurity, Data Analytics, Digital Marketing, HR, Excel, Project Management, Python, SQL. All `/courses?query=...`. |
| Professional Certificates | Google AI, Cybersecurity, Data Analytics, IT Support, Project Management, UX Design; IBM AI Engineering, IBM AI Product Manager, IBM Data Science; Intuit Academy Bookkeeping. |
| Courses & Specializations | AI Essentials, AI For Business (Wharton), AI For Everyone, AI in Healthcare, Deep Learning, Excel Skills for Business, Financial Markets, Machine Learning, Prompt Engineering for ChatGPT, Python for Everybody. |
| Career Resources | Career Aptitude Test `/resources/career-quiz`, several `/articles/*`, "Share your Coursera learning story" (Airtable form, not followed). |
| Coursera | About `/about`, Leadership `/about/leadership`, Careers (careers.coursera.com), Catalog `/browse`, Coursera Plus `/courseraplus`, Professional Certificates `/professional-certificates`, Degrees `/degrees`, For Enterprise `/business`, For Government `/government`, For Campus `/campus`, Become a Partner (partnerships.coursera.org), Udemy. |
| Community | Learners (coursera.community), Partners `/partners`, Beta Testers (support article), Free Courses `/courses?query=free`, Blog (blog.coursera.org), Podcast (Spotify), Tech Blog (Medium), Social Impact `/social-impact`. |
| More | Press `/about/press`, Investors (investor.coursera.com), Terms `/about/terms`, Privacy `/about/privacy`, Help (learner.coursera.help), Accessibility (help article), Contact `/about/contact`, Articles `/articles`, Directory `/directory`, Affiliates `/about/affiliates`, Modern Slavery Statement (PDF), Cookies Preference Center `/about/cookies-manage`. |

Social: Facebook, LinkedIn, Twitter, YouTube, Instagram, TikTok. App Store and Google Play badges. Copyright line: "© 2026 Coursera Inc. All rights reserved."

## Auth dialog

One dialog for Log In and Join for Free. Title "Authentication modal". Heading "Log in or create account". Email placeholder `name@email.com`, empty. Continue with Google, Facebook, and Apple are buttons. "Sign up with your organization" and "Having trouble logging in?" were not opened. Continue was not clicked. reCAPTCHA notice is visible; no challenge was solved. Notes: [login-review.json](login-review.json). `login_extracted` stays `not-started`.
