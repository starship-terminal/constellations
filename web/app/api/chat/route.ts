// POST /api/chat — the librarian's endpoint. The provider key is held by the
// server (saved under Settings > Model provider, else ANTHROPIC_API_KEY; see
// lib/provider-api.ts) and never travels with a message. Runs the tool loop
// in lib/chat and enriches the returned results with card data for the UI.
import { NextResponse } from "next/server";
import { runChat, ProviderError } from "@/lib/chat/chat";
import { carriesKey, redact, resolveProvider } from "@/lib/provider-api";
import { loadData, mediaUrl } from "@/lib/catalog";
import { loadReferoIndex } from "@/lib/refero";
import { markdown } from "@/lib/markdown";
import { tintOf } from "@/lib/style-labels";

export const dynamic = "force-dynamic";


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
          card.tint = tintOf(s.swatches) || undefined;
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
  let body: { messages?: { role: string; content: string }[] };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: "bad JSON" }, { status: 400 });
  }
  // A page from before keys moved server-side still sends its key with each
  // message. Refuse it (the page's own load moves the key to the server).
  if (carriesKey(body))
    return NextResponse.json(
      { error: "key_in_body", message: "Reload the page: the key is now saved on the server under Settings > Model provider." },
      { status: 400 },
    );
  let held;
  try {
    held = await resolveProvider();
  } catch {
    return NextResponse.json({ error: "internal error" }, { status: 500 });
  }
  if (held.error) return NextResponse.json({ error: held.error });
  if (!held.cfg) return NextResponse.json({ error: "no_provider" });
  const cfg = held.cfg;
  const messages = Array.isArray(body.messages) ? body.messages : [];
  try {
    const result = await runChat(messages, cfg);
    return NextResponse.json({
      ...result,
      ...(result.error ? { error: redact(result.error, cfg.api_key) } : {}),
      reply: result.reply ? markdown(result.reply, { base: "chat", remoteImages: false }) : "",
      // The model's own markdown, which the page sends back as history;
      // `reply` is rendered HTML for display only.
      raw: result.reply || "",
      results: await enrich(result.results),
    });
  } catch (e) {
    const msg = e instanceof ProviderError || e instanceof Error ? e.message : "chat failed";
    return NextResponse.json({ error: redact(msg, cfg.api_key) });
  }
}
