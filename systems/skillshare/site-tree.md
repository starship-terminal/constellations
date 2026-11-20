# Skillshare public site tree

Mapped on 2026-11-21 from https://www.skillshare.com/ in headless Playwright before screenshots. Signed out. Locale redirect: `/` becomes `/en/`. Viewport used for the map: 1440x900. No form was submitted. No email, password, code, or social login was entered.

Auth wall, recorded and not followed:

| Control | Lands on | Stop |
|---|---|---|
| Header Sign In | https://auth.skillshare.com/u/login (title Log in \| Skillshare) | Auth0 login. Email and password, or Google, Facebook, Apple. Not submitted. |
| Header Sign Up | https://auth.skillshare.com/u/signup (title Sign up \| Skillshare) | Auth0 signup. Not submitted. |
| https://www.skillshare.com/en/login | Stays on `/en/login` (title Sign In - Skillshare) | Email field, Continue with Google, Continue with Facebook, Continue with Apple, Sign In. Not typed. Not clicked. |
| Continue with email (homepage signup module) | Same Auth0 family as Sign Up | Not clicked. Recorded as a wall. |
| Continue with Google, Facebook, Apple | Social login | Not clicked. |
| Start for Free, Enroll, Sign Up to Teach, Join for Free (affiliates) | Signup or partner join | Not followed when the control is an account start. |
| Blog nav Try Skillshare For Free | `/membership/checkout?coupon=blog1month` | Checkout. Not opened. |
| Blog email field | Newsletter | Not typed. Not submitted. |

## Home `https://www.skillshare.com/en/`

Title: Online Classes for Creatives \| Skillshare. H1: Creative Classes Taught by the Best Creative Pros. Page height about 8397px. Light only. No `data-theme`. DataGrail consent aside (`.dg-consent-banner`) is hidden, never answered.

| Control | Opens |
|---|---|
| Logo (aria Home, `/en/?via=header`) | Home |
| Browse (anchor, no href, class `browse`) | Header category menu, stays on `/en/`. Items below. Escape closes it. |
| Search box (combobox, placeholder Search classes, digital products, teachers, and more) | Focus shows an empty suggestion shell. Typing `watercolor` shows a link to `/en/search?query=watercolor&searchMethod=naturalLang`. Public search. Not submitted as an account form. |
| Sign In | Auth wall. Stop. |
| Sign Up | Auth wall. Stop. |
| Continue with Google / Facebook / Apple | Social wall. Stop. |
| Continue with email | Auth wall. Stop. |
| Terms of Service, Privacy Policy (signup module) | `/en/terms`, `/en/privacy`, which redirect to legal.skillshare.com |
| Class cards | `/en/classes/<slug>/<id>` | Cloudflare "Just a moment..." / 403 in this client. Branch stopped. |
| Teacher names on cards | `/user/<handle>` or `/profile/<name>/<id>` | Not opened as a separate capture. Public teacher names. |
| Meet the teacher tiles | `/en/user/<handle>?via=loh` or `/en/profile/...` | Same. |
| Learn More | `/teams?via=loh_rdsgn`, which redirects to `/en/for-teams/home` |
| Footer category columns | `/en/browse/<category>` |
| Footer software links | `/en/search/classes?query=...` or `?software=...` |
| Footer More | Parent browse or `/en/browse?via=footer` |
| About, Careers, Press, Blog, Affiliate Program | `/en/about`, `/en/careers`, `/en/press`, `/en/blog/`, `/en/affiliates` |
| Partnerships | `http://www.skillshare.com/partner/brandpartnerships/` | External partner page. Not captured. |
| Become a Teacher | `/en/teach` |
| Teacher Help Center | help.skillshare.com category | Zendesk. Not the primary capture. |
| Teacher Rules & Requirements | Redirects to legal.skillshare.com article |
| Gift Memberships | `/gift/membership` |
| Digital Products | `/en/shop/digital-products` |
| 1-on-1 Sessions | `/en/one-on-one-sessions` |
| Help | https://help.skillshare.com (Help Center home) |
| Privacy, Terms | legal.skillshare.com articles |
| Your Privacy Choices (`href="#"`) | In-page privacy choices. Not clicked (consent POST risk). Banner hidden. |
| Notice to CA Residents | `/en/privacy#privacy-ccpa` then legal host |
| App Store, Play Store | External store listings. Not captured. |
| Social icons | Instagram, TikTok, Pinterest, X, Facebook, LinkedIn, YouTube. External. Not captured. |

