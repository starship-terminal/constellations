// Captures getfernand.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. getfernand.com
// (Nuxt, BEM/SCSS) paints light on every route — there is no marketing theme toggle.
// app.getfernand.com is the Vue SPA: /auth/login and /create are reachable signed out and
// paint light. help.getfernand.com (the docs site, same palette) has a real "Switch to
// dark mode" link (a.switch__dark) that toggles body.dark-mode — the `dark` shots are the
// real toggled theme, not a reconstruction. Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary (/updates/ is ~44k px and tiles).
// Nothing is sent, bought or signed into: the only presses are local UI toggles — the
// hero "Install with AI" menu button, the "Watch a 2 minute demo" dialog, the Fernand
// chat-widget launcher (its own product, opened once; never typed into), the help
// search field, the help dark-mode link and the mobile menu toggle. The login and
// signup forms are measured and shot at rest, never submitted; every link is measured,
// never followed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, APP, HELP, LOGIN_URL, SIGNUP_URL } from './lib.mjs';

// Full-colour shots are working files, never committed: by default they go outside the repository,
// to ~/.design-systems/<slug>/raw-shots for a package's copy at systems/<slug>/tools/capture/public/.
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
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
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
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
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Opens the hero's "Install with AI" menu — a real aria-haspopup="menu" button
// whose items copy a setup prompt per agent (Claude, Cursor, …). A local UI
// toggle; its items are never activated.
async function aiMenu(p, S, shotName) {
  const btn = p.locator('button.ai-setup__toggle').filter({ visible: true }).first();
  if (!(await btn.count())) return;
  const expanded = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  for (let i = 0; i < 3 && !(await expanded()); i++) {
    await clickEl(btn);
    await wait(p, 700);
    if (!(await expanded())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 700); }
  }
  if (!(await expanded())) { log('  ! ai menu did not report open'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape');
  await wait(p, 400);
}

// Opens the "Watch a 2 minute demo" dialog — a local UI toggle that mounts
// .demo-modal with a YouTube-nocookie embed. The video is paused for the shot;
// nothing else in it is pressed.
async function demoModal(p, S, shotName) {
  const btn = p.locator('button.hero-demo__btn').filter({ visible: true }).first();
  if (!(await btn.count())) return;
  const open = async () => !!(await p.locator('.demo-modal__dialog').filter({ visible: true }).count());
  for (let i = 0; i < 3 && !(await open()); i++) {
    await clickEl(btn);
    await wait(p, 1200);
  }
  if (!(await open())) { log('  ! demo modal did not open'); return; }
  await p.evaluate(() => document.querySelectorAll('.demo-modal video').forEach((v) => v.pause())).catch(() => {});
  await wait(p, 400);
  await S.view(shotName);
  await p.keyboard.press('Escape');
  await wait(p, 500);
}

// Opens the Fernand chat-widget launcher — the product's own embeddable widget,
// loaded on every marketing page. The click only reveals the widget panel; no
// message is typed or sent.
async function launcher(p, S, shotName) {
  const el = p.locator('.fernand__launcher').filter({ visible: true }).first();
  if (!(await el.count())) return;
  await clickEl(el);
  await wait(p, 2500);
  const open = await p.evaluate(() => {
    const b = document.querySelector('.fernand__backdrop');
    return b && b.getBoundingClientRect().width > 200;
  }).catch(() => false);
  if (!open) { log('  ! launcher panel did not report open'); return; }
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await p.locator('.fernand__backdrop').click({ position: { x: 5, y: 5 } }).catch(() => {});
  await wait(p, 600);
}

// Types into the help search field — a local filter; the popover lists matching
// articles. The text is deleted again; nothing is sent.
async function helpSearch(p, S, shotName) {
  const f = p.locator('#search-field').filter({ visible: true }).first();
  if (!(await f.count())) return;
  await f.click();
  await p.keyboard.type('channel', { delay: 20 });
  await wait(p, 1400);
  await S.view(shotName);
  await p.keyboard.press('Escape').catch(() => {});
  await p.evaluate(() => { const c = document.querySelector('#search-close'); if (c) c.click(); }).catch(() => {});
  await wait(p, 500);
}

// Clicks the help site's real "Switch to dark mode" link (a.switch__dark) —
// the user-facing toggle that sets body.dark-mode; it persists via
// localStorage, so the same context keeps it until switched back.
async function helpDark(p, on) {
  const cur = await p.evaluate(() => document.body.classList.contains('dark-mode')).catch(() => false);
  if (cur === on) return true;
  const sw = p.locator('a.switch__dark').first();
  if (!(await sw.count())) return false;
  await clickEl(sw);
  await wait(p, 1200);
  return (await p.evaluate(() => document.body.classList.contains('dark-mode')).catch(() => false)) === on;
}

const desktop = {
  home: { url: BASE + '/', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('ai-menu', () => aiMenu(p, S, 'ai-menu'));
    await step('demo-modal', () => demoModal(p, S, 'demo-modal'));
    await step('launcher', () => launcher(p, S, 'launcher-open'));
    await S.full();
  } },
  pricing: { url: BASE + '/pricing/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { url: BASE + '/about-us/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { url: BASE + '/blog/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  updates: { url: BASE + '/updates/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'updates-article': { url: BASE + '/updates/dodo-payments-integration/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  integrations: { url: BASE + '/integrations/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'integration-slack': { url: BASE + '/integrations/slack/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'feature-ai': { url: BASE + '/feature/ai-agents/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'feature-headless': { url: BASE + '/feature/headless-customer-support/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'alternative-intercom': { url: BASE + '/alternative/intercom/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  privacy: { url: BASE + '/privacy/', wait: 6000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  signup: { url: SIGNUP_URL, wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
  } },
  help: { url: HELP + '/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('search', () => helpSearch(p, S, 'search'));
    await S.full();
  } },
  'help-article': { url: HELP + '/getting-started', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'help-dark': { url: HELP + '/getting-started', wait: 7000, theme: 'dark', run: async (p, S) => {
    if (!(await helpDark(p, true))) { log('  ! dark toggle unavailable'); return; }
    await S.view('default');
    await S.full();
    await helpDark(p, false);
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { url: BASE + '/pricing/', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  help: { url: HELP + '/getting-started', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      // The mobile menu toggle (a.menu__toggle, m--show) opens the nav panel —
      // a local UI toggle; its links are never followed.
      const t = p.locator('a.menu__toggle').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await wait(p, 900);
      await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  login: { url: LOGIN_URL, wait: 8000, theme: 'light', run: async (p, S) => {
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
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${spec.theme}`, vw, vh, dpr, spec.url);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
