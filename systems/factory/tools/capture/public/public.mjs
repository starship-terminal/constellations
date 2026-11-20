// Captures factory.com's (and docs.factory.com's) public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix. Every factory.com
// marketing page ships <html data-theme="light"> — the dark token layer is painted only inside
// scoped sections ([data-dark-hero] heroes, .invert-color-scheme panels, the site footer) — so the
// marketing shots are all *-light-*. docs.factory.com ships a real user theme toggle (three
// icon-only .theme-selector-button controls), so the docs pages are captured in both themes:
// *-light-* first, then "Switch to Dark theme" is clicked (a local UI toggle, never a form) and
// *-dark-* shots taken. app.factory.ai boots a splash then redirects to the auth.factory.ai
// sign-in card, captured at rest as signin-dark-*. Desktop shots are 1440x900 at 1x, mobile
// 390x844 at 2x, `*-full` shots 1x. A page taller than one viewport is saved as name.partN.png
// tiles — scrolled viewport screenshots, not fullPage captures: factory.com drives its section
// reveals from scroll progress, so a fullPage shot paints unrevealed sections blank. Tiles are
// stitched back together by quantize.py; an unbounded page truncates at 16 tiles and the log
// records the boundary. The fixed header is hidden for every tile after the first so it does not
// repeat down the stitched sheet. Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the header's Product/Company mega-menu buttons, the docs theme selector and the mobile
// "Open menu" button. The contact form (a lazily-mounted HubSpot form) and the sign-in card are
// shot at rest, never submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, DOCS, LOGIN_URL } from './lib.mjs';

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
  for (let y = 0; y < h; y += 600) { await p.evaluate((y) => scrollTo({ top: y, behavior: 'instant' }), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo({ top: 0, behavior: 'instant' })); await wait(p, 900);
}

// Hides the page's fixed-position chrome (the blurred site header and any
// overlay strip near the viewport top) so stitched tiles below the first do
// not repeat it. Tags what it hides for showChrome to restore.
async function hideChrome(p) {
  await p.evaluate(() => {
    document.querySelectorAll('[data-m-hidden]').forEach((x) => { x.style.removeProperty('visibility'); x.removeAttribute('data-m-hidden'); });
    document.querySelectorAll('header, [data-site-header], div, aside, nav').forEach((x) => {
      // In-content sticky elements (sticky labels inside main/section) are
      // real tile content; only hide page-level fixed chrome.
      if (x.closest('main, section, article')) return;
      const cs = getComputedStyle(x);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') return;
      const r = x.getBoundingClientRect();
      if (r.top > 120 || r.width < 200 || r.height < 8 || r.height > 400) return;
      x.setAttribute('data-m-hidden', '1');
      x.style.setProperty('visibility', 'hidden', 'important');
    });
  }).catch(() => {});
}
async function showChrome(p) {
  await p.evaluate(() => document.querySelectorAll('[data-m-hidden]').forEach((x) => { x.style.removeProperty('visibility'); x.removeAttribute('data-m-hidden'); })).catch(() => {});
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  // `full` tiles a tall page as scrolled viewport screenshots: factory.com's
  // section reveals are scroll-driven, so a fullPage capture paints them
  // blank while a real scrolled viewport shows the revealed state. Each tile
  // is one viewport; the fixed header chrome is hidden after the first tile
  // so it does not repeat. The sidecar's capture.clip is rewritten to the
  // tile's document region (viewport-relative clip y0 is what the shot was;
  // the document y is what it covers).
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    // A still-open mega-menu or consent overlay can lock body scroll, which
    // collapses scrollHeight to the viewport — re-strip overlays and re-read.
    const docH = () => p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0, document.documentElement.offsetHeight));
    const vh0 = this.requested.viewport.height;
    let H = await docH();
    const collapsed = H <= vh0 * 1.2;
    for (let i = 0; i < 4 && H <= vh0 * 1.2; i++) {
      await p.keyboard.press('Escape').catch(() => {});
      await p.mouse.move(720, 500).catch(() => {});
      await wait(p, 1200);
      await closePromo(p);
      H = await docH();
    }
    // The first scroll pass ran while the document was collapsed — scrub again
    // so lazily-mounted sections exist before the tiles are shot.
    if (collapsed && H > vh0 * 1.2) await lazyScroll(p);
    const vh = this.requested.viewport.height;
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXT = 16;
    const tiles = Math.min(Math.ceil(H / vh), MAXT);
    if (H > MAXT * vh) log(`  ! ${name}: page is ${H}px tall, capturing first ${MAXT * vh}px only (infinite/growing page boundary)`);
    if (tiles <= 1) {
      await screenshotWithMetadata(p, { path: f + '.png', scale: 'css', fullPage: true }, this.requested);
    } else {
      for (let i = 0; i < tiles; i++) {
        const y = i * vh;
        const h = Math.min(vh, H - y);
        // The last tile covers the page bottom: scroll clamps to H-vh, so the
        // tile region sits lower inside the viewport.
        const sy = Math.min(y, Math.max(0, H - vh));
        await p.evaluate((y) => scrollTo({ top: y, behavior: 'instant' }), sy);
        await wait(p, 1100);
        if (i > 0) await hideChrome(p);
        else await closePromo(p);
        const file = `${f}.part${i}.png`;
        await screenshotWithMetadata(p, { path: file, clip: { x: 0, y: y - sy, width: this.vw, height: h } }, this.requested);
        const side = JSON.parse(fs.readFileSync(file + '.capture.json', 'utf8'));
        side.capture = { ...side.capture, mode: 'scrolledViewportTile', clip: { x: 0, y, width: this.vw, height: h } };
        fs.writeFileSync(file + '.capture.json', JSON.stringify(side, null, 2) + '\n');
        log('  tile', i, 'y=' + y);
      }
      await showChrome(p);
    }
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Opens one of the header's mega-menus ("Product"/"Enterprise"/"Company" —
// buttons carrying aria-expanded, local UI toggles, never links) and shoots
// the .megamenu-viewport panel. Hover, click and keyboard are all tried: the
// menus open on pointer hover on the real site, which a headless run may or
// may not deliver.
async function navMenu(p, S, name) {
  const btn = p.locator('header button').filter({ hasText: new RegExp(`^${name}$`) }).filter({ visible: true }).first();
  if (!(await btn.count())) return;
  const expanded = async () => (await btn.getAttribute('aria-expanded').catch(() => null)) === 'true';
  for (let i = 0; i < 3 && !(await expanded()); i++) {
    await btn.hover().catch(() => {});
    await wait(p, 700);
    if (!(await expanded())) { await clickEl(btn, 4000); await wait(p, 800); }
    if (!(await expanded())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 800); }
  }
  if (!(await expanded())) { log('  ! menu', name, 'did not report open'); return; }
  await S.view('menu-' + name.toLowerCase());
  await p.keyboard.press('Escape');
  await p.mouse.move(700, 500);
  await wait(p, 600);
}

