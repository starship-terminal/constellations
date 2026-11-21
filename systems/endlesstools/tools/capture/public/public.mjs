// Captures endlesstools.io's and app.endlesstools.io's public pages into RAW
// (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png; mobile ones get a `mobile-` prefix. Two
// surfaces paint signed out: the Next.js/Tailwind-v4 marketing one-pager on
// endlesstools.io and the app host's public shell (the /login card and the
// /legal/* document pages). Both paint dark only; no light theme exists.
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A
// page taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together; an unbounded page truncates at 8 chunks
// and the log records the boundary. Nothing is sent, submitted or signed
// into: the only presses are local UI toggles — the Yearly/Monthly billing
// toggle and the login card's "Log in with password" switch. The newsletter
// form and the login form were never submitted; no consent overlay was seen
// (any would be hidden, never answered).
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
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
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      // The billing toggle is a local UI switch between the same two labels;
      // flipping it never submits or buys anything. Scroll it into view first
      // so the shot shows the toggle, not whatever the page settled on.
      const t = p.locator('button').filter({ hasText: /^\s*Monthly\s*$/ }).filter({ visible: true }).first();
      if (await t.count()) {
        await t.scrollIntoViewIfNeeded();
        await clickEl(t);
        await wait(p, 800);
        await p.evaluate(() => {
          const btn = [...document.querySelectorAll('button')].find((el) => /^\s*Monthly\s*$/.test(el.innerText || ''));
          if (!btn) return;
          const y = btn.getBoundingClientRect().top + window.scrollY - 160;
          window.scrollTo(0, Math.max(0, y));
        });
        await wait(p, 600);
        await S.view('monthly');
      }
    });
    await S.full();
  } },
  login: { url: APP + '/login', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('password', async () => {
      // "Log in with password" swaps the OTP form for the password form — a
      // local toggle. The form is never filled or submitted.
      const t = p.locator('button').filter({ hasText: /Log in with password/i }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('password'); }
    });
  } },
  privacy: { url: APP + '/legal/privacy_policy', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  terms: { url: APP + '/legal/terms_of_use', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: APP + '/login', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
  privacy: { url: APP + '/legal/privacy_policy', wait: 8000, run: async (p, S) => {
    await S.view('default');
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = 'dark';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    const target = spec.url || BASE + spec.path;
    await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path || spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
