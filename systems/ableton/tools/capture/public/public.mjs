// Captures ableton.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. One theme (light).
// Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU
// texture is saved as name.partN.png tiles, which quantize.py stitches back together.
// Nothing is sent, bought, downloaded or signed into. Presses are local UI only: the More disclosure,
// the phone Menu, in-page FAQ and gallery controls, and one video dialog that is closed again.
// The cookie bar is hidden, never answered. Login and register are shot at rest as the auth boundary
// (no credentials, no submit). Add-to-cart, downloads, newsletter, language and country are never followed.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, killGeo, clearChallenge, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

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
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    // Bound unbounded catalogues (Packs lists hundreds of cards). Eight chunks is the kit cap.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    if (H > MAXH) log('  truncated', name, 'H=' + H, 'kept=' + hCap);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const rest = async (p, S) => { await S.view('default'); await S.full(); };

const desktop = {
  home: { path: '/en/', run: async (p, S) => {
    // The consent bar is hidden by the pre-tour sweep; un-hide it for one
    // documented shot of the component as rendered, then hide it again.
    await p.evaluate(() => { const el = document.querySelector('#biscuits-overlay'); if (el) el.style.display = ''; });
    await wait(p, 400);
    await S.raw('cookie-banner');
    await p.evaluate(() => { const el = document.querySelector('#biscuits-overlay'); if (el) el.style.display = 'none'; });
    await S.view('default');
    await step('more-menu', async () => {
      const more = p.locator('.js-main-nav-more-button').first();
      if (await more.count()) { await more.click(); await wait(p, 900); await S.view('more-menu'); await more.click(); await wait(p, 400); }
    });
    await S.full();
  } },
  live: { path: '/en/live/', run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const faq = p.locator('a.nav-button-link, button.nav-button-link').first();
      if (await faq.count()) {
        await faq.scrollIntoViewIfNeeded();
        await faq.click();
        await wait(p, 500);
        await S.view('faq-open');
        await faq.click().catch(() => {});
        await wait(p, 300);
      }
    });
    await step('video-dialog', async () => {
      const play = p.locator('.js-preview-play, .js-video-modal-open, button[class*="preview"]').first();
      if (await play.count()) {
        await play.click();
        await wait(p, 900);
        await S.view('video-dialog');
        const close = p.locator('.js-video-modal-close, .js-close-button').first();
        if (await close.count()) await close.click().catch(() => {});
        await wait(p, 300);
      }
    });
    await S.full();
  } },
  push: { path: '/en/push/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  move: { path: '/en/move/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  note: { path: '/en/note/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  link: { path: '/en/link/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  packs: { path: '/en/packs/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  shop: { path: '/en/shop/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  trial: { path: '/en/trial/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  blog: { path: '/en/blog/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  about: { path: '/en/about/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  help: { path: '/en/help/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  jobs: { path: '/en/jobs/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  login: { path: '/en/login/', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  register: { path: '/en/register/', run: async (p, S) => {
    // Same document as login. Shot at rest to record the password wall. Nothing typed, nothing submitted.
    await S.view('default');
    await S.full();
  } },
  classroom: { path: '/en/classroom/', run: rest },
  colleges: { path: '/en/colleges-universities/', run: rest },
  training: { path: '/en/certified-training/', run: rest },
  apprenticeships: { path: '/en/ausbildung/', run: rest },
  contact: { path: '/en/contact-us/', run: rest },
  press: { path: '/en/press/', run: rest },
  legal: { path: '/en/legal/', run: rest },
  privacy: { path: '/en/privacy/', run: rest },
  imprint: { path: '/en/imprint/', run: rest },
  corporate: { path: '/en/corporate-information/', run: rest },
  cookies: { path: '/en/cookie-settings/', run: rest },
  'one-thing': { path: '/en/one-thing/', run: rest },
  'user-groups': { path: '/en/community/user-groups/', run: rest },
  certification: { path: '/en/education/certification-program/', run: rest },
  events: { path: '/en/events/', run: rest },
  'shop-live': { path: '/en/shop/live/', run: rest },
  'shop-education': { path: '/en/shop/education/', run: rest },
  'help-live': { path: '/en/help/live/', run: rest },
  'blog-post': { path: '/en/blog/live-13-is-coming/', run: rest },
  'compare-editions': { path: '/en/live/compare-editions/', run: rest },
  newsletter: { path: '/en/subscribe-to-newsletter/', run: rest },
};

const mobilePages = [
  'home', 'live', 'push', 'move', 'note', 'link', 'shop', 'packs', 'help', 'trial',
  'blog', 'about', 'jobs', 'login', 'classroom', 'contact', 'legal', 'one-thing', 'events',
];

async function openPhoneMenu(p, S) {
  await S.view('default');
  await step('phone-menu', async () => {
    const trigger = p.locator('.js-main-nav-trigger').first();
    if (await trigger.count()) {
      await trigger.click();
      await wait(p, 700);
      await S.view('menu-open');
      await trigger.click().catch(() => {});
      await wait(p, 300);
    }
  });
  await S.full();
}

const mobile = Object.fromEntries(mobilePages.map((k) => [k, {
  path: desktop[k].path,
  run: k === 'home' ? openPhoneMenu : async (p, S) => { await S.view('default'); await S.full(); },
}]));

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    let ok = false;
    for (let attempt = 0; attempt < 3 && !ok; attempt++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) break;
      let clean = true;
      for (let i = 0; i < 6; i++) {
        await wait(p, 1200);
        if (await p.evaluate(() => /something went wrong|^not found$/i.test(document.body.innerText.trim())).catch(() => false)) { clean = false; break; }
      }
      ok = clean;
    }
    if (!ok) { log('  BLOCKED challenge-or-error', spec.path); await ctx.close(); continue; }
    await killGeo(p);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
