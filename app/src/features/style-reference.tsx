"use client";
import Link from "next/link";
import {
  useEffect,
  useRef,
  useState,
  type KeyboardEvent as ReactKeyboardEvent,
  type ReactNode,
  type CSSProperties,
} from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { ArrowLeft, ArrowRight, ExternalLink, Maximize2 } from "lucide-react";
import type { LibraryDetail, ReferenceMedia } from "@/contracts/library";
import {
  CopyButton,
  DownloadButton,
  ErrorState,
  Modal,
  Spinner,
} from "@/components/shared";
import { SaveReference } from "@/components/reference";
import { MediaBookmarkButton } from "@/components/media-bookmark";
import {
  hasComponentMarkup,
  isUnresolvedCapture,
  styleHost,
} from "./styles-data";
import { StyleCard } from "./styles-index";
import styles from "./style-reference.module.css";

type Data = Record<string, any>;
const list = (value: unknown): Data[] =>
  Array.isArray(value)
    ? value.filter((entry) => entry && typeof entry === "object")
    : [];
const textList = (value: unknown): string[] =>
  Array.isArray(value)
    ? value
        .map((entry) =>
          typeof entry === "string" ? entry : String(entry?.text || ""),
        )
        .filter(Boolean)
    : [];
const label = (value: string) =>
  value
    .replace(/([a-z])([A-Z])/g, "$1 $2")
    .replace(/[-_]/g, " ")
    .replace(/^./, (char) => char.toUpperCase());
const length = (value: unknown, fallback = "14px") =>
  typeof value === "number"
    ? `${value}px`
    : typeof value === "string" && value
      ? /^\d+(\.\d+)?$/.test(value)
        ? `${value}px`
        : value
      : fallback;
const description = (value: unknown): string =>
  typeof value === "string" ? value : "";
function moveTab(
  event: ReactKeyboardEvent<HTMLDivElement>,
  keys: string[],
  current: string,
  select: (key: string) => void,
) {
  const index = keys.indexOf(current);
  const next =
    event.key === "ArrowRight"
      ? (index + 1) % keys.length
      : event.key === "ArrowLeft"
        ? (index - 1 + keys.length) % keys.length
        : event.key === "Home"
          ? 0
          : event.key === "End"
            ? keys.length - 1
            : -1;
  if (next < 0 || !keys.length) return;
  event.preventDefault();
  select(keys[next]);
  event.currentTarget
    .querySelectorAll<HTMLButtonElement>('[role="tab"]')
    [next]?.focus();
}

