// Re-shoots screenshots/ from the built gallery and records every focus-visible state.
// Needs Playwright with Chromium, which is not a package dependency: point PLAYWRIGHT_DIR
// at any folder whose node_modules holds it (default ~/.design-systems/pw).
//   node tools/screenshots.mjs            all shots
//   node tools/screenshots.mjs focus      only the focus crops and raw/focus-states.json
import fs from 'node:fs';
import http from 'node:http';
import os from 'node:os';
import path from 'node:path';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';

process.chdir(path.join(path.dirname(fileURLToPath(import.meta.url)), '..'));
const pwDir = process.env.PLAYWRIGHT_DIR || path.join(os.homedir(), '.design-systems/pw');
const {chromium} = createRequire(path.join(pwDir, 'package.json'))('playwright');
const only = process.argv[2];

const types = {'.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
  '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.png': 'image/png', '.md': 'text/plain'};
const server = http.createServer((req, res) => {
  const file = path.join(process.cwd(), decodeURIComponent(new URL(req.url, 'http://x').pathname));
  if (!file.startsWith(process.cwd()) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, {'content-type': types[path.extname(file)] || 'application/octet-stream'});
  fs.createReadStream(file).pipe(res);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}/style-guide.html`;

const sections = ['Overview', 'Colors', 'Typography', 'Geometry', 'Buttons', 'Badges and tags', 'Forms', 'Feedback',
  'Navigation', 'Surfaces', 'Data', 'Icons', 'Import', 'App shell', 'States'];
const slug = s => s.toLowerCase().replace(/ and /g, '-').replace(/ /g, '-');
const file = (i, s) => `${String(i + 1).padStart(2, '0')}-${slug(s)}.png`;

const browser = await chromium.launch();
async function open(section, {theme = 'light', width = 1440, height = 900, scale = 1} = {}) {
  const page = await browser.newPage({viewport: {width, height}, deviceScaleFactor: scale, reducedMotion: 'reduce'});
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') console.log(`[${section}] console ${m.type()}: ${m.text()}`); });
  page.on('pageerror', e => console.log(`[${section}] page error: ${e.message}`));
  await page.goto(`${base}${theme === 'light' ? '' : '?theme=' + theme}#${encodeURIComponent(section)}`);
  await page.waitForLoadState('networkidle');
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  return page;
}
const shoot = async (page, out, opts = {fullPage: true}) => {
  fs.mkdirSync(path.dirname(out), {recursive: true});
  await page.screenshot({path: out, animations: 'disabled', ...opts});
  console.log('wrote', out);
};

if (!only) {
  // Light desktop, one full page per section; the numbering matches the guide's navigation
  // up to 13, then the open states, then the two sections added on 2026-10-17.
  for (const [i, s] of sections.entries()) {
    if (i > 12) continue;
    const page = await open(s); await shoot(page, 'screenshots/' + file(i, s)); await page.close();
  }
  let page = await open('Surfaces');
  await page.getByRole('button', {name: 'Open example modal'}).click(); await page.getByRole('dialog').waitFor();
  await shoot(page, 'screenshots/14-modal-open.png', {}); await page.close();
  page = await open('Navigation');
  await page.getByRole('button', {name: 'More actions'}).click(); await page.getByText('Duplicate').waitFor();
  await shoot(page, 'screenshots/15-popover-open.png', {}); await page.close();
  page = await open('App shell'); await shoot(page, 'screenshots/16-app-shell.png');
  await page.getByRole('button', {name: 'Save', exact: true}).click(); await page.getByText('Product saved').waitFor();
  await shoot(page, 'screenshots/17-app-shell-toast.png');
  await page.getByRole('button', {name: 'Export'}).click(); await page.getByText('Export failed').waitFor();
  await shoot(page, 'screenshots/18-app-shell-error-toast.png'); await page.close();
  page = await open('States'); await shoot(page, 'screenshots/19-states.png');
  await page.getByRole('button', {name: 'Delete product'}).click(); await page.getByRole('dialog').waitFor();
  await shoot(page, 'screenshots/20-delete-confirm.png', {}); await page.close();
  page = await open('Feedback');
  await page.getByRole('button', {name: 'Hover or focus for help'}).hover(); await page.getByRole('tooltip').waitFor();
  await shoot(page, 'screenshots/21-tooltip-open.png', {}); await page.close();

  // dark-experimental and the phone width, for the sections that hold components.
  for (const s of ['Buttons', 'Badges and tags', 'Forms', 'Feedback', 'Navigation', 'Surfaces', 'Data', 'App shell', 'States']) {
    const i = sections.indexOf(s);
    page = await open(s, {theme: 'dark-experimental'}); await shoot(page, 'screenshots/dark/' + file(i, s)); await page.close();
    page = await open(s, {width: 390, height: 844}); await shoot(page, 'screenshots/phone/' + file(i, s)); await page.close();
  }
  page = await open('App shell', {width: 390, height: 844});
  await page.getByRole('button', {name: 'Toggle menu'}).click(); await page.getByRole('link', {name: 'Customers'}).waitFor();
  await page.waitForTimeout(400);
  // The open drawer locks page scroll, so a full-page shot stops at the viewport: shoot the shell itself.
  await page.locator('.shell').screenshot({path: 'screenshots/phone/14-app-shell-nav-open.png', animations: 'disabled'});
  console.log('wrote screenshots/phone/14-app-shell-nav-open.png'); await page.close();
}

