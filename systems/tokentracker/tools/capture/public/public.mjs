// Captures TokenTracker's local dashboard into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; phone ones get a `mobile-` prefix. Every page is shot in dark
// (the dashboard's default) and light, desktop 1440x900 and phone 390x844, both at 2x.
// Nothing is sent, created or signed into: the presses are period tabs, the sidebar collapse chevron,
// a filter select (closed with Escape), the mobile menu, tab switches inside a page, Share then Copy
// (drawn and copied inside the headless browser), one Skills tick and its Remove confirmation
// (cancelled with Escape), and an invalid proxy host typed and cleared. lib.mjs aborts every
// non-GET request, so none of these can save, sync or remove anything.
// mask() runs before every shot, so paths, session titles and skill names never reach a PNG.
import fs from 'fs';
import { launch, mask, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../raw/full/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const failures = [];
const step = async (label, fn) => { try { await fn(); } catch (e) { failures.push(label); log('  FAILED', label, String(e.message).split('\n')[0]); } };

class Shooter {
  constructor(p, prefix) { this.p = p; this.prefix = prefix; }
  async view(name) { await mask(this.p); await this.p.screenshot({ path: `${RAW}/${this.prefix}-${name}.png` }); log('  shot', this.prefix, name); }
  // The content scrolls inside the shell's own scroller, so a full shot grows that scroller instead.
  async full(name = 'full') {
    const p = this.p;
    const h = await p.evaluate(() => {
      const sc = [...document.querySelectorAll('div')].filter((d) => /(auto|scroll)/.test(getComputedStyle(d).overflowY) && d.scrollHeight > d.clientHeight + 50).sort((a, b) => b.scrollHeight - a.scrollHeight)[0];
      return sc ? sc.scrollHeight + 40 : document.documentElement.scrollHeight;
    });
    const vp = p.viewportSize();
    await p.setViewportSize({ width: vp.width, height: Math.min(h, 6000) });
    await wait(p, 1200);
    await this.view(name);
    await p.setViewportSize(vp);
    await wait(p, 600);
  }
}

const click = async (p, loc) => { await loc.first().click({ timeout: 4000 }); await wait(p, 700); };
const byText = (p, t, role = 'button') => p.getByRole(role, { name: t, exact: true });

const desktop = {
  dashboard: { path: '/dashboard', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await step('nav-hover', async () => { await p.getByRole('link', { name: 'Sessions' }).first().hover(); await wait(p, 400); await S.view('nav-hover'); await p.mouse.move(1430, 890); });
    await step('period-week', async () => { await click(p, byText(p, 'Week', 'tab')); await wait(p, 1500); await S.view('period-week'); await click(p, byText(p, 'Month', 'tab')); });
    await step('cost-hover', async () => { await p.locator('main button[aria-label="View cost breakdown"]').first().hover(); await wait(p, 600); await S.view('cost-hover'); await p.mouse.move(1430, 890); });
    await step('sidebar-collapsed', async () => { await click(p, p.getByRole('button', { name: /collapse|sidebar/i })); await wait(p, 800); await S.view('sidebar-collapsed'); await click(p, p.getByRole('button', { name: /expand|sidebar/i })); });
    // Share card, then Copy: the card is drawn and copied inside this headless browser, raising a toast.
    await step('share-toast', async () => {
      await click(p, p.locator('main button').filter({ hasText: /^Share$/ }));
      await wait(p, 1500); await S.view('share-open');
      await p.locator('[role=dialog] button').filter({ hasText: /^Copy/i }).first().click({ timeout: 4000 });
      await wait(p, 900); await S.view('toast');
      await p.keyboard.press('Escape'); await wait(p, 500);
    });
  } },
  // First run: a second TokenTracker started with an empty HOME (no usage yet), on its own port.
  onboarding: { base: process.env.TT_EMPTY_BASE || 'http://127.0.0.1:7681', path: '/dashboard', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'sessions-loading': { path: '/sessions', wait: 1800, routes: (p) => p.route('**/functions/tokentracker-sessions**', (r) => setTimeout(() => r.fallback().catch(() => {}), 20000)), run: async (p, S) => { await S.view('default'); } },
  'sessions-error': { path: '/sessions', routes: (p) => p.route('**/functions/tokentracker-sessions**', (r) => r.abort()), run: async (p, S) => { await S.view('default'); } },
  sessions: { path: '/sessions', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => { await p.getByPlaceholder(/search/i).first().click(); await wait(p, 400); await S.view('search-focused'); await p.keyboard.press('Escape'); await p.mouse.click(1430, 890); });
    await step('select-open', async () => { await click(p, p.locator('span.truncate', { hasText: /^All tools$/ }).locator('xpath=ancestor::*[self::button or @role="combobox"][1]')); await wait(p, 500); await S.view('select-open'); await p.keyboard.press('Escape'); await wait(p, 400); });
    await step('row-hover', async () => { await p.locator('.sessions-row').nth(1).hover(); await wait(p, 400); await S.view('row-hover'); await p.mouse.move(1430, 890); });
    await step('empty', async () => { const f = p.getByPlaceholder(/search/i).first(); await f.click(); await p.keyboard.type('zzqx-no-match', { delay: 10 }); await wait(p, 1200); await S.view('empty'); await f.fill(''); await wait(p, 500); });
  } },
  limits: { path: '/limits', run: async (p, S) => { await S.view('default'); await S.full(); } },
  skills: { path: '/skills', run: async (p, S) => {
    await S.view('default');
    // One row ticked, bulk Remove opens the confirmation, Escape cancels, the tick is cleared.
    // The confirm button is never pressed; non-GET requests are blocked regardless.
    await step('confirm', async () => {
      const box = p.locator('main input[type="checkbox"]').first();
      await box.check(); await wait(p, 600); await S.view('selected');
      await p.locator('main button').filter({ hasText: /^Remove$/ }).filter({ visible: true }).first().click({ timeout: 4000 });
      await wait(p, 900); await S.view('confirm');
      await p.keyboard.press('Escape'); await wait(p, 600);
      if (await p.locator('[role=dialog]').filter({ visible: true }).count()) throw new Error('confirmation did not close');
      await box.uncheck(); await wait(p, 300);
    });
    await step('browse', async () => { await click(p, byText(p, 'Browse')); await wait(p, 2500); await S.view('browse'); }); } },
  settings: { path: '/settings', run: async (p, S) => {
    await S.view('default');
    await step('segment-hover', async () => { await byText(p, 'Full').first().hover(); await wait(p, 400); await S.view('segment-hover'); await p.mouse.move(1430, 890); });
    await step('account', async () => { await click(p, byText(p, 'Account')); await S.view('account'); });
    await step('usage-limits', async () => { await click(p, byText(p, 'Usage & Limits')); await S.view('usage-limits'); });
    await step('labs', async () => { await click(p, byText(p, 'Labs')); await S.view('labs'); });
    // Network: an invalid proxy host typed and left, then cleared. Never saved.
    await step('network-error', async () => {
      await click(p, byText(p, 'Network')); await S.view('network');
      // The proxy fields show only for Manual; choosing it is not saved until Save, which is never pressed.
      await click(p, byText(p, 'Manual'));
      const f = p.locator('main input[type="text"][placeholder]').filter({ visible: true }).first();
      const before = await f.inputValue();
      await f.click(); await p.keyboard.press('ControlOrMeta+a'); await p.keyboard.type('http://proxy.example/path', { delay: 10 }); await p.keyboard.press('Tab');
    // Errors show on Test connection (or Save). With an invalid host the check fails before any request
    // is made; the test itself would be a POST, which the capture blocks. Save is never pressed.
    await p.locator('main button').filter({ hasText: /^Test connection$/ }).first().click({ timeout: 4000 }); await wait(p, 700);
      await S.view('network-error');
      await f.fill(before); await p.keyboard.press('Tab'); await wait(p, 300); await click(p, byText(p, 'System'));
    });
  } },
  widgets: { path: '/widgets', run: async (p, S) => { await S.view('default'); await S.full(); } },
  achievements: { path: '/achievements', run: async (p, S) => { await S.view('default'); } },
  pet: { path: '/pet-settings', run: async (p, S) => { await S.view('default'); } },
  'service-status': { path: '/service-status', run: async (p, S) => { await wait(p, 4000); await S.view('default'); } },
};

