"use client";

// The package page's interactive body: sticky section rail with scroll-spy,
// screenshot/component crops opening the shared lightbox, tag filters, and
// swatch/icon copy. Every fs-shaped value arrives pre-rendered as a plain
// prop from the RSC page.
import Link from "next/link";
import { useEffect, useMemo, useRef, useState } from "react";
import type { DesignSystem, PkgFile, Shot, TypeStyle } from "@/lib/catalog";
import { mediaUrl } from "@/lib/url";
import type { GradeValue, SystemReport } from "@/lib/scorecard";
import { useLightbox } from "@/components/Lightbox";
import type { LbSys } from "@/components/Lightbox";
import { useToast } from "@/components/Toast";
import { copyWithToast } from "@/components/CopyButton";
import { themeLabel } from "@/lib/style-labels";

// Mirror of scorecard.ts's GRADES, inlined so this client bundle never pulls
// the fs-reading module in for a constant.
const GRADE_UI: Record<GradeValue, { glyph: string; word: string }> = {
  meets: { glyph: "●", word: "Meets" },
  partly: { glyph: "◐", word: "Partly" },
  missing: { glyph: "○", word: "Missing" },
  na: { glyph: "–", word: "Not applicable" },
};
const GRADE_ORDER: GradeValue[] = ["meets", "partly", "missing", "na"];

const ICONS_SHOWN = 48;

const fileName = (p: string) => p.split("/").pop() || p;
const cssLen = (v: string | number) => (typeof v === "number" ? `${v}px` : v);
const sentence = (t: string) => t.trim().replace(/\.$/, "");
const humanSize = (n: number) =>
  n < 1024 ? `${n} B` : n < 1024 * 1024 ? `${(n / 1024).toFixed(1)} KB` : `${(n / 1024 / 1024).toFixed(1)} MB`;
// px length of a CSS step ("12px", "0.75rem") for proportional bars; 0 when
// the value is not a simple length.
const pxOf = (v: string) => {
  const m = /^([\d.]+)\s*(px|rem|em)$/.exec(v.trim());
  if (!m) return 0;
  const n = parseFloat(m[1]);
  return m[2] === "px" ? n : n * 16;
};

/** Shots in first-seen group order: [group, items][]. */
function grouped(items: Shot[]): [string, Shot[]][] {
  const m = new Map<string, Shot[]>();
  for (const i of items) {
    const a = m.get(i.group);
    if (a) a.push(i);
    else m.set(i.group, [i]);
  }
  return [...m.entries()];
}

