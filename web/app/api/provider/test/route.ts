// POST /api/provider/test: list the provider's models with a newly typed key,
// or with the key the server already holds (only for the endpoint it is held
// for). See lib/provider-api.ts.
import { NextResponse } from "next/server";
import { listModels } from "@/lib/chat/chat";
import { handleTest } from "@/lib/provider-api";

export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  let body: unknown;
  try {
    body = await req.json();
  } catch {
    body = undefined;
  }
  const r = await handleTest(body, listModels);
  return NextResponse.json(r.body, { status: r.status, headers: { "cache-control": "no-store" } });
}
