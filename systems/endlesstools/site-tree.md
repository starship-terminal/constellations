# Endless Tools public site tree

Mapped on 2026-11-21 from the homepage at https://endlesstools.io/ before any screenshot of this pass. The page title is "Endless Tools". It is a live marketing site, not a parked or captcha wall. The page paints dark (body background `rgb(0, 0, 0)`, `color-scheme: normal`). No page-level theme switch.

The T3 preview tab loaded the homepage and answered DOM reads. Preview screenshots failed twice because the browser was not producing frames ("The browser is not producing screenshot frames"). Control destinations below were read from the live DOM. Photographs of this pass were taken afterwards with the package's public Playwright kit.

Opened means the control was used and the destination was loaded or photographed. Linked means the href was read and the page was not opened from that control. Sign-in, sign-up, and identity-provider walls stop the branch. Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved.

The marketing site is a one-pager. There is no header menu, no dialog, and no in-page route other than `/`. A CookieYes root (`#cookieyes-banner`) is in the DOM and was not answered. The bar has no `<header>` or `<nav>` element.

## Bar, desktop

| Control | Opens |
|---|---|
| Log in | `https://app.endlesstools.io/login`. Login wall. Stopped. |
| Start for free | `https://app.endlesstools.io/login`. Same wall. Not followed from this control. |

A second "Start for free" button sits at the origin with no href. It was not used.

## Homepage body

URL stays `/` unless noted. Prior capture: [home-dark-default.png](screenshots/home-dark-default.png).

| Control | Result |
|---|---|
| Start exploring | `https://app.endlesstools.io/login`. Wall. Not followed. Also a button with no href, not used. |
| Yearly Save 17% | Local billing toggle. Same URL. Photographed as [home-dark-monthly.png](screenshots/home-dark-monthly.png) after Monthly is pressed. |
| Monthly | Local billing toggle. Same URL. Not a purchase. |
| Try for free | `https://app.endlesstools.io/login`. Wall. Not followed. |
| Go PRO | `https://app.endlesstools.io/login`. Wall. Not followed. |
| Get Education | `https://app.endlesstools.io/login`. Wall. Not followed. |
| Create team | `https://app.endlesstools.io/login`. Wall. Not followed. |
| 3D model by ion.fbx | `https://www.fab.com/listings/6efe17ea-b2b8-42cb-bda9-796386bc518a`. External listing. Linked, not followed. |
| CC BY 4.0 | `https://creativecommons.org/licenses/by/4.0/`. External licence. Linked, not followed. |
| Request Education access | `mailto:hi@endlesstools.io?subject=Education%20access%20request`. Mail. Not sent. |
| Previous / Next | Testimonial carousel. Same URL. Not a navigation. |
| Stay updated | Newsletter form (`method=get`, action `/`). Field placeholder "Your email", plus a consent checkbox. Not filled. Not submitted. |
| @framer, @endlesstools, @wabi, @visualelectric, @rodeodotclub, @surrealapp, @toolfolio, and the hashtag links | `https://x.com/...`. External posts. Linked, not followed. |

## Footer

| Control | Opens |
|---|---|
| Privacy Policy | `https://app.endlesstools.io/legal/privacy_policy`. Public legal page. |
| Get in touch | `mailto:hi@endlesstools.io`. Mail. Not sent. |
| Instagram | `https://www.instagram.com/endlesstools/`. External. Linked, not followed. |
| Linked In | `https://eu.linkedin.com/company/endless-tools`. External. Linked, not followed. |
| X | `https://x.com/endlesstools`. External. Linked, not followed. |
| TikTok | `https://www.tiktok.com/@endlesstools`. External. Linked, not followed. |
| Privacy policy | `https://app.endlesstools.io/legal/privacy_policy`. Same public legal page. |
| Terms of use | `https://app.endlesstools.io/legal/terms_of_use`. Public legal page. |

## Phone (390)

The same one-pager. No menu button. Log in and Start for free remain the only bar controls, and both still point at the login wall. Photographed in [mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png).

## Login wall

`https://app.endlesstools.io/login` is the stop. The empty card was photographed. The local "Log in with password" toggle, when present, only swaps the form. It was not filled. Continue, Google, Apple, and any other identity provider were not clicked.
