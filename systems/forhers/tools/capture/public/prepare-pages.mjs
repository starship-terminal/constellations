// Rebuilds the local page copies the capture scripts serve (SCRATCH/pages/<key>.html)
// from the Wayback snapshots listed in PAGES (lib.mjs): fetches each record raw
// (the id_ flavour carries no Wayback chrome), strips every script, rewrites
// absolute asset URLs to the local prefixes servePages mirrors
// (/asset/<host>/ for off-site hosts, the site's own /css/ /forhims/ /image/
// paths stay relative and mirror from www.forhers.com).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node prepare-pages.mjs [key ...]
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import { execFileSync } from 'node:child_process';
import { PAGES, SCRATCH, ASSET_HOSTS } from './lib.mjs';
import { cleanTag } from './sanitize.mjs';

export function rewrite(html) {
  let out = html
    .replace(/<script\b[\s\S]*?<\/script\s*>/gi, '')
    .replace(/<script\b[^>]*\/?>/gi, '')
    .replace(/<link\b[^>]*\bas=["']?script["']?[^>]*>/gi, '')
    .replace(/<link\b[^>]*\brel=["']?preload["']?[^>]*\bas=["']?script["']?[^>]*>/gi, '')
    // inline handlers (onload=, onerror= ...) and script URLs run script too:
    // every start tag is re-read attribute by attribute (so <svg/onload=…>
    // and href="javascript: …" are caught), and the server adds a
    // script-src 'none' policy behind it
    .replace(/<[a-zA-Z](?:"[^"]*"|'[^']*'|[^'">])*>/g, cleanTag);
  for (const host of ASSET_HOSTS) {
    out = out.split(`https://${host}/`).join(`/asset/${host}/`);
    out = out.split(`http://${host}/`).join(`/asset/${host}/`);
    out = out.split(`//${host}/`).join(`/asset/${host}/`);
  }
  // Same-host absolute asset URLs resolve relative anyway; make them local so
  // the mirror serves them (srcset data holds https://www.forhers.com/forhims/…).
  out = out.replace(/https?:\/\/(?:www\.)?forhers\.com\/(css|forhims|image|fonts|shop|_next)\//g, '/$1/');
  return out;
}

const only = process.argv.slice(2);
fs.mkdirSync(path.join(SCRATCH, 'pages'), { recursive: true });
for (const [key, { url, ts }] of Object.entries(PAGES)) {
  if (only.length && !only.includes(key)) continue;
  // curl, not fetch: web.archive.org labels some plain records content-encoding: gzip, which fetch refuses to decode (curl --compressed fails too).
  let buf = execFileSync('curl', ['-sS', '-L', '--fail', '--max-time', '180', `https://web.archive.org/web/${ts}id_/${url}`], { maxBuffer: 96 << 20 });
  // Some records are stored gzipped with no usable Content-Encoding; they open with the gzip magic.
  if (buf[0] === 0x1f && buf[1] === 0x8b) buf = zlib.gunzipSync(buf);
  const html = rewrite(buf.toString('utf8'));
  fs.writeFileSync(path.join(SCRATCH, 'pages', `${key}.html`), html);
  console.log(key, html.length, 'bytes');
}
