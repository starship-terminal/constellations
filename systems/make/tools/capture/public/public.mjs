// Captures Make's public marketing site into RAW (full-colour PNGs). quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mobile names get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. *-full shots are 1x and capped at 8 tiles.
//
// Auth walls are recorded and not entered past the first paint: /login and /register.
// No form is submitted. Cookie buttons are never clicked; OneTrust is aborted and the banner hidden.
// Sign in, Get started free, Google, Apple, SSO and captcha controls are not followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function hideConsent(page) {
  await page.addStyleTag({
    content: '#onetrust-consent-sdk,#onetrust-banner-sdk,.onetrust-pc-dark-filter{display:none!important;visibility:hidden!important;pointer-events:none!important;}',
  }).catch(() => {});
}

async function prepare(context) {
  await context.route('**/*onetrust*', (r) => r.abort());
  await context.route('**/*cookielaw*', (r) => r.abort());
  await context.route('**/*cookiepro*', (r) => r.abort());
  await context.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h && y < 12000; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await hideConsent(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
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
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function clickShadowText(page, text) {
  return page.evaluate((text) => {
    const walk = (root) => {
      const nodes = root.querySelectorAll ? [...root.querySelectorAll('button, a, [role="button"]')] : [];
      for (const el of nodes) {
        const t = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim();
        if (t === text) { el.click(); return true; }
      }
      for (const el of (root.querySelectorAll ? root.querySelectorAll('*') : [])) {
        if (el.shadowRoot) {
          const hit = walk(el.shadowRoot);
          if (hit) return true;
        }
      }
      return false;
    };
    return walk(document);
  }, text);
}

async function openFaq(page) {
  return page.evaluate(() => {
    const buttons = [...document.querySelectorAll('button[aria-expanded="false"], [role="button"][aria-expanded="false"]')];
    const b = buttons.find((el) => {
      const t = (el.innerText || '').trim();
      return t.length > 8 && !/cookie|consent|filter/i.test(t);
    });
    if (!b) return null;
    b.click();
    return (b.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80);
  });
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('product-menu', async () => {
      if (!(await clickShadowText(p, 'Product'))) throw new Error('no Product toggle');
      await wait(p, 700);
      await S.view('product-menu');
      await p.keyboard.press('Escape');
      await p.mouse.click(700, 780);
      await wait(p, 300);
    });
    await step('faq', async () => {
      const label = await openFaq(p);
      if (!label) throw new Error('no faq');
      await wait(p, 400);
      await p.evaluate(() => {
        const b = [...document.querySelectorAll('[aria-expanded="true"]')].find((el) => (el.innerText || '').length > 8);
        b?.scrollIntoView({ block: 'center' });
      });
      await wait(p, 300);
      await S.view('faq');
      log('  faq', label);
    });
    await S.full();
  } },
  product: { path: '/product', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const label = await openFaq(p);
      if (!label) throw new Error('no faq');
      await wait(p, 400);
      await p.evaluate(() => {
        const b = [...document.querySelectorAll('[aria-expanded="true"]')].find((el) => (el.innerText || '').length > 8);
        b?.scrollIntoView({ block: 'center' });
      });
      await wait(p, 300);
      await S.view('faq');
    });
    await S.full();
  } },
  integrations: { path: '/integrations', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const box = p.getByPlaceholder('Search integrations...');
      await box.click();
      await box.fill('slack');
      await wait(p, 900);
      await S.view('search');
    });
    await step('filters', async () => {
      const b = p.getByRole('button', { name: /Open filters|Category/i }).first();
      if (await b.count()) { await b.click(); await wait(p, 600); await S.view('filters'); }
      else throw new Error('no filter control');
    });
  } },
  templates: { path: '/templates', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const box = p.getByPlaceholder('Search templates...');
      await box.click();
      await box.fill('gmail');
      await wait(p, 900);
      await S.view('search');
    });
  } },
  maia: { path: '/maia', run: async (p, S) => {
    await S.view('default');
    await step('tab', async () => {
      const hit = await p.evaluate(() => {
        const b = [...document.querySelectorAll('button, [role="tab"]')].find((el) => /Learn as you build/.test(el.innerText || ''));
        if (!b) return false;
        b.click();
        return true;
      });
      if (!hit) throw new Error('no tab');
      await wait(p, 500);
      await S.view('tab');
    });
  } },
  enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  security: { path: '/security', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  'blog-post': { path: '/blog/waves26-the-glass-box-for-the-agentic-era', run: async (p, S) => {
    await S.view('default');
    await step('toc', async () => {
      const hit = await p.evaluate(() => {
        const b = [...document.querySelectorAll('button, summary, [aria-expanded]')].find((el) => /Table of contents/.test(el.innerText || ''));
        if (!b) return false;
        b.click();
        return true;
      });
      if (!hit) throw new Error('no toc');
      await wait(p, 400);
      await S.view('toc');
    });
  } },
  'success-stories': { path: '/success-stories', run: async (p, S) => { await S.view('default'); } },
  'talk-to-sales': { path: '/talk-to-sales', run: async (p, S) => { await S.view('default'); } },
  contact: { path: '/contact-us', run: async (p, S) => { await S.view('default'); } },
  partners: { path: '/partners-directory', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const box = p.getByPlaceholder('Search by partner');
      await box.click();
      await box.fill('a');
      await wait(p, 700);
      await S.view('search');
    });
  } },
  careers: { path: '/careers', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('wall'); } },
  register: { path: '/register', run: async (p, S) => { await S.view('wall'); } },
  'not-found': { path: '/this-page-is-not-a-make-route', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const opened = await pageOpenMenu(p);
      if (!opened) throw new Error('no menu');
      await wait(p, 700);
      await S.view('menu');
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  integrations: { path: '/integrations', run: async (p, S) => { await S.view('default'); } },
  product: { path: '/product', run: async (p, S) => { await S.view('default'); } },
  login: { path: '/login', run: async (p, S) => { await S.view('wall'); } },
};

async function pageOpenMenu(p) {
  const byRole = p.getByRole('button', { name: /Open menu|Menu/i });
  if (await byRole.count()) { await byRole.first().click(); return true; }
  return clickShadowText(p, 'Open menu');
}

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];
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
  });
  await prepare(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const resp = await p.goto('https://www.make.com' + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2500);
    await hideConsent(p);
    log('  status', resp?.status(), 'url', new URL(p.url()).pathname);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
