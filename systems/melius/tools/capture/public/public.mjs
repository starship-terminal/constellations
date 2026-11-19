// Captures Melius public signed-out surfaces into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/melius/raw-shots \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a mobile- prefix.
// Desktop 1440x900 at 2x. Mobile 390x844 at 2x. A page taller than one GPU
// texture is saved as name.partN.png tiles (quantize.py stitches them) and
// truncated at 8 chunks.
//
// Sign In, Start for Free, Get started, billing and newsletter are never
// followed from a button press. Login and signup are opened by URL and left
// unsubmitted. A Cloudflare challenge stops that launch.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, APP, DOCS, hideConsent, clearChallenge, patch } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'melius', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function pinTop(p) {
  await p.evaluate(() => {
    const stop = (obj) => { try { obj && obj.stop && obj.stop(); } catch { /* optional */ } };
    stop(window.lenis);
    stop(window.__lenis);
    document.documentElement.classList.add('lenis-stopped');
    const zero = (el) => { try { el.scrollTop = 0; } catch { /* read-only */ } };
    zero(document.documentElement);
    zero(document.body);
    zero(document.scrollingElement);
    window.scrollTo(0, 0);
  }).catch(() => {});
}

async function settle(p) {
  await hideConsent(p);
  await p.evaluate(() => {
    document.querySelectorAll('video').forEach((v) => { try { v.pause(); } catch { /* autoplay */ } });
  }).catch(() => {});
}

