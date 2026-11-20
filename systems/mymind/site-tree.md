# mymind.com site tree

Mapped 2026-11-21 from https://mymind.com/ in headless Chromium (Playwright), desktop 1440×900. www.mymind.com redirects to mymind.com. The sitemap at https://mymind.com/sitemap.xml lists 202 URLs. Every visible control below says what it opens: a page, a menu, a dialog, an external site, or a dead end. Auth walls were recorded and not entered.

The signed-in app is not on this host. Log in, Sign up, Try it out, Create an account and pricing Sign up all leave mymind.com for access.mymind.com. https://mymind.com/login is a 404 page on the marketing site.

## Shell (every marketing page)

| Control | Opens |
|---|---|
| Logo | page https://mymind.com/ |
| What | page https://mymind.com/ (same document; no separate /what in the nav) |
| Why | page https://mymind.com/why |
| How | page https://mymind.com/how |
| Log in | auth wall https://access.mymind.com/signin |
| Sign up | auth wall https://access.mymind.com/ |
| Watch the intro (home) | in-page video, not a new page |

At 390px the header collapses. A control labelled Menu (`a.open-menu`, aria-label "Menu") opens an in-page overlay, not a new URL. The overlay lists What, Why and How, plus LOG IN and SIGN UP. LOG IN opens the auth wall https://access.mymind.com/signin. SIGN UP opens the auth wall https://access.mymind.com/. The close control (×) dismisses the overlay and stays on the same page.

Footer, repeated on the long marketing pages:

| Control | Opens |
|---|---|
| See how it works / mymind walkthroughs / Video tutorials | page https://mymind.com/videos |
| Why people love mymind | page https://mymind.com/reviews |
| Our pricing | page https://mymind.com/pricing |
| mymind & ADHD | page https://mymind.com/adhd |
| iOS app / iPhone app / GET APP | external https://apps.apple.com/us/app/mymind-extend-your-mind/id1520332347 |
| Android app / GET APP | external https://play.google.com/store/apps/details?id=com.mymind.access |
| Browser extension | page https://mymind.com/browser-extensions |
| MacOS app / INSTALL (Safari) | external https://apps.apple.com/us/app/mymind-extend-your-mind/id1532801185 |
| Chrome / Edge INSTALL | external Chrome Web Store |
| Looking for another browser? | external https://mymind.helpscoutdocs.com/article/97-install-browser-extension |
| Our manifesto | page https://mymind.com/manifesto |
| Our promise | page https://mymind.com/our-promise |
| Mind Palace | page https://mymind.com/palace |
| Interviews | page https://mymind.com/interviews |
| @mymind on Twitter | external https://twitter.com/mymind |
| Guides & contact form | external https://mymind.helpscoutdocs.com/ |
| Sign in to mymind | auth wall https://access.mymind.com/signin |
| Create an account | auth wall https://access.mymind.com/ |
| Terms & Conditions | page https://mymind.com/terms |
| Privacy Policy | page https://mymind.com/privacypolicy |
| FAQ | page https://mymind.com/faq |

## Home https://mymind.com/

| Control | Opens |
|---|---|
| TRY IT OUT | auth wall https://access.mymind.com/signin |
| SIGN UP FOR FREE | auth wall https://access.mymind.com/signin |
| SEE THE MAGIC OF SMART BOOKMARKING | page https://mymind.com/videos#save-anything-with-one-click |
| HOW TO SAVE ANYTHING TO YOUR NEW MIND | page https://mymind.com/videos#savingstuff |
| WATCH THE VIDEO | page https://mymind.com/videos#instantly-find-folders |
| NOT CONVINCED? WE HAVE MORE | page https://mymind.com/reviews |
| processor.ai marks | external https://processor.ai/ |
| video elements | in-page playback, no dialog |

## Product pages

