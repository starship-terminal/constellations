// Public screenshots for Stable Audio. Full-colour PNGs go to RAW, never the repo.
// Cookie banner is hidden, never clicked. No form is submitted. Auth branches are
// not opened. Names are {page}-dark-{state}.png; phone shots use a mobile- prefix.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node shoot.mjs [name,name]
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'stable-audio', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const only = new Set((process.argv[2] || '').split(',').filter(Boolean));
const log = (...a) => console.log(...a);

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const HIDE = '#onetrust-consent-sdk,#onetrust-banner-sdk,.onetrust-pc-dark-filter{display:none!important;visibility:hidden!important;pointer-events:none!important}';

async function hideConsent(page) {
  await page.addStyleTag({ content: HIDE }).catch(() => {});
}

async function lazyScroll(page) {
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) {
    await page.evaluate((yy) => scrollTo(0, yy), y);
    await page.waitForTimeout(160);
  }
  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(350);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.page = page;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
  }
  async view(name) {
    await hideConsent(this.page);
    await screenshotWithMetadata(this.page, { path: path.join(RAW, `${this.prefix}-${name}.png`) }, this.requested);
    log('  shot', `${this.prefix}-${name}`);
  }
  async full(name = 'full') {
    await hideConsent(this.page);
    await lazyScroll(this.page);
    const H = await this.page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const hCap = Math.min(H, 8 * chunk);
    if (H > hCap) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    const f = path.join(RAW, `${this.prefix}-${name}`);
    if (hCap <= chunk) await screenshotWithMetadata(this.page, { path: `${f}.png`, fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(this.page, {
          path: `${f}.part${i}.png`, fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    log('  shot', `${this.prefix}-${name}`, 'H=' + H);
    await this.page.evaluate(() => scrollTo(0, 0));
  }
}

const jobs = [
  { name: 'home', url: 'https://stableaudio.com/', run: async (page, S) => {
    await S.view('default');
    await page.getByRole('button', { name: 'Presets' }).first().click();
    await page.waitForTimeout(400);
    await S.view('presets');
    await page.keyboard.press('Escape');
    await page.waitForTimeout(200);
    await page.locator('button.HeroMadLib_word__CogYq').first().hover();
    await page.waitForTimeout(200);
    await S.view('word-hover');
    await page.getByRole('button', { name: 'Roll the dice' }).first().click();
    await page.waitForTimeout(450);
    await S.view('rolled');
    await page.getByRole('button', { name: 'Help' }).first().click();
    await page.waitForTimeout(350);
    await S.view('help');
    const done = page.getByRole('button', { name: 'Done' }).first();
    if (await done.count()) await done.click();
    await page.getByRole('button', { name: 'Make my mix' }).first().click();
    await page.waitForTimeout(500);
    await S.view('signup-dialog');
    const notNow = page.getByRole('button', { name: 'Not now' });
    if (await notNow.count()) await notNow.first().click();
    await page.waitForTimeout(250);
    const faq = page.locator('summary.HomeFaq_question__y2yCc').first();
    await faq.scrollIntoViewIfNeeded();
    await faq.click();
    await page.waitForTimeout(250);
    await S.view('faq-open');
    await page.evaluate(() => scrollTo(0, 0));
    await S.full();
  } },
  { name: 'plugin', url: 'https://stableaudio.com/plugin', run: async (page, S) => {
    await S.view('default');
    await page.getByRole('button', { name: 'Windows', exact: true }).first().click();
    await page.waitForTimeout(300);
    await S.view('windows');
    await S.full();
  } },
  { name: 'pricing', url: 'https://stableaudio.com/pricing', run: async (page, S) => {
    await S.view('default');
    const q = page.locator('summary').first();
    if (await q.count()) {
      await q.scrollIntoViewIfNeeded();
      await q.click();
      await page.waitForTimeout(250);
      await S.view('faq-open');
    }
    await page.evaluate(() => scrollTo(0, 0));
    await S.full();
  } },
  { name: 'guide', url: 'https://stableaudio.com/guide', run: async (page, S) => { await S.view('default'); await S.full(); } },
  { name: 'manual', url: 'https://stableaudio.com/docs/manual', run: async (page, S) => { await S.view('default'); await S.full(); } },
  { name: 'terms', url: 'https://stableaudio.com/terms', run: async (page, S) => { await S.view('default'); await S.full(); } },
  { name: 'account', url: 'https://stableaudio.com/account', run: async (page, S) => { await S.view('default'); await S.full(); } },
  { name: 'not-found', url: 'https://stableaudio.com/blog', run: async (page, S) => { await S.view('default'); } },
];

const browser = await chromium.launch({ headless: true });
for (const mobile of [false, true]) {
  for (const job of jobs) {
    const key = (mobile ? 'mobile-' : '') + job.name;
    if (only.size && !only.has(key) && !only.has(job.name)) continue;
    if (mobile && job.name === 'not-found') continue;
    const context = await browser.newContext(mobile
      ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, userAgent: UA_MOBILE }
      : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA });
    const page = await context.newPage();
    page.setDefaultTimeout(20000);
    log('open', key);
    try {
      await page.goto(job.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await page.waitForTimeout(800);
      await hideConsent(page);
      const S = new Shooter(page, key + '-dark', mobile ? 390 : 1440, mobile ? 844 : 900, mobile ? 2 : 1);
      if (mobile && job.name === 'home') {
        await S.view('default');
        await page.getByRole('button', { name: 'Open menu' }).first().click();
        await page.waitForTimeout(400);
        await S.view('menu');
        await page.keyboard.press('Escape').catch(() => {});
        await page.waitForTimeout(200);
        await S.full();
      } else if (mobile) {
        await S.view('default');
        await S.full();
      } else {
        await job.run(page, S);
      }
    } catch (e) {
      log('  FAILED', key, String(e.message).split('\n')[0]);
    }
    await context.close();
  }
}
await browser.close();
log('raw', RAW);
