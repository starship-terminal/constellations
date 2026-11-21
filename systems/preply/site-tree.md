# Preply site tree

Mapped 2026-11-21 from the public homepage at https://preply.com/, signed out, in headless Chromium. Desktop viewport measured 1440×900 at devicePixelRatio 2. Phone viewport measured 390×844 at devicePixelRatio 2. One light theme. `color-scheme` stayed `normal` when the browser asked for dark, and the header stayed `#ff7aac`.

No email, password, name, phone, or address was typed. No form was submitted. Identity providers were not clicked. Booking, messaging, and checkout were not entered. The cookie bar was left on the first shots, then hidden with CSS for the clean home, footer, and listing shots. Accept was never clicked.

The control map is also the shot list in [screenshots/](screenshots).

## Shell (desktop)

A near-black bar sits above a pink header. The bar's close control is an X on the same page. "Join us" leaves the bar.

| Control | Opens |
|---|---|
| Wordmark (`a`, href `/`) | page https://preply.com/ |
| Find tutors (`a`) | page https://preply.com/en/online/english-tutors |
| For business (`a`) | page https://preply.com/en/business-language-training |
| Become a tutor (`a`) | page https://preply.com/en/teach |
| Proven Progress (`a`) | page https://preply.com/en/proven-progress-platform |
| English, SGD (`button`, aria-label "Select language and currency") | dropdown on the same page, 260px wide. See [home-light-language-menu](screenshots/home-light-language-menu.png). |
| Help (`a`, aria-label "Help") | page https://help.preply.com/en/ (leaves the marketing host). Not followed. |
| Log In (`a`) | page https://preply.com/en/login. Login wall. Branch stopped. See [login-light-default](screenshots/login-light-default.png). |

Language, inside that dropdown, is a second list of page links. Currency is a list of buttons (SGD, BRL, GBP, EUR, PLN, UAH, USD) that stay on the page. Currency was not changed. See [home-light-language-list](screenshots/home-light-language-list.png).

| Language | Opens |
|---|---|
| English | https://preply.com/ |
| Bahasa Indonesia | https://preply.com/id/ |
| Deutsch | https://preply.com/de/ |
| Español | https://preply.com/es/ |
| Français | https://preply.com/fr/ |
| Italiano | https://preply.com/it/ |
| Nederlands | https://preply.com/nl/ |
| Polski | https://preply.com/pl/ |
| Português | https://preply.com/pt/ |
| Română | https://preply.com/ro/ |
| Svenska | https://preply.com/sv/ |
| Türkçe | https://preply.com/tr/ |
| Русский | https://preply.com/ru/ |
| Українська | https://preply.com/ua/ |
| العربية | https://preply.com/ar/ |
| ภาษาไทย | https://preply.com/th/ |
| 日本語 | https://preply.com/ja/ |
| 普通话 | https://preply.com/zh/ |
| 한국어 | https://preply.com/ko/ |

## Phone (390)

The nav links collapse. A button labelled "Open menu" opens a drawer from the right on the same page. Close is an X. The drawer lists Log In, Home, Find tutors, For business, Proven Progress, Become a tutor, Messages, and Help, then English and SGD selects. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) and [mobile-home-light-default](screenshots/mobile-home-light-default.png).

Messages (`/en/messages`) redirects to `/en/login`. That is the same login wall. Nothing was typed.

## Home https://preply.com/

| Control | Opens |
|---|---|
| Join us (Ukraine bar) | page https://preply.com/en/stand-with-ukraine |
| Find your tutor | page https://preply.com/en/get-started?subject=english. Signup path. Not submitted. See [signup-light-default](screenshots/signup-light-default.png) for the empty student wall at `/en/signup`. |
| Language tiles further down the page | subject listings such as `/en/online/spanish-tutors` |
| Become a tutor (lower section) | page https://preply.com/en/teach |

See [home-light-default](screenshots/home-light-default.png) and [home-light-full](screenshots/home-light-full.png).

## Footer (every marketing page)

Four columns: About us, For students, For tutors, For companies. Then Support, Contacts, Preply social, Apps, and four link farms (Learn, Online language classes and courses, 1-on-1 tutors, Tutors near you).

The published office line is "USA, 1309 Beacon Street, Suite 300, Brookline, MA, 02446". That is company copy, not a personal address.

