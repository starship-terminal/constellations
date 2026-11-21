# Quizlet public site tree

Mapped on 2026-11-21 from https://quizlet.com/, signed out, before the later screenshots. `body` class is `theme-default flex-sidebar`. Page background `rgb(246, 247, 251)`. Type `hurme_no2-webfont, -apple-system, system-ui, sans-serif`. `emulateMedia` dark left the class and the background unchanged.

Desktop CSS viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2. Phone CSS viewport measured 390 by 844 at device pixel ratio 2.

A Ketch cookie host (`#lanyard_root`) covered the page. It was hidden with CSS. Consent was not accepted and not rejected. A Google one-tap sheet appeared unprompted on the phone profile. It was closed. Continue was not clicked.

## Header

Present on the homepage at 1440.

| Control | Kind | Opens |
|---|---|---|
| Logo | link | https://quizlet.com/ |
| Teachers | link | https://quizlet.com/sign-up?signupOrigin=teacher-global-nav-button&isTeacherSignup=true. Not followed. |
| Study tools | button | A menu. Students: Flashcards, Learn, Study Guides, Test, Expert Solutions, Study groups, Learning games. Teachers: Live, Blast. |
| Subjects | button | A menu. Headings: Exams, Literature, Arts and Humanities, Languages, Math, Science, Social Science, Other. |
| Create | button | A menu: Flashcard set, Folder, Study group. Items have no public href in the dump. Not clicked. |
| Search | combobox, aria Search | Already in the bar. Placeholder rotates among practice tests, flashcards, a question, and study guides. |
| Log in | button | A dialog on the homepage. Not an anchor. |
| Sign up for free | button | A dialog on the homepage. |

Study tools menu items:

| Item | Href |
|---|---|
| Flashcards | /features/flashcards |
| Learn | /features/learn |
| Study Guides | /study-guides/upload |
| Test | /features/test |
| Expert Solutions | /explanations |
| Study groups | /features/study-groups |
| Learning games | /features/learning-games |
| Live | /features/live |
| Blast | /features/blast |

Subjects exam links that were in the menu dump:

| Item | Href |
|---|---|
| IELTS | /exams/international-english-language-testing-system-academic/16788060 |
| TOEFL | /exams/test-of-english-as-a-foreign-language-internet-based-test/16785257 |
| TOEIC | /exams/toeic-listening-and-reading-test/16788273 |
| SAT | /content/digital-sat-practice-and-test |
| ACT | /content/act-practice-questions |
| AP | /content/ap-exams |
| DMV Learner's Permit | /content/dmv-practice-tests-center |

Literature, Arts and Humanities, Languages, Math, Science, Social Science, and Other were headings. Their child links were not fully dumped. Escape did not close the product menus, so the Subjects and Create shots still show the earlier menus beside them.

## Homepage body

Headline "How do you want to study?". Cards Record Lecture, Study Guides, Flashcards, and Games link to https://quizlet.com/sign-up. Not followed from the cards. "I'm a teacher" links to https://quizlet.com/teachers. A promo banner links to /worldrecord?source=banner. Its Close control hides the promo. RSVP was not clicked.

## Footer

Shot: [home-light-footer](screenshots/home-light-footer.png). Columns About, For students, For teachers, Resources, plus language, Country, social, copyright, and COPPA.

