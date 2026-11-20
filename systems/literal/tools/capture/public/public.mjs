// Captures literal.club public signed-out pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     CDP=http://127.0.0.1:9339 node public.mjs [page,page,...]
//
// Attaches over CDP to a Chrome started with a throwaway profile (see lib.mjs);
// every page opens in a fresh context. A Cloudflare challenge is a boundary:
// open() throws and the page is skipped, never solved or clicked. Consent is hidden, never answered. Sign in,
// Join, Continue, Sign in with Apple, Want to read, Like and Comment are
// never activated. The email and password fields are not typed into.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { BASE, hideConsent, launchBrowser, newPage, open } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'literal', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const BOOK = '/book/the-midnight-library-mrpx0';
const PROFILE = '/kikimeower';

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 12000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 160);
    await hideConsent(p);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, theme) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.theme = theme;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await this.p.evaluate(() => scrollTo(0, 0)).catch(() => {});
    await wait(this.p, 200);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 250);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => {
      await p.locator('input[name="query"]').first().click();
      await wait(p, 400);
      await S.view('search-focused');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  explore: { path: '/explore', run: async (p, S) => { await S.view('default'); await S.full(); } },
  book: { path: BOOK, run: async (p, S) => {
    await S.view('default');
    await step('show-more', async () => {
      const b = p.locator('[class*="Collapsable_button"]').first();
      if (await b.count()) { await b.click(); await wait(p, 500); await S.view('show-more'); }
    });
    await S.full();
  } },
  profile: { path: PROFILE, run: async (p, S) => { await S.view('default'); await S.full(); } },
  signin: { path: '/signin', run: async (p, S) => { await S.view('default'); await S.full(); } },
  register: { path: '/register', run: async (p, S) => { await S.view('default'); } },
  press: { path: '/press', run: async (p, S) => { await S.view('default'); await S.full(); } },
  legal: { path: '/legal', run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { path: '/privacy-policy', run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { path: '/terms-and-conditions', run: async (p, S) => { await S.view('default'); await S.full(); } },
  supporter: { path: '/supporter', run: async (p, S) => { await S.view('default'); await S.full(); } },
  guides: { path: '/guides', run: async (p, S) => { await S.view('default'); await S.full(); } },
  developers: { path: '/developers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); } },
  app: { path: '/app', run: async (p, S) => { await S.view('default'); await S.full(); } },
  changelog: { path: '/changelog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  tracker: { path: '/book-tracker-app', run: async (p, S) => { await S.view('default'); await S.full(); } },
  club: { path: '/book-club-app', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  import: { path: '/import/goodreads', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  explore: { path: '/explore', run: async (p, S) => { await S.view('default'); await S.full(); } },
  book: { path: BOOK, run: async (p, S) => { await S.view('default'); await S.full(); } },
  profile: { path: PROFILE, run: async (p, S) => { await S.view('default'); } },
  signin: { path: '/signin', run: async (p, S) => { await S.view('default'); await S.full(); } },
  changelog: { path: '/changelog', run: async (p, S) => { await S.view('default'); } },
};

const browser = await launchBrowser();
let total = 0;

async function runSet(specs, { mobile: mob, theme }) {
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  for (const k of Object.keys(specs)) {
    const name = (mob ? 'mobile-' : '') + k + (theme === 'dark' ? '-dark' : '');
    const pageName = (mob ? 'mobile-' : '') + k;
    if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(pageName) && !pageArg.includes(k)) continue;
    const spec = specs[k];
    const page = await newPage({ browser, width: vw, height: vh, colorScheme: theme });
    log(name, theme);
    const prefix = `${(mob ? 'mobile-' : '') + k}-${theme}`;
    const S = new Shooter(page, prefix, vw, vh, dpr, theme);
    try {
      await open(page, BASE + spec.path, { wait: spec.wait || 1400 });
      await spec.run(page, S);
    } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
    total += S.count;
    await page.close().catch(() => {});
  }
}

const themes = (process.env.THEMES || 'light,dark').split(',');
for (const theme of themes) {
  await runSet(desktop, { mobile: false, theme });
  await runSet(mobile, { mobile: true, theme });
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
