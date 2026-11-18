// Captures krea.ai's public signed-out pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-dark-{state}.png. The painted theme is html.dark, so the
// filename theme is dark even where a marketing page shares the app shell.
// Desktop shots are 1440x900 at 1x, mobile shots 390x844 at 2x, *-full shots
// 1x. A page taller than one GPU texture is tiled; an unbounded page
// truncates at 8 chunks.
//
// Nothing is signed into, submitted or purchased. Sign in, Sign up, Log in,
// Continue with Google/Apple/SSO/Email, Book a call and checkout CTAs are
// never clicked. Consent overlays are hidden, never answered. The only
// presses are local UI toggles: sidebar, Tools menu, pricing interval, FAQ,
// mobile nav.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) { console.error('set RAW=<scratch dir>'); process.exit(2); }
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  // Marketing routes scroll #root-scroll-container, not the document. Wheel
  // and scroll that node so later sections mount, then expand it so a
  // full-page screenshot includes them.
  let last = 0;
  for (let i = 0; i < 30; i++) {
    const h = await p.evaluate(() => {
      const el = document.getElementById('root-scroll-container') || document.scrollingElement;
      el.scrollTop = el.scrollHeight;
      return el.scrollHeight;
    });
    await p.mouse.wheel(0, 900);
    await wait(p, 160);
    if (h === last && i > 6) break;
    last = h;
    if (h > 8 * 14000) break;
  }
  await p.evaluate(() => {
    const el = document.getElementById('root-scroll-container');
    if (!el) return;
    const h = el.scrollHeight;
    el.style.setProperty('height', h + 'px', 'important');
    el.style.setProperty('max-height', 'none', 'important');
    el.style.setProperty('overflow', 'visible', 'important');
    document.documentElement.style.setProperty('height', 'auto', 'important');
    document.body.style.setProperty('height', 'auto', 'important');
    window.scrollTo(0, 0);
  });
  await wait(p, 400);
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const opts = (extra) => ({ path: extra, scale: 'css' });
    if (hCap <= chunk) await screenshotWithMetadata(p, { ...opts(f + '.png'), fullPage: true }, this.requested);
    else {
      const n = Math.ceil(hCap / chunk);
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({ parts: n, height: hCap, complete: false }) + '\n');
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { ...opts(`${f}.part${i}.png`), fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
      fs.writeFileSync(`${f}.parts.json`, JSON.stringify({ parts: n, height: hCap, complete: true }) + '\n');
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

const desktop = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('tools-menu', async () => {
      const b = p.getByRole('button', { name: 'Tools', exact: true }).first();
      if (!(await b.count())) return;
      await b.click();
      await wait(p, 800);
      await S.view('tools-menu');
      await p.keyboard.press('Escape');
      await wait(p, 400);
    });
    await step('sidebar', async () => {
      const b = p.getByRole('button', { name: 'Toggle Sidebar' }).first();
      if (!(await b.count())) return;
      await b.click();
      await wait(p, 700);
      await S.view('sidebar-folded');
      await b.click();
      await wait(p, 400);
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      const b = p.getByRole('button', { name: /^Monthly$/ }).first();
      if (await b.count()) { await b.click(); await wait(p, 700); await S.view('monthly'); }
    });
    await S.full();
  } },
  enterprise: { path: '/enterprise', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { path: '/blog', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  plugins: { path: '/plugins', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  mcp: { path: '/mcp', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  features: { path: '/features/ai-image-generator', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', wait: 3000, run: async (p, S) => { await S.view('default'); } },
  image: { path: '/image', wait: 4500, run: async (p, S) => { await S.view('default'); } },
  notfound: { path: '/about', wait: 2500, run: async (p, S) => { await S.view('default'); } },
  docs: { path: '/docs', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { path: '/terms', wait: 3000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('nav', async () => {
      const b = p.getByRole('button', { name: /menu|sidebar|navigation/i }).first();
      if (!(await b.count())) return;
      await b.click();
      await wait(p, 700);
      await S.view('nav');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 4500, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { path: '/login', wait: 3000, run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = 'dark';
  // krea.ai forces window.devicePixelRatio to 1, so a 2x context writes a
  // 780px PNG that the screenshot helper rejects. Mobile shots stay 1x.
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh }, deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: 'dark',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const target = BASE + spec.path;
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, target);
  try {
    await p.goto(target, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED', target); await ctx.close(); continue; }
    await wait(p, spec.wait || 4000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
