// Captures Monarch's public marketing pages (www.monarch.com) into RAW.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node shoot.mjs [name,name,...]
//
// Names are {page}-light-{state}.png. Phone shots get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Full pages are 1x.
// The cookie banner is hidden with CSS. Accept, Reject, and Save are never clicked.
// Sign-in, sign-up, onboarding, profile, survey, and newsletter forms are never filled or submitted.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'monarchmoney', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const BASE = 'https://www.monarch.com';
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const HIDE = `
  [class*="osano"], .osano-cm-window, .osano-cm-dialog { display: none !important; }
`;

async function hideBanner(p) {
  await p.addStyleTag({ content: HIDE }).catch(() => {});
  await p.evaluate(() => {
    const close = document.querySelector('[aria-label="Close this consent banner"]');
    let node = close;
    for (let i = 0; i < 12 && node; i++) {
      const t = node.innerText || '';
      const h = node.getBoundingClientRect().height;
      if (/cookies/i.test(t) && h > 20 && h < 800) {
        node.style.setProperty('display', 'none', 'important');
        break;
      }
      node = node.parentElement;
    }
    for (const el of document.querySelectorAll('[class*="osano"], [id*="osano"]')) {
      el.style.setProperty('display', 'none', 'important');
    }
  }).catch(() => {});
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); }
};

async function openFaq(p, label) {
  const b = p.getByRole('button', { name: label }).first();
  await b.scrollIntoViewIfNeeded();
  await b.click();
  await wait(p, 500);
}

