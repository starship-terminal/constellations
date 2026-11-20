// Unit tests for the Content-Security-Policy (lib/csp.ts) and for web/proxy.ts
// attaching it to page responses (proxy.ts is loaded through
// lib/test/resolve-app.mjs, which resolves "@/" as Next does). Run with
// `pnpm test`.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { register } from "node:module";
import { before, describe, it } from "node:test";
import { contentSecurityPolicy, needsCsp, newNonce, REFERO_CDN_ORIGIN } from "./csp.ts";

register("./test/resolve-app.mjs", import.meta.url);

/** directive name -> its source list */
const parse = (csp: string) =>
  new Map(
    csp.split(";").map((d) => {
      const [name, ...sources] = d.trim().split(/\s+/);
      return [name, sources] as const;
    }),
  );

describe("contentSecurityPolicy in production", () => {
  const csp = parse(contentSecurityPolicy({ nonce: "abc123", mediaBase: "https://media.example/bucket" }));

  it("runs only scripts that carry the nonce", () => {
    assert.deepEqual(csp.get("script-src"), ["'self'", "'nonce-abc123'", "'strict-dynamic'"]);
  });

  it("names no unsafe-eval anywhere and no unsafe-inline for scripts or style elements", () => {
    for (const [name, sources] of csp) {
      assert.ok(!sources.includes("'unsafe-eval'"), `${name} allows eval`);
      if (name !== "style-src-attr") assert.ok(!sources.includes("'unsafe-inline'"), `${name} allows inline`);
    }
    assert.deepEqual(csp.get("style-src"), ["'self'", "'nonce-abc123'"]);
  });

  it("keeps the page out of frames and plugins and pins base and form targets", () => {
    assert.deepEqual(csp.get("frame-ancestors"), ["'none'"]);
    assert.deepEqual(csp.get("object-src"), ["'none'"]);
    assert.deepEqual(csp.get("base-uri"), ["'self'"]);
    assert.deepEqual(csp.get("form-action"), ["'self'"]);
    assert.deepEqual(csp.get("connect-src"), ["'self'"]);
    assert.deepEqual(csp.get("frame-src"), ["'none'"]);
  });

  it("loads images and video from this origin and the two refero media hosts only", () => {
    const media = ["'self'", "https://media.example", REFERO_CDN_ORIGIN];
    assert.deepEqual(csp.get("img-src"), media);
    assert.deepEqual(csp.get("media-src"), media);
  });

  it("names the CDN tools/catalog.py builds refero URLs from", () => {
    const py = readFileSync(new URL("../../tools/catalog.py", import.meta.url), "utf8");
    const cdn = /^REFERO_CDN = "([^"]+)"/m.exec(py)?.[1];
    assert.ok(cdn, "REFERO_CDN not found in tools/catalog.py");
    assert.equal(new URL(cdn).origin, REFERO_CDN_ORIGIN);
  });

  it("serves refero media from this origin alone when the media base is empty or not a URL", () => {
    for (const mediaBase of ["", "/media", "javascript:alert(1)"])
      assert.deepEqual(parse(contentSecurityPolicy({ nonce: "n", mediaBase })).get("img-src"), ["'self'", REFERO_CDN_ORIGIN]);
  });
});

describe("contentSecurityPolicy in development", () => {
  const csp = parse(contentSecurityPolicy({ nonce: "n", dev: true }));
  it("adds only what next dev needs", () => {
    assert.deepEqual(csp.get("script-src"), ["'self'", "'nonce-n'", "'strict-dynamic'", "'unsafe-eval'"]);
    assert.deepEqual(csp.get("style-src"), ["'self'", "'unsafe-inline'"]);
    assert.deepEqual(csp.get("frame-ancestors"), ["'none'"]);
  });
});

describe("newNonce", () => {
  it("is fresh base64 each time", () => {
    const a = newNonce();
    assert.match(a, /^[A-Za-z0-9+/]{22}==$/);
    assert.notEqual(a, newNonce());
  });
});

describe("needsCsp", () => {
  it("covers pages and leaves API, media and build assets alone", () => {
    for (const p of ["/", "/gallery", "/gallery/acme/files/systems/acme/README.md", "/settings", "/docs/CAPTURE", "/nope"])
      assert.equal(needsCsp(p), true, p);
    for (const p of ["/api/chat", "/api", "/media/systems/acme/style-guide.html", "/_next/static/chunks/a.js", "/_next/image", "/favicon.ico"])
      assert.equal(needsCsp(p), false, p);
    assert.equal(needsCsp("/mediafile"), true);
  });
});

describe("proxy", () => {
  type Proxy = (req: unknown) => Response;
  let proxy: Proxy;
  let NextRequest: new (url: string, init?: RequestInit) => unknown;
  before(async () => {
    ({ proxy } = (await import("../proxy.ts")) as { proxy: Proxy });
    ({ NextRequest } = (await import("next/server")) as unknown as { NextRequest: typeof NextRequest });
  });
  const get = (path: string) => proxy(new NextRequest(`http://127.0.0.1:8800${path}`, { headers: { host: "127.0.0.1:8800" } }));

  it("sends the policy on a page response, with a nonce for this response alone", () => {
    const a = get("/gallery").headers.get("content-security-policy");
    const b = get("/gallery").headers.get("content-security-policy");
    assert.ok(a, "no Content-Security-Policy on a page");
    const nonce = /'nonce-([^']+)'/.exec(a)?.[1];
    assert.ok(nonce);
    assert.ok(!b?.includes(nonce), "two responses shared a nonce");
    assert.doesNotMatch(a, /unsafe-eval/);
    assert.doesNotMatch(parse(a).get("script-src")!.join(" "), /unsafe-inline/);
  });

  it("forwards the nonce and the policy to the render", () => {
    const res = get("/");
    const csp = res.headers.get("content-security-policy")!;
    const nonce = /'nonce-([^']+)'/.exec(csp)![1];
    // NextResponse.next({ request: { headers } }) passes overridden request
    // headers to the render as x-middleware-request-<name>.
    assert.equal(res.headers.get("x-middleware-request-x-nonce"), nonce);
    assert.equal(res.headers.get("x-middleware-request-content-security-policy"), csp);
  });

  it("leaves media files with their own sandbox policy", () => {
    assert.equal(get("/media/systems/acme/style-guide.html").headers.get("content-security-policy"), null);
  });

  it("still refuses a foreign Host before any policy", () => {
    const res = proxy(new NextRequest("http://evil.test/", { headers: { host: "evil.test" } }));
    assert.equal(res.status, 403);
  });
});
