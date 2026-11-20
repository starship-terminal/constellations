"use client";

// The package index: hero with the research bar (search + platform chips +
// ask), a filter toolbar, and the card grid / list. Search scores rows like
// the old app.js: facet words count double, one term may miss on 3+ words.
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { DesignSystem, GalleryData } from "@/lib/catalog";
import { mediaUrl } from "@/lib/url";
import { useChat } from "@/components/Chat";
import { useSlashFocus } from "@/components/keys";
import { scoreRow, terms, type Facet } from "@/lib/search";
import { themeLabel, tintOf } from "@/lib/style-labels";
import { useUrlMirror } from "@/components/url-state";

const isDark = (t: string) => /dark/.test(t);
const portrait = (s: DesignSystem) => s.tags.includes("ios");
const hayOf = (s: DesignSystem, categories: Record<string, string>) =>
  [s.name, s.slug, s.goodFor, s.category, categories[s.category], ...s.tags, ...s.themes, ...s.fonts.map((f) => f.family)]
    .join(" ")
    .toLowerCase();

const SCRUB_MAX = 8;
function scrubFrames(s: DesignSystem) {
  const rest = s.screenshots.filter((i) => i.path !== s.cover.path && (portrait(s) || !i.tags.includes("mobile")));
  const step = Math.max(1, Math.ceil(rest.length / (SCRUB_MAX - 1)));
  const frames = rest.filter((_, i) => i % step === 0).slice(0, SCRUB_MAX - 1);
  frames.unshift({ path: s.cover.path, name: "cover", group: "", tags: [], thumb: s.cover.thumb });
  return frames;
}

const icon = (s: DesignSystem, cls = "app-icon") =>
  s.icon ? <img className={cls} src={mediaUrl(s.icon)} alt="" loading="lazy" /> : <i>{s.name[0].toUpperCase()}</i>;

function Card({ s, frames }: { s: DesignSystem; frames: { path: string; thumb?: string }[] }) {
  const vp = useRef<HTMLDivElement>(null);
  const stack = useRef<HTMLDivElement>(null);
  const cur = useRef(0);
  const onMove = (e: React.MouseEvent) => {
    const el = vp.current;
    if (!el || frames.length < 2) return;
    const r = el.getBoundingClientRect();
    const i = Math.min(frames.length - 1, Math.floor(Math.max(e.clientX - r.left, 0) / (r.width / frames.length)));
    if (i === cur.current) return;
    cur.current = i;
    const img = document.createElement("img");
    img.src = mediaUrl(frames[i].thumb || frames[i].path);
    img.alt = "";
    img.decoding = "async";
    const st = stack.current;
    if (!st) return;
    st.append(img);
    img.addEventListener("load", () => {
      if (img.parentNode !== st) return;
      const before: Element[] = [];
      for (const c of Array.from(st.children)) {
        if (c === img) break;
        before.push(c);
      }
      const keep = before.findLast((c) => c instanceof HTMLImageElement && c.complete && c.naturalWidth > 0);
      for (const c of before) if (c !== keep) c.remove();
    }, { once: true });
    img.addEventListener("error", () => img.remove(), { once: true });
    while (st.children.length > 4) st.children[1].remove();
  };
  const tint = tintOf(s.swatches);
  return (
    <Link className={`card${portrait(s) ? " portrait" : ""}`} href={`/gallery/${s.slug}`} style={tint ? ({ "--tint": tint } as React.CSSProperties) : undefined}>
      <div className="cover">
        <div className="viewport" ref={vp} onMouseMove={onMove}>
          <div className="stack" ref={stack}>
            <img src={mediaUrl(s.cover.thumb || s.cover.path)} alt={`${s.name} screenshot`} loading="lazy" decoding="async" />
          </div>
        </div>
      </div>
      <div className="card-foot">
        <span className="foot-icon">{icon(s)}</span>
        <div className="foot-txt">
          <h2>{s.name}</h2>
        </div>
      </div>
    </Link>
  );
}

