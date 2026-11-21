# Hers site tree

Mapped on 2026-11-21 from the public homepage [https://www.forhers.com/](https://www.forhers.com/), signed out, light theme. The page title was "Hers | Women’s Healthcare, Online | Hers". `colorScheme` was `normal`. There is no theme switch.

The header has three controls: the wordmark, Log in, and Slide Menu Toggle. Log in and the slide menu were opened. No email, password, phone, or code was typed. No identity provider was clicked. No form was submitted. No consultation or purchase was started. Quiz paths (`/quiz`, `/g/i/...`, `/c/...`, `/lp/...`) were not followed.

## Promo bar

A lime banner sits above the header.

| Control | Opens |
|---|---|
| Peptides+ is here. Check it out | `/peptides-plus` |

## Header

| Control | Opens |
|---|---|
| Wordmark (`aria-label` Home) | `/` |
| Log in (`aria-haspopup`) | Login menu on the same page. Not a navigation. |
| Slide Menu Toggle (`aria-label`, `aria-haspopup`) | Slide drawer on the same page. |

There is no Sign up control in the header.

## Log in

The header Log in control (`data-testid` GlobalNavigationLogin, `aria-haspopup`) opens the login wall. The wall also loads at `/account/login`. That visit bounced back to the homepage and painted the 404 chrome beside the form. The query string on that bounce is not copied here. Shot: [login-light-wall.png](screenshots/login-light-wall.png). Not submitted.

| Control | Opens |
|---|---|
| Email, Password | Empty fields. Not typed. |
| Forgot your password? | Password reset. Not opened. |
| Log in (submit) | Not pressed. |
| Create an account | Registration. Not opened. |
| Continue with Google | Identity provider. Not clicked. |
| Continue with Apple | Identity provider. Not clicked. |
| Close | Dismisses the wall. |

There is no Sign up control in the header.

## Slide menu

Slide Menu Toggle opens a drawer. Each category button replaces the panel. It does not navigate. Close returns to the homepage. The drawer photographed this visit was already on More. Shot: [home-light-menu.png](screenshots/home-light-menu.png). The other panels were read from the homepage navigation payload, not photographed one by one.

| Control | Opens |
|---|---|
| Weight Loss | Weight Loss panel |
| Peptides+ | Peptides+ panel |
| Hair Regrowth | Hair Regrowth panel |
| Menopause | Menopause panel |
| Perimenopause | Perimenopause panel |
| Labs | Labs panel |
| More | More panel |

The home panel also lists TOP TREATMENTS, LEARN, and OUR BRANDS. Those links are below.

### Weight Loss panel

| Item | Opens |
|---|---|
| Weight loss treatments | `/weight-loss` |
| Membership | `/weight-loss/membership` |
| Hers App | `/weight-loss/app` |
| The Science | `/weight-loss/science` |
| FAQs | `/weight-loss/faq` |
| Wegovy® Pill | `/weight-loss/wegovy-pill` |
| Wegovy® Pill Microdosing Plan | `/weight-loss/wegovy-pill-microdose` |
| Wegovy® Pen | `/weight-loss/wegovy-pen` |
| Ozempic® Pill | `/weight-loss/ozempic-pill` |
| Zepbound® KwikPen® | `/weight-loss/zepbound-kwikpen` |
| Zepbound® Vial | `/weight-loss/zepbound-vial` |
| Foundayo™ Pill | `/weight-loss/foundayo-pill` |
| Ozempic® | `/g/i/wm` (intake). Not followed. |
| Mounjaro® | `/g/i/wm` (intake). Not followed. |
| Meal replacement kits | `/weight-loss/meal-replacement` |
| See if you’re eligible | `/g/i/wm` (intake). Not followed. |
| Calculate your body mass index | `/tools/bmi-calculator` |
| Calculate your daily calories burned | `/tools/tdee-calculator` |
| Calculate your caloric deficit | `/tools/calorie-deficit-calculator` |
| Calculate your daily protein intake | `/tools/protein-calculator` |
| Calculate your daily water intake | `/tools/water-intake-calculator` |
| Quiz: Why Can't I Lose Weight? | `/tools/why-cant-i-lose-weight` |
| Pricing | `/weight-loss/drug-pricing` |
| FSA/HSA reimbursement | `/weight-loss/fsa-hsa` |
| Start your free weight loss assessment (featured) | `/c/wm` (consultation). Not followed. |

### Peptides+ panel

| Item | Opens |
|---|---|
| Peptides+ | `/peptides-plus` |
| The Science | `/peptides-plus/science` |
| Quality & Safety | `/peptides-plus/quality` |
| Clinical Standards | `/peptides-plus/clinical-standards` |
| Sermorelin | `/peptides-plus/sermorelin` |
| Glutathione | `/peptides-plus/glutathione` |
| L-carnitine | `/peptides-plus/l-carnitine` |
| NAD+ | `/peptides-plus/nad` |
| Vitamin B12 | `/peptides-plus/vitamin-b12` |

### Hair Regrowth panel

| Item | Opens |
|---|---|
| About Hers Hair | `/hair-care` |
| Hair loss treatments | `/hair-loss` |
| Hair Blends | `/hair-blends` |
| Take the free hair quiz (featured) | `/quiz?currentStep=1`. Not followed. |
| Overall thinning, Stress related thinning, Aging and hormones, Menopausal | Same quiz. Not followed. |
| Hair Vitamins + Minoxidil | `/hair-blends` |
| Biotin + Minoxidil Gummy | `/hair-loss/minoxidil-biotin-hair-gummy` |
| Biotin + Minoxidil Chew | `/hair-loss/minoxidil-biotin-chew` |
| Postmenopausal Hair Loss Spray | `/hair-loss/hair-growth-spray` |
| Oral Minoxidil | `/hair-loss/oral-minoxidil` |
| Minoxidil Solution | `/hair-loss/minoxidil` |
| Minoxidil Foam | `/hair-loss/minoxidil-women` |
| Latisse® | `/hair-loss/latisse` |
| Triple Threat shampoo & conditioner | `/hair-loss/shampoo-and-conditioner` |
| Full Volume shampoo & conditioner | `/hair-care/volumizing-shampoo-conditioner` |
| Biotin Builder Gummies | `/hair-loss/vitamins` |
| Triple Threat Shampoo | `/hair-loss/shampoo` |
| Triple Threat Conditioner | `/hair-loss/conditioner` |
| Full Volume Shampoo | `/hair-care/volumizing-shampoo` |
| Full Volume Conditioner | `/hair-care/volumizing-conditioner` |

### Menopause panel

| Item | Opens |
|---|---|
| Menopause | `/menopause` |
| Hot flashes, Night sweats, Sleep changes | `/g/i/pm` (intake). Not followed. |
| Hers Menopause guide | `/learn/menopause` |
| Progesterone | `/drugs/info/progesterone` |
| Estrogen | `/drugs/info/estrogen` |

### Perimenopause panel

| Item | Opens |
|---|---|
| Perimenopause | `/perimenopause` |
| Hot flashes, Night sweats, Sleep changes | `/g/i/pm` (intake). Not followed. |
| Hers Menopause guide | `/learn/menopause` |
| Progesterone | `/drugs/info/progesterone` |
| Estrogen | `/drugs/info/estrogen` |

### Labs panel

| Item | Opens |
|---|---|
| Labs | `/labs` |
| 130+ Health signals tested | `/labs/biomarkers` |
| Hers Multi-Cancer Test by Galleri® | `/labs/cancer-test` |
| Heart | `/labs/heart-health` |
| Metabolism | `/labs/metabolic-health` |
| Hormones | `/labs/hormone-health` |
| Inflammation & Stress | `/labs/inflammation-and-stress` |
| Thyroid | `/labs/thyroid-health` |
| Kidney | `/labs/kidney-health` |
| Liver | `/labs/liver-health` |
| Immune Defense | `/labs/immune-defense` |
| Nutrients | `/labs/nutrients` |
| Blood | `/labs/blood-health` |
| Start testing today (featured) | `/g/i/dg` (intake). Not followed. |

### More panel

Opened from More. Shot: [home-light-menu-more.png](screenshots/home-light-menu-more.png).

| Item | Opens |
|---|---|
| Mental Health | `/psychiatry` |
| Supplements | `/vitamins-women` |
| Sex | `/sexual-health` |
| Anxiety, Depression, See all (Mental Health) | `/psychiatry` |
| Omg Ring | `/sexual-health/couples-vibrator` |
| Roller Coaster | `/sexual-health/personal-vibrator` |
| Glide aloe vera | `/sexual-health/aloe-vera-personal-lubricant` |
| Birth control pills | `/birth-control` |
| Desire libido gummies | `/vitamins-women/libido-gummies` |
| See all (Sexual Health) | `/sexual-health` |
| Anti-aging | `/skin-care/anti-aging` |
| Acne | `/acne/acne-cream` |
| Skincare essentials, See all (Skin) | `/skin-care` |
| Desire libido pills | `/vitamins-women/libido-pills` |
| Detox gut health | `/vitamins-women/digestive-health-probiotic` |
| See all (Supplements) | `/vitamins-women` |

### Home panel extras

| Item | Opens |
|---|---|
| Wegovy® Pill | `/weight-loss/wegovy-pill` |
| Wegovy® Pen | `/weight-loss/wegovy-pen` |
| Zepbound® KwikPen® | `/weight-loss/zepbound-kwikpen` |
| Hair Vitamins + Minoxidil | `/hair-loss/minoxidil-hair-vitamin` |
| Biotin + Minoxidil Gummy | `/hair-loss/minoxidil-biotin-hair-gummy` |
| About Hers | `/about` |
| Clinical Excellence | `/about/clinical-excellence` |
| Blog | `/blog` |
| Hers benefits | `/benefits` |
| visit hims.com | `https://www.hims.com/`. Not opened. |

## Homepage body

| Control | Opens |
|---|---|
| Start your weight loss today / Find your Rx match | `/` (in-page). Not an intake. |
| Get glowing with Peptides+ / Find your fit | `/g/i/pp` (intake). Not followed. |
| Grow fuller hair | `/c/hl` (consultation). Not followed. |
| Treat menopause | `/lp/mp-start`. Not followed. |
| Get a health check | `/labs` |
| Unsure where to begin? Start here | Treatment dialog on `/`. Not submitted. |
| Get started (weight loss) | `/` |
| Wegovy® Pill, Zepbound® KwikPen®, Foundayo®, Wegovy® Pen, Wegovy® Pill Microdosing Plan, Zepbound® Vial, Ozempic® Pill | Product pages under `/weight-loss/...` |
| Ozempic® (lineup card) | `/g/i/wm`. Not followed. |
| Meet the app / Learn more (app) | `/weight-loss/app` |
| See source | The Lancet article. Not opened. |
| Get started / Learn more (Peptides+) | `/g/i/pp` (not followed), `/peptides-plus` |
| Peptide product cards | `/peptides-plus/glutathione`, `/peptides-plus/l-carnitine`, `/peptides-plus/sermorelin`, `/peptides-plus/vitamin-b12`, `/peptides-plus/nad` |
| Peptide stack cards | `/peptides-plus` |
| Get started / See if I'm eligible (hair) | `/c/hl`. Not followed. |
| Stop thinning or shedding, Regrow thicker, fuller hair, All the above | Hair quiz choices on `/`. Not submitted. |
| Previous testimonial / Next testimonial | Moves the testimonial rail. Same page. |
| Get results | `/c/hl`. Not followed. |
| Start my labs / Learn more / Explore the plan / Get the science | `/labs` |
| Meet the markers | `/labs/biomarkers` |
| Read more | Expands copy on `/`. |
| Get the guide | `/learn/menopause` |

## Treatment dialog

"Unsure where to begin? Start here" opens a dialog: "Do you have a treatment in mind already?"

| Control | Opens |
|---|---|
| GLP-1 pills | Intake. Not followed. |
| GLP-1 injections | Intake. Not followed. |
| I’d like a provider recommendation | Intake. Not followed. |

The dialog was photographed and closed. No option was chosen.

## Footer

| Column | Items |
|---|---|
| Learn | `/labs`, `/weight-loss`, `/learn/menopause`, `/blog/hair`, `/blog/mental-health`, `/blog/skin`, `/drugs/compare`, `/drugs/info` |
| Tools | `/tools/bmi-calculator`, `/tools/tdee-calculator`, `/tools/calorie-deficit-calculator`, `/tools/protein-calculator`, `/tools/why-cant-i-lose-weight`, `/tools/water-intake-calculator` |
| Popular | `/weight-loss/wegovy`, `/birth-control`, `/hair-loss/latisse`, `/well-being/propranolol`, `/hair-loss/oral-minoxidil`, `/hair-loss/minoxidil-biotin-chew`, `/drug/valacyclovir-herpes`, `/psychiatry/bupropion`, `/psychiatry/escitalopram`, `/skin-care/anti-aging` |
| Hers | `/about`, `/blog`, `/about/how-it-works`, `/editorial-standards`, `https://support.hims.com/hc/en-us` (not opened), `https://investors.forhims.com/` (not opened) |
| Careers | `/careers-professionals`, `/careers-providers` |
| Connect | `https://support.forhims.com/hc/en-us` (not opened), `https://news.hims.com/` (not opened) |

Fine print: `/terms-and-conditions`, `/privacy-policy`, `/telehealth-consent`, `/sitemap.html`, `/consumer-health-data-privacy-policy`. Social links (Facebook, Twitter, Instagram, TikTok) and `https://www.hims.com/` were not opened. LegitScript was not opened.

## Phone

At 390px the same header controls remain: wordmark, Log in, Slide Menu Toggle. Shot of the homepage only: [home-light-mobile.png](screenshots/home-light-mobile.png).
