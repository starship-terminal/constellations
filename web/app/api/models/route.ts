// POST /api/models — settings page "Test" button. Lists the provider's models
// through the same config normalisation the chat uses (posted cfg, else env).
import { NextResponse } from "next/server";
import { providerConfig, listModels } from "@/lib/chat/chat";

export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  let body: { provider?: Record<string, string> };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ ok: false, error: "bad JSON" }, { status: 400 });
  }
  const cfg = providerConfig(body.provider);
  if (!cfg) return NextResponse.json({ ok: false, error: "no_provider" });
  return NextResponse.json(await listModels(cfg));
}
