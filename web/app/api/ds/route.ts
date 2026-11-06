// GET /api/ds — the ds CLI client (cli/ds in the checkout), verbatim. install.sh
// curls this into ~/.local/bin. Mirrors server/routes.py's /api/ds.
import { promises as fs } from "node:fs";
import path from "node:path";
import { ROOT } from "@/lib/repo";

export const dynamic = "force-dynamic";

export async function GET() {
  const target = path.join(ROOT, "cli", "ds");
  try {
    const body = await fs.readFile(target);
    return new Response(new Uint8Array(body), {
      headers: { "content-type": "text/plain; charset=utf-8", "cache-control": "no-store" },
    });
  } catch {
    return Response.json({ error: "cli/ds not in this checkout" }, { status: 404 });
  }
}
