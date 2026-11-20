// Public Washington Post capture. Headed Chrome: headless Chromium gets ERR_HTTP2_PROTOCOL_ERROR.
// Nothing is submitted. Sign-in, Google, Apple, and account branches are recorded and not followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium } from '/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs';
import { screenshotWithMetadata } from '../screenshot.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'washington-post', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const only = new Set((process.argv[2] || '').split(',').filter(Boolean));
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function hideOverlays(p) {
  return p.addStyleTag({ content: `
    #softwall-12170b694010-77a1b3b0, [id^="softwall-"], [class*="regiwall"], [data-testid="regiwall"] { display: none !important; }
  ` }).catch(() => {});
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full') {
    const p = this.p;
    const H0 = await p.evaluate(() => document.documentElement.scrollHeight);
    const steps = Math.min(12, Math.ceil(H0 / 700));
    for (let i = 0; i < steps; i++) {
      await p.evaluate((y) => scrollTo(0, y), i * 700);
      await wait(p, 180);
    }
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    // Playwright's fullPage path on this site returns a viewport-sized PNG once the page
    // is taller than the viewport, so every full shot is a clip tile. Tile height stays
    // under the screenshot helper's expected size.
    // clip taller than the viewport still returns a viewport PNG on this site.
    const chunk = this.vh;
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png`)) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    if (H > MAXH) log(`  ! ${name}: ${H}px, capturing first ${hCap}px`);
    if (hCap <= this.vh + 2) {
      await screenshotWithMetadata(p, { path: f + '.png' }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await p.evaluate((yy) => scrollTo(0, yy), y);
        await wait(p, 250);
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png` }, this.requested);
      }
    }
    log('  shot', this.prefix + '-' + name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const pages = [
  { id: 'home', url: 'https://www.washingtonpost.com/' },
  { id: 'politics', url: 'https://www.washingtonpost.com/politics/' },
  { id: 'opinions', url: 'https://www.washingtonpost.com/opinions/' },
  { id: 'games', url: 'https://www.washingtonpost.com/games/' },
  { id: 'elections', url: 'https://www.washingtonpost.com/elections/2026-midterms/' },
  { id: 'sports', url: 'https://www.washingtonpost.com/sports/' },
  { id: 'world', url: 'https://www.washingtonpost.com/world/' },
  { id: 'accessibility', url: 'https://www.washingtonpost.com/accessibility/' },
  { id: 'about', url: 'https://www.washingtonpost.com/about-the-post/' },
  { id: 'subscribe', url: 'https://subscribe.washingtonpost.com/acquisition/?p=s_v&s_l=ONSITE_FOOTER_DIGITAL' },
  { id: 'signin', url: 'https://www.washingtonpost.com/subscribe/signin/?next_url=https%3A%2F%2Fwww.washingtonpost.com%2F&itid=nav_sign_in', wall: true },
  { id: 'search', url: 'https://www.washingtonpost.com/search' },
  { id: 'ask', url: 'https://www.washingtonpost.com/ask-the-post-ai/' },
  { id: 'weather', url: 'https://www.washingtonpost.com/weather/' },
  { id: 'live', url: 'https://www.washingtonpost.com/washington-post-live/' },
];

async function runWidth(mob) {
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const prefix0 = mob ? 'mobile-' : '';
  const browser = await chromium.launch({ channel: 'chrome', headless: false });
  for (const spec of pages) {
    const name = prefix0 + spec.id;
    if (only.size && !only.has(name) && !only.has(spec.id)) continue;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      locale: 'en-US',
      isMobile: mob,
      hasTouch: mob,
      userAgent: mob
        ? 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
        : undefined,
    });
    const p = await ctx.newPage();
    const S = new Shooter(p, `${prefix0}${spec.id}-light`, vw, vh, dpr);
    log(name);
    try {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 50000 });
      await wait(p, 2800);
      await hideOverlays(p);
      await S.view('default');
      if (!spec.wall && spec.id !== 'signin') await S.full();
      if (!mob && spec.id === 'home') {
        await p.getByRole('button', { name: /Search and browse sections/i }).first().click();
        await wait(p, 900);
        await S.view('sections');
        await p.keyboard.press('Escape');
        await wait(p, 400);
        const alerts = p.getByRole('button', { name: /News alerts/i });
        if (await alerts.count()) {
          await alerts.first().click();
          await wait(p, 900);
          await S.view('alerts');
          await p.keyboard.press('Escape');
        }
        const search = p.locator('#query, input[name=query]').first();
        await p.getByRole('button', { name: /Search and browse sections/i }).first().click();
        await wait(p, 600);
        if (await search.count()) {
          await search.click();
          await search.fill('public');
          await wait(p, 400);
          await S.view('search-filled');
          await p.keyboard.press('Escape');
        }
        const cta = p.locator('a[data-qa="subs-offer"], a:has-text("Save and subscribe")').first();
        if (await cta.count()) {
          await cta.hover();
          await wait(p, 300);
          await S.view('subscribe-hover');
        }
      }
      if (mob && spec.id === 'home') {
        const latest = p.getByRole('button', { name: /^Latest$/ });
        if (await latest.count()) {
          await latest.first().click();
          await wait(p, 800);
          await S.view('latest');
        }
        const menu = p.getByRole('button', { name: /Search and browse sections/i });
        if (await menu.count()) {
          await menu.first().click();
          await wait(p, 800);
          await S.view('sections');
          await p.keyboard.press('Escape');
        }
      }
    } catch (e) {
      log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
    }
    await ctx.close();
  }
  await browser.close();
}

await runWidth(false);
await runWidth(true);
log('done', RAW);
