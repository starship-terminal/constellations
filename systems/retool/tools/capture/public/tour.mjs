// Captures retool.com's public marketing pages into RAW (full-colour PNGs).
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x, phone 390x844 at 2x. Login, signup, Google, and every
// form submit are never used. A control that leaves for login.retool.com stops
// that branch. Cookie banners are hidden, never answered.
import fs from 'fs';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, chromium, UA, UA_MOBILE, BASE, LAUNCH_OPTS, patch } from './tour-lib.mjs';

const RAW = process.env.RAW || new URL('../../../../../../.design-systems/retool/raw-shots/', import.meta.url).pathname;
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 24000));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png`, animations: 'disabled' }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true, animations: 'disabled' }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`, fullPage: true, animations: 'disabled',
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

const step = async (label, fn) => {
  try { await fn(); } catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function openMenu(p, name) {
  const btn = p.locator('button').filter({ hasText: new RegExp('^' + name + '$') }).first();
  await btn.click({ timeout: 5000 });
  await wait(p, 700);
}

const PAGES = {
  home: '/',
  pricing: '/pricing',
  'use-cases': '/use-cases',
  'app-gallery': '/app-gallery',
  'gallery-item': '/app-gallery/github-development-analytics',
  build: '/build-enterprise-apps',
  launch: '/launch-enterprise-apps',
  scale: '/scale-enterprise-apps',
  govern: '/govern-enterprise-apps',
  agents: '/build-enterprise-apps/agents',
  apps: '/build-enterprise-apps/apps',
  ai: '/ai',
  workflows: '/build-enterprise-apps/workflows',
  database: '/build-enterprise-apps/database',
  external: '/launch-enterprise-apps/external',
  mobile: '/launch-enterprise-apps/mobile',
  'self-hosted': '/govern-enterprise-apps/self-hosted',
  security: '/secure-vibe-coding',
  'app-gen': '/ai-app-generation',
  data: '/for/data-teams',
  engineering: '/for/engineering-teams',
  operations: '/for/operations-teams',
  finance: '/for/financial-services',
  manufacturing: '/for/manufacturing',
  enterprise: '/enterprise',
  startups: '/startups',
  integrations: '/integrations',
  'integration-item': '/integrations/postgresql',
  templates: '/templates',
  'template-item': '/templates/postgresql-admin-panel',
  utilities: '/utilities',
  blog: '/blog',
  'blog-post': '/blog/retool-launches-react-ai-app-builder',
  customers: '/customers',
  'customer-story': '/customers/ramp',
  videos: '/resources/videos',
  resources: '/resources',
  about: '/about',
  careers: '/careers',
  partners: '/partners',
  newsroom: '/newsroom',
  demo: '/demo',
  waitlist: '/agents-waitlist',
  sitemap: '/sitemap-page',
  'use-case': '/use-case/admin-panels',
  competitor: '/competitor/airtable',
};

const desktopExtra = {
  home: async (p, S) => {
    await step('solution-menu', async () => {
      await openMenu(p, 'Solution');
      await S.view('solution-menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('audience-menu', async () => {
      await openMenu(p, 'Audience');
      await S.view('audience-menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('resources-menu', async () => {
      await openMenu(p, 'Resources');
      await S.view('resources-menu');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('ask-ai', async () => {
      await p.locator('button').filter({ hasText: /Ask AI/ }).first().click({ timeout: 4000 });
      await wait(p, 800);
      await S.view('ask-ai');
      await p.keyboard.press('Escape');
      await wait(p, 300);
    });
    await step('starter-prompts', async () => {
      await p.getByRole('button', { name: 'Starter prompts' }).first().click({ timeout: 4000 });
      await wait(p, 700);
      await S.view('starter-prompts');
      await p.keyboard.press('Escape');
    });
    await step('import-dialog', async () => {
      await p.getByRole('button', { name: 'Import code' }).first().click({ timeout: 4000 });
      await wait(p, 700);
      await S.view('import-dialog');
      await p.keyboard.press('Escape');
    });
    await step('agents-dialog', async () => {
      await p.getByRole('button', { name: 'Build with AI agents' }).first().click({ timeout: 4000 });
      await wait(p, 700);
      await S.view('agents-dialog');
      await p.keyboard.press('Escape');
    });
  },
  pricing: async (p, S) => {
    await step('faq', async () => {
      const q = p.locator('button').filter({ hasText: /\?$/ }).first();
      if (await q.count()) {
        await q.scrollIntoViewIfNeeded();
        await q.click();
        await wait(p, 500);
        await S.view('faq');
      }
    });
  },
};

const mobileExtra = {
  home: async (p, S) => {
    await step('menu', async () => {
      await p.getByRole('button', { name: 'Open navigation' }).click({ timeout: 4000 });
      await wait(p, 700);
      await S.view('menu');
      await step('solution', async () => {
        await p.locator('#global-nav-mobile-menu button').filter({ hasText: /^Solution$/ }).first().click();
        await wait(p, 500);
        await S.view('menu-solution');
      });
    });
  },
};

async function runSet(mobile) {
  const vw = mobile ? 390 : 1440;
  const vh = mobile ? 844 : 900;
  const dpr = mobile ? 2 : 1;
  const extra = mobile ? mobileExtra : desktopExtra;
  const browser = await chromium.launch(LAUNCH_OPTS);
  for (const [name, path] of Object.entries(PAGES)) {
    const key = (mobile ? 'mobile-' : '') + name;
    if (pageArg.length && !pageArg.includes(key) && !pageArg.includes(name)) continue;
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mobile ? UA_MOBILE : UA,
      isMobile: mobile,
      hasTouch: mobile,
      locale: 'en-US',
      reducedMotion: 'reduce',
    });
    await patch(ctx);
    const p = await ctx.newPage();
    const S = new Shooter(p, `${key}-dark`, vw, vh, dpr);
    log(key, path);
    try {
      const res = await p.goto(BASE + path, { waitUntil: 'domcontentloaded', timeout: 90000 });
      await wait(p, 2800);
      const landed = p.url();
      if (/login\.retool\.com/.test(landed)) {
        log('  STOP login wall', landed);
        await ctx.close();
        continue;
      }
      if (!res || res.status() >= 400) log('  status', res && res.status());
      await closePromo(p);
      await S.view('default');
      await S.full();
      if (extra[name]) await extra[name](p, S);
    } catch (e) {
      log('  PAGE FAILED', key, String(e.message || e).split('\n')[0]);
    }
    await ctx.close();
  }
  await browser.close();
}

const which = process.argv[3] || 'both';
if (which !== 'mobile') await runSet(false);
if (which !== 'desktop') await runSet(true);
log('done');
