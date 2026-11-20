# Readings

Captured 19 November 2026. T3 preview tab, then headless Chromium for screenshots of pages that had already loaded without a Cloudflare challenge.

## Viewports

| Surface | innerWidth | innerHeight | devicePixelRatio | visualViewport scale |
|---|---|---|---|---|
| Home, first read | 1169 | 731 | 2 | 1 |
| Pricing and login after resize | 1440 | 900 | 2 | 1 |
| Headless desktop | 1440 | 900 | 2 | 1 |
| Headless phone | 390 | 844 | 2 | 1 |

`preview_snapshot` returned "The browser is not producing screenshot frames." Measurements already read were kept. Screenshots are from headless Chromium after that.

## Pages

- https://www.sunsama.com/ marketing home. Cookie banner dismissed with the Accept button. No account.
- https://www.sunsama.com/pricing public pricing.
- https://app.sunsama.com/login signed-out login. Email field was focused to read the focus border. The form was not submitted. Google, Outlook and SSO were not clicked. No calendar was connected. No signup.

## Marketing colours, computed

| Role | Value | Where |
|---|---|---|
| Page | #ffffff | body |
| Warm wash | #f6f5f1 | .goodbgshape, --bg-secondary-new |
| Card | #fafafa | .subfeaturecard, --bg-light-grey-new |
| Feature card | #f8f8f8 | .more-fea-card |
| Ink | #202228 | body, --black |
| Muted | #202228 at alpha 0.6 | .more-fea-desc |
| Accent | #ff891c | a.buttonprimary, --ss-orange |
| Accent label | #ffffff | .buttonlabel |
| Outline button | white fill, 3px #ff891c border, #ff891c label | variant a01c4f |
| Border | #f2f2f2 | .subfeaturecard, --border-new |
| Feature border | #0000001f | .more-fea-card |

Primary hover is declared as #db7414. A live hover was not held.

## Login colours, computed at 1440

| Role | Value | Where |
|---|---|---|
| Page | #f7f8fa | .onboarding-base-container |
| Card | #ffffff, radius 16px, padding 40px, 400 by 576 | .onboarding-main-container |
| Ink | #413f39 | body, active tab |
| Muted | #787878 | inactive tab, recover line |
| Placeholder | #b4b4b4 | input ::placeholder |
| Divider | #a1a1a1 | .text-divider, uppercase OR |
| OAuth border | 1px solid #dcdcdc, radius 4px, height 45.3 | .onboarding-btn-google |
| Email button | #d2d2d2 fill, #ffffff text, height 45.3 | .onboarding-btn-secondary |
| Focus | 1px solid #8cb4f0 | email input after focus() |
| Link | #2ca7ff | a.blue-link |
| Active tab | 2px solid #413f39, weight 600 | .auth-mode-tab-active |
| Tab bar | 1px solid #dcdcdc | .auth-mode-tabs |

The login stylesheet has `.dark` rules. The signed-out page did not have the dark class. Dark was not captured.

## Fonts

Marketing: DM Sans. Login: Avenir, then Arial, Helvetica Neue, Helvetica, sans-serif.

## Not entered

No email was typed. No password. No Google, Outlook or SSO click. No calendar connection. No card, phone or company SSO. Signup at /start/signup was not opened.