// Focus-visible: press Tab once so the page is in keyboard modality, focus each control,
// and record every computed outline/box-shadow that changed on the control, its parent,
// its siblings and their pseudo-elements.
const targets = [
  ['button-primary', 'Buttons', p => p.getByRole('button', {name: 'Save product'})],
  ['button-secondary', 'Buttons', p => p.getByRole('button', {name: 'Cancel'})],
  ['button-tertiary', 'Buttons', p => p.getByRole('button', {name: 'Learn more'})],
  ['button-plain', 'Buttons', p => p.getByRole('button', {name: 'View details'})],
  ['button-critical', 'Buttons', p => p.getByRole('button', {name: 'Delete product'})],
  ['icon-button', 'Buttons', p => p.getByRole('button', {name: 'Search'})],
  ['button-segmented', 'Buttons', p => p.getByRole('button', {name: 'Week'})],
  ['tag-remove', 'Badges and tags', p => p.getByRole('button', {name: 'Remove Wholesale'})],
  ['text-field', 'Forms', p => p.getByLabel('Product title')],
  ['text-area', 'Forms', p => p.getByLabel('Description')],
  ['select', 'Forms', p => p.getByLabel('Status')],
  ['checkbox', 'Forms', p => p.getByLabel('Track quantity')],
  ['radio', 'Forms', p => p.getByLabel('Digital product')],
  ['range-slider', 'Forms', p => p.getByLabel('Discount')],
  ['tooltip-activator', 'Feedback', p => p.getByRole('button', {name: 'Hover or focus for help'})],
  // Tabs use a roving tabindex: only the selected tab takes focus.
  ['tab', 'Navigation', p => p.getByRole('tab', {name: 'All products'})],
  ['pagination', 'Navigation', p => p.getByRole('button', {name: 'Next'})],
  ['menu-activator', 'Navigation', p => p.getByRole('button', {name: 'More actions'})],
  ['nav-item', 'App shell', p => p.getByRole('link', {name: 'Products'})],
  ['list-row', 'App shell', p => p.getByRole('link', {name: 'View Everyday tote'})],
  ['list-row-checkbox', 'App shell', p => p.getByRole('checkbox', {name: /Everyday tote/})],
  ['search-field', 'App shell', p => p.getByPlaceholder('Search products')],
  ['link', 'States', p => p.getByRole('link', {name: 'a plain link'})],
];
const READ = (el) => {
  const props = ['outline-style', 'outline-width', 'outline-color', 'outline-offset', 'box-shadow', 'border-color', 'background-color'];
  const out = {};
  const nodes = [['self', el], ['parent', el.parentElement], ...[...(el.parentElement?.children || [])].filter(n => n !== el).map((n, i) => ['sibling' + i, n])];
  for (const [who, n] of nodes) for (const pseudo of [null, '::before', '::after']) {
    const cs = getComputedStyle(n, pseudo);
    if (pseudo && cs.content === 'none') continue;
    out[who + (pseudo || '') + ' .' + ([...n.classList].join('.') || n.tagName.toLowerCase())] = Object.fromEntries(props.map(k => [k, cs.getPropertyValue(k)]));
  }
  return out;
};
const results = {};
for (const [name, section, find] of targets) {
  const page = await open(section, {scale: 2});
  const el = find(page);
  try { await el.scrollIntoViewIfNeeded({timeout: 3000}); } catch (e) { results[name] = {section, error: 'not found: ' + e.message.split('\n')[0]}; console.log(name, 'NOT FOUND'); await page.close(); continue; }
  const before = await el.evaluate(READ);
  await page.keyboard.press('Tab');
  await el.focus();
  await page.waitForTimeout(200);
  const after = await el.evaluate(READ);
  const visible = await el.evaluate(e => e.matches(':focus-visible'));
  const changed = {};
  for (const [k, v] of Object.entries(after)) {
    const diff = Object.fromEntries(Object.entries(v).filter(([p, x]) => before[k]?.[p] !== x));
    if (Object.keys(diff).length) changed[k] = diff;
  }
  const box = await el.boundingBox();
  const pad = 16;
  const clip = {x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad), width: box.width + 2 * pad, height: box.height + 2 * pad};
  await shoot(page, `screenshots/focus/${name}.png`, {clip});
  results[name] = {section, focusVisible: visible, changed};
  await page.close();
}
fs.writeFileSync('raw/focus-states.json', JSON.stringify({
  method: 'Chromium via Playwright, 1440 px at 2x, light theme. Tab pressed once for keyboard modality, then the control focused; values are computed styles that differ from the unfocused control.',
  gallery: '@shopify/polaris 13.9.5', results}, null, 2) + '\n');
console.log('wrote raw/focus-states.json');
await browser.close();
server.close();
