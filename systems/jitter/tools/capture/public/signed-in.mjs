// Signed-in jitter.video capture. Persistent Chromium profile, email session.
// Never Google/SSO. Never open billing checkout, Export paid, or Invite.
//
//   PROFILE=~/.design-systems/jitter/chrome-profile \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//   node signed-in.mjs [page,page]
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, patch, closePromo } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
const PROFILE = process.env.PROFILE || path.join(os.homedir(), '.design-systems', 'jitter', 'chrome-profile');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function gateText(text) {
  const t = (text || '').toLowerCase();
  if (/verify you are human|i'm not a robot|recaptcha|hcaptcha/.test(t)) return 'captcha';
  if (/\bphone\b|\bsms\b/.test(t) && /enter your|verify your number/.test(t)) return 'phone';
  if (/card number|cvc|expiry/.test(t) && /pay|subscribe|billing/.test(t)) return 'payment';
  return null;
}

async function assertFree(page, name) {
  const body = await page.evaluate(() => (document.body && document.body.innerText) || '');
  const g = gateText(body);
  if (g) throw new Error(`${name}: STOP ${g}`);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
}

async function dismissEditorChrome(p) {
  await closePromo(p);
  for (const label of ['Close', 'Dismiss']) {
    const b = p.getByRole('button', { name: new RegExp(`^${label}$`, 'i') });
    if (await b.count()) {
      const n = await b.count();
      for (let i = 0; i < Math.min(n, 4); i++) {
        await b.nth(i).click({ timeout: 1500 }).catch(() => {});
      }
    }
  }
  await p.evaluate(() => {
    const close = [...document.querySelectorAll('button,[role="button"]')].filter((el) => {
      const t = (el.innerText || el.getAttribute('aria-label') || '').trim();
      return t === '×' || t === 'x' || t === 'X' || t.toLowerCase() === 'close';
    });
    close.slice(0, 4).forEach((el) => el.click());
  }).catch(() => {});
  await wait(p, 400);
}

async function hrefStarting(page, prefix) {
  return page.evaluate((prefix) => {
    const a = [...document.querySelectorAll('a[href]')].find((el) => (el.getAttribute('href') || '').startsWith(prefix));
    return a ? a.getAttribute('href') : null;
  }, prefix);
}

const desktop = {
  files: {
    url: '/files/', wait: 2500,
    run: async (p, S) => {
      await S.view('default');
      const search = p.getByPlaceholder(/search/i).first();
      if (await search.count()) {
        await search.click();
        await wait(p, 300);
        await S.view('search-focus');
        await p.keyboard.press('Escape').catch(() => {});
      }
      const avatar = p.locator('a[href="/account/"], button').filter({ hasText: /^K$/ }).first();
      if (await avatar.count()) {
        await avatar.click({ timeout: 4000 }).catch(() => {});
        await wait(p, 500);
        await S.view('account-menu');
        await p.keyboard.press('Escape').catch(() => {});
      }
    },
  },
  account: {
    url: '/account/', wait: 2500,
    run: async (p, S) => { await S.view('default'); },
  },
  trash: {
    url: '/trash/', wait: 2500,
    run: async (p, S) => { await S.view('default'); },
  },
  apptemplates: {
    url: '/templates/all/', wait: 3000,
    run: async (p, S) => { await S.view('default'); },
  },
  team: {
    url: '/files/', wait: 2000,
    run: async (p, S) => {
      const href = await hrefStarting(p, '/files/team/');
      if (href) {
        await p.goto(BASE + href, { waitUntil: 'domcontentloaded', timeout: 45000 });
        await wait(p, 2200);
        await closePromo(p);
      }
      await S.view('default');
    },
  },
  brandkit: {
    url: '/files/', wait: 2000,
    run: async (p, S) => {
      const href = await hrefStarting(p, '/teams/');
      const lib = await p.evaluate(() => {
        const a = [...document.querySelectorAll('a[href]')].find((el) => /\/libraries\//.test(el.getAttribute('href') || ''));
        return a ? a.getAttribute('href') : null;
      });
      const dest = lib || href;
      if (dest) {
        await p.goto(/^https?:/.test(dest) ? dest : BASE + dest, { waitUntil: 'domcontentloaded', timeout: 45000 });
        await wait(p, 2200);
        await closePromo(p);
      }
      await S.view('default');
    },
  },
  workspace: {
    url: '/files/', wait: 2000,
    run: async (p, S) => {
      const href = await p.evaluate(() => {
        const a = [...document.querySelectorAll('a[href]')].find((el) => {
          const h = el.getAttribute('href') || '';
          return /^\/teams\/\?id=/.test(h) || (/^\/teams\//.test(h) && !/libraries/.test(h));
        });
        return a ? a.getAttribute('href') : null;
      });
      if (href) {
        await p.goto(BASE + href, { waitUntil: 'domcontentloaded', timeout: 45000 });
        await wait(p, 2500);
        await closePromo(p);
      } else {
        const item = p.getByText('Workspace settings', { exact: true });
        if (await item.count()) await item.click({ force: true, timeout: 4000 }).catch(() => {});
        await wait(p, 2200);
      }
      await S.view('default');
    },
  },
  editor: {
    url: '/files/', wait: 2200,
    run: async (p, S) => {
      const create = p.getByText('Create new file', { exact: true });
      if (await create.count()) {
        await create.click({ timeout: 5000 });
        await wait(p, 4000);
      }
      await assertFree(p, 'editor');
      await S.view('promo');
      await dismissEditorChrome(p);
      await S.view('default');
      const animate = p.getByRole('button', { name: /^Animate$/i }).first();
      if (await animate.count()) {
        await animate.click({ timeout: 3000 }).catch(() => {});
        await wait(p, 800);
        await S.view('animate');
        const design = p.getByRole('button', { name: /^Design$/i }).first();
        if (await design.count()) await design.click({ timeout: 2000 }).catch(() => {});
      }
    },
  },
};

const mobile = {
  files: {
    url: '/files/', wait: 2500,
    run: async (p, S) => { await S.view('default'); },
  },
  account: {
    url: '/account/', wait: 2500,
    run: async (p, S) => { await S.view('default'); },
  },
  editor: {
    url: '/files/', wait: 2200,
    run: async (p, S) => {
      const create = p.getByText('Create new file', { exact: true });
      if (await create.count()) {
        await create.click({ timeout: 5000 });
        await wait(p, 4000);
      }
      await dismissEditorChrome(p);
      await S.view('default');
    },
  },
  trash: {
    url: '/trash/', wait: 2200,
    run: async (p, S) => { await S.view('default'); },
  },
};

const contextOpts = (mob) => mob
  ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
  : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' };

const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true })),
];

let total = 0;
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await chromium.launchPersistentContext(PROFILE, {
    headless: true,
    ...contextOpts(mob),
    args: ['--disable-blink-features=AutomationControlled'],
  });
  await patch(ctx);
  const p = ctx.pages()[0] || await ctx.newPage();
  p.setDefaultTimeout(20000);
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const u = /^https?:/.test(spec.url) ? spec.url : BASE + spec.url;
    await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 2500);
    await closePromo(p);
    await assertFree(p, name);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
