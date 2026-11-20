# OneSoil public site tree

Mapped on 2026-11-21 from https://onesoil.ai/ (redirects to https://onesoil.ai/en) in headless Playwright at 1440x900, then the phone menu at 390x844. Controls were opened and closed. No form was submitted. No password, code, Google, or Apple control was used.

The marketing site is a Next.js app. Header buttons open a full-screen panel (`fixed inset-0 z-50`), not a small dropdown. There is no theme switch on the public pages. `prefers-color-scheme` was light during the map. The stylesheet custom properties sampled on home are Tailwind internals (`--tw-*`) plus `--font-geologica` and `--font-arabic`, not a product token layer.

## Home chrome

| Control | Opens |
|---|---|
| Logo "OneSoil" | https://onesoil.ai/en |
| Products (button, `aria-expanded`) | Full-screen products panel. See Products. |
| Solutions (button) | Full-screen solutions panel. See Solutions. |
| Company (button) | Full-screen company panel. See Company. |
| EN (button, `aria-haspopup`, `aria-controls` language) | Full-screen language list. See Language. |
| Schedule a demo | https://onesoil.ai/en/contact-us?form=schedule_demo |
| Try Free | https://app.onesoil.ai/ which redirects to the sign-in wall. Recorded and stopped. |
| Testimonial dots "Go to testimonial 1" through "Go to testimonial 5" | Same home page, carousel slide. No navigation. |

## Products panel

| Control | Opens |
|---|---|
| OneSoil Platform | https://onesoil.ai/en/platform |
| OneSoil Global Analytics | https://onesoil.ai/en/global-analytics |
| AI Agronomist | https://onesoil.ai/en/ai-agronomist |
| Field Force Assistant | https://onesoil.ai/en/solutions/field-force-assistant |
| For those who grow | https://onesoil.ai/en/solutions/farmers |
| For those who help to grow | https://onesoil.ai/en/solutions/input-suppliers |
| Global Analytics (second link in the panel) | https://onesoil.ai/en/global-analytics |
| Schedule a demo, Try Free | Same as header. Try Free stops at the app sign-in wall. |

## Solutions panel

| Control | Opens |
|---|---|
| Farmers | https://onesoil.ai/en/solutions/farmers |
| Soil Sampling Services | https://onesoil.ai/en/solutions/soil-sampling |
| Agro Consulting | https://onesoil.ai/en/solutions/agro-consulting |
| Machinery Dealers | https://onesoil.ai/en/solutions/machinery-dealers |
| Input Suppliers | https://onesoil.ai/en/solutions/input-suppliers |
| For those who grow | https://onesoil.ai/en/solutions/farmers |
| For those who help to grow | https://onesoil.ai/en/solutions/input-suppliers |
| Global Analytics | https://onesoil.ai/en/global-analytics |

## Company panel

| Control | Opens |
|---|---|
| Blog | https://onesoil.ai/en/resources |
| Help Center | https://help.onesoil.ai/en/ (separate public help site) |
| Contacts | https://onesoil.ai/en/contact-us |
| For those who grow, For those who help to grow, Global Analytics | Same marketing pages as above |

## Language panel

Each row is a locale of the same marketing tree. Captured locale is English only.

| Control | Opens |
|---|---|
| AR العربية | https://onesoil.ai/ar |
| DE Deutsch | https://onesoil.ai/de |
| EN English | https://onesoil.ai/en |
| ES Español | https://onesoil.ai/es |
| FI Suomi | https://onesoil.ai/fi |
| FR Français | https://onesoil.ai/fr |
| LT Lietuvių | https://onesoil.ai/lt |
| PL Polski | https://onesoil.ai/pl |
| PT Português | https://onesoil.ai/pt |
| RU Русский | https://onesoil.ai/ru |
| UK Українська | https://onesoil.ai/uk |

## Phone (390)

| Control | Opens |
|---|---|
| Logo | https://onesoil.ai/en |
| EN | Language list inside the menu (same locales) |
| Open menu | Full-screen menu. Label becomes Close menu. |
| Products, Solutions, Company | Expand in place inside that menu. Same destinations as the desktop panels. |
| Schedule a demo, Try Free | Same as desktop. Try Free stops at the app sign-in wall. |

