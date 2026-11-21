# Promova public site tree

Mapped from https://promova.com/ on 2026-11-21 in headless Chromium (Playwright), signed out, before screenshots. The homepage loaded (HTTP 200, title "Promova – Your Online Language Learning App & Language Courses").

This tree records every visible control on the homepage and where it goes. Auth, signup, onboarding, and form branches stop at the wall. No form was submitted. No password, code, Google, or Apple control was used.

Locale switches (`/es`, `/pt`, `/fr`, `/uk`, `/el`) are the same marketing site in another language. They were recorded and not captured as separate states.

## Header (desktop)

| Control | Opens |
|---|---|
| Wordmark | Page https://promova.com/ |
| Languages (button, `aria-haspopup=menu`) | Menu. See Languages menu. |
| Courses (button, `aria-haspopup=menu`) | Menu. See Courses menu. |
| Why Promova (button, `aria-haspopup=menu`) | Menu. See Why Promova menu. |
| Resources (button, `aria-haspopup=menu`) | Menu. See Resources menu. |
| SIGN UP | Auth wall https://promova.com/sign-up. Title "Promova \| Sign up". No email form rendered; only footer legal text. Branch stopped. |
| GET STARTED | Onboarding wall https://promova.com/foxtrot/org-main?screen=1. Title "Learn Languages". Screen 1 of 15, "I want to learn …" language picker. Branch stopped. No option was chosen. |

## Languages menu

Each item is a page.

| Item | Opens |
|---|---|
| Learn English (POPULAR) | https://promova.com/learn-english-online |
| Learn Spanish | https://promova.com/page/learn-spanish-language |
| Learn French | https://promova.com/page/learn-french |
| Learn German | https://promova.com/page/learn-german |
| Learn Italian | https://promova.com/page/learn-italian |
| Learn Korean | https://promova.com/page/learn-korean-language |
| Learn Japanese | https://promova.com/page/learn-japanese-online |
| Learn Chinese | https://promova.com/page/learn-chinese |
| Learn Arabic | https://promova.com/page/learn-arabic-online |
| Learn Portuguese | https://promova.com/page/learn-portuguese-online |
| Learn Ukrainian | https://promova.com/page/learn-ukrainian-online |
| Learn Latin American Spanish | https://promova.com/page/learn-latin-american-spanish |
| American Sign Language | https://promova.com/page/learn-american-sign-language |

## Courses menu

Each item is a page.

| Item | Opens |
|---|---|
| Promova x Oleksandr Usyk | https://promova.com/page/learn-with-usyk |
| Online language course | https://promova.com/course/online-language-course |
| Promova AI Tutor | https://promova.com/page/ai-tutor |
| Learn English with AI | https://promova.com/page/practice-with-ai |
| Learn Spanish with AI | https://promova.com/page/ai-spanish-tutor |
| Speak with AI | https://promova.com/page/speak-with-ai |
| Business English | https://promova.com/practice/business-english |
| English for travel | https://promova.com/practice/english-for-travel |
| English for work | https://promova.com/page/english-for-work |
| English for it | https://promova.com/page/english-for-it |
| English for marketing | https://promova.com/page/english-for-marketing |
| English for engineers | https://promova.com/page/english-for-engineers |
| English for finance | https://promova.com/page/english-for-finance |
| English for negotiating | https://promova.com/page/english-for-negotiating |
| Public Speaking Classes | https://promova.com/page/presentation-skills-english-lessons |
| English For Public Speaking | https://promova.com/page/english-for-public-speaking |
| Brainrot course | https://promova.com/page/brainrot-slang-course |
| Neurodiversity in the Workplace | https://promova.com/page/neurodiversity-for-companies |

## Why Promova menu

Each item is a page.

| Item | Opens |
|---|---|
| Who we are | https://promova.com/who-we-are |
| Promova features | https://promova.com/page/promova-features |
| Promova reviews | https://promova.com/page/promova-review |
| Promova's Educational Board | https://promova.com/page/edu-board |
| Our Editorial Process | https://promova.com/our-editorial-process |
| Android language learning app | https://promova.com/app/language-learning-app-for-android |
| IOS language learning app | https://promova.com/app/ios-language-learning-app |
| AI language learning app | https://promova.com/page/ai-language-learning-app |

## Resources menu

Each item is a page.

