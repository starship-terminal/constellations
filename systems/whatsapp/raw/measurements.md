# Measurements

Read on 2026-11-19 from public whatsapp.com pages, signed out, in headless Chromium. Desktop viewport 1440 x 900 at deviceScaleFactor 1. Phone viewport 390 x 844 at deviceScaleFactor 2 (PNG 780 x 1688).

The T3 preview tab loaded the same home page at innerWidth 1169, devicePixelRatio 2, and returned the same computed colours. It produced no screenshot frames.

| Element | Computed |
|---|---|
| body | background `#ffffff` on contact, color `#1c1e21`, font WhatsApp Sans Var 12px / 400, line-height 16.08px |
| header at 1440 | 1440 x 80, background `#fcf5eb`, padding 16px 60px, color `#111b21` |
| header at 390 | 390 x 58, background `#fcf5eb`, padding 12px 24px |
| header at 1169 (preview) | padding 12px 24px, height 77 |
| h1 home at 1440 | 80px / 400, line-height 80px, color `#ffffff` |
| h1 home at 390 | 44px / 400, line-height 44px, color `#ffffff` |
| h1 download | 60px / 400, line-height 60px, color `#1c1e21` |
| home h2 | 48px or 60px / 400 |
| lede | 18px / 400, line-height 25px, color `#1c1e21` |
| nav Privacy | 16px / 500, line-height 16px, color `#1c1e21` |
| Download | 145 x 45, padding 12px 20px, radius 50px, fill `#25d366`, label `#1c1e21`, border 1px solid `#1c1e21`, weight 500 |
| Download hover | fill unchanged, rgb(37, 211, 102) |
| Download focus | outline rgb(0, 95, 204) auto 1px, offset 1px, box-shadow none |
| Log in | 116 x 46, padding 14px 20px, radius 50px, fill `#ffffff`, border 1px solid `#111b21` |
| Learn more | 16px / 400, transparent, no radius |
| footer | background `#111b21`, labels 12px `#ffffff`, links 18px `#ffffff` |
| privacy field | background `#111b21` |
| mint band | background `#e6ffda` |
| home sections | background `#fcf5eb` |
| contact link | sampled `#0373e9` from screenshot pixels |
| language select | in DOM, display none, radius 50px, fill `#111b21`, color `#ffffff` |
| motion | color 0.33s linear, border-color 0.5s ease-out, background-color 0.33s linear; a header control uses 0.67s cubic-bezier(0.2, 0, 0, 1) |
| reduced motion | matchMedia reduce was true; the same 0.33s and 0.5s durations remained |

No custom properties on `:root`. `@font-face` WhatsApp Sans Var, weights 400, 500, 700, one woff2.
