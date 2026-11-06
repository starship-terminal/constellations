"use client";

// A refero style's page surface: tabbed media viewer with the shared
// lightbox, the tabbed document pane (HTML rendered server-side), the token
// export as swatches and tables, and the similar-styles strip. All props are
// plain serializable data prepared by the RSC page.
import Link from "next/link";
import { useId, useMemo, useState } from "react";
import type { ReferoEntity } from "@/lib/refero";
import { RfFav, RfImg } from "@/components/ReferoIndex";
import { host } from "@/lib/refero-media";
import { useLightbox } from "@/components/Lightbox";
import { copyWithToast } from "@/components/CopyButton";
import { useToast } from "@/components/Toast";

export interface ReferoMediaPair {
  local: string | null;
  remote: string | null;
}
export interface ReferoDoc {
  key: string;
  label: string;
  file: string;
  raw: string;
  code: boolean;
  html: string;
}
export interface ReferoSimilar {
  slug: string | null;
  name: string | null;
  why: string | null;
  img: ReferoMediaPair | null;
  fav: ReferoMediaPair | null;
}

interface DsColor {
  hex?: string;
  value?: string;
  name?: string;
  role?: string;
  group?: string;
}
interface DsFont {
  family?: string;
  source?: string;
  substitute?: string;
  weight?: string;
  sizes?: string;
  lineHeight?: string;
  letterSpacing?: string;
  fontFeatureSettings?: string;
  role?: string;
}
interface DsStep {
  role?: string;
  size?: number;
  lineHeight?: number;
  letterSpacing?: number;
  weight?: number | string;
  family?: string;
}
interface DsSpacing {
  baseUnit?: number | string;
  density?: string;
  pageMaxWidth?: string;
  sectionGap?: string;
  cardPadding?: string;
  elementGap?: string;
  radius?: Record<string, string>;
}
interface DsElev {
  element?: string;
  style?: string;
}
interface Ds {
  description?: string;
  colors?: DsColor[];
  typography?: DsFont[];
  typeScale?: DsStep[];
  spacing?: DsSpacing;
  elevation?: DsElev[];
  elevationPhilosophy?: string;
  dos?: unknown[];
  donts?: unknown[];
}

const MEDIA_TABS = [
  ["shot", "Screenshot", "img"],
  ["video", "Video", "video"],
  ["detail", "Detail clip", "video"],
  ["poster", "Poster", "img"],
] as const;
type MediaKind = (typeof MEDIA_TABS)[number][0];

const copySvg = (
  <svg viewBox="0 0 24 24" width="11" height="11" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <rect width="14" height="14" x="8" y="8" rx="2" />
    <path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2" />
  </svg>
);
const dlSvg = (
  <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <path d="M12 3v12" />
    <path d="m7 10 5 5 5-5" />
    <path d="M5 21h14" />
  </svg>
);
const extSvg = (
  <svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
    <path d="M7 17 17 7" />
    <path d="M8 7h9v9" />
  </svg>
);


// Arrow keys, Home and End move between tabs and select the one reached
// (WAI-ARIA tabs with automatic activation); only the selected tab is in
// the Tab order, so Tab moves on to the panel.
function onTabKeys(ev: React.KeyboardEvent<HTMLElement>) {
  const tabs = Array.from(ev.currentTarget.querySelectorAll<HTMLButtonElement>('[role="tab"]'));
  const at = tabs.indexOf(document.activeElement as HTMLButtonElement);
  if (at < 0) return;
  const to =
    ev.key === "ArrowRight" ? (at + 1) % tabs.length
    : ev.key === "ArrowLeft" ? (at - 1 + tabs.length) % tabs.length
    : ev.key === "Home" ? 0
    : ev.key === "End" ? tabs.length - 1
    : -1;
  if (to < 0) return;
  ev.preventDefault();
  tabs[to].focus();
  tabs[to].click();
}

