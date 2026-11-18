// Fetches Macaw's Webflow stylesheet (cross-origin, so the CSSOM cannot read it)
// and records custom properties plus the button / nav / form rules.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const OUT = path.join(REF, 'raw', 'webflow-css.json');
const URL = 'https://cdn.prod.website-files.com/666ef0f57dd9231f728c9840/css/macaw-prod.webflow.7735a213d.min.css';
const res = await fetch(URL);
if (!res.ok) { console.error(res.status); process.exit(1); }
const css = await res.text();
const vars = [...css.matchAll(/(--[a-zA-Z0-9_-]+)\s*:\s*([^;}{]+)/g)].slice(0, 80).map((m) => [m[1], m[2].trim().slice(0, 120)]);
const interesting = [];
for (const sel of ['.button', '.button-secondary-gray', '.navbar_component', '.form-input', '.heading-style-h1', '.text-color-primary600', '.pricing-toggle-button', '.faq01_question']) {
  const i = css.indexOf(sel + '{');
  if (i >= 0) interesting.push({ sel, css: css.slice(i, i + 280) });
}
fs.writeFileSync(OUT, JSON.stringify({
  readAt: new Date().toISOString(),
  source: URL,
  bytes: css.length,
  varCount: vars.length,
  vars,
  interesting,
}, null, 2) + '\n');
console.log('bytes', css.length, 'vars', vars.length, 'rules', interesting.length);
