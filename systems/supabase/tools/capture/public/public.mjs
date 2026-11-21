// Captures Supabase's public marketing site into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x.
// Nothing is typed, submitted, or signed into. GitHub, Google, and SSO are not clicked.
// Login and signup are photographed empty, then the run stops.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, hideConsent, isWall, openPublic } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'supabase', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 140);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 350);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
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
    await wait(p, 200);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openMenu(p, label) {
  const btn = p.getByRole('button', { name: label, exact: true }).first();
  if (!(await btn.count())) { log('  menu trigger missing', label); return false; }
  await btn.click({ timeout: 4000 });
  await wait(p, 500);
  const expanded = await btn.getAttribute('aria-expanded');
  if (expanded !== 'true') log('  menu not expanded', label, expanded);
  return expanded === 'true';
}

async function themeToggle(p) {
  const b = p.getByRole('button', { name: /toggle theme/i }).first();
  if (!(await b.count())) return false;
  await b.click({ timeout: 3000 });
  await wait(p, 500);
  return true;
}

const desktop = {
  home: { url: 'https://supabase.com/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    for (const label of ['Product', 'Developers', 'Solutions']) {
      await step('menu-' + label, async () => {
        if (await openMenu(p, label) && !isWall(p.url())) await S.view('menu-' + label.toLowerCase());
        await p.keyboard.press('Escape').catch(() => {});
        await wait(p, 200);
      });
    }
    await step('theme-menu', async () => {
      if (!(await themeToggle(p))) return;
      await S.view('theme-menu');
      const light = p.getByRole('menuitem', { name: /^light$/i }).or(p.getByText(/^Light$/, { exact: true })).first();
      if (await light.count()) {
        await light.click({ timeout: 3000 });
        await wait(p, 700);
        await S.view('theme-light');
        if (await themeToggle(p)) {
          const system = p.getByText(/^System$/, { exact: true }).first();
          if (await system.count()) await system.click({ timeout: 3000 }).catch(() => {});
          await wait(p, 400);
        }
      }
    });
  } },
  pricing: { url: 'https://supabase.com/pricing', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  docs: { url: 'https://supabase.com/docs', run: async (p, S) => {
    await S.view('default');
    await step('search', async () => {
      const s = p.getByRole('button', { name: /search/i }).or(p.locator('button[aria-label*="Search" i], [data-testid*="search"]')).first();
      if (await s.count()) {
        await s.click({ timeout: 3000 });
        await wait(p, 600);
        if (!isWall(p.url())) await S.view('search');
        await p.keyboard.press('Escape').catch(() => {});
      }
    });
  } },
  database: { url: 'https://supabase.com/database', run: async (p, S) => { await S.view('default'); } },
  auth: { url: 'https://supabase.com/auth', run: async (p, S) => { await S.view('default'); } },
  features: { url: 'https://supabase.com/features', run: async (p, S) => { await S.view('default'); } },
  blog: { url: 'https://supabase.com/blog', run: async (p, S) => { await S.view('default'); } },
  customers: { url: 'https://supabase.com/customers', run: async (p, S) => { await S.view('default'); } },
  company: { url: 'https://supabase.com/company', run: async (p, S) => { await S.view('default'); } },
  security: { url: 'https://supabase.com/security', run: async (p, S) => { await S.view('default'); } },
  enterprise: { url: 'https://supabase.com/solutions/enterprise', run: async (p, S) => { await S.view('default'); } },
  brand: { url: 'https://supabase.com/brand', run: async (p, S) => { await S.view('default'); } },
  changelog: { url: 'https://supabase.com/changelog', run: async (p, S) => { await S.view('default'); } },
  support: { url: 'https://supabase.com/support', run: async (p, S) => { await S.view('default'); } },
  contact: { url: 'https://supabase.com/contact/sales', run: async (p, S) => { await S.view('default'); } },
  status: { url: 'https://status.supabase.com/', run: async (p, S) => { await S.view('default'); } },
  login: { url: 'https://supabase.com/dashboard', run: async (p, S) => {
    if (isWall(p.url()) || /sign/i.test(await p.title())) await S.view('default');
    else await S.view('default');
  } },
  signup: { url: 'https://supabase.com/dashboard/sign-up', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { url: 'https://supabase.com/', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const b = p.getByRole('button', { name: /main menu|menu/i }).first();
      if (await b.count()) {
        await b.click({ timeout: 4000 });
        await wait(p, 600);
        if (!isWall(p.url())) await S.view('menu');
      }
    });
  } },
  pricing: { url: 'https://supabase.com/pricing', run: async (p, S) => { await S.view('default'); } },
  login: { url: 'https://supabase.com/dashboard', run: async (p, S) => { await S.view('default'); } },
  signup: { url: 'https://supabase.com/dashboard/sign-up', run: async (p, S) => { await S.view('default'); } },
};

async function runSet(label, spec, contextOpts) {
  const names = pageArg.length ? pageArg.filter((n) => spec[n]) : Object.keys(spec);
  if (!names.length) return;
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext(contextOpts);
  const page = await context.newPage();
  const notes = [];
  for (const name of names) {
    const job = spec[name];
    log(label, name, job.url);
    try {
      const opened = await openPublic(page, job.url);
      notes.push({ name, ...opened, title: await page.title() });
      log('  ', opened.status, opened.url.slice(0, 120), 'wall=' + opened.wall);
      if (opened.wall && name !== 'login' && name !== 'signup') {
        log('  skip shot, unexpected wall');
        continue;
      }
      const prefix = (label === 'mobile' ? 'mobile-' : '') + name + '-dark';
      const S = new Shooter(page, prefix, contextOpts.viewport.width, contextOpts.viewport.height, contextOpts.deviceScaleFactor);
      await job.run(page, S);
    } catch (e) {
      log('  FAILED page', name, String(e.message).split('\n')[0]);
      notes.push({ name, error: String(e.message).split('\n')[0] });
    }
  }
  fs.writeFileSync(path.join(RAW, `notes-${label}.json`), JSON.stringify(notes, null, 2) + '\n');
  await browser.close();
}

await runSet('desktop', desktop, {
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
  colorScheme: 'dark',
});
await runSet('mobile', mobile, {
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  userAgent: UA_MOBILE,
  isMobile: true,
  hasTouch: true,
  locale: 'en-US',
  colorScheme: 'dark',
});
log('done', PKG);
