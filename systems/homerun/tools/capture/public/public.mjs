// Captures Homerun's public marketing pages.
//
//   RAW=~/.design-systems/homerun/raw-shots PLAYWRIGHT=... node public.mjs [page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x, names prefixed mobile-.
// Does not submit forms, type credentials, or follow login walls.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideOverlays } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'homerun', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 12000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
  await hideOverlays(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: source };
    this.count = 0;
  }
  async view(name) {
    await hideOverlays(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function openDropdown(p, label) {
  const loc = p.locator('.w-dropdown-toggle').filter({ hasText: new RegExp('^' + label) }).first();
  if (!(await loc.count())) return false;
  await loc.hover();
  await wait(p, 400);
  await loc.click({ force: true }).catch(() => {});
  await wait(p, 500);
  return true;
}

async function openMenuButton(p) {
  const b = p.locator('button, .menu-button, .w-nav-button, [aria-label="menu"]').first();
  const navBtn = p.locator('.w-nav-button').first();
  if (await navBtn.count()) {
    await navBtn.click({ force: true });
    await wait(p, 700);
    return true;
  }
  return false;
}

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    if (await openDropdown(p, 'Resources')) await S.view('resources-menu');
    await p.keyboard.press('Escape').catch(() => {});
    await p.mouse.move(10, 400);
    await wait(p, 300);
    if (await openDropdown(p, 'Log in')) await S.view('login-menu');
    await p.keyboard.press('Escape').catch(() => {});
    await p.mouse.move(10, 400);
    await wait(p, 200);
    const feat = p.locator('.w-dropdown-toggle, [aria-haspopup="menu"]').filter({ hasText: 'Get an overview of your hiring process' }).first();
    if (await feat.count()) {
      await feat.scrollIntoViewIfNeeded();
      await feat.click({ force: true });
      await wait(p, 500);
      await S.view('feature-open');
    }
    const cta = p.getByRole('link', { name: 'Start free trial' }).first();
    if (await cta.count()) { await cta.hover(); await wait(p, 300); await S.view('cta-hover'); }
  } },
  ats: { url: BASE + '/ats', run: async (p, S) => { await S.view('default'); await S.full(); } },
  hr: { url: BASE + '/hr', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
    const faq = p.locator('[aria-haspopup="menu"], .w-dropdown-toggle').filter({ hasText: /free trial/i }).first();
    if (await faq.count()) { await faq.scrollIntoViewIfNeeded(); await faq.click({ force: true }); await wait(p, 400); await S.view('faq-open'); }
  } },
  customers: { url: BASE + '/customers', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'customer-story': { url: BASE + '/customer-stories/freshheads-and-homerun', run: async (p, S) => { await S.view('default'); await S.full(); } },
  partner: { url: BASE + '/partner-program', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { url: BASE + '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  article: { url: BASE + '/expertise-opinion/ai-and-candidate-fraud-a-recruiters-guide', run: async (p, S) => { await S.view('default'); await S.full(); } },
  updates: { url: BASE + '/blog/product-updates', run: async (p, S) => { await S.view('default'); await S.full(); } },
  update: { url: BASE + '/product-updates/updates-to-our-public-api', run: async (p, S) => { await S.view('default'); } },
  guides: { url: BASE + '/guides', run: async (p, S) => { await S.view('default'); await S.full(); } },
  guide: { url: BASE + '/guides/hiring-process', run: async (p, S) => { await S.view('default'); } },
  templates: { url: BASE + '/templates', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'job-descriptions': { url: BASE + '/job-description-templates', run: async (p, S) => { await S.view('default'); } },
  referral: { url: BASE + '/referral-program', run: async (p, S) => { await S.view('default'); await S.full(); } },
  integrations: { url: BASE + '/integrations', run: async (p, S) => { await S.view('default'); await S.full(); } },
  slack: { url: BASE + '/integrations/slack', run: async (p, S) => { await S.view('default'); } },
  features: { url: BASE + '/product/features', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'feature-ats': { url: BASE + '/product/applicant-tracking', run: async (p, S) => { await S.view('default'); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { url: BASE + '/contact', run: async (p, S) => { await S.view('default'); await S.full(); } },
  gdpr: { url: BASE + '/gdpr', run: async (p, S) => { await S.view('default'); } },
  terms: { url: BASE + '/terms-of-service', run: async (p, S) => { await S.view('default'); } },
  privacy: { url: BASE + '/privacy-statement', run: async (p, S) => { await S.view('default'); } },
  careers: { url: 'https://jobs.homerun.co/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  help: { url: 'https://help.homerun.co/en/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  newsletter: { url: BASE + '/artofwork/newsletter', run: async (p, S) => { await S.view('default'); } },
  missing: { url: BASE + '/this-page-does-not-exist', run: async (p, S) => { await S.view('default'); } },
  // Login wall: load, record, do not type.
  login: { url: 'https://app.homerun.co/login', run: async (p, S) => { await S.view('wall'); } },
};

const mobilePages = ['home', 'ats', 'hr', 'pricing', 'customers', 'blog', 'integrations', 'about', 'contact', 'help', 'careers', 'login'];

const b = await chromium.launch({ headless: true });
let total = 0;

async function runOne(name, spec, mob) {
  const prefix = (mob ? 'mobile-' : '') + name + '-light';
  if (pageArg.length && !pageArg.includes(mob ? 'mobile-' + name : name)) return;
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(prefix);
  const S = new Shooter(p, prefix, vw, vh, dpr, spec.url.split('?')[0]);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2500);
    await hideOverlays(p);
    if (mob && name !== 'login') {
      await S.view('default');
      await S.full();
      if (name === 'home' && await openMenuButton(p)) await S.view('menu');
    } else {
      await spec.run(p, S);
    }
  } catch (e) {
    log('  PAGE FAILED', prefix, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}

for (const k of Object.keys(desktop)) await runOne(k, desktop[k], false);
for (const k of mobilePages) await runOne(k, desktop[k], true);
log('done', total, 'screenshots ->', RAW);
await b.close();