export function StyleImage({
  media,
  alt,
  className,
}: {
  media: ReferenceMedia;
  alt: string;
  className?: string;
}) {
  const [url, setUrl] = useState(media.url),
    [failed, setFailed] = useState(false);
  useEffect(() => {
    setUrl(media.url);
    setFailed(false);
  }, [media.url]);
  return failed ? (
    <p className={styles.unavailable}>
      This image is unavailable from the mirror and original source.
    </p>
  ) : (
    <img
      src={url}
      alt={alt}
      className={className}
      loading="lazy"
      decoding="async"
      onError={() => {
        if (media.fallback && url !== media.fallback) setUrl(media.fallback);
        else setFailed(true);
      }}
    />
  );
}
function StyleVideo({
  media,
  poster,
}: {
  media: ReferenceMedia;
  poster?: ReferenceMedia;
}) {
  const [url, setUrl] = useState(media.url),
    [failed, setFailed] = useState(false),
    [posterUrl, setPosterUrl] = useState(
      poster?.url || media.poster || undefined,
    );
  useEffect(() => {
    setUrl(media.url);
    setFailed(false);
  }, [media.url]);
  useEffect(() => {
    const initial = poster?.url || media.poster || undefined;
    setPosterUrl(initial);
    if (!initial || !poster?.fallback) return;
    const image = new Image();
    image.onerror = () => setPosterUrl(poster.fallback || undefined);
    image.src = initial;
    return () => {
      image.onerror = null;
    };
  }, [poster?.url, poster?.fallback, media.poster]);
  return failed ? (
    <p className={styles.unavailable}>
      This recording is unavailable from the mirror and original source.
    </p>
  ) : (
    <video
      key={media.id}
      src={url}
      poster={posterUrl}
      controls
      playsInline
      preload="metadata"
      onError={() => {
        if (media.fallback && url !== media.fallback) setUrl(media.fallback);
        else setFailed(true);
      }}
    />
  );
}
const MEDIA_LABELS: Record<string, string> = {
  shot: "Screenshot",
  video: "Scrolling video",
  detail: "Detail clip",
  poster: "Poster",
  detail_poster: "Detail still",
};
export function StyleMedia({ detail }: { detail: LibraryDetail }) {
  const opener = useRef<HTMLButtonElement | null>(null);
  const media = detail.media.filter((item) => item.kind !== "favicon");
  const ordered = Object.keys(MEDIA_LABELS).flatMap((kind) =>
    media.filter((item) => (item.kind || item.id) === kind),
  );
  const [selected, setSelected] = useState(ordered[0]?.id || ""),
    [lightbox, setLightbox] = useState<string | null>(null);
  const current = ordered.find((item) => item.id === selected) || ordered[0];
  const images = ordered.filter((item) => item.type === "image");
  const lightboxIndex = images.findIndex((item) => item.id === lightbox);
  const lightboxMedia = images[lightboxIndex];
  useEffect(() => {
    if (!lightbox || images.length < 2) return;
    const keydown = (event: KeyboardEvent) => {
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key))
        return;
      event.preventDefault();
      const next =
        event.key === "Home"
          ? 0
          : event.key === "End"
            ? images.length - 1
            : (lightboxIndex +
                (event.key === "ArrowLeft" ? -1 : 1) +
                images.length) %
              images.length;
      setLightbox(images[next].id);
    };
    document.addEventListener("keydown", keydown);
    return () => document.removeEventListener("keydown", keydown);
  }, [lightbox, detail.media]);
  if (!current)
    return (
      <p className={styles.unavailable}>
        No preview was captured for this style.
      </p>
    );
  const posterKind =
    (current.kind || current.id) === "detail" ? "detail_poster" : "poster";
  return (
    <section className={styles.mediaSection} aria-label="Style media">
      <div
        className={styles.mediaTabs}
        role="tablist"
        aria-label="Preview type"
        onKeyDown={(event) =>
          moveTab(
            event,
            ordered.map((item) => item.id),
            current.id,
            setSelected,
          )
        }
      >
        {ordered.map((item) => (
          <button
            key={item.id}
            id={`media-tab-${item.id}`}
            role="tab"
            aria-selected={current.id === item.id}
            tabIndex={current.id === item.id ? 0 : -1}
            aria-controls="style-media-panel"
            onClick={() => setSelected(item.id)}
          >
            {MEDIA_LABELS[item.kind || item.id] || item.name}
          </button>
        ))}
      </div>
      <div
        className={styles.mediaViewer}
        id="style-media-panel"
        role="tabpanel"
        aria-labelledby={`media-tab-${current.id}`}
      >
        {current.type === "video" ? (
          <StyleVideo
            media={current}
            poster={media.find((item) => (item.kind || item.id) === posterKind)}
          />
        ) : (
          <button
            className={styles.openImage}
            onClick={(event) => {
              opener.current = event.currentTarget;
              setLightbox(current.id);
            }}
            aria-label={`Open ${MEDIA_LABELS[current.kind || current.id] || current.name} in lightbox`}
          >
            <StyleImage
              media={current}
              alt={`${detail.name}: ${current.name}`}
            />
            <span>
              <Maximize2 size={14} />
              Enlarge
            </span>
          </button>
        )}
      </div>
      {lightboxMedia && (
        <Modal
          open
          onOpenChange={(open) => {
            if (!open) {
              setLightbox(null);
              requestAnimationFrame(() => opener.current?.focus());
            }
          }}
          title={`${detail.name}: ${MEDIA_LABELS[lightboxMedia.kind || lightboxMedia.id] || lightboxMedia.name}`}
          className={styles.lightbox}
        >
          <div className={styles.lightboxContent}>
            <div className={styles.lightboxControls}>
              <button
                className="pill small"
                disabled={images.length < 2}
                onClick={() =>
                  setLightbox(
                    images[(lightboxIndex - 1 + images.length) % images.length]
                      .id,
                  )
                }
              >
                <ArrowLeft size={14} />
                Previous
              </button>
              <span>
                {lightboxIndex + 1} of {images.length}
              </span>
              <MediaBookmarkButton
                referenceId={detail.id}
                mediaId={lightboxMedia.id}
                compact
              />
              <button
                className="pill small"
                disabled={images.length < 2}
                onClick={() =>
                  setLightbox(images[(lightboxIndex + 1) % images.length].id)
                }
              >
                Next
                <ArrowRight size={14} />
              </button>
            </div>
            <StyleImage
              media={lightboxMedia}
              alt={`${detail.name}: ${lightboxMedia.name}`}
            />
          </div>
        </Modal>
      )}
    </section>
  );
}

