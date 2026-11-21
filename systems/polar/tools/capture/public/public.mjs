// Captures Polar's public pages into RAW (full-colour PNGs). quantize.py
// turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x.
// Marketing pages paint dark. Docs paint light until the theme button is
// clicked. Filenames use the theme the page actually paints.
//
// Nothing is typed. No form is submitted. No identity provider is clicked.
// No checkout is started. Sign in and Get Started are opened only far
// enough to photograph the empty wall, then closed.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'polar', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

async function patch(context) {
  await context.addInitScript(() => {
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

async function hideCookie(page) {
  await page.evaluate(() => {
    for (const x of document.querySelectorAll('div, section, aside, [role="dialog"]')) {
      const t = x.innerText || '';
      const r = x.getBoundingClientRect();
      const cs = getComputedStyle(x);
      const overlay = (cs.position === 'fixed' || cs.position === 'sticky')
        && r.width > 80 && r.height > 40 && r.height < innerHeight * 0.7
        && /cookie|we value your privacy|consent|accept all/i.test(t)
        && !/sign in with/i.test(t);
      if (overlay) x.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 12000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 140);
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
  async view(name, source) {
    await hideCookie(this.p);
    this.requested.sanitizedSourceUrl = source || null;
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix + '-' + name);
  }
  async full(name = 'full', source) {
    const p = this.p;
    await hideCookie(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    this.requested.sanitizedSourceUrl = source || null;
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
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
    await wait(p, 300);
  }
}

async function openMenu(page, label) {
  const ok = await page.evaluate((label) => {
    const nav = document.querySelector('nav, header');
    if (!nav) return false;
    const walk = (el) => {
      for (const n of el.childNodes) {
        if (n.nodeType === 3 && (n.textContent || '').trim() === label) {
          const p = n.parentElement;
          if (p) { p.setAttribute('data-polar-menu', label); return true; }
        } else if (n.nodeType === 1 && walk(n)) return true;
      }
      return false;
    };
    return walk(nav);
  }, label);
  if (!ok) return false;
  await page.locator(`[data-polar-menu="${label}"]`).hover();
  await wait(page, 700);
  return true;
}

async function clickNavButton(page, name) {
  const btn = page.locator('nav button, header button').filter({ hasText: new RegExp('^' + name + '$') }).first();
  if (!(await btn.count())) return false;
  await btn.click({ timeout: 5000 });
  await wait(page, 900);
  return true;
}

const desktop = {
  home: { url: 'https://polar.sh/', theme: 'dark', source: 'https://polar.sh/', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/');
    if (await openMenu(p, 'Features')) {
      await S.view('features-menu', 'https://polar.sh/');
      await p.mouse.move(10, 700);
      await wait(p, 300);
    }
    if (await openMenu(p, 'Docs')) {
      await S.view('docs-menu', 'https://polar.sh/');
      await p.mouse.move(10, 700);
      await wait(p, 300);
    }
    if (await clickNavButton(p, 'Sign in')) {
      await S.view('signin-dialog', 'https://polar.sh/');
      await p.keyboard.press('Escape');
      await wait(p, 400);
    }
    await S.full('full', 'https://polar.sh/');
  } },
  pricing: { url: 'https://polar.sh/resources/pricing', theme: 'dark', source: 'https://polar.sh/resources/pricing', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/resources/pricing');
    await S.full('full', 'https://polar.sh/resources/pricing');
  } },
  docs: { url: 'https://polar.sh/docs/introduction', theme: 'light', source: 'https://polar.sh/docs/introduction', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/docs/introduction');
    const themeBtn = p.getByRole('button', { name: /switch to dark theme/i }).first();
    if (await themeBtn.count()) {
      await themeBtn.click();
      await wait(p, 800);
      await S.view('dark', 'https://polar.sh/docs/introduction');
      const back = p.getByRole('button', { name: /switch to light theme/i }).first();
      if (await back.count()) { await back.click(); await wait(p, 500); }
    }
    await S.full('full', 'https://polar.sh/docs/introduction');
  } },
  blog: { url: 'https://polar.sh/blog', theme: 'dark', source: 'https://polar.sh/blog', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/blog');
    await S.full('full', 'https://polar.sh/blog');
  } },
  company: { url: 'https://polar.sh/company', theme: 'dark', source: 'https://polar.sh/company', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/company');
    await S.full('full', 'https://polar.sh/company');
  } },
  integrate: { url: 'https://polar.sh/integrate', theme: 'dark', source: 'https://polar.sh/integrate', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/integrate');
  } },
  feature: { url: 'https://polar.sh/features/usage-billing', theme: 'dark', source: 'https://polar.sh/features/usage-billing', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/features/usage-billing');
  } },
  notfound: { url: 'https://polar.sh/pricing', theme: 'light', source: 'https://polar.sh/pricing', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/pricing');
  } },
  auth: { url: 'https://polar.sh/auth', theme: 'light', source: 'https://polar.sh/auth', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/auth');
  } },
  signup: { url: 'https://polar.sh/signup', theme: 'light', source: 'https://polar.sh/signup', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/signup');
  } },
};

const mobile = {
  home: { url: 'https://polar.sh/', theme: 'dark', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/');
    const menu = p.locator('nav button, header button').filter({ hasText: /^$/ }).first();
    const buttons = p.locator('nav button, header button');
    const n = await buttons.count();
    for (let i = 0; i < n; i++) {
      const t = ((await buttons.nth(i).innerText().catch(() => '')) || '').trim();
      const aria = await buttons.nth(i).getAttribute('aria-label').catch(() => '');
      if (!t && /menu|open/i.test(aria || '')) {
        await buttons.nth(i).click().catch(() => {});
        await wait(p, 700);
        await S.view('menu-open', 'https://polar.sh/');
        await p.keyboard.press('Escape');
        break;
      }
    }
    if (n && !(await p.locator('img').count())) { /* no-op, keep lint quiet */ }
    void menu;
    await S.full('full', 'https://polar.sh/');
  } },
  pricing: { url: 'https://polar.sh/resources/pricing', theme: 'dark', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/resources/pricing');
  } },
  auth: { url: 'https://polar.sh/auth', theme: 'light', run: async (p, S) => {
    await S.view('default', 'https://polar.sh/auth');
  } },
};

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
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name, spec.theme);
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, 2200);
    await hideCookie(p);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
