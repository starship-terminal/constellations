// POST /api/models — settings page "Test" button. Lists the provider's models
// for the config the page posted. It never falls back to the server's env
// key: the test is of the browser's own config, which needs no model yet.
import { NextResponse } from "next/server";
import { listModels } from "@/lib/chat/chat";
import { baseUrlOf } from "@/lib/provider-defaults";

export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  let body: { provider?: Record<string, string> };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ ok: false, error: "bad JSON" }, { status: 400 });
  }
  const p = body.provider && typeof body.provider === "object" ? body.provider : {};
  const base_url = baseUrlOf(p).replace(/\/+$/, "");
  if (!p.api_key || !base_url) return NextResponse.json({ ok: false, error: "no_provider" });
  return NextResponse.json(
    await listModels({ ...p, api: p.api || "openai", base_url, api_key: p.api_key, model: p.model || "" }),
  );
}
