# Mangomint patterns

Public pages, 2026-11-18. The salon admin was not reached. Recorded in [components.md](components.md) Gaps and in the catalog `capture.gaps`.

## Marketing frame

A cream page (`#fcfafa`), an 80px transparent header, then a 54px headline. [Home](screenshots/home-light-default.png) leads with "Everything you need to power your salon and spa", an outline Book a demo, a filled Try it now, and a mono "Watch a video tour" link. [Phone](screenshots/mobile-home-light-default.png) collapses the bar to the wordmark, a Pricing pill, and a hamburger. The open menu is a full list with Book demo and Try it now ([open](screenshots/mobile-home-light-menu.png)).

## Businesses menu

Businesses is a local dropdown, not a page. It lists Hair Salons, Med Spas, IV Therapy and the other verticals ([open](screenshots/home-light-businesses.png)). The desktop Features menu did not open: the click timed out. Phone Features is a collapsed row in the menu shot.

## Pricing

`/pricing/` publishes "Monthly price is $120 per location and $10 per user." Add-ons are Phone $70/mo per line, Marketing starting at $30/mo, and Payroll $50/mo plus $8 per worker. The calculator default in the shot showed $200/mo. One FAQ was opened locally ([open](screenshots/pricing-light-faq-open.png)). Start a free trial was not pressed.

## Demo and trial

`/demo/` is "Talk to one of our software experts" with service chips and a Continue control ([page](screenshots/demo-light-default.png)). `/trial/` is step 1 of 5, the same chips ([page](screenshots/trial-light-default.png)). Continue was measured and not pressed, so no later step, no validation, and no account was created.

## Public booking

`booking.mangomint.com` without a company id says the id is missing. Marketing embeds company id `737397`. That page loads signed out, titled "Mangomint Internal - Book appointment", with "Select a service" and one Rebook a past service control. The service list is empty ([desktop](screenshots/book-light-default.png), [phone](screenshots/mobile-book-light-default.png)). Rebook was not pressed. No slot and no checkout.

## Sign-in wall

`app.mangomint.com` redirects to `/login`: navy page, email, password, a visibility toggle, Log In, and Forgot password ([desktop](screenshots/login-light-default.png), [phone](screenshots/mobile-login-light-default.png)). The email field was typed into with a throwaway address, then cleared. Log In was not pressed. Forgot password was opened and not submitted ([page](screenshots/forgot-password-light-default.png)).

## Other public pages

About, customers, blog, contact, learn and legal all load signed out. Learning Center search was focused and not queried. `/login` on the marketing host is a 404 ([shot](screenshots/notfound-light-default.png)). `book.mangomint.com` and `online.mangomint.com` did not resolve.

## Motion

Reduced motion is partial: marketing pages keep many transitions, the login host honours reduce ([raw/motion.json](raw/motion.json)). The app sheet declares `--mt-duration-fast` 150ms, `--mt-duration-base` 200ms, `--mt-duration-normal` 300ms and `--mt-duration-slow` 500ms. Those are declared custom properties. The token file's durations come from the probe, not from a guessed ramp.