| Item | Opens |
|---|---|
| Our blog | https://promova.com/blog |
| Language learning tools | https://promova.com/page/language-learning-tools |
| English grammar | https://promova.com/skills/english-grammar |
| English vocabulary | https://promova.com/skills/english-vocabulary |
| English pronunciation | https://promova.com/skills/english-pronunciation |
| Spanish grammar | https://promova.com/skills/gramatica-en-espanol |
| English Level Test | https://promova.com/test-your-english-level |
| Spanish Level Test | https://promova.com/page/spanish-level-test-online |
| French Level Test | https://promova.com/page/french-level-test-online |
| German Level Test | https://promova.com/page/german-level-test |
| Italian Level Test | https://promova.com/page/italian-level-test |

## Homepage body controls

| Control | Opens |
|---|---|
| TRY NOW (hero and repeated CTAs) | Onboarding wall https://promova.com/foxtrot/org-main?screen=1. Branch stopped. |
| Language chips (English, Spanish, French, German, Italian, Japanese, Korean, Chinese, Portuguese, Spanish LATAM, Arabic, Ukrainian) | Local filter or scroll on the homepage. Not a new page. Not a form submit. |
| view all | Expands the language chip list on the page. Local state. |
| Previous review / Next review | Local carousel. Stays on the homepage. |
| Blog cards (Best Language Learning Apps in 2026, Basic Japanese Phrases, and siblings) | Blog article pages under https://promova.com/blog/. Representative articles captured; the full article catalog is not enumerated here. |
| START SPEAKING (promo band) | Onboarding wall https://promova.com/foxtrot/learn-english-with-usyk?screen=1. Branch stopped. |
| App Store / Google Play / AppGallery badges | External store links on promova.onelink.me. Not captured (leaves the site). |
| Locale links (English, Español, Português, Français, Українська, Ελληνικά) | Same marketing site at `/`, `/es`, `/pt`, `/fr`, `/uk`, `/el`. Recorded, not captured as separate packages. |

## Phone header (390)

The desktop nav buttons are not in the phone header. A control labelled "side navigation" opens a drawer. Inside it, Languages, Courses, Why Promova, and Resources each open a nested panel. "close side navigation" and "close all and return to main" close those panels. The drawer links match the desktop menus above.

## Footer

Company, language, app, course, skill, and legal links. Social icons leave the site (Instagram, Facebook, TikTok, YouTube) and were not followed.

| Group | Opens |
|---|---|
| Company (Our blog, Who we are, Editorial Process, Educational Board, reviews, Ambassador, Affiliate, Promova for Good, Press Center, Contact us, FAQ, Sitemap) | Pages on promova.com. Contact us has an email and message form. Not submitted. |
| Learn languages | Same language pages as the Languages menu, plus Japanese is in the menu and not repeated in every footer column. |
| App pages | https://promova.com/app/* and selected https://promova.com/page/* product pages. |
| Skills and tools | https://promova.com/skills/* and tool pages. |
| Terms | https://promova.com/terms/terms-and-conditions |
| Privacy | https://promova.com/terms/privacy-policy |

Footer links that are not already in a header menu:

| Item | Opens |
|---|---|
| Ambassador Program | https://promova.com/page/ambassador |
| Affiliate Program | https://promova.com/online/affiliate |
| Promova for Good | https://promova.com/page/promova-4-good |
| Press Center | https://promova.com/press-center |
| Contact us | https://promova.com/contact-us (form present, not submitted) |
| FAQ | https://promova.com/faq |
| Sitemap | https://promova.com/sitemap |
| Free for Ukraine | https://promova.com/free-for-ukraine |
| How to pronounce | https://promova.com/how-to-pronounce |
| Synonyms | https://promova.com/synonyms-of |
| Past tense | https://promova.com/past-tense-of |
| Part of speech | https://promova.com/what-part-of-speech |
| Antonyms | https://promova.com/antonyms-of |

## Auth and dead ends

| URL | Result |
|---|---|
| https://promova.com/sign-up | Auth wall. No email field rendered. Footer legal text only. Stopped. |
| https://promova.com/sign-in | Login wall. Title "Promova \| Log in". No email form rendered. Stopped. |
| https://promova.com/login | 404 "page not found" with the marketing shell and "GO TO HOMEPAGE". |
| https://promova.com/foxtrot/org-main?screen=1 | Onboarding quiz, screen 1 of 15. Stopped. No answer chosen. |
| https://promova.com/pricing | 404 "page not found". No public pricing page at this path. |
| Google / Apple | Not present as clickable controls on the loaded sign-up page. Not used. |

## Capture set

Representative public pages, desktop 1440x900 and phone 390x844: home (menus, language chips, review carousel, phone drawer), one language page, one course page, features, who we are, FAQ (search field, not submitted), blog index, contact (form visible, not filled), one level-test landing, privacy, 404, and the two walls above as evidence that the branch stops. Sibling marketing pages share the same shell and were not each screenshotted.
