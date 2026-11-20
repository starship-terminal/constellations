// GET /api/status: what the page needs at boot. `configured` says whether the
// chat can run (a saved provider or the env key), `source` where its key
// comes from ("saved", "env" or "none"); `envProvider` is the older field the
// page read before keys moved server-side. No key is ever in the answer.
import { NextResponse } from "next/server";
import { providerState } from "@/lib/provider-api";

export const dynamic = "force-dynamic";

export async function GET() {
  let s;
  try {
    s = await providerState();
  } catch {
    return NextResponse.json({ envProvider: false, configured: false, source: "none", model: null });
  }
  return NextResponse.json(
    {
      envProvider: s.envAvailable,
      configured: s.configured,
      source: s.source,
      model: s.provider?.model ?? null,
      ...(s.error ? { error: s.error } : {}),
    },
    { headers: { "cache-control": "no-store" } },
  );
}
