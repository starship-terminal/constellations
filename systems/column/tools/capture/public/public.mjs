// Captures Column's public pages. Never types, never submits, never clicks OAuth.
//
//   RAW=~/.design-systems/column/raw-shots PLAYWRIGHT=... node public.mjs [page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Cookie banner is hidden, never accepted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'column', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function hideCookie(p) {
  await p.evaluate(() => {
    for (const el of document.querySelectorAll('div, section, aside')) {
      const t = el.innerText || '';
      if (/cookie/i.test(t) && /accept/i.test(t) && el.getBoundingClientRect().height > 30 && el.getBoundingClientRect().height < 280) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h, 12000); y += 700) {
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
    await hideCookie(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    await hideCookie(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function openMenu(p, name) {
  const btn = p.getByRole('button', { name, exact: true }).first();
  if (!(await btn.count())) return false;
  await btn.click({ force: true });
  await wait(p, 500);
  return (await btn.getAttribute('aria-expanded')) === 'true';
}

const desktop = {
  home: { path: 'https://column.com/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    if (await openMenu(p, 'Products')) { await S.view('products-menu'); await p.keyboard.press('Escape'); await wait(p, 250); }
    if (await openMenu(p, 'Developers')) { await S.view('developers-menu'); await p.keyboard.press('Escape'); await wait(p, 250); }
    if (await openMenu(p, 'Get started')) { await S.view('get-started-menu'); await p.keyboard.press('Escape'); }
  } },
  ach: { path: 'https://column.com/ach/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  contact: { path: 'https://column.com/contact/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  company: { path: 'https://column.com/company/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: 'https://column.com/blog/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  careers: { path: 'https://column.com/careers/', run: async (p, S) => { await S.view('default'); } },
  docs: { path: 'https://docs.column.com/', run: async (p, S) => {
    await S.view('default');
    const search = p.getByRole('button', { name: /^Search/ }).first();
    if (await search.count()) {
      await search.click();
      await wait(p, 700);
      await S.view('search-open');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    }
    const theme = p.getByRole('button', { name: 'Toggle theme' }).first();
    if (await theme.count()) {
      await theme.click();
      await wait(p, 600);
      await S.view('theme-toggled');
      await theme.click().catch(() => {});
      await wait(p, 300);
    }
  } },
  login: { path: 'https://dashboard.column.com/login', run: async (p, S) => {
    // Boundary only. Do not type, submit, or click OAuth / passkey / create.
    await S.view('wall');
  } },
};

const mobile = {
  home: { path: 'https://column.com/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    const menu = p.getByRole('button', { name: 'Open menu' });
    if (await menu.count()) {
      await menu.click();
      await wait(p, 600);
      await S.view('menu-open');
    }
  } },
  contact: { path: 'https://column.com/contact/', run: async (p, S) => { await S.view('default'); } },
  docs: { path: 'https://docs.column.com/', run: async (p, S) => { await S.view('default'); } },
  login: { path: 'https://dashboard.column.com/login', run: async (p, S) => { await S.view('wall'); } },
};

const browser = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.path, { waitUntil: 'load', timeout: 90000 });
    await wait(p, 1800);
    await hideCookie(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, '->', RAW);
await browser.close();
