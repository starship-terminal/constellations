// Captures docusign.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Three surfaces paint
// signed out: the Next.js/Emotion marketing site on www.docusign.com (home, eSignature, the free
// trial form, the signature generator, customer stories and the company page), the plan storefront
// on ecom.docusign.com (which geo-redirects to /en-SG/ — captured as served) and the public sign-in
// page apps.docusign.com/send (which lands on account.docusign.com's OAuth form; measured, never
// filled or submitted). Everything paints light; the hero and footer sections are painted
// #26065d purple islands, not a theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x,
// `*-full` shots 1x. A page taller than one GPU texture is saved as name.partN.png tiles, which
// quantize.py stitches back together; an unbounded page truncates at 8 chunks and the log records
// the boundary. Nothing is sent, bought, signed into or submitted: the only presses are local UI
// toggles — the Products mega-menu trigger, the mobile hamburger, an FAQ accordion row, the
// Draw/Type tabs and colour swatches of the signature generator, a sample name typed into its
// name field, the Monthly billing toggle and a customer-story video's own Expand button. The
// OneTrust banner, Sierra chat, Guideflow player and the locale nudge are hidden, never answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, CY } from './lib.mjs';

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
const urlFor = (spec) => spec.path.startsWith('http') ? spec.path : BASE + spec.path;

const desktop = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('nav-products', async () => {
      const t = p.locator('nav[data-cy="navbar"] button').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first();
      // A click opens the full-width mega-menu (aria-expanded on the trigger);
      // Escape closes it again.
      if (await t.count()) { await clickEl(t); await wait(p, 1400); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  esignature: { path: '/products/electronic-signature', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const f = p.locator('button').filter({ hasText: /Is eSignature built for/i }).filter({ visible: true }).first();
      if (await f.count()) { await clickEl(f); await wait(p, 900); await S.view('faq'); }
    });
    await step('video-modal', async () => {
      const v = p.getByRole('button', { name: /Expand Customer Story Video/i }).filter({ visible: true }).first();
      if (await v.count()) { await clickEl(v); await wait(p, 2500); await S.view('modal'); await p.keyboard.press('Escape'); await wait(p, 600); }
    });
    await S.full();
  } },
  trial: { path: '/free-trial', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  signgen: { path: '/signature-generator', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('type', async () => {
      const t = p.locator('button').filter({ hasText: /^\s*Type\s*$/ }).filter({ visible: true }).first();
      if (await t.count()) {
        await clickEl(t); await wait(p, 1200);
        const f = p.locator('input#signature-name').first();
        if (await f.count()) { await f.click(); await p.keyboard.type('Alex Sample', { delay: 20 }); await wait(p, 1500); }
        await S.view('type');
      }
    });
    await S.full();
  } },
  stories: { path: '/customer-stories', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  company: { path: '/company', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  // The plan storefront geo-redirects (to /en-SG/ from this vantage); captured
  // as served. Buy Now and Contact Sales are measured, never followed.
  pricing: { path: 'https://ecom.docusign.com/plans-and-pricing/esignature', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      const t = p.locator('button').filter({ hasText: /^\s*Monthly\s*$/ }).filter({ visible: true }).first();
      if (await t.count()) { await clickEl(t); await wait(p, 1200); await S.view('monthly'); }
    });
    await S.full();
  } },
  // The public sign-in form behind "Log In" (an OAuth redirect onto
  // account.docusign.com). The landing URL carries a signed OAuth state, so the
  // sidecar records the sanitized host URL. Measured, never filled/submitted.
  login: { path: 'https://apps.docusign.com/send', wait: 9000, sanitized: 'https://account.docusign.com/oauth/auth', run: async (p, S) => {
    await S.view('default');
  } },
};

const mobile = {
  home: { path: '/', wait: 10000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      let m = p.locator('[data-cy="mobilenavhamburgermenu"] button, button[data-cy="mobilenavhamburgermenu"]').filter({ visible: true }).first();
      if (!(await m.count())) m = p.locator('nav[data-cy="navbar"] button').filter({ visible: true }).last();
      if (await m.count()) { await clickEl(m); await wait(p, 1500); await S.view('menu'); await p.keyboard.press('Escape'); }
    });
    await S.full();
  } },
  signgen: { path: '/signature-generator', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { path: 'https://ecom.docusign.com/plans-and-pricing/esignature', wait: 11000, run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = 'light';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  if (spec.sanitized) S.requested.sanitizedSourceUrl = spec.sanitized;
  try {
    if (spec.path) {
      await p.goto(urlFor(spec), { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
      await wait(p, spec.wait || 7000);
    }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