| Control | Opens |
|---|---|
| About Quizlet | https://quizlet.com/mission |
| How Quizlet works | https://quizlet.com/features/how-quizlet-works |
| Careers | https://quizlet.com/careers |
| Advertise with us | https://quizlet.com/ads/home |
| Flashcards | https://quizlet.com/features/flashcards |
| Test | https://quizlet.com/features/test |
| Learn | https://quizlet.com/features/learn |
| Study groups | https://quizlet.com/features/study-groups |
| Solutions | https://quizlet.com/explanations |
| Modern Learning Lab | https://quizlet.com/content/modern-learning-lab |
| Quizlet Plus | https://quizlet.com/upgrade?source=footer |
| Study Guides | https://quizlet.com/study-guides/upload |
| Pomodoro timer | https://quizlet.com/features/pomodoro-timer |
| Learning games | https://quizlet.com/features/learning-games |
| Live | https://quizlet.com/features/live |
| Blog | https://quizlet.com/blog |
| Be the Change | https://quizlet.com/features/bethechange |
| Quizlet Plus for teachers | https://quizlet.com/upgrade?showTeacher&source=footer |
| Teachers | https://quizlet.com/teachers |
| Help center | https://quizlet.com/help |
| Sign up | https://quizlet.com/sign-up?signupOrigin=global-footer |
| Honor code | https://quizlet.com/honor-code |
| Community guidelines | https://quizlet.com/guidelines |
| Accessibility statement | https://quizlet.com/accessibility |
| Terms | https://quizlet.com/tos |
| Privacy | https://quizlet.com/privacy |
| California Privacy | https://quizlet.com/privacy#california |
| Your Privacy/Cookie Choices | https://quizlet.com/your-privacy-choices |
| Interest-Based Advertising | https://quizlet.com/privacy#your_choice_personal_information_title |
| Quizlet for Schools | https://quizlet.com/features/quizletforschools |
| Parents | https://quizlet.com/features/family-plan |
| Content hub | https://quizlet.com/content/hub |
| AI tools | https://quizlet.com/features/ai-study-tools |
| Get the app | https://quizlet.com/mobile |
| Ads and Cookie Settings | button. Not clicked. |

Country links in the footer: /ca, /gb, /au, /nz, /de, /fr, /es, /it, /jp, /kr, /in, /cn, /mx, /se, /nl, /ch, /br, /pl, /tr, /ua, /tw, /vn, /id, /ph, /ru. Not followed.

## Phone

At 390 the header collapses to a menu button. The drawer lists Students tools, Teachers Live and Blast, and Subjects. Shot: [nav-light-phone-menu](screenshots/nav-light-phone-menu.png). An App Store badge overlaps the bottom of the drawer. That is site chrome.

## Walls this pass does not enter

| Control | Why it stops |
|---|---|
| Log in | Dialog on the homepage. Empty username and password fields. Google, Facebook, Apple, and WhatsApp are listed and were not clicked. Forgot password and magic link were not clicked. Shot: [login-light-empty](screenshots/login-light-empty.png). |
| Sign up for free | Dialog on the homepage. Birthday, email, and password empty. Terms checkbox unchecked. Identity providers not clicked. Shot: [signup-light-empty](screenshots/signup-light-empty.png). |
| Create menu items | Flashcard set, Folder, Study group. Not clicked. The flashcards marketing page sends "Create a flashcard set" to a login URL. That link was not followed. |
| Press and Hold captcha | A new browser context, and a later location change to a study-set URL, painted "Access to this page has been denied". Not solved. |
| Google one-tap | Appeared unprompted on the phone profile. Closed. Continue was not clicked. |
| Trial | The upgrade page was photographed. The trial button was not clicked. |

## Pages opened from the tree

| Control | Landed | Shot |
|---|---|---|
| Homepage | https://quizlet.com/ | [home-light-default](screenshots/home-light-default.png) |
| Study tools, Flashcards | https://quizlet.com/features/flashcards | [flashcards-light-default](screenshots/flashcards-light-default.png) |
| Footer, Quizlet Plus | https://quizlet.com/upgrade | [pricing-light-default](screenshots/pricing-light-default.png) |
| Footer, scrolled | https://quizlet.com/ | [home-light-footer](screenshots/home-light-footer.png) |
| Search field | stayed on the homepage | [search-light-open](screenshots/search-light-open.png). Typed algebra. Did not submit. No suggestion list. |

## Not opened

| Target | Why |
|---|---|
| Public study set | An earlier preview load of a public set rendered terms. A later navigation to that URL hit Press and Hold. No study-set screenshot is in this package. |
| Teachers page | Text loaded once, then a captcha covered the frame. The shot was discarded. |
| Learn, explanations, search results | Direct navigations in a new context hit Press and Hold. Discarded. |
| Phone inner page | A phone flashcards shot was covered by a captcha and discarded. |
| Identity providers, forms, trials | Stopped at the empty walls. |
