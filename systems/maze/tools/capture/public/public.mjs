// Captures Maze's public signed-out surfaces into RAW (full-colour PNGs).
//
//   RAW=~/.design-systems/maze/raw-shots \
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a mobile- prefix.
// Desktop 1440x900 at 1x. Mobile 390x844 at 2x. A page taller than one GPU
// texture is saved as name.partN.png tiles (quantize.py stitches them) and
// truncated at 8 chunks.
//
// CookieYes (maze.co) and OneTrust (auth.maze.co) are hidden, never clicked. Log in, Try Maze
// for free, Get a demo, Contact sales, Sign up and Download are never
// followed from a button press. The login page is opened by URL and left
// unsubmitted. The public report is Maze's published sample; it is not a
// study, and no study is started.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, AUTH, REPORT, hideConsent, clearChallenge, patch } from './lib.mjs';

const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'maze', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function pinTop(p) {
  // Lenis owns scroll and the header is fixed, so a shot taken after a
  // scroll shows the hero under an empty band where the nav should be.
  // Stop Lenis, then write scrollTop on the document and every scroller.
  await p.evaluate(() => {
    const stop = (obj) => { try { obj && obj.stop && obj.stop(); } catch {} };
    stop(window.lenis);
    stop(window.__lenis);
    stop(window.Lenis);
    document.documentElement.classList.add('lenis-stopped');
    const zero = (el) => { try { el.scrollTop = 0; } catch {} };
    zero(document.documentElement);
    zero(document.body);
    zero(document.scrollingElement);
    document.querySelectorAll('[data-lenis], .lenis, html, body').forEach(zero);
    window.scrollTo(0, 0);
  }).catch(() => {});
  await p.evaluate(() => {
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
  }).catch(() => {});
}

async function settle(p) {
  await hideConsent(p);
  await p.evaluate(() => {
    document.querySelectorAll('video').forEach((v) => { try { v.pause(); } catch {} });
  }).catch(() => {});
}

async function lazyScroll(p) {
  // Walk to the bottom. An unchanged height is not the bottom: images with
  // reserved space do not grow the document when they load.
  const cap = 8 * Math.floor(14000 / (p.viewportSize()?.deviceScaleFactor || 1));
  for (let y = 0; y < cap; y += 700) {
    const h = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    if (y >= h - 800) break;
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 160);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
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
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    // maze.co's Lenis scroll is not window.scrollY. A viewport shot can be
    // the page mid-scroll while the sidecar still says y=0. When the hero
    // has left the top of the frame, crop the top of a full-page shot.
    if (pin && this.prefix.startsWith('home')) {
      const h1y = await this.p.evaluate(() => Math.round(document.querySelector('h1')?.getBoundingClientRect().y || 0)).catch(() => 0);
      if (h1y > 180) {
        // The scrolled viewport shot moves, with its sidecar, to -scrolled.png, and the crop takes the
        // published name with a sidecar that says it is a crop, so the package's links show the
        // corrected frame and every sidecar matches its image. A page that tiled has no single
        // -full.png; then there is nothing to crop and the viewport shot stays as shot.
        const full = `${RAW}/${this.prefix}-full.png`;
        if (!fs.existsSync(full)) await this.full();
        if (fs.existsSync(full)) {
          const { execFileSync } = await import('node:child_process');
          const crop = path.join(path.dirname(fileURLToPath(import.meta.url)), 'crop-top.py');
          const vh = this.p.viewportSize().height;
          const scrolled = file.replace(/\.png$/, '-scrolled.png');
          fs.renameSync(file, scrolled);
          if (fs.existsSync(file + '.capture.json')) {
            // The moved sidecar names its own image, as full() does for renamed captures.
            const meta = JSON.parse(fs.readFileSync(file + '.capture.json', 'utf8'));
            meta.screenshot = path.basename(scrolled);
            fs.writeFileSync(scrolled + '.capture.json', JSON.stringify(meta, null, 1) + '\n');
            fs.unlinkSync(file + '.capture.json');
          }
          const cropped = file;
          execFileSync('python3', [crop, full, cropped, String(this.vw * this.dpr), String(vh * this.dpr)], { stdio: 'inherit' });
          fs.writeFileSync(cropped + '.capture.json', JSON.stringify({
            schemaVersion: 1, screenshot: path.basename(cropped), requested: this.requested,
            capture: { mode: 'crop-of-full-page', from: path.basename(full), y: 0, height: vh },
            note: `the viewport shot had scrolled (h1 at y=${h1y}) and is kept as ${path.basename(scrolled)}; this is the top ${vh}px of the full page`,
          }, null, 1) + '\n');
          log('  cropped the top of the full page into', path.basename(cropped), 'h1 was', h1y);
        } else log('  ! no single full-page shot to crop; the viewport shot is kept as shot, h1 was', h1y);
      }
    }
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
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function goto(p, url) {
  await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 70000 });
  await clearChallenge(p);
  // Wait until the hero has painted. maze.co hydrates after the header,
  // and Lenis keeps the headline at opacity 0 for a moment. Hiding consent
  // before hydration blanks the React tree, so this wait comes first.
  for (let i = 0; i < 16; i++) {
    const ready = await p.evaluate(() => {
      const h = document.querySelector('h1');
      if (!h) return (document.body.innerText || '').length > 40;
      const cs = getComputedStyle(h);
      const r = h.getBoundingClientRect();
      return r.height > 20 && parseFloat(cs.opacity) > 0.5 && (h.innerText || '').length > 2;
    }).catch(() => false);
    if (ready) break;
    await wait(p, 500);
  }
  await hideConsent(p);
  // The headline enters one word at a time. Wait until that settles, then
  // pin the scroll so a Lenis tick cannot leave the hero mid-move.
  await wait(p, 1600);
  await pinTop(p);
  await wait(p, 400);
  await hideConsent(p);
  await pinTop(p);
  if (/app\.maze\.co\/report/.test(url)) {
    for (let i = 0; i < 12; i++) {
      const body = await p.evaluate(() => (document.body.innerText || '').replace(/\s+/g, ' ').slice(0, 60)).catch(() => '');
      if (body && !/^Loading/i.test(body) && body.length > 30) break;
      await wait(p, 1500);
    }
    await hideConsent(p);
  }
}

