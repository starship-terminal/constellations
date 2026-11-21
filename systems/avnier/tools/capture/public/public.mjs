// Captures avnier.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. The site paints one light
// theme. Desktop shots are 1440x900 at 1x, mobile 390x844 at 2x. A page taller than one GPU texture
// is saved as name.partN.png tiles, which quantize.py stitches back together; an unbounded page
// truncates at 8 chunks and the log records the boundary.
//
// avnier.com serves headless Chrome a 200 (see lib.mjs). Nothing is bought, sent or signed into:
// the only presses are local UI toggles — the SHOP mega-menu hover, the mobile drawer and a PDP
// variant radio where the DOM offers one. The Axeptio consent SDK and the shipping-country popup
// are hidden, never answered (no Accept/Reject is ever clicked); the consent view is captured
// before it is hidden.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

// Scrolls far enough to trigger lazy loading, but never past maxY: on an
// unbounded page the scroll target is the tile cap, not the reported height.
async function lazyScroll(p, maxY = Infinity) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < Math.min(h, maxY); y += 600) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 200); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 900);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr }; this.count = 0; }
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  // A shot without closePromo: the page as it arrives, consent layer included if it shows.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    const chunk = Math.floor(14000 / this.dpr);
    // Infinite-scroll pages grow scrollHeight without bound while lazyScroll
    // walks them; the tile ceiling is applied to the scroll itself, so a page
    // reporting millions of pixels cannot tie up the run before the cap.
    const MAXH = 8 * chunk;
    const H0 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    await lazyScroll(p, Math.min(H0, MAXH));
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only (infinite/growing page boundary)`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    this.count++; log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
  }
}
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 8000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

// Hover a top-level mega-menu item. The label is a text node on the <li>, not
// an <a>, so hasText on a link misses it. The dropdown is a sibling panel.
const openMega = async (p, index) => {
  // The item's accessible text includes the hidden panel, so a /^SHOP/ filter misses it.
  const item = p.locator('.mega-menu__list > .mega-menu__item').nth(index);
  if (!(await item.count())) return false;
  const box = await item.boundingBox();
  if (!box) return false;
  await item.hover({ force: true, position: { x: Math.min(box.width / 2, 36), y: 16 } }).catch(() => {});
  await p.mouse.move(box.x + Math.min(box.width / 2, 36), Math.max(8, box.y + 16));
  await p.evaluate((i) => {
    const li = document.querySelectorAll('.mega-menu__list > .mega-menu__item')[i];
    if (!li) return;
    for (const type of ['mouseover', 'mouseenter']) li.dispatchEvent(new MouseEvent(type, { bubbles: type === 'mouseover', view: window }));
  }, index);
  await wait(p, 1100);
  const open = await p.evaluate((i) => {
    const drop = document.querySelector('.mega-menu__dropdown');
    if (!drop) return false;
    const r = drop.getBoundingClientRect();
    if (getComputedStyle(drop).display === 'none' || r.height < 40) return false;
    const panel = drop.querySelectorAll(':scope > .mega-menu__dropdown-item')[i];
    if (!panel) return true;
    const pr = panel.getBoundingClientRect();
    return pr.height > 40 && getComputedStyle(panel).display !== 'none';
  }, index);
  return open;
};

// The first-order dialog is a cross-origin frame. Page script cannot see its
// text, so the frame is removed through the browser session. Never filled.
const dropPromoFrames = async (p) => {
  // The first-order dialog is a Klaviyo form in the light DOM (form.klaviyo-form).
  // Hide that form and its fixed shell. Never type into it and never submit it.
  const n = await p.evaluate(() => {
    let n = 0;
    document.querySelectorAll('form.klaviyo-form, form.needsclick, [class*="klaviyo-form"]').forEach((el) => {
      let host = el;
      for (let i = 0; i < 6 && host && host !== document.body; i++) {
        const cs = getComputedStyle(host);
        if (cs.position === 'fixed' || host.className.toString().includes('kl-private')) {
          host.style.setProperty('display', 'none', 'important');
          n++;
          return;
        }
        host = host.parentElement;
      }
      el.style.setProperty('display', 'none', 'important');
      n++;
    });
    return n;
  }).catch(() => 0);
  if (n) log('  promo hidden', n);
  await wait(p, 300);
  return n;
};

const openSearch = async (p) => {
  const opened = await p.evaluate(() => {
    const s = [...document.querySelectorAll('summary[aria-label="Recherche"]')].find((el) => !el.closest('#menu-drawer, header-drawer'));
    if (!s) return false;
    s.click();
    return true;
  });
  if (!opened) return false;
  await wait(p, 700);
  return true;
};

const desktop = {
  home: { path: '/', wait: 8000, run: async (p, S) => {
    await S.raw('consent');                       // the page as it arrives, consent layer included
    await step('promo', async () => {
      // The first-order code dialog arrives on its own, inside a closed shadow
      // root. Record the page as it arrives, never fill the dialog.
      await S.raw('promo');
    });
    await S.view('default');
    await step('megamenu', async () => { if (await openMega(p, 0)) await S.view('megamenu'); await p.mouse.move(700, 8); await wait(p, 500); });
    await step('marque-menu', async () => { if (await openMega(p, 1)) await S.view('marque-menu'); await p.mouse.move(700, 8); await wait(p, 400); });
    await step('search', async () => {
      await dropPromoFrames(p);
      await closePromo(p);
      if (!(await openSearch(p))) return;
      await dropPromoFrames(p);
      await wait(p, 500);
      await S.view('search');
      await p.keyboard.press('Escape').catch(() => {});
    });
    await S.full();
  } },
  shop: { path: '/collections/tous-les-produits', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('filter', async () => {
      const facet = p.locator('.facets__disclosure summary, #FacetsWrapperDesktop summary').filter({ hasText: /COULEUR/i }).first();
      if (await facet.count()) { await facet.click({ force: true }); await wait(p, 600); await S.view('filter'); }
    });
    await S.full();
  } },
  pdp: { path: '/products/doudoune-symphony', wait: 8000, run: async (p, S) => {
    // A named public product so size, colour and the size-guide dialog are
    // the same controls the site tree records. The grid's first card can be
    // a different product on another day.
    const href = await p.evaluate(() => location.pathname.startsWith('/products/') ? location.pathname : null);
    if (!href) { log('  no product link found'); return; }
    await p.goto(/^https?:/.test(href) ? href : BASE + href, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await clearChallenge(p); await wait(p, 8000);
    await S.view('default');
    await step('variant-picked', async () => {
      const r = p.locator('fieldset input[type="radio"][name="taille"], variant-radios input[type="radio"]').nth(1);
      if (await r.count()) { await r.check({ force: true }).catch(() => r.evaluate((el) => el.click())); await wait(p, 700); await S.view('variant-picked'); }
    });
    await step('size-guide', async () => {
      await dropPromoFrames(p);
      const b = p.locator('button.product-popup-modal__button').filter({ hasText: /taille/i }).first();
      if (await b.count()) {
        await b.click({ force: true });
        await dropPromoFrames(p);
        await wait(p, 800);
        await S.view('size-guide');
        await p.keyboard.press('Escape').catch(() => {});
      }
    });
    await S.full();
  } },
  cart: { path: '/', wait: 8000, run: async (p, S) => {
    // /cart 404s: the cart is the side-cart drawer opened by the header's
    // PANIER link (JS intercepts the /cart href, so the click stays on '/').
    const cartLink = p.locator('header a').filter({ hasText: /panier/i }).filter({ visible: true }).first();
    if (await cartLink.count()) { await cartLink.click().catch(() => {}); await wait(p, 2600); }
    await S.view('default');
  } },
  login: { path: '/account/login', wait: 8000, run: async (p, S) => {
    // The customer login form: email + password + CONNEXION. Never submitted.
    // No field is typed. No SSO control is clicked.
    await S.view('default');
    await S.full();
  } },
  contact: { path: '/pages/contact', wait: 6000, run: async (p, S) => {
    // Public contact page. The form is not filled and not submitted.
    await S.view('default');
  } },
  story: { path: '/pages/histoire', wait: 6000, run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', wait: 8000, run: async (p, S) => {
    await S.view('default');
    // The full-page shot comes first: once the drawer is open it covers the
    // home view, and full() hides consent/popup layers only.
    await S.full();
    await step('menu', async () => {
      const m = p.locator('summary[aria-label="Menu"]').first();
      if (await m.count()) { await m.click({ force: true }).catch(() => clickEl(m)); await wait(p, 1200); await S.view('menu'); }
    });
  } },
  'shop': { path: '/collections/tous-les-produits', wait: 8000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch({ channel: 'chrome', headless: true });
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'fr-FR' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(spec.url || BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
