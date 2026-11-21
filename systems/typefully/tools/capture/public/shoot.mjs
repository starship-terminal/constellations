// Public Typefully screenshots. Desktop 1440x900 at 1x, phone 390x844 at 2x.
// Full-colour PNGs go to RAW (default ~/.design-systems/typefully/raw-shots).
// Nothing is submitted. Google, X, LinkedIn and Apple are never clicked.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node shoot.mjs [name,name]
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
const BASE = 'https://typefully.com';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'typefully', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
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
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function openAuth(p, S, which) {
  const btn = p.getByRole('button', { name: which, exact: true }).first();
  if (!(await btn.count())) return;
  await btn.click();
  await wait(p, 900);
  await S.view(which === 'Log in' ? 'login-dialog' : 'signup-dialog');
  await p.keyboard.press('Escape');
  await wait(p, 300);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('login', () => openAuth(p, S, 'Log in'));
    await step('signup', () => openAuth(p, S, 'Sign up'));
    await step('email', async () => {
      await p.getByRole('button', { name: 'Log in', exact: true }).first().click();
      await wait(p, 700);
      const email = p.getByRole('button', { name: 'Email', exact: true }).last();
      if (await email.count()) {
        await email.click();
        await wait(p, 600);
        await S.view('login-email');
      }
      await p.keyboard.press('Escape');
    });
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('social-set-menu', async () => {
      const row = p.locator('[aria-expanded]').filter({ hasText: /social set/i }).first();
      if (await row.count()) {
        await row.click();
        await wait(p, 500);
        await S.view('social-set-menu');
        await p.keyboard.press('Escape');
      }
    });
    await step('comparison', async () => {
      const row = p.locator('[aria-expanded="false"]').filter({ hasText: 'Publishing' }).first();
      if (await row.count()) {
        await row.scrollIntoViewIfNeeded();
        await row.click();
        await wait(p, 400);
        await S.view('comparison-open');
      }
    });
  } },
  ai: { path: '/ai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'ai-agents': { path: '/ai-agents', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'x-twitter': { path: '/x-twitter', run: async (p, S) => { await S.view('default'); await S.full(); } },
  linkedin: { path: '/linkedin', run: async (p, S) => { await S.view('default'); } },
  threads: { path: '/schedule-threads-posts', run: async (p, S) => { await S.view('default'); } },
  bluesky: { path: '/bluesky', run: async (p, S) => { await S.view('default'); } },
  'content-ideas': { path: '/content-ideas', run: async (p, S) => { await S.view('default'); } },
  analytics: { path: '/social-media-analytics', run: async (p, S) => { await S.view('default'); } },
  scheduling: { path: '/social-media-scheduling', run: async (p, S) => { await S.view('default'); } },
  profile: { path: '/profile', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'minimal-twitter': { path: '/minimal-twitter', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'blog-post': { path: '/blog/x-analytics-ai-agents', run: async (p, S) => { await S.view('default'); await S.full(); } },
  changelog: { path: '/changelog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'changelog-entry': { path: '/changelog/new-x-posts-media-limits', run: async (p, S) => { await S.view('default'); } },
  announcements: { path: '/announcements', run: async (p, S) => { await S.view('default'); } },
  academy: { path: '/academy', run: async (p, S) => { await S.view('default'); } },
  jobs: { path: '/jobs', run: async (p, S) => { await S.view('default'); await S.full(); } },
  shortcuts: { path: '/shortcuts', run: async (p, S) => { await S.view('default'); await S.full(); } },
  tools: { path: '/tools', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'tools-ai': { path: '/tools/ai', run: async (p, S) => { await S.view('default'); } },
  'fake-tweet': { path: '/tools/fake-tweet-generator', run: async (p, S) => {
    await S.view('default');
    await step('advanced', async () => {
      const b = p.getByRole('button', { name: 'Show Advanced Options' });
      if (await b.count()) { await b.click(); await wait(p, 400); await S.view('advanced'); }
    });
    await step('focused', async () => {
      const field = p.getByPlaceholder('Enter your tweet text here...');
      if (await field.count()) {
        await field.click();
        await wait(p, 300);
        await S.view('textarea-focused');
      }
    });
  } },
  counter: { path: '/tools/twitter-character-counter', run: async (p, S) => { await S.view('default'); } },
  'linkedin-preview': { path: '/tools/linkedin-post-preview', run: async (p, S) => { await S.view('default'); } },
  glossary: { path: '/social-media-glossary', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => {
      const field = p.getByPlaceholder('Search for a marketing term ...');
      if (await field.count()) { await field.click(); await wait(p, 300); await S.view('search-focused'); }
    });
  } },
  'glossary-term': { path: '/social-media-glossary/algorithm', run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs/api', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const b = p.getByRole('button', { name: /Open Search/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 600); await S.view('search'); await p.keyboard.press('Escape'); }
    });
  } },
  notfound: { path: '/login', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  tools: { path: '/tools', run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs/api', run: async (p, S) => { await S.view('default'); } },
  glossary: { path: '/social-media-glossary', run: async (p, S) => { await S.view('default'); } },
  jobs: { path: '/jobs', run: async (p, S) => { await S.view('default'); } },
  ai: { path: '/ai', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
    colorScheme: 'light',
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const res = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    log('  status', res && res.status(), 'url', new URL(p.url()).pathname);
    await wait(p, spec.wait || 1800);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
