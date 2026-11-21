# Clearful public site tree

Mapped on 2026-11-21 from [https://clearful.com/](https://clearful.com/) in headless Chromium, signed out. Each row is a control that was visible on the page and the page, menu, or overlay it opened. Login and signup branches stop at the wall. No form was submitted. No email or password was typed. Apple, Google, and the other identity buttons were not clicked.

## Home, desktop 1440

The nav is a Webflow navbar (`.navbar1_component`, 72px). It has no dropdown. The hamburger (`.w-nav-button`) is in the DOM and hidden at this width.

| Control | Opens |
|---|---|
| Logo | [https://clearful.com/](https://clearful.com/) |
| Guided Journals | [https://clearful.com/library](https://clearful.com/library) |
| Log In | [https://app.clearful.com/#/sign-in](https://app.clearful.com/#/sign-in). Sign-in wall. Branch stops. |
| Start a journal — it's free (nav pill) | Get-app overlay (`.modal_get-app`) on the same page. Close returns to the page. |
| Start journaling for free (hero) | Same get-app overlay. |
| Start a journal for free (lower CTA) | Same get-app overlay. |
| Weekly, Monthly, Quarterly, Bi-Yearly, Yearly | Timeline tabs on the home page (`a.w-tab-link`). They swap a pane. They do not navigate. |
| What's New (footer) | [https://clearful.com/whats-new](https://clearful.com/whats-new) |
| Home Screen Widgets | [https://clearful.com/apple-widgets-for-ios](https://clearful.com/apple-widgets-for-ios) |
| Flow Editor | [https://clearful.com/flow-editor](https://clearful.com/flow-editor) |
| Journaling Library | [https://clearful.com/library](https://clearful.com/library) |
| Journal Prompts | [https://clearful.com/journal-prompts](https://clearful.com/journal-prompts) |
| Help Center | [https://support.clearful.com/](https://support.clearful.com/) |
| Contact Us | [https://clearful.com/contact-us](https://clearful.com/contact-us) |
| About Us | [https://clearful.com/about-us](https://clearful.com/about-us) |
| Press Room | [https://clearful.com/press-and-media](https://clearful.com/press-and-media) |
| Terms of Service | [https://clearful.com/terms-of-service](https://clearful.com/terms-of-service) |
| Privacy Policy | [https://clearful.com/privacy-policy](https://clearful.com/privacy-policy) |
| App Store, Mac App Store, Google Play (footer and overlay) | Store listings. Off-site. Not captured. |
| Web (overlay) | [https://app.clearful.com/](https://app.clearful.com/). Same sign-in wall. Branch stops. |
| Instagram, X, Facebook, LinkedIn, Pinterest | Off-site social profiles. Not captured. |

## Get-app overlay

Opened by every "Start a journal" control. It is a full-viewport panel, not a new URL.

| Control | Opens |
|---|---|
| Close | Dismisses the overlay. The page stays put. |
| App Store | Apple listing `id1513257639`. Off-site. |
| Mac App Store | Same Apple listing. Off-site. |
| Google Play Store | Play listing `journal.diary.gratitude.mindfulness.selfcare.mental.health`. Off-site. |
| Web | [https://app.clearful.com/](https://app.clearful.com/). Sign-in wall. Branch stops. |

## Phone 390

The desktop nav links collapse. The hamburger (`.w-nav-button`, `aria-expanded`) opens a full-height menu.

| Control | Opens |
|---|---|
| Menu button | Nav drawer: Guided Journals, Log In, Start a journal — it's free. |
| Guided Journals (drawer) | [https://clearful.com/library](https://clearful.com/library) |
| Log In (drawer) | [https://app.clearful.com/#/sign-in](https://app.clearful.com/#/sign-in). Wall. Branch stops. |
| Start a journal — it's free (drawer) | Get-app overlay. |
| Close (drawer) | Dismisses the drawer. |

## Marketing pages reached from the home footer or nav

| Page | Distinct controls beyond the shared nav and footer |
|---|---|
| [https://clearful.com/library](https://clearful.com/library) | 40 journal cards, each to `/library/<slug>`. "See all journal prompts" goes to `/journal-prompts`. Start-a-journal opens the get-app overlay. |
| [https://clearful.com/journal-prompts](https://clearful.com/journal-prompts) | Category links to `/journal-prompts/<slug>` (21 in the sitemap). |
| [https://clearful.com/whats-new](https://clearful.com/whats-new) | Tabs: All, New Features, Product Improvements, New Guided Journals, Bug Fixes. They swap a pane. "Open Clearful" is `https://clearful.page.link/open` (app deep link, not followed). |
| [https://clearful.com/flow-editor](https://clearful.com/flow-editor) | Shared nav and footer, plus the get-app CTA. |
| [https://clearful.com/apple-widgets-for-ios](https://clearful.com/apple-widgets-for-ios) | Shared nav and footer, plus the get-app CTA. |
| [https://clearful.com/about-us](https://clearful.com/about-us) | Shared nav and footer. |
| [https://clearful.com/press-and-media](https://clearful.com/press-and-media) | Shared nav and footer. Press assets link out. |
| [https://clearful.com/pro](https://clearful.com/pro) | Pro marketing. Checkout and account upgrade sit behind the app. Not followed. |
| [https://clearful.com/pricing](https://clearful.com/pricing) | Plan copy. Purchase controls that leave for the app were not followed. |
| [https://clearful.com/contact-us](https://clearful.com/contact-us) | Name, email, and message fields. Not filled. Not submitted. |
| [https://clearful.com/privacy-policy](https://clearful.com/privacy-policy) | Legal text. |
| [https://clearful.com/terms-of-service](https://clearful.com/terms-of-service) | Legal text. |
| [https://clearful.com/new-home](https://clearful.com/new-home) | Alternate home in the sitemap. Same shell as the home page. |
| [https://clearful.com/app-support](https://clearful.com/app-support) | Near-empty Webflow page titled "app-beacon". No further links. |

Two library cards and one prompt page and one post were opened as samples of those templates: `/library/journal-prompts-for-couples`, `/library/reflective-journal-prompts`, `/journal-prompts/anxiety-journal-prompts`, `/post/types-of-journals-exploring-the-different-types-of-journaling`. The other cards use the same template. They were not each photographed.

## Help center

[https://support.clearful.com/](https://support.clearful.com/) is a separate host with its own nav.

| Control | Opens |
|---|---|
| Browse | [https://support.clearful.com/help](https://support.clearful.com/help) |
| Popular | [https://support.clearful.com/popular](https://support.clearful.com/popular) |
| What's new | [https://clearful.com/whats-new](https://clearful.com/whats-new) |
| Open Clearful | `https://clearful.page.link/open`. App deep link. Not followed. |
| Search for an answer | Search field on the same page. Nothing was typed. |
| Topic links | `/help/<topic>/<article>` on support.clearful.com. One article was opened: `/help/getting-started/using-clearful`. |
| Email Clearful Support | `mailto:`. Not opened. |

## Sign-in wall

[https://app.clearful.com/#/sign-in](https://app.clearful.com/#/sign-in) asks to continue with email, Apple, or Google. The branch stops there. Continue with email was not opened, so the email and password fields behind it were not reached. No code was sent.

## Not on the public tree

The journaling canvas, entries, AI reviews, settings, billing, and onboarding live behind the sign-in wall. They were not captured. The sitemap also lists template posts under `/post/` that are Webflow sample articles. One was opened as a template sample. The rest were not.
