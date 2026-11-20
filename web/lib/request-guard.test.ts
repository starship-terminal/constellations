// Unit tests for the rules web/proxy.ts applies to every request. The host
// cases are shared with tools/test_routes.py (server/front-door-cases.json),
// so the gallery and the Python /api/ server cannot drift apart again.
// Run with `pnpm test`.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { describe, it } from "node:test";
import { MCP_BODY_LIMIT } from "./mcp-batch.ts";
import { API_BODY_LIMIT, hostAllowed, refusal, type GuardRequest } from "./request-guard.ts";

const cases = JSON.parse(readFileSync(new URL("../../server/front-door-cases.json", import.meta.url), "utf8")) as {
  allowedHosts: string;
  hosts: { host: string; allowed: boolean }[];
};

describe("hostAllowed", () => {
  for (const c of cases.hosts)
    it(`${c.allowed ? "answers" : "refuses"} Host ${JSON.stringify(c.host)}`, () => {
      assert.equal(hostAllowed(c.host, cases.allowedHosts), c.allowed);
    });

  it("answers no Host header (not a browser)", () => {
    assert.equal(hostAllowed(null), true);
  });

  it("refuses an allowed-hosts name when the list is unset", () => {
    assert.equal(hostAllowed("designs.example.test"), false);
  });
});

const post = (over: Partial<GuardRequest> = {}): GuardRequest => ({
  method: "POST",
  pathname: "/api/chat",
  host: "127.0.0.1:8800",
  origin: "http://127.0.0.1:8800",
  secFetchSite: "same-origin",
  contentType: "application/json",
  contentLength: "20",
  ...over,
});
const status = (r: GuardRequest) => refusal(r)?.status ?? 200;

describe("refusal", () => {
  it("lets a same-origin JSON POST and any safe read through", () => {
    assert.equal(status(post()), 200);
    assert.equal(status(post({ method: "GET", contentType: null, contentLength: null, origin: "https://evil.test" })), 200);
  });

  it("refuses an unknown Host on reads too", () => {
    assert.deepEqual(refusal(post({ method: "GET", host: "evil.test" })), {
      status: 403,
      error: "unknown host: add it to DESIGN_SYSTEMS_ALLOWED_HOSTS",
    });
  });

  it("refuses cross-site and foreign-origin writes", () => {
    assert.equal(status(post({ secFetchSite: "cross-site" })), 403);
    assert.equal(status(post({ origin: "https://evil.test" })), 403);
    assert.equal(status(post({ origin: "null" })), 403);
    assert.equal(status(post({ origin: "http://127.0.0.1:8800/" })), 403);
  });

  it("lets a headerless client through", () => {
    assert.equal(status(post({ origin: null, secFetchSite: null })), 200);
  });

  it("needs application/json, by media type, not substring", () => {
    assert.equal(status(post({ contentType: "Application/JSON; charset=utf-8" })), 200);
    assert.equal(status(post({ contentType: "text/plain" })), 415);
    assert.equal(status(post({ contentType: "text/plain; application/json" })), 415);
    assert.equal(status(post({ contentType: null })), 415);
  });

  it("needs a numeric Content-Length on API routes only", () => {
    assert.equal(status(post({ contentLength: null })), 411);
    assert.equal(status(post({ contentLength: "ten" })), 411);
    assert.equal(status(post({ pathname: "/gallery/x", contentLength: null })), 200);
  });

  it("caps the body: 256 KB for /api/mcp as a JSON-RPC error, 128 KB elsewhere", () => {
    assert.equal(status(post({ contentLength: String(API_BODY_LIMIT) })), 200);
    assert.equal(status(post({ contentLength: String(API_BODY_LIMIT + 1) })), 413);
    assert.equal(status(post({ pathname: "/api/mcp", contentLength: String(MCP_BODY_LIMIT) })), 200);
    assert.deepEqual(refusal(post({ pathname: "/api/mcp", contentLength: String(MCP_BODY_LIMIT + 1) })), {
      status: 413,
      error: "",
      mcpTooLarge: true,
    });
  });

  it("lets DELETE (MCP session teardown) through without a body", () => {
    assert.equal(status(post({ method: "DELETE", pathname: "/api/mcp", contentType: null, contentLength: null })), 200);
    assert.equal(status(post({ method: "DELETE", origin: "https://evil.test" })), 403);
  });
});