function MediaTabs({ e }: { e: ReferoEntity }) {
  const lb = useLightbox();
  const ids = useId();
  const tabs = useMemo(
    () =>
      MEDIA_TABS.filter(([k]) => {
        const m = e.media?.[k];
        return m && (m.local || m.remote);
      }),
    [e],
  );
  const [tab, setTab] = useState<MediaKind>(tabs[0]?.[0] ?? "shot");
  if (!tabs.length) return null;
  const cur = tabs.some(([k]) => k === tab) ? tab : tabs[0][0];
  const media = e.media[cur]!;
  const isVideo = MEDIA_TABS.find(([k]) => k === cur)?.[2] === "video";

  // poster= cannot fall back on its own, so the remote URL wins like app.js.
  const posterOf = (m: ReferoMediaPair | null | undefined) => (m ? m.remote || m.local || undefined : undefined);
  const poster =
    cur === "detail"
      ? posterOf(e.media.detail_poster) || posterOf(e.media.poster)
      : cur === "video"
        ? posterOf(e.media.poster)
        : undefined;

  // detail_poster joins the lightbox set even though it is not a tab.
  const items = (
    [
      ["shot", "Screenshot"],
      ["poster", "Poster"],
      ["detail_poster", "Detail still"],
    ] as const
  )
    .map(([k, label]) => {
      const m = e.media?.[k];
      if (!m || !(m.local || m.remote)) return null;
      return { key: k, path: (m.local || m.remote)!, name: `${e.name || e.slug} — ${label}` };
    })
    .filter((x): x is { key: "shot" | "poster" | "detail_poster"; path: string; name: string } => !!x);

  return (
    <section className="rf-sec">
      {tabs.length > 1 && (
        <div className="rf-tabs" role="tablist" aria-label="Media" onKeyDown={onTabKeys}>
          {tabs.map(([k, label]) => (
            <button
              key={k}
              id={`${ids}-tab-${k}`}
              role="tab"
              type="button"
              aria-selected={k === cur}
              aria-controls={`${ids}-panel`}
              tabIndex={k === cur ? 0 : -1}
              onClick={() => setTab(k)}
            >
              {label}
            </button>
          ))}
        </div>
      )}
      <div
        className="rf-media"
        {...(tabs.length > 1 ? { id: `${ids}-panel`, role: "tabpanel", "aria-labelledby": `${ids}-tab-${cur}` } : {})}
      >
        {isVideo ? (
          <video
            className="rf-vid"
            controls
            playsInline
            preload="metadata"
            poster={poster}
            src={media.local || media.remote || undefined}
            onError={(ev) => {
              const v = ev.currentTarget;
              if (media.remote && v.src !== media.remote) v.src = media.remote;
            }}
          />
        ) : (
          <button
            className="rf-open"
            type="button"
            aria-label="Open in lightbox"
            onClick={() => lb.open({ items, index: Math.max(0, items.findIndex((i) => i.key === cur)) })}
          >
            <RfImg media={media} alt={`${e.name || e.slug} preview`} />
          </button>
        )}
      </div>
    </section>
  );
}

function DocsPane({ e, docs }: { e: ReferoEntity; docs: ReferoDoc[] }) {
  const { toast } = useToast();
  const [tab, setTab] = useState(0);
  const ids = useId();
  if (!docs.length) return null;
  const d = docs[Math.min(tab, docs.length - 1)];
  const download = () => {
    const blob = new Blob([d.raw], { type: "text/plain" });
    const a = Object.assign(document.createElement("a"), {
      href: URL.createObjectURL(blob),
      download: `${e.slug}-${d.file}`,
    });
    a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 4000);
  };
  return (
    <section className="rf-sec">
      <h2 className="rf-h2">Documents</h2>
      <div className="rf-pane">
        <div className="rf-tabs" role="tablist" aria-label="Documents" onKeyDown={onTabKeys}>
          {docs.map((x, i) => (
            <button
              key={x.key}
              id={`${ids}-tab-${i}`}
              role="tab"
              type="button"
              aria-selected={d === x}
              aria-controls={`${ids}-panel`}
              tabIndex={d === x ? 0 : -1}
              onClick={() => setTab(i)}
            >
              {x.label}
            </button>
          ))}
        </div>
        <div className="rf-docbar">
          <span className="rf-docname">
            {e.slug}-{d.file}
          </span>
          <div className="acts">
            <button
              className="rf-mini"
              type="button"
              title="Copy this document"
              onClick={() => copyWithToast(d.raw, toast, `${d.label} copied`)}
            >
              {copySvg}
              Copy
            </button>
            <button className="rf-mini" type="button" title="Download this document" onClick={download}>
              {dlSvg}
              <span>.{d.file.split(".").pop()}</span>
            </button>
            {e.page_url && (
              <a className="rf-cta" href={e.page_url} target="_blank" rel="noopener">
                <span className="cta-t">Open on refero</span>
                {extSvg}
              </a>
            )}
          </div>
        </div>
        <div className="rf-pane-body" id={`${ids}-panel`} role="tabpanel" tabIndex={0} aria-labelledby={`${ids}-tab-${docs.indexOf(d)}`}>
          {d.code ? (
            <pre className="rf-code">
              <code dangerouslySetInnerHTML={{ __html: d.html }} />
            </pre>
          ) : (
            <div className="md rf-doc-md" dangerouslySetInnerHTML={{ __html: d.html }} />
          )}
        </div>
      </div>
    </section>
  );
}

