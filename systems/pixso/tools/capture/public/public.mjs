// Captures pixso.net public pages into RAW (full-colour PNGs).
//
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-light-{state}.png; mobile ones get a `mobile-` prefix.
// Desktop 1440x900 at 1x, phone 390x844 at 2x. One light theme.
// Nothing is submitted. Login, Google, NAVER and SSO are not clicked.
// Contact, newsletter and help-search fields are not typed into.
import fs from 'fs';
import path from 'node:path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';

const RAW = process.env.RAW || new URL('../../../../../.design-systems-placeholder', import.meta.url).pathname;
const RAWDIR = process.env.RAW || path.join(process.env.HOME, '.design-systems', 'pixso', 'raw-shots');
fs.mkdirSync(RAWDIR, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 12000));
  for (let y = 0; y < h; y += 700) { await p.evaluate((y) => scrollTo(0, y), y); await wait(p, 180); }
  await p.evaluate(() => scrollTo(0, 0)); await wait(p, 500);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    await screenshotWithMetadata(this.p, { path: `${RAWDIR}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAWDIR}/${this.prefix}-${name}`;
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    for (const old of fs.readdirSync(RAWDIR).filter((n) => n.startsWith(path.basename(f) + '.part'))) fs.unlinkSync(`${RAWDIR}/${old}`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };

async function openMenu(p, name) {
  const btn = p.getByRole('button', { name, exact: true }).first();
  if (!(await btn.count())) return false;
  await btn.hover({ timeout: 3000 });
  await wait(p, 600);
  return true;
}

async function openMobileMenu(p) {
  const btn = p.getByRole('button', { name: 'Open navigation menu' }).first();
  if (!(await btn.count())) return false;
  await btn.click();
  await wait(p, 700);
  return true;
}

const pageShot = (pathName) => ({ path: pathName, wait: 2500, run: async (p, S) => { await S.view('default'); await S.full(); } });

const desktop = {
  home: { path: '/', wait: 2800, run: async (p, S) => {
    await S.view('default');
    await step('product-menu', async () => { if (await openMenu(p, 'Product')) await S.view('product-menu'); await p.mouse.move(10, 800); await wait(p, 200); });
    await step('ai-menu', async () => { if (await openMenu(p, 'AI design')) await S.view('ai-menu'); await p.mouse.move(10, 800); await wait(p, 200); });
    await step('resources-menu', async () => { if (await openMenu(p, 'Resources & learning')) await S.view('resources-menu'); await p.mouse.move(10, 800); await wait(p, 200); });
    await step('enterprise-menu', async () => { if (await openMenu(p, 'Enterprise')) await S.view('enterprise-menu'); await p.mouse.move(10, 800); await wait(p, 200); });
    await step('cta-hover', async () => {
      const a = p.getByRole('link', { name: 'Get started', exact: true }).first();
      if (await a.count()) { await a.hover(); await wait(p, 300); await S.view('cta-hover'); }
    });
    await S.full();
  } },
  pricing: pageShot('/pricing/'),
  'ui-design': pageShot('/ui-design-collaboration/'),
  prototyping: pageShot('/prototyping/'),
  whiteboard: pageShot('/pixso-whiteboard/'),
  'design-system': pageShot('/design-system/'),
  'pixso-ai': pageShot('/pixso-ai-generator/'),
  mcp: pageShot('/pixso-mcp/'),
  'ai-design': pageShot('/ai-design-generator/'),
  'ai-ui': pageShot('/ai-ui-generator/'),
  'ai-web': pageShot('/ai-webpage-generator/'),
  'ai-app': pageShot('/ai-app-generator/'),
  enterprise: pageShot('/pixso-enterprise/'),
  'private-deployment': pageShot('/private-deployment/'),
  contact: pageShot('/contact-us/'),
  about: pageShot('/about/'),
  download: pageShot('/download/'),
  help: pageShot('/help/en/'),
  'help-design': pageShot('/help/en/design/'),
  developer: pageShot('/developer/en/'),
  articles: pageShot('/articles/'),
  tips: pageShot('/tips/'),
  releases: pageShot('/releases/'),
  plugins: pageShot('/plugins/'),
  community: pageShot('/community/home'),
  'community-library': pageShot('/community/home?classify=library'),
  'community-file': pageShot('/community/file/R8CXYv9rZuUoqacyhdpHqQ'),
  'plugin-detail': pageShot('/plugins/?id=ZQ1nImofnq3TrZDdTu-FnQ'),
  'vs-figma': pageShot('/pixso-vs-figma/'),
  'vs-sketch': pageShot('/pixso-vs-sketch/'),
  reviews: pageShot('/reviews/'),
  privacy: pageShot('/private-policy/'),
  terms: pageShot('/terms-conditions/'),
  brainstorming: pageShot('/brainstorming/'),
  'web-design': pageShot('/web-designing/'),
  'ux-design': pageShot('/ux-design-collaboration/'),
  lifetime: pageShot('/pixso-lifetime-plan/'),
  login: { path: '/user/login/', wait: 2500, run: async (p, S) => {
    // Wall only. Do not type, do not click Google, NAVER or SSO.
    await S.view('default');
    await S.full();
  } },
};

const mobile = {
  home: { path: '/', wait: 2500, run: async (p, S) => {
    await S.view('default');
    await step('menu-open', async () => { if (await openMobileMenu(p)) await S.view('menu-open'); });
    await S.full();
  } },
  pricing: pageShot('/pricing/'),
  'ui-design': pageShot('/ui-design-collaboration/'),
  'pixso-ai': pageShot('/pixso-ai-generator/'),
  enterprise: pageShot('/pixso-enterprise/'),
  contact: pageShot('/contact-us/'),
  download: pageShot('/download/'),
  help: pageShot('/help/en/'),
  community: pageShot('/community/home'),
  plugins: pageShot('/plugins/'),
  articles: pageShot('/articles/'),
  login: { path: '/user/login/', wait: 2500, run: async (p, S) => { await S.view('default'); } },
  whiteboard: pageShot('/pixso-whiteboard/'),
  prototyping: pageShot('/prototyping/'),
};

const b = await chromium.launch({ headless: true });
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
    const res = await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 45000 });
    log('  status', res && res.status(), p.url().replace(/https:\/\/pixso\.net/, ''));
    if (!(await clearChallenge(p))) { log('  BLOCKED', spec.path); await ctx.close(); continue; }
    await wait(p, spec.wait || 2000);
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, String(e.message).split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAWDIR);
await b.close();
