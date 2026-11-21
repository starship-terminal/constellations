# Tilda public site tree

Mapped from the English homepage [https://tilda.cc/](https://tilda.cc/) on 2026-11-21 in headless Chromium (Playwright), viewport 1440×900, before screenshots. The page title was "Create a Website for Free. Tilda Website Builder". `html lang` is `en`. No theme switch exists on the public marketing shell. The cookie banner is hidden in captures and never answered.

Auth walls are recorded and not entered. No email, password, name, survey, newsletter, or cookie preference was typed or submitted.

## Header controls

The header is `#t-header` (record type 934). At 1440 and at 390 it paints the same wordmark and links. No hamburger was found at 390×844.

| Control | Opens |
|---|---|
| Wordmark "Tilda Publishing" | [https://tilda.cc/?lang=en](https://tilda.cc/?lang=en) (same homepage) |
| PRICING | [https://tilda.cc/pricing/](https://tilda.cc/pricing/) |
| #MADEONTILDA | [https://tilda.cc/madeontilda/](https://tilda.cc/madeontilda/) |
| BLOG | [http://blog-en.tilda.cc/](http://blog-en.tilda.cc/) (separate host) |
| MORE (`li.tmain-submenu__hooklink`) | Click toggles `.tmain-submenu__container` (class `tmain-submenu__container_show`, display flex, about 572px tall). Hover alone left it `display: none`. Close control is `.tmain-submenu__close`. Stays on `/`. |
| LOG IN (`a.t934__enter`) | [https://tilda.cc/login/](https://tilda.cc/login/) auth wall. Stop. |
| SIGN UP (`a.t934__reg`) | [https://tilda.cc/registration/](https://tilda.cc/registration/) auth wall. Stop. |

## MORE menu

One panel, four category headings. Each row is an `a.tmain-submenu__link` (languages use `a.tmain-submenu__lang`).

### Platform

| Label | Opens |
|---|---|
| Home Page | `/` |
| Pricing | `/pricing/` |
| All the Features | `/en/features/` |
| Templates | `/tpls/` |
| Website Examples | `/madeontilda/` |
| Blog | `http://blog-en.tilda.cc/` |
| Website Builder | `/lp/website-builder/` |
| Create a Landing Page | `/lp/create-a-landing-page-for-business/` |
| Creating an Online Store | `/lp/build-online-store/` |
| Create a Company Blog | `/lp/create-blog/` |
| Create Online Courses | `/lp/course-builder/` |
| SEO on Tilda | `/lp/seo/` |
| Email Campaign Builder | `/lp/email-campaign-builder/` |
| Online Form Builder | `/lp/forms/` |
| Zero Block. Web Design Editor | `http://zero.tilda.cc/` |
| Step-by-Step Animation | `/lp/step-by-step-animation/` |
| Tilda CRM | `/lp/crm/` |
| Membership | `/lp/membership/` |
| Create a Quiz | `/lp/quiz/` |
| AI Website Builder | `/lp/ai/` |
| MCP Server | `https://blog-en.tilda.cc/mcp-server` |
| CMS Feeds | `/lp/feeds/` |
| Tilda Docs | `/lp/docs/` |
| Adaptive Image Loading | `/lp/image-optimization/` |
| Digital Accessibility | `/lp/accessibility/` |
| Solutions | Opens a nested flyout inside the MORE panel (chevron on the row). The flyout was not expanded in this capture, so its child links are not listed. |
| Platform Overview | `/lp/review/` |
| Media Kit | `/mediakit/` |
| Terms of Service | `/terms/` |
| Privacy Policy | `/privacy/` |
| Language links | `/ru/`, `/?lang=en`, `https://tilda.kz/kk/?lang=kk`, `/es/`, `/pt/`, `/fr/`, `/de/`, `/ua/`, `/ja/`, `/cn/` |

### Support

| Label | Opens |
|---|---|
| Help Center | `https://help.tilda.cc` |
| FAQ | `/en/answers/` |
| Video Tutorials | `https://tilda.education/en/#videotutorials` |
| Code Export and API | `https://help.tilda.cc/#developers` |
| Abuse | `/abuse/` |

### Education

Coursebook and article links on `tilda.education` (Landing Page Coursebook, How to Make a Website, Zero Block guide, navigation, SEO, design mistakes, web animation, storytelling, fonts, video tutorials). Not the product chrome. One article is linked from the homepage card row and was not walked further.

### More

| Label | Opens |
|---|---|
| Free Icons for Business | `/free-icons/` |
| Campaign URL Builder | `/utm/` |
| Color Library | `/colors/` |
| Hire a Designer | `https://experts.tilda.cc/` |
| Tilda Sans Typeface | `/lp/tildasans/` |
| Broken Link Checker | `/broken-links` |
| Online Vector Editor | `/vector` |

## Homepage interactions that are not navigation

| Control | What it does |
|---|---|
| Cookie banner `#cookiebanner` (record 972) | "Accept all", "Reject all", "Cookie settings". Settings opens a checkbox panel (`input[name=cookie_type]`). Not clicked in the capture. Hidden with CSS. |
| Cookie Policy link | `/cookie-policy/` |
| Hero and section CTAs "Create a website for free" / "Get started" | `/registration/` auth wall. Stop. |
| In-page "Overview" | `#overview` on the same page |
| Feature carousel arrows (`.t-slds__arrow`, `.t1196__control`) and bullets | Change the visible slide. Local UI. |
| Feature cards (CRM, Feeds, MCP, Quiz, Members, Courses, Catalog, Experts, Docs, Email) | Same destinations as the MORE menu rows |
| Three `.t-popup` dialogs, closed (`display: none`) | Anchored by cards whose href is `#landing-page`, `#store`, `#zero` ("How to make a landing page", "How to build an online store", "How to design in Zero Block"). Close control is `button[aria-label="Close dialog window"]`. |
| Article cards (`a.t-card__link`) | External education articles, `target=_blank` |

## Auth walls (stop)

| URL | What loaded | What was not done |
|---|---|---|
| [https://tilda.cc/login/](https://tilda.cc/login/) | Title "Sign in - Tilda". Email field `#email`, password field `#password`, button "Log in", links "Sign up" and "Forgot password?". No Google or Apple button. | Password not submitted. Email not typed. |
| [https://tilda.cc/registration/](https://tilda.cc/registration/) | Title "Registration - Tilda". Name, email, password, button "Sign up". | No field typed. Not submitted. |

## Capture set

Representative public pages from the header and MORE menu, each at 1440×900 and 390×844:

- `/` home, including the opened MORE panel
- `/pricing/` plan cards and currency select
- `/en/features/`
- `/tpls/` template gallery and category radios
- `/madeontilda/`
- `/en/answers/` FAQ search field (typed into, not submitted) and a category panel
- `/colors/` published palette
- `/lp/ai/`
- `/lp/tildasans/`
- `/terms/`
- `/login/` and `/registration/` as wall screenshots only

Not captured as separate pages: the long tail of `/lp/*` marketing pages (same block system as home), `blog-en.tilda.cc`, `help.tilda.cc`, `tilda.education`, `experts.tilda.cc`, `zero.tilda.cc`, other languages, and the editor behind login.