function Swatch({ c }: { c: DsColor }) {
  const { toast } = useToast();
  const v = c.hex || c.value || "";
  const grad = /gradient/i.test(v);
  return (
    <button
      className="rf-sw"
      type="button"
      title={`Copy ${grad ? "gradient" : v}`}
      onClick={() => copyWithToast(v, toast, `Copied ${v}`)}
    >
      <span className="sw-i" style={{ background: v }}>
        <span className="sw-copy">
          {copySvg}
          Copy
        </span>
      </span>
      <span className="rf-sw-txt">
        <b>{c.name || v}</b>
        <code>{grad ? "Gradient" : v}</code>
        {c.role && <span className="rf-sw-role">{c.role}</span>}
      </span>
    </button>
  );
}

const GROUP_LABELS: Record<string, string> = {
  neutral: "Neutrals",
  accent: "Accent",
  semantic: "Semantic",
  brand: "Brand",
};

function Colors({ ds }: { ds: Ds }) {
  const colors = ds.colors || [];
  if (!colors.length) return null;
  const groups = new Map<string, DsColor[]>();
  for (const c of colors) {
    const g = c.group || "other";
    const arr = groups.get(g);
    if (arr) arr.push(c);
    else groups.set(g, [c]);
  }
  const order = [...groups.keys()].sort(
    (a, b) => Number(a === "neutral") - Number(b === "neutral") || a.localeCompare(b),
  );
  return (
    <section className="rf-sec">
      <h2 className="rf-h2">Color Palette</h2>
      {order.map((g) => (
        <div key={g}>
          <h3 className="rf-h3">{GROUP_LABELS[g] || g[0].toUpperCase() + g.slice(1)}</h3>
          <div className="rf-swatches">
            {groups.get(g)!.map((c, i) => (
              <Swatch key={i} c={c} />
            ))}
          </div>
        </div>
      ))}
    </section>
  );
}

const cssLen = (v: number | string | undefined, fb = "14px") => {
  if (v === undefined || v === null || v === "") return fb;
  return typeof v === "number" ? `${v}px` : /^[\d.]+$/.test(v) ? `${v}px` : v;
};

function ScaleRow({ t }: { t: DsStep }) {
  return (
    <div className="rf-scale-row">
      <span className="rf-scale-label">
        {t.role || "step"}
        <code>
          {[t.size != null ? `${t.size}px` : null, t.weight, t.lineHeight]
            .filter((x) => x != null && x !== "")
            .join(" · ")}
        </code>
      </span>
      <span
        className="rf-scale-sample"
        style={{
          fontSize: cssLen(t.size),
          lineHeight: String(t.lineHeight ?? 1.4),
          fontWeight: Number(t.weight ?? 400),
        }}
      >
        The quick brown fox jumps over the lazy dog
      </span>
    </div>
  );
}

