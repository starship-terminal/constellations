// Captures Sonarworks public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Nothing is submitted. CookieScript and
// GetSiteControl are removed from the DOM, never clicked. Login, signup, Facebook, Google
// and Apple are not followed. Email fields are not typed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideOverlays } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'sonarworks', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < h; y += 700) {
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
    await hideOverlays(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await hideOverlays(p);
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
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function hoverMenu(p, S) {
  await p.locator('[data-menu="company-top-navigation"]').hover({ force: true });
  await wait(p, 400);
  await S.view('company-menu');
}

async function hoverProduct(p, S) {
  await p.locator('a[data-navigation="soundid-reference-navigation"]').first().hover({ force: true });
  await wait(p, 500);
  await S.view('product-menu');
}

async function openMobile(p, S) {
  await p.locator('#menu-open-button').click({ force: true });
  await wait(p, 500);
  await S.view('menu');
}

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => { await S.view('default'); await hoverMenu(p, S); await hoverProduct(p, S); await S.full(); } },
  reference: { url: BASE + '/soundid-reference', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'reference-multichannel': { url: BASE + '/soundid-reference/multichannel', run: async (p, S) => { await S.view('default'); } },
  'vm-pro': { url: BASE + '/soundid-vm-pro', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'virtual-monitoring': { url: BASE + '/soundid-vm-pro/virtual-monitoring', run: async (p, S) => { await S.view('default'); } },
  voiceai: { url: BASE + '/soundid-produce/voiceai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'preset-catalog': { url: BASE + '/soundid-produce/voiceai/preset-catalog', run: async (p, S) => { await S.view('default'); } },
  soundid: { url: BASE + '/soundid', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'enabled-devices': { url: BASE + '/soundid/enabled-devices', run: async (p, S) => { await S.view('default'); } },
  headphones: { url: BASE + '/soundid/supported-headphones', run: async (p, S) => { await S.view('default'); } },
  android: { url: BASE + '/soundid/android', run: async (p, S) => { await S.view('default'); } },
  integrations: { url: BASE + '/soundid-reference/integrations', run: async (p, S) => { await S.view('default'); } },
  oria: { url: BASE + '/soundid-reference/integrations/audient-oria-mini', run: async (p, S) => { await S.view('default'); } },
  dolby: { url: BASE + '/soundid-reference/tools/dolby-atmos-personalization', run: async (p, S) => { await S.view('default'); } },
  ebooks: { url: BASE + '/soundid-reference/ebooks', run: async (p, S) => { await S.view('default'); } },
  upgrades: { url: BASE + '/soundid-reference/upgrades', run: async (p, S) => { await S.view('default'); } },
  'download-mac': { url: BASE + '/soundid-reference/download/mac', run: async (p, S) => { await S.view('default'); } },
  'download-center': { url: BASE + '/download-center', run: async (p, S) => { await S.view('default'); await S.full(); } },
  pricing: { url: BASE + '/soundid-reference/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  reviews: { url: BASE + '/reviews', run: async (p, S) => { await S.view('default'); } },
  blog: { url: BASE + '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  company: { url: BASE + '/company', run: async (p, S) => { await S.view('default'); } },
  careers: { url: BASE + '/company/careers', run: async (p, S) => { await S.view('default'); } },
  'media-kit': { url: BASE + '/company/media-kit', run: async (p, S) => { await S.view('default'); } },
  contacts: { url: BASE + '/company/contacts', run: async (p, S) => { await S.view('default'); } },
  licensing: { url: BASE + '/licensing', run: async (p, S) => { await S.view('default'); } },
  affiliate: { url: BASE + '/affiliate-program', run: async (p, S) => { await S.view('default'); } },
  withdrawal: { url: BASE + '/withdrawal', run: async (p, S) => { await S.view('default'); } },
  legal: { url: BASE + '/legal', run: async (p, S) => { await S.view('default'); } },
  privacy: { url: BASE + '/legal/privacy', run: async (p, S) => { await S.view('default'); } },
  cookies: { url: BASE + '/legal/cookies-policy', run: async (p, S) => { await S.view('default'); } },
  'brand-assets': { url: BASE + '/soundid-reference/brand-assets', run: async (p, S) => { await S.view('default'); } },
  login: { url: BASE + '/account/login', run: async (p, S) => { await S.view('wall'); } },
  store: { url: 'https://store.sonarworks.com/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  cart: { url: 'https://store.sonarworks.com/cart', run: async (p, S) => { await S.view('default'); } },
  'store-headphones': { url: 'https://store.sonarworks.com/collections/individually-calibrated-headphones', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => { await S.view('default'); await openMobile(p, S); await S.full(); } },
  reference: { url: BASE + '/soundid-reference', run: async (p, S) => { await S.view('default'); await openMobile(p, S); } },
  'vm-pro': { url: BASE + '/soundid-vm-pro', run: async (p, S) => { await S.view('default'); } },
  voiceai: { url: BASE + '/soundid-produce/voiceai', run: async (p, S) => { await S.view('default'); } },
  soundid: { url: BASE + '/soundid', run: async (p, S) => { await S.view('default'); } },
  pricing: { url: BASE + '/soundid-reference/pricing', run: async (p, S) => { await S.view('default'); } },
  'download-center': { url: BASE + '/download-center', run: async (p, S) => { await S.view('default'); } },
  blog: { url: BASE + '/blog', run: async (p, S) => { await S.view('default'); } },
  company: { url: BASE + '/company', run: async (p, S) => { await S.view('default'); } },
  contacts: { url: BASE + '/company/contacts', run: async (p, S) => { await S.view('default'); } },
  legal: { url: BASE + '/legal', run: async (p, S) => { await S.view('default'); } },
  login: { url: BASE + '/account/login', run: async (p, S) => { await S.view('wall'); } },
  store: { url: 'https://store.sonarworks.com/', run: async (p, S) => { await S.view('default'); } },
  cart: { url: 'https://store.sonarworks.com/cart', run: async (p, S) => { await S.view('default'); } },
  reviews: { url: BASE + '/reviews', run: async (p, S) => { await S.view('default'); } },
  integrations: { url: BASE + '/soundid-reference/integrations', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.route('**/*cookie-script.com/**', (route) => route.abort());
  await ctx.route('**/*getsitecontrol.com/**', (route) => route.abort());
  const p = await ctx.newPage();
  log(name, spec.url);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const resp = await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 1600);
    await hideOverlays(p);
    const finalUrl = p.url().split('?')[0];
    log('  status', resp && resp.status(), 'landed', finalUrl);
    if (resp && resp.status() >= 400) { log('  SKIP status'); await ctx.close(); continue; }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
