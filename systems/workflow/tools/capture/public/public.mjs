// Captures Workflow's public marketing site into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [name,name,...]
//
// Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x and take a
// mobile- prefix. Nothing is submitted. Auth and sign-up URLs are recorded
// and not walked. Forms are not filled.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, isAuth } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'workflow', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const FEATURES = [
  'comments', 'approval-button-a-signal-that-your-work-is-complete', 'get-feedback-from-anyone',
  'version-naming', 'shareable-links', 'add-comments-to-videos', 'add-comments-to-websites',
  'check-boxes', 'introducing-the-command-bar', 'figma-plugin-v3', 'search', 'workflow-ai',
  'say-hello-to-our-free-starter-plan', 'task-labels', 'private-projects',
];

const PAGES = {
  home: '/',
  features: '/features',
  about: '/about',
  pricing: '/pricing',
  contact: '/contact',
  policies: '/policies',
  help: '/help',
  referral: '/referral-program',
  careers: '/backups-templates/careers',
  'not-found': '/login',
  'compare-markup': '/compare/workflow-vs-markup',
  'compare-ruttl': '/compare/workflow-vs-ruttl',
  'compare-bugherd': '/compare/workflow-vs-bugherd',
  'compare-pastel': '/compare/workflow-vs-pastel',
  'compare-loom': '/compare/workflow-vs-loom',
  'story-summon': '/community-stories-new/summonstudio',
  'story-adria': '/community-stories-new/adria-studio',
  'resource-loom': '/resources/how-to-leave-loom',
  'team-sophia': '/team/sophia-oneal',
  'help-article': '/help/what-reviewers-see-3ferr',
  'feature-comments': '/features/comments',
  'feature-command-bar': '/features/introducing-the-command-bar',
};

for (const slug of FEATURES) PAGES['feat-' + slug.replace(/[^a-z0-9]+/g, '-').slice(0, 40)] = '/features/' + slug;

async function lazyScroll(p) {
  let h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 9000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
    h = await p.evaluate(() => document.documentElement.scrollHeight);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.vh = vh; this.dpr = dpr;
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
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(path.basename(f) + '.part'))) fs.unlinkSync(path.join(RAW, old));
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
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

async function hideBanners(p) {
  await p.addStyleTag({ content: '.downtime-banner,.referral-banner,.affiliate-banner,.announcement{display:none!important}' }).catch(() => {});
}

async function shotInteractions(p, S, { mobile }) {
  await S.view('default');
  if (!mobile) {
    await step('nav-hover', async () => {
      const link = p.locator('a.nav--item.expanded', { hasText: 'Features' }).first();
      if (await link.count()) {
        await link.hover();
        await wait(p, 350);
        await S.view('nav-features-hover');
        await p.mouse.move(8, 8);
        await wait(p, 200);
      }
    });
    await step('button-hover', async () => {
      const btn = p.locator('a.button--new, a.button').first();
      if (await btn.count() && await btn.isVisible()) {
        await btn.hover();
        await wait(p, 300);
        await S.view('cta-hover');
        await p.mouse.move(8, 8);
      }
    });
  } else {
    await step('menu', async () => {
      const toggle = p.locator('a.nav--menu, .nav--menu').first();
      if (await toggle.count() && await toggle.isVisible()) {
        await toggle.click();
        await wait(p, 600);
        await S.view('menu-open');
        await toggle.click().catch(() => {});
        await wait(p, 400);
      }
    });
  }
  await S.full();
}

async function homeExtras(p, S, { mobile }) {
  await step('tabs', async () => {
    for (const label of ['Figma', 'Images', 'Videos', 'Presentations']) {
      const tab = p.getByRole('tab', { name: label }).first();
      if (await tab.count()) {
        await tab.click();
        await wait(p, 500);
        await S.view('tab-' + label.toLowerCase());
      }
    }
    const live = p.getByRole('tab', { name: 'Live websites' }).first();
    if (await live.count()) await live.click();
  });
  await step('motion', async () => {
    const pause = p.locator('#feedback-video-bar-play, a.accessibility--motion-button').first();
    if (await pause.count() && await pause.isVisible()) {
      await pause.click();
      await wait(p, 400);
      await S.view('motion-paused');
      await pause.click().catch(() => {});
    }
  });
  await step('demo', async () => {
    const watch = p.locator('a, button').filter({ hasText: 'Watch demo' }).first();
    if (await watch.count() && await watch.isVisible()) {
      await watch.scrollIntoViewIfNeeded();
      await watch.click();
      await wait(p, 900);
      await S.view('demo-open');
      const close = p.locator('.video--overlay-close').first();
      if (await close.count()) await close.click({ force: true }).catch(() => p.keyboard.press('Escape'));
      else await p.keyboard.press('Escape');
      await wait(p, 400);
    }
  });
  if (!mobile) {
    await step('testimonials', async () => {
      const tab = p.getByRole('tab', { name: 'Reviewers' }).first();
      if (await tab.count()) {
        await tab.scrollIntoViewIfNeeded();
        await tab.click();
        await wait(p, 500);
        await S.view('testimonials-reviewers');
      }
    });
  }
}

const b = await chromium.launch();
let total = 0;
const keys = Object.keys(PAGES);
const runs = [
  ...keys.map((k) => ({ k, mob: false })),
  ...['home', 'features', 'pricing', 'about', 'help', 'contact', 'policies'].map((k) => ({ k, mob: true })),
];

for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
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
  log(name, PAGES[k]);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    const res = await p.goto(BASE + PAGES[k], { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, 1600);
    if (isAuth(p.url())) {
      log('  AUTH WALL', p.url(), 'stopping branch');
      await ctx.close();
      continue;
    }
    log('  status', res?.status(), 'final', p.url().replace(BASE, ''));
    await hideBanners(p);
    if (k === 'home') await homeExtras(p, S, { mobile: mob });
    await shotInteractions(p, S, { mobile: mob });
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
