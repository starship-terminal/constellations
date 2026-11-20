# Patterns

| Pattern | Where | What was on screen |
|---|---|---|
| Marketing shell | https://parallel.ai/ at 1169x731 | White header, 74px, side padding 48px. Wordmark in Gerstner Programm. Nav links in 13px FT System Mono, ink `#858483`. CONTACT is the grey button. LOG IN is the orange button. |
| Phone shell | Same URL at 390x844 | Header 66px, side padding 16px. Wordmark plus a MENU button (white, 13px mono, 34px tall). Desktop nav links were not in the header. |
| Hero | Home | h1 "Where agents find answers", 36px at 1169px and 28px at 390px, weight 500, ink `#181818`. Lede in `#858483`, 26px at desktop and 20px at 390px. |
| Pricing columns | https://parallel.ai/pricing | Four names: Launch, Build, Scale, Enterprise. Names are 26px weight 500. Prices (Free, Pay-as-you-go, $1,000/mo, Custom) are 26px weight 400 in `#858483`. POPULAR sits on Build. The upgrade and contact-sales actions were not clicked. |
| Signed-out login | https://platform.parallel.ai/login?redirectTo=%2F | Dark shell. Heading "Get started with Parallel" at 28px. Google, SSO, an email field, and Continue with email. Form column is 360px wide. |
| Docs | https://docs.parallel.ai/getting-started/overview | Light docs chrome. Sidebar ink `#777370`. Overview is the orange selected row. Search is a 36px pill. Get API Key was not opened. |

The marketing page did not show a dark theme toggle. The login page loaded with `class="dark"` on `html`. That is a separate surface, not a theme switch of the marketing site.