// Desktop nav items are buttons inside links. Hover the visible PLATFORM
// control. Do not click through to a product page from the menu.
async function shotMenu(p, S) {
  // The desktop dropdown lives in the DOM at y=0 with a 0-size box until
  // hover, and hover has not opened it in this session. Force the panel
  // visible for one shot, then put the style back. Do not follow a link.
  const shown = await p.evaluate(() => {
    const panel = [...document.querySelectorAll('header a[href="/platform/"]')].find((a) => a.getBoundingClientRect().height > 80)
      || document.querySelector('header a[href="/features/research-panel/"]');
    if (!panel) return false;
    let el = panel;
    for (let i = 0; i < 6 && el.parentElement; i++) {
      const r = el.getBoundingClientRect();
      if (r.width > 600 && r.height > 80) break;
      el = el.parentElement;
    }
    el.setAttribute('data-m-menu', '1');
    el.style.setProperty('display', 'block', 'important');
    el.style.setProperty('opacity', '1', 'important');
    el.style.setProperty('visibility', 'visible', 'important');
    el.style.setProperty('transform', 'none', 'important');
    el.style.setProperty('position', 'fixed', 'important');
    el.style.setProperty('top', '80px', 'important');
    el.style.setProperty('left', '160px', 'important');
    el.style.setProperty('z-index', '80', 'important');
    return true;
  });
  if (!shown) {
    log('  platform panel not in the DOM');
    return;
  }
  await wait(p, 300);
  await S.view('platform-menu', { pin: false });
  await p.evaluate(() => {
    const el = document.querySelector('[data-m-menu]');
    if (el) el.removeAttribute('style');
  }).catch(() => {});
}

async function openPlatform(p) {
  await pinTop(p);
  // Nav labels are an icon font, so innerText is empty and a text filter
  // misses. The visible trigger is the header link to /platform/ whose box
  // sits in the nav row (y < 70). The dropdown panel is a second, taller
  // link at the same href, parked below the row until hover.
  const hit = await p.evaluate(() => {
    const links = [...document.querySelectorAll('header a[href="/platform/"]')].map((a) => {
      const r = a.getBoundingClientRect();
      return { y: Math.round(r.y), h: Math.round(r.height), w: Math.round(r.width) };
    });
    const el = [...document.querySelectorAll('header a[href="/platform/"]')].find((a) => {
      const r = a.getBoundingClientRect();
      return r.y >= 0 && r.y < 160 && r.height > 10 && r.height < 90 && r.width > 40;
    });
    if (!el) return { miss: links.slice(0, 4) };
    const r = el.getBoundingClientRect();
    return { x: r.x + Math.min(36, r.width / 2), y: r.y + r.height / 2 };
  });
  if (!hit || hit.miss) {
    log('  platform trigger missed', JSON.stringify(hit && hit.miss));
    return false;
  }
  await p.mouse.move(hit.x, hit.y);
  await wait(p, 900);
  return true;
}

async function openMobileMenu(p) {
  const btn = p.getByRole('button', { name: /open navigation/i });
  if (await btn.count()) {
    await btn.click();
    await wait(p, 700);
    return true;
  }
  return false;
}

const desktop = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.full();
    await S.view('default');
    if (await openPlatform(p)) await S.view('platform-menu', { pin: false });
    else await shotMenu(p, S);
  } },
  pricing: { url: BASE + '/pricing/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  platform: { url: BASE + '/platform/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  reporting: { url: BASE + '/platform/ux-reporting/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  customers: { url: BASE + '/customers/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  report: { url: REPORT, run: async (p, S) => { await S.view('default'); await S.full(); } },
  login: { url: AUTH + '/login', run: async (p, S) => { await S.view('default'); await S.full(); } },
  demo: { url: BASE + '/demo/', run: async (p, S) => { await S.view('default'); } },
  research: { url: BASE + '/resources/user-research-report/', run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const mobile = {
  home: { url: BASE + '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    if (await openMobileMenu(p)) await S.view('menu-open');
  } },
  pricing: { url: BASE + '/pricing/', run: async (p, S) => { await S.view('default'); await S.full(); } },
  report: { url: REPORT, run: async (p, S) => { await S.view('default'); } },
  login: { url: AUTH + '/login', run: async (p, S) => { await S.view('default'); } },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = (mob ? mobile : desktop)[k];
  if (!spec.url) { log(name, 'skipped: MAZE_REPORT_URL is not set (see lib.mjs)'); continue; }
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
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
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await browser.close();
