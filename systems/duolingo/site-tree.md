# Duolingo public site tree

Mapped on 2026-11-22 from https://www.duolingo.com/, signed out, in a fresh browser. Homepage `data-duo-theme` is `light`. Body background `rgb(255, 255, 255)`. The footer paints owl green `rgb(88, 204, 2)`.

Desktop CSS viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2. Phone CSS viewport measured 390 by 844 at device pixel ratio 2.

No cookie banner covered the page. Nothing was accepted or rejected.

## Homepage header

Present at 1440 and at 390. There is no hamburger on the homepage.

| Control | Kind | Opens |
|---|---|---|
| Duolingo wordmark | link | https://www.duolingo.com/ |
| Site language: English | button | A language list. On the homepage click it did not paint a menu in the hero. The same control on the chess page painted a two-column language list in an earlier pass. Footer "Site language" is the list that was photographed as links. Language hosts were not followed. |
| Get started | link | https://www.duolingo.com/register. Course picker, photographed empty. No course was chosen. |
| I already have an account | button | Login overlay on `https://www.duolingo.com/?isLoggingIn=true`. Photographed empty. |

## Homepage body

| Control | Kind | Opens |
|---|---|---|
| Course strip | links | One public page per course, for example `/course/es/en/Learn-Spanish`, `/chess`, `/math`. Spanish was not opened. Chess was opened as the inner marketing page. |
| research shows that it works | link | https://www.duolingo.com/efficacy |
| App Store, Google Play | links | Off-site. Not followed. |
| Certify your English | link | https://englishtest.duolingo.com/en. Left the product. Not followed. |
| Try 1 week free | button | Not clicked. |
| Get started, lower | link | `/register` again. Not followed a second time. |

## Footer

Shot: [home-light-footer](screenshots/public-2026-11/home-light-footer.png). The footer paints owl green. A white bar with the wordmark and Get started stays above it.

| Control | Opens |
|---|---|
| Courses | https://www.duolingo.com/courses |
| Mission | https://about.duolingo.com |
| Approach | https://about.duolingo.com |
| Efficacy | https://www.duolingo.com/efficacy |
| Duolingo Handbook | https://duolingo.com/handbook |
| Research | https://research.duolingo.com |
| Careers | https://careers.duolingo.com/#careers |
| Store | https://store.duolingo.com/ |
| Press | https://press.duolingo.com |
| Investors | https://investors.duolingo.com |
| Contact us | https://about.duolingo.com#contact |
| Duolingo | https://www.duolingo.com/ |
| Duolingo for Schools | https://schools.duolingo.com/ |
| Duolingo English Test | https://englishtest.duolingo.com/en |
| Podcast | https://podcast.duolingo.com |
| Duolingo for Business | https://www.duolingo.com/business |
| Super Duolingo | https://www.duolingo.com/super |
| Gift Super Duolingo | https://www.duolingo.com/gift |
| Duolingo Max | https://blog.duolingo.com/duolingo-max/ |
| Duolingo for Android, Duolingo for iOS | Store listings. Not followed. |
| Duolingo FAQs | https://www.duolingo.com/help |
| Schools FAQs | Zendesk help. Not followed. |
| Duolingo English Test FAQs | Off-site. Not followed. |
| Status | https://status.duolingo.com/ |
| Community guidelines | https://www.duolingo.com/guidelines |
| Terms | https://www.duolingo.com/terms |
| Privacy | https://www.duolingo.com/privacy |
| Do Not Sell or Share My Personal Information | about.duolingo.com. Not followed. |
| Blog, Instagram, TikTok, Twitter, YouTube, LinkedIn | Off-site. Not followed. |
| Site language links | Locale hosts such as `en.duolingo.com`. Not followed. |

## Inner pages that were opened

| Page | URL | What it showed |
|---|---|---|
| Courses | /courses | Public catalog, "Courses for English Speakers". Course cards with learner counts. Header is macaw blue with Login and Get started. "I speak English" is a control on the same page. It was not changed. |
| Schools | https://schools.duolingo.com/ | Public marketing page. A banner says Duolingo for Schools will sunset on July 31, 2027. Login is in the header. Login was not clicked. |
| Efficacy | /efficacy | Public page. Nav: Efficacy, Method, Studies, Resources, Research. None of those tabs were opened. |
| Help | /help | Help Center. FAQ groups. Accordions were not opened. No search field was visible. |
| Chess | /chess | Public marketing page. Mint hero. Start playing and I already have an account. A phone mock shows a unit card. Start playing was not clicked. |
| Register | /register | "I want to learn..." course cards. No card was chosen. |

## Login and signup walls

Login is an overlay on the homepage, reached from "I already have an account". The address becomes `https://www.duolingo.com/?isLoggingIn=true`. That query is a public flag, not a session. Fields were empty. Google, Facebook, and Apple were visible and not clicked. Forgot was not clicked. Log in was not clicked. A reCAPTCHA notice is text. No captcha was solved.

Sign up is the next overlay, reached from the Sign up control on the login wall. It asks "How old are you?" with an empty Age field. Next is disabled. Age was not typed. Next was not clicked. Login in the corner was not used to go further.

## Phone

At 390 the homepage stacks the illustration, the headline, Get started, and I already have an account. There is no drawer.

The courses page at 390 hides Login and Get started behind a hamburger. That control opens a small menu, not a full-screen drawer: Sign in, Get started, Download the Duolingo app, Site language: English. Sign in was not clicked. Course cards become a two-column grid.

## Not opened

Spanish and the other course landing pages, Math, Super, Gift, Business, Handbook, about, careers, store, press, investors, podcast, English Test, status, terms, privacy, guidelines, store listings, and social profiles. No course card on `/register` was chosen. No lesson was started. A signed-in app was not opened.
