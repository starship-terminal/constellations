// Public Clearful capture. Headless Playwright only. No forms, no SSO, no sign-in.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node shoot.mjs [name,name,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Full pages are 1x and truncated
// at 8 GPU chunks. Raw PNGs land in ~/.design-systems/clearful/raw-shots.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'clearful', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1';

const MARKETING = [
  ['home', 'https://clearful.com/'],
  ['library', 'https://clearful.com/library'],
  ['journal-prompts', 'https://clearful.com/journal-prompts'],
  ['whats-new', 'https://clearful.com/whats-new'],
  ['flow-editor', 'https://clearful.com/flow-editor'],
  ['widgets', 'https://clearful.com/apple-widgets-for-ios'],
  ['about', 'https://clearful.com/about-us'],
  ['press', 'https://clearful.com/press-and-media'],
  ['pro', 'https://clearful.com/pro'],
  ['pricing', 'https://clearful.com/pricing'],
  ['contact', 'https://clearful.com/contact-us'],
  ['privacy', 'https://clearful.com/privacy-policy'],
  ['terms', 'https://clearful.com/terms-of-service'],
  ['new-home', 'https://clearful.com/new-home'],
  ['app-support', 'https://clearful.com/app-support'],
];

const LIBRARY_SAMPLES = [
  ['library-couples', 'https://clearful.com/library/journal-prompts-for-couples'],
  ['library-reflective', 'https://clearful.com/library/reflective-journal-prompts'],
];
const PROMPT_SAMPLE = ['prompt-anxiety', 'https://clearful.com/journal-prompts/anxiety-journal-prompts'];
const POST_SAMPLE = ['post-types', 'https://clearful.com/post/types-of-journals-exploring-the-different-types-of-journaling'];
const SUPPORT = [
  ['support', 'https://support.clearful.com/'],
  ['support-popular', 'https://support.clearful.com/popular'],
  ['support-help', 'https://support.clearful.com/help'],
  ['support-article', 'https://support.clearful.com/help/getting-started/using-clearful'],
];

async function hideConsent(p) {
  await p.evaluate(() => {
    for (const el of document.querySelectorAll('[class*="cookie"], [id*="cookie"], [class*="consent"], #onetrust-banner-sdk')) {
      el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

async function openGetApp(p) {
  const trigger = p.locator('a.button.w-button, a.button-primary-filled').filter({ hasText: /Start a journal|Start journaling/ }).first();
  await trigger.click();
  await p.locator('.modal_get-app').waitFor({ state: 'visible', timeout: 8000 });
  await wait(p, 500);
}

async function closeGetApp(p) {
  const close = p.locator('.modal_get-app_close-button').first();
  if (await close.count()) {
    await close.click();
    await wait(p, 400);
  }
}

async function openMobileMenu(p) {
  const btn = p.locator('.w-nav-button').first();
  await btn.click();
  await wait(p, 600);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = {
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      sanitizedSourceUrl: source,
    };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
    const startH = await p.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < Math.min(startH, 12000); y += 700) {
      await p.evaluate((yy) => scrollTo(0, yy), y);
      await wait(p, 120);
    }
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function runPage(browser, spec, mobile) {
  const [key, url] = spec;
  const prefix = (mobile ? 'mobile-' : '') + key;
  if (pageArg.length && !pageArg.includes(prefix) && !pageArg.includes(key)) return;
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: false,
    hasTouch: mobile,
    locale: 'en-US',
  });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const page = await context.newPage();
  page.setDefaultTimeout(20000);
  log('PAGE', prefix, url);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await wait(page, 1400);
    await hideConsent(page);
    const S = new Shooter(page, prefix, vw, vh, dpr, url.split('#')[0]);
    await S.view('default');
    if (!mobile) await S.full();
    if (key === 'home') {
      await openGetApp(page);
      await S.view('get-app');
      await closeGetApp(page);
      if (mobile) {
        await openMobileMenu(page);
        await S.view('menu-open');
      } else {
        // timeline tabs: click Monthly without leaving the page
        const monthly = page.locator('a.w-tab-link', { hasText: 'Monthly' }).first();
        if (await monthly.count()) {
          await monthly.click();
          await wait(page, 500);
          await S.view('timeline-monthly');
        }
      }
    }
    if (key === 'whats-new' && !mobile) {
      const tab = page.locator('a.w-tab-link', { hasText: 'New Features' }).first();
      if (await tab.count()) {
        await tab.click();
        await wait(page, 500);
        await S.view('tab-features');
      }
    }
    if (key === 'support' && !mobile) {
      const search = page.getByRole('button', { name: /Search for an answer/ }).first();
      if (await search.count()) {
        await search.click();
        await wait(page, 600);
        await S.view('search-open');
        await page.keyboard.press('Escape');
      }
    }
  } catch (e) {
    log('  FAILED', prefix, String(e.message).split('\n')[0]);
  } finally {
    await context.close();
  }
}

async function runSignIn(browser, mobile) {
  const prefix = (mobile ? 'mobile-' : '') + 'sign-in';
  if (pageArg.length && !pageArg.includes(prefix)) return;
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const url = 'https://app.clearful.com/#/sign-in';
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mobile ? UA_MOBILE : UA,
    isMobile: false,
    hasTouch: mobile,
    locale: 'en-US',
  });
  await context.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const page = await context.newPage();
  log('PAGE', prefix, url);
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForTimeout(3500);
    const measured = await page.evaluate(() => ({
      innerWidth: window.innerWidth,
      innerHeight: window.innerHeight,
      dpr: window.devicePixelRatio,
    }));
    log('  viewport', JSON.stringify(measured));
    // app.clearful.com ignores deviceScaleFactor and always paints at 2x.
    // A clip at the CSS viewport keeps the PNG at 2 * 390 x 2 * 844.
    if (mobile && measured.dpr === 1) {
      await screenshotWithMetadata(page, {
        path: `${RAW}/${prefix}-wall.png`,
        clip: { x: 0, y: 0, width: vw, height: vh },
        scale: 'device',
      }, {
        viewport: { width: vw, height: vh },
        deviceScaleFactor: 2,
        sanitizedSourceUrl: 'https://app.clearful.com/#/sign-in',
      });
      log('  shot', prefix + '-wall (clipped, host dpr ignored)');
    } else {
      const S = new Shooter(page, prefix, vw, vh, dpr, 'https://app.clearful.com/#/sign-in');
      await S.view('wall');
    }
  } catch (e) {
    log('  FAILED', prefix, String(e.message).split('\n')[0]);
  } finally {
    await context.close();
  }
}

const browser = await chromium.launch({ headless: true });
const all = [...MARKETING, ...LIBRARY_SAMPLES, PROMPT_SAMPLE, POST_SAMPLE, ...SUPPORT];
for (const spec of all) await runPage(browser, spec, false);
for (const spec of [['home', 'https://clearful.com/'], ['library', 'https://clearful.com/library'], ['pricing', 'https://clearful.com/pricing'], ['contact', 'https://clearful.com/contact-us'], ['support', 'https://support.clearful.com/']]) {
  await runPage(browser, spec, true);
}
await runSignIn(browser, false);
await runSignIn(browser, true);
await browser.close();
log('done', RAW);
