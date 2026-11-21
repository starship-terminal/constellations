// Captures webflow.com's public pages into RAW (full-colour PNGs). quantize.py
// turns them into screenshots/.
//
//   RAW=~/.design-systems/webflow/raw-shots PLAYWRIGHT=... node public.mjs [name,name]
//
// Names are {page}-{theme}-{state}.png. Mobile names get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Full pages cap at 8 tiles.
// Nothing is submitted. Login, signup, Google, and Apple are never clicked.
// Dark mode is a public nav control (html.u-mode-dark). Cookie overlays are
// hidden, never posted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'webflow', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const AUTH = /webflow\.com\/(login|signup|dashboard)(\/|$|\?)/i;

async function hideConsent(p) {
  // Hide only the consent card. Never click Accept all or Reject all (those POST).
  // Match the smallest box that holds the card text. A wide parent also contains
  // that text, and hiding it blanks the page.
  await p.evaluate(() => {
    const hits = [];
    for (const el of document.querySelectorAll('div, aside, section')) {
      const t = el.innerText || '';
      if (!/Accept all/i.test(t) || !/cookie/i.test(t)) continue;
      const r = el.getBoundingClientRect();
      if (r.width < 200 || r.height < 70 || r.width > 460 || r.height > 360) continue;
      hits.push({ el, area: r.width * r.height });
    }
    hits.sort((a, b) => a.area - b.area);
    if (hits[0]) hits[0].el.style.setProperty('display', 'none', 'important');
  }).catch(() => {});
}

