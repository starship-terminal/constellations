// Captures Matter's public signed-out pages into RAW (full-colour PNGs);
// quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/matter/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,...]
//
// Names are {page}-dark-{state}.png; mobile ones get a `mobile-` prefix.
// getmatter.com paints one near-black marketing theme (CSS modules, --mr-*
// tokens, MR-Camphor). Captured: the marketing home, web-extension,
// newsletters, privacy and terms; the public Words That Matter newsletter
// (words.getmatter.com) home and one published article; the public docs
// (docs.getmatter.com) home; and the web reader sign-in card at
// web.getmatter.com (measured, never submitted). Desktop shots are 1440x900
// at 1x, mobile 390x844 at 2x. A page taller than one GPU texture is saved
// as name.partN.png tiles; an unbounded page truncates at 8 chunks.
// Nothing is sent, signed into, purchased or submitted. Consent overlays
// are hidden, never clicked. Docs theme is toggled only as local UI.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
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

const desktop = {
  home: { url: BASE + '/', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'web-extension': { url: BASE + '/web-extension', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  newsletters: { url: BASE + '/newsletters', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  privacy: { url: BASE + '/privacy', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  terms: { url: BASE + '/terms', wait: 4000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  // Publication home is a subscribe gate (the page itself). Capture the gate.
  // Never press Subscribe. A public article is captured separately.
  words: { url: 'https://words.getmatter.com/', wait: 5000, run: async (p, S) => { await S.view('default'); } },
  article: { url: 'https://words.getmatter.com/p/anu-coolhunt-before-sunrise-why-i', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  // docs.getmatter.com paints light, so its files are docs-light-*; the default 'dark' prefix
  // named them docs-dark-* with a `light` state, which the committed files are not.
  docs: { url: 'https://docs.getmatter.com/', theme: 'light', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('theme', async () => {
      const b = p.getByRole('button', { name: /theme/i }).first();
      if (await b.count()) {
        await b.click();
        await wait(p, 600);
        const light = p.getByRole('menuitem', { name: /^Light$/ }).or(p.getByRole('button', { name: /^Light$/ })).or(p.getByText('Light', { exact: true })).first();
        if (await light.count()) { await light.click(); await wait(p, 800); await S.view('theme'); }
      }
    });
    await S.full();
  } },
  signin: { url: 'https://web.getmatter.com/', theme: 'light', wait: 5000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  article: { url: 'https://words.getmatter.com/p/anu-coolhunt-before-sunrise-why-i', wait: 5000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { url: 'https://docs.getmatter.com/', theme: 'light', wait: 5000, run: async (p, S) => { await S.view('default'); } },
  signin: { url: 'https://web.getmatter.com/', theme: 'light', wait: 5000, run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const theme = spec.theme || 'dark';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 4000);
    await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
