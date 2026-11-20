// Captures front.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs PYTHON=/path/to/python3 node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; the app shell's dark pass is {page}-dark-*.png and
// mobile shots get a `mobile-` prefix. Desktop shots are 1440x900 at 1x, mobile shots
// 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together.
//
// Nothing is sent, created or signed into. The only activations are local UI
// toggles: the header's Product/Solutions/Resources mega menus (hover/click),
// the pricing billing switch and FAQ disclosures, the mobile burger menu, and
// the help centre's own nav. The OneTrust banner and the Qualified "Quinn"
// widget are hidden (never answered); the widget is shot once when it
// auto-opens, never engaged. Sign in, Request a demo, Try for free, the auth
// forms and the demo/signup forms are screenshotted, never submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { M, closePromo, chromium, UA, UA_MOBILE, BASE, APP, HELP, DEV } from './lib.mjs';

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
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever (acuityscheduling filled
    // 111 GB once). Truncate hard and record the boundary instead.
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
// The ReadMe portal scrolls inside a container, not the document: a fullPage
// shot only paints the 900px viewport. Resize the viewport to the container's
// scrollHeight (bounded) so the article column is captured whole.
const devScroll = async (p, S) => step('full-scroll', async () => {
  const h = await p.evaluate(() => {
    let best = 0;
    for (const el of document.querySelectorAll('body *')) {
      const s = getComputedStyle(el);
      if ((s.overflowY === 'auto' || s.overflowY === 'scroll') && el.clientHeight > 200 && el.scrollHeight > el.clientHeight + 100)
        best = Math.max(best, el.scrollHeight);
    }
    return best;
  });
  if (h > 1000) {
    const H = Math.min(h + 40, 14000);
    await p.setViewportSize({ width: 1440, height: H }); await wait(p, 1200);
    await S.view('full-scroll');
    await p.setViewportSize({ width: 1440, height: 900 });
  }
});
// A header mega menu by its button label: Product | Solutions | Resources.
const menu = async (p, label, shot) => {
  const b = p.locator(`header button:has-text("${label}")`).first();
  await b.hover(); await wait(p, 900);
  if (!(await p.locator('header [class*="menu" i], header [class*="dropdown" i], header [class*="panel" i]').first().isVisible().catch(() => false))) {
    await b.click().catch(() => {}); await wait(p, 900);
  }
  await shot();
  await p.keyboard.press('Escape'); await p.mouse.move(720, 500); await wait(p, 400);
};

const desktop = {
  home: { url: BASE + '/', wait: 10000, widget: true, run: async (p, S) => {
    // The Qualified widget auto-opens on the marketing home: shot once as
    // shipped (vendor surface, never engaged), then hidden for the rest.
    await step('widget', async () => { await wait(p, 4000); await closePromo(p, { keepWidget: true }); await S.view('widget'); });
    await closePromo(p);
    await S.view('default');
    await S.full();
    await step('menu-product', () => menu(p, 'Product', () => S.view('menu-product')));
    await step('menu-solutions', () => menu(p, 'Solutions', () => S.view('menu-solutions')));
    await step('menu-resources', () => menu(p, 'Resources', () => S.view('menu-resources')));
  } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => {
    await S.view('default');
    await step('billed-monthly', async () => {
      const t = p.locator('input.peer.sr-only, [class*="billing" i] input, label:has-text("Billed") input').first();
      const wrap = p.locator('label:has-text("Billed"), :text("Billed Annually")').first();
      if (await t.count()) { await t.click({ force: true }).catch(() => {}); } else if (await wrap.count()) { await wrap.click().catch(() => {}); }
      await wait(p, 900); await S.view('billed-monthly');
      if (await t.count()) { await t.click({ force: true }).catch(() => {}); } else if (await wrap.count()) { await wrap.click().catch(() => {}); }
      await wait(p, 500);
    });
    await step('faq', async () => {
      const faq = p.locator('button', { hasText: /What is a seat\?/ }).first();
      // The FAQ section lazy-renders; bring it in via the DOM, not actionability waits.
      await faq.evaluate((el) => el.scrollIntoView({ block: 'center' })).catch(() => {});
      await wait(p, 1200); await faq.click({ timeout: 8000 }).catch(() => {}); await wait(p, 900); await S.view('faq-open');
    });
    await S.full();
  } },
  product: { url: BASE + '/product', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'product-omnichannel': { url: BASE + '/product/omnichannel-support-inbox', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'product-ai': { url: BASE + '/product/ai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'customer-service': { url: BASE + '/customer-service', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'customer-stories': { url: BASE + '/customer-stories', run: async (p, S) => { await S.view('default'); await S.full(); } },
  story: { url: BASE + '/customer-stories/uber-freight', run: async (p, S) => { await S.view('default'); await S.full(); } },
  integrations: { url: BASE + '/integrations', run: async (p, S) => { await S.view('default'); await S.full(); } },
  compare: { url: BASE + '/compare/front-vs-intercom', run: async (p, S) => { await S.view('default'); await S.full(); } },
  industry: { url: BASE + '/industries/b2b-tech', run: async (p, S) => { await S.view('default'); await S.full(); } },
  team: { url: BASE + '/teams/customer-service-support', run: async (p, S) => { await S.view('default'); await S.full(); } },
  resources: { url: BASE + '/resources', run: async (p, S) => { await S.view('default'); await S.full(); } },
  blog: { url: BASE + '/blog', run: async (p, S) => { await S.view('default'); await S.full(); } },
  article: { url: BASE + '/blog/customer-service-automation-ai', run: async (p, S) => { await S.view('default'); await S.full(); } },
  glossary: { url: BASE + '/glossary', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  reviews: { url: BASE + '/reviews', run: async (p, S) => { await S.view('default'); await S.full(); } },
  download: { url: BASE + '/download', run: async (p, S) => { await S.view('default'); await S.full(); } },
  security: { url: BASE + '/security', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'request-demo': { url: BASE + '/request-demo', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('filled', async () => {
      const f = p.locator('input[type="email"], input[name="email"]').first();
      if (await f.count()) { await f.click(); await p.keyboard.type('name@example.com', { delay: 8 }); await wait(p, 400); await S.view('filled'); await f.focus(); await p.keyboard.press('ControlOrMeta+a'); await p.keyboard.press('Backspace'); }
    });
    await S.full();
  } },
  signup: { url: BASE + '/signup', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('filled', async () => {
      const f = p.locator('input[type="email"], input[type="text"]').first();
      if (await f.count()) { await f.click(); await p.keyboard.type('name@example.com', { delay: 8 }); await wait(p, 400); await S.view('filled'); await f.focus(); await p.keyboard.press('ControlOrMeta+a'); await p.keyboard.press('Backspace'); }
    });
    await S.full();
  } },
  'whats-new': { url: BASE + '/whats-new', run: async (p, S) => { await S.view('default'); await S.full(); } },
  signin: { url: 'https://app.frontapp.com/signin', wait: 12000, run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('filled', async () => {
      const f = p.locator('input[type="email"], input[name="email"]').first();
      if (await f.count()) { await f.click(); await p.keyboard.type('name@example.com', { delay: 8 }); await wait(p, 400); await S.view('filled'); await f.focus(); await p.keyboard.press('ControlOrMeta+a'); await p.keyboard.press('Backspace'); }
    });
  } },
  'signindark': { url: 'https://app.frontapp.com/signin', dark: true, wait: 12000, theme: 'dark', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'signup-app': { url: 'https://app.frontapp.com/signup', wait: 12000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'signupappdark': { url: 'https://app.frontapp.com/signup', dark: true, wait: 12000, theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  forgot: { url: 'https://app.frontapp.com/forgot-password', wait: 12000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'forgotdark': { url: 'https://app.frontapp.com/forgot-password', dark: true, wait: 12000, theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  help: { url: HELP + '/', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'help-article': { url: HELP + '/en/', pick: 'article', wait: 9000, run: async (p, S) => {
    // The first article card the help centre lists; a reader's own click.
    const a = p.locator('a[href*="/articles/"], main a').filter({ hasText: /./ }).first();
    const href = await a.getAttribute('href').catch(() => null);
    if (href) { await p.goto(new URL(href, HELP).href, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {}); await wait(p, 6000); }
    await closePromo(p);
    await S.view('default'); await S.full();
  } },
  'help-contact': { url: HELP + '/en/contact-us', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  dev: { url: DEV + '/docs/welcome', wait: 10000, run: async (p, S) => { await S.view('default'); await S.full(); await devScroll(p, S); } },
  'dev-ref': { url: DEV + '/reference/getting-started', wait: 10000, run: async (p, S) => { await S.view('default'); await S.full(); await devScroll(p, S); } },
};

const mobile = {
  'mobile-home': { url: BASE + '/', run: async (p, S) => {
    await S.view('default'); await S.full();
    await step('menu', async () => {
      const b = p.locator('button[aria-label*="menu" i]').first();
      await b.evaluate((el) => el.scrollIntoView({ block: 'start' })).catch(() => {});
      await b.click({ timeout: 8000 }).catch(() => b.dispatchEvent('click').catch(() => {}));
      await wait(p, 1500); await S.view('menu');
      await p.keyboard.press('Escape').catch(() => {});
    });
  } },
  'mobile-pricing': { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'mobile-signin': { url: 'https://app.frontapp.com/signin', wait: 12000, run: async (p, S) => { await S.view('default'); } },
  'mobile-signindark': { url: 'https://app.frontapp.com/signin', dark: true, wait: 12000, theme: 'dark', run: async (p, S) => { await S.view('default'); } },
  'mobile-help': { url: HELP + '/', wait: 9000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', colorScheme: spec.dark ? 'dark' : 'light' });
  await ctx.addInitScript(() => {
    // no navigator.webdriver mask: removed in the 2026-11 audit (D7), not run since
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
  // The app shell reads front-theme-preference from localStorage and falls
  // back to prefers-color-scheme; set both so the dark pass is the product's
  // own switch, not an emulated paint.
  if (spec.dark) await ctx.addInitScript(() => { try { localStorage.setItem('front-theme-preference', 'dark'); } catch { /* before origin */ } });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-${spec.theme || 'light'}`, vw, vh, dpr);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await wait(p, spec.wait || 8000);
    if (spec.widget) { /* home handles it in run */ await closePromo(p, { keepWidget: true }); }
    else await closePromo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