async function clickNamed(p, name, { exact = true, role = 'button' } = {}) {
  const loc = role === 'button'
    ? p.getByRole('button', { name, exact })
    : p.getByRole(role, { name, exact });
  const n = await loc.count();
  for (let i = 0; i < n; i++) {
    const b = loc.nth(i);
    if (await b.isVisible().catch(() => false)) {
      await b.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' }));
      await wait(p, 200);
      await b.click({ timeout: 8000 });
      await wait(p, 450);
      return true;
    }
  }
  throw new Error('not visible: ' + name);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('banner');
    await hideBanner(p);
    await wait(p, 300);
    await S.view('default');
    await S.full();
    await step('features-menu', async () => {
      await p.getByRole('button', { name: 'Features', exact: true }).click();
      await wait(p, 600);
      await S.view('features-menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('tab-budget', async () => { await clickNamed(p, 'Budget'); await S.view('tab-budget'); });
    await step('tab-collaborate', async () => { await clickNamed(p, 'Collaborate'); await S.view('tab-collaborate'); });
    await step('tab-plan', async () => { await clickNamed(p, 'Plan'); await S.view('tab-plan'); });
    await step('tab-track', async () => { await clickNamed(p, 'Track'); await S.view('tab-track'); });
    await step('cta-hover', async () => {
      const cta = p.getByRole('link', { name: /Unlock better money habits|Get started today/ }).first();
      await cta.scrollIntoViewIfNeeded();
      await cta.hover();
      await wait(p, 400);
      await S.view('cta-hover');
    });
    await step('nav-signin-focus', async () => {
      const link = p.getByRole('link', { name: 'Sign in', exact: true }).first();
      await link.focus();
      await wait(p, 250);
      await S.view('signin-focus');
    });
  } },
  tracking: { path: '/features/tracking', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('faq', async () => { await openFaq(p, /How is my net worth calculated/); await S.view('faq-open'); });
  } },
  budgeting: { path: '/features/budgeting', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('category-tab', async () => { await clickNamed(p, 'Category Budgeting'); await S.view('tab-category'); });
    await step('faq', async () => { await openFaq(p, /How does Monarch/); await S.view('faq-open'); });
  } },
  planning: { path: '/features/planning', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('faq', async () => { await openFaq(p, /Can I set goals/); await S.view('faq-open'); });
  } },
  couples: { path: '/for-couples', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('faq', async () => { await openFaq(p, /How does Monarch work for couples/); await S.view('faq-open'); });
  } },
  professionals: { path: '/for-professionals', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('tab-coaches', async () => { await clickNamed(p, 'Money Coaches'); await S.view('tab-coaches'); });
    await step('faq', async () => { await openFaq(p, /How do I sign up for the Monarch Professionals/); await S.view('faq-open'); });
  } },
  'professionals-signup': { path: '/for-professionals/sign-up', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('row', async () => { await clickNamed(p, 'Tracking'); await S.view('row-tracking'); });
    await step('faq', async () => { await openFaq(p, /What is the cost of a subscription/); await S.view('faq-open'); });
    await step('cta-hover', async () => {
      const cta = p.getByRole('link', { name: /Try Monarch free/ }).first();
      await cta.scrollIntoViewIfNeeded();
      await cta.hover();
      await wait(p, 350);
      await S.view('cta-hover');
    });
  } },
  download: { path: '/download', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  blog: { path: '/blog', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  'blog-post': { path: '/blog/how-to-make-a-budget-and-stick-to-it', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
  } },
  about: { path: '/about', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('filter-design', async () => { await clickNamed(p, 'Design'); await S.view('filter-design'); });
  } },
  careers: { path: '/careers', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('dept-menu', async () => {
      await p.getByRole('button', { name: 'All departments' }).click();
      await wait(p, 500);
      await S.view('dept-menu');
      await p.keyboard.press('Escape');
    });
  } },
  press: { path: '/press', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  'whats-new': { path: '/whats-new', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  calculators: { path: '/calculators', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  'calc-health': { path: '/calculators/financial-health-calculator', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
  } },
  'calc-debt': { path: '/calculators/debt-payoff-calculator', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('strategy-menu', async () => {
      await p.getByRole('button', { name: /Avalanche/ }).click();
      await wait(p, 500);
      await S.view('strategy-menu');
      await p.keyboard.press('Escape');
    });
  } },
  'calc-mortgage': { path: '/calculators/mortgage-calculator', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('advanced', async () => { await clickNamed(p, 'Advanced'); await S.view('advanced'); });
  } },
  compare: { path: '/compare/mint-alternative', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('faq', async () => { await openFaq(p, /How do I transfer my Mint data/); await S.view('faq-open'); });
  } },
  directory: { path: '/professional-directory', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('filter', async () => { await clickNamed(p, 'Money Coach'); await S.view('filter-coach'); });
    await step('fee-dialog', async () => {
      const b = p.getByRole('button', { name: 'Hourly' }).first();
      await b.scrollIntoViewIfNeeded();
      await b.click();
      await wait(p, 600);
      await S.view('fee-dialog');
      await p.keyboard.press('Escape');
    });
  } },
  glossary: { path: '/personal-finance-term-glossary', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('filter', async () => { await clickNamed(p, 'Credit'); await S.view('filter-credit'); });
    await step('read-more', async () => {
      const b = p.getByRole('button', { name: /Read more/ }).first();
      await b.scrollIntoViewIfNeeded();
      await b.click();
      await wait(p, 400);
      await S.view('definition-open');
    });
  } },
  connections: { path: '/connection-status', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  canada: { path: '/canada', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  promos: { path: '/promo-codes', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  security: { path: '/security', run: async (p, S) => {
    await hideBanner(p); await S.view('default'); await S.full();
    await step('faq', async () => { await openFaq(p, /Can Monarch access or move money/); await S.view('faq-open'); });
  } },
  privacy: { path: '/privacy', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  terms: { path: '/terms', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
  optout: { path: '/opt-out-request-form', run: async (p, S) => { await hideBanner(p); await S.view('default'); await S.full(); } },
};

const mobilePages = ['home', 'pricing', 'tracking', 'blog', 'download', 'calculators', 'directory', 'about'];

const b = await chromium.launch({ headless: true });
let total = 0;
const runs = [
  ...Object.keys(desktop).map((k) => ({ k, mob: false })),
  ...mobilePages.map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const spec = desktop[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  const p = await ctx.newPage();
  log(name, spec.path);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const resp = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    log('  status', resp && resp.status(), 'url', p.url());
    await wait(p, 2500);
    if (mob) {
      await hideBanner(p);
      await S.view('default');
      await S.full();
      await step('menu', async () => {
        const menu = p.getByRole('button', { name: 'Open menu' });
        if (await menu.count()) {
          await menu.click();
          await wait(p, 600);
          await S.view('menu');
          await p.keyboard.press('Escape');
        }
      });
    } else {
      await spec.run(p, S);
    }
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