const mobile = {
  dashboard: { path: '/dashboard', run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { await click(p, p.getByRole('button', { name: /menu|open navigation/i })); await wait(p, 700); await S.view('menu-open'); await p.keyboard.press('Escape'); });
  } },
  sessions: { path: '/sessions', run: async (p, S) => { await S.view('default'); } },
  limits: { path: '/limits', run: async (p, S) => { await S.view('default'); } },
  settings: { path: '/settings', run: async (p, S) => { await S.view('default'); } },
};

for (const theme of ['dark', 'light']) {
  for (const [set, pages, isMobile] of [['desktop', desktop, false], ['mobile', mobile, true]]) {
    const { browser, context } = await launch({ mobile: isMobile, theme });
    for (const [name, def] of Object.entries(pages)) {
      if (pageArg.length && !pageArg.includes(name)) continue;
      const p = await context.newPage();
      log(set, theme, name);
      await step(name, async () => {
        if (def.routes) await def.routes(p);
        await p.goto((def.base || BASE) + def.path, { waitUntil: 'load', timeout: 60000 });
        await wait(p, def.wait || 3500);
        await def.run(p, new Shooter(p, `${isMobile ? 'mobile-' : ''}${name}-${theme}`));
      });
      await p.close();
    }
    await browser.close();
  }
}
if (failures.length) {
  log('FAILED states:', failures.join(', '));
  process.exit(1);
}