async function setTheme(p, theme) {
  if (theme !== 'dark') return;
  await p.evaluate(() => {
    document.documentElement.classList.add('u-mode-dark');
    try { localStorage.setItem('darkMode', 'true'); } catch { /* private mode */ }
  });
  await wait(p, 400);
}

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = 8 * 14000;
  for (let y = 0; y < Math.min(h, cap); y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
    h = await p.evaluate(() => document.documentElement.scrollHeight);
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
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, animations: 'disabled' }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideConsent(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`)) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, animations: 'disabled' }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, animations: 'disabled', clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openDropdown(p, id) {
  const btn = p.locator(`[aria-controls="${id}"]`).first();
  await btn.click({ timeout: 5000 });
  await wait(p, 500);
}

async function openPhoneMenu(p) {
  const btn = p.locator('.w-nav-button').first();
  await btn.click({ timeout: 5000 });
  await wait(p, 600);
}

function pages(theme) {
  return {
    home: { path: '/', run: async (p, S) => {
      await S.view('default');
      await step('platform-menu', async () => { await openDropdown(p, 'dropdown_content_0'); await S.view('platform-menu'); await p.keyboard.press('Escape'); await wait(p, 200); });
      await step('solutions-menu', async () => { await openDropdown(p, 'dropdown_content_1'); await S.view('solutions-menu'); await p.keyboard.press('Escape'); await wait(p, 200); });
      await step('resources-menu', async () => { await openDropdown(p, 'dropdown_content_2'); await S.view('resources-menu'); await p.keyboard.press('Escape'); await wait(p, 200); });
      await step('role-menu', async () => {
        const role = p.locator('[role="button"]').filter({ hasText: /^marketing teams$/i }).first();
        if (await role.count()) { await role.click({ timeout: 4000 }); await wait(p, 400); await S.view('role-menu'); await p.keyboard.press('Escape'); }
      });
      await step('dialog', async () => {
        const b = p.locator('button[aria-label="Open Dialog"]').nth(3);
        await b.evaluate((el) => el.click());
        await wait(p, 700);
        await S.view('dialog');
        await p.keyboard.press('Escape');
      });
      await step('cta-hover', async () => {
        const cta = p.getByRole('link', { name: /Start for free|Get started/i }).first();
        if (await cta.count()) { await cta.hover(); await wait(p, 300); await S.view('cta-hover'); }
      });
      await S.full();
    } },
    pricing: { path: '/pricing', run: async (p, S) => {
      await S.view('default');
      await step('yearly', async () => {
        const t = p.locator('input[name="toggle"], [role="switch"]').first();
        if (await t.count()) { await t.evaluate((el) => el.click()); await wait(p, 500); await S.view('billing-toggle'); }
      });
      await S.full();
    } },
    enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
    platform: { path: '/platform', run: async (p, S) => { await S.view('default'); await S.full(); } },
    source: { path: '/source', run: async (p, S) => { await S.view('default'); } },
    'feature-design': { path: '/feature/design', run: async (p, S) => { await S.view('default'); } },
    'feature-ai': { path: '/feature/ai', run: async (p, S) => { await S.view('default'); } },
    templates: { path: '/templates', run: async (p, S) => {
      await S.view('default');
      await step('search-focus', async () => {
        const q = p.locator('input[name="query"], input[type="search"]').first();
        if (await q.count() && await q.isVisible().catch(() => false)) {
          await q.focus();
          await wait(p, 300);
          await S.view('search-focus');
        }
      });
    } },
    blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
    customers: { path: '/customers', run: async (p, S) => { await S.view('default'); } },
    security: { path: '/security', run: async (p, S) => { await S.view('default'); } },
    accessibility: { path: '/accessibility', run: async (p, S) => { await S.view('default'); } },
    apps: { path: '/apps', run: async (p, S) => { await S.view('default'); } },
    resources: { path: '/resources', run: async (p, S) => { await S.view('default'); } },
    'contact-sales': { path: '/enterprise/contact-sales', run: async (p, S) => {
      await S.view('default');
      // Look only. Do not fill email, company, or support fields. Do not submit.
    } },
    login: { path: '/login', run: async (p, S) => {
      await S.view('wall');
      // Record the wall. Do not type. Do not click Continue with Google.
    } },
    signup: { path: '/signup', run: async (p, S) => { await S.view('wall'); } },
    legal: { path: '/legal/terms', run: async (p, S) => { await S.view('default'); } },
    about: { path: '/company/about', run: async (p, S) => { await S.view('default'); } },
    'vs-framer': { path: '/vs/framer', run: async (p, S) => { await S.view('default'); } },
    community: { path: '/community', run: async (p, S) => { await S.view('default'); } },
    'made-in-webflow': { path: '/made-in-webflow', run: async (p, S) => { await S.view('default'); } },
  };
}

function mobilePages(theme) {
  return {
    home: { path: '/', run: async (p, S) => {
      await S.view('default');
      await step('menu', async () => { await openPhoneMenu(p); await S.view('menu'); await p.keyboard.press('Escape'); });
      await S.full();
    } },
    pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
    enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); } },
    login: { path: '/login', run: async (p, S) => { await S.view('wall'); } },
    signup: { path: '/signup', run: async (p, S) => { await S.view('wall'); } },
    templates: { path: '/templates', run: async (p, S) => { await S.view('default'); } },
    blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  };
}

const browser = await chromium.launch({ headless: true });
let total = 0;
const themes = ['light', 'dark'];
const jobs = [];
for (const theme of themes) {
  for (const k of Object.keys(pages())) jobs.push({ k, theme, mob: false });
  for (const k of Object.keys(mobilePages())) jobs.push({ k, theme, mob: true });
}
for (const { k, theme, mob } of jobs) {
  const name = (mob ? 'mobile-' : '') + k + '-' + theme;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobilePages() : pages())[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript((theme) => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    if (theme === 'dark') {
      try { localStorage.setItem('darkMode', 'true'); } catch { /* ignore */ }
      document.documentElement.classList.add('u-mode-dark');
    }
  }, theme);
  const p = await ctx.newPage();
  const prefix = `${mob ? 'mobile-' : ''}${k}-${theme}`;
  const S = new Shooter(p, prefix, vw, vh, dpr);
  log('page', prefix);
  try {
    const res = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 50000 });
    await wait(p, 1800);
    await setTheme(p, theme);
    const url = p.url();
    if (k !== 'login' && k !== 'signup' && AUTH.test(url)) {
      log('  AUTH WALL', url.split('?')[0]);
      await S.view('wall');
    } else {
      const status = res && res.status();
      if (status && status >= 400) log('  status', status);
      await spec.run(p, S);
    }
  } catch (e) {
    log('  PAGE FAILED', prefix, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, '->', RAW);
await browser.close();
