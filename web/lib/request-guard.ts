// The request rules web/proxy.ts applies before any route runs, kept free of
// next/server so the node test runner can load them. The host rule is the one
// server/routes.py applies; server/front-door-cases.json holds the cases both
// test suites run.
import { MCP_BODY_LIMIT } from "./mcp-batch.ts";

// Request body caps, the same as server/routes.py: 256 KB for /api/mcp, 128 KB
// for every other API route (chat and models take a JSON body of messages and
// provider settings).
export const API_BODY_LIMIT = 128_000;

export const bodyLimit = (pathname: string): number => (pathname === "/api/mcp" ? MCP_BODY_LIMIT : API_BODY_LIMIT);

// "name:port" -> [name, port]; brackets keep an IPv6 literal's colons. null
// when the value is not a host with an optional numeric port.
function splitHost(value: string): [string, string] | null {
  const m = /^(\[[^\]]*\]|[^:[\]]*)(?::(\d{1,5}))?$/.exec(value.trim().toLowerCase());
  if (!m || !m[1]) return null;
  if (m[2] !== undefined && Number(m[2]) > 65535) return null;
  return [m[1], m[2] ?? ""];
}

const IPV4 = /^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$/;

function isIpLiteral(name: string): boolean {
  if (IPV4.test(name)) return true;
  if (!/^\[[0-9a-f:.]+\]$/.test(name)) return false;
  try {
    return new URL(`http://${name}/`).hostname.length > 2;
  } catch {
    return false;
  }
}

/**
 * Whether to answer a request addressed to `host` (the Host header). DNS
 * rebinding makes an attacker's page same-origin with this app, so the name
 * must be one an attacker cannot point at this machine: loopback names
 * (localhost, *.localhost), IP literals, Tailscale's *.ts.net, or an entry of
 * DESIGN_SYSTEMS_ALLOWED_HOSTS (`allowed`: comma-separated `name`, any port,
 * or `name:port`; case-insensitive). No Host at all is not a browser and
 * passes, as in server/routes.py.
 */
export function hostAllowed(host: string | null, allowed = ""): boolean {
  if (host === null || host.trim() === "") return true;
  if (/[\s/\\?#@,]/.test(host)) return false;
  const parts = splitHost(host);
  if (!parts) return false;
  const [name, port] = parts;
  if (name === "localhost" || name.endsWith(".localhost") || name.endsWith(".ts.net") || isIpLiteral(name)) return true;
  return allowed
    .split(",")
    .map((x) => x.trim())
    .filter(Boolean)
    .some((entry) => {
      const e = splitHost(entry);
      return !!e && e[0] === name && (!e[1] || e[1] === port);
    });
}

// The essence of a MIME type: "Application/JSON; charset=utf-8" ->
// "application/json". A substring test would pass "text/plain;
// application/json", which browsers still send without a preflight.
export const mediaType = (value: string | null) => (value ?? "").split(";")[0].trim().toLowerCase();

export function sameOrigin(origin: string, host: string | null): boolean {
  if (!host) return false;
  try {
    const url = new URL(origin);
    // "null" (sandboxed frames, file: pages) does not parse and is refused.
    return (url.protocol === "http:" || url.protocol === "https:") && url.origin === origin && url.host === host.toLowerCase();
  } catch {
    return false;
  }
}

export interface GuardRequest {
  method: string;
  pathname: string;
  host: string | null;
  origin: string | null;
  secFetchSite: string | null;
  contentType: string | null;
  contentLength: string | null;
}

/** Why the request is refused, or null to let it through. `mcpTooLarge`
    asks the caller for the JSON-RPC 413 body instead of a plain error. */
export type Refusal = { status: number; error: string; mcpTooLarge?: boolean };

const SAFE_METHODS = new Set(["GET", "HEAD", "OPTIONS"]);

export function refusal(r: GuardRequest, allowedHosts = ""): Refusal | null {
  if (!hostAllowed(r.host, allowedHosts))
    return { status: 403, error: "unknown host: add it to DESIGN_SYSTEMS_ALLOWED_HOSTS" };
  if (SAFE_METHODS.has(r.method)) return null;
  if (r.secFetchSite === "cross-site") return { status: 403, error: "Cross-site requests are not allowed." };
  // The Host header is what the browser addressed; forwarded headers are
  // client-controlled and never used here.
  if (r.origin !== null && !sameOrigin(r.origin, r.host))
    return { status: 403, error: "This request must come from this app's own origin." };
  // DELETE carries no body (MCP session teardown) and is never a simple
  // request, so a browser cannot send it cross-site without a preflight.
  if (r.method === "DELETE") return null;
  if (mediaType(r.contentType) !== "application/json") return { status: 415, error: "Send application/json." };
  if (r.pathname.startsWith("/api/")) {
    // A request with no Content-Length (chunked) is not trusted to be small.
    if (r.contentLength === null || !/^\d+$/.test(r.contentLength.trim())) return { status: 411, error: "Send a Content-Length." };
    if (Number(r.contentLength) > bodyLimit(r.pathname))
      return r.pathname === "/api/mcp"
        ? { status: 413, error: "", mcpTooLarge: true }
        : { status: 413, error: "The request body is too large." };
  }
  return null;
}
