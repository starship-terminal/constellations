# Navia site tree

Mapped on 2026-11-21 from https://www.thenavia.com/ in headless Chromium, before screenshots. The marketing site is a public Webflow site. The product app is a sign-in wall. No form was submitted. No password, code, or profile field was filled.

## Hosts

| Host | What it is | Reached |
|---|---|---|
| https://www.thenavia.com/ | Public marketing site, blog, legal, contact | Yes, HTTP 200 |
| https://app.thenavia.com/ | Product app | Yes. Paints "Welcome to Navia. Please sign in to access your account" with Sign In and Sign Up. Stopped. |
| https://accounts.thenavia.com/sign-in | Clerk-style sign-in | Sign In on the app navigates here. Cloudflare "Just a moment" security check. Stopped. Known wall: email or username and password, or Facebook, Google, or passkey. |
| https://www.app.thenavia.com/ | Footer "Get started for free!" link | DNS does not resolve (`ERR_NAME_NOT_RESOLVED`). Dead branch. |
| https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ1BE6qAd367fV-wLx4PSb8tzag8z6FL3dYcbcDIRkgJGumcwi1CyhSl4XGJTGAW6dPU7rjxpePz | "Book a demo" and "Schedule a meeting" | External booking page. Not captured. |
| https://www.google.com/search?q=Navia | "5 stars on google" | External. Not captured. Google was not clicked. |
| https://www.instagram.com/getoutoftheoffice/ | "Join the out of office club" | External. Not captured. |
| https://www.greaterthanstudio.com/ | Footer "Site by" | External studio credit. Not captured. |
| https://www.cookieyes.com/ | Cookie banner "Visit CookieYes website" | External. Not captured. |
| https://flodesk.com/c/THENAVIAWAY | Affiliate link inside a blog post | External. Not followed. |

## Theme

One light theme. `prefers-color-scheme: dark` still paints the cream page `rgb(250, 244, 230)` and ink `rgb(54, 49, 42)`. No theme switch exists. Phone captures are the same theme at 390 x 844.

## Home (https://www.thenavia.com/)

Nav, desktop, always visible:

| Control | Opens |
|---|---|
| Logo ("return to home") | https://www.thenavia.com/ |
| Platform | Same page, `#platform` |
| Pricing | Same page, `#pricing` |
| Resources | https://www.thenavia.com/blog (a link, not a dropdown) |
| Get started | https://app.thenavia.com/ (sign-in wall) |

Nav, phone: a `menu` button (`aria-expanded`, controls `w-nav-overlay-0`) opens an overlay with Platform, Pricing, Resources, and Get started for free. Get started for free goes to the same sign-in wall.

Hero and body links, all on the home page:

| Control | Opens |
|---|---|
| Get started for free | https://app.thenavia.com/ (wall) |
| Book a demo | Google Calendar appointment page (external) |
| 5 stars on google | Google search (external; not clicked) |
| Feature items (four, role=button): "Your marketing to-do list, planned for you", "Effortlessly create content that stays on brand", "A writer that speaks in your voice", "Track your progress and keep momentum" | In-page selected state. Clicking one adds `is-active` to that item and removes it from the others. No new page. |
| Sign up (three plan cards) | https://app.thenavia.com/ (wall) |
| View plans | Same page, `#pricing` |
| Schedule a meeting (two) | Same Google Calendar appointment page |
| Join the out of office club | Instagram (external) |
| Get started for free! | https://www.app.thenavia.com/ (does not resolve) |
| View all resources | `https://www.thenavia.com/#` (same page, empty hash) |
| Four article cards | The four blog posts listed under Blog below |
| Contact us | https://www.thenavia.com/contact-us |
| Privacy Policy | https://www.thenavia.com/privacy-policy |
| Terms and conditions | https://www.thenavia.com/terms-and-conditions |
| Site by | https://www.greaterthanstudio.com/ |

Pricing is three static cards (Basic free, Business $49/mo, Growth $79/mo). No billing toggle.

## Overlays on every marketing page

CookieYes banner, on first paint: Customise, Reject All, Accept All.

| Control | Opens |
|---|---|
| Customise | Preference center (`#ckyPreferenceCenter`): category rows Necessary, Functional, Analytics, Performance, Advertisement, Uncategorised, each with Show more, plus Reject All, Save My Preferences, Accept All, Close |
| Reject All | Closes the banner. No account. |
| Accept All | Closes the banner and consents. Not used for the capture. |
| Consent Preferences (reopen) | Same preference center, after the banner is gone |

Flodesk popup (`data-ff-type="popup"`, name `popupImage`), auto-mounted: an image, a Close button, and an email field labelled as a newsletter signup ("Join the Community" submit). The form posts to `form.flodesk.com`. Not filled. Not submitted. Close dismisses it. The field is a newsletter field, so it stays empty.

## Blog

Index: https://www.thenavia.com/blog. Title "Learn how to grow your business". "All articles" is a heading, not a filter. No category control.

| Control | Opens |
|---|---|
| Article card | That post |
| Next | `?55a1b861_page=2`, then 3, then 4. Page 4 has no Next. |
| Same nav and footer as home | Same destinations |

Pagination, measured before screenshots: page 1 has 13 article links, page 2 has 13, page 3 has 13, page 4 has 8. 44 unique article paths. The sitemap lists 45 `/blog/...` posts plus the index, so one sitemap URL is not on the index.

A post (example: `/blog/how-do-i-know-if-my-marketing-is-working`) is an article with in-body links to other posts, a "Get started with Navia for free" link to the app wall, related-post cards, and the same footer. No share menu.

## Contact (https://www.thenavia.com/contact-us)

A Webflow form: First name, Last name, Email, Phone number, a select ("What are you messaging about?": Select one, General help, Invoicing/payments, Other), Message, and a submit button. Not filled. Not submitted. The select can be opened to show its options; no value is chosen for a submission. A Webflow embed says "Please accept cookies to access this content" until cookies are accepted. That embed is left blocked.

## Legal

| Page | Notes |
|---|---|
| https://www.thenavia.com/privacy-policy | Static page. Same nav, cookie banner, footer. |
| https://www.thenavia.com/terms-and-conditions | Static page. Same chrome. |
| https://www.thenavia.com/do-not-sell-or-share-my-personal-information | Static explainer. Cookie banner and the same Flodesk popup mount. No account form was filled. |

These pages link out to CookieYes, Google opt-out, and the EDPB. Those external pages were not captured.

## Sitemap

https://www.thenavia.com/sitemap.xml lists 51 URLs (home, blog index, three legal pages, contact, 45 blog posts). `robots.txt` points at that sitemap only.

## Stopped branches

- Sign In and Sign Up on https://app.thenavia.com/ go to https://accounts.thenavia.com/sign-in. Recorded. Not passed.
- Newsletter popup and the contact form. Recorded as present. Not filled.
- Google, Instagram, Calendar, CookieYes, Greater Than Studio, Flodesk. External. Not used as product UI.
- `www.app.thenavia.com` does not resolve.