function Typography({ ds }: { ds: Ds }) {
  const [all, setAll] = useState(false);
  const fonts = ds.typography || [];
  const scale = ds.typeScale || [];
  if (!fonts.length && !scale.length) return null;
  const stack = (f: DsFont) =>
    `"${String(f.family || "").replace(/"/g, "")}", ${f.substitute ? `"${f.substitute}", ` : ""}${
      /mono/i.test(f.family || "") ? "ui-monospace, monospace" : "system-ui, sans-serif"
    }`;
  const spec = (f: DsFont) =>
    (
      [
        ["Weight", f.weight],
        ["Sizes", f.sizes],
        ["Line height", f.lineHeight],
        ["Tracking", f.letterSpacing],
        ["Features", f.fontFeatureSettings],
        ["Substitute", f.substitute],
      ] as const
    )
      .filter((x) => x[1])
      .map(([k, v]) => (
        <span key={k} style={{ display: "contents" }}>
          <dt>{k}</dt>
          <dd>{v}</dd>
        </span>
      ));
  return (
    <section className="rf-sec">
      <h2 className="rf-h2">Typography</h2>
      {!!scale.length && (
        <div className="rf-scale">
          {(all ? scale : scale.slice(0, 8)).map((t, i) => (
            <ScaleRow key={i} t={t} />
          ))}
        </div>
      )}
      {!all && scale.length > 8 && (
        <button className="btn" type="button" onClick={() => setAll(true)}>
          Show all {scale.length} steps
        </button>
      )}
      <div className="rf-fonts">
        {fonts.map((f, i) => (
          <div className="rf-font" key={i}>
            <div className="rf-font-sample" style={{ fontFamily: stack(f) }}>
              {f.family || "Unknown"} Aa 123
            </div>
            <dl className="rf-font-spec">{spec(f)}</dl>
            {f.role && <p className="rf-note">{f.role}</p>}
          </div>
        ))}
      </div>
    </section>
  );
}

