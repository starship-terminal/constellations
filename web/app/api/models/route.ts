// POST /api/models: the older name of POST /api/provider/test, kept for a page
// loaded before the move. It takes {provider: {...}}, the shape that page
// posted, and applies the same rules (lib/provider-api.ts).
import { NextResponse } from "next/server";
import { listModels } from "@/lib/chat/chat";
import { handleTest } from "@/lib/provider-api";

export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  let body: { provider?: unknown } | undefined;
  try {
    body = await req.json();
  } catch {
    body = undefined;
  }
  const r = await handleTest(body && typeof body === "object" ? body.provider : undefined, listModels);
  return NextResponse.json(r.body, { status: r.status, headers: { "cache-control": "no-store" } });
}
