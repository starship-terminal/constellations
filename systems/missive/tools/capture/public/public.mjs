// Captures Missive's public signed-out surfaces into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/missive/raw-shots \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png. Mail screens also get a dark run,
// {page}-dark-{state}.png, because mail.missiveapp.com paints
// [data-theme="dark"]. Marketing is one light theme.
// Desktop 1440x900 at 1x. Mobile 390x844 at 2x.
//
// Log in, Try for free, Book a demo and Create an account are opened by
// URL, never by submitting a form. Book a demo leaves for Calendly and is
// not followed. No password is typed. No payment, phone or government ID.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, MAIL, hideConsent, clearChallenge, patch } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'missive', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const cap = 8 * Math.floor(14000 / (p.viewportSize()?.deviceScaleFactor || 1));
  for (let y = 0; y < cap; y += 700) {
    const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    if (y >= h - 800) break;
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 140);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 300);
  await hideConsent(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = {
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      sanitizedSourceUrl: source,
    };
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
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
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
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function gotoReady(p, url) {
  await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  const ok = await clearChallenge(p);
  if (!ok) throw new Error('challenge blocked ' + url);
  await wait(p, 1600);
  await hideConsent(p);
  await p.evaluate(() => window.scrollTo(0, 0)).catch(() => {});
}

async function setMailTheme(p, theme) {
  await p.evaluate((theme) => {
    document.documentElement.setAttribute('data-theme', theme);
    try { localStorage.setItem('theme', theme); } catch {}
  }, theme);
  await wait(p, 400);
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

const desktop = {
  home: { url: BASE + '/', source: 'https://missiveapp.com/', theme: 'light', run: async (p, S) => {
    await S.view('default');
    // Product menu is hover-only. A click on the toggle opens the privacy
    // sheet, so this capture does not click it. The menu shot is taken only
    // when hover actually opens the list.
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', source: 'https://missiveapp.com/pricing', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  features: { url: BASE + '/features', source: 'https://missiveapp.com/features', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  customers: { url: BASE + '/customers', source: 'https://missiveapp.com/customers', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  download: { url: BASE + '/download', source: 'https://missiveapp.com/download', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  security: { url: BASE + '/security', source: 'https://missiveapp.com/security', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog', source: 'https://missiveapp.com/blog', theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  login: { url: MAIL + '/#login', source: 'https://mail.missiveapp.com/#login', theme: 'both', run: async (p, S, shoot) => {
    await setMailTheme(p, 'light');
    await shoot('light', 'default');
    await step('email-focused', async () => {
      await p.locator('input[type="email"]').click();
      await wait(p, 300);
      await shoot('light', 'email-focused');
    });
    await step('login-hover', async () => {
      await p.getByRole('button', { name: 'Log in', exact: true }).hover();
      await wait(p, 250);
      await shoot('light', 'login-hover');
    });
    await setMailTheme(p, 'dark');
    await shoot('dark', 'default');
  } },
  signup: { url: MAIL + '/#signup', source: 'https://mail.missiveapp.com/#signup', theme: 'both', run: async (p, S, shoot) => {
    await setMailTheme(p, 'light');
    await shoot('light', 'default');
    await setMailTheme(p, 'dark');
    await shoot('dark', 'default');
  } },
  sso: { url: MAIL + '/#sso', source: 'https://mail.missiveapp.com/#sso', theme: 'light', run: async (p, S) => {
    await setMailTheme(p, 'light');
    await S.view('default');
  } },
};

const mobile = {
  home: { url: BASE + '/', source: 'https://missiveapp.com/', theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', source: 'https://missiveapp.com/pricing', theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  login: { url: MAIL + '/#login', source: 'https://mail.missiveapp.com/#login', theme: 'light', run: async (p, S) => {
    await setMailTheme(p, 'light');
    await S.view('default');
  } },
  signup: { url: MAIL + '/#signup', source: 'https://mail.missiveapp.com/#signup', theme: 'light', run: async (p, S) => {
    await setMailTheme(p, 'light');
    await S.view('default');
  } },
};

async function runSpec(name, spec, { mob }) {
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(mob
    ? { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: 'light' }
    : { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: UA, locale: 'en-US', colorScheme: 'light' });
  await patch(context);
  const p = await context.newPage();
  const prefixBase = (mob ? 'mobile-' : '') + name;
  log(prefixBase);
  const S = new Shooter(p, `${prefixBase}-light`, vw, vh, dpr, spec.source);
  let count = 0;
  try {
    await gotoReady(p, spec.url);
    const shoot = async (theme, state) => {
      if (theme === 'dark') await setMailTheme(p, 'dark');
      const shooter = new Shooter(p, `${prefixBase}-${theme}`, vw, vh, dpr, spec.source);
      await shooter.view(state);
      count += shooter.count;
    };
    if (spec.theme === 'both') await spec.run(p, S, shoot);
    else {
      await spec.run(p, S);
      count += S.count;
    }
  } catch (e) {
    log('  PAGE FAILED', prefixBase, e.message.split('\n')[0]);
  }
  await context.close();
  await browser.close();
  return count;
}

let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false, spec: desktop[k] })),
  ...Object.keys(mobile).map((k) => ({ k, mob: true, spec: mobile[k] })),
];
for (const { k, mob, spec } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  total += await runSpec(k, spec, { mob });
}
log('done', total, 'screenshots ->', RAW);