export function GalleryIndex({ data }: { data: GalleryData }) {
  const params = useSearchParams();
  const router = useRouter();
  const chat = useChat();
  const qRef = useRef<HTMLInputElement>(null);
  const [q, setQ] = useState(params.get("q") || "");
  const [cat, setCat] = useState(params.get("cat") || "all");
  const [dark, setDark] = useState(false);
  const [platform, setPlatform] = useState("all");
  const [view, setView] = useState<"grid" | "list">("grid");
  useEffect(() => {
    try {
      const s = JSON.parse(localStorage.getItem("ds-index") || "{}");
      if (s.cat && !params.get("cat")) setCat(s.cat);
      if (s.dark) setDark(true);
      if (s.platform) setPlatform(s.platform);
      if (s.view === "list") setView("list");
    } catch {}
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useSlashFocus(qRef);
  useUrlMirror({ q: q.trim() || null, cat: cat === "all" ? null : cat });

  const save = (patch: object) => {
    try {
      const s = JSON.parse(localStorage.getItem("ds-index") || "{}");
      localStorage.setItem("ds-index", JSON.stringify({ ...s, ...patch, q: "" }));
    } catch {}
  };

  const toks = useMemo(() => terms(q), [q]);
  const facets = useMemo<Facet<DesignSystem>[]>(
    () => [
      [new Set(Object.keys(data.categories)), (s, t) => s.category === t],
      [new Set(data.systems.flatMap((s) => s.tags)), (s, t) => s.tags.includes(t)],
      [new Set(["dark", "light", "mixed"]), (s, t) => s.themes.some((x) => x.includes(t))],
    ],
    [data],
  );
  const list = useMemo(
    () =>
      data.systems.filter(
        (s) =>
          (cat === "all" || s.category === cat) &&
          (!dark || s.themes.some(isDark)) &&
          (platform === "all" || s.tags.includes(platform)) &&
          scoreRow(s, hayOf(s, data.categories), toks, facets) > 0,
      ),
    [data, cat, dark, platform, toks, facets],
  );
  const frames = useMemo(() => new Map(list.map((s) => [s.slug, scrubFrames(s)])), [list]);
  const cats = Object.entries(data.categories).filter(([k]) => data.systems.some((s) => s.category === k));

  const ask = () => chat.open(q || undefined);

  return (
    <div className="page">
      <div className="g-hero">
        <h1>Design systems</h1>
        <p className="sub">
          {list.length === data.systems.length ? data.systems.length : `${list.length} of ${data.systems.length}`} styles captured from real
          products. Measured tokens, a rendered style guide and the original screenshots.
          {chat.enabled ? " Ask in plain words." : ""}
        </p>
        <div className="research">
          <label className="field">
            <svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true">
              <circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" strokeWidth="1.6" />
              <path d="M11 11l3.5 3.5" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
            </svg>
            <input
              ref={qRef}
              type="search"
              placeholder={chat.enabled ? "Ask for a style, mood or use…" : "Search name, use, tag…"}
              autoComplete="off"
              aria-label="Search design systems"
              value={q}
              onChange={(e) => setQ(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && chat.enabled) {
                  e.preventDefault();
                  ask();
                }
              }}
            />
            <kbd>/</kbd>
          </label>
          <div className="r-chips" role="group" aria-label="Platform">
            {(
              [
                ["all", "All"],
                ["web", "Web apps"],
                ["ios", "iOS apps"],
                ["desktop", "Desktop apps"],
              ] as const
            ).map(([k, label]) => (
              <button
                key={k}
                className="r-chip"
                type="button"
                aria-pressed={platform === k}
                onClick={() => {
                  setPlatform(k);
                  save({ platform: k });
                }}
              >
                {label}
              </button>
            ))}
          </div>
          <button
            className="r-go"
            type="button"
            aria-label={chat.enabled ? "Ask the librarian" : "Search"}
            onClick={() => (chat.enabled ? ask() : qRef.current?.focus())}
          >
            <svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M8 13V3M3.5 7.5 8 3l4.5 4.5" />
            </svg>
          </button>
        </div>
      </div>

      <div className="toolbar">
        <div className="chips">
          <button className="chip" aria-pressed={cat === "all"} onClick={() => { setCat("all"); save({ cat: "all" }); }}>
            All<span className="n">{data.systems.length}</span>
          </button>
          {cats.map(([k, v]) => (
            <button key={k} className="chip" aria-pressed={cat === k} onClick={() => { setCat(k); save({ cat: k }); }}>
              {v}
              <span className="n">{data.systems.filter((s) => s.category === k).length}</span>
            </button>
          ))}
        </div>
        <div className="toolbar-side">
          <button className="chip" aria-pressed={dark} onClick={() => { setDark(!dark); save({ dark: !dark }); }}>
            Has dark theme
          </button>
          <div className="seg" role="group" aria-label="Layout">
            <button data-view="grid" aria-pressed={view === "grid"} onClick={() => { setView("grid"); save({ view: "grid" }); }}>
              Gallery
            </button>
            <button data-view="list" aria-pressed={view === "list"} onClick={() => { setView("list"); save({ view: "list" }); }}>
              List
            </button>
          </div>
        </div>
      </div>

      {!list.length ? (
        <p className="empty">No style matches. Clear the search or filters.</p>
      ) : view === "list" ? (
        <div className="table-wrap">
          <table className="list">
            <thead>
              <tr>
                <th></th><th>Name</th><th>Category</th><th>Good for</th><th>Palette</th><th>Themes</th><th>Score</th><th>Captured</th>
              </tr>
            </thead>
            <tbody>
              {list.map((s) => (
                <tr
                  key={s.slug}
                  onClick={(e) => {
                    // The name cell holds the real link (keyboard, middle-click,
                    // open in new tab); a click elsewhere on the row follows it.
                    if (!(e.target as HTMLElement).closest("a")) router.push(`/gallery/${s.slug}`);
                  }}
                >
                  <td>
                    <div className="thumb"><img loading="lazy" src={mediaUrl(s.cover.thumb || s.cover.path)} alt="" /></div>
                  </td>
                  <td className="nm">
                    {icon(s)}
                    <Link href={`/gallery/${s.slug}`}>{s.name}</Link>
                  </td>
                  <td>{data.categories[s.category] || s.category}</td>
                  <td className="gf">{s.goodFor}</td>
                  <td><Strip sw={Object.values(s.swatches)[0] || []} /></td>
                  <td className="dt themes">{s.themes.map(themeLabel).join(", ")}</td>
                  <td className="dt">{s.score ? `${s.score.meets}/${s.score.applicable} met` : ""}</td>
                  <td className="dt">{s.captured}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <div className="grid">
          {list.map((s) => (
            <Card key={s.slug} s={s} frames={frames.get(s.slug) || []} />
          ))}
        </div>
      )}
    </div>
  );
}

function Strip({ sw }: { sw: { role: string; value: string | null }[] }) {
  return (
    <div className="strip" title={sw.map((x) => `${x.role} ${x.value}`).join(" · ")}>
      {sw.map((x, i) => (
        <span key={i} style={{ background: x.value || "transparent" }} />
      ))}
    </div>
  );
}