## Footer (home, also repeated on marketing pages)

| Control | Opens |
|---|---|
| OneSoil | https://onesoil.ai/en |
| Download on the App Store | Apple App Store listing for OneSoil Scouting. External. Not the web app. |
| Get it on Google Play | Google Play listing. External. |
| OneSoil Platform, OneSoil Global Analytics, Farmers, Soil Sampling Services, Agro Consulting, Machinery Dealers, Input Suppliers | The marketing pages above |
| Blog | https://onesoil.ai/en/resources |
| Help Center | https://help.onesoil.ai/en/ |
| Contacts | https://onesoil.ai/en/contact-us |
| Published contact mailto | Mail client. Not followed. The address is not written into this package. |
| Follow Us | https://www.linkedin.com/company/onesoil/ |
| Cookies Policy, Privacy Policy, Terms of Service | Google Docs. External. Not captured as product UI. |

## Page-level interactions

| Page | Control | Opens |
|---|---|---|
| https://onesoil.ai/en/platform | Open Web App | https://app.onesoil.ai/ sign-in wall. Stop. |
| https://onesoil.ai/en/platform | Download | Popover: App Store, Google Play, and Close. Same store listings as the footer. |
| https://onesoil.ai/en/platform | FAQ buttons (for example "Do I need to upload my own data to get started?") | Accordion on the same page. First item expands to public copy about field boundaries and subscription features. |
| https://onesoil.ai/en/platform | API Documentation | https://onesoil.ai/en/contact-us (not a docs app) |
| https://onesoil.ai/en/platform | Help Center | https://help.onesoil.ai/en/ |
| https://onesoil.ai/en/solutions/farmers | Open App | https://app.onesoil.ai sign-in wall. Stop. |
| https://onesoil.ai/en/solutions/farmers, agro-consulting, input-suppliers | FAQ buttons | Accordions on the same page. |
| https://onesoil.ai/en/ai-agronomist | Download | Same store popover pattern as platform. |
| https://onesoil.ai/en/ai-agronomist | Download the app | https://onesoil.ai (home). |
| https://onesoil.ai/en/resources | Category cards | `/en/resources/category/data-research`, `company-news`, `farmer-stories`, `learn` |
| https://onesoil.ai/en/resources | Article cards | Individual `/en/resources/<slug>` posts. One representative post is captured (`what-is-ndvi`). The other posts are the same article template. |
| https://onesoil.ai/en/resources/what-is-ndvi | Open the app | https://app.yield.onesoil.ai/ sign-in wall. Stop. |
| https://onesoil.ai/en/contact-us | Contact form (name, job title, company, phone, email, country, message, consent, Submit) | Not filled. Not submitted. Empty state only. |
| https://onesoil.ai/en/contact-us?form=schedule_demo | Same form, plus role chips (Founder / Owner, Agronomist, Precision Ag Specialist, Sales / Marketing, Other) | Not filled. Not submitted. Role chips are a choice control, captured by opening the page, not by sending the form. |

## Stopped branches

| URL | What happened |
|---|---|
| https://onesoil.ai/login and https://onesoil.ai/en/login | 404, "This page could not be found." |
| https://app.onesoil.ai/login | 200, then redirects to `https://app.onesoil.ai/auth/login?next=%2Flogin&internal=true`. Visible controls: Sign in, Sign up, e-mail, password, Forgot your password?, Google, Sign in with Apple, language. Stopped. No field was typed. |
| https://app.onesoil.ai/ | Navigation interrupted into a browser error page in headless Chromium (the login redirect). Treated as the same sign-in wall. |
| https://b2b.onesoil.ai/ | 200 redirect to https://onesoil.ai/en/global-analytics |
| https://yield.onesoil.ai/ | 200 redirect to https://onesoil.ai/en/platform |
| https://updates.onesoil.ai/ | TLS failure (`ERR_SSL_VERSION_OR_CIPHER_MISMATCH`). Not captured. |
| https://help.onesoil.ai/en/ | 200, public help home ("Tips and tricks from the OneSoil Team"). Separate product surface. Captured as the landing page only, not its whole article tree. |

Sitemap also lists about 40 more `/en/resources/<slug>` posts and the same routes in 10 other locales. Those are the same templates. They are not separate components.
