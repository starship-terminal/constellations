// Shared helpers for rendering the static Duolingo page copies (render.mjs).
// Adapted from the kit (tools/kit/capture/signed-in/lib.mjs) by way of systems/linear.
//
// A copy is a signed-in duolingo.com page with every stylesheet inlined (snapshot.js read them
// from the CSSOM), so what still comes from the network is images and fonts on Duolingo's two
// CloudFront hosts. Every response from those hosts is kept in a local cache directory the first
// time it is fetched (CDN_CACHE, default <SNAPS>-cdn-cache beside the copies) and served from
// there afterwards, so a re-run is offline and identical. Nothing is requested from duolingo.com
// itself or any other host: those requests are aborted.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

export const SNAPS = process.env.SNAPS ? path.resolve(process.env.SNAPS) : null;
export const CACHE = process.env.CDN_CACHE ? path.resolve(process.env.CDN_CACHE) : SNAPS && `${SNAPS}-cdn-cache`;

// PRODUCT (adapt): the hosts that serve the product's stylesheets, fonts and images.
const CDN = /^https:\/\/(d35aaqx5ub95lt|d3gq3s1iyyx31w)\.cloudfront\.net\//;

// Duolingo registers its faces from script (new FontFace), and a copy has no scripts, so the
// faces are declared again here from the same CDN files the live page loaded (see tokens-notes.md,
// Fonts). Without this a copy renders in the fallback sans-serif.
export const FONTS = `
@font-face{font-family:duolingo-sans;font-weight:100 900;font-style:normal;src:url(https://d35aaqx5ub95lt.cloudfront.net/vendor/f2331bbfd902cdf8971c4d3184a44283.woff2) format("woff2")}
@font-face{font-family:duolingo-sans;font-weight:100 900;font-style:italic;src:url(https://d35aaqx5ub95lt.cloudfront.net/vendor/3bbe299f41d8289a47d91773fee0cb6a.woff2) format("woff2")}
@font-face{font-family:feather;font-weight:700;src:url(https://d35aaqx5ub95lt.cloudfront.net/vendor/68d22534874c554b0c9ebabea379fc60.woff2) format("woff2")}
*{caret-color:transparent!important}`;

export async function routeCdn(ctx) {
  if (!CACHE) throw new Error('set SNAPS (the directory of page copies) or CDN_CACHE');
  fs.mkdirSync(CACHE, { recursive: true });
  await ctx.route('**/*', async (route) => {
    const url = route.request().url();
    if (url.startsWith('file:') || url.startsWith('data:') || url.startsWith('blob:')) return route.continue();
    if (!CDN.test(url) || route.request().method() !== 'GET') return route.abort();
    const key = crypto.createHash('sha1').update(url).digest('hex');
    const body = path.join(CACHE, key);
    const meta = body + '.json';
    if (fs.existsSync(meta)) {
      const m = JSON.parse(fs.readFileSync(meta, 'utf8'));
      return route.fulfill({ status: m.status, headers: m.headers, body: fs.readFileSync(body) });
    }
    try {
      const res = await route.fetch({ timeout: 30000 });
      const buf = await res.body();
      const headers = { 'content-type': res.headers()['content-type'] || 'application/octet-stream', 'access-control-allow-origin': '*' };
      if (res.status() === 200) {
        fs.writeFileSync(body, buf);
        fs.writeFileSync(meta, JSON.stringify({ url, status: 200, headers }));
      }
      return route.fulfill({ status: res.status(), headers, body: buf });
    } catch {
      return route.abort();
    }
  });
}
