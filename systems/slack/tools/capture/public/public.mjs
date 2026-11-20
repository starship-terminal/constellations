// Captures Slack's public marketing pages.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Full pages tile at 8 chunks.
// Cookie banners are hidden, never accepted. No form is submitted. Sign-in
// and get-started are not opened here: those walls are a separate headed pass.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'slack', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 24; i++) {
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    if (h === last && i > 2) break;
    last = h;
    await p.evaluate((y) => scrollTo(0, y), Math.min(h, i * 700));
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: BASE };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

const pages = [
  ['home', '/'],
  ['pricing', '/pricing'],
  ['features', '/features'],
  ['channels', '/features/channels'],
  ['enterprise', '/enterprise'],
  ['solutions', '/solutions'],
  ['engineering', '/solutions/engineering'],
  ['resources', '/resources'],
  ['stories', '/customer-stories'],
  ['blog', '/blog'],
  ['help', '/help'],
  ['whats-new', '/whats-new'],
  ['marketplace', 'https://slack.com/marketplace'],
  ['trust', '/trust'],
  ['demo', '/demo'],
  ['downloads', '/downloads'],
  ['contact', '/contact-sales'],
  ['legal', '/legal'],
  ['accessibility', '/accessibility'],
  ['about', '/about'],
  ['templates', '/templates/gallery'],
  ['events', '/events'],
];

const external = [
  ['design', 'https://slack.design/'],
  ['developers', 'https://docs.slack.dev/'],
];

async function shootSet(mob) {
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const browser = await chromium.launch({ headless: true });
  let total = 0;
  const jobs = [...pages, ...external];
  for (const [key, urlPath] of jobs) {
    const name = (mob ? 'mobile-' : '') + key;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(key)) continue;
    const url = urlPath.startsWith('http') ? urlPath : BASE + urlPath;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA,
      isMobile: mob,
      hasTouch: mob,
      locale: 'en-US',
    });
    const p = await ctx.newPage();
    log(name, url);
    const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
    try {
      const resp = await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
      await wait(p, 2800);
      await hideConsent(p);
      const title = await p.title();
      const status = resp ? resp.status() : 0;
      if (status >= 400 || /not supported|access denied|just a moment/i.test(title)) {
        log('  SKIP', status, title);
      } else {
        await S.view('default');
        if (!mob && key === 'home') {
          await step('product-menu', async () => {
            await p.getByRole('button', { name: 'Product', exact: true }).first().click();
            await wait(p, 700);
            await S.view('product-menu');
            await p.keyboard.press('Escape');
            await wait(p, 300);
          });
          await step('solutions-menu', async () => {
            await p.getByRole('button', { name: 'Solutions', exact: true }).first().click();
            await wait(p, 700);
            await S.view('solutions-menu');
            await p.keyboard.press('Escape');
          });
          await step('resources-menu', async () => {
            await p.getByRole('button', { name: 'Resources', exact: true }).first().click();
            await wait(p, 700);
            await S.view('resources-menu');
            await p.keyboard.press('Escape');
          });
          await step('search', async () => {
            await p.locator('#nav_search_btn').click();
            await wait(p, 500);
            await S.view('search');
            await p.keyboard.press('Escape');
          });
          await step('region', async () => {
            await p.getByRole('button', { name: /Change region/i }).first().click();
            await wait(p, 700);
            await S.view('region');
            await p.keyboard.press('Escape');
          });
          await step('cta-hover', async () => {
            const cta = p.getByRole('link', { name: 'GET STARTED' }).first();
            await cta.hover();
            await wait(p, 400);
            await S.view('cta-hover');
          });
        }
        if (mob && key === 'home') {
          await step('menu', async () => {
            await p.locator('#nav_menu_btn').click();
            await wait(p, 700);
            await S.view('menu');
            await p.keyboard.press('Escape');
          });
        }
        if (key === 'pricing') {
          await step('faq', async () => {
            const q = p.getByRole('button').filter({ hasText: /what|how|free/i }).first();
            if (await q.count()) {
              await q.scrollIntoViewIfNeeded();
              await q.click();
              await wait(p, 500);
              await S.view('faq');
            }
          });
        }
        await S.full();
      }
    } catch (e) {
      log('  PAGE FAILED', name, e.message.split('\n')[0]);
    }
    total += S.count;
    await ctx.close();
  }
  await browser.close();
  return total;
}

const onlyMobile = pageArg.length && pageArg.every((n) => n.startsWith('mobile-'));
const onlyDesktop = pageArg.length && pageArg.every((n) => !n.startsWith('mobile-'));
let total = 0;
if (!onlyMobile) total += await shootSet(false);
if (!onlyDesktop) total += await shootSet(true);
log('done', total, '->', RAW);
