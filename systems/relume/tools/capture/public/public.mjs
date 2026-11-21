// Captures Relume's public pages. Full-colour PNGs go to RAW; quantize.py writes screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [name,name]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x, prefixed mobile-. Themes: light (default)
// and dark (body.p-theme-dark, switched by the public theme button, not an account setting).
// Login, signup, Google, SSO, and every form are not used. The cookie banner is hidden.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent, patch } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'relume', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 14; i++) {
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    if (h <= last + 20 && i > 0) break;
    last = h;
    for (let y = 0; y < Math.min(h, 9000); y += 700) {
      await p.evaluate((y) => scrollTo(0, y), y);
      await wait(p, 120);
    }
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    // Webflow pages report a scrollHeight the screenshot clip does not match
    // (a 1440x900 viewport PNG against an 8000px expected clip). Capture the
    // scrolled viewport instead, and record the document height in the log.
    const p = this.p;
    await hideConsent(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    await p.evaluate(() => scrollTo(0, Math.round(document.documentElement.scrollHeight * 0.45)));
    await wait(p, 400);
    await screenshotWithMetadata(p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name, 'scrolled-viewport H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function setTheme(p, theme) {
  await p.evaluate((theme) => {
    document.documentElement.setAttribute('data-theme', theme);
    document.body.classList.toggle('p-theme-dark', theme === 'dark');
  }, theme);
  await wait(p, 350);
}

async function openProducts(p) {
  const b = p.getByRole('button', { name: 'Products', exact: true }).first();
  if (await b.count()) { await b.click({ timeout: 4000 }); await wait(p, 500); return true; }
  return false;
}

const PAGES = [
  { key: 'home', path: '/', full: true, extra: async (p, S) => {
    await step('products-menu', async () => { if (await openProducts(p)) { await S.view('products-menu'); await p.keyboard.press('Escape'); } });
  } },
  { key: 'pricing', path: '/pricing', full: true, extra: async (p, S) => {
    await step('export-tab', async () => {
      const t = p.getByRole('tab', { name: 'Export pricing' }).first();
      if (await t.count()) { await t.click(); await wait(p, 500); await S.view('export-tab'); }
    });
  } },
  { key: 'publish', path: '/publish', full: true },
  { key: 'studio', path: '/studio', full: false },
  { key: 'export', path: '/export', full: true },
  { key: 'mcp', path: '/mcp', full: true },
  { key: 'components', path: '/components', full: false, extra: async (p, S) => {
    await step('preferences', async () => {
      const b = p.getByRole('button', { name: 'Preferences' }).first();
      if (await b.count()) { await b.click(); await wait(p, 500); await S.view('preferences'); await p.keyboard.press('Escape'); }
    });
  } },
  { key: 'react', path: '/react/components', full: false },
  { key: 'component', path: '/components/application-shell-1', full: false },
  { key: 'whats-new', path: '/whats-new', full: false },
  { key: 'style-guide', path: '/style-guide', full: true },
  { key: 'docs', path: '/resources/publish/docs', full: false },
  { key: 'doc', path: '/resources/publish/doc/getting-started-with-relume-publish', full: false },
  { key: 'support', path: '/support', full: false },
  { key: 'inspiration', path: '/inspiration', full: false },
  { key: 'showcase', path: '/showcase', full: false, extra: async (p, S) => {
    await step('highlights', async () => {
      const t = p.getByRole('tab', { name: 'Highlights' }).first();
      if (await t.count()) { await t.click(); await wait(p, 500); await S.view('highlights'); }
    });
  } },
  { key: 'community', path: '/community-love', full: false },
  { key: 'voting', path: '/component-voting', full: false },
  { key: 'figma', path: '/figma-library', full: false },
  { key: 'chrome', path: '/chrome-extension', full: false },
  { key: 'whitelabel', path: '/whitelabel', full: false },
  { key: 'library-mcp', path: '/library-mcp', full: false },
  { key: 'claude', path: '/claude-design-export', full: false },
  { key: 'affiliates', path: '/affiliates', full: false },
  { key: 'contact', path: '/contact-sales', full: false },
  { key: 'guides', path: '/guides', full: false },
  { key: 'legal', path: '/legal/privacy-policy', full: false },
  { key: 'login', path: '/app/login', full: false },
  { key: 'signup', path: '/app/signup', full: false },
];

async function runSet({ mobile, theme }) {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(context);
  const page = await context.newPage();
  const prefixBase = (mobile ? 'mobile-' : '') ;
  const dpr = mobile ? 2 : 1;
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  try {
    for (const spec of PAGES) {
      const name = prefixBase + spec.key + '-' + theme;
      if (pageArg.length && !pageArg.some((a) => name.includes(a) || spec.key === a)) continue;
      log('PAGE', name);
      try {
        await page.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 50000 });
        await wait(page, 2200);
        await hideConsent(page);
        if (theme === 'dark') await setTheme(page, 'dark');
        const final = page.url();
        if (/\/app\/(login|signup)/.test(final) && !/login|signup/.test(spec.key)) {
          log('  WALL', final);
          continue;
        }
        const S = new Shooter(page, name, vw, vh, dpr);
        await S.view('default');
        if (!mobile && spec.extra) await spec.extra(page, S);
        if (mobile && spec.key === 'home') {
          await step('menu', async () => {
            const b = page.getByRole('button', { name: 'Open menu' }).first();
            if (await b.count()) { await b.click(); await wait(page, 600); await S.view('menu'); }
          });
        }
        if (spec.full && !mobile) await S.full();
        if (spec.full && mobile && spec.key === 'home') await S.full();
      } catch (e) {
        log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
      }
    }
  } finally {
    await context.close();
    await browser.close();
  }
}

const want = pageArg;
const jobs = [
  { mobile: false, theme: 'light' },
  { mobile: false, theme: 'dark' },
  { mobile: true, theme: 'light' },
  { mobile: true, theme: 'dark' },
];
for (const job of jobs) {
  if (want.length) {
    const tag = (job.mobile ? 'mobile' : 'desktop') + '-' + job.theme;
    if (!want.some((a) => a === 'all' || tag.includes(a) || a === job.theme || (job.mobile && a.startsWith('mobile')) || (!job.mobile && !a.startsWith('mobile')))) {
      // still run if a page key was named
      const pageKeys = PAGES.map((p) => p.key);
      if (!want.some((a) => pageKeys.includes(a))) continue;
    }
  }
  await runSet(job);
}
log('done');
