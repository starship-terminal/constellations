// Captures OneSoil's public marketing pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x, phone shots 390x844 at 2x. Names are
// {page}-light-{state}.png; phone ones get a mobile- prefix.
//
// Nothing is submitted. Try Free, Open Web App and Open App leave the
// marketing site for the sign-in wall and are not followed. Contact and demo
// forms are not filled. Google and Apple are not clicked. Cookie banners, if
// any, are hidden rather than answered.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const inPackage = path.basename(path.dirname(PKG)) === 'systems';
if (!process.env.RAW && !inPackage) {
  console.error('set RAW=<scratch dir> (this copy is not inside systems/<slug>/tools/)');
  process.exit(2);
}
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', path.basename(PKG), 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function hideOverlays(p) {
  await p.evaluate(() => {
    document.querySelectorAll('#onetrust-banner-sdk, [id*="onetrust" i], [class*="cookie" i], [id*="cookie-banner" i], [class*="consent" i]').forEach((el) => {
      el.style.setProperty('display', 'none', 'important');
    });
  }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`,
          fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function openMenu(p, name) {
  await p.evaluate(() => scrollTo(0, 0));
  const btn = p.locator('header').getByRole('button', { name, exact: true }).first();
  await btn.click();
  await wait(p, 600);
}

async function shotPage(p, S, extra) {
  await hideOverlays(p);
  await S.view('default');
  if (extra) await extra(p, S);
  await S.full();
}

const desktop = {
  home: { path: '/en', run: async (p, S) => {
    await shotPage(p, S, async () => {
      await step('products-menu', async () => {
        await openMenu(p, 'Products');
        await S.view('products-menu');
        await p.keyboard.press('Escape');
        await wait(p, 300);
      });
      await step('solutions-menu', async () => {
        await openMenu(p, 'Solutions');
        await S.view('solutions-menu');
        await p.keyboard.press('Escape');
        await wait(p, 300);
      });
      await step('company-menu', async () => {
        await openMenu(p, 'Company');
        await S.view('company-menu');
        await p.keyboard.press('Escape');
        await wait(p, 300);
      });
      await step('language-menu', async () => {
        await openMenu(p, 'EN');
        await S.view('language-menu');
        await p.keyboard.press('Escape');
        await wait(p, 300);
      });
      await step('button-hover', async () => {
        const cta = p.locator('header').getByRole('link', { name: 'Schedule a demo' }).first();
        await cta.hover();
        await wait(p, 400);
        await S.view('cta-hover');
        await p.mouse.move(8, 8);
      });
      await step('button-focus', async () => {
        const cta = p.locator('header').getByRole('link', { name: 'Schedule a demo' }).first();
        await cta.focus();
        await wait(p, 250);
        await S.view('cta-focus');
        await p.evaluate(() => document.activeElement && document.activeElement.blur());
      });
      await step('testimonial-2', async () => {
        const dot = p.getByRole('button', { name: 'Go to testimonial 2' });
        if (await dot.count()) {
          await dot.click();
          await wait(p, 700);
          await S.view('testimonial-2');
        }
      });
    });
  } },
  platform: { path: '/en/platform', run: async (p, S) => {
    await shotPage(p, S, async () => {
      await step('download', async () => {
        const b = p.getByRole('button', { name: /^Download$/ }).first();
        await b.scrollIntoViewIfNeeded();
        await b.click();
        await wait(p, 500);
        await S.view('download');
        await p.getByRole('button', { name: 'Close' }).first().click().catch(() => p.keyboard.press('Escape'));
        await wait(p, 300);
      });
      await step('faq', async () => {
        const b = p.getByRole('button', { name: /Do I need to upload/i }).first();
        await b.scrollIntoViewIfNeeded();
        await b.click();
        await wait(p, 400);
        await S.view('faq');
      });
    });
  } },
  'global-analytics': { path: '/en/global-analytics', run: async (p, S) => { await shotPage(p, S); } },
  'ai-agronomist': { path: '/en/ai-agronomist', run: async (p, S) => { await shotPage(p, S); } },
  farmers: { path: '/en/solutions/farmers', run: async (p, S) => { await shotPage(p, S); } },
  'soil-sampling': { path: '/en/solutions/soil-sampling', run: async (p, S) => { await shotPage(p, S); } },
  'agro-consulting': { path: '/en/solutions/agro-consulting', run: async (p, S) => { await shotPage(p, S); } },
  'machinery-dealers': { path: '/en/solutions/machinery-dealers', run: async (p, S) => { await shotPage(p, S); } },
  'input-suppliers': { path: '/en/solutions/input-suppliers', run: async (p, S) => { await shotPage(p, S); } },
  'field-force': { path: '/en/solutions/field-force-assistant', run: async (p, S) => { await shotPage(p, S); } },
  resources: { path: '/en/resources', run: async (p, S) => { await shotPage(p, S); } },
  'resources-learn': { path: '/en/resources/category/learn', run: async (p, S) => { await shotPage(p, S); } },
  article: { path: '/en/resources/what-is-ndvi', run: async (p, S) => { await shotPage(p, S); } },
  contact: { path: '/en/contact-us', run: async (p, S) => {
    await shotPage(p, S, async () => {
      await step('field-focus', async () => {
        const field = p.locator('input[name="name"]').first();
        await field.scrollIntoViewIfNeeded();
        await field.click();
        await wait(p, 300);
        await S.view('field-focus');
        await field.blur();
      });
    });
  } },
  demo: { path: '/en/contact-us?form=schedule_demo', run: async (p, S) => {
    await shotPage(p, S, async () => {
      await step('role', async () => {
        const chip = p.getByRole('button', { name: 'Agronomist' }).first();
        if (await chip.count()) {
          await chip.scrollIntoViewIfNeeded();
          await chip.click();
          await wait(p, 300);
          await S.view('role');
        }
      });
    });
  } },
  help: { path: 'https://help.onesoil.ai/en/', absolute: true, run: async (p, S) => { await shotPage(p, S); } },
  missing: { path: '/en/login', run: async (p, S) => { await hideOverlays(p); await S.view('default'); } },
};

const mobile = {
  home: { path: '/en', run: async (p, S) => {
    await hideOverlays(p);
    await S.view('default');
    await step('menu', async () => {
      await p.getByRole('button', { name: 'Open menu' }).click();
      await wait(p, 500);
      await S.view('menu');
      await p.locator('div.fixed').getByRole('button', { name: 'Products', exact: true }).first().click();
      await wait(p, 400);
      await S.view('products');
      await p.getByRole('button', { name: 'Close menu' }).click().catch(() => {});
      await wait(p, 300);
    });
    await S.full();
  } },
  platform: { path: '/en/platform', run: async (p, S) => { await shotPage(p, S); } },
  resources: { path: '/en/resources', run: async (p, S) => { await shotPage(p, S); } },
  contact: { path: '/en/contact-us', run: async (p, S) => { await shotPage(p, S); } },
  article: { path: '/en/resources/what-is-ndvi', run: async (p, S) => { await shotPage(p, S); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const url = spec.absolute ? spec.path : BASE + spec.path;
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await wait(p, spec.wait || 1800);
    await spec.run(p, S);
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
