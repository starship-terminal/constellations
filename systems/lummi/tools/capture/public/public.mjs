// Captures Lummi's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/lummi/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The public site paints one
// light theme (a *-dark token set exists in CSS and is not switched from any public control). Desktop
// shots are 1440x900 at 1x, mobile shots 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches. Infinite grids truncate at 8
// chunks. Nothing is submitted, downloaded, or signed into. Login and signup walls are recorded as a
// URL and that branch stops. Cookie banners are hidden, never answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lummi', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 4800);
  for (let y = 0; y < cap; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
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
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 300);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function dismissWhatsNew(p) {
  const b = p.getByRole('button', { name: 'Close', exact: true });
  if (await b.count()) { await b.first().click({ force: true }).catch(() => {}); await wait(p, 400); }
}

const view = async (p, S) => { await dismissWhatsNew(p); await closePromo(p); await S.view('default'); await S.full(); };

const desktop = {
  home: { path: '/', wait: 3500, run: async (p, S) => {
    await S.view('whats-new');
    await dismissWhatsNew(p);
    await S.view('default');
    await step('overflow', async () => {
      await p.getByRole('button', { name: 'footer-dropdown' }).click();
      await wait(p, 700);
      await S.view('overflow');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('tools', async () => {
      await p.getByRole('button', { name: 'Tools', exact: true }).click();
      await wait(p, 600);
      await S.view('tools');
      await p.keyboard.press('Escape');
      await wait(p, 250);
    });
    await step('search', async () => {
      await p.getByPlaceholder('Search or create anything!').click();
      await wait(p, 800);
      await S.view('search');
      await p.keyboard.press('Escape');
      await wait(p, 250);
    });
    await step('daily-picks', async () => {
      await p.getByRole('button', { name: 'Daily picks' }).first().click();
      await wait(p, 600);
      await S.view('daily-picks');
      await p.keyboard.press('Escape');
    });
    await step('pro-dialog', async () => {
      await p.getByRole('button', { name: 'Try Pro for free' }).click();
      await wait(p, 800);
      await S.view('pro-dialog');
      await p.getByRole('button', { name: 'Close', exact: true }).first().click().catch(() => p.keyboard.press('Escape'));
      await wait(p, 300);
    });
    await S.full();
  } },
  illustration: { path: '/illustration', run: async (p, S) => view(p, S) },
  '3d': { path: '/3d', run: async (p, S) => view(p, S) },
  photo: { path: '/photo/speaker-on-stage-8_rbc', run: async (p, S) => view(p, S) },
  'photo-illustration': { path: '/illustration/twisted-tree-on-hill-_t1fa', run: async (p, S) => view(p, S) },
  'photo-3d': { path: '/3d/stylized-blue-train-mwjip', run: async (p, S) => view(p, S) },
  creator: { path: '/creator/amino', run: async (p, S) => view(p, S) },
  creators: { path: '/creators', run: async (p, S) => view(p, S) },
  shoot: { path: '/shoot/kEvKXqN/nature-illustrations', run: async (p, S) => view(p, S) },
  collection: { path: '/collection/FZNoVl5/everyday-palette', run: async (p, S) => view(p, S) },
  search: { path: '/s/photo/thanksgiving', run: async (p, S) => view(p, S) },
  explore: { path: '/explore', run: async (p, S) => view(p, S) },
  category: { path: '/category/nature', run: async (p, S) => view(p, S) },
  daily: { path: '/daily/photo', run: async (p, S) => view(p, S) },
  pro: { path: '/pro', run: async (p, S) => view(p, S) },
  contribute: { path: '/contribute', run: async (p, S) => view(p, S) },
  developers: { path: '/developers', run: async (p, S) => view(p, S) },
  'developers-api': { path: '/developers/api', run: async (p, S) => {
    await S.view('default');
    const u = p.url();
    if (/login|auth|signup/i.test(u)) { log('  wall', u); return; }
    await S.full();
  } },
  'api-reference': { path: '/developers/api-reference', run: async (p, S) => view(p, S) },
  blog: { path: '/blog', run: async (p, S) => view(p, S) },
  'blog-articles': { path: '/blog/articles', run: async (p, S) => view(p, S) },
  'blog-article': { path: '/blog/ui-trends-2026', run: async (p, S) => view(p, S) },
  trends: { path: '/trends', run: async (p, S) => view(p, S) },
  'trend-detail': { path: '/trends/still-life-trend', run: async (p, S) => view(p, S) },
  events: { path: '/events', run: async (p, S) => view(p, S) },
  sref: { path: '/sref-codes', run: async (p, S) => view(p, S) },
  'sref-category': { path: '/sref-codes/cinematic', run: async (p, S) => view(p, S) },
  about: { path: '/about', run: async (p, S) => view(p, S) },
  custom: { path: '/custom', run: async (p, S) => view(p, S) },
  advertise: { path: '/advertise', run: async (p, S) => view(p, S) },
  love: { path: '/love-corner', run: async (p, S) => view(p, S) },
  privacy: { path: '/privacy', run: async (p, S) => view(p, S) },
  terms: { path: '/terms', run: async (p, S) => view(p, S) },
  license: { path: '/license', run: async (p, S) => view(p, S) },
  updates: { path: '/updates', run: async (p, S) => view(p, S) },
  apps: { path: '/apps', run: async (p, S) => view(p, S) },
  'apps-figma': { path: '/apps/figma', run: async (p, S) => view(p, S) },
  prompts: { path: '/image-prompt-generator', run: async (p, S) => view(p, S) },
  docs: { path: 'https://docs.lummi.ai/', absolute: true, run: async (p, S) => view(p, S) },
  es: { path: '/es', run: async (p, S) => view(p, S) },
  login: { path: '/login', run: async (p, S) => {
    await S.view('wall');
    log('  wall recorded, branch stops', p.url());
  } },
};

const mobilePages = ['home', 'illustration', '3d', 'photo', 'creator', 'explore', 'pro', 'blog', 'about', 'apps', 'login'];
const mobile = Object.fromEntries(mobilePages.map((k) => [k, { ...desktop[k], run: async (p, S) => {
  if (k === 'home') {
    await S.view('whats-new');
    await dismissWhatsNew(p);
    await S.view('default');
    await step('overflow', async () => {
      const b = p.getByRole('button', { name: 'footer-dropdown' });
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('overflow'); await p.keyboard.press('Escape'); }
    });
    await S.full();
    return;
  }
  if (k === 'login') { await S.view('wall'); return; }
  await view(p, S);
} }]));

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.absolute ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 2500);
    if (/\/login|auth\/login|accounts\.google/i.test(p.url()) && k !== 'login' && !name.endsWith('login')) {
      log('  WALL', p.url(), 'stopping branch');
      await S.view('wall');
    } else {
      await spec.run(p, S);
    }
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
