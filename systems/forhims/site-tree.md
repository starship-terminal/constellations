# Hims UK public site tree

Mapped from [https://www.forhims.co.uk/](https://www.forhims.co.uk/) on 2026-11-21 in headless Chromium before screenshots. The marketing site is `www.forhims.co.uk`. The signed-in app and the intake quiz live on `app.forhims.co.uk`. One light theme (`color-scheme: normal`, `html.brand-hims`). No theme switch on the public surface.

Cookie banner: Ketch dialog "About cookies on our site" (Accept all, Customise). Hidden by aborting the Ketch CDN. No consent button was clicked.

Private strings are not written here. The footer press address and the complaints support address are published contacts; they are omitted from this file on purpose.

## Global chrome (desktop 1440)

Sticky bar, class family `global-navigationstyles__*`.

| Control | Opens |
|---|---|
| Logo ("Link to homepage") | `/` |
| Weight | `/weight-loss` |
| Hair | `/hair-loss` |
| Sex (button, floating menu) | Menu: Erectile Dysfunction → `/erectile-dysfunction`; Premature Ejaculation → `/premature-ejaculation`. Closes on Escape. |
| Learn (button, floating menu) | Menu: Blog → `/blog`; Condition Guides → `/conditions`. Closes on Escape. |
| Treatments | `/customer/treatments` → redirects to `/customer/login?onauth-next=/customer/treatments`. Login wall. Stop. |
| Messaging | `/customer/support` → login wall. Stop. |
| Profile | `/customer/profile` → login wall. Stop. |
| LOGIN (button) | `https://app.forhims.co.uk/login` (Email, Password, Keep me logged in, Log in, Forgot your password, Sign up). Stop. Do not type. |
| Banner "Click here for details" | `/migration-privacy` |
| Carousel Previous slide / Next slide | Moves the on-page slide. Local. |
| Footer Treatments / Explore / Learn / Connect headings | Expanding sections, already open on desktop. |

Footer destinations (same on every marketing page):

| Label | Opens |
|---|---|
| Weight Management | `/weight-loss` |
| Hair Loss | `/hair-loss` |
| Erectile Dysfunction | `/erectile-dysfunction` |
| Premature Ejaculation | `/premature-ejaculation` |
| GLP-1 Injections | `/weight-loss` |
| Sildenafil | `/erectile-dysfunction/sildenafil` |
| Generic Cialis | `/erectile-dysfunction/tadalafil` |
| Viagra Connect | `/erectile-dysfunction/viagra-connect` |
| Hair Loss Spray | `/hair-loss` |
| Finasteride Pills | `/hair-loss/finasteride` |
| Minoxidil Serum | `/hair-loss/minoxidil` |
| Dapoxetine For PE | `/premature-ejaculation/dapoxetine` |
| Premature Ejaculation Pills | `/premature-ejaculation` |
| About Us | `/about` |
| How It Works | `/how-it-works` |
| Good Health | `/blog` |
| Condition Guides | `/conditions` |
| Purpose | `/purpose` |
| Reviews | `/hims-reviews` |
| Investors | `https://investors.hims.com/` (external) |
| Careers | `https://www.hims.com/careers-professionals` (external) |
| Help Centre | `https://ukhims.zendesk.com/hc/en-gb` (external) |
| Contact Us | Zendesk article (external) |
| Press (media only) | mailto, not followed |
| Terms & Conditions | `/terms-and-conditions` |
| Privacy Policy | `/privacy-policy` |
| Pharmacy Terms | `/pharmacy-terms` |
| Sitemap | `/sitemap.html` (1132 unique paths; mostly blog posts and condition guides) |
| Complaints | `/complaints` |
| LegitScript, CQC | external registers |

## Phone (390)

Same destinations. At 390 the Weight, Hair, Sex and Learn labels still paint under the wordmark. The hamburger opens the account drawer (Get started, Log in, Forgot password, then Weight, Hair, ED, Early Climax). Footer sections start collapsed (`aria-expanded=false` on the expanding headings).

## Home `/`

| Control | Opens |
|---|---|
| Explore treatments (button) | Stays on `/`. No dialog. The button's own link target is `/`. |
| Lose weight | `/c/wl` → `app.forhims.co.uk/flow/...?t=weight_loss`. Assessment wall. Stop. |
| Have great sex | `/c/e` → app flow `t=erectile`. Stop. |
| Regrow hair | `/c/hl` → app flow `t=hair`. Stop. |
| Have longer sex | `/c/p` → app flow `t=premature`. Stop. |
| Get started | `/c` (public chooser, see below) |
| Category tiles (image links) | `/weight-loss`, `/erectile-dysfunction`, `/hair-loss`, `/premature-ejaculation` |

## Category landings

| Page | Public controls beyond chrome |
|---|---|
| `/weight-loss` | Get started, Am I eligible? → `/c/wl` (assessment wall, stop). Learn more → `/weight-loss/wegovy`, `/weight-loss/mounjaro`. FAQ accordion (local expand). |
| `/hair-loss` | Take the free hair quiz, Get started → `/c/hl` (stop). Learn more → `/hair-loss/minoxidil`, `/hair-loss/finasteride-and-minoxidil`, `/hair-loss/finasteride`. Review Rating and Sort selects (local, not submitted). FAQ accordion. |
| `/erectile-dysfunction` | Get started → `/c/e` (stop). Learn more → `/erectile-dysfunction/sildenafil`, `/tadalafil`, `/viagra-connect`, `/cialis-together`, `/tadalafil-daily`. Review pager and Rating/Sort selects. FAQ accordion. |
| `/premature-ejaculation` | Get started → `/c/p` (stop). One Get started → `/consultation/pej` (consultation branch, stop if it asks for profile or plan fields). Learn more → `/premature-ejaculation/dapoxetine`, `/sildenafil-for-pe`, `/tadalafil-daily-for-pe`. FAQ accordion. |

## Product pages (public PDP pattern)

Example: `/erectile-dysfunction/sildenafil`. "Meet The Generic ED Pill" opens a drawer; "Close the drawer" closes it. Safety link → `/safety-information/sildenafil`. Primary CTA → `/c/e` (assessment wall, stop). Same pattern on the other product URLs listed above.

## Chooser and walls

| URL | What it is |
|---|---|
| `/c` | Public chooser: "What are you looking to do?" Grow thicker, fuller hair → `/c/hl`; Perform your best in bed → `/c/edpej-treatment-guidance`; Reach your healthy weight goal → `/c/wl`. |
| `/c/wl`, `/c/hl`, `/c/e`, `/c/p` | Redirect to `app.forhims.co.uk/flow/...`. Assessment. Stop. Do not answer. |
| `/customer/login` | Email and password. Known probe. Stop. |
| `https://app.forhims.co.uk/login` | Email and password. Stop. |
| `/customer/treatments`, `/customer/support`, `/customer/profile` | Redirect to the login page. Stop. |

## Content

| Page | Notes |
|---|---|
| `/about`, `/how-it-works`, `/purpose` | Editorial. CTAs go to `/c` or `/c/wl` (chooser or assessment wall). |
| `/blog` | Category chips: All `/blog`, Weight Loss, Hair, Sex, Skin, Lifestyle. Article cards. Next page `/blog/page/2`. Hundreds of posts in the sitemap; one index, one category, one article are enough to show the pattern. |
| `/conditions` | Guide cards. Next page `/conditions?page=2`. One index and one guide. |
| `/hims-reviews` | "See the reviews", review pager, Rating and Sort selects. Find my treatment → `/`. Get started → `/c/hl` (stop). |
| `/migration-privacy` | Links to `/privacy-policy` and `/legacy-privacy-policy`. |
| `/privacy-policy`, `/terms-and-conditions`, `/pharmacy-terms`, `/complaints` | Long legal text. Complaints page shows a published support address; do not copy it into the package. |
| `/sitemap.html` | Index of the public tree. |
| `/sex-report/` | Separate template. "Download the whitepaper" → `/sex-report/documents/HimsHers_UK_2023.pdf`. Not a UI state. |
| `/skin`, `/safety-information` | Styled 404 ("Hey now - page not found!"). Product safety lives at `/safety-information/<slug>`. |

## Not captured on purpose

- Login, signup, forgot password, Google, Apple.
- Assessment flows on `app.forhims.co.uk/flow/`.
- Profile, birthday, plan, survey, onboarding, newsletter fields. None of the public marketing pages exposed a newsletter field.
- The rest of the sitemap's blog posts, condition guides, and medical-expert bios (same templates).
- External investors, careers, Zendesk, LegitScript, CQC.
