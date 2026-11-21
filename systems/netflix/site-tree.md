# Netflix public site tree

Mapped from the public marketing homepage before screenshots, in headless Chromium, on 2026-11-21. The homepage at `https://www.netflix.com/` redirects to a regional marketing URL. This file names controls and destinations. It does not name the region, and it stores no email, phone, or location.

No password, code, captcha, or identity-provider control was used. No email or phone was typed. No form was submitted.

## Homepage

URL: `https://www.netflix.com/` then the regional marketing path. Theme: one dark marketing surface. No theme toggle.

| Control | Opens |
|---|---|
| Wordmark | Stays on the marketing homepage |
| Language `select` (header and footer), options English and the other published locale | Reloads the same marketing page in that locale. Native select popup; headless capture cannot show the OS menu |
| Sign In | Login wall. Stop. Known wall shape: email or mobile number, password, Continue. Do not type or submit |
| Email address field (hero and lower CTA) | Focuses an empty email field. Not typed |
| Get Started | Would submit the email form. Not clicked |
| Trending title button (`top-10-element-*`) | Title preview dialog on the same page (`title-modal`): synopsis, rating, Get started |
| Get started inside the title dialog | Signup wall. Not clicked |
| Trending Next | Scrolls the title row. Stays on the homepage |
| FAQ question buttons (six) | Expands that answer in place. Questions: What is Netflix?, How much does Netflix cost?, Where can I watch?, How do I cancel?, What can I watch on Netflix?, Is Netflix good for children? |
| Footer: Questions? Contact us. | `https://help.netflix.com/contactus` (help contact). Issue field not typed |
| Footer: FAQ | `https://help.netflix.com/support/412` (help article) |
| Footer: Help Centre | `https://help.netflix.com/` |
| Footer: Account | `https://www.netflix.com/youraccount` redirects to the login wall. Stop |
| Footer: Media Centre | `https://media.netflix.com/` (separate media-center surface). The public homepage headline names a place, so that screenshot is not in the package |
| Footer: Investor Relations | `http://ir.netflix.com/` redirects to the investor profile on `ir.netflix.net` |
| Footer: Jobs | `https://jobs.netflix.com/jobs` redirects to `https://jobs.netflix.com/` |
| Footer: Ways to Watch | `https://www.netflix.com/watch` redirects to the help devices article |
| Footer: Terms of Use | `https://help.netflix.com/legal/termsofuse` |
| Footer: Privacy | `https://help.netflix.com/legal/privacy` |
| Footer: Cookie Preferences | OneTrust Privacy Preference Center dialog on the same page. Not saved |
| Footer: Corporate Information | Help corporate article. Not captured: the page prints contact addresses |
| Footer: Contact Us | Same help contact page as Questions? Contact us. |
| Footer: Speed Test | `https://fast.com/` |
| Footer: Legal Notices | `https://help.netflix.com/legal/notices` |
| Footer: Only on Netflix | Public originals grid on the marketing host (`/browse/genre/839338`, with a region segment in the path) |

Hidden until Cookie Preferences is opened: OneTrust close, cookie-detail, back, filter, clear, apply, cancel, save. Save and Apply were not clicked.

## Title page

Reached from a trending title's public title URL (example shape `/title/<id>`), not by typing.

| Control | Opens |
|---|---|
| Netflix Home | Marketing homepage |
| Sign In | Login wall. Stop |
| Trailers, Episodes, More to watch, Plans | In-page anchors on the same title URL |
| Previous / Next navigation | Scrolls the in-page nav |
| Join now | Signup wall (`/signup`, plan step). Not clicked |
| Play, Unmute, Expand, Subtitles | Hero playback controls on the public title page |
| Trailer and teaser cards | Trailer playback on the same page. Not started, so the branch stays on the settled page |
| More-to-watch titles | Other public `/title/<id>` pages. One title page stands for the pattern |
| Email + Join now blocks | Signup. Not typed, not submitted |

## Originals grid

Footer "Only on Netflix" opens a public genre page: heading, email + Join now (not used), horizontal rows with Next, and title links to `/title/<id>`.

## Login and signup walls

| URL | What it asks | Action |
|---|---|---|
| Regional `/login` | Email or mobile number, password, Continue, Get help | Recorded. Not typed. Not submitted. Get help not followed |
| `/youraccount` | Redirects to the same login wall | Stop |
| `/signup` | Step 1 of 3, Choose your plan, Next | Recorded. Next not clicked. No plan, birthday, profile, or payment field filled |

## Help Center (`help.netflix.com`)

Public. Header: logo (netflix.com), Help Center, Join Netflix (`/signup` wall, not followed), Sign in (login wall, not followed).

| Control | Opens |
|---|---|
| Search field | Focus only. No query typed, no search submitted |
| Popular topic links | Help articles (signup, plans, sign-in, parental controls). Plans article captured as the pricing article |
| Topic tiles | Topic hubs. Not each hub; the home plus three articles stand for the pattern |
| Contact issue field | Not typed |
| Contact quick links (reset password, update email, sign-in help, payment) | Account walls. Stop |
| Article Yes / No | Feedback controls. Not clicked |
| Print | Browser print. Not used |
| Language select | Locale reload. Not changed |

Captured help pages: home, the FAQ article linked from the marketing footer, the devices article (Ways to Watch), Terms of Use, Privacy (first viewport; the page is longer than the capture cap), Legal Notices (first viewport).

## Sibling sites linked from the footer

These load as their own public surfaces. Each is one desktop viewport plus the phone homepage where noted. Their inner search, apply, and sign-in branches stop.

| Site | First screen | Stopped branches |
|---|---|---|
| Media Center | Stories grid, interest chips, search. Screenshot omitted: the headline names a place | Press Log In, Apply, article bodies |
| Jobs | Campaign homepage, location and team selects, keyword field | Keyword not typed. View roles (another host) not followed |
| Investor profile | Company profile, section nav, keyword search | Search not submitted. Later financial pages not followed |
| Speed test | Result readout, language control, privacy link | Privacy article not followed. No number entered |

## Phone (390)

Same homepage controls, stacked. No separate hamburger was present on the marketing homepage. Sign In, language select, FAQ, trending titles, and footer links are the same destinations as desktop. Title, login wall, help home, and originals grid were opened at phone width. Signup Next, email fields, and identity providers were not used.
