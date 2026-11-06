// GET /api/install.sh — cli/install.sh with @DS_BASE@ filled from the
// request's forwarded Host/proto, so `curl … | sh` installs a client that
// already knows this server's origin. Mirrors server/routes.py's handler.
import { promises as fs } from "node:fs";
import path from "node:path";
import { ROOT } from "@/lib/repo";

export const dynamic = "force-dynamic";

export async function GET(req: Request) {
  const target = path.join(ROOT, "cli", "install.sh");
  let script: string;
  try {
    script = await fs.readFile(target, "utf-8");
  } catch {
    return Response.json({ error: "cli/install.sh not in this checkout" }, { status: 404 });
  }
  const fwd = (n: string) => (req.headers.get(n) ?? "").split(",")[0].trim();
  const host = fwd("x-forwarded-host") || fwd("host");
  const proto = fwd("x-forwarded-proto") || new URL(req.url).protocol.replace(":", "");
  const base = host ? `${proto}://${host}` : new URL(req.url).origin;
  return new Response(script.replaceAll("@DS_BASE@", base), {
    headers: { "content-type": "text/x-shellscript; charset=utf-8", "cache-control": "no-store" },
  });
}
