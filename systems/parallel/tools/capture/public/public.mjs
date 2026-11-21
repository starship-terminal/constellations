// Captures Parallel's public pages (useparallel.com) into RAW.
//
//   RAW=~/.design-systems/parallel/raw-shots PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/capture/public/public.mjs
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Nothing is submitted. Login,
// signup, LinkedIn, Google and Apple controls are not clicked. A wall URL is
// recorded in site-tree.md and that branch stops.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, closePromo } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'parallel', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const only = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 8 * 14000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr, source) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.source = source;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: source };
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    await lazyScroll(this.p);
    const H = await this.p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(14000 / this.dpr);
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${this.prefix}-${name}.part`))) fs.unlinkSync(`${RAW}/${old}`);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(this.p, { path: f + '.png', fullPage: true }, this.requested);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(this.p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
    }
    log('  shot', this.prefix, name, 'H=' + H);
    await this.p.evaluate(() => scrollTo(0, 0));
    await wait(this.p, 300);
  }
}

async function goto(p, route) {
  const res = await p.goto(BASE + route, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await wait(p, 2200);
  await closePromo(p);
  const status = res ? res.status() : 0;
  const title = await p.title();
  const wall = await p.evaluate(() => /password|continue with linkedin|sign in with linkedin|work email/i.test((document.body.innerText || '').slice(0, 600)));
  log('open', route, status, title.slice(0, 60), wall ? 'WALL' : '');
  return { status, wall, url: p.url() };
}

const desktop = [
  { name: 'home', route: '/', extra: async (p, S) => {
    await p.getByRole('button', { name: 'Explore', exact: true }).click();
    await wait(p, 500);
    await S.view('explore-menu');
    await p.keyboard.press('Escape');
    await wait(p, 300);
  } },
  { name: 'employers', route: '/employers', extra: async (p, S) => {
    await p.getByRole('button', { name: 'Overview', exact: true }).click();
    await wait(p, 500);
    await S.view('overview-menu');
    await p.keyboard.press('Escape');
    await wait(p, 200);
    const faq = p.getByRole('button', { name: /Is it free to post a job/ });
    if (await faq.count()) { await faq.click(); await wait(p, 400); await S.view('faq-open'); }
  } },
  { name: 'platform', route: '/employers/platform' },
  { name: 'recruiting', route: '/employers/recruiting' },
  { name: 'studio', route: '/employers/studio' },
  { name: 'ai-training', route: '/ai-training', extra: async (p, S) => {
    const faq = p.getByRole('button', { name: /What is AI training work/ });
    if (await faq.count()) { await faq.click(); await wait(p, 400); await S.view('faq-open'); }
  } },
  { name: 'work-form', route: '/work-form' },
  { name: 'manifesto', route: '/manifesto' },
  { name: 'blog', route: '/blog', extra: async (p, S) => {
    const cat = p.getByRole('link', { name: 'Careers', exact: true }).first();
    if (await cat.count()) { await cat.click(); await wait(p, 800); await S.view('category-careers'); }
  } },
  { name: 'blog-post', route: '/blog/the-quest-for-meaningful-work' },
  { name: 'pricing', route: '/pricing' },
  { name: 'search', route: '/app/candidate/search', extra: async (p, S) => {
    const filters = p.getByRole('button', { name: 'All Filters' });
    if (await filters.count()) { await filters.click(); await wait(p, 600); await S.view('filters'); await p.keyboard.press('Escape'); await wait(p, 300); }
    const companies = p.getByRole('button', { name: 'Companies', exact: true });
    if (await companies.count()) { await companies.first().click(); await wait(p, 900); await S.view('companies'); }
  } },
  { name: 'job', route: '/app/candidate/job/6aff911a9a678d5f427fedc8' },
  { name: 'company', route: '/company/vercel' },
  { name: 'paths', route: '/app/candidate/paths' },
  { name: 'companies', route: '/all-companies' },
  { name: 'collections', route: '/collections' },
  { name: 'case-studies', route: '/case-studies' },
  { name: 'case-study', route: '/case-studies/how-xano-did-it' },
  { name: 'resources', route: '/resources' },
  { name: 'help', route: '/help-center' },
  { name: 'release-notes', route: '/release-notes' },
  { name: 'careers', route: '/parallel/careers', extra: async (p, S) => {
    const loc = p.getByRole('button', { name: 'All Locations' });
    if (await loc.count()) { await loc.click(); await wait(p, 400); await S.view('location-filter'); await p.keyboard.press('Escape'); }
  } },
  { name: 'career-job', route: '/parallel/careers/6a8a319b9ab14e830c53514b' },
  { name: 'terms', route: '/about/terms' },
  { name: 'privacy', route: '/about/privacy' },
  { name: 'candidate-manifesto', route: '/about/candidatemanifesto' },
  { name: 'templates', route: '/templates' },
  { name: 'whats-next', route: '/whats-next' },
  { name: 'sync-jobs', route: '/sync-jobs' },
  { name: 'login-wall', route: '/login', wall: true },
  { name: 'employer-login-wall', route: '/employers/login', wall: true },
  { name: 'signup-wall', route: '/signup', wall: true },
];

const mobile = [
  { name: 'home', route: '/', extra: async (p, S) => {
    await p.getByRole('button', { name: 'Open menu' }).click();
    await wait(p, 600);
    await S.view('menu-open');
  } },
  { name: 'employers', route: '/employers' },
  { name: 'search', route: '/app/candidate/search' },
  { name: 'job', route: '/app/candidate/job/6aff911a9a678d5f427fedc8' },
  { name: 'ai-training', route: '/ai-training' },
  { name: 'blog', route: '/blog' },
  { name: 'pricing', route: '/pricing' },
  { name: 'work-form', route: '/work-form' },
  { name: 'careers', route: '/parallel/careers' },
];

const browser = await chromium.launch();
let total = 0;

async function runOne(spec, mob) {
  const prefix = (mob ? 'mobile-' : '') + spec.name + '-light';
  if (only.length && !only.includes(prefix) && !only.includes(spec.name) && !only.includes((mob ? 'mobile-' : '') + spec.name)) return;
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  const source = BASE + spec.route;
  const S = new Shooter(p, prefix, vw, vh, dpr, source);
  try {
    const info = await goto(p, spec.route);
    if (info.wall && !spec.wall) { log('  stopped at wall', info.url); }
    else {
      await S.view('default');
      if (!spec.wall) await S.full();
      if (spec.extra && !info.wall) await spec.extra(p, S);
    }
  } catch (e) { log('  FAILED', prefix, String(e.message).split('\n')[0]); }
  total += 1;
  await ctx.close();
}

for (const spec of desktop) await runOne(spec, false);
for (const spec of mobile) await runOne(spec, true);
log('done', total, 'pages ->', RAW);
await browser.close();
