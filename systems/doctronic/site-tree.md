# Doctronic public site tree

Captured 2026-11-21 from https://www.doctronic.ai/ in headless Chromium, signed out. Product version on the marketing sidebar: v1.40.575.

This is the public tree. A control that opens a login or signup wall is recorded and that branch stops. No email, code, password, or SSO button was used. Get Login Code and Get Sign up Code were not clicked.

Sitemap indexes (URL counts only, not a walk of every article):

| Index | URLs |
|---|---|
| sitemap-main.xml | 393 |
| sitemap-landing-pages.xml | 423 |
| sitemap-blog.xml | 11941 |
| sitemap-online-treatment.xml | 1742 |
| sitemap-conditions.xml | 1415 |
| sitemap-drugs.xml | 1361 |
| sitemap-compare.xml | 1206 |
| sitemap-questions.xml | 1270 |
| sitemap-apcm-form.xml | 129 |
| sitemap-authors.xml | 22 |
| sitemap-partners.xml | 5 |
| sitemap-pharmacy-support.xml | 1 |
| sitemap-questionnaires.xml | 1 |

Representative pages were opened. The long catalogs (blog posts, drugs, conditions, compare, questions, APCM forms, city and drug landing pages) share the marketing shell. They are the same page type repeated, not a second product.

## Home `/`

| Control | Opens |
|---|---|
| Skip to content | In-page `#content` |
| Logo | Page `/` |
| Log in (`data-test-id=log-in-button`) | Dialog at `/?modal=signin`. Stop. |
| Sign up (`data-test-id=sign-up-button`) | Dialog at `/?modal=signup`. Stop. |
| Open sidebar | Menu, marketing sidebar. See below. |
| Pause animations | Same page. Label becomes Resume animations. |
| Doctronic (headline trigger) | Tooltip trigger. A second copy is in the DOM at 0×0. No tooltip text was read. |
| Hero textarea | Field. Not submitted. Start chat is the submit control. |
| Anonymous | Dialog at `/?modal=anonymous-info`. Copy: anonymous chats are not linked to an account. Got it closes it. |
| Start chat (button and links) | Page `/chat/` |
| Trustpilot | External https://www.trustpilot.com/review/www.doctronic.ai |
| Previous / Next testimonial | Same page, carousel |
| Watch [name] testimonial | Same page, video iframe. Not a login wall. |
| All treatments | Page `/online-treatment/` |
| Cold & flu, Anxiety, Depression, UTI, Erectile dysfunction, Tooth infection, High blood pressure, Muscle spasms | Pages under `/online-treatment/<slug>/` |
| Our blog | Page `/blog/` |
| Learn about GLP-1s | Page `/prescription-glp-1/` |
| Get an OBGYN chat | Page `/obgyn/` |
| Check your symptoms | Page `/symptom-checker/` |
| What is AI Primary Care? | Page `/ai-primary-care/` |
| Instagram, X, LinkedIn, Facebook, YouTube, TikTok | External profile links |
| Footer AI Doctor Chat, All Conditions | Page `/` |
| Symptom Checker, Urology, Telehealth, Type 2 Diabetes, Heart Conditions, STIs, Respiratory | Pages `/symptom-checker/`, `/urology/`, `/telehealth/`, `/type-2-diabetes/`, `/cardiology/`, `/sexually-transmitted-disease/`, `/pulmonology/` |
| About Doctronic | Page `/our-philosophy/` |
| Careers | Page `/careers/` |
| Our Medical Reviewers | Page `/authors/` |
| Team | Page `/about/` |
| Blog | Page `/blog/` |
| FAQs | Page `/resource-center/` |
| Privacy Policy | Page `/privacy-policy/` |
| Terms of Service | Page `/terms-of-service/` |
| Do not sell or share my personal information | Page `/do-not-sell/` (a form; not submitted) |
| App Store, Google Play | External store listings |
| Verify LegitScript Approval | External https://www.legitscript.com/websites/?checker_keywords=doctronic.ai |
| Footer Log in | Same login dialog. Stop. |

## Marketing sidebar

Opened from Open sidebar. Close control: Close marketing sidebar.

| Control | Opens |
|---|---|
| Logo | Page `/` |
| New chat | Page `/chat/` |
| About Chat | Menu. Items below. |
| How it works | Page `/how-your-ai-doctor-works/` |
| Diagnosing symptoms | Page `/diagnose-me/` |
| EHR, Refill Prescriptions, Primary Care, Prescription Refill, No Insurance, Mental Health, Dermatology, Men's Health, Women's Health, Weight Loss, ED, Thyroid, Urology, Endocrinology | Service links inside About Chat. Destinations were not opened one by one after the menu was recorded. |
| Health Record | Page `/ehr/` (public MedMemory marketing page, not the signed-in record) |
| Health Information | Menu. Items below. |
| About us | Page `/our-philosophy/` |
| Careers | Page `/careers/` |
| For Partners | Page `/partners/` |
| Sign up for free | Signup dialog. Stop. |
| Log in | Login dialog. Stop. |
| HIPAA, Private & Secure | Labels, not links |

