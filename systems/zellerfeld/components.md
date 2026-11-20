# Components

Public signed-out components measured on www.zellerfeld.com on 2026-11-19. Values are computed styles. Crops were not cut: the preview browser produced no screenshot frames, and the headless shots are the evidence.

| Component | Where | Values |
|---|---|---|
| Announcement strip | Home, top | 40px tall, 16px Exposure, white on the black page. Text: "PERFECT FIT GUARANTEE. WE MAKE SURE YOUR SHOES FIT." |
| Header | Home, 1440 | Black, 84px tall, padding 24px 40px. At 390 the padding is 24px 16px. |
| Icon button | Menu, home | 36x36, radius 4px, fill rgba(255, 255, 255, 0.1), Phonic 14px. |
| Wordmark | Header | 134x28 link, gap 8px, radius 4px. Focus ring declared as 2px #3773f5. |
| Search | Header, desktop | Placeholder "WHAT ARE YOU LOOKING FOR?". Hidden at 390. Not submitted. |
| Outline button | CREATE | 36px tall, padding 0 16px, radius 4px, 1px solid #ff5e3e, text #ff5e3e, Phonic 14px, tracking -0.14px, uppercase. Hover did not change the fill. |
| Ghost button | SIGN IN | Same size, fill rgba(255, 255, 255, 0.1), white text. Opens the sign-in card. Not submitted. |
| Primary button | START ONBOARDING, BUY NOW, newsletter | Fill #ff5e3e, text #000. Onboarding is 36px. BUY NOW is 56px tall and 333px wide. |
| Rank row | Home lists | Title Lateral Zeller TM 14px/700. Creator Phonic 12px uppercase at 50% white. Price Phonic 14px/703, tracking -0.14px. |
| Sold-out badge | Product rows | Phonic 12px/703, padding 4px, radius 6px, 1px border at 20% white, text at 50% white. |
| Product panel | /products/pdf-bol-sneaker | 443px wide, padding 24px, radius 12px, 1px border at 20% white. |
| Colour label | Product panel | "PICK COLOR" and the selected name "BLACK". Swatches are image tiles. |
| Reviews link | Product panel | Outline button, 36px, coral text and border. Not followed into a write flow. |
| FAQ heading | /pages/faq | Lateral Zeller TM 72px/700, line-height 72px, tracking -1.8px, at 1440. |
| FAQ row | details/summary | Summary Exposure 16px. Open answer Exposure 16px at 60% white, line-height 20px. |
| Newsletter field | /pages/newsletter | Lateral 16px, tracking -0.8px, placeholder "Enter your email". Not submitted. |
| Newsletter note | Same page | Exposure 12px, white at 60%. |
| Sign-in card | /sign-in | Panel rgb(250, 250, 250), about 402x472, radius 8px, on a black page. |
| Sign-in title | Card | Lateral Zeller TM 20px/700, colour rgb(23, 23, 23). |
| Google button | Card | 322x56, Phonic 14px/500, uppercase. Not pressed. |
| Email field | Card | 322x40, radius 6px, padding 8px 16px, Phonic 16px/703, uppercase placeholder. Not submitted. |
| Continue | Card | 322x56, fill #ff5e3e, text black, Phonic 14px/500. Not pressed. |
| Use phone | Card | 12px Lateral, coral. Not pressed. |
| Sign up | Card | Coral link. Not followed. |
| Cookie dialog | First load | White card, radius 16px, padding 16px, shadow matching --shadow-lg. Accept is black fill, white Phonic 14px, 36px tall. Decline is black at 5%. Hidden for screenshots, never submitted. |
| Footer heading | Home footer | "Shipping worldwide", Lateral Zeller TM 32px/700. |
| Footer column label | Footer | "Company", Exposure 16px, white at 50%. |
| Footer link | Footer | Phonic 14px, uppercase, tracking -0.14px, white. |

## Gaps

- No light theme. `html` has no theme attribute. Semantic colours are declared on `.dark`. `prefers-color-scheme: light` was not given a second palette.
- Checkbox, radio, switch, select, tabs-as-a-widget, tooltip, toast, table, avatar, and badge-as-a-status-system were not present on the public pages that were measured.
- The feed tabs ("Today's top shoes", "Selected for you", "All time favourites") are visible in the home screenshot. Their computed style was not isolated from the carousel, so they are not tokenised.
- Hover on CREATE did not change the computed fill. Pressed and disabled were not forced.
- Focus-visible was declared on the wordmark (`ring-[#3773f5]`) and on FAQ summaries. A keyboard focus ring was not captured as its own crop.
- Size picker and checkout were not opened. BUY NOW was hovered, not followed.
- Phone sign-in, Google sign-in, sign-up, and newsletter submit were not entered.
- Studio dashboard was opened only far enough to see a guest drop zone. It was not measured as the store system and no file was uploaded.
- Icon SVGs were not extracted. The wordmark and menu glyph are in the screenshots.
