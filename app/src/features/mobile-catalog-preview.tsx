"use client";
import { useEffect, useRef, useState, type CSSProperties } from "react";

interface Crop {
  x: number;
  y: number;
  width: number;
  height: number;
}
interface CaptureCrop {
  bounds: Crop;
  width: number;
  height: number;
  source: string;
}

/** Keep back-and-forth scrubbing off the pixel-scan path with a bounded cache. */
export function readCachedCrop(
  cache: Map<string, CaptureCrop>,
  source: string,
  read: () => CaptureCrop,
): CaptureCrop {
  const cached = cache.get(source);
  if (cached) return cached;
  const measured = read();
  if (cache.size >= 16) cache.delete(cache.keys().next().value!);
  cache.set(source, measured);
  return measured;
}

/** JPEG catalog thumbnails flatten transparent capture margins onto white. */
export function originalMobilePreview(thumbnail: string): string {
  return thumbnail.startsWith("/media/data/thumbs/systems__") &&
    thumbnail.endsWith(".jpg")
    ? `/media/${thumbnail
        .slice("/media/data/thumbs/".length)
        .replaceAll("__", "/")
        .replace(/\.jpg$/, ".png")}`
    : thumbnail;
}

/** Crop transparency only. White app content is part of the real screenshot. */
export function alphaCropBounds(
  pixels: Uint8ClampedArray,
  width: number,
  height: number,
): Crop {
  let left = width,
    top = height,
    right = -1,
    bottom = -1;
  for (let y = 0; y < height; y++)
    for (let x = 0; x < width; x++) {
      if (pixels[(y * width + x) * 4 + 3] < 8) continue;
      left = Math.min(left, x);
      top = Math.min(top, y);
      right = Math.max(right, x);
      bottom = Math.max(bottom, y);
    }
  return right < left
    ? { x: 0, y: 0, width, height }
    : { x: left, y: top, width: right - left + 1, height: bottom - top + 1 };
}

export function coverCrop(
  crop: Crop,
  width: number,
  height: number,
  targetWidth: number,
  targetHeight: number,
) {
  const scale = Math.max(targetWidth / crop.width, targetHeight / crop.height);
  return {
    width: width * scale,
    height: height * scale,
    left: (targetWidth - crop.width * scale) / 2 - crop.x * scale,
    top: (targetHeight - crop.height * scale) / 2 - crop.y * scale,
  };
}

export function MobileCatalogPreview({
  image,
  fallback,
  name,
}: {
  image: string;
  fallback: string;
  name: string;
}) {
  const container = useRef<HTMLDivElement>(null);
  const cropCache = useRef(new Map<string, CaptureCrop>());
  const [failed, setFailed] = useState("");
  const source = failed === image ? fallback : image;
  const [crop, setCrop] = useState<CaptureCrop | null>(null);
  const [size, setSize] = useState({ width: 0, height: 0 });
  useEffect(() => {
    const node = container.current;
    if (!node) return;
    const observer = new ResizeObserver(([entry]) =>
      setSize({
        width: entry.contentRect.width,
        height: entry.contentRect.height,
      }),
    );
    observer.observe(node);
    return () => observer.disconnect();
  }, []);
  const ready = crop?.source === source;
  const style: CSSProperties = {
    position: "absolute",
    maxWidth: "none",
    objectFit: "cover",
    ...(ready && size.width && size.height
      ? {
          ...coverCrop(
            crop.bounds,
            crop.width,
            crop.height,
            size.width,
            size.height,
          ),
          opacity: 1,
        }
      : { opacity: 0 }),
  };
  return (
    <div ref={container} className="media-preview">
      <img
        src={source}
        alt={`${name} design preview`}
        loading="lazy"
        style={style}
        onError={() => setFailed(image)}
        onLoad={(event) => {
          const image = event.currentTarget;
          const key = `${source}:${image.naturalWidth}x${image.naturalHeight}`;
          setCrop(
            readCachedCrop(cropCache.current, key, () => {
              const ratio = Math.min(
                1,
                2048 / Math.max(image.naturalWidth, image.naturalHeight),
              );
              const canvas = document.createElement("canvas");
              canvas.width = Math.max(
                1,
                Math.round(image.naturalWidth * ratio),
              );
              canvas.height = Math.max(
                1,
                Math.round(image.naturalHeight * ratio),
              );
              const context = canvas.getContext("2d");
              let bounds: Crop = {
                x: 0,
                y: 0,
                width: canvas.width,
                height: canvas.height,
              };
              if (context)
                try {
                  context.drawImage(image, 0, 0, canvas.width, canvas.height);
                  bounds = alphaCropBounds(
                    context.getImageData(0, 0, canvas.width, canvas.height)
                      .data,
                    canvas.width,
                    canvas.height,
                  );
                } catch {
                  /* An opaque or unavailable canvas still uses edge-to-edge cover. */
                }
              return {
                bounds,
                width: canvas.width,
                height: canvas.height,
                source,
              };
            }),
          );
        }}
      />
    </div>
  );
}
