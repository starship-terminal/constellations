// GET/POST/DELETE /api/provider: the chat's server-held model provider. The
// logic and its rules live in lib/provider-api.ts; this file only maps them
// onto Next's request and response.
import { NextResponse } from "next/server";
import { listModels } from "@/lib/chat/chat";
import { handleGet, handleRemove, handleSave } from "@/lib/provider-api";

export const dynamic = "force-dynamic";

const reply = (r: { status: number; body: Record<string, unknown> }) =>
  NextResponse.json(r.body, { status: r.status, headers: { "cache-control": "no-store" } });

const readJson = async (req: Request): Promise<unknown> => {
  try {
    return await req.json();
  } catch {
    return undefined;
  }
};

export async function GET() {
  return reply(await handleGet());
}

export async function POST(req: Request) {
  return reply(await handleSave(await readJson(req), listModels));
}

export async function DELETE() {
  return reply(await handleRemove());
}