### Browse menu (opened from header Browse)

Stays on `/en/`. No dialog role. Visible links:

| Label | URL |
|---|---|
| AI & Innovation | `/en/browse/ai-innovation?via=header` |
| Animation & 3D | `/en/browse/animation-3d?via=header` |
| Art & Illustration | `/en/browse/art-illustration?via=header` |
| Crafts & DIY | `/en/browse/crafts-diy?via=header` |
| Creative Career | `/en/browse/creative-career?via=header` |
| Creativity & Inspiration | `/en/browse/creativity-inspiration?via=header` |
| Design | `/en/browse/design?via=header` |
| Development | `/en/browse/development?via=header` |
| Film & Video | `/en/browse/film-video?via=header` |
| Home & Lifestyle | `/en/browse/home-lifestyle?via=header` |
| Marketing & Business | `/en/browse/marketing-business?via=header` |
| Music & Audio | `/en/browse/music-audio?via=header` |
| Personal Development | `/en/browse/personal-development?via=header` |
| Photography | `/en/browse/photography?via=header` |
| Productivity | `/en/browse/productivity?via=header` |
| Writing & Publishing | `/en/browse/writing-publishing?via=header` |
| All Classes | `/en/browse?via=header` |
| All Learning Paths | `/en/paths?via=header` |
| All Student Projects | `/en/projects?via=header` |
| Digital Products | `/en/shop/digital-products?via=header` |
| 1-on-1 Sessions | `/en/one-on-one-sessions?via=header` |
| Blog | `/blog?via=header` (serves `/en/blog/`) |

Footer illustration column adds subcategories: Surface & Pattern Design, Drawing & Inking, Painting, Illustration, Lettering & Calligraphy, Mixed Media & Collage, Digital Art, AI for Art & Illustration, More Art & Illustration. Same pattern on other footer columns. One subcategory (illustration) is captured as the filter example. The rest are the same browse template.

## Pages that load