| Column | Opens |
|---|---|
| Who we are | https://preply.com/en/about-us |
| How it works | https://preply.com/en/how-it-works |
| Preply reviews | https://preply.com/en/reviews |
| Preply app | https://preply.com/en/app |
| Proven progress platform | https://preply.com/en/proven-progress-platform |
| Preply community guidelines | https://preply.com/en/community-guidelines |
| Work at Preply! | https://preply.com/en/careers |
| Preply's Learning Research | https://preply.com/en/learning-research |
| Media kit | https://preply.com/en/about-us/media-kit |
| Preply Blog | https://preply.com/en/blog/ |
| Questions and Answers | https://preply.com/en/questions |
| Student discount | https://preply.com/en/student-discount |
| Refer a friend | https://preply.com/en/referral |
| Test your English for free | https://preply.com/en/language-tests/english |
| Test your vocab | https://preply.com/en/learn/english/test-your-vocab |
| Preply discounts | https://preply.com/en/learn/discounts |
| Preply Subscription | https://preply.com/en/subscription |
| Become an online tutor | https://preply.com/en/teach |
| Teach English / French / Spanish / German online | `/en/online/<language>-tutoring-jobs` |
| See all online tutoring jobs | https://preply.com/en/online/tutoring-jobs |
| Corporate language training | https://preply.com/en/business-language-training |
| Corporate English / Spanish training | `/en/corporate-<language>-training` |
| Corporate training blog | https://preply.com/en/blog/for-businesses/ |
| Resource center | https://preply.com/en/blog/resource-center/ |
| English level test for companies | https://preply.com/en/english-level-test-for-companies |
| Francization for businesses | https://preply.com/en/business/francization-course-for-businesses |
| Language training for employee relocation | https://preply.com/en/business/language-training-for-employee-relocation |
| Need any help? | https://help.preply.com/en/ |
| Facebook, Instagram, YouTube, LinkedIn, TikTok | leave the host |
| App Store, Google Play | leave the host |
| Legal Center | https://preply.com/en/legal |
| Privacy Policy, Cookie Policy, Legal Notice | PDFs on termsofuse.preply.com |

See [home-light-footer](screenshots/home-light-footer.png).

## Pages captured

| Page | What else it opens |
|---|---|
| https://preply.com/en/online/english-tutors | Public tutor listing. Subject search, Goal, Focus areas, Price per lesson, Also speaks, Country of birth, Tutor categories, Select availability, Sort, and a name search. Goal opens a dialog on the same page: Career and business, Culture travel and hobby, Exam preparation, Lessons for kids. Price opens a range slider. The name search expands a field labelled "Search by name or keyword". Nothing was typed. Book trial lesson, Send message, View full schedule, and profile links were not followed. See [tutors-light-default](screenshots/tutors-light-default.png), [tutors-light-list](screenshots/tutors-light-list.png), [tutors-light-filter](screenshots/tutors-light-filter.png), [tutors-light-price](screenshots/tutors-light-price.png), [tutors-light-search](screenshots/tutors-light-search.png), [mobile-tutors-light-list](screenshots/mobile-tutors-light-list.png). |
| https://preply.com/en/how-it-works | Find my tutor and Get started go to the signup path. Book trial lesson cards were not followed. See [how-light-default](screenshots/how-light-default.png). |
| https://preply.com/en/subscription | Marketing page for the subscription. Find your tutor goes to signup. No price table was on the captured view. See [pricing-light-default](screenshots/pricing-light-default.png). |
| https://preply.com/en/business-language-training | Separate business header (Why Preply Business, Use Cases, Knowledge Base, Book a demo). A lead form (first name, last name, email, job function, company size) was not filled. See [business-light-default](screenshots/business-light-default.png). |
| https://preply.com/en/teach | Create a tutor profile now starts tutor signup. Not followed. See [teach-light-default](screenshots/teach-light-default.png). |
| https://preply.com/en/proven-progress-platform | Marketing page for the progress product. See [progress-light-default](screenshots/progress-light-default.png). |
| https://preply.com/en/stand-with-ukraine | Campaign page. Learn how to help was not followed into a donation. See [ukraine-light-default](screenshots/ukraine-light-default.png). |
| https://preply.com/en/login | Empty login wall. Google, Facebook, Apple, and corporate SSO were not clicked. Email and password were empty. See [login-light-default](screenshots/login-light-default.png). |
| https://preply.com/en/signup | Empty student signup wall. Google and Facebook were not clicked. Name, email, and password were empty. See [signup-light-default](screenshots/signup-light-default.png). |
| https://preply.com/en/this-page-does-not-exist-preply | HTTP 404. "We can't find this page." Explore tutors and Preply home. See [notfound-light-default](screenshots/notfound-light-default.png). |

## Where this stopped

Login and signup were photographed empty. Messages redirects to login. Book trial lesson, Send message, Create a tutor profile, Book a demo, and the business lead form were not entered. There is no public empty tutor search: a nonsense subject URL is the 404 page, and a `search` query on the English listing still shows tutors. A keyword that returns zero tutors would have required typing into the search field and submitting it, which this pass did not do.
