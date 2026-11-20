# Readings

Captured 2026-11-19 from the live public site. Preview browser tab `tab_48` loaded the pages and `preview_evaluate` read computed styles. `preview_snapshot` failed twice with "The browser is not producing screenshot frames". Screenshots were then taken with headless Playwright on the same public URLs. None of those loads showed a Cloudflare challenge.

Viewport evidence is in each `screenshots/*.png.capture.json`.

## Pages

| Page | URL | Status |
|---|---|---|
| Home | https://risecalendar.com/ | 200, sunset essay |
| Pricing | https://risecalendar.com/pricing | 200 |
| Blog | https://risecalendar.com/blog | 200 |
| Post | https://risecalendar.com/blog/announcing-rise-2.0 | 200 |
| Manifesto | https://risecalendar.com/manifesto | 200 |
| Comparison | https://risecalendar.com/alternative-to-asana | 200 |
| Sign-in | https://risecalendar.com/signin | 404 |
| Login | https://risecalendar.com/login and https://beta.risecalendar.com/login | 404 |
| App | https://beta.risecalendar.com/app | opaque redirect, then the sunset essay |

## :root

From stylesheet `ec71784565c9a205.css`. Triplets are R,G,B.

| Name | Triplet |
|---|---|
| --foreground | 30,42,41 |
| --background | 252,252,254 |
| --surface | 247,247,252 |
| --sidebar | 248,249,253 |
| --input | 241,242,248 |
| --border | 214,217,228 |
| --offset-text | 183,187,205 |
| --offset-dark | 108,111,125 |
| --primary | 113,97,236 |
| --negative | 255,42,90 |
| --warning | 255,193,65 |
| --success | 25,190,47 |
| --system-black | 0,0,0 |
| --system-white | 255,255,255 |
| --system-blue | 0,0,238 |
| --dolphin | 100,127,160 |
| --blue | 1,115,240 |
| --violet | 105,70,228 |
| --pink | 228,63,255 |
| --orange | 255,106,1 |
| --yellow | 255,179,1 |
| --turquoise | 19,177,168 |
| --green | 16,180,38 |

No second block. No `prefers-color-scheme`. No `prefers-reduced-motion`.

## Computed, desktop innerWidth 1440 unless noted

- Body: background rgb(255, 255, 255), color rgb(30, 42, 41), font __Inter_9d3317, 16px / 24px, weight 400.
- Header: 80px, padding 28px 0, white, sticky.
- Home title: 48px / 48px, weight 700, letter-spacing -2.4px. At 390px: 30px / 36px, -1.5px.
- Article: max-width 768px, padding 80px 20px.
- Inline link: color rgb(113, 97, 236), weight 600.
- Pricing primary button: 34px, padding 8px 16px, radius 4px, background rgb(113, 97, 236), color white. Hover rgba(113, 97, 236, 0.8).
- Pricing secondary button: white, border 1px solid rgb(214, 217, 228). Hover background rgb(241, 242, 248), color rgba(30, 42, 41, 0.9).
- Pricing cards: 480 by 357, padding 36px, radius 6px, gap 20px.
- Switch off track: 32 by 16, rgba(108, 111, 125, 0.6). On track: rgb(113, 97, 236). Thumb translates 16px.
- Turning the switch on changes the Teams price from €10 to €8. That is content, not a colour token.
- Comparison h1 at 1440: 56px / 56px, -2.8px. At 390: 30px / 36px, -1.5px.
- Comparison CTA: 46px, 18px, padding 8px 24px, primary background.
- Breakpoints in the stylesheet: 640px, 768px, 1024px.

## Logo stops

Bottom gradient: #767DF9, #7161EC at 0.4958, #5730E3. Top gradient: #FF7557, #FFAF66. Word fill: black.

## Not entered

No email, password, card, phone, or OAuth. No Google Calendar connection. AgentMail was not used. Signup is not an email form. The sign-in URL 404s.