| Page | URL after load | Notes |
|---|---|---|
| Browse all | `/en/browse?via=header` | H1 Online Classes. Buttons: Start for Free (wall), Category. Height about 2500px. |
| Illustration browse | `/en/browse/illustration?via=footer` | H1 Online Illustration Classes. Buttons: Filters, Software, Materials, Category, prev, next. Height about 2965px. |
| Learning paths | `/en/paths?via=header` | H1 Reach Your Learning Goals With Hand-Picked, Sequential Classes. Path cards link to `/en/paths/<slug>`. Enroll is a wall. Height about 8650px. |
| Student projects | `/en/projects?via=header` | H1 Student Projects. Project cards link to `/en/projects/<slug>/<id>`. Public student names. Height about 3229px. |
| Digital products | `/en/shop/digital-products?via=header` | Title Shop Digital Products. Buttons: File Type, Filters, Reset Filters, View results, prev, next. Product links `/en/shop/digital-products/...`. Height about 3070px. |
| 1-on-1 sessions | `/en/one-on-one-sessions` | H1 Learning Just Got Personal With 1-on-1 Sessions. Category links. Search for Teachers field. Show More. Booking is a wall if it asks for an account. Height about 2409px. |
| About | `/en/about` | H1 Inspiring discovery through creativity. Watch Mimi's Story opens a video, not an account. Height about 2053px. |
| Press | `/en/press` | H1 Press & Media. Press links are external articles. Contact is a mailto. Height about 9172px. |
| Blog | `/en/blog/` | Separate blog chrome: Main Menu, Articles, Resources, News, Classes, Load More. Email field not filled. Height about 2600px. |
| Affiliates | `/en/affiliates` | H1 Become a Skillshare Affiliate. Join for Free goes to Impact. Mailto present. Not followed. Height about 2409px. |
| Teach | `/en/teach` | H1 Real humans teaching real creative skills. Sign Up to Teach is a wall. Watch Her Story is a video. Height about 5213px. |
| Gift | `/gift/membership` | H1 Gift a Skillshare Membership. Purchase is a wall. Height about 4995px. |
| Teams | `/teams` redirects to `/en/for-teams/home` | H1 All the Skills Your Creative Team Needs for Today and Tomorrow. Own nav: AI Classes, audience pages, Pricing, Sign In (wall). Height about 6685px. |
| Help Center | https://help.skillshare.com/hc/en-us | Zendesk. H1 Skillshare Help Center. Search field. Language menu (Deutsch, Español, Français, Português). Not submitted. |
| Terms | `/en/terms` redirects to legal.skillshare.com article | Zendesk legal. Height about 26348px. Truncate full-page capture. |
| Privacy | `/en/privacy` redirects to legal.skillshare.com article | Same. Height about 28211px. Truncate. |
| Teacher rules | `/en/teacher-rules-and-requirements` redirects to legal.skillshare.com | Same chrome as terms. |
| Careers | `/en/careers` redirects to https://apply.workable.com/skillshare/ | Workable. Cookie dialog present. Hidden, never accepted or declined. |
| Login page | `/en/login` | Wall. Screenshot the wall only. Do not type. |
| Search results | `/en/search/classes?query=illustration` | Title illustration. Public results. |

## Phone 390x844

Home header shows logo, hamburger (`svg.ss-icon-hamburger`, title Drawer, role button), Sign In, Sign Up. Sign In and Sign Up are the same walls. Drawer opens the mobile nav. Search combobox is in the collapsed header, not in the first 200px of visible controls.

Playwright `isMobile` with a 390 viewport reported `innerWidth` 466 in one probe. Capture records the measured `innerWidth`. If it is not 390, the context is relaunched without `isMobile` so the CSS viewport is 390.

## Interactions to capture

| Interaction | Where | What it opens |
|---|---|---|
| Browse menu | Home header | Category menu listed above |
| Mobile drawer | Home hamburger | Mobile nav |
| Search focus | Header combobox | Suggestion shell |
| Search query | Header, type a public word, follow the search link | `/en/search?query=watercolor` |
| Filters | Illustration browse, Filters button | Filter panel (Software, Materials also present) |
| Category | Browse Category button | Category list, same destinations as the Browse menu |
| Watch story | About, Watch Mimi's Story | Video overlay, if it stays on skillshare.com |
| Pagination | Browse prev/next | Next page of the same list. One next click, no account. |
| Help language menu | Help Center | Language list. Not switched (would change the captured language). |

## Not present on the public surface

Dark theme toggle. No `data-theme`, no `.dark`, color-scheme normal, zero custom properties on `:root` in the first stylesheet pass. Checkbox, radio, switch, toast, and table were not found on the marketing shell. Login page has an email field and a checkbox. Those are the wall, not filled.

## Not captured, with reason

| Branch | Reason |
|---|---|
| Class detail `/en/classes/<slug>/<id>` | Cloudflare security verification (403, title Just a moment...) in headless Chromium and system Chrome via Playwright. Homepage lists the URLs. Branch stopped. |
| Auth0 login and signup | Known wall. |
| `/en/login` email, password, Google, Facebook, Apple | Known wall. Not typed. Not clicked. |
| Checkout, enroll, gift purchase, affiliate join | Account or payment. |
| Blog newsletter email | Do not type an email. |
| Workable cookie Accept / Decline | Consent POST. Banner hidden. |
| DataGrail banner | Hidden, never answered. |
| External press, social, app stores, Impact, partnerships | Off the product UI. |
