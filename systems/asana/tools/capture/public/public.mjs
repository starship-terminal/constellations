// Captures asana.com's public pages into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix. Every captured route
// paints light (the --darkmode-* set is declared, never bound). Desktop shots are 1440x900 at 1x,
// mobile 390x844 at 2x, `*-full` shots 1x. A page taller than one GPU texture is saved as
// name.partN.png tiles, which quantize.py stitches back together; an unbounded page truncates at
// 8 chunks and the log records the boundary.
// asana.com is a Next.js marketing site; headless Chromium is not challenged. The product on
// app.asana.com sits behind sign-in and is a boundary. Nothing is sent or signed into: the
// only presses are local UI toggles — the nav flyout, a pricing FAQ and the mobile menu.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, LAUNCH_OPTS } from './lib.mjs';

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
  async view(name) { await closePromo(this.p); await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  // A shot without closePromo: the consent card and the location dialog still up, as the page arrives.
  async raw(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', name); }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
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

// Public pages the homepage header, Products menu, Solutions menu and footer
// open. site-tree.md is the map. Auth hosts and external sites are not here.
const pageOf = (slug, path, extra) => ({ path, wait: 7000, run: async (p, S) => {
  await S.view('default');
  if (extra) await extra(p, S);
  await S.full();
} });

const desktop = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('flyout', async () => {
      const t = p.locator('button').filter({ hasText: /^Products$/ }).first();
      if (await t.count()) { await t.click(); await wait(p, 900); await S.view('flyout'); await p.keyboard.press('Escape').catch(() => {}); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 8000, run: async (p, S) => {
    await S.view('default');
    await step('faq', async () => {
      const t = p.locator('button[aria-expanded="false"]').filter({ visible: true }).first();
      if (await t.count()) { await t.scrollIntoViewIfNeeded(); await clickEl(t); await wait(p, 900); await S.view('faq'); }
    });
    await S.full();
  } },
  'product-ai': pageOf('product-ai', '/product/ai'),
  'product-overview': pageOf('product-overview', '/product'),
  'service-management': pageOf('service-management', '/product/service-management'),
  'client-management': pageOf('client-management', '/product/client-management'),
  command: pageOf('command', '/product/command'),
  'ai-teammates': pageOf('ai-teammates', '/product/ai/ai-teammates'),
  'ai-studio': pageOf('ai-studio', '/product/ai/ai-studio'),
  dash: pageOf('dash', '/product/ai/dash'),
  'admin-security': pageOf('admin-security', '/features/admin-security'),
  apps: pageOf('apps', '/apps'),
  developers: pageOf('developers', '/developers'),
  'whats-new': pageOf('whats-new', '/whats-new'),
  enterprise: pageOf('enterprise', '/enterprise'),
  'small-business': pageOf('small-business', '/small-business'),
  nonprofit: pageOf('nonprofit', '/industry/nonprofit'),
  agencies: pageOf('agencies', '/agencies'),
  'team-operations': pageOf('team-operations', '/teams/operations'),
  'team-marketing': pageOf('team-marketing', '/teams/marketing'),
  'team-it': pageOf('team-it', '/teams/it'),
  'team-leaders': pageOf('team-leaders', '/teams/leaders'),
  government: pageOf('government', '/industry/government-solutions'),
  healthcare: pageOf('healthcare', '/industry/healthcare'),
  retail: pageOf('retail', '/industry/retail'),
  finance: pageOf('finance', '/industry/financial-services'),
  education: pageOf('education', '/industry/education'),
  manufacturing: pageOf('manufacturing', '/industry/manufacturing'),
  media: pageOf('media', '/industry/media-entertainment'),
  'use-goals': pageOf('use-goals', '/uses/goal-management'),
  'use-planning': pageOf('use-planning', '/uses/organizational-planning'),
  'use-intake': pageOf('use-intake', '/uses/project-intake'),
  'use-resource': pageOf('use-resource', '/uses/resource-planning'),
  'use-launch': pageOf('use-launch', '/uses/product-launch'),
  uses: pageOf('uses', '/uses'),
  features: pageOf('features', '/features'),
  sales: pageOf('sales', '/sales'),
  'create-account': pageOf('create-account', '/create-account'),
  resources: pageOf('resources', '/resources'),
  templates: pageOf('templates', '/templates'),
  'plan-starter': pageOf('plan-starter', '/plan/starter'),
  'plan-advanced': pageOf('plan-advanced', '/plan/advanced'),
  teams: pageOf('teams', '/teams'),
  'resource-center': pageOf('resource-center', '/resources/category/all'),
  events: pageOf('events', '/events'),
  'customer-success': pageOf('customer-success', '/customer-success'),
  partners: pageOf('partners', '/partners'),
  'site-map': pageOf('site-map', '/site-map'),
  company: pageOf('company', '/company'),
  leadership: pageOf('leadership', '/leadership'),
  customers: pageOf('customers', '/customers'),
  jobs: pageOf('jobs', '/jobs'),
  blog: pageOf('blog', '/inside-asana'),
  culture: pageOf('culture', '/culture-and-belonging'),
  press: pageOf('press', '/press'),
  trust: pageOf('trust', '/trust'),
  privacy: pageOf('privacy', '/privacy'),
  terms: pageOf('terms', '/terms'),
  accessibility: pageOf('accessibility', '/accessibility'),
  certifications: pageOf('certifications', '/certifications'),
};

const mobile = {
  home: { path: '/', wait: 9000, run: async (p, S) => {
    await S.view('default');
    await step('menu', async () => {
      const m = p.locator('button[aria-label*="menu" i], button[aria-label*="Menu" i], [class*="hamburger"], button').filter({ hasText: /^Menu$/ }).first();
      const any = p.locator('header button, nav button').filter({ visible: true }).first();
      const target = (await m.count()) ? m : any;
      if (await target.count()) { await clickEl(target); await wait(p, 1200); await S.view('menu'); }
    });
    await S.full();
  } },
  pricing: { path: '/pricing', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'product-ai': { path: '/product/ai', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  sales: { path: '/sales', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  'create-account': { path: '/create-account', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  resources: { path: '/resources', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  templates: { path: '/templates', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  enterprise: { path: '/enterprise', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
  apps: { path: '/apps', wait: 7000, run: async (p, S) => { await S.view('default'); await S.full(); } },
};

const b = await chromium.launch(LAUNCH_OPTS);
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
    // Akamai answers some first hits on a fresh context with 403; a reload
    // after a wait clears most of them (see lib.mjs open()).
    let ok = false;
    for (let a = 0; a < 3 && !ok; a++) {
      await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      ok = await clearChallenge(p);
      if (!ok) await wait(p, 5000);
    }
    if (!ok) { log('  BLOCKED challenge', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 7000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
