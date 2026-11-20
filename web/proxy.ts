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
// can read the library and spend the key. The host rule is server/routes.py's
// (loopback names, IP literals, *.ts.net, DESIGN_SYSTEMS_ALLOWED_HOSTS), and
// server/front-door-cases.json holds the cases both test suites run. The
// rules themselves live in lib/request-guard.ts so they can be unit-tested.
//
// Two rules are this app's alone: POST needs application/json (server/routes.py
// relies on its Origin check for browsers instead) and an API body needs a
// Content-Length (411), where routes.py reads a missing one as an empty body.
import { tooLargeResponse } from "@/lib/mcp-batch";
import { refusal } from "@/lib/request-guard";
import { NextResponse, type NextRequest } from "next/server";
// Loads the repo-root .env, where DESIGN_SYSTEMS_ALLOWED_HOSTS may live.
import "@/lib/env";

export function proxy(request: NextRequest) {
  const h = request.headers;
  const refused = refusal(
    {
      method: request.method,
      pathname: request.nextUrl.pathname,
      host: h.get("host"),
      origin: h.get("origin"),
      secFetchSite: h.get("sec-fetch-site"),
      contentType: h.get("content-type"),
      contentLength: h.get("content-length"),
    },
    process.env.DESIGN_SYSTEMS_ALLOWED_HOSTS ?? "",
  );
  if (!refused) return NextResponse.next();
  // /api/mcp speaks JSON-RPC, so its oversize refusal is a JSON-RPC error.
  if (refused.mcpTooLarge) return tooLargeResponse();
  return NextResponse.json({ error: refused.error }, { status: refused.status });
}
