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
import { NextResponse, type NextRequest } from "next/server";

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

function refuse(status: number, error: string) {
  return NextResponse.json({ error }, { status });
}

export function proxy(request: NextRequest) {
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

  return NextResponse.next();
}
