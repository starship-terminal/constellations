// Captures riverside.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x, `*-full` shots 1x. A page taller
// than one GPU texture is saved as name.partN.png tiles, which quantize.py stitches back together;
// an unbounded page truncates at 8 chunks and the log records the boundary.
// Nothing is sent, uploaded or signed into. Login, Start for Free and register are recorded as walls
// and not filled. Forms are not submitted. Cookie dialogs are hidden, never answered.
// Local presses only: nav dropdowns, pricing tabs, an FAQ accordion, the mobile menu.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || (process.env.HOME + '/.design-systems/riverside/raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function pageHeight(p) {
  return p.evaluate(() => {
    const root = document.documentElement;
    const body = document.body;
    const nodes = [root, body, document.querySelector('main'), document.querySelector('.page-wrapper'), document.querySelector('.main-wrapper')].filter(Boolean);
    let h = 0;
    for (const n of nodes) {
      const sh = n.scrollHeight || 0;
      // A 900px html height is the viewport, not the page, when the body is taller.
      if (n === root && body && sh <= (window.innerHeight || 900) + 2 && (body.scrollHeight || 0) > sh + 40) continue;
      h = Math.max(h, sh, n.offsetHeight || 0);
    }
    for (const n of document.querySelectorAll('section, .section')) {
      const r = n.getBoundingClientRect();
      h = Math.max(h, r.bottom + window.scrollY);
    }
    return Math.ceil(h);
  });
}

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 48; i++) {
    const h = await pageHeight(p);
    if (h <= last + 40 && i > 3) break;
    last = Math.max(last, h);
    await p.evaluate((y) => window.scrollTo(0, y), Math.min(last - 100, (i + 1) * 800));
    await wait(p, 160);
  }
  await p.evaluate(() => window.scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    await closePromo(p);
    const H = await pageHeight(p);
    log('  height', name, H);
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    // Infinite-scroll pages grow scrollHeight without bound after lazyScroll;
    // without a ceiling the tile loop writes forever. Truncate hard and record
    // the boundary instead.
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    // Stage every tile under a .new name and swap it in only after the whole
    // shot succeeds, so a failed tile never truncates the previous capture.
    const staged = [];
    try {
      if (hCap <= chunk) {
        await screenshotWithMetadata(p, { path: f + '.new.png', fullPage: true }, this.requested);
        staged.push([f + '.new.png', f + '.png']);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          const tmp = `${f}.part${i}.new.png`;
          await screenshotWithMetadata(p, { path: tmp, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
          staged.push([tmp, `${f}.part${i}.png`]);
        }
      }
    } catch (e) {
      for (const [tmp] of staged) { for (const f of [tmp, tmp + '.capture.json']) fs.existsSync(f) && fs.unlinkSync(f); }
      throw e;
    }
    // `.new.png` staging names also start with `${prefix}-${name}.part`, so the
    // stale-tile sweep must skip them or it deletes the files about to be renamed.
    const stale = (n) => !n.includes('.new') && (n.startsWith(`${this.prefix}-${name}.part`) || n === `${this.prefix}-${name}.png` || n === `${this.prefix}-${name}.png.capture.json`);
    for (const old of fs.readdirSync(RAW).filter(stale)) fs.unlinkSync(`${RAW}/${old}`);
    for (const [tmp, final] of staged) {
      fs.renameSync(tmp, final);
      // The sidecar follows the image: rename it and point its `screenshot`
      // name at the final file, or a finished capture has no matching record.
      const sidecar = tmp + '.capture.json';
      if (fs.existsSync(sidecar)) {
        try {
          const meta = JSON.parse(fs.readFileSync(sidecar, 'utf8'));
          if (meta.screenshot) meta.screenshot = final.split('/').pop();
          fs.writeFileSync(sidecar, JSON.stringify(meta, null, 2) + '\n');
        } catch { /* leave the record as-is rather than lose it */ }
        fs.renameSync(sidecar, final + '.capture.json');
      }
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// A Webflow dropdown toggle opens a menu already in the DOM. The toggle text
// includes a chevron, so a ^Label$ filter misses it. Match the label, then
// force the matching .w-dropdown open so the list paints in the viewport.
const openDropdown = async (p, label) => {
  const opened = await p.evaluate((name) => {
    const toggles = [...document.querySelectorAll('.nav-dropdown-toggle--updated')];
    const t = toggles.find((el) => new RegExp('^' + name + '\\b').test((el.innerText || '').trim()));
    if (!t) return false;
    const drop = t.closest('.w-dropdown');
    if (!drop) return false;
    drop.classList.add('w--open');
    t.classList.add('w--open');
    t.setAttribute('aria-expanded', 'true');
    const list = drop.querySelector('.w-dropdown-list');
    if (list) {
      list.classList.add('w--open');
      list.style.setProperty('display', 'block', 'important');
      list.style.setProperty('opacity', '1', 'important');
      list.style.setProperty('visibility', 'visible', 'important');
    }
    return true;
  }, label);
  if (!opened) return false;
  await wait(p, 500);
  return true;
};

const openFaq = async (p) => {
  const a = p.locator('.faq-question, .w-dropdown-toggle, [class*="accordion"], summary, [role="button"]').filter({ visible: true });
  const n = await a.count();
  for (let i = 0; i < Math.min(n, 12); i++) {
    const el = a.nth(i);
    const text = ((await el.innerText().catch(() => '')) || '').trim();
    if (text.length < 12 || text.length > 180) continue;
    if (/cookie|allow all|platform|solutions|resources|english/i.test(text)) continue;
    await el.scrollIntoViewIfNeeded().catch(() => {});
    await clickEl(el);
    await wait(p, 700);
    return true;
  }
  return false;
};

const shotPage = async (p, S, extra) => {
  await S.view('default');
  if (extra) await extra(p, S);
  await S.full();
};

const desktop = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('platform-menu', async () => {
      if (await openDropdown(p, 'Platform')) {
        await wait(p, 400);
        await S.view('platform-menu');
      }
    });
    await p.keyboard.press('Escape').catch(() => {});
    await p.mouse.click(700, 500).catch(() => {});
    await wait(p, 400);
    await step('solutions-menu', async () => { if (await openDropdown(p, 'Solutions')) await S.view('solutions-menu'); });
    await p.keyboard.press('Escape').catch(() => {});
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('monthly', async () => {
      const tab = p.locator('button, [role="tab"], a, div').filter({ hasText: /^Monthly$/ }).filter({ visible: true }).first();
      if (await tab.count()) { await clickEl(tab); await wait(p, 800); await S.view('monthly'); }
    });
    await S.full();
  } },
  recording: { path: '/recording', wait: 4500, run: async (p, S) => shotPage(p, S) },
  editor: { path: '/video-editor', wait: 4500, run: async (p, S) => shotPage(p, S) },
  agents: { path: '/agents', wait: 4500, run: async (p, S) => shotPage(p, S) },
  business: { path: '/business', wait: 4500, run: async (p, S) => shotPage(p, S) },
  faq: { path: '/faq', wait: 4500, run: async (p, S) => {
    await S.view('default');
    await step('open', async () => { if (await openFaq(p)) await S.view('open'); });
    await S.full();
  } },
  blog: { path: '/blog', wait: 4500, run: async (p, S) => shotPage(p, S) },
  tools: { path: '/tools', wait: 4500, run: async (p, S) => shotPage(p, S) },
  about: { path: '/about', wait: 4500, run: async (p, S) => shotPage(p, S) },
  login: { path: '/login', wait: 4000, run: async (p, S) => {
    // Wall only. Do not type, do not click Google or Apple, do not submit.
    await S.view('wall');
  } },
};

const mobile = {
  home: { path: '/', wait: 5000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('.w-nav-button, .menu-button').filter({ visible: true }).first();
      if (await m.count()) { await clickEl(m); await wait(p, 1200); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 4500, run: async (p, S) => shotPage(p, S) },
  recording: { path: '/recording', wait: 4500, run: async (p, S) => shotPage(p, S) },
  faq: { path: '/faq', wait: 4500, run: async (p, S) => shotPage(p, S) },
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
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