Health Information menu:

| Control | Opens |
|---|---|
| Online Treatment | Page `/online-treatment/` |
| Drug Information | Page `/drugs/` |
| Condition Information | Page `/conditions/` |
| Lexapro Refills, Sibo, Corneal Abrasion, Anal Fissures, Clonidine Refill | Pages under `/online-treatment/` |
| Top Blogs | Page `/blog/` |
| Six article titles | Pages under `/blog/` |

## Login dialog `/?modal=signin`

| Control | Opens |
|---|---|
| Close modal | Closes the dialog |
| Back to log in options | Returns to `/?modal=signin` from the email step |
| Log in with email | Same dialog, `/?modal=signin&step=email`. Asks for an email. Get Login Code was not clicked. |
| Continue with Google | Not clicked. Stop. |
| Continue with Apple | Not clicked. Stop. |
| Continue with Facebook | Not clicked. Stop. |
| Create an account | Signup dialog `/?modal=signup` |
| Terms of Service, Privacy Policy (on the email step) | Pages `/terms-of-service/`, `/privacy-policy/` |

Email step fields: one email input, placeholder "Email address...". No password field. Button label: Get Login Code. Not clicked.

## Signup dialog `/?modal=signup`

| Control | Opens |
|---|---|
| Close modal | Closes the dialog |
| Sign up with email | Same dialog, `/?modal=signup&step=email`. Asks for an email. Get Sign up Code was not clicked. |
| Sign up with Google, Apple, Facebook | Not clicked. Stop. |
| Log in here | Login dialog |
| Terms of Service, Privacy Policy | Those pages |

## Chat `/chat/`

Public empty composer. Signed-in nav items redirect to the login wall.

| Control | Opens |
|---|---|
| Expand sidebar | Menu of the product rail |
| New chat | Page `/chat/` |
| Health record | ` /health-record/ ` redirects to `/chat/?modal=signin&returnUrl=%2Fhealth-record%2F`. Stop. |
| Appointments | `/appointments/` redirects to the same login wall. Stop. |
| Prescriptions | Page `/prescription-refill/portal/` (public portal shell) |
| Sign up for free | Signup dialog. Stop. |
| Log in | Login dialog. Stop. |
| Support mail link | `mailto:` link on the chat rail. Not opened. The address is not copied here. |
| Terms of Service, Privacy Policy | Those pages |
| Anonymous | Anonymous-info dialog |
| Composer textarea | Field. Not submitted. |
| Send message | Would submit the composer. Not clicked. |
| Check my symptoms | Starts an anonymous chat path on `/chat/` with a query token. The token value was not read into the package. The composer placeholder changed to "Reply to Doctronic...". No message was sent. |
| Get treatment advice, Get or refill a prescription, Understand my lab results | Same class of chip. Not followed after the first chip showed a handoff URL. |

## Other public pages opened

| Path | What it is |
|---|---|
| `/our-philosophy/` | About / philosophy |
| `/about/` | Team |
| `/careers/` | Careers |
| `/partners/` | Health systems and plans. Child pages in the partners sitemap: health-system-savings, reducing-emergency-department-visits, clinical-safety-benchmark, evidence |
| `/online-treatment/` | Treatment index |
| `/symptom-checker/` | Symptom checker marketing |
| `/blog/` | Blog index |
| `/resource-center/` | FAQs |
| `/authors/` | Medical reviewers |
| `/ai-primary-care/` | Primary care marketing |
| `/contact-us/` | Contact |
| `/press-media/` | Press |
| `/how-your-ai-doctor-works/` | How it works |
| `/privacy-policy/`, `/terms-of-service/` | Legal |
| `/do-not-sell/` | Opt-out form. Not submitted. |
| `/prescription-refill/portal/` | Public refill portal shell |
| `/ehr/` | MedMemory marketing |
| `/for-partners/` | 404, "We can't find that page." The real partners URL is `/partners/` |
| `/questionnaires/` | 404. The questionnaires sitemap has one URL that was not opened |
| `/pharmacy-support/` | Returned the home document in this client (status 200, home controls). Not treated as a distinct page |

No cookie consent wall appeared, so none was hidden or accepted.