| Page | Extra controls | Opens |
|---|---|---|
| /why | essay links into /how and /videos anchors | page |
| /how | FOR DESIGNERS, FOR WRITERS, FOR MARKETERS, FOR DEVELOPERS, FOR RESEARCHERS | in-page anchors on /how |
| /how | video tutorial links | page https://mymind.com/videos#… |
| /how | FOR EVERYONE | page https://mymind.com/ |
| /how | CREATE YOUR NEW MIND | auth wall https://access.mymind.com/signin |
| /what | HAVE A LOOK BEHIND THE SCENES | page https://mymind.com/how |
| /what | READ MORE ABOUT THE WHY | page https://mymind.com/why |
| /what | Download Browser Extension | page https://mymind.com/browser-extensions |
| /what | Sign in / Create a new account | auth wall (recorded, not opened) |
| /what | Report a bug & help | external Help Scout |
| /videos | PLAY VIDEO cards | in-page anchors, or https://mymind.com/videos?preview_id=…&preview=true (same page, preview query). No dialog. |
| /reviews | quotes | dead end (no further control) |
| /adhd | essay | footer only |
| /browser-extensions | store INSTALL links | external stores |
| /browser-extensions | Click here to learn more | external Help Scout article |
| /browser-extensions | OUR PROMISE FROM US TO YOU | page https://mymind.com/our-promise |
| /mobile | iOS / Android tabs (`div[role=button]`) | in-page tab, not a new page |
| /mobile | empty role=button controls | dead end (no navigation) |
| /artworks | Get the mobile app | page https://mymind.com/mobile |
| /artworks | artwork credits | external artist sites |
| /pricing | Monthly | in-page billing toggle |
| /pricing | Yearly SAVE ~20% | in-page billing toggle |
| /pricing | SIGN UP | auth wall https://access.mymind.com/ |
| /pricing | We're serious / For your eyes only / Proudly Indie | page https://mymind.com/our-promise |
| /pricing | AI summaries | page https://mymind.com/new-feature-the-advanced-ai-summary |
| /pricing | Companion apps / smartphone app | page https://mymind.com/mobile |
| /pricing | 8 reasons to use mymind | page https://mymind.com/6-reasons-mastermind |
| /manifesto | principles | dead end (prose) |
| /our-promise | promise | dead end (prose) |
| /private-first | essay | dead end (prose) |

## Indexes

| Page | Control | Opens |
|---|---|---|
| /palace | each card title (about 170) | page, one essay URL per card (sitemap articles) |
| /interviews | each name | page /into-the-mind-of-… or /on-the-mind-of-… or /into-my-mind-… |
| /interviews | Firefox .xpi | file download https://mymind.com/assets/uploads/2021/11/mymind_an_extension_for_your_mind-2.0.2-fx.xpi |

One palace essay and one interview were opened to confirm the template. The rest are the same article layout. They are listed in the sitemap, not each captured as a separate state.

## Legal and policy

Each is a prose page. In-page links go to sibling policies or the footer. No forms.

| Path | Title |
|---|---|
| /faq | Questions and answers about your new mind. |
| /privacypolicy | Privacy Policy |
| /terms | Terms of Service |
| /data-security | We protect your data as if it's our own. |
| /subprocessors | mymind subprocessors (vendor links are external) |
| /ai-usage-policy | AI Usage Policy |
| /cancellation-policy | Cancellation Policy |
| /refund-policy | Fair Refund Policy |
| /inactive-account-policy | Inactive account policy |
| /use-restrictions | Use Restrictions |
| /extension-privacy | Our Browser Extension Privacy Policy |

/faq links "mass-import" to page https://mymind.com/why-mymind-does-not-have-an-import-feature-as-of-now.

## Auth walls (stopped)

| Control or URL | Result |
|---|---|
| https://mymind.com/login | page, HTTP 404, heading "404 - Not found". Links back to home and the same Log in / Sign up walls. |
| https://access.mymind.com/signin | auth wall. A headed browser on 2026-11-21 showed a welcome screen and did not open an email form. Headless Chromium from this capture got HTTP 403 from CloudFront ("Request blocked") and no form. Not entered. |
| https://access.mymind.com/ | auth wall (Sign up / pricing SIGN UP). Same CloudFront 403 in headless Chromium. Not entered. |

No password, code, Google, or Apple control was used.

## Not on the marketing tree

The signed-in library, search, cards, spaces and settings are behind the auth wall. Help Scout (mymind.helpscoutdocs.com) is a separate host and was not crawled.