function Section({ title, children }: { title: string; children: ReactNode }) {
  return (
    <section className={styles.section}>
      <h2>{title}</h2>
      {children}
    </section>
  );
}
function CopyValue({
  value,
  children,
  className,
  style,
}: {
  value: string;
  children?: ReactNode;
  className?: string;
  style?: CSSProperties;
}) {
  const [copied, setCopied] = useState(false),
    [error, setError] = useState("");
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const request = useRef(0);
  useEffect(() => {
    setCopied(false);
    setError("");
    request.current += 1;
    if (timer.current) clearTimeout(timer.current);
    return () => {
      request.current += 1;
      if (timer.current) clearTimeout(timer.current);
    };
  }, [value]);
  return (
    <>
      <button
        type="button"
        className={`${styles.copyValue} ${className || ""}`}
        style={style}
        title={`Click to copy "${value}"`}
        aria-label={`Copy ${value}`}
        onClick={async () => {
          const attempt = ++request.current;
          if (timer.current) clearTimeout(timer.current);
          setCopied(false);
          setError("");
          try {
            await navigator.clipboard.writeText(value);
            if (attempt !== request.current) return;
            setCopied(true);
            timer.current = setTimeout(() => setCopied(false), 1800);
          } catch {
            if (attempt !== request.current) return;
            setError("Clipboard unavailable. Select and copy this value:");
          }
        }}
      >
        {children || value}
        <span className="sr-only" role="status">
          {copied ? `Copied ${value}` : ""}
        </span>
      </button>
      {error && (
        <span className={styles.copyFallback} role="status">
          {error} <code tabIndex={0}>{value}</code>
        </span>
      )}
    </>
  );
}

