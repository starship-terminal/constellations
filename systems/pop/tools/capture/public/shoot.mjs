// Public screenshots for pop.site. Writes full-colour PNGs to RAW.
//
//   PLAYWRIGHT=... node shoot.mjs [name,name,...]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Names are {page}-light-{state}.png
// with a mobile- prefix on phone shots. Claim, login, signup and the privacy
// form are never clicked or filled. FAQ expand is a same-page toggle.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'pop', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const PAGES = [
  ['home', '/'],
  ['pricing', '/pricing'],
  ['blog', '/blog'],
  ['sections', '/sections'],
  ['featured', '/featured'],
  ['press-logos', '/pressandmedia-logos'],
  ['press-mocks', '/pressandmedia-product-mocks'],
  ['terms', '/terms'],
  ['privacy', '/privacy'],
  ['myinformation', '/myinformation'],
  ['notfound', '/enterprise'],
  ['article-meet', '/articles/meet-the-new-pop-site'],
  ['article-analytics', '/articles/why-pop-site-analytics-are-powerful'],
  ['article-squarespace', '/articles/pop-site-vs.-squarespace-the-best-squarespace-alternative-in-2026'],
  ['article-alerts', '/articles/introducing-the-pop-site-alerts-app-for-ios'],
  ['article-shopify', '/articles/introducing-the-new-shopify-pop-site-integration'],
  ['article-featured', '/articles/pop-site-featured-see-who-s-talking-about-pop-site'],
  ['article-subdomains', '/articles/why-pop-site-subdomains-are-better-for-your-brand-than-traditional-link-in-bio-tools'],
  ['article-themes', '/articles/introducing-animated-themes'],
  ['article-landbook', '/articles/pop-site-is-featured-in-landbook'],
  ['article-disrupt', '/articles/pop-site-is-featured-in-product-disrupt-issue-186'],
  ['article-linktree', '/articles/launch-your-personal-brand-with-pop-site-a-free-linktree-alternative'],
  ['article-squarespace-free', '/articles/use-pop-site-instead-of-squarespace-to-make-a-website-thank-us-later-(it-s-free)'],
  ['article-linktree-why', '/articles/pop-site-is-the-best-alternative-to-linktree-here-s-why'],
];

const want = new Set((process.argv[2] || '').split(',').filter(Boolean));
const log = (...a) => console.log(...a);

async function shoot(page, file, requested, opts = {}) {
  await screenshotWithMetadata(page, { path: file, ...opts }, requested);
}

async function fullPage(page, prefix, requested) {
  await page.evaluate(async () => {
    const h = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
    for (let y = 0; y < h; y += 700) {
      scrollTo(0, y);
      await new Promise((r) => setTimeout(r, 120));
    }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(400);
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const dpr = requested.deviceScaleFactor;
  const vw = requested.viewport.width;
  const chunk = Math.floor(14000 / dpr);
  const MAXH = 8 * chunk;
  const hCap = Math.min(H, MAXH);
  const f = `${RAW}/${prefix}-full`;
  if (H > MAXH) log('  ! truncated', H, 'to', hCap);
  if (hCap <= chunk) await shoot(page, f + '.png', requested, { fullPage: true });
  else {
    for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await shoot(page, `${f}.part${i}.png`, requested, {
        fullPage: true,
        clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
      });
    }
  }
  await page.evaluate(() => scrollTo(0, 0));
  log('  full H=' + H);
}

const browser = await chromium.launch({ headless: true });
let n = 0;
for (const mobile of [false, true]) {
  for (const [name, route] of PAGES) {
    const key = (mobile ? 'mobile-' : '') + name;
    if (want.size && !want.has(key) && !want.has(name)) continue;
    const vw = mobile ? 390 : 1440;
    const vh = mobile ? 844 : 900;
    const dpr = mobile ? 2 : 1;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mobile ? UA_MOBILE : UA,
      isMobile: mobile,
      hasTouch: mobile,
      locale: 'en-US',
    });
    const page = await ctx.newPage();
    const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: 'https://pop.site' + route };
    const prefix = `${key}-light`;
    log(key, route);
    try {
      const res = await page.goto('https://pop.site' + route, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await page.waitForTimeout(2200);
      log('  status', res && res.status(), 'inner', await page.evaluate(() => [innerWidth, innerHeight, devicePixelRatio]));
      await shoot(page, `${RAW}/${prefix}-default.png`, requested);
      n++;
      if (name === 'home') {
        const q = page.locator('[data-framer-name="Question"]').first();
        if (await q.count()) {
          await q.scrollIntoViewIfNeeded();
          await q.click();
          await page.waitForTimeout(700);
          await shoot(page, `${RAW}/${prefix}-faq.png`, requested);
          n++;
          await page.evaluate(() => scrollTo(0, 0));
        }
      }
      if (!mobile || ['home', 'pricing', 'blog', 'sections', 'featured', 'notfound', 'myinformation'].includes(name)) {
        await fullPage(page, prefix, requested);
        n++;
      }
    } catch (e) {
      log('  FAILED', key, e.message.split('\n')[0]);
    }
    await ctx.close();
  }
}
log('done', n, '->', RAW);
await browser.close();
