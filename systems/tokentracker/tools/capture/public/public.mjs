// Captures TokenTracker's local dashboard into RAW (full-colour PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; phone ones get a `mobile-` prefix. Every page is shot in dark
// (the dashboard's default) and light, desktop 1440x900 and phone 390x844, both at 2x.
// Nothing is sent, created or signed into: the only presses are period tabs, the sidebar collapse
// chevron, a filter select (closed with Escape), the mobile menu, and tab switches inside a page.
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
  } },
  sessions: { path: '/sessions', run: async (p, S) => {
    await S.view('default');
    await step('search-focused', async () => { await p.getByPlaceholder(/search/i).first().click(); await wait(p, 400); await S.view('search-focused'); await p.keyboard.press('Escape'); await p.mouse.click(1430, 890); });
    await step('select-open', async () => { await click(p, p.locator('span.truncate', { hasText: /^All tools$/ }).locator('xpath=ancestor::*[self::button or @role="combobox"][1]')); await wait(p, 500); await S.view('select-open'); await p.keyboard.press('Escape'); await wait(p, 400); });
    await step('row-hover', async () => { await p.locator('.sessions-row').nth(1).hover(); await wait(p, 400); await S.view('row-hover'); await p.mouse.move(1430, 890); });
  } },
  limits: { path: '/limits', run: async (p, S) => { await S.view('default'); await S.full(); } },
  skills: { path: '/skills', run: async (p, S) => { await S.view('default'); await step('browse', async () => { await click(p, byText(p, 'Browse')); await wait(p, 2500); await S.view('browse'); }); } },
  settings: { path: '/settings', run: async (p, S) => {
    await S.view('default');
    await step('segment-hover', async () => { await byText(p, 'Full').first().hover(); await wait(p, 400); await S.view('segment-hover'); await p.mouse.move(1430, 890); });
    await step('account', async () => { await click(p, byText(p, 'Account')); await S.view('account'); });
    await step('usage-limits', async () => { await click(p, byText(p, 'Usage & Limits')); await S.view('usage-limits'); });
    await step('labs', async () => { await click(p, byText(p, 'Labs')); await S.view('labs'); });
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
        await p.goto(BASE + def.path, { waitUntil: 'load', timeout: 60000 });
        await wait(p, 3500);
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