// Sets the docs theme through the three-way .theme-selector-button control in
// the docs header — a local UI toggle, no form, no navigation.
async function setDocsTheme(p, theme) {
  const btn = p.locator(`button.theme-selector-button[aria-label="Switch to ${theme} theme"]`).first();
  if (!(await btn.count())) throw new Error('no theme selector');
  await clickEl(btn);
  await wait(p, 900);
  const cur = await p.evaluate(() => document.documentElement.getAttribute('data-theme'));
  // a toggle that did not paint must not write a light page as *-dark-*.png:
  // throw, and step() logs the state as missing (2026-11 audit, not run)
  if (cur !== theme.toLowerCase()) throw new Error(`docs theme reads ${JSON.stringify(cur)} after switching to ${theme}`);
  return cur;
}

// Waits for the lazily-mounted HubSpot contact form's fields to appear.
async function waitForm(p) {
  for (let i = 0; i < 12; i++) {
    const n = await p.evaluate(() => document.querySelectorAll('input:not([type="hidden"]),textarea').length).catch(() => 0);
    if (n >= 3) return;
    await wait(p, 1500);
  }
  log('  ! contact form fields never mounted');
}

const desktop = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('menu-product', () => navMenu(p, S, 'Product'));
    await step('menu-company', () => navMenu(p, S, 'Company'));
    await S.full();
  } },
  enterprise: { url: BASE + '/enterprise', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-desktop': { url: BASE + '/product/desktop', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-cli': { url: BASE + '/product/cli', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-ide': { url: BASE + '/product/ide', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-automations': { url: BASE + '/product/automations', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-software-factory': { url: BASE + '/product/software-factory', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-security-factory': { url: BASE + '/product/security-factory', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-connectors': { url: BASE + '/product/connectors', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-cloud-agents': { url: BASE + '/product/cloud-agents', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-droid-computers': { url: BASE + '/product/droid-computers', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-agent-effectiveness': { url: BASE + '/product/agent-effectiveness', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-missions': { url: BASE + '/product/missions', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-router': { url: BASE + '/product/router', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  // The mega-menu's "Agent Readiness" links /agent-readiness; /product/agent-readiness
  // is a separate codebase-evaluation page that the menu does not reach.
  'agent-readiness': { url: BASE + '/agent-readiness', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'product-analytics': { url: BASE + '/product/analytics', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  news: { url: BASE + '/news', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  company: { url: BASE + '/company', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  events: { url: BASE + '/events', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact', wait: 7000, theme: 'light', run: async (p, S) => {
    await waitForm(p);
    await S.view('default');
    await S.full();
  } },
  security: { url: BASE + '/security', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  partners: { url: BASE + '/partners', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  ambassador: { url: BASE + '/ambassador', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  oss: { url: BASE + '/oss', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  science: { url: BASE + '/science', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'privacy-policy': { url: BASE + '/privacy-policy', wait: 6000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  'docs-home': { url: DOCS + '/docs', wait: 7000, theme: 'light', run: async (p, S, mk) => {
    await S.view('default');
    await S.full();
    await step('docs-dark', async () => {
      await setDocsTheme(p, 'Dark');
      const D = mk('dark');
      await D.view('default');
      await D.full();
    });
  } },
  'docs-changelog': { url: DOCS + '/docs/changelog/release-notes', wait: 7000, theme: 'light', run: async (p, S, mk) => {
    await S.view('default');
    await S.full();
    await step('docs-dark', async () => {
      await setDocsTheme(p, 'Dark');
      const D = mk('dark');
      await D.view('default');
    });
  } },
  'docs-quickstart': { url: DOCS + '/docs/factory-app/quickstart', wait: 7000, theme: 'light', run: async (p, S, mk) => {
    await S.view('default');
    await S.full();
    await step('docs-dark', async () => {
      await setDocsTheme(p, 'Dark');
      const D = mk('dark');
      await D.view('default');
      await D.full();
    });
  } },
  signin: { url: LOGIN_URL, wait: 0, theme: 'dark', run: async (p, S) => {
    // app.factory.ai boots a splash, then redirects to the auth.factory.ai
    // sign-in card. Wait for the card's fields, then shoot at rest.
    for (let i = 0; i < 25; i++) {
      await wait(p, 2000);
      const ready = await p.evaluate(() => {
        const t = (document.body && document.body.innerText) || '';
        return /sign in/i.test(t) && !!document.querySelector('input[type="email"], input[name="email"]');
      }).catch(() => false);
      if (ready) break;
    }
    await wait(p, 2500);
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { url: BASE + '/', wait: 9000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await step('drawer', async () => {
      // The header's "Open menu" button toggles the nav overlay — a local UI
      // toggle; its links are never followed. The overlay is the <nav> inside
      // the header (its label is an aria-label, not innerText, so match the
      // attribute), and a closed overlay still reports a full-size box, so
      // "open" has to require the panel to intersect the viewport.
      const ham = p.locator('header button[aria-label*="menu" i]').first();
      const btn = (await ham.count()) ? ham : p.locator('header button').filter({ hasText: /open menu|close menu/i }).first();
      const open = () => p.evaluate(() => !!([...document.querySelectorAll('body > div, body > nav, [role="dialog"], .megamenu-viewport, header nav')].find((x) => {
        const r = x.getBoundingClientRect(); const cs = getComputedStyle(x);
        const onScreen = r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth;
        return r.height > 300 && onScreen && /\S/.test(x.textContent || '') && (cs.position === 'fixed' || cs.position === 'absolute') && cs.visibility !== 'hidden' && cs.opacity !== '0';
      }))).catch(() => false);
      if (!(await open())) await clickEl(btn);
      await wait(p, 1000);
      if (!(await open())) { await btn.focus(); await p.keyboard.press('Enter'); await wait(p, 1000); }
      await S.view('drawer');
      await p.keyboard.press('Escape');
    });
    await S.full();
  } },
  pricing: { url: BASE + '/pricing', wait: 8000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
  } },
  contact: { url: BASE + '/contact', wait: 7000, theme: 'light', run: async (p, S) => {
    await waitForm(p);
    await S.view('default');
    await S.full();
  } },
  'docs-home': { url: DOCS + '/docs', wait: 7000, theme: 'light', run: async (p, S) => {
    await S.view('default');
    await S.full();
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
  const shooters = [];
  const mk = (theme) => { const s = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, spec.url); shooters.push(s); return s; };
  const S = mk(spec.theme);
  try {
    await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S, mk);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += shooters.reduce((n, s) => n + s.count, 0);
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
