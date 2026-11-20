// Captures manychat.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// manychat.com paints a single light theme, so every shot is `-light`.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x.
// A page taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together; an unbounded page truncates at 8 chunks.
//
// The Product nav item opens its mega dropdown on click (a local UI toggle).
// The mobile hamburger opens a drawer the same way. Log in, Get started,
// Start for free and Try 14 days for free lead to app.manychat.com signup or
// sign-in: measured as links, never followed. The Usercentrics privacy layer
// is hidden, never answered. Nothing is submitted, signed into or purchased.
// The bot builder and the in-app template library sit behind sign-in.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
  const cap = Math.min(H, 8 * 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => window.scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => window.scrollTo(0, 0));
  await wait(p, 700);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++; log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else {
      const n = Math.ceil(hCap / chunk);
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({ parts: n, height: hCap, complete: false }) + '\n');
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({ parts: n, height: hCap, complete: true }) + '\n');
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 400);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function menuPainted(p) {
  return p.evaluate(() => [...document.querySelectorAll('a')].some((a) => {
    if (!/automate your instagram marketing/i.test(a.textContent || '')) return false;
    const r = a.getBoundingClientRect();
    const cs = getComputedStyle(a);
    if (!(r.height > 8 && r.width > 8 && r.top >= 0 && r.top < 700)) return false;
    if (cs.visibility === 'hidden' || cs.display === 'none' || cs.opacity === '0') return false;
    for (let n = a; n && n !== document.documentElement; n = n.parentElement) {
      const pcs = getComputedStyle(n);
      if (pcs.visibility === 'hidden' || pcs.display === 'none' || pcs.opacity === '0') return false;
    }
    return true;
  }));
}

async function menuShot(p, S) {
  await step('menu', async () => {
    const item = p.locator('nav div, nav a, nav button, header div, header a, header button').filter({ hasText: /^PRODUCT$/ }).first();
    if (!(await item.count())) { log('  menu trigger missing'); return; }
    await item.click({ timeout: 5000 }).catch(() => item.evaluate((el) => el.click()));
    let painted = false;
    for (let i = 0; i < 8; i++) {
      if (await menuPainted(p)) { painted = true; break; }
      await wait(p, 250);
    }
    if (!painted) { log('  menu did not paint; not saving home-light-menu'); return; }
    await S.view('menu');
    await p.keyboard.press('Escape').catch(() => {});
    await wait(p, 400);
  });
}

async function drawerShot(p, S) {
  await step('drawer', async () => {
    const ham = p.locator('header button[aria-label], button[aria-label*="menu" i], button[aria-label*="navigation" i]').first();
    const fallback = p.locator('header button').last();
    const btn = (await ham.count()) ? ham : fallback;
    if (!(await btn.count())) return;
    await btn.click({ timeout: 5000 }).catch(() => btn.evaluate((el) => el.click()));
    await wait(p, 900);
    await S.view('drawer');
    await p.keyboard.press('Escape').catch(() => {});
    await wait(p, 400);
  });
}

async function billingShot(p, S) {
  await step('billing', async () => {
    const hit = await p.evaluate(() => {
      document.querySelectorAll('[data-mc-bill]').forEach((n) => n.removeAttribute('data-mc-bill'));
      const text = (el) => (el.innerText || '').replace(/\s+/g, ' ').trim();
      const nodes = [...document.querySelectorAll('label, button, div, span')].filter((el) => {
        if (text(el) !== 'Monthly' && text(el) !== 'MONTHLY') return false;
        const r = el.getBoundingClientRect();
        const cs = getComputedStyle(el);
        return r.width > 8 && r.width < 220 && r.top > 40 && r.top < 500
          && cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0';
      });
      nodes.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width);
      const el = nodes[0];
      if (!el) return false;
      el.setAttribute('data-mc-bill', '1');
      return { tag: el.tagName, w: Math.round(el.getBoundingClientRect().width) };
    });
    if (!hit) { log('  monthly label missing; not saving pricing-light-monthly'); return; }
    const monthly = p.locator('[data-mc-bill="1"]').first();
    await monthly.click({ timeout: 5000 }).catch(() => monthly.evaluate((el) => el.click()));
    await wait(p, 700);
    const selected = await p.evaluate(() => {
      const el = document.querySelector('[data-mc-bill="1"]');
      if (!el) return false;
      const pressed = el.getAttribute('aria-pressed') === 'true' || el.getAttribute('aria-checked') === 'true';
      const input = el.querySelector('input') || (el.htmlFor && document.getElementById(el.htmlFor));
      return pressed || !!(input && input.checked) || /selected|active|current/i.test(el.className || '');
    });
    if (!selected) log('  monthly click did not report selected; saving the post-click frame anyway');
    await S.view('monthly');
  });
}

const desktop = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await menuShot(p, S);
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await billingShot(p, S);
    await S.full();
  } },
  instagram: { path: '/product/instagram', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'how-to': { path: '/resources/how-to', wait: 4500, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await drawerShot(p, S);
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 4500, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const b = await chromium.launch() /* automation is not hidden: a bot check is a boundary, not bypassed */;
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const target = BASE + spec.path;
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr, target);
  try {
    await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', target); await ctx.close(); continue; }
    await wait(p, spec.wait || 4000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
