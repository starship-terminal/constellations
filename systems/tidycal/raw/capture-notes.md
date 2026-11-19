# Capture notes

Measured 2026-11-19. Public signed-out surfaces only.

The T3 preview browser opened https://tidycal.com/ in its own tab. Computed styles were read with getComputedStyle. Viewport there was 1169 by 731, device pixel ratio 2, visual viewport scale 1. Login, pricing, and register loaded in the same tab. None was a Cloudflare challenge.

preview_snapshot returned "The browser is not producing screenshot frames" on register and again after a retry. Measurements already read were kept. No screenshot was invented from that browser.

Headless Chromium then loaded the same public pages, because they had already loaded without a challenge. Viewport 1440 by 900 and 390 by 844, device pixel ratio 2, visual viewport scale 1. PNG pixel size is 2 times the CSS viewport. Page screenshots in screenshots/ are 256-colour PNGs. Crops stay full colour.

## Pages

| Page | URL | Status |
|---|---|---|
| Home | https://tidycal.com/ | Measured and screenshotted |
| Pricing | https://tidycal.com/pricing | Measured and screenshotted. Buy and Get the deal were not followed |
| Login | https://tidycal.com/login | Measured and screenshotted. Form not submitted. Google and LinkedIn not pressed |
| Register | https://tidycal.com/register | Measured and screenshotted. Name, email, and password were not filled. reCAPTCHA present. Not submitted |
| Forgot password | https://tidycal.com/forgot-password | Screenshotted. Email not entered. Not submitted |
| Directory | https://tidycal.com/directory | Loaded. Not kept. The page lists other people's names and profile pictures |

## Not entered

- No email, name, or password was typed.
- No AgentMail signup. Register is email-capable, but it also offers Google and sits behind reCAPTCHA. The task allows AgentMail only for an email-only form.
- No calendar OAuth. Continue with Google, Continue with LinkedIn, and Sign up with Google were not pressed.
- No card. Pricing "Buy on" and "Buy now" leave for AppSumo or checkout and were not pressed.
- No phone, government ID, wallet, or KYC.

## Theme

html has no data-bs-theme on these pages. The stylesheet declares html[data-bs-theme=dark] rules for the nav and footer. That theme was not on the public pages, so dark values are a gap.
