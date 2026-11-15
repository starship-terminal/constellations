// Runs before every route. The app has no login and its API spends the
// server's provider key (ANTHROPIC_API_KEY from .env), so a request that
// changes or costs something must come from this app's own pages or from a
// non-browser client (the ds CLI, MCP hosts, curl), never from another site.
//
// A cross-site page can POST to 127.0.0.1:8800 without a CORS preflight as
// long as the body is a "simple" content type (text/plain, form data), so the
// guard requires application/json, which forces a preflight this app never
// answers. Browsers also send Origin and Sec-Fetch-Site on such requests;
// either one naming another site is rejected. Non-browser clients send
// neither header and pass. The same rules as app/'s mutationGuard
// (app/src/server/research/http.ts).
//
// Every request, reads included, must also name an allowed Host. Without
// that, DNS rebinding (an attacker's name re-pointed at 127.0.0.1) makes the
// attacker's page same-origin with this app, so the checks below pass and it
// can read the library and spend the key. Loopback names on any port are
// always allowed; DESIGN_SYSTEMS_ALLOWED_HOSTS adds more, comma-separated,
// each `name` (any port) or `name:port`, case-insensitive: the same format
// server/routes.py reads. Unset means loopback only.
import { MCP_BODY_LIMIT, tooLarge } from "@/lib/mcp-batch";
import { NextResponse, type NextRequest } from "next/server";
// Loads the repo-root .env, where DESIGN_SYSTEMS_ALLOWED_HOSTS may live.
import "@/lib/env";

const LOOPBACK = /^(localhost|127\.0\.0\.1|\[::1\])(:\d{1,5})?$/i;

// "Name:port" -> [name, port]; brackets keep an IPv6 literal's colons.
function splitHost(value: string): [string, string] {
  const m = /^(\[[^\]]*\]|[^:]*)(?::(\d*))?$/.exec(value.trim().toLowerCase());
  return m ? [m[1], m[2] ?? ""] : ["", ""];
}

function hostAllowed(host: string | null): boolean {
  if (!host || /[\s/\\?#@,]/.test(host)) return false;
  if (LOOPBACK.test(host)) return true;
  const [name, port] = splitHost(host);
  if (!name) return false;
  return (process.env.DESIGN_SYSTEMS_ALLOWED_HOSTS ?? "")
    .split(",")
    .map((x) => x.trim())
    .filter(Boolean)
    .some((entry) => {
      const [n, p] = splitHost(entry);
      return n === name && (!p || p === port);
    });
}

const SAFE_METHODS = new Set(["GET", "HEAD", "OPTIONS"]);

// The essence of a MIME type: "Application/JSON; charset=utf-8" ->
// "application/json". A substring test would pass "text/plain;
// application/json", which browsers still send without a preflight.
const mediaType = (value: string | null) =>
  (value ?? "").split(";")[0].trim().toLowerCase();

function sameOrigin(origin: string, host: string | null): boolean {
  if (!host) return false;
  try {
    const url = new URL(origin);
    // "null" (sandboxed frames, file: pages) does not parse and is refused.
    return (
      (url.protocol === "http:" || url.protocol === "https:") &&
      url.origin === origin &&
      url.host === host.toLowerCase()
    );
  } catch {
    return false;
  }
}

// Request body caps, the same as server/routes.py: 256 KB for /api/mcp, 128 KB
// for every other API route (chat and models take a JSON body of messages and
// provider settings). Checked against Content-Length before any route reads
// the body. A request with no Content-Length (chunked) is not trusted to be
// small: it is refused with 411 so a client cannot stream past the cap.
const API_BODY_LIMIT = 128_000;

function bodyLimit(pathname: string): number {
  return pathname === "/api/mcp" ? MCP_BODY_LIMIT : API_BODY_LIMIT;
}

function refuse(status: number, error: string) {
  return NextResponse.json({ error }, { status });
}

export function proxy(request: NextRequest) {
  if (!hostAllowed(request.headers.get("host")))
    return refuse(403, "This app only answers loopback hosts or DESIGN_SYSTEMS_ALLOWED_HOSTS.");

  if (SAFE_METHODS.has(request.method)) return NextResponse.next();

  if (request.headers.get("sec-fetch-site") === "cross-site")
    return refuse(403, "Cross-site requests are not allowed.");

  const origin = request.headers.get("origin");
  // The Host header is what the browser addressed; request.url can be
  // normalised to localhost. Forwarded headers are client-controlled and
  // never used here.
  if (origin !== null && !sameOrigin(origin, request.headers.get("host")))
    return refuse(403, "This request must come from this app's own origin.");

  // DELETE carries no body (MCP session teardown) and is never a simple
  // request, so a browser cannot send it cross-site without a preflight.
  if (request.method !== "DELETE" && mediaType(request.headers.get("content-type")) !== "application/json")
    return refuse(415, "Send application/json.");

  if (request.method !== "DELETE" && request.nextUrl.pathname.startsWith("/api/")) {
    const length = request.headers.get("content-length");
    if (length === null || !/^\d+$/.test(length.trim()))
      return refuse(411, "Send a Content-Length.");
    if (Number(length) > bodyLimit(request.nextUrl.pathname))
      // /api/mcp speaks JSON-RPC, so its refusal is a JSON-RPC error.
      return request.nextUrl.pathname === "/api/mcp"
        ? NextResponse.json(tooLarge(), { status: 413 })
        : refuse(413, "The request body is too large.");
  }

  return NextResponse.next();
}
