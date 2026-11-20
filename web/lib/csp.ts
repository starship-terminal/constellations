// The Content-Security-Policy web/proxy.ts sends with every page. Package
// Markdown is written by unattended capture agents from third-party pages, so
// lib/markdown.ts's sanitizeHtml is the first wall; this policy is the second:
// if markup ever slips through, the browser still runs no script the server
// did not send, loads nothing from hosts the app does not use, and lets no
// other site frame the page.
//
// Scripts: Next attaches the per-request nonce to its own scripts (it reads it
// from this header on the request) and layout.tsx puts it on the theme script;
// 'strict-dynamic' then trusts the chunks those scripts load, so no host list
// is needed and no inline script without the nonce runs. Pages must be
// rendered per request for that, which layout.tsx's headers() call ensures.
//
// Styles: <style> and stylesheets need 'self' or the nonce, but style
// attributes are allowed (style-src-attr): React renders style={...} props
// into the server HTML as attributes, and a nonce cannot cover an attribute.
// sanitizeHtml drops style attributes from package Markdown, and a style
// attribute can load nothing from a host img-src and font-src do not list.
//
// Images and video: this origin's /media/, plus the two hosts the refero pages
// fall back to when a file is not mirrored locally: the media bucket
// (DESIGN_SYSTEMS_MEDIA_BASE, lib/repo.ts mediaBase) and refero's CDN
// (REFERO_CDN in tools/catalog.py). Package and docs Markdown use no remote
// images today.
//
// No upgrade-insecure-requests: the app is served over plain http on loopback
// and the tailnet, where upgrading its own requests to https would break them.
//
// `next dev` needs more: React's dev build uses eval for its error overlay,
// and the dev server injects <style> tags without a nonce for hot reload. So
// development adds 'unsafe-eval' to script-src and swaps the style nonce for
// 'unsafe-inline'. Production has neither.

/** refero's CDN origin; tools/catalog.py REFERO_CDN lives under it. */
export const REFERO_CDN_ORIGIN = "https://images.refero.design";

/** A fresh, unguessable nonce for one response. */
export function newNonce(): string {
  return Buffer.from(crypto.getRandomValues(new Uint8Array(16))).toString("base64");
}

/** The origin of an http(s) URL, or null (empty, relative or another scheme). */
function originOf(u: string): string | null {
  try {
    const url = new URL(u);
    return url.protocol === "https:" || url.protocol === "http:" ? url.origin : null;
  } catch {
    return null;
  }
}

export interface CspOptions {
  nonce: string;
  /** `next dev`: adds what React's dev build and hot reload need. */
  dev?: boolean;
  /** Base URL of mirrored refero media (mediaBase()); empty serves it from /media/. */
  mediaBase?: string;
}

export function contentSecurityPolicy({ nonce, dev = false, mediaBase = "" }: CspOptions): string {
  const media = ["'self'", ...new Set([originOf(mediaBase), REFERO_CDN_ORIGIN].filter((o): o is string => !!o))].join(" ");
  const directives = [
    "default-src 'self'",
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic'${dev ? " 'unsafe-eval'" : ""}`,
    `style-src 'self' ${dev ? "'unsafe-inline'" : `'nonce-${nonce}'`}`,
    "style-src-attr 'unsafe-inline'",
    `img-src ${media}`,
    `media-src ${media}`,
    "font-src 'self'",
    "connect-src 'self'",
    "frame-src 'none'",
    "worker-src 'none'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
  ];
  return directives.join("; ");
}

/** Paths that answer with a page (or a page's RSC payload) and so carry the
    policy. API routes answer JSON or text; /media/ files carry their own
    sandbox policy (app/media/[...path]/route.ts), which a page policy would
    break for a style guide's inline scripts; build assets need none. */
export function needsCsp(pathname: string): boolean {
  return !/^\/(api|media|_next\/static|_next\/image)(\/|$)/.test(pathname) && pathname !== "/favicon.ico";
}
