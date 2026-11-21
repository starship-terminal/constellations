// Captures Reclaim's public pages. Nothing is submitted. Login, signup,
// Google, Microsoft, Dropbox and SSO are never clicked. The Osano cookie
// banner is hidden, never answered.
//
//   PLAYWRIGHT=... node public.mjs [page,page,...]
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, closePromo, patch } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'reclaim-ai', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 120); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openMenu(p, label) {
  const t = p.locator('.header-link.w-dropdown-toggle').filter({ hasText: new RegExp('^' + label + '$') }).first();
  await t.hover({ timeout: 4000 });
  await wait(p, 500);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('product-menu', async () => { await openMenu(p, 'Product'); await S.view('product-menu'); await p.mouse.move(8, 400); });
    await step('teams-menu', async () => { await openMenu(p, 'Teams'); await S.view('teams-menu'); await p.mouse.move(8, 400); });
    await step('resources-menu', async () => { await openMenu(p, 'Resources'); await S.view('resources-menu'); await p.mouse.move(8, 400); });
    await step('faq', async () => {
      const b = p.locator('button, .faq-q').filter({ hasText: /What is Reclaim/i }).first();
      await b.scrollIntoViewIfNeeded();
      await b.click();
      await wait(p, 400);
      await S.view('faq');
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      await p.getByText('Monthly', { exact: true }).first().click();
      await wait(p, 500);
      await S.view('monthly');
    });
    await step('features', async () => {
      await p.getByText('See all features').first().click();
      await wait(p, 400);
      await S.view('features');
    });
    await step('faq', async () => {
      const b = p.locator('button').filter({ hasText: /How does Reclaim/ }).first();
      await b.scrollIntoViewIfNeeded();
      await b.click();
      await wait(p, 400);
      await S.view('faq');
    });
    await S.full();
  } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); await S.full(); } },
  enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'blog-post': { path: '/blog/10-google-calendar-issues-you-didnt-know-you-had', run: async (p, S) => { await S.view('default'); } },
  glossary: { path: '/glossary', run: async (p, S) => { await S.view('default'); } },
  search: { path: '/search', run: async (p, S) => { await S.view('default'); } },
  integrations: { path: '/integrations', run: async (p, S) => { await S.view('default'); } },
  'integration-asana': { path: '/integrations/asana', run: async (p, S) => { await S.view('default'); } },
  customers: { path: '/customers', run: async (p, S) => { await S.view('default'); } },
  'customer-story': { path: '/customers/1password', run: async (p, S) => { await S.view('default'); } },
  compare: { path: '/compare', run: async (p, S) => { await S.view('default'); } },
  'compare-clockwise': { path: '/compare/clockwise-alternative', run: async (p, S) => { await S.view('default'); } },
  features: { path: '/features/habits', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'feature-focus': { path: '/features/focus-time', run: async (p, S) => { await S.view('default'); } },
  team: { path: '/teams/engineering', run: async (p, S) => { await S.view('default'); } },
  agents: { path: '/ai-agent-library', run: async (p, S) => { await S.view('default'); } },
  'agent-detail': { path: '/ai-agent-library/adapt-workdays-automatically', run: async (p, S) => { await S.view('default'); } },
  initiative: { path: '/initiatives/company-focus-time', run: async (p, S) => { await S.view('default'); } },
  webinars: { path: '/webinars-demos', run: async (p, S) => { await S.view('default'); } },
  affiliate: { path: '/affiliate-program', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
  careers: { path: '/careers', run: async (p, S) => { await S.view('default'); } },
  security: { path: '/security', run: async (p, S) => { await S.view('default'); } },
  discount: { path: '/pricing/education-discount', run: async (p, S) => { await S.view('default'); } },
  pomodoro: { path: '/pomodoro-timer', run: async (p, S) => {
    await S.view('default');
    await step('break-tab', async () => {
      await p.getByText('Short Break', { exact: true }).first().click();
      await wait(p, 400);
      await S.view('short-break');
    });
  } },
  calculator: { path: '/meeting-cost-calculator', run: async (p, S) => { await S.view('default'); } },
  login: { path: 'https://app.reclaim.ai/login', abs: true, run: async (p, S) => { await S.view('wall'); } },
  signup: { path: 'https://app.reclaim.ai/signup', abs: true, run: async (p, S) => { await S.view('wall'); } },
  help: { path: 'https://help.reclaim.ai/en/', abs: true, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const btn = p.locator('.w-nav-button').first();
      await btn.click();
      await wait(p, 600);
      await S.view('menu');
      const product = p.locator('.mobile_nav_carrot.product').first();
      if (await product.count()) { await product.click(); await wait(p, 400); await S.view('product'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: '/contact', run: async (p, S) => { await S.view('default'); } },
  blog: { path: '/blog', run: async (p, S) => { await S.view('default'); } },
  features: { path: '/features/habits', run: async (p, S) => { await S.view('default'); } },
  login: { path: 'https://app.reclaim.ai/login', abs: true, run: async (p, S) => { await S.view('wall'); } },
  pomodoro: { path: '/pomodoro-timer', run: async (p, S) => { await S.view('default'); } },
  enterprise: { path: '/enterprise', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', reducedMotion: 'reduce' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.abs ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2200);
    await closePromo(p);
    // Stop if a public link bounced into Google / Microsoft sign-in.
    if (/accounts\.google\.com|login\.microsoftonline\.com|dropbox\.com/i.test(p.url())) {
      log('  STOP auth redirect', p.url().slice(0, 80));
      await S.view('auth-redirect');
    } else {
      await spec.run(p, S);
    }
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
