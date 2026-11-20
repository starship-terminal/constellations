// Rebuilds the local page copies the capture scripts serve (SCRATCH/pages/<key>.html)
// from the Wayback snapshots listed in PAGES (lib.mjs): fetches each record raw
// (the id_ flavour carries no Wayback chrome), points the two CDN hosts at the
// local /cdn-static/ and /cdn-images/ prefixes (servePages mirrors those from
// web.archive.org on demand) strips every script, event handler and script URL, so nothing executes.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node prepare-pages.mjs [key ...]
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import { execFileSync } from 'node:child_process';
import { PAGES, SCRATCH } from './lib.mjs';
import { cleanTag } from './sanitize.mjs';

export function rewrite(html) {
  return html
    .replace(/<script\b[\s\S]*?<\/script\s*>/gi, '')
    .replace(/<script\b[^>]*\/?>/gi, '')
    .replace(/<link\b[^>]*\bas=["']?script["']?[^>]*>/gi, '')
    // inline handlers and script URLs run script too: every start tag is
    // re-read attribute by attribute (sanitize.mjs), and servePages adds a
    // script-src 'none' policy behind it (2026-11 audit; not run since)
    .replace(/<[a-zA-Z](?:"[^"]*"|'[^']*'|[^'">])*>/g, cleanTag)
    .replace(/(?:https?:)?\/\/cdn-static\.farfetch-contents\.com\//g, '/cdn-static/')
    .replace(/(?:https?:)?\/\/cdn-images\.farfetch-contents\.com\//g, '/cdn-images/');
}

const only = process.argv.slice(2);
fs.mkdirSync(path.join(SCRATCH, 'pages'), { recursive: true });
for (const [key, { url, ts }] of Object.entries(PAGES)) {
  if (only.length && !only.includes(key)) continue;
  // curl, not fetch: web.archive.org labels some plain records content-encoding: gzip, which fetch refuses to decode (curl --compressed fails too).
  let buf = execFileSync('curl', ['-sS', '-L', '--fail', '--max-time', '120', `https://web.archive.org/web/${ts}id_/${url}`], { maxBuffer: 64 << 20 });
  // Some records are stored gzipped with no usable Content-Encoding; they open with the gzip magic.
  if (buf[0] === 0x1f && buf[1] === 0x8b) buf = zlib.gunzipSync(buf);
  const html = rewrite(buf.toString('utf8'));
  fs.writeFileSync(path.join(SCRATCH, 'pages', `${key}.html`), html);
  console.log(key, html.length, 'bytes');
}
