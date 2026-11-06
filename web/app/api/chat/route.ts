// POST /api/chat — the librarian's endpoint. Keeps ANTHROPIC_API_KEY (or a
// browser-supplied provider config) server-side; runs the tool loop in
// lib/chat and enriches the returned results with card data for the UI.
import { NextResponse } from "next/server";
import { providerConfig, runChat, ProviderError } from "@/lib/chat/chat";
import { loadData, mediaUrl } from "@/lib/catalog";
import { loadReferoIndex } from "@/lib/refero";
import { markdown } from "@/lib/markdown";

export const dynamic = "force-dynamic";

const tintOf = (swatches: Record<string, { role: string; value: string | null }[]>) =>
  Object.values(swatches)
    .flat()
    .find((x) => /accent|primary|brand|face/i.test(x.role))?.value || undefined;

async function enrich(results: Record<string, unknown>[]) {
  const out = [];
  for (const r of results) {
    const card: Record<string, unknown> = {};
    try {
      if (r.store === "systems") {
        const data = await loadData();
        const s = data.systems.find((x) => x.slug === r.slug);
        if (s) {
          card.cover = mediaUrl(s.cover.thumb || s.cover.path);
          if (s.icon) card.icon = mediaUrl(s.icon);
          card.tint = tintOf(s.swatches);
          card.tagline = s.goodFor;
        }
      } else if (r.store === "refero") {
        const idx = await loadReferoIndex();
        const e = idx.styles.find((x) => x.slug === r.slug);
        if (e) {
          if (e.card) card.cover = `/media/refero-media/${e.card === "p" ? "posters" : "shots"}/${e.slug}.jpg`;
          else if (e.cardRemote) card.cover = e.cardRemote;
          card.icon = `/media/refero-media/favicons/${e.slug}.png`;
          card.tagline = e.tagline ?? undefined;
        }
      }
    } catch {
      // card enrichment is best-effort; a bare name link still works
    }
    out.push({ ...r, card });
  }
  return out;
}

export async function POST(req: Request) {
  let body: { messages?: { role: string; content: string }[]; provider?: Record<string, string> };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: "bad JSON" }, { status: 400 });
  }
  const cfg = providerConfig(body.provider);
  if (!cfg) return NextResponse.json({ error: "no_provider" });
  const messages = Array.isArray(body.messages) ? body.messages : [];
  try {
    const result = await runChat(messages, cfg);
    return NextResponse.json({
      ...result,
      reply: result.reply ? markdown(result.reply, { base: "chat" }) : "",
      results: await enrich(result.results),
    });
  } catch (e) {
    const msg = e instanceof ProviderError ? e.message : e instanceof Error ? e.message : String(e);
    return NextResponse.json({ error: msg });
  }
}
