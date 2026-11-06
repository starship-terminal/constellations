// GET /api/status — what the page needs at boot: whether the server itself can
// drive the chat (env ANTHROPIC_API_KEY) so the UI can hide or enable it.
import { NextResponse } from "next/server";

export const dynamic = "force-dynamic";

export function GET() {
  return NextResponse.json({
    envProvider: !!process.env.ANTHROPIC_API_KEY,
    model: process.env.ANTHROPIC_API_KEY ? process.env.DS_CHAT_MODEL || "claude-sonnet-4-5" : null,
  });
}
