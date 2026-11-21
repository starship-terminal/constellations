# Soundtrap public site tree

Mapped from the live site on 2026-11-21, signed out, in headless Chromium, before any package screenshots. Official site: [https://www.soundtrap.com/](https://www.soundtrap.com/). A request for `/` redirects to `/musicmakers`. Soundtrap (by Spotify) is a browser DAW. The studio, account, and checkout sit behind login. This file records which control opens which page, menu, dialog, or interaction. It is the shot plan, not a token source.

Consent: OneTrust mounts a preference center (`#onetrust-consent-sdk`) on these pages. It is hidden in CSS for captures and never answered. Allow All, Reject All, and Confirm My Choices are not clicked.

Auth stop: if a control lands on a login or signup wall, the URL is recorded and that branch stops. No email, password, birthday, invite code, plan, survey, or newsletter field is filled. No form is submitted. Google, Apple, Facebook, and Microsoft controls are not clicked.

## Shell

| Control | Opens |
|---|---|
| Logo (header) | [https://www.soundtrap.com/musicmakers](https://www.soundtrap.com/musicmakers) |
| Music Makers | `/musicmakers` (home) |
| Features | [https://www.soundtrap.com/content/features](https://www.soundtrap.com/content/features) |
| Education | [https://www.soundtrap.com/edu/](https://www.soundtrap.com/edu/) |
| Blog | [https://blog.soundtrap.com/](https://blog.soundtrap.com/) |
| Pricing | `/pricing` on the music-makers shell; `/pricing-education` when the Education header is showing |
| Log in | [https://www.soundtrap.com/login](https://www.soundtrap.com/login) on the music-makers shell; [https://www.soundtrap.com/edu/login](https://www.soundtrap.com/edu/login) on Education. Wall. Stop. |
| Get started (header link) | [https://www.soundtrap.com/signup](https://www.soundtrap.com/signup). Wall. Stop. |
| Get started for free (home hero button, `aria-haspopup="dialog"`) | Radix dialog: Personal Use → `/signup` (wall, stop); Educational Use → `/edu/` |
| Open navigation menu (phone only, 390) | Same header links in an overlay: Music Makers, Features, Education, Blog, Pricing, Log in, Get started. Escape or the control closes it. |
| Footer language `<details>` summary "English" | Menu of locale home pages: English `/musicmakers`, Deutsch `/de/musicmakers`, Español `/es/musicmakers`, Français `/fr/musicmakers`, Bahasa Indonesia `/id/musicmakers`, Italiano `/it/musicmakers`, Nederlands `/nl-NL/musicmakers`, Norsk `/no/musicmakers`, Polski `/pl/musicmakers`, Português (Brasil) `/pt-BR/musicmakers`, Svenska `/sv/musicmakers`, Türkçe `/tr/musicmakers`. Same path prefix on other marketing pages. English is the capture locale. |
| Skip to main content | In-page `#main` |

Desktop header links are visible at 1440. The hamburger is the phone path to the same links.

## Home `/musicmakers`

| Control | Opens |
|---|---|
| Record vocals online | `/content/product/record-voice-online` |
| sampler | `/content/product/sampler` |
| online MIDI editor | `/content/product/online-midi-editor` |
| loops and sample packs | `/content/product/audio-loops-sample-packs` |
| free drum kits and loops | `/content/product/free-drum-kits-and-loops` |
| Get started (mid-page) | `/signup`. Wall. Stop. |
| Previous slide / Next slide | Local carousel of Soundtrap Originals. No navigation. |
| Play {pack}, Soundtrap Originals | Local audio preview. Label flips to Pause {pack}. Not a form. |
| Open in studio | `/studio/fork/{id}/` redirects to `/login?url=...`. Wall. Stop. One probe is enough for the family. |
| Explore sounds | `/originals` |
| mixing and mastering tools | `/content/product/online-daw-features` |
| Vocal tuning / pitch correction software | `/content/product/auto-tune-by-antares` |
| online piano roll | `/content/product/online-piano-roll` |
| Patterns beatmaker / beats | `/content/product/patterns-beatmaker` |
| song templates | `/content/product/song-templates` |
| Read more (four tutorials) | Redirects to `blog.soundtrap.com`: `/create-a-song-with-soundtrap/`, `/make-a-beat/`, `/mixing-a-song-online/`, `/how-to-remix-a-song/` |
| Play video / Pause video | Local hero video. Not a form. |

## Features `/content/features`

Same marketing shell. In-page controls:

| Control | Opens |
|---|---|
| Get started / Sign up now | `/signup`. Wall. Stop. |
| Learn more (vocals) | `/content/product/vocal-suite` |
| Explore packs | `/originals` |
| Open in Studio / Try now (studio fork) | `/studio/fork/...` then login. Wall. Stop. |
| Explore instruments | `/content/instruments` |
| Try now (some cards) | `/signup`. Wall. Stop. |
| Download now | `st-app-downloads.storage.googleapis.com` macOS `.dmg`. External file. Not followed as a page. |
| Play {preset or pack} | Local audio preview. |

## Education `/edu/`

Different header: Pricing goes to education pricing, Log in goes to the school login.

| Control | Opens |
|---|---|
| Get started (admin) | `/edu/get-started?role=admin&source=edu-landing`. Account chooser ("Create a new Educational account" / join with invite or LMS). Branch stops before any field is filled. |
| Get started (teacher) | `/edu/get-started?role=teacher&source=edu-landing`. Same chooser. Stop before fields. |
| Join your school | `/invite?role=student&source=edu-landing`. Invite-code form. Stop. Do not type a code. |
| Learn more (video scoring) | `districts.soundtrap.com` feature page. External marketing host. |
| View Lesson Plan | PDF under `/public/lessonplans/` (Literacy, Music, WorldLanguage, Science, TechAndBusiness, Math). Files, not UI states. |
| Trust Center | `/legal/trust-center` |
| Language `<select name="languagepicker">` | Locale of the education page. Not changed (would navigate). Recorded, not submitted. |

Education footer adds Press (`press.soundtrap.com`), EDU blog (`edu.soundtrap.com`), Community (Facebook group, external), Jobs (LinkedIn, external), `/legal/privacy_edu`, `/legal/terms`, `/legal/trust-center`.

## Pricing

| Control | Opens |
|---|---|
| Individual | `/pricing` (from education pricing: `/pricing?source=edu_pricing_switch`) |
| Education | `/pricing-education` |
| Monthly / Yearly | Local billing toggle (`button.toggle-button`, `aria-pressed`). Yearly is the loaded state. Monthly is a local UI state, not a form submit. |
| Try it free! / Sign up! | `/signup` or a trial start that requires an account. Wall. Stop. |
| Promotional Offer Terms | `/legal/terms/promotional-offer` |
| Language select | Locale switch. Not changed. |

Education pricing extra controls:

| Control | Opens |
|---|---|
| Try free for 30 days / Try it now / Buy now | Account or checkout wall. Stop. |
| Contact sales / Request it here | `soundtrap.me/price_quote`. External quote form. Stop. Do not fill it. |
| More info: {feature} | Tooltip, for example Time restore: "Keep track of what collaborators have changed or restore previous project versions." |
| Bank wire article | Support article on purchase by bank wire. Public help page. |

## Originals

| Control | Opens |
|---|---|
| `/originals` | Pack marketing page. Play buttons and carousels are local. Open in studio is a login wall. |
| Explore Originals / Find sounds | `/originals/explore` ("Sounds for days"). Public catalog of play buttons and carousels. No search field on the public page (the only text input seen was the hidden OneTrust cookie search). |

## Storytellers `/storytellers`

Podcast marketing page. Get started goes to `/pricing`. Same shell otherwise.

## About, developers, legal

| Control | Opens |
|---|---|
| About | `/about`. Links onward to `/signup` (wall), `/musicmakers`, `schools.soundtrap.com/edu`, `edu.soundtrap.com/blog/`, `/content` (redirects to the blog), `/thirdpartysoftware`, support request (`soundtrap.zendesk.com/hc/en-us/requests/new`, a request form, stop). |
| Developers | `/developers`. Code samples in textareas (read, not edited). "Edit on Soundtrap" hits `/publicapi/import/...` and is treated as a studio/login wall. Stop. `supported_browsers` 404s ("Oops, page not found"). CORS links leave the site (`enable-cors.org`). |
| Legal cluster from the cookies page | Privacy world and edu, terms creator world/us, terms edu world/us, promotional offer, community guidelines, cookies, trust center, subprocessors, DPA. |

## Blog, support, careers

| Control | Opens |
|---|---|
| Blog home | `blog.soundtrap.com`. Categories: News, Songwriting & Music Theory, Music Production, Vocal Production, Mixing & Mastering, Sample Packs & Genres, plus Instruments on some cards. |
| search blog | Reveals a search field ("Search for:"). Not typed. Not submitted. |
| A post | Public article. Four home "Read more" posts are the sample. The archive is unbounded, so further posts are the same template, not new components. |
| Support home | `support.soundtrap.com/hc/en-us` (Zendesk). Search field posts to `/hc/en-us/search`. Not submitted. |
| Category cards | Account & Payment, The Studio, General, Troubleshooting, Soundtrap for Education. |
| Submit a request | Zendesk request form. Stop. |
| Sign in | `soundtrap.zendesk.com/access?...`. Wall. Stop. |
| Careers home | `careers.soundtrap.com` (Teamtailor). CAREER MENU, Share page (menu: Facebook, X, LinkedIn; external, not clicked), location `<select>` (not changed), Jobs, Connect, Data & privacy. |
| Employee login | `app.teamtailor.com/...`. Wall. Stop. |
| Candidate Connect login | `/connect/login`. Wall. Stop. |

## Walls (recorded, branch stopped)

| URL | What is on screen | What was not done |
|---|---|---|
| `/login` | Email, password, Log in, Forgot your password? (`/forgotpassword`), Sign up, Log in with Google, Apple, Facebook, Microsoft School Account | No email typed. Password not submitted. Social buttons not clicked. |
| `/signup` | Email, confirm email, password, birth month/day/year, Sign up, Sign up with Google, Sign up with Facebook, Log in | No fields filled. No social click. |
| `/edu/login` | School email, password, Google School Account, Microsoft School Account, "Select your school login system", "Log in with email and password" | No fields filled. No social click. |
| `/edu/get-started?role=teacher` and `role=admin` | "Join Soundtrap for Education" role chooser, then account creation | Stopped before any field. |
| `/invite?role=student` | Invite code field and Join | Code not typed. Form not submitted. |
| `/studio/fork/{id}/` | Redirects to `/login?url=...` | Stop. |
| `/forgotpassword` | Linked from login. Password-reset wall. Not opened past the login record. | No email typed. |
| Zendesk sign-in and request forms | Account or ticket forms | Stop. |
| `soundtrap.me/price_quote` | Sales quote form | Stop. |

## External (not captured as pages)

Discord, Instagram, TikTok, YouTube, X, Facebook, LinkedIn, cookiepedia.co.uk, onetrust.com, enable-cors.org, the macOS `.dmg`, Facebook EDU community, LinkedIn jobs. Social login hosts are never opened.

## Themes and widths

One public theme. `html` has no `data-theme` and no dark class. `color-scheme` reads `normal`. No public theme switch was found. Captures are light only, at desktop 1440×900 and phone 390×844.

Signed-in studio, projects, collaboration, checkout, and account settings are not reachable without an account. They are gaps, not inferred screens.