export function SystemDetail({
  sys,
  categoryLabel,
  briefHtml,
  healthHtml,
  report,
  files,
}: {
  sys: DesignSystem;
  categoryLabel: string;
  /** README `brief` section, rendered server-side; null when not generated. */
  briefHtml: string | null;
  /** README `health` section, rendered server-side; null when not generated. */
  healthHtml: string | null;
  /** Newest audit's per-criterion report; null when the audit lacks this package. */
  report: SystemReport | null;
  files: Record<string, PkgFile[]>;
}) {
  const lb = useLightbox();
  const { toast } = useToast();
  const root = useRef<HTMLDivElement>(null);
  const [active, setActive] = useState("");
  const [shotFilter, setShotFilter] = useState("all");

  const portrait = sys.tags.includes("ios");
  const lbSys = useMemo<LbSys>(
    () => ({
      slug: sys.slug,
      name: sys.name,
      icon: sys.icon ? mediaUrl(sys.icon) : undefined,
      category: sys.category,
      categoryLabel,
      tags: sys.tags,
      swatches: (sys.swatches[sys.tokenTheme] || Object.values(sys.swatches)[0] || []).map((x) => ({
        role: x.role,
        value: x.value,
      })),
    }),
    [sys, categoryLabel],
  );

  // The tokenTheme palette as role -> value, for shadow stages and icon tiles.
  const themeColors = useMemo(() => {
    const sw = sys.swatches[sys.tokenTheme] || Object.values(sys.swatches)[0] || [];
    const by = Object.fromEntries(sw.map((x) => [x.role, x.value]));
    return {
      page: by.page || "#ffffff",
      surface: by.surface || by.page || "#ffffff",
      text: by.text || "#111111",
      muted: by.muted || "#666666",
    };
  }, [sys]);

  const shotTags = useMemo(() => [...new Set(sys.screenshots.flatMap((i) => i.tags))], [sys]);
  const shotTagCounts = useMemo(() => {
    const c: Record<string, number> = {};
    for (const i of sys.screenshots) for (const t of i.tags) c[t] = (c[t] || 0) + 1;
    return c;
  }, [sys]);
  const shownShots = useMemo(
    () => (shotFilter === "all" ? sys.screenshots : sys.screenshots.filter((i) => i.tags.includes(shotFilter))),
    [sys, shotFilter],
  );
  const shotGroups = useMemo(() => grouped(shownShots), [shownShots]);
  const cropGroups = useMemo(() => grouped(sys.components), [sys]);
  const fileGroups = useMemo(() => Object.entries(files), [files]);
  const gaps = useMemo(
    () => [...Object.entries(sys.layoutGaps), ...Object.entries(sys.omitted)],
    [sys],
  );

  const openShots = (shot: Shot) =>
    lb.open({
      items: shownShots.map((i) => ({ path: mediaUrl(i.path), name: i.name, tags: i.tags })),
      index: Math.max(0, shownShots.indexOf(shot)),
      opts: { sys: lbSys, onTag: (t) => setShotFilter(t) },
    });
  const openCrops = (shot: Shot) =>
    lb.open({
      items: sys.components.map((i) => ({ path: mediaUrl(i.path), name: i.name, tags: i.tags })),
      index: Math.max(0, sys.components.indexOf(shot)),
      opts: { sys: lbSys },
    });
  const openIcons = (index: number) =>
    lb.open({
      items: sys.icons.items.slice(0, ICONS_SHOWN).map((p) => ({
        path: mediaUrl(p),
        name: fileName(p).replace(/\.[^.]+$/, ""),
      })),
      index,
      opts: { sys: lbSys },
    });
  const copy = async (value: string | null) => {
    if (!value) return;
    await copyWithToast(value, toast, `${value} copied`);
  };

  // Type-style helpers (ported from the old gallery): a catalog font supplies
  // its stack; anything else falls back to the generic family its name says.
  const stackFor = (family?: string) => {
    const f = family && sys.fonts.find((x) => x.family.toLowerCase() === family.toLowerCase());
    if (f) return f.stack;
    if (!family) return "inherit";
    const generic = /mono|code/i.test(family)
      ? "ui-monospace, monospace"
      : /serif/i.test(family) && !/sans/i.test(family)
        ? "Georgia, serif"
        : "system-ui, sans-serif";
    return `"${family.replace(/"/g, "")}", ${generic}`;
  };
  const typeSpec = (t: TypeStyle) =>
    [
      t.family || "",
      t.size
        ? `${t.size}${t.lineHeight != null ? `/${t.lineHeight}` : ""}`
        : t.lineHeight != null
          ? `line-height ${t.lineHeight}`
          : "",
      t.weight != null ? String(t.weight) : "",
      t.letterSpacing && !/^0(px|em|rem)?$/.test(t.letterSpacing) ? `${t.letterSpacing} tracking` : "",
    ]
      .filter(Boolean)
      .join(" · ");

  const swatchCount = Object.values(sys.swatches).reduce((n, sw) => n + sw.length, 0);
  const fileCount = fileGroups.reduce((n, [, l]) => n + l.length, 0);
  const secs: [id: string, label: string, count: number | string | null][] = [
    ["shots", "Screenshots", sys.screenshots.length],
    ["brief", "Brief", briefHtml ? null : 0],
    ["colors", "Colors", swatchCount],
    ["type", "Type", sys.fonts.length + sys.typeStyles.length],
    ["spacing", "Spacing", sys.spacing.length],
    ["shape", "Shape", sys.radii.length + sys.shadows.length],
    ["components", "Components", sys.components.length],
    ["icons", "Icons", sys.icons.total],
    ["health", "Health", sys.score || report || healthHtml || gaps.length ? null : 0],
    ["files", "Files", fileCount || sys.docs.length],
  ];
  const visible = secs.filter(([, , c]) => c !== 0);

  // Scroll-spy: the rail marks the topmost section intersecting the viewport band.
  useEffect(() => {
    const els = Array.from(root.current?.querySelectorAll<HTMLElement>(".pd-sec[id]") ?? []);
    if (!els.length) return;
    const obs = new IntersectionObserver(
      (entries) => {
        for (const e of entries) if (e.isIntersecting) setActive(e.target.id);
      },
      { rootMargin: "-10% 0px -80% 0px" },
    );
    for (const el of els) obs.observe(el);
    return () => obs.disconnect();
  }, []);

  const shotTile = (i: Shot, contain: boolean, onOpen: (s: Shot) => void) => (
    <button key={i.path} className={`shot${contain ? " contain" : ""}`} onClick={() => onOpen(i)}>
      <div className="frame">
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img loading="lazy" decoding="async" src={mediaUrl(i.thumb || i.path)} alt={i.name} />
      </div>
      <span>{i.name}</span>
      {!!i.tags.length && (
        <span className="shot-tags">
          {i.tags.map((t) => (
            <span key={t} className="tag">
              {t}
            </span>
          ))}
        </span>
      )}
    </button>
  );

  return (
    <div className="page" ref={root}>
      <Link className="back" href="/gallery">
        ← All styles
      </Link>
      <header className="pkg-head">
        <h1>
          {sys.icon ? (
            /* eslint-disable-next-line @next/next/no-img-element */
            <img src={mediaUrl(sys.icon)} alt="" />
          ) : (
            <i className="pd-initial">{sys.name[0].toUpperCase()}</i>
          )}
          {sys.name}
        </h1>
        {!!sys.goodFor && <p className="pd-lede">{sys.goodFor}</p>}
        <div className="pkg-sub">
          {!!sys.url && (
            <a className="site" href={sys.url} target="_blank" rel="noopener">
              {sys.url.replace(/^https?:\/\//, "")} ↗
            </a>
          )}
          <span>{categoryLabel}</span>
          {!!sys.themes.length && <span>{sys.themes.map(themeLabel).join(", ")}</span>}
          {!!sys.captured && <span>Captured {sys.captured}</span>}
          {!!sys.access && <span>{sys.access}</span>}
          {sys.score && (
            <Link className="chip pd-score" href={`/scorecard/${sys.slug}`}>
              {sys.score.meets}/{sys.score.applicable} met · {sys.score.date}
            </Link>
          )}
        </div>
        <div className="actions">
          {!!sys.styleGuide && (
            <a className="btn primary" href={mediaUrl(sys.styleGuide)} target="_blank" rel="noopener">
              Open style guide ↗
            </a>
          )}
          {!!sys.tokens && (
            <a className="btn" href={mediaUrl(sys.tokens)} download>
              tokens.json ↓
            </a>
          )}
          {!!sys.entry && (
            <Link className="btn" href={`/gallery/${sys.slug}/files/${sys.entry}`}>
              Read README
            </Link>
          )}
        </div>
      </header>

      <div className="pkg">
        <nav className="rail" aria-label={`${sys.name} sections`}>
          <ul>
            {visible.map(([id, label, count]) => (
              <li key={id}>
                <a href={`#${id}`} aria-current={active === id ? "page" : undefined}>
                  <span>{label}</span>
                  {count != null && <span className="n">{count}</span>}
                </a>
              </li>
            ))}
          </ul>
        </nav>

        <div className="pd-main">
          {!!sys.screenshots.length && (
            <section id="shots" className="pd-sec">
              <header className="sec-head">
                <h2>Screenshots</h2>
                <p>
                  Captures of the real product{sys.widths.length ? ` at ${sys.widths.join("px, ")}px` : ""}. For layout
                  and proportion, never for colour values.
                </p>
              </header>
              {!!shotTags.length && (
                <div className="subfilters">
                  <button className="chip" aria-pressed={shotFilter === "all"} onClick={() => setShotFilter("all")}>
                    All<span className="n">{sys.screenshots.length}</span>
                  </button>
                  {shotTags.map((t) => (
                    <button key={t} className="chip" aria-pressed={shotFilter === t} onClick={() => setShotFilter(t)}>
                      {t}
                      <span className="n">{shotTagCounts[t]}</span>
                    </button>
                  ))}
                </div>
              )}
              {shotGroups.map(([g, items]) => (
                <div key={g}>
                  {shotGroups.length > 1 && <div className="group-title">{g}/</div>}
                  <div className={`shots${portrait ? " phone" : ""}`}>{items.map((i) => shotTile(i, !portrait && i.tags.includes("mobile"), openShots))}</div>
                </div>
              ))}
            </section>
          )}

          {briefHtml && (
            <section id="brief" className="pd-sec">
              <header className="sec-head">
                <h2>Brief</h2>
                <p>The README’s generated brief. Read it before designing in this style.</p>
              </header>
              <article className="md" dangerouslySetInnerHTML={{ __html: briefHtml }} />
            </section>
          )}

          {!!swatchCount && (
            <section id="colors" className="pd-sec">
              <header className="sec-head">
                <h2>Colors</h2>
                <p>The colour roles for each captured theme. Click a swatch to copy its value.</p>
              </header>
              <div className="palettes">
                {Object.entries(sys.swatches).map(([theme, sw]) => (
                  <div className="palette" key={theme}>
                    <div className="palette-head">
                      <span>{themeLabel(theme)}</span>
                      <span>click a swatch to copy</span>
                    </div>
                    <div className="swatches">
                      {sw.map((x, i) => (
                        <button className="swatch" key={i} title={x.token} onClick={() => copy(x.value)}>
                          <i style={{ background: x.value || "transparent" }} />
                          <b>{x.role}</b>
                          <code>{x.value ?? "—"}</code>
                          <code>{x.token}</code>
                        </button>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </section>
          )}

          {!!(sys.fonts.length || sys.typeStyles.length) && (
            <section id="type" className="pd-sec">
              <header className="sec-head">
                <h2>Type</h2>
                <p>
                  Font families, then every type style in {fileName(sys.tokens)}, rendered live. A font this machine
                  lacks falls back to the system face.
                </p>
              </header>
              {!!sys.fonts.length && (
                <div className="fonts">
                  {sys.fonts.map((f) => (
                    <div className="font" key={f.token}>
                      <div className="sample" style={{ fontFamily: f.stack }}>
                        {f.family} Aa 123
                      </div>
                      <b>{f.family}</b>
                      <code>{f.stack}</code>
                      <code>{f.token}</code>
                    </div>
                  ))}
                </div>
              )}
              {!!sys.typeStyles.length && (
                <>
                  <h3 className="sub-title">
                    Type styles <span className="n">{sys.typeStyles.length}</span>
                  </h3>
                  <div className="type-styles">
                    {sys.typeStyles.map((t) => (
                      <div className="type-row" key={t.name}>
                        <div className="type-meta">
                          <b>{t.name}</b>
                          <code>{typeSpec(t)}</code>
                        </div>
                        <div
                          className="type-sample"
                          style={{
                            fontFamily: stackFor(t.family),
                            fontSize: t.size,
                            fontWeight: t.weight,
                            lineHeight: t.lineHeight,
                            letterSpacing: t.letterSpacing,
                            textAlign: "right",
                          }}
                        >
                          The quick brown fox jumps over the lazy dog
                        </div>
                      </div>
                    ))}
                  </div>
                </>
              )}
            </section>
          )}

          {!!sys.spacing.length && (
            <section id="spacing" className="pd-sec">
              <header className="sec-head">
                <h2>Spacing</h2>
                <p>Every spacing step in {fileName(sys.tokens)}, drawn to scale.</p>
              </header>
              <div className="space-list">
                {sys.spacing.map((x) => {
                  const px = pxOf(x.value);
                  return (
                    <div className="space-row" key={x.name}>
                      <code className="nm" title={x.name}>
                        {x.name}
                      </code>
                      <div className="space-track">
                        <span className="space-bar" style={px ? { width: Math.min(px, 160) } : { width: x.value }} />
                      </div>
                      <code className="val">{x.value}</code>
                    </div>
                  );
                })}
              </div>
            </section>
          )}

          {!!(sys.radii.length || sys.shadows.length) && (
            <section id="shape" className="pd-sec">
              <header className="sec-head">
                <h2>Shape</h2>
                <p>Radius steps and shadow tokens, drawn on the {sys.tokenTheme} theme’s own surface colours.</p>
              </header>
              {!!sys.radii.length && (
                <>
                  <h3 className="sub-title">
                    Radius <span className="n">{sys.radii.length}</span>
                  </h3>
                  <div className="radius-grid">
                    {sys.radii.map((x) => (
                      <div className="radius-tile" key={x.name}>
                        <div className="radius-box" style={{ borderRadius: cssLen(x.value) }} />
                        <b title={x.name}>{x.name}</b>
                        <code>{x.value}</code>
                      </div>
                    ))}
                  </div>
                </>
              )}
              {!!sys.shadows.length && (
                <>
                  <h3 className="sub-title">
                    Shadows <span className="n">{sys.shadows.length}</span>
                  </h3>
                  <div className="shadow-stage" style={{ background: themeColors.page }}>
                    <div className="shadow-grid">
                      {sys.shadows.map((x) => (
                        <figure className="shadow-card" key={x.token}>
                          <div
                            className="shadow-sample"
                            style={{ background: themeColors.surface, boxShadow: x.css }}
                          />
                          <figcaption>
                            <b style={{ color: themeColors.text }}>{x.token}</b>
                            <code style={{ color: themeColors.muted }} title={x.css}>
                              {x.css}
                            </code>
                          </figcaption>
                        </figure>
                      ))}
                    </div>
                  </div>
                </>
              )}
            </section>
          )}

          {!!sys.components.length && (
            <section id="components" className="pd-sec">
              <header className="sec-head">
                <h2>Components</h2>
                <p>Element crops cut from the captures.</p>
              </header>
              {cropGroups.map(([g, items]) => (
                <div key={g}>
                  {cropGroups.length > 1 && <div className="group-title">{g}/</div>}
                  <div className="shots">{items.map((i) => shotTile(i, true, openCrops))}</div>
                </div>
              ))}
            </section>
          )}

          {sys.icons.total > 0 && (
            <section id="icons" className="pd-sec">
              <header className="sec-head">
                <h2>Icons</h2>
                <p>Icon SVGs kept in the package.</p>
              </header>
              <div className="icon-grid" style={{ "--icon-bg": themeColors.page } as React.CSSProperties}>
                {sys.icons.items.slice(0, ICONS_SHOWN).map((p, i) => (
                  <figure
                    className="icon-tile"
                    key={p}
                    role="button"
                    tabIndex={0}
                    title={p.replace(`${sys.dir}/`, "")}
                    onClick={() => openIcons(i)}
                    onKeyDown={(e) => {
                      if (e.key === "Enter" || e.key === " ") {
                        e.preventDefault();
                        openIcons(i);
                      }
                    }}
                  >
                    <div className="icon-face">
                      {/* eslint-disable-next-line @next/next/no-img-element */}
                      <img loading="lazy" src={mediaUrl(p)} alt="" />
                    </div>
                    <figcaption>{fileName(p).replace(/\.[^.]+$/, "")}</figcaption>
                  </figure>
                ))}
              </div>
              {sys.icons.total > Math.min(sys.icons.items.length, ICONS_SHOWN) && (
                <p className="faint">
                  Showing the first {Math.min(sys.icons.items.length, ICONS_SHOWN)} of {sys.icons.total}. The rest are
                  in <code>{sys.dir}/icons/</code>.
                </p>
              )}
            </section>
          )}

          {(sys.score || report || healthHtml || !!gaps.length) && (
            <section id="health" className="pd-sec">
              <header className="sec-head">
                <h2>Health</h2>
                <p>
                  Grades from the newest scorecard audit
                  {report ? ` — ranked ${report.rank} of ${report.total} on ${report.platform}` : ""}.
                </p>
              </header>
              {sys.score && (
                <div className="sc-cards">
                  {GRADE_ORDER.map((g) => (
                    <div className="sc-card" key={g}>
                      <b>
                        <span className={`sc-badge g-${g}`}>{GRADE_UI[g].glyph}</span> {sys.score?.[g] ?? 0}
                      </b>
                      <p>{GRADE_UI[g].word}</p>
                    </div>
                  ))}
                </div>
              )}
              {sys.score && (
                <p className="faint">
                  {sys.score.meets} of {sys.score.applicable} applicable criteria met · audited {sys.score.date}
                  {sys.score.contrast ? ` · Contrast: ${sys.score.contrast}` : ""}
                </p>
              )}
              {report &&
                report.layers.map((layer) => (
                  <div key={layer.name}>
                    <h3 className="sub-title">
                      {layer.name} <span className="n">{layer.rows.length}</span>
                    </h3>
                    <div className="pd-sc-rows">
                      {layer.rows.map((r) => (
                        <div className="pd-sc-row" key={r.id} title={r.doneWhen}>
                          <span className={`sc-badge g-${r.grade}`}>{GRADE_UI[r.grade].glyph}</span>
                          <div>
                            <b>
                              <span className="id">{r.id}</span>
                              {r.title}
                            </b>
                            {!!r.evidence && <p>{r.evidence}</p>}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              {healthHtml && (
                <>
                  <h3 className="sub-title">README notes</h3>
                  <article className="md" dangerouslySetInnerHTML={{ __html: healthHtml }} />
                </>
              )}
              {!!gaps.length && (
                <>
                  <h3 className="sub-title">Known gaps</h3>
                  {gaps.map(([part, why]) => (
                    <div className="nc" role="note" key={part}>
                      <span className="nc-tag">Gap</span>
                      <p>
                        <code>{part}</code> {sentence(why)}.
                      </p>
                    </div>
                  ))}
                </>
              )}
              <div className="actions">
                <Link className="btn" href={`/scorecard/${sys.slug}`}>
                  Full scorecard
                </Link>
              </div>
            </section>
          )}

          {(fileCount > 0 || !!sys.docs.length) && (
            <section id="files" className="pd-sec">
              <header className="sec-head">
                <h2>Files</h2>
                <p>Every readable file in the package, grouped by directory.</p>
              </header>
              {!!sys.docs.length && (
                <div className="doc-pick">
                  {sys.docs.map((d) => (
                    <Link key={d} className="chip" href={`/gallery/${sys.slug}/files/${d}`}>
                      {fileName(d)}
                    </Link>
                  ))}
                </div>
              )}
              {fileGroups.map(([g, list]) => (
                <details className="pd-files" key={g || "root"} open={!g || fileGroups.length <= 3}>
                  <summary>
                    {g ? `${g}/` : "Package root"}
                    <span className="n">{list.length}</span>
                  </summary>
                  <ul>
                    {list.map((f) => (
                      <li key={f.rel}>
                        <Link href={`/gallery/${sys.slug}/files/${f.rel}`}>{f.name}</Link>
                        <span className="pd-size">{humanSize(f.size)}</span>
                      </li>
                    ))}
                  </ul>
                </details>
              ))}
            </section>
          )}
        </div>
      </div>
    </div>
  );
}