function Spacing({ ds }: { ds: Ds }) {
  const sp = ds.spacing || {};
  const el = ds.elevation || [];
  const rows = (
    [
      ["Base unit", sp.baseUnit != null && sp.baseUnit !== "" ? cssLen(sp.baseUnit) : null],
      ["Density", sp.density],
      ["Max width", sp.pageMaxWidth],
      ["Section gap", sp.sectionGap],
      ["Card padding", sp.cardPadding],
      ["Element gap", sp.elementGap],
    ] as const
  ).filter((r) => r[1]);
  const radii = Object.entries(sp.radius || {});
  if (!rows.length && !radii.length && !el.length && !ds.elevationPhilosophy) return null;
  const px = (v: unknown) => {
    const m = String(v).match(/^([\d.]+)px$/);
    return m ? +m[1] : null;
  };
  return (
    <section className="rf-sec">
      <h2 className="rf-h2">Spacing &amp; Shape</h2>
      <div className="rf-tables">
        {!!rows.length && (
          <table className="rf-table">
            <thead>
              <tr>
                <th>Purpose</th>
                <th>Value</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {rows.map(([k, v]) => {
                const p = px(v);
                return (
                  <tr key={k}>
                    <td>{k}</td>
                    <td>
                      <code>{String(v)}</code>
                    </td>
                    <td className="rf-bar-cell">{p ? <span className="rf-bar" style={{ width: `min(${p}px, 100%)` }} /> : null}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}
        {!!radii.length && (
          <table className="rf-table">
            <thead>
              <tr>
                <th>Element</th>
                <th>Radius</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {radii.map(([k, v]) => (
                <tr key={k}>
                  <td>{k}</td>
                  <td>
                    <code>{v}</code>
                  </td>
                  <td>
                    <i className="rf-rbox" style={{ borderRadius: v }} />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
      {!!el.length && (
        <div className="rf-elev">
          {el.map((x, i) => (
            <div className="rf-elev-row" key={i}>
              <i className="rf-ebox" style={{ boxShadow: x.style }} />
              <div>
                <b>{x.element}</b>
                <code>{x.style}</code>
              </div>
            </div>
          ))}
        </div>
      )}
      {ds.elevationPhilosophy && <p className="rf-note">{ds.elevationPhilosophy}</p>}
    </section>
  );
}

function Guidelines({ ds }: { ds: Ds }) {
  const dos = ds.dos || [];
  const donts = ds.donts || [];
  if (!dos.length && !donts.length) return null;
  const txt = (t: unknown) =>
    typeof t === "string" ? t : String((t as { text?: string })?.text ?? JSON.stringify(t));
  const col = (title: string, items: unknown[], mark: string, cls: string) =>
    items.length ? (
      <div className={`rf-guide ${cls}`}>
        <h3 className="rf-h3">{title}</h3>
        <ul>
          {items.map((t, i) => (
            <li key={i}>
              <span className="mk">{mark}</span>
              <span>{txt(t)}</span>
            </li>
          ))}
        </ul>
      </div>
    ) : null;
  return (
    <section className="rf-sec">
      <h2 className="rf-h2">Guidelines</h2>
      <div className="rf-guides">
        {col("Do", dos, "✓", "do")}
        {col("Don\u2019t", donts, "✕", "dont")}
      </div>
    </section>
  );
}

function Similar({ items }: { items: ReferoSimilar[] }) {
  if (!items.length) return null;
  return (
    <section className="rf-sec">
      <h2 className="rf-h2">More like this</h2>
      <div className="rf-grid rf-sim">
        {items.map((x, i) =>
          x.slug && x.img ? (
            <Link className="rf-card" key={x.slug} href={`/refero/${encodeURIComponent(x.slug)}`}>
              <div className="rf-tile">
                <div className="rf-shot">
                  <RfImg media={x.img} alt={`${x.name || x.slug} screenshot`} />
                </div>
              </div>
              <div className="rf-card-foot">
                {x.fav && <RfFav media={x.fav} name={x.name} />}
                <div className="rf-card-txt">
                  <h3>{x.name || x.slug}</h3>
                  <p>{x.why || ""}</p>
                </div>
              </div>
            </Link>
          ) : (
            <div className="rf-card rf-plain" key={x.slug || i} title="Not in this library">
              <div className="rf-tile">
                <div className="rf-shot rf-empty">
                  <span>{(x.name || "?")[0].toUpperCase()}</span>
                </div>
              </div>
              <div className="rf-card-foot">
                <div className="rf-card-txt">
                  <h3>{x.name || "?"}</h3>
                  <p>{x.why || ""}</p>
                </div>
              </div>
            </div>
          ),
        )}
      </div>
    </section>
  );
}

export function ReferoDetail({ entity: e, docs, similar }: { entity: ReferoEntity; docs: ReferoDoc[]; similar: ReferoSimilar[] }) {
  const ds = (e.ds || {}) as Ds;
  const fav = e.media?.favicon || null;
  const chips = (
    [
      ["theme", e.theme],
      ["industry", e.industry],
      ["type", e.type],
      ["style", e.style],
    ] as const
  ).filter((x) => x[1]);
  return (
    <div className="page">
      <Link className="rf-back" href="/refero">
        ← Refero styles
      </Link>
      <div className="rf-title">
        <h1>{e.name || e.slug}</h1>
        {fav && (fav.local || fav.remote) && <RfFav media={fav} name={e.name} big />}
      </div>
      {e.tagline && <p className="rf-tagline">{e.tagline}</p>}
      {ds.description && <p className="rf-desc">{ds.description}</p>}
      {!!chips.length && (
        <div className="rf-chips-row">
          {chips.map(([k, v]) => (
            <Link key={k} className="chip" href={`/refero?${k}=${encodeURIComponent(v!)}`}>
              {v}
            </Link>
          ))}
        </div>
      )}
      {e.source_url && (
        <a className="rf-src" href={e.source_url} target="_blank" rel="noopener">
          {extSvg}
          {host(e.source_url)}
        </a>
      )}
      <MediaTabs e={e} />
      <DocsPane e={e} docs={docs} />
      <Colors ds={ds} />
      <Typography ds={ds} />
      <Spacing ds={ds} />
      <Guidelines ds={ds} />
      <Similar items={similar} />
    </div>
  );
}