async function lazyScroll(p) {
  const cap = 8 * Math.floor(14000 / (p.viewportSize()?.deviceScaleFactor || 1));
  for (let y = 0; y < cap; y += 700) {
    const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    if (y >= h - 800) break;
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 140);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 300);
  await hideConsent(p);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name, { pin = true } = {}) {
    await settle(this.p);
    if (pin) await pinTop(this.p);
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.p, { path: file, animations: 'disabled' }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const staged = [];
    try {
      if (hCap <= chunk) {
        await screenshotWithMetadata(p, { path: f + '.new.png', fullPage: true, animations: 'disabled' }, this.requested);
        staged.push([f + '.new.png', f + '.png']);
      } else {
        for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
          const tmp = `${f}.part${i}.new.png`;
          await screenshotWithMetadata(p, { path: tmp, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) }, animations: 'disabled' }, this.requested);
          staged.push([tmp, `${f}.part${i}.png`]);
        }
      }
    } catch (e) {
      for (const [tmp] of staged) {
        fs.existsSync(tmp) && fs.unlinkSync(tmp);
        fs.existsSync(tmp + '.capture.json') && fs.unlinkSync(tmp + '.capture.json');
      }
      throw e;
    }
    const keep = new Set();
    for (const [tmp, final] of staged) {
      fs.renameSync(tmp, final);
      keep.add(path.basename(final));
      const sideTmp = tmp + '.capture.json';
      const sideFinal = final + '.capture.json';
      if (fs.existsSync(sideTmp)) {
        try {
          const meta = JSON.parse(fs.readFileSync(sideTmp, 'utf8'));
          meta.screenshot = path.basename(final);
          fs.writeFileSync(sideTmp, JSON.stringify(meta, null, 2) + '\n');
        } catch { /* keep the sidecar as written */ }
        fs.renameSync(sideTmp, sideFinal);
        keep.add(path.basename(sideFinal));
      }
    }
    const stem = `${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => !keep.has(n) && (n.startsWith(`${stem}.part`) || n === `${stem}.png` || n === `${stem}.png.capture.json`))) {
      fs.unlinkSync(path.join(RAW, old));
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await pinTop(p);
    await wait(p, 200);
  }
}

async function goto(p, url) {
  await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  const ok = await clearChallenge(p);
  if (!ok) throw new Error('Cloudflare challenge at ' + url + '; stopping this launch');
  for (let i = 0; i < 16; i++) {
    const ready = await p.evaluate(() => {
      const h = document.querySelector('h1, h2, form, input');
      if (!h) return (document.body.innerText || '').length > 40;
      const cs = getComputedStyle(h);
      const r = h.getBoundingClientRect();
      return r.height > 8 && parseFloat(cs.opacity) > 0.4 && (document.body.innerText || '').length > 20;
    }).catch(() => false);
    if (ready) break;
    await wait(p, 400);
  }
  await hideConsent(p);
  await wait(p, 500);
  await pinTop(p);
  // The home hero types itself in. Wait until the headline is one line of
  // Reckless, then pin again so a Lenis tick cannot leave it mid-move.
  if (url === BASE + '/' || url === BASE) {
    for (let i = 0; i < 20; i++) {
      const done = await p.evaluate(() => {
        const h = document.querySelector('h1');
        if (!h) return false;
        const t = (h.innerText || '').replace(/\s+/g, ' ').trim();
        const cs = getComputedStyle(h);
        return t === 'Create anything you imagine' && parseFloat(cs.opacity) > 0.9 && h.getBoundingClientRect().height < 80;
      }).catch(() => false);
      if (done) break;
      await wait(p, 400);
    }
    await pinTop(p);
    await wait(p, 300);
  }
}

async function openDesktopMenu(p) {
  const hit = await p.evaluate(() => {
    const el = [...document.querySelectorAll('header button, header a, nav button, nav a')].find((n) => {
      const t = (n.innerText || '').trim();
      const r = n.getBoundingClientRect();
      return t === 'Product' && r.y < 90 && r.height > 10 && r.height < 60 && r.width > 40;
    });
    if (!el) return null;
    const r = el.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  });
  if (!hit) {
    log('  product menu trigger missed');
    return false;
  }
  await p.mouse.move(hit.x, hit.y);
  await wait(p, 700);
  return true;
}

async function openMobileMenu(p) {
  const hit = await p.evaluate(() => {
    const buttons = [...document.querySelectorAll('header button, nav button')];
    const el = buttons.find((b) => {
      const r = b.getBoundingClientRect();
      const label = (b.getAttribute('aria-label') || b.innerText || '').toLowerCase();
      return r.width > 16 && r.width < 80 && r.y < 90 && r.height > 16 && (label.includes('menu') || r.x > 280);
    }) || buttons.find((b) => {
      const r = b.getBoundingClientRect();
      return r.width > 16 && r.width < 64 && r.y < 80 && r.x > 280;
    });
    if (!el) return { n: buttons.length };
    const r = el.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2, label: el.getAttribute('aria-label') || '' };
  });
  if (!hit || !hit.x) {
    log('  mobile menu missed', JSON.stringify(hit));
    return false;
  }
  await p.mouse.click(hit.x, hit.y);
  await wait(p, 600);
  return true;
}

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    if (await openDesktopMenu(p)) await S.view('product-menu', { pin: false });
  } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  enterprise: { url: BASE + '/enterprise', run: async (p, S) => { await S.view('default'); await S.full(); } },
  about: { url: BASE + '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  manifesto: { url: BASE + '/manifesto', run: async (p, S) => { await S.view('default'); } },
  models: { url: BASE + '/models', run: async (p, S) => { await S.view('default'); await S.full(); } },
  brand: { url: BASE + '/brand', run: async (p, S) => { await S.view('default'); } },
  contact: { url: BASE + '/contact', run: async (p, S) => { await S.view('default'); } },
  creator: { url: BASE + '/creator-program', run: async (p, S) => { await S.view('default'); } },
  ditto: { url: BASE + '/product/ditto', run: async (p, S) => { await S.view('default'); } },
  image: { url: BASE + '/product/ai-image-generator', run: async (p, S) => { await S.view('default'); } },
  login: { url: APP + '/login', run: async (p, S) => { await S.view('default'); await S.full(); } },
  signup: { url: APP + '/signup', run: async (p, S) => { await S.view('default'); await S.full(); } },
  docs: { url: DOCS + '/', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    if (await openMobileMenu(p)) await S.view('menu-open', { pin: false });
  } },
  pricing: { url: BASE + '/pricing', run: async (p, S) => { await S.view('default'); } },
  login: { url: APP + '/login', run: async (p, S) => { await S.view('default'); } },
  signup: { url: APP + '/signup', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = 2;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name, spec.url);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await goto(p, spec.url);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message).split('\n')[0]);
    if (/Cloudflare/i.test(String(e.message))) {
      await ctx.close();
      await browser.close();
      process.exit(2);
    }
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