function CopyColor({ color }: { color: Data }) {
  const value = color.gradient || color.hex || color.value || "";
  const [copied, setCopied] = useState("");
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const request = useRef(0);
  useEffect(() => {
    setCopied("");
    request.current += 1;
    if (timer.current) clearTimeout(timer.current);
    return () => {
      request.current += 1;
      if (timer.current) clearTimeout(timer.current);
    };
  }, [value]);
  return (
    <button
      className={styles.swatch}
      title={`Copy ${value}`}
      onClick={async () => {
        const attempt = ++request.current;
        if (timer.current) clearTimeout(timer.current);
        setCopied("");
        try {
          await navigator.clipboard.writeText(value);
          if (attempt !== request.current) return;
          setCopied("Copied");
          timer.current = setTimeout(() => setCopied(""), 1800);
        } catch {
          if (attempt !== request.current) return;
          setCopied("Clipboard unavailable. Select the value to copy.");
        }
      }}
    >
      <span className={styles.swatchPaint} style={{ background: value }} />
      <strong>{color.name || value}</strong>
      <code>{value}</code>
      {color.role && <p>{color.role}</p>}
      <span className={styles.copyFeedback} role="status">
        {copied}
      </span>
    </button>
  );
}
function StyleColors({ design }: { design: Data }) {
  const colors = list(design.colors);
  const priority = ["brand", "accent", "neutral", "neutrals"];
  const groups = [
    ...new Set(colors.map((color) => color.group || "Palette")),
  ].sort((a, b) => {
    const rank = (value: string) => {
      const i = priority.indexOf(value.toLowerCase());
      return i < 0 ? priority.length : i;
    };
    return rank(a) - rank(b);
  });
  return colors.length ? (
    <Section title="Color palette">
      {groups.map((group) => (
        <div key={group}>
          <h3 className={styles.subheading}>{label(group)}</h3>
          <div className={styles.swatches}>
            {colors
              .filter((color) => (color.group || "Palette") === group)
              .map((color, i) => (
                <CopyColor color={color} key={i} />
              ))}
          </div>
        </div>
      ))}
    </Section>
  ) : null;
}
function StyleTypography({ design }: { design: Data }) {
  const fonts = list(design.typography),
    scale = list(design.typeScale).sort(
      (a, b) =>
        parseFloat(String(b.size || 0)) - parseFloat(String(a.size || 0)),
    );
  const [all, setAll] = useState(false),
    [allFonts, setAllFonts] = useState(false);
  return fonts.length || scale.length ? (
    <Section title="Typography">
      <p className={styles.note}>
        Samples use fonts installed on this device, with system fallbacks.
        Original font files are not bundled.
      </p>
      {!!scale.length && (
        <div className={styles.scale}>
          {(all ? scale : scale.slice(0, 8)).map((step, i) => (
            <div className={styles.scaleRow} key={i}>
              <div>
                <strong>{step.role || `Step ${i + 1}`}</strong>
                <code>
                  {[
                    step.size != null ? length(step.size) : null,
                    step.family,
                    step.weight != null ? `weight ${step.weight}` : null,
                    step.lineHeight != null
                      ? `line height ${step.lineHeight}`
                      : null,
                    step.letterSpacing != null
                      ? `tracking ${length(step.letterSpacing)}`
                      : null,
                  ]
                    .filter(Boolean)
                    .join(" · ")}
                </code>
              </div>
              <CopyValue
                value={String(step.family || fonts[0]?.family || "sans-serif")}
                className={styles.scaleSample}
                style={{
                  fontFamily: `"${String(step.family || fonts[0]?.family || "").replace(/"/g, "")}", var(--sans)`,
                  fontSize: length(step.size),
                  fontWeight: step.weight || 400,
                  lineHeight: step.lineHeight || 1.4,
                  letterSpacing:
                    step.letterSpacing != null
                      ? length(step.letterSpacing)
                      : undefined,
                }}
              >
                The quick brown fox jumps
              </CopyValue>
            </div>
          ))}
        </div>
      )}
      {scale.length > 8 && (
        <button
          className="pill small"
          aria-expanded={all}
          onClick={() => setAll(!all)}
        >
          {all ? "Show fewer steps" : `Show all ${scale.length} steps`}
        </button>
      )}
      <div className={styles.fonts}>
        {(allFonts ? fonts : fonts.slice(0, 3)).map((font, i) => (
          <div className={styles.font} key={i}>
            <h3
              style={{
                fontFamily: `"${String(font.family || "").replace(/"/g, "")}", var(--sans)`,
              }}
            >
              <CopyValue value={String(font.family || "Typeface")} />
            </h3>
            <dl>
              {[
                ["Weight", font.weight],
                ["Sizes", font.sizes],
                ["Line height", font.lineHeight],
                ["Tracking", font.letterSpacing],
                ["OpenType features", font.fontFeatureSettings],
                ["Substitute", font.substitute],
                ["Source", font.source],
              ]
                .filter(([, value]) => value)
                .map(([key, value]) => (
                  <div key={key}>
                    <dt>{key}</dt>
                    <dd>{value}</dd>
                  </div>
                ))}
            </dl>
            {font.role && <p className={styles.note}>{font.role}</p>}
          </div>
        ))}
      </div>
      {fonts.length > 3 && (
        <button
          className="pill small"
          aria-expanded={allFonts}
          onClick={() => setAllFonts(!allFonts)}
        >
          {allFonts ? "Show fewer fonts" : `Show all ${fonts.length} fonts`}
        </button>
      )}
    </Section>
  ) : null;
}
function StyleSpacing({ design }: { design: Data }) {
  const spacing = design.spacing || {},
    radii = Object.entries(spacing.radius || {}),
    elevation = list(design.elevation);
  const rows = Object.entries(spacing).filter(
    ([key, value]) =>
      key !== "radius" && ["string", "number"].includes(typeof value),
  );
  return rows.length ||
    radii.length ||
    elevation.length ||
    design.elevationPhilosophy ? (
    <Section title="Spacing & shape">
      {!!rows.length && (
        <dl className={styles.definition}>
          {rows.map(([key, value]) => (
            <div key={key}>
              <dt>{label(key)}</dt>
              <dd>
                <CopyValue
                  value={key === "baseUnit" ? length(value) : String(value)}
                >
                  <code>
                    {key === "baseUnit" ? length(value) : String(value)}
                  </code>
                </CopyValue>
              </dd>
            </div>
          ))}
        </dl>
      )}
      {!!radii.length && (
        <>
          <h3 className={styles.subheading}>Corner radius</h3>
          <div className={styles.radii}>
            {radii.map(([key, value]) => (
              <div key={key}>
                <i style={{ borderRadius: length(value, "0px") }} />
                <span>
                  {label(key)}
                  <CopyValue value={String(value)}>
                    <code>{String(value)}</code>
                  </CopyValue>
                </span>
              </div>
            ))}
          </div>
        </>
      )}
      {!!elevation.length && (
        <>
          <h3 className={styles.subheading}>Elevation</h3>
          <div className={styles.elevation}>
            {elevation.map((entry, i) => (
              <div key={i}>
                <i style={{ boxShadow: entry.style || entry.shadow }} />
                <div>
                  <strong>{entry.element || entry.name || "Elevation"}</strong>
                  <code>{entry.style || entry.shadow}</code>
                </div>
              </div>
            ))}
          </div>
        </>
      )}
      {design.elevationPhilosophy && (
        <p className={styles.note}>{design.elevationPhilosophy}</p>
      )}
    </Section>
  ) : null;
}
function ComponentPreview({
  component,
  slug,
  index,
}: {
  component: Data;
  slug: string;
  index: number;
}) {
  const html = typeof component.html === "string" ? component.html : "";
  const available = hasComponentMarkup(html);
  const [source, setSource] = useState(false);
  const srcDoc = `<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; img-src data: https:; font-src data: https:; base-uri 'none'; form-action 'none'"><style>body{margin:0;padding:24px;font:14px system-ui,sans-serif;color:#171717;background:#fff}*{box-sizing:border-box}img{max-width:100%}</style></head><body>${html}</body></html>`;
  return (
    <div className={styles.component}>
      <h3>{component.name || `Component ${index + 1}`}</h3>
      {component.role && (
        <p className={styles.componentRole}>{component.role}</p>
      )}
      {component.description && (
        <p className={styles.note}>{component.description}</p>
      )}
      {available ? (
        <>
          <div className={styles.componentTools}>
            <button
              className="pill small"
              aria-pressed={source}
              onClick={() => setSource(!source)}
            >
              {source ? "Show preview" : "HTML source"}
            </button>
            <CopyButton value={html} label="Copy HTML" />
            <DownloadButton
              value={html}
              name={`${slug}-component-${index + 1}.html`}
              label="Download HTML"
            />
          </div>
          <p className={styles.note}>
            Reconstructed HTML from Refero. The sandbox disables scripts and
            forms; appearance may differ from the product.
          </p>
          {source ? (
            <pre className={styles.componentSource}>
              <code>{html}</code>
            </pre>
          ) : (
            <iframe
              title={`${component.name || "Component"} reconstructed preview`}
              sandbox=""
              srcDoc={srcDoc}
              loading="lazy"
              className={styles.componentFrame}
            />
          )}
        </>
      ) : html ? (
        <p className={styles.note}>
          HTML preview unavailable: the captured source contains an unresolved
          upstream reference.
        </p>
      ) : null}
    </div>
  );
}
function StyleComponents({ design, slug }: { design: Data; slug: string }) {
  const components = list(design.components),
    [all, setAll] = useState(false);
  return components.length ? (
    <Section title="Components">
      <p className={styles.note}>
        Third-party descriptions and reconstructions. Available HTML previews
        are shown with their source.
      </p>
      {(all ? components : components.slice(0, 4)).map((component, i) => (
        <ComponentPreview key={i} component={component} slug={slug} index={i} />
      ))}
      {components.length > 4 && (
        <button
          className="pill small"
          aria-expanded={all}
          onClick={() => setAll(!all)}
        >
          {all
            ? "Show fewer components"
            : `Show all ${components.length} components`}
        </button>
      )}
    </Section>
  ) : null;
}
export function StyleOverview({ detail }: { detail: LibraryDetail }) {
  const interpretation = detail.interpreted;
  const design = (interpretation?.designSystem || {}) as Data;
  const tags = [
    ["theme", interpretation?.theme || detail.themes[0]],
    ["type", interpretation?.productType || detail.productType],
    ["style", interpretation?.designStyle || detail.designStyle],
    ["industry", interpretation?.industry || detail.industry],
  ].filter(([, value]) => value);
  const dos = textList(design.dos),
    donts = textList(design.donts);
  const similar = interpretation?.similar || [];
  const favicon = detail.media.find((item) => item.kind === "favicon");
  return (
    <article className={styles.overview}>
      <StyleMedia detail={detail} />
      <div className={styles.title}>
        <h1>{detail.name}</h1>
        {favicon ? (
          <StyleImage media={favicon} alt="" />
        ) : detail.icon ? (
          <img src={detail.icon} alt="" />
        ) : null}
      </div>
      {detail.description && (
        <p className={styles.tagline}>{detail.description}</p>
      )}
      <p className={styles.description}>{detail.descriptionLong}</p>
      <div className={styles.facets}>
        {tags.map(([key, value]) => (
          <Link key={key} href={`/styles?${key}=${encodeURIComponent(value!)}`}>
            {value}
          </Link>
        ))}
        {detail.tags.map((tag) => (
          <Link
            key={`tag-${tag}`}
            href={`/styles?tag=${encodeURIComponent(tag)}`}
          >
            {tag}
          </Link>
        ))}
      </div>
      <div className={styles.actions}>
        <SaveReference item={detail} />
        {detail.sourceUrl && (
          <a
            className="pill small"
            href={detail.sourceUrl}
            target="_blank"
            rel="noreferrer"
          >
            {styleHost(detail.sourceUrl)}
            <ExternalLink size={13} />
          </a>
        )}
        {interpretation?.pageUrl && (
          <a
            className="pill small"
            href={interpretation.pageUrl}
            target="_blank"
            rel="noreferrer"
          >
            Open on Refero
            <ExternalLink size={13} />
          </a>
        )}
      </div>
      <div className={styles.evidence}>
        <strong>Third-party interpretation</strong>
        <p>
          Refero interprets product styles and reconstructs components. Prefer
          measured package values when available.
          {detail.captured ? ` Extracted ${detail.captured.slice(0, 10)}.` : ""}
        </p>
      </div>
      {design.northStar && (
        <Section title="Design direction">
          <p className={styles.note}>{description(design.northStar)}</p>
        </Section>
      )}
      <StyleColors design={design} />
      <StyleTypography design={design} />
      <StyleSpacing design={design} />
      {!!(dos.length || donts.length) && (
        <Section title="Guidelines">
          <div className={styles.guidelines}>
            {dos.length > 0 && (
              <div>
                <h3>Do</h3>
                <ul>
                  {dos.map((note, i) => (
                    <li key={i}>{note}</li>
                  ))}
                </ul>
              </div>
            )}
            {donts.length > 0 && (
              <div>
                <h3>Don’t</h3>
                <ul>
                  {donts.map((note, i) => (
                    <li key={i}>{note}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </Section>
      )}
      <StyleComponents design={design} slug={detail.slug} />
      {design.surfaces && list(design.surfaces).length > 0 && (
        <Section title="Surfaces">
          <div className={styles.swatches}>
            {list(design.surfaces).map((surface, i) => (
              <CopyColor
                key={i}
                color={{ ...surface, role: surface.purpose }}
              />
            ))}
          </div>
        </Section>
      )}
      {[
        ["Imagery", design.imagery],
        ["Layout", design.layout],
      ]
        .filter(([, value]) => typeof value === "string" && value)
        .map(([title, value]) => (
          <Section title={title} key={title}>
            <p className={styles.note}>{value}</p>
          </Section>
        ))}
      {list(design.customSections).map((section, i) => (
        <Section title={section.title || `Design note ${i + 1}`} key={i}>
          {isUnresolvedCapture(section.content) ? (
            <p className={styles.note}>
              This design note is unavailable: the captured source contains an
              unresolved upstream reference.
            </p>
          ) : (
            <div className={styles.markdown}>
              <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {description(section.content)}
              </ReactMarkdown>
            </div>
          )}
        </Section>
      ))}
      {!!similar.length && (
        <Section title="Similar styles">
          <div className={styles.similar}>
            {similar.map((item, i) => (
              <div key={`${item.slug}-${i}`}>
                {item.slug ? (
                  <Link href={`/styles/refero/${item.slug}`}>
                    <strong>{item.name || item.slug}</strong>
                    <ArrowRight size={14} />
                  </Link>
                ) : (
                  <strong>
                    {item.name || "Similar brand"}
                    <small>Not in this collection</small>
                  </strong>
                )}
                {item.why && <p className={styles.note}>{item.why}</p>}
              </div>
            ))}
          </div>
        </Section>
      )}
      {!!detail.related.length && (
        <Section title="More to explore">
          <div className={styles.related}>
            {detail.related.slice(0, 6).map((item) => (
              <StyleCard key={item.id} item={item} />
            ))}
          </div>
        </Section>
      )}
    </article>
  );
}

function Code({ value, format }: { value: string; format: string }) {
  const pattern =
    /(\/\*[\s\S]*?\*\/|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|--[\w-]+|@[\w-]+|\b(?:true|false|null|\d+(?:\.\d+)?)\b)/g;
  return (
    <code>
      {format.endsWith(".md")
        ? value.split(/(^#{1,6} .+$|^> .+$|`[^`\n]+`)/gm).map((part, i) => (
            <span
              key={i}
              className={
                part.startsWith("#")
                  ? styles.codeProperty
                  : part.startsWith(">")
                    ? styles.codeString
                    : part.startsWith("`")
                      ? styles.codeNumber
                      : undefined
              }
            >
              {part}
            </span>
          ))
        : value.split(pattern).map((part, i) => (
            <span
              key={i}
              className={
                i % 2
                  ? part.startsWith("/*")
                    ? styles.codeComment
                    : part.startsWith("--") || part.startsWith("@")
                      ? styles.codeProperty
                      : part.startsWith('"') || part.startsWith("'")
                        ? styles.codeString
                        : styles.codeNumber
                  : undefined
              }
            >
              {part}
            </span>
          ))}
    </code>
  );
}
export function StyleDocuments({ detail }: { detail: LibraryDetail }) {
  const formatOrder = [
    "DESIGN.md",
    "theme.css",
    "variables.css",
    "tokens.json",
  ];
  const keys = Object.keys(detail.exports).sort((a, b) => {
      const rank = (key: string) => {
        const i = formatOrder.indexOf(key);
        return i < 0 ? formatOrder.length : i;
      };
      return rank(a) - rank(b);
    }),
    [tab, setTab] = useState(
      keys.includes("DESIGN.md") ? "DESIGN.md" : keys[0] || "DESIGN.md",
    ),
    [variant, setVariant] = useState<"compact" | "extended">("extended"),
    [loadedUrl, setLoadedUrl] = useState<string | null>(null),
    [rendered, setRendered] = useState(false),
    [wrap, setWrap] = useState(true),
    [value, setValue] = useState(""),
    [loading, setLoading] = useState(true),
    [error, setError] = useState("");
  const exportUrl = detail.exports[tab];
  const url = exportUrl
    ? `${exportUrl}${exportUrl.includes("?") ? "&" : "?"}variant=${variant}`
    : undefined;
  const ready = !!url && loadedUrl === url && !loading && !error;
  useEffect(() => {
    setTab(
      Object.keys(detail.exports).includes("DESIGN.md")
        ? "DESIGN.md"
        : Object.keys(detail.exports)[0] || "DESIGN.md",
    );
  }, [detail.id]);
  useEffect(() => {
    const request = new AbortController();
    setLoading(true);
    setError("");
    setValue("");
    setLoadedUrl(null);
    if (!url) {
      setLoading(false);
      setError("No document is available in this format.");
      return;
    }
    fetch(url, { signal: request.signal })
      .then(async (response) => {
        if (!response.ok) {
          const body = await response.json().catch(() => null);
          throw new Error(body?.error || "This document could not be loaded.");
        }
        return response.text();
      })
      .then((text) => {
        if (!request.signal.aborted) {
          setValue(text);
          setLoadedUrl(url);
        }
      })
      .catch((error) => {
        if (!request.signal.aborted) setError(error.message);
      })
      .finally(() => {
        if (!request.signal.aborted) setLoading(false);
      });
    return () => request.abort();
  }, [url, detail.id]);
  const markdown = tab.toLowerCase().endsWith(".md");
  const labels: Record<string, string> = {
    "DESIGN.md": "DESIGN.md",
    "theme.css": "Tailwind v4",
    "variables.css": "CSS Variables",
    "tokens.json": "Design Tokens",
  };
  return (
    <section className={styles.documents} aria-label="Style documents">
      <div
        className={styles.documentTabs}
        role="tablist"
        aria-label="Document format"
        onKeyDown={(event) => moveTab(event, keys, tab, setTab)}
      >
        {keys.map((key) => (
          <button
            key={key}
            role="tab"
            aria-selected={tab === key}
            tabIndex={tab === key ? 0 : -1}
            aria-controls="style-document-panel"
            id={`document-tab-${key.replace(/\W/g, "-")}`}
            onClick={() => setTab(key)}
          >
            {labels[key] || key}
          </button>
        ))}
      </div>
      <div className={styles.documentToolbar}>
        <div
          className={styles.documentVariants}
          role="group"
          aria-label="Document detail"
        >
          {(["compact", "extended"] as const).map((mode) => (
            <button
              key={mode}
              type="button"
              aria-pressed={variant === mode}
              onClick={() => setVariant(mode)}
            >
              {mode === "compact" ? "Compact" : "Extended"}
            </button>
          ))}
        </div>
        <span className="sr-only">
          {detail.slug}-{variant}-{tab}
        </span>
        <div className={styles.documentActions}>
          {markdown && (
            <button
              className="pill small"
              aria-pressed={!rendered}
              onClick={() => setRendered(!rendered)}
            >
              {rendered ? "View source" : "Read document"}
            </button>
          )}
          {(!markdown || !rendered) && (
            <button
              className="pill small"
              aria-pressed={wrap}
              onClick={() => setWrap(!wrap)}
            >
              {wrap ? "Wrap on" : "Wrap off"}
            </button>
          )}
          {ready && (
            <>
              <CopyButton value={value} />
              <DownloadButton
                value={value}
                name={`${detail.slug}-${variant}-${tab}`}
              />
            </>
          )}
        </div>
      </div>
      <div
        className={styles.documentBody}
        role="tabpanel"
        id="style-document-panel"
        aria-labelledby={`document-tab-${tab.replace(/\W/g, "-")}`}
        tabIndex={0}
      >
        {loading || (!error && !ready) ? (
          <Spinner label={`Opening ${variant} document…`} />
        ) : error ? (
          <ErrorState message={error} />
        ) : markdown && rendered ? (
          <div className={styles.markdown}>
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                a: ({ href, children }) => (
                  <a href={href} target="_blank" rel="noreferrer">
                    {children}
                  </a>
                ),
                img: ({ alt }) => (
                  <span className={styles.note}>
                    {alt ? `[Image: ${alt}]` : "[Image]"}
                  </span>
                ),
              }}
            >
              {value}
            </ReactMarkdown>
          </div>
        ) : (
          <pre className={wrap ? styles.wrap : ""}>
            <Code value={value} format={tab} />
          </pre>
        )}
      </div>
      <div className={styles.documentFoot}>
        Interpreted by Refero · {variant === "compact" ? "Compact" : "Extended"}{" "}
        export from the captured source
      </div>
    </section>
  );
}
