# BYBORRE public site tree

Mapped 2026-11-21 from [https://byborre.com/](https://byborre.com/) in headless Chromium (Playwright), signed out, desktop 1440 and phone 390. Every row is a control that was visible, and the page or overlay it opened. Cookie Reject and Accept were not clicked. No form was submitted. Login and sign-up branches stop at the wall.

The marketing site is a Nuxt app on `byborre.com`. Design Studio lives at `/dashboard` and is behind the login dialog. `create.byborre.com` is named in the FAQ as the design editor and was not opened.

## Shell, every public page

| Control | Where | Opens |
|---|---|---|
| Marquee "ORDER FREE SAMPLES — WORLDWIDE SHIPPING" | top bar, link | [/collection](https://byborre.com/collection) |
| Wordmark BYBORRE | header, link | [/](https://byborre.com/) |
| Textile Room, yellow New badge | header, link | [/collection](https://byborre.com/collection) |
| Design Studio | header, link | login wall on `/?redirectTo=/dashboard`. Stopped. See [login-review.json](login-review.json) |
| Collaborations + | header, button | mega menu, stays on the current page. Plus becomes a close mark |
| About + | header, button | mega menu, stays on the current page |
| Contact | header, link | [/contact](https://byborre.com/contact) |
| Cart, bag icon, aria-label Cart | header, button | cart drawer overlay. Close returns to the page |
| Account, person icon, no accessible name | header, button | same login wall as Design Studio. Stopped |
| Open menu, aria-label Open menu | header, phone only (hidden at 1440) | full-screen mobile menu. Close menu dismisses it |

### Collaborations menu

| Control | Opens |
|---|---|
| Projects | [/projects](https://byborre.com/projects) |
| Brands | [/brands](https://byborre.com/brands) |
| Designers | [/designers](https://byborre.com/designers) |
| Go to Textile Room, on the sample card | [/collection](https://byborre.com/collection) |
| Go to Design Studio, on the creative-control card | login wall (`/dashboard`). Stopped |

### About menu

| Control | Opens |
|---|---|
| Knit Innovation | [/knit-innovation](https://byborre.com/knit-innovation) |
| Responsibility | [/responsibility](https://byborre.com/responsibility) |
| Creative Control | [/creative-control](https://byborre.com/creative-control) |
| Go to Textile Room | [/collection](https://byborre.com/collection) |
| Go to Design Studio | login wall. Stopped |

### Cart drawer

Empty on this visit. Title Cart, Close, illustration, "Your cart is empty", "Add samples to continue", Explore button to [/collection](https://byborre.com/collection). No checkout control was present. Add to cart on the pop-up store was not clicked.

### Mobile menu (390)

Close menu. Cart button (opens the same drawer). Login/Sign-up button (opens the login wall; stopped). Textile Room, Design Studio (login wall), Collaborations +, About +, Contact. Promo cards: Go to Textile Room, Go to Design Studio (login wall). Expanding Collaborations or About reveals the same links as the desktop menus.

### Footer, every public page

| Column | Control | Opens |
|---|---|---|
| legal | TERMS & CONDITIONS | [/terms-and-conditions](https://byborre.com/terms-and-conditions) |
| legal | PRIVACY POLICY | [/privacy-policy](https://byborre.com/privacy-policy) |
| legal | COOKIE SETTINGS | in-page control. Click did not open a separate panel in this session; the first-visit banner is the consent UI. Not accepted or rejected |
| Company | Careers | [https://byborre.homerun.co/](https://byborre.homerun.co/) (200, title BYBORRE). External board, not crawled |
| Company | Team | [/team](https://byborre.com/team) |
| Company | Founders' story | [/founders-story](https://byborre.com/founders-story) |
| Operations | Pop-up Store | [/popup-store](https://byborre.com/popup-store) |
| Operations | FAQ | [/faq](https://byborre.com/faq) |
| Operations | Ways of working | [/ways-of-working](https://byborre.com/ways-of-working) |
| Resources | Press | [https://news.byborre.com/](https://news.byborre.com/) (200, BYBORRE Newsroom). External, not crawled |
| Resources | pCon | [https://catalogs.pcon-solutions.com/](https://catalogs.pcon-solutions.com/#/brands/o-07e8c2a7f6ec42c0852ee1a39ec7389b). External catalog, not crawled |
| Resources | Help center | [https://help-center.byborre.com/knowledge](https://help-center.byborre.com/knowledge) (200, Help Center). External, not crawled. A same-host `/knowledge` path 404s |
| Contact | Email us | [/contact](https://byborre.com/contact) |
| Contact | LinkedIn | [https://www.linkedin.com/company/byborre](https://www.linkedin.com/company/byborre). External profile, not an identity-provider login. Not clicked as a sign-in |
| Contact | Instagram | [https://www.instagram.com/byborre](https://www.instagram.com/byborre). External, not crawled |
| wordmark | BYBORRE | [/](https://byborre.com/) |

### Cookie banner (first visit)

Fixed card: "We use cookies", Privacy policy link to [/privacy-policy](https://byborre.com/privacy-policy), Reject, Accept. Hidden for screenshots. Neither button was clicked, so no consent was posted.

## Home `/`

| Control | Opens |
|---|---|
| Explore samples | [/collection](https://byborre.com/collection) |
| Explore knitting technology | [/knit-innovation](https://byborre.com/knit-innovation) |
| Get started | [/creative-control](https://byborre.com/creative-control) |
| Discover responsibility | [/responsibility](https://byborre.com/responsibility) |

Hero video failed to play in headless Chromium (Mux `manifestIncompatibleCodecsError`). The poster and the "Media Error" overlay are what the capture shows. No theme switch exists on the public site.

## Textile Room `/collection`

| Control | Opens |
|---|---|
| Go to Pop-up Store | [/popup-store](https://byborre.com/popup-store) |
| Color swatches, checkboxes, max 3, plus a reset slash | filters the grid in place. Names: Reset, Beige, Brown, Purple, Red, Orange, Yellow, Green, Blue, Gray |
| Pattern button | dropdown: Floral, Basic, Organic, Illustration, Geometric, Gradient. Stays on `/collection` |
| Textile card (Configure textile, Order free sample, family name) | that family's page, for example [/collection/blink?color=orange&shade=balance](https://byborre.com/collection/blink?color=orange&shade=balance) |
| Card bag icon | same family page (sample path), not a checkout |

35 textile families were listed. Each card is the same control type. Families seen: Blink, Nelly, Lumi, Otto, Dune, Groma, Guido, Viktor, Tosho, Etaney, Rovin, Eirene, Niels, Marcelle, Kalle, Miko, Billie, Emma, Dirk Duif, Alina, Odette Ex, Eva, Iris, Britt, Kyra, Jiwon, Joep, Daniel, Daphna, and the rest of the 35.

## Textile family, example `/collection/blink`

Query `color`, `shade`, and sometimes `repeat` updates the configuration in place.

| Control | Opens |
|---|---|
| PHOTO / RENDER | switches the gallery in place |
| Gallery next arrow | next image, in place |
| Share | button present. Click did not open a share sheet or leave the page in this session |
| Color radios | updates `?color=` on the same family |
| Tone cards BASE, BALANCE, BOLD | updates `?shade=` |
| Repeat, where the family has it | updates `?repeat=` (small, medium, large) |
| Order sample | stays on the family page in this session (yellow bar). Not submitted. A checkout was not started |
| Get in touch with sales | [/contact](https://byborre.com/contact) |
| Material accordion | expands in place. Inner link "See textile passport" |
| Performance specs, Suggested use, Downloads | accordions, collapsed by default, expand in place |
| Download textile passport | file action. Not downloaded |
| "also on Pop-up Store" when shown | [/popup-store?sku=…](https://byborre.com/popup-store) |
| You may also like cards | another family page |
| Order free sample on a related card | that family's page |

## Pop-up Store `/popup-store`

Same color checkboxes as Textile Room. Add to cart is present and was not clicked (purchase path). Go to Textile Room returns to [/collection](https://byborre.com/collection). A `?sku=` query deep-links a listed knit.

## Creative Control `/creative-control`

| Control | Opens |
|---|---|
| Explore Textile Room / Get started | [/collection](https://byborre.com/collection) |
| Explore Design Studio | [/responsibility](https://byborre.com/responsibility) on this capture (the labelled control resolved there) |

## Responsibility `/responsibility`

| Control | Opens |
|---|---|
| European partners | [https://www.lavatextiles.com/news/oekotex-step](https://www.lavatextiles.com/news/oekotex-step). External, not crawled |
| Environmental Product Declaration | [https://www.environdec.com/library/epd30200](https://www.environdec.com/library/epd30200). External, not crawled |
| Download our Impact Report | HubSpot landing page on `byborre-20009495.hs-sites.com`. External, not crawled |

Knit Innovation `/knit-innovation`, Team `/team`, Founders' story `/founders-story`, Ways of working `/ways-of-working`, Terms `/terms-and-conditions`, and Privacy `/privacy-policy` are long-form pages. Their only in-page controls are the shell, the sample marquee, and (on legal pages) in-body links to the other legal page. No forms.

## FAQ `/faq`

Three groups: Textile information, Ordering and delivery, Responsibility. Each question is a button that expands the answer in place. One opened answer names `create.byborre.com` as the design editor and says an account is required. That host was not opened.

## Contact `/contact`

A form is visible and was not filled or submitted: First name, Last name, Email, Profession, Company name, Company vertical (select), How can we assist you? (select), project description (textarea), How did you hear about us?, Submit. Named people on the page are published staff, not account data.

## Projects, Brands, Designers

Index pages. Each card is a link to a story, plus a Read more button on the card.

| Index | Story pattern | Example |
|---|---|---|
| `/projects` | `/byborre-x-<slug>` | `/byborre-x-the-social-hub` |
| `/brands` | `/byborre-x-<slug>` | `/byborre-x-ahrend` |
| `/designers` | `/byborre-x-<slug>` | `/byborre-x-pastina` |

Three stories were opened (Social Hub, Ahrend, Pastina). Each is a long-form page with the shared shell and no extra form. The other cards are the same control type and were not each opened.

## Stopped branches

| Control | URL recorded | Why stopped |
|---|---|---|
| Design Studio, Go to Design Studio, account icon, Login/Sign-up | `https://byborre.com/?redirectTo=/dashboard` | login dialog. Email and password. Nothing typed |
| Sign up, inside that dialog | same URL, dialog swaps to Sign up to continue | work email, full name, company, field of work, password. Nothing typed. No account created |
| Forgot password? | same URL, dialog swaps to Forgot password? | asks for an email to send a reset code. Not submitted. No code arrived |
| `/dashboard` direct | redirects to `/?redirectTo=/dashboard` and the same login dialog | signed-in app not entered |
| Add to cart, checkout, sample order submit, contact Submit, newsletter | not followed | purchase, trial, and form-submit ban |
